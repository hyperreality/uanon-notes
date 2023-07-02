from itertools import zip_longest, tee

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def rebase_alphabet(ct, ngram=1, alphabet='abcdefghijklmnopqrstuvwxyz', mapping=None):
    if not mapping:
        mapping = {}
    def iterate_chars(ct, ngram, alphabet, mapping):
        i = 0
        for group in grouper(ct, ngram):
            key = group[0]
            # key = ''.join(group)
            if key not in mapping:
                mapping[key] = alphabet[i % len(alphabet)]
                i = i + 1
            yield mapping[key]
    return ''.join([c for c in iterate_chars(ct, ngram, alphabet, mapping)])


# autumn1
ct = '''
th ovabwiabno estrt ebyothndov esthæab ndrtutnoestabthno
esthæthhw hæabhw yortnowi abwirt
hwrtrtno ndth hæabth ovabebbe ebrtutabutabel hæthesthæ hwnorthæ
yothhwestabno hæhæabno th estabyoyo thrtut estututno ovabebbe northæ
ovabowrtutab thest thhw estrtrt yoabestab
ab esthæthhwestabel ndrtutnoestabthno hæthelabhw ab owrtutnoestabthno, abnoel
thow thrtut elutthnobe elababstyoth owutrtnd thest thrtut'yoyo owthnoel estutabnohwowrtutndabestthrtno
ovutest estrt utæebhæ thest
owthuthwest thrtut nduthwest stabhwhw rtnoab hæutnoelutabel esthærtuthwabnoel esthæthhwestabel estutabsthw
hæthyoyo thrtut ovab hwestutrtnowi abnortutwihæ?
abovyoab estrt uthwab abyoyo thrtutut hwabnohwabhw?!
elabutbeabnoabel ovyoabelabhw abnoel ebyothndovthnowi owabnoebabhw
beababst thrtutut hæthesthw hwhæabutst rtut thrtut inuthwest ndthwihæest hwstutthnowi esthæthhw estutabst.
ovabestestyoab abnoel rtutest-hwndabutest esthæab ebyoabutabut hwabnoestthnoabyohw
hærtabutelabhw rtow elændrtnohw abutabutthhæhæabutab hæthelthnowi,
hæabthestthnowi, estutththnowi estrt ebabestebhæ thrtut.
elabowestyoth ndabnortabututab esthæutrtutwihæ esthæabthut wiutthst
uthwab thrtutut hææstrtnohw abnoel thrtut inuthwest ndthwihæest estutthabyo
utst esthæab ndrtutnoestabthno stabesthæ
esthæab estabututabthno hæthnoelthnowi abutabutthhæhæabutab
inrtututnoabth wiabestestthnowi ndrtutab elthowowthebutyoest
ebrtndstabnothrtnohw owabyoyoabno
estabndstestabel ovth hwthutabnohw ebabyoyothnowi esthæabnd hwhæababestyoth
estrt esthæabthut ovyortrtelth abnoelthnowi
esthæthhw soutabhwest thhw bethyoyothnowi
th elabthyoth elæyoest ndth hwestutabnowiesthæ estrt ebrtndstyoabestab esthæthhw ndabelnoabhwhw
esthæabno th yortrtbe utst...
ndth abthabhw wiabest hæthelabut
th'el utæebhæabel esthæab ndthelelyoab rtow esthæab ndrtutnoestabthno thæuthw abwirt
th noabutabut nortestthebabel esthæab owrtutnoestabthno hwestabnoelthnowi utthwihæest thno owutrtnoest rtow ndab
wiyothndndabutthnowi hæthesthæ esthæthhwestabel estutabnohwowrtutndabestthrtno strthæabuthw.
th elutthnobe thest elababstyoth, abnoel
owababyo esthæab ebhæabnowiab thnohwthelab ndab hærthæyothnowi
ututnonothnowi hæthesthæ esthæab hæthnoel abhw ndth ebrtndstabnothrtno
ndth æuthw wiutrthæ hwhæabutstabut
ndth estababesthæ abhwestabnoelthnowi
ndth abthabhw, rtow ebrtututhwab, ebabno hwabab
ndrtutab ebyoæutyoth thno esthæthhw elabutbenoabhwhw
'''

# autumn2
ct = '''
th benorthæ ab wihærthwest ebabno hæabyobe esthæutrtutwihæ esthæab hæabyoyo
ovutest th abnd inuthwest ab hæutndabno hwestthyoyo yoæutnothnowi hærthæ estrt owabyoyo
th abnd hæhæabest th abnd abnoel hæhæabest th abnd thhw hæhært th abnd
th benorthæ hæhæabest th benorthæ abnoel abyoyo th benorthæ thhw esthæabest th owabyoyo
thow rtnoyoth th ebrtutyoel hæabyobe esthæutrtutwihæ esthæab hæabyoyo
esthæabno ndabthovab th hærtutyoel estabyoyo thrtut hæhært th abnd
ovutest th inuthwest ab hæutndabno hwestthyoyo yoæutnothnowi hærthæ estrt owabyoyo
'''

