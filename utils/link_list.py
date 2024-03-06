class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self) -> str:
        if self.next is None:
            return f'ListNode({self.val})'
        return f'ListNode({self.val}, {self.next})'


def build_link_list(nums: list[int]):
    current = ListNode(nums[0])
    head = current

    for num in nums[1:]:
        node = ListNode(num)
        current.next = node
        current = node

    return head


# link_list = build_link_list([3, 2, 0, -4])
# print(link_list)
