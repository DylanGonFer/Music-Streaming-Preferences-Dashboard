import pandas as pd # type: ignore
from pandasql import sqldf # type: ignore


#Top Genre By Country
df = pd.read_csv("clean_dataset.csv")
query = """
SELECT Country, "Top Genre", MAX(genre_count) AS max_genre_count FROM (
    SELECT Country, "Top Genre", COUNT(*) AS genre_count FROM df
    GROUP BY Country, "Top Genre"
) AS subquery GROUP BY Country
"""
sqldf(query, locals()).to_csv("top_genre_by_country.csv", index=False)  


#Top Genre By Platform
query = """
SELECT "Streaming Platform", "Top Genre", MAX(genre_count) AS max_genre_count FROM (
    SELECT "Streaming Platform", "Top Genre", COUNT(*) AS genre_count FROM df
    GROUP BY "Streaming Platform", "Top Genre"
) AS subquery GROUP BY "Streaming Platform"
"""
sqldf(query, locals()).to_csv("top_genre_by_platform.csv", index=False)  


#Top Genre By Age
query = """
SELECT Age, "Top Genre", MAX(genre_count) AS max_genre_count FROM (
    SELECT age, "Top Genre", COUNT(*) AS genre_count FROM df
    GROUP BY Age, "Top Genre"
) AS subquery GROUP BY Age
"""
sqldf(query, locals()).to_csv("top_genre_by_Age.csv", index=False)  
 

#Repeat Song Rate By Country
query = """
SELECT ROUND(AVG("Repeat Song Rate (%)"),2) AS avg_repeat, Country FROM df
GROUP BY Country
"""
sqldf(query, locals()).to_csv("repeat_song_rate_by_country.csv", index=False)  


#Repeat Song Rate All Over The World
query = """
SELECT AVG("Repeat Song Rate (%)") AS avg_repeat FROM df
"""
sqldf(query, locals()).to_csv("repeat_song_rate_all_over_the_world.csv", index=False)       


#Most Popular Artists By Country (Map)
query = """
SELECT Country, "Most Played Artist", MAX(artist_count) AS max_artist_count FROM (
    SELECT Country, "Most Played Artist", COUNT(*) AS artist_count FROM df
    GROUP BY Country, "Most Played Artist") AS subquery
GROUP BY Country
"""
sqldf(query, locals()).to_csv("most_popular_artists_by_country.csv", index=False)