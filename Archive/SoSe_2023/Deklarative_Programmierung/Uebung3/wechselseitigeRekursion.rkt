#lang racket/base

(define (gerade? n)
  (cond
    [(zero? n) #t]
    [else (ungerade? (- n 1))]
    )
  )

(define (ungerade? n)
  (cond
    [(zero? n) #f]
    [else (gerade? (- n 1))]
    )
  )

(display (gerade? 100))
(display (gerade? 101))
(newline)
(display (ungerade? 100))
(display (ungerade? 101))

;gerade funktioniert die Implementation noch nicht für negative Zahlen
;dafür müsste man anfangs checken, ob die Zahl negativ ist und dann +1
;statt -1 rechnen