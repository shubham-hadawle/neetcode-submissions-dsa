class MinStack:
	def __init__(self):
		self.stack = []
		self.minStack = []		# Use a MinStack to keep a track of the minimum element while elements are pushed & popped out of the normal stack
		
	def push(self, val: int) -> List:
		self.stack.append(val)
		if self.minStack:
			self.minStack.append(min(val, self.minStack[-1]))
		else:
			self.minStack.append(val)
		return None
		
	def pop(self) -> int:
		val = self.stack.pop()
		self.minStack.pop()
		return val
		
	def top(self) -> int:
		val = self.stack[-1]
		return val
		
	def getMin(self) -> int:
		minVal = self.minStack[-1]
		return minVal