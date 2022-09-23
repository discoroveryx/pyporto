from abc import ABC, abstractmethod


class SubAction(ABC):

    @abstractmethod
    def run(self):
        ...
