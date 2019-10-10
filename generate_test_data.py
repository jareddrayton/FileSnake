from pathlib import Path

show_name = "Hunter X Hunter"

file_type = ".mkv"

episodes = 148

p = Path('Test')
p.mkdir()

for i in range(1, episodes + 1):

    s = Path(show_name + str(i) + file_type)
    
    path =  Path.cwd() / p / s

    Path(path).touch()