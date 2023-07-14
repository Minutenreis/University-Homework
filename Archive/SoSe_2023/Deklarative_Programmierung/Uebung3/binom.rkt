#lang racket/base

(define (binom n k)
  (cond
    [(and (<= 1 k) (<= k n)) (+ (binom (- n 1) (- k 1)) (binom (- n 1) k))]
    [(and (= k 0) (>= n 0)) 1]
    [else 0]
    )
  )

(display (binom 4 2))
(newline)
(display (binom 4 3))

; Dies ist eine rein rekursive Funktion (sie splittet sich auf 2 Funktionen je auf, ist also nicht iterativ)