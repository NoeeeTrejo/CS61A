(define (partial-sums stream)
  'YOUR-CODE-HERE

  (define (helper num lst)
  (cond
  ((null? lst) nil)
  ((= num 0) (cons-stream (car lst) (helper (car lst) (cdr-stream lst))))
  (else (cons-stream (+ (car lst) num)  (helper (+ num (car lst)) (cdr-stream lst)))
  ))
  )
  (helper 0 stream)
)
