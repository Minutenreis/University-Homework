fac(0,1).
fac(N,F) :-
    fac(N1, F1),
    (   var(N); nonvar(N),
        (   N > N1; N =< N1, !, false)),
    (   var(F); nonvar(F),
        (   F >= F1; F<F1, !, false)),
    N is N1 + 1,
    F is F1 * N.
    
