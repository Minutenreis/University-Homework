p(X, X).
p(X, Z) :- % p(X,Z) <- q(X,Y) && p(Y,Z)
    q(X, Y),
    p(Y, Z).
q(a, b).