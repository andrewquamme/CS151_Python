## Andrew Quamme CS 151 Program 4
## Program to process loan approval and interest rate 
## for inputted FICO scores while also 
## trying to incorperate material from Module 4

def main():
    ## Selection menu
    print("\n0. Quit   1. Get Loan Approval")
    selection = eval(input())
    if selection == 0:
        exit()
    elif selection == 1:
        fico = eval(input("Enter FICO Score: "))
        approval, rate = getApproval(fico)      # Send FICO for approval
        output(approval, rate)                  # Send approval info for output
        main()                                  # Restart the program
    else:
        print("Try again")
        main()
    
def getApproval(fico):
    ## Function to take FICO score as input and
    ## calculate if loan is approved or not.
    ## Returns a tuple containing approval Y/N and interest rate
    approval = 'Y'          # Initialize approval to Yes
    if fico >= 760:         # Determine interest rate based on FICO score
        rate = .03080
    elif fico >= 700:
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
    return (approval, rate) # Return the approval Y/N and interest rate
    
def output(approval, rate):
    ## Function to take approval Y/N and interest rate and
    ## print approval decision and-if approved-at what interest rate
    if approval == 'Y':
        print("Loan is approved - the rate is {0:.3%}".format(rate))
    else:
        print("Loan is not approved")

main()
