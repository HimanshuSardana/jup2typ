import os
import base64
import re
from typing import List, Dict, Any

class Converter:
    """
    Converter class for transforming notebook cell data into Typst source format.

    Attributes:
        cells (list[dict]): List of cell dictionaries containing notebook data.
        image_dir (str): Directory to save extracted images.
        template_src (str): Path to the Typst template file.
        color (str): Color theme to use in the Typst output.
    """

    def __init__(
        self,
        cells: list[dict],
        image_dir: str = "images",
        template_src: str = "./templates/template_1.typ",
        color: str = "blue"
    ):
        """
        Initialize the Converter.

        Args:
            cells (list[dict]): List of notebook cell data.
            image_dir (str, optional): Directory for saving images. Defaults to "images".
            template_src (str, optional): Path to Typst template. Defaults to "./templates/template_1.typ".
            color (str, optional): Color theme for Typst output. Defaults to "blue".
        """
        self.cells = cells
        self.image_dir = image_dir
        self.template_src = template_src
        self.color = color
        os.makedirs(self.image_dir, exist_ok=True)

    def convert(self) -> str:
        """
        Convert the notebook cells to Typst source format.

        Returns:
            str: The generated Typst source as a string.

        Raises:
            FileNotFoundError: If the template file does not exist.
        """
        if not os.path.exists(self.template_src):
            raise FileNotFoundError(f"Template file not found: {self.template_src}")

        with open(self.template_src, "r") as f:
            typst_source = f.read()

        typst_source = typst_source.replace("blue", self.color)
        curr_question = 1
        img_counter = 1

        for cell in self.cells:
            if cell.get('cell_type') == "code":
                typst_source += (
                    f"\n#solution()[{cell.get('formatted_source', '')}]\n"
                )

                outputs = cell.get('outputs', '').strip()
                if outputs:
                    typst_source += (
                        f"#output()[```txt\n{outputs}\n```\n]\n"
                    )

                for img_b64 in cell.get('images', []):
                    img_data = base64.b64decode(img_b64)
                    img_filename = os.path.join(self.image_dir, f"cell_{img_counter}.png")
                    with open(img_filename, "wb") as img_file:
                        img_file.write(img_data)
                    typst_source += (
                        f'#align(center)[#image("{img_filename}", width: 80%)]\n'
                    )
                    img_counter += 1

            else:
                line = cell.get('source', '').replace("#", "=")

                if line.startswith("Title"):
                    title = line.split("Title:")[1].strip()
                    typst_source += f"#title(\"{title}\")\n"
                else:
                    match = re.match(r"Question\s+(\d+):\s*(.*)", line)
                    if match:
                        qno = match.group(1)
                        question = match.group(2)
                        line = f'#question("{qno}",[{question}])'
                    typst_source += line + "\n"
                    curr_question += 1

        return typst_source
