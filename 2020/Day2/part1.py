from typing import List

def pass_validity(min:int ,max:int ,char:str ,password:str) -> bool:
    """
    A function that takes a password and return if the password is valid or not 
    based on password policy.
    ...

    Parameters
    ----------
    min: lowest number of times the (char) must appear for the password to be valid.
    
    max: an int number indicates the highest number of times the (char) must appear for the password to be valid.
    
    char: the letter that must be appear in the password based on min and max. 
    
    password: a string contains the password that must be verfired if it is a valid or not.

    Returns
    ----------
    
        a bool value either True to indicate valid or False to indicate invalid.
    
    """
    
    char_count=password.count(char)
    if (char_count <= max ) and (char_count >= min):
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
        valid=pass_validity(int(minmax[0]),int(minmax[1]),char[0],password)
        
        if valid:
            n_valid+=1

    print("The number of passwords that are valid according to their policies is:", n_valid)
