import uuid
import typing


class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
        self.id = uuid.uuid4()

    def __repr__(self) -> str:
        return f" —> {self.data}"

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def __len__(self) -> int:
        total = 0
        if self.head is not None:
            curr_node = self.head

            while curr_node.next_node is not None:
                total += 1
                curr_node = curr_node.next_node
        return total

    def __str__(self):
        result = ""
        curr_node = self.head

        while curr_node is not None:
            result += curr_node.__repr__()
            curr_node = curr_node.next_node

        return result

    def __iter__(self) -> list:
        curr_node = self.head
        while curr_node is not None:
            yield curr_node.data
            curr_node = curr_node.next_node

    def insert_to_front(self, data):
        if data is None:
            return None

        self.head = Node(data, self.head)
        return self.head

    def append(self, data):
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

    def delete(self, data: typing.Union[Node, typing.Any]):
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
