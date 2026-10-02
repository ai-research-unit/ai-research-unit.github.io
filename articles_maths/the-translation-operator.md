
# __The Translation Operator__

## Introduction

The simplest operator on a function of a group is the one that shifts the argument. On $\mathbb R^n$ the
translation by $y$ is
$$
(\tau_yf)(x)=f(x-y),
$$
so that the family $\{\tau_y\}_{y\in\mathbb R^n}$ is a representation of the additive group: $\tau_y\tau_z=\tau_{y+z}$
and $\tau_0=\mathrm{id}$. Its importance is that it makes the group act on the function space, and that on
$L^2(\mathbb R^n)$ it acts by unitaries; the operators that commute with it are exactly the
translation-invariant ones, which is why convolution and Fourier multipliers are the same subject. This
article develops the family as an operator family: the isometry and unitary properties, the continuity in
the group variable, the infinitesimal generator that differentiation supplies, the spectrum and the
characters, and the diagonalisation by the Fourier operator. It is the article in which the group of
translations and the algebra it generates are placed among the operators of the corpus.

The prerequisites are *Measure Theory and Integration* for the translation invariance of Lebesgue measure,
the $L^p$ spaces and the continuity of translation, *Fourier Analysis on Euclidean Spaces* for the
characters, the transform and its commutation with translation, *Convolution Operators*, the previous
article of this group, for the translation-invariant operators and the multiplier correspondence, and
*Modes of Convergence* for convergence in $L^p$. The unitary and spectral vocabulary — unitary operator,
spectrum, Stone's theorem, one-parameter group — is quoted from *Banach and Hilbert Spaces*, later in this
Part, and from *Semigroups and Evolution Equations*, later in this Part, where the one-parameter groups and
their generators are developed; the concrete facts are proved here, and nothing structural is assumed
beyond the measure-theoretic continuity of translation. The general locally compact group, its Haar
measure and its unitary representations are the subject of *Locally Compact Groups and Haar Measure*,
*Representations of Locally Compact Groups* and *Harmonic Analysis on Groups*, in the neighbouring category
*Analysis on Groups* of this Part; the group is $\mathbb R^n$, or a group whose theory is available, and the
general case is named as a forward reference only. The difference operator $\tau_h-\mathrm{id}$ and its
discrete theory are *The Difference Operator*, the next article of this group. No geometry is invoked; the
group structure is used through translation alone.

## The Translation Operator

### Definition and the Representation Property

**Definition.** Let $G$ be a group acting on a set $X$ on the left, $(x,g)\mapsto gx$, let $f$ be a function
on $X$, and for $g\in G$ define
$$
(\tau_gf)(x)=f(g^{-1}x).
$$
The map $\tau_g$ is the **translation** (or **shift**) by $g$. On $G$ itself, where $G$ acts by left
multiplication, this is $(\tau_gf)(x)=f(g^{-1}x)$; on the additive group $(\mathbb R^n,+)$ it is
$(\tau_yf)(x)=f(x-y)$; on $(\mathbb Z,+)$ it is $(\tau_af)_n=f_{n-a}$.

**Proposition (representation).** The maps $\tau_g$ satisfy $\tau_e=\mathrm{id}$,
$\tau_g\tau_h=\tau_{gh}$ and $\tau_g^{-1}=\tau_{g^{-1}}$, so $g\mapsto\tau_g$ is a representation of $G$ by
linear operators on the space of functions; the representation is faithful on a space containing a
function of two distinct values.

**Proof.** $(\tau_g\tau_hf)(x)=\tau_hf(g^{-1}x)=f(h^{-1}g^{-1}x)=f((gh)^{-1}x)=(\tau_{gh}f)(x)$ by the
inverse law $(gh)^{-1}=h^{-1}g^{-1}$, and the rest is immediate. If $g\neq h$, a function separating $g^{-1}x$
from $h^{-1}x$ at some point $x$ is moved differently by the two. $\blacksquare$

### Isometry and Unitarity

**Theorem.** On $L^p(\mathbb R^n)$, $1\leq p\leq\infty$, the translation is an isometry,
$\lVert\tau_yf\rVert_p=\lVert f\rVert_p$, by the translation invariance of Lebesgue measure; on
$L^2(\mathbb R^n)$ it is a unitary operator, $\tau_y^\dagger\tau_y=\tau_y\tau_y^\dagger=\mathrm{id}$, with
$\tau_y^\dagger=\tau_{-y}=\tau_y^{-1}$ and $\langle\tau_yf,\tau_yg\rangle=\langle f,g\rangle$.

