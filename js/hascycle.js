
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */

function ListNode(val) {
     this.val = val;
      this.next = null; }
 
var hasCycle = function(head) {
    let slow = head;
    let fast = head;

    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;

        if (slow === fast) return true; 
    }

    return false; 
};

 
// Example usage
    const head = new ListNode(3);
     head.next = new ListNode(2);   
    head.next.next = new ListNode(0);
    head.next.next.next = new ListNode(-4);
    head.next.next.next.next = head.next; // creates a cycle    
    console.log(hasCycle(head)); // should return true