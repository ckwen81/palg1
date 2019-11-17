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