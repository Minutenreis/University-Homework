import os
import subprocess

mypath = "Rezepte"

allFiles = [f for f in os.listdir(
    mypath) if os.path.isfile(os.path.join(mypath, f)) & f.endswith(".adoc")]
allFiles.sort()

if "Kochbuch.adoc" in allFiles:
    allFiles.remove("Kochbuch.adoc")
    os.remove("Rezepte/Kochbuch.adoc")

kochbuchStart = """
= Kochbuch
:toc: auto
:toclevels: 1
:doctype: book

:leveloffset: 1

"""

kochbuch = open("Rezepte/Kochbuch.adoc", "x")
kochbuch.write(kochbuchStart)
for file in allFiles:
    kochbuch.write("include::" + file + "[]\n\n")
kochbuch.close()

subprocess.run(["asciidoctor-pdf", "Rezepte/Kochbuch.adoc"])
