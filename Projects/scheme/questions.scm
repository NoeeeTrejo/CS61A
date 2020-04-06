(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  (map (lambda (lst) (append (list first) lst)) rests)
  )

(define (zip pairs)
(list (map car pairs) (map (lambda (lst) (car (cdr lst))) pairs))
)

;; Problem 16
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 16
  (define (helper_func n s)
  (cond
    ((null? s) nil)
    (else
      (cons (list n (car s)) (helper_func (+ n 1) (cdr s))))
  ))
  (helper_func 0 s)
  )
  ; END PROBLEM 16

;; Problem 17
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 17
  (cond
    ((= total 0) (list nil))
    ((null? denoms) nil)
    ((> (car denoms) total) (list-change total (cdr denoms)))
    (else
      (define with_first (list-change (- total (car denoms)) denoms))
      (define without_first (list-change total (cdr denoms)))
      (append (cons-all (car denoms) with_first) without_first)
    )))
  ; END PROBLEM 17

;; Problem 18
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 18
         'replace-this-line
         expr
         ; END PROBLEM 18
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 18
         'replace-this-line
         expr
         ; END PROBLEM 18
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           'replace-this-line
           (cons form (cons params (map let-to-lambda body)))
           ; END PROBLEM 18
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           'replace-this-line
            (cons (cons 'lambda (cons (car (zip values)) (map let-to-lambda body)))
            (map let-to-lambda (cadr (zip values))))
            ; END PROBLEM 18
           ))
        (else
         ; BEGIN PROBLEM 18
         'replace-this-line
         (cons (car expr) (map let-to-lambda (cdr expr)))
         ; END PROBLEM 18
         )))
