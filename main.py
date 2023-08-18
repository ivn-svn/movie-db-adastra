from movies_dataset import MoviesDatasetAnalyzer

def modified_main():
    """The modified main function."""
    dataset = MoviesDatasetAnalyzer(r'C:\Users\ivsve\Desktop\adastra_task\the-movies-dataset\csv_files\movies_metadata.csv')
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
        print(f"Title: {row['title']}, Rating: {row['vote_average']:.1f} ({row['collection_name'] if row['collection_name'] else 'No Collection'})")
    print()
    # Top 5 highest rated movies
    print('Top 5 highest rated movies:')
    top_movies = dataset.get_top_5_highest_rated_movies()
    for index, row in top_movies.iterrows():
        print(f"Title: {row['title']}, Rating: {row['vote_average']:.1f} ({row['collection_name'] if row['collection_name'] else 'No Collection'})")
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
modified_main()
