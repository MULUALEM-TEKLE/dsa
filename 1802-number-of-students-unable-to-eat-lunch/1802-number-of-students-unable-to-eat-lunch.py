class Student : 
    def __init__(self, preference = -1) : 
        self.preference = preference 
        self.next = None


class StudentsQueue :
    def  __init__(self) : 
        self.first = Student()
        self.last = Student()
        self.first.next = self.last
        self.length = 0

    # enque
    def enqueue(self, val) : 
        new_student = Student(val)
        new_student.next = self.last
        cur = self.first
        while cur != self.last : 
            if cur.next == self.last : 
                cur.next = new_student
                self.length += 1 
                break
            cur = cur.next
        

    # deque
    def dequeue(self): 
        res = self.first.next
        self.first.next = self.first.next.next
        self.length -= 1
        return res

    # check for item
    def is_in_queue(self, preference):
        cur = self.first.next
        while cur != self.last:
            if cur.preference == preference : 
                return True
            cur = cur.next
        return False

   
    # print queue
    def print_queue(self) : 
        queue_string = ""
        cur = self.first.next 
        while cur != self.last : 
            queue_string += f"{cur.preference} -> "
            cur = cur.next
    
        print(queue_string)


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # sandwiches are in stack, add to an array in reverse order to achieve this
        sandwiches_stack = list(reversed(sandwiches))

        # students are in queue, implement a singly linkedlist queue for this 
        # with ability to remove from front and add to end
        students_queue = StudentsQueue()
        
        for preference in students : 
            students_queue.enqueue(preference)

        # check there's atleast one student who's willing to eat what is on top of the stack
        # (make it part of the queue implementation)
        # print(f"is {sandwiches_stack[len(sandwiches_stack) - 1]} in queue?  
        # ans:  {students_queue.is_in_queue(sandwiches_stack[-1])}")
        while sandwiches_stack and students_queue.is_in_queue(sandwiches_stack[-1]): 
            # if there is one proceed
            # deque from the queue and compare with the top of the stack
            student_preference = students_queue.dequeue().preference

            if student_preference == sandwiches_stack[-1] : 
            # if similar pop the stack and that's it
                sandwiches_stack.pop()
                
            # if not similar dont pop and enqueue the student back
            else : 
                students_queue.enqueue(student_preference)

        # if there's no student willing to it what is at the top of the stack then we're done
        # count the length of the queue and return that(maybe a part of the queue implementation )
        return students_queue.length

        