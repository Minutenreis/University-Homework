

mag(john, peter).
mag(peter, X) :- mag(X, peter).
mag(olli, peter) :- not(mag(peter, john)).

% 2. Erklärung rechts:
% Standardisierungen | Unifikationen
% Es werden die Variablen aus den gleichzumachenden Regeln
% standardisiert um Namensdopplungen zu vermeiden!
% Beispielaufruf: ?- trace, mag(X,Y).

% Anfrage: mag(X,Y)
% ?- mag(X,Y)
%|
%|-[1] mag(john, peter)     X=john, Y=peter
%|
%|-[2] mag(Y, peter)     X->X' | Y=X', X=peter
%|   |
%|   |-[2.1] mag(john, peter)     Y=john
%|   |
%|   |-[2.2] mag(peter, peter)     X->X'' | X''=peter, Y=peter
%|   |    |
%|   |    |-[2.2.2] ...// Prolog bleibt in diesem endlosen Zyklus stecken
%|   |
%|   |
% ALLES AB HIER WIRD NICHT ERREICHT, WÄRE ABER LOGISCHE KONSEQUENZ
%|   |
%...

% 3.
mystery([], 0).
mystery([H|T], N) :- mystery(T, N1), N is H+N1.

% Das Mystery Predikat addiert die Elemente der
% gegebenen Liste auf, es ist einfach rekursiv

% 4. Es ist nicht gegeben in welcher Reihenfolge
% die Liste die Binärdarstellung wiedergeben soll.
% Wir können also das Prädikat rekursiv oder 
% auch endrekursiv gestalten:
binaer(0,[]) :- !.
binaer(X,Liste) :-
    X1 is X//2, 
    binaer(X1,L0),
    (   X mod 2 =:= 0, Liste = [0|L0];
    	X mod 2 =:= 1, Liste = [1|L0]).

% jetzt noch die liste umdrehen? Dann noch endrekursiv:
binaer_e(X, Liste) :-
    binaer_h(X, [], Liste).

binaer_h(0, L, L) :- !.
binaer_h(X, L1, Liste) :-
    (   X mod 2 =:= 0, append([0],L1,L2);
    	X mod 2 =:= 1, append([1],L1,L2)),
    X1 is X//2,
    binaer_h(X1, L2, Liste).

% 5. Einfach:
my_member(Element, Liste) :- member(Element, Liste).

% Member selbst schreiben:
mymember(H, [H|_]).
mymember(Ele, [_|T]) :-
    mymember(Ele, T).
    
    