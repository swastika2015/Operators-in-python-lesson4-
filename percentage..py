print("Enter the marks obtained in 4 subjects")


Maths=int(input("Marks obtained in Maths:"))
Physics=int(input("Marks obtained in Physics:"))
Chemistry=int(input("Marks obtained in Chemistry:"))
English=int(input("Marks obtained in English:"))

sum=Maths+Physics+Chemistry+English

print("sum of all four subjects is:",sum)

perc= (sum/400)*100

print(end="Percentage Mark=")
print(perc)