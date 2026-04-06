hex_data = "0A631B241B032E3D420137785F35077C6238147E6D2B44372D14016B3D05376F7F006E6F056A3B7852606D56376F7F073B3C06606E28036E3A552F"
key = "X0R_K3Y"
key_bytes = [ord(c) for c in key]
#aqui eu converto o hexadecimal diretamente em bytes
data_bytes = [int(hex_data[i:i+2], 16) for i in range(0, len(hex_data), 2)]
#aqui eu aplico o xor dos bytes gerados a partir do hex com o os bytes obtidos da string Key
decrypted = [data_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(data_bytes))]
print('Resultado:', ''.join(chr(b) for b in decrypted))
