# Write a program to check whether two sentences are anagrams of each other.

#anagram
sentence1 = input("Enter the first sentence: ")
sentence2 = input("Enter the second sentence: ")

clean1 = sentence1.replace(" ", "").lower()
clean2 = sentence2.replace(" ", "").lower()

if sorted(clean1) == sorted(clean2):
    print("The sentences are anagrams.")
else:
    print("The sentences are not anagrams.")
