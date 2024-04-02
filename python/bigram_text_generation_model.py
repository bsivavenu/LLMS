import random
import re
# # import random

# # Sample text data
# text_data = "I like to eat apples and bananas. I prefer apples over bananas."

# # Function to generate bigrams from text data
# def generate_bigrams(text):
#     words = text.split()
#     bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
#     return bigrams

# # Function to build bigram model
# def build_bigram_model(text):
#     bigrams = generate_bigrams(text)
#     model = {}
#     for word1, word2 in bigrams:
#         if word1 in model:
#             model[word1].append(word2)
#         else:
#             model[word1] = [word2]
#     return model

# # Function to generate text using bigram model
# def generate_text(model, start_word, length=10):
#     current_word = start_word
#     generated_text = [current_word]
#     for _ in range(length):
#         if current_word in model:
#             next_word = random.choice(model[current_word])
#             generated_text.append(next_word)
#             current_word = next_word
#         else:
#             break
#     return ' '.join(generated_text)

# # Build bigram model
# bigram_model = build_bigram_model(text_data)

# # Generate text using the bigram model
# generated_text = generate_text(bigram_model, 'I', length=10)
# print("Generated Text:", generated_text)

# .....................................................................

import random
import re
# Sample text data

text_data = open('../sivaolddata/0.txt','r').read()

# Function for data preprocessing
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation (except periods to retain sentence boundaries)
    text = re.sub(r'[^\w\s.]', '', text)
    return text

# Function to generate ngrams from text data
def generate_ngrams(text, n):
    words = text.split()
    ngrams = [tuple(words[i:i+n]) for i in range(len(words)-n+1)]
    return ngrams

# Function to build ngram model
def build_ngram_model(text, n):
    ngrams = generate_ngrams(text, n)
    model = {}
    for gram in ngrams:
        prefix = gram[:-1]
        suffix = gram[-1]
        if prefix in model:
            model[prefix].append(suffix)
        else:
            model[prefix] = [suffix]
    return model

# Function to generate text using ngram model
def generate_text(model, start_prefix, length=100):
    current_prefix = start_prefix
    generated_text = list(current_prefix)
    for _ in range(length):
        if current_prefix in model:
            next_word = random.choice(model[current_prefix])
            generated_text.append(next_word)
            current_prefix = tuple(list(current_prefix[1:]) + [next_word])  # Update current prefix
        else:
            break
    return ' '.join(generated_text)

# Function to find a suitable starting prefix
def find_starting_prefix(model, text):
    # Get all prefixes present in the model
    all_prefixes = list(model.keys())
    # Shuffle the prefixes to avoid bias
    random.shuffle(all_prefixes)
    # Iterate through shuffled prefixes to find a suitable one
    for prefix in all_prefixes:
        if ' '.join(prefix) in text:
            return prefix
    # If no suitable prefix found, return None
    return None


# Preprocess text data
preprocessed_text_data = preprocess_text(text_data)

# Build ngram model
n = 3  # Change n to experiment with different n-grams
ngram_model = build_ngram_model(preprocessed_text_data, n)

# Find a suitable starting prefix
starting_prefix = find_starting_prefix(ngram_model, preprocessed_text_data)
print(starting_prefix)

if starting_prefix:
    # Generate text using the ngram model
    generated_text = generate_text(ngram_model, ('rag','is'))
    print("Generated Text:", generated_text)
else:
    print("No suitable starting prefix found in the text data.")
