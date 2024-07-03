import os
import nbformat
from pathlib import Path

def notebookExtractor(fileNames: list, sourceDir: str, outputDir: str):
    for fileName in fileNames:
        try:
            # read notebook file
            nb = nbformat.read(f"{sourceDir}/{fileName}", as_version=4)
        except Exception as e:
            raise Exception(e)

        # extract code from cell
        user_code = ''
        for cell in nb.cells:
            # only reads cell with type 'code' and not having "# EXCLUDE THIS CELL" flag
            if cell.cell_type == 'code' and '# EXCLUDE THIS CELL' not in cell.source:
                # append code strings
                user_code += cell.source + '\n\n'

        # generate output file
        output_path = os.path.join(
            outputDir,  # folder name in current directory
            f"{Path(fileName).stem}.py" # extract filename from extension
        )   

        with open(output_path, mode='w', encoding='utf-8') as f:
            f.write(user_code)
    
    return None