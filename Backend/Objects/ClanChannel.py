#! /usr/bin/python3
from Objects import Clan
from Objects import ClanUser
from Objects import Message
from Objects import User

class clanchannel(object):
	def __init__(self, messages, users):
		self.messages = []
		self.users = []
		