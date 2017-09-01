import media
import fresh_tomatoes

# Making several instances of the class Movie

toy_story = media.Movie("Toy story", "A boy and toys", "images/toy_story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "Animated Creatures", "images/avatar.jpg", "https://www.youtube.com/watch?v=d1_JBMrrYw8")

annabelle = media.Movie("Annabelle", "Horrible doll movie", "images/annabelle.jpg", "https://www.youtube.com/watch?v=KisPhy7T__Q")

grudge = media.Movie("Grudge", "Horror movie with" ,"images/grudge.jpg", "https://www.youtube.com/watch?v=o2vDoFYNRMc")

inception = media.Movie("Inception", "Inception" ,"images/inception.jpg", "https://www.youtube.com/watch?v=YoHD9XEInc0")

hunger_games = media.Movie("Hunger Games", "Advanterous movie with thrill" ,"images/hunger_games.jpg", "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, annabelle, grudge, inception, hunger_games]

# Calling fresh_tomatoes function open_movies_page to make a website

fresh_tomatoes.open_movies_page(movies)
#print(movie_website.Movie.__doc__)



