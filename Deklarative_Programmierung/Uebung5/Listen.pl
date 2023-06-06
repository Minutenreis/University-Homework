id(X, X).% [1,[2,3]|[4,5],6]
% Nein, es handelt sich um keine Liste, da [2,3]|[4,5] kein valider Ausdruck ist.
% es darf keine Listenschreibweise auf ein Paar folgen [[2,3]|[4,5],6] ist also illegal
id(X, X).

% [[1,2|[3]]|[4,5]]
% = [[1,2,3],4,5]

% SWIPL Prolog erlaubt kein .(X,Y) und '[|]'(X,Y) wird von meinem Formatter automatisch zu [X|Y] umgewandelt
createList(X) :-
    N1=[3],
    N2=[2|N1],
    N3=[1|N2],
    N4=[5],
    N5=[4|N4],
    X=[N3|N5].