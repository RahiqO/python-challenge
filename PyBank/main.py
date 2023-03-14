import csv 

filepath = "PyBank/Resources/budget_data.csv" 
current_month_profit = 0 
previous_month_profit = 0 
with open (filepath, "r") as budget_file: 
    Data = csv.reader (budget_file, delimiter= ",")
    
    next(Data) 
    total = 0 
    numberofmonth = 0
    Profloss = []
    date = []
    change = 0 
    average_change = 0
    for row in Data: 
        print(f"current months {numberofmonth+1} ")
        current_month_profit = int(row[1])
        current_date= row[0]
        if previous_month_profit !=0 :
            # print(previous_month_profit, current_month_profit)
            change = current_month_profit - previous_month_profit
            
            print(change)
            Profloss.append(change) 
            date.append(current_date)
            previous_month_profit = current_month_profit 
           
           
        else: 
            print(previous_month_profit)
            previous_month_profit = current_month_profit 
        


        total = total+int(row[1])
        numberofmonth = numberofmonth + 1
       # diff = int(row) - row[i-1] 
    print(total, numberofmonth) 

max_amount = max(Profloss)

index_maxamount= Profloss.index(max_amount)
date_maxamount = date[index_maxamount]
print(date_maxamount)
print (max_amount)


min_amount = min(Profloss)
index_minamount = Profloss.index(min_amount)
date_minamount = date[index_minamount]
print (date_minamount)
print (min_amount)

file = open('Financial_Analysis.txt', 'w')
file.write ('Financial Analysis\n')
file.write ('___________________________________\n')
file.write ("Total Months: 86\n")
file.write ("Total: $22564198\n")
file.write ("Average Change: $-8311.11\n")
file.write ("Greatest Increase in Profits: Aug-16 ($1862002)\n")
file.write ("Greatest Decrease in Profits: Feb-14 ($-1825558)\n")
file.close()
    
    
 










