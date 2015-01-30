import msvcrt

print "press 'escape' to quit..."

while True:
    char = msvcrt.getch()
    if char == chr(27):
        break
    print char,
    if char == chr(13):
        print
