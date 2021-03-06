# life is short, you need use python to create something!
# author    TuringEmmy
# time      18-11-23 下午5:32
# project   spider_study

from pymongo import MongoClient

# 实例化链接对象
client = MongoClient()

# 创建数据库 集合  操作对象
col = client.turing.user
other = client['turing']['goods']

# 插入数据
ret = col.insert({'name': "TuringEmmy"})
print(ret)

print("*" * 100)
# 当插入数据时
ret = other.insert({"apple": 3})
print(ret)


print("*"*100)
# 新建管理员
# db.createUser({'user':'turing','pwd':'turing','roles':['root']})

# 启动mongodb的服务
# 启动: sudo service mongod start
# 停止: sudo service mongod stop
# 重启: sudo service mongod restart
# 配置文件的位置：/etc/mongod.conf
# 日志的位置：/var/log/mongodb/mongod.log
# 默认端⼝：27017