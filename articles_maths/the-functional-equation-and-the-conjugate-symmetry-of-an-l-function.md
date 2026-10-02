
# __The Functional Equation and the Conjugate Symmetry of an L-Function__

## Introduction

A Dirichlet series with an Euler product is completed by the archimedean factor $\Gamma$, and the completed function satisfies a functional equation relating its values at $s$ and at $1-s$. When the coefficients are real the equation has the conjugate symmetry $\Lambda(s)=\epsilon\overline{\Lambda(1-\bar s)}$, which is the reflection across the critical line together with complex conjugation. This article states the completion, the functional equation and the conjugate symmetry in the form fixed for the category, proves the elementary consequences, and identifies the exact hypotheses on the archimedean factor and the conductor. It is the entry point of the `* Theory` group of this category: the conjugate symmetry of the zeros and the critical line is *The Conjugate Symmetry and the Critical Line*, the positivity form of the equation is *Positivity and the Explicit Formula* and *Hermitian Forms and the Zeta Function*, and the operator reading is in *Multiplication Operators on an L-Function* and *Shift Operator on a Dirichlet Series*.

The conventions are those of the category. The Dirichlet series of an arithmetic function $f$ is $L(f,s)=\sum_nf(n)n^{-s}$; the coefficient involution is $f^*(n)=\overline{f(n)}$; the local factor at $p$ is $L_p(f,s)$; the conductor is $N\ge1$ and the archimedean parameters are $\mu_1,\dots,\mu_d$. The algebra of arithmetic functions and its Euler product are as in *The Euler Product Operator*. Nothing here reads a distance as an object; the completion is a product of gamma factors and a power of the conductor, and the equation is an identity of meromorphic functions.

## The Completion

### Definition

**Definition.** Let $L(f,\cdot)$ have analytic continuation to a meromorphic function of finite order, conductor $N$, degree $d$, archimedean parameters $\mu_j\in\mathbb{C}$, and sign $\epsilon$ of modulus $1$. The **completed $L$-function** is
$$
\Lambda_f(s)=N^{s/2}\prod_{j=1}^{d}\Gamma(s+\mu_j)\,L(f,s).
$$
The **conjugate completion** is $\Lambda_{f^*}$, and the **dual completion** is $\widetilde\Lambda_f(s)=\overline{\Lambda_{f^*}(\bar s)}$.

**Proposition.** The completion is meromorphic of finite order, with poles only those of $L(f,\cdot)$; the gamma factors are nonzero, so the completion removes no zeros of $L(f,\cdot)$ except the archimedean ones that are introduced; and the assignment $f\mapsto\Lambda_f$ is linear in $f$ and compatible with the coefficient involution.

**Proof.** The product of finitely many gamma functions is meromorphic with poles on the vertical lines determined by the $\mu_j$, and $N^{s/2}$ is entire and nonvanishing; the linearity is the linearity of the Dirichlet series and of the product. This is the standard completion of *L-Functions*.

### The archimedean factor

**Theorem.** The archimedean factor $\gamma_\infty(s)=\prod_j\Gamma(s+\mu_j)$ satisfies the reflection identity
$$
\gamma_\infty(s)\,\gamma_\infty(1-s)\cdot(\text{a rational factor in }s)=\text{an explicit nonvanishing factor},
$$
so that the quotient $\Lambda_f(1-s)/\Lambda_{f^*}(s)$ is the product of the sign, the conductor power and the ratio of gamma factors, and it is a function of exponential type with no zeros or poles of its own.

**Proof.** The reflection formula of the gamma function, together with the substitution $s\mapsto1-s$ in $N^{s/2}$, gives the identity; the details are in *L-Functions*. The absence of extra zeros and poles is the nonvanishing of $\Gamma$ on $\mathbb{C}$.

## The Functional Equation

### Statement

