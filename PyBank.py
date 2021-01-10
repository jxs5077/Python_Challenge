import os
import csv


file_path=os.path.join('.','Resources','PyBank_budget_data.csv')

dates=[]
profit_losses=[]
total_PL=[]
PL_changes=[]

csvfile=open("./Resources/PyBank_budget_data.csv")
csvreader=csv.reader(csvfile, delimiter=',') 

csv_header=next(csvreader)

for each_row in (csvreader):
    dates.append(each_row[0])
    profit_losses.append(int(each_row[1]))
   
total_PL= sum(profit_losses) 


for i in range(len(profit_losses)-1):
    PL_changes.append(profit_losses[i+1]-profit_losses[i])

average_change=(sum(PL_changes)/len(PL_changes))

average_format=format(average_change,",.2f")


dates_PLchanges = dict(zip(dates, PL_changes))

greatest_value=max(PL_changes)
greatest_date=list(dates_PLchanges.keys())[list(dates_PLchanges.values()).index(greatest_value)+1]

smallest_value=min(PL_changes)
smallest_date=list(dates_PLchanges.keys())[list(dates_PLchanges.values()).index(smallest_value)+1]




Financial_Analysis=(
  "Financial Analysis\n"
  "----------------------------\n"
  f"Total Months: {len(dates)}\n"
  f"Total: {str(total_PL)}\n"    
  f"Average  Change: ${str(average_format)}\n"
  f"Greatest Increase in Profits:  {str(greatest_date)} (${greatest_value})\n"
  f"Greatest Decrease in Profits:  {str(smallest_date)} (${smallest_value})\n"
)

print(Financial_Analysis)  # leave in place

with open("Analysis/Financial_Analysis.txt",mode="w") as output_text_file:
    output_text_file.write(Financial_Analysis)
    
