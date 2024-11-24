from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import hashlib
import secrets

def pad(dados, tam_bloco):
    pad_len = tam_bloco - (len(dados) % tam_bloco)
    return dados + bytes([pad_len] * pad_len)

def unpad(dados, tam_bloco):
    pad_len = dados[-1]
    if pad_len > tam_bloco or pad_len == 0:
        raise ValueError("Padding invalido.")
    return dados[:-pad_len]

p = int(
    "B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D18"
    "9838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A7372"
    "4EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708"
    "DF1FB2BC2E4A4371", 16
)
a = int(
    "d559f3f776c7ccd8b38b31d83e1c82cc64fd63c338ce71b7e00cf13d92f1606df1d947efc08a2116"
    "850c052c708ae5644f399fc20d2618d94a7b50b629a635656a741bc2c7b55915dc08efff9b18ad09"
    "fba19e1667c7699069082761f092e100431f2a57eee0b2364b2d38fc5d5dfd9c496e9ec67129d706"
    "d422ceec47819a3", 16
)
B = int(
    "00AD415535A58A8B13210B7BCD64484321AB2E720504E4EDFC6916F7F553281C1050904A7BF2FCD1"
    "201DA7D4442560FAC43F2DDBE767B8379354A742D92224331A7129B80387F1A32601D3F7F72CA7FC"
    "BADBAD7E132401058B1751340C4C9758A51B78683C2DFF71EA1C4158CFF018751C61D67188D9A9EE"
    "3FE509E3742334154A", 16
)

# Calculando V
V = pow(B, a, p)
print(f"\nValor de V: {V}")

# Derivando S
S = hashlib.sha256(V.to_bytes((V.bit_length() + 7) // 8, byteorder="big")).digest()[-16:]
print(f"Chave de sessao (S): {S.hex()}")

# Decifrando a mensagem
IV = bytes.fromhex("c0dc2a198226f4a08fbc93ea939d20bc")
EMsg = bytes.fromhex(
    "0746eaaf15cb3558bd46f7c941a08c1acfae8f66a5dde4d63572b87b81e79dfcc02864cb835e224f"
    "fb216509d963b6d9"
)

cipher = Cipher(algorithms.AES(S), modes.CBC(IV))
decifrador = cipher.decryptor()
plaintext = decifrador.update(EMsg) + decifrador.finalize()

# Remover padding
plaintext = unpad(plaintext, 16)
print(f"\nMensagem decifrada (bytes): {plaintext.hex()}")

# Decodificando - Latin-1
try:
    mensagem_decodificada = plaintext.decode('latin1')
    print(f"Mensagem decifrada: {mensagem_decodificada}")
except UnicodeDecodeError:
    print("Erro ao decifrar mensagem")

# Resposta: mensagem invertida
mensagem_invertida = plaintext[::-1]
nIV = secrets.token_bytes(16)

cipher = Cipher(algorithms.AES(S), modes.CBC(nIV))
criptografador = cipher.encryptor()
resposta_cifra = criptografador.update(pad(mensagem_invertida, 16)) + criptografador.finalize()

resposta_final = nIV + resposta_cifra
print(f"\nResposta cifrada: {resposta_final.hex()}")

# Verificando a resposta cifrada
cipher = Cipher(algorithms.AES(S), modes.CBC(nIV))
decifrador_resposta = cipher.decryptor()
resposta_descriptografada = decifrador_resposta.update(resposta_cifra) + decifrador_resposta.finalize()

resposta_descriptografada = unpad(resposta_descriptografada, 16)

if resposta_descriptografada == mensagem_invertida:
    print(f"Resposta - Mensagem invertida (bytes): {resposta_descriptografada.hex()}")
    print(f"Resposta - Mensagem invertida: {resposta_descriptografada.decode('latin1')}")
else:
    print("Erro: A resposta cifrada não corresponde a resposta invertida.")
