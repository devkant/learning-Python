import 	fresh_tomatoes
import	media

toy_story	=	media.Movie("Toy Story",
							"A story of boy and its story",
							"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
							"https://www.youtube.com/watch?v=LDXYRzerjzU")
#print(toy_story.storyline)

avatar	=	media.Movie("avatar",
						"a marine on an alien plane",
						"https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
						"https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)


coco	=	media.Movie("Coco",
						"a story of a mexican boy and his family",
						"https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",
						"https://www.youtube.com/watch?v=xlnPHQ3TLX8")
#coco.show_trailer()

movies	=[toy_story,avatar,coco]
#Fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)