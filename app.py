from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from jieba.analyse import extract_tags  # 提取关键字
import utils
import random
import string



app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route('/time')
def get_time():
    return utils.get_time()


@app.route('/c1')
def get_c1_data():
    data = utils.get_c1_data()
    # 将字典转换成json
    return jsonify({"confirm": data[0], "suspect": data[1],
                    "heal":data[2], "dead": data[3]})



@app.route('/l1',  methods=["get", "post"])
def get_l1_data():
    day,confirm,suspect,heal,dead = [],[],[],[],[]
    for a,b,c,d,e in utils.get_l1_data():
        day.append(a.strftime("%Y.%m.%d"))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    # 将字典转换成json
    return jsonify({"day":day,"confirm":confirm,"suspect":suspect,"heal":heal,"dead":dead})


@app.route('/l2',  methods=["get", "post"])
def get_l2_data():
    day, confirm_add, suspect_add = [], [], []
    for a,b,c in utils.get_l2_data():
        day.append(a.strftime("%m.%d"))
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({"day":day, "confirm_add": confirm_add, "suspect_add": suspect_add})

@app.route('/r1',  methods=["get", "post"])
def get_r1_data():
    city=[]
    confirm=[]
    for a,b in utils.get_r1_data():
        city.append(a)
        confirm.append(int(b))
    return jsonify({"city":city, "confirm":confirm})

# global data1
# @app.route('/temp', methods=["get", "post"])
# def temp():
#     global data1
#     da = request.form.get('value')
#     if da:
#         data1 = da
#     da = data1
#     return da

@app.route('/c2', methods=["get", "post"])
def get_c2_data():
    global data1
    value_temp = request.form.get('se_value')
    if value_temp:
        data1 = value_temp
    value_temp = data1
    res = []
    c2 = utils.get_c2_data()
    if value_temp == "现有确诊":
        c2 = utils.get_c2_data1()

    for i in c2:
        res.append({'name': i[0], 'value': int(i[1])})
    # 将字典转换成json
    return jsonify({"data": res, "text": value_temp})


@app.route('/r2',  methods=["get", "post"])
def get_r2_data():
    word=[]
    for i in utils.get_r2_data():
        k = i[0].rstrip(string.digits)  # 移除数字
        v = random.randint(1,200)  # 随机给一个数字
        ks = extract_tags(k)
        for j in ks:
            if not j.isdigit():
                word.append({"name": j, "value": v})
    return jsonify({"kws": word})



if __name__ == '__main__':
    app.run(debug=True)


# # ---------------------------------
#
# @app.route('/login')
# def login():
#     name = request.values.get("name")
#     pwd = request.values.get("pwd")
#     return f"name = {name}, pwd = {pwd}"
#
# @app.route('/ajax', methods=["get", "post"])
# def test():
#     name = request.values.get("name")
#     con = request.values.get("content")
#     print(f"name = {name}, content = {con}")
#     return '1000'
#
# @app.route('/abc')
# def abc():
#     id = request.values.get("id")
#     return f"""
#     <form action="/login">
#         账号：<input name="name"><br>
#         密码：<input name="pwd"><br>
#         <input type="submit">
#     </form>
#     """
# # ----------------------------------
#
#
