
# __Shift Operator on a Dirichlet Series__

## Introduction

The shift of the argument of a Dirichlet series is the simplest operation one can perform on it: replace $L(s)$ by $L(s+t)$. On the coefficient sequence the same operation multiplies the $n$-th coefficient by $n^{-t}$, so the shift is a diagonal operator, and it is a one-parameter group of contractions whose generator is the unbounded diagonal operator with entries $-\log n$. The shift is not an analytic continuation, but it is the exact symmetry of the continuation: the domain of $L(\cdot+t)$ is the domain of $L$ translated by $t$, the zeros are translated by $-t$, and the functional equation, which relates $s$ to $1-s$, conjugates the shift by $t$ into the shift by $-t$. This article defines the shift, computes its norms, spectrum and generator, and states its interplay with the functional equation and the zero distribution.

The conventions are those of the category. The Dirichlet series of $f$ is $L(f,s)=\sum_nf(n)n^{-s}$; the Hilbert space is $\mathcal{H}=\ell^2$ with the form $\langle f,g\rangle=\sum_nf(n)\overline{g(n)}$; the abscissa of absolute convergence of $L(f,\cdot)$ is written $\sigma_a$. The companion article *The Shift Operator on the Coefficients* treats the operators $D_m$, $S_m$ on the coefficients; the functional equation and the reflection are in *The Functional Equation and the Conjugate Symmetry of an L-Function*, later in this category. Nothing here reads a distance as an object; convergence is the convergence of the Dirichlet series and the spectrum is the spectrum of the diagonal operator on $\mathcal{H}$.

## The One-Parameter Shift

### Definition

**Definition.** For $t\in\mathbb{C}$ the **shift** $\Sigma_t$ acts on a Dirichlet series by
$$
(\Sigma_tL)(s)=L(s+t),
$$
and on the coefficient function by $(\Sigma_tf)(n)=n^{-t}f(n)$. The single operator $\Sigma=\Sigma_1$ is the **unit shift**.

**Proposition.** The shift is well defined on the formal Dirichlet series, it maps functions of bounded support to functions of bounded support, and
$$
\Sigma_t\Sigma_u=\Sigma_{t+u},\qquad \Sigma_0=\mathrm{id},\qquad \Sigma_t^{-1}=\Sigma_{-t}
$$
as operators on the formal series. On any Dirichlet series that converges somewhere it maps the half-plane of convergence $\Re s>\sigma$ to the half-plane $\Re s>\sigma-\Re t$.

**Proof.** The coefficient relation $(\Sigma_tf)(n)=n^{-t}f(n)$ is the definition read coefficientwise; the shift identity is $n^{-t}n^{-u}=n^{-(t+u)}$. The half-plane statement is that $L(s+t)$ converges when $\Re(s+t)>\sigma$, i.e. $\Re s>\sigma-\Re t$.

### Norms and the semigroup

**Theorem.** On $\mathcal{H}=\ell^2$ the operator $\Sigma_t$ is diagonal, $\Sigma_t=\operatorname{diag}(n^{-t})$, with
$$
\|\Sigma_t\|_{\mathcal{H}}=1 \quad\text{for } \Re t\ge0,
$$
and $\Sigma_t$ is a contraction for $\Re t\ge0$; it is unitary exactly for $t$ purely imaginary, in which case $\Sigma_{i\theta}=\operatorname{diag}(n^{-i\theta})$ and $\Sigma_{i\theta}^*=\Sigma_{-i\theta}$. The family $(\Sigma_t)_{\Re t\ge0}$ is a strongly continuous contraction semigroup whose generator is the closed unbounded operator
$$
A=\operatorname{diag}(-\log n),\qquad \mathcal{D}(A)=\Bigl\{f\in\mathcal{H}:\sum_n|f(n)|^2(\log n)^2<\infty\Bigr\}.
$$

**Proof.** A diagonal operator with diagonal entries $d_n$ has norm $\sup_n|d_n|$, and $|n^{-t}|=n^{-\Re t}\le1$ for $\Re t\ge0$ with spectrum on the unit circle exactly when $\Re t=0$. The semigroup property is the proposition; strong continuity is the dominated convergence applied to the entries, which tend to $1$ as $t\to0$ for each fixed $n$, together with the uniform bound $1$. The generator of a diagonal contraction semigroup is the diagonal operator of the derivatives at $0$, namely $\frac{d}{dt}n^{-t}|_{t=0}=-\log n$, whose domain is as displayed; the details are the standard theory of *Semi-Groups*.

## Spectrum and Zeros

### The spectrum

