""" Selection of code that opens a plain text file, parses it into the Google Translate API 
	(whose library must be downloaded via https://github.com/BoseCorp/py-googletrans.git)
	translates, then formats translation into a single sentence.
	
"""

# file-input.py
f = open('TestText.txt','r')
message = f.read()
print(message)
f.close()

#if clicked, clicked item becomes variable Query, string

from googletrans import Translator
translator = Translator()
#print slice_translation(str(translator.translate(message))) # test line


# Give slice of translated portion for only the translation
def find_third_equals(s):     #give index of third = sign
    letter_count = 0
    for i in range(len(s)):
        if s[i] == "=":
            letter_count += 1
            if letter_count == 3:
                return i + 1
                
def find_pronunciation(s):    #give index of pronunciation
    return int(s.find(" pronunciation"))
    
def slice_translation(s):    #give slice of string for substring of only translated word
    return s[find_third_equals(s):find_pronunciation(s)-1]
# Test function to slice    
#print slice_translation("<Translated src=ko dest=ja text=hello there pronunciation=Kon'nichiwa.>")
# Slice functions above

print slice_translation(str(translator.translate(message)))
