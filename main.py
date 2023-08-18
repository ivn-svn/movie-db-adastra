#!/usr/bin/env python
import logging
from bokeh.io import output_file, show
from bokeh.layouts import column

from movies_dataset import MoviesDatasetAnalyzer
import bokeh_visuals

# Setup logging configurations
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')


def main():
    """The modified main function."""
    try:
        dataset = MoviesDatasetAnalyzer(
            r'C:\Users\ivsve\Desktop\adastra_task\the-movies-dataset\csv_files\movies_metadata.csv')
        dataset.load_data()

        print('--- MOVIE DATASET ANALYSIS ---\n')

        # Number of unique movies
        print(f'Number of unique movies: {dataset.get_number_of_unique_movies()}')

        # Average rating
        print(f'Average rating: {dataset.get_average_rating():.2f}\n')

        # Top 5 highest rated movies without considering vote count
        print('Top 5 highest rated movies (without considering vote count):')
        top_movies_without_filter = dataset.get_top_5_highest_rated_movies_without_vote_filter()
        for index, row in top_movies_without_filter.iterrows():
            print(
                f"Title: {row['title']}, Rating: {row['vote_average']:.1f} ({row['collection_name'] if row['collection_name'] else 'No Collection'})")
        print()

        # Top 5 highest rated movies
        print('Top 5 highest rated movies:')
        top_movies = dataset.get_top_5_highest_rated_movies()
        for index, row in top_movies.iterrows():
            print(
                f"Title: {row['title']}, Rating: {row['vote_average']:.1f} ({row['collection_name'] if row['collection_name'] else 'No Collection'})")
        print()

        # Number of movies released each year
        print('Number of movies released each year:')
        year_counts = dataset.get_number_of_movies_released_each_year()
        for year, count in year_counts.items():
            print(f"{year}: {count} movies")
        print()

        # Number of movies in each genre
        print('Number of movies in each genre:')
        genre_counts = dataset.get_number_of_movies_in_each_genre()
        for genre, count in genre_counts.items():
            print(f"{genre}: {count} movies")
        print()

        print('Top Movies Weighted\n\n')
        top_movies_weighted = dataset.get_top_movies_by_weighted_rating()
        print(top_movies_weighted)

        # Save dataset to JSON
        dataset.save_data('movies_dataset.json')
        print('Dataset saved to movies_dataset.json')

    except Exception as e:
        logging.error(f"Error in data loading or processing: {e}")

    # Visualizations with Bokeh:
    try:
        dataset = MoviesDatasetAnalyzer(
            r'C:\Users\ivsve\Desktop\adastra_task\the-movies-dataset\csv_files\movies_metadata.csv')
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
        div_num_unique_movies = bokeh_visuals.display_number_of_unique_movies(num_unique_movies)
        div_average_rating = bokeh_visuals.display_average_rating(average_rating)
        p5 = bokeh_visuals.plot_top_movies_without_vote_filter(top_movies_without_vote_filter)
        p1 = bokeh_visuals.plot_top_movies(top_movies)
        p2 = bokeh_visuals.plot_movies_per_year(year_counts)
        p3 = bokeh_visuals.plot_genre_counts(genre_counts)
        p4 = bokeh_visuals.plot_top_movies_weighted(weighted_rating)

        # Combine plots and display
        show(column(div_num_unique_movies, div_average_rating, p1, p2, p3, p4, p5))

    except Exception as e:
        logging.error(f"Error in visualization: {e}")


if __name__ == '__main__':
    main()
