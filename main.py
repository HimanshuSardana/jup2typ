from src.parser import Parser
from src.converter import Converter
import json

def main():
    parser = Parser()
    cells = parser.parse_json()

    # for i in cells:
    #     print(i['source'] if i['cell_type'] == 'markdown' else '')

    converter = Converter(cells)
    typst_source = converter.convert()
    print(typst_source)

if __name__ == "__main__":
    main()
