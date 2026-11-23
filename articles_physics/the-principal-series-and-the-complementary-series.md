# __The Principal Series and the Complementary Series__

## Introduction

The unitary representations of the Lorentz group are almost all infinite-dimensional, and they come in two continuous families: the principal series, unitary for a purely imaginary parameter, and the complementary series, unitary for a real parameter in a bounded interval. The finite-dimensional representations of *The Finite-Dimensional Representations and Their Unitarity Defect* are the exceptions at the reducibility points, not the rule.

This article states the induction picture from which both series are built, gives the parameter ranges in which each is unitary, says where the ranges come from, identifies the exceptional parameters, and lists the labels.

The article assumes *The Finite-Dimensional Representations and Their Unitarity Defect* for the contrast, *The Null Cone: The Massless Boundary* and *$P$, $T$ and the Representation Labels* for the physical labels, and *Wigner's Classification: Two Casimirs, Three Orbits* for the orbit picture that the series must reproduce.

## The Induction Picture

### The Borel Subgroup

The group $G=SL_2(\mathbb{C})$ has a minimal parabolic subgroup

$$
B=MAN,\qquad
M=\Bigl\{\operatorname{diag}(e^{i\theta_{\mathrm{axr}}/2},e^{-i\theta_{\mathrm{axr}}/2})\Bigr\},\quad
A=\Bigl\{\operatorname{diag}(e^{\theta_{\mathrm{rpd}}/2},e^{-\theta_{\mathrm{rpd}}/2})\Bigr\},\quad
N=\Bigl\{\begin{pmatrix}1&z\\0&1\end{pmatrix}\Bigr\},
$$

with $M$ compact, $A$ the boost and $N$ the null translations. The quotient $G/B$ is the sky, $\mathbb{CP}^{1}$.

### Induction

A character of $B$ is fixed by two data:

$$
\chi_{\digamma_{\mathrm{par}},n_{\mathrm{par}}}\bigl(m(\theta_{\mathrm{axr}})a(\theta_{\mathrm{rpd}})n\bigr)=e^{in_{\mathrm{par}}\theta_{\mathrm{axr}}}\,e^{\digamma_{\mathrm{par}}\theta_{\mathrm{rpd}}},
\qquad n_{\mathrm{par}}\in\tfrac12\mathbb{Z},\quad \digamma_{\mathrm{par}}\in\mathbb{C}.
$$

The induced representation $I^{\digamma_{\mathrm{par}},n_{\mathrm{par}}}=\operatorname{Ind}_B^G\chi_{\digamma_{\mathrm{par}},n_{\mathrm{par}}}$ acts on sections of a line bundle over the sky, and the parameter $\digamma_{\mathrm{par}}$ is the **exponent**: it is the weight with which the boost subgroup rescales the fibre.

### Why This Is the Right Starting Point

Every irreducible admissible representation of $SL_2(\mathbb{C})$ is a subquotient of some $I^{\digamma_{\mathrm{par}},n_{\mathrm{par}}}$ — the subquotient theorem. So the series is not an example; it is the catalogue, and the finite-dimensional representations are among its subquotients.

### The Parameter

$\digamma_{\mathrm{par}}$ is complex and $n_{\mathrm{par}}$ is discrete. Two identifications reduce the parameter space: $\digamma_{\mathrm{par}}$ and $-\digamma_{\mathrm{par}}$ give contragredient representations, and $n_{\mathrm{par}}$ and $-n_{\mathrm{par}}$ give conjugates. So the essential parameter is the pair $(\digamma_{\mathrm{par}}\bmod\pm,n_{\mathrm{par}}\bmod\pm)$, and the physical labels of the block are read from it.

## The Principal Series

### The Definition

The **principal series** is $\digamma_{\mathrm{par}}$ purely imaginary:

$$
\digamma_{\mathrm{par}}=i\rho,\qquad \rho\in\mathbb{R}.
$$

The character is then unitary: $\lvert e^{\digamma_{\mathrm{par}}\theta_{\mathrm{rpd}}}\rvert=1$ for real $\theta_{\mathrm{rpd}}$, so $\chi_{\digamma_{\mathrm{par}},n_{\mathrm{par}}}$ is a character into the unit circle.

### Why It Is Unitary

Induction preserves unitarity when the inducing character is unitary and the inducing subgroup is closed and unimodular-compatible. Concretely, the inner product

$$
\langle f_1,f_2\rangle=\int_{G/B}\overline{f_1(x)}\,f_2(x)\,d\mu(x)
$$

