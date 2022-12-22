from core.services.parse import DataParserBase


class YAMLParser(DataParserBase):
    def identifier(self) -> str:
        return "#YAMLParser"


    def name(self) -> str:
        return "YAMLParser"


    def parse(self, data: str) -> None:
        print(data)
        return None


    def parseFile(self, fname: str) -> None:
        print(fname)
        return None