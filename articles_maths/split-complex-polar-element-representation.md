
# __Split-Complex Polar Element Representation__

## Introduction

This article is about the **polar representation** of a split-complex number: the statement that every split-complex number whose norm does not vanish is the product of a positive real scale and a unit split-complex number of norm $\pm1$, and the description of the unit factor as an exponential.

The algebra $\mathbb{D}$ is the two-dimensional *indefinite* algebra, and its polar representation is the companion of the definite case treated in *Complex Polar Element Representation*. The two algebras carry the same basis, the same conjugation and the same dimension, and differ in one sign, $j^2 = +1$ instead of $i^2 = -1$; the consequences for the polar representation are the three that organise this article. The norm is indefinite, so the modulus is a square root of an absolute value and the sign of the norm separates the algebra into two regimes with different unit factors. The unit factor is hyperbolic rather than trigonometric, so the unit group is not compact and its exponential is injective. And the norm vanishes on a pair of lines, so the polar representation has a genuine boundary, the null cone, which is at the same time the zero-divisor set of the algebra.

The plan is as follows. The norm and its three regions are recorded, the modulus and the unit set are defined, and existence and uniqueness are proved. The unit factor is then described as an exponential, and the exponential is organised by the same trichotomy $\nu^2 = -1$, $0$, $+1$ that governs the whole family, of which the split-complex algebra occupies exactly one row. The two regimes, the null cone, the group of units and the matrix picture follow, and worked examples close the article. The conventions are those of *Split-Complex Algebra*: the basis is $1$, $j$, the multiplication is $jj = +1$, the conjugate is $\bar{A} = a - j a'$, the norm is $N(A) = A\bar{A} = a^2 - a'^2$, and the idempotent basis is $\Pi_1 = (1+j)/2$, $\Pi_2 = (1-j)/2$. The hyperbolic angle and the unit hyperbola are those of *Hyperbolic Rotations*, whose polar decomposition $A = \rho u$ with $\rho > 0$ and $N(u) = \pm1$ this article reorganises into the slots of the family. Every numerical value displayed below was recomputed in double precision.

## The Norm and Its Three Regions

The norm of a split-complex number $A = a + j a'$ is

$$
N(A) = A\bar{A} = a^2 - a'^2 .
$$

It is multiplicative, $N(AB) = N(A)N(B)$, and indefinite of signature $(1,1)$. Its sign partitions the algebra into three regions, which are the three regions of the Lorentzian plane:

| region | condition | sign of $N(A)$ | name |
|---|---|---|---|
| spacelike | $\lvert a\rvert > \lvert a'\rvert$ | positive | the two sectors containing $\pm1$ |
| null | $\lvert a\rvert = \lvert a'\rvert$ | zero | the null cone, the zero-divisor set |
| timelike | $\lvert a\rvert < \lvert a'\rvert$ | negative | the two sectors containing $\pm j$ |

The null cone is the pair of lines $a = \pm a'$, that is, the two lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$ with the origin removed; it is also the zero-divisor set, since $N(A) = 0$ with $A \neq 0$ says exactly that $A$ is a nonzero element without an inverse. This single set is where the polar representation fails, and it is the first time in the family that the failure set of the representation is non-empty.

## The Modulus and the Unit Set

### The Two Factors

**Definition.** Let $A \in \mathbb{D}$ with $N(A) \neq 0$. The **polar representation** of $A$ is the writing

$$
A = \rho\,u, \qquad \rho \in \mathbb{R}, \quad \rho > 0, \qquad u \in \mathbb{D}, \quad \lvert N(u)\rvert = 1,
$$

in which $\rho$ is the **modulus** of $A$ and $u$ is its **unit factor**.

The modulus is a positive real, as in the complex case. The unit factor is constrained by $\lvert N(u)\rvert = 1$ rather than by $N(u) = 1$, and this is forced by the indefiniteness: a unit factor of norm $-1$ exists, while a general element of negative norm cannot be written with a unit factor of norm $+1$. The constraint is one real equation, so the unit factor carries one parameter out of the two of a general element, and the counts $1+1$ add to the real dimension two.

### The Modulus and the Regime

