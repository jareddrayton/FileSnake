import shutil
from pathlib import Path


# Tests to write
# mixed filetypes e.g. .avi and mkv



file_type = ".mkv"

episodes = 148

def usecase1_test(show_name):
    
    p = Path(show_name)
    
    if p.exists():
        shutil.rmtree(show_name)
        
    p.mkdir()
    
    for i in range(1, episodes + 1):
        s = Path(show_name + str(i) + file_type)
        path = Path.cwd() / p / s
        Path(path).touch()