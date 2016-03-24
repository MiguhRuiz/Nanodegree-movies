import definitions
import fresh_tomatoes

option1 = definitions.Film("Steve Jobs", "http://pics.filmaffinity.com/Steve_Jobs-647763435-large.jpg", "aEr6K1bwIVs")
# print(toy_story.title)

option2 = definitions.Film("The Matrix", "http://pics.filmaffinity.com/The_Matrix-155050517-large.jpg", "m8e-FF8MsqU")
# print(avatar.title)
# avatar.show_trailer()

option3 = definitions.Film("The Social Network", "http://pics.filmaffinity.com/The_Social_Network-460155430-large.jpg", "lB95KLmpLR4")

movies = [option1, option2, option3]
fresh_tomatoes.open_movies_page(movies)
