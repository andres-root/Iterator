# import logging


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
        self.has_next()

    def has_next(self):
        """
        Returns true or false if there is another element in the set.
        """
        try:
            if self.current_index >= len(self.array_list):
                raise Exception('Sorry. No more items on list to show.')

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
        """
        Returns the value of the next element in the array.
        """
        try:
            if self.current_index >= len(self.array_list):
                raise Exception('Sorry. No more items on list to show.')

            if self.subindex >= len(self.current_node):
                self.has_next()

            n = self.current_node[self.subindex]
            self.subindex += 1

            return n
        except Exception as e:
            print(e)

    def remove(self):
        """
        Removes the last element returned by the iterator.
        """
        try:
            if len(self.current_node) > 0:
                del self.current_node[self.subindex - 1]
            
            self.subindex -= 1
            
            return self.current_node
        except Exception as e:
            print(e)


def test_case_1(array_list):
    """
    Test print all elements
    """
    it = Iterator(array_list)
    while (it.has_next()):
        print(it.next())

def test_case_2(array_list):
    """
    Test print all elements once
    """
    it = Iterator(array_list)
    while (it.has_next()):
        it.has_next()
        print(it.next())

def test_case_3(array_list):
    """
    Test print next element
    """
    it = Iterator(array_list)
    for i in range(20):
        print(it.next())

def test_case_4(array_list):
    """
    Test remove multiples of 3
    """
    it = Iterator(array_list)
    while (it.has_next()):
        x = it.next()
        if (x % 3 == 0):
            it.remove()
    print(array_list)
    assert array_list == [[], [1, 2], [4, 5], [], [], [], [7, 8], [], [], [10], []]

def test_case_5(array_list):
    """
    Test remove everything from the list
    """
    it = Iterator(array_list)
    while it.has_next():
        it.next()
        it.remove()
    print(array_list)
    assert array_list == [[], [], [], [], [], [], [], [], [], [], []]


if __name__ == '__main__':
    array_list = [[], [1, 2, 3], [4, 5], [], [], [6], [7, 8], [], [9], [10], []]
    
    # Scenario 1
    print('Test case 1:')
    test_case_1(array_list)
    print('===================================')
    print('Test case 2:')
    test_case_2(array_list)
    print('===================================')
    print('Test case 3:')
    test_case_3(array_list)
    print('===================================')

    # # Scenario 2
    print('Test case 4:')
    test_case_4(array_list)
    print('===================================')
    print('Test case 5:')
    test_case_5(array_list)