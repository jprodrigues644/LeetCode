""" 21. Merge Two Sorted Lists
Easy
Topics
premium lock icon
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order. """

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):         
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        temp = ListNode(0)
        current = temp
        
        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If there are remaining nodes in either list, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # Return the merged list, which starts from the next of dummy node
        return temp.next
# Example usage:
list1 = ListNode(1, ListNode(2, ListNode(4)))     
list2 = ListNode(1, ListNode(3, ListNode(4)))
solution = Solution()     
merged_list = solution.mergeTwoLists(list1, list2)
while merged_list:
    print(merged_list.val, end=" -> ")                    
    merged_list = merged_list.next                                            
# Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 ->