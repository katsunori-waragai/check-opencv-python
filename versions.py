import urllib.request
from pprint import pprint
def get_versions_in_pypi():
    """
    https://pypi.org/rss/project/opencv-python/releases.xml
    :return:
    """

    url = "https://pypi.org/rss/project/opencv-python/releases.xml"

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = res.read()

    # print(body)
    lines = body.splitlines()
    print(lines)
    links = []
    for line in lines:
        if line.find(b"<link>") > -1 and line.find(b"</link>") > -1:
            links.append(line)
    pprint(links)
get_versions_in_pypi()