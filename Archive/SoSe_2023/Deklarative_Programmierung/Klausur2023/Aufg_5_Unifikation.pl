efface(X, [X|T], T).
efface(X, [H|T], [H|T1]) :-
    efface(X, T, T1).