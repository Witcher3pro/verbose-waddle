import math
A2=str(input("er n i en m'te rot?"))

if A2=="ja":
    """ Her Spør jeg brukeren mange spørsmål om logaritmen i en kvadratrot """
    
    An=(float(input("Hva er n?")))
    Ak=(int(input("Hvilken rot er n kvadratisert i? 2 er den laveste roten")))
    Ap=(int(input("Hva er n opphøyd i?")))
    Atrue=An**(Ap/Ak)
    Atrue_grunntall=(float(input("Hva er grunntallet til logaritmen? ")))
    print("Log",Atrue,"=",math.log(Atrue,Atrue_grunntall))
    """ Under her så spør jeg brukeren om logaritmen er en brøk """
else:
    A3=str(input("Er logartimen en brøk?"))
    if A3=="ja":
        A_a=float(input("Hva er telleren?"))
        A_ap=int(input("Hva er telleren opphøyd i?"))
        A_b=float(input("Hva er nevneren"))
        A_bp=int(input("Hva er nevneren opphøyd i?"))
        A_ab=A_a**A_ap/A_b**A_bp
        A_grunntall=float(input("Hva er grunntallet til logaritmen?"))
        #Her sjekker jeg om brøken har noen potenser slik at hvis brøken har det så skriver den det og hvis ikke så gjør den ikke det
        if A_ap>1 or A_bp>1:
            print("Log/ln",A_a,"^",A_ap,"/",A_b,"^",A_bp,"=",math.log(A_ab,A_grunntall))
        else:
            print("Log/ln",A_a,"/",A_b,"=",math.log(A_ab,A_grunntall))
    else:
        #Her sjekker koden om logaritmen er en parantes med flere variabler
        A4=str(input("er logaritmen i en parantes?"))
        if A4=="ja":
            A_a=float(input("Hva er a i parantesen?"))
            A_ap=int(input("Hva er a  opphøyd i?"))
            A_b=float(input("Hva er b i parantesen?"))
            A_bp=int(input("Hva er b opphøyd i?"))
            A_ab=(A_a**A_ap)*(A_b**A_bp)
            A_grunntall=int(input("Hva er grunntallet?"))
            print("Log/ln (",A_a,"^",A_ap,"*",A_b,"^",A_bp,") =",math.log(A_ab,A_grunntall))
        
