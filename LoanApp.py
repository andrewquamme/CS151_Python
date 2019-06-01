## Andrew Quamme CS 151 Program 5
## Program to process loan approval and interest rate 
## for file of names and FICO scores

def main():
    ## Flow control function
    records = fileToList("Apps.dat")    # Read file to be processed
    for i in range(len(records)):       # Send FICO for approval & append rate
        records[i].append(getApproval(records[i][1]))  
    printResults(records)               # Display results

def fileToList(fileName):
    ## Function to open file, strip lines, and split lines
    ## Returns a list of list of records from the file
    infile = open(fileName, 'r')
    listOfRecords = [line.strip() for line in infile]
    infile.close()
    for i in range(len(listOfRecords)):
        listOfRecords[i] = listOfRecords[i].split(',')
        listOfRecords[i][0] = eval(listOfRecords[i][0])
        listOfRecords[i][1] = eval(listOfRecords[i][1])       
    return listOfRecords

def getApproval(fico):
    ## Function to take FICO score as input and
    ## calculate if loan is approved or not.
    ## Returns interest rate
    try:
        if fico >= 760:         # Determine interest rate based on FICO score
            rate = '3.080%'
        elif fico >= 700:
            rate = '3.302%'
        elif fico >= 680:
            rate = '3.479%'
        elif fico >= 660:
            rate = '3.693%'
        elif fico >= 640:
            rate = '4.123%'
        elif fico >= 620:
            rate = '4.669%'
        else:
            rate = 'Denied'     # Loan not approved if FICO is < 620
    except TypeError:           # Show ERROR if FICO is not entered properly
        rate = 'ERROR'
    return (rate)

def printResults(records):
    ## Function to display name, FICO, and interest rate
    print("{0:10}{1:10}{2:10}".format("Name","FICO","Rate"))    # Print headers
    print("{0:10}{1:10}{2:10}".format("-----","-----","-----"))
    for i in range(len(records)):
        print("{0:10}{1:<10}{2:10}".format(records[i][0], records [i][1],records[i][2]))

main()
