def vowels(s):
    return sum(1 for char in s if char in "aeiouAEIOU")
string = "Hello world"
vowel_count = vowels(string)
print(f"Number of vowels in the string is: {vowel_count}")
