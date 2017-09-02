import webbrowser


class Movie():
    """init function to initialize the variables and provide memory space"""
    def __init__(self, title,
                 storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    """show_trailer function to open a browser window and show the trailer"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
