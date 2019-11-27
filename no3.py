import calendar

def get_calendar(yy,mm):
    return(calendar.month(yy,mm,w=0,l=0))

print(get_calendar(11, 2019))