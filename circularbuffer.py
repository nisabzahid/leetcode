class RingBuffer:
    def __init__(self, size=0):
        self.size = size
        self.oldest_position=-1
        self.buffer=[None] * self.size
    def get(self):
        return self.buffer
    def set_char(self, char):
        self.oldest_position = (self.oldest_position + 1) % self.size
        self.buffer[self.oldest_position] = char
       
    def __str__(self):
        return " ".join(filter(lambda x: x is not None , self.buffer)) if self.buffer else " empty buffer"
buffer = RingBuffer(4)
print(buffer.get())
for i in range(6):
    print(i)
    buffer.set_char(str(i))
    print(buffer)
print(buffer)

        
