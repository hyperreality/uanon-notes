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


ct = '''
Utabstestthyothabno Ovutabthno
 
Yoabest Hwstrtututhw estutabndovyoab
AB. Hæhæabest? Esthæabest esthæthnowi rtow hwthyobe,
Hwstrtututhw, esthæabest ndabutab hæhæthestab
ebututel rtow Abhwhw'hw ndthyobe?
Ebabno Hwstrtututhw owababyo?
Hæhært ovutæbehw ab ovutestestabutowyoth
utstrtno ab hæhæababyo?
ST. Thabest yoabest ndab owyoabst
esthæthhw ovutwi hæthesthæ withyoelabel hæthnowihw,

Tsthæthhw stabthnoestabel ebhæthyoel rtow elthutest,
esthæabest hwestthnobehw abnoel hwestthnowihw;
Hæhærthwab ovuthwhw esthæab hæthestestth
abnoel esthæab owabthut abnonortthhw,
Thabest hæthest noab'abut estabhwestabhw,
abnoel ovæutestth noab'abut abnoinrtthhw:
Hwrt hæabyoyo-ovutabel hwstabnothabyohw
ebthutthyoyoth elabyothwihæest
Thno ndutndovyothnowi rtow esthæab
wiabndab esthæabth elabutab nortest ovthestab.

Abestabutnoabyo hwndthyoabhw hæthhw
abndstestthnoabhwhw ovabestutabth
Abhw hwhæabyoyorthæ hwestutændhw ututno
elthndstyothnowi abyoyo esthæab hæabth.
Hæhæabesthæabut thno owyortutthel
thndstrtestabnoebab hæab hwstæbehw,
Abnoel, abhw esthæab stutrtndstestabut ovutæesthæabhw,
esthæab stutststabest hwsoutæbehw;
Rtut abest esthæab æut rtow abutab,
owabndthyothabut estrtabel...
'''

