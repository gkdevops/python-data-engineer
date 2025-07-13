import streamlit as st
import pandas as pd

# Sample data as a Python dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 35],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
}

# Convert the dictionary to a Pandas DataFrame
df = pd.DataFrame(data)

# Set the title of the Streamlit app
st.title('Simple Streamlit App with Sample Data')

# Display the DataFrame
st.subheader('Here is the sample data:')
st.dataframe(df)

# You can add more interactive elements here if you like
st.subheader('Let\'s explore the data a bit more:')

# Show the average age
average_age = df['Age'].mean()
st.write(f'The average age is: {average_age:.2f}')

# Show the unique cities
unique_cities = df['City'].unique()
st.write('The unique cities are:', unique_cities)
