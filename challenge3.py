import codecs

string1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def xorchecker(string):
    #answer is 53('5')
    start = 32
    end = 126
    while start <= end:
        byte_string1 = bytearray.fromhex(string)
        byte_result = bytearray(len(byte_string1))
        #byte_result = bytearray(len(string))
        for i in range(len(string)):
            byte_result[i] = string[i] ^ start
        if (scorecounter(codecs.decode(byte_result.hex(),'hex').decode())) >5 :
            print("key:..",chr(start),"message:..")
            print(codecs.decode(byte_result.hex(),'hex').decode())
            print("Score:..", scorecounter(codecs.decode(byte_result.hex(),'hex').decode()))
            print("--------------------------------------------------------------")
        start = start + 1



def scorecounter(message):
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000, '': -1000.9,
        '<': -.2, '':-1000.9
    }
    score = 0

    for i in range(len(message)):
        try:
            score = score + character_frequencies[message[i].lower()]
        except:
            pass
    return score

def printer():
    counter = 0
    xorchecker(string1)

xorchecker(string1)
#Cooking MC's like a pound of bacon == x