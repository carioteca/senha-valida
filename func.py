import re

no_match = []
verify = 0

def min_size_def (passw, value):

    if len(passw) < value:
        global no_match
        no_match.append('MinSize')
    else:
        global verify
        verify += 1
    return no_match, verify

def min_upper_def(passw, value):
    caracter = re.findall('[A-Z]', passw)
    if len(caracter) < value :
        no_match.append('minUppercase')
    else:
        global verify
        verify += 1
    return no_match, verify

def min_lower_def(passw, value):
   caracter = re.findall('[a-z]', passw)
   if len(caracter) < value :
        no_match.append('minLowercase')
   else:
        global verify
        verify += 1
   return no_match, verify
 
def min_dig_def(passw, value):
    caracter = re.findall('[0-9]', passw)
    if len(caracter) >= value :
        global verify
        verify += 1
    else:
        no_match.append('minDigit')
    return no_match, verify  

def min_special_def(passw, value):
    pattern = r'[!@#$%^&*[()-+/{}]'
    caracter = re.findall(pattern, passw)
    caracter += re.findall(']', passw)
    if len(caracter) < value:
        no_match.append('minSpecialChars')
    else:
        global verify
        verify += 1
    return no_match, verify




def change_pos_def(passw):
    global verify
    qtd = len(passw) - 1
    for i in range(0, len(passw)):
        rep = char_repet_def(passw, i)
        cond = sequence_rep_def(rep)
        if cond == "noRepeted":
            no_match.append("noRepeted")
            break
        if cond != "noRepeted" and i == qtd:
             verify += 1
        

def char_repet_def(passw, pos):
    seq = 0 
    rep = []
    for i in passw:
        char = passw[pos]
        if char.upper() == i or char.lower() == i:
            rep.append(seq)
        seq += 1
    return rep

def sequence_rep_def(list_rep):
    values = 0
    n = "noRepeted"
    for i in range(0, len(list_rep)):
        anterior = i
        proxima = i + 1

        limite = len(list_rep)
        if proxima != limite:
            values = list_rep[anterior] + 1
            if values == list_rep[proxima]:
                return n