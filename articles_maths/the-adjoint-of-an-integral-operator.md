
# __The Adjoint of an Integral Operator__

## Introduction

The adjoint of an operator is the operator that moves the operator to the other side of the pairing, and for
an integral operator it is again an integral operator, whose kernel is the conjugate transpose of the
original one. If the pairing is the Hilbert pairing $\langle f,g\rangle=\int f\bar g$, then
$$
T_K^\dagger=T_{K^*},\qquad K^*(x,y)=\overline{K(y,x)} ,
$$
and the operator $T_K$ is self-adjoint exactly when its kernel is Hermitian. The passage
$T\mapsto T^\dagger$ is the involution on the operators, the archetype of the `* Operator Theory` group:
it is conjugate-linear, involutive, an isometric anti-automorphism of the operator algebra, and it carries
the element involution $K\mapsto K^*$ of the kernel to the operator adjoint. This article derives that
correspondence, distinguishes the two adjoints of an integral operator — the Hilbert adjoint, taken with
respect to the sesquilinear pairing, and the transpose, taken with respect to the bilinear pairing — and
identifies the Hermitian case.

The article is the first of the `* Operator Theory` group of *Foundations of Analysis*. Its prerequisites
are *The Integral Operator*, the first article of this category, for the integral operator and the kernel;
*Banach and Hilbert Spaces*, later in this Part, for the adjoint of a bounded operator, its uniqueness and
its algebraic properties, quoted as established; *Conventions in Mathematics* for the marks, where the
**dagger** is the adjoint of an operator and the **star** the involution of an element; and *Hermitian
Kernels and the Integral Operator*, the last article of the `* Theory` group, for the kernel involution and
the dictionary of the two conditions. The spectral theory that the Hermitian case supports is *Hermitian
Integral Kernels*, the next article; the general adjoint of a bounded operator, with domain considerations
for the unbounded case, is *The Adjoint of a Bounded Operator* and the later unbounded-operator material,
both later in this Part; the distributional kernel is *The Schwartz Kernel Theorem*, later in this Part. No
geometry is invoked.

## The Pairing and the Adjoint

### The Pairing

Throughout, $X$ is a measure space with a $\sigma$-finite measure $\mu$, and $L^2=L^2(X,\mu)$ carries the
**Hilbert pairing**
$$
\langle f,g\rangle=\int_Xf\bar g\,d\mu ,
$$
conjugate-linear in the second slot and linear in the first. The **bilinear pairing** is
$$
\{f,g\}=\int_Xfg\,d\mu ,
$$
with no conjugation, defined for the pairs for which the integral converges. The two pairings differ by the
conjugate on the second slot, and they produce two different adjoints of the same operator.

### The Adjoint of a Bounded Operator

**Definition.** For a bounded operator $T:L^2\to L^2$, the **adjoint** $T^\dagger$ is the unique bounded
operator with
$$
\langle Tf,g\rangle=\langle f,T^\dagger g\rangle\qquad\text{for all }f,g\in L^2 ;
$$
it exists by the Riesz representation theorem, and it is characterised by those identities.

**Theorem (properties of the adjoint).** The map $T\mapsto T^\dagger$ is conjugate-linear and involutive,
$$
(T+S)^\dagger=T^\dagger+S^\dagger,\qquad
(\lambda T)^\dagger=\bar\lambda T^\dagger,\qquad
T^{\dagger\dagger}=T ,
$$
it reverses products,
$$
(ST)^\dagger=S^\dagger T^\dagger ,
$$
and it is isometric, $\lVert T^\dagger\rVert=\lVert T\rVert$. Consequently $T$ is **self-adjoint** if
$T^\dagger=T$, **unitary** if $T^\dagger T=TT^\dagger=\mathrm{id}$, and **normal** if
$TT^\dagger=T^\dagger T$.

