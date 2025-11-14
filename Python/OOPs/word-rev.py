
''' 
write a program reverse of the word/sentence but maintain the same sequence of words.
'''

def rev_word(sentence):
    return sentence[::-1]

if __name__ == "__main__":
    # input_sentence = "Hello World"

    # user input
    input_sentence = input("Enter a sentence to reverse: ")
    reversed_sentence = rev_word(input_sentence)
    print(f"Original Sentence: {input_sentence}")
    print(f"Reversed Sentence: {reversed_sentence}")



def rev_word(sentence):
    words = sentence.split()  # Split sentence into words
    reversed_words = [word[::-1] for word in words]  # Reversing each word
    return ' '.join(reversed_words)  

if __name__ == "__main__":
    # User input
    input_sentence = input("Enter a sentence to reverse the words: ")
    reversed_sentence = rev_word(input_sentence)
    
    print(f"Original Sentence: {input_sentence}")
    print(f"Sentence with Reversed Words: {reversed_sentence}")
