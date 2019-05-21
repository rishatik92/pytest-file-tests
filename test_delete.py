from .test_simple import test_create_file, test_create_subdir


def test_delete_file(tmp_path):
    "check file deleting"
    file = test_create_file(tmp_path)
    assert file.exists()

    file.unlink()

    assert not file.exists()


def test_delete_dir(tmpdir):
    "check directory deleting"

    directory = test_create_subdir(tmpdir)
    directory.remove()
    assert not directory.exists()


def test_move_file(tmp_path):
    "check file deleting"
    file = test_create_file(tmp_path)
    new_file = tmp_path / "new_file"

    assert not new_file.exists()
    assert file.exists()

    file.replace(new_file)  # replacing file

    print(new_file)
    assert not file.exists()
    assert new_file.exists()
