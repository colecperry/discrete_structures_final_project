
from Caesar import CaesarCipher
from affine import AffineCipher

caesar = CaesarCipher(input("Enter a key for the cipher: "))

encrypted = caesar.encrypt(input("Enter a string to encrypt: "))
print(f"Encrypted string: {encrypted}")

decrypted = caesar.decrypt(encrypted)
print(f"Decrypted string: {decrypted}")

affine = AffineCipher(
    input("Enter an x coefficient for the shift key function: "),
    input("Enter a constant for the shift key function: ")
)

# call the ecnrypt method, and assign True or False return value to 'success'
success, a_encrypted = affine.encrypt(input("Enter a string to encrypt: "))
# print result of encryption
print(f"Encrypted string: {a_encrypted}")

# if encryption was successful initiate decryption
if success:
    success, a_decrypted = affine.decrypt(a_encrypted)
    # if decryption was successful print decrypted string
    if success:
        print(f"Decrypted string: {a_decrypted}")