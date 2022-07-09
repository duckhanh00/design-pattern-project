from singleton import SingletonClass
from singleton_child import SingletonChild

# SingletonChild has the same instance of SingletonClass and also shares the same state
singleton = SingletonClass()
new_singleton = SingletonClass()
child_singleton = SingletonChild()

print(singleton is new_singleton) 
print(singleton is child_singleton)

singleton.singleton_variable = "Singleton Variable"
print("new_singleton: ", new_singleton.singleton_variable)
print("child_singleton ", child_singleton.singleton_variable)

new_singleton.singleton_variable = "Modify Singleton Variable by new_singleton"
print("singleton: ", singleton.singleton_variable)
print("child_singleton: ", child_singleton.singleton_variable)

child_singleton.singleton_variable = "Modify Singleton Variable by child_singleton"
print("singleton: ", singleton.singleton_variable)
print("new_singleton: ", new_singleton.singleton_variable)