class propertyCalculator():

    def __init__(self, rentalIncome, expenses, cashFlow, RoI):
        self.rentalIncome = rentalIncome
        self.expenses = expenses
        self.cashFlow = cashFlow
        self.RoI = RoI


## Rental Income
    def takeRentalIncome(self):
        newRentalIncome = input('Enter your rental Income: ')
        self.rentalIncome = float(newRentalIncome)

# Expenses
    def takeExpenses(self):
        newExpenses = input('Enter your expenses: ')
        self.expenses = float(newExpenses)

# Cash flow = Rental Income - Expenses

    def calculateCashFlow(self):
        self.cashFlow = self.rentalIncome - self.expenses
        print(f'Your total cash flow is  {self.cashFlow} per month')
        self.cashFlow = self.cashFlow * 12

# Cash on Cash RoI = Cash Flow / Investment

    def RoICalculator(self):
        investment = input('Enter the total amount of investment you have in the property')
        RoI = (self.cashFlow / float(investment)) * 100
        print(f'Your total RoI is {RoI}')

initalValues = propertyCalculator(0.0,0.0,0.0,0.0)

def run():
    while True:
        response = input('What would you want to do, (rental/expenses/cashflow/roi/quit): ')

        if response.lower() == 'quit':
            print('Thanks for using the calculator')
            break
        elif response.lower() == 'rental':
            initalValues.takeRentalIncome()
        elif response.lower() == 'expenses':
            initalValues.takeExpenses()
        elif response.lower() == 'cashflow':
            initalValues.calculateCashFlow()
        elif response.lower() == 'roi':
            initalValues.RoICalculator()
        else:
            print('Invalid command')

run()

