import streamlit as st

st.title("Sentiment Analyzer")

# Sidebar inputs
name = st.sidebar.text_input("What's your name?", "Anonymous")
message = st.sidebar.text_area("Tell me what you feel today:")

# Define lists of positive and negative words
positive_words = ['good', 'excited', 'happy', 'great', 'fantastic', 'wonderful']
negative_words = ['bad', 'sad', 'angry', 'terrible', 'awful', 'miserable']

# Function to classify the sentiment and display a message
def classify_sentiment(message):
    st.write(f"Hi, {name}!")
    words = message.lower().split()
    if any(word in positive_words for word in words):
        st.write("That's good! :smile:")
    elif any(word in negative_words for word in words):
        st.write("I hope you feel better soon. :disappointed:")
    else:
        st.write("Keep going! :neutral_face:")

# Display results when button is clicked
if st.sidebar.button('Say it'):
    classify_sentiment(message)

# Notes and instructions
st.sidebar.markdown("---")
st.sidebar.markdown("### Notes")
st.sidebar.markdown("Before running the app, install Streamlit using: `pip install streamlit`")
st.sidebar.markdown("To run the app, use the following command in the terminal:")
st.sidebar.code("streamlit run streamlit_test.py")
