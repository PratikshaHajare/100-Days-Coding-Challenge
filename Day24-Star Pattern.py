'''
Day 24 coding Statement : Write a program to print Pyramid pattern using stars

Description

Get the number of lines as the input and print stars in that many lines or rows in a pyramid shape.

Input

4

Output

  *

 ***

*****

*******'''
n=int(input("Enter No:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print(end="\n")