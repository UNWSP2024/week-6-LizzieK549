# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program

StateTax = .05
CountyTax = .025

def main():
    TotalSales = float(input("Enter the total sales for the month: "))


    #Get/call tax amounts
    state_tax = statetaxmethod(TotalSales)
    county_tax = countytaxmethod(TotalSales)

    #Calculate total
    total = state_tax + county_tax

    print("State Tax = "f"${state_tax:,.2f}")
    print("County Tax = "f"${county_tax:,.2f}")
    print("Total Tax = "f"${total:,.2f}")

def statetaxmethod(TotalSales):
    return TotalSales * StateTax
def countytaxmethod(TotalSales):
    return TotalSales * CountyTax

main()