**Proof.** The change of variable $x\mapsto x+y$ preserves Lebesgue measure, so $\int\lvert f(x-y)\rvert^pdx=\int\lvert f\rvert^p$;
the inner product identity is the polarisation, and the adjoint is computed from
$\langle\tau_yf,g\rangle=\int f(x-y)\overline{g(x)}dx=\int f(u)\overline{g(u+y)}du=\langle f,\tau_{-y}g\rangle$.
$\blacksquare$

On a group with a measure, the same proof needs the measure to be invariant under the left action, which is
the defining property of the Haar measure; this is why the general theory belongs to *Locally Compact Groups
and Haar Measure*, and why only groups with an explicit invariant measure — the Euclidean spaces, the
integers, the finite groups, the circle — are used in this article and its companions.

### Continuity in the Group Variable

**Theorem (strong continuity).** For $1\leq p<\infty$ and $f\in L^p(\mathbb R^n)$ the map
$y\mapsto\tau_yf$ is continuous from $\mathbb R^n$ to $L^p(\mathbb R^n)$; that is,
$\lVert\tau_yf-f\rVert_p\to0$ as $y\to0$, and the map is uniformly continuous in the sense that
$\lVert\tau_yf-\tau_{y'}f\rVert_p=\lVert\tau_{y-y'}f-f\rVert_p$ depends on $y-y'$ only. For
$p=\infty$ with the supremum norm the statement is false.

**Proof.** The continuity of translation in $L^p$ for $1\leq p<\infty$ is proved by approximating $f$ by a
continuous compactly supported function, for which the statement is uniform continuity, and using the
density; the translation-invariance of the norm gives the difference form. For $p=\infty$ the indicator of a
half-line is moved by the translation by an amount bounded away from $0$ in the supremum norm, so the
statement fails. $\blacksquare$

**Remark (the strong operator topology).** The theorem says that $y\mapsto\tau_y$ is continuous when the
space of operators carries the strong operator topology, the topology of pointwise convergence, but not
when it carries the operator-norm topology: $\lVert\tau_y-\mathrm{id}\rVert=\sqrt2$ for every $y\neq0$ on
$L^2$, since $\lVert\tau_yf-f\rVert^2\leq2\lVert f\rVert^2$ with equality for a function whose support is
disjoint from its strict translate. The family is therefore a strongly
continuous but not norm-continuous unitary representation, which is exactly the situation covered by
Stone's theorem and not by the norm-convergent exponential of a bounded generator.

## The Infinitesimal Generator

### Differentiation as the Generator

**Theorem (generator of the translation group).** On $L^2(\mathbb R^n)$ let $A_j$ be the operator defined on
the Schwartz class by $A_jf=-\partial_jf$. Then $A_j$ is the infinitesimal generator of the one-parameter
unitary group $t\mapsto\tau_{te_j}$:
$$
\tau_{te_j}=e^{tA_j},\qquad
A_jf=\lim_{t\to0}\frac{\tau_{te_j}f-f}{t}=-\partial_jf ,
$$
the limit being in $L^2$. The operator $A_j$ is closed, densely defined, and skew-adjoint,
$A_j^\dagger=-A_j$; under the Fourier operator it becomes multiplication by the purely imaginary function
$2\pi i\xi_j$.

**Proof.** On the Schwartz class the difference quotient converges to $-\partial_jf$ in $L^2$ by Taylor's
formula and the integrability of the second derivative. The operator $-\partial_j$ is skew-adjoint because
integration by parts gives $\langle-\partial_jf,g\rangle=\langle f,\partial_jg\rangle=\langle f,-(-\partial_j)g\rangle$
on $\mathcal S$, and $\mathcal S$ is a core. The identification with the Fourier side is
$\mathcal F(-\partial_j)\mathcal F^{-1}=M_{-2\pi i\xi_j}$, the differentiation identity of the Fourier
article with a sign. The exponential identity and the closedness are the content of Stone's theorem for a
strongly continuous one-parameter unitary group, in *Semigroups and Evolution Equations*, later in this
Part. $\blacksquare$

