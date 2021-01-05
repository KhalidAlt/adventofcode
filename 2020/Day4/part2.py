from typing import List
import re

def passport_validity(pport:List[str],fields:List[str]=['byr','iyr','eyr','hgt','hcl','ecl','pid']) -> int:

    items_count=0
    f_len=len(fields)
    

    

    for i in pport:
        
        if ":" in i:
            item=i[:i.index(":")] # extract the info name
        
            f_value=i[i.index(":")+1:] # extract the value of the info
        
        if item=='byr':
            items_count+= 2002>=int(f_value)>=1920 
        elif item=='iyr':
            items_count+= 2020>=int(f_value)>=2010 
            
        elif item=='eyr':
            items_count+= 2030>=int(f_value)>=2020
        elif item=='hgt':

            if f_value[-2:]=='cm':
                items_count+= 193>=int(f_value[:-2])>=150  
            elif f_value[-2:]=='in':
                items_count+= 76>=int(f_value[:-2])>=59

        elif item=='ecl':

            items_count+= f_value in ['amb' ,'blu','brn' ,'gry' ,'grn', 'hzl' ,'oth']
                
        elif item=='pid':
            items_count+= f_value.isdigit() &  (len(f_value)>=9)  
        else:
            items_count+=int( re.search(r"#[a-z0-9]{6}", f_value) != None )
            
    if items_count == f_len:
        return True
        
    else: return False

    
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
    
    
    print(" the number of valid passports :,", n_valid)


