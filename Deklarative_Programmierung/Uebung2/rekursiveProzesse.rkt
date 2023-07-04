#lang racket/base

(define (a-plus x y)
  (if (zero? x)
     y
     (1+ (a-plus (1- x) y))))

(define (b-plus x y)
  (if (zero? x)
     y
     (b-plus (1- x) (1+ y))))

(define (1+ x)
  (+ x 1))

(define (1- x)
  (- x 1))

(a-plus 4 5)
(b-plus 4 5)