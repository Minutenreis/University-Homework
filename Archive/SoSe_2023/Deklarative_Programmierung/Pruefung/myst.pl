myst(X, [X|T], T).
myst(X, [H|T], [H|T1]) :-
    myst(X, T, T1).

mergesort([], []). 
mergesort([A], [A]).

mergesort(Lst, Sorted) :-
    divide(Lst, L1, L2),
    mergesort(L1, S1),
    mergesort(L2, S2),
    my_merge(S1, S2, Sorted).

divide([], [], []).
divide([A], [A], []).
divide(Lst, L1, L2) :-
    length(Lst, N),
    H is N-N//2,
    length(L1, H),
    append(L1, L2, Lst).

my_merge(A, [], A).
my_merge([], B, B).
my_merge([A|Ra], [B|Rb], [A|M]) :-
    A=<B,
    my_merge(Ra, [B|Rb], M).
my_merge([A|Ra], [B|Rb], [B|M]) :-
    A>B,
    my_merge([A|Ra], Rb, M).