**Proof.** The properties are those of the adjoint of a bounded operator in *Banach and Hilbert Spaces*,
later in this Part, and are quoted from there; the anti-multiplicativity is the computation
$\langle STf,g\rangle=\langle Tf,S^\dagger g\rangle=\langle f,T^\dagger S^\dagger g\rangle$, and the
isometry is $\lVert T^\dagger\rVert=\sup_{\lVert g\rVert=1}\sup_{\lVert f\rVert=1}\lvert\langle Tf,g\rangle\rvert=\lVert T\rVert$.
$\blacksquare$

**Remark (the marks).** By *Conventions in Mathematics* the **dagger** names the adjoint of an operator and
the **star** names the involution of an element, the layer of the `* Theory` group. The two are distinct
structures, and the identity $T_K^\dagger=T_{K^*}$ below is the statement that, for integral operators, the
element involution $K\mapsto K^*$ produces the operator adjoint $T\mapsto T^\dagger$; that agreement is
proved, never assumed.

### The Transpose and the Adjoint

**Definition.** With respect to the bilinear pairing, the **transpose** of a bounded operator $T$ is the
operator $T^{\mathrm t}$ with
$$
\{Tf,g\}=\{f,T^{\mathrm t}g\}\qquad\text{for all }f,g ,
$$
when it exists. For an integral operator the transpose has the transposed kernel, while the Hilbert adjoint
has the conjugate transposed kernel; the two coincide exactly for real kernels.

**Theorem.** Let $T_K$ be bounded with kernel $K$. Then provided the interchanges below are legitimate,
$$
T_K^{\mathrm t}=T_{K^{\mathrm t}},\quad K^{\mathrm t}(x,y)=K(y,x),
\qquad
T_K^\dagger=T_{K^*},\quad K^*(x,y)=\overline{K(y,x)} ,
$$
so that the transpose, the adjoint and the conjugate are related by
$K^*=\overline{K^{\mathrm t}}$ and $T_K^\dagger=\overline{T_K^{\mathrm t}}$.

**Proof.** For the transpose,
$$
\{T_Kf,g\}=\iint K(x,y)f(y)g(x)\,d\mu(y)d\mu(x)
=\int f(y)\Bigl(\int K(x,y)g(x)\,d\mu(x)\Bigr)d\mu(y)=\{f,T_{K^{\mathrm t}}g\} ,
$$
the middle integral being $(T_{K^{\mathrm t}}g)(y)$ with the kernel $K(y,x)$; the Hilbert case replaces $g$ by
$\bar g$ throughout and produces $\overline{K(y,x)}$. The two differ by the conjugation on the second slot,
which is exactly the relation $K^*=\overline{K^{\mathrm t}}$. $\blacksquare$

## The Adjoint of an Integral Operator

### The Kernel of the Adjoint

**Theorem (the adjoint kernel).** Let $K\in L^2(X\times X)$ and let $T_K$ be the integral operator of $K$,
bounded on $L^2$. Then
$$
T_K^\dagger=T_{K^*},\qquad K^*(x,y)=\overline{K(y,x)} ,
$$
and $T_{K^*}$ is the integral operator of the conjugate transpose kernel, which lies in $L^2(X\times X)$ with
the same norm, $\lVert K^*\rVert_{L^2}=\lVert K\rVert_{L^2}$.

**Proof.** By Fubini and the definition of the pairing,
$$
\langle T_Kf,g\rangle=\iint K(x,y)f(y)\overline{g(x)}\,d\mu(y)d\mu(x)
=\iint f(y)\overline{\Bigl(\int\overline{K(x,y)}g(x)\,d\mu(x)\Bigr)}\,d\mu(y)
=\langle f,T_{K^*}g\rangle ,
$$
and the inner integral is $(T_{K^*}g)(y)$ with $K^*(y,x)=\overline{K(x,y)}$, that is
$K^*(x,y)=\overline{K(y,x)}$. The uniqueness of the adjoint identifies $T_K^\dagger$ with $T_{K^*}$, and the
norm identity is the substitution $x\leftrightarrow y$. $\blacksquare$

