import base64
import os

class Converter:
    def __init__(self, cells, image_dir="images"):
        self.cells = cells
        self.image_dir = image_dir
        os.makedirs(image_dir, exist_ok=True)  # ensure images folder exists

    def convert(self):
        typst_source = f"""#import "@preview/showybox:2.0.4": showybox

#let question(number, body) = context [
  #showybox(
    frame: (
      border-color: blue,
      title-color: blue,
      body-color: white,
    ),
    title-style: (
      color: white,
      weight: "bold",
      align: left,
      boxed-style: (
        radius: 4pt,
      ),
    ),
    title: [
      #smallcaps()[#text(size: 10pt, weight: "bold")[
          == Question #number
        ]]
    ],
  )[#body
    #v(1mm)
  ]
]
        """
        curr_question = 1
        img_counter = 1

        for cell in self.cells:
            if cell['cell_type'] == "code":
                typst_source += cell['formatted_source'] + "\n"
            
                if cell.get('outputs') and cell['outputs'].strip():
                    typst_source += f"""=== #smallcaps()[Output]
```txt
{cell['outputs']}
```\n"""

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

                if line.startswith("Question"):
                    qno = line.split()[1].strip(":")
                    question = line[len("Question ")+1:].strip()
                    line = f"""#question("{qno}",[{question[1:]}])"""

                typst_source += line + "\n"
                curr_question += 1

        return typst_source

