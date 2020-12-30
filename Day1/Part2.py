def sum_part2(x: List[float] ) -> float:
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
    z:int
        a number that holds the result of the multiplication
    
    """
    
    for i,item in enumerate(x):
        for j,jtem in enumerate(x):
    
            temp=x+item+jtem
            temp[i]=0
            temp[j]=0
            if 2020 in temp:
                index=list.index( list(temp) , 2020 )
                print("Three entries", x[index] ,",",jtem,"and" , item ,"that sum to 2020")
                print("The multiplication result is ", x[index]*item*jtem)
                return  x[index]*item*jtem
    print("There are no Three entries that sum to 2020")
    

if __name__ == "__main__":
    expense=[]
    text_file = open("input_day1_2020.txt", "r")
    for line in text_file:
        expense.append(int(line.strip()))
    sum=sum_part2(np.array(expense))

