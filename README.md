# Implementacija A* algoritma
Repozitorij vključuje kodo za mojo maturitetno seminarsko nalogo pri predmetu Informatika za šolsko leto 2023/2024 z naslovom "Učinkovito iskanje najkrajše poti v grafih".

Koda je napisana izkjučno v programskem jeziku Python, za delovanje programa pa je potrebna knjižnica "pygame".
V repozitoriju sta dve različici programa:
* Prva z imenom "main.py", ki vključuje glavno različico programa. Ta različica izriše vse korake, ki jih izvede program, torej je v danem trenutku razvidno, katera polja je program že obiskal in katerih ne. Različica je bolj prijazna uporabniku, saj deluje kot animacija
* Druga različica se imenuje "no_drawing.py" in je namenjena testiranju večjih mrež in bolj zapletenih postavitev ovir. Različica izriše samo začetno stanje, ko uporabnik postavi vse ovire in končno stanje, ko je algoritem končan. Tako je program veliko hitrejši, saj ni v vsakem koraku potrebno izrisovati trenutne situacije.

## Navodila za uporabo
* Uporabnik program zažene kot normalen program v jeziku Python.
* Pojavi se "pygame" okno, na katerem je narisana mreža. Uporabnik nato izbere začetno in končno polje tako, da kazalec miške postavi na želeno lokacijo in pritisne levi gumb. Začetno polje se pobarva zeleno, končno pa rdeče. Uporabnik lahko izbere le eno začetno in eno končno polje.
* Uporabnik lahko nato z kratkim pritiskom ali držanjem levega gumba izbere poljubna polja na mreži, ki bodo postala ovire. Ovire se obarvajo črno, in ne morejo biti postavljene na polji, kjer sta začetno in končno polje. Uporabnik lahko posamezno oviro tudi odstrani s pritiskom na levi miškin gumb. Uporabnik ne more odstraniti začetnega ali končnega polja.
* Ko je uporabnik zadovoljen z izbiro ovir, lahko pritisne tipko presledek na tipkovnici in s tem začene algoritem, ki bo poiskal najkrajšo pot med izbranim začetnim in končnim poljem. Če je pot nemogoče najti, bo program izpisal "Pot je nemogoče poiskati" v ukazno vrstico in se samodejno zaprl.
