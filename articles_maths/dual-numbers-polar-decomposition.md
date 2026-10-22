
# __Dual-Numbers Polar Decomposition__

## Introduction

This article develops the polar decomposition of the dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$. It follows *Dual-Numbers Algebra* for the conventions, *Dual-Numbers Norm and Invertibility* for the norm and the real size function on the units, *Shears and Parabolic Rotations* for the group of units and the shear, and *Dual-Numbers Exponential and Lie Group Structure* for the exponential. The comparison throughout is with the complex polar decomposition, whose phase factor is the unit circle.

The polar decomposition of the dual numbers is the **third and last case of the exponential rule** and the **missing link of the polar series**. The rule is the classification of a generator $\nu$ of a one-parameter group by the sign of $\nu^2$: for $\nu^2 = -1$ the exponential winds, giving the elliptic case; for $\nu^2 = +1$ it boosts, giving the hyperbolic case; for $\nu^2 = 0$ it shears, giving the parabolic case. The dual-number generator $\varepsilon$ has $\varepsilon^2 = 0$, and its case of the rule is the parabolic one. The polar series of the family of number systems — complex, split complex, dual — is completed by this row; the dual case is the only one whose polar form has a nilpotent factor and no compact phase.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Throughout, $R$ is a commutative ring with identity in which $2$ is invertible; the field specialisation $R = k$ is flagged, and the ordered and geometric specialisation is $R = \mathbb{R}$, in which case the algebra is written $\mathbb{D}'$. A general dual number is

$$
Q = q + \varepsilon q', \qquad q, q' \in R,
$$

The conventions and the symbols are those of *Dual-Numbers Algebra* and of the corpus (*Conventions in Mathematics*); the symbols this article uses are collected in §*Summary of Notation*.

## Why a Single Scale and a Single Nilpotent Factor

### The Counting

The algebra $\mathbb{D}'_{\mathbb{R}}$ has real dimension two. In this article the word **unit** carries the ring sense of the corpus: a **unit** of the algebra is an invertible element, one with $q\neq0$, and the **group of units** $(\mathbb{D}')^\times$ is the set of them. It is not the corpus's **unit element**, which is an element of norm one for the norm in view (*Conventions in Mathematics*, §*The Unitary Convention*); here the unit elements $\langle Q\rangle=1$ are the subgroup $\{\pm1\}\cdot(1+\mathrm{M})$, a proper subset of the group of units. The group of units is, by *Dual-Numbers Norm and Invertibility*, a semidirect product that is in fact a direct product,

