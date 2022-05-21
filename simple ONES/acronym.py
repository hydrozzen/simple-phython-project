#Acronyms Using Python
sentence=input("enter a sentencew and i will be making an acronym from that")
text=sentence.split()
a =""
for i  in text: 
    a = a+str(i[0]).upper()
print(a)