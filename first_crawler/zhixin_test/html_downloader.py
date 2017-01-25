import urllib.request


class HtmlDownloader(object):
    def download(self, new_url):
        if new_url is None:
            return None
        reponse = urllib.request.urlopen(new_url)

        if reponse.getcode() != 200:
            return  None
        return  reponse.read()