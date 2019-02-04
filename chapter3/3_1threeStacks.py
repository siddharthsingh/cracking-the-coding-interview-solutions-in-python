class stack():

    def __init__(self,size,number_of_stacks):
        """

        :param size: Size of the array to use for the stacks
        :param number_of_stacks: Number of stacks to fit in this array
        """
        if not size:raise ValueError
        self.number_of_stacks = number_of_stacks
        self.stacks = [None]*size
        self.total_elements = 0
        self.stack_base = []
        self.stack_top = []
        size_of_each = size//number_of_stacks
        for i in range(number_of_stacks):
            self.stack_base.append((i*size_of_each)-1)
            self.stack_top.append((i*size_of_each)-1)

    def empty(self,stack_number):
        """

        :param stack_number: type: int: Number of the stack for which we are checking emptiness
        :return: boolean :
        """

        if self.stack_base[stack_number] == self.stack_top[stack_number]:
            return True
        return False

    def push(self,stack_number,value):
        if self.total_elements == len(self.stacks):
            raise OverflowError
        if self.stack_top[stack_number] == len(self.stacks) and self.stack_base[(stack_number+1)%self.number_of_stacks] == -1:
            self.copy_forward((stack_number + 1)%self.number_of_stacks)
        elif self.stack_top[stack_number] >= self.stack_base[(stack_number+1)%self.number_of_stacks] and self.stack_base[(stack_number+1)%self.number_of_stacks] != -1:
#             ToDo: copy element forward
            self.copy_forward(stack_number+1)
        self.stack_top[stack_number] = (self.stack_top[stack_number]+1)%len(self.stacks)
        self.stacks[self.stack_top[stack_number]] = value
        self.total_elements+=1

    def copy_forward(self,stack_number):
        if self.stack_top[stack_number] >= self.stack_base[(stack_number + 1) % self.number_of_stacks]:
            self.copy_forward((stack_number+1)%self.number_of_stacks)

        stack_base = self.stack_base[stack_number]
        stack_top = self.stack_top[stack_number]
        if stack_base == stack_top:
            self.stack_base[stack_number] += 1
            self.stack_top[stack_number] += 1
            return

        self.stacks[stack_base+2:stack_top+2] = self.stacks[stack_base+1:stack_top+1]
        self.stack_base[stack_number] += 1
        self.stack_top[stack_number] += 1



stack_ = stack(9,3)
print(stack_.stacks)
stack_.push(0,1)
stack_.push(2,2)
stack_.push(1,1)
stack_.push(2,2)
stack_.push(2,2)
# stack_.push(2,2)

print(stack_.stacks)
