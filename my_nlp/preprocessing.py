def splitSentence(text, punct):
    sentences = []
    temp = ""
    for i in text:
        if i not in punct:
            temp = temp + i
        else:
            sentences.append(temp.strip())
            temp = ""
    sentences.append(temp.strip())
    return sentences


def splitWords(sentences):
    words = []
    for i in sentences:
        temp = ""
        for j in i:
            if j != " ":
                temp = temp + j
            else:
                if temp:
                    words.append(temp)
                    temp = ""
        if temp:
            words.append(temp)
    return words


def removeStopWords(words, stopWords):
    wordsFilter = []
    for word in words:
        if word not in stopWords:
            wordsFilter.append(word)
    return wordsFilter


def removeSpecialCharactersPunctuation(wordsFilter, symbols):
    wordsCleaned = []
    for word in wordsFilter:
        temp = ""
        for i in word:
            if i not in symbols:
                temp = temp + i
        if temp:
            wordsCleaned.append(temp)
    return wordsCleaned


def nGrams(wordsCleaned, n):
    ngramWords = []
    for i in range(len(wordsCleaned) - n + 1):
        ngramWord = tuple(wordsCleaned[i: i + n])
        ngramWords.append(ngramWord)
    return ngramWords


def wordCounting(wordsCleaned):
    wordCount = {}
    for word in wordsCleaned:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    return wordCount


def bagOfWords(sentences):
    wordsUnique = sorted(set(word for sentence in sentences for word in sentence))
    vocab_index = {word: i for i, word in enumerate(wordsUnique)}

    matrix = []
    for sentence in sentences:
        word_count = [0] * len(wordsUnique)
        for word in sentence:
            word_count[vocab_index[word]] += 1
        matrix.append(word_count)

    return wordsUnique, matrix
