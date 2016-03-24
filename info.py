import webbrowser
class Film():
    def __init__(self, name, poster, videoid):
        self.title = name
        self.poster_url = poster
        self.video_id = videoid

    def show_trailer(self):
        webbrowser.open(self.video_url)
