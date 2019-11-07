from read_from_file_or_net import get_stuff_from_net as get_url
import gettysburg_v2 as gb

# The following are the strings which define the basic HTML document. Later on we will make an HTML 'span' element for
# each word with an appropriate font size set. The resulting collection of 'span's is sandwiched between these two basic
# strings to form the final document.


HTML_START_TEXT = "<!DOCTYPE html>\n" \
                  "<html>\n<head lang=\"en\">\n" \
                  "<meta charset=\"UTF-8\">\n" \
                  "<title>Tag Cloud Generator</title>\n" \
                  "</head>\n" \
                  "<body>\n" \
                  "<div style=\"text-align: center; vertical-align: middle; font-family: arial; color: white; " \
                  "background-color:black; border:1px solid black\">\n"
HTML_END_TEXT = "</div>\n" \
                "</body>\n" \
                "</html>"

# These are the min/max allowable font sizes for the words
MIN_FONT_SIZE = 20
MAX_FONT_SIZE = 200

# IRLs for source data
SPEECH_URL = "http://193.1.33.31:88/pa1/gettysburg.txt"
STOPWORDS_URL = "http://193.1.33.31:88/pa1/stopwords.txt"

def main():
    try:
        # Get speech and stop word files from the net and store in local cache
        speech = get_url(SPEECH_URL).split('\n')
        stopwords = tuple(get_url(STOPWORDS_URL).split(','))

        speech = gb.make_word_list(speech, stopwords)
        counts = gb.count_words(speech)

        span_strings = ""

        for k, v in counts.items():
            # Make an html 'span' element for each word including font size. Size is set as frequency * min size. Max
            # size is the upper limit.
            span_string = "<span style=\"font-size: {}px\"> {} </span>\n"\
                .format(int(min(v * MIN_FONT_SIZE, MAX_FONT_SIZE)), k)
            span_strings += span_string

        # Make final html document and write it to local cache
        html_final = HTML_START_TEXT + span_strings + HTML_END_TEXT

        with open(".cache/tag_cloud.html", "w") as fh:
            fh.write(html_final)


    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()