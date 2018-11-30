## Projekt na predmet strojové učenie 2018

# Slabikár (slabikar.py)

Obsahuje nástroj na rozdelenie slovenského textu na slabiky. Nepísmenkové znaky sú brané ako špeciálne slabiky. Nástroj si nevie poradiť s okrajovými prípadmi, ktoré sú spôsobené nešťastnými predponami/príponami, ktoré kolidujú s iným pravidlom. Napr. *ch* sa nedelí, ale v slove *viachlasný* je akurát na rozhraní dvoch morfém, a teda výsledné slabiky by mali byť *viac-hlas-ný*. Taktiež, nevie si poradiť s dvojicou samohlások, ktoré majú jednoslabičnú výslovnosť *au-to*. Tieto prípady sú však pomerne ojedinelé 
