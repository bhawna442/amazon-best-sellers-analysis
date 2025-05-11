import pandas as pd 
df=pd.read_csv('bestsellers.csv')
# head -> first 5 rows
print(df.head())
# shape-> dimension of sheet
print(df.shape)
# columns-> tuple of column names
print(df.columns)
#summary of each col
print(df.describe)


# Data Cleaning!!!!

# remove duplicates inplace=True means changes are done to the original dataframe itself
df.drop_duplicates(inplace=True)

# renaming columns for convinience
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

#convert data type as necessary
df["Price"]=df["Price"].astype(float)

# Data Analysis !!!!

author_counts=df["Author"].value_counts()
print(author_counts)

# avg rating group by genre
avg_rating_by_genre= df.groupby("Genre").mean("Rating")
print(avg_rating_by_genre)

# avg rating group by genre
avg_rating_by_genre= df.groupby("Genre").mean("Rating")
print(avg_rating_by_genre)

author_counts.head(10).to_csv('top_authors.csv')
avg_rating_by_genre.to_csv('avg_rating_by_genre.csv')
