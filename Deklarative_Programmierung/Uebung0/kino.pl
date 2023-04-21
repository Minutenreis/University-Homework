gehen_kino(anna, bernd).
gehen_kino(A,B) :- gehen_kino(B,A).

gehen_kino(fritz).
gehen_kino(A) :- gehen_kino(A,_B).
