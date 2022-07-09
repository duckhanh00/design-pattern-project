from borg_singleton import BorgSingleton
from child_borg import ChildBorg
from share_borg_state import ShareBorgState

borg = BorgSingleton()
borg.shared_variable = "Shared Variable"

child_borg = ChildBorg()
share_borg_state = ShareBorgState()

# not same instance
print(child_borg is borg)
print(share_borg_state is borg)
print(share_borg_state._shared_borg_state is borg._shared_borg_state)

# same state
print(child_borg.shared_variable is borg.shared_variable)

child_borg.shared_variable = "Modify shared_variable by child_borg"
print("singleton: ", borg.shared_variable)
print("singleton: ", borg._shared_borg_state)
print("share_borg_state: ", share_borg_state._shared_borg_state)
print("share_borg_state: ", share_borg_state.shared_variable)
