from Crypto.Cipher import AES

alphabet = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

key = [4,32,16,32,29,70,72,20,70,70]

cipher = bytes.fromhex("0d211d212b5556285555")

ans = ""
for i, b in enumerate(cipher):
    out = b - key[i]
    ans += alphabet[out]

print(ans)

