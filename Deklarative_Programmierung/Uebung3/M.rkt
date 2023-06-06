#lang racket/base
;McCarthy 91 Function
;M(n) = { n - 10 if n > 100; 91 if n <= 100 }
; wenn n <= 100, dann ist 91 die Lösung wegen unterer Rekursion
; n < 90: m(n)= m(m(n+11)) = m(n+22)
; 90 <= n < 100: m(n) = m(n+11) = m(n+11-10) = m(n+1)
; m(100) = m(m(111)) = m(101) = 91
; und n > 100 ist einfach nur einfache Anwendung des Rekursionsschema
; Terminierung oben beschrieben => steigt bis 100 und dann terminiert auf 91 oder terminiert nach erstem Schritt fall n > 100
(define (m n)
  (cond
    [(> n 100) (- n 10)]
    [else (m (m (+ n 11)))]
    )
  )

(define (mItStart n)
  (mIt n 1))

(define (mIt n c) ; c zählt anzahl an m() aufrufen
  (cond
    [(zero? c) n]
    [(> n 100) (mIt (- n 10) (- c 1))] ; n > 100
    [else (mIt (+ n 11) (+ c 1))]; n < 100
    )
  )

(displayln (mItStart 87))
(displayln (mItStart 32))
(displayln (mItStart 104))
(displayln (m 100))
(displayln (m 32))