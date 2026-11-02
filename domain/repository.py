from abc import ABC, abstractmethod

class Repository(ABC):

    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def add(self, delivery):
        raise NotImplementedError

    @abstractmethod
    def save(self, delivery):
        raise NotImplementedError