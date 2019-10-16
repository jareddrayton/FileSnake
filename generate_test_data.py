import shutil
from pathlib import Path

def usecase1_test(show_name, episodes):

    file_type = ".mkv"

    p = Path(show_name)
    
    if p.exists():
        shutil.rmtree(show_name)
        
    p.mkdir()
    
    for i in range(1, episodes + 1):
        s = Path(show_name + str(i) + file_type)
        path = Path.cwd() / p / s
        Path(path).touch()