import random

#1 just a list
list1=[1,2,33,555,22]
#2 another list
list2=['ok',1,233,'nooo','word',23.78,3232,'dfsf',True,19]
#3 dictionary
d1={'name':'john','last_Name':'jay'}
#4 print it
print(d1)
#5 dictionary print message
print("Hello", d1['name'], d1['last_Name'], "!")
#6 dictionary like before and it has values as well
d2={'name':'john','last_Name':'jay'}
#7 printing d2 dictionary
print(d2)
#8 nested dictionary with 3 keys and their values
stuff={1:{'name':'kale','age':20,'sex':'male'},
2:{'name':'Joe','age':23,'sex':'male'},
3:{'name':'katie','age':21,'sex':'female'}}
#9 printing a message with each of the dictionaries
print("Hello", stuff[1]['name'],"you're", stuff[1]['age'],"and you're", stuff[1]['sex'],"!")
print("Hello", stuff[2]['name'],"you're", stuff[2]['age'],"and you're", stuff[2]['sex'],"!")
print("Hello", stuff[3]['name'],"you're", stuff[3]['age'],"and you're", stuff[3]['sex'],"!")
#10 two empty list used for taking in user input
l1=[]
l2=[]
#for loop to take in 5 user inputs and append them to each empty from before
for i in range(5):
    x=input("First list enter your"+str(i+1)+"number: ")
    l1.append(x)

for i in range(5):
    x=input("Second list enter your"+str(i+1)+"number: ")
    l2.append(x)
#sort both list then compare them and see if its the same or different
l1.sort()
l2.sort()
#if theyre the same print they are, if not print they're not
if l1==l2:
    print("Both lists are the same")
else:
    print("Both lists are not the same")

#11 an empty list
l3=[]
#for loop and generate 5 random numbers from the range of 0 to 100 and store them into
#the list
for i in range(5):
    n=random.randint(0,100)
    l3.append(n)

#12 all 5 vowels
vowels=['a','e','i','o','u']
#nested for loops matching each pair
for i in range(5):
    for j in range (5):
        #if theyre the same, don't print and pass to do nothing
        if vowels[i]==vowels[j]:
            pass
        #otherwise if theyre not the same, print this combo
        else:
            print(vowels[i],vowels[j])

#13 list of numbers
lista=[1,2,3,4,5,3,3,4,5,5]
#while loop to pop each number
while len(lista)>0:
    #while there are still more than 2 elements, keep popping the third one
    if(len(lista)>2):
        print(lista.pop(2))
    else:
        lista.pop()

#14 empty list
l4=[]
#for loop to generate 10 random numbers from range 0-100 and append it to the list
for i in range(10):
    n=random.randint(0,100)
    l4.append(n)
#print the 10 random number list
print(l4)

#15 filled in the list
l5=[2,3,5]
#add each element together from the list into the sum and print
sum=0
for i in range(len(l5)):
    sum+=l5[i]
print("the sum is: "+str(sum))