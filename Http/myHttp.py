import urllib.request


class myHttp(object):
    """docstring for myHttp"""

    def __init__(self, url):
        self.url = url

    def readPage(self):
        req = urllib.request.Request(self.url)
        res = urllib.request.urlopen(req)
        return res

    def outputPage(self, filename, path):
        page = self.readPage().read().decode("utf8")

        with open(path + "/" + filename, "w") as f:
            f.write(page)

    def sendRequest(self):
        pass


c = myHttp(b'www.baidu.com')
c.outputPage('text.html', '/')
