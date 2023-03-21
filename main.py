pebble_height = 3
pebble_width = 1
WIDTH = 40
HEIGHT = 20

ball_x = 20
ball_y = 10

pebble_links_x = 1
pebble_links_y = 10

pebble_rechts_x = 38
pebble_rechts_y = 10

def in_range(value, start, end):
    if start <= value and value <= end:
        return True
    else:
        return False

def liegt_punkt_in_pebble(x, y, pos_x, pos_y):
    if in_range(x, pos_x, pos_x + pebble_width) and in_range(y, pos_y, pos_y + pebble_height):
        return True
    return False

def bewegePebble(istLinks, richtung):
    global pebble_links_y, pebble_rechts_y
    if istLinks:
        if richtung == "w":
            pebble_links_y = pebble_links_y - 1
        else:
            pebble_links_y = pebble_links_y + 1
    else:
        if richtung == "w":
            pebble_rechts_y = pebble_rechts_y - 1
        else:
            pebble_rechts_y = pebble_rechts_y + 1



zaehler = 0
spielLaeuft = True
while spielLaeuft:
    if zaehler == 5:
        bewegePebble(True, input("Wohin möchtest du dich bewegen (w|s)"))
        bewegePebble(False, input("Wohin möchtest du dich bewegen (w|s)"))
        zaehler = 0

    ball_x = ball_x + 1
    ball_y = ball_y + 1

    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):

            if x == ball_x and y == ball_y:
                print("O", end="")
            elif liegt_punkt_in_pebble(x, y, pebble_links_x, pebble_links_y):
                print("|", end="")
            elif liegt_punkt_in_pebble(x, y, pebble_rechts_x, pebble_rechts_y):
                print("|", end="")
            else:
                print(" ", end="")
        print("")
    zaehler = zaehler + 1
