#lang racket
; binäre Bäume
(define the-empty-tree '())
(define (empty-tree? tree) (eq? tree the-empty-tree))
(define (entry tree) (car tree))
(define (left-branch tree) (cadr tree))
(define (right-branch tree) (caddr tree))
(define (make-tree entry left right) (list entry left right))

; Mengenkonstruktor und leere Menge
(define (make-set liste) (liste->baum liste)) ;direkt liste->baum genutzt; nur korrekt wenn Liste keine Dopplungen enthält
(define the-empty-set the-empty-tree) ; redundant
(define (empty-set? set) (empty-tree? set)) ; redundant

; Prüfung auf Enthaltensein von Elementen und Anfügen von Elementen
(define (element-of-set? x set)
  (cond ((null? set) #f)
       ((= x (entry set)) #t)
       ((< x (entry set))
        (element-of-set? x (left-branch set)))
       ((> x (entry set))
        (element-of-set? x (right-branch set)))))

(define (adjoin-set x set); nicht genutzt, weil ein Großteil sich um Bäume im Allgemeinen und nicht Mengen im speziellen bezieht
  (cond ((null? set) (make-tree x '() '()))
       ((= x (entry set)) set)
       ((< x (entry set))
        (make-tree (entry set)
                  (adjoin-set x (left-branch set))
                  (right-branch set)))
       ((> x (entry set))
        (make-tree (entry set)
                  (left-branch set)
                  (adjoin-set x (right-branch set))))))

(define (liste->baum liste) ; TODO: implement
  (liste->baum-helper liste the-empty-tree)
  )

(define (liste->baum-helper liste baum)
  (if (null? liste) baum
     (liste->baum-helper (cdr liste) (baum-einfuegen  baum (car liste))))
  )

(define (baum-einfuegen baum element)
  (if (empty-tree? baum) (make-tree element '() '())
     (if (< element (entry baum))
        (make-tree (entry baum) (baum-einfuegen (left-branch baum) element) (right-branch baum))
        (make-tree (entry baum) (left-branch baum) (baum-einfuegen (right-branch baum) element))
        )
     )
  )

(define (baum->liste-infix baum) ;inorder treewalk
  (if (empty-tree? baum) '()
     (append (baum->liste-infix (left-branch baum)) (list (entry baum)) (baum->liste-infix (right-branch baum)))
     )
  )

(define (baum->liste-praefix baum) ;inorder treewalk
  (if (empty-tree? baum) '()
     (append (list (entry baum)) (baum->liste-praefix (left-branch baum))  (baum->liste-praefix (right-branch baum)))
     )
  )

(define (schnitt baum1 baum2); baum1 n baum2
  (liste->baum (filter (lambda (x) (element-of-set? x baum2)) (baum->liste-praefix baum1)))
  )

(define (vereinigung baum1 baum2); baum1 U baum2
  (liste->baum (append (baum->liste-praefix baum2) (filter (lambda (x) (not (element-of-set? x baum2))) (baum->liste-praefix baum1))))
  ); filter damit elemente nicht doppelt vorkommen

(define (differenz baum1 baum2); baum1 \ baum2
  (liste->baum (filter (lambda (x) (not (element-of-set? x baum2))) (baum->liste-praefix baum1))))

(define (set-eq? baum1 baum2)
  (and (empty-tree? (differenz baum1 baum2)) (empty-tree? (differenz baum2 baum1)))
  )

(define (flatten lst)
  (if (null? lst) '() ; end of list
     (if (list? (car lst)) (append (flatten (car lst)) (flatten (cdr lst))); if first is list => flatten
        (cons (car lst) (flatten (cdr lst))); else just append first element, recursion on rest
        )
     )
  )

;http://codeimmersion.i3ci.hampshire.edu/2009/09/20/a-simple-scheme-shuffle/
(define (permutate lst)
  (if (< (length lst) 2) lst
     (let ((item (list-ref lst (random (length lst))))) ;get item from random position
       (cons item (permutate (remove item lst))); append item and remove it from list
       )
     )
  )

; Tests with * mean that permutate would have made the results unreliable (unknown inputorder => unknown output)
(displayln (liste->baum '(4 2 1 3 7 6 8))) ; should be (4 (2 (1 () ()) (3 () ())) (7 (6 () ()) (8 () ())))*
(displayln (baum->liste-infix (liste->baum (permutate '(1 2 3 3 5 6 7))))) ; should be (1 2 3 4 5 6 7)
(displayln (baum->liste-praefix (liste->baum '(4 2 1 3 7 6 8)))) ; should be (4 2 1 3 7 6 8)*
(displayln (baum->liste-infix (schnitt (liste->baum (permutate '(1 2 3 4 5 6 7))) (liste->baum (permutate '(1 2 3 4 5 6 7)))))) ; should be (1 2 3 4 5 6 7)
(displayln (baum->liste-infix (vereinigung (liste->baum (permutate '(1 2 3 4 5 6 7))) (liste->baum (permutate '(1 2 3 4 5 6 7)))))) ; should be (1 2 3 4 5 6 7)
(displayln (baum->liste-infix (differenz (liste->baum (permutate '(1 2 3 4 5 6 7))) (liste->baum (permutate '(1 2 3 4 5 6 7)))))) ; should be ()

(displayln (baum->liste-infix (schnitt (liste->baum (permutate '(1 2 4 0 3))) (liste->baum (permutate '(4 5 -3)))))) ; should be (4)
(displayln (baum->liste-infix (vereinigung (liste->baum (permutate '(1 2 4 0 3))) (liste->baum (permutate '(4 5 -3)))))) ; should be (-3 0 1 2 3 4 5)
(displayln (baum->liste-infix (differenz (liste->baum (permutate '(1 2 4 0 3))) (liste->baum (permutate '(4 5 -3)))))) ; should be (0 1 2 3)

(displayln (set-eq? (liste->baum (permutate '(1 2 4 0 3))) (liste->baum (permutate '(4 5 -3))))) ; should be #f
(displayln (set-eq? (liste->baum (permutate '(1 2 4 0 3))) (liste->baum (permutate '(4 2 1 3 0))))) ; should be #t

(displayln (flatten '((1 2 3) (4 (5 6)) (7 8 9)))); should be (1 2 3 4 5 6 7 8 9)*


; sollte man alle Bäume als Menge annehmen? denn in der Aufgabe war im Großteil nur von Bäumen im Allgemeinen die Rede
; und nicht von Mengen => Funktionen für Bäume statt Mengen definiert; sonst Baum-einfuegen durch adjoin-set ersetzen