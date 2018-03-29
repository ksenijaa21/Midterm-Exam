"""
===================   TASK 4   ====================
* Name: Convert To Upper
*
* Write a function `convert_2_upper` that will take
* a string as an argument. The function should
* convert all lowercase letter to uppercase without
* usage of built-in function `upper()`.

* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here


def convert_2_upper(recenica):

    nova_recenica = ""

    for character in recenica:
        broj_slova = ord(character)

        if broj_slova > 96 and broj_slova < 123:
            broj_velikog_slova = broj_slova -32
            character = chr(broj_velikog_slova)

        nova_recenica += character

    return nova_recenica

recenica = input("Unesi: ")
novarecenica = print(convert_2_upper(recenica))
