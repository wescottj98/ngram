ngram = {}
def addWord(word):
    wordStr = " "
    # turn array of strings passed in parameter "word" into a single string
    wordStr = wordStr.join(word)
    # add words or increment value if they exist already
    if wordStr in ngram:
        ngram[wordStr] = ngram[wordStr]+1
    else:
        ngram[wordStr] = 1

wSpace = {}
def sortSpace(string):
    spaces = 0
    # count number of spaces between words to sort by m-value
    for i in range(0, len(string)):
        if string[i]==' ':
            spaces = spaces + 1
    # sort by m-value
    if str(spaces) in wSpace:
        wSpace[str(spaces)].append(string)
    else:
        wSpace[str(spaces)] = [string]

# optional code for removing stop words
rmStopWords = []
stopWords = ["a","is","the"]
def removeStopWords(word):
    if not word in stopWords:
        rmStopWords.append(word)


# parameters
# text = "a good puzzle is a fun puzzle"
text = open('data.txt', 'r').read()
m = 2
removeStopWordsFromText = False

# n refers to number of words in text for calculating complexity
# complexity is ~ < 2n*m + 2n
# O complexity is Linear O(n) (assuming n>m)

words = text.split()
cnt = 1

for word in words:
    removeStopWords(word)

if removeStopWordsFromText:
    words = rmStopWords

# n*m complexity

# go through text and sort each word into a dictionary where
# the word is the key and the value is the number of times that word appears

# the operation stated above takes place m times
while cnt < m+1:
    for i in range(0, len(words)):
        # condition prevents out of bounds condition and extra counting of the
        # last word
        if not i+cnt > len(words):
            addWord(words[i:i+cnt])
    cnt = cnt + 1

# information about ngrams is collected, still needs to be organized to 
# fit the specifications for output
ngrams = []

# < n complexity
for key, value in ngram.items():
    ngrams.append(key+ " " +str(value))

# < n complexity
for string in ngrams:
    sortSpace(string)

# < n*m complexity
for key, value in wSpace.items():
    v = sorted(value)
    for i in v:
        print(i)
