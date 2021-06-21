import string
import itertools
from termcolor import colored


p1 = "RJD TFDTCOCOS PE UNSHLI EFLMTEFE JSQ DNSCTX JOSDOSJPOGNJSE JTUFCNGRI BJDOS JPDTCTUSHERQSJ EDT FQR JBYJ EPT TCBOOV EFYJWRNSFE RJJY CMHDK MTCDFEFT XPTQ WCTW OMTBO TUSQERQSD OMY RJC YJMOB DJSUI WJCE NOD OBLITFJB DOF STDE SJC TDOC YMSCT DT UJCW OJHTCYJE BTMO RJC DYDTS YRJJE DFOC ZUPO F OOBNS NS RJB ODOE ND UIJODT CSI TDSYQOFE RJCTB JNE DFOC ENXM YT TDJ YJC DHYE DOE SJC YTYCT CSI RJB OMTI XDJB NNYPJ RJJE CTJ TOD OFPLOB DOC IBYD YBOM POD OBLITFJB RJNX NX POOV RJF CBJNSSNLI PE CMJY RJJE XHNVO BDWEMNLNGRI OPRJNSJ QJCZ OTMLPTD YT EN XHNVQ GD JNLNTXNGQF BMT RJCO RJF OSHYF EPS TRFJ RSHSXDFSIDODF JLI XNPYJ RJCO XHRJ MPHJSHRJNHDW FRSTDT PE EMPDQTJNM IRPDO HQMYRJ XHX SCTBFE SNY LENGXGPO DOE SIJX NR XJCS JR ODYDOT UL ED YF JNSJ QJC NPTU FBBFERGXC YJE YT EFTUTMZ OJTLMD JT UN EDOE JSI LENGYJSHYJ RJDJT MXM SPEFSTYJSINSJ LE UJCHS IJTUMTE YJC OZTCNHIX OCTNSNE RCOLMB ODYFEUIBOSNSX USKSNLJ MYBQ HTCXGYE GNM NFEF OGNHQHNBJJ YL JNEX IHSJ UMYCT TNQBJ YJC SHIDBND YJY CMJY EMTU HSJ EPT EJY EPTLI JY JCCTSY YT LYCTEMOC JST UWTDOOX OBU QX NLXDTSJHJYJ RJF DNEDT DOI XMEJDQ VTFTFR XIJHM NSEPWR DOE FONDTJ RJC NPTU YLPQNHOPQT YFJSJBNXY TE UJCN HNVM QCOCOCFS HNVMVJER IKNOFTQR XDT CSMYO DU TDYF BMT CFNGBYNSH JS XPNJYIJLI TN XNNLOB DOI XBOB FXGEFOS DT TMTY PE RYL YNJI SNSC OFJDT OFUSJNUT PE QT GNM VCTSNLI YT TQDWDFFE NS TQNWOCT WPT PRTU OBCTO SP ENSC NDY BYDO XHRJPTU OKL YBSHDKDHSJPO YT KQNIF T ETR PNTQ ODYCTO SN TFOCTJYF BBOTD CUPN OCDONSKBQP DKERJNSX CMGNTU GQNSEBPMEFE FSI PRYJ H DDO POOV JMNB ETQS USCOGQNSH IDOIX EPS TP MNYNYNYPOH JB FYBT MQS EMNWPRSNDFSJPOR XCTJ YM EDYDTD TRPOCS UDYFDJCT NDQCTYBST JMY RP ENSC ND JJBNS XHRJNS RJD TDYDT PE OPNXDY DOID INUHODXDX NO SJC TCBO YT OBCT YMQMID"
p2 = "RJD OCOJ TC KCT OCOPS HX SMTRJYMNE F OTMOFS MPTL DQU CMNTC ODOMT CTF T MPPJNSK BMT JCTC NX DOTYJCS TYJCOW TTEBO DHMKCT EHZGTDYZBPCMWBSO GNMVJEX NN H XHRJ ETR ZDY CTD JNVO BOPSX SZ"

known = {}

alpha = string.ascii_uppercase


known = {
    "SH": "RI",
    "DO": "EN",
    "MT": "OR",
    "NE": "OD",
    "PT": "OU",
    "RJ": "TH",
    "UO": "TN",
    "XS": "SN",
    "XH": "WI",
    "YM": "WO",
}

s1 = "CO"
for s3 in alpha:
    diff = alpha.index(s1[0]) - alpha.index(s3)
    s4 = alpha[alpha.index(s1[1]) + diff]
    print(f"{s1}->{s3}{s4}")
    diff = alpha.index(s1[0]) - alpha.index(s3)
    try:
        s4 = alpha[alpha.index(s1[1]) - diff]
    except:
        pass
    print(f"{s1}->{s3}{s4}")

for k,v in known.items():
    # print(k,v)
    diff = alpha.index(k[0]) - alpha.index(v[0])
    #assert alpha.index(v[1]) - alpha.index(k[1]) == diff

print(known)
print()

def transcribe(text):
    out = ""
    cur = ""
    space = False
    for i,p in enumerate(text):
        if p == " ":
            if cur:
                space = True
            else:
                out += " "
            continue

        if cur:
            bigram = cur + p
            lookup = known.get(bigram)
            if lookup:
                if space:
                    out += colored(f"{lookup[0]} {lookup[1]}", 'green')
                    space = False
                else:
                    out += colored(f"{lookup[0]}{lookup[1]}", 'green')
            else:
                if space:
                    out += colored(f"{bigram[0]} {bigram[1]}", 'white')
                    space = False
                else:
                    out += colored(f"{bigram[0]}{bigram[1]}", 'white')
            cur = ""
        else:
            cur += p
    print("".join(out))


transcribe(p1)
transcribe(p2)
