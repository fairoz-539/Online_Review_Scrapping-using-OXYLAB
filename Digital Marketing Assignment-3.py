import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pprint import pprint
import re

def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<[^>]*>', '', text)
    # Remove special characters and numbers
    text = re.sub(r'[^A-Za-z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Remove extra whitespace
    text = ' '.join(text.split())
    return text

def get_reviews_with_oxylabs(username, password, url):
    api_url = 'https://realtime.oxylabs.io/v1/queries'
    payload = {
        'source': 'universal',
        'url': url
    }
    response = requests.post(api_url, auth=(username, password), json=payload)
    if response.status_code == 200:
        data = response.json()
        html_content = data.get('results', [])[0].get('content', '')
        soup = BeautifulSoup(html_content, 'html.parser')
        review_elements = soup.find_all('div', itemprop='reviewBody')
        reviews = []
        for review_element in review_elements:
            likes_section = review_element.find('h3', class_='input-fields sub-heading', string='Likes')
            dislikes_section = review_element.find('h3', class_='input-fields sub-heading', string='Dislikes')
            likes = likes_section.find_next_sibling('p').get_text(strip=True) if likes_section else ""
            dislikes = dislikes_section.find_next_sibling('p').get_text(strip=True) if dislikes_section else ""
            likes = clean_text(likes)
            dislikes = clean_text(dislikes)
            reviews.append((likes, dislikes))
        return reviews
    else:
        print("Failed to retrieve reviews from Oxylabs API.")
        return []

def perform_sentiment_analysis(reviews):
    positive_reviews = []
    negative_reviews = []
    for likes, dislikes in reviews:
        # Perform sentiment analysis
        likes_analysis = TextBlob(likes)
        dislikes_analysis = TextBlob(dislikes)

        # Classify likes as positive reviews and dislikes as negative reviews
        if likes_analysis.sentiment.polarity >= 0:
            positive_reviews.append(likes)
        if dislikes_analysis.sentiment.polarity < 0:
            negative_reviews.append(dislikes)

    return positive_reviews, negative_reviews

def create_word_cloud(reviews, title):
    # Join all reviews into a single string
    text = ' '.join(reviews)
    # Create a WordCloud object
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    # Plot the WordCloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title(title)
    plt.axis('off')
    plt.show()

def main():
    # Ask the user for the URL
    url = input("Enter the URL to scrape reviews: ")

    # Oxylabs credentials
    username = 'Your_oxylab_user_name'
    password = 'Your_oxylab_password'

    # Get the reviews from the URL
    reviews = get_reviews_with_oxylabs(username, password, url)
    if not reviews:
        return

    # Perform sentiment analysis
    positive_reviews, negative_reviews = perform_sentiment_analysis(reviews)

    # Create word clouds
    create_word_cloud(positive_reviews, 'Positive Reviews Word Cloud')
    create_word_cloud(negative_reviews, 'Negative Reviews Word Cloud')

if __name__ == "__main__":
    main()
