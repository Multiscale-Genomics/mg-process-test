#!/usr/bin/env python

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

import argparse

from basic_modules.workflow import Workflow
from utils import logger

from mg_process_test.tool.testTool import testTool

# ------------------------------------------------------------------------------


class process_test(Workflow):
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

# ------------------------------------------------------------------------------


def main_json(config, in_metadata, out_metadata):
    """
    Main function
    -------------

    This function launches the app using configuration written in
    two json files: config.json and input_metadata.json.
    """
    # 1. Instantiate and launch the App
    logger.info("1. Instantiate and launch the App")
    from apps.jsonapp import JSONApp
    app = JSONApp()
    result = app.launch(process_test,
                        config,
                        in_metadata,
                        out_metadata)

    # 2. The App has finished
    logger.info("2. Execution finished; see " + out_metadata)

    return result

# ------------------------------------------------------------------------------

if __name__ == "__main__":

    # Set up the command line parameters
    PARSER = argparse.ArgumentParser(description="Test Pipeline")
    PARSER.add_argument("--config", help="Configuration file")
    PARSER.add_argument("--in_metadata", help="Location of input metadata file")
    PARSER.add_argument("--out_metadata", help="Location of output metadata file")
    PARSER.add_argument("--local", action="store_const", const=True, default=False)

    # Get the matching parameters from the command line
    ARGS = PARSER.parse_args()

    CONFIG = ARGS.config
    IN_METADATA = ARGS.in_metadata
    OUT_METADATA = ARGS.out_metadata
    LOCAL = ARGS.local

    if LOCAL:
        import sys
        sys._run_from_cmdl = True  # pylint: disable=protected-access

    RESULTS = main_json(CONFIG, IN_METADATA, OUT_METADATA)
    print(RESULTS)
