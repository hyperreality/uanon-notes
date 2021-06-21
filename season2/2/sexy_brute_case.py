import requests

for i1 in ['U', 'u']:
    for i2 in ['L', 'l']:
        for i3 in ['Y', 'y']:
            for i4 in ['Z', 'z']:
                for i5 in ['N', 'n']:
                    for i6 in ['J', 'j']:
                        url = f"https://bit.ly/3{i1}{i2}{i3}{i4}{i5}{i6}"
                        r = requests.get(url)
                        print(f"{url} {len(r.content)}")
