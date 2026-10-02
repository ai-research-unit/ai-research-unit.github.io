
# __Positive Definite Distributions__

## Introduction

Positive definiteness is a condition on a function that can be tested against the smooth compactly supported
functions, and this makes it a condition on a distribution. A distribution $T$ on $\mathbb R^n$ is **positive
definite** if
$$
\langle T,\varphi*\varphi^{*}\rangle\geq0\qquad\text{for all }\varphi\in C_c^\infty(\mathbb R^n),
$$
where $\varphi^{*}(x)=\overline{\varphi(-x)}$ is the convolution involution of the group algebra; the
Gaussian smoothings of $T$ are then positive definite functions in the sense of the earlier article, and the
theorem of **Bochner–Schwartz** states that a distribution is positive definite exactly when it is the
Fourier transform of a positive measure of at most polynomial growth — a positive **tempered** measure. The
present article is the distributional form of Bochner's theorem, and it is the natural meeting point of the
two threads of this category: the Fourier analysis of the earlier categories and the operator theory of
*-involutions developed in the present one.

This article is the fifth of the `*` group of *Foundations of Analysis*. Its prerequisites are
*Distributions and Fundamental Solutions*, later in this Part, for the test functions, the distributions,
the convolution of distributions and the Fourier transform of a tempered distribution, and *Positive
Definite Functions and Hermitian Kernels* and *Hermitian Measures and Complex Measures*, the earlier
articles of this group, for Bochner's theorem, the positive definite functions and the involution on the
measures. The Fourier transform of a tempered distribution and the Paley–Wiener and Schwartz theorems are
*Distributions and Fundamental Solutions*; the Riesz representation and the convergence of measures are
*Measure Theory and Integration*; the Hilbert-space construction of the positive functional is the
Kolmogorov decomposition of the first article of this group. The smooth **Bochner theorem** for functions is
*Harmonic Analysis on Groups*, in the neighbouring category *Analysis on Groups* of this Part; the
Lévy–Khinchine formula and the infinitely divisible laws, which are the probabilistic reading of the
theorem, belong to *Measure-Theoretic Probability*, in a later Part, and are named only. The Hermitian
kernels of the last article of the group carry the same involution in the operator form. No geometry is
invoked.

## The Involutions on Distributions

### The Convolution Involution

**Definition.** On $C_c^\infty(\mathbb R^n)$ the **convolution involution** is
$\varphi^{*}(x)=\overline{\varphi(-x)}$; it is conjugate-linear, involutive, and multiplicative for the
convolution, $(\varphi*\psi)^{*}=\psi^{*}*\varphi^{*}$. On the distributions it induces
$$
T^{*}(\varphi)=\overline{T(\varphi^{*})} ,
$$
the **adjoint involution**; a distribution is **Hermitian** if $T^{*}=T$ and **real** if $T(\varphi)\in\mathbb R$
for every real $\varphi$.

**Remark (the two involutions).** As in *Hermitian Measures and Complex Measures*, the involution $T^{*}$
must be distinguished from the **value-conjugation** $\bar T(\varphi)=\overline{T(\bar\varphi)}$, which is
induced by conjugation of the test function alone. Positive definiteness uses $T^{*}$, the involution of the
convolution algebra, and not $\bar T$; the two agree on the tempered distributions whose reflection is
itself, and the distinction is recorded so that the star is read as the algebra involution. The mark is
consistent with *Conventions in Mathematics*: dagger for the adjoint of an operator, star for the involution
of an algebra element, and the adjoint involution here is the algebra star.

### Positive Definiteness

**Definition.** A distribution $T\in\mathcal D'(\mathbb R^n)$ is **positive definite** if
$$
\langle T,\varphi*\varphi^{*}\rangle\geq0\qquad\text{for every }\varphi\in C_c^\infty(\mathbb R^n) .
$$

