%Var1
cs(N, V, S) :- % Stars and Bars => N+V-1 über N-1
    N>0,
    N1 is N+V-1,
    K1 is N-1,
    N_K is N1-K1,
    fak(N1, F1),
    fak(K1, F2),
    fak(N_K, F3),
    S is F1//(F2*F3).

fak(0, 1).
fak(N, S) :-
    N>0,
    N1 is N-1,
    fak(N1, S1),
    S is N*S1. 

%Var2
sols(1, V) :-
    V>=0.
sols(N, V) :-
    N>=1,
    between(0, V, X1),
    V1 is V-X1,
    N1 is N-1,
    sols(N1, V1).

cs1(N, V, S) :-
    findall(_, sols(N, V), S1),
    length(S1, S).

%Var3
sols3(N, V) :-
    length(L, N), % L = [X1, X2, ..., Xn]
    maplist(between(0, V), L), % L = [X1, X2, ..., Xn], X1 in [0, V], X2 in [0, V], ..., Xn in [0, V]
    sum_list(L, V). % L = [X1, X2, ..., Xn], X1 + X2 + ... + Xn = V
cs3(N, V, S) :-
    findall(_, sols3(N, V), S1),
    length(S1, S).