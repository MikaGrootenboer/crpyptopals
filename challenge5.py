import codecs

given_string = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"
#byte_key = codecs.encode(key)
expected_result = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
repeat_key = codecs.encode(key)
byte_string = codecs.encode(given_string)
byte_result =  bytearray(len(byte_string))

def repeater(key):
    key_index = 0
    for i in range(len(byte_string)):
        byte_result[i] = byte_string[i] ^ repeat_key[key_index]
        if key_index+1 == len(key):
            key_index =0
        else:
            key_index = key_index +1
    return byte_result

def control(main,defin):
    if main == defin:
        print("Nice")

control(expected_result,codecs.encode(repeater(key),'hex').decode())



