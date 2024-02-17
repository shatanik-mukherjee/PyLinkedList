#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Simple pythonic implementations of singly and doubly linked lists.
################################################################################
# MIT License

# Copyright (c) 2024 Shatanik Mukherjee

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
################################################################################
# Author: Shatanik Mukherjee
# Copyright: Copyright (c) 2024
# Credits: [Shatanik Mukherjee]
# License: MIT License
# Version: 1.0.1
# Maintainer: Shatanik Mukherjee
# Email: shatanikmukherjee171@gmail.com
# Status: Dev
################################################################################

"""
Simple pythonic implementations of singly and doubly linked lists.
"""

# Generic/Built-in
from typing import Iterable, Union

# Owned
from node import Node

__author__ = "Shatanik Mukherjee"
__copyright__ = "Copyright (c) 2024"
__credits__ = ["Shatanik Mukherjee"]
__license__ = "MIT License"
__version__ = "1.0.1"
__maintainer__ = "Shatanik Mukherjee"
__email__ = "shatanikmukherjee171@gmail.com"
__status__ = "Dev"


class SinglyLinkedList:
    """
    Simple implementation of a singly linked list.

    Doesn't support negative indexing.
    """

    def __init__(
        self, x: Union["SinglyLinkedList", "DoublyLinkedList", Iterable] = None
    ) -> None:
        self.__size: int = 0
        self.shape: tuple = tuple([self.__size])
        self.__head = None
        self.__tail = None
        if x:
            if (
                not isinstance(x, SinglyLinkedList)
                and not isinstance(x, DoublyLinkedList)
                and not isinstance(x, Iterable)
            ):
                raise TypeError(f"'{type(x).__name__}' object is an invalid type")
            if isinstance(x, SinglyLinkedList) or isinstance(x, DoublyLinkedList):
                for i in range(len(x)):
                    self.append(x.get(i))
            else:
                for element in x:
                    self.append(element)

    def __len__(self) -> int:
        return self.__size

    def __str__(self) -> str:
        if not self.__head:
            return str([])
        _list = []
        current = self.__head
        while current:
            _list.append(current.value)
            current = current.next
        return str(_list)

    def size(self) -> int:
        """
        Returns the size of the linked list.
        """
        return self.__size

    def get(self, index: int):
        """
        Returns the element at a given `index` of the linked list.

        Doesn't support negative indexing; raises `IndexError` if `index` is out of range.
        """
        if not isinstance(index, int):
            raise TypeError(
                f"'{type(index).__name__}' object cannot be interpreted as an integer"
            )
        if index < 0 or index >= self.__size:
            raise IndexError("linked list index out of range")
        count = 0
        current = self.__head
        while current:
            if count == index:
                break
            current = current.next
            count += 1
        return current.value

    def index(self, x) -> int:
        """
        Returns the index of the first occurrence of an element `x` in the linked list.

        Raises `ValueError` if `x` is not present.
        """
        index = 0
        current = self.__head
        while current:
            if x == current.value:
                break
            current = current.next
            index += 1
        if not self.__head or index == self.__size:
            raise ValueError(
                f"{repr(x) if isinstance(x, str) else x} is not in the linked list"
            )
        return index

    def append(self, x) -> None:
        """
        Adds an element `x` at the end of the linked list.
        """
        node = Node(x)
        if not self.__head:
            self.__head = node
            self.__tail = node
            self.__size = 1
            self.shape = tuple([self.__size])
        else:
            self.__tail.next = node
            self.__tail = node
            self.__size += 1
            self.shape = tuple([self.__size])

    def insert(self, index: int, x) -> None:
        """
        Adds an element `x` at a given `index` of the linked list.

        Doesn't support negative indexing; when `index <= 0` then `x` is added at the beginning;

        `x` is added at the end if `index >= SinglyLinkedList.size()`.
        """
        if not isinstance(index, int):
            raise TypeError(
                f"'{type(index).__name__}' object cannot be interpreted as an integer"
            )
        if index <= 0:
            node = Node(x)
            if not self.__head:
                self.__head = node
                self.__tail = node
                self.__size = 1
                self.shape = tuple([self.__size])
            else:
                node.next = self.__head
                self.__head = node
                self.__size += 1
                self.shape = tuple([self.__size])
        elif index >= self.__size:
            self.append(x)
        else:
            node = Node(x)
            count = 0
            current = self.__head
            while current:
                if count == index - 1:
                    break
                current = current.next
                count += 1
            node.next = current.next
            current.next = node
            self.__size += 1
            self.shape = tuple([self.__size])

    def pop(self, index: Union[int, None] = None):
        """
        Removes and returns the element at a given `index` of the linked list.

        Doesn't support negative indexing; raises `IndexError` if `index` is out of range.
        """
        if index is not None and not isinstance(index, int):
            raise TypeError(
                f"'{type(index).__name__}' object cannot be interpreted as an integer"
            )
        if not self.__head:
            raise IndexError("pop from empty linked list")
        if index is None:
            if self.__size == 1:
                value = self.__head.value
                self.__head = None
                self.__size = 0
                self.shape = tuple([self.__size])
                return value
            count = 0
            current = self.__head
            while current:
                if count == self.__size - 2:
                    break
                current = current.next
                count += 1
            value = current.next.value
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            self.shape = tuple([self.__size])
            return value
        if index < 0 or index >= self.__size:
            raise IndexError("pop index out of range")
        if index == 0:
            value = self.__head.value
            self.__head = self.__head.next
            self.__size -= 1
            self.shape = tuple([self.__size])
            return value
        count = 0
        current = self.__head
        while current:
            if count == index - 1:
                break
            current = current.next
            count += 1
        value = current.next.value
        if index == self.__size - 1:
            self.__tail = current
            self.__tail.next = None
        else:
            current.next = current.next.next
        self.__size -= 1
        self.shape = tuple([self.__size])
        return value

    def remove(self, x) -> None:
        """
        Removes an element `x` from the linked list.

        Raises `ValueError` if `x` is not present.
        """
        self.pop(self.index(x))

    def extend(
        self, x: Union["SinglyLinkedList", "DoublyLinkedList", Iterable]
    ) -> None:
        "Adds the element(s) of a linked list or an iterable `x` at the end of an existing linked list."
        if (
            not isinstance(x, SinglyLinkedList)
            and not isinstance(x, DoublyLinkedList)
            and not isinstance(x, Iterable)
        ):
            raise TypeError(f"'{type(x).__name__}' object is an invalid type")
        if isinstance(x, SinglyLinkedList) or isinstance(x, DoublyLinkedList):
            for i in range(len(x)):
                self.append(x.get(i))
        else:
            for element in x:
                self.append(element)

    def reverse(self) -> None:
        """
        Reverses the order of the elements in the linked list.
        """
        _list = []
        for i in range(len(self)):
            _list.append(self.get(i))
        _list.reverse()
        self.__head = None
        for element in _list:
            self.append(element)