**Corollary.** The finite differences $\tau_{te_j}-\mathrm{id}$ approximate the generator, and
$\tau_{te_j}=\mathrm{id}+tA_j+o(t)$; the forward difference $\Delta_h=\tau_{-h}-\mathrm{id}$ is the discrete
analogue of $A_j$, and the two are related by $\Delta_{te_j}=t\partial_j+o(t)=-tA_j+o(t)$ on the domain
of $A_j$.

## The Spectrum and the Characters

### The Characters as Eigenfunctions

**Definition.** A **character** of $G$ is a continuous homomorphism $\chi:G\to\mathbb T$ into the circle
group; on $\mathbb R^n$ the characters are $e_\xi(x)=e^{2\pi ix\cdot\xi}$ for $\xi\in\mathbb R^n$, and on
the circle they are $e_m(x)=e^{2\pi imx}$ for $m\in\mathbb Z$.

**Proposition.** Every character is an eigenfunction of every translation, with
$$
\tau_g e_\xi=\overline{e_\xi(g)}\,e_\xi .
$$
Consequently the characters simultaneously diagonalise the whole representation, and the algebra generated
by the translations is commutative.

**Proof.** $\tau_ge_\xi(x)=e_\xi(x-g)=e_\xi(x)e_\xi(-g)=\overline{e_\xi(g)}e_\xi(x)$, using
$e_\xi(-g)=\overline{e_\xi(g)}$ for a character. $\blacksquare$

### The Spectrum

**Theorem.** On $L^2(\mathbb R^n)$ the translation $\tau_y$ is unitary; for $y=0$ it is the identity, and for
$y\neq0$ its spectrum is the whole unit circle, $\sigma(\tau_y)=\mathbb T$, and it has no eigenvalues. On a
finite group $G$ the translation $\tau_g$ has the characters as a basis of eigenvectors, with eigenvalues
the $\lvert G\rvert$-th roots of unity; on $\ell^2(\mathbb Z)$ the shift $S=\tau_1$ has spectrum $\mathbb T$
and no eigenvalues.

**Proof.** The Fourier operator conjugates $\tau_y$ into multiplication by $e_y(\xi)=e^{-2\pi iy\cdot\xi}$
by *The Fourier Operator* of this group; the spectrum of a multiplication operator $M_m$ on $L^2$ is the
essential range of $m$, and for $y\neq0$ the function $\xi\mapsto e^{-2\pi iy\cdot\xi}$ sweeps the circle,
so the essential range is $\mathbb T$. An eigenvalue would require $e_y$ to be constant on a set of positive
measure, which it is not. On a finite group the characters form an orthonormal basis and the eigenvalues are
$\overline{\chi(g)}$, roots of unity; on $\ell^2(\mathbb Z)$ the shift equation $Sf=\lambda f$ gives
$f_n=\lambda^{-n}f_0$, which is square-summable only if $f=0$, whatever $\lambda$. $\blacksquare$

**Corollary (the diagonalisation).** On a finite abelian group the translation operators are diagonal in
the character basis; on $\mathbb R^n$ and on $\mathbb Z$ the characters diagonalise the representation in
the sense of the spectral theorem or of the Gelfand transform, but the diagonalising functions are not
elements of $L^2$, so that the diagonalisation is continuous rather than discrete.

## The Commutant and the Convolution Operators

### The Operators that Commute with Translation

**Theorem.** A bounded operator on $L^2(\mathbb R^n)$ commutes with every translation $\tau_y$ if and only if
it is a Fourier multiplier operator $T_m$ for a unique $m\in L^\infty(\mathbb R^n)$; a bounded operator on
$L^1(\mathbb R^n)$ with the same property is convolution with a finite measure. In particular the convolution
operators $T_k$ with $k\in L^1$ are exactly the translation-invariant operators with an integrable profile.

**Proof.** This is the translation-invariance theorem of *Convolution Operators*, the previous article of
this group: the Fourier operator carries the translations into the multiplications by the characters, and
an operator commuting with all of them is a multiplication operator. The analysis case is the measure
algebra. $\blacksquare$

### Translation as the Atoms of Convolution

**Theorem.** For $k\in L^1(\mathbb R^n)$ the convolution operator is a superposition of translations,
$$
(T_kf)(x)=\int_{\mathbb R^n}k(y)\,(\tau_yf)(x)\,dy ,
$$
the integral converging in $L^p$ for $f\in L^p$ and $1\leq p<\infty$. The closed algebra generated by the
translations in the strong operator topology is the algebra of translation-invariant operators.