**Theorem.** On $\mathcal{H}=\ell^2$ the spectrum of the unit shift $\Sigma$ is
$$
\operatorname{spec}(\Sigma)=\overline{\{\,n^{-1}:f(n)\ne0\,\}}\cup\{0\},
$$
and the spectrum of $\Sigma_t$ is the closure of $\{n^{-t}:f(n)\ne0\}$ together with $0$. These are the spectra of a diagonal operator, and they are countable with $0$ as the only accumulation point.

**Proof.** For a diagonal operator the spectrum is the closure of the set of diagonal entries together with the limit points of the diagonal entries which are not eigenvalues of finite multiplicity; here the entries $n^{-t}$ form a sequence tending to $0$ unless the support is finite, so the spectrum is the closure of the values attained, and $0$ belongs to the spectrum whenever the support is infinite. This is the standard spectral computation for diagonal operators, in *Spectral Theory*.

### The zeros

**Theorem (the zero shift).** If $\rho$ is a zero of the analytic continuation of $L(f,\cdot)$ and $\rho$ is not a pole of the factors involved in the completion, then $\rho-t$ is a zero of the analytic continuation of $\Sigma_tL(f,\cdot)$. Consequently the multiset of zeros of $\Sigma_tL$ is the multiset of zeros of $L$ translated by $-t$; in particular the abscissa of convergence satisfies $a(\Sigma_tL)=a(L)-\Re t$ in the sense that a zero-free region translates, and the zero-counting function satisfies
$$
N_{\Sigma_tL}(T)=N_{L}(T+\Im t)+O(1).
$$

**Proof.** The analytic continuation of $\Sigma_tL$ is the translate of that of $L$ by $t$, so its values at $s$ are the values of $L$ at $s+t$; a zero at $\rho$ of $L$ therefore produces a zero at $\rho-t$ of $\Sigma_tL$. The counting function translates with the imaginary part of $t$, and the $O(1)$ accounts for the boundary strip; this is the Riemann–von Mangoldt principle of *Zeta Functions*.

## The Functional Equation and the Shift

### Conjugation by the reflection

**Definition.** The **reflection** $\mathcal{R}$ acts on functions of $s$ by $(\mathcal{R}F)(s)=F(1-s)$, so that the completed $L$-function satisfies $\mathcal{R}\Lambda_f=\epsilon\Lambda_{f^*}$ as in *The Functional Equation and the Conjugate Symmetry of an L-Function*.

**Theorem.** For all $t$, $\ \mathcal{R}\Sigma_t\mathcal{R}=\Sigma_{-t}$: the reflection conjugates the shift by $t$ into the shift by $-t$. Equivalently, on the completed function,
$$
(\mathcal{R}\Sigma_t\mathcal{R}\Lambda_f)(s)=\Lambda_f(s-t).
$$

**Proof.** $(\mathcal{R}\Sigma_t\mathcal{R}\Lambda)(s)=(\Sigma_t\mathcal{R}\Lambda)(1-s)=(\mathcal{R}\Lambda)(1-s+t)=\Lambda(1-(1-s+t))=\Lambda(s-t)=\Sigma_{-t}\Lambda(s)$. The computation uses only the two definitions.

**Corollary.** The group of shifts is generated by $\Sigma$ together with the reflection in the sense that $\mathcal{R}$ acts on the one-parameter group by $t\mapsto-t$; hence any statement about the zeros on one side of the critical line transfers to the other by the functional equation and the shifts. In particular the functional equation together with the integer shifts generates the translation group acting on the multiset of zeros, and it is the reason the zeros of a completed $L$-function come in the symmetric quadruples $\rho$, $1-\rho$, $\bar\rho$, $1-\bar\rho$ when the coefficients are real.

## Worked Examples

**Example (the zeta function).** For $\zeta(s)=\sum_nn^{-s}$, $\Sigma_t\zeta(s)=\zeta(s+t)$ and the coefficients are $n^{-t}$. The zeros of $\zeta(s+1)$ are the zeros of $\zeta$ translated by $-1$; the pole of $\zeta$ at $s=1$ becomes a pole of $\Sigma_{-1}\zeta$ at $s=2$ and a regular behaviour of $\Sigma_1\zeta$ at $s=0$.

**Example (a Dirichlet character).** For $L(\chi,s)$ with $\chi$ of conductor $q$, $\Sigma_t$ multiplies the coefficients by $n^{-t}$; the shift changes the conductor and the gamma factor of the completed function, so the functional equation of the shifted series involves a different completion.

