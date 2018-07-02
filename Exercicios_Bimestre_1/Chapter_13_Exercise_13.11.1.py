
# coding: utf-8

# In[42]:


# Write a program that reads a file and writes out a new file with the lines in reversed order 
# (i.e. the first line in the old file becomes the last one in the new file.)

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

lines_stack = Stack()

file_in  = open('text_in.txt', "r")
file_out = open('text_out.txt', "w")

while True:
    line = file_in.readline()
    lines_stack.push(line)
    if (len(line)) == 0:
        break

while lines_stack.size() > 0:
    new_line = lines_stack.peek()
    lines_stack.pop()
    file_out.write(new_line)

file_in.close()
file_out.close()

