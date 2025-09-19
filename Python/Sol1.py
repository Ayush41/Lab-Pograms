from collections import Counter

def count_character_frequency(review):
    review = review.replace(" ", "")
    
    char_count = Counter(review)
    
    # Sort the characters by frequency in descending order
    sorted_char_count = char_count.most_common()

    print("Character frequencies in descending order:")
    for char, count in sorted_char_count:
        print(f"{char}: {count}")

review = input("Enter the cust review: ")
count_character_frequency(review)
