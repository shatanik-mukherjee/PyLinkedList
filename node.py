#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Representation of node structure of a linked list.
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
Representation of node structure of a linked list.
"""

__author__ = "Shatanik Mukherjee"
__copyright__ = "Copyright (c) 2024"
__credits__ = ["Shatanik Mukherjee"]
__license__ = "MIT License"
__version__ = "1.0.1"
__maintainer__ = "Shatanik Mukherjee"
__email__ = "shatanikmukherjee171@gmail.com"
__status__ = "Dev"


class Node:
    """
    Represents the nodes of a linked list.
    """

    def __init__(self, value) -> None:
        self.prev = None
        self.next = None
        self.value = value
