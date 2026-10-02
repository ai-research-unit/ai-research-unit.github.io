
# __Convolution Operators__

## Introduction

A convolution operator is the integral operator whose kernel depends only on the difference of its
arguments. On $\mathbb R^n$ with the profile $k$ it is
$$
(T_kf)(x)=(k*f)(x)=\int_{\mathbb R^n}k(x-y)f(y)\,dy ,
$$
and its defining feature is invariance under translation: $T_k$ commutes with every shift of the
argument. That single invariance determines the operator's whole behaviour, because translation is
diagonalised by the Fourier transform, and a convolution operator is carried by that transform into
multiplication by a function — its **multiplier**. This article develops the operator and that
correspondence: the algebra of profiles, the multiplier it defines, and the boundedness of the operator,
which is read off from the profile by Young's inequality when the profile is integrable and from the
multiplier by Plancherel when it is not.

The prerequisites are *Measure Theory and Integration* for the convolution of integrable functions, the
$L^p$ spaces and Hölder's and Minkowski's inequalities, *Fourier Analysis on Euclidean Spaces* for the
transform $\hat f(\xi)=\int f(x)e^{-2\pi ix\cdot\xi}dx$, the convolution theorem, the Plancherel theorem,
the multiplier theorem of Mihlin and Hörmander, and the Hilbert and Riesz transforms, *Modes of
Convergence* for convergence in $L^p$, and *The Integral Operator*, the previous article of this group,
for the kernel form, the Hilbert–Schmidt class and compactness. Nothing beyond the transform on
$\mathbb R^n$ is assumed; the convolution algebra of a general locally compact abelian group, the measure
algebra and the characters are the subject of *Harmonic Analysis on Groups*, in the neighbouring category
*Analysis on Groups* of this Part, and of *Convolution on a Group*, later in that category, and are named
here as forward references only. The dual statements for $\mathbb Z$ and for the circle are recorded as
the discrete and periodic instances of the same theorems, in the terms available here. No article is about
an application: the operator is defined and bounded, and nothing is computed for its own sake.

## The Convolution Operator

### Definition and Elementary Properties

**Definition.** Let $k\in L^1(\mathbb R^n)$. The **convolution operator** with **profile** $k$ is
$T_kf=k*f$, where
$$
(k*f)(x)=\int_{\mathbb R^n}k(x-y)f(y)\,dy=\int_{\mathbb R^n}k(y)f(x-y)\,dy ,
$$
the two forms agreeing by the change of variable $y\mapsto x-y$.

**Proposition (the convolution operator is an integral operator).** $T_k$ is the integral operator
$T_K$ of *The Integral Operator* with kernel $K(x,y)=k(x-y)$, the kernel being measurable on
$\mathbb R^n\times\mathbb R^n$; and $T_k$ commutes with every translation. Writing
$(\tau_yf)(x)=f(x-y)$ for the translation by $y$ of *The Translation Operator*, later in this group, one
has $\tau_yT_k=T_k\tau_y$ for every $y$.

**Proof.** The kernel is the composition of the measurable map $(x,y)\mapsto x-y$ with $k$, so it is
measurable. For the commutation,
$$
(\tau_yT_kf)(x)=\int k(x-y-z)f(z)\,dz=\int k(x-w)f(w-y)\,dw=(T_k\tau_yf)(x)
$$
after the change of variable $w=y+z$, and by Fubini the two iterated integrals are equal for almost every
$x$. $\blacksquare$

**Theorem (the profile algebra).** Convolution is commutative and associative on $L^1(\mathbb R^n)$,
$$
k*l=l*k,\qquad (k*l)*m=k*(l*m),\qquad \lVert k*l\rVert_1\leq\lVert k\rVert_1\lVert l\rVert_1 ,
$$
so $L^1(\mathbb R^n)$ is a commutative Banach algebra under convolution; it has no identity, and the
operators compose by $T_kT_l=T_{k*l}=T_lT_k$.

**Proof.** Commutativity and associativity are the change of variable $z=x-y$ and Fubini–Tonelli;
the norm inequality is Fubini. The composition is the kernel product of *The Integral Operator*,
$(k*l)(x-y)=\int k(x-z)l(z-y)\,dz$. There is no identity: an identity $\delta$ would satisfy
$k*\delta=k$, and taking the Fourier transform below would give $\hat k\hat\delta=\hat k$ for every
$k\in L^1$ with $\hat k\not\equiv0$, so $\hat\delta\equiv1$, which is not the transform of an $L^1$
function; the point mass at $0$ has this property but is not an $L^1$ function. $\blacksquare$

