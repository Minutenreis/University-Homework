IN              ;a lesen
STORE a (13)    ;a speichern
LOADK 16        ;16 laden
SUB a (13)      ;16 - a => wenn ergebnis < 0, dann B= 12, sonst B = 5 + A
JLT (10)        ;B = 12
LOADK 5
ADD a (13)
OUT
HALT
LOADK 12
OUT
HALT
DW a