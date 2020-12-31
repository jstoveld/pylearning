def highlight_word(sentence, word):
    for x in sentence.lower().split():
        if word == x:
            sentence = sentence.replace(x, word.upper())
            return(sentence)
        elif (word+str("!")) == x:
            word = (word+str("!"))
            word = word.upper()
            sentence = sentence.replace(x, word)
            return(sentence)
    

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))