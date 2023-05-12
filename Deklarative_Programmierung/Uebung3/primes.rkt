#lang racket/base

(define (prime? n)
  (cond
    [(< n 2) #f]
    [(= n 2) #t]
    [else (primeHelp n 2)]
    )
  )

(define (primeHelp n m)
  (cond
    [(= m n) #t]
    [(devides? n m) #f]
    [else (primeHelp n (+ m 1))]
    )
  )

(define (devides? n m) ; ist m Teiler von n
  (zero? (modulo n m))
  )

(define (first-primes n); tries for each prime all possible factors
  (cond
    [(= n 0) null]
    [else (first-primes-helper n 2 '())]
    )
  )

(define (first-primes-helper n m l)
  (cond
    [(= n (length l)) l]
    [(prime? m) (first-primes-helper n (+ m 1) (append l (list m)))]
    [else (first-primes-helper n (+ m 1) l)]
    ))

(define (fast-first-primes n) ;tries for each number all possible primes as factor
  (cond
    [(= n 0) null]
    [else (fast-first-primes-helper n 2 '())]
    )
  )

(define (fast-first-primes-helper n m l)
  (cond
    [(= n (length l)) l]
    [(fast-prime? m l) (fast-first-primes-helper n (+ m 1) (append l (list m)))]
    [else (fast-first-primes-helper n (+ m 1) l)]
    ))

(define (fast-prime? n l)
  (cond
    [(< n 2) #f]
    [(= n 2) #t]
    [else (fast-primeHelp n l)]
    )
  )
(define (fast-primeHelp n l)
  (andmap (lambda (x) (not (devides? n x))) l) ;returns true if n is not devided by any prime
  )


(display (prime? 2))
(newline)
(display (prime? 3))
(newline)
(display (prime? 4))
(newline)
(display (prime? 91))
(newline)
(display (prime? 97))
(newline)
(display (first-primes 30))
(newline)
(display (fast-first-primes 30))