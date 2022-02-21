import pandas as pd
import numpy as np



Annual_Rate = float(input("Enter the Annual Rate: "))
Number_of_periods = int(input("Enter the number of periods i.e Quarterly, Montly, ect..: "))


def function():
    EAR1 = ((1+Annual_Rate/Number_of_periods)**Number_of_periods)
    EAR2 = ((EAR1)-1)
    EAR3 = "{:.3%}".format(EAR2)
    print(f'The EAR is: {EAR3}')
function()

