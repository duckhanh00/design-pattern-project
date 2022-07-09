print("execute singleton.py")
import singleton
print("shared_variable:", singleton.shared_variable)

print("execute sample_module_1.py")
import sample_module_1
print("shared_variable:", singleton.shared_variable)

print("execute sample_module_2.py")
import sample_module_2
print("shared_variable:", singleton.shared_variable)

