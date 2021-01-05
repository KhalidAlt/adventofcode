from typing import List

def passport_validity(pport:List[str],fields=['byr','iyr','eyr','hgt','hcl','ecl','pid']) -> int:

    items_count=0
    f_len=len(fields)
    for i in pport:
        
        item=i[:i.index(":")]
        if item in fields:
            items_count+=1
        if items_count == f_len:
            return True
            

    
if __name__ == "__main__":

    filename = "Days_2020/input_day4.txt"
    n_valid=0
    with open(filename) as f:
        passport=f.read().split("\n\n")
        passport=[i.replace('\n',' ').split(" ") for i in passport]
        for p in passport:
            valid=passport_validity(p)
            
            if valid==True:
                n_valid+=1
    
    
    print(" The number of valid passports : ", n_valid)
