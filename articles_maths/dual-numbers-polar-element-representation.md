
# __Dual-Numbers Polar Element Representation__

## Introduction

This article develops the polar representation of the dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$. It follows *Dual-Numbers Algebra* for the conventions, *Dual-Numbers Norm and Invertibility* for the norm and the real size function on the units, *Shears and Parabolic Rotations* for the group of units and the shear, and *Dual-Numbers Exponential and Lie Group Structure* for the exponential. Its structural model is *The Polar Element Representation of Biquaternions*.

The polar representation of the dual numbers is the **third and last row of the exponential trichotomy** and the **missing link of the polar series**. The trichotomy is the classification of a generator $\nu$ of a one-parameter group by the sign of $\nu^2$: for $\nu^2 = -1$ the exponential winds, giving the elliptic case; for $\nu^2 = +1$ it boosts, giving the hyperbolic case; for $\nu^2 = 0$ it shears, giving the parabolic case. The dual-number generator $\varepsilon$ has $\varepsilon^2 = 0$, and its row of the trichotomy is the parabolic one. The polar series of the family of number systems — complex, split complex, dual, quaternion, split quaternion, biquaternion, split biquaternion — is completed by this row; the dual case is the only one whose polar form has a nilpotent factor and no compact phase, and it is the link between the two-dimensional and higher-dimensional forms.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Throughout, $R$ is a commutative ring with identity in which $2$ is invertible; the field specialisation $R = k$ is flagged, and the ordered and geometric specialisation is $R = \mathbb{R}$, in which case the algebra is written $\mathbb{D}'$. A general dual number is

$$
A = a + \varepsilon a', \qquad a, a' \in R,
$$

with $a = \operatorname{Re} A$, $a' = \operatorname{Inf} A$, dual conjugation $\bar A = a - \varepsilon a'$, norm $N(A) = A\bar A = a^2$, maximal ideal $\mathrm{M} = (\varepsilon)$, real submodule $R_{\mathbb{D}'}$ and infinitesimal submodule $\varepsilon R_{\mathbb{D}'}$.

## Why a Single Scale and a Single Nilpotent Factor

### The Counting

The algebra $\mathbb{D}'_{\mathbb{R}}$ has real dimension two. The group of units is, by *Dual-Numbers Norm and Invertibility*, a semidirect product that is in fact a direct product,

