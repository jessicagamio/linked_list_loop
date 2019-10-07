

def find_loop(ll):
    """determine existence of loop"""

    #iterated through loop using two variables j and k.
    j = self.head
    k = self.head.next.next

    #while the list has no end.
    while k != None or k.next != None:

        if k == j:
            return j

        else:
            k = k.next.next
            j = j.next

    # if list has an end there is no loop.
    else:
        return False

