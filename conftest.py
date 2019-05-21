import pytest
from pathlib import Path
from threading import Thread, Event
from time import sleep
"""some fixtures here"""

@pytest.fixture
def file_auto_remover(request,tmpdir):
    """This fixture will try to remove all files which contain given mask as parameter"""

    class FileRemover(object):

        def __init__(self,file_mask):
            self.__path = Path(tmpdir.strpath)
            self.tmpdir = tmpdir
            self.__mask = file_mask
            self.__stop_flag = Event()
            print("path is:",self.__path,
                  "the file mask is: "+ self.__mask)
            self.__th = Thread(target=self.__find_and_delete, args=(self.__stop_flag,))
            self.__th.daemon = True

        def start(self):
            self.__th.start()

        def __find_and_delete(self, stop_flag):
            while (not stop_flag.is_set()):
                for file in self.__path.glob(self.__mask):
                    if file.is_file():
                        print(file," will be deleted")
                        file.unlink()
                sleep(0.1)


        def close(self):
            self.__stop_flag.set()

    file_remover = FileRemover(request.param)
    request.addfinalizer(file_remover.close)
    return file_remover