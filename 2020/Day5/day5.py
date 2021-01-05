from typing import List
import numpy as np

def bps(seat_inst:List[str]) -> int:
    """
    A function that takes a list of instruction about your seat and return your seat ID
    using binary partions space algorithm. 
    ...

    Parameters
    ----------
        
        seat_inst: a string letters that indicate that instruction of the partitioning either
    in the uper half or lower half based on the character. 
    
    Returns
    ----------
    
        The seat ID. 
    
    """
    col=np.arange(0,8)
    row=np.arange(0,128)
    
    for i in seat_inst[:-3]:
        if i=='B':
            row=row[row.shape[0]//2:]
        else:
            row=row[:row.shape[0]//2]
    for i in seat_inst[-3:]:
        if i=='R':
            col=col[col.shape[0]//2:]
        else:
            col=col[:col.shape[0]//2]

    return (row*8)+col
    

    
if __name__ == "__main__":
    seat_id=[]
    filename = "Days_2020/input_day5.txt"
    text_file = open(filename, "r")
    seat_inst=text_file.readlines()
    
    ############# Part 1 ############
    
    for seat_i in seat_inst:        
        seat_id.append(bps(seat_i.replace('\n',''))[0])
        
    larger_seat=max(seat_id)
    
    print("The highest seat:",larger_seat)
    ############# Part 2 ############
    seat_id.sort()
    
    print("Your Seat:",sum(range(seat_id[0],seat_id[-1]+1)) - sum(seat_id))
