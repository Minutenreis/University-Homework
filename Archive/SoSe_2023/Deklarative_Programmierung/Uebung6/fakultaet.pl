fac(N, F) :-
    fac(N, F, 0, 1).
fac(N, F, N, F).
fac(N, F, N0, F0) :-
    gt(N, N0),
    gt(F, F0),
    N1 is N0+1,
    F1 is F0*N1,
    fac(N, F, N1, F1).
gt(Var, Value) :- % Var > Value if Var is bound
    (   nonvar(Var),
        Var>Value
    ;   var(Var)
    ).