**Corollary (the Hermitian case).** The following are equivalent: $T_K$ is self-adjoint; $K^*=K$, that is
$K(y,x)=\overline{K(x,y)}$ for almost every $(x,y)$; and the sesquilinear form
$(f,g)\mapsto\langle T_Kf,g\rangle$ is Hermitian, $\langle T_Kf,g\rangle=\overline{\langle T_Kg,f\rangle}$.
In particular a real kernel is self-adjoint exactly when it is symmetric, $K(y,x)=K(x,y)$.

**Proof.** The first two are equivalent by the theorem and the uniqueness of the kernel of a Hilbert–Schmidt
operator; the Hermitian property of the form is the polarisation of self-adjointness and is the kernel form
of the Hermitian condition, as in the `* Theory` article. For a real kernel, $\overline{K(x,y)}=K(x,y)$, so
$K^*=K$ is $K(y,x)=K(x,y)$. $\blacksquare$

### The Involution on the Operators

**Theorem.** The map $T\mapsto T^\dagger$ restricted to the integral operators is the conjugate transport of
the kernel involution: on the class of integral operators with $L^2$ kernels,
$$
T_K^\dagger=T_{K^*},\qquad
(T_KT_L)^\dagger=T_L^\dagger T_K^\dagger,\qquad
(T_K^\dagger)^\dagger=T_K ,
$$
and it is an isometry of the Hilbert–Schmidt class onto itself.

**Proof.** The first identity is the theorem above; the anti-multiplicativity is the property of the adjoint
of a bounded operator, read on the kernels through the correspondence
$\langle T_K,T_L\rangle_{\mathrm{HS}}=\iint K\bar L$ of the `* Theory` article; the involution property
$T^{\dagger\dagger}=T$ and the isometry are the same properties transported. $\blacksquare$

**Example (the Volterra operator).** The Volterra operator $Vf(x)=\int_0^xf(y)\,dy$ has the kernel
$K(x,y)=\mathbf 1_{0\leq y\leq x}$, and its adjoint has the kernel
$K^*(x,y)=\mathbf 1_{0\leq x\leq y}$, so that
$$
(V^\dagger f)(x)=\int_x^1f(y)\,dy .
$$
The operator is not self-adjoint, and $V+V^\dagger$ and $V-V^\dagger$ are its self-adjoint and skew-adjoint
parts; the example shows that the kernel involution is the sharpening of the operator adjoint for integral
operators.

**Example (rank one).** For $K(x,y)=\varphi(x)\overline{\psi(y)}$ the operator is
$T_Kf=\varphi\int\bar\psi f$, and the adjoint kernel is
$\overline{K(y,x)}=\overline{\varphi(y)}\psi(x)$, so that $T_K^\dagger g=\psi\int\bar\varphi g$; the two
coincide with $K$ when $\varphi=\psi$ and $\lVert\varphi\rVert=1$, which recovers the orthogonal projection
of rank one as the self-adjoint case.

**Example (the Fourier and Hilbert operators).** The Fourier operator $\mathcal F$ of *The Fourier Operator*
is symmetric, $\mathcal F^{\mathrm t}=\mathcal F$, and unitary, so that its adjoint is its inverse,
$\mathcal F^\dagger=\mathcal F^{-1}=\overline{\mathcal F}$; the adjoint is worked out in full in *The Adjoint
of the Fourier Operator*, the last article of this group. The Hilbert transform $H$ of *The Fourier Transform
and Conjugate Symmetry* has the purely imaginary multiplier $-i\operatorname{sgn}$, so it is skew-adjoint,
$H^\dagger=-H$, and $iH$ is self-adjoint; this is the multiplier form of the kernel involution.

## The Distributional Case

**Theorem (distributional adjoint).** Let $T$ be a bounded operator $C_c^\infty(Y)\to\mathcal D'(X)$ with
distribution kernel $K\in\mathcal D'(X\times Y)$, by the Schwartz kernel theorem. Then the adjoint
$T^\dagger$ has the conjugate transpose kernel,
$$
K^\dagger(x,y)=\overline{K(y,x)} ,
$$
the conjugate being taken in the distributional sense,
$\langle K^\dagger,\Phi\rangle=\overline{\langle K,\Phi^{\dagger}\rangle}$ for a test function $\Phi$, and
$T$ is self-adjoint exactly when $K$ is Hermitian as a distribution.

