hex_num = input("Ingresa un numero hexadecimal de tres digitos: ")
dec_num = int(hex_num, 16)
bin_num = bin(dec_num)[2:].zfill(12)

print("The binary representation of", hex_num, "is:", bin_num)