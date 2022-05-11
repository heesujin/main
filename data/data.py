from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://heesu:heesujin@cluster0.seicp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.recycle

doc = {
    'name':'순후추',
    'explanation':'후추는 냄새를 맡으면 재채기가 나올 정도로 자극적인 매운맛을 내는 향신료이다. 느끼한 맛을 가리거나 감칠맛을 더하기 위해 사용하는 후추의 올바른 분리배출 방법은 무엇일까?'
}

db.lists.insert_one(doc)