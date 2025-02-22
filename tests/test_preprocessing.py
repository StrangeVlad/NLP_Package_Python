from my_nlp.preprocessing import (
    splitSentence, splitWords, removeStopWords,
    removeSpecialCharactersPunctuation, nGrams, wordCounting, bagOfWords
)

def test_splitSentence():
    text = "Hello world! How are you? I'm fine."
    result = splitSentence(text, ['!', '?', '.'])
    assert result == ["Hello world", "How are you", "I'm fine"]

def test_splitWords():
    sentences = ["Hello world", "How are you"]
    result = splitWords(sentences)
    assert result == ["Hello", "world", "How", "are", "you"]

def test_removeStopWords():
    words = ["I", "love", "coding"]
    stopwords = ["I"]
    assert removeStopWords(words, stopwords) == ["love", "coding"]

def test_removeSpecialCharactersPunctuation():
    words = ["hell@", "wo#rld", "co$ding"]
    symbols = ["@", "#", "$"]
    assert removeSpecialCharactersPunctuation(words, symbols) == ["hell", "world", "coding"]

def test_nGrams():
    words = ["I", "love", "coding"]
    assert nGrams(words, 2) == [("I", "love"), ("love", "coding")]

def test_wordCounting():
    words = ["apple", "banana", "apple"]
    assert wordCounting(words) == {"apple": 2, "banana": 1}

def test_bagOfWords():
    sentences = [["I", "love", "coding"], ["I", "love", "Python"]]
    vocab, matrix = bagOfWords(sentences)
    assert vocab == ["I", "Python", "coding", "love"]
    assert matrix == [[1, 0, 1, 1], [1, 1, 0, 1]]