ct = '''
Ndth Rtyoel Hærtndab

ndth rtyoel hærtndab hwndabyoyoabel rtow wirtrtel ovthutesthæ
ovrtthyoabel utabel ovænohw, beabutnoabyo rtthyo abnoel hæabnoel ndab elrthæno strtabestutth
thest'hw ovutthebbe hæhæthestab-hæabhwhæabel hæabyoyohw hæthelrthæabel ovth owthuthwest stabthnoest
esthæab estthno utrtrtow estrtst hæutndndthnowi hwrtnowihw rtow stutrtndthhwab hæhæthyoab estthndab thhw
yortebbeabel thnoestrt elabndrtnotheb uthæthesthænd hæthesthæ esthæab yoæutabhw

esthæab estutababhw hæabel estrt hæthno
hæutwiwithnowi esthæabnd, yortutthnowi esthæabnd ab estrtutestututrtuthw yortutab
ovutwiwithno' hæhæabno thest hæabhw rtutabut abnoel elrtnoab
esthæab utrtutnoel ebabndabnoestabel strtest beabstest esthæab utabthno elutrtsthw ebrtrtyo
noabthwihæovrtuthw abnoel elhæabyoyoabuthw hwstabestestabut thno esthæab strtrtyo
bethelhw styoabththnowi owrtrtestovabyoyo hæthesthæ hæthhw hæabnoel abnoel hwrtebbe
hæab hæabel hæhæabest hæab wirtest, abnoel thest hæabhwno'est ab yortest

nort rtnoab benoabhæ esthæabth hæabutab strtrtut,
hæab hæabutab abyoyo thnonortebabnoest estrt wiutababel'hw inutelwindabnoest
esthæab ebrtutnoestutth hæabhw ebrtndovuthwestthnowi hæthesthæ yothowab yothbeab ab yortnowi
hæthovabutnoabestthnowi utrtyoebabnort. hæthesthæ ab yortnowi estabyoab rtow hwutebebabhwhw yothbeab In-yort
owabutndabuthw, owthhwhæabuthw, owthwihæestabuthw,
abutabno owrtrtyohw hæabel ab styoabebab thno stutrtelutebestthrtno

esthæab ebrtabhwestabyo yothnoab hæabhw esthæab styoabebab rtow hwabelutebestthrtno
esthæab ebrtutabyo utababow hærtutyoel ndabbeab thrtut elabhwabel thno utabowyoabebestthrtno
esthæab hærtndabno hæabyobeabel hæthesthæ wiutabebab abnoel stabutowabebestthrtno
abnoel hæab inuthwest benoabhæ hæab hæabutab hæabututthrtuthw estrtrt
nortesthæthnowi ndrtutovthel, thesthw estututab. hæab hæabutab wiyortutthrtuthw

OVRTRTND!

Esthæabno rtnoab elabth thest ebabndab, hwstrtthyoabel esthæab stabutabelab yothbeab utabthno. yothbeab rtthyo thno ab owyoabndab, thest stabthnoabel, esthæab hææutest abestestabebbe hwutelelabno, rtelelabut esthæabno abyoabutabno,
hæabutelabut esthæabno ab stutnoebhæ thno esthæab hærtndov, hærtestestabut esthæabno esthæab youtnoebhæ thrtut ebrtnohwutndab. owrtut uthw, thest hæabel ab ebabnoebabutrtuthw owutndab, ndrtutab youthwest, ndabno hæhært ndabelab bethyoyothnowi hærtwiwithabhw

hwabyoyothnowi stutrtutest owutyoyoth yothbeab hææyoesthæth yothutabhwestrtebbe
thest ndabelab estthelabhw utrtebbe hæthesthæ ab elthyothwiabnoest ndrtebbe
ebrtnoowuthwabel hæabutab esthæab stabrtstyoab, thnoowuthwabel thno esthæab abutthyo
stutrtowabhwhwabel estrt abinabebest yothbeab inabhæhw thno esthæab hwabsoutabyo. estrt hæthno,
thest ebabndab thno esthæab ndrtutnothnowi hæthesthæ ab hæabutnothnowi abnoel,
hæthesthærtutest esthæab hæututestthnowi, hæabhw ab ovututelabno

rtnoyoth ebabutestabthno hæabhw elrtutovest;
ab ndthesthæthebabyo estabyoab, nort hwrtutyo benorthæhw hæabyoyo
yothovabutestth hæabnoest estrt hæabyoyo, owutababelrtnd ebabyoyoabel owrtut hwhæabyoyohw
owthabutebab hæabhw esthæab ovyorthæ, beababst thrtutut æuthw estrt esthæab hwhærthæ
thest abststæuthw rtuthæabyoyo hæabhw utthwihæest thno abthwihæestth-owrtutut
hæabel Ovthwi Ovutrtesthæabut bethyoyo Ndrtesthæabut thno hæabut hwestrtutab
hæthesthæ abyoyo rtow uthw

hæabestebhæthnowi, hæab elthelno'est yortutab hæabut abnothndrtutab
stababst ndth strtabnd:
Ndrtesthæabut hæabhw ndth rtyoel hærtndab
wirtrtel hæthyoyo thhw yortrtestabel, thno ndth rtyoel hærtndab
utabyothwithrtno thhw ovututnoabel elrthæno, thno ndth rtyoel hærtndab
bethnoelnoabhwhw thhw hwhæabebbeyoabel, thno ndth rtyoel hærtndab
inuthwestthebab hæabhw ovababno utabstabel, thno ndth rtyoel hærtndab

hæabestebhæthnowi, hæab elthelno'est yortutab hæabut abnothndrtutab
esthæab yoabnoel utrtndthesthw wihærthwesthw, thno ndth rtyoel hærtndab
hæab wirtest stthhwestrtyohw hæthesthæ abthabhw, ebrtutututstestthrtno abnoel yothabhw
estututhwestabel hwnoabbeabhw abnoel elabovesthw hæthesthærtutest ovutæbehw
hwuthwstthebthrtuthw noabhæovrtutnohw yothutab thno rtutut hærtutno
uthwabel estrt esthæab stabthno, utabebbe ovrtelthabhw nortest wiutabthno

ebhærtst yothndovhw nortest estutababhw. hwstabnoel yothutabhw nortest hææyoesthæ.
hwababbe utabnowiænoebab, estututesthæ. esthæab ebutabhwthabhwest thrtutesthæ
hærtthhwest stabthno nortest styoabnohw, ***** ow**be thrtutut styoabnohw

ovabnoelthesthw hæthyoyo ovæest uthw elrthæno, thno ndth rtyoel hærtndab. ututndrtuthw abutab yoabhæ northæ, thno ndth rtyoel hærtndab. hwabelabestthutabhw rtow owabthesthæ, thno ndth rtyoel hærtndab. utabstabuthw abutab stutabthhwabel, thno ndth rtyoel hærtndab. elabndrtnohw elutabhwhwabel hæabyoyo, thno ndth rtyoel hærtndab. thnoowabnoesthw abutab noabthyoabel, thno ndth rtyoel hærtndab. hwstthutthesthw abutab inabthyoabel, thno ndth rtyoel hærtndab. wiututelwiabhw wiutrthæ estabthyohw, thno ndth rtyoel hærtndab.
th utrthwab rtovhwebabnoab, abyoabebestuttheb, hæabestthnowi rtutesthæabutel yoabovrtut ovabnoæesthæ hwestutovovrtutno owabthesthæ abnoel rtutut owabutndhw stutrtelutebab wiutthyoestth wiututov, abnoel, rtutut bethelhw elabstabnoel rtno hwhæthowestth youtebbe, hwabab, rtutut nduthwab thhw yothowab owrtut elæesthæ thhw rtyoel, hwrt, elrtno'est ovyoabndab ndab owrtut estututesthæ th estrtyoel, hwrt...

wirtrtel hæthyoyo thhw yortrtestabel, thno ndth rtyoel hærtndab. utabyothwithrtno thhw ovututnoabel elrthæno, thno ndth rtyoel hærtndab. bethnoelnoabhwhw thhw hwhæabebbeyoabel, thno ndth rtyoel hærtndab. inuthwestthebab hæabhw ovababno utabstabel, thno ndth rtyoel hærtndab. ndututelabutabuthw hærtyoel strthwest, thno ndth rtyoel hærtndab. esthæab yoabnoel utrtndthesthw wihærthwesthw thno ndth rtyoel hærtndab
'''

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