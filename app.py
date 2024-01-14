import streamlit as st 
import base64
import SentimentAnalysisFlipkart

def add_bg(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: wide
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

def main():
    st.set_page_config(page_title="FLIPKART",page_icon=":tada:",layout="wide")
    st.title("Sentimental Analysis of Products")
    add_bg('C:/Users/naiva/OneDrive/Desktop/project5/hehe.jpg')
    
    url = st.text_input("Enter the URL:")
    
    if st.button("Analyze"):
        data = SentimentAnalysisFlipkart.webScrapingReviews(url)
        SentimentAnalysisFlipkart.sentimentAnalysis(data)
        st.markdown(
            '<div style="background-color: #FFD700; padding: 10px; border-radius: 10px;">'
            '<h3 style="color: black; text-align: center;">Here is the overall analysis:</h3>'
            '</div>',
            unsafe_allow_html=True
        )
        SentimentAnalysisFlipkart.visualization()

    

   
if __name__=='__main__':
    main()
# streamlit run app.py