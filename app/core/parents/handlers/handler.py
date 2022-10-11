from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def run(self):
        ...
