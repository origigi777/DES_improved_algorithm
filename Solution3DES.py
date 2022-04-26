
P_i = [58, 50, 42, 34, 26, 18, 10, 2,
       60, 52, 44, 36, 28, 20, 12, 4,
       62, 54, 46, 38, 30, 22, 14, 6,
       64, 56, 48, 40, 32, 24, 16, 8,
       57, 49, 41, 33, 25, 17, 9, 1,
       59, 51, 43, 35, 27, 19, 11, 3,
       61, 53, 45, 37, 29, 21, 13, 5,
       63, 55, 47, 39, 31, 23, 15, 7]

P_f = [40, 8, 48, 16, 56, 24, 64, 32,
       39, 7, 47, 15, 55, 23, 63, 31,
       38, 6, 46, 14, 54, 22, 62, 30,
       37, 5, 45, 13, 53, 21, 61, 29,
       36, 4, 44, 12, 52, 20, 60, 28,
       35, 3, 43, 11, 51, 19, 59, 27,
       34, 2, 42, 10, 50, 18, 58, 26,
       33, 1, 41, 9, 49, 17, 57,
       25]

PC_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

S_box = [

    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]

S_box2 = [

    [[12, 3, 4, 8, 15, 6, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [15, 1, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ],

    [[12, 3, 4, 8, 15, 6, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [15, 1, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ],

    [[12, 3, 4, 8, 15, 6, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [15, 1, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ],

    [[12, 3, 4, 8, 15, 6, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [15, 1, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ],

    [[12, 3, 4, 8, 15, 6, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [15, 1, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ],

    [[12, 3, 4, 8, 15, 6, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [15, 1, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ],

    [[12, 3, 4, 8, 15, 6, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [15, 1, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ],

    [[12, 3, 4, 8, 15, 6, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [15, 1, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def str_to_bit_array2(text2):
    array2 = list()
    for char in text2:
        binval2 = binvalue2(char, 8)
        array2.extend([int(x) for x in list(binval2)])
    return array2
# Re-creates the string from the bit array.
def bit_array_to_str2(array2):
    res2 = ''.join([chr(int(y, 2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in nsplit2(array2, 8)]])
    return res2

def binvalue2(val2, bitsize2):
    binval2 = bin(val2)[2:] if isinstance(val2, int) else bin(ord(val2))[2:]
    if len(binval2) > bitsize2:
        raise "Binary value is too large"
    while len(binval2) < bitsize2:
        binval2 = "0" + binval2
    return binval2
 # Split a list into sublists of size n
def nsplit2(s, n):
    return [s[k:k + n] for k in range(0, len(s), n)]


# Convert a string into a list of bits
def str_to_bit_array(text):
    array = list()
    for char in text:
        binval = binvalue(char, 8)  # Get the character value on one byte.
        array.extend([int(x) for x in list(binval)])  # Adding the bits to the final list.
    return array

 # Re-creates the string from the bit array
def bit_array_to_str(array):
    res = ''.join([chr(int(y, 2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in nsplit(array, 8)]])
    return res
# Returns the binary value as a string of the given size
def binvalue(val, bitsize):
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "Binary value is too large"
    while len(binval) < bitsize:
        binval = "0" + binval  # Add as many 0 as needed to get the wanted size(padding).
    return binval

# Split a list into sublists of size n
def nsplit(s, n):
    return [s[k:k + n] for k in range(0, len(s), n)]


ENCRYPT = 1
DECRYPT = 0

class des():
    def __init__(self):
        self.password = None
        self.text = None
        self.keys = list()


    def run(self, key, text, action=ENCRYPT, padding=False):
        if len(key) < 8:
            raise "Key Should be 8 bytes long !"
        elif len(key) > 8:
            key = key[:8]

        self.password = key
        self.text = text

        if padding and action == ENCRYPT:
            self.addPadding()
        elif len(self.text) % 8 != 0:
            raise "Data size should be multiple of 8 !"

        self.generatekeys()  # Generates all the keys.
        text_blocks = nsplit(self.text, 8)  # Splits the text in blocks of 8 bytes.
        result = list()
        for block in text_blocks:  # Loops over all the blocks of data.
            block = str_to_bit_array(block)  # Converts the block in bit array.
            block = self.pmt(block, P_i)  # Applies the initial permutation.
            l, r = nsplit(block, 32)  # l(LEFT),r(RIGHT).
            tmp = None
            for i in range(16):  # 16 rounds.
                r_e = self.expand(r, E)  # Expand r to match K_i size (48bits).
                if action == ENCRYPT:
                    tmp = self.xor(self.keys[i], r_e)  # If encrypting,uses K_i.
                else:
                    tmp = self.xor(self.keys[15 - i], r_e)  # If decrypting,start by the last key.
                tmp = self.substitute(tmp)  # Method that will apply the SBOXes
                tmp = self.pmt(tmp, P)
                tmp = self.xor(l, tmp)
                l = r
                r = tmp
            result += self.pmt(r + l, P_f)  # Does the last permutation and appends the result to result.
        final_res = bit_array_to_str(result)
        if padding and action == DECRYPT:
            return self.removePadding(final_res)  # Removes the padding,if decrypt and padding are true.
        else:
            return final_res  # Returns the final string of data ciphered or deciphered.

    def substitute(self, r_e):  # Substitutes bytes by using SBOX.
        subblocks = nsplit(r_e, 6)  # Splits bit array into sublist of 6 bits.
        result = list()
        for i in range(len(subblocks)):  # For all the sublists
            block = subblocks[i]
            row = int(str(block[0]) + str(block[5]), 2)  # Get the row with the first and last bit
            column = int(''.join([str(x) for x in block[1:][:-1]]), 2)  # Column is the 2,3,4,5th bits
            val = S_box[i][row][column]  # Take the value in the SBOX appropriated for the round (i)
            bin = binvalue(val, 4)  # Convert the value to binary
            result += [int(x) for x in bin]  # And append it to the resulting list
        return result

    def pmt(self, block, table):
        return [block[x - 1] for x in table]

    def expand(self, block, table):  # Does the exact same thing than permutation.
        return [block[x - 1] for x in table]

    def xor(self, t1, t2):  # Applies a XOR and returns the resulting list.
        return [x ^ y for x, y in zip(t1, t2)]

    def generatekeys(self):  # Algorithm that generates all the keys.
        self.keys = []
        key = str_to_bit_array(self.password)
        key = self.pmt(key, PC_1)  # Applies the initial permutation on the key.
        l, r = nsplit(key, 28)  # Splits it in to left(l) and right(r).
        for i in range(16):  # Applies the 16 rounds.
            l, r = self.shift(l, r, SHIFT[i])  # Applies the shift w.r.t the round.
            tmp = l + r  # Merges them.
            self.keys.append(self.pmt(tmp, PC_2))  # Applies the permutation to get the K_i.

    def shift(self, l, r, n):  # Shifts a list of the given value.
        return l[n:] + l[:n], r[n:] + r[:n]

    def addPadding(self):  # Adds padding to the data
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len)

    def removePadding(self, data):  # Removes the padding of the plain text (If there is padding).
        pad_len = ord(data[-1])
        return data[:-pad_len]

    def encrypt(self, key, text, padding=True):
        return self.run(key, text, ENCRYPT, padding)

    def decrypt(self, key, text, padding=True):
        return self.run(key, text, DECRYPT, padding)

class des2():
    def __init__(self):
        self.password2 = None
        self.text2 = None
        self.keys2 = list()

    def run2(self, key2, text2, action2=ENCRYPT, padding2=False):
        if len(key2) < 8:
            raise "Key Should be 8 bytes long !"
        elif len(key2) > 8:
            key2 = key2[:8]

        self.password2 = key2
        self.text2 = text2

        if padding2 and action2 == ENCRYPT:
            self.addPadding2()
        elif len(self.text2) % 8 != 0:
            raise "Data size should be multiple of 8 !"

        self.generatekeys2()
        text_blocks2 = nsplit2(self.text2, 8)
        result2 = list()
        for block2 in text_blocks2:
            block2 = str_to_bit_array2(block2)
            block2 = self.pmt2(block2, P_i)
            l2, r2 = nsplit2(block2, 32)
            tmp2 = None
            for j in range(16):
                r_e2 = self.expand2(r2, E)
                if action2 == ENCRYPT:
                    tmp2 = self.xor2(self.keys2[j], r_e2)
                else:
                    tmp2 = self.xor2(self.keys2[15 - j], r_e2)
                tmp2 = self.substitute2(tmp2)
                tmp2 = self.pmt2(tmp2, P)
                tmp2 = self.xor2(l2, tmp2)
                l2 = r2
                r2 = tmp2
            result2 += self.pmt2(r2 + l2, P_f)
        final_res2 = bit_array_to_str2(result2)
        if padding2 and action2 == DECRYPT:
            return self.removePadding2(final_res2)
        else:
            return final_res2

    def substitute2(self, r_e2):
        subblocks2 = nsplit2(r_e2, 6)
        result2 = list()
        for i in range(len(subblocks2)):
            block2 = subblocks2[i]
            row = int(str(block2[0]) + str(block2[5]), 2)
            column = int(''.join([str(x) for x in block2[1:][:-1]]), 2)
            val2 = S_box2[i][row][column]
            bin2 = binvalue2(val2, 4)
            result2 += [int(x) for x in bin2]
        return result2

    def pmt2(self, block, table):
        return [block[x - 1] for x in table]

    def expand2(self, block, table):
        return [block[x - 1] for x in table]

    def xor2(self, t1, t2):
        return [x ^ y for x, y in zip(t1, t2)]

    def generatekeys2(self):
        self.keys2 = []
        key2 = str_to_bit_array2(self.password2)
        key2 = self.pmt2(key2, PC_1)
        l2, r2 = nsplit2(key2, 28)
        for i in range(16):
            l2, r2 = self.shift2(l2, r2, SHIFT[i])
            tmp2 = l2 + r2
            self.keys2.append(self.pmt2(tmp2, PC_2))

    def shift2(self, l2, r2, n2):
        return l2[n2:] + l2[:n2], r2[n2:] + r2[:n2]

    def addPadding2(self):
        pad_len = 8 - (len(self.text2) % 8)
        self.text2 += pad_len * chr(pad_len)

    def removePadding2(self, data):
        pad_len = ord(data[-1])
        return data[:-pad_len]

    def encrypt2(self, key2, text2, padding2=True):
        return self.run2(key2, text2, ENCRYPT, padding2)

    def decrypt2(self, key2, text2, padding2=True):
        return self.run2(key2, text2, DECRYPT, padding2)

key = input("Enter  8 ASCII Character Key:")
if len(key) < 8:
    raise "Key Should be 8 bytes long !"
elif len(key) > 8:
    key = key[:8] #cuts the key in 8 digits
text = input("Plaintext:")
d = des()
ciphered = d.encrypt(key, text, padding=True)
plain = d.decrypt(key, ciphered, padding=True)

def part2():
    print("******* part 2 the comparing--> different S-box comparing to check if avalanche effect is working *****")
    key2 = key
    text2 = text
    d2 = des2()
    ciphered2 = d2.encrypt2(key2, text2, padding2=True)
    plain2 = d2.decrypt2(key2, ciphered2, padding2=True)

    print("the encryption is: %r" % ciphered2)
    bonus2 = input("do you want to reverse  back in DES?")
    if bonus2 == 'yes':
        print("the decryption is: ", plain2)
    else:
        print("plese write yes")

    if ciphered != ciphered2:
        print("***************the avalanche effect is working correct! the encryptions are differents because of the s box************")
    else:
        print("somthing wrong")

print("the encryption is: %r" % ciphered)
bonus = input("do you want to reverse  back in DES?")
if bonus == 'yes':
    print("the decryption is: ", plain)
    part2()

else :
    print("please  write yes")