on $L^{2}$ sections is invariant, because the cocycle that appears when the group acts is $\chi_{\digamma_{\mathrm{par}},n_{\mathrm{par}}}$ evaluated on the $B$-component, and its modulus is one. So the invariance of the inner product is the statement $\lvert\chi\rvert=1$.

That is the whole proof, and it is worth contrasting with the finite-dimensional case: there, the same computation produces the factor $e^{(n_{\mathrm{par}}+n)\theta_{\mathrm{rpd}}}$, whose modulus is not one, and the representation fails.

### The Labels

The principal series is labelled by

$$
(i\rho,n_{\mathrm{par}}),\qquad \rho\in\mathbb{R},\quad 2n_{\mathrm{par}}\in\mathbb{Z},
$$

so one continuous and one discrete label. The continuous label is the obstruction's replacement: the finite-dimensional defect $\tfrac12(j_1+j_2)$ becomes a continuous parameter, and the growth that it measured is absent because the parameter is imaginary.

### What It Physically Is

The principal series is the home of the massless and the continuous-spin representations. The label $\rho$ is the continuous-spin parameter, and the discrete label $n_{\mathrm{par}}$ is a helicity-like charge. The block's massless representations sit at the boundary values of $\rho$ where the module becomes reducible.

## The Complementary Series

### The Definition of the Complementary Series

The **complementary series** is $\digamma_{\mathrm{par}}$ real with

$$
0<\lvert\digamma_{\mathrm{par}}\rvert<1,
$$

with the same inducing data and a *different* inner product.

### Why the $L^{2}$ Product Fails There

For real $\digamma_{\mathrm{par}}$ the character has modulus $e^{\digamma_{\mathrm{par}}\theta_{\mathrm{rpd}}}\neq1$, so the $L^{2}$ inner product is not invariant: the group action rescales sections by a positive factor that depends on the point. The naive product is therefore not the one to use.

### The Nonlocal Product

Instead one uses the intertwining operator

$$
(J_{\digamma_{\mathrm{par}}}f)(x)=\int_{G/B}\lvert c(x,y)\rvert^{-1-\digamma_{\mathrm{par}}}f(y)\,d\mu(y),
$$

which is a nonlocal integral operator with a kernel singular on the diagonal, and one defines

$$
\langle f_1,f_2\rangle_{\digamma_{\mathrm{par}}}=\langle f_1,J_{\digamma_{\mathrm{par}}}f_2\rangle_{L^{2}} .
$$

The operator $J_{\digamma_{\mathrm{par}}}$ is positive definite exactly in the range $\lvert\digamma_{\mathrm{par}}\rvert<1$ (for the spherical case), and that positivity is the unitarity of the complementary series. Outside the range it has negative directions, and the "inner product" is indefinite.

### Why It Is Called Complementary

Because its parameter range complements the principal series' in the plane of $\digamma_{\mathrm{par}}$: the principal series is the imaginary axis, the complementary series is the open interval $(-1,1)$ on the real axis, and the two together with their boundary points exhaust the unitary parameters for this family. The name is a statement about the parameter plane and not about the representations' contents.

## The Discrete Series and Temperedness

### The Discrete Series

The third series is not induced from the Borel subgroup at all. A unitary module belongs to the **discrete series** when its matrix coefficients are square-integrable on the group, so that the module occurs as a direct summand of the regular representation $L^{2}(G)$ rather than as a direct integral of induced modules.

Its existence is a rank criterion, not an accident: a semisimple group has a nonempty discrete series exactly when its maximal compact subgroup has the same rank as the group itself, because only then does the group possess a compact Cartan subgroup. The Lorentz group passes the criterion, since its compact subgroup $\mathrm{SU}(2)$ has rank one and the group's rank is also one. The members are labelled by a discrete set, the same half-integer pair $(n_{\mathrm{par}},n)$ that labels the algebraic modules, subject to a non-degeneracy condition; the block does not need the condition, because no article here uses a discrete-series module.

The structural point is what matters: the discrete series is the part of the unitary dual that comes from *below*, as summands of $L^{2}(G)$, while the principal and complementary series come from *above*, as induced modules. The finite-dimensional carriers of the algebra belong to neither.

### Temperedness

A unitary module is **tempered** when its matrix coefficients lie in $L^{2+\epsilon}(G)$ for every $\epsilon>0$: they decay at least as fast as an $L^{2}$ function, but the borderline case is not required.

- The principal series is tempered. Its parameters are on the imaginary axis, $\digamma_{\mathrm{par}}=i\rho$ with $\rho$ real, and the growth of the matrix coefficients is oscillatory rather than exponential.
- The complementary series is not tempered. Its parameter is real with $\lvert\digamma_{\mathrm{par}}\rvert<1$, and its matrix coefficients decay more slowly than $L^{2}$ requires; that is the same failure that forced the nonlocal inner product.
- The discrete series is tempered, since square-integrability is stronger than membership in every $L^{2+\epsilon}$.

