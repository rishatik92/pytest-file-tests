import pytest
import time

def test_bad_char(tmp_path):
    """Test prohibition to name with bad characters"""

    BAD_NAME = "\\//text"
    cant_create = tmp_path/ BAD_NAME
    with pytest.raises(FileNotFoundError):
        cant_create.write_text("some text")



MASK = "*password*"

@pytest.mark.parametrize("file_auto_remover",[(MASK)],indirect=True)
def test_auto_remover(file_auto_remover):
    """checking autoremove passwords file"""

    file_auto_remover.start()
    tmpdir = file_auto_remover.tmpdir
    MUST_BE_DELETED = "some_password_user"
    KEEPED_FILE = "not_delete"

    file1 = tmpdir.join(KEEPED_FILE)
    file1.write(666)
    file2 = tmpdir.join(MUST_BE_DELETED)
    file2.write(666)

    time.sleep(1)

    assert file1.exists()
    assert not file2.exists()
