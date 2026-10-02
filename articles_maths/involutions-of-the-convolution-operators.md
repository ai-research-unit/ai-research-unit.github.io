
# __Involutions of the Convolution Operators__

## Introduction

A convolution operator is built from a profile and the group structure, $T_kf=k*f$, and the involution of the
group turns the profile into a new profile that produces the adjoint operator. On $\mathbb R^n$ with the
Hilbert pairing of $L^2$,
$$
k^*(x)=\overline{k(-x)},\qquad T_k^\dagger=T_{k^*} ,
$$
and the passage $k\mapsto k^*$ is the involution on the profiles, conjugate-linear, involutive, an isometric
anti-automorphism of the convolution algebra; the correspondence $k\mapsto T_k$ carries it to the adjoint of
the operator. This is the fourth article of the `* Operator` material of this category, and it is the group
analogue of the adjoint of an integral operator: the kernel of a convolution operator is $k(x-y)$, and the
conjugate transpose kernel is exactly $k^*(x-y)$. On the Fourier side, where the operator is multiplication
by the multiplier $\hat k$, the adjoint is multiplication by the conjugate multiplier $\overline{\hat k}$, and
the operator is unitary exactly when the multiplier has modulus one — the **unitary multipliers**, which are
the unitary convolution operators and the group they form.

The article is the third of the `* Operator Theory` group of *Foundations of Analysis*. Its prerequisites
are *Convolution Operators*, the second article of the first group of this category, for the convolution
operator, its multiplier and its boundedness; *The Integral Operator* for the kernel form; *The Fourier
Operator* for the unitary transform and the Plancherel theorem; *The Fourier Transform and Conjugate
Symmetry* for the involution on functions and the identity $\widehat{f^*}=\overline{\hat f}$; *Hermitian
Measures and Complex Measures* for the Hermitian and positive measures; *The Adjoint of an Integral Operator*,
the previous article of this group, for the adjoint and the marks; and *Banach and Hilbert Spaces*, later in
this Part, for the adjoint of a bounded operator and the unitary operators, quoted as established. The
convolution algebra of a general locally compact group, the modular function in the involution, the two
conventions for a non-unimodular group, and the regular representation built from the group algebra are
*The Convolution Algebra $L^1(G)$*, *The Group Algebra as an Algebra of Operators* and *Convolution on a
Group*, in the neighbouring category *Analysis on Groups* of this Part, and are named here as forward
references only; the present article stays on $\mathbb R^n$ and on the discrete and periodic instances where
the group is abelian and the modular function is trivial. No geometry is invoked.

## Convolution Operators and the Group Pairing

### The Convolution Operator

**Definition.** Let $k\in L^1(\mathbb R^n)$. The **convolution operator** of the profile $k$ is
$$
(T_kf)(x)=(k*f)(x)=\int_{\mathbb R^n}k(x-y)f(y)\,dy ,
$$
a bounded operator on $L^2(\mathbb R^n)$ with $\lVert T_k\rVert\leq\lVert k\rVert_1$, commuting with every
translation: $T_kL_a=L_aT_k$ for the shift $L_af(x)=f(x-a)$.

### The Group Pairing

**Definition.** The **group pairing** on $L^2(\mathbb R^n)$ is the Hilbert pairing
$$
\langle f,g\rangle=\int_{\mathbb R^n}f\bar g .
$$
It is invariant under translation and inversion,
$$
\langle L_af,L_ag\rangle=\langle f,g\rangle,\qquad \langle \check f,\check g\rangle=\langle f,g\rangle ,
$$
with $\check f(x)=f(-x)$, and this invariance is what makes the adjoint of a convolution operator again a
convolution operator. The pairing is the one carried by the convolution algebra; the bilinear pairing
$\{f,g\}=\int fg$, which produces the transpose, is its companion in the same way as for an integral
operator.

### The Involution on the Profiles

