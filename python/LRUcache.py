#wE Implement the node class first : 

class Node :
     def __init__(self, key, value):  
        self.key, self.value = key, value
        self.prev = None
        self.next = None

        
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next =  self.right
        self.right.prev = self.left  # lru pour le moins recent mru pour le plus recent
      
    # Pour retirer un noeud (au milieu)  
    def remove (self, node) : 
        next , prev  = node.next , node.prev 
        prev.next = next
        next.prev = prev 
        
    # Insersion à droite 
    
    def insert (self , node) : 
        prev , next = self.right.prev , self.right
        prev.next = node 
        next.prev = node 
        node.prev = prev
        node.next = next
        #self.right.prev = node
        
        
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        val = -1 
        #On recoit une cle , et la valeur selectionné devient la nouvelle valeur mru
        
        # si la cle existe on return sa valeur
        
        if key in self.cache: 
            val = self.cache[key].value
            self.remove( self.cache[key]) 
            self.insert(self.cache[key])
        
        return val
        

    def put(self, key, value):
        if key in self.cache :
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)> self.capacity:
             lru = self.left.next
             self.remove(lru)
             del self.cache[lru.key]
        


import unittest

class TestLRUCache(unittest.TestCase):
    def test_example_1(self):
        lru = LRUCache(2)
        results = []

        lru.put(1, 1)  # {1=1}
        results.append(None)

        lru.put(2, 2)  # {1=1, 2=2}
        results.append(None)

        results.append(lru.get(1))  # return 1 → {2=2, 1=1}

        lru.put(3, 3)  # evicts 2 → {1=1, 3=3}
        results.append(None)

        results.append(lru.get(2))  # return -1

        lru.put(4, 4)  # evicts 1 → {3=3, 4=4}
        results.append(None)

        results.append(lru.get(1))  # return -1
        results.append(lru.get(3))  # return 3
        results.append(lru.get(4))  # return 4

        expected = [None, None, 1, None, -1, None, -1, 3, 4]
        self.assertEqual(results, expected)

if __name__ == "__main__":
    unittest.main()