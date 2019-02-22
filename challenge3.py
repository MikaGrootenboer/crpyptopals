import codecs
from langdetect import detect


string1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
def xorchecker(string):
    start = 65
    end = 90
    while start <= end:
        score = 0
        byte_string1 = bytearray.fromhex(string)
        byte_result = bytearray(len(byte_string1))

        for i in range(len(byte_string1)):
            byte_result[i] = byte_string1[i] ^ start
        print("key:..",chr(start),"message:..",codecs.decode(byte_result.hex(),'hex').decode())
        start = start + 1
    print("===========================================================================================================")


def score(tester):
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    score = 0
    for i, c in enumerate(tester):
        score = score + character_frequencies[c]
    print(score)

#score("vvrpwjuprxivlwv xzvw")
#score(xorchecker(string1))
#xorchecker(string1)
#Cooking MC's like a pound of bacon == x