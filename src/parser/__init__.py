import json
import base64

class Parser:
    def __init__(self, path: str):
        self.path = path

    def parse_json(self):
        cells = []
        with open(self.path, 'r') as file:
            data = json.load(file)
            for cell in data.get('cells', []):
                cell_data = {
                    'cell_type': cell.get('cell_type', ''),
                    'source': ''.join(cell.get('source', [])),
                    'formatted_source': (
                        f"""```python\n{''.join(cell.get('source', []))}\n```"""
                        if cell.get('cell_type') == 'code'
                        else ''.join(cell.get('source', []))
                    ),
                    'outputs': ''
                }

                images = []
                outputs_text = []
                for output in cell.get('outputs', []):
                    if not isinstance(output, dict):
                        continue

                    if 'text' in output:
                        outputs_text.append(''.join(output.get('text', [])))
                    elif 'data' in output:
                        data_dict = output.get('data', {})
                        if 'text/plain' in data_dict:
                            outputs_text.append(''.join(data_dict['text/plain']))
                        if 'image/png' in data_dict:
                            images.append(data_dict['image/png'])  # base64 str

                cell_data['outputs'] = ''.join(outputs_text)
                if images:
                    cell_data['images'] = images  # list of decoded bytes

                cells.append(cell_data)
        return cells

