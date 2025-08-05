from src.parser import Parser
from src.converter import Converter
import subprocess
import json

def main():
    parser = Parser("./Untitled1.ipynb")
    cells = parser.parse_json()

    for i in cells:
        print(json.dumps(i, indent=4))

    converter = Converter(cells)
    typst_source = converter.convert()


    with open("test.typ", "w") as f:
        f.write(typst_source)

    print("Conversion complete! The Typst source has been saved to test.typ")
    subprocess.run(["typst", "compile", "test.typ"])
    print("Compilation complete! The PDF has been generated.")

if __name__ == "__main__":
    main()
