delete_all(_, [], []).
delete_all(X, [X|T], L) :-
    delete_all(X, T, L).
delete_all(X, [H|T], L) :-
    dif(X, H),
    delete_all(X, T, L1),
    L=[H|L1].

list2set([], []).
list2set([H|T], [H|L]) :-
    delete_all(H, T, L1),
    list2set(L1, L).

set_diff(Lst1, Lst2, Res) :-
    diff_help(Lst1, Lst2, Res1),
    list2set(Res1, Res).

diff_help(L, [], L).
diff_help(L, [H|T], R) :-
    delete_all(H, L, L1),
    diff_help(L1, T, R).