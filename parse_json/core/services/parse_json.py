from core.services.parse import DataParserBase


class JSONParser(DataParserBase):
    def identifier(self) -> str:
        return "#JSONParser"


    def name(self) -> str:
        return "JSONParser"


    def parse(self, data: str) -> None:
        print(data)
        return None


    def parseFile(self, fname: str) -> None:
        print(fname)
        return None