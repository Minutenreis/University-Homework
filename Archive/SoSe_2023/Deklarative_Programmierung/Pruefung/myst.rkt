#lang racket

(define (mystery a b)
  (cond
    [(> b 0) (+ (mystery a (- b 1)) a)]
    [(< b 0) (- (mystery a (+ b 1)) a)]
    [else 0]
    )
  )

(mystery 3 4)
(mystery 3 -4)
(mystery -3 4)
(mystery -3 -4)
(mystery 3.04 4)
(mystery 3.04 -4)
; (mystery 1 -0.31)