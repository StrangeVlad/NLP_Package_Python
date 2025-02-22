# My NLP Package

## 📖 Description

A simple NLP package for text preprocessing in Python. It includes:

- Sentence Splitting
- Word Splitting
- Stopword Removal
- Special Character & Punctuation Removal
- N-Grams
- Word Counting
- Bag of Words Model

---

## 🚀 Installation

Clone the repository:

```sh
git clone https://github.com/StrangeVlad/NLP_Package_Python.git
cd my_nlp_package
```

Then install it using:

```sh
pip install -e .
```

## ⚡ Usage

Importing the package

```sh
from my_nlp.preprocessing import splitSentence, removeStopWords

text = "I love coding! NLP is awesome."
sentences = splitSentence(text, ['!', '.'])
print(sentences)  # ['I love coding', 'NLP is awesome']

words = ["I", "love", "coding"]
filtered_words = removeStopWords(words, ["I"])
print(filtered_words)  # ['love', 'coding']
```

## 🛠 Features

### 1️⃣ Split Sentence

```sh
splitSentence("Hello world. Python is fun!", ["."])
# Output: ['Hello world', 'Python is fun!']
```

### 2️⃣ Split Words

```sh
splitWords(["Hello world"])
# Output: ['Hello', 'world']
```

### 3️⃣ Remove Stopwords

```sh
removeStopWords(["I", "love", "coding"], ["I"])
# Output: ['love', 'coding']
```

### 4️⃣ Remove Special Characters

```sh
removeSpecialCharactersPunctuation(["lo$$ve", "code!", "play????ing"], ["$", "!", "?"])
# Output: ['love', 'code', 'playing']
```

### 5️⃣ Generate N-Grams

```sh
nGrams(["love", "coding", "NLP"], 2)
# Output: [('love', 'coding'), ('coding', 'NLP')]
```

### 6️⃣ Word Counting

```sh
wordCounting(["love", "coding", "love"])
# Output: {'love': 2, 'coding': 1}
```

### 7️⃣ Bag of Words

```sh
bagOfWords([["I", "love", "coding"], ["coding", "is", "fun"]])
# Output: Vocabulary: ['I', 'coding', 'fun', 'is', 'love']
```

# Bag of Words Matrix:

- [1, 1, 0, 0, 1]

- [0, 1, 1, 1, 0]

## 📜 License

This project is licensed under the MIT License.

## 🤝 Contributing

Feel free to contribute by submitting pull requests or opening issues.

## 📩 Contact

## For any questions or feedback, contact me at your.email@example.com.

### **🚀 Next Steps**

1. **Update `Zagane Mohammed Mounir` and `mounir.zagane@example.com`** with your actual info.
2. **Upload to GitHub**:
   ```sh
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```
