try: 
    file = open("arquivo.txt", "x")

    file.write("SÓ ALEGRIA HA! HA! HA!")

    file.close()

except FileExistsError:
    print("O arquivo já existe.")
    