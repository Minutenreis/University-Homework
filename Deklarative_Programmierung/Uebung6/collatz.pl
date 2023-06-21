nextCollatz(N, CN) :-
    0 is N mod 2,
    CN is N/2.

nextCollatz(N, CN) :-
    1 is N mod 2,
    CN is 3*N+1.

collatz(1, [1, 4, 2]).
collatz(2, [2, 1, 4]).
collatz(4, [4, 2, 1]).

collatz(N, [N|L]) :-
    notBaseCase(N),
    nextCollatz(N, CN),
    collatz(CN, L). 

    
notBaseCase(N) :-
    dif(N, 1),
    dif(N, 2),
    dif(N, 4).