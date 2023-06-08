% Restrekursiv
getZerosTail(List, X) :-
    getZerosTail(List, X, 0).

getZerosTail([], X, X).
getZerosTail([H|T], X, Acc) :-
    H=0,
    Acc1 is Acc+1,
    getZerosTail(T, X, Acc1).
getZerosTail([H|T], X, Acc) :-
    H\=0,
    getZerosTail(T, X, Acc).

% Rekursion vor Akkumulator
getZerosSlow([], X) :-
    X=0.
getZerosSlow([H|T], X) :-
    H=0,
    getZerosSlow(T, X1),
    X is X1+1.
getZerosSlow([H|T], X) :-
    H\=0,
    getZerosSlow(T, X).


% Skalarprodukt
dotProduct([], [], 0).

dotProduct([H1|T1], [H2|T2], N) :-
    Temp is H1*H2,
    dotProduct(T1, T2, Remaining),
    N is Temp+Remaining.

dotTail(List1, List2, N) :-
    dotTail(List1, List2, N, 0).

dotTail([], [], N, N).

dotTail([H1|T1], [H2|T2], N, Acc) :-
    Temp is Acc+H1*H2,
    dotTail(T1, T2, N, Temp).

% Dotproduct Term => is durch = ersetzen
dotTerm(List1, List2, N) :-
    dotTerm(List1, List2, N, 0).

dotTerm([], [], N, N).

dotTerm([H1|T1], [H2|T2], N, Acc) :-
    Temp=Acc+H1*H2,
    dotTerm(T1, T2, N, Temp).

dotTermCheck(List1, List2, Res) :-
    dotTerm(List1, List2, N),
    Res is N.

% Primchecker
isPrime(1).
isPrime(N) :-
    N>1,
    isPrime(N, 2).

isPrime(N, N).
isPrime(N, X) :-
    N>X,
    N rem X=\=0,
    X1 is X+1,
    isPrime(N, X1).

% sortieren (Insertionsort von rechts)
sortList([], []).
sortList([H|T], Sorted) :-
    sortList(T, SortedTail),
    insertSorted(H, SortedTail, Sorted).

insertSorted(X, [], [X]).
insertSorted(X, [H|T], [X, H|T]) :-
    X=<H.
insertSorted(X, [H|T], [H|T2]) :-
    X>H,
    insertSorted(X, T, T2).

%TODO: Bogosort