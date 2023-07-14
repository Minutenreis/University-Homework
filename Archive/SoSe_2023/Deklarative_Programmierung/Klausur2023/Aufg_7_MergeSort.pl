sortiert([], []). 
sortiert([X], [X]).
sortiert(List, Sorted) :-
    geteilt(List, ListA, ListB),
    sortiert(ListA, SortedA),
    sortiert(ListB, SortedB),
    vereint(SortedA, SortedB, Sorted).

geteilt(L, L1, L2) :-
    length(L, N),
    H is N-N//2,
    length(L1, H),
    append(L1, L2, L).

vereint(A, [], A).
vereint([], B, B).
vereint([H1|T1], [H2|T2], [H1|Together]) :-
    H1=<H2,
    vereint(T1, [H2|T2], Together).
vereint([H1|T1], [H2|T2], [H2|Together]) :-
    H1>H2,
    vereint([H1|T1], T2, Together).