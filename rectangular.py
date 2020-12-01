def kare():
    n = input('please enter a number to make a square from #:')
    if n.isdigit():
        n = int(n)
        print(n * '#')
        for i in range((n-2)):
            print('#'+ (n-2)*' ' + '#')
        print(n * '#')
    else:
        print('please enter a number')        
kare()
