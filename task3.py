"""
===================   TASK 3   ====================
* Name: Negative and Non-Negative Elements
*
* Write a script that will populate a list with as
* many elements as user defines. For taken number
* of elements the script should take the input from
* user for each element. You should expect that
* user will always provide integer numbers. At the
* end, the script should print how many negative
* and non-negative numbers there were present in
* the list.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

# Write your code here

def is_nonnegative(broj):

    if broj >= 0:
        return True
    else:
        return False


list_length = int(input("Koliko brojeva treba da ima lista? "))

lista_brojeva = []

for i in range(list_length):
    novi_broj = int(input("Unesite broj #" + str(i+1) + ": "))
    lista_brojeva.append(novi_broj)

total_nonnegative = total_negative = 0

for broj in lista_brojeva:

    if is_nonnegative(broj):
        total_nonnegative += 1
    else:
        total_negative += 1


print("Lista brojeva: ", str(lista_brojeva))
print("Broj nenegativnih: ", total_nonnegative)
print("Broj negativnih: ", total_negative)













