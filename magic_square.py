# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 07:50:57 2024

@author: anjal
"""
def magic_square(n):
    magicSquare=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
    i=n//2
    j=n-1
    s=n*n
    count=1
    while(count<=s):
        if(i==-1 and j==n): # Condition 4
            j=n-2
            i=0
        else:
            if(j==n): #column value is exceeding
                j=0
            if(i<0):
                i=n-1
        if(magicSquare[i][j]!=0):
            j=j-2
            i=i+1
            continue #skip whatever is there after this line 
        else: 
            magicSquare[i][j] = count
            count=count+1
        i=i-1
        j=j+1   #condition 1
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print()
    print("The sum of each row/column/diagonal is: ", str(n*(n**2+1)/2))
num=int(input("Enter the number: "))
magic_square(num)