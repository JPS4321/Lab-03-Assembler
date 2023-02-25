def bin_to_hex(bin_num):
    hex_dict = {
        "0000": "0",
        "0001": "1",
        "0010": "2",
        "0011": "3",
        "0100": "4",
        "0101": "5",
        "0110": "6",
        "0111": "7",
        "1000": "8",
        "1001": "9",
        "1010": "A",
        "1011": "B",
        "1100": "C",
        "1101": "D",
        "1110": "E",
        "1111": "F",
    }
    hex_num = ""
    for i in range(0, len(bin_num), 4):
        hex_digit = hex_dict[bin_num[i:i+4]]
        hex_num += hex_digit
    return hex_num

bin_num = input("Ingrese un numero binario de 12 digitos: ")
hex_num = bin_to_hex(bin_num)
print(hex_num)