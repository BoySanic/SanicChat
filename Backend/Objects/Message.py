import Objects.User
import datetime
class message(object):
	def __init__(self, content, timesent, user):
		self.content = content
		self.timesent = timesent
		self.user = user
