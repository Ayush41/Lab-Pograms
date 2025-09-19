password = input("Enter the password: ")

longest = ""

for i in range(len(password)):
    substring = ""
    for j in range(i, len(password)):
        if password[j] in substring:
            break
        substring += password[j]
    if len(substring) > len(longest):
        longest = substring

print("Longest substring without repeating characters:", longest)
