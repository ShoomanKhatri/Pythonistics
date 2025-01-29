str1 = "race"
str2 = "Care"

str1 = str1.lower()
str2 = str2.lower()

if len(str1)== len(str2):
    
    sorted_str1  = sorted(str1)
    sorted_str2  = sorted(str2)
    
    if sorted_str1 == sorted_str2:
        print("This is anagram")
    else:
        print("not anagram")
else:
    print("not anagram")
        



