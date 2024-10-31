import nbformat

notebooks = ['english_sentiment.ipynb','chinese-sentiment_log.ipynb', 'rus_sentiment.ipynb','analysis-sentiments-datasets-fin.ipynb']
merged_notebook = nbformat.v4.new_notebook()

for nb_file in notebooks:
    with open(nb_file, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
        nb = nbformat.v4.upgrade(nb)
        nbformat.validate(nb)  
        merged_notebook.cells.extend(nb.cells)

with open('merged_notebook_sentiment.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(merged_notebook, f)

print("Notebooks merged successfully ")