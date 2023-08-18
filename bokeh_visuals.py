import logging
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import column
from bokeh.models.widgets import Div

from movies_dataset import MoviesDatasetAnalyzer
from bokeh.plotting import figure

# Setup logging configurations
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')

def plot_top_movies_weighted(top_movies_weighted):
    p = figure(x_range=top_movies_weighted['title'], height=250, title="Top Movies by Weighted Rating")
    p.vbar(x=top_movies_weighted['title'], top=top_movies_weighted['weighted_rating'], width=0.9)
    p.xgrid.grid_line_color = None
    p.yaxis.axis_label = "Weighted Rating"
    p.xaxis.major_label_orientation = 1.2
    return p


# a. Top 5 highest rated movies
def plot_top_movies(top_movies):
    p1 = figure(x_range=top_movies['title'], title="Top 5 Highest Rated Movies",
                toolbar_location=None, tools="", y_axis_label="Rating")
    p1.vbar(x=top_movies['title'], top=top_movies['vote_average'], width=0.9)
    p1.xaxis.major_label_orientation = "vertical"

    return p1


# b. Number of movies released each year
def plot_movies_per_year(year_counts):
    p2 = figure(title="Number of Movies Released Each Year", tools="", y_axis_label="Number of Movies",
                x_axis_label="Year")
    p2.line(year_counts.index, year_counts.values, line_width=2)
    p2.circle(year_counts.index, year_counts.values, size=10, fill_color="white")

    return p2


# c. Number of movies in each genre
def plot_genre_counts(genre_counts):
    p3 = figure(y_range=list(genre_counts.index), title="Number of Movies in Each Genre",
                toolbar_location=None, tools="", x_axis_label="Number of Movies")
    p3.hbar(y=genre_counts.index, right=genre_counts.values, height=0.6)

    return p3

def display_number_of_unique_movies(num_unique_movies):
    """Display the number of unique movies."""
    text = f"<div style='font-size: 16px; margin: 10px;'>Number of Unique Movies: <h2 style='color: #555;'> {num_unique_movies}</h2></div>"
    return Div(text=text)

def display_average_rating(average_rating):
    """Display the average rating of all movies."""
    text = f"<div style='font-size: 16px; margin: 10px;'>Average Rating of All Movies: <h1 style='color: #0074D9;'> {average_rating:.2f} </h1></div>"
    return Div(text=text)

def plot_top_movies_without_vote_filter(top_movies_without_vote_filter):
    """Plot the top 5 highest rated movies without considering the number of votes."""
    p = figure(x_range=top_movies_without_vote_filter['title'], title="Top 5 Highest Rated Movies (No Vote Filter)",
               toolbar_location=None, tools="", y_axis_label="Rating")
    p.vbar(x=top_movies_without_vote_filter['title'], top=top_movies_without_vote_filter['vote_average'], width=0.9)
    p.xaxis.major_label_orientation = "vertical"
    return p

def plot_top_movies_bayesian(top_movies_bayesian):
    """Plot the top movies ranked by the Bayesian average rating."""
    p = figure(x_range=top_movies_bayesian['title'], title="Top Movies by Bayesian Rating",
               toolbar_location=None, tools="", y_axis_label="Bayesian Rating")
    p.vbar(x=top_movies_bayesian['title'], top=top_movies_bayesian['bar_score'], width=0.9)
    p.xaxis.major_label_orientation = "vertical"
    return p


# Assuming dataset has already been loaded using MoviesDatasetAnalyzer class
dataset = MoviesDatasetAnalyzer(r'C:\Users\ivsve\Desktop\adastra_task\the-movies-dataset\csv_files\movies_metadata.csv')
dataset.load_data()

top_movies = dataset.get_top_5_highest_rated_movies()
year_counts = dataset.get_number_of_movies_released_each_year()
genre_counts = dataset.get_number_of_movies_in_each_genre()
weighted_rating = dataset.get_top_movies_by_weighted_rating()
num_unique_movies = dataset.get_number_of_unique_movies()
average_rating = dataset.get_average_rating()
top_movies_without_vote_filter = dataset.get_top_5_highest_rated_movies_without_vote_filter()

# Output to an HTML file
output_file("movies_visualization.html")


# Create plots
# ****
# Uncomment if you are to solely use bokeh_visuals.py
# ****
#
# div_num_unique_movies = display_number_of_unique_movies(num_unique_movies)
# div_average_rating = display_average_rating(average_rating)
# p1 = plot_top_movies(top_movies)
# p2 = plot_movies_per_year(year_counts)
# p3 = plot_genre_counts(genre_counts)
# p4 = plot_top_movies_weighted(weighted_rating)
# p5 = plot_top_movies_without_vote_filter(top_movies_without_vote_filter)
#
# # Combine plots and display
# show(column(div_num_unique_movies, div_average_rating, p1, p2, p3, p4, p5))
