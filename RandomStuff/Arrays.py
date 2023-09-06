#func to find if an element exists within an array
# def find(self, item = 2):
#     for j in range(self.nItems):
#         if self._a[j] == item:
#             return j
#     return -1

# def search(self, item=2):
#     return self.get(self.find(item)) 




#array items are stored in a private instance and numb of items stored in array is public (nItems)
class Array(object):

    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.nItems = 0
    
    def insert(self, item):
        self.__a[self.nItems] = item
        self.nItems += 1
    
    def search(self, item):
        for j in range(self.nItems):
            if self.__a[j] == item:
                return self.__a[j]
        return None
    
    def delete(self, item):
        for j in range(self.nItems):
            if self.__a[j] == item:
                for k in range(j, self.nItems):
                    self.__a[k] = self.__a[k + 1] #move items from right over 1
                self.nItem -= 1
        return False

    def traverse(self, function=print): #traverse all items and apply a function
        for j in range(self.nItems):
            function(self.__a[j])

    
    def find (self, item):
        lo = 0
        hi = len(self.nItems) - 1

        while lo <= hi:
            mid = (hi + lo) // 2
            if self.__a[mid] == item:
                return mid
            elif self.__a[mid] > item:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo # if item not found, return insertion point instead


smallest = None
print("Before:", smallest)
for i in [3, 41, 12, 9, 74, 15]:
    if smallest is None or i < smallest:
        smallest = i
    print("Loop:", i, smallest)
print("Smallest:", smallest)

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
print(parts)
n = parts[1]