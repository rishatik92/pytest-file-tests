TEXT = "simple_text"

def test_create_file(tmp_path):
    "test file creation"

    file = tmp_path / "empty_file.txt"
    file.touch()
    assert file.is_file()
    return file

def test_create_subdir(tmpdir):
    "test directory creation"

    some_directory = tmpdir.mkdir("some_dir")
    assert some_directory.isdir()
    return some_directory

def test_wrote_file(tmpdir):
    """ Test for file writing"""
    
    file = tmpdir.join("simple_file.txt")
    file.write(TEXT)
    wrote_text = file.read()
    assert wrote_text == TEXT
    return file
