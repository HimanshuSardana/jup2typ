from src.parser import Parser
import json

def main():
    parser = Parser()
    cells = parser.parse_json()
    
    print(f"{json.dumps(cells, indent=2)}")

if __name__ == "__main__":
    main()
