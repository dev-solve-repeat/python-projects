#  https://www.google.com/search?q=weather+kochi
# User agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36
# span id: wob_tm


from requests_html import HTMLSession
import speech2text

s = HTMLSession()
cityName = "Kochi"
url = f'https://www.google.com/search?q=weather+{cityName}'

r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'})

temp = r.html.find('span#wob_tm', first = True).text
print(temp)
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first = True).text
print(unit)
desc = r.html.find('span#wob_dc', first = True).text #When id use # and when class use "."
print(desc)

