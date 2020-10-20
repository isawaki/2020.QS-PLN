import pyperclip, re

# Cria regex para telefone.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?               # codigo de area
    (\s|-|\.)?                       # separador
    (\d{3})                          # primeiros 3 digitos
    (\s|-|\.)                        # separador
    (\d{4})                          # ultimos 4 digitos
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   # extensao
    )''', re.VERBOSE)

# TODO: Cria a regex para e-mail
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+        # nome do usuario
    @                        # simbolo @
    [a-zA-Z0-9.-]+           # nome do dominio
    (\.[a-zA-Z]{2,4}){1,2}   # ponto seguido de outros caracteres
    )''', re.VERBOSE)

# TODO: Encontra correspondências no texto do clipboard
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# TODO: Copia os resultados para o clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')