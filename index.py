from csv import reader
data = []
count=0
with open('file.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        print(row)
	data[count]=row
	count+=1