Taking norms in $A = \rho u$ gives $N(A) = \rho^2N(u)$, so $\lvert N(A)\rvert = \rho^2$ and

$$
\rho = \sqrt{\lvert N(A)\rvert} .
$$

The square root is again a non-negative real taken of a non-negative real, with no sign choice and no branch choice. Since $\rho > 0$, the sign of $N(u)$ is forced to be the sign of $N(A)$:

$$
\operatorname{sign}N(u) = \operatorname{sign}N(A),
$$

so the two regimes of the norm are the two regimes of the unit factor, and a single polar representation does not straddle them. In the idempotent coordinates $A = A_+\Pi_1 + A_-\Pi_2$ the norm is the product $N(A) = A_+A_-$, so the modulus is the geometric mean

$$
\rho = \sqrt{\lvert A_+A_-\rvert},
$$

which is the modulus of the companion article *Hyperbolic Rotations*, written there as the geometric mean of the two component moduli.

### Existence and Uniqueness

**Theorem.** Every split-complex number $A$ with $N(A) \neq 0$ has exactly one polar representation.

*Existence.* Put $\rho = \sqrt{\lvert N(A)\rvert}$ and $u = A/\rho$. Since $N(A) \neq 0$, $\rho > 0$, and $\lvert N(u)\rvert = \lvert N(A)\rvert/\rho^2 = 1$ because $N(\lambda A) = \lambda^2N(A)$ for real $\lambda$. Hence $A = \rho u$ with $\rho > 0$ and $\lvert N(u)\rvert = 1$.

*Uniqueness.* Suppose $A = \rho u = \rho'u'$ with $\rho, \rho' > 0$ and $\lvert N(u)\rvert = \lvert N(u')\rvert = 1$. Taking absolute values of the norm gives $\rho^2 = \lvert N(A)\rvert = \rho'^2$, so $\rho = \rho'$ because both are positive, and then $u = A/\rho = u'$.

The pair is unique and the modulus is forced; the freedom that remains is in the coordinate of the unit factor, and it is larger than in the complex case, the unit set $\lvert N\rvert = 1$ having four connected components rather than one.

## The Exponential Form

### The Unit Set and Its Four Branches

The unit set of $\mathbb{D}$ is

$$
\{u \in \mathbb{D} : \lvert N(u)\rvert = 1\} = \{N = 1\} \sqcup \{N = -1\},
$$

the union of the two hyperbolas, each with two branches. In the hyperbolic angle $\phi$ of *Hyperbolic Rotations*,

$$
N(u) = +1: \quad u = \pm e^{\phi j} = \pm\big(\cosh\phi + j\sinh\phi\big), \qquad N(u) = -1: \quad u = \pm j\,e^{\phi j} = \pm\big(\sinh\phi + j\cosh\phi\big),
$$

with $\phi \in \mathbb{R}$ in each case. The four signs and branches are the four connected components of the unit set, and each is a copy of the line. The two hyperbolas are exchanged by multiplication by $j$, which is the reflection $(a,a')\mapsto(a',a)$ in the line $a = a'$, and the two branches of each hyperbola are exchanged by the sign.

### The Trichotomy of the Exponential

The exponential of $\nu\phi$ is trigonometric, parabolic or hyperbolic according to the sign of $\nu^2$, the rule recorded in *Complex Polar Element Representation*. In $\mathbb{D}$ the trichotomy collapses to a single row, and the collapse is the content of the next table.

| equation | solutions in $\mathbb{D}$ | count | row of the trichotomy |
|---|---|---|---|
| $\nu^2 = -1$ | none | $0$ | trigonometric: absent |
| $\nu^2 = 0$ | $\nu = 0$ only | $1$ | parabolic: degenerate, $\exp = 1$ |
| $\nu^2 = +1$ | $\nu = \pm 1$ and $\nu = \pm j$ | $4$ | hyperbolic: the two branches |

