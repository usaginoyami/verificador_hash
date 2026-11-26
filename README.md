# Verificador de Hash 🔐

Aplicativo desenvolvido em **Python** para verificar a integridade de arquivos por meio da comparação de códigos hash.

O programa permite selecionar um arquivo do computador, inserir um hash de referência e verificar se o conteúdo do arquivo corresponde ao código informado.

## Funcionalidades

- Seleção de arquivos diretamente pelo computador.
- Comparação entre hash informado e hash calculado.
- Interface gráfica simples e intuitiva.
- Suporte a quatro algoritmos:
  - MD5
  - SHA-1
  - SHA-256
  - SHA-512
- Leitura de arquivos em blocos de 1 MB, evitando carregar arquivos grandes inteiramente na memória.
- Resultado visual indicando se o hash corresponde ou é diferente.

## Tecnologias utilizadas

- Python 3
- Tkinter – Interface gráfica.
- Hashlib – Cálculo dos códigos hash.
- Pathlib – Manipulação de caminhos e arquivos.

## Requisitos

- Python 3.8 ou superior.
- Tkinter instalado (geralmente já incluído na instalação padrão do Python).

## Como utilizar

**1. Clone o repositório**

```bash
git clone https://github.com/SEU-USUARIO/verificador-hash.git
```

**2. Entre na pasta**

```bash
cd verificador-hash
```

**3. Execute o aplicativo**

```bash
python verificador_hash.py
```

## Como funciona

1. Selecione o arquivo que deseja verificar.
2. Escolha o algoritmo de hash.
3. Insira o código hash de referência.
4. Clique em **VERIFICAR ARQUIVO**.
5. Consulte o resultado apresentado.

### Resultados possíveis

- **HASH COMPATÍVEL:** o hash calculado é idêntico ao informado.
- **HASH DIFERENTE:** o conteúdo do arquivo não corresponde ao hash informado.

## Segurança e observações

O aplicativo verifica a integridade dos arquivos através de funções criptográficas de hash.

Uma correspondência indica que o conteúdo do arquivo corresponde ao hash fornecido, mas não garante, por si só, a autenticidade ou procedência do arquivo.

Para uma verificação confiável, utilize hashes publicados por fontes oficiais.

## Licença

Este projeto pode ser disponibilizado sob a licença MIT. Para isso, adicione um arquivo `LICENSE` com o texto da licença correspondente.

---

**Desenvolvido em Python.**
