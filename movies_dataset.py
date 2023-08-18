import json
import pandas as pd
import scipy.stats as st
import math


class MoviesDatasetAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.df = None

    def load_data(self):
        """Loads the dataset from the CSV file."""
        self.df = pd.read_csv(self.filename, low_memory=False)
        self.df['release_date'] = pd.to_datetime(self.df['release_date'], errors='coerce')

    def extract_collection_name(self, collection_str):
        """Extracts the collection name from the string representation of a dictionary."""
        try:
            collection_dict = json.loads(collection_str.replace("'", "\""))
            return collection_dict.get('name', '')
        except (json.JSONDecodeError, TypeError, AttributeError):
            return ''

    def get_number_of_unique_movies(self):
        """Returns the number of unique movies in the dataset."""
        return self.df['title'].nunique()

    def get_average_rating(self):
        """Returns the average rating of all the movies."""
        return self.df['vote_average'].mean()

    def get_top_5_highest_rated_movies_without_vote_filter(self):
        """Returns the top 5 highest rated movies without considering the number of votes."""
        top_movies = self.df.sort_values(by='vote_average', ascending=False).head(5)
        top_movies['collection_name'] = top_movies['belongs_to_collection'].apply(self.extract_collection_name)
        return top_movies[['title', 'collection_name', 'vote_average']]

    def get_top_5_highest_rated_movies(self):
        """Returns the top 5 highest rated movies."""
        filtered_movies = self.df[self.df['vote_count'] > 50]
        top_movies = filtered_movies.sort_values(by='vote_average', ascending=False).head(5)
        top_movies['collection_name'] = top_movies['belongs_to_collection'].apply(self.extract_collection_name)
        return top_movies[['title', 'collection_name', 'vote_average']]

    def get_number_of_movies_released_each_year(self):
        """Returns the number of movies released each year."""
        return self.df['release_date'].dt.year.value_counts().sort_index(ascending=False)

    def extract_genres(self, genres_str):
        """Extracts genres from the string representation of a list of dictionaries."""
        try:
            genres_list = json.loads(genres_str.replace("'", "\""))
            return [genre_dict['name'] for genre_dict in genres_list]
        except (json.JSONDecodeError, TypeError, AttributeError):
            return []

    def get_number_of_movies_in_each_genre(self):
        """Returns the number of movies in each genre."""
        genres_series = self.df['genres'].apply(self.extract_genres)
        return genres_series.explode().value_counts()

    def weighted_rating(self, r, v):
        """Computes the weighted rating for a movie."""
        M = 2500
        C = self.df['vote_average'].mean()
        return (v / (v + M) * r) + (M / (v + M) * C)

    def get_top_movies_by_weighted_rating(self):
        """Returns the top movies ranked by the weighted rating."""
        self.df['weighted_rating'] = self.df.apply(lambda x: self.weighted_rating(x['vote_average'], x['vote_count']),
                                                   axis=1)
        top_movies = self.df.sort_values('weighted_rating', ascending=False).head(5)
        top_movies['collection_name'] = top_movies['belongs_to_collection'].apply(self.extract_collection_name)
        return top_movies[['title', 'collection_name', 'weighted_rating']]

    def save_data(self, filename):
        """Saves the dataset to a JSON file."""
        self.df.to_json(filename, date_format='iso')  # added date_format to handle datetime objects


# Testing the modified class again
modified_dataset = MoviesDatasetAnalyzer(
    r'C:\Users\ivsve\Desktop\adastra_task\the-movies-dataset\csv_files\movies_metadata.csv')
modified_dataset.load_data()
top_movies_modified = modified_dataset.get_top_5_highest_rated_movies()
top_movies_modified
