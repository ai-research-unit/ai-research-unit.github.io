
# __The Integral Operator__

## Introduction

An integral operator is the map that averages a function against a weight in two variables. For a
measurable kernel $K$ on the product of two measure spaces it is
$$
(T_Kf)(x)=\int_YK(x,y)\,f(y)\,d\nu(y),
$$
and the equation $T_Kf=g$ is the *integral equation* of the second kind when the unknown appears also
outside the integral, $f-T_Kf=g$. The operator is the classical inverse of a differential operator: the
solution of a linear differential equation is written as an integral against a fundamental solution, and
the resolvent of a differential operator is, where it exists as an integral operator, an operator of this
form. This article develops the operator itself, with no hypothesis beyond the integral and the
$L^2$ inner product: the algebra its kernels carry, its boundedness on $L^2$ under the three hypotheses
that supply it, the Hilbert–Schmidt case in which the kernel is square-integrable, and the compactness
that the square-integrable case yields.

The prerequisites are *Measure Theory and Integration* for the Lebesgue integral, the $L^p$ spaces, the
Cauchy–Schwarz and Hölder inequalities and the Fubini–Tonelli theorem, and *Modes of Convergence* for
convergence in $L^p$. The $L^2$ inner product is the one of that article, $\langle f,g\rangle=\int f\bar g$,
linear in the first argument and conjugate-linear in the second. Nothing here uses the general theory of
operators on a Hilbert space beyond the inner product and Cauchy–Schwarz: the boundedness, the
Hilbert–Schmidt norm and the compactness are all proved concretely from the integral. The operator norm,
the adjoint of a bounded operator, the spectral theorem, the Fredholm alternative and the general theory
of compact operators are the subject of *Banach and Hilbert Spaces* and of *Compact Operators*, later in
this Part; the theorem that *every* continuous operator on test functions is an integral operator with a
distribution kernel is *The Schwartz Kernel Theorem*, later in this Part, and no such representation is
claimed here for a kernel that fails the integrability hypotheses below. The kernel of the adjoint and the
Hermitian and positive definite kernels are the subject of the `*` group of this category; the
translation-invariant kernel, which defines a convolution operator, is *Convolution Operators*, the next
article of this group, and is only an example here.

## The Operator and Its Kernel

### Definition

**Definition.** Let $(X,\mathcal A,\mu)$ and $(Y,\mathcal B,\nu)$ be $\sigma$-finite measure spaces,
$\mathbb K=\mathbb R$ or $\mathbb C$, and let $K:X\times Y\to\mathbb K$ be measurable for
$\mathcal A\otimes\mathcal B$. The **integral operator with kernel $K$** is
$$
(T_Kf)(x)=\int_YK(x,y)f(y)\,d\nu(y),
$$
defined for those $f\in L^2(Y,\nu)$ for which the integral converges for $\mu$-almost every $x$, and
$T_Kf$ is then defined as a class in $L^2(X,\mu)$ wherever it lies in $L^2$. The function $K$ is the
**kernel**, and when $X=Y$ and $\mu=\nu$ the kernel is a kernel **on** $X$. When the two variables of the
kernel must be told apart, the first is the variable of the image and the second the variable of the
source, so that $K(x,y)$ multiplies the value of $f$ at $y$ and the result is read at $x$.

Two kernels agreeing $\mu\otimes\nu$-almost everywhere define the same operator on the functions for which
both integrals converge, and this is the only ambiguity; the article works with kernels as functions and
records the equality almost everywhere where it matters. The definitions are arranged so that the
Hilbert–Schmidt hypothesis $K\in L^2(X\times Y,\mu\otimes\nu)$ below makes $T_K$ a bounded operator
defined on all of $L^2(Y,\nu)$.

### The Algebra of Kernels

**Theorem (composition of integral operators).** Let $K\in L^2(X\times Z,\mu\otimes\lambda)$ and
$L\in L^2(Z\times Y,\lambda\otimes\nu)$. Then the function
$$
(K\star L)(x,y)=\int_ZK(x,z)L(z,y)\,d\lambda(z)
$$
is defined for almost every $(x,y)$, lies in $L^2(X\times Y,\mu\otimes\nu)$, and satisfies
$T_KT_L=T_{K\star L}$.

