#!/usr/bin/env python

# ex_function.py - example for function

pi = 3.141

def krog_obseg(rr):
    # rr - vhodna spremenljivka radij kroga
    # funkcija vrne obseg kroga, to je 2*pi*radij
    obseg = 2 * pi * rr
    return obseg

# TODO dodaj funkcijo za izracun obsega prvavokotnika
# vhodne spremenljivke sta a in b - dolzine obeh stranic
# def pravokotnik_obseg(aa, bb):

def for_zanka_primer():
    # for zanka isto stvar veckrat ponovi
    print "For zanka primer"
    for ii in range(1, 10):
        print " ii=%d" % (ii)
    print "Obseg krogov z radijem od 1 do 10"
    for radij in range(1, 10):
        print " radij=%d" % (radij)
        obseg = krog_obseg (radij)
        print "krog - radij=%f, obseg=%f" % (radij, obseg)

# TODO definiraj razred/class Krog, in Kvader.
# ta bo imel metode obseg() in ploscina().

def list_primer():
    # list je "container", nekaj, v kar shranjujes elemente
    # potem lahko s for zanko nad vsemi elemnti izveden neko operacijo
    # kateri so psi v Podpeci
    vsi_psi = ["Tara", "Tor", "Miki"]
    for pes in vsi_psi:
        print "ime psa je %s " % (pes)

# TODO kaj je objekt
# Nekaj, kar ima lastnosti, npr. traktor, ki ima ime, hitrost, barvo itd.
# Ali pa macka, ki je iz 4 clenok/kvadrov, vsak clen ima svojo pozicijo.

# kako zgleda traktor v farming simulator
# en xml, kjer ime traktorja, hitrost, obrati kardana.
# pri macka mis lahko macko zamenjava s traktorjem :)

def main():
    radij1 = 10
    obseg1 = krog_obseg(radij1) # rezultat bo priblizno 62.82
    print "krog1 - radij1=%f, obseg1=%f" % (radij1, obseg1)

    radij1 = 35
    obseg1 = krog_obseg(radij1) # rezultat bo priblizno 219.87
    print "krog2 - radij1=%f, obseg1=%f" % (radij1, obseg1)

    for_zanka_primer()
    list_primer()

main()

#
