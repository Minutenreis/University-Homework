zaehle_elemente(_, [], 0).
zaehle_elemente(H, [H|T], N) :-
    zaehle_elemente(H, T, N1),
    N is N1+1.
zaehle_elemente(Ele, [H|T], N) :-
    dif(Ele, H),
    zaehle_elemente(Ele, T, N).