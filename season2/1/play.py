import string
import itertools
from termcolor import colored
from string import ascii_uppercase
from itertools import product
from re import findall


p1 = "RJD TFDTCOCOS PE UNSHLI EFLMTEFE JSQ DNSCTX JOSDOSJPOGNJSE JTUFCNGRI BJDOS JPDTCTUSHERQSJ EDT FQR JBYJ EPT TCBOOV EFYJWRNSFE RJJY CMHDK MTCDFEFT XPTQ WCTW OMTBO TUSQERQSD OMY RJC YJMOB DJSUI WJCE NOD OBLITFJB DOF STDE SJC TDOC YMSCT DT UJCW OJHTCYJE BTMO RJC DYDTS YRJJE DFOC ZUPO F OOBNS NS RJB ODOE ND UIJODT CSI TDSYQOFE RJCTB JNE DFOC ENXM YT TDJ YJC DHYE DOE SJC YTYCT CSI RJB OMTI XDJB NNYPJ RJJE CTJ TOD OFPLOB DOC IBYD YBOM POD OBLITFJB RJNX NX POOV RJF CBJNSSNLI PE CMJY RJJE XHNVO BDWEMNLNGRI OPRJNSJ QJCZ OTMLPTD YT EN XHNVQ GD JNLNTXNGQF BMT RJCO RJF OSHYF EPS TRFJ RSHSXDFSIDODF JLI XNPYJ RJCO XHRJ MPHJSHRJNHDW FRSTDT PE EMPDQTJNM IRPDO HQMYRJ XHX SCTBFE SNY LENGXGPO DOE SIJX NR XJCS JR ODYDOT UL ED YF JNSJ QJC NPTU FBBFERGXC YJE YT EFTUTMZ OJTLMD JT UN EDOE JSI LENGYJSHYJ RJDJT MXM SPEFSTYJSINSJ LE UJCHS IJTUMTE YJC OZTCNHIX OCTNSNE RCOLMB ODYFEUIBOSNSX USKSNLJ MYBQ HTCXGYE GNM NFEF OGNHQHNBJJ YL JNEX IHSJ UMYCT TNQBJ YJC SHIDBND YJY CMJY EMTU HSJ EPT EJY EPTLI JY JCCTSY YT LYCTEMOC JST UWTDOOX OBU QX NLXDTSJHJYJ RJF DNEDT DOI XMEJDQ VTFTFR XIJHM NSEPWR DOE FONDTJ RJC NPTU YLPQNHOPQT YFJSJBNXY TE UJCN HNVM QCOCOCFS HNVMVJER IKNOFTQR XDT CSMYO DU TDYF BMT CFNGBYNSH JS XPNJYIJLI TN XNNLOB DOI XBOB FXGEFOS DT TMTY PE RYL YNJI SNSC OFJDT OFUSJNUT PE QT GNM VCTSNLI YT TQDWDFFE NS TQNWOCT WPT PRTU OBCTO SP ENSC NDY BYDO XHRJPTU OKL YBSHDKDHSJPO YT KQNIF T ETR PNTQ ODYCTO SN TFOCTJYF BBOTD CUPN OCDONSKBQP DKERJNSX CMGNTU GQNSEBPMEFE FSI PRYJ H DDO POOV JMNB ETQS USCOGQNSH IDOIX EPS TP MNYNYNYPOH JB FYBT MQS EMNWPRSNDFSJPOR XCTJ YM EDYDTD TRPOCS UDYFDJCT NDQCTYBST JMY RP ENSC ND JJBNS XHRJNS RJD TDYDT PE OPNXDY DOID INUHODXDX NO SJC TCBO YT OBCT YMQMID"
p2 = "RJD OCOJ TC KCT OCOPS HX SMTRJYMNE F OTMOFS MPTL DQU CMNTC ODOMT CTF T MPPJNSK BMT JCTC NX DOTYJCS TYJCOW TTEBO DHMKCT EHZGTDYZBPCMWBSO GNMVJEX NN H XHRJ ETR ZDY CTD JNVO BOPSX SZ"
 
def uniq(seq):
    seen = {}
    return [seen.setdefault(x, x) for x in seq if x not in seen]
 
def partition(seq, n):
    return [seq[i : i + n] for i in range(0, len(seq), n)]
 
 
"""Instantiate a specific encoder/decoder."""
def playfair(key, from_ = 'J', to = None):
    if to is None:
        to = 'I' if from_ == 'J' else ''
 
    def canonicalize(s):
        return "".join(filter(str.isupper, s.upper())).replace(from_, to)
 
    # Build 5x5 matrix.
    m = partition(uniq(canonicalize(key + ascii_uppercase)), 5)
 
    # Pregenerate all forward translations.
    enc = {}
 
    # Map pairs in same row.
    for row in m:
        for i, j in product(range(5), repeat=2):
            if i != j:
                enc[row[i] + row[j]] = row[(i + 1) % 5] + row[(j + 1) % 5]
 
    # Map pairs in same column.
    for c in zip(*m):
        for i, j in product(range(5), repeat=2):
            if i != j:
                enc[c[i] + c[j]] = c[(i + 1) % 5] + c[(j + 1) % 5]
 
    # Map pairs with cross-connections.
    for i1, j1, i2, j2 in product(range(5), repeat=4):
        if i1 != i2 and j1 != j2:
            enc[m[i1][j1] + m[i2][j2]] = m[i1][j2] + m[i2][j1]
 
    # Generate reverse translations.
    dec = dict((v, k) for k, v in enc.items())
 
    def sub_enc(txt):
        lst = findall(r"(.)(?:(?!\1)(.))?", canonicalize(txt))
        return " ".join(enc[a + (b if b else 'X')] for a, b in lst)
 
    def sub_dec(encoded):
        return "".join(dec[p] for p in partition(canonicalize(encoded), 2))
 
    return sub_enc, sub_dec
 
 
(encode, decode) = playfair("", from_="A")
print("p1:", decode(p1))
print("p2:", decode(p2))
