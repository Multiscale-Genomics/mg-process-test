# mg-process-test



Example pipelines file that is ready to run in the VRE matching the code in the HowTo documentation

# Requirements
- pyenv and pyenv-virtualenv
- Python 2.7.12
- Python Modules:
  - pylint
  - pytest
  - mg-tool-api

Installation
------------

For a guide to the full installation procedure the see [ReadTheDocs](http://mg-process-fastq.readthedocs.io).

Directly from GitHub:

.. code-block:: none
   :linenos:

   cd ${HOME}/code

   git clone https://github.com/Multiscale-Genomics/mg-process-test.git

   cd mg-process-test

Create the Python environment

.. code-block:: none
   :linenos:

   pyenv-virtualenv 2.7.12 mg-process-test
   pip install -e .
   pip install -r requirements.txt
