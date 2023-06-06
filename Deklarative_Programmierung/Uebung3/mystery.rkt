#lang racket/base

(define (mystery b) ; converts an integer to binary (but switched directions)
  (if (= b 0)
     '()
     (if (= (remainder b 2) 0)
        (cons 0 (mystery (/ b 2)))
        (cons 1 (mystery (floor (/ b 2)))))))
; Erklärung: man guckt sich immer an, ob das hinterste bit 1 oder 0 ist und teilt dann durch 2
; => Leftshift: man betrachtet jetzt also die stelle eins nach links


(define (mystery2 a b) ; multiplies float or int a with int b
  (if (= b 0)
     0
     (if (= (remainder b 2) 0) ; if b is even
        (mystery2 (+ a a) (/ b 2)) ; halbiere b, verdopple a
        (+ a (mystery2 (+ a a) (floor (/ b 2))))))) ; b = 2n+1 => n = floor(b/2) => a * b = a * (2n+1) = a * 2n + a = 2a * n + a

(define (mystery3 a b); gibt liste aus mit a*2^i für i = 0,1, dabei sind die ungeraden b's rechts, die geraden links
  (if (= b 0)
     '()
     (if (= (remainder b 2) 0) ; if b is even
        (cons a (mystery3 (+ a a) (/ b 2))) ; (a, mystery3(2a, b/2))
        (append (mystery3 (+ a a) (floor (/ b 2))) (list a))))) ; (mystery3 (2a, floor(b/2)), a)

(define (test) 13)

(displayln (mystery (test)))
(displayln (mystery2 0.5 (test)))
(displayln (mystery3 1 (test)))

;Kombination irritiert mich gerade noch, wofür braucht man die multiplikation aus mystery2?s

