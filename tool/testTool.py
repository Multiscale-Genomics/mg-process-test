"""
.. See the NOTICE file distributed with this work for additional information
   regarding copyright ownership.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from __future__ import print_function

import sys

try:
    if hasattr(sys, '_run_from_cmdl') is True:
        raise ImportError
    from pycompss.api.parameter import FILE_OUT
    from pycompss.api.task import task
    from pycompss.api.api import compss_wait_on
except ImportError:
    print("[Warning] Cannot import \"pycompss\" API packages.")
    print("          Using mock decorators.")

    from dummy_pycompss import FILE_OUT
    from dummy_pycompss import task
    from dummy_pycompss import compss_wait_on

from basic_modules.tool import Tool
from basic_modules.metadata import Metadata
from utils import logger

# ------------------------------------------------------------------------------

class testTool(Tool):
    """
    Tool for writing to a file
    """

    def __init__(self, configuration=None):
        """
        Init function
        """
        logger.info("Test writer")
        Tool.__init__(self)

        if configuration is None:
            configuration = {}

        self.configuration.update(configuration)

    @task(file_loc=FILE_OUT)
    def test_writer(self, file_loc):
        """
        Writes a single line to a file and then returns that file

        Parameters
        ----------
        file_loc : str
            Location of an output file

        Returns
        -------
        bool
            Writes to the file, which is returned by pyCOMPSs to the defined location
        """
        with open(file_loc, "w") as file_handle:
            file_handle.write("This is the test writer")

        return True

    def run(self, input_files, input_metadata, output_files):
        """
        The main function to run the test_writer tool

        Parameters
        ----------
        input_files : dict
            List of input files - In this case there are no input files required
        input_metadata: dict
            Matching metadata for each of the files, plus any additional data
        output_files : dict
            List of the output files that are to be generated

        Returns
        -------
        output_files : dict
            List of files with a single entry.
        output_metadata : dict
            List of matching metadata for the returned files
        """

        results = self.test_writer(
            output_files['output']
        )

        results = compss_wait_on(results)

        output_metadata = {
            "output": Metadata(
                data_type="<data_type>",
                file_type="txt",
                file_path=output_files["output"],
                sources=[],
                taxon_id=9606,
                meta_data={
                    "tool": "testTool"
                }
            )
        }

        return (output_files, output_metadata)
