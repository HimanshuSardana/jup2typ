class Converter:
    def __init__(self, cells):
        self.cells = cells

    def convert(self):
        typst_source = ""
        """
        Convert cells to typst source code.
        """
        for cell in self.cells:
            if cell['cell_type'] == "code":
                typst_source += cell['formatted_source'] + "\n"
            else:
                # cell type is markdown
                line = cell['source']
                line = line.replace("#", "=")

                if line.startswith("="):
                    line = f"""#question(number: "1", body: {line})"""

                typst_source += line + "\n"

        return typst_source

