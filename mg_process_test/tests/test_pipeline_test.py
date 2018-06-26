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

import os.path
import pytest

from basic_modules.metadata import Metadata
from process_test import process_test


@pytest.mark.testTool
def test_test_pipeline():
    """
    Test case to ensure that the Genome indexing pipeline code works.

    Running the pipeline with the test data from the command line:

    .. code-block:: none

       pytest tests/test_pipeline_test.py
    """
    resource_path = os.path.join(os.path.dirname(__file__), "data/")

    input_files = {
        "input": resource_path + "test_input.txt"
    }

    metadata = {
        "input": Metadata(
            "text", "txt", input_files["input"], None,
            {"assembly": "test"}
        )
    }

    files_out = {
        "output": resource_path + 'test.txt',
    }

    tt_handle = process_test()
    tt_files, tt_meta = tt_handle.run(input_files, metadata, files_out)

    # Add tests for all files created
    for f_out in tt_files:
        print("GENOME RESULTS FILE:", f_out)
        assert os.path.isfile(tt_files[f_out]) is True
        assert os.path.getsize(tt_files[f_out]) > 0
        assert f_out in tt_meta
