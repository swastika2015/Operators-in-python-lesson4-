Amount=int(input("Enter your withdraw amount:"))


Note_1= Amount//100
Note_2= (Amount%100)//50
Note_3= ((Amount%100)%50)//10

print("Number of 100 rupees needed:", Note_1) 
print("Number of 50 rupees needed:", Note_2) 
print("Number of 10 rupees needed:", Note_3) 