**Proof.** For almost every $(x,y)$ the integrand is the product of the two functions
$z\mapsto K(x,z)$ and $z\mapsto L(z,y)$, which lie in $L^2(Z,\lambda)$ for almost every $x$ and almost
every $y$ respectively; Cauchy–Schwarz gives
$$
\int_Z\lvert K(x,z)L(z,y)\rvert\,d\lambda(z)
\le\Bigl(\int_Z\lvert K(x,z)\rvert^2d\lambda(z)\Bigr)^{1/2}
\Bigl(\int_Z\lvert L(z,y)\rvert^2d\lambda(z)\Bigr)^{1/2},
$$
so $(K\star L)(x,y)$ is defined and finite almost everywhere and measurable. Integrating its square and
applying Cauchy–Schwarz once more, then Tonelli,
$$
\iint_{X\times Y}\lvert(K\star L)(x,y)\rvert^2dx\,dy
\le\iint_{X\times Y}\Bigl(\int_Z\lvert K(x,z)\rvert^2dz\Bigr)
\Bigl(\int_Z\lvert L(z,y)\rvert^2dz\Bigr)dx\,dy
=\lVert K\rVert_2^2\,\lVert L\rVert_2^2 ,
$$
which is finite; hence $K\star L\in L^2(X\times Y)$. For the equality of operators, let $f\in L^2(Y,\nu)$
and compute formally and then justify by Fubini–Tonelli applied to the absolutely convergent triple
integral, which the estimate above bounds:
$$
(T_KT_Lf)(x)=\int_ZK(x,z)\Bigl(\int_YL(z,y)f(y)\,d\nu(y)\Bigr)d\lambda(z)
=\int_Y\Bigl(\int_ZK(x,z)L(z,y)\,d\lambda(z)\Bigr)f(y)\,d\nu(y)=(T_{K\star L}f)(x). \qquad\blacksquare
$$

**Proposition (the kernel product is associative).** For kernels
$K\in L^2(X\times W)$, $L\in L^2(W\times Z)$ and $M\in L^2(Z\times Y)$ one has
$(K\star L)\star M=K\star(L\star M)$ almost everywhere. The product is bilinear, and the square-integrable
kernels on $X$ form an associative algebra under $\star$ with the kernel
$K_0(x,y)$ of the identity of the algebra acting as unit wherever such a kernel exists.

**Proof.** Both sides are the triple integral $\iiint K(x,w)L(w,z)M(z,y)\,dw\,dz$ over the product, which
is finite almost everywhere by two applications of Cauchy–Schwarz and is symmetric in the bracketing by
Fubini–Tonelli. Bilinearity is linearity of the integral. $\blacksquare$

### Examples

**Example (rank-one kernels).** For $u\in L^2(X,\mu)$ and $v\in L^2(Y,\nu)$ put
$K(x,y)=u(x)\overline{v(y)}$. Then
$$
(T_Kf)(x)=u(x)\int_Y\overline{v(y)}f(y)\,d\nu(y)=u(x)\,\langle f,v\rangle ,
$$
so $T_K$ has rank at most one, its image being the span of $u$; it has rank exactly one when $u$ and $v$
are both nonzero.

**Example (the finite-dimensional case).** For $X=\{1,\dots,m\}$ and $Y=\{1,\dots,n\}$ with counting
measure, every measurable kernel is a matrix $K=(K_{ij})$ and $T_K$ is multiplication by that matrix; the
composition $K\star L$ is the matrix product, and the Hilbert–Schmidt norm below is the Euclidean norm of
the matrix entries. The general theory is thus the infinite-dimensional extension of the algebra of
matrices acting on column vectors.

**Example (the Volterra kernel).** On $X=Y=\mathbb R$ with Lebesgue measure, $K(x,y)=\mathbf 1_{\{x>y\}}$
gives $(T_Kf)(x)=\int_{-\infty}^xf(y)\,dy$, the indefinite integral; the operator is not translation
invariant and is a standard example of a quasinilpotent operator, the spectral theory beyond the present
Article.

**Example (the translation-invariant kernel).** On $X=Y=\mathbb R^n$ with Lebesgue measure, a kernel of
the form $K(x,y)=k(x-y)$ with $k\in L^1(\mathbb R^n)$ gives
$(T_Kf)(x)=\int k(x-y)f(y)\,dy=(k*f)(x)$, a **convolution operator**. These are the kernels whose
operators commute with all translations, and they are the subject of *Convolution Operators*, the next
article of this group.

