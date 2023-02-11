# PyAnnGen: to generate type annotations for Python

The tool implementation and its results in RQ3.

### PyAnnGen Usage

Run this command to use PyAnnGen:

    python3 PyAnnGen.py <pytype_dir> <type4py_dir> <hityper_dir> <output_dir>

For example, to reproduce our results (as we provide in pyanngen_results/):

    python3 PyAnnGen.py pytype_results/ type4py_results/ hityper_results/ output_results/


**Attention：** Keep all the inputs in the same format. Notice the order of the tools on the command line, which has a big impact on the results. You can also adapt the tool to your own data based on the algorithms in the *PyAnnGen.py*.
