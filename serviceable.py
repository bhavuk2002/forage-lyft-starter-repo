from abc import ABC, abstractmethod

class serviceable(ABC):
    @abstractmethod
    def need_services(self):
        pass