**Theorem (the equivalent forms).** For $T\in\mathcal D'(\mathbb R^n)$ the following are equivalent: $T$ is
positive definite; the Hermitian form $K(\varphi,\psi)=\langle T,\varphi*\psi^{*}\rangle$ on
$C_c^\infty(\mathbb R^n)$ is positive semidefinite; for every finite set of points and coefficients the
smoothed kernel is positive semidefinite. A positive definite distribution is Hermitian, and the map
$(\varphi,\psi)\mapsto\langle T,\varphi*\psi^{*}\rangle$ is a positive semidefinite Hermitian form.

**Proof.** The equivalence is the computation
$K(\varphi,\psi)=\langle T,\varphi*\psi^{*}\rangle$ and the polarisation of the quadratic form
$\varphi\mapsto K(\varphi,\varphi)=\langle T,\varphi*\varphi^{*}\rangle$; the Hermitian property is obtained
by applying the inequality to $\varphi+\lambda\psi$ and varying $\lambda$, as for kernels and for measures.
$\blacksquare$

**Theorem (functions give distributions).** A locally integrable function $f$ on $\mathbb R^n$ of at most
polynomial growth, regarded as a distribution, is positive definite exactly when the function $f$ is
positive definite in the sense of *Positive Definite Functions and Hermitian Kernels*, almost everywhere.

**Proof.** If $f$ is a positive definite function then
$\langle f,\varphi*\varphi^{*}\rangle=\iint f(x-y)\varphi(y)\overline{\varphi(x)}\,dydx\geq0$ by the
definition; conversely the inequality for a smooth nonnegative approximate identity concentrated at the
points recovers the positive definiteness of the function. $\blacksquare$

Thus the positive definite distributions contain the positive definite functions of polynomial growth, and
the theorem below shows that they contain nothing wilder than a positive measure.

### The Bochner–Schwartz Theorem

**Definition.** A positive measure $\mu$ on $\mathbb R^n$ is **tempered** if
$\int_{\mathbb R^n}(1+\lvert\xi\rvert)^{-N}d\mu(\xi)<\infty$ for some $N$; equivalently, if it is the
Fourier transform of a tempered distribution, i.e. if the function
$\hat\mu(x)=\int e^{-2\pi ix\cdot\xi}d\mu(\xi)$ is a tempered distribution.

**Theorem (Bochner–Schwartz).** A distribution $T\in\mathcal D'(\mathbb R^n)$ is positive definite if and
only if there is a unique positive tempered measure $\mu$ with $T=\hat\mu$; that is,
$$
\langle T,\varphi\rangle=\int_{\mathbb R^n}\hat\varphi(\xi)\,d\mu(\xi)
=\int_{\mathbb R^n}\Bigl(\int_{\mathbb R^n}\varphi(x)e^{-2\pi ix\cdot\xi}dx\Bigr)d\mu(\xi) .
$$
Equivalently, the Fourier transform is a bijection between the positive definite distributions and the
positive tempered measures, and it carries the positive definite distributions onto a cone which is the
image of the positive cone of the measures.

### Proof Sketch

