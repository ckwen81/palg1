"""Sample prograam to illustrate (i) how to read a text file and (ii) how to get stuff from the net.

This program implements two functions:
1. Reads any text file and return s its contents as a single variable. It's then up to you to iterate through the file
and do something with its contents. Note that the file you are reading MUST be a text file.
2. Accepts a URL and attempts to return the resource. If it can't be decoded then we assume that it's not text and throw
an error. If the status code of the response isn't in the 200s (everything OK) or the 300s (OK but redirected) then we
also throw an error.

Mark Foley
October 2019
"""


def read_any_text_file(file_name):
    """
    This function trys to read and text file and return its contents.

    :param file_name: The file to read. If the file isn't in the same directory as this program, you'll need to enter
    the full path, i.e. /home/username/path/to/file or drive_letter:\\full\\path\\to\\file

    :return: File contents, if possible.
    """
    try:
        whole_file = None
        with open(file_name, "r") as fh:
            # for line in fh:
            #     print(line.strip())
            whole_file = fh.read()

        return whole_file
    except Exception as e:
        print(f"Something bad happened when trying to read {file_name}.\nI can't return anything.\n{e}")
        return None


def get_stuff_from_net(url):
    """
    This function accepts a URL as input and attempts to retrieve this resource from the Net.

    :param url: The required resource URL, fully qualified, i.e. http{s}://... Add a space at the end or else you'll
    attempt to launch a browser

    :return: The content of the resource appropriately decoded if possible.
    """
    try:
        import requests

        response = requests.get(url)
        print("-" * 50)
        for k, v in response.headers.items():
            print(f"{k}: {v}")
        print(f"Status code: {response.status_code} - {response.reason}")
        print(f"Encoding: {response.encoding}")
        print("-" * 50)

        if response.status_code > 399:
            raise ValueError(f"HTTP status code is {response.status_code} - {response.reason}. ")
        if response.encoding:
            return response.content.decode(response.encoding)
        return response.content.decode()
    except Exception as e:
        print(f"Something bad happened when trying to get {url}.\nI can't return anything.\n{e}")
        return None


def main():
    """
    This is a function to test that the file-read and URL-get functions work properly. Only use in stand-alone mode.

    :return: Nothing
    """
    file_to_read = input("Enter filename: ")
    url_to_read = input("Enter web address: ")

    result = read_any_text_file(file_to_read.strip())
    print(f"\n{'=' * 50}\nContents of {file_to_read}\n{'-' * 50}\n{result}\n{'=' * 50}")
    result = get_stuff_from_net(url_to_read.strip())
    print(f"\n{'=' * 50}\nContents of {url_to_read}\n{'-' * 50}\n{result}\n{'=' * 50}")


if __name__ == "__main__":
    """Before executing code, the Python interpreter reads source file and define few special variables/global variables.
    If the python interpreter is running that module (the source file) as the main program, it sets the special 
    __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will 
    be set to the module’s name. Module’s name is available as value to __name__ global variable. A module is a file 
    containing Python definitions and statements. The file name is the module name with the suffix .py appended.
    """
    main()
