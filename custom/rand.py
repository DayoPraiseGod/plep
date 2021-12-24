import random as rd

def uniqid(length):
    """
    This is a unique number generator written by Adesanmi D. PraiseGod on 22/12/2021
    when writting code for PLEP project to asign unique id for CSC320 project clients
    """

    cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sma = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"

    key = [cap, sma, num]

    unique_no = ""

    for i in range(length):
        choise = key[rd.randint(0, len(key)-1)]
        size = len(choise)
        unique_no += choise[rd.randint(0, size-1)]
        
    return unique_no

