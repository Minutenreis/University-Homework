#lang racket/base

(define (primfak n)
  (reverse (primfak-helper n 2 '())))

(define (primfak-helper n i lst)
  (if (= n 1) lst
     (if (devides? n i)
        (primfak-helper (/ n i) i (cons i lst))
        (primfak-helper n (+ i 1) lst)); its faster to check for all i instead of first calculating primes
     )
  )

(define (devides? n m) ; ist m Teiler von n
  (zero? (modulo n m))
  )

(define (test-primfak n)
  (= (apply * (primfak n)) n)
  )

(displayln (test-primfak 12))
(displayln (test-primfak 15))
(displayln (test-primfak 23))
(displayln (test-primfak 2318892))
(displayln (test-primfak 221))
