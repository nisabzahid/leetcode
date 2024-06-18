while first :
            curr = ListNode()
            curr.val =  (carry + first.val) % 10
            carry = 1 if (carry + first.val) > 9 else 0
            first = first.next
            node.next = curr
            node = node.next