**Example (approximate identities).** A sequence $\phi_m\in L^1$ with $\int\phi_m=1$, $\lVert\phi_m\rVert_1$
bounded and $\int_{\lvert x\rvert>\delta}\lvert\phi_m\rvert\to0$ for every $\delta>0$ satisfies
$T_{\phi_m}f=\phi_m*f\to f$ in $L^p$ for $1\leq p<\infty$ and at every Lebesgue point of $f$, by
*Fourier Analysis on Euclidean Spaces*; the family is an approximate identity for the algebra, though not
an identity.

### The Discrete and Periodic Instances

The same definitions hold with $\mathbb R^n$ replaced by a group whose operation is written additively.

**Example ($\mathbb Z$).** For a sequence $a=(a_n)\in\ell^1(\mathbb Z)$ the convolution operator on
$\ell^2(\mathbb Z)$ is
$$
(T_af)_n=(a*f)_n=\sum_{m\in\mathbb Z}a_{n-m}f_m ,
$$
and the **shift** $S$ with $(Sf)_n=f_{n-1}$ is the convolution operator with the sequence
$\delta_1=(0,1,0,\dots)$. The profiles form the Banach algebra $\ell^1(\mathbb Z)$ under convolution, with
$\lVert a*b\rVert_1\leq\lVert a\rVert_1\lVert b\rVert_1$.

**Example (the circle).** For $k\in L^1(\mathbb T)$ with $\mathbb T=\mathbb R/\mathbb Z$ the operator
$(T_kf)(x)=\int_{\mathbb T}k(x-y)f(y)\,dy$ acts on $L^2(\mathbb T)$, and its eigenfunctions are the
characters $e_m(x)=e^{2\pi imx}$ with eigenvalues the Fourier coefficients $\hat k(m)$.

The two examples are the cases $G=\mathbb Z$ and $G=\mathbb T$ of the convolution algebra $L^1(G)$ whose
general theory belongs to *Harmonic Analysis on Groups*, and they are recorded here because every theorem
below is proved in the same way for all three and because the discrete shift is the simplest operator
whose multiplier is not a function of a continuous variable.

## The Fourier Multiplier

### The Convolution Theorem and the Multiplier

**Theorem (the convolution theorem).** For $k,f\in L^1(\mathbb R^n)$ the transform of the convolution is
the product of the transforms,
$$
\widehat{(k*f)}(\xi)=\hat k(\xi)\hat f(\xi),
$$
with the normalisation $\hat f(\xi)=\int f(x)e^{-2\pi ix\cdot\xi}dx$ fixed by *Fourier Analysis on
Euclidean Spaces*.

**Proof.** By Fubini–Tonelli and the change of variable $z=x-y$, the double integral
$\iint k(y)f(x-y)e^{-2\pi ix\cdot\xi}dy\,dx$ equals
$\int k(y)e^{-2\pi iy\cdot\xi}dy\int f(z)e^{-2\pi iz\cdot\xi}dz$, and the two factors are
$\hat k(\xi)$ and $\hat f(\xi)$. $\blacksquare$

**Definition.** A **Fourier multiplier** is a function $m\in L^\infty(\mathbb R^n)$, and the
**multiplier operator** it defines is
$$
T_mf=\mathcal F^{-1}(m\hat f),
$$
where $\mathcal F$ is the Fourier transform as an operator on $L^2(\mathbb R^n)$ and $\mathcal F^{-1}$ its
inverse; the function $m$ is the **symbol** of $T_m$. For $k\in L^1$ the convolution theorem says that
$T_k=T_{\hat k}$ on the intersection $L^1\cap L^2$, and therefore on all of $L^2$: **the multiplier of a
convolution operator is the Fourier transform of its profile.**

### Boundedness on $L^2$

**Theorem.** For every $m\in L^\infty(\mathbb R^n)$ the multiplier operator $T_m$ is bounded on
$L^2(\mathbb R^n)$, with
$$
\lVert T_m\rVert_{L^2\to L^2}=\lVert m\rVert_\infty .
$$

