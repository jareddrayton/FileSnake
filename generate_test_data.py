show = "Hunter X Hunter"

episodes = 148

file_type = ".mkv"

for i in range(1, episodes + 1):

    with open("Test\\" + show + str(i) + file_type, "w") as f:
        f.closed