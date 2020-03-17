

import csv                                                          


cwb_filename = '107061206.csv'                                      
data = []
header = []
with open(cwb_filename) as csvfile:                                 
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        data.append(row) 


    sum = list(range(5))    
    output = list(range(5))
    stationid = list(range(5))

    stationid = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']    

    for i in range(5):                                              
        sum[i] = 0
        for row in data :
            if row['station_id'] == stationid[i] :                     
                if row['HUMD'] == '-99.000' or row['HUMD'] == '-999.000' :
                    sum[i] = 0

                else :    
                    sum[i] += float(row['HUMD'])
    
    for i in range(5): 
        if sum[i] == 0 :      
            output[i] = [stationid[i], 'None']                          
        else :
            output[i] = [stationid[i], sum[i]]


    print(output) 
     