## Boundedness on $L^2$

### The Square-Integrable Kernel

**Theorem (the Hilbert–Schmidt bound).** If $K\in L^2(X\times Y,\mu\otimes\nu)$, then $T_K$ maps
$L^2(Y,\nu)$ boundedly into $L^2(X,\mu)$, with
$$
\lVert T_K\rVert\leq\lVert K\rVert_{L^2(X\times Y)},
\qquad
\lVert K\rVert_{L^2(X\times Y)}^2=\iint_{X\times Y}\lvert K(x,y)\rvert^2d\mu(x)\,d\nu(y).
$$

**Proof.** For $f\in L^2(Y,\nu)$ and almost every $x$ the function $y\mapsto K(x,y)$ lies in $L^2(Y,\nu)$
by Tonelli, so Cauchy–Schwarz gives $\lvert(T_Kf)(x)\rvert^2\le\lVert K(x,\cdot)\rVert_2^2\lVert f\rVert_2^2$
and hence, after integrating in $x$ and applying Tonelli,
$$
\lVert T_Kf\rVert_2^2
\le\int_X\lVert K(x,\cdot)\rVert_2^2\,d\mu(x)\,\lVert f\rVert_2^2
=\lVert K\rVert_{L^2(X\times Y)}^2\lVert f\rVert_2^2 .
$$
The operator is linear and defined on all of $L^2(Y,\nu)$ by this estimate, so it is bounded with the
stated bound. $\blacksquare$

The inequality is the reason the square-integrable kernels are the class the corpus works with: the
operator norm is controlled by a double integral, and every kernel that satisfies $\lVert K\rVert_2<\infty$
defines a bounded operator with no further hypothesis.

### The Schur Test

**Theorem (Schur test).** Let $X=Y$ and let $K\ge0$ be a measurable kernel for which there is $C\ge0$ with
$$
\int_XK(x,y)\,d\mu(y)\leq C\ \text{for almost every }x,
\qquad
\int_XK(x,y)\,d\mu(x)\leq C\ \text{for almost every }y .
$$
Then $T_K$ maps $L^p(\mu)$ boundedly into itself for every $1\leq p\leq\infty$, with
$\lVert T_K\rVert_{L^p\to L^p}\leq C$.

**Proof.** The case $p=1$ is Fubini and the case $p=\infty$ is the first hypothesis. For $1<p<\infty$ put
$q=p/(p-1)$ and write $K\lvert f\rvert=K^{1/q}\cdot K^{1/p}\lvert f\rvert$; Hölder gives
$$
\lvert(T_Kf)(x)\rvert\leq\Bigl(\int_XK(x,y)\,d\mu(y)\Bigr)^{1/q}
\Bigl(\int_XK(x,y)\lvert f(y)\rvert^p\,d\mu(y)\Bigr)^{1/p}
\leq C^{1/q}\Bigl(\int_XK(x,y)\lvert f(y)\rvert^p\,d\mu(y)\Bigr)^{1/p}.
$$
Raising to the $p$-th power and integrating in $x$, then applying Tonelli and the second hypothesis,
$$
\lVert T_Kf\rVert_p^p\leq C^{p/q}\int_X\int_XK(x,y)\lvert f(y)\rvert^p\,d\mu(y)\,d\mu(x)
\leq C^{p/q}\,C\lVert f\rVert_p^p=C^p\lVert f\rVert_p^p ,
$$
since $p/q+1=p$. $\blacksquare$

**Remark.** The test also holds with two weights: if $p_0,q_0>0$ are measurable and
$\int_XK(x,y)q_0(y)\,dy\leq Cp_0(x)$, $\int_XK(x,y)p_0(x)\,dx\leq Cq_0(y)$ almost everywhere, then $T_K$ is
bounded on the weighted space $L^p(p_0^p\,d\mu)$ with the same constant. The unweighted statement is the
one used in this corpus, and the weighted one is recorded because the kernel of a Riemann–Liouville
fractional integral satisfies it.

### Kernels in $L^1$ and the Young Bound

