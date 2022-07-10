from abc import ABCMeta, abstractmethod
import copy
# https://refactoring.guru/design-patterns/prototype/python/example
# https://www.geeksforgeeks.org/prototype-method-python-design-patterns/ 

# class - Courses
class Courses(metaclass = ABCMeta):
    def __init__(self):
        self.id = None
        self.type = None
 
    @abstractmethod
    def course(self):
        pass
 
    def get_type(self):
        return self.type
 
    def get_id(self):
        return self.id
 
    def set_id(self, sid):
        self.id = sid
 
    def clone(self):
        return copy.copy(self)
    
    def deep_copy(self, memo=None):
        if memo is None:
            memo = {}
        return copy.deepcopy(self, memo)
 
# class - DSA course
class DSA(Courses):
    def __init__(self):
        super().__init__()
        self.type = "Data Structures and Algorithms"
 
    def course(self):
        print("Inside DSA::course() method")
 
# class - SDE Course
class SDE(Courses):
    def __init__(self):
        super().__init__()
        self.type = "Software Development Engineer"
 
    def course(self):
        print("Inside SDE::course() method.")
 
# class - STL Course
class STL(Courses):
    def __init__(self):
        super().__init__()
        self.type = "Standard Template Library"
 
    def course(self):
        print("Inside STL::course() method.")
 
# class - Courses At GeeksforGeeks Cache
class CoursesCache:
     
    # cache to store useful information
    cache = {}
 
    @staticmethod
    def get_course(course_id):
        course = CoursesCache.cache.get(course_id, None)
        return course.clone()
    
    @staticmethod
    def get_course_deep(course_id):
        course = CoursesCache.cache.get(course_id, None)
        return course.deep_copy()

    @staticmethod
    def load():
        sde = SDE()
        sde.set_id("1")
        CoursesCache.cache[sde.get_id()] = sde
 
        dsa = DSA()
        dsa.set_id("2")
        CoursesCache.cache[dsa.get_id()] = dsa
 
        stl = STL()
        stl.set_id("3")
        CoursesCache.cache[stl.get_id()] = stl
 
# main function
if __name__ == '__main__':
    CoursesCache.load()
    
    print("Use copy")
    sde = CoursesCache.get_course("1")
    print(sde.get_type())
 
    dsa = CoursesCache.get_course("2")
    print(dsa.get_type())
 
    stl = CoursesCache.get_course("3")
    print(stl.get_type())

    print("Use deep copy")
    sde = CoursesCache.get_course_deep("1")
    print(sde.get_type())
 
    dsa = CoursesCache.get_course_deep("2")
    print(dsa.get_type())
 
    stl = CoursesCache.get_course_deep("3")
    print(stl.get_type())