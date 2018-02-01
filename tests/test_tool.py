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

from tool.testTool import testTool
from basic_modules.metadata import Metadata

@pytest.mark.testTool
def test_testTool():
    """
    Test case to ensure that the testTool works.

    .. code-block:: none

       pytest tests/test_tool.py
    """
    resource_path = os.path.join(os.path.dirname(__file__), "data/")

    input_files = {
        "input": resource_path + "test_input.txt"
    }

    output_files = {
        "output": resource_path + "test_output.txt"
    }

    metadata = {
        "input": Metadata(
            "text", "txt", input_files["input"], None,
            {"assembly": "test"}
        )
    }

    tt_handle = testTool()
    tt_handle.run(input_files, metadata, output_files)

    assert os.path.isfile(output_files["output"]) is True
    assert os.path.getsize(output_files["output"]) > 0
