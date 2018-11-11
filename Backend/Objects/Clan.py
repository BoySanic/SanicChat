#! /usr/bin/python3
from Objects import ClanChannel
from Objects import ClanUser
from Objects import User
from Objects import Message

class clan(object):
	def __init__(self, channels, users):
		self.channels = [ClanChannel("#general")]
		self.users = users
