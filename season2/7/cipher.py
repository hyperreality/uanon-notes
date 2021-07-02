import string
from collections import Counter

cipher408 = [
  "flight_takeoff",
  "megaphone",
  "public_off",
  "explore_off",
  "cloud-error1",
  "cloud-sun-lightning",
  "menu1",
  "error_outline",
  "warning1",
  "cloud-lightning",
  "legend_toggle",
  "sparkle",
  "cloud-moon-lightning",
  "lightning2",
  "cloud-error2",
  "live_help",
  "bug_report",
  "closed_caption_off",
  "legend_toggle",
  "puzzle-piece",
  "game",
  "cloud-sun-lightning1",
  "megaphone1",
  "live_help",
  "coronavirus",
  "legend_toggle",
  "cloud-error",
  "file",
  "public_off",
  "switch_camera",
  "note-important",
  "lightning5",
  "document-error",
  "balance-scale",
  "menu_book",
  "satellite",
  "alarm_off",
  "warning",
  "flight_takeoff",
  "megaphone",
  "grid_off",
  "help_center",
  "compute",
  "cloud-error1",
  "cloud-moon-lightning",
  "view_module",
  "cloud-lightning1",
  "signal_cellular_off",
  "flight_takeoff",
  "music_off",
  "explore_off",
  "public_off",
  "closed_caption_off",
  "flight_takeoff",
  "sparkle",
  "directions_off",
  "offline_bolt",
  "bug_report",
  "error_outline",
  "legend_toggle",
  "warning1",
  "cloud-error2",
  "megaphone1",
  "lightning7",
  "puzzle-piece",
  "legend_toggle",
  "grid_off",
  "cloud-sun-lightning",
  "lightning2",
  "flight_takeoff",
  "mail-error",
  "buildings",
  "game",
  "live_help",
  "buildings",
  "live_help",
  "coronavirus",
  "legend_toggle",
  "bug_report",
  "file",
  "blur_off",
  "public_off",
  "compute",
  "virus",
  "buildings",
  "switch_camera",
  "music_off",
  "document-error",
  "legend_toggle",
  "live_help",
  "live_help",
  "legend_toggle",
  "public_off",
  "do_not_disturb_off",
  "menu_book",
  "cloud-error2",
  "note-important",
  "offline_bolt",
  "lightning5",
  "cloud-sun-lightning1",
  "cloud-lightning1",
  "alarm_off",
  "live_help",
  "legend_toggle",
  "warning1",
  "warning",
  "do_not_disturb_off",
  "cloud-error",
  "satellite",
  "signal_cellular_off",
  "legend_toggle",
  "cloud-error1",
  "flight_takeoff",
  "puzzle-piece",
  "explore_off",
  "help_center",
  "megaphone",
  "cloud-moon-lightning",
  "lightning7",
  "sparkle",
  "closed_caption_off",
  "lightning2",
  "cloud-error2",
  "menu1",
  "error_outline",
  "grid_off",
  "cloud-lightning",
  "legend_toggle",
  "megaphone1",
  "blur_off",
  "public_off",
  "coronavirus",
  "balance-scale",
  "buildings",
  "file",
  "music_off",
  "mail-error",
  "lightning5",
  "document-error",
  "music",
  "cloud-sun-lightning",
  "bug_report",
  "cloud-error",
  "switch_camera",
  "puzzle-piece",
  "warning",
  "cloud-sun-lightning1",
  "cloud-error2",
  "buildings",
  "menu_book",
  "warning1",
  "menu1",
  "cloud-moon-lightning",
  "directions_off",
  "buildings",
  "satellite",
  "grid_off",
  "view_module",
  "closed_caption_off",
  "music_off",
  "lightning5",
  "signal_cellular_off",
  "lightning1",
  "help_center",
  "megaphone",
  "puzzle-piece",
  "game",
  "alarm_off",
  "warning",
  "flight_takeoff",
  "warning1",
  "cloud-lightning1",
  "lightning7",
  "bug_report",
  "lightning1",
  "cloud-moon-lightning",
  "legend_toggle",
  "virus",
  "compute",
  "closed_caption_off",
  "live_help",
  "live_help",
  "explore_off",
  "cloud-error2",
  "sparkle",
  "cloud-error1",
  "note-important",
  "note-important",
  "buildings",
  "megaphone1",
  "balance-scale",
  "mail-error",
  "offline_bolt",
  "directions_off",
  "file",
  "switch_camera",
  "lightning2",
  "blur_off",
  "do_not_disturb_off",
  "error_outline",
  "cloud-sun-lightning1",
  "puzzle-piece",
  "menu_book",
  "cloud-error2",
  "coronavirus",
  "browser_not_supported",
  "satellite",
  "grid_off",
  "virus",
  "buildings",
  "megaphone",
  "cloud-sun-lightning",
  "music_off",
  "document-error",
  "buildings",
  "lightning5",
  "warning1",
  "sparkle",
  "puzzle-piece",
  "flight_takeoff",
  "grid_off",
  "game",
  "megaphone1",
  "cloud-moon-lightning1",
  "warning",
  "alarm_off",
  "cloud-error2",
  "mail-error",
  "compute",
  "music_off",
  "music",
  "file",
  "puzzle-piece",
  "note-important",
  "buildings",
  "warning1",
  "offline_bolt",
  "legend_toggle",
  "flight_takeoff",
  "buildings",
  "balance-scale",
  "buildings",
  "switch_camera",
  "cloud-lightning1",
  "grid_off",
  "do_not_disturb_off",
  "menu_book",
  "music_off",
  "satellite",
  "cloud-moon-lightning",
  "browser_not_supported",
  "megaphone",
  "public_off",
  "sparkle",
  "cloud-error1",
  "directions_off",
  "mail-error",
  "explore_off",
  "virus",
  "buildings",
  "public_off",
  "legend_toggle",
  "help_center",
  "cloud-sun-lightning",
  "live_help",
  "buildings",
  "error_outline",
  "mail-error",
  "megaphone1",
  "browser_not_supported",
  "file",
  "warning1",
  "closed_caption_off",
  "menu1",
  "note-important",
  "switch_camera",
  "grid_off",
  "music_off",
  "menu_book",
  "live_help",
  "coronavirus",
  "warning1",
  "cloud-error2",
  "game",
  "lightning2",
  "flight_takeoff",
  "balance-scale",
  "mail-error",
  "compute",
  "lightning5",
  "live_help",
  "live_help",
  "cloud-error",
  "warning",
  "cloud-lightning1",
  "public_off",
  "satellite",
  "puzzle-piece",
  "cloud-moon-lightning",
  "signal_cellular_off",
  "do_not_disturb_off",
  "legend_toggle",
  "public_off",
  "lightning7",
  "closed_caption_off",
  "cloud-sun-lightning1",
  "cloud-error2",
  "view_module",
  "bug_report",
  "lightning5",
  "lightning1",
  "explore_off",
  "alarm_off",
  "flight_takeoff",
  "directions_off",
  "buildings",
  "grid_off",
  "offline_bolt",
  "legend_toggle",
  "flight_takeoff",
  "buildings",
  "error_outline",
  "legend_toggle",
  "virus",
  "megaphone",
  "legend_toggle",
  "music_off",
  "coronavirus",
  "view_module",
  "megaphone",
  "warning",
  "cloud-error1",
  "puzzle-piece",
  "cloud-error1",
  "compute",
  "warning1",
  "note-important",
  "buildings",
  "cloud-moon-lightning",
  "public_off",
  "sparkle",
  "grid_off",
  "cloud-sun-lightning",
  "live_help",
  "cloud-moon-lightning",
  "menu1",
  "offline_bolt",
  "music_off",
  "cloud-lightning",
  "legend_toggle",
  "megaphone1",
  "closed_caption_off",
  "lightning2",
  "cloud-error2",
  "live_help",
  "error_outline",
  "legend_toggle",
  "cloud-error",
  "file",
  "puzzle-piece",
  "game",
  "blur_off",
  "lightning5",
  "view_module",
  "view_module",
  "switch_camera",
  "warning",
  "warning1",
  "menu_book",
  "cloud-error2",
  "mail-error",
  "cloud-lightning1",
  "balance-scale",
  "buildings",
  "coronavirus",
  "legend_toggle",
  "directions_off",
  "virus",
  "grid_off",
  "cloud-moon-lightning",
  "live_help",
  "satellite",
  "puzzle-piece",
  "legend_toggle",
  "music_off",
  "explore_off",
  "cloud-sun-lightning1",
  "flight_takeoff",
  "closed_caption_off",
  "note-important",
  "warning1",
  "cloud-sun-lightning",
  "view_module",
  "balance-scale",
  "compute",
  "cloud-moon-lightning",
  "signal_cellular_off",
  "flight_takeoff",
  "game",
  "megaphone",
  "grid_off",
  "document-error",
  "cloud-lightning1",
  "alarm_off",
  "cloud-error1",
  "explore_off",
  "lightning2",
  "sparkle",
]
cipher340 = [
  "location_disabled",
  "warning",
  "document-error",
  "lightning1",
  "error_outline",
  "explore_off",
  "megaphone1",
  "megaphone",
  "lightning2",
  "offline_bolt",
  "legend_toggle",
  "cloud-sun-lightning",
  "closed_caption_off",
  "help_center",
  "game",
  "switch_left",
  "view_module",
  "signal_cellular_off",
  "sparkle",
  "cloud-lightning",
  "cloud-error1",
  "warning1",
  "balance-scale",
  "puzzle-piece",
  "buildings",
  "cloud-error3",
  "compute",
  "virus",
  "coronavirus",
  "mail-error",
  "auto_fix_off",
  "directions_off",
  "cloud-moon-lightning1",
  "note",
  "history_toggle_off",
  "switch_right",
  "music_off",
  "cloud-lightning1",
  "megaphone",
  "lightning5",
  "coronavirus",
  "grid_off",
  "satellite",
  "closed_caption_off",
  "cloud-lightning",
  "cloud-error",
  "location_disabled",
  "explore_off",
  "power_input",
  "cloud-moon-lightning",
  "directions_off",
  "cloud-error3",
  "cloud-error1",
  "warning1",
  "music_off",
  "support",
  "puzzle-piece",
  "blur_off",
  "flight_takeoff",
  "error_outline",
  "cloud-error2",
  "megaphone1",
  "lightning1",
  "game",
  "motion_photos_off",
  "legend_toggle",
  "buildings",
  "switch_camera",
  "megaphone",
  "edit_off",
  "closed_caption_off",
  "mail-error1",
  "lightning7",
  "music",
  "buildings",
  "cloud-lightning",
  "coronavirus",
  "buildings",
  "document-error",
  "cloud-error3",
  "cloud-moon-lightning1",
  "flight_takeoff",
  "cloud-sun-lightning1",
  "mail-error",
  "note",
  "cloud-lightning1",
  "cloud-error",
  "cloud-sun-lightning",
  "coronavirus",
  "offline_bolt",
  "public_off",
  "view_module",
  "lightning3",
  "lightning5",
  "balance-scale",
  "help_center",
  "history_toggle_off",
  "browser_not_supported",
  "cloud-error1",
  "switch_right",
  "warning1",
  "location_disabled",
  "virus",
  "buildings",
  "menu1",
  "sparkle",
  "error2",
  "compute",
  "lightning2",
  "switch_left",
  "do_not_disturb_off",
  "warning",
  "menu_book",
  "explore_off",
  "switch_camera",
  "notist",
  "error2",
  "lightning7",
  "buildings",
  "coronavirus",
  "directions_off",
  "coronavirus",
  "music_off",
  "menu_book",
  "menu_book",
  "error_outline",
  "menu_book",
  "megaphone",
  "edit_off",
  "support",
  "menu_book",
  "buildings",
  "buildings",
  "mail-error1",
  "buildings",
  "closed_caption_off",
  "cloud-lightning",
  "buildings",
  "document-error",
  "offline_bolt",
  "coronavirus",
  "do_not_disturb_off",
  "cloud-error1",
  "warning1",
  "buildings",
  "music_off",
  "signal_cellular_off",
  "bug_report",
  "cloud-moon-lightning1",
  "help_center",
  "menu_book",
  "cloud-moon-lightning",
  "note",
  "history_toggle_off",
  "lightning1",
  "megaphone",
  "virus",
  "switch_left",
  "blur_off",
  "notist",
  "closed_caption_off",
  "public_off",
  "cloud-error",
  "edit_off",
  "cloud-sun-lightning",
  "cloud-lightning",
  "legend_toggle",
  "switch_right",
  "buildings",
  "auto_fix_off",
  "cloud-error1",
  "buildings",
  "location_disabled",
  "balance-scale",
  "lightning7",
  "music",
  "sparkle",
  "grid_off",
  "cloud-error2",
  "mail-error1",
  "power_input",
  "flight_takeoff",
  "switch_camera",
  "error2",
  "explore_off",
  "satellite",
  "buildings",
  "warning1",
  "megaphone1",
  "motion_photos_off",
  "compute",
  "buildings",
  "notion",
  "directions_off",
  "cloud-moon-lightning",
  "view_module",
  "warning",
  "note",
  "buildings",
  "history_toggle_off",
  "music_off",
  "puzzle-piece",
  "mail-error",
  "buildings",
  "game",
  "lightning1",
  "switch_right",
  "cloud-sun-lightning1",
  "error_outline",
  "location_disabled",
  "megaphone",
  "offline_bolt",
  "help_center",
  "auto_fix_off",
  "note-important",
  "explore_off",
  "buildings",
  "legend_toggle",
  "buildings",
  "signal_cellular_off",
  "closed_caption_off",
  "do_not_disturb_off",
  "menu1",
  "menu_book",
  "grid_off",
  "document-error",
  "directions_off",
  "cloud-moon-lightning1",
  "coronavirus",
  "bug_report",
  "switch_left",
  "cloud-lightning1",
  "public_off",
  "switch_camera",
  "virus",
  "coronavirus",
  "cloud-error",
  "cloud-lightning",
  "cloud-sun-lightning",
  "lightning5",
  "cloud-error2",
  "error_outline",
  "lightning3",
  "sparkle",
  "offline_bolt",
  "edit_off",
  "mail-error1",
  "compute",
  "document-error",
  "lightning2",
  "megaphone1",
  "cloud-error1",
  "puzzle-piece",
  "error2",
  "note",
  "warning1",
  "cloud-moon-lightning1",
  "power_input",
  "cloud-error",
  "blur_off",
  "cloud-moon-lightning",
  "music",
  "switch_left",
  "warning",
  "coronavirus",
  "help_center",
  "music_off",
  "game",
  "cloud-sun-lightning1",
  "balance-scale",
  "edit_off",
  "motion_photos_off",
  "cloud-lightning1",
  "history_toggle_off",
  "megaphone",
  "switch_right",
  "buildings",
  "view_module",
  "mail-error",
  "signal_cellular_off",
  "satellite",
  "puzzle-piece",
  "menu1",
  "location_disabled",
  "support",
  "lightning7",
  "mail-error1",
  "closed_caption_off",
  "lightning5",
  "do_not_disturb_off",
  "lightning1",
  "explore_off",
  "virus",
  "directions_off",
  "buildings",
  "cloud-error2",
  "legend_toggle",
  "note",
  "puzzle-piece",
  "error_outline",
  "auto_fix_off",
  "offline_bolt",
  "buildings",
  "history_toggle_off",
  "switch_right",
  "buildings",
  "buildings",
  "cloud-lightning",
  "megaphone1",
  "document-error",
  "power_input",
  "grid_off",
  "sparkle",
  "lightning2",
  "help_center",
  "motion_photos_off",
  "cloud-moon-lightning1",
  "cloud-error1",
  "bug_report",
  "warning1",
  "compute",
  "menu_book",
  "buildings",
  "music_off",
  "flight_takeoff",
  "cloud-moon-lightning",
  "view_module",
  "lightning1",
  "mail-error",
  "location_disabled",
  "auto_fix_off",
  "explore_off",
  "virus",
  "power_input",
  "live_help",
  "motion_photos_off",
  "cloud-error",
  "megaphone",
  "legend_toggle",
  "warning"
]

