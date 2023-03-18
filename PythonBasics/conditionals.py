def year2century(year):
    str_year = str(year)
    if(len(str_year)<3):
        return 1
    elif(len(str_year) ==3):
        if(str_year[1:3] == "00"): # 100, 200, 300, ....., 900
            return int(str_year[0])
        else:                      # 190, 250, 450
            return int(str_year[0])+1
    else:                          # 1750, 1700, 1805
        if(str_year[2:4] == "00"): # 1700, 1900, 1100
            return int(str_year[:2])
        else:                      # 1705, 1645, 1258
            return int(str_year[:2])+1
        
print(year2century(1453))
print(year2century(999))
print(year2century(100))
print(year2century(1507))