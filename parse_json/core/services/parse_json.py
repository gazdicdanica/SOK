import json

from core.services.parse import DataParserBase

from core.core.services.model import *


def loadData(fname: str):
    print(fname)
    with open(fname, 'rt', buffering=100000) as fn:
        data = fn.read()
    return json.loads(data)


class JSONParser(DataParserBase):
    def identifier(self) -> str:
        return "#JSONParser"

    def name(self) -> str:
        return "JSONParser"

    def parse(self, data: str) -> None:
        print(data)
        return None

    def parseFile(self, fname: str) -> None:
        fname = "../../test_data/data.json"
        return self.createGraph(loadData(fname))

    def createGraph(self, parsed_data):
        # return self.connectGraph(parsed_data, Graph())
        return self.connectGraph(parsed_data)

    # def connectGraph(self, current_dict, graph, parent=None):
    def connectGraph(self, current_dict, parent=None):
        v = Node()
        for key in current_dict.values():
            print(key)


if __name__ == '__main__':
    parse_json = JSONParser()
    parse_json.parseFile("")

