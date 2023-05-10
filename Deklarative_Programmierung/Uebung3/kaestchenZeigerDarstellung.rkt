#lang racket/base

(1 (2 3) 4)

(define (abs x) (cond ((>= x 0) x) (else (- x))))