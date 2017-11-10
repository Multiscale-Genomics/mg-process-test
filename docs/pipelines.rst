Pipelines
=========

Test Tool
---------
.. automodule:: process_test

   This is a demonstration pipeline using the testTool.

   Running from the command line
   =============================

   Parameters
   ----------
   config : file
      Location of the config file for the workflow
   in_metadata : file
      Location of the input list of files required by the process
   out_metadata : file
      Location of the output results.json file for returned files

   Returns
   -------
   output : file
      Text file with a single entry

   Example
   -------
   When using a local verion of the [COMPS virtual machine](http://www.bsc.es/computer-sciences/grid-computing/comp-superscalar/downloads-and-documentation):

   .. code-block:: none
      :linenos:

      cd /home/compss/code/mg-process-test
      runcompss --lang=python process_test.py --config /home/compss/code/mg-process-test/tool_config/process_test.json --in_metadata /home/compss/code/mg-process-test/tests/json/input_test.json --out_metadata /home/compss/code/mg-process-test/tests/results.json

   Methods
   =======
   .. autoclass:: process_test.process_test
      :members:
