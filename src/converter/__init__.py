class Converter:
    def __init__(self, cells):
        self.cells = cells

    def convert(self):
        typst_source = f"""
        #let question(number, body) = [
            #smallcaps()[Question #number]
            #body
        ]
        """
        curr_question = 1
        for cell in self.cells:
            if cell['cell_type'] == "code":
                typst_source += cell['formatted_source'] + "\n"
            
                if cell['outputs'] and cell['outputs'].strip():
                    typst_source += f"""
                    === Output
                    ```txt
                    {cell['outputs']}
                    ```
                    """
            else:
                # cell type is markdown
                line = cell['source']
                line = line.replace("#", "=")

                if line.startswith("Question"):
                    qno = line.split()[1].strip(":")
                    question = line[len("Question "):].strip()
                    line = f"""#question("{qno}","{question[1:]}")"""

                typst_source += line + "\n"
                curr_question += 1

        return typst_source