**Proof sketch.** Suppose first that $T=\hat\mu$ with $\mu\geq0$ tempered. Then for
$\varphi\in C_c^\infty$,
$$
\langle T,\varphi*\varphi^{*}\rangle=\int\lvert\hat\varphi(\xi)\rvert^2\,d\mu(\xi)\geq0 ,
$$
because $\widehat{\varphi*\varphi^{*}}=\lvert\hat\varphi\rvert^2$ by the convolution and involution
identities of the Fourier article; so $T$ is positive definite. Conversely let $T$ be positive definite, and
let $\rho_\epsilon(x)=\epsilon^{-n}\rho(x/\epsilon)$ be a nonnegative even approximate identity with
$\rho\in C_c^\infty$ real and even, so that $\rho_\epsilon^{*}=\rho_\epsilon$ and
$\rho_\epsilon\to\delta_0$. The convolutions $T_\epsilon=T*\rho_\epsilon$ are functions, and they are
positive definite: for finite data,
$$
\sum_{i,j}\overline{c_i}c_jT_\epsilon(x_i-x_j)
=\Bigl\langle T,\Bigl(\sum_ic_i\rho_\epsilon(\cdot-x_i)\Bigr)*\Bigl(\sum_ic_i\rho_\epsilon(\cdot-x_i)\Bigr)^{*}\Bigr\rangle\geq0 ,
$$
since $\rho_\epsilon^{*}=\rho_\epsilon$. By Bochner's theorem for continuous positive definite functions,
$T_\epsilon=\hat\mu_\epsilon$ with $\mu_\epsilon\geq0$ a finite measure. As $\epsilon\to0$,
$T_\epsilon\to T$ in $\mathcal D'$; the measures $\mu_\epsilon$ converge weakly, after passing to a
subsequence, to a positive measure $\mu$, and the temperedness of $T$ — the fact that $T$ is a distribution
of finite order — bounds the growth of the masses $\mu_\epsilon$ on the balls and forces
$\int(1+\lvert\xi\rvert)^{-N}d\mu<\infty$ for $N$ large enough, so that $\mu$ is tempered and
$T=\hat\mu$. Uniqueness is the injectivity of the Fourier transform on tempered distributions. The
details of the growth control and the weak convergence belong to *Measure Theory and Integration* and
*Distributions and Fundamental Solutions*. $\blacksquare$

The proof is the smoothing argument: the distribution is regularised into positive definite functions, each
of which is the transform of a positive measure by Bochner's theorem, and the measures are shown to
converge; the positive definite distributions are therefore exactly the distributional transforms of the
positive tempered measures, and the theorem is the distributional Bochner theorem.

## Consequences and Examples

### The Cone of Positive Definite Distributions

**Theorem.** The positive definite distributions form a closed convex cone in $\mathcal D'$: sums with
nonnegative coefficients of positive definite distributions are positive definite, the limit in $\mathcal D'$
of positive definite distributions is positive definite, and a positive definite distribution is Hermitian.
Under the Fourier transform the cone becomes the cone of positive tempered measures.

**Proof.** The defining inequality is preserved by nonnegative linear combinations and by distributional
limits; the Hermitian property comes from polarisation; the cone statement on the transform side is
Bochner–Schwartz, and the positivity and temperedness of the measures are preserved by limits. $\blacksquare$

