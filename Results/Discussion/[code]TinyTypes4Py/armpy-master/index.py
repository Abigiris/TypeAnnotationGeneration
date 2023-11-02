import csv
from item import item_id
import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")


class InvertedIndex:
    def __init__(self):
        self.index = dict()
        self.num_transactions = 0

    def add(self, transaction):
        self.num_transactions += 1
        for item in transaction:
            if not isinstance(item, int):
                raise TypeError("Item must be item id (int)")
            if item not in self.index:
                self.index[item] = set()
            self.index[item].add(self.num_transactions)

    def load(self, data):
        if not isinstance(data, str):
            raise TypeError("InvertedIndex.load() expects a string")
        for transaction in data.splitlines():
            self.add([item_id(s) for s in transaction.split(",")])

    def load_csv(self, csvFilePath):
        if not isinstance(csvFilePath, str):
            raise TypeError(
                "InvertedIndex.load_csv() expects a path as string")
        with open(csvFilePath, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                transaction = map(item_id, line)
                self.add(transaction)

    def items(self):
        return self.index.keys()

    def count(self, itemset):
        for item in itemset:
            if not isinstance(item, int):
                raise TypeError("Itemset must contain only int item ids")
        if (not isinstance(itemset, set) and
            not isinstance(itemset, frozenset) and
            not isinstance(itemset, list)):
            raise TypeError("InvertedIndex.support() expects a set of items")
        return len(set.intersection(*[self.index[i]
                                      for i in itemset]))

    def support(self, itemset):
        return self.count(itemset) / self.num_transactions