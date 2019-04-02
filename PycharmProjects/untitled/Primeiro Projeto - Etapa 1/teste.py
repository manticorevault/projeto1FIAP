nivel = input("Digite seu nível de usuário (USR, ADM ou GUEST)").upper()
genero = input("Digite seu gênero (M ou F)").upper()

if nivel=="ADM" and genero=="M":
    print("Olá, administrador")
elif nivel=="ADM":
    print("Olá, administradora")

if nivel=="USR" and genero=="M":
    print("Olá, usuário")
elif nivel=="USR":
    print("Olá, usuária")

if nivel=="GUEST" and genero=="M":
    print("Olá, convidado")
elif nivel=="GUEST":
    print("Olá, convidada")

if nivel=="" and genero=="M":
    print("Olá, desconhecido")
elif nivel=="":
    print("Olá, desconhecido")

print("Seja bem vindo ao sistema teste em Python")