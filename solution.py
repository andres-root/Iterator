

def exclusive(f):
    def wrapper(*args, **kwargs):
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper


class Iterator():
    def __init__(self, array_list=[[]]):
        self.array_list = array_list
        self.current_node = array_list[0]
        self.current_index = 0
        self.subindex = 0
        
        # Init next node
        self.hasNext()

    def hasNext(self):
        try:
            while self.current_index < len(self.array_list):
                if self.subindex < len(self.current_node):
                    return True
                else:
                    self.current_node = self.array_list[self.current_index]
                    self.subindex = 0
                    self.current_index += 1
                
                    if len(self.current_node) > 0:
                        return True
            return False
        except Exception as e:
            print(e)

    def next(self):
        try:
            if self.subindex >= len(self.current_node):
                self.subindex = 0

            n = self.current_node[self.subindex]
            self.subindex += 1

            return n
        except Exception as e:
            print(e)

    def remove(self):
        try:
            if len(self.current_node) > 0:
                del self.current_node[self.subindex - 1]
            
            return self.current_node
        except Exception as e:
            print(e)


def testCase1(arrayList):
    it = Iterator(arrayList)
    while (it.hasNext()):
        print(it.next())
        continue

def testCase2(arrayList):
    it = Iterator(arrayList)
    while (it.hasNext()):
        it.hasNext()
        print(it.next())

def testCase3(arrayList):
    it = Iterator(arrayList)
    for i in range(20):
        print(it.next())

def testCase4(arrayList):
    it = Iterator(arrayList)
    while (it.hasNext()):
        x = it.next()
        if (x % 4 == 0):
            it.remove()
    print(arrayList)

def testCase5(arrayList):
    '''Remove everything from the list'''
    it = Iterator(arrayList)
    while it.hasNext():
        it.next()
        it.remove()
    print(arrayList)

arrayList = [[], [1, 2, 3], [4, 5], [], [], [6], [7, 8], [], [9], [10], []]
if __name__ == '__main__':
    # Scenario 1
    print('Test case 1:')
    testCase1(arrayList)
    print('===================================')
    print('Test case 2:')
    testCase2(arrayList)
    print('===================================')
    print('Test case 3:')
    testCase3(arrayList)
    print('===================================')

    # # Scenario 2
    print('Test case 4:')
    testCase4(arrayList)
    print('===================================')
    print('Test case 5:')
    testCase5(arrayList)