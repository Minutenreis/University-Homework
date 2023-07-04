#lang racket

; (define (scale lst s)
;   (map (lambda (x) (* x s)) lst))

(define (scale lst s)
  (if (empty? lst)
     '()
     (cons (* (car lst) s) (scale (cdr lst) s))
     ))

(define (lstadd lst1 lst2)
  (cond
    [(and (null? lst1) (null? lst2)) '()]
    [(null? lst1) lst2]
    [(null? lst2) lst1]
    [else (cons (+ (car lst1) (car lst2)) (lstadd (cdr lst1) (cdr lst2)))]
    ))

(define (polymulti pol1 pol2)
  (define (polymulti-helper pol1 pol2)
    (if (empty? pol1)
       '()
       (lstadd (scale pol2 (car pol1))
              (cons 0 (polymulti-helper (cdr pol1) pol2)))))
  (polymulti-helper pol1 pol2))


(scale '(1 2 3) 2)
(lstadd '(1 2 3) '(4 5 6 7))
(polymulti '(1 1 2) '(2 0 0 1))