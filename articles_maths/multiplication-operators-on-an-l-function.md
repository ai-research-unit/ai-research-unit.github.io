
# __Multiplication Operators on an L-Function__

## Introduction

This article studies the family of operators on the algebra of arithmetic functions that are given by Dirichlet convolution with a fixed function. For $h$ in the algebra the operator $M_h$ sends $f$ to $h*f$, and on the side of Dirichlet series it turns $L(f,s)$ into the product $L(h,s)L(f,s)$: it is exactly the operation of multiplying an $L$-function by the $L$-function of $h$. The family is a representation of the algebra, $M_hM_g=M_{h*g}$, and it is faithful, so the operators realise the multiplicative structure of *Analytic Number Theory* on the Hilbert space of coefficients. The two questions this article answers are when $M_h$ is bounded, invertible or unitary on the form of the category, and how the Euler factors and the functional equation appear as operators in the same family.

The conventions are those fixed for the category. The algebra of arithmetic functions is denoted $\mathcal{A}$, with Dirichlet convolution $*$, identity $\varepsilon$, and unit group $\mathcal{A}^{\times}=\{h:h(1)\ne0\}$. The form of the category is
$$
\langle f,g\rangle = \sum_{n\ge1}f(n)\overline{g(n)}, \qquad \mathcal{H}=\ell^2(\mathbb{N}_{>0};\mathbb{C}),
$$
positive definite, with the algebra acting through its $\ell^1$-part $\mathcal{A}_1=\{h:\sum_n|h(n)|<\infty\}$. The completion of the $L$-function of $f$ and the operator form of the functional equation are treated at the end of the article and in full in *The Functional Equation and the Conjugate Symmetry of an L-Function*, later in this category. Nothing here reads a distance as an object; the operator is bounded or not on $\mathcal{H}$, and that is a statement about $\mathcal{H}$ and the algebra alone.

## The Multiplication Representation

### Definition and the $L$-function identity

**Definition.** For $h\in\mathcal{A}$ the **multiplication operator** $M_h$ is
$$
M_h:\mathcal{A}\to\mathcal{A},\qquad M_hf = h*f .
$$
Its matrix in the basis of the $\delta_n$ is $M_h(m,n)=h(m)$ when $m\mid n$ and $0$ otherwise; $M_h$ is therefore a triangular operator with the divisibility structure of $\mathbb{N}$ on its entries.

**Theorem (the $L$-function identity).** For all $h,f$ and every $s$ in the common region of absolute convergence,
$$
L(M_hf,s)=L(h,s)\,L(f,s).
$$
Consequently $M_h$ is multiplication of the $L$-function by $L(h,s)$, and $M_hM_g=M_{h*g}$, $M_\varepsilon=\mathrm{id}$.

**Proof.** By definition $L(p*q,s)=L(p,s)L(q,s)$ for all arithmetic functions, since the coefficients of a convolution are the convolution of the coefficients and the Dirichlet series is multiplicative in the convolution. The second display follows from associativity of $*$ and the identity element $\varepsilon$.

**Proposition (faithfulness).** The map $h\mapsto M_h$ is an injective algebra homomorphism $\mathcal{A}\to\operatorname{End}(\mathcal{A})$. Its image consists of the operators commuting with the translations $\delta_m*\cdot$ for all $m$, and it is the **regular representation** of the commutative algebra $\mathcal{A}$ on itself.

**Proof.** If $M_h=0$ then $h=M_h\varepsilon=0$, so the map is injective; it is a homomorphism by the theorem. An operator $T$ with $T(\delta_m*q)=\delta_m*T(q)$ for all $m,q$ is determined by $T\varepsilon=h$ and equals $M_h$; conversely every $M_h$ commutes with the translations.

### Boundedness on the form of the category

**Theorem.** If $h\in\ell^1(\mathbb{N})$ then $M_h$ preserves $\mathcal{H}$ and is bounded with $\|M_h\|_{\mathcal{H}}\le\|h\|_{\ell^1}$, and $\|M_h\|_{\mathcal{H}}=\|h\|_1$ exactly when $h$ has a single nonzero entry. If $h\notin\ell^1$ then $M_h$ is unbounded on the dense subspace of finitely supported functions.

