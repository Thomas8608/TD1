# -*- coding: utf-8 -*-




import struct



def pistes(fichier):

    f=open(fichier,"rb")

    data=f.read()

    N=struct.unpack_from("i",data[40:44],0)[0]

    Left=[]

    Right=[]

    for i in range(N//4):

        Left.append(struct.unpack_from("h",data[44+4*i:44+4*i+2],0)[0])

        Right.append(struct.unpack_from("h",data[46+4*i:46+4*i+2],0)[0])

        

    return Left,Right

    

def recopie(Left,Right,filename):

    if len(Left)!=len(Right):

        print ('listes de taille différente')

    else:

        f=open(filename,"wb")

        len_tot=4*len(Left)+44

        f.write(b"RIFF")

        f.write(struct.pack("I",len_tot-8))

        f.write(b"WAVEfmt ")

        f.write(struct.pack("IHHIIHH",16,1,2,44100,176400,4,16))

        f.write(b"data")

        f.write(struct.pack("I",len_tot-44))

       

        for i in range(len(Left)):

            f.write(struct.pack("h",Left[i]))

            f.write(struct.pack("h",Right[i]))

        f.close()

        return f



def modif1(fichier,filename):

    Left,Right=pistes(fichier)

    N=len(Left)

    Left2=[Left[2*i] for i in range (N//2)]

    Right2=[Left[2*i] for i in range (N//2)]

    

    return recopie(Left2,Right2,filename)



def modif2(fichier,filename):

    Left,Right=pistes(fichier)

    N=len(Left)

    Left2=[]

    Right2=[]

    for i in range(N-1):

        Left2.append(Left[i])

        Left2.append(0.5*Left[i]+0.5*Left[i+1])

        Right2.append(Right[i])

        Right2.append(0.5*Right[i]+0.5*Right[i+1])

    return recopie(Left2,Right2,filename)



#en multipliant la fréquence d'échantillonage par k ( ainsi que le nombre 

#d'octets par seconde) on accélère le son d'un facteur k

def recopie2(Left,Right,filename,k):

    if len(Left)!=len(Right):

        print ('listes de taille différente')

    else:

        f=open(filename,"wb")

        len_tot=4*len(Left)+44

        f.write(b"RIFF")

        f.write(struct.pack("I",len_tot-8))

        f.write(b"WAVEfmt ")

        f.write(struct.pack("IHHIIHH",16,1,2,int(k*44100),int(k*176400),4,16))

        f.write(b"data")

        f.write(struct.pack("I",len_tot-44))

       

        for i in range(len(Left)):

            f.write(struct.pack("h",Left[i]))

            f.write(struct.pack("h",Right[i]))

        f.close()

        return f

def modif3(fichier,filename,k):

    return recopie2(pistes(fichier)[0],pistes(fichier)[1],filename,k)



def modif4(fichier,filename,d,a):#d=délai a=atténuation

    Left,Right=pistes(fichier)

    N=len(Left)

    D=int(d*44100)

    for i in range(0,D):

        Left2=[Left[i]  for i in range (D)]

        Right2=[Right[i]  for i in range (D)]

        

    for i in range(D,N):

        Left2.append(Left[i] + int(a*Left[i-D]) )

        Right2.append(Right[i] + int(a*Right[i-D]) )

        

    

    return recopie(Left2,Right2,filename)

    

    