**Theorem (Young).** Let $K(x,y)=k(x-y)$ on $\mathbb R^n$ with $k\in L^1(\mathbb R^n)$. Then for
$1\leq p\leq\infty$,
$$
\lVert T_Kf\rVert_p=\lVert k*f\rVert_p\leq\lVert k\rVert_1\lVert f\rVert_p .
$$

**Proof.** For $p=1$ the inequality is Fubini, $p=\infty$ the trivial bound, and for $1<p<\infty$ it is
Minkowski's integral inequality applied to
$\lvert k*f\rvert(x)\leq\int\lvert k(y)\rvert\lvert f(x-y)\rvert\,dy$. $\blacksquare$

The Young bound is the reason a kernel that decays like an integrable function gives a bounded operator
even when it is not square-integrable: $k$ may be the Poisson kernel, which lies in $L^1$ and not in $L^2$.
The two hypotheses of this section overlap and neither contains the other; the square-integrable case is
the one that gives compactness below, and the $L^1$ case need not.

## The Hilbert–Schmidt Case

### The Hilbert–Schmidt Norm

**Definition.** An integral operator $T_K$ is **Hilbert–Schmidt** if
$K\in L^2(X\times Y,\mu\otimes\nu)$, and its **Hilbert–Schmidt norm** is
$$
\lVert T_K\rVert_{\mathrm{HS}}=\lVert K\rVert_{L^2(X\times Y)}
=\Bigl(\iint_{X\times Y}\lvert K(x,y)\rvert^2\,d\mu(x)\,d\nu(y)\Bigr)^{1/2}.
$$
The operator is of **finite rank** if its image is finite-dimensional, and **of rank one** if the image is
one-dimensional.

By the Hilbert–Schmidt bound, $\lVert T_K\rVert_{\mathrm{op}}\leq\lVert T_K\rVert_{\mathrm{HS}}$, so the
Hilbert–Schmidt norm dominates the operator norm; the two are not equal in general, and the inequality is
strict for a rank-one kernel whose factor has norm one, where $\lVert T_K\rVert_{\mathrm{op}}=1$ while
$\lVert T_K\rVert_{\mathrm{HS}}$ is the product of the two factor norms and may be larger.

**Theorem (the Hilbert–Schmidt norm is basis independent).** Let $(X,\mu)$ and $(Y,\nu)$ be separable
measure spaces, with orthonormal bases $\{e_i\}$ of $L^2(X,\mu)$ and $\{f_j\}$ of $L^2(Y,\nu)$. Then
$$
\lVert T_K\rVert_{\mathrm{HS}}^2=\sum_{i,j}\lvert\langle T_Kf_j,e_i\rangle\rvert^2 ,
$$
the series converging and the value not depending on the two bases.

**Proof.** The functions $e_i(x)\overline{f_j(y)}$ form an orthonormal basis of
$L^2(X\times Y,\mu\otimes\nu)$, and the identity
$$
\langle K,e_i\otimes\overline{f_j}\rangle
=\iint K(x,y)\overline{e_i(x)}\,f_j(y)\,d\mu(x)\,d\nu(y)=\langle T_Kf_j,e_i\rangle
$$
holds by Fubini–Tonelli, the integrand being summable. Parseval's identity in $L^2(X\times Y)$ gives the
statement, and the basis-independence is the basis-independence of the Parseval sum. $\blacksquare$

### The Ideal Property

**Theorem.** Let $K\in L^2(X\times Z)$ and $L\in L^2(Z\times Y)$. Then $K\star L\in L^2(X\times Y)$ and
$$
\lVert K\star L\rVert_{\mathrm{HS}}\leq\lVert K\rVert_{\mathrm{HS}}\,\lVert L\rVert_{\mathrm{HS}} .
$$
Consequently the Hilbert–Schmidt operators are closed under composition and under multiplication on either
side by an integral operator, and the composition of two Hilbert–Schmidt operators is Hilbert–Schmidt.

**Proof.** The first two statements are the composition theorem of the first section together with the
estimate $\lVert K\star L\rVert_2\leq\lVert K\rVert_2\lVert L\rVert_2$ proved there. $\blacksquare$

**Remark.** The Hilbert–Schmidt operators form a two-sided ideal of the algebra of bounded operators on
$L^2$, and this is where the general theory begins; the concrete statement above is all that the corpus
uses before *Banach and Hilbert Spaces*, later in this Part, where the ideal is placed in the algebra
$B(L^2)$ and the trace-class operators are introduced.