**Proof.** By the Plancherel theorem $\mathcal F$ is a unitary operator of $L^2$, so $T_m$ is unitarily
equivalent to multiplication by $m$; and a multiplication operator $M_m$ on $L^2$ has norm
$\lVert m\rVert_\infty$, the estimate $\lVert M_mf\rVert_2\leq\lVert m\rVert_\infty\lVert f\rVert_2$ being
immediate and the reverse inequality following from the existence, for each $\epsilon>0$, of a set of
positive finite measure on which $\lvert m\rvert\geq\lVert m\rVert_\infty-\epsilon$. $\blacksquare$

**Corollary.** For $k\in L^1(\mathbb R^n)$ the convolution operator is bounded on $L^2$ with
$$
\lVert T_k\rVert_{L^2\to L^2}=\lVert\hat k\rVert_\infty\leq\lVert k\rVert_1 ,
$$
the equality being the theorem and the inequality the trivial bound $\lvert\hat k\rvert\leq\lVert k\rVert_1$;
the inequality is strict unless $\lvert\hat k\rvert=\lVert k\rVert_1$ almost everywhere, and the two
quantities agree for the Poisson kernel of the examples below.

## Boundedness on $L^p$

### Young's Inequality

**Theorem (Young).** For $1\leq p,q,r\leq\infty$ with $1+1/r=1/p+1/q$ and $k\in L^p$, $f\in L^q$,
$$
\lVert k*f\rVert_r\leq\lVert k\rVert_p\lVert f\rVert_q .
$$
In particular, for $k\in L^1$ the operator $T_k$ is bounded on every $L^p$, $1\leq p\leq\infty$, with
$\lVert T_k\rVert_{L^p\to L^p}\leq\lVert k\rVert_1$.

**Proof.** The case $p=1$, $q=r$ is Minkowski's integral inequality applied to
$\lvert k*f\rvert(x)\leq\int\lvert k(y)\rvert\lvert f(x-y)\rvert\,dy$; the case $q=1$ is the same by
commutativity of the convolution; and the general case follows from these two by the Riesz–Thorin
interpolation theorem of *Fourier Analysis on Euclidean Spaces*. $\blacksquare$

**Corollary (the profile-to-operator map).** The map $k\mapsto T_k$ is an injective algebra homomorphism
of the commutative Banach algebra $L^1(\mathbb R^n)$ into the algebra of bounded operators on $L^p$, for
each $p$; it is an isometry onto its image for $p=2$ exactly when $\lvert\hat k\rvert$ is constant, and it
is injective because $\hat k=0$ forces $k=0$ almost everywhere.

**Proof.** Linearity and multiplicativity are the profile algebra; the injectivity is the injectivity of
the Fourier transform on $L^1$, which follows from the inversion theorem of *Fourier Analysis on Euclidean
Spaces*. $\blacksquare$

### Multipliers Beyond $L^1$

The profiles form a small part of the bounded translation-invariant operators. The general statement is
the following, whose proof is the multiplier theorem of the Fourier article.

**Theorem (Mihlin–Hörmander).** Let $m\in C^k(\mathbb R^n\setminus\{0\})$ with
$\lvert\partial^\alpha m(\xi)\rvert\leq C_\alpha\lvert\xi\rvert^{-\lvert\alpha\rvert}$ for every
$\lvert\alpha\rvert\leq k>n/2$. Then $T_m$ is bounded on $L^p(\mathbb R^n)$ for every $1<p<\infty$, with
$\lVert T_m\rVert_{L^p\to L^p}\leq C_{p,n}\sup_{\lvert\alpha\rvert\leq k}C_\alpha$.

**Proof sketch.** This is proved in *Fourier Analysis on Euclidean Spaces* by decomposing $m$ into pieces
supported on dyadic annuli and realising each piece as convolution with an $L^1$ function of controlled
norm; the cancellation of the pieces away from the origin is what limits the result to $1<p<\infty$, and
the Hilbert and Riesz transforms show that the endpoint $p=1$ and $p=\infty$ fail in general.

The theorem shows that the convolution theorem is not the only source of multipliers: the Hilbert
transform has symbol $-i\operatorname{sgn}(\xi)$, which is not the Fourier transform of any $L^1$ function,
and it is bounded on $L^p$ for $1<p<\infty$ and of weak type $(1,1)$ but not bounded on $L^1$.

### Convolution Operators and Translation Invariance

