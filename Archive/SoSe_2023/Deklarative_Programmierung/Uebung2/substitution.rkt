#lang racket/base

(define (string-sort a b)
  (cond ((string=? a b) a)
       ((string<? a b) (string-append a ", " b))
       (else (string-append b ", " a))))
(define a "b")
(define b "a")

(display (string-sort a b))