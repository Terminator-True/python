"""
Fes un programa en Python anomenat ex3.py que generi una llista formada per tots els paràmetres que li passem
 com argument i la mostri per consola.
"""
import sys
ll=sys.argv
ll.pop(0)
print(ll)