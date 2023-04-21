#lang racket/base
(define (fac n)
  (if (= n 0)
      1
      (* n (fac (- n 1)))))

(display (fac 100))
(display "\n")