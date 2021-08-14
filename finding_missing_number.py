#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"""

import sys        
global a        

#input stepsize
stp = int(input("Enter the step size : "))

# number of elements
n = int(input("Enter number of elements : "))
 
# Below line read inputs from user using map() function
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
 
print("\nList is - ", a)


def step_sequence(vec):
    lst = []
    
    if(len(vec)==0):
        sys.exit("Input as only one element")
        
    else:
        for i in range(0,len(vec)-1):
            #print(i)
            #print(lst)
            temp = vec[i+1]-vec[i]
            #print(temp)
            num = vec[i] + 1
            #print(num)
            if temp>1:
                while num < vec[i+1]:
                    lst.append(num)
                    num = num + 1
        return lst
    

global lt
lt = [0] * (stp+1)
temp = [0] * (stp+1)
f = []
b = []
vc = []

for i in range(0,stp-1):
    
    print("\n Performing step: ",i+1)    
    f = []
    b = []
    temp = [0] * (stp+1)
    while len(lt)>1:
    #while (len(temp)!=stp and len(lt)>1):
        bck = lt
        lt = step_sequence(a)
        if len(lt)==0:
            break
        print(lt)
        #print(f)
        #print(b)
        f.append(a[0])
        b.append(a[-1])
        a = lt
        

    
    #if len(lt) == 0:
    #    a = bck
    
    vc = f + a + b[::-1]
    a = vc
    lt = [0] * (stp+1)

    if len(vc)==stp:
        sys.exit("Normalization complete")    

    print("\n Vector for Step",i+2,":",a)
    

        
    