import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject
from endpoints.get_object import GetObject
from endpoints.put_object import PutObject
from endpoints.patch_object import PatchObject


class BaseTest:

    def setup_method(self):
        self.create_ends = CreateObject()
        self.get_ends = GetObject()
        self.delete_ends = DeleteObject()
        self.put_ends = PutObject()
        self.patch_ends = PatchObject()
