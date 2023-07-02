a1 = """agates:sagos
agaves:sagos
alamos:sales
alamos:salts
alares:salts
alarms:sales
alarms:salts
amatol:lamel
apalit:tapet
apathy:yaply
arabit:tarot
atavus:sates
atazir:rater
avails:saves
caches:scabs
caches:scads
caches:scags
caches:scams
caches:scans
caches:scars
caches:scats
cactus:scabs
cactus:scads
cactus:scags
cactus:scams
cactus:scans
cactus:scars
dudine:educe
elects:selfs
emends:semis
enemas:sends
erects:serfs
icings:sicks
idioms:sides
idiots:sides
iliads:silks
iliads:silos
iliads:silts
lilacs:slims
lilacs:slips
lilacs:slits
momble:emote
nances:snags
nances:snaps
nanpie:enage
nanpie:enate
nantle:enage
ninths:snips
nonces:snobs
nonces:snots
nonces:snows
nongas:snobs
nongas:snots
nongas:snows
nonius:snobs
nonius:snots
nonius:snows
nuncle:enure
odours:sodas
papers:spans
papers:spats
papers:spays
peplos:specs
peplos:spews
peplus:specs
peplus:speos
peplus:spews
pipers:spics
pipers:spins
pipers:spits
pipets:spics
pipets:spins
pupils:spuds
pupils:spues
pupils:spurs
rarest:tract
rarest:trait
rarest:trant
rarest:trapt
taters:stabs
taters:stags
taters:stays
tetras:stems
tetras:steps
tetras:stews
titans:sties
titans:stirs
tithes:stirs
titles:stirs
totals:stops
totals:stows
totems:stoas
totems:stops
totems:stows
toters:stoas
toters:stops
toters:stows
tutors:stubs
tutors:studs
tutors:stuns"""

first = [c.split(':') for c in a1.split("\n")]

# print(first)

a2 = """abatis:instr
adance:cheng
adaunt:notum
alaite:their
apalit:istle
apalit:iztle
avails:lesiy
avails:lysin
avaunt:notum
awakes:ensky
babels:loser
babels:lysed
babery:royet
babied:eldin
babies:elsin
babies:eosin
bebait:iotas
bebang:nogal
bebump:mopus
biblus:unsly
bobcat:aitch
buboed:eidos
buboed:endow
buboes:epsom
cactus:unsty
cecils:lysin
cecity:tayir
cicely:layed
cicely:layer
cyclas:aisle
cyclas:arsle
cycler:earls
dadoes:epsom
dadoes:eusol
deduct:citua
didoes:epsom
didoes:eusol
dudaim:ismal
dudish:sahib
dudism:semic
dudler:earls
dudler:early
egesta:trash
egesta:trasy
ejecta:thack
ejecta:tlaco
ejecta:track
ejects:tasco
elects:tasco
emends:dasnt
emends:disna
erects:tasco
exedra:roads
exeunt:notum
fifers:rased
fifers:rasen
fifers:rosed
fifers:rosel
fifers:roset
fifths:haste
fifths:hasty
gagers:risen
gagers:rosed
gagers:rosel
gagers:roset
giglot:oftly
giglot:outly
guglia:italy
guglio:idola
guglio:idols
iciest:sated
idiasm:somal
idiasm:sumac
idioms:mason
idioms:meson
koklas:aisle
koklas:arsle
mamies:elsin
mamies:eosin
memory:rayon
mimeos:onset
mimeos:orsel
mimeos:ousel
mimeos:owsen
mimeos:owser
mimers:rased
mimers:rasen
mimers:rosed
mimers:rosel
mimers:roset
moment:nates
moment:niter
nanism:semic
ninety:tayer
ninety:toyed
ninety:toyer
ninths:haste
ninths:hasty
nonage:gleam
nonage:great
nonair:ihram
nonary:riyal
nonius:upsit
nonuse:sieur
oboist:satin
obolus:unsly
odours:resun
odours:resup
papern:runed
papern:runes
papers:risen
papers:rosed
papers:rosel
papers:roset
papery:royet
papier:enrib
papion:ornis
papism:semic
papist:sotie
papule:lieut
papule:lieux
peplus:unsly
pipage:gleam
pipage:glean
pipage:great
pipers:rased
pipers:rasen
pipers:rosed
pipers:rosel
pipers:roset
pipery:rayed
pipery:royet
popely:layed
popely:layer
popery:rayed
popish:sahib
pupate:tread
pupate:tweag
pupate:tweak
pupils:lesiy
pupils:lysin
pupoid:indol
pupoid:indow
rarest:sited
rerail:inlaw
rerail:inlay
rerail:islam
rerail:islay
rerank:nikau
sisham:abmho
sister:earth
suslik:inkle
taters:risen
taters:rosed
taters:rosel
tetany:noyau
tetard:rudas
titers:rased
titers:rasen
titers:rosed
titers:rosel
titler:earls
titler:early
totems:maser
totems:miser
totems:mused
totems:muser
totems:mysel
toters:rased
toters:rasen
toters:risen
tutors:resow
tutory:rayon
urushi:heist
urushi:hoise
urushi:hoist
usuary:riyal
usuary:royal
uvulae:atelo
uvulae:axels
uvulae:ayelp
uvulas:aisle
uvulas:arsle
vivace:cheap
vivace:cheat
vivace:clead
vivace:cleam
vivace:clean
vivace:clear
vivace:cleat
vivace:creak
vivace:cream
vivace:creat
vivant:notal
vivary:royal
vively:layed
vively:layer
vivers:rased
vivers:rasen
vivers:rosed
vivers:rosel
vivers:roset"""

second = [c.split(':') for c in a2.split("\n")]

# print(second)

# inter = [c for c in second if c in first]

# print(inter)

for row1 in first:
    for row2 in second:
        if row1[0] == row2[0]:
            # print(row1[1])
            # print(row2[1])
            if row1[1][2] == row2[1][4]:
                print(row1[1])
                print(row2[1])