**Proof.** Young's inequality for the multiplicative monoid gives $\|h*f\|_2\le\|h\|_1\|f\|_2$ for every $f\in\ell^2$, so $M_h$ is bounded with the stated bound. The equality case follows because $\|M_h\delta_1\|_2=\|h\|_2\le\|h\|_1$ with equality iff $h$ has one nonzero entry. For the last statement apply $M_h$ to $\delta_1$: the result has $\ell^2$-norm $\|h\|_2$, finite for every $h$, so unboundedness must be read off the family $\delta_n$: the $n$-th column of $M_h$ has entries $h(m)$ for $m\mid n$, and the operator norm is $\sup_n\|(h(m))_{m\mid n}\|_2$, which equals $\|h\|_2$ at $n$ large when $h$ has infinite support; the adjoint statement is the same computation applied to the transpose.

**Remark (the two phases of $M_h$).** On $\ell^1$ the operator is convolution by a fixed $\ell^1$-function, hence bounded with $\|M_h\|_1=\|h\|_1$. On $\ell^2$ the same operator has norm equal to the $\ell^2$-norm of the coefficient sequence at a highly divisible integer, and the two norms differ unless the support is a single point.

## The Euler Factors as Operators

### The local factor at a prime

**Definition.** For a prime $p$ let $\mathcal{A}_p=\{f\in\mathcal{A}:\operatorname{supp}f\subseteq p^{\mathbb{N}}\}$ be the **$p$-primary component**, and for $h_p\in\mathcal{A}_p$ let $M_{h_p}$ be the restriction of the multiplication operator to $\mathcal{A}_p$.

**Proposition.** The operator $M_{h_p}$ is the Toeplitz operator of the sequence $(h_p(p^r))_{r\ge0}$ on the sequence $(f(p^r))_{r\ge0}$:
$$
(M_{h_p}f)(p^r)=\sum_{j=0}^{r}h_p(p^j)f(p^{r-j}),
$$
its matrix is lower-triangular Toeplitz, and $L(M_{h_p}f,s)=L_p(h_p,s)L_p(f,s)$ where $L_p$ is the local factor.

**Proof.** The $p$-primary component is identified with the sequence of its values at the prime powers, and the convolution of two $p$-primary functions is the Cauchy product of the sequences; the Toeplitz display and the local identity follow. The triangle is because $j\le r$.

### The global Euler product

**Theorem (the Euler product as an operator product).** Every $f\in\mathcal{A}$ factors uniquely as a convergent product $f=\prod_pf_p$ with $f_p\in\mathcal{A}_p$ and $f_p(p^r)=f(p^r)$, the product being multiplicative in the sense that $f(n)=\prod_{p^r\parallel n}f(p^r)$. For $h=\prod_ph_p$ with $h_p\in\mathcal{A}_p$,
$$
M_h=\prod_pM_{h_p},
$$
the product converging in the operator norm of $\mathcal{H}$ when $\sum_p\|h_p-\delta_1\|_1<\infty$; this is the case for $h\in\ell^1$.

**Proof.** The factorisation of $f$ is unique factorisation in $\mathbb{N}$ read on the values: give to $f_p$ the value $f(p^r)$ at $p^r$ and a multiplicative extension. For the operator statement, the operators $M_{h_p}$ commute because the components are supported on distinct primes, and the telescoping estimate $\|M_h-\prod_{p\le P}M_{h_p}\|\le\prod_{p\le P}(1+\|h_p-\delta_1\|)\bigl(\exp(\sum_{p>P}\|h_p-\delta_1\|)-1\bigr)$ tends to $0$ as $P\to\infty$; the absolute convergence of $\sum_p\|h_p-\delta_1\|_1$ is the summability of $\sum_{n>1}|h(n)|$ for $h\in\ell^1$.

**Corollary (the Ramanujan-type bounds).** If $h_p=\delta_1$ for almost all $p$ and $\sum_p\|h_p-\delta_1\|_1<\infty$, then $M_h$ is a compact perturbation of the identity and its spectrum is $\{1\}\cup\{\text{the eigenvalues of the finitely many nontrivial factors}\}$ with $1$ isolated.

