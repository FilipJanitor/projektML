def slabikar(text): #normalny string
  stav = 1
  #lower nefunguje na unicode. Shit
  samohlasky = set(["a","e","i","o","u","á","é","í","ó","ô","ú","ä","y","ý","ì"])
  dvojhlasky = set(["ia","ie","iu"])
  nedelitelne = set(["dz","ch","dž"])
  specznaky = set(["\n", "-",".",":",",","\"","\'",";","!", "?","(",")","-", "‒", "’", "„", "“"," ", "‚", "‘"])
  slabicne = set(["r","l","ŕ","ĺ"]) #len ak su medzi dvoma spoluhlaskami
  spoluhlasky = set(["d","t","n","l","h","g","k","ď","ť","ň","ľ","c","č","ž","š","j","m","b","p","v","z","s","f","r","ŕ","ĺ","q","w","x"])
  start,i = 0,0
  prvasamoh = 0
  rozsek = 0 #rozsek pouzivame na rozseknutie skupiny spoluhlasok
  pocitac = 0 #hovori, o kolko sa ma zvacsit rozsek ak pride dalsia spoluhlaska
  data = []
  state = 1
  while i <= len(text): #text vzdy konci na specznak, cize to triggerne stav 10 a ten nekonzumuje
    if stav == 1:
      #kvoli konzumentovi, uz sme docitali
      if i == len(text):
        break
      if text[i].lower() in samohlasky:
        stav = 4
        prvasamoh = i
        i += 1
        continue
      if text[i].lower() in spoluhlasky:
        stav = 2
        i += 1
        continue
      if text[i].lower() in specznaky: #v prvom stave ak vidime specznak, musime ho skonzumovat #tu sa prida parsovanie cisel
        i+=1
        stav = 10#stav = 1
        #vycistit
        continue#continue
    if stav == 2:
      if text[i].lower() in samohlasky:
        stav = 4
        prvasamoh = i
        i += 1
        continue
      if text[i].lower() in slabicne:
        #pozor na nastavenie prvej samohlasky
        prvasamoh = i
        stav = 3
        i += 1
        continue
      if text[i].lower() in spoluhlasky:
        i += 1
        continue
      if text[i].lower() in specznaky:
        stav = 10#stav = 1
        #vycistit
        continue#continue
    if stav == 3:
      if text[i].lower() in spoluhlasky:#bola slabicna
        pocitac = 1
        stav = 6
        i += 1
        continue
      if text[i].lower() in samohlasky:
        stav = 4
        prvasamoh = i
        i += 1
        continue
      if text[i].lower() in specznaky:
        stav = 10#stav = 1
        #vycistit
        continue#continue
    if stav == 4:
      if text[prvasamoh:i+1].lower() in dvojhlasky:#dvojhlasku nedelime
        stav = 4
        prvasamoh = i
        i += 1
        continue
      if text[i].lower() in samohlasky: #dve samohlasky za sebou anie dvojhlaska. Toto deli
        stav = 10
        continue
      if text[i].lower() in spoluhlasky:
        pocitac += 1
        stav = 6
        i += 1
        continue
      if text[i].lower() in specznaky:
        stav = 10 #ziadne i+i, desiatka upratuje na zaklade aktualnej polohy. Ten spec znak este nesmieme precitat
        continue
    if stav == 5: #nepouzit 
      #pozor, aj jednohlaskova slabika moze byt na konci slova. Cize to rozdelime uplne normalne Ko-re-a
      #vycistit
      stav = 1
      continue
        
    if stav == 6: #nedelitelna dvojhlaska sa sprava ako jednohlaska. Hmm viac-hlas-ny ALE na-cho-vat SLOVENCIN
      #precitana je jedna spoluhlaska
      if text[i-1:i+1].lower() in nedelitelne:
        # toto je ten okrajovy pripad. Kedze ale nedelitelne nie su same sebe prefixom, mozeme to takto spravit
        pocitac = 2
        i += 1
        stav = 6
        continue
      if text[i].lower() in samohlasky: #delime po prvej samohlaske
        i = prvasamoh + rozsek + 1 #rozsek v tomto pripade bude 0
        stav = 10
        continue
      #za-vrz-gal
      if text[i].lower() in slabicne:
        stav = 7
        i+=1
        continue
        #osetrit, zistit ci je slabicna. Ak nie je, je to cluster(take slovo asi ani nie je) a delime normlane, po prvej. Ak je slabicna pred prvou
      if text[i].lower() in spoluhlasky: #ak je skupina 2 a viac spoluhlasok, delime po prvej hlaske
        rozsek = pocitac
        i = prvasamoh + rozsek + 1 #rozsek v tomto pripade bude 0
        stav = 10
        continue
      if text[i].lower() in specznaky: #koniec slova
        stav = 10
        continue
        
    if stav == 7: #precitali sme mozno slabicnu 
      if text[i].lower() in spoluhlasky: #bola slabicna, cize sekame na zaciatku
        i = prvasamoh + rozsek + 1 #rozsek v tomto pripade bude 0
        stav = 10
        continue
      else:
        rozsek = pocitac #nebola slabicna, je to cluster, sekame po prvej
        i = prvasamoh + rozsek + 1 #rozsek v tomto pripade bude 0
        stav = 10
        continue
    
    if stav == 10:
      temp = text[start:i]
      start = i
      prvasamoh,pocitac, rozsek = 0,0,0
      stav = 1
      data.append(temp)
      continue      
    print("bro!")
    print(stav)
    print(i)
    print(text[i])
    break
  return data

moj = ""
with open("subor.txt","r") as cf:
  moj = cf.read()
print(len(slabikar(moj)))
