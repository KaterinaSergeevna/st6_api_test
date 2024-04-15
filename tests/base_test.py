import pytest
from endpoints.create_publication import CreatePublication
from endpoints.delete_publication import DeletePublication
from endpoints.get_publication import GetPublication
from endpoints.put_publication import PutPublication
from endpoints.patch_publication import PatchPublication


class BaseTest:

    def setup_method(self):
        self.create_ends = CreatePublication()
        self.get_ends = GetPublication()
        self.delete_ends = DeletePublication()
        self.put_ends = PutPublication()
        self.patch_ends = PatchPublication()