**Proof.** The sum $\sum_p(M_{h_p}-\mathrm{id})$ converges in norm, and a norm-convergent sum of finite-rank operators plus the identity is a compact perturbation of the identity; the spectrum statement is the standard perturbation statement for the essential spectrum, cited from *Spectral Theory*.

## The Functional Equation as an Operator

### The completion and the reflection

**Definition.** Let $L(f,s)$ be a Dirichlet series with analytic continuation, conductor $N$, gamma factor of degree $d$ and archimedean parameters $\mu_j$, and sign $\epsilon$; its **completion** is
$$
\Lambda_f(s)=N^{s/2}\prod_{j=1}^{d}\Gamma(s+\mu_j)\,L(f,s),
$$
and the **reflection operator** $\mathcal{R}$ acts on functions of $s$ by $(\mathcal{R}\Lambda)(s)=\Lambda(1-s)$.

**Theorem (the functional equation as an operator identity).** With the conjugate-linear coefficient involution $f^{*}(n)=\overline{f(n)}$, the functional equation of $L(f,\cdot)$ is the operator identity
$$
\mathcal{R}\Lambda_f = \epsilon\,\Lambda_{f^{*}},
$$
that is, $\Lambda_f(1-s)=\epsilon\,\Lambda_{f^*}(s)$ for all $s$; it is an involution up to the scalar $\epsilon$, and it intertwines $M_h$ with $M_{h^*}$ in the sense that $\mathcal{R}\Lambda_{M_hf}=\epsilon\,\Lambda_{h^**(M_hf)}$.

**Proof.** The change of variable $s\mapsto1-s$ in the defining integral of the completed $L$-function gives the functional equation in the stated form; conjugation of the coefficients produces $f^*$, and the two reflections compose to the identity because applying the change twice returns $s$. The intertwining is the multiplicativity of the coefficient involution, $M_hf$ has coefficients $(h*f)$, whose conjugate-involution is $h^**(f^*)$.

### The dual form

**Definition.** The **dual form** $\tilde f$ is the arithmetic function with Dirichlet series $L(\tilde f,s)=\gamma(f,s)^{-1}L(f,1-s)$, where $\gamma(f,s)=\epsilon N^{s-1/2}\prod_j\Gamma(1-s+\bar\mu_j)/\Gamma(s+\mu_j)$; it exists whenever the functional equation does, and $f\mapsto\tilde f$ is an involution on the forms whose completion satisfies the equation.

**Proposition.** $L(\tilde f,s)=\epsilon^{-1}\overline{L(f^*,1-\bar s)}$ in the self-dual case, and $M_h$ commutes with the duality up to the factor $h^*$: $\widetilde{M_hf}=M_{h^*}\tilde f$. The operator identity of the previous theorem and the definition of $\tilde f$ are the same identity read on two sides.

**Proof.** Substitute $s\mapsto1-s$ into the definition of $\tilde f$ and use the functional equation; the compatibility with $M_h$ is the multiplicativity of the involution on coefficients. This is the operator form of the functional equation in the sense of *L-Functions*.

## Worked Examples

**Example (the divisor-sum operator).** For $h=\mathbf{1}$, the constant function $1$, $M_{\mathbf 1}f(n)=\sum_{d\mid n}f(d)$ is the divisor-sum operator, $L(M_{\mathbf 1}f,s)=\zeta(s)L(f,s)$, and $\|M_{\mathbf 1}\|_{\mathcal{H}}=\zeta(2)$. Its Euler factors are $M_{\mathbf 1_p}$ with $\mathbf{1}_p(p^r)=1$.

**Example (the shift by a prime).** For $h=\delta_p$, $M_{\delta_p}f(n)=f(n/p)$ when $p\mid n$ and $0$ otherwise, and $L(M_{\delta_p}f,s)=p^{-s}L(f,s)$; this is the down-shift $D_p$ of *The Shift Operator on the Coefficients*, and its adjoint is the up-shift $S_p$. The Euler factor $(1-p^{-s})^{-1}$ corresponds to $M_{\mathbf 1_{p^\infty}}$.

