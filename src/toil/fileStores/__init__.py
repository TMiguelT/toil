# Copyright (C) 2015-2019 Regents of the University of California
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import

import os

__all__ = ['fileStore', 'nonCachingFileStore', 'cachingFileStore']

class FileID(str):
    """
    A small wrapper around Python's builtin string class. It is used to represent a file's ID in the file store, and
    has a size attribute that is the file's size in bytes. This object is returned by importFile and writeGlobalFile.
    """

    def __new__(cls, fileStoreID, *args):
        return super(FileID, cls).__new__(cls, fileStoreID)

    def __init__(self, fileStoreID, size):
        # Don't pass an argument to parent class's __init__.
        # In Python 3 we can have super(FileID, self) hand us object's __init__ which chokes on any arguments.
        super(FileID, self).__init__()
        self.size = size

    @classmethod
    def forPath(cls, fileStoreID, filePath):
        return cls(fileStoreID, os.stat(filePath).st_size)
