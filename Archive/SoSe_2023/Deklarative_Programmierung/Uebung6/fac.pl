fac(0,1).
fac(N,F) :-
    nonvar(N),
    N > 0,
    N1 is N-1,
    fac(N1, F1),
    F is N*F1.

fac(N,F) :-
    var(N),var(F),
    fac(N1, F1),
    N is N1 + 1,
    F is F1 * N.

fac(N,F) :-
    var(N),nonvar(F),
    fac(N1, F1),
    N is N1 + 1,
    (   F1 > F, !, false;
    F is F1 * N).
    