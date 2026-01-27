from pypdf import PdfReader
import itertools
import string
import time

arquivo = "arquivo1.pdf"
# Caracteres: a-z, A-Z, 0-9
# Se quiser tirar maiúsculas para ir mais rápido, remova 'string.ascii_uppercase'
caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Define o intervalo de tamanho da senha (ex: de 1 a 6 caracteres)
tamanho_minimo = 3
tamanho_maximo = 3

print(f"🔠 Caracteres usados: {caracteres}")
print("🚀 Iniciando força bruta...")

inicio = time.time()
tentativas_totais = 0

for tamanho in range(tamanho_minimo, tamanho_maximo + 1):
    print(f"\n--- Testando senhas com {tamanho} caracteres ---")
    
    # Gera todas as combinações possíveis para esse tamanho
    gerador = itertools.product(caracteres, repeat=tamanho)
    
    for combinacao in gerador:
        senha = ''.join(combinacao)
        tentativas_totais += 1

        try:
            # Em pypdf, criar o reader dentro do loop é mais seguro para resetar o estado
            reader = PdfReader(arquivo) 
            ok = reader.decrypt(senha)

            if ok == 1 or ok == 2:
                fim = time.time()
                print(f"\n✅ SENHA ENCONTRADA: {senha}")
                print(f"⏱ Tempo total: {fim - inicio:.2f} segundos")
                print(f"🔢 Tentativas: {tentativas_totais}")
                exit() # Encerra o programa imediatamente

            # Mostra progresso a cada 1000 tentativas
            if tentativas_totais % 1000 == 0:
                print(f"Tentando: {senha} (Total: {tentativas_totais})")

        except KeyboardInterrupt:
            print("\n🛑 Interrompido pelo usuário.")
            exit()
        except Exception:
            pass

print("\n❌ Nenhuma senha encontrada até o tamanho limite.")  # Para rodar: python quebrarletras_pdf.py 
# cd C:\Users\104426\Downloads (colocar nome do arquivo)
