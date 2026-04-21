import os
import payaes

## abrir o arquivo criptografado

file_name = 'test.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## chave de descriptografia
key = b'testeransomware'
aes = payaes.AESModeOfOperationCTR(key)
decrypted_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar um novo arquivo descriptografados
new_file = 'test.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypted_data)
new_file.close()