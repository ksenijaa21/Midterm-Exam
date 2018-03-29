"""
===================   TASK 2   ====================
* Name: Product Of Digits
*
* Write a script that will take an input from user
* as integer number and display product of digits
* for a given number. Consider that user will always
* provide integer number.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""

# Write your code here

def proizvod_cifara(broj):


    if not isinstance(broj, int):
        return -1

    proizvod = 1

    while broj > 0:
        cifra = broj % 10
        broj = broj // 10
        proizvod = proizvod * cifra

    return proizvod


def main():

    int_broj = 523
    proizvod = proizvod_cifara(int_broj)
    print("Proizvod cifara je: ", proizvod)

main()
