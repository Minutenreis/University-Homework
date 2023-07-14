#lang racket

(+ (* 1 (- 2 3) 4) 5)
(define y 3)
((lambda (x) (- x y)) 5)
(list? (cons y 8))
(append '(1 2) (list y))
(member 5 '(1 3 5 3 5))
(/ 7 2)