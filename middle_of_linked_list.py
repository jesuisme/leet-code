"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.

https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3290/
"""

# 1. Traverse the list to determine how long it is
# 2. Find the middle node (if odd length) or the second of the middle two nodes (even length)
# 3. return the portion of the list from the middle node to the end

# May have up to 100 nodes


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, length=0, starting_point=0):
        """
        Traverse the linked list
        :param length: How many nodes to traverse; 0 means to the end
        :param starting_point: Which node to start from; 0 means the head
        :return:
        """
        output_list = []
        current_node = self.head
        if starting_point != 0:  # start from somewhere other than the head
            for i in range(starting_point):
                if current_node.next is not None:
                    current_node = current_node.next
                else:
                    break

        output_head_node = current_node
        number_of_elements = 0
        while current_node:
            output_list.append(current_node.val)
            number_of_elements += 1
            if length == number_of_elements:
                break
            else:
                current_node = current_node.next

        return number_of_elements, output_head_node, output_list


class Solution:
    def create_linked_list(self, elements):
        linked_list = LinkedList()
        current_node = None
        for idx, val in enumerate(elements):
            if idx == 0:
                linked_list.head = ListNode(val)
                current_node = linked_list.head
            else:
                current_node.next = ListNode(val)
                current_node = current_node.next

        return len(elements), linked_list

    def middleNode(self, head: ListNode) -> ListNode:
        list_to_check = LinkedList()
        list_to_check.head = head

        list_length, list_head, list_elements = list_to_check.traverse()

        # find the place to split the list in half
        second_half = list_length // 2

        final_length, final_head, output = list_to_check.traverse(starting_point=second_half)

        return final_head


if __name__ == '__main__':
    sln = Solution()
    length_of_list, my_list = sln.create_linked_list(list(range(100)))
    # length_of_list, my_list = sln.create_linked_list([1, 2, 3, 4, 5, 6])
    # length_of_list, my_list = sln.create_linked_list([1, 2, 3, 4, 5])
    length, output_head, output_list = my_list.traverse(length=3, starting_point=55)
    print(length, output_head.val, output_list)
    print('Middle')
    half_head = sln.middleNode(my_list.head)
    print(half_head.val)
