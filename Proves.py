def subrutina(): 
    def sub_subrutina(): 
        a = 5 
        print(a) 
        return 
    global a 
    a = 4 
    sub_subrutina() 
    print(a) 
    return 
a = 3 
subrutina() 
print(a) 
