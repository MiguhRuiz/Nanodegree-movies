import info
import fresh_tomatoes

toy_story = info.Film("Toy Story", "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg", "KYz2wyBy3kc")
# print(toy_story.title)

avatar = info.Film("Avatar", "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp", "kbA9TfGphOI")
# print(avatar.title)
# avatar.show_trailer()

school_of_rock = info.Film("School Of Rock", "http://cps-static.rovicorp.com/3/JPG_400/MI0000/398/MI0000398846.jpg?partner=allrovi.com", "XCwy6lW5Ixc")

movies = [toy_story, avatar, school_of_rock]
fresh_tomatoes.open_movies_page(movies)