class DoublyLinkedList:
    """
    Simple implementation of a doubly linked list.

    Supports negative indexing.
    """

    def __init__(
        self, x: Union["DoublyLinkedList", "SinglyLinkedList", Iterable] = None
    ) -> None:
        self.__size: int = 0
        self.shape: tuple = tuple([self.__size])
        self.__head = None
        self.__tail = None
        if x:
            if (
                not isinstance(x, DoublyLinkedList)
                and not isinstance(x, SinglyLinkedList)
                and not isinstance(x, Iterable)
            ):
                raise TypeError(f"'{type(x).__name__}' object is an invalid type")
            if isinstance(x, DoublyLinkedList) or isinstance(x, SinglyLinkedList):
                for i in range(len(x)):
                    self.append(x.get(i))
            else:
                for element in x:
                    self.append(element)

    def __len__(self) -> int:
        return self.__size

    def __str__(self) -> str:
        if not self.__head:
            return str([])
        _list = []
        current = self.__head
        while current:
            _list.append(current.value)
            current = current.next
        return str(_list)

    def size(self) -> int:
        """
        Returns the size of the linked list.
        """
        return self.__size

    def get(self, index: int):
        """
        Returns the element at a given `index` of the linked list.

        Supports negative indexing; raises `IndexError` if `index` is out of range.
        """
        if not isinstance(index, int):
            raise TypeError(
                f"'{type(index).__name__}' object cannot be interpreted as an integer"
            )
        if abs(index) > self.__size or index >= self.__size:
            raise IndexError("linked list index out of range")
        if index < 0:
            count = -1
            current = self.__tail
            while current:
                if count == index:
                    break
                current = current.prev
                count -= 1
            return current.value
        count = 0
        current = self.__head
        while current:
            if count == index:
                break
            current = current.next
            count += 1
        return current.value

    def index(self, x) -> int:
        """
        Returns the index of the first occurrence of an element `x` in the linked list.

        Raises `ValueError` if `x` is not present.
        """
        index = 0
        current = self.__head
        while current:
            if x == current.value:
                break
            current = current.next
            index += 1
        if not self.__head or index == self.__size:
            raise ValueError(
                f"{repr(x) if isinstance(x, str) else x} is not in linked list"
            )
        return index

    def append(self, x) -> None:
        """
        Adds an element `x` at the end of the linked list.
        """
        node = Node(x)
        if not self.__head:
            self.__head = node
            self.__tail = node
            self.__size = 1
            self.shape = tuple([self.__size])
        else:
            node.prev = self.__tail
            self.__tail.next = node
            self.__tail = node
            self.__size += 1
            self.shape = tuple([self.__size])

    def insert(self, index: int, x) -> None:
        """
        Adds an element `x` at a given `index` of the linked list.

        Supports negative indexing; behaves exactly as the `insert()` method of list.
        """
        if not isinstance(index, int):
            raise TypeError(
                f"'{type(index).__name__}' object cannot be interpreted as an integer"
            )
        if index < 0:
            node = Node(x)
            if abs(index) >= self.__size:
                if not self.__head:
                    self.__head = node
                    self.__tail = node
                    self.__size = 1
                    self.shape = tuple([self.__size])
                else:
                    node.next = self.__head
                    self.__head.prev = node
                    self.__head = node
                    self.__size += 1
                    self.shape = tuple([self.__size])
            else:
                if not self.__head:
                    self.__head = node
                    self.__tail = node
                    self.__size = 1
                    self.shape = tuple([self.__size])
                else:
                    count = -1
                    current = self.__tail
                    while current:
                        if count == index - 1:
                            break
                        current = current.prev
                        count -= 1
                    node.next = current.next
                    current.next.prev = node
                    node.prev = current
                    current.next = node
                    self.__size += 1
                    self.shape = tuple([self.__size])
        elif index == 0:
            node = Node(x)
            if not self.__head:
                self.__head = node
                self.__tail = node
                self.__size = 1
                self.shape = tuple([self.__size])
            else:
                self.__head.prev = node
                node.next = self.__head
                self.__head = node
                self.__size += 1
                self.shape = tuple([self.__size])
        elif index >= self.__size:
            self.append(x)
        else:
            node = Node(x)
            count = 0
            current = self.__head
            while current:
                if count == index - 1:
                    break
                current = current.next
                count += 1
            node.next = current.next
            current.next.prev = node
            node.prev = current
            current.next = node
            self.__size += 1
            self.shape = tuple([self.__size])

    def pop(self, index: Union[int, None] = None):
        """
        Removes and returns the element at a given `index` of the linked list.

        Supports negative indexing; behaves exactly as the `pop()` method of list.

        Raises `IndexError` if `index` is out of range.
        """
        if index is not None and not isinstance(index, int):
            raise TypeError(
                f"'{type(index).__name__}' object cannot be interpreted as an integer"
            )
        if not self.__head:
            raise IndexError("pop from empty linked list")
        if index is None:
            if self.__size == 1:
                value = self.__head.value
                self.__head = None
                self.__size = 0
                self.shape = tuple([self.__size])
                return value
            value = self.__tail.value
            self.__tail = self.__tail.prev
            self.__tail.next = None
            self.__size -= 1
            self.shape = tuple([self.__size])
            return value
        if index < 0:
            if abs(index) > self.__size:
                raise IndexError("pop index out of range")
            if index == -1:
                value = self.__tail.value
                self.__tail = self.__tail.prev
                self.__tail.next = None
                self.__size -= 1
                self.shape = tuple([self.__size])
                return value
            if abs(index) == self.__size:
                value = self.__head.value
                self.__head.next.prev = None
                self.__head = self.__head.next
                self.__size -= 1
                self.shape = tuple([self.__size])
                return value
            count = -1
            current = self.__tail
            while current:
                if count == index:
                    break
                current = current.prev
                count -= 1
            value = current.value
            current.prev.next = current.next
            current.next.prev = current.prev
            self.__size -= 1
            self.shape = tuple([self.__size])
            return value
        if index >= self.__size:
            raise IndexError("pop index out of range")
        if index == 0:
            value = self.__head.value
            self.__head.next.prev = None
            self.__head = self.__head.next
            self.__size -= 1
            self.shape = tuple([self.__size])
            return value
        if index == self.__size - 1:
            value = self.__tail.value
            self.__tail = self.__tail.prev
            self.__tail.next = None
            self.__size -= 1
            self.shape = tuple([self.__size])
            return value
        count = 0
        current = self.__head
        while current:
            if count == index:
                break
            current = current.next
            count += 1
        value = current.value
        current.prev.next = current.next
        current.next.prev = current.prev
        self.__size -= 1
        self.shape = tuple([self.__size])
        return value

    def remove(self, x) -> None:
        """
        Removes an element `x` from the linked list.

        Raises `ValueError` if `x` is not present.
        """
        self.pop(self.index(x))

    def extend(
        self, x: Union["DoublyLinkedList", "SinglyLinkedList", Iterable]
    ) -> None:
        "Adds the element(s) of a linked list or an iterable `x` at the end of an existing linked list."
        if (
            not isinstance(x, DoublyLinkedList)
            and not isinstance(x, SinglyLinkedList)
            and not isinstance(x, Iterable)
        ):
            raise TypeError(f"'{type(x).__name__}' object is an invalid type")
        if isinstance(x, DoublyLinkedList) or isinstance(x, SinglyLinkedList):
            for i in range(len(x)):
                self.append(x.get(i))
        else:
            for element in x:
                self.append(element)

    def reverse(self) -> None:
        """
        Reverses the order of the elements in the linked list.
        """
        ptr = None
        current = self.__tail = self.__head
        while current:
            ptr = current.prev
            current.prev = current.next
            current.next = ptr
            current = current.prev
        if ptr:
            self.__head = ptr.prev
