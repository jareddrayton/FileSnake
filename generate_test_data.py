import shutil
from pathlib import Path


# Tests to write
# mixed filetypes e.g. .avi and mkv


def usecase1_test():
    
    show_name = "Yu Yu Hakusho"

    episodes = 148

    file_type = ".mkv"

    p = Path(show_name)
    
    if p.exists():
        shutil.rmtree(show_name)
        
    p.mkdir()
    
    for i in range(1, episodes + 1):
        s = Path(show_name + str(i) + file_type)
        path = Path.cwd() / p / s
        Path(path).touch()

usecase1_test()