def read_text():
	quotes	=	open("/run/media/devkant/New Volume/git/learning-Python/movie_quotes.txt")
	contents_of_file	=	quotes.read()
	print(contents_of_file)
	quotes.close()

read_text()