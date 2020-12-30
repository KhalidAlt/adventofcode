from typing import List
import numpy as np

def sum_to_2020(x: List[float] ) -> float:
    """
    A function that takes a list and find two entries that sum to 2020
    and returen their multiplication
    ...
    Parameters
    ----------
    x : list
        a list that contains you expense report
    Returns
    ----------
        a number that holds the result of the multiplication
    
    """
    
    for i,item in enumerate(x):
        temp=x+item
        temp[i]=0
        if 2020 in temp:
            index=list.index( list(temp) , 2020 )
            print("Two entries", x[index] ,"and" , item ,"that sum to 2020")
            print("The multiplication result is ", x[index]*item)
            return  x[index]*item
    print("There are no two entries that sum to 2020")
    

if __name__ == "__main__":
    expense=[]
    text_file = open("input_day1_2020.txt", "r") 
    for line in text_file:
        expense.append(int(line.strip()))
