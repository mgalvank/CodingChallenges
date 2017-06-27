from datetime import datetime
import math

def compute(S,E):
    entrance_fee = 2
    first_hour_fee = 3
    successive_hour_fee = 4


    #Convert string into datetime object
    start_time = datetime.strptime(S, '%H:%M')
    end_time = datetime.strptime(E, '%H:%M')

    #Get time in hours and round to the next hour
    total_hours = math.ceil(((end_time - start_time).total_seconds())/3600)

    total_cost = int(entrance_fee + first_hour_fee + ( (total_hours-1) * successive_hour_fee
                                                       if total_hours-1 != 0 else 0))

    return total_cost


print "Total_cost", compute("9:42","10:42")