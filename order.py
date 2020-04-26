import pymysql
num='001'
course='百年孤独'
db = pymysql.connect(host='localhost', user='root', password='', database='test', charset='utf8')  # 连接本地数据库
cur = db.cursor()  # 设置一个指针
# 插入语句
cur.execute("select * from book" )
db.commit()
result = cur.fetchall()  # 获取单条数据
# result1 = str(result)
# print(result[0][0])
for row in result:
    print(row[1])