"""
Quick brown fox jumped over the lazy dog.
"""
received = input("Please enter a sentence to see\
how many times each letter used: ").strip().lower()
result = {}
for i in received:
    keys = result.keys()
    if i in keys:
        result[i] += 1
    else:
        result[i] = 1
result

