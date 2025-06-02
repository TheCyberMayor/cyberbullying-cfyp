
import pandas as pd
import re
import string

# Load the dataset
df = pd.read_csv("4258172b-f37c-4edc-b97b-bea85b0aa7e5.csv")

# Define a built-in list of common English stopwords
stopwords = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for',
    'if', 'in', 'into', 'is', 'it', 'no', 'not', 'of', 'on', 'or',
    'such', 'that', 'the', 'their', 'then', 'there', 'these', 'they',
    'this', 'to', 'was', 'will', 'with', 'you', 'your', 'i', 'me',
    'my', 'we', 'our', 'he', 'she', 'him', 'her', 'his', 'its', 'from'
}

# Define the text cleaning function
def clean_text(text):
    text = re.sub(r'\x[0-9A-Fa-f]+', ' ', text)
    text = re.sub(r'\u[0-9A-Fa-f]+', ' ', text)
    text = text.encode('ascii', 'ignore').decode('utf-8')
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    tokens = [word for word in tokens if word not in stopwords]
    return ' '.join(tokens)

# Apply the cleaning function to the Text column
df['clean_text'] = df['Text'].astype(str).apply(clean_text)

# Save the cleaned dataset
df.to_csv("cleaned_cyberbullying_dataset.csv", index=False)
