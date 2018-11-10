class user(object):
	#constructor
	def __init__(self, username, userid, bio, profile_picture_id):
		self.userid = userid #ulong
		self.username = username #string
		self.bio = bio #string
		self.profile_picture_id = profile_picture_id #string
