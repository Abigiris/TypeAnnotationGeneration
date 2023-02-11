# Dataset

All the Python projects used in our study are from [ManyTypes4Py](https://github.com/saltudelft/many-types-4-py-dataset "ManyTypes4Py"). But since we only trust the type annotations provided by developers, we need to filter the Python projects in it.

- We remove projects that are not accessible, such as those deleted by repository owners.
- We only take the latest version of a multi-version project, because these versions are almost duplicates. 
- We remove projects that do not contain any developer-provided type annotations, even though tools could handle them.
- We remove a few projects that the tools could not handle, such as crashes in the inference process.

There are 3,379 projects left, containing 125,254 Python files and 691,843 functions. Our carefully-cleaned dataset is stored in *projects-cleaned.txt* and you can download the complete data from [here](https://drive.google.com/drive/folders/1QCX7aI56pjBLTfhjJVEt98iVDwIrLjA5). Our selection criteria are based on the source code and evaluated tools. As the software is constantly updated, you can also use the initial de-duplicated project list stored in *projects-raw* to build a new dataset.

