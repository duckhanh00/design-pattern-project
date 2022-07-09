from borg_singleton import BorgSingleton
class ShareBorgState(BorgSingleton):
    _shared_borg_state = {}