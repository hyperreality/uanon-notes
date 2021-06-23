def A1Z26_encrypt(cistring):
    string = ""     # Placeholder variable
    cistring = cistring.lower()     # Format to Lowercase
    cistring = "".join(cistring.split())    # Remove spaces from string
    for x in range(0, len(cistring)):   # Loop through each character of string
        char = ord(cistring[x]) - 96    # Convert character to numeric 1 - 26
        if char > 0 and char <= 26 : string += str(char) + ""    # Store value in 'string' variable
    return(string)      # Return cipher string
 
def A1Z26_decrypt(cistring):
    string = ""     # Placeholder variable
    data = cistring.split() # Split string at " "
 
    for char in data:   # Loop through each character
        char = chr(int(char) + 96)  # Convert number to letter
        string += char  # Add character to string
    return(string)      # Return cipher string

locs = [
    "The Mall",
    "Horse Guards Rd",
    "Spur Rd",
    "Strand",
    "Downing St",
    "Birdcage Walk",
    "Victoria Memorial",
    "Statue of the Earl Mountbatten",
    "Whitehall",
    "Trafalgar Square",
    "Buckingham Palace",
    "Westminster Hall",
    "Admiralty Arch",
    "Trafalgar Square",
    "Parliament St",
    "Old Palace Yard",
    "Abingdon St",
    "House of Commons",
    "Victoria Embankment",
    "One Great George Street",
]

locs_time = [
    "Horse Guards Rd",
    "Spur Rd",
    "The Mall",
    "Strand",
    "Downing St",
    "Birdcage Walk",
    "Victoria Memorial",
    "Statue of the Earl Mountbatten",
    "Trafalgar Square",
    "Whitehall",
    "Buckingham Palace",
    "Westminster Hall",
    "Admiralty Arch",
    "Trafalgar Square",
    "Abingdon St",
    "Old Palace Yard",
    "Parliament St",
    "House of Commons",
    "Victoria Embankment",
    "One Great George Street",
]

IND = 1

def output(out):
    # print(out)
    print(out.upper())
    # print(A1Z26_encrypt(out))

def get_second(lst):
    out = ""
    for i,l in enumerate(lst):
        out += l[IND]
    output(out)

    out = ""
    for i,l in enumerate(lst):
        if i % 2 == 0:
            continue
        out += l[IND]
    output(out)

    out = ""
    for i,l in enumerate(lst):
        if i % 2 == 1:
            continue
        out += l[IND]
    output(out)

get_second(locs)
get_second(locs[::-1])
get_second(locs_time)
get_second(locs_time[::-1])
