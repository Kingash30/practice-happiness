from datetime import datetime, tzinfo, timezone
import pymongo 
from bson import ObjectId
import matplotlib.pyplot as plt

client = ('mongodb+srv')

result = client['conscent']['purchases'].aggregate([
    {
        '$match': {
            'clientId': ObjectId('615416e390b3f82052063f17'), 
            'createdAt': {
                '$gte': datetime(2021, 9, 29, 7, 33, 55, tzinfo=timezone.utc), 
                '$lt': datetime(2023, 6, 8, 0, 0, 0, tzinfo=timezone.utc)
            }
        }
    }, {
        '$addFields': {
            'createdAt': {
                '$dateToString': {
                    'format': '%Y-%m-%d',
                    'date': '$createdAt'
                }
            }
        }
    }, {
        '$group': {
            '_id': '$createdAt', 
            'fieldN': {
                '$sum': '$price'
            }
        }
    }
])

results = list(client.aggregate(result))

dates = [result['_id'] for result in results]
purchases = [result['totalPurchases'] for result in results]

plt.bar(dates, purchases)
plt.xlabel("Date")
plt.ylabel("Total Purchases")
plt.title("Total Daily Purchases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
