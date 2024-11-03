import nbformat

notebooks = ['Singular Notebook/ADM RQ 1-4.ipynb','Singular Notebook/rq5-7_new.ipynb', 'Singular Notebook/merged_notebook_sentiment.ipynb','Singular Notebook/algo.ipynb']
merged_notebook = nbformat.v4.new_notebook()

for nb_file in notebooks:
    with open(nb_file, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
        nb = nbformat.v4.upgrade(nb)
        nbformat.validate(nb)  
        merged_notebook.cells.extend(nb.cells)

with open('merged_notebook.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(merged_notebook, f)

print("Notebooks merged successfully ")