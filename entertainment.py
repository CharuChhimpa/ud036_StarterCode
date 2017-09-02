import media
import fresh_tomatoes


# Toy story movie : title, storyline, poster, trailer
toy_story = media.Movie(
  "Toy story",
  "A boy and toys",
  "images/toy_story.jpg",
  "https://www.youtube.com/watch?v=KYz2wyBy3kc"
)

# Avatar movie : title, storyline, poster, trailer
avatar = media.Movie(
  "Avatar",
  "Animated Creatures",
  "images/avatar.jpg",
  "https://www.youtube.com/watch?v=d1_JBMrrYw8"
)

# Annabelle movie : title, storyline, poster, trailer
annabelle = media.Movie(
  "Annabelle",
  "Horrible doll movie",
  "images/annabelle.jpg",
  "https://www.youtube.com/watch?v=KisPhy7T__Q"
)

# Grudge movie : title, storyline, poster, trailer
grudge = media.Movie(
  "Grudge",
  "Horror movie with",
  "images/grudge.jpg",
  "https://www.youtube.com/watch?v=o2vDoFYNRMc"
)

# Inception movie : title, storyline, poster, trailer
inception = media.Movie(
  "Inception",
  "Inception",
  "images/inception.jpg",
  "https://www.youtube.com/watch?v=YoHD9XEInc0"
)

# Hunger games : title, storyline, poster, trailer
hunger_games = media.Movie(
  "Hunger Games",
  "Advanterous movie with thrill",
  "images/hunger_games.jpg",
  "https://www.youtube.com/watch?v=mfmrPu43DF8"
)

# Movies list to pass to media file
movies = [
  toy_story,
  avatar,
  annabelle,
  grudge,
  inception,
  hunger_games
]

# Calling fresh_tomatoes function open_movies_page to make a website

fresh_tomatoes.open_movies_page(movies)
