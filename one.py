print("welcome")
a = 20 
b = 30 
print(a+b)

print("subtraction")
print(b-a)

print("mult")
print(a*b)

print("hi i am shilpa")

def check_even_odd(i):
    if (i%2) == 0 :
        print(i ," even number")
    else:
        print(i, "  odd number") 


for i in range(1,11):
    check_even_odd(i)
    
print("the code is running perfet")


import pandas as pd 
import matplotlib.pyplot as plt


class dataset :
    dataset = pd.read_csv("adult_reconstruction.csv")
    print(dataset.head(5))
    print(dataset.info)

class distribution :
    print()