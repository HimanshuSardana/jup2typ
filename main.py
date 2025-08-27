import argparse
import subprocess
from src.parser import Parser
from src.converter import Converter

def main():
    """
    Main entry point for the Jupyter to Typst converter.

    Parses command-line arguments to specify the input Jupyter notebook (.ipynb),
    output Typst file (.typ), optional Typst template, and color theme.
    Converts the notebook to Typst source, writes it to a file, and compiles it to PDF.

    Command-line arguments:
        -p, --path:        Path to the input .ipynb file (required)
        -o, --output:      Path to the output .typ file (default: output.typ)
        -t, --template:    Path to the Typst template file (optional)
        -c, --color:       Color for the Typst document (default: blue)
        -i, --interactive: Enable interactive mode (default: False)
    """
    arg_parser = argparse.ArgumentParser(description="Convert Jupyter notebook to Typst and compile to PDF.")
    _ = arg_parser.add_argument('-p', '--path', required=True, help="Path to the input .ipynb file")
    _ = arg_parser.add_argument('-o', '--output', default="output.typ", help="Path to the output .typ file (default: output.typ)")
    _ = arg_parser.add_argument('-t', '--template', default=None, help="Path to the Typst template file (optional)")
    _ = arg_parser.add_argument('-c', '--color', default="blue", help="Color for the Typst document (default: blue)")
    _ = arg_parser.add_argument('-i', '--interactive', default=False, action='store_true', help="Enable interactive mode (default: False)")
    args = arg_parser.parse_args()

    if args.interactive:
        print("Interactive mode is not implemented in this version.")
        return

    parser = Parser(args.path)
    cells = parser.parse_json()

    converter = Converter(cells=cells, template_src=args.template if args.template else "./templates/template_1.typ", color=args.color)
    typst_source = converter.convert()

    with open(args.output, "w") as f:
        _ = f.write(typst_source)

    print(f"Conversion complete! The Typst source has been saved to {args.output}")

    _ = subprocess.run(["typst", "compile", args.output])
    print("Compilation complete! The PDF has been generated.")

if __name__ == "__main__":
    main()
