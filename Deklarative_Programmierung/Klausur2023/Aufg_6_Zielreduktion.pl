sieht(adam, berta).
sieht(chris, dora) :-
    sieht(dora, adam).
sieht(berta, adam).
sieht(_X,Y):- sieht(_Z, Y).
sieht(X,_Y):- sieht(X, _Z).

% adam, berta, dora, dora, dora, ...