**Example (a normalised eigenform).** For $L(f,s)$ of *The Hecke Operator*, $\Sigma_tL(f,s)=\sum_na_nn^{-s-t}$ has coefficients $a_nn^{-t}$; this is the local twist of the modular form, and it is the operator whose fixed points are the series with all nonzero coefficients on the locus $n^{-s}n^{-t}=n^{-s}$ for $t=0$.

## Failure of the Degenerate Cases

The shift has four degenerate boundaries. First, for $\Re t>0$ the operator $\Sigma_t$ is not invertible: it is a contraction with no inverse on $\mathcal{H}$, since the diagonal entry $n^{-t}$ tends to $0$ and the range is not closed; the group law $\Sigma_t^{-1}=\Sigma_{-t}$ holds on the formal series but $\Sigma_{-t}$ then leaves $\mathcal{H}$ for the $t$ with $\Re t>0$. Second, the semigroup is not uniformly continuous: the generator $A=\operatorname{diag}(-\log n)$ is unbounded and densely defined but not bounded, and the difference $\|\Sigma_t-\mathrm{id}\|$ does not tend to $0$ as $t\to0$. Third, the zero-shift statement fails at the zeros created by the archimedean factor of the completion: the trivial zeros of $\zeta$ are produced by the poles of the gamma factor and the reflection, and the shift moves them off the integers, where they are no longer zeros of the completed function; the "multiset of zeros" of the statement is the multiset of zeros of the $L$-function alone, not of the completion. Fourth, if $L(f,\cdot)$ has only finitely many nonzero coefficients the spectrum consists of finitely many points and the generator has finite rank; this is the degenerate case of a Dirichlet polynomial, where all of the statements reduce to the finite-dimensional linear algebra of the diagonal matrix $\operatorname{diag}(n^{-t})$.

## Summary

For $t\in\mathbb{C}$ the shift $\Sigma_t$ sends $L(s)$ to $L(s+t)$ and the coefficients $f(n)$ to $n^{-t}f(n)$; it satisfies $\Sigma_t\Sigma_u=\Sigma_{t+u}$ and is a one-parameter group of diagonal operators with $\|\Sigma_t\|_{\mathcal{H}}=1$ for $\Re t\ge0$ and unitary exactly for $t$ purely imaginary. Its generator is the unbounded diagonal operator $\operatorname{diag}(-\log n)$ with domain $\{f:\sum|f(n)|^2(\log n)^2<\infty\}$. The spectrum of $\Sigma$ on $\mathcal{H}$ is the closure of $\{n^{-1}:f(n)\ne0\}$ with $0$ adjoined, the zeros of $\Sigma_tL$ are those of $L$ translated by $-t$, and the reflection satisfies $\mathcal{R}\Sigma_t\mathcal{R}=\Sigma_{-t}$, so the functional equation and the shifts together generate the translations acting on the zeros. The degenerate boundaries are the noninvertibility of $\Sigma_t$ for $\Re t>0$, the unboundedness of the generator, the trivial zeros created by the completion and the finite-dimensional collapse for a Dirichlet polynomial.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Sigma_t$, $(\Sigma_tL)(s)=L(s+t)$ | The shift by $t$ |
| $(\Sigma_tf)(n)=n^{-t}f(n)$ | Action on the coefficients |
| $\Sigma_t\Sigma_u=\Sigma_{t+u}$ | The group law |
| $\|\Sigma_t\|_{\mathcal{H}}=1$ for $\Re t\ge0$ | The contraction property |
| $A=\operatorname{diag}(-\log n)$ | The generator |
| $\operatorname{spec}(\Sigma)=\overline{\{n^{-1}:f(n)\ne0\}}\cup\{0\}$ | The spectrum |
| $N_{\Sigma_tL}(T)=N_L(T+\Im t)+O(1)$ | The zero count under the shift |
| $\mathcal{R}$, $(\mathcal{R}F)(s)=F(1-s)$ | The reflection |
| $\mathcal{R}\Sigma_t\mathcal{R}=\Sigma_{-t}$ | Conjugation of the shift by the reflection |

## Further Reading

- Einar Hille and Ralph Phillips, *Functional Analysis and Semi-Groups* (American Mathematical Society, 1957), for the strongly continuous semigroups and the generator of a contraction semigroup.
- Hugh Montgomery and Robert Vaughan, *Multiplicative Number Theory I: Classical Theory* (Cambridge University Press, 2007), for the analytic continuation and the abscissae of Dirichlet series.
- Harold Edwards, *Riemann's Zeta Function* (Academic Press, 1974), for the Riemann–von Mangoldt count and the zero distribution.
- Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory* (American Mathematical Society, 2004), for the completed $L$-function and the reflection.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 1976), for the unbounded diagonal operators and their spectra.
