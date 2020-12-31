import string

file_contents = "In the control room was silence like fabric strained to \
    the verge oftearing. Softly through the weave of it came the murmur of \
    the engines, fretful, unhappy, the whimper of something sick."

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    words = file_contents.lower().split()
    words = [''.join(c for c in s if c not in string.punctuation) for s in words]
    words = [''.join(c for c in s if c not in uninteresting_words) for s in words]

    print(words)
    # frequency = [words.count(i) for i in words]

calculate_frequencies(file_contents)