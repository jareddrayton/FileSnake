import shutil
import random

from pathlib import Path


def usecase1_test(show_name, episodes):

    file_type = ".mkv"

    p = Path(show_name)
    
    if p.exists():
        shutil.rmtree(show_name)
        
    p.mkdir()
    
    for i in range(1, episodes + 1):
        episode = Path(show_name + str(i) + file_type)
        path = Path.cwd() / p / episode
        Path(path).touch()


def usecase2_test(show_name, episodes):

    file_type = ".mkv"

    seasons = 4

    file_hierarchy = {}

    for i in range(1, seasons):
        file_hierarchy[str(i)] = episodes//seasons

    file_hierarchy[str(seasons)] = (episodes//seasons) + (episodes%seasons)

    p = Path(show_name)
    
    if p.exists():
        shutil.rmtree(show_name)
    
    p.mkdir()

    episode_list = []

    for i in range(1, episodes + 1):
            episode_list.append(Path(show_name + str(i) + file_type))

    for k, v in file_hierarchy.items():
        s = p / "Season {}".format(k)
        s.mkdir()

        for i in range(v):
            path = Path.cwd() / s / episode_list[i]
            Path(path).touch()
        
        episode_list = episode_list[v:]