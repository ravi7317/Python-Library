class Node:
	"""A node in a singly linked list."""

	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList:
	"""A basic singly linked list."""

	def __init__(self):
		self.head = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self.head is None

	def prepend(self, value):
		node = Node(value)
		node.next = self.head
		self.head = node
		self._size += 1

	def append(self, value):
		node = Node(value)
		if self.head is None:
			self.head = node
		else:
			current = self.head
			while current.next is not None:
				current = current.next
			current.next = node
		self._size += 1

	def find(self, value):
		current = self.head
		while current is not None:
			if current.value == value:
				return current
			current = current.next
		return None

	def delete(self, value):
		"""Remove the first matching value; return whether it was found."""
		previous = None
		current = self.head
		while current is not None:
			if current.value == value:
				if previous is None:
					self.head = current.next
				else:
					previous.next = current.next
				self._size -= 1
				return True
			previous = current
			current = current.next
		return False

	def to_list(self):
		values = []
		current = self.head
		while current is not None:
			values.append(current.value)
			current = current.next
		return values

	def __iter__(self):
		current = self.head
		while current is not None:
			yield current.value
			current = current.next

	def __str__(self):
		return " -> ".join(map(str, self)) + " -> None"
