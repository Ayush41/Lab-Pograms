
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