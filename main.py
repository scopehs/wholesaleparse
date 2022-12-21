import csv, os
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="parse",
    database="parse"
)

def parse_csv(filename):
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        print(f'Processing {filename}.')
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            mycursor = mydb.cursor()
            sql = "INSERT INTO invoices (accountId, accountName, invoiceNumber, invoiceDate, orderNumber, productNumber, description, quantity, netPrice, per, goods, vat, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (
                row["Account"],
                row["Name"],
                row["Invoice Number"],
                row["Invoice Date"],
                row["Order Number"],
                row["Product"],
                row["Description"],
                row["Quantity"],
                row["Net Price"],
                row["Per"],
                row["Goods"],
                row["VAT"],
                row["Total"]
                )
            mycursor.execute(sql, val)
            mydb.commit()
            line_count += 1
        print(f'Processed {line_count} lines.')


# define the folder to search
path = "data"

# change directory
os.chdir(path)

# iterate through all files in the folder
for file in os.listdir():
    # check files end is csv
    if file.endswith(".csv"):
        # read files.
        parse_csv(file)