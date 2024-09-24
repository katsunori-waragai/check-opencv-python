import urllib.request
from pprint import pprint
def get_versions_in_pypi():
    """
    https://pypi.org/rss/project/opencv-python/releases.xml
    :return:
    """
    def remove_marker(line):
        return line.replace("<link>", "").replace("</link>", "").strip()

    url = "https://pypi.org/rss/project/opencv-python/releases.xml"

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = res.read()

    lines = body.decode().splitlines()
    links = [remove_marker(line) for line in lines if line.find("<link>") > -1 and line.find("</link>") > -1]
    links = sorted(links)
    pprint(links)
    oname = "versions.txt"
    with open(oname, "wt") as f:
        for a in links:
            f.write(f"{a}\n")

get_versions_in_pypi()