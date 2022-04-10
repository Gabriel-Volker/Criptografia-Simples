from Cryptodome.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from binascii import hexlify, unhexlify
def criptografar(senha, text):
        codificacao = AES.new(senha.encode("utf-8"), AES.MODE_CBC) # Define o tipo de criptografia
        vetor_inicializacao = codificacao.iv # Define um vetor de inicialização aleatório
        textocodificado = vetor_inicializacao + codificacao.encrypt(pad(text.encode("utf-8"), AES.block_size)) # Criptografa a mensagem e envia
        return textocodificado                                                                  # junto o vetor de comunicação sem criptografia
def descriptografar(senha, text):
        try:
            vetor_inicializacao = text[:16]                                                         # Pega o vetor de inicialização da mensagem
            codificacao = AES.new(senha.encode("utf-8"), AES.MODE_CBC, vetor_inicializacao)         # Define o tipo de criptografia
            textodecodificado = (unpad(codificacao.decrypt(text[16:]), AES.block_size)).decode()    # Descriptografa o texto e torna-o legivel
            return textodecodificado
        except:
            print("A senha utilizada para a descriptografia está incorreta.")
while True:
    decisao = input("O que você deseja fazer? \n 1: Criptografar\n 2: Descriptografar\n 3: Sair\n")
    if decisao == "1":
        passworda = str(input("Digite uma senha de 16 caracteres para a criptografia AES: "))
        msg = input("Digite uma mensagem para criptografar: ")
        a = criptografar(passworda, msg)
        print(hexlify(a))
    elif decisao == "2":
        password2 = input("Digite uma senha de 16 caracteres para descriptografar: ")
        msg2 = input("Digite uma mensagem para descriptografar: ")
        msg2 = bytes.fromhex(msg2)
        print("A mensagem descriptogradada é: ")
        print(descriptografar(password2, msg2))
    elif decisao == "3":
        exit()
    else:
        print("Digite 1, 2 ou 3")

# Senha que vamos utilizar: Dezesseis_letras
# Mensagem: Teste de criptografia.