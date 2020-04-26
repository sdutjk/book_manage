from tkinter import *  
from tkinter.messagebox import *  
import pymysql
from tkinter import  ttk
class InputFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.E3 = Entry(self)
        self.E4 = Entry(self)
        self.E5 = Entry(self)
        self.E6 = Entry(self)
        self.createPage()  

    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1


    def write(self,name,num,course,score):
        db = pymysql.connect(host='localhost', user='root', password='', database='test', charset='utf8')  # 连接本地数据库
        cur = db.cursor()  # 设置一个指针
        # 插入语句
        cur.execute("select * from book where bnum=%s", (name))  # 执行一条语句
        db.commit()
        result = cur.fetchall()
        if result:
            #messagebox.showinfo(title='结果', message="该图书已存在！")
            messagebox.showinfo(title='结果', message="图书编号存在，添加失败！")
        elif len(result)==0:
            db = pymysql.connect(host='localhost', user='root', password='', database='test', charset='utf8')  # 连接本地数据库
            cur = db.cursor()  # 设置一个指针
            # 插入语句
            cur.execute("select * from book where bname = %s and bauthor =%s", (num,course))  # 执行一条语句
            db.commit()
            result2 = cur.fetchall()
            if result2:
                messagebox.showinfo(title='结果', message="图书已存在，添加失败！")
            else:
                db = pymysql.connect(host='localhost', user='root', password='', database='test', charset='utf8')  # 连接本地数据库
                cur = db.cursor()  # 设置一个指针
                sql = "insert into book(bnum,bname,bauthor,btime) values (%s,%s,%s,%s)"
                cur.execute(sql, [name, num, course, score])
                db.commit()
                messagebox.showinfo(title='结果', message="添加成功！")




    
    def click(self):
        name = self.E1.get()
        num = self.E2.get()
        course = self.E3.get()
        score = self.E4.get()
        if self.Isspace(name) or self.Isspace(num) or self.Isspace(course) or self.Isspace(score) :
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            self.write(name,num,course,score)
            
        
        
    def createPage(self):  
        Label(self).grid(row=0, stick=W, pady=10)
        
        Label(self, text = '图书编号: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)

        Label(self, text = '图书名: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)

        Label(self, text = '图书作者: ').grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=E) 

        Label(self, text = '出版日期: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)       
        
        Button(self, text='添加图书',command=self.click).grid(row=6, column=1, stick=E, pady=10)
  
  
class DeleteFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.createPage()
        
    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1

    def delete(self,num,course):
        db = pymysql.connect(host='localhost', user='root', password='', database='test', charset='utf8')  # 连接本地数据库
        cur = db.cursor()  # 设置一个指针
        sql = "delete from book where bnum=%s and bname=%s"
        cur.execute(sql, [num,course])
        db.commit()
        messagebox.showinfo(title='结果', message="删除图书成功！")



        
    def click(self):
        num = self.E1.get()
        course = self.E2.get()
        if self.Isspace(num) or self.Isspace(course):
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            self.delete(num,course)
            
    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        
        Label(self, text = '图书编号: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)

        Label(self, text = '图书名称: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)

        Button(self, text='删除',command=self.click).grid(row=6, column=1, stick=E, pady=10)  
  
  
class ModifyFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.E1 = Entry(self)
        self.E2 = Entry(self)
        self.E3 = Entry(self)
        self.E4 = Entry(self)
        self.E5 = Entry(self)
        self.createPage()  

    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1

        
    def modify(self,name,num,course,score):
        db = pymysql.connect(host='localhost', user='root', password='', database='test', charset='utf8')  # 连接本地数据库
        cur = db.cursor()  # 设置一个指针
        # 插入语句
        cur.execute("select * from book where bnum=%s", (name))  # 执行一条语句
        db.commit()
        result = cur.fetchall()
        if(len(result)==0):
            messagebox.showinfo(title='提示', message="没有该图书信息！")
        else:
            db = pymysql.connect(host='localhost', user='root', password='', database='test', charset='utf8')  # 连接本地数据库
            cur = db.cursor()  # 设置一个指针
            sql = "update book set bname=%s,bauthor=%s,btime=%s where bnum=%s"
            cur.execute(sql, [num, course,score,name])
            db.commit()
            messagebox.showinfo(title='提示', message ="修改图书信息成功!")

    def click(self):
        name = self.E1.get()
        num = self.E2.get()
        course = self.E3.get()
        score = self.E4.get()
        if self.Isspace(name) or self.Isspace(num) or self.Isspace(course) or self.Isspace(score) :
            messagebox.showinfo(title='提示', message ="输入项为空")
        else:
            self.modify(name,num,course,score)
        
        
    def createPage(self):  
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text = '图书编号: ').grid(row=1, stick=W, pady=10)
        self.E1.grid(row=1, column=1, stick=E)

        Label(self, text = '图书名称: ').grid(row=2, stick=W, pady=10)
        self.E2.grid(row=2, column=1, stick=E)

        Label(self, text = '图书作者: ').grid(row=3, stick=W, pady=10)
        self.E3.grid(row=3, column=1, stick=E) 

        Label(self, text = '出版日期: ').grid(row=4, stick=W, pady=10)
        self.E4.grid(row=4, column=1, stick=E)       
        
        Button(self, text='修改',command=self.click).grid(row=6, column=1, stick=E, pady=10)  

class QueryFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root
        # self.E1 = Entry(self)
        # self.E2 = Entry(self)
        self.result=''
        self.createPage()  

    def Isspace(self,text):
        temp = 0
        for i in text:
           if not i.isspace():
               temp = 1
               break;

        if temp==1:
            return 0
        else:
            return 1

    def query(self,num,course):
        db = pymysql.connect(host='localhost', user='root', password='', database='test', charset='utf8')  # 连接本地数据库
        cur = db.cursor()  # 设置一个指针
        # 插入语句
        cur.execute("select bnum,bname from book where bnum=%s and bname=%s", (num,course))
        db.commit()
        result = cur.fetchall()  # 获取单条数据
        result1=str(result)
        if result:

                 messagebox.showinfo(title='结果', message ="姓名："+result1[0] +"\n学号:"+result1[1] +"\n科目:"+result1[2] +"\n成绩:"+result1[3] )
                 return

        # messagebox.showinfo(title='提示', message ="没有该信息")
        # f.close()
        # return


    def show(self):
        db = pymysql.connect(host='localhost', user='root', password='', database='test', charset='utf8')  # 连接本地数据库
        cur = db.cursor()  # 设置一个指针
        # 插入语句
        cur.execute("select * from book ")
        db.commit()
        self.result = cur.fetchall()  # 获取单条数据

        tree_data = ttk.Treeview(self)  # c创建一个表格
        tree_data['columns'] = ('图书编号', '图书名称', '图书作者', '出版日期')
        tree_data.column('#0', width=1)
        tree_data.column('图书编号', width=100)
        tree_data.column('图书名称', width=100)
        tree_data.column('图书作者', width=100)
        tree_data.column('出版日期', width=100)
        # 设置列名
        tree_data.heading('图书编号', text='图书编号')
        tree_data.heading('图书名称', text='图书名称')
        tree_data.heading('图书作者', text='图书作者')
        tree_data.heading('出版日期', text='出版日期')
        for row in self.result:
            tree_data.insert('', 0, values=(row[0], row[1], row[2], row[3]))
        tree_data.grid(row=6, column=1, stick=E, pady=10)
            
    def createPage(self):
        Label(self,text='图书信息').grid(row=5, column=1, pady=10)

        Button(self,text='Fresh',command=self.show).grid(row=5,column=2,pady=10)



