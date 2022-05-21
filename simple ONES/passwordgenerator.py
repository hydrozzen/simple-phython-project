#password generator,it will give yopu a password
import random
passlen=int(input("Enter the length of your password then i will generate the password of your desired length "))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen))
print(p) 