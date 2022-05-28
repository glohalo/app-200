# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 15:24:18 2022

@author: Administrador
"""
#####Problem 1. ###
##### Working with strings###
smallest = None
largest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fnum = float(num)
    except:
        print("Invalid input")
        continue
    if smallest == None:
        smallest = int(num)
        
    elif smallest > int(num):
        smallest = int(num)
        print(smallest)
        
    if largest == None:
        largest = int(num)

    elif int(num) > largest:
        largest = int(num)
        
print("Maximum is", largest)
print("Minimum is", smallest)


### problem 1.a ###
#fname = input("Enter file name: ")
fh = open('Practica.txt')
count = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    x = line[20:]
#    print(x)
    count += float(x)
#    print(line)
print("Done")
print("Average spam confidence: ", count/27)

#### 1.b##
# fname = input("Enter file name: ")
# try:
#     fh = open('string_list.txt')
# except:
#     print("File cannot be opened: ", fname)
#     quit()
fh = open('string_list.txt')   
lst = list()
for line in fh:
    line = line.rstrip()
    lst.append(line)
    
words = lst[0].split()
words = words + lst[1].split() + lst[2].split() + lst[3].split()
words.sort()
final_lst = []
for word in words:
    if word not in final_lst:
        final_lst.append(word)
print(final_lst)

#### problem 2 ####
## list and strings ##
try:
    fname = input("Enter file name: ")
except:
    print('File cannot be opened', fname)
    quit()
    
fn = open(fname)
count = 0
for line in fn:
    line = line.rstrip()
    wds = line.split()    
    #building the guardian
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    print(wds[1])
    count = count + 1    
print("There were", count, "lines in the file with From as the first word")

### Problem 3 ###
### Dictionaries ###

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

list_wds = list()
dict_wds = dict()
for line in handle:
    line = line.rstrip()
    wds = line.split()    
    #building the guardian
    if len(wds) < 3 or wds[0] != 'From' :
        continue
    list_wds.append(wds[1]) 
# Create a dict from the list    
for email in list_wds:
    dict_wds[email] = dict_wds.get(email, 0) + 1
# Get the most common email
largest = -1 #some trick because the numbers should be always positive
word = None
for k,v in dict_wds.items():
    if v > largest:
        largest = v
        print('largest number before: ', largest)
        word = k
        print('this is the word ', word)
print(word, largest)

#####Problem 9
#Same file
#count the emailsfor each hour
#generate a list of tuples


handle = open('string_list2.txt')
list_wds = list()
for line in handle:
    line = line.rstrip()
    wds = line.split()    
    #building the guardian
    if len(wds) < 2 or wds[0] != 'From':
        continue
    list_wds.append(wds[5])
    
#Extract the first two digits in the list
Hour = (sorted([hour[0:2] for hour in list_wds]))
# Create a dict from the list   
dict_h = dict()
for i in Hour:
    dict_h[i] = dict_h.get(i, 0) + 1
for k, v in dict_h.items():
    print(k, v)
