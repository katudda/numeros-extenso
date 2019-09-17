from dicionario import dicionario

def num_extenso(x):
    resultado = ''
    _int, cent = str(x).split(',')
    
    if len(_int) > 9:
        return 'Este programa só aceita até 9 dígitos antes da vírgula'

    if len(cent) != 2:
        return 'Este programa só aceita 2 dígitos depois da vírgula'

    num = str(_int).zfill(9)
    chunks, chunk_size = len(num), 3
    splited = [ num[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
    mi, m, c = splited

    
    if int(mi) > 0:
        if int(mi) == 1:
           resultado += centenas(mi) + 'milhão'          
        else:
            resultado += centenas(mi) + 'milhões' 

    if int(mi) >= 1 and int(m) == 0 and int(c) == 0:
        resultado += ' de'
    elif int(mi) >= 1 and int(m) == 0 and int(c) > 0:
        resultado += ' e '

    if int(m) > 0 and int(c) == 0:
        resultado += centenas(m) + 'mil' 
    elif int(m) >= 1 and int(c) > 0:
        resultado += centenas(m) + 'mil e '

    resultado += centenas(c)

    if int(m) == 0 and int(c) == 1:
        resultado += 'real'
    elif int(mi) == 0 and int(m) == 0 and int(c) == 0:
        resultado = 'zero reais'
    else: 
        resultado += 'reais'

    if int(cent) == 1:
        resultado += ' e ' + centenas(cent) + 'centavo'
    elif int(cent) > 0:
        resultado += ' e ' + centenas(cent) + 'centavos'

    return resultado.strip().capitalize().replace('  ', ' ')


def centenas(c):
    resultado = ''
    cn, dz, un = c.zfill(3)
    cn, dz, un = int(cn), int(dz), int(un)

    if cn == 1 and dz == 0 and un == 0:
        resultado += dicionario['centena'][int(cn)] + ' ' 
    elif cn == 1 and (dz > 0 or un > 0):
        resultado += str(dicionario['centena'][cn]).replace('m', 'nto e') + ' '
    elif cn > 0:
        resultado += str(dicionario['centena'][cn]) + ' e'
        
    if dz < 1 or (dz == 1 and un == 0):
        resultado += dicionario['dezena'][dz] + ' ' 
    elif dz == 1 and un > 0:
        resultado += dicionario['dezena'][un+1] + ' ' 
    elif dz > 0:
        resultado += dicionario['dezenaDez'][dz] + ' e ' 

    if (dz > 1 or dz == 0) and un <= 9:
        resultado += dicionario['unidade'][un] + ' '

    return resultado


if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    print(num_extenso(sys.argv[1]))