**Theorem (the functional equation).** There is a meromorphic function of $s$, the **gamma factor** $\gamma(f,s)$, such that
$$
L(f,1-s)=\gamma(f,s)\,L(f^*,s),
$$
equivalently
$$
\Lambda_f(1-s)=\epsilon\,\overline{\Lambda_{f^*}(\bar s)},
$$
where $\epsilon$ is the sign. When $f^*=f$, that is when the coefficients are real, the equation reads $\Lambda_f(s)=\epsilon\overline{\Lambda_f(1-\bar s)}$; and $\epsilon=\pm1$ in the self-dual case with the convention that the archimedean factor is normalised so that the sign is a fourth root of unity in general.

**Proof.** The two displays are the two forms of the same identity, obtained from each other by the substitution $s\mapsto1-s$ and complex conjugation. The analytic input is the integral representation of the completion as the Mellin transform of a theta-like series, in which the functional equation is the Poisson summation applied to the underlying quadratic form; the general case is assembled from the local factors, each of which satisfies a local functional equation, by the Euler product of *The Euler Product Operator*. The reference is *L-Functions*.

### Elementary consequences

**Theorem.** The functional equation has the following consequences.
$$
L(f,-n)=0 \ \text{ for the negative integers } n \text{ making } \gamma(f,s) \text{ vanish and not cancelled}, \qquad \operatorname{ord}_{s=\rho}L(f,\cdot)=\operatorname{ord}_{s=1-\rho}L(f^*,\cdot),
$$
so the zeros are symmetric under $s\mapsto1-s$ up to conjugation, and the only possible poles are the poles of the gamma factor and of $L(f,\cdot)$ itself. The completed function satisfies $\Lambda_f(s)=\epsilon^2\Lambda_f(s)$ after two reflections, so $\epsilon^2$ is the consistency of the equation with the reflection of order two.

**Proof.** Apply the functional equation at $s=\rho$ and at $s=1-\rho$; the gamma factor is nonvanishing at the location of a genuine zero, so the orders match. The trivial zeros are the points where the gamma factor has a pole and $L(f,\cdot)$ is regular. The consistency statement is the square of the reflection.

## Conjugate Symmetry

**Definition.** The **conjugate symmetry** is the involution of the $s$-plane
$$
\kappa(s)=1-\bar s ,
$$
fixing pointwise the **critical line** $\Re s=1/2$, and the **conjugate reflection** of a function is $F\mapsto\overline{F(\bar\cdot)}$.

**Theorem.** If the coefficients of $f$ are real, so that $f^*=f$ and $\Lambda_f$ is real on the real axis in the region of convergence, then
$$
\Lambda_f(\kappa(s))=\epsilon\,\overline{\Lambda_f(s)},
$$
so the zeros of $\Lambda_f$ are symmetric under $\kappa$, the zero set is invariant under $s\mapsto\bar s$ and $s\mapsto1-s$ separately, and the zeros come in the quadruples $\rho$, $\bar\rho$, $1-\rho$, $1-\bar\rho$ (with coincidences at the critical line and the real axis).

**Proof.** $\kappa$ is an involution of order two fixing $\Re s=1/2$; the functional equation and the reality of the coefficients give the display, and applying the reflection twice gives the symmetry group generated by $\kappa$ and $s\mapsto\bar s$, which is the Klein four-group acting on the zero multiset. The critical line is the fixed set of $\kappa$ and therefore carries the zeros that are fixed by the symmetry.

**Corollary (the critical strip).** The zeros of $\Lambda_f$ other than the trivial ones lie in the **critical strip** $0\le\Re s\le1$, and within it are symmetric under the Klein four-group. The Riemann hypothesis asserts that they lie on the critical line $\Re s=1/2$; the statement of the conjecture, its arithmetic significance and the evidence for it belong to *Riemann Hypothesis*, written in this part.

## Worked Examples

