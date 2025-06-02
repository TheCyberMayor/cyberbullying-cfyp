
# Objective 1: Dataset Preprocessing for Cyberbullying Detection

## 📁 Dataset Information
- **Rows:** 8,799
- **Columns:** `index`, `oh_label`, `Date`, `Text`
- `oh_label`: Target label (0 = non-bullying, 1 = bullying)
- `Text`: User-generated text content to classify

## 🧹 Preprocessing Workflow
The following steps were applied to clean and prepare the text:

1. Remove hexadecimal (`\x`) and Unicode (`\u`) escape sequences.
2. Strip non-ASCII characters (e.g., emojis, accented letters).
3. Convert text to lowercase.
4. Remove punctuation.
5. Remove common English stopwords.
6. Retain only meaningful words for model training.

## 🏷️ Labeling
- `oh_label`:
  - `0` = Non-cyberbullying
  - `1` = Cyberbullying

## 🐍 Python Code Used

```python
import pandas as pd
import re
import string

# Load the dataset
df = pd.read_csv("4258172b-f37c-4edc-b97b-bea85b0aa7e5.csv")

# Define a built-in list of common English stopwords as a fallback
stopwords = {
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'but', 'by', 'for',
    'if', 'in', 'into', 'is', 'it', 'no', 'not', 'of', 'on', 'or',
    'such', 'that', 'the', 'their', 'then', 'there', 'these', 'they',
    'this', 'to', 'was', 'will', 'with', 'you', 'your', 'i', 'me',
    'my', 'we', 'our', 'he', 'she', 'him', 'her', 'his', 'its', 'from'
}

# Define the cleaning function
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

# Apply the cleaning function to the text column
df['clean_text'] = df['Text'].astype(str).apply(clean_text)

# Save the cleaned DataFrame
df.to_csv("cleaned_cyberbullying_dataset.csv", index=False)
```

---

## ✅ Output
- Cleaned dataset: `cleaned_cyberbullying_dataset.csv` (includes new column `clean_text`)
- Ready for use in traditional ML, deep learning, and transformer models
