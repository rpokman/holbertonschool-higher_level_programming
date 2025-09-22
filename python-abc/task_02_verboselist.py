#!/usr/bin/env python3
from abc import ABC, abstractmethod

class VerboseList(list):

    def append(self, item):
        """Add a single item and print a message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Add multiple items and print a message."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove a single item and print a message."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item at a given index and print a message."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
