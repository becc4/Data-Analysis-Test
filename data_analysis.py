"""
What is the difference between the imdb score and the meta rating?
Rating/score ratios compared to eachother

What are the trends in genre over the years?
Genres of top movies compared to Released_Year
"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("imdb_top_1000.csv", usecols= ["Series_Title", "Released_Year", "Genre", "IMDB_Rating", "Meta_score", "Gross"])

#print(df.tail())

#print(df.describe())
print(df.info())

# Counting how many movies were given 100 ratings, to later compare to Gross (if I can ever figure Gross out, since it's an object)
#print(df["Meta_score"].value_counts())  # 63
#print(df["IMDB_Rating"].value_counts()) # 17, this is too low for a graph

#print(df[["Meta_score", "IMDB_Rating"]].nunique())

""" Check for Null """
# 63 are null
null_Meta = df["Meta_score"].isnull()
#print("Null Meta", df["Meta_score"].isnull().sum())

# IMDB no null
#print("Null IMDB", df["IMDB_Rating"].isnull().sum())

# 169 are null
#print("Null Gross", df["Gross"].isnull().sum())

# Delete Null Gross
new_list = df.dropna(axis=0, inplace=True)   # Hold on, does this drop all nulls?
#print(df.head())

df.sort_values("Gross", ascending = True, inplace = True)
#print(df.head(50))

""" Plot the Graph """
plt.close("all")

meta = df["Meta_score"]
imdb = df["IMDB_Rating"]
#gross = df.sort_values("Gross", ascending = True)
gross = df["Gross"]
#print(gross)
#print("GROSS\n", df.sort_values("Gross", ascending = False)["Gross"])

#plt.scatter(gross, meta, color = 'blue')
plt.scatter(meta, imdb, color = 'red') # I like this one better, more clear line and less busy
plt.xlabel('Meta', color = 'black')
plt.ylabel('IMDB', color = 'black')
plt.title("Relationship between the ratings and gross of a movie")
#plt.show()

""" Second question """
genres = df["Genre"].value_counts()
genres = genres.head() # Top 5 genres

#print(genres)

# With this, I already know how popular every year was (recent years have more top movies)
df.sort_values("Released_Year", ascending = True, inplace = True)
#print(df)

# I only want genre.head() so I'm gonna have to cut any rows that don't fit that
# ["Drama", "Comedy, Drama", "Drama, Romance", "Crime, Drama, Thriller", "Crime, Drama"]
drama = df[df["Genre"] == "Drama"]
comdram = df[df["Genre"] == "Comedy, Drama"]
dramrom = df[df["Genre"] == "Drama, Romance"]
crimdramthrill = df[df["Genre"] == "Crime, Drama, Thriller"]
crimdram = df[df["Genre"] == "Crime, Drama"]

""" Graph it """
plt.scatter(df["Released_Year"], df["Meta_score"], color = "white") # Used so there's a common X-axis

#plt.scatter(drama["Released_Year"], drama["Meta_score"], color = 'red')
#plt.scatter(comdram["Released_Year"], comdram["Meta_score"], color = 'black')
#plt.scatter(dramrom["Released_Year"], dramrom["Meta_score"], color = 'green')
#plt.scatter(crimdramthrill["Released_Year"], crimdramthrill["Meta_score"], color = 'blue')
#plt.scatter(crimdram["Released_Year"], crimdram["Meta_score"], color = 'purple')
#print(df.sort_values("Meta_score").head(20))

plt.xlabel('Years')
plt.ylabel('Meta score Rating')
plt.title("Relationship between the years and score of a movie by genre")
plt.show()