Temperedness is the property that decides membership in the Plancherel formula. The Plancherel measure of the Lorentz group is supported on the tempered part of the unitary dual, with a continuous density on the principal series; the complementary series is a set of measure zero for it. So a reader who asks "which modules enter the harmonic analysis of the group" gets the tempered ones, and a reader who asks "which modules describe a physical state" gets them too, because a state must be normalisable in a sense the group respects.

## The Exceptional Cases

### The Boundary $\lvert\digamma_{\mathrm{par}}\rvert=1$

At $\digamma_{\mathrm{par}}=\pm1$ the intertwining operator degenerates: it is no longer invertible, and the representation is reducible, with a finite-dimensional subquotient. The complementary series therefore terminates at $\digamma_{\mathrm{par}}=\pm1$ and does not continue to larger $\lvert\digamma_{\mathrm{par}}\rvert$.

This is the same phenomenon as a spin chain's "special" couplings: the parameter value at which an operator's positivity fails is a value at which the module changes its composition.

### The Reducibility Points

At special $\digamma_{\mathrm{par}}$ — integers, with parity fixed by $n_{\mathrm{par}}$ — the induced representation has a finite-dimensional subquotient, and the quotient or submodule is one of the representations of *The Finite-Dimensional Representations and Their Unitarity Defect*. So the finite-dimensional representations are not a separate family: they are the points of the parameter plane at which the series has a kink.

### $\digamma_{\mathrm{par}}=0$

$\digamma_{\mathrm{par}}=0$ is the middle of the complementary interval and the limit of the principal series as $\rho\to0$. The representation there is reducible and has the trivial representation as a subquotient. So $\digamma_{\mathrm{par}}=0$ is simultaneously the interior of the complementary range and a reducibility point, which is why the spherical function's analysis needs the parameter kept away from zero.

### The Degenerate $n_{\mathrm{par}}$

$n_{\mathrm{par}}=0$ is the spherical case: the representation has a vector fixed by the maximal compact subgroup. For $n_{\mathrm{par}}\neq0$ the series is nonspherical and the analysis of the intertwining operator is the same with a matrix-valued kernel. The block uses the spherical case, and the statement of the parameter range is the same.

### The Two Signs

The contragredient of $I^{\digamma_{\mathrm{par}},n_{\mathrm{par}}}$ is $I^{-\digamma_{\mathrm{par}},-n_{\mathrm{par}}}$. For imaginary $\digamma_{\mathrm{par}}$ this is the complex conjugate representation, $I^{\bar\digamma_{\mathrm{par}},-n_{\mathrm{par}}}$, so the principal series is closed under contragredience and its members are self-contragredient up to the exchange $n_{\mathrm{par}}\to-n_{\mathrm{par}}$. For real $\digamma_{\mathrm{par}}$ the contragredient is a genuinely different member with the exponent's sign reversed. That is a real difference between the two series and it is why the complementary series is paired. The sign of $\digamma_{\mathrm{par}}$ is invisible in the principal series' labels and visible in the complementary series'.

## The Labels of the Representations

### The Two Labels

| series | $\digamma_{\mathrm{par}}$ | continuous label | discrete label |
|---|---|---|---|
| principal | $i\rho$, $\rho\in\mathbb{R}$ | $\rho$ | $n_{\mathrm{par}}\in\tfrac12\mathbb{Z}$ |
| complementary | real, $0<\lvert\digamma_{\mathrm{par}}\rvert<1$ | $\digamma_{\mathrm{par}}$ | $n_{\mathrm{par}}\in\tfrac12\mathbb{Z}$ |
| finite-dimensional | integers (reducibility points) | none | $(j_1,j_2)$ |

### What the Labels Are Not

They are not the mass and the spin. The mass and the spin are Poincaré labels, computed from the two Casimirs of *$P$, $T$ and the Representation Labels*; the labels $(\rho,n_{\mathrm{par}})$ are Lorentz labels, and a physical one-particle module is an induced representation of the Poincaré group whose fibre is a Lorentz module. The two label sets are related but not identical, and a reader who conflates them will expect the wrong counting.

### The Casimir

On the series the Lorentz Casimir takes a continuous real value determined by $\digamma_{\mathrm{par}}$, and the value is monotone in $\lvert\digamma_{\mathrm{par}}\rvert$ on the complementary interval. At the reducibility points it coincides with the finite-dimensional value. The normalisation is a convention; the structural statement is that the Casimir is real on the whole unitary parameter set, which is exactly what unitarity requires.

