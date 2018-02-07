(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  (map (lambda (x) (append (cons first nil) x)) rests)
  )

(define (map proc items)
  (if (null? items) nil
  (cons (proc (car items)) (map proc (cdr items)))
  )
  )

(define (zip pairs)
  (list (map car pairs) (map cadr pairs)))

;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
  (define (helper s ind total)
    (if (null? s) total
      (helper (cdr s) (+ ind 1) (append total(list (list ind (car s))))))
    )
  (helper s 0 nil)
  )


;; Problem 18
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 18
  (cond 
    ((= total 0) '(())) ;if total = 0 then ( () )
    ((or (< total 0) (null? denoms)) '()) ;if total < 0 then ()
    ((> (car denoms) total) (list-change total (cdr denoms))); if first thing in denoms is greater than total (e.g. 25 > 10) call it again on 10 (10 5 1)
    (else (append 
        (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) 
      (list-change total (cdr denoms))
      )
    )
  )
  )
  ; END PROBLEM 18

;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (cons form (cons params (let-to-lambda body)))
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (append(list(cons (quote lambda) (cons (car(zip (let-to-lambda values))) (let-to-lambda body)))) (cadr(zip (let-to-lambda values))))
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr)
         ; END PROBLEM 19
         )))
