import nltk

input_string = "This is a sample input for tokenization in python."

# Ensure the necessary NLTK data is downloaded
nltk.download('punkt')

# Tokenize the input string into words
words = nltk.word_tokenize(input_string)

# Print the tokenized words
print(words)