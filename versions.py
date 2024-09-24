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

    lines = body.decode().splitlines()
    links = []
    for line in lines:
        if line.find("<link>") > -1 and line.find("</link>") > -1:
            value = line.replace("<link>", "").replace("</link>", "").strip()
            links.append(value)
    links = sorted(links)
    pprint(links)
get_versions_in_pypi()