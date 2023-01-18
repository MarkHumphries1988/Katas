import datetime
def lengthen_date(date):
    date=date.split(".")
    
    if date[0]=="01" or date[0]=="31" or date[0]=="21":
        ending="st"
    elif date[0]=="02" or date[0]=="22":
        ending="nd"
    elif date[0]=="03" or date[0]=="23":
        ending="rd"
    else:
        ending="th"


    
   
    
    date=[int(x) for x in date]
    date1=datetime.date(day=date[0],month=date[1],year=date[2]).strftime('%A %d')
    date2=datetime.date(day=date[0],month=date[1],year=date[2]).strftime(' %B %Y')
    

    return date1+ending+date2
    
   

    pass
