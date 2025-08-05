import json

FILE_PATH = "./test.json"

class Parser:
    def __init__(self, path: str = FILE_PATH):
        self.path = path

    def parse_json(self):
        cells = []
        with open(self.path, 'r') as file:
            data = json.load(file)
            for cell in data.get('cells', []):
                cells.append({
                    'cell_type': cell.get('cell_type', ''),
                    'source': ''.join(cell.get('source', [])),
                    'formatted_source': f"""```python\n{''.join(cell.get('source', []))}\n```""" if cell['cell_type'] == 'code' else cell.get('source', ''),
                })
        return cells
