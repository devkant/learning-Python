import urllib.request
def read_text():
	quotes	=open("/home/devkant/Desktop/git/learning-Python//movie_quotes.txt")
	contents_of_file	=	quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

def check_profanity(text_to_check):
	text = urllib.parse.quote(text_to_check)
	connection=urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text)
	output	=	connection.read()
	if	'false' in str(output):
		print("Document is clean")
	else:
		print("It contains curse words")
	connection.close()
	
read_text()
