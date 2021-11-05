from flask import Flask, render_template,  jsonify, request, url_for
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# HTML 연결
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/quiz')
def quiz():
   return render_template('quiz.html')


@app.route('/result')
def result():
   return render_template('result.html')

#data
@app.route('/quizdata', methods=['GET'])
def showQuiz():
    quiz = list(db.mbtiprac.find({}, {'_id': False}))
    return jsonify({'all_quiz':quiz})

# 로컬호스트:5000
if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)