**Definition.** The **involution** of a profile $k$ is the profile
$$
k^*(x)=\overline{k(-x)} ,
$$
the conjugate of the reflection. It is conjugate-linear and involutive, $(\lambda k+\mu l)^*=\bar\lambda k^*+\bar\mu l^*$,
$(k^*)^*=k$, it is an anti-automorphism of the convolution,
$$
(k*l)^*=l^**k^* ,
$$
and it is isometric, $\lVert k^*\rVert_1=\lVert k\rVert_1$, by the translation invariance of the Lebesgue
measure.

**Proof.** The conjugate-linearity and the involution are immediate from the definition. For the
anti-automorphism, write $Rk(x)=k(-x)$ for the reflection; the reflection commutes with the convolution,
$R(k*l)=(Rk)*(Rl)$, because on the abelian group the convolution is commutative and the substitution
$y\mapsto-y$ shows both sides equal $\int k(-x-y)l(y)dy$. Hence
$$
(k*l)^*=\overline{R(k*l)}=\overline{(Rk)*(Rl)}
=\overline{Rk}*\overline{Rl}=k^**l^*=l^**k^* ,
$$
the last equality by the commutativity of the convolution, and the products exchange as the anti-automorphism
requires. The norm identity is the substitution $x\mapsto-x$. $\blacksquare$

## The Adjoint of a Convolution Operator

### The Adjoint Kernel

**Theorem.** For $k\in L^1(\mathbb R^n)$ the adjoint of the convolution operator is the convolution operator
of the involution,
$$
T_k^\dagger=T_{k^*},\qquad (T_k^\dagger f)(x)=\int_{\mathbb R^n}\overline{k(y-x)}f(y)\,dy ,
$$
and the kernel of $T_k$ is $K(x,y)=k(x-y)$, whose conjugate transpose is
$K^*(x,y)=\overline{k(y-x)}=k^*(x-y)$, the kernel of $T_{k^*}$.

**Proof.** By the change of variable $y\mapsto x-y$ in the pairing,
$$
\langle T_kf,g\rangle=\iint k(x-y)f(y)\overline{g(x)}\,dydx
=\iint f(y)\overline{\Bigl(\int\overline{k(x-y)}g(x)\,dx\Bigr)}\,dy
=\iint f(y)\overline{\Bigl(\int\overline{k(z)}g(y+z)\,dz\Bigr)}\,dy ,
$$
and substituting $w=y+z$ in the inner integral gives
$\int\overline{k(w-y)}g(w)\,dw=(T_{k^*}g)(y)$, so $\langle T_kf,g\rangle=\langle f,T_{k^*}g\rangle$ and
$T_k^\dagger=T_{k^*}$ by the uniqueness of the adjoint; the kernel statement is the substitution
$K(x,y)=k(x-y)$. $\blacksquare$

### The Involution on the Operators

**Theorem.** The map $T_k\mapsto T_k^\dagger$ on the convolution operators is the transport of the profile
involution under $k\mapsto T_k$:
$$
T_k^\dagger=T_{k^*},\qquad
(T_kT_l)^\dagger=T_l^\dagger T_k^\dagger,\qquad
(T_k^\dagger)^\dagger=T_k ,
$$
and $k\mapsto T_k$ is a $\ast$-homomorphism of the convolution algebra into the bounded operators,
$T_{k*l}=T_kT_l$ and $T_{k^*}=T_k^\dagger$; the element involution of the `* Theory` layer and the adjoint
of the `* Operator` layer therefore agree, and this agreement is the statement that the left regular
representation is a $\ast$-representation.

**Proof.** The adjoint identity is the theorem above; the multiplicative identity is the associativity of
the convolution, $k*(l*f)=(k*l)*f$; the anti-multiplicativity follows from the anti-automorphism
$(k*l)^*=l^**k^*$ and the multiplicative identity. The agreement of the two layers is the identity
$T_{k^*}=T_k^\dagger$ itself. $\blacksquare$

**Example (the Dirac profiles).** The profile $\delta_a$ gives the shift $T_{\delta_a}=L_a$, and
$\delta_a^*=\delta_{-a}$, so $L_a^\dagger=L_{-a}$, as the translation invariance of the pairing requires.
The profile $k(x)=\mathbf 1_{[0,\infty)}(x)e^{-x}$ on $\mathbb R$ has the involution
$k^*(x)=\mathbf 1_{(-\infty,0]}(x)e^{x}$, and $T_k$ is the operator that integrates the exponential weight
forward, with $T_{k^*}$ integrating it backward.

