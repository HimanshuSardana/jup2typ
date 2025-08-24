# jup2typ
A simple script I wrote to convert Jupyter Notebooks into Typst documents. (so i could stop having to manually copy paste code snippets and outputs)

## Usage
```txt
usage: main.py [-h] -p PATH [-o OUTPUT] [-t TEMPLATE] [-c COLOR]

Convert Jupyter notebook to Typst and compile to PDF.

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  Path to the input .ipynb file
  -o OUTPUT, --output OUTPUT
                        Path to the output .typ file (default: output.typ)
  -t TEMPLATE, --template TEMPLATE
                        Path to the Typst template file (optional)
  -c COLOR, --color COLOR
                        Color for the Typst document (default: blue)
```

## Themes
There are currently a total of 4 themes

The script turns a plain Jupyter Notebook  
![Default Notebook](assets/notebook.png) 

into a Typst document with one of the following themes:

<details>
<summary>Theme 1</summary>

![Template 1](assets/temp_1.png)

</details>

<details>
<summary>Theme 2</summary>

![Template 2](assets/temp_2.png)

</details>

<details>
<summary>Theme 3</summary>

![Template 3](assets/temp_3.png)

</details>

<details>
<summary>Theme 4</summary>

![Template 4](assets/temp_4.png)

</details>

### TODOs
- [x] Add templates
- [ ] Add title page option
- [ ] Add interactive mode

