from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['your_database_name']
collection = db['your_collection_name']

# Step 2: Query the collection
transactions = collection.find()

# Step 3: Retrieve base currency rate
base_currency = 'USD'  # Set your base currency code
conversion_rates = {}  # Dictionary to store conversion rates

for transaction in transactions:
    transaction_date = transaction['date']
    currency = transaction['currency']
    conversion_rate = transaction['conversion_rate']
    
    if transaction_date not in conversion_rates:
        conversion_rates[transaction_date] = {}
    
    conversion_rates[transaction_date][currency] = conversion_rate

# Step 4: Convert non-base currency transactions
total_revenue = 0

for transaction in transactions:
    transaction_date = transaction['date']
    amount = transaction['amount']
    currency = transaction['currency']
    
    if currency != base_currency:
        conversion_rate = conversion_rates[transaction_date][currency]
        amount_in_base_currency = amount * conversion_rate
    else:
        amount_in_base_currency = amount
    
    total_revenue += amount_in_base_currency

# Step 5: Calculate total revenue
print("Total revenue in base currency:", total_revenue)
