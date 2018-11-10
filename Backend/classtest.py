from Objects import Message
from Objects import User
import datetime
test = User.user("boysanic", 1, "Fuck you", "dickandballs")
print(test.username)
print(test.userid)
print(test.bio);
print(test.profile_picture_id)
test2 = Message.message("You suck haha", datetime.datetime.now(), test)
print(test2.content)
print(test2.user.username)