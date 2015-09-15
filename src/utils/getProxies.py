from lxml import html
import requests
page = requests.post('http://spys.ru/en/http-proxy-list/', {"xpp":3})
tree = html.fromstring(page.text)

proxies = tree.xpath('//tr/td[1]/font[2]')
# proxies = tree.xpath('//tr/td[1]/font[2]')
# proxies = tree.xpath('//tr/td[1]/font[2]/following-sibling::text()[1]')
print proxies
