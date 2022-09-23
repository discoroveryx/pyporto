from abc import ABC, abstractmethod


class Action(ABC):

    @abstractmethod
    def run(self):
        ...
