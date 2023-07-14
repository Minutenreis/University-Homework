#lang racket

(define (myst x)
  (if (< x 3)
     (+ 1 (* x x))
     (myst (myst (modulo x 3)))))

(define (myst-direct x)
  (cond
    [(< x 3) (+ 1 (* x x))]
    [(= (modulo x 3) 0) 2]
    [(= (modulo x 3) 1) 5]
    [else (myst-direct x)]
    ))

(myst 0)
(myst 1)
(myst 2)
(myst 3)
(myst 4)
; (myst 5)

(myst-direct 0)
(myst-direct 1)
(myst-direct 2)
(myst-direct 3)
(myst-direct 4)
(myst-direct 5)