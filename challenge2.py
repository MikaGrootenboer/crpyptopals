import codecs

string1 = "1c0111001f010100061a024b53535009181c"
key = "686974207468652062756c6c277320657965"

byte_string1= bytearray.fromhex(string1)
byte_key = bytearray.fromhex(key)
byte_result = bytearray(len(byte_string1))
byte_reverse = bytearray(len(byte_result))

def decoder():
    for i in range(len(byte_string1)):
        byte_result[i] = byte_string1[i] ^ byte_key[i]

    print(byte_result.decode())
    print(codecs.encode(byte_result,'hex').decode())


#reverse function (for personal testing)
def reverse():
    for c in range(len(byte_reverse)):
        byte_reverse[c] = byte_result[c] ^ byte_key[c]
        print(byte_key[c])
    print(codecs.encode(byte_reverse,'hex').decode())

decoder()