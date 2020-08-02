'''
表单，一般采用flask-wtf处理Form：
https://github.com/lepture/flask-wtf
https://pypi.org/project/Flask-WTF/
https://github.com/lepture/flask-wtf
https://blog.csdn.net/bird333/article/details/80722747

https://flask-wtf.readthedocs.io/en/stable/
https://flask-wtf.readthedocs.io/en/stable/quickstart.html#validating-forms

当您的用户提交将reCAPTCHA(验证码)集成到其中的表单时，您将获得一个名为“ g-recaptcha-response”的字符串作为有效负载的一部分。
为了检查Google是否已验证该用户，请发送带有以下参数的POST请求：
URL：https://www.google.com/recaptcha/api/siteverify
*** 由于google墙了，所以 在中国还不能使用 wtf的验证码功能。

'''

from flask import Flask, render_template, make_response, redirect
from flask_wtf import FlaskForm,RecaptchaField #引入FlaskForm类，作为自定义Form类的基类
from wtforms import StringField,SubmitField       #StringField对应HTML中type="text"的<input>元素，SubmitField对应type='submit'的<input>元素
from wtforms.validators import DataRequired

import config

app = Flask(__name__)
app.config.from_object(config) #只识别大写 key.isupper()


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')

@app.route("/form",methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():        #服务器收到没有表单数据的GET请求 ，因此form.validate_on_submit() == False
        name = form.name.data            #不执行，跳过
        return redirect('/list')                #不执行 ，跳过
    return render_template('form.html', name=name, form=form)            #把name,form变量传入模板，渲染，返回给客户端。

@app.route("/list")
def process_request_list():
    lists = ["test1","test2","test3","test4"]
    resp = make_response(render_template('list.html', data=lists))
    resp.headers['Content-type'] = 'text/html; charset=UTF-8'
    return resp

# main
if __name__ == '__main__':
    print("started.\n"
          "url: 0.0.0.0:10000/\n"
          "app-debug: ", app.debug)
    # 载入配置文件
    app.run(host="0.0.0.0",port=10000)