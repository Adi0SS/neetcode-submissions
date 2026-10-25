import threading
class Singleton:
    _instance_lock = threading.Lock()

    # In python consider this method as the 'getInstance'
    _unique_instance = None
    def __new__(cls):
        if cls._unique_instance is None:
            with cls._instance_lock:
                if cls._unique_instance is None:
                    cls._unique_instance = super(Singleton, cls).__new__(cls)
                    cls._unique_instance._init_Singleton()
        return cls._unique_instance

    def _init_Singleton(self):
        self.value = None

    def getValue(self) -> str:
        return self.value
        

    def setValue(self, value: str):
        self.value = value

