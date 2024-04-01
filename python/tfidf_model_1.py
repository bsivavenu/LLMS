from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def summarize_documents(documents, num_sentences=3):
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    
    # Fit transform the documents
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Compute pairwise cosine similarity
    cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Initialize summary list
    summaries = []
    
    # Generate summary for each document
    for i in range(len(documents)):
        # Get similarity scores for current document
        similarity_scores = list(enumerate(cosine_similarities[i]))
        
        # Sort the similarity scores in descending order
        similarity_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Get indices of top sentences
        top_indices = [score[0] for score in similarity_scores[1:num_sentences+1]]
        
        # Sort the top indices
        top_indices.sort()
        
        # Extract top sentences and join them
        top_sentences = ' '.join([documents[idx] for idx in top_indices])
        
        # Add summary to the list
        summaries.append(top_sentences)
    
    return summaries

# Example usage
# documents = [
#     "Machine learning is the scientific study of algorithms and statistical models that computer systems use to perform a specific task without using explicit instructions, relying on patterns and inference instead.",
#     "Deep learning is a subset of machine learning where artificial neural networks, algorithms inspired by the human brain, learn from large amounts of data.",
#     "Natural language processing is a field of computer science, artificial intelligence, and linguistics concerned with the interactions between computers and human languages, in particular how to program computers to process and analyze large amounts of natural language data.",
# ]

documents = open('../0.txt','r').readlines()
# print(type(documents))
# Generate summaries
summaries = summarize_documents(documents)
# print(summaries)
# Print summaries
for i, summary in enumerate(summaries):
    print(f"Summary for document {i+1}:")
    print(summary)
    print()
