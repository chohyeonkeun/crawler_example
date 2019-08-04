import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190515"

custom_headers = {
    'referer': "https://movie.naver.com/common/css/old_common.css?20190313140445",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
}
req = requests.get(url)
if req.status_code == requests.codes.ok:
    html = BeautifulSoup(req.text, 'html.parser')
    movies = html.select('.list_ranking .title')
    for i, movie in enumerate(movies):
        rank = i + 1
        name = movie.select_one('.tit5')
        print(rank, name)

"""
이미지(img src) 크롤링하고 싶은 경우
soup = BeautifulSoup(req.text, '.pht217')

img_names = soup.find_all('img')
for img in img_names:
   print(img['src'])
"""