**Example (the zeta function).** $\zeta(s)$ with $N=1$, $d=1$, $\mu_1=0$, sign $\epsilon=1$: $\Lambda(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$ and $\Lambda(s)=\Lambda(1-s)$; the trivial zeros are the negative even integers, from the poles of $\Gamma(s/2)$.

**Example (a Dirichlet character).** For $\chi$ of conductor $q$ and parity $a\in\{0,1\}$, $N=q$, $d=1$, $\mu_1=a/2$, and the sign is $\epsilon=\tau(\chi)/(i^aq^{1/2})$, a root of unity; the completed function satisfies the conjugate symmetry with the Gauss sum in the sign.

**Example (a normalised eigenform).** For $L(f,s)$ of *The Hecke Operator*, $N$ the level, $d=2$, $\mu_1=(k-1)/2$, $\mu_2=(k+1)/2$; the sign is $\epsilon=\pm1$ for the forms in the new subspace fixed by the Fricke involution, and the equation is the classical Hecke functional equation.

## Failure of the Degenerate Cases

The functional equation fails in four degenerate configurations. First, the equation is only meromorphic, so a pole of $\Lambda_f$ at $s=1$ is the pole of $L(f,\cdot)$ and the gamma factor cannot cancel it; the equation is then an identity of meromorphic functions with a genuine pole, and the notion of "the zeros" must be read outside the pole. Second, if the archimedean factor is not normalised, the sign $\epsilon$ depends on the normalisation and the equation acquires an extra exponential factor; the normalisation is part of the data and is fixed here. Third, if the coefficients are not real the conjugate symmetry is the general equation with $f^*$ on the right, and the zero symmetry is under $s\mapsto1-\bar s$ composed with the coefficient involution, which may have no fixed points on the critical line. Fourth, in the degenerate case of a Dirichlet polynomial with no Euler product the "functional equation" is not available unless the polynomial is the truncation of a genuine $L$-function, and the completion does not repair the absence of the analytic structure. These are the boundary cases of the completion.

## Summary

For an $L$-function with conductor $N$, degree $d$, archimedean parameters $\mu_j$ and sign $\epsilon$, the completion is $\Lambda_f(s)=N^{s/2}\prod_j\Gamma(s+\mu_j)L(f,s)$ and the functional equation is $\Lambda_f(1-s)=\epsilon\overline{\Lambda_{f^*}(\bar s)}$, or $\Lambda_f(s)=\epsilon\overline{\Lambda_f(1-\bar s)}$ when the coefficients are real. The conjugate symmetry is the involution $\kappa(s)=1-\bar s$ fixing the critical line, and for real coefficients the zeros of $\Lambda_f$ are invariant under the Klein four-group generated by $\kappa$ and complex conjugation, so they come in the quadruples $\rho,\bar\rho,1-\rho,1-\bar\rho$ and lie in the critical strip outside the trivial zeros from the gamma factor. The equation is an identity of meromorphic functions, the sign is a root of unity depending on the normalisation, and the degenerate cases are the poles of the completion, the non-reality of the coefficients and the absence of an Euler product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda_f(s)=N^{s/2}\prod_j\Gamma(s+\mu_j)L(f,s)$ | Completed $L$-function |
| $N$, $d$, $\mu_j$, $\epsilon$ | Conductor, degree, archimedean parameters, sign |
| $\gamma(f,s)$ | Gamma factor |
| $\Lambda_f(1-s)=\epsilon\overline{\Lambda_{f^*}(\bar s)}$ | Functional equation |
| $f^*(n)=\overline{f(n)}$ | Coefficient involution |
| $\kappa(s)=1-\bar s$ | Conjugate symmetry |
| $\Re s=1/2$ | Critical line |
| $0\le\Re s\le1$ | Critical strip |
| $\rho,\bar\rho,1-\rho,1-\bar\rho$ | The zero quadruple |

## Further Reading

- Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory* (American Mathematical Society, 2004), for the completion and the functional equation.
- Harold Edwards, *Riemann's Zeta Function* (Academic Press, 1974), for the zeta case and the theta-function proof.
- Goro Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions* (Princeton University Press, 1971), for the Hecke functional equation.
- John Tate, *Fourier Analysis in Number Fields and Hecke's Zeta-Functions* (thesis, Princeton, 1950), for the local-global construction of the completion.
- Jerrold Tunnell, *The Functional Equation for L-Functions* (lecture notes), for the elementary derivation of the gamma factors.
