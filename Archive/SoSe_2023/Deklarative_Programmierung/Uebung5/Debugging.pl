%ich bin mir nicht hundertprozent sicher, warum es funktioniert, aber es funktioniert
perm(Liste, [ErstesElement|Rest]) :-
    append(Liste1, Liste2, Liste3),
    append(Liste1, [ErstesElement|Liste2], Liste),
    perm(Liste3, Rest).

perm([], []). /* Abbruchbedingung */
append([], Liste, Liste).

append([ErstesElement|Rest], Liste, [ErstesElement|Liste1]) :-
    append(Rest, Liste, Liste1).