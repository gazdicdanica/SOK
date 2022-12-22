from abc import ABC, abstractmethod


class DataParserBase(ABC):
    @abstractmethod
    def identifier(self) -> str:
        pass


    @abstractmethod
    def name(self) -> str:
        pass


    # TODO: What is the argument and what is the return type?
    @abstractmethod
    def render(self) -> None:
        pass