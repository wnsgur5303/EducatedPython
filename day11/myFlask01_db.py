from flask import Flask
from flask import request
from flask.templating import render_template
from flask import Flask, request, render_template, redirect
import pymysql

class MyManager:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', passwd='java', db='python', charset='utf8')
        self.curs= self.conn.cursor()
        
    def __del__(self):
        self.conn.close()

    def getPricesPer(self,s_name):
        sql = "select * from stock WHERE s_name = '"+s_name+"' order by in_time desc"
        
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        a = []
        for row in rows :
            a.append(row)
            print(row[1])
        return a

mm = MyManager()

prices = mm.getPricesPer('삼성전자')

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask!"

@app.route("/forward.do")
def forward():
    title = "Good Morning"
    return render_template('forward.html',prices)


if __name__ == "__main__":
    app.run()