$$
(\mathbb{D}')^\times \cong \mathbb{R}^\times \times (\mathbb{R}, +),
$$

of real dimension two. A polar decomposition writes every element of a group as a product of independent one-parameter factors; for a two-dimensional abelian group the natural count is therefore two factors, and they are a scale and a shear.

| Factor | Dimension | Range | Role |
|---|---|---|---|
| Scale | $1$ | $r > 0$ | modulus $|q|$ |
| Sign | $0$ | $\{\pm 1\}$ | the order-two component of $\mathbb{R}^\times$ |
| Shear | $1$ | $s \in \mathbb{R}$ | parabolic angle $s = q'/q$ |

So there is one positive scale, one discrete sign, and one real angle, and the angle is not a compact phase but a shear parameter.

### The Absence of a Compact Phase

In the complex case the unit group contains the circle $\mathrm{U}(1)$, whose parameter is an angle modulo $2\pi$; in the split-complex case it contains a hyperbola, whose parameter is an unbounded rapidity; in the dual case the non-scalar factor is the shear group $1 + \mathrm{M} \cong (\mathbb{R}, +)$, a line. There is no compact one-parameter subgroup of $(\mathbb{D}')^\times$ other than the central $\{\pm 1\}$, so the polar form has no angle modulo anything: it has a single real parabolic angle, globally defined and without period. This is why *the exponential rule ends in a straight line rather than a circle*.

### The Centrality of the Nilpotent

Because $\mathbb{D}'_R$ is commutative, every element is central, and in particular the nilpotent $\varepsilon$ is central and the shear factor $\exp(s\varepsilon) = 1 + s\varepsilon$ is central. The phase-like factor is central but *nilpotent*, so it cannot be extracted by a logarithm taking values in a torus. The centrality is what makes the order of the factors in the polar form immaterial here.

## The Exponential Form

### The Word as Exponentials

The word $Q = r\,u\,\exp(s\varepsilon)$ is a product of a scale, a sign and a shear, and the scale and the shear are exponentials:

$$
Q = \exp(\ln\lvert q\rvert)\cdot u\cdot\exp(s\varepsilon) , \qquad u = \pm 1 , \qquad s = \frac{q'}{q} .
$$

| # | factor | name | real dimension | exponential | case | closed form | parameter and range | unit axis |
|---|---|---|---|---|---|---|---|---|
| 1 | $r$ | scale | $1$ | $\exp(\ln\lvert q\rvert)$ | hyperbolic | $\lvert q\rvert$ | $\lvert q\rvert > 0$ | — |
| 2 | $u$ | sign | $0$ | — | discrete | $\pm1$ | $u = \pm1$ | — |
| 3 | $\exp(s\varepsilon)$ | shear | $1$ | $\exp(s\varepsilon)$ | parabolic | $1 + s\varepsilon$ | $s = q'/q \in \mathbb{R}$ | $\varepsilon$ |

The exponent follows the rule of the series: the character of the exponential is trigonometric, hyperbolic or parabolic according to the square of the root of the exponent, the trigonometric case for a root of $-1$, the hyperbolic for a root of $+1$, and the parabolic for a nilpotent root, where the series truncates to the unit plus the exponent. The dual numbers have no root of $-1$ and none of $+1$, so the trigonometric and hyperbolic rows are empty and the parabolic row is the only one occupied; the shear is the exponential $\exp(s\varepsilon) = 1 + s\varepsilon$ of the nilpotent $\varepsilon$. The sign $u$ is discrete and is not an exponential. The algebra is commutative, so the three factors commute, the order is free, and the two exponents **amalgamate into one**, $Q = \exp(\ln\lvert q\rvert + s\varepsilon)$, for an element of positive real part; the sign is the one component the exponential does not reach.

## The Modulus

### The Norm

The norm is $\langle Q\rangle = Q\bar Q = q^2$, multiplicative and degenerate, with vanishing locus the maximal ideal $\mathrm{M}$; this is established in *Dual-Numbers Norm and Invertibility*. On a unit it is a nonzero element of $R$, and over $\mathbb{R}$ it is a positive real number.

### The Square Root and the Branch

**Definition.** The **modulus** of $Q = q + \varepsilon q'$ over $\mathbb{R}$ is

$$
r(Q) = \sqrt{|\langle Q\rangle|} = \sqrt{q^2} = |q|.
$$

The modulus takes values in $\mathbb{R}_{\ge 0}$ and is the continuous multiplicative function on the units that equals $|\lambda|$ on the real scalars and is invariant under the shear group, by the theorem of *Dual-Numbers Norm and Invertibility*; those two requirements characterise it, and without the shear-invariance it is one of a one-parameter family. It is a genuine positive scale on the units and vanishes on the maximal ideal.

### The Sign

**Definition.** Over $\mathbb{R}$ the **sign** of a unit $Q = q + \varepsilon q'$ is

$$
u(Q) = \operatorname{sgn}(q) \in \{\pm 1\}.
$$

It is the discrete part of the real scale, and it distinguishes the two connected components of $(\mathbb{D}')^\times$.

## The Nilpotent Central Factor

### The Element of Real Part One

**Definition.** The **unit shear** attached to a real number $s$ is

$$
\exp(s\varepsilon) := \exp(s\varepsilon) = 1 + s\varepsilon \in 1 + \mathrm{M}.
$$

The exponential is polynomial because $(s\varepsilon)^2 = 0$; the series terminates after its second term.

### The Closed Form of the Shear

**Proposition.** The map $s \mapsto \exp(s\varepsilon)$ is an isomorphism of groups $(\mathbb{R},+) \to 1 + \mathrm{M}$, and it is a homeomorphism onto the shear group.

**Proof.** $\exp(s\varepsilon)\exp(t\varepsilon) = (1 + s\varepsilon)(1 + t\varepsilon) = 1 + (s+t)\varepsilon = \exp((s+t)\varepsilon)$, and the inverse is $s \mapsto s\varepsilon$ under the dual logarithm.

### The Parabolic Angle

**Definition.** If $Q = q + \varepsilon q'$ is a unit, the **parabolic angle** of $Q$ is

$$
s(Q) = \frac{q'}{q} \in \mathbb{R}.
$$

The angle is the parameter of the shear factor: $Q = q\,\exp((q'/q)\varepsilon)$. It is additive under multiplication, since $s(Q_1 Q_2) = s(Q_1) + s(Q_2)$ when the scale is one, and it is globally defined without period.

## The Theorem

### Statement

**Theorem.** Let $R$ be an ordered commutative ring with $2$ invertible, and let $Q = q + \varepsilon q'$ be a unit, so that $q \in R^\times$. Then $Q$ has a unique representation

$$
Q = r\,u\,\exp(s\varepsilon), \qquad r > 0, \quad u \in \{\pm 1\}, \quad s \in R,
$$

with $r = |q|$, $u = \operatorname{sgn}(q)$ and $s = q^{-1}q'$. Over an ordered field, in particular over $R = \mathbb{R}$, the hypothesis is simply $q \neq 0$.

### Existence

Since $q$ is a unit, one has $q = r\,u$ with $r = |q| > 0$ and $u = \operatorname{sgn}(q)$, a nonzero element of an ordered ring being positive or negative, and then

$$
Q = q\Bigl(1 + q^{-1}\varepsilon q'\Bigr) = r\,u\,\exp\bigl(q^{-1}\varepsilon q'\bigr),
$$

using $\exp(s\varepsilon) = 1 + s\varepsilon$. So the polar data exist for every unit.

### Uniqueness

Suppose $r\,u\,\exp(s\varepsilon) = r'\,u'\,\exp(s'\varepsilon)$ with $r, r' > 0$ and $u, u' \in \{\pm 1\}$. Comparing real parts gives $ru = r'u'$, hence $r = r'$ and $u = u'$ by positivity and the sign; comparing infinitesimal parts gives $rus = r'u's'$, hence $s = s'$. So the data are unique.

### The Domain and the Boundary

The domain of the polar decomposition is the set of units, $\mathbb{D}' \setminus \mathrm{M}$, an open dense subset with two connected components, distinguished by the sign $u$. Its boundary is the maximal ideal $\mathrm{M}$, on which the representation fails. The polar data are the two coordinates $(r, s)$ on each component together with the discrete sign: a cylinder-like pair of half-planes, the exact degeneration of the disc-like parametrisation of the complex case.

## The Algorithm

Given a unit $Q = q + \varepsilon q'$ with $q \in R^\times$ (over a field, $q \neq 0$), the polar data are computed as follows.

1. **Real part.** Read $q = \operatorname{Re} Q$.
2. **Modulus.** Set $r = |q|$.
3. **Sign.** Set $u = \operatorname{sgn}(q)$, so that $q = ru$.
4. **Angle.** Set $s = q^{-1}q'$.
5. **Reassembly.** Output $Q = r\,u\,(1 + s\varepsilon)$.

The algorithm is exact in rational arithmetic when $q$ and $q'$ are rational; no transcendental quantity is produced, because the exponential is polynomial.

## A Worked Example

Take $Q = 2 + 3\varepsilon$.

1. $q = 2$.
2. $r = |2| = 2$.
3. $u = \operatorname{sgn}(2) = 1$.
4. $s = 3/2$.
5. $Q = 2\cdot 1\cdot(1 + \tfrac{3}{2}\varepsilon) = 2 + 3\varepsilon$.

Take $Q = -4 + \varepsilon$.

1. $q = -4$.
2. $r = 4$.
3. $u = \operatorname{sgn}(-4) = -1$.
4. $s = 1/(-4) = -\tfrac{1}{4}$.
5. $Q = 4\cdot(-1)\cdot(1 - \tfrac{1}{4}\varepsilon) = -4 + \varepsilon$.

Take $Q = 3\varepsilon$. Then $q = 0$, no modulus is defined, and the polar decomposition fails: the element lies on the boundary $\mathrm{M}$ and is a zero divisor.

## The Factors and Their Meanings

| Factor | Symbol | Range | Meaning |
|---|---|---|---|
| Scale | $r = |q|$ | $\mathbb{R}_{>0}$ | the unique real modulus |
| Sign | $u = \operatorname{sgn}(q)$ | $\{\pm 1\}$ | the component of the unit group |
| Shear | $\exp(s\varepsilon)$ | $1 + \mathrm{M}$ | the nilpotent central factor |
| Parabolic angle | $s = q'/q$ | $\mathbb{R}$ | the additive shear parameter |

The scale and the sign give the real factor $q = ru$; the shear gives the nilpotent factor $\exp(s\varepsilon)$. The two are independent, and their product is the whole unit.

### The Scale

The scale $r = |q|$ is the continuous multiplicative real size on the units normalised by $|\lambda|$ on the scalars and invariant under the shear; it is the degeneration of the complex modulus $\sqrt{a^2 + a'^2}$ and of the split-complex modulus $\sqrt{|a^2 - a'^2|}$. In the dual case the modulus loses its dependence on the second coordinate entirely, which is the analytic face of the degeneracy of the norm.

### The Central Factor

The factor $\exp(s\varepsilon)$ is central because the algebra is commutative, and it is nilpotent-off-the-identity because $\varepsilon$ is nilpotent. It plays the role that the complex phase $\exp(i\theta)$ plays in the complex polar form; the difference is that here the phase generator is nilpotent, so the "phase" is a shear and not a rotation.

## Degenerate Cases

### The Nilpotent Elements

For $Q = \varepsilon q'$ with $q' \neq 0$ the real part vanishes, $r = 0$, and no polar data exist; the polar decomposition degenerates on the entirety of the punctured maximal ideal. This is the boundary of the domain.

### The Real Elements

For $Q = q$ real, $q \neq 0$, the angle is $s = 0$ and $Q = r\,u\,\exp(0) = ru$; the polar form reduces to the modulus and the sign.

### The Pure Shears

For $Q = 1 + s\varepsilon$ the modulus is $r = 1$ and the sign is $u = 1$, so $Q = \exp(s\varepsilon)$; the pure shears are exactly the norm-one elements of positive real part.

### The Negative Real Axis

For $Q = -1 + s\varepsilon$ the modulus is $r = 1$ and the sign is $u = -1$; the element lies in the other component of the unit group, and there is no continuous way to pass between the components, since the shear parameter does not distinguish them.

## Relation to the Two Partial Forms

The dual polar form is the common degeneration of the complex and split-complex forms. Writing the complex modulus and angle as $\rho = \sqrt{a^2 + a'^2}$ and $\theta = \arctan(a'/a)$, and the split-complex modulus and rapidity as $\rho = \sqrt{|a^2 - a'^2|}$ and $\psi = \operatorname{artanh}(a'/a)$, the dual form is obtained by sending the second-coordinate contribution to zero:

$$
\rho \longrightarrow |q|, \qquad \theta \text{ or } \psi \longrightarrow s = \frac{q'}{q}, \qquad \exp(i\theta) \text{ or } \exp(\psi j) \longrightarrow 1 + s\varepsilon.
$$

The two transcendental functions $\theta$ and $\psi$ collapse to the rational function $q'/q$, and the two compact or non-compact rotations collapse to the shear. In the family of the three two-dimensional algebras, the dual polar form is the third and last row, and it is the only one whose exponential is polynomial.

## The Series of Polar Decompositions

The polar decompositions of the number systems of the corpus form a series, of which the dual case is one member.

| Algebra | Norm | Modulus | Phase factor | Kind |
|---|---|---|---|---|
| $\mathbb{C}$ | $a^2 + a'^2$ | $\sqrt{a^2+a'^2}$ | $\exp(i\theta)$ | elliptic |
| $\mathbb{D} = \mathbb{R}[j]$ | $a^2 - a'^2$ | $\sqrt{|a^2-a'^2|}$ | $\exp(\psi j)$ | hyperbolic |
| $\mathbb{D}'$ | $q^2$ | $|q|$ | $1 + s\varepsilon$ | parabolic |

The dual row is the missing link between the two two-dimensional cases: it is the case whose norm is degenerate, and it is the only member of the series whose polar phase factor is nilpotent. Reading down the column of phase factors, one passes from a compact circle, to a hyperbola, to a line; the dual line is the unique entry with no compact part and no period, and the series is exhaustive for the two-dimensional algebras in the same way that the rule is exhaustive for a generator of a one-parameter group.

## Summary

The polar decomposition of the dual-number algebra is

$$
Q = r\,u\,\exp(s\varepsilon), \qquad r = |q| > 0, \quad u = \operatorname{sgn}(q) \in \{\pm 1\}, \quad s = \frac{q'}{q},
$$

for every dual number $Q = q + \varepsilon q'$ with $q \neq 0$. It has a single positive scale $r = |q|$, the continuous multiplicative real size on the units normalised on the scalars and invariant under the shear; a discrete sign $u$; and a single **nilpotent central factor** $\exp(s\varepsilon) = 1 + s\varepsilon$ whose parameter is the **parabolic angle** $s = q'/q$, additive, globally defined and without period. Because the algebra is commutative the factor is central, and because the generator is nilpotent the exponential is polynomial and the factor is a shear rather than a rotation. The representation exists and is unique for every element with invertible real part; its domain is the set of units and its boundary is the maximal ideal $\mathrm{M}$, where the modulus tends to zero and the representation degenerates. The dual case is the third and last case of the exponential rule — elliptic, hyperbolic, parabolic — and the missing link of the polar series: it is the two-dimensional row with a degenerate norm and no compact phase, the common degeneration of the complex and split-complex polar forms, and the transitional two-dimensional member of the series.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra over $R$; $\varepsilon^2 = 0$ |
| $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$ | Dual-number algebra over $\mathbb{R}$ |
| $\mathbb{D}$ | Split-complex algebra, unit $j$, $j^2 = +1$ |
| $Q = q + \varepsilon q'$ | General dual number |
| $q = \operatorname{Re} Q$, $q' = \operatorname{Inf} Q$ | Real and infinitesimal parts |
| $\bar{Q} = q - \varepsilon q'$ | Dual conjugation |
| $\langle Q\rangle = Q\bar Q = q^2$ | Norm |
| $r = |q|$ | Modulus, real size on the units (shear-invariant) |
| $u = \operatorname{sgn}(q)$ | Sign, component of the unit group |
| $\mathrm{M} = (\varepsilon)$ | Maximal ideal, boundary of the polar domain |
| $1 + \mathrm{M}$ | Shear group, image of $s \mapsto \exp(s\varepsilon)$ |
| $\exp(s\varepsilon) = 1 + s\varepsilon$ | Nilpotent central factor |
| $s = q^{-1}q'$ | Parabolic angle |

## Further Reading

- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, New York, 1968), for the polar forms of the complex, split-complex and dual algebras and their degeneration.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, London, 2012), for the elliptic–parabolic–hyperbolic trichotomy of one-parameter subgroups.
- Erdal Inönü and Eugene P. Wigner, "On the contraction of groups and their representations", *Proceedings of the National Academy of Sciences of the USA* **39** (1953) 510–524, for the contraction that produces the parabolic case as a limit of the elliptic and hyperbolic cases.
- Eduard Study, *Geometrie der Dynamen* (Teubner, Leipzig, 1903), for the classical parametrisation of the dual numbers.
