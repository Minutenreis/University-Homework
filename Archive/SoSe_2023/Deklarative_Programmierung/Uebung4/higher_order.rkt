#lang racket/base
; Verzeihen sie mir, aber ich mache mal vorerst nur die Operationen auf je eine Liste

(define (my-map proc lst )  ;lambda (x) => any, list
  (if (null? lst) '() ;last element reached
     (cons (proc (car lst)) ;apply function to first element
          (my-map proc (cdr lst)))) ; repeat for all other elements
  )
(define (my-filter proc lst)  ;lambda (x) => bool, list
  (if (null? lst) '() ;last element reached
     (if (proc (car lst)) ;if function returns true
        (cons (car lst) ;add element to list
             (my-filter proc (cdr lst))) ;repeat for all other elements
        (my-filter proc (cdr lst)))) ;repeat for all other elements
  )
(define (my-foldl proc init lst)  ;lambda (x, init) => any, list
  (if (null? lst) init ;last element reached
     (my-foldl proc (proc (car lst) init) (cdr lst))) ;add current element to init and repeat for all other elements
  )
(define (my-foldr proc init lst)
  (if (null? lst) init ;last element reached
     (proc (car lst) (my-foldr proc init (cdr lst)))) ;call later functioncalls first recursively
  )
(define (my-apply proc lst . v) ; how to use (func proc v ... lst) syntax?
  (eval (cons proc (append v lst)) (make-base-namespace))
  )
(define (my-member elem lst)
  (if (null? lst) #f ;last element reached
     (if (equal? elem (car lst)) lst ;if element is equal to current element
        (my-member elem (cdr lst)))) ;repeat for all other elements
  )

; Test cases for 1
; (displayln (my-map (lambda (x) (+ x 1)) '(1 2 3 4)))
; (displayln (map (lambda (x) (+ x 1)) '(1 2 3 4)))
; (displayln (my-filter (lambda (x) (equal? x 1)) '(1 2 3 4)))
; (displayln (filter (lambda (x) (equal? x 1)) '(1 2 3 4)))
; (displayln (my-foldl (lambda (x y) (- x y)) 0 '(1 2 3 4)))
; (displayln (foldl (lambda (x y) (- x y)) 0 '(1 2 3 4)))
; (displayln (my-foldr (lambda (x y) (- x y)) 0 '(1 2 3 4)))
; (displayln (foldr (lambda (x y) (- x y)) 0 '(1 2 3 4)))
; (displayln (my-apply + '(1 2 3 4) 1 2 3))
; (displayln (apply + 1 2 3 '(1 2 3 4)))
; (displayln (my-member 3 '(1 2 3 4 5)))
; (displayln (member 3 '(1 2 3 4 5)))

(define (get-odd lst)
  (my-filter (lambda (x) (equal? (modulo x 2) 1)) lst))
(define (4-quad lst)
  (if (my-member 4 lst)
     (my-map (lambda (x) (* x x)) lst)
     lst
     )
  )
(define (cross-sum-mod-5-reverse lst)
  (if (= (modulo (sum-of-cross-sums (4-quad lst)) 5) 0)
     (my-foldl cons '() lst)
     lst)
  )
(define (sum-of-cross-sums lst)
  (my-foldl + 0 (my-map cross-sum lst))
  )

;https://stackoverflow.com/a/6360768
(define (cross-sum x)
  (if (= x 0) 0
     (+ (modulo x 10)
       (cross-sum (/ (- x (modulo x 10)) 10)))))

(define (difference lst)
  (my-foldl (lambda (x y) (- x y)) 0 (4-quad lst))
  )

; Test cases for 2

(define (given-list) '(1 2 3 4))
(displayln (get-odd (given-list)))
(displayln (4-quad (given-list)))
(displayln (cross-sum-mod-5-reverse (given-list)))
(displayln (difference (given-list))) ; was genau ist hier gefragt?
;was soll die Differenzen von (1 2 3 4) sein
; 1 - 2 - 3 - 4 = -8? (2-1),(3-2),(4-3) = (1 1 1)? (2-1) + (3-2) + (4-3) = 3 = (4-1)?

;wie macht man die 2.3 bitte3 effizient und elegant? die Bedingung ist "Summer_der_Quersummen(maybeQuadra(lst)) mod 5 = 0"

;nein meine eigenen Funktionen haben die Aufgabe verständlicherweise nicht vereinfacht, sind ja in allen Fällen maximal genau so gut wie nativ Funktionen

