#lang racket/base

(define small-number 0.00001) ; überall außer sprt.good-enough (wie beschreibe ich verschachtelte Funktionen?)
(define pi 3.14) ; überall außer umfang
(define radius 10) ; überall außer umfang
(define umfang-static (* 2 pi radius)) ; überall
(define (umfang radius)
  (define pi 3.14159) ; nur innerhalb von umfang
  (* 2 pi radius)
  )
(define (average x y) ;überall
  (define (half-of x) (/ x 2)) ;half-of nur innerhalb von average
  (half-of (+ x y))
  )
(define square x) (* x x)) ;überall ;fehlende Klammer auf
(define (sqrt x) ;überall
  (define (good-enough? guess x); nur innerhalb von sqrt
    (define small-number 0.001); nur innerhalb von sqrt.good-enough?
    (< (abs (- (square guess) x)) small-number))
  (define (improve guess x) (average guess (/ x guess))); nur innerhalb von sqrt
  (define (sqrt-iter guess x); nur innerhalb von sqrt
    (cond ((good-enough? guess x) guess)
         (else (sqrt-iter (improve guess x) x))))
  (cond ((< x 0) "Fehler")
       ((zero? x) 0)
       (else (sqrt-iter 1 x))))