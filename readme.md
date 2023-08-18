[TOC]

## Movies Database Analysis

1. **Basic Statistics and Sorting**:
   - The dataset is loaded, and basic statistics like the mean, standard deviation, and various percentiles of the `vote_count` are calculated.
   - Movies are initially sorted based on their average rating (`vote_average`). However, this approach can be misleading as movies with a perfect rating but very few votes (e.g., 1 vote) can end up at the top.
   - To address this, movies are then sorted by `vote_average` but only considering those with a vote count greater than 400, thus filtering out movies with very few votes.

2. **Score using Min-Max Scaling**:
   - The `vote_count` for each movie is scaled to a range of 1 to 10 using Min-Max scaling.
   - A new score called `average_count_score` is calculated by multiplying the `vote_average` with the scaled `vote_count_score`.
   - Movies are then ranked based on this new score, which gives importance to both the average rating and the number of votes a movie has received.

3. **Weighted Rating**:
   - A formula is introduced to calculate a weighted rating. The idea is to give more weight to movies with more votes.
   - The formula uses a threshold \( M \) (chosen to be 2500 in this case) to decide how much weight to give to the actual average rating of the movie versus the average rating of all movies.
   - Movies are then ranked based on this weighted rating.

4. **Bayesian Average Rating**:
   - There is also another rather complicated approach to solve this, called Bayesian Average Rating. It uses formulas to do the calculation.
   - Another approach introduced is the Bayesian Average Rating. This technique is often used when the number of votes varies widely among items (movies, in this case).
   - Instead of using just the average, this method considers the distribution of votes. The confidence level is set at 95%.
   - Movies are then ranked based on this Bayesian average score.

### Observations:
- The simple sorting based on average ratings can be misleading as movies with very few but high ratings can be at the top.
- Using a weighted rating or Bayesian average rating can provide a more balanced ranking as they consider both the rating and the number of votes.
- Min-Max scaling of the vote count and then multiplying it with the average rating is a simpler approach but may not be as robust as the Bayesian method, especially when the number of votes varies widely among movies.

In summary, while each method has its merits, the choice of method would depend on the specific use case, the nature of the data, and the desired outcome.

## Sources

1. [Measurement Problems - IMDB Application](https://www.kaggle.com/code/serdargundogdu/measurement-problems-imdb-application/notebook)
2. [Dataset Source Link](https://www.kaggle.com/rounakbanik/the-movies-dataset)
