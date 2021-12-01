"""
Escriviu un programa que comprova si dues llistes tenen elements en comú.

"""

ll1=[1,2,3,4,5]
ll2=[1,2,4,5,433,322,511]
print("Els següents números están repetits a les dues llistes: ")
for el in ll1:
    for el2 in ll2:
        if el==el2:
            print(el,end=" ")
            