The trigonometric row is empty because $\mathbb{D}$ has no root of $-1$: the equations $a^2+a'^2 = -1$ and $2aa' = 0$ are incompatible over the reals, so $\mathbb{D}$ carries no complex structure and admits no compact one-parameter subgroup of rotations. The parabolic row is degenerate because $\mathbb{D}$ has no nilpotent: the same two equations with $-1$ replaced by $0$ force $a = a' = 0$. The only live row is the hyperbolic one, and its four roots split into two kinds: $\pm1$ are the central directions, whose exponentials $e^{\pm\phi}$ are the two halves of the positive scale, and $\pm j$ are the non-scalar directions, whose exponentials are the unit hyperbolas.

### The Unit Factor as an Exponential

The unit factor of a split-complex number is therefore always a hyperbolic exponential:

$$
u = \epsilon\,e^{\phi j}, \qquad A = \rho\,\epsilon\,e^{\phi j}, \qquad \phi = \operatorname{artanh}\frac{a'}{a}, \qquad N(A) > 0,
$$

in the positive regime, and

$$
u = \epsilon\,j\,e^{\phi j}, \qquad A = \rho\,\epsilon\,\big(\sinh\phi + j\cosh\phi\big), \qquad \phi = \operatorname{artanh}\frac{a}{a'}, \qquad N(A) < 0,
$$

in the negative one, with $\epsilon = \pm1$ the branch sign. The two formulas are the two halves of the statement that the unit factor is an exponential of the direction $j$, multiplied by $j$ on the left in the second case.

### The Factor Is Central

In the biquaternion algebra the boost is a non-central factor, and its non-commutativity with the rotor is what makes the order of the four factors part of the statement. In $\mathbb{D}$ nothing of the kind occurs, because $\mathbb{D}$ is commutative, so *every* element is central, the hyperbolic factor included: $e^{\phi j}$ may be transposed with any other factor at no cost. The absence of a rotor slot in this algebra is the same fact seen from the other side. The factor is nevertheless non-trivial in its action: in the idempotent coordinates

$$
e^{\phi j}\big(A_+\Pi_1 + A_-\Pi_2\big) = e^{\phi}A_+\,\Pi_1 + e^{-\phi}A_-\,\Pi_2 ,
$$

verified on $A = 2 + 3j$, where $A_+ = 5$, $A_- = -1$ and both sides agree to $10^{-14}$: the hyperbolic factor scales the two idempotent coordinates by reciprocal positive factors. That squeeze is why the unit hyperbola is not a circle, and why the angle $\phi$ is not periodic.

## Position and Signature

The two independent dichotomies of the family — position with respect to the conjugation, and the sign of the square of the direction — place the split-complex unit factor in a slot that the definite algebra leaves empty.

| algebra | Hermitian direction | anti-Hermitian direction | occupied by the unit factor |
|---|---|---|---|
| $\mathbb{C}$ | $\nu = \pm1$, $\nu^2 = +1$: the scale | $\nu = \pm i$, $\nu^2 = -1$ | anti-Hermitian, signature $-1$: the circle |
| $\mathbb{D}$ | $\nu = \pm1$, $\nu^2 = +1$: the scale | $\nu = \pm j$, $\nu^2 = +1$ | anti-Hermitian, signature $+1$: the hyperbola |

In $\mathbb{D}$ the generator $j$ is anti-Hermitian, $\bar{j} = -j$, and has square $+1$, so the unit factor is the exponential of an anti-Hermitian direction of *hyperbolic* signature. This combination — the anti-Hermitian position with the $\nu^2 = +1$ signature — is the one that the definite algebras cannot produce: in $\mathbb{C}$ and in $\mathbb{H}$ the anti-Hermitian directions all have $\nu^2 = -1$, so every unit factor there is trigonometric and every unit group compact. In the biquaternion algebra the combination occurs, but on the Hermitian side, where it is the boost. The split-complex algebra is thus the smallest algebra of the family in which a unit factor is hyperbolic, and it exhibits the phenomenon without the non-commutativity that complicates the biquaternion case.

## The Null Cone: The Boundary of the Representation

The polar representation is defined on the complement of the null cone and nowhere else. If $N(A) = 0$ and $A \neq 0$ then $\rho = 0$, the unit factor $u = A/\rho$ does not exist, and no rescaling of $A$ has norm $\pm1$:

$$
A = 1 + j = 2\Pi_1, \qquad N(A) = 0, \qquad \Pi_1^2 = \Pi_1, \qquad \Pi_1\Pi_2 = 0 .
$$

The element $1+j$ is a positive real multiple of the idempotent $\Pi_1$, and the idempotents are the primitive zero divisors of the algebra; they are the two directions of the null cone. The boundary is therefore not a defect of the theorem but a property of the algebra: the modulus of a null element vanishes while the element does not, and the vanishing of the modulus is exactly the absence of the positive factor. This is the first appearance in the family of a boundary of the polar representation, and it is the phenomenon that the quaternion algebra does not have, that the split-quaternion and biquaternion algebras have on cones of their own, and that the split-biquaternion algebra does not have at all.

## The Group of Units

The group of units of $\mathbb{D}$ is the complement of the null cone, $\mathbb{D}^\times = \{A : N(A) \neq 0\}$, and the polar representation is its decomposition into the scale and the unit set, as in the complex case but with a unit set of four components:

$$
\mathbb{D}^\times \cong \mathbb{R}_{>0} \times \mathbb{R} \times (\mathbb{Z}/2\mathbb{Z})^2, \qquad A \longmapsto \Big(\rho,\ \phi,\ \operatorname{sign}A_+,\ \operatorname{sign}A_-\Big),
$$

the hyperbolic angle and the two signs being the coordinates of the unit factor and $\rho$ the modulus. The first factor is the scale, the second the hyperbolic angle, and the two signs the branch; the isomorphism is the polar representation read as a group isomorphism. The unit set is not compact, because the hyperbola is unbounded, and the exponential $\phi \mapsto e^{\phi j}$ is injective, with trivial kernel:

$$
e^{\phi j} = 1 \iff \phi = 0, \qquad \operatorname{Re}e^{\phi j} = \cosh\phi \geq 1,
$$

the real part recovering $\lvert\phi\rvert$ and the sign of the imaginary part recovering the sign of $\phi$. The angle is therefore a coordinate without a period, in contrast with the class modulo $2\pi$ of the complex case: the unit factor ranges over the circle $\mathbb{R}/2\pi\mathbb{Z}$ in the definite algebra and over the line $\mathbb{R}$ in the indefinite one.

## The Matrix Picture

### Multiplication by $j$ as a Reflection Form

In the real basis $\{1,j\}$ a split-complex number is the pair $(a,a')$ and multiplication by $A = a+j a'$ is the linear map

$$
M_A = \begin{pmatrix} a & a' \\ a' & a \end{pmatrix} = a\,I + a'\,J, \qquad J = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad J^2 = I .
$$

The matrix $J$ is a reflection, and $J^2 = I$ is the matrix form of $j^2 = +1$, so the single live row of the trichotomy of $\mathbb{D}$ is the row $J^2 = I$ of the matrix picture. The determinant and the trace are

$$
\det M_A = a^2 - a'^2 = N(A), \qquad \operatorname{tr}M_A = 2a,
$$

so the norm is again the determinant, and the modulus is $\rho = \sqrt{\lvert\det M_A\rvert}$. The polar representation becomes

$$
M_A = \rho\,M_u, \qquad M_u = \begin{pmatrix} \cosh\phi & \sinh\phi \\ \sinh\phi & \cosh\phi \end{pmatrix}, \qquad \det M_u = 1,
$$

and the matrices $M_u$ are the two-component hyperbola $SO(1,1)$, with the identity component $SO^+(1,1)$ for $\phi \in \mathbb{R}$. Inside the two-dimensional family $aI + bJ$ the polar decomposition is again the splitting of a matrix into a scalar and an isometry, but the isometry group is now non-compact, and the similarity it describes is a similarity of the Lorentzian plane: it preserves the indefinite form $N$ and not the Euclidean one.

| factor | matrix | determinant | isometry type |
|---|---|---|---|
| $\rho$ | $\rho I$, $\rho > 0$ | $\rho^2$ | similarity of ratio $\rho$ |
| $e^{\phi j}$ | hyperbolic rotation by $\phi$ | $1$ | Lorentzian isometry, $SO^+(1,1)$ |
| $A = \rho e^{\phi j}$ | conformal matrix of the Lorentzian plane | $\rho^2$ | similarity: hyperbolic rotation and scaling |

## Worked Examples

### The Positive Regime

Take $A = 5 + 3j$. Then $N(A) = 25 - 9 = 16 > 0$, so

$$
\rho = 4, \qquad \tanh\phi = \frac{a'}{a} = \frac{3}{5}, \qquad \phi = \operatorname{artanh}\frac{3}{5} = \ln 2 = 0.6931471805599453 ,
$$

and the unit factor is

$$
u = \frac{A}{\rho} = 1.25 + 0.75j, \qquad e^{\phi j} = \cosh\phi + j\sinh\phi = 1.25 + 0.75j,
$$

so that $A = 4e^{\phi j}$ exactly, with $\cosh\phi = 1.25$ and $\sinh\phi = 0.75$ verified to machine precision. In the idempotent coordinates $A_+ = 8$ and $A_- = 2$, the modulus is their geometric mean, $4 = \sqrt{16}$, and the hyperbolic angle is half the logarithm of their ratio, $\phi = \tfrac12\ln4 = \ln2$.

### The Negative Regime

Take $A = 1 + 2j$. Then $N(A) = 1 - 4 = -3 < 0$, so

$$
\rho = \sqrt{3} = 1.7320508075688772, \qquad \tanh\phi = \frac{a}{a'} = \frac{1}{2}, \qquad \phi = \operatorname{arsinh}\frac{1}{\sqrt3} = 0.5493061443340549 ,
$$

and the unit factor is on the hyperbola of norm minus one,

$$
u = \frac{A}{\rho} = 0.5773502691896258 + 1.1547005383792517\,j = \sinh\phi + j\cosh\phi = j\,e^{\phi j},
$$

with $\rho\sinh\phi = 1$ exactly and $\rho\cosh\phi = 2$ to one unit in the last place ($1.9999999999999998$). The same element written with a unit factor of norm $+1$ does not exist, which is the statement $\operatorname{sign}N(u) = \operatorname{sign}N(A)$ of the modulus section.

### The Boundary and the Degenerate Shapes

| $A$ | $N(A)$ | regime | $\rho$ | $u$ | $\phi$ |
|---|---|---|---|---|---|
| $2$ | $4$ | positive | $2$ | $1$ | $0$ |
| $-2$ | $4$ | positive | $2$ | $-1$ | $0$ |
| $j$ | $-1$ | negative | $1$ | $j$ | $0$ |
| $1+j$ | $0$ | null | — | — | no polar form |
| $\Pi_1$ | $0$ | null | — | — | no polar form |

The first two lines are the spacelike axis, with unit factor $\pm1$ and vanishing angle; the third is the timelike axis, with unit factor $j$ and vanishing angle, on the hyperbola of norm $-1$. The last two lines are the null cone: the modulus vanishes, the unit factor is undefined, and the two elements are the idempotent $\Pi_1$ and its double, which are zero divisors and not units.

## Comparison with the Other Members of the Series

| algebra | modulus | unit factor | unit group | boundary |
|---|---|---|---|---|
| $\mathbb{C}$ | $\sqrt{N}$, positive real | $e^{i\theta}$, $\theta$ mod $2\pi$ | compact, one component | none |
| $\mathbb{D}$ | $\sqrt{\lvert N\rvert}$, positive real | $e^{\phi j}$ or $je^{\phi j}$, $\phi \in \mathbb{R}$ | non-compact, four components | the null cone, $\{N = 0\}$ |
| $\mathbb{H}$ | $\sqrt{N}$, positive real | $S^3$ rotor | compact, one component | none |
| $\mathbb{H}_{\mathrm{s}}$ | $\sqrt{\lvert N\rvert}$ with two regimes | two-component unit group | non-compact | the null cone of the determinant form |
| $\mathbb{B}$ | $\sqrt{N}$, a branch of the complex square root | boost and rotor, phase central | non-compact | the complex null cone, $\{N = 0\}$ |

The progression from $\mathbb{C}$ to $\mathbb{D}$ is the exchange of one sign, and it changes the exponential from trigonometric to hyperbolic, the unit group from compact to non-compact, and the boundary from empty to the null cone. The split-complex algebra is the minimal model of the second kind, and it is the reason the family is presented in this order: every difficulty that the four-dimensional algebras present in a compounded form appears in $\mathbb{D}$ alone, where it can be separated from the non-commutativity that the quaternion and biquaternion algebras add.

## Summary

Every split-complex number $A$ with $N(A) \neq 0$ has exactly one polar representation $A = \rho u$, with modulus $\rho = \sqrt{\lvert N(A)\rvert} > 0$ and unit factor $u = A/\rho$ satisfying $\lvert N(u)\rvert = 1$. The sign of the norm is a regime, forced by $\operatorname{sign}N(u) = \operatorname{sign}N(A)$, and the unit set has four components: $u = \pm e^{\phi j}$ in the positive regime and $u = \pm je^{\phi j}$ in the negative one, with the hyperbolic angle $\phi$ a coordinate of the line. Of the three rows of the trichotomy $\nu^2 = -1$, $0$, $+1$, only the hyperbolic row is live in $\mathbb{D}$: there is no root of $-1$ and no nilpotent, so there is no trigonometric factor and no parabolic one, and the unit factor is an exponential of the anti-Hermitian direction $j$ of signature $+1$. That position and that signature together are what no definite algebra of the family can produce, and the split-complex algebra is the smallest in which a unit factor is hyperbolic. Every element is central, since $\mathbb{D}$ is commutative, so the factor may be transposed freely, unlike the biquaternion boost; the transpose is the same element. The unit group has four components and is not compact, and the exponential of the hyperbolic angle is injective, so the angle has no period. The polar representation is defined exactly on the complement of the null cone, which is the zero-divisor set, and the boundary is the first in the family to be non-empty: on it the modulus vanishes and the unit factor does not exist.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{D}$ | the split-complex algebra, basis $1$, $j$, $j^2 = +1$ |
| $A = a + j a'$ | a split-complex number, $a$ and $a'$ real |
| $\bar{A} = a - j a'$ | the split-complex conjugate |
| $N(A) = A\bar{A} = a^2-a'^2$ | the norm, indefinite of signature $(1,1)$ |
| $\Pi_{1,2} = (1\pm j)/2$ | the idempotent basis, $A = A_+\Pi_1 + A_-\Pi_2$ |
| $\rho = \sqrt{\lvert N(A)\rvert} = \sqrt{\lvert A_+A_-\rvert}$ | the modulus, a positive real |
| $u = A/\rho$ | the unit factor, $\lvert N(u)\rvert = 1$ |
| $\phi$ | the hyperbolic angle or rapidity, $\phi \in \mathbb{R}$ |
| $\epsilon$ | the branch sign, $\pm1$ |
| $J = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ | the reflection matrix of multiplication by $j$; $J^2 = I$, the matrix form of $j^2 = +1$ |
| $M_A = a\,I + a'\,J$ | matrix of multiplication by $A$, $\begin{pmatrix} a & a' \\ a' & a \end{pmatrix}$; $\det M_A = N(A)$ |
| $M_u$, $M_\phi = M_{e^{\phi j}}$ | matrices of the unit factors, $\det M_u = 1$; the identity component is $\{M_{e^{\phi j}}\}$ |
| $SO^+(1,1) = \{M_{e^{\phi j}}\}$ | the identity component of the unit matrices, $\phi \in \mathbb{R}$ |

## Further Reading

- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the polar form of split complex numbers and the hyperbola as the unit locus.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split complex algebra, its idempotents and its zero divisors.
- Felix Klein, *Vorlesungen über nicht-euklidische Geometrie* (Springer, 1928), for the hyperbolic plane, its isometries and the role of the asymptotic directions.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, 2012), for the three regimes of the hyperbolic parametrisation and their geometric meaning.
- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds* (Springer, Graduate Texts in Mathematics 149, 2nd ed. 2006), for hyperbolic geometry, its isometry groups and the parametrisation by rapidity.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for norms of arbitrary signature and the connected components of their isometry groups.
