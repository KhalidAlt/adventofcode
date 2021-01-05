from typing import List

def count_trees(map: List[str] ,slope: List[int]=[3,1]) -> int:
    """
    A function that takes a map coordinates in a grid contains trees and squres.
    Then the function returns the number of trees that encountred. 
    ...

    Parameters
    ----------
    map: a list of string that contains the grid of the map.
        
    slope: a list of integer point out to the slope of traversing the map in the right and down direction.
    
    Returns
    ----------
    
        Number of trees that encountred through traversing the map 
    
    """
    n_trees=0
    last_index=len(map[0])

    row_move,down_move=slope
    row_org=row_move
    
    for i in range(0,len(map)-down_move,down_move):
        

        
        if(map[i+down_move][row_move%last_index]=="#"):

            n_trees+=1
            

        row_move+=row_org

    return n_trees



if __name__ == "__main__":

    text_file = open("Days_2020/input_day3.txt", "r")
    lines=text_file.read().split()
    
    # Part One 
    print("how many trees would you encounter? if you follow a slope of right 3 and down 1 :",count_trees(lines))
    
    
    multi=1
    
    coordinates=[1,1],[3,1],[5,1],[7,1],[1,2]
    
    for j in coordinates:
        ntrees=count_trees(lines,j)
        multi*=ntrees
        
    ## The second Part :
    print("What is the number of trees encountered on each of the listed slopes multiplied togther:", multi)
