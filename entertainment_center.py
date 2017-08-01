# Project1: Movie Trailer Website
# Submitted by: Sayed Zahed Abdullah Sohel
# Date of submission: 7/20/2017
# File name: entertainment_center.py

import media
import fresh_tomatoes

# Dunkirk movie: Movie Title, Poster image URL, Youtube trailer URL
dunkirk = media.Movie("Dunkirk",
                      "https://i0.wp.com/media2.slashfilm.com/slashfilm/wp/wp-content/images/dunkirk-poster.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")  # NOQA

# Spider-Man: Homecoming: Movie Title, Poster image URL, Youtube trailer URL
spiderman = media.Movie("Spider-Man: Homecoming",
                        "http://i2.wp.com/www.slashfilm.com/wp/wp-content/images/spiderman-homecoming-finalposter2.jpg?resize=366%2C542",  # NOQA
                        "https://www.youtube.com/watch?v=U0D3AOldjMU")  # NOQA

# Transformers: Movie Title, Poster image URL, Youtube trailer URL
transformers = media.Movie("Transformers: The Last Knight",
                           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSssghc9DvmJwLTNbkGm2ImTMFpOVVyOD-PcOsVErrA0GqiW7ebyQ",  # NOQA
                           "https://www.youtube.com/watch?v=sQm3djLYWB8")  # NOQA

# Despicable Me 3 movie: Movie Title, Poster image URL, Youtube trailer URL
despicable_me_3 = media.Movie("Despicable Me 3",
                              "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRf_pH9ONqcR5ijfcn_ATIeIvV9JiQLMQ1QzVuETKKterZVIGVfvg",  # NOQA
                              "https://www.youtube.com/watch?v=oagwBHoh6Rs")  # NOQA

# The Mummyk movie: Movie Title, Poster image URL, Youtube trailer URL
the_mummy = media.Movie("The Mummy",
                        "http://www.impawards.com/2017/posters/mummy.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=IjHgzkQM2Sg")  # NOQA

# Wonder Woman movie: Movie Title, Poster image URL, Youtube trailer URL
wonder_woman = media.Movie("Wonder Woman",
                           "https://cdn.traileraddict.com/content/warner-bros-pictures/wonder-woman-2017-5.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=5lGoQhFb4NM")  # NOQA

# Guardians of the Galaxy: Movie Title, Poster image URL, Youtube trailer URL
gog_2 = media.Movie("Guardians of the Galaxy Vol. 2",
                    "https://media0dk-a.akamaihd.net/56/44/9309ee7890499a5b4d7d825f02dbe80e.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=2cv2ueYnKjg")  # NOQA

# The Fate of the Furious: Movie Title, Poster image URL, Youtube trailer URL
furious = media.Movie("The Fate of the Furious",
                      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0Xx6ywg7Pw_XhTS06KCgsYXKgvo8FYCQiEJpHs3A3tu4p8OqAUw",  # NOQA
                      "https://www.youtube.com/watch?v=JwMKRevYa_M")  # NOQA

# Power Rangers movie: Movie Title, Poster image URL, Youtube trailer URL
power_rangers = media.Movie("Power Rangers",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU1MTkxNzc5NF5BMl5BanBnXkFtZTgwOTM2Mzk3MTI@._V1_UY1200_CR74,0,630,1200_AL_.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=Q-C4qqsgs8w")  # NOQA

# Kong: Skull Island movie: Movie Title, Poster image URL, Youtube trailer URL
kong = media.Movie("Kong: Skull Island",
                   "http://www.impawards.com/2017/posters/kong_skull_island_ver10_xlg.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=AP0-9FBs2Rs&vl=en")  # NOQA

# Logan movie: Movie Title, Poster image URL, Youtube trailer URL
logan = media.Movie("Logan",
                    "https://images-na.ssl-images-amazon.com/images/I/81knWA39ANL._AC_UL320_SR208,320_.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=Div0iP65aZo")

# Rogue One movie: Movie Title, Poster image URL, Youtube trailer URL
rogue = media.Movie("Rogue One",
                    "http://media.comicbook.com/2016/11/rogue-one-international-poster-scarif-209818.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=frdj1zb9sMY")

movies = [dunkirk, spiderman, transformers, despicable_me_3, the_mummy,
          wonder_woman, gog_2, furious, power_rangers, kong, logan, rogue]
# movies list contains all movie objects

fresh_tomatoes.open_movies_page(movies)
