import sys, string


def analyze(self):
    # Normalize String Case
    s = self
    s_low = s.lower()

    # Split the string into words
    words = []
    words = s_low.split()

    # Remove punctuation marks
    chars = list(string.punctuation)  # creates a list of all punctuation marks
    w_clean = []

    # for each word in list of words
    for word in words:
        # if the first or last character of the word is punctuation
        if (word[0] in chars) or (word[len(word) - 1] in chars):
            # loop through list of punctuation and replace any found in word with blanks
            for char in chars:
                if (char in word):
                    updated_word = word.replace(char, "")
                    # add word to clean list
                    w_clean.append(updated_word)
        # if word has no punctuation, add it to clean list
        elif word[:len(word)] not in chars:
            w_clean.append(word)

    # count distinct words- key is that set can only contain unique values
    distinct_words = set()
    for word in w_clean:
        distinct_words.add(word)

    # define distinct words as a list
    distinct_list = []
    for word in distinct_words:
        distinct_list.append(word)

    # Compute word frequencies
    word_freq = dict()
    for word in w_clean:
        if word not in word_freq.keys():
            word_freq[word] = 1
        else:
            word_freq[word] += 1

    # return something
    return word_freq, distinct_list

if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None

    return_val = analyze(arg)
