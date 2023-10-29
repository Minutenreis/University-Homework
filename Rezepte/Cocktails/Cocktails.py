import os
import subprocess

mypath = os.path.dirname(__file__)

allFiles = [f for f in os.listdir(
    mypath) if os.path.isfile(os.path.join(mypath, f)) & f.endswith(".adoc")]
allFiles.sort()

if "Cocktails.adoc" in allFiles:
    allFiles.remove("Cocktails.adoc")
    os.remove(os.path.join(mypath,"Cocktails.adoc"))

CocktailsStart = """
= Cocktails Hagen & Reis
:toc: auto
:toclevels: 2
:doctype: book

:leveloffset: 2

"""

Cocktails = open(os.path.join(mypath,"Cocktails.adoc"), "x")
Cocktails.write(CocktailsStart)
for file in allFiles:
    Cocktails.write("include::" + file + "[]\n\n")
Cocktails.close()

subprocess.run(["asciidoctor-pdf", os.path.join(mypath,"Cocktails.adoc")])
