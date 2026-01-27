from pypdf import PdfReader

arquivo = "arquivo1.pdf"  # nome exato do seu PDF

for i in range(100000):
    senha = f"{i:05d}"

    try:
        reader = PdfReader(arquivo)   # recria o leitor a cada tentativa
        ok = reader.decrypt(senha)

        if ok == 1 or ok == 2:
            print("\n✅ SENHA ENCONTRADA:", senha)
            break

        if i % 1000 == 0:
            print("Testando:", senha)

    except Exception:
        pass
else:
    print("❌ Senha não encontrada entre 00000 e 99999")     # Para rodar: python quebrar_pdf.py quebrarletras_pdf.py
