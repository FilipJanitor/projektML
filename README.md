## Projekt na predmet strojové učenie 2018 

# Umelý Dante

Vzhľadom na veľkosť jednotlivých súborov a omedzenia bandwidthu pre git-lfs je potrebné stiahnuť si posledný release (tu)[https://github.com/FilipJanitor/projektML/releases] a pozerať si stránku `index.html`.

Keďže dáta spojené s vizualizáciou sú väčšie, ako sa javascriptu zvykne páčiť, je potrebné prezerať si ich postupne a urobiťˇdrobné úpravy. Súbory v priečinku `out/` majú koncovky názvu tvaru `číslo` a znak `c` alebo `s`. Číslo označuje seed, ktorý bol použitý pri generovaní, znak zas, či sa jedná o básne písmenového alebo slabikového modelu. Stránka očakáva súbor `out/dataS.json` pre slabikový model a `out/dataC.json` pre písmenkový model. Pre používanie a prezeranie aktivácií je teda potrebné adekvátne si súbory premenovávať.