## Compactness

### Compactness

**Definition.** A bounded operator $T:L^2(X,\mu)\to L^2(X,\mu)$ is **compact** if the closure of the image
of the closed unit ball is compact, equivalently if every bounded sequence $(f_n)$ has a subsequence whose
images $Tf_n$ converge; if the image has finite dimension the operator is of finite rank and compact. The
definition and its consequences — the spectral theory of a compact operator, the Fredholm alternative —
are the subject of *Compact Operators* and *Banach and Hilbert Spaces*, later in this Part; the property
is used here only in the concrete case proved below.

### Finite-Rank Approximation

**Theorem (square-integrable kernels are compact).** Let $(X,\mu)$ and $(Y,\nu)$ be separable measure
spaces with orthonormal bases $\{e_i\}$ and $\{f_j\}$ and let $K\in L^2(X\times Y)$. For $N\geq1$ put
$$
K_N(x,y)=\sum_{i,j\leq N}\langle T_Kf_j,e_i\rangle\,e_i(x)\overline{f_j(y)} .
$$
Then each $T_{K_N}$ has finite rank at most $N^2$, the kernels converge, $\lVert K-K_N\rVert_2\to0$, and
consequently $\lVert T_K-T_{K_N}\rVert_{\mathrm{op}}\to0$. Hence $T_K$ is compact.

