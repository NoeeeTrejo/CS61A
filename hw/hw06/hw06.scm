;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (car (cdr s)))

(define (caddr s)
  'YOUR-CODE-HERE
  (car (cddr s)))

(define (sign x)
  'YOUR-CODE-HERE
  (cond
        ((< x 0) -1)
        ((> x 0)  1)
        (else 0)
        )
)

(define (square x) (* x x))

(define (pow b n)
    'YOUR-CODE-HERE
    ;     ; (cond
    ;     ;     ((= n 0) 1)
    ;     ;     ((= n 1) b)
    ;     ;     (else (* b (pow b (- n 1))))
    ;     ; )
    ; )

    (cond
         ((= n 0)
             1)
         ((= n 1)
            b)
         ((even? n)
                  (* (square b) (pow b (/ n 2))))
        ((odd? n)
               (pow b (- n 1))))
          )


(define (unique s)
  'YOUR-CODE-HERE
  (define lambda_expression (lambda (y) (not (eq? y (car s)))))
    (cond
      ((null? s)
        nil)
      (else
        (cons
        (car s)
          (unique (filter lambda_expression (cdr s)))))
      ))