$$
(\mathbb{D}')^\times \cong \mathbb{R}^\times \times (\mathbb{R}, +),
$$

of real dimension two. A polar representation writes every element of a group as a product of independent one-parameter factors; for a two-dimensional abelian group the natural count is therefore two factors, and they are a scale and a shear.

| Factor | Dimension | Range | Role |
|---|---|---|---|
| Scale | $1$ | $r > 0$ | modulus $|a|$ |
| Sign | $0$ | $\{\pm 1\}$ | the order-two component of $\mathbb{R}^\times$ |
| Shear | $1$ | $s \in \mathbb{R}$ | parabolic angle $s = a'/a$ |

So there is one positive scale, one discrete sign, and one real angle, and the angle is not a compact phase but a shear parameter.

### The Absence of a Compact Phase

In the complex case the unit group contains the circle $U(1)$, whose parameter is an angle modulo $2\pi$; in the split-complex case it contains a hyperbola, whose parameter is an unbounded rapidity; in the dual case the non-scalar factor is the shear group $1 + \mathrm{M} \cong (\mathbb{R}, +)$, a line. There is no compact one-parameter subgroup of $(\mathbb{D}')^\times$ other than the central $\{\pm 1\}$, so the polar form has no angle modulo anything: it has a single real parabolic angle, globally defined and without period. This is why *the exponential trichotomy ends in a straight line rather than a circle*.

### The Centrality of the Nilpotent

Because $\mathbb{D}'_R$ is commutative, every element is central, and in particular the nilpotent $\varepsilon$ is central and the shear factor $\exp(s\varepsilon) = 1 + s\varepsilon$ is central. In the biquaternion algebra the corresponding polar phase is the central imaginary unit $i$, a central *unit*; in the dual algebra the phase-like factor is central but *nilpotent*, so it cannot be extracted by a logarithm taking values in a torus. The centrality is what makes the order of the factors in the polar form immaterial here.

## The Trichotomy of the Exponential

Let $\nu$ be an element of a real associative algebra and consider the one-parameter group $t \mapsto \exp(t\nu)$. The behaviour of the group is governed by $\nu^2$.

- **Elliptic** ($\nu^2 = -\mathrm{id}$ up to scale): the exponential is periodic, the group is compact, and it is conjugate to the circle $U(1)$. This is the complex case, with the phase angle modulo $2\pi$.
- **Hyperbolic** ($\nu^2 = +\mathrm{id}$ up to scale): the exponential is unbounded and its graph is a hyperbola, the group is non-compact, and the parameter is a rapidity defined up to no period. This is the split-complex case.
- **Parabolic** ($\nu^2 = 0$): the exponential is polynomial, its image is a line of unipotent elements, and the group is non-compact and torsion-free. This is the dual case.

The trichotomy is exhaustive for a generator of square $\sigma\,\mathrm{id}$ with $\sigma$ real, since $\sigma$ is negative, positive or zero. The dual-number polar representation is the parabolic row, and it is the only row in which the exponential is algebraic rather than transcendental.

## The Modulus

### The Norm

The norm is $N(A) = A\bar A = a^2$, multiplicative and degenerate, with vanishing locus the maximal ideal $\mathrm{M}$; this is established in *Dual-Numbers Norm and Invertibility*. On a unit it is a nonzero element of $R$, and over $\mathbb{R}$ it is a positive real number.

### The Square Root and the Branch

**Definition.** The **modulus** of $A = a + \varepsilon a'$ over $\mathbb{R}$ is

$$
r(A) = \sqrt{|N(A)|} = \sqrt{a^2} = |a|.
$$

The modulus takes values in $\mathbb{R}_{\ge 0}$ and is the continuous multiplicative function on the units that equals $|\lambda|$ on the real scalars and is invariant under the shear group, by the theorem of *Dual-Numbers Norm and Invertibility*; those two requirements characterise it, and without the shear-invariance it is one of a one-parameter family. It is a genuine positive scale on the units and vanishes on the maximal ideal.

### The Sign

**Definition.** Over $\mathbb{R}$ the **sign** of a unit $A = a + \varepsilon a'$ is

$$
u(A) = \operatorname{sgn}(a) \in \{\pm 1\}.
$$

It is the discrete part of the real scale, and it distinguishes the two connected components of $(\mathbb{D}')^\times$.

## The Nilpotent Central Factor

### The Element of Real Part One

**Definition.** The **unit shear** attached to a real number $s$ is

$$
e^{s\varepsilon} := \exp(s\varepsilon) = 1 + s\varepsilon \in 1 + \mathrm{M}.
$$

The exponential is polynomial because $(s\varepsilon)^2 = 0$; the series terminates after its second term.

### The Closed Form of the Shear

**Proposition.** The map $s \mapsto e^{s\varepsilon}$ is an isomorphism of groups $(\mathbb{R},+) \to 1 + \mathrm{M}$, and it is a homeomorphism onto the shear group.

**Proof.** $e^{s\varepsilon}e^{t\varepsilon} = (1 + s\varepsilon)(1 + t\varepsilon) = 1 + (s+t)\varepsilon = e^{(s+t)\varepsilon}$, and the inverse is $s \mapsto s\varepsilon$ under the dual logarithm.

### The Parabolic Angle

**Definition.** If $A = a + \varepsilon a'$ is a unit, the **parabolic angle** of $A$ is

$$
s(A) = \frac{a'}{a} \in \mathbb{R}.
$$

The angle is the parameter of the shear factor: $A = a\,e^{(a'/a)\varepsilon}$. It is additive under multiplication, since $s(AB) = s(A) + s(B)$ when the scale is one, and it is globally defined without period.

## The Theorem

### Statement

**Theorem.** Let $R$ be an ordered commutative ring with $2$ invertible, and let $A = a + \varepsilon a'$ be a unit, so that $a \in R^\times$. Then $A$ has a unique representation

$$
A = r\,u\,\exp(s\varepsilon), \qquad r > 0, \quad u \in \{\pm 1\}, \quad s \in R,
$$

with $r = |a|$, $u = \operatorname{sgn}(a)$ and $s = a^{-1}a'$. Over an ordered field, in particular over $R = \mathbb{R}$, the hypothesis is simply $a \neq 0$.

### Existence

Since $a$ is a unit, one has $a = r\,u$ with $r = |a| > 0$ and $u = \operatorname{sgn}(a)$, a nonzero element of an ordered ring being positive or negative, and then

$$
A = a\Bigl(1 + a^{-1}\varepsilon a'\Bigr) = r\,u\,\exp\bigl(a^{-1}\varepsilon a'\bigr),
$$

using $\exp(s\varepsilon) = 1 + s\varepsilon$. So the polar data exist for every unit.

### Uniqueness

Suppose $r\,u\,e^{s\varepsilon} = r'\,u'\,e^{s'\varepsilon}$ with $r, r' > 0$ and $u, u' \in \{\pm 1\}$. Comparing real parts gives $ru = r'u'$, hence $r = r'$ and $u = u'$ by positivity and the sign; comparing infinitesimal parts gives $rus = r'u's'$, hence $s = s'$. So the data are unique.

### The Domain and the Boundary

The domain of the polar representation is the set of units, $\mathbb{D}' \setminus \mathrm{M}$, an open dense subset with two connected components, distinguished by the sign $u$. Its boundary is the maximal ideal $\mathrm{M}$, on which the representation fails. The polar data are the two coordinates $(r, s)$ on each component together with the discrete sign: a cylinder-like pair of half-planes, the exact degeneration of the disc-like parametrisation of the complex case.

## The Algorithm

Given a unit $A = a + \varepsilon a'$ with $a \in R^\times$ (over a field, $a \neq 0$), the polar data are computed as follows.

1. **Real part.** Read $a = \operatorname{Re} A$.
2. **Modulus.** Set $r = |a|$.
3. **Sign.** Set $u = \operatorname{sgn}(a)$, so that $a = ru$.
4. **Angle.** Set $s = a^{-1}a'$.
5. **Reassembly.** Output $A = r\,u\,(1 + s\varepsilon)$.

The algorithm is exact in rational arithmetic when $a$ and $a'$ are rational; no transcendental quantity is produced, because the exponential is polynomial.

## A Worked Example

Take $A = 2 + 3\varepsilon$.

1. $a = 2$.
2. $r = |2| = 2$.
3. $u = \operatorname{sgn}(2) = 1$.
4. $s = 3/2$.
5. $A = 2\cdot 1\cdot(1 + \tfrac{3}{2}\varepsilon) = 2 + 3\varepsilon$.

Take $A = -4 + \varepsilon$.

1. $a = -4$.
2. $r = 4$.
3. $u = \operatorname{sgn}(-4) = -1$.
4. $s = 1/(-4) = -\tfrac{1}{4}$.
5. $A = 4\cdot(-1)\cdot(1 - \tfrac{1}{4}\varepsilon) = -4 + \varepsilon$.

Take $A = 3\varepsilon$. Then $a = 0$, no modulus is defined, and the polar representation fails: the element lies on the boundary $\mathrm{M}$ and is a zero divisor.

## The Factors and Their Meanings

| Factor | Symbol | Range | Meaning |
|---|---|---|---|
| Scale | $r = |a|$ | $\mathbb{R}_{>0}$ | the unique real modulus |
| Sign | $u = \operatorname{sgn}(a)$ | $\{\pm 1\}$ | the component of the unit group |
| Shear | $e^{s\varepsilon}$ | $1 + \mathrm{M}$ | the nilpotent central factor |
| Parabolic angle | $s = a'/a$ | $\mathbb{R}$ | the additive shear parameter |

The scale and the sign give the real factor $a = ru$; the shear gives the nilpotent factor $e^{s\varepsilon}$. The two are independent, and their product is the whole unit.

### The Scale

The scale $r = |a|$ is the continuous multiplicative real size on the units normalised by $|\lambda|$ on the scalars and invariant under the shear; it is the degeneration of the complex modulus $\sqrt{a^2 + a'^2}$ and of the split-complex modulus $\sqrt{|a^2 - a'^2|}$. In the dual case the modulus loses its dependence on the second coordinate entirely, which is the analytic face of the degeneracy of the norm.

### The Central Factor

The factor $e^{s\varepsilon}$ is central because the algebra is commutative, and it is nilpotent-off-the-identity because $\varepsilon$ is nilpotent. It plays the role that the complex phase $e^{i\theta}$ plays in the complex polar form and that the central imaginary unit $i$ plays in the biquaternion form; the difference is that here the phase generator is nilpotent, so the "phase" is a shear and not a rotation.

## Degenerate Cases

### The Nilpotent Elements

For $A = \varepsilon a'$ with $a' \neq 0$ the real part vanishes, $r = 0$, and no polar data exist; the polar representation degenerates on the entirety of the punctured maximal ideal. This is the boundary of the domain.

### The Real Elements

For $A = a$ real, $a \neq 0$, the angle is $s = 0$ and $A = r\,u\,e^{0} = ru$; the polar form reduces to the modulus and the sign.

### The Pure Shears

For $A = 1 + s\varepsilon$ the modulus is $r = 1$ and the sign is $u = 1$, so $A = e^{s\varepsilon}$; the pure shears are exactly the norm-one elements of positive real part.

### The Negative Real Axis

For $A = -1 + s\varepsilon$ the modulus is $r = 1$ and the sign is $u = -1$; the element lies in the other component of the unit group, and there is no continuous way to pass between the components, since the shear parameter does not distinguish them.

## Relation to the Two Partial Forms

The dual polar form is the common degeneration of the complex and split-complex forms. Writing the complex modulus and angle as $\rho = \sqrt{a^2 + a'^2}$ and $\theta = \arctan(a'/a)$, and the split-complex modulus and rapidity as $\rho = \sqrt{|a^2 - a'^2|}$ and $\psi = \operatorname{artanh}(a'/a)$, the dual form is obtained by sending the second-coordinate contribution to zero:

$$
\rho \longrightarrow |a|, \qquad \theta \text{ or } \psi \longrightarrow s = \frac{a'}{a}, \qquad e^{i\theta} \text{ or } e^{\psi j} \longrightarrow 1 + s\varepsilon.
$$

The two transcendental functions $\theta$ and $\psi$ collapse to the rational function $a'/a$, and the two compact or non-compact rotations collapse to the shear. In the family of the three two-dimensional algebras, the dual polar form is the third and last row, and it is the only one whose exponential is polynomial.

## The Series of Polar Representations

The polar representations of the number systems of the corpus form a series, of which the dual case is one member.

| Algebra | Norm | Modulus | Phase factor | Kind |
|---|---|---|---|---|
| $\mathbb{C}$ | $a^2 + a'^2$ | $\sqrt{a^2+a'^2}$ | $e^{i\theta}$ | elliptic |
| $\mathbb{D} = \mathbb{R}[j]$ | $a^2 - a'^2$ | $\sqrt{|a^2-a'^2|}$ | $e^{\psi j}$ | hyperbolic |
| $\mathbb{D}'$ | $a^2$ | $|a|$ | $1 + s\varepsilon$ | parabolic |
| $\mathbb{H}$ | $a^2 + \|\vec v\|^2$ | $\|Q\|$ | unit sphere | spherical |
| $\mathbb{H}_{\mathrm{s}}$ | $a^2 + b^2 - c^2 - d^2$ | $\sqrt{|\cdot|}$ | one-sheeted hyperboloid | hyperbolic |
| $\mathbb{B}$ | $Q_0^2 + \|\vec Q\|^2$ (complex) | $\sqrt{|N|}$ | $U(1)\times SU(2)$ | elliptic–spherical |
| $\mathbb{H}_{\mathbb{D}}$ | split signature | $\sqrt{|\cdot|}$ | $SL(2,\mathbb{R})$-type | mixed |

The dual row is the missing link between the two-dimensional cases and the quaternionic cases: it is the two-dimensional case whose norm is degenerate, and it is the only member of the series whose polar phase factor is nilpotent. Reading down the column of phase factors, one passes from a compact circle, to a hyperbola, to a line, then to a three-sphere and its indefinite analogues; the dual line is the unique entry with no compact part and no period, and the whole series is exhaustive for the algebras of the corpus in the same way that the trichotomy is exhaustive for a generator of a one-parameter group.

## Summary

The polar representation of the dual-number algebra is

$$
A = r\,u\,\exp(s\varepsilon), \qquad r = |a| > 0, \quad u = \operatorname{sgn}(a) \in \{\pm 1\}, \quad s = \frac{a'}{a},
$$

for every dual number $A = a + \varepsilon a'$ with $a \neq 0$. It has a single positive scale $r = |a|$, the continuous multiplicative real size on the units normalised on the scalars and invariant under the shear; a discrete sign $u$; and a single **nilpotent central factor** $e^{s\varepsilon} = 1 + s\varepsilon$ whose parameter is the **parabolic angle** $s = a'/a$, additive, globally defined and without period. Because the algebra is commutative the factor is central, and because the generator is nilpotent the exponential is polynomial and the factor is a shear rather than a rotation. The representation exists and is unique for every element with invertible real part; its domain is the set of units and its boundary is the maximal ideal $\mathrm{M}$, where the modulus tends to zero and the representation degenerates. The dual case is the third and last row of the exponential trichotomy — elliptic, hyperbolic, parabolic — and the missing link of the polar series: it is the two-dimensional row with a degenerate norm and no compact phase, the common degeneration of the complex and split-complex polar forms, and the transitional two-dimensional member of the series that continues with the quaternion, split-quaternion, biquaternion and split-biquaternion forms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra over $R$; $\varepsilon^2 = 0$ |
| $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$ | Dual-number algebra over $\mathbb{R}$ |
| $\mathbb{D}$ | Split-complex algebra, unit $j$, $j^2 = +1$ |
| $A = a + \varepsilon a'$ | General dual number |
| $a = \operatorname{Re} A$, $a' = \operatorname{Inf} A$ | Real and infinitesimal parts |
| $\bar{A} = a - \varepsilon a'$ | Dual conjugation |
| $N(A) = A\bar A = a^2$ | Norm |
| $r = |a|$ | Modulus, real size on the units (shear-invariant) |
| $u = \operatorname{sgn}(a)$ | Sign, component of the unit group |
| $\mathrm{M} = (\varepsilon)$ | Maximal ideal, boundary of the polar domain |
| $1 + \mathrm{M}$ | Shear group, image of $s \mapsto e^{s\varepsilon}$ |
| $e^{s\varepsilon} = 1 + s\varepsilon$ | Nilpotent central factor |
| $s = a^{-1}a'$ | Parabolic angle |
| $\mathbb{B}$ | Biquaternion algebra, the model of the polar series |
| $\mathbb{H}_{\mathrm{s}}, \mathbb{H}_{\mathbb{D}}$ | Split quaternions and split biquaternions |

## Further Reading

- I. M. Yaglom, *Complex Numbers in Geometry* (Academic Press, New York, 1968), for the polar forms of the complex, split-complex and dual algebras and their degeneration.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, London, 2012), for the elliptic–parabolic–hyperbolic trichotomy of one-parameter subgroups.
- Erdal Inönü and Eugene P. Wigner, "On the contraction of groups and their representations", *Proceedings of the National Academy of Sciences of the USA* **39** (1953) 510–524, for the contraction that produces the parabolic case as a limit of the elliptic and hyperbolic cases.
- Eduard Study, *Geometrie der Dynamen* (Teubner, Leipzig, 1903), for the classical parametrisation of the dual numbers.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for the parallel analysis of the norms and unit groups across the number systems.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the four-factor polar representation of the biquaternion case.
