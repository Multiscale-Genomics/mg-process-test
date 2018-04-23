#!/bin/bash

# See the NOTICE file distributed with this work for additional information
# regarding copyright ownership.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Get the location of this script - Should be in the root of the module
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd $DIR
cd tests/data

# Known test data files to keep
c=$(git rev-parse --abbrev-ref HEAD)
a=$(git ls-tree -r $c --name-only | sort)

# Remove all files in tests/data/* that are not in the git repo
b=$(tree -aifF --noreport | grep -v /$ | sed 's/^\.\///' | sed 's/^\.$//' | sort)
for i in $b; do
    skip=0
    for j in $a; do
        if [ "${i}" = "${j}" ]; then
            skip=1
            break
        fi
    done
    if [ $skip != 1 ]; then
        rm -r $i
    fi
done

# Remove all empty dirs in tests/data
b=$(find . -type d -empty)
for i in $b; do
    skip=0
    for j in $a; do
        if [ "${i}" = "${j}" ]; then
            skip=1
            break
        fi
    done
    if [ $skip != 1 ]; then
        rm -r $i
    fi
done