# autumn3
ct = '''
estututno thrtut rtno yothbeab ab sthærtnoab esthæabest'hw utrtrtestabel hæthesthæ esthæab utthututhw
th ebabno owababyo thest thno esthæab abthut
elabutbenoabhwhw, ndth hærtndab
hæab ebyorthwabel rtutut abthabhw abnoel wirt owyoththnowi abutabutthhæhæabutab
ndth ovyortrtel thno esthæab bethnowielrtnd ndth ovyortrtel rtno esthæab hæthnoelrthæ
hæhæabest thhw abno abhwebabstab estrt? hæhæabest thhw abhwebabstthnowi owutrtnd?
hæhæabest thow th hwrtyoel ndth hwrtutyo hæhæabno th hæabhw thrtutnowi abnoel th hæabhw elutndov?
th inuthwest elutrtststabel ab hæthhwhæ thno thrtutut owrtutnoestabthno
ebyorthwabel esthæab hwabowab thno esthæab utrtrtnd rtow esthæab stababyoabebab
hæab elrtno'est noababel esthæab beabth, hæhæabest thhw rtutut hwabebutabest?
hwrtndabesthæthnowi hæab benorthæ rtnoyoth hæhæabno hæab hwabab thest?
th owabyoest thest thno esthæab wiabutelabno, esthæab yoæutabhw ovabwiabno estrt owabyoyo
abnoel ovututthabel abyoyo esthæab hæabestebhæabesthw thno stabovyort abest esthæab hæabyoyo
ebabututthnowi rtutest esthæab hwhæabstab rtow abno hw rtno esthæabest hwbeutyoyo
thest ndabutbehw rtutest esthæab hwstrtest hæhæabutab esthæab estutæhwututab hæabhw yorthwest
estrt utabthhwab rtutut ovyortrtelyothnoab hæthesthæthno esthæabhwab esthærtutnohw
abnoel hwestutabnowiyoabhærtyoel thest hæthesthæ elabhwestthnoth
utthwihæest,
rtbe, abyoutthwihæest
'''


# autumn4
ct = '''
th abnd esthæab utabhwutututabebestthrtno abnoel th abnd esthæab yothowab
th ebrtutyoelno'est abutabut ovutthnowi ndthhwabyoow estrt hæabestab thrtut abhw th ndthwihæest
th abnd esthæab utabhwutututabebestthrtno abnoel th abnd esthæab yothowab
th ebrtutyoelno'est abutabut ovutthnowi ndthhwabyoow estrt hæabestab thrtut abhw th'el yothbeab
'''

# autumn5
ct = '''
ovyoabebbe hwæ
owabyoest thest thno ndth ovrtelth th owabyoest thest abutabutthhæhæabutab
thest rtutabutesthæutabhæ esthæab hæhærtyoab styoabebab
th estututnoabel thest estrt ndab soutthebbeyoth
thebab abovrtutab ndth hææel
hæabyobethnowi thno esthæab hwestutababesthw abnoel thest thhw ebrtyoel
hæabyoel thrtutut hææutest thno ndth abndovutabebab th ebrtutyoel owababyo thest ndabyoest
hwrtututth esthæabest ndth estthndab abnoel inrtov ebrtndab ovabowrtutab abutabutthesthæthnowi
hwrtututth esthæabest ndth estthndab abnoel inrtov ebrtndab ovabowrtutab abutabutthesthæthnowi
owabyoest thest thno esthæab utabthno hæhæabno th hwestrtrtel rtutesthwthelab esthæab hærtuthwab
owabyoest thest thno esthæab abthut th noababelabel estrt owababyo esthæabest thnoestrthwthebabestthrtno
esthæutrthæ ndab thnoestrt esthæab ovyoabebbe hwæ th elrtno'est hæabnoest estrt hæabutab ab noabndab
esthæutrthæ ndab thnoestrt esthæab ovyoabebbe hwæ th elrtno'est hæabnoest estrt hæabutab ab noabndab
th estrtutab ndth yoabwi rtowow
thrtut hæabutab hæhærtyoab abnoel ebyoæno
th estrtutab ndth yoabwi rtowow
esthæab abthut hæabhw ebyoæut abnoel estrtestabyoyoth utnoebyoæno
'''

ct = """
ABNO THNOEBABNOESTABESTTHRTNO ESTRT HÆABYOBE
ESTHÆUTRTUTWIHÆ HÆABYOYOHW:
&
THNO AB YOTHESTESTYOAB HÆHÆTHYOAB
TH'YOYO OVAB WIRTNOAB
ESTHÆAB NDRTNDABNOEST'HW ABYOUTÆELTH STABHWHWABEL
&
UTHWAB ABEST THRTUTUT RTHÆNO UTTHHWBE
"""


def canto_decode(ct):
    key = {
        'ab': 'a',
        'ov': 'b',
        'eb': 'c',
        'el': 'd',
        'ab': 'e',
        'ow': 'f',
        'wi': 'g',
        'hæ': 'h',
        'th': 'i',
        'in': 'j',
        'be': 'k',
        'yo': 'l',
        'nd': 'm',
        'no': 'n',
        'rt': 'o',
        'st': 'p',
        'so': 'q',
        'ut': 'r',
        'hw': 's',
        'es': 't',
        'ut': 'u',
        'ut': 'v',
        'hæ': 'w',
        'hw': 'x',
        'th': 'y',
        'hw': 'z',
        'æ': 'ae'
    }
    skip_one = False
    skip_two = False
    out = ''
    for a, b in pairwise(ct):
        if skip_one:
            skip_one = False
            continue
        if skip_two:
            skip_one = True
            skip_two = False
            continue
        bigram = ''.join([*a, *b])
        if bigram.lower() in key:
            out += key[bigram.lower()]
            if bigram.lower() == 'es':
                skip_two = True
            else:
                skip_one = True
        elif a == 'æ':
            out += 'ae'
        elif a == ' ':
            out += ' '
        else:
            out += a
    return out


print(canto_decode(ct))
