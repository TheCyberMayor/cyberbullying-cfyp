# Define a built-in list of common English stopwords as a fallback
built_in_stopwords = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for',
    'if', 'in', 'into', 'is', 'it', 'no', 'not', 'of', 'on', 'or',
    'such', 'that', 'the', 'their', 'then', 'there', 'these', 'they',
    'this', 'to', 'was', 'will', 'with', 'you', 'your', 'i', 'me',
    'my', 'we', 'our', 'he', 'she', 'him', 'her', 'his', 'its', 'from'
}

# Redefine the cleaning function using built-in stopwords
def clean_text_fallback(text):
    text = re.sub(r'\\x[0-9A-Fa-f]+', ' ', text)
    text = re.sub(r'\\u[0-9A-Fa-f]+', ' ', text)
    text = text.encode('ascii', 'ignore').decode('utf-8')
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    tokens = [word for word in tokens if word not in built_in_stopwords]
    return ' '.join(tokens)

# Apply fallback cleaning
df['clean_text'] = df['Text'].astype(str).apply(clean_text_fallback)

# Show a few cleaned samples
df[['Text', 'clean_text']].head(10)
