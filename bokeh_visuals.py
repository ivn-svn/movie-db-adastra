from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import column

from movies_dataset import MoviesDatasetAnalyzer


# a. Top 5 highest rated movies
def plot_top_movies(top_movies):
    p1 = figure(x_range=top_movies['title'], title="Top 5 Highest Rated Movies",
                toolbar_location=None, tools="", y_axis_label="Rating")
    p1.vbar(x=top_movies['title'], top=top_movies['vote_average'], width=0.9)
    p1.xaxis.major_label_orientation = "vertical"

    return p1

# b. Number of movies released each year
def plot_movies_per_year(year_counts):
    p2 = figure(title="Number of Movies Released Each Year", tools="", y_axis_label="Number of Movies", x_axis_label="Year")
    p2.line(year_counts.index, year_counts.values, line_width=2)
    p2.circle(year_counts.index, year_counts.values, size=10, fill_color="white")

    return p2

# c. Number of movies in each genre
def plot_genre_counts(genre_counts):
    p3 = figure(y_range=list(genre_counts.index), title="Number of Movies in Each Genre",
                toolbar_location=None, tools="", x_axis_label="Number of Movies")
    p3.hbar(y=genre_counts.index, right=genre_counts.values, height=0.6)

    return p3

# Assuming dataset has already been loaded using your MoviesDatasetAnalyzer class
dataset = MoviesDatasetAnalyzer(r'C:\Users\ivsve\Desktop\adastra_task\the-movies-dataset\csv_files\movies_metadata.csv')
dataset.load_data()

top_movies = dataset.get_top_5_highest_rated_movies()
year_counts = dataset.get_number_of_movies_released_each_year()
genre_counts = dataset.get_number_of_movies_in_each_genre()

# Output to an HTML file
output_file("movies_visualization.html")

# Create plots
p1 = plot_top_movies(top_movies)
p2 = plot_movies_per_year(year_counts)
p3 = plot_genre_counts(genre_counts)

# Combine plots and display
show(column(p1, p2, p3))
