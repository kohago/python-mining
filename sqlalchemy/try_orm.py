from database import init_db,db_session
from model.user import User


#init_db()

user1 = User("hoge1","1Hoge Jim","pw1")
db_session.add(user1)
db_session.commit()

user2 = User("hoge2","2Hoge Jim","pw2")
user3 = User("hoge3","3Hoge Jim","pw3")

db_session.add(user2)
db_session.add(user3)
db_session.commit()