## The Fourier Multiplier Form

### The Adjoint Multiplier

**Theorem.** On the Fourier side the convolution operator is the multiplication operator
$$
T_k=\mathcal F^{-1}M_{\hat k}\mathcal F,\qquad (M_{\hat k}h)(\xi)=\hat k(\xi)h(\xi) ,
$$
and the adjoint is the multiplication by the conjugate multiplier,
$$
T_k^\dagger=\mathcal F^{-1}M_{\overline{\hat k}}\mathcal F,\qquad \widehat{k^*}=\overline{\hat k} ,
$$
so that the operator is self-adjoint exactly when $\hat k$ is real, skew-adjoint exactly when $\hat k$ is
purely imaginary, and normal for every $k$.

**Proof.** The convolution theorem gives $\widehat{k*f}=\hat k\hat f$, so $\mathcal F$ intertwines $T_k$
with the multiplication by $\hat k$; the Fourier transform is unitary by Plancherel, so the adjoint of
$\mathcal F^{-1}M_{\hat k}\mathcal F$ is $\mathcal F^{-1}M_{\hat k}^\dagger\mathcal F$, and the adjoint of a
multiplication operator is the multiplication by the conjugate function. The identity
$\widehat{k^*}=\overline{\hat k}$ is the conjugate-symmetry theorem of *The Fourier Transform and Conjugate
Symmetry*; the self-adjoint and skew-adjoint cases are the reality and the pure-imaginariness of $\hat k$, and
normality is automatic for a multiplication operator. $\blacksquare$

**Example (the Hilbert and Riesz transforms).** The Hilbert transform of *The Fourier Transform and
Conjugate Symmetry* is convolution with the kernel $1/(\pi x)$ on $\mathbb R$ and has the multiplier
$-i\operatorname{sgn}\xi$, purely imaginary, so it is skew-adjoint, $H^\dagger=-H$, as recorded there; the
Riesz transforms $R_j$ on $\mathbb R^n$ have the multipliers $-i\xi_j/\lvert\xi\rvert$, also purely
imaginary, so each is skew-adjoint, $R_j^\dagger=-R_j$, and their symbols are unimodular, so each $R_j$ is
unitary after the sign. The examples show both extremities of the multiplier dictionary.

### The Unitary Multipliers

**Theorem.** Let $k\in L^1(\mathbb R^n)$ with $\hat k\in L^\infty$. Then the convolution operator $T_k$ is
unitary on $L^2$ if and only if the multiplier is unimodular,
$$
T_k^\dagger T_k=T_kT_k^\dagger=\mathrm{id}\ \Longleftrightarrow\ \lvert\hat k(\xi)\rvert=1\ \text{for almost every }\xi ,
$$
and the unitary convolution operators form a group under composition, the **group of unitary multipliers**;
under the Fourier transform it is the group of unimodular functions that arise as transforms of profiles.

**Proof.** A multiplication operator $M_m$ is unitary exactly when $\lvert m\rvert=1$ almost everywhere, so
the statement is the unitarity of $M_{\hat k}$ transported by the unitary $\mathcal F$; the group property is
composition and the invariance of unimodularity, and the conjugation identifies it with the group of
unimodular multipliers. For the finite and discrete instances the same proof applies with the discrete
Fourier transform, and the group is the unitary group of the finite convolution algebra. $\blacksquare$

**Example (the discrete and periodic cases).** On $\mathbb Z$ the involution is $k^*(n)=\overline{k(-n)}$
and the multiplier is the function on the circle $\hat k(\theta)=\sum_nk(n)e^{-in\theta}$; the shift
$k=\delta_m$ has $\hat k(\theta)=e^{-im\theta}$, of modulus one, and $T_{\delta_m}$ is unitary. On a finite
abelian group the same dictionary holds with the discrete Fourier transform, and the unitary multipliers are
the profiles whose transform has modulus one.

