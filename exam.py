# -*- coding: utf-8 -*-
"""
Created on Thu May 26 23:31:57 2022

@author: Administrador
"""

def Sum(num1, num2):
    if num1 == num2:
        return "-1"
    if num2 >= num1:
        return "true"
    if num1 >= num2:
        return "-1"
    # new = 0
    # for i in range(1, num+1):
    #     new += i
    #     return new

num2=3
num1=300
print(Sum(num1, num2))

def caesar(string, num):
    result = " "
    for i in range(len(string)):
        char = string[i]
        if (char.isupper()):
            result += chr((ord(char) + num-65) %26 +65)
        else:
            result += chr((ord(char) + num-97) % 26 + 97)
    return result

string= "Caesar Cipher"
num = 2
print(caesar(string, num))

def areBracketsBalanced(expr):
    stack = []
 
    # Traversing the Expression
    for char in expr:
        if char in ["(", "{", "["]:
 
            # Push the element in the stack
            stack.append(char)
        else:
 
            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Check Empty Stack
    if stack:
        return False
    return True
expr = "[rrr)()"
print(areBracketsBalanced(expr))