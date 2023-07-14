zaehle_elemente(_, [], 0).
zaehle_elemente(A, [A|T], N) :-
    zaehle_elemente(A, T, N1),
    N is N1+1.
zaehle_elemente(A, [B|T], N) :-
    dif(A, B),
    zaehle_elemente(A, T, N).