**Theorem (the convolution operators are the translation-invariant ones, the $L^2$ case).** Let $A$ be a
bounded operator on $L^2(\mathbb R^n)$ commuting with every translation $\tau_y$,
$y\in\mathbb R^n$. Then $A=T_m$ for a unique $m\in L^\infty(\mathbb R^n)$, and
$\lVert A\rVert=\lVert m\rVert_\infty$. Conversely every $T_m$ is bounded and commutes with every
translation.

**Proof sketch.** Conjugating by the unitary $\mathcal F$, the translations become the multiplications by
the characters $e_\xi(y)=e^{-2\pi iy\cdot\xi}$, so $\mathcal FAA^{-1}$ commutes with $M_{e_\xi}$ for every
$\xi$. An operator $B$ on $L^2$ of a finite measure space commuting with $M_f$ for every
$f\in L^\infty$ is itself a multiplication operator: putting $g=B\mathbf 1$, for every bounded $f$ one
has $Bf=B M_f\mathbf 1=M_fB\mathbf 1=fg$, and the identity extends by density and continuity. The
characters generate $L^\infty(\mathbb R^n)$ in the strong operator topology — this is the abelian case of
the duality theory behind the Gelfand transform — so the hypothesis gives such a $B$ with
$B=M_m$, and $\tilde A=\mathcal F A\mathcal F^{-1}=M_m$ with $m\in L^\infty$. The uniqueness of $m$ and the
norm are the preceding theorem, and the converse is the definition. The $\sigma$-finite case is reduced to
the finite one by exhausting $\mathbb R^n$ with sets of finite measure. $\blacksquare$

**Remark (the $L^1$ case and the measure algebra).** A bounded operator on $L^1(\mathbb R^n)$ commuting
with all translations is convolution with a finite complex measure $\mu$, $T_\mu f=\mu*f$, and the finite
measures form the **measure algebra** $M(\mathbb R^n)$ under convolution, with
$L^1(\mathbb R^n)\subseteq M(\mathbb R^n)$ as the absolutely continuous measures. A general translation-
invariant operator on $L^2$ therefore has a symbol that is the Fourier–Stieltjes transform of a measure
only when the operator is convolution with a measure, and the multipliers that are not of this form — the
Hilbert transform among them — are the genuinely singular ones. The measure algebra, the convolution of
measures and the characters are the subject of *Harmonic Analysis on Groups* and *Convolution on a Group*,
and of *Locally Compact Groups and Haar Measure*, all in *Analysis on Groups*, the neighbouring category
of this Part.

## Examples

**Example (the heat semigroup).** The heat kernel of *Fourier Analysis on Euclidean Spaces*,
$K_t(x)=(4\pi t)^{-n/2}e^{-\lvert x\rvert^2/4t}$, lies in $L^1$ with $\lVert K_t\rVert_1=1$ and has
transform $\hat K_t(\xi)=e^{-4\pi^2t\lvert\xi\rvert^2}$. The operators $T_{K_t}$ are bounded on every
$L^p$ with norm at most $1$, act as $T_{K_t}f=K_t*f$, satisfy the semigroup law
$T_{K_t}T_{K_s}=T_{K_{t+s}}$ and have multipliers $e^{-4\pi^2t\lvert\xi\rvert^2}$; the limit as
$t\downarrow0$ is the identity on the profiles for which the approximation theorem applies, which is why
the family is an approximate identity and not an identity.

**Example (the Poisson kernel).** On $\mathbb R$ the function $P_t(x)=\frac1\pi\frac{t}{x^2+t^2}$
satisfies $P_t\in L^1$, $\lVert P_t\rVert_1=1$ and $\hat P_t(\xi)=e^{-2\pi t\lvert\xi\rvert}$; the operators
satisfy $T_{P_t}T_{P_s}=T_{P_{t+s}}$, so they form a semigroup of contractions on each $L^p$ whose
multipliers are $e^{-2\pi t\lvert\xi\rvert}$.

**Example (the Hilbert transform).** The Hilbert transform $H$ of *Fourier Analysis on Euclidean Spaces*
has kernel $1/(\pi x)$ taken as a principal value and multiplier $-i\operatorname{sgn}(\xi)$. It is
translation invariant and bounded on $L^2$ with norm $1$, but it is not a convolution operator with an
$L^1$ profile, since $1/(\pi x)$ is not integrable and the multiplier is not continuous at the origin.

## Compactness

