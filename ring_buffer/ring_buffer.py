class RingBuffer:
    def __init__(self, capacity, storage = None, increm_old = 0):
        self.capacity = capacity
        self.storage = []
        self.increm_old = increm_old

    def append(self, item):
        # if the length of the storage is less than
        # the capacity num that was passed in
        if len(self.storage) < self.capacity:
            # append passed in item into the list
            self.storage.append(item)
        # if the list is full
        else:
            # if all the current items have not been overwritten
            if self.increm_old <= (self.capacity - 1):
                # replace the oldest item
                self.storage[self.increm_old] = item
                # increment index to replace next oldest item
                self.increm_old = (self.increm_old + 1)
            # if all the current items have been overwritten
            elif self.increm_old > (self.capacity - 1):
                # set the increm_old var to 0 to replace the
                # new oldest item in the list
                self.increm_old = 0
                # replace the oldest item
                self.storage[self.increm_old] = item
                # increment index to replace next oldest item
                self.increm_old = (self.increm_old + 1)

    def get(self):
        # return list
        return self.storage