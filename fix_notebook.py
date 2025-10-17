import json
import sys

if len(sys.argv) != 2:
    print("Usage: python fix_notebook.py Notebook.ipynb")
    sys.exit(1)

filename = sys.argv[1]
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Remove widgets metadata
notebook['metadata'].pop('widgets', None)

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2)

print(f"Fixed metadata for {filename}")
