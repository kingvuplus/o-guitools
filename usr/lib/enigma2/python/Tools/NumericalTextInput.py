# -*- coding: utf-8 -*-
from enigma import eTimer
from Components.Language import language

class NumericalTextInput:
	def __init__(self, nextFunc=None, handleTimeout = True, search = False):
		self.mapping = []
		self.lang = language.getLanguage()
		self.useableChars=None
		self.nextFunction=nextFunc

		if handleTimeout:
			self.timer = eTimer()
			self.timer.callback.append(self.timeout)
		else:
			self.timer = None
		self.lastKey = -1
		self.pos = -1

		if search:
			self.mapping.append (u"%_0") # 0
			self.mapping.append (u" 1") # 1
			self.mapping.append (u"abc2") # 2
			self.mapping.append (u"def3") # 3
			self.mapping.append (u"ghi4") # 4
			self.mapping.append (u"jkl5") # 5
			self.mapping.append (u"mno6") # 6
			self.mapping.append (u"pqrs7") # 7
			self.mapping.append (u"tuv8") # 8
			self.mapping.append (u"wxyz9") # 9
			return

		if self.lang == 'de_DE':
			self.mapping.append (u".,?'+\"0-()@/:_$!") # 0
			self.mapping.append (u" 1") # 1
			self.mapping.append (u"aشbc2AشBC") # 2
			self.mapping.append (u"def3DEF") # 3
			self.mapping.append (u"ghi4GHI") # 4
			self.mapping.append (u"jkl5JKL") # 5
			self.mapping.append (u"mnoö6MNOÖ") # 6
			self.mapping.append (u"pqrsß7PQRSß") # 7
			self.mapping.append (u"tuüv8TUÜV") # 8
			self.mapping.append (u"wxyz9WXYZ") # 9
		elif self.lang == 'ar_AE':
			self.mapping.append (u".,?'+\"0-()@/:_$!") # 0
			self.mapping.append (u" 1") # 1
			self.mapping.append (u"ب ت ة ث 2") # 2
			self.mapping.append (u"ا ء 3") # 3
			self.mapping.append (u"س ش ص ض 4") # 4
			self.mapping.append (u"د ذ ر ز 5") # 5
			self.mapping.append (u"ج ح خ 6") # 6
			self.mapping.append (u"ن ه و ي 7") # 7
			self.mapping.append (u"ف ق ك ل م 8") # 8
			self.mapping.append (u"ط ظ ع غ 9") # 9
		else:
			self.mapping.append (u".,?'+\"0-()@/:_$!") # 0
			self.mapping.append (u" 1") # 1
			self.mapping.append (u"abc2ABC") # 2
			self.mapping.append (u"def3DEF") # 3
			self.mapping.append (u"ghi4GHI") # 4
			self.mapping.append (u"jkl5JKL") # 5
			self.mapping.append (u"mno6MNO") # 6
			self.mapping.append (u"pqrs7PQRS") # 7
			self.mapping.append (u"tuv8TUV") # 8
			self.mapping.append (u"wxyz9WXYZ") # 9

	def setUseableChars(self, useable):
		self.useableChars = useable

	def getKey(self, num):
		cnt=0
		if self.lastKey != num:
			if self.lastKey != -1:
				self.nextChar()
			self.lastKey = num
			self.pos = -1
		if self.timer is not None:
			self.timer.start(1000, True)
		while True:
			self.pos += 1
			if len(self.mapping[num]) <= self.pos:
				self.pos = 0
			if self.useableChars:
				pos = self.useableChars.find(self.mapping[num][self.pos])
				if pos == -1:
					cnt += 1
					if cnt < len(self.mapping[num]):
						continue
					else:
						return None
			break
		return self.mapping[num][self.pos]

	def nextKey(self):
		if self.timer is not None:
			self.timer.stop()
		self.lastKey = -1

	def nextChar(self):
		self.nextKey()
		if self.nextFunction:
			self.nextFunction()

	def timeout(self):
		if self.lastKey != -1:
			self.nextChar()
