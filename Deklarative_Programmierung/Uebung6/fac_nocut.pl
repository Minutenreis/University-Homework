fac(N, F) :-
    fac(N, F, 0, 1).
fac(N, F, N, F).
fac(N, F, N0, F0) :-
    (   nonvar(N),
        N>N0
    ;   var(N)
    ),
    (   nonvar(F),
        F>F0
    ;   var(F)
    ),
    N1 is N0+1,
    F1 is F0*N1,
    fac(N, F, N1, F1).