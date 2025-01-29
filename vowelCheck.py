
def showVowel(input_string):
    
    vowel = "aeiouAEIOU"
    
    
    for char in input_string:
        if char in vowel:
            return True
        else:
            return False
    
        
user_input = input("Enter you string: ")

if showVowel(user_input):
      print("vowel exists")
else:
    print("vowel doesnt exist")
  
    
            
    
