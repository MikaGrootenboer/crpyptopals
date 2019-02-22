import codecs,base64, math
from challenge3 import xorchecker

encryp_base64  = open("challenge6.txt").read()
encryp_bytes = base64.b64decode(encryp_base64)
encryp_bits = bin(int.from_bytes(encryp_bytes,'big'))[2:]
teststring1 = "this is a test"
teststring2 = "wokka wokka!!!"

#step 2
#input has to be bytes!
def hamming_dist(string1,string2):
    bitstring1 = bin(int.from_bytes(string1,'big'))[2:]
    bitstring2 = bin(int.from_bytes(string2,'big'))[2:]
    sorted_bitstring = len(bitstring1) if len(bitstring1) < len(bitstring2) else len(bitstring2)
    counter = 0
    for i in range(sorted_bitstring):
        if bitstring1[i] != bitstring2[i]:
            counter = counter +1
    return counter
#step 3
def cihper_xor(firstkey,secondkey,message):
    hamming_key={}
    for keysize in range(firstkey,secondkey):
        first_key_instance = message[:keysize]
        #print("keysize:",keysize,"first instance :",first_key_instance)
        second_key_instance = message[keysize:(keysize*2)]
        #print("keysize:",keysize,"second instance:",second_key_instance)
        hamming_distance = hamming_dist(first_key_instance,second_key_instance)/keysize
        hamming_key[keysize] = hamming_distance
        #print("hamm dist:",hamming_distance)
        #print("-------------------------------------------------------------------")

    # step 4
    key_value_list = sorted(hamming_key.items(),key=lambda kv : kv[1])[:3]
    keys = [k[0] for k in key_value_list]
    #print(key_value_list)
    #print(keys)

    #step 5
    for key in keys:
        new_block_list=[]
        block_position = 0
        for i in range(math.ceil(len(encryp_bytes)/key)):
            new_block_list.append(encryp_bytes[block_position:(block_position+key)])
            block_position = block_position +key
        print(new_block_list)

        #step 6
        transpose_blocks = []
        for i in range(key):
            temp_block_list = bytearray()
            for key_block in new_block_list:
                try:
                    temp_block_list.append(key_block[i])
                except:
                    continue
            transpose_blocks.append(temp_block_list)
        print(transpose_blocks)

        #step 7
        xorchecker(transpose_blocks[0])







cihper_xor(2,41,encryp_bytes)

