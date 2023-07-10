import telebot
import requests

TOKEN = '6100085419:AAEYozlbOqVihXvldlIpXUxKQWXESKBsyEo'

# Create a new Telebot instance
bot = telebot.TeleBot(6296490897:AAHa8rIVs5oXQTB_PJ7fDSjwyZbhdJARGxE)

# Define the start message for the bot
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the INFINITY HACK3RS MOVIE! To get started, type in the name of a movie you'd like to search for.BOT CREATED BY KRESSWELL @EscaliBud")

# Define the movie search function
@bot.message_handler(func=lambda message: True)
def movie_search(message):
    movie_name = message.text
    api_url = 'http://www.omdbapi.com/?apikey=4a08b314&t=' + movie_name
    response = requests.get(api_url).json()
    if response['Response'] == 'False':
        bot.reply_to(message, 'Movie not found. Please try again.')
    else:
        movie_title = response['Title']
        movie_plot = response['Plot']
        movie_genre = response['Genre']
        movie_imdb_rating = response['imdbRating']
        movie_poster = response['Poster']
        bot.send_photo(message.chat.id, movie_poster)
        bot.reply_to(message, 'Title: {}\n\nGenre: {}\n\nIMDb Rating: {}\n\nPlot: {}'.format(movie_title, movie_genre, movie_imdb_rating, movie_plot))

# Start the bot
bot.polling()