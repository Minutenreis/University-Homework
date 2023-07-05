collatz(N, L) :-
    nonvar(L),
    collatzNorm(N, L).

collatz(N, L) :-
    var(L),
    collatzList(N, L).

nextCollatz(N, CN) :-
    0 is N mod 2,
    CN is N/2.
nextCollatz(N, CN) :-
    1 is N mod 2,
    CN is 3*N+1.

collatzNorm(1, [1, 4, 2]).
collatzNorm(2, [2, 1, 4]).
collatzNorm(4, [4, 2, 1]).
collatzNorm(N, [N|L]) :-
    notBaseCase(N),
    nextCollatz(N, CN),
    collatzNorm(CN, L). 

notBaseCase(N) :-
    dif(N, 1),
    dif(N, 2),
    dif(N, 4).

collatzList(N, L) :-
    collatzList(N, L, 1, [1, 4, 2]).
collatzList(N, L, N, L).
collatzList(N, L, N0, _) :-
    gt(N, N0),
    N1 is N0+1,
    collatzNorm(N1, L1),
    collatzList(N, L, N1, L1).

gt(Var, Value) :- % Var > Value if Var is bound
    (   nonvar(Var),
        Var>Value
    ;   var(Var)
    ).