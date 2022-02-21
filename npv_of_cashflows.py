import numpy as np
import pandas as pd
import numpy_financial as npf

# Cashflows, just add more cashflows if there are more years 
cash_flow_0 = int(input('Enter year zero cash flows (enter as a negitive): '))
cash_flow_1 = int(input('Enter year 1 cash flows: '))
cash_flow_2 = int(input('Enter year 2 cash flows: '))
cash_flow_3 = int(input('Enter year 3 cash flows: '))
rate = float(input('What is the return rate: '))
total_cash_flow = (cash_flow_0, cash_flow_1, cash_flow_2, cash_flow_3)

def npvCalc():
    npv1 = npf.npv(rate, total_cash_flow)
    print(f'The NPV is: {npv1}')
npvCalc()