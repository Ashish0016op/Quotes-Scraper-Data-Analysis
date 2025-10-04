import streamlit as st
import pandas as pd

st.title("Quotes Data Analysis & SQL Insights")

# Load data
df = pd.read_csv("cleaned_data.csv")
st.header("Data Overview")
st.dataframe(df.head())
st.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

if 'author' in df.columns:
    st.subheader("Top Authors by Number of Quotes")
    st.bar_chart(df['author'].value_counts().head(10))

# Show SQL Insights file as code
st.header("SQL Insights")
with open("SQL_Insights.sql", "r") as sqlfile:
    sql_code = sqlfile.read()
st.code(sql_code, language="sql")

st.subheader("Try Your Own SQL Query (on cleaned_data.csv)")
try:
    import pandasql
    user_query = st.text_area("Enter SQL query (use table name 'df')", "SELECT * FROM df LIMIT 5;")
    if st.button("Run SQL Query"):
        res = pandasql.sqldf(user_query, {"df": df})
        st.dataframe(res)
except ImportError:
    st.info("Install pandasql to enable interactive SQL querying: pip install pandasql")

st.write("---")
st.caption("Project by Ashish Kumar")