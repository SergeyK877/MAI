import sys

fileFrom = sys.argv[1]
fileTo = sys.argv[2]


def IsTerminal(command):
    return command[0] == command[3] and command[1] == command[2]


def ReadCommandsFrom(file_name, remove_terminal_commands):
    commands = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.replace("\n", "")
            if line == "":
                continue
            words = line.split("//")
            commandString = words[0]
            comment = "//".join(words[1:])

            command = commandString.split(",")
            command[0] = int(command[0])
            command[3] = int(command[3])

            if remove_terminal_commands and IsTerminal(command):
                continue
            commands.append((command, comment))
    return commands


commandFrom = ReadCommandsFrom(fileFrom, True)
commandTo = ReadCommandsFrom(fileTo, False)

shiftSize = 0
for command, comment in commandFrom:
    if command[3] > shiftSize:
        shiftSize = command[3]

for command, comment in commandTo:
    command[0] += shiftSize
    command[3] += shiftSize


for i, (command, comment) in enumerate(commandFrom):
    print(",".join(map(str, command)), end="")
    if i == 0:
        comment = comment + f"BEGIN {fileFrom}"
    if i == len(commandFrom) - 1:
        comment = comment + f"END {fileFrom}"
    if len(comment) > 0:
        comment = " // " + comment
    print(comment)

for i, (command, comment) in enumerate(commandTo):
    print(",".join(map(str, command)), end="")
    if i == 0:
        comment = comment + f"BEGIN {fileTo}"
    if i == len(commandTo) - 1:
        comment = comment + f"END {fileTo}"
    if len(comment) > 0:
        comment = " // " + comment
    print(comment)
