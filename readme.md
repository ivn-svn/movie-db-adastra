[TOC]

# Data Analysis on Kaggle.com Movie Datasets

The purpose of this repo is to provide a script doing the following on a Kaggle dataset:
   - Use the Kaggle Movie Database
   - Reads a CSV dataset.
   - Loads data with pandas.
   - Performs operations on the DataFrame.
   - Saves the final DataFrame as JSON.
   - Visualizes the results with a Python library called Bokeh
   - When the script has finished its work, you will be redirected to a local HTML file with the visualizations.

### The story behind Kaggle and the datasets
Kaggle is an online community platform for data scientists and machine learning enthusiasts, est. 2010, acquired by Google in 2017. Kaggle allows users to collaborate with other users, find and publish datasets, use GPU integrated notebooks, and compete with other data scientists to solve data science challenges.

## Folder Structure
<br>
This repository locally (on your side) after cloned and after the code has been run, has the following file & folder structure: 
<br>
<br>

📂 `.idea` - My .idea folder of my project.
│
├── 📄 `.gitignore`

├── 📄 `misc.xml`
│
├── 📄 `modules.xml`
│
├── 📄 `movie-db-adastra.iml`
│
├── 📄 `vcs.xml`
│
└── 📄 `workspace.xml`

📄 `bokeh_visuals.py` - This is the library (Bokeh), which I used to draw the results in HTML files.

📂 `dist`
│
└── 📄 `MoviesAnalyzer-0.1.0.tar.gz`

📄 `folder_structure.py` - I used it to get a JSON from which I derive the folder structure you read now.

📄 `main.py` - the main file containing the class instantiation and function calls.

📂 `MoviesAnalyzer.egg-info` - This is part of the package. 
│
├── 📄 `dependency_links.txt`
│
├── 📄 `PKG-INFO`
│
├── 📄 `requires.txt`
│
├── 📄 `SOURCES.txt`
│
└── 📄 `top_level.txt`

📄 `movies_dataset.json` 

📄 `movies_dataset.py` - The most important script containing the class `MoviesDatasetAnalyzer` 

📄 `movies_visualization.html` - The file you get once you run the main.py.

📄 `readme.md` - The document you are now reading.

📄 `requirements.txt` - The requirements.

📄 `setup.py` - The requested setup.py file. 

📄 `tests.py` - Basic unittests with dummy data. 

📄 `__init__.py`
<br>
<br>

There are several approaches to visualizing the contents of the [Kaggle dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset).
Because the standard statistics coming from the main CSV file show 5 rather less popular movies, I decided to educate myself on the topic and found a useful thread on the Kaggle forums which I have linked in the sources here. It elaborates on several different statistical methods. You will find a short summary below. 


## Movies Database Analysis: Possible Methods for the Analysis
<br>

1. **Basic Statistics and Sorting**:
   - The dataset is loaded, and basic statistics like the mean, standard deviation, and various percentiles of the `vote_count` are calculated.
   - Movies are initially sorted based on their average rating (`vote_average`). However, this approach can be misleading as movies with a perfect rating but very few votes (e.g., 1 vote) can end up at the top.
   - To address this, movies are then sorted by `vote_average` but only considering those with a vote count greater than 400, thus filtering out movies with very few votes.
<br>

2. **Score using Min-Max Scaling**:
   - The `vote_count` for each movie is scaled to a range of 1 to 10 using Min-Max scaling.
   - A new score called `average_count_score` is calculated by multiplying the `vote_average` with the scaled `vote_count_score`.
   - Movies are then ranked based on this new score, which gives importance to both the average rating and the number of votes a movie has received.
<br>

3. **Weighted Rating**:
   - A formula is introduced to calculate a weighted rating. The idea is to give more weight to movies with more votes.
   - The formula uses a threshold \( M \) (chosen to be 2500 in this case) to decide how much weight to give to the actual average rating of the movie versus the average rating of all movies.
   - Movies are then ranked based on this weighted rating.
<br>

4. **Bayesian Average Rating**:
   - There is also another rather complicated approach to solve this, called Bayesian Average Rating. It uses formulas to do the calculation. This technique is often used when the number of votes varies widely among items (movies, in this case).
   - Instead of using just the average, this method considers the distribution of votes. The confidence level is set at 95%.
   - Movies are then ranked based on this Bayesian average score.

### Observations:
- The simple sorting based on average ratings can be misleading as movies with very few but high ratings can be at the top.
- Using a weighted rating or Bayesian average rating can provide a more balanced ranking as they consider both the rating and the number of votes.
- Min-Max scaling of the vote count and then multiplying it with the average rating is a simpler approach but may not be as robust as the Bayesian method, especially when the number of votes varies widely among movies.

In summary, while each method has its merits, the choice of method would depend on the specific use case, the nature of the data, and the desired outcome. For this reason, I have used all methods except the Bayesian in my script. 

## Sources

1. [Measurement Problems - IMDB Application](https://www.kaggle.com/code/serdargundogdu/measurement-problems-imdb-application/notebook)
2. [Dataset Source Link](https://www.kaggle.com/rounakbanik/the-movies-dataset)
