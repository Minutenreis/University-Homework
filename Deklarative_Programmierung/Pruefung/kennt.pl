kennt(klaus, petra).
kennt(klaus, joachim).
kennt(anna, klaus) :-
    kennt(petra, klaus).
kennt(B, A) :-
    kennt(A, B).

