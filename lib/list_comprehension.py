#!/usr/bin/env python3

def return_evens(num_list):
    num_list = [n for n in num_list if n%2 == 0]
    return num_list

    

def make_exclamation(sentence_list):
    sentence_list =  [f"{words}!" for words in sentence_list]
    return sentence_list

print(make_exclamation(["Hello", "World"]))