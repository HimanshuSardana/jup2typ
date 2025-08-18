import argparse
import subprocess
import json

from src.parser import Parser
from src.converter import Converter

def main():
    arg_parser = argparse.ArgumentParser(description="Convert Jupyter notebook to Typst and compile to PDF.")
    arg_parser.add_argument('-p', '--path', required=True, help="Path to the input .ipynb file")
    arg_parser.add_argument('-o', '--output', default="output.typ", help="Path to the output .typ file (default: output.typ)")
    args = arg_parser.parse_args()

    parser = Parser(args.path)
    cells = parser.parse_json()

    for i in cells:
        print(json.dumps(i, indent=4))

    converter = Converter(cells)
    typst_source = converter.convert()

    with open(args.output, "w") as f:
        f.write(typst_source)

    print(f"Conversion complete! The Typst source has been saved to {args.output}")

    subprocess.run(["typst", "compile", args.output])
    print("Compilation complete! The PDF has been generated.")

if __name__ == "__main__":
    main()

