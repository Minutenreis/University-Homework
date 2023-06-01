knoten(n1).
knoten(n2). knoten(n3). knoten(n4).
knoten(n5). knoten(n6). knoten(n7).
nachbar(n1, n2). nachbar(n1, n3). nachbar(n1, n4).
nachbar(n2, n5). nachbar(n2, n6). nachbar(n2, n7).
nachbar(n3, n5). nachbar(n3, n6). nachbar(n3, n7).
nachbar(n4, n5). nachbar(n4, n6). nachbar(n4, n7).
nachbar(n6, n1).

start(n1).


loesung(X) :-
    knoten(X),
    ist_loesung(X).

ist_loesung(n6).

loesungen(X, Y) :-
    start(X),
    erreichbar(X, Y),
    loesung(Y).

% erreichbar ist die transitive Hülle von nachbar, weil Y von X aus erreichbar ist, wenn es eine Folge
% von Knoten gibt, die alle Nachbarn sind: erreichbar(X,Y) :- nachbar(X,A), nachbar(A,B), ..., nachbar(W,X), nachbar(X,Y).
erreichbar(X, X).
erreichbar(X, Y) :-
    nachbar(X, Z),
    erreichbar(Z, Y).

% loesungen(n1,S). =>
% S = n6 ;
% S = n6 ;
% S = n6 ;
% false.

% erstes Ergebnis: n1 => n2 => n6
% zweites Ergebnis: n1 => n3 => n6
% drittes Ergebnis: n1 => n4 => n6

% Prolog sucht immer erst so lange weiter bis es keine Lösung mehr findet und backtracked dann
% => Depth First Search, es geht also erst nach n2 und such nach der Lösung (Weg zu n6),
% bevor es dann nach dem Absuchen zu n3 geht und dann nach n4. In jedem Teilbereich werden alle weiteren Wege untersucht.
% Wenn es keine Lösung gibt, wird zurückgegangen und der nächste Weg untersucht.

% Deswegen ist es wichtig, dass es keine Zyklen gibt, sonst läuft Prolog unendlich 
% (unendlich Ergebnisse, wenn n6 auf dem Zyklus liegt, sonst keines)