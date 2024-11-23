import csv

# Input and output file names
csv_file = 'large_twitch_edges.csv'
txt_file = 'large_twitch_edges.txt'

# Open the CSV file and create a text file
with open(csv_file, 'r') as csvfile, open(txt_file, 'w') as txtfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header row

    # Write edges to the text file
    for row in reader:

        txtfile.write(f"{row[0]} {row[1]}\n")

print(f"Edge list has been written to {txt_file}")