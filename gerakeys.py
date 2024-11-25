import random

def generate_private_key(p, length=30):
    return random.randint(10**(length-1), p-1)

def calculate_public_key(g, a, p):
    return pow(g, a, p)

p = int("""
    B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B61
    6073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BF
    ACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0
    A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371
""".replace("\n", "").replace(" ", ""), 16)

g = int("""
    A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31
    266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4
    D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28A
    D662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5
""".replace("\n", "").replace(" ", ""), 16)

private_key_a = generate_private_key(p)
public_key_A = calculate_public_key(g, private_key_a, p)

is_a_valid = private_key_a < p
is_g_valid = g < p
print(f"Valor de 'a' (chave privada): {hex(private_key_a)}")
print(f"Valor de 'A' (chave pública): {hex(public_key_A)}")
print(f"'a' é menor que 'p': {is_a_valid}")
print(f"'g' é menor que 'p': {is_g_valid}")
print(f"Valor de 'a' (chave privada): {(private_key_a)}")
print(f"Valor de 'A' (chave pública): {(public_key_A)}")