print(f"Length cipher408: {len(set(cipher408))}")
print(Counter(cipher408).most_common())
print(f"Length cipher340: {len(set(cipher340))}")
print(Counter(cipher340).most_common())
print(set(cipher408) - set(cipher340))
print(set(cipher340) - set(cipher408))
# print(len(set([c[0] for c in cipher408])))
# print(len(set([c[0] for c in cipher340])))
# print(len(cipher408))
# print(len(cipher340))

def flatten(t):
    return [item for sublist in t for item in sublist]

def make_rows(cipher, size):
    cipher_rows = []
    temp = []
    for i,c in enumerate(cipher):
        temp.append(c)
        if (i+1) % size == 0:
            cipher_rows.append(temp)
            temp = []
    return cipher_rows

def print_grid(cipher):
    for r in cipher:
        print(r)

def zodiac_transpose(cipher):
    width = len(cipher[0])
    height = len(cipher)
    out = []
    i, j = 0, 0
    for cnt in range(width * height):
        print(cipher[i][j])
        out.append(cipher[i][j])
        i += 1
        j += 2
        if i >= height:
            i -= height
        if j >= width:
            j -= width
    return out
    # return make_rows(out, 17)

def symbolise(cipher):
    out = []
    temp = ""
    seen = {}
    alpha = string.ascii_lowercase + string.ascii_uppercase + string.digits + '!"#$%&\'()*+'
    ind = 0
    for i, c in enumerate(cipher):
        if c not in seen:
            seen[c] = alpha[ind]
            ind += 1
        temp += seen[c]

        if (i+1) % 17 == 0:
            out.append(temp)
            temp = ""

    for t in out:
        print(t)

cipher408_rows = make_rows(cipher408, 17)
cipher340_rows = make_rows(cipher340, 17)

transposed = zodiac_transpose(cipher340_rows[:9])
print(transposed)
transposed2 = zodiac_transpose(cipher340_rows[9:18])
print(transposed2)
transposed3 = zodiac_transpose(cipher340_rows[18:])
print(transposed3)

symbolise(transposed + transposed2 + transposed3)
# print()
# symbolise(cipher340)

# bla = make_rows([i for i in range(340)], 17)[:9]

# transposed = zodiac_transpose(bla)
# print(make_rows(transposed, 17))


# print(symbolise(flatten(cipher340_rows[18:])))
