import os
import subprocess

mypath = "Rezepte/Cocktails"

allFiles = [f for f in os.listdir(
    mypath) if os.path.isfile(os.path.join(mypath, f)) & f.endswith(".adoc")]
allFiles.sort()

if "Cocktails.adoc" in allFiles:
    allFiles.remove("Cocktails.adoc")
    os.remove("Rezepte/Cocktails/Cocktails.adoc")

CocktailsStart = """
= Cocktails Dreßler
:toc: auto
:toclevels: 2
:doctype: book

:leveloffset: 2

"""

Cocktails = open("Rezepte/Cocktails/Cocktails.adoc", "x")
Cocktails.write(CocktailsStart)
for file in allFiles:
    Cocktails.write("include::" + file + "[]\n\n")
Cocktails.close()

subprocess.run(["asciidoctor-pdf", "Rezepte/Cocktails/Cocktails.adoc"])
