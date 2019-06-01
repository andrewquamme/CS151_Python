## Andrew Quamme CS 151 Program 3

def apply(fico):
    ## Function to take FICO score as input and calculate if loan is approved
    ## or not, and output if loan is approved--and at what interest rate

    approval = 'Y'      # Initialize approval to 'Y'
    if fico >= 760:     # Determine interest rate based on FICO score
        rate = .03080
    elif fico >=  700:
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
        
    if approval == 'Y':     # Output loan approval decision and interest rate
        print("Loan is approved - the rate is {0:.3%}".format(rate))
    else:
        print("Loan is not approved")


