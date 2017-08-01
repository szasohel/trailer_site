# Project1: Movie Trailer Website
# Submitted by: Sayed Zahed Abdullah Sohel
# Date of submission: 7/20/2017
# File name: media.py

import webbrowser


class Movie():
    '''
    Class name: Movie Class
    Description: This class store movie object has a
    title, poster image url and a youtube url of it's trailer.
'''

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title  # title of the movie
        self.poster_image_url = poster_image  # url of the poster of the movie
        self.trailer_youtube_url = trailer_youtube
        # youtube link of trailer of the movie
