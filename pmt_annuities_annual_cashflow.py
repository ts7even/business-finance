import numpy as np 
import numpy_financial as npf

r = float(input("What is the intrest rate?: "))
t = int(input("what is the time?: "))
pv = int(input("What is the present value? Enter as negitive: "))


def annuities():
    pmt = npf.pmt(r, t, pv, 0 )
    print(f'The annual cash flow from the annuity is: {pmt}')
annuities()

# Works perfectly