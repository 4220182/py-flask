'''
1. 模版放置在./templates目录下。
2. config.py 是存放所有配置文件
'''

from flask import Flask, render_template, make_response
import config

app = Flask(__name__)
app.config.from_object(config) #只识别大写 key.isupper()

# 测试传递单个参数
@app.route("/app")
def process_request_app():
    url = "/login"
    resp = make_response(render_template('app.html', url=url))
    resp.headers['Content-type'] = 'text/html; charset=UTF-8'
    return resp

# 测试传递dict
@app.route("/dict")
def process_request_dict():
    dicts = {"username": "zyh", "age": 12}
    resp = make_response(render_template('dict.html', data=dicts))
    resp.headers['Content-type'] = 'text/html; charset=UTF-8'
    return resp

# 测试传递list
@app.route("/list")
def process_request_list():
    lists = ["test1","test2","test3","test4"]
    resp = make_response(render_template('list.html', data=lists))
    resp.headers['Content-type'] = 'text/html; charset=UTF-8'
    return resp

# 测试整体传送参数
@app.route("/send")
def process_request_send():
    lists = ["test1","test2","test3","test4"]
    dicts = {"username": "zyh", "age": 12}
    data = {"lists": lists,
            "dicts": dicts}

    resp = make_response(render_template('send-args.html', **data))
    resp.headers['Content-type'] = 'text/html; charset=UTF-8'
    return resp

# main
if __name__ == '__main__':
    print("started.\n"
          "url: 0.0.0.0:10000/\n"
          "app-debug: ", app.debug)
    # 载入配置文件
    app.run(host="0.0.0.0",port=10000)