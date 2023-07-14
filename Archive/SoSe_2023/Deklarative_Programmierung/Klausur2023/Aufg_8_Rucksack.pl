gen_cap(MaxCap, MaxCap).
gen_cap(MaxCap, Cap) :-
    MaxCap>0,
    MaxCap1 is MaxCap-1,
    gen_cap(MaxCap1, Cap).

vollgepackt(0, _, []).
vollgepackt(N, [H|T], [H|Caps]) :-
    N>0,
    N1 is N-H,
    vollgepackt(N1, T, Caps).
vollgepackt(N, [_|T], Caps) :-
    N>0,
    vollgepackt(N, T, Caps).

rucksack(MaxCap, Items, Bag) :-
    gen_cap(MaxCap, Cap),
    vollgepackt(Cap, Items, Bag).

rucksack_alt(MaxCap, Items, Bag) :-
    vollgepackt(MaxCap, Items, Bag).

rucksack_alt(MaxCap, Items, Bag) :-
    MaxCap>0,
    Cap is MaxCap-1,
    rucksack_alt(Cap, Items, Bag).