% Standarddirektionalität: Ele, Liste geg, N ges.
% var(X) ... nicht instanziiertes X (X ist Variable)
% nonvar(X) ... X ist instanziiert (X bereits belegt)
zaehle_elemente(_, [], 0).
zaehle_elemente(Ele, [H|T], N) :-
    nonvar(Ele), nonvar(H), nonvar(T),
    H = Ele,
    zaehle_elemente(H, T, N1),
    N is N1+1.
zaehle_elemente(Ele, [H|T], N) :-
    nonvar(Ele), nonvar(H), nonvar(T),
    Ele \= H,
    zaehle_elemente(Ele, T, N).
zaehle_elemente(Ele, Liste, N) :-
    nonvar(Liste),
    var(Ele),
    unique_member(Liste, Liste2),
    member(Ele, Liste2),
    zaehle_elemente(Ele, Liste, N).

% delete entfernt alle Vorkommen von Ele aus einer Liste
% Ele, Liste gegeben, neue Liste gesucht
delete(_, [], []).
delete(Ele, [H|T], [H|T2]) :-
    H \= Ele,
    delete(Ele, T, T2).
delete(H, [H|T], T2) :-
    delete(H, T, T2).
    
% unique_member wandlet eine Liste in eine 
% neue Liste ohne Dopplungen um
% Liste gegeben, neue Liste gesucht
unique_member([],[]).
unique_member([H|T], [H|TU]) :-
    delete(H, T, T2),
    unique_member(T2, TU).
    
    
    
    