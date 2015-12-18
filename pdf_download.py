from pattern.web import URL

url_list = [url_list.rstrip('\n') for url_list in open('url.txt')]

for index, search_url in enumerate(url_list):
    if search_url[-4:] == ".pdf":
        url = URL(search_url)
        f = open(search_url[-5:], 'wb')
        f.write(url.download(cached = False))
        f.close()
