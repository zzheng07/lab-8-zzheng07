import random


def generate():
    relations = [None] * 26

    for index in range(26):
        relations[index] = set()

    for index in range(26):
        count = random.randint(1, 25)
        person = index
        friends = relations[index]

        for _ in range(1, count):
            friend = random.randint(1, 25)
            if (friend != person):
                friends.add(friend)
                relations[friend].add(person)

    return relations


def transform(index, x):
    line = chr(index + 65) + ","
    line += ",".join([chr(y + 65) for y in x])
    return line


def write_to_files(c, friend_lists):
    lines = [transform(index + c * 13, x) for index, x in enumerate(friend_lists)]
    content = "\n".join(list(lines))
    filename = "friend_list{0}.txt".format(c + 1)
    f = open(filename, "w")
    f.write(content)
    f.close()


friend_lists = generate()

write_to_files(0, friend_lists[0:13])
write_to_files(1, friend_lists[13:])
