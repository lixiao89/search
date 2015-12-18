from pygoogle import pygoogle
from pattern.web import URL


g = pygoogle('logistic regression')
g.pages = 5

print '*Found %s results*'%(g.get_result_count())
url_list = g.get_urls()

with open('url.txt', 'w') as file:
    for url_search in url_list:
        file.write("{}\n".format(url_search))

# for seach_url in url_list:
#     print search_url
    # if search_url[-4:] == ".pdf":
    #     url = URL(search_url)
    #     f = open(search_url[-10:], 'wb')
    #     f.write(url.download(cached = False))
    #     f.close()
        

