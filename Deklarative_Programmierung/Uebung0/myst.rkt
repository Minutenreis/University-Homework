#lang racket/base
; if a < b: return 2 a + 1
; if a > b: return 2 b
(define (myst a b)
  (if (zero? b)
      0
      (+ 1 (myst (- b 1) a))))

(display (myst 4 5))
(display "\n")