**Remark.** No nonzero convolution operator on $L^2(\mathbb R^n)$ is compact. By the theorem above such an
operator is $T_m$ for a multiplier $m$; under the unitary $\mathcal F$ it is multiplication by $m$, and a
multiplication operator on the $L^2$ of a non-atomic space of infinite measure is compact only if its
symbol vanishes almost everywhere, as was proved in *The Integral Operator*. Equivalently, the kernel
$K(x,y)=k(x-y)$ of a convolution operator is never in $L^2(\mathbb R^n\times\mathbb R^n)$ unless it is
zero, since the measure of the product is infinite; and the Hilbert–Schmidt kernels that give compact
operators are exactly the kernels that are not translation invariant. The contrast is the reason the
spectral theory of a self-adjoint convolution operator has no discrete part beyond the symbol, and the
reason the integral equations of the previous article, whose kernels decay off the diagonal, behave
differently.

## Summary

A convolution operator on $\mathbb R^n$ is $T_kf=k*f$ with $k\in L^1$; it is the integral operator with
kernel $k(x-y)$ and it commutes with every translation. The profiles form the commutative Banach algebra
$L^1(\mathbb R^n)$ under convolution, with $\lVert k*l\rVert_1\leq\lVert k\rVert_1\lVert l\rVert_1$, no
identity and approximate identities; the operators compose as $T_kT_l=T_{k*l}$, and the same definitions
give the discrete convolution on $\ell^1(\mathbb Z)$ and the periodic convolution on $L^1(\mathbb T)$. The
Fourier transform carries a convolution operator into multiplication by its multiplier,
$\widehat{k*f}=\hat k\hat f$, so the multiplier of $T_k$ is $\hat k$; a general multiplier is any
$m\in L^\infty$, the operator $T_m=\mathcal F^{-1}(m\hat f)$ is bounded on $L^2$ with norm
$\lVert m\rVert_\infty$, and the convolution operators are exactly the bounded operators that commute with
all translations. On $L^p$ the profile gives boundedness by Young's inequality,
$\lVert k*f\rVert_r\leq\lVert k\rVert_p\lVert f\rVert_q$, in particular $\lVert T_k\rVert_{L^p\to L^p}\leq
\lVert k\rVert_1$; multipliers beyond those of $L^1$ profiles — the Hilbert and Riesz transforms among them
— are covered by the Mihlin–Hörmander theorem, which gives $L^p$ boundedness for a symbol with the
standard differentiability and size, and fails at the endpoints. Finally, no nonzero convolution operator
on $L^2(\mathbb R^n)$ is compact, compactness being the property of the kernels that are not translation
invariant.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k*l$ | Convolution of profiles, $(k*l)(x)=\int k(x-y)l(y)\,dy$ |
| $T_k$ | Convolution operator $T_kf=k*f$, the integral operator with kernel $k(x-y)$ |
| $m$ | Fourier multiplier, a bounded function, and the symbol of $T_m$ |
| $T_m$ | Multiplier operator $T_mf=\mathcal F^{-1}(m\hat f)$ |
| $\hat f$, $\mathcal F$ | Fourier transform and the unitary operator it defines on $L^2$ |
| $\tau_y$ | Translation, $(\tau_yf)(x)=f(x-y)$; $T_k\tau_y=\tau_yT_k$ |
| $\mathbb T$ | The circle $\mathbb R/\mathbb Z$ |
| $e_\xi$, $e_m$ | Characters, $e_\xi(x)=e^{2\pi ix\cdot\xi}$, $e_m(x)=e^{2\pi imx}$ |
| $K_t$, $P_t$ | Heat kernel and Poisson kernel |
| $H$ | Hilbert transform, symbol $-i\operatorname{sgn}\xi$ |

## Further Reading

- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton
  University Press, 1971), for the convolution theorem, the multipliers and the singular integrals.
- Elias M. Stein, *Singular Integrals and Differentiability Properties of Functions* (Princeton University
  Press, 1970), for the Mihlin–Hörmander multiplier theorem and the Hilbert and Riesz transforms.
- Walter Rudin, *Fourier Analysis on Groups* (Interscience, 1962), for the convolution algebra $L^1(G)$,
  the measure algebra and the characters on a locally compact abelian group.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953; reprinted Dover,
  2011), for $L^1(G)$ as a Banach algebra and the multiplier correspondence.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis, Vol. I and II* (Springer, 1963, 1970), for
  the convolution of measures and the Fourier–Stieltjes transform.
- Adriaan C. Zaanen, *Linear Analysis* (North-Holland, 1953), for Young's inequality and the convolution
  operators on $L^p$.
