# Write your solution here
sentence = input("Please type in a sentence: ")
index = 0

while len(sentence) > 0:
    index = sentence.find(" ")
    print(sentence[0])
    if index < 0:
        break
    sentence = sentence[index + 1:]
        
        
        
    
