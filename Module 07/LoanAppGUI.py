from tkinter import *

def showRate():
    ## Function to take entered FICO score and
    ## calculate if loan is approved or not.
    ## Outputs rate/denial to read only widget
    try:
        fico = eval(conOFentFICO.get())
    except SyntaxError:
        rate = 'ERROR'
        entRate["fg"]="red"
    except NameError:
        rate = 'ERROR'
        entRate["fg"]="red"
    else:
        entRate["fg"]="black"
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
    
    conOFentRate.set(rate)      # Output rate/denial into read only widget

window = Tk()
window.title("Loan App")
## Place widgets on a 3x3 grid for entering FICO, calculate button and
## output for interest rate/denial
Label(window, text="FICO Score: ").grid(row=0, column=0, pady=5, sticky=E)
conOFentFICO = StringVar()
entFICO = Entry(window, width=8, textvariable=conOFentFICO)
entFICO.grid(row=0, column=1, sticky=W)
entFICO.focus()                 # Place cursor in entry widget on load
btnCalc = Button(window, text="Calculate", command=showRate)
btnCalc.grid(row=1, column=0, columnspan=2, padx=85)
Label(window, text="Interest Rate:").grid(row=2, column=0, pady=5, sticky=E)
conOFentRate = StringVar()
entRate = Entry(window, state="readonly", width=8, textvariable=conOFentRate)
entRate.grid(row=2, column=1, sticky=W)

window.mainloop
