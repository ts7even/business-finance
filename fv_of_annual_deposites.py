import numpy as np 
import numpy_financial as npf

r = float(input("What is the intrest rate?: "))
t = int(input("what is the time?: "))
pv = int(input("What is the present value or the annual deposit? Enter as negitive: "))


def annuities():
    fv = npf.fv(r, t, pv, 0 )
    print(f'The future value from the the annual payments is: {fv}')
annuities()

# This works