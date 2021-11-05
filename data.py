from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# data.html -> DB,

soup = BeautifulSoup(open("templates/data.html"), 'html.parser') # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
trs = soup.select('table > tbody > tr') # select를 이용해서, tr들을 불러오기

for tr in trs:
    question = tr.select_one('td.question').text
    answer1 = tr.select_one('td.answer1').text
    value1 = tr.select_one('td.value1').text
    answer2 = tr.select_one('td.answer1').text
    value2 = tr.select_one('td.answer1').text
    doc = {
        'question' : question,
        'answer1' : answer1,
        'value1' : value1,
        'answer2' : answer2,
        'value2' : value2
    }

    db.mbtiprac.insert_one(doc)