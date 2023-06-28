mag(john, peter).
mag(peter, X) :-
    mag(X, peter).
mag(olli, peter) :-
    not(mag(peter, john)).

binaer(0, 0).
binaer(1, 1).
binaer(Dec, Bi) :-
    Dec>1,
    Rest is Dec mod 2,
    Dec1 is Dec div 2,
    binaer(Dec1, B1),
    atom_concat(B1, Rest, Bi).

my_member(X, [X|_]).
my_member(X, [_|T]) :-
    my_member(X, T).