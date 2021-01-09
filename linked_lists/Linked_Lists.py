import uuid
from typing import Any, Optional


class Node:

    def __init__(self, data: Any, next_node: "Node" = None):
        self.data = data
        self.next_node = next_node
        self.id = uuid.uuid4()

    def __repr__(self) -> str:
        return f" —> {self.data}"

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:

    def __init__(self, head: Optional[Node] = None):
        self.head = head

    def __len__(self) -> int:
        total = 0
        if self.head is not None:
            curr_node = self.head

            while curr_node.next_node is not None:
                total += 1
                curr_node = curr_node.next_node
        return total

    def __str__(self) -> str:
        result = ""
        curr_node = self.head

        while curr_node is not None:
            result += curr_node.__repr__()
            curr_node = curr_node.next_node

        return result

    def __iter__(self) -> iter:
        curr_node = self.head
        while curr_node is not None:
            yield curr_node.data
            curr_node = curr_node.next_node

    def insert_to_front(self, data: Any) -> Optional[Node]:
        if data is None:
            return None

        self.head = Node(data, self.head)
        return self.head

    def append(self, data: Any) -> Optional[Node]:
        if data is None:
            return None

        node = Node(data=data)

        if self.head is None:
            self.head = node
            return node

        curr_node = self.head
        while curr_node.next_node is not None:
            curr_node = curr_node.next_node

        curr_node.next_node = node
        return node

    def delete(self, data: Any) -> Optional[Node]:
        if data is None or self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        prev_node = self.head
        curr_node = self.head.next_node
        while curr_node is not None:

            if curr_node.data == data:
                prev_node.next_node = curr_node.next_node
                return curr_node

            prev_node = curr_node
            curr_node = curr_node.next
