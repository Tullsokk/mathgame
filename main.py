
from random import randint

print("hei og velkommen")
print("Hva er ditt navn?")
navn = input()
print ("Hei " + navn)
print("Hvor gammel er du?")
alder = int(input())
if alder > 8:
    maxtall = 20
else:
    maxtall = 10
    
        
    

print("Hvor mange oppgaver vil du løse?")

antalloppgaver = int(input())

antallsvar=0
score=0
antallsvar = 1

while antallsvar <= antalloppgaver:
    x= randint(1,maxtall)
    y= randint(1,maxtall)
    riktigsvar = x+y
    print("Oppgave " + str(antallsvar) +  ": Hva er " + str(x) + " + " + str(y) + "?")
    svar=int(input())
    if svar == riktigsvar:
        print("Riktig svar! Bra jobba " + navn)
        score = score + 1
        antallsvar = antallsvar + 1
    elif svar != riktigsvar:
        print("Feil svar, riktig svar var " + str(riktigsvar))
        score = score
        antallsvar = antallsvar + 1
print ("Du fikk " + (str(score) + " av "  + str(antalloppgaver) + " Riktige svar"))
    
