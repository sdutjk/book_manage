from tkinter import *  
from tkinter.messagebox import *  
from MainPage import *
import pymysql

class LoginPage(object):  
    def __init__(self, master=None):  
        self.root = master #定义内部变量root  
        self.root.geometry('%dx%d' % (300, 200)) #设置窗口大小  
        self.username = StringVar()  
        self.password = StringVar()  
        self.createPage()  
  
    def createPage(self):
        self.page = Frame(self.root) #创建Frame  
        self.page.pack()  
        Label(self.page).grid(row=0, stick=W)  
        Label(self.page, text = '账户: ').grid(row=1, stick=W, pady=10)  
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)  
        Label(self.page, text = '密码: ').grid(row=2, stick=W, pady=10)  
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)  
        Button(self.page, text='登陆', command=self.loginCheck).grid(row=3, column=0, pady=5)
        Button(self.page, text='注册', command=self.register).grid(row=3, column=1, pady=5)  
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=2, pady=5)
        
  
    def loginCheck(self):  
        name = self.username.get()  
        password = self.password.get()
        if self.isLegalUser(name,password):
            self.page.destroy()  
            MainPage(self.root)  
        else:  
            showinfo(title='错误', message='账号或密码错误！')
            
    def isLegal(self,string):
        alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in string:
            if i in alp:
                pass
            else:
                return False
        return True
        
    def isLegalUser(self,name,password):
        db = pymysql.connect(host='localhost', user='root', password='', database='test', charset='utf8')  # 连接本地数据库
        cur = db.cursor()  # 设置一个指针
        # 插入语句
        cur.execute("select * from admin where num = %s and pwd = %s", (name, password))  # 执行一条语句
        db.commit()
        result = cur.fetchall()  # 获取单条数据
        if result:
            return True
        else:
            return False

                
    def register(self):
        name = self.username.get()  
        password = self.password.get()
        if len(name)==0 or len(password)==0:
            showinfo(title='错误', message='账号密码不能为空')
            return
        for i in password:
            if i is ',' or i is ' ':
                showinfo(title='错误', message='密码不能含有非法字符')
                return
        if self.isLegal(name):
            pass
        else:
            showinfo(title='错误', message='账号不能含有非法字符')
            return
        db = pymysql.connect(host='localhost', user='root', password='', database='test', charset='utf8')  # 连接本地数据库
        cur = db.cursor()  # 设置一个指针
        # 插入语句
        cur.execute("select * from admin where num = %s and pwd = %s", (name, password))  # 执行一条语句
        db.commit()
        result = cur.fetchall()  # 获取单条数据
        if result:
            messagebox.showinfo(title='结果', message="已存在该用户信息！")
        else:
            sql = "insert into admin(num,pwd) values (%s,%s)"
            cur.execute(sql, [name,password])
            db.commit()
            messagebox.showinfo(title='结果', message="注册成功！")





