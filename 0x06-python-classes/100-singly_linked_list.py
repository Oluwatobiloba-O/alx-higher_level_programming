#!/usr/bin/python3
"""Represents a node in a singly linked list."""


class Node:
    """Represents a node in a singly linked list."""
    
    def __init__(self, data, next_node=None):
        """Initializes a node with given data.
        Args:
            data (int): Calls for validation from the setter.
            next_node (Node): Calls for validation from the setter.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the node's data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the node's data, must be an integer."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the node's next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""
    
    def __init__(self):
        """It initalizes an empty linked list.
        
        Args:
            head: the head of the linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """Inserts is new node in sorted order."""
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            cur = self.__head
            while (cur.next_node is not None and
                    cur.next_node.data < value):
                cur = cur.next_node
            new_node.next_node = cur.next_node
            cur.next_node = new_node

    def __str__(self):
        """returns the list in string format.

        Args:
            result: Prints the linked list, one node per line."""
        values = ""
        cur = self.__head
        while cur:
            values += str(cur.data)
            if cur.next_node:
                values += "\n"
            cur = cur.next_node
        return result
