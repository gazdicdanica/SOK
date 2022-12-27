from abc import ABC, abstractmethod
from model import *
# TODO: parse should return graph type.

class DataParserBase(ABC):
    @abstractmethod
    def identifier(self) -> str:
        pass


    @abstractmethod
    def name(self) -> str:
        pass


    @abstractmethod
    def parse(self, data: str) -> Graph:
        pass


    @abstractmethod
    def parseFile(self, fname: str) -> None:
        pass