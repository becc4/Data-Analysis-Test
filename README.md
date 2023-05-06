# Data Analysis of Movies
## Overview

I was learning about Data Analysis with this project. I initially didn't create a series of questions because I didn't know what would be reasonable and I also had to change the database I used because the original was too large. However, in this prokect, I learned how to count, sort, describe, and plot amongst other things.

My software intakes a file on top rated movies ([imdb top 1000](imdb_top_1000.csv)) and organizes it into useful information (removes nulls), imdb rating score, release year, and genre (remove irrelevent genres).
Because there were so many featured genres, I used the top 5.
The y-axis always goes smallest to largest, even if the numbers are unclear in the graphics.

Questions I wanted to answer:
- What is the difference between imdb scores and meta ratings? - Compare imdb scores and meta ratings
- What are the trends in genre over the years? - Genres of top movies compared to Released_Year and ratings

[Software Demo Video](https://youtu.be/C9b4ndxKXyc)

## Development Environment

I used VSCode and wrote the program in python. I imported pandas and matplotlib to analize the data and then present it.

## Useful Websites

{Make a list of websites that you found helpful in this project}
* [pandas.pydata](https://pandas.pydata.org/docs/user_guide/10min.html#min)
* [Medium](https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77)
* [IMDB Movies Dataset] (https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)
* [pandas.pydata](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html)
* [Real Python](https://realpython.com/pandas-plot-python/)
* [pandas.pydata](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)
* [datapine](https://www.datapine.com/documentation/null-values/)