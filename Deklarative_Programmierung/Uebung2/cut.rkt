#lang typed/racket

(: cut (-> String Integer Integer String))
(define (cut str x y)
  (if (or (< x 0) (> y (string-length str)) (> x y))
     (error 'cut "Invalid index")
     (string-append
      (substring str 0 x)
      (substring str y (string-length str))
      )
     )
  )

(display (cut "Hello World" 0 10))