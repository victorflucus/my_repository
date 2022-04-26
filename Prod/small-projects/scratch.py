# This script starts with a paragraph of text and ends up with a frequency count of the distinct words in that text.
# It includes the following steps:
#    Convert a string to lowercase characters.
#    Split the lowercase string into individual words.
#    Count the number of words in the lowercase string.
#    Determine the number of distinct words in the lowercase string.
#    Calculate the number of times each word appears in the lowercase string.
#    Remove the punctuation from the lowercase string.
#    Perform a count analysis on the text without punctuation characters.


# Define string to work with
s = """Imagine a vast sheet of paper on which straight Lines, Triangles, Squares, Pentagons, Hexagons, and other figures,  
instead of remaining fixed in their places, move freely about, on or in the surface, but without the power of rising above \
or sinking below it, very much like shadows - only hard and with luminous edges - and you will then have a pretty correct \
notion of my country and countrymen. Alas, a few years ago, I should have said "my universe": but now my mind has been \
opened to higher views of things."""

# Normalize String Case
s_low = s.lower()

# Split the string into words
words = []
words = s_low.split()

# Count the words
word_count = len(words)

# Remove punctiation marks

import string  # import string module

chars = list(string.punctuation)  # use string.punctuation built in python to creat a list of all punctuations
w_clean = []

# for each word in list of words
for word in words:
    # if the first or last character of the word is punctuation
    if (word[0] in chars) or (word[len(word) - 1] in chars):
        # loop through list of punctuation and replace any found in word with blaks
        for char in chars:
            updated_word = word.replace(char, "")
        # add word to clean list
        w_clean.append(updated_word)
    # if word has no punctuation, add it to clean list
    elif word[:len(word)] not in chars:
        w_clean.append(word)

# count words without punctuation
num_clean_words = len(w_clean)

# count distinct words- key is that set can only contain unique values
distinct_words = set()
for word in words:
    distinct_words.add(word)

# define distinct words as a list
distinct_list = []
for word in distinct_words:
    distinct_list.append(word)

# Compute word frequencties
#   this code illustrates this as a dictionary consiting of keys that are
#   all of the distinct words in the list. Key values represent the number of time the e word(key )
#   is found in the string

word_freq = dict()

for word in words:
    if word not in word_freq.keys():
        word_freq[word] = 1
    else:
        word_freq[word] += 1

print(word_freq)
print(distinct_list)