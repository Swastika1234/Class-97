string=input("enter string: ")
characterCount=0
wordCount=1

for i in string:
    characterCount+=1
    if(i==' '):
        wordCount+=1


print("number of words in the string= ")
print(wordCount)

print("number of words in the string= ")
print(characterCount)