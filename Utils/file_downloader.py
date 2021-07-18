import requests


def download_file_from_link(file_name:str, link: str, link_manipulator=None):
    """
    Function to download file content from given link.
    :param link_manipulator: replace parts of link with certain string
    :param file_name: name of the file, that the downloaded content to be stored in
    :param link: download link
    :return: Integer
    """
    try:
        if link_manipulator:
            link = link.replace(link_manipulator[0], link_manipulator[1])

        with requests.get(link, stream=True) as r:
            r.raise_for_status()
            with open(file_name, 'wb') as file_writer:
                for chunk in r.iter_content(chunk_size=1024):
                    file_writer.write(chunk)
        return 0
    except (ConnectionError, TimeoutError):
        return -1