**Proof.** The Schwartz kernel theorem of *The Schwartz Kernel Theorem*, later in this Part, provides the
kernel; the computation of the previous sections carries over with the pairings of test functions against
distributions, and the Hermitian condition is the distributional form of $K^*=K$, as in *Positive Definite
Distributions*, the `* Theory` article. $\blacksquare$

**Remark (unbounded operators).** An unbounded operator has an adjoint only after its domain is fixed, and
the adjoint may be densely defined and closed without the original being so; the distinction between a
symmetric operator and a self-adjoint one, which coincide for bounded operators, is exactly the failure of
the domain to match under the passage to the adjoint. This is *The Adjoint of a Bounded Operator* and the
unbounded-operator material of *Analysis on Linear Spaces*, later in this Part; here the integral operators
are bounded, and the subtlety does not arise.

## Summary

The adjoint of a bounded operator on $L^2(X,\mu)$ is characterised by
$\langle Tf,g\rangle=\langle f,T^\dagger g\rangle$ for the Hilbert pairing $\langle f,g\rangle=\int f\bar g$;
it is conjugate-linear, involutive, isometric and reverses products, and it is the involution of the
`* Operator Theory` group, written with the dagger by *Conventions in Mathematics*, while the star is
reserved for the involution of the elements. For an integral operator the adjoint is the integral operator
with the conjugate transpose kernel, $T_K^\dagger=T_{K^*}$ with $K^*(x,y)=\overline{K(y,x)}$, and the
transpose with respect to the bilinear pairing has the transposed kernel $K(y,x)$; the two differ by the
conjugation, $K^*=\overline{K^{\mathrm t}}$, and agree exactly for real kernels. The operator $T_K$ is
self-adjoint exactly when its kernel is Hermitian, $K(y,x)=\overline{K(x,y)}$, which for a real kernel is
symmetry; examples are the Volterra operator, whose adjoint integrates from $x$ to $1$, the rank-one
projections, the symmetric unitary Fourier operator with $\mathcal F^\dagger=\mathcal F^{-1}$ and the
skew-adjoint Hilbert transform $H^\dagger=-H$. The distributional case follows from the Schwartz kernel
theorem, with the same conjugate transpose kernel. The spectral theory of the self-adjoint case, and the
distinction of symmetric from self-adjoint for unbounded operators, are owned by later articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle f,g\rangle=\int f\bar g$ | Hilbert pairing of $L^2(X,\mu)$ |
| $\{f,g\}=\int fg$ | Bilinear pairing |
| $T^\dagger$ | Adjoint of the operator $T$ |
| $T^{\mathrm t}$ | Transpose of $T$ with respect to the bilinear pairing |
| $K^*(x,y)=\overline{K(y,x)}$ | Conjugate transpose kernel |
| $K^{\mathrm t}(x,y)=K(y,x)$ | Transposed kernel |
| $T_K^\dagger=T_{K^*}$ | The adjoint of the integral operator |
| self-adjoint / unitary / normal | $T^\dagger=T$ / $T^\dagger T=TT^\dagger=\mathrm{id}$ / $TT^\dagger=T^\dagger T$ |

## Further Reading

- Frigyes Riesz and Béla Szőkefalvi-Nagy, *Functional Analysis* (Ungar, 1955; reprinted Dover, 1990), for the
  adjoint of a bounded operator and the integral operators.
- Paul R. Halmos, *Introduction to Hilbert Space and the Theory of Spectral Multiplicity* (Chelsea, 1951),
  for the adjoint, its algebraic properties and the self-adjoint case.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic
  Press, 1980), for the adjoint of bounded and unbounded operators and the domain questions.
- John B. Conway, *A Course in Functional Analysis* (2nd ed., Springer, 1990), for the Hilbert-space adjoint
  and the integral operators.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II* (Interscience, 1963), for the adjoint of
  integral operators and the distributional kernel.
