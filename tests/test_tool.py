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

from tool.testTool import testTool

def test_testTool():
    """
    Test case to ensure that the GEM indexer works.
    """
    resource_path = os.path.dirname(__file__)
    text_file = resource_path + "/test.txt"

    input_files = {}

    output_files = {
        "output": text_file
    }

    metadata = {}

    print(input_files, output_files)

    tt_handle = testTool()
    tt_handle.run(input_files, metadata, output_files)

    assert os.path.isfile(text_file) is True
    assert os.path.getsize(text_file) > 0