**Theorem (order and the measure).** A positive definite distribution has a well-defined **order**, and the
growth of its spectral measure is tied to it: if $T$ is of order at most $N$, then
$\int(1+\lvert\xi\rvert)^{-2N-n-1}d\mu<\infty$. In particular, the positive definite distributions of finite
order are exactly the transforms of the positive measures with the corresponding polynomial growth, and a
bounded continuous positive definite function is exactly a positive definite distribution whose measure is
finite (Bochner's theorem in the function case).

**Proof.** The order of a distribution is the least $N$ with $\lvert\langle T,\varphi\rangle\rvert\leq
C\sum_{\lvert\alpha\rvert\leq N}\sup\lvert\partial^\alpha\varphi\rvert$, and the transformed pairing
$\int\hat\varphi\,d\mu$ shows that the growth of $\mu$ is controlled by the seminorms of $\varphi$ used;
the finite-measure case is Bochner's theorem for bounded continuous functions. $\blacksquare$

### Examples

**Example (the Dirac mass and Lebesgue measure).** The Dirac mass $T=\delta_0$ is positive definite, because
$$
\langle\delta_0,\varphi*\varphi^{*}\rangle=(\varphi*\varphi^{*})(0)=\int_{\mathbb R^n}\lvert\varphi(x)\rvert^2dx\geq0 ,
$$
and its spectral measure is the Lebesgue measure $d\mu=d\xi$; conversely the constant function $T=1$ is
positive definite with spectral measure $\delta_0$, since $\langle1,\varphi*\varphi^{*}\rangle=\lvert\int\varphi\rvert^2\geq0$.
The pair is the extreme case of Bochner–Schwartz: the distribution transform of the Lebesgue measure is the
Dirac mass and conversely.

**Example (positive definite functions).** A positive measure $\mu$ with a density gives the positive
definite function $\hat\mu$; for the Gaussian density $\sqrt t\,e^{-\pi t\lvert\xi\rvert^2}$ this is the
positive definite function $e^{-\pi\lvert x\rvert^2/t}$, and for the measure $\frac12(\delta_\xi+\delta_{-\xi})$
it is the cosine $\cos(2\pi x\cdot\xi)$. Every character $e^{2\pi ix\cdot\xi}$ is positive definite with
spectral measure $\delta_\xi$, and every finite positive combination of characters with coefficients is
positive definite, with the corresponding discrete measure.

**Example (a Hermitian distribution that is not positive definite).** The tempered distribution
$T=1+\lvert x\rvert^2$ is Hermitian but is not positive definite: its Fourier transform is the distribution
$\delta_0-\frac1{4\pi^2}\Delta\delta_0$, which is not a positive measure, as the sign of its action on a
nonconstant positive test function shows. The example exhibits the gap between the Hermitian distributions
and the positive definite ones, exactly as a real symmetric matrix with a negative eigenvalue is Hermitian
and not positive.

## Summary

A distribution is positive definite when $\langle T,\varphi*\varphi^{*}\rangle\geq0$ for all test functions,
where $\varphi^{*}(x)=\overline{\varphi(-x)}$ is the convolution involution; the condition is equivalent to
the positive semidefiniteness of the Hermitian form $\langle T,\varphi*\psi^{*}\rangle$, and it forces $T$ to
be Hermitian for the adjoint involution $T^{*}(\varphi)=\overline{T(\varphi^{*})}$, which is distinct from
the value-conjugation $\bar T$ and is the algebra involution. The theorem of Bochner–Schwartz states that a
distribution is positive definite exactly when it is the transform $\hat\mu$ of a unique positive tempered
measure $\mu$, so that the Fourier transform is a bijection between the positive definite distributions and
the positive tempered measures; the proof is the smoothing argument, in which the positive definite
distributions are approximated by positive definite functions, Bochner's theorem supplies a positive measure
for each, and the measures converge. Positive definite distributions form a closed convex cone, containing
the positive definite functions of polynomial growth as the locally integrable members, and the order of the
distribution is the polynomial growth rate of its spectral measure; a bounded continuous positive definite
function is exactly the case of a finite measure.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\varphi^{*}(x)=\overline{\varphi(-x)}$ | Convolution involution on test functions |
| $T^{*}(\varphi)=\overline{T(\varphi^{*})}$ | Adjoint involution on distributions |
| $\bar T$, value-conjugation | $\bar T(\varphi)=\overline{T(\bar\varphi)}$, distinct from $T^{*}$ |
| $\langle T,\varphi*\varphi^{*}\rangle\geq0$ | Positive definiteness of a distribution |
| $\hat\mu(x)=\int e^{-2\pi ix\cdot\xi}d\mu(\xi)$ | Transform of a measure |
| $\mu$ tempered | $\int(1+\lvert\xi\rvert)^{-N}d\mu<\infty$ for some $N$ |
| $T=\hat\mu$ | Bochner–Schwartz representation |

## Further Reading

- Laurent Schwartz, *Théorie des distributions* (Hermann, 1966), for the original form of the
  Bochner–Schwartz theorem.
- Israel M. Gelfand and Naum Ya. Vilenkin, *Generalized Functions, Vol. 4: Applications of Harmonic
  Analysis* (Academic Press, 1964), for positive definite distributions and their structure.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (2nd ed., Springer, 1990), for
  the distribution theory and the Fourier transform of tempered distributions.
- Walter Rudin, *Fourier Analysis on Groups* (Interscience, 1962), for the group form of Bochner's theorem
  and the positive definite functions.
- Ken-iti Sato, *Lévy Processes and Infinitely Divisible Distributions* (Cambridge University Press, 1999),
  for the probabilistic reading of the positive definite distributions and the Lévy–Khinchine formula.
- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton
  University Press, 1971), for the Fourier transform on the Schwartz class and the tempered distributions.