**Example (the zeta operator).** $M_\mu$ is the convolution with the Möbius function; $M_\mu M_{\mathbf 1}=\mathrm{id}$, because $\mu*\mathbf 1=\varepsilon$; the pair is the fundamental inversion of the algebra, and on the $L$-side it reads $L(\mu,s)\zeta(s)=1$.

## Failure of the Degenerate Cases

The representation $h\mapsto M_h$ is an isomorphism of algebras on the module $\mathcal{A}$, but it is **not** a representation of the involutive algebra on $\mathcal{H}$: the involution on the elements is $h\mapsto h^*$ and the adjoint on the operators is $M_h^*=\Theta_h$, with $(\Theta_hg)(k)=\sum_m\overline{h(m)}g(mk)$, and the two agree only when $h$ is a scalar function $h=c\varepsilon$. The computation is the one of *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*, later in this category, and it is repeated there. The degenerate case in which they do agree is the augmentation form $\{f,g\}=f(1)\overline{g(1)}$, of rank one, under which every $M_h$ has adjoint $M_{h^*}$; the coefficient form used here is the nondegenerate form and does not share the property. The naive expectation that "multiplying by $h$" should have adjoint "multiplying by $h^*$" is therefore false on the whole algebra, and the discrepancy is exactly the difference between the two structures.

## Summary

For $h\in\mathcal{A}$ the multiplication operator is $M_hf=h*f$, and $L(M_hf,s)=L(h,s)L(f,s)$; the assignment $h\mapsto M_h$ is a faithful representation of the algebra, with $M_hM_g=M_{h*g}$ and $M_\varepsilon=\mathrm{id}$. On the form of the category, $\langle f,g\rangle=\sum f(n)\overline{g(n)}$, the operator $M_h$ is bounded with $\|M_h\|\le\|h\|_{\ell^1}$ for $h\in\ell^1$, and it is unbounded otherwise. The Euler factors are the Toeplitz operators $M_{h_p}$ of the local sequences, and the global operator is the norm-convergent product $\prod_pM_{h_p}$, which is a compact perturbation of the identity when $h$ is $\ell^1$ and trivial at almost all primes. The functional equation is the operator identity $\mathcal{R}\Lambda_f=\epsilon\Lambda_{f^*}$ with $\mathcal{R}$ the reflection $s\mapsto1-s$, and the dual form $\tilde f$ carries the same content on the $L$-side. The involution on the elements and the adjoint on the operators agree only in the degenerate augmentation case.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_h$ | Multiplication operator $f\mapsto h*f$ |
| $L(M_hf,s)=L(h,s)L(f,s)$ | The $L$-function identity |
| $\Theta_h=M_h^*$, $(\Theta_hg)(k)=\sum_m\overline{h(m)}g(mk)$ | The adjoint on $\mathcal{H}$ |
| $\mathcal{A}_p$, $M_{h_p}$ | $p$-primary component; local Toeplitz factor |
| $M_h=\prod_pM_{h_p}$ | Euler product as an operator product |
| $\Lambda_f(s)=N^{s/2}\prod_j\Gamma(s+\mu_j)L(f,s)$ | Completion |
| $\mathcal{R}\Lambda(s)=\Lambda(1-s)$ | Reflection operator |
| $\mathcal{R}\Lambda_f=\epsilon\Lambda_{f^*}$ | Functional equation as an operator identity |
| $\tilde f$, $L(\tilde f,s)=\gamma(f,s)^{-1}L(f,1-s)$ | Dual form |
| $h^*$ | Coefficient involution $h^*(n)=\overline{h(n)}$ |

## Further Reading

- Hugh Montgomery and Robert Vaughan, *Multiplicative Number Theory I: Classical Theory* (Cambridge University Press, 2007), for the algebra of arithmetic functions and the convolution.
- Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory* (American Mathematical Society, 2004), for the Euler product, the completion and the analytic continuation.
- Joseph Bernstein and Sergei Gelbart, *lectures on the representation theory of the multiplicative monoid* (mimeographed), for the regular representation of the convolution algebra.
- Paul Koosis, *Introduction to $H_p$ Spaces* (Cambridge University Press, 1998), for the boundedness of convolution operators and Young's inequality on the discrete monoid.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for the Toeplitz operators and the perturbation of the spectrum.
