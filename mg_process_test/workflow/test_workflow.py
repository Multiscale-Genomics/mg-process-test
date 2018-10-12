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

from basic_modules.workflow import Workflow
from utils import logger

from mg_process_test.tool.testTool import testTool

# ------------------------------------------------------------------------------


class process_test(Workflow):  # pylint: disable=invalid-name,too-few-public-methods
    """
    Functions for demonstrating the pipeline set up.
    """

    configuration = {}

    def __init__(self, configuration=None):
        """
        Initialise the tool with its configuration.

        Parameters
        ----------
        configuration : dict
           a dictionary containing parameters that define how the operation
           should be carried out, which are specific to each Tool.
        """
        logger.info("Processing Test")
        if configuration is None:
            configuration = {}

        self.configuration.update(configuration)

    def run(self, input_files, metadata, output_files):
        """
        Main run function for processing a test file.

        Parameters
        ----------
        input_files : dict
           Dictionary of file locations
        metadata : list
           Required meta data
        output_files : dict
           Locations of the output files to be returned by the pipeline

        Returns
        -------
        output_files : dict
           Locations for the output txt
        output_metadata : dict
           Matching metadata for each of the files
        """

        # Initialise the test tool
        tt_handle = testTool(self.configuration)
        tt_files, tt_meta = tt_handle.run(input_files, metadata, output_files)

        return (tt_files, tt_meta)
