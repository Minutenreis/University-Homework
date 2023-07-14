#lang racket/base

(define (fib n); Baumartige Rekursion
  (
   if (< n 2)
     n
     (+ (fib (- n 1)) (fib (- n 2)))
     )
  )

(define (fibIt n)
  (
   if (< n 2)
     n
     (fibItHelper n 0 1)
     )
  )

(define (fibItHelper n fn fn+1); mindestens 3 parameter: gesuchter Wert, f(n-1), f(n-2)
  (
   if (= n 0)
     fn+1
     (fibItHelper (- n 1) fn+1 (+ fn fn+1))
     )
  )

(define (phi precision) ; maxError = 10^(-precision) => precision = decimal places matched
  (phi-helper (expt 10 (- precision)) 2 1 1)
  )

(define (phi-helper maxError Fn Fn-1 lastResult) ; calculate until subsequent results are smaller than maxError
  (
   if (< (abs (- (/ Fn Fn-1) lastResult)) maxError)
     (/ Fn Fn-1)
     (phi-helper maxError (+ Fn Fn-1) Fn (/ Fn Fn-1))
     )
  )

(require srfi/48)
(require racket/format)
(define (display-phi precision) ;sadly approximation in last decimal place
  (display (format (string-append "~0," (~v precision) "F") (phi precision)))
  (newline)
  )

(displayln (fib 10))
(displayln (fibIt 10))
(display-phi 11)
