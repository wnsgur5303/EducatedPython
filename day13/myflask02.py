from flask import Flask, request, Response, jsonify, render_template
import json
import pymysql
import logging



app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello Flask"

@app.route("/param", methods=['GET','POST'])
def param():
    if request.method == "POST":
        name = request.form.get('name', "kimchulsu")
    if request.method == "GET":
        name = request.args.get('name', "kimchulsu")  
    return "param="+name

@app.route("/forward.do")
def forward():
    title = "Good Morning"
    return render_template('forward.html',title=title)

@app.route("/db.do")
def db():
    mylogger.debug("conn select")
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    curs.execute("select emp_id,emp_name,nickname from emp")
    rows = curs.fetchall()
    conn.close()
    print(rows)
    return render_template('db.html',title="good",list=[1,2,3],db_list=rows)


@app.route("/upd.ajax")
def ajax_udp():
    mylogger.debug("conn update")
    emp_id = request.args.get('emp_id')
    emp_name = request.args.get('emp_name')
    nickname = request.args.get('nickname')
    
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    cnt = curs.execute("update emp set emp_name = '"+emp_name+"',nickname = '"+nickname+"' where emp_id = "+emp_id+"")
    rows = curs.fetchall()
    conn.commit()
    conn.close()
    obj ={"cnt":cnt}
    json_return=json.dumps(obj)
    mylogger.debug("update ok")
    return jsonify(json_return)
    
    

@app.route("/del.ajax") 
def ajax_del():
    mylogger.debug("conn delete")
    emp_id = request.args.get('emp_id')
    print("emp_id",emp_id)
    
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    cnt = curs.execute("delete from emp where emp_id = "+emp_id+"")
    rows = curs.fetchall()
    conn.commit()
    conn.close()
    obj ={"cnt":cnt}
    json_return=json.dumps(obj)
    mylogger.debug("delete ok")
    return jsonify(json_return)
 
 
 
@app.route("/ins.ajax")
def ajax_ins():
    mylogger.debug("conn insert")
    emp_name = request.args.get('emp_name')
    nickname = request.args.get('nickname')
    
    conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
    curs = conn.cursor()
    cnt = curs.execute("INSERT INTO emp(emp_name, nickname) VALUES('"+emp_name+"','"+nickname+"')")
    rows = curs.fetchall()
    conn.commit()
    conn.close()
    obj ={"cnt":cnt}
    json_return=json.dumps(obj)
    mylogger.debug("insert ok")
    return jsonify(json_return)

    
if __name__ == "__main__":
    mylogger = logging.getLogger("my")
    mylogger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    stream_hander = logging.StreamHandler()
    stream_hander.setFormatter(formatter)
    mylogger.addHandler(stream_hander)
    
    

    file_handler = logging.FileHandler('my.log')
    file_handler.setFormatter(stream_hander)
    
    mylogger.addHandler(file_handler)
    app.run()