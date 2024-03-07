import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Get best_math_schools (The best math results are at least 80% of the *maximum possible score of 800* for math.)
best_math_schools = schools[(schools['average_math'] / 800) >= 0.8][['school_name','average_math']].sort_values(by='average_math',ascending=False)
print(best_math_schools)

# Get top 10 performing schools based on the combined SAT scores
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
top_10_schools = schools[['school_name','total_SAT']].sort_values(by='total_SAT',ascending=False).head(10)
print(top_10_schools)

# Which single borough has the largest standard deviation in the combined SAT score?

# Save your results as a pandas DataFrame called largest_std_dev.
# The DataFrame should contain one row, with
# "borough" - the name of the NYC borough with the largest standard deviation of "total_SAT".
# "num_schools" - the number of schools in the borough.
# "average_SAT" - the mean of "total_SAT".
# "std_SAT" - the standard deviation of "total_SAT".
# Round all numeric values to two decimal places.

boroughs = schools.groupby('borough')['total_SAT'].agg(['count','mean','std']).round(2)
boroughs.rename(columns = {"count":"num_schools","mean":"average_SAT","std":"std_SAT"}, inplace=True)
boroughs.reset_index(inplace=True)

largest_std_dev = boroughs[boroughs['std_SAT'] == boroughs['std_SAT'].max()]
print(largest_std_dev)