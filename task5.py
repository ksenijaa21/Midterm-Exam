"""
===================   TASK 5   ====================
* Name: Del Boy Millionaire
*
* Help Del Boy become a millionaire. Del Boy is
* trading bitcoins on crypto-exchanges with simple
* algorithm. He is buying where the price of bitcoin
* is the lowest and selling where the bitcoin is
* the most expensive. Write a function `get_profit`
* which will take a list of bitcoin prices in USD as
* argument. The function should return what is the
* maximum possible profit for given bitcoin prices
* on different exchanges.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""

# Write your function here


def get_profit(list_of_bitcoin):

    list_of_bitcoin = [11564, 81734.3, 4985, 283654]
    most_expensive = list_of_bitcoin[0]
    least_expensive = list_of_bitcoin[0]

    for i in range(len(list_of_bitcoin) - 1):

        if most_expensive < list_of_bitcoin[i + 1]:
            most_expensive = list_of_bitcoin[i + 1]

    print(most_expensive)
    for i in range(len(list_of_bitcoin) - 1):

        if least_expensive > list_of_bitcoin[i + 1]:
            least_expensive = list_of_bitcoin[i + 1]
    print(least_expensive)

    return most_expensive - least_expensive