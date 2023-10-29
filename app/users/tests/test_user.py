import pytest
from app.users import user, manager


@pytest.fixture
def user_fixture():
    return user.User()

@pytest.fixture
def teste_fixture():
    return 'teste'

def test_user_process_teste(teste_fixture):
    assert  teste_fixture == 'teste'


@pytest.fixture
def manager_fixture():
    return manager.Manager()

def test_user_can_process_admin(user_fixture):
    assert user_fixture.can_process_admin() == False

def test_manager_can_process_admin(manager_fixture):
    assert manager_fixture.can_process_admin() == True

@pytest.mark.parametrize("name", ["Fulano"])
def test_user_can_update_name(user_fixture, name):
    user_fixture.set_name(name)

    assert user_fixture.name == name

@pytest.mark.parametrize("name", ["Fulano"])
def test_manager_can_update_name(manager_fixture, name):
    manager_fixture.set_name(name)

    assert manager_fixture.name == name