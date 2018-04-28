class Song(object):
	
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print (line)

	def do_it(self, m):
		return m * self.base