**Example (Hermitian measures).** The measure-profiles of *Hermitian Measures and Complex Measures* obey the
same involution, and the convolution operator of a measure $\mu$ is self-adjoint exactly when the measure is
Hermitian, that is when $\hat\mu=\overline{\hat\mu}$ is real; the unitary case is the unimodular $\hat\mu$,
and the classification of the idempotent and the unimodular measures belongs to *Harmonic Analysis on
Groups*, in the neighbouring category *Analysis on Groups*, later in this Part.

**Remark (the general group).** On a general locally compact group the involution carries the modular
function, $f^*(x)=\overline{f(x^{-1})}\Delta(x)^{-1}$, and on a non-unimodular group the two convolutions
differ; the factor $\Delta$ is exactly what restores the isometry $\lVert f^*\rVert_1=\lVert f\rVert_1$, and
the resulting algebra is a Banach $\ast$-algebra. This is *The Convolution Algebra $L^1(G)$* and
*Convolution on a Group*, in the neighbouring category *Analysis on Groups*, later in this Part, and on the
abelian, compact and discrete groups treated here $\Delta\equiv1$ and the involution reduces to
$f^*(x)=\overline{f(x^{-1})}$.

## Summary

The convolution operator $T_kf=k*f$ has, under the group pairing $\langle f,g\rangle=\int f\bar g$, the
adjoint $T_k^\dagger=T_{k^*}$ with the involution $k^*(x)=\overline{k(-x)}$, which is the conjugate
transpose of the kernel $K(x,y)=k(x-y)$; the involution on the profiles is conjugate-linear, involutive, an
isometric anti-automorphism of the convolution, $(k*l)^*=l^**k^*$, and the correspondence $k\mapsto T_k$
carries it to the adjoint, being a $\ast$-homomorphism of the convolution algebra into the bounded operators.
On the Fourier side the operator is multiplication by $\hat k$, the adjoint is multiplication by
$\overline{\hat k}$ since $\widehat{k^*}=\overline{\hat k}$, and the operator is self-adjoint exactly for
real $\hat k$, skew-adjoint exactly for purely imaginary $\hat k$ and unitary exactly for unimodular
$\hat k$; the unitary convolution operators are the **unitary multipliers**, and they form a group under
composition, identified by the Fourier transform with the group of unimodular multipliers. The Hilbert
transform and the Riesz transforms are the skew-adjoint unimodular examples, and the Hermitian measures are
the self-adjoint measure-profiles. On a non-unimodular group the involution carries the modular function and
the two convolutions differ, which is the concern of the convolution-algebra articles of *Analysis on
Groups*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_kf=k*f$ | Convolution operator of the profile $k$ |
| $\langle f,g\rangle=\int f\bar g$ | Group pairing of $L^2$ |
| $k^*(x)=\overline{k(-x)}$ | Involution of a profile |
| $K(x,y)=k(x-y)$ | Kernel of the convolution operator |
| $T_k^\dagger=T_{k^*}$ | Adjoint of the convolution operator |
| $\widehat{k^*}=\overline{\hat k}$ | Involution on the Fourier side |
| $\hat k$ real / purely imaginary / unimodular | self-adjoint / skew-adjoint / unitary $T_k$ |
| unitary multipliers | The unitary convolution operators under composition |
| $f^*(x)=\overline{f(x^{-1})}\Delta(x)^{-1}$ | The general-group involution (forward reference) |

## Further Reading

- Frigyes Riesz and Béla Szőkefalvi-Nagy, *Functional Analysis* (Ungar, 1955; reprinted Dover, 1990), for the
  convolution operators, the adjoint and the multipliers.
- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton
  University Press, 1971), for the convolution algebra, the multipliers and the Riesz transforms.
- Walter Rudin, *Fourier Analysis on Groups* (Interscience, 1962), for the convolution algebra of a locally
  compact abelian group, the involution and the multipliers.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953), for the Banach
  $\ast$-algebra of a group, the involution and the modular function.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic
  Press, 1980), for the unitary operators and the multipliers.
