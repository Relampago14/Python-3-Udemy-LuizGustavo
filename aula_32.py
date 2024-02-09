# Apresentação do método .format para formatar strings e de quebra uma breve explicação sobre parâmetros

cru = 'CRU'
zei = 'ZEI'
ro = 'RO'
classico = 6.1

string = '{primeiro} {segundo} {terceiro} {quarto:.1f}'
string_formatada = string.format(primeiro=cru, segundo=zei, terceiro=ro, quarto=classico)
print(string_formatada)
