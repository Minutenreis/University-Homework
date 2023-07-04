#lang racket/base

( define ( foo x )
   ( if ( < x 0)
       `()
       ( append ( foo (- x 1) ) ( list x ) ) ) )

( define (foo2 x)
   (define (foohelp x list)
     (if (< x 0)
        list
        (foohelp (- x 1)  (cons x list))))
   (foohelp x '())
   )

( define (footest x)
   (display (foo x))
   (displayln (foo2 x))
   )

(footest 3)
(footest 5)
(footest -1)
(footest 0)

