#lang racket/base

(define (collatz n)
  (reverse (collatz-helper n '()))
  )

(define (collatz-helper n list)
  (if (member n list)
     list
     (if (even? n)
        (collatz-helper (/ n 2) (cons n list))
        (collatz-helper (+ (* 3 n) 1) (cons n list))
        )
     )
  )

(define (b_collatz n)
  (b_collatz-helper n 1 '())
  )

(define (b_collatz-helper n i longestList) ; int int list
  (if (< n i)
     longestList
     (let ((newList (collatz i)))
       (if (> (length newList) (length longestList))
          (b_collatz-helper n (+ i 1) newList)
          (b_collatz-helper n (+ i 1) longestList)
          )
       )
     )
  )

(define (b_fast_collatz n)
  (b_fast-collatz-helper n 1 '())
  )

(define (b_fast-collatz-helper n i longestList) ; int int list
  (if (< n i)
     longestList
     (let ((newList (fast-collatz i)))
       (if (> (length newList) (length longestList))
          (b_collatz-helper n (+ i 1) newList)
          (b_collatz-helper n (+ i 1) longestList)
          )
       )
     )
  )

(define (fast-collatz n)
  (reverse (fast-collatz-helper n '()))
  )

(define (fast-collatz-helper n list); remove O(n) call to member by using knowledge of collatz
  (cond
    [(<= n 4) (collatz-helper n list)]; base case for 4 2 1
    [(even? n) (fast-collatz-helper (/ n 2) (cons n list))]
    [else (fast-collatz-helper (/ (+ (* 3 n) 1) 2) (cons (+ (* 3 n) 1) (cons n list)))] ; calculates 2 steps at once
    )
  )



(displayln (collatz 8))
(displayln (fast-collatz 8))
(displayln (b_collatz 22))
(displayln (b_fast_collatz 22))

; ich glaube es gibt weitere optimierungen, wo man die längen der vorherig ausgerechneten listen in der Berechnung neuer nutzt
; doch das übersteigt mir gerade, was ich hier erreichen will; also lediglich eine schnellere Variante von Collatz