**Proof.** The identity is the definition of the convolution in the two-variable form, and the convergence
is Minkowski's integral inequality, $\lVert\int k(y)\tau_yf\,dy\rVert_p\leq\lVert k\rVert_1\lVert f\rVert_p$;
the closure statement is the theorem above together with the density of the profiles in the multipliers
that are transforms of measures. $\blacksquare$

## The General Locally Compact Group

The definitions of this article use only the group operation and an invariant measure. On a locally compact
group $G$ with left Haar measure $\mu$, the left translation $(\tau_gf)(x)=f(g^{-1}x)$ is an isometry of
$L^p(G,\mu)$ for every $p$ and a unitary of $L^2(G,\mu)$, and $g\mapsto\tau_g$ is strongly continuous, by
the left invariance of the Haar measure; the convolution $(f*h)(x)=\int f(y)h(y^{-1}x)\,d\mu(y)$ is the
superposition of the translations, and the operators commuting with the representation form its
**commutant**, whose study — the group von Neumann algebra, the unitary representations and their
irreducibility — is the subject of *Locally Compact Groups and Haar Measure*, *Representations of Locally
Compact Groups* and *Harmonic Analysis on Groups*, in the neighbouring category *Analysis on Groups* of
this Part. The present Article is the abelian and explicit instance of that theory, and the one the operator
articles of this corpus use.

## Summary

The translation $\tau_g$ on a function space, $(\tau_gf)(x)=f(g^{-1}x)$, is a representation of the group:
$\tau_g\tau_h=\tau_{gh}$, $\tau_e=\mathrm{id}$. On $L^p$ of a group with invariant measure it is an
isometry, and on $L^2$ a unitary; on $L^p(\mathbb R^n)$, $1\leq p<\infty$, it is strongly continuous in the
group variable but not continuous in the operator norm, $\lVert\tau_y-\mathrm{id}\rVert=\sqrt2$ for
$y\neq0$. Its
infinitesimal generator on the one-parameter subgroup $t\mapsto\tau_{te_j}$ is the skew-adjoint operator
$-\partial_j$, which the Fourier operator turns into multiplication by $2\pi i\xi_j$; the characters are
eigenfunctions of every translation, $\tau_ge_\xi=\overline{e_\xi(g)}e_\xi$, and they diagonalise the
representation, discretely on a finite group and in the spectral sense on $\mathbb R^n$ and $\mathbb Z$. The
translation $\tau_y$ for $y\neq0$ is unitary with spectrum the unit circle and no eigenvalues on
$L^2(\mathbb R^n)$. The operators commuting with all translations are exactly the multiplier operators, and
a convolution operator is an integral superposition of translations; the general locally compact group
instance belongs to the group-theoretic category of this Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau_g$ | Translation, $(\tau_gf)(x)=f(g^{-1}x)$; $\tau_yf(x)=f(x-y)$ on $\mathbb R^n$ |
| $\tau_y^\dagger=\tau_{-y}$ | Adjoint of a translation, a unitary on $L^2$ |
| $e_\xi$, $e_m$ | Characters $e^{2\pi ix\cdot\xi}$, $e^{2\pi imx}$ |
| $S$ | Shift on $\ell^2(\mathbb Z)$, $S=\tau_1$ |
| $A_j=-\partial_j$ | Infinitesimal generator of $t\mapsto\tau_{te_j}$, skew-adjoint |
| $\Delta_h=\tau_{-h}-\mathrm{id}$ | Forward difference, the discrete generator |
| $T_k$, $T_m$ | Convolution and multiplier operators, the commutant of the translations |

## Further Reading

- Walter Rudin, *Fourier Analysis on Groups* (Interscience, 1962), for translation, convolution and the
  characters on a locally compact abelian group.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953; reprinted Dover,
  2011), for the representation theory of the translation group and its commutant.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic
  Press, 1980), for strongly continuous unitary groups, Stone's theorem and the generator.
- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton
  University Press, 1971), for translation, the continuity of translation and the multiplier operators.
- Kôsaku Yosida, *Functional Analysis* (6th ed., Springer, 1980), for the translation group on $L^p$ and
  the semigroup generated by differentiation.
