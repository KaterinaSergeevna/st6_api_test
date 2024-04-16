import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def post_id(create_object):
    create_object.create_new_publication()
    post_id = create_object.response_json['id']
    yield post_id
    DeleteObject().delete(post_id)


@pytest.fixture()
def create_object():
    return CreateObject()
