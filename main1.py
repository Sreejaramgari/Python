import csv
try:
    with open('Contacts.csv','w', newline="")as file:
        #print("Customers csv file created")
        writer_obj = csv.writer(file)
        lines = [['name','mobile'],['sreeja','8919140357'],['shravya','6304829938']]
        writer_obj.writerows(lines)

except Exception as e:
    print("Error", e)