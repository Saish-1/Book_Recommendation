import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Book Recommendation App")
st.markdown("-----")
st.header("Most Popular Books:")
Popular_books = joblib.load("Most_Popular_Books.pkl")
User_based = joblib.load("User_Based.pkl")
similarity_score = joblib.load("Similarity_scores.pkl")
Book_Titles = joblib.load("Book-Titles.pkl")
col1,col2,col3,col4 = st.columns(4)
with col1:
    st.image("https://images.amazon.com/images/P/0439139597.0",width=150,caption='Harry Potter and the Goblet of Fire (Book 4)')
    st.image("https://images.amazon.com/images/P/0345339703.0",width=150,caption='The Lord of the Rings, Part 1')
    st.image("https://images.amazon.com/images/P/0316666343.0",width=150,caption='The Lovely Bones')
    st.image("https://images.amazon.com/images/P/0312195516.0",width=150,caption='The Red Tent (Bestselling Backlist)')
    st.image("https://images.amazon.com/images/P/3257208626.0",width=150,caption="Fahrenheit 451")
with col2:
    st.image("https://images.amazon.com/images/P/0439136350.0",width=150,caption='Harry Potter and the Prisoner of Azkaban (Book 3)')
    st.image("https://images.amazon.com/images/P/0345339681.0",width=150,caption='The Hobbit')
    st.image("https://images.amazon.com/images/P/0451524934.0",width=150,caption="1984")
    st.image("https://images.amazon.com/images/P/0385484518.0",width=150,caption="Tuesdays with Morrie")
    st.image("https://images.amazon.com/images/P/0452282152.0",width=150,caption="Girl with a Pearl Earring")

with col3:
    st.image("https://images.amazon.com/images/P/043935806X.0",width=150,caption='Harry Potter and the Order of the Phoenix (Book 5)')
    st.image("https://images.amazon.com/images/P/0385504209.0",width=150,caption='The Da Vinci Code')
    st.image("https://images.amazon.com/images/P/0786868716.0",width=150,caption='The Five People You Meet in Heaven')
    st.image("https://images.amazon.com/images/P/0060392452.0",width=150,caption='Stupid White Men ')
    st.image("https://images.amazon.com/images/P/0805063897.0",width=150,caption='Nickel and Dimed')

with col4:
    st.image("https://images.amazon.com/images/P/0439064872.0",width=150,caption='Harry Potter and the Chamber of Secrets (Book 2)')
    st.image("https://images.amazon.com/images/P/0316769487.0",width=150,caption='The Catcher in the Rye')
    st.image("https://images.amazon.com/images/P/059035342X.0",width=150,caption="Harry Potter and the Sorcerer's Stone")
    st.image("https://images.amazon.com/images/P/0446310786.0",width=150,caption='To Kill a Mockingbird')
    st.image("https://images.amazon.com/images/P/0142001740.0",width=150,caption='The Secret Life of Bees')

with st.sidebar:
    st.header("Book Recommendation:")
    st.markdown("-----")
    st.subheader("Enter the name of the Book you have previously read:")
    BookName = st.selectbox("Enter Book Name",Book_Titles)
    def recommend(book_name):
        
        index = index = np.where(User_based.index == book_name)[0][0]
        similar_items = sorted(list(enumerate(similarity_score[index])),key = lambda x:x[1],reverse=True)[1:6]
        for i in similar_items:
            st.write(User_based.index[i[0]])

    recommend(BookName)