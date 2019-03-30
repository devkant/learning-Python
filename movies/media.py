import	webbrowser
class	Movie():
	"""This class is class for movie"""
	VALID_RATING	=	["G","PG","PG-13","R"]
	def	__init__(self,title,movie_storyline,poster_image,trailer_youtube):
		self.title	=	title
		self.storyline	=	movie_storyline
		self.poster_image_url	=	poster_image
		self.trailer_youtube_url	=	trailer_youtube

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
		