### The Reading

The finite-dimensional defect measured the growth of a representation under a boost. In the series there is no growth: the parameter is either imaginary, so the boost acts by a phase, or real and small, so the nonlocal product absorbs the growth. That is the sense in which the series is the "unitarised" version of the finite-dimensional labels.

## What the Block Uses

### The Massless Label

The boundary values of the principal series are the massless labels, and the helicity is the discrete label at the boundary. That is why the massless representations are "at the edge of the series" and not "the massless limit of a massive series": the parameter space's boundary is where they sit.

### The Cosmological and Thermal Uses

The series is what a Lorentz-invariant thermal or cosmological two-point function is expanded in, because only unitary representations can appear in a spectral decomposition. The complementary series appears in the Euclidean continuation, where its parameter becomes the scaling dimension of a boundary operator.

That last statement is the block's bridge to the conformal material: the complementary series' parameter is the shadow of a conformal dimension, and the bound $\lvert\digamma_{\mathrm{par}}\rvert<1$ is the unitarity bound.

### What Is Not Done Here

The block does not construct the series as a Hilbert space, does not prove the positivity of the intertwining operator, and does not compute the Plancherel measure. Those are three substantial theorems, they are in the references, and none of the block's physical statements depends on them.

## Summary

The irreducible unitary representations of the Lorentz group are induced from the Borel subgroup with a character $e^{2im\alpha}e^{\digamma_{\mathrm{par}}\theta_{\mathrm{rpd}}}$. For $\digamma_{\mathrm{par}}$ purely imaginary the induced $L^{2}$ representation is unitary with the ordinary inner product, and that is the principal series, labelled $(i\rho,n_{\mathrm{par}})$. For real $\digamma_{\mathrm{par}}$ with $\lvert\digamma_{\mathrm{par}}\rvert<1$ a nonlocal intertwining operator supplies an invariant product and the representation is unitary, and that is the complementary series. At $\lvert\digamma_{\mathrm{par}}\rvert=1$ the operator degenerates, and at integer $\digamma_{\mathrm{par}}$ the representation has a finite-dimensional subquotient, which is how the finite-dimensional representations of the previous article appear as points of the same catalogue. The finite-dimensional defect has no counterpart here: the parameter is imaginary or small, and the boost's growth is a phase or is absorbed. The third series is the discrete one: it is not induced from the Borel subgroup but occurs as a direct summand of $L^{2}(G)$, and it exists because the group and its maximal compact subgroup have the same rank. Of the three, the principal and the discrete series are tempered and the complementary series is not, so the Plancherel density lives on the principal series.

## Summary of Notation

| symbol | meaning |
|---|---|
| $B=MAN$ | the minimal parabolic subgroup |
| $\chi_{\digamma_{\mathrm{par}},n_{\mathrm{par}}}$ | the character $e^{in_{\mathrm{par}}\theta_{\mathrm{axr}}}e^{\digamma_{\mathrm{par}}\theta_{\mathrm{rpd}}}$ |
| $\theta_{\mathrm{rpd}}$ | the boost coordinate of the Borel element, i.e. the rapidity, written $\theta_{\mathrm{rpd}}$ elsewhere in the block |
| $\digamma_{\mathrm{par}}$ | the exponent, the continuous parameter |
| $n_{\mathrm{par}}$ | the discrete charge, the $M$-weight |
| $I^{\digamma_{\mathrm{par}},n_{\mathrm{par}}}$ | the induced representation |
| $J_{\digamma_{\mathrm{par}}}$ | the intertwining operator |
| $\lvert\digamma_{\mathrm{par}}\rvert<1$ | the complementary range |

## Further Reading

- A. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples*, Princeton University Press, 1986 — parabolic induction, the principal and complementary series, and the intertwining operators.
- I. M. Gelfand, M. I. Graev and N. Ya. Vilenkin, *Generalized Functions*, Vol. 5, Academic Press, 1966 — the series of $SL_2(\mathbb{C})$ computed explicitly, with the Plancherel measure.
- N. Ya. Vilenkin, *Special Functions and the Theory of Group Representations*, AMS, 1968 — the complementary series of $SL_2(\mathbb{C})$ and the spherical functions.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1, Cambridge University Press, 1995, §5.6 — why the physical representations are infinite-dimensional and how the continuous labels arise.
- *The Finite-Dimensional Representations and Their Unitarity Defect* — the representations that the reducibility points recover.
- *$P$, $T$ and the Representation Labels* — the Poincaré labels that are not these labels.
