import csv

# Open the original CSV file
with open('!Projects\BTC Algo\Data\Other\ImportBTCData.csv', 'r') as f:

    # Read the rows into a list and reverse the order
    rows = list(csv.reader(f))
    rows.reverse()

# Save the reversed rows to a new CSV file
with open('!Projects\BTC Algo\Graph\BTC_Master.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

############################################################################################################## Open the reversed CSV file  for saving ATH Data points
with open('!Projects\BTC Algo\Graph\BTC_Master.csv', 'r') as f:

    # Create two output files
    output_file_1 = open('!Projects\BTC Algo\Graph\Broken Up Cycles\ATH\cycle_2009.csv', 'w', newline='')
    output_writer_1 = csv.writer(output_file_1)
    output_writer_1.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']) 

    output_file_2 = open('!Projects\BTC Algo\Graph\Broken Up Cycles\ATH\cycle_2013.csv', 'w', newline='')
    output_writer_2 = csv.writer(output_file_2)
    output_writer_2.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']) 

    output_file_3 = open('!Projects\BTC Algo\Graph\Broken Up Cycles\ATH\cycle_2017.csv', 'w', newline='')
    output_writer_3 = csv.writer(output_file_3)
    output_writer_3.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']) 

    output_file_4 = open('!Projects\BTC Algo\Graph\Broken Up Cycles\ATH\cycle_2021.csv', 'w', newline='')
    output_writer_4 = csv.writer(output_file_4)
    output_writer_4.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']) 

    # Read each line of the original CSV file and write it to the appropriate output file
    line_num = 0
    for line in csv.reader(f):
        if line_num <= 1232:
            output_writer_1.writerow(line)
        elif line_num <= 2709:
            output_writer_2.writerow(line)
        elif line_num <= 4133:
            output_writer_3.writerow(line)
        else:
            output_writer_4.writerow(line)
        line_num += 1

    # Close the output files
    output_file_1.close()
    output_file_2.close()
    output_file_3.close()
    output_file_4.close()

##################################################################################### Open the reversed CSV file  for saving ATL Data points
with open('!Projects\BTC Algo\Graph\BTC_Master.csv', 'r') as f:

    # Create two output files
    output_file_1 = open('!Projects\BTC Algo\Graph\Broken Up Cycles\ATL\cycle_2009.csv', 'w', newline='')
    output_writer_1 = csv.writer(output_file_1)
    output_writer_1.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']) 

    output_file_2 = open('!Projects\BTC Algo\Graph\Broken Up Cycles\ATL\cycle_2013.csv', 'w', newline='')
    output_writer_2 = csv.writer(output_file_2)
    output_writer_2.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']) 

    output_file_3 = open('!Projects\BTC Algo\Graph\Broken Up Cycles\ATL\cycle_2017.csv', 'w', newline='')
    output_writer_3 = csv.writer(output_file_3)
    output_writer_3.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']) 

    output_file_4 = open('!Projects\BTC Algo\Graph\Broken Up Cycles\ATL\cycle_2021.csv', 'w', newline='')
    output_writer_4 = csv.writer(output_file_4)
    output_writer_4.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Market Cap']) 

    # Read each line of the original CSV file and write it to the appropriate output file
    line_num = 0
    for line in csv.reader(f):
        if line_num <= 1644:
            output_writer_1.writerow(line)
        elif line_num <= 3074:
            output_writer_2.writerow(line)
        elif line_num <= 4499:
            output_writer_3.writerow(line)
        else:
            output_writer_4.writerow(line)
        line_num += 1

    # Close the output files
    output_file_1.close()
    output_file_2.close()
    output_file_3.close()
    output_file_4.close()