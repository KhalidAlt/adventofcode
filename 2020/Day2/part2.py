from typing import List


def pass_validity2(pos1:int ,pos2:int ,char:str ,password:str) -> bool:
    """
    A function that takes a password and return if the password is valid or not 
    based on password policy.
    ...

    Parameters
    ----------
    pos1: an int number that indicates the first position in which the (char) may appear.
    
    pos2: an int number that indicates the first position in which the (char) may appear..
    
    char: the letter that must be appear in only one positions given in the policy (pos1,pos2). 
    
    password: a string contains the password that must be verfired if it is a valid or not.

    Returns
    ----------
    
        a bool value either True to indicate valid or False to indicate invalid.
    
    """
    pos1=password[pos1-1]
    pos2=password[pos2-1]

    if (pos1 == char) ^ (pos2 == char):
        return True
    else:
        return False
    

if __name__ == "__main__":

    text_file = open("input_day2.txt", "r")
    lines=text_file.readlines()
    n_valid=0
    for line in lines:
        minmax,char,password=line.split()
        minmax=minmax.split('-')
        valid=pass_validity2(int(minmax[0]) ,int(minmax[1]) ,char[0],password)
        if valid:
            n_valid+=1

    print("The number of passwords that are valid according to their policies is:", n_valid)
