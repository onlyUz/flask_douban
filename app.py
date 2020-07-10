from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/index')
def index():
    return home()


@app.route('/movie')
def movie():
    conn = sqlite3.connect("豆瓣电影Top250.db")
    cur = conn.cursor()
    sql = "select * from doubanTop250"
    data = cur.execute(sql)
    datalist = []
    for item in data:
        datalist.append(item)
    conn.commit()
    conn.close()
    return render_template("movie.html", movies=datalist)


@app.route('/score')
def score():
    score = []
    number = []
    conn = sqlite3.connect("豆瓣电影Top250.db")
    cur = conn.cursor()
    sql = "select score,count(score) from doubanTop250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(str(item[0]))
        number.append(item[1])

    conn.commit()
    conn.close()
    return render_template("score.html", score=score, number=number)


@app.route('/word')
def word():
    return render_template("word.html")


@app.route('/team')
def team():
    return render_template("team.html")


if __name__ == '__main__':
    app.run()