**Proof.** Each $K_N$ is a finite sum of rank-one kernels $e_i\otimes\overline{f_j}$, so $T_{K_N}$ has
finite rank; the convergence $\lVert K-K_N\rVert_2\to0$ is Parseval's identity in the orthonormal basis
$\{e_i\otimes\overline{f_j}\}$, and the operator-norm convergence follows from the Hilbert–Schmidt bound
applied to $K-K_N$. It remains to see that a norm limit of finite-rank operators is compact. Let $S_n$ be
finite rank with $\lVert S-S_n\rVert\to0$. Given a bounded sequence $f_m$ with $\lVert f_m\rVert\leq1$,
extract by the compactness of $S_1$ a subsequence on which $S_1f_m$ converges, then a further subsequence
on which $S_2f_m$ converges, and so on diagonally, obtaining a subsequence on which $S_nf_m$ converges for
every $n$. On that subsequence
$$
\lVert Sf_m-Sf_{m'}\rVert\leq\lVert S-S_n\rVert\lVert f_m-f_{m'}\rVert+\lVert S_nf_m-S_nf_{m'}\rVert
\leq2\lVert S-S_n\rVert+\lVert S_nf_m-S_nf_{m'}\rVert ,
$$
and choosing $n$ first and then $m,m'$ large makes both terms small. Hence $Sf_m$ is Cauchy, and the
diagonal subsequence converges; $S$ is compact. $\blacksquare$

**Corollary.** Every Hilbert–Schmidt integral operator is compact, and so is every finite-rank operator.
The Hilbert–Schmidt norm is not the operator norm: the family $K_N$ converges to $K$ in the
Hilbert–Schmidt norm and therefore in the operator norm, and the limit is compact although a general
bounded operator need not be.

**Remark (what compactness does not follow from).** The Young bound of the previous section gives a
bounded operator for every $k\in L^1(\mathbb R^n)$, and such an operator is never compact unless it is
zero. A translation-invariant operator on $L^2(\mathbb R^n)$ is unitarily equivalent to multiplication by
its multiplier, and a multiplication operator by a function $m$ on $L^2$ of a non-atomic space of infinite
measure is compact exactly when $m=0$ almost everywhere: if $\lvert m\rvert\geq c>0$ on a set of positive
finite measure then the restriction to the $L^2$ of that set is bounded below by $c$, so its unit ball
would be relatively compact only if that space had finite dimension. Hence a nonzero convolution operator
on $L^2(\mathbb R^n)$ is not compact, and compactness is a property of the kernels that are not
translation invariant. The criterion is developed with the convolution operators themselves in
*Convolution Operators*, and in general in *Compact Operators*, later in this Part.

### The Integral Equation

The interest of compactness is that it makes the integral equation solvable. If $K\in L^2(X\times X)$,
then $T_K$ is compact, and the equation $f-T_Kf=g$, with $g\in L^2$, falls under the **Fredholm
alternative**: either $f-T_Kf=g$ has a unique solution for every $g$, or the homogeneous equation
$f-T_Kf=0$ has a nonzero finite-dimensional solution space, and in the second case the equation is
solvable exactly for those $g$ orthogonal to the solutions of the homogeneous adjoint equation. The
adjoint kernel that enters the second alternative is the subject of *The Adjoint of an Integral Operator*,
later in this category; the alternative itself is stated and proved in *Compact Operators*, later in this
Part, and the present Article supplies only the compactness on which it rests.

## Summary

An integral operator $T_K$ with kernel $K$ on the product of two $\sigma$-finite measure spaces is the map
$f\mapsto\int K(x,\cdot)f$, linear and defined on all of $L^2$ once $K$ is square-integrable. The kernels
compose by $(K\star L)(x,y)=\int K(x,z)L(z,y)\,dz$, the product is associative and bilinear, and
$T_KT_L=T_{K\star L}$; the finite-dimensional instance is matrix multiplication, and a kernel of the form
$k(x-y)$ gives a convolution operator.

The operator is bounded on $L^2$ with $\lVert T_K\rVert\leq\lVert K\rVert_{L^2(X\times Y)}$ whenever the
kernel is square-integrable, by Cauchy–Schwarz and Tonelli; it is bounded on every $L^p$ with
$\lVert T_K\rVert\leq C$ whenever a nonnegative kernel has row and column integrals bounded by $C$, by the
Schur test; and it is bounded on every $L^p$ with $\lVert T_K\rVert\leq\lVert k\rVert_1$ when the kernel is
translation invariant with an integrable profile, by Young's inequality. The Hilbert–Schmidt operators are
the square-integrable kernels, with norm $\lVert T_K\rVert_{\mathrm{HS}}=\lVert K\rVert_2$ dominating the
operator norm, basis-independent and multiplicative under composition; they are the ideal of the bounded
operators that this article reaches without the general theory. A square-integrable kernel is the
$L^2$-limit of its finite-rank truncations and the operator the operator-norm limit of finite-rank
operators, hence compact; and compactness is exactly what makes the integral equation $f-T_Kf=g$ amenable
to the Fredholm alternative.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(X,\mathcal A,\mu)$, $(Y,\mathcal B,\nu)$ | $\sigma$-finite measure spaces, source and image |
| $K(x,y)$ | The kernel; first variable of the image, second of the source |
| $T_K$ | The integral operator, $(T_Kf)(x)=\int_YK(x,y)f(y)\,d\nu(y)$ |
| $K\star L$ | Kernel product $(K\star L)(x,y)=\int_ZK(x,z)L(z,y)\,dz$, with $T_{K\star L}=T_KT_L$ |
| $\lVert K\rVert_2$ | $L^2(X\times Y)$ norm of the kernel |
| $\lVert T_K\rVert$ | Operator norm on $L^2$ |
| $\lVert T_K\rVert_{\mathrm{HS}}=\lVert K\rVert_2$ | Hilbert–Schmidt norm |
| $C$ | Schur constant, bounding the row and column integrals |
| $k$ | Profile of a translation-invariant kernel $K(x,y)=k(x-y)$ |
| compact | Image of the closed unit ball relatively compact |

## Further Reading

- Frigyes Riesz and Béla Sz.-Nagy, *Functional Analysis* (Dover, 1955), for the integral operator, the
  Schur test and the classical integral equations.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II: Spectral Theory* (Interscience, 1963),
  for the Hilbert–Schmidt and compact operators and their ideals.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic
  Press, 1980), for the compactness of integral operators and the Fredholm alternative.
- Israel Gohberg, Seymour Goldberg and Marinus A. Kaashoek, *Classes of Linear Operators, Vol. I*
  (Birkhäuser, 1990), for the algebra of kernels and the Schatten classes.
- Adriaan C. Zaanen, *Linear Analysis* (North-Holland, 1953), for the Schur test and the boundedness of
  integral operators on $L^p$.
- Gerald B. Folland, *Real Analysis: Modern Techniques and Their Applications* (2nd ed., Wiley, 1999), for
  the integral operator with a square-integrable kernel as an example in Hilbert space.
