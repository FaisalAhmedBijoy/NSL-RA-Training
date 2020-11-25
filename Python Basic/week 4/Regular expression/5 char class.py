'''
character class is used as [] to check a char belong or not
'''
import re
#char set all vowel
pattern =r"[aeiou]"
if re.search(pattern,'gray'):
    print("the word 'gray'  contain vowel")
else:
    print("No vowel")
if re.search(pattern,'xxuu'):
    print("the word 'xxww' does not contain vowel")
else:
    print("No vowel")
    
