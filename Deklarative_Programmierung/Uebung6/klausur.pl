mystpl(Lst, Res) :-
    myst_helper(Lst, Res1),
    mystpl(Res1, Res).
mystpl(Lst, Lst).
myst_helper([H1, H2|T], [H2, H1|T]) :-
    H2<H1.
myst_helper([H1, H2|T], [H1|Res]) :-
    H2>=H1,
    myst_helper([H2|T], Res).