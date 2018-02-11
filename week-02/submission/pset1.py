print("starting pset1")
print(" ")


print("A.Lists")
l=["girls","just","wanna","have fun"] #A.1 Create a list containing any 4 strings.
print(l[2]) #A.2 Print the 3rd item in the list
print(l[0:2]) #A.3 Print the 1st and 2nd item in the list using [:] index slicing
l.append("last") #A.4 Add a new string with text “last” to the end of the list and print the list.
print(l)
print(len(l), "items in list") #A.5 Get the list length and print it.
l[4]="new" #A.6 Replace the last item in the list with the string “new” and print
print(l)
print(" ")


print("B.Strings")
sentence_words=['I','am','learning','Python','to','munge','large','datasets','and','visualize','them']
print(' '.join(sentence_words)) #B.1 Convert the list into a normal sentence with join(), then print
sentence_words.reverse() #B.2 Reverse the order of this list using the .reverse() method, then print.
print(sentence_words)
sentence_words.sort() #B3. use the .sort() method to sort the list using the default sort order.
print(".sort()",sentence_words)
print("sorted()",sorted(sentence_words))#B.4.1 Perform the same operation using the sorted() function.
print(".sort() is a method, it acts in place and on the object that called, sorted() is a function, it creates a new list and act upon a variable inserted in its ()")#B.4.2Provide a brief description of how the sorted() function differs from the .sort() method.
sws=sorted(sentence_words, key=lambda x:x.lower())#B.5 case-insensitive alphabetical sort.
print(sws)
print(" ")


print("C. Random Function")
from random import randint
def my_random(high,low=0):#C random function returning an integer between a low and a high number supplied by the user, but that can be called with the low number optional (default to 0).
    return randint(low,high)
assert(0 <= my_random(100) <= 100)
assert(50 <= my_random(100, low = 50) <= 100)
print(my_random(150,-50)) #print random number within bounds -50<x<150
print(" ")


print("E. Password Validation Function")
password="Fun_2018" #insert any password to be checked

def checker(x): #function to check password for compliance with rules
    import string
    n=['0','1','2','3','4','5','6','7','8','9']
    u=string.ascii_lowercase.upper()
    s=['!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']
    ok_l=[]
    ok_n=[]
    ok_u=[]
    ok_s=[]
    if 8<=len(x)<=14:
        ok_l.append(1)
    for i in x:
        if i in n:
            ok_n.append(i)
    for i in x:
        if i in u:
            ok_u.append(i)
    for i in x:
        if i in s:
            ok_s.append(i)
    if len(ok_l)==1 and len(ok_n)>=2 and len(ok_u)>=1 and len(ok_s)>=1:
        print ("excellent password!")
        return "success"
    else:
        print ("Your password doesn't follow the rules, try again")
        return "error"
checker(password)
print(" ")

print("F. Exponentiation Function")
def exp(x,y):
    total=1
    i=1
    while i<=(y):
        total=total*x
        i=i+1
    return total
print(" ")


print("G. Extra Credit: Min and Max Functions")

def minimum(x): #min definition
    min_=x[0]
    for i in x:
        if i<min_:
            min_=i
    return min_

def maximum(x): #max definition
    min_=x[0]
    for i in x:
        if i>min_:
            min_=i
    return min_
