import requests

class curr_converter():

    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']
 
    def convert(self, curr1, curr2, amount):
        initial_amount = amount    
        if curr1 != 'USD':
            amount = amount / self.currencies[curr1]
        amount = round(amount * self.currencies[curr2], 4)
        return amount
        

def converter(curr1, curr2, amount):
    try:
        url1 = 'https://api.exchangerate-api.com/v4/latest/USD'  
        converter = curr_converter(url1)
        return converter.convert(curr1, curr2, amount)
    except:
        return "Connection Error"