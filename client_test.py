import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote(['top_ask']['price'], (quote['top_bid']["price"] + quote['top_ask']['price'])/2)))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote(['top_ask']['price'], (quote['top_bid']["price"] + quote['top_ask']['price'])/2)))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio(self):
    A = 0
    B = 1
    self.assertEqual(getRatio(A,B),0)

    A = 1
    B = 0
    self.assertEqual(getRatio(A,B),None)

    A = 0
    B = 0
    self.asserEqual(getRatio(A,B), None)
    
    A = 3
    B = 2
    self.assertEqual(getRatio(A,B),1.5)




if __name__ == '__main__':
    unittest.main()
