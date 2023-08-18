import unittest
from unittest.mock import patch
from io import StringIO
from movies_dataset import MoviesDatasetAnalyzer
import pandas as pd

SAMPLE_DATA = """id,belongs_to_collection,release_date,title,genres,vote_average,vote_count
1,"{'id': 1, 'name': 'Collection A'}",2022-01-01,Movie A,"[{'id': 1, 'name': 'Action'}]",8.5,100
2,,2022-01-02,Movie B,"[{'id': 2, 'name': 'Comedy'}]",7.5,50
3,"{'id': 1, 'name': 'Collection A'}",2022-01-03,Movie C,"[{'id': 1, 'name': 'Action'}, {'id': 2, 'name': 'Comedy'}]",9.0,60
"""

class TestMoviesDatasetAnalyzer(unittest.TestCase):

    def setUp(self):
        # Mocking the data loading process to use our sample data
        self.analyzer = MoviesDatasetAnalyzer('dummy_filename.csv')
        with patch('pandas.read_csv', return_value=pd.read_csv(StringIO(SAMPLE_DATA), low_memory=False)):
            self.analyzer.load_data()

    def test_get_number_of_unique_movies(self):
        self.assertEqual(self.analyzer.get_number_of_unique_movies(), 3)

    def test_get_average_rating(self):
        self.assertAlmostEqual(self.analyzer.get_average_rating(), 8.33, 2)

    def test_get_top_5_highest_rated_movies_without_vote_filter(self):
        top_movies = self.analyzer.get_top_5_highest_rated_movies_without_vote_filter()
        self.assertEqual(len(top_movies), 3)
        self.assertEqual(top_movies.iloc[0]['title'], 'Movie C')

    def test_get_top_5_highest_rated_movies(self):
        top_movies = self.analyzer.get_top_5_highest_rated_movies()
        self.assertEqual(len(top_movies), 2)
        self.assertEqual(top_movies.iloc[0]['title'], 'Movie C')


if __name__ == '__main__':
    unittest.main()
