from flask import Flask, render_template, request, session, redirect, url_for
from entity.user import User
from dao.userdao import UserDAO
from dao.jobdao import JobDAO
from dao.moviedao import MovieDAO
import os
from entity.getpic import Img
from datetime import timedelta
from util import pageutils

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)   #设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  #设置session的保存时间。
userDAO = UserDAO()
jobDAO=JobDAO()
movieDAO=MovieDAO()

@app.route('/')   #  flask的路由，就是用来关联url和处理函数
def index():      #  就是做了跳转
    if session.get("userName"):
        users = userDAO.getAllUsers()
        return render_template('main.html', users=users)
    else:
        return render_template('index2.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    #return render_template('main.html')

    userName = request.form['userName']
    userPwd  = request.form['userPwd']
    if userName != "" and userPwd != "":
        user = User()
        user.userName = userName
        user.userPwd  = userPwd
        result = userDAO.getUserByUserNameAndPwd(user)
        session['userName'] = userName  # session 存放在服务器上，在超时时间之前一直存在
    if result:
        users = userDAO.getAllUsers()
        return render_template('main.html', users=users)
    else:
        message = "用户名或密码不正确"
        return render_template('index2.html', message=message, code=500)  # 第一参数是其他的URL，message是带过去的数据
    pass


# 通过路由中转到注册页面
@app.route('/goregister', methods=['GET'])
def goregister():
    return render_template('register.html')
    pass

@app.route('/register', methods=['GET', 'POST'])
def register():
    userName = request.form['userName']
    userPwd  = request.form['userPwd']
    if userName != "" and userPwd != "":
        user = User()
        user.userName = userName
        user.userPwd  = userPwd
        result = userDAO.createUser(user)
    if result:
        return render_template('index.html', message="注册成功，请登录", code=500)  # 第一参数是其他的URL，message是带过去的数据
    if result:
        return render_template('register.html', message="注册失败", code=500)  # 第一参数是其他的URL，message是带过去的数据
    pass

# url传参是采用的get方法， 参数传递的格式是在URL后带？，多个参数用&连接
@app.route('/delete', methods=['GET', 'POST'])
def deleteUser():
    userId = request.args.get('userId')  #
    print(userId)
    result = 0
    if userId != "":
        result = userDAO.deleteUserById(userId)
        pass
    if result:
        message = "删除成功"
    else:
        message = "删除失败"
    users = userDAO.getAllUsers()
    return render_template('main.html', users=users, message=message)
    pass
@app.route('/gojob', methods=['GET'])
def gojob():

    jobs=jobDAO.getAllJobs()
    pager_obj = pageutils.Pagination(request.args.get("page", 1), len(jobs), request.path, request.args, per_page_count=20)
    index_list = jobs[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template('job.html',html=html,index_list=index_list)
    pass
@app.route('/goposition',methods=['POST','GET'])
def position():
    jobposition=request.form['position']
    print(jobposition)
    jobs = jobDAO.getJobsposition(jobposition)
    pager_obj = pageutils.Pagination(request.args.get("page", 1), len(jobs), request.path, request.args,
                                     per_page_count=20)
    index_list = jobs[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template('job.html', html=html, index_list=index_list)
    pass
@app.route('/gocompany',methods=['POST','GET'])
def jobcompany():
    jobcompany=request.form['jobcompany']
    print(jobcompany)
    jobs = jobDAO.getJobcompany(jobcompany)
    pager_obj = pageutils.Pagination(request.args.get("page", 1), len(jobs), request.path, request.args,
                                     per_page_count=20)
    index_list = jobs[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template('job.html', html=html, index_list=index_list)
    pass
@app.route('/gojobarea',methods=['POST','GET'])
def jobarea():
    jobarea=request.form['jobarea']
    print(jobarea)
    jobs = jobDAO.getJobarea(jobarea)
    pager_obj = pageutils.Pagination(request.args.get("page", 1), len(jobs), request.path, request.args,
                                     per_page_count=20)
    index_list = jobs[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template('job.html', html=html, index_list=index_list)
    pass
@app.route('/gomovie', methods=['GET'])
def gomovie():
    movies=movieDAO.getAllMovies()
    pager_obj = pageutils.Pagination(request.args.get("page", 1), len(movies), request.path, request.args,
                                     per_page_count=20)
    index_list = movies[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template('movie.html', html=html, index_list=index_list)
    pass
@app.route('/gophoto', methods=['GET'])
def gophoto():
    return render_template('photos.html')
    pass
@app.route('/gohuge', methods=['GET'])
def gohuge():
    return render_template('huge.html')
    pass
@app.route('/goluhan', methods=['GET'])
def goluhan():
    return render_template('luhan.html')
    pass
@app.route('/goreba', methods=['GET'])
def goreba():
    return render_template('reba.html')
    pass
@app.route('/gowjk', methods=['GET'])
def gowjk():
    return render_template('wjk.html')
    pass
@app.route('/gopic', methods=['GET'])
def gopic():
    return render_template('pic.html')
    pass
@app.route('/pic1', methods=['GET'])
def pic1():
    return render_template('pic1.html')
    pass
@app.route('/pic2', methods=['GET'])
def pic2():
    return render_template('pic2.html')
    pass
@app.route('/pickey',methods=['POST'])
def pickey():
    key=request.form['key']
    img = Img(key)
    img.run()
    return render_template('pic2.html')
@app.route('/goechart', methods=['GET'])
def goechart():
    return render_template('echrt.html')
    pass
@app.route('/gomap', methods=['GET'])
def gomap():
    return render_template('map.html')
    pass
@app.route('/gorealdata', methods=['GET'])
def gorealdata():
    return render_template('realdata.html')
    pass

@app.route('/zaxiang', methods=['GET'])
def zaxiang():
    return render_template('zaxiang.html')
    pass
@app.route('/tupianlunbo', methods=['GET'])
def tupianlunbo():
    return render_template('lunbo.html')
    pass
@app.route('/zhuanpan', methods=['GET'])
def zhuanpan():
    return render_template('zhuanpan.html')
    pass
@app.route('/ditu', methods=['GET'])
def ditu():
    return render_template('ditu.html')
    pass
@app.route('/biaobai', methods=['GET'])
def biaobai():
    return render_template('biaobai.html')
    pass

if __name__ == '__main__':
    app.run()
'''
定义：处理URL和函数之间关系的程序。
简单的说：路由就是将URL绑定到一个函数上面，这样浏览器客户端向web服务器发送一个URL请求后，服务器中的
路由收到这个URL后，能立马找到对应的函数进行处理。
'''
