import base64
import re
import os

class Converter:
    def __init__(self, cells, image_dir="images"):
        self.cells = cells
        self.image_dir = image_dir
        self.template_src = "./templates/template_3.typ"
        os.makedirs(image_dir, exist_ok=True)  # ensure images folder exists

    def convert(self):
        template_src = ""
        if os.path.exists(self.template_src):
            with open(self.template_src, "r") as f:
                template_src = f.read()
        else:
            raise FileNotFoundError(f"Template file not found: {self.template_src}")

        typst_source = template_src
        curr_question = 1
        img_counter = 1

        for cell in self.cells:
            if cell['cell_type'] == "code":
                typst_source += f"""
                #solution()[{cell['formatted_source']}]
                """
            
                if cell.get('outputs') and cell['outputs'].strip():
                    typst_source += f"""#output()[```txt
{cell['outputs'].strip()}
                    ```]\n"""

                if "images" in cell:
                    for img_b64 in cell['images']:
                        img_data = base64.b64decode(img_b64)  # decode here
                        img_filename = os.path.join(self.image_dir, f"cell_{img_counter}.png")
                        with open(img_filename, "wb") as f:
                            f.write(img_data)
                        typst_source += f"""#align(center)[#image("{img_filename}", width: 80%)]\n"""
                        img_counter += 1

            else:
                line = cell['source']
                line = line.replace("#", "=")

                if line.startswith("Title"):
                    title = line.split("Title:")[1].strip()
                    typst_source += f"#title(\"{title}\")\n"

                else:
                    match = re.match(r"Question\s+(\d+):\s*(.*)", line)
                    if match:
                        qno = match.group(1)
                        question = match.group(2)
                        line = f"""#question("{qno}",[{question}])"""

                    typst_source += line + "\n"
                    curr_question += 1

        return typst_source

