## Andrew Quamme CS 151 Program 4
## Program to process loan approval and interest rate 
## for different FICO scores

def main():
    ## Send prdetermined FICO scores for processing
    approval(779)
    approval(653)
    approval(619)
        
def approval(fico):
    ## Function to take FICO score as input and
    ## calculate if loan is approved or not 
    print("FICO Score: " + str(fico))
    approval = 'Y'      # Initialize approval to Yes
    if fico >= 760:     # Determine interest rate based on FICO score
        rate = .03080
    elif fico >=700:
        rate = .03302
    elif fico >= 680:
        rate = .03479
    elif fico >= 660:
        rate = .03693
    elif fico >= 640:
        rate = .04123
    elif fico >= 620:
        rate = .04669
    else:
        approval = 'N'      # Loan not approved if FICO is < 620
        rate = 'n/a'
    output(approval, rate)      # Send approval & rate for output  

def output(approval, rate):
    ## Function to take approval value and and output approval
    ## decision and-if approved-at what interest rate
    if approval == 'Y':
        print("Loan is approved - the rate is {0:.3%}".format(rate))
    else:
        print("Loan is not approved")
main()
