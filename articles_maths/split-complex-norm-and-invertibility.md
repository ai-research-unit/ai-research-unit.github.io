
# __Split-Complex Norm and Invertibility__

## Introduction

This article treats the multiplicative size of a split-complex number: the **norm form** $N(Z) = Z\bar{Z} = a^2-b^2$, its multiplicativity, the region on which it vanishes, and the invertibility criterion it supplies. It is the two-dimensional member of the family of norm-form articles, and its counterpart is *Biquaternion Norm and Invertibility*; the four-dimensional case has a complex-valued norm form that can vanish on a large cone, while here the form is real and indefinite of signature $(1,1)$, and its vanishing set is a pair of lines.

The organisation follows the biquaternion article. The norm form is defined and shown multiplicative; it is shown **not** to be definite, and its square root $|N|^{1/2}$ is shown to be a modulus only up to a sign, which produces the two regimes that recur throughout the category. The Euclidean form is then separated from the norm form, as in the four-dimensional case, and the invertibility of an element is reduced to the non-vanishing of the norm form. The group of units, its four components and its non-compactness are established, the elements are classified in three ways, and the distribution of the invertible elements among the distinguished subspaces is tabulated.

The conventions are those of *Split-Complex Algebra*: the basis is $1$, $j$, with $j^2 = +1$, a general element is $Z = a + j b$ with $a = \operatorname{Re}Z$ and $b = \operatorname{Im}Z$, the conjugate is $\bar{Z} = a-j b$, and the idempotent basis is $\Pi_\pm = \tfrac12(1\pm j)$ with $Z = Z_+\Pi_1 + Z_-\Pi_2$, $Z_\pm = a\pm b$. The modulus $\rho = \sqrt{|N(Z)|}$ is defined in this article as the positive scale carried by the polar factorisation. Every numerical claim below was recomputed in double precision.

## The Norm Form

### Definition

The **norm form** of a split-complex number $Z = a + j b$ is

$$
N(Z) = Z \bar{Z} = (a+j b)(a-j b) = a^2 - b^2.
$$

It is a **quadratic form** on the real vector space $\mathbb{D} \cong \mathbb{R}^2$: it is homogeneous of degree two, $N(\lambda Z) = \lambda^2 N(Z)$ for $\lambda \in \mathbb{R}$, and its polarisation is the symmetric bilinear form

$$
g(Z, W) = \frac{1}{2}\big(N(Z+W) - N(Z) - N(W)\big) = a c - b d, \qquad Z = a+j b, \; W = c+j d,
$$

whose matrix in the basis $\{1, j\}$ is $\operatorname{diag}(1, -1)$ and whose signature is $(1,1)$. In the idempotent coordinates the norm form is the product

$$
N(Z) = Z_+ Z_-,
$$

which is the reason the norm form vanishes exactly when one idempotent coordinate vanishes.

### Multiplicativity

**Theorem.** The norm form is multiplicative:

$$
N(Z W) = N(Z) N(W), \qquad Z, W \in \mathbb{D}.
$$

**Proof.** Write $Z = a+j b$ and $W = c+j d$. Then $ZW = (a c+b d) + (a d+b c)j$, so

$$
N(ZW) = (a c+b d)^2 - (a d+b c)^2 = a^2c^2 + 2abcd + b^2d^2 - a^2d^2 - 2abcd - b^2c^2 = (a^2-b^2)(c^2-d^2),
$$

which is $N(Z)N(W)$. Equivalently, in the idempotent basis multiplication is componentwise, so $N(ZW) = (Z_+W_+)(Z_-W_-) = (Z_+Z_-)(W_+W_-)$. $\square$

The identity $(a^2-b^2)(c^2-d^2) = (a c+b d)^2 - (a d+b c)^2$ is the hyperbolic form of the two-dimensional Brahmagupta–Fibonacci identity. Multiplicativity makes $N$ a group homomorphism on the units,

$$
N : \mathbb{D}^\times \longrightarrow \mathbb{R}^\times,
$$

a fact used repeatedly below.

### The Norm Form Is Not Definite

The form $N$ takes both signs and vanishes on a pair of lines. Its sign partitions $\mathbb{D}$ into three regions, which are the three regions of the Lorentzian plane:

| region | condition | sign of $N(Z)$ | contains |
|---|---|---|---|
| spacelike | $\lvert a\rvert > \lvert b\rvert$ | positive | the two sectors through $\pm 1$ |
| null | $\lvert a\rvert = \lvert b\rvert$ | zero | the null cone, the zero-divisor set |
| timelike | $\lvert a\rvert < \lvert b\rvert$ | negative | the two sectors through $\pm j$ |

The **isotropic cone**, or null cone, is

$$
\mathcal{N} = \{Z \in \mathbb{D} : N(Z) = 0\} = \{Z = a+j b : a = \pm b\} = \mathbb{R}\Pi_1 \cup \mathbb{R}\Pi_2,
$$

the union of the two null lines through the origin. Since $N$ is a nonzero quadratic form that vanishes on a nonzero vector, it is not definite, not semidefinite, and not anisotropic; its square root $\sqrt{N}$ is therefore not a norm, and even $|N|^{1/2}$ fails to be a norm because it vanishes on the nonzero elements of $\mathcal{N}$. The form $N$ is therefore indefinite, and neither $N$ nor $|N|^{1/2}$ is a norm on $\mathbb{D}$.

### The Modulus and the Two Regimes

**Definition.** The **modulus** of $Z$ is

$$
\rho = \sqrt{|N(Z)|} = \sqrt{|a^2-b^2|}.
$$

It is a non-negative real, positive exactly on $\mathbb{D}^\times = \mathbb{D}\setminus\mathcal{N}$, and zero exactly on the null cone. In the idempotent coordinates it is the **geometric mean** of the two component moduli,

$$
\rho = \sqrt{|Z_+ Z_-|},
$$

because $N(Z) = Z_+Z_-$.

The modulus is multiplicative:

$$
\rho(ZW) = \sqrt{|N(ZW)|} = \sqrt{|N(Z)|\,|N(W)|} = \rho(Z)\rho(W).
$$

So $\rho$ is multiplicative and absolutely homogeneous, $\rho(\lambda Z)=|\lambda|\rho(Z)$ for $\lambda\in\mathbb{R}$; it is positive on $\mathbb{D}^\times$ and vanishes on $\mathcal{N}$. It is **not** subadditive, hence not a norm and not a semi-norm: for $Z=1+j$ and $W=1-j$ one has $\rho(Z)=\rho(W)=0$ while $\rho(Z+W)=\rho(2)=2$. The **two regimes** are the two sign classes:

$$
N(Z) > 0 \ (\text{spacelike}), \qquad N(Z) < 0 \ (\text{timelike}),
$$

and on each regime the modulus is a genuine scale, while the unit element that accompanies it carries the sign; a single polar factorisation therefore never straddles the two regimes.

### Worked Verification

The multiplicativity is checked on a general pair, not a single example. For $Z = a+j b$ and $W = c+j d$ the identity $N(ZW)=N(Z)N(W)$ was verified above symbolically; numerically, taking $Z = 2+3j$ and $W = 1+2j$ gives $ZW = 8+7j$, so $N(ZW) = 64-49 = 15$, while $N(Z) = 4-9 = -5$ and $N(W) = 1-4 = -3$, and $(-5)(-3) = 15$. The modulus is multiplicative: $\rho(ZW) = \sqrt{15}$ and $\rho(Z)\rho(W) = \sqrt5\sqrt3 = \sqrt{15}$.

## The Euclidean Form

### Definition

The **Euclidean form** is

$$
\langle Z, Z \rangle = a^2 + b^2 = \operatorname{Re}(Z^2) = \operatorname{Re}(Z\bar Z) + 2b^2,
$$

and the associated bilinear pairing of $Z = a+j b$ and $W = c+j d$ is

$$
\langle Z, W \rangle = a c + b d.
$$

It is the ordinary Euclidean inner product on $\mathbb{R}^2$, positive-definite and symmetric. It is **not** multiplicative, and the Euclidean norm is not preserved by the split-complex product: for $Z = 1+j$ one has $\|Z\|_E^2 = 2$ while $\|Z^2\|_E = \|2+2j\|_E = 2\sqrt2 \neq 2$.

### The Euclidean Norm

The **Euclidean norm** is

$$
\|Z\|_E = \sqrt{\langle Z, Z\rangle} = \sqrt{a^2+b^2}.
$$

It is a genuine norm on the real vector space $\mathbb{D} \cong \mathbb{R}^2$: positive-definite, subadditive, homogeneous of degree one. It is the norm that turns $\mathbb{D}$ into a topological algebra and that underlies the analysis of *Split Complex Analysis*; the modulus $\rho$ is a different object, multiplicative but not subadditive and not positive-definite.

### Relation Between the Norm Form and the Euclidean Form

The two forms are related by

$$
N(Z) = a^2 - b^2 = \langle Z, Z\rangle - 2b^2 = \operatorname{Re}(Z\bar Z), \qquad \|Z\|_E^2 = a^2+b^2 = N(Z) + 2b^2,
$$

and by the idempotent form

$$
Z_+^2 + Z_-^2 = (a+b)^2 + (a-b)^2 = 2(a^2+b^2) = 2\|Z\|_E^2.
$$

So the Euclidean form is the sum of the norm form and twice the square of the imaginary part, and the idempotent form is exactly twice the Euclidean norm squared. The biquaternion article separates its norm form from its Hermitian form in the same spirit: there the Hermitian form is a biquaternion whose scalar part is the Euclidean norm squared; here there is no Hermitian form, only the Euclidean one, and the two are related by the diagonal display above.

## Invertibility

### Definition

An element $Z \in \mathbb{D}$ is a **unit** if there exists $W \in \mathbb{D}$ with $ZW = 1$; then $W$ is the **inverse** of $Z$, written $W = Z^{-1}$. Since $\mathbb{D}$ is commutative, there is no distinction between a left inverse and a right inverse: if $ZW = 1$ then $WZ = ZW = 1$.

The **group of units** is

$$
\mathbb{D}^\times = \{Z \in \mathbb{D} : Z \text{ is a unit}\}.
$$

### Criterion for Invertibility

**Theorem.** An element $Z \in \mathbb{D}$ is a unit if and only if $N(Z) \neq 0$. Equivalently, the units are exactly the complement of the null cone.

**Proof.** If $N(Z) \neq 0$, then

$$
Z \cdot \frac{\bar{Z}}{N(Z)} = \frac{Z\bar{Z}}{N(Z)} = \frac{N(Z)}{N(Z)} = 1,
$$

so $Z$ is a unit with the inverse displayed in the next paragraph. Conversely, if $ZW = 1$, then taking norm forms gives $N(Z)N(W) = N(1) = 1$, so $N(Z) \neq 0$. $\square$

In idempotent coordinates the criterion reads: $Z = Z_+\Pi_1 + Z_-\Pi_2$ is a unit iff $Z_+ \neq 0$ and $Z_- \neq 0$, since $N(Z) = Z_+Z_-$. So the non-units are exactly the elements supported on a single idempotent, that is, the nonzero elements of $\mathbb{R}\Pi_1 \cup \mathbb{R}\Pi_2$; these are the zero divisors of *Split-Complex Zero Divisors*.

### The Inverse Formula

**Proposition.** For a unit $Z = a+j b$,

$$
Z^{-1} = \frac{\bar{Z}}{N(Z)} = \frac{a - j b}{a^2-b^2}.
$$

**Proof.** The product $Z\bar Z = N(Z)$ is a nonzero real scalar, so $Z(\bar Z/N(Z)) = 1$; uniqueness of the inverse in a unital associative algebra gives the formula. $\square$

In idempotent coordinates the inverse is componentwise,

$$
Z^{-1} = Z_+^{-1} \Pi_1 + Z_-^{-1} \Pi_2,
$$

which is the inverse of $Z$ under the isomorphism $\mathbb{D} \cong \mathbb{R}\oplus\mathbb{R}$. The inverse map $Z \mapsto Z^{-1}$ is a continuous map $\mathbb{D}^\times \to \mathbb{D}^\times$, since its components $a/(a^2-b^2)$ and $-b/(a^2-b^2)$ are rational functions of $(a,b)$ with non-vanishing denominator on $\mathbb{D}^\times$.

## The Group of Units

### Basic Properties

The set $\mathbb{D}^\times$ is a group under multiplication: it contains $1$; it is closed under multiplication because $N(ZW) = N(Z)N(W) \neq 0$ when both factors are units; it is closed under inversion by the formula above; and associativity and commutativity are inherited from the algebra. Since the algebra is commutative, $\mathbb{D}^\times$ is **abelian**.

Under the isomorphism $\mathbb{D} \cong \mathbb{R}\oplus\mathbb{R}$ the group of units corresponds to

$$
\mathbb{D}^\times \cong \mathbb{R}^\times \times \mathbb{R}^\times,
$$

the inverse image of the pairs with both coordinates nonzero. Each factor $\mathbb{R}^\times$ has two connected components, $a>0$ and $a<0$, so the product has four.

### The Four Components

**Theorem.** The group of units $\mathbb{D}^\times$ has exactly **four** connected components, indexed by the signs of the two idempotent coordinates:

$$
\mathbb{D}^\times_0 = \{Z : Z_+ > 0, \; Z_- > 0\}, \qquad \{Z : Z_+ > 0, \; Z_- < 0\},
$$
$$
\{Z : Z_+ < 0, \; Z_- > 0\}, \qquad \{Z : Z_+ < 0, \; Z_- < 0\}.
$$

**Proof.** The map $Z \mapsto (Z_+, Z_-)$ is a homeomorphism of $\mathbb{D}^\times$ onto $\mathbb{R}^\times \times \mathbb{R}^\times$, and $\mathbb{R}^\times$ has two components; a product of two spaces with two components each has four. $\square$

The identity component is $\mathbb{D}^\times_0 = \{Z : Z_+>0, Z_->0\} = \{N(Z)>0, \operatorname{Re}Z>0\}$, the connected component of the identity, and it is isomorphic as a Lie group to $\mathbb{R}^2$; it is the image of the exponential map, treated in *Split-Complex Exponential and Lie Group Structure*.

### Non-Compactness

The group $\mathbb{D}^\times$ is **not compact**: the real units $Z = t$ with $t \geq 1$ form an unbounded subset of $\mathbb{D}^\times$ in the Euclidean norm. Equivalently, the unit hyperbola $\{N = 1\}$ is unbounded, in contrast with the compact unit circle of $\mathbb{C}$. This is the first appearance in the family of a non-compact group of units, and it is forced by the indefiniteness of the norm form.

### The Three-Way Classification

Every element falls into exactly one of the three classes of the norm form:

| class | condition | unit? | inverse location |
|---|---|---|---|
| spacelike | $N(Z) > 0$ | yes | spacelike |
| null | $N(Z) = 0$ | no | — |
| timelike | $N(Z) < 0$ | yes | timelike |

The classification is preserved by multiplication, since $N(ZW) = N(Z)N(W)$: the product of two spacelike elements is spacelike, and a spacelike times a timelike is timelike. The zero element is null but not a zero divisor; every other null element is a zero divisor, by the criterion above.

**The algebra is not a division algebra.** The nonzero null elements $\Pi_1$ and $\Pi_2$ are zero divisors, $(1+j)(1-j) = 0$; equivalently $N$ vanishes on a nonzero vector. So $\mathbb{D}$ is a commutative ring in which not every nonzero element is invertible, and Frobenius's theorem places it outside the list $\mathbb{R}, \mathbb{C}, \mathbb{H}$ of finite-dimensional associative real division algebras.

## Distribution of the Invertible Elements

The two distinguished one-dimensional subspaces of $\mathbb{D}$ are the eigenspaces of the conjugation, $\mathbb{R}_{\mathbb{D}}$ and $j\mathbb{R}_{\mathbb{D}}$. On each the restricted norm form is definite, so the null cone meets each only at the origin.

### The Real Subspace $\mathbb{R}_{\mathbb{D}}$

On $\mathbb{R}_{\mathbb{D}}$ the norm form is $N(a) = a^2$, positive definite and vanishing only at $a=0$. Every nonzero real number is a spacelike unit, with $N>0$; the units of $\mathbb{R}_{\mathbb{D}}$ are $\mathbb{R}^\times$, the two open rays. There are no zero divisors on $\mathbb{R}_{\mathbb{D}}$.

### The Split Imaginary Subspace $j\mathbb{R}_{\mathbb{D}}$

On $j\mathbb{R}_{\mathbb{D}}$ the norm form is $N(j b) = -b^2$, negative definite and vanishing only at $b=0$. Every nonzero element $j b$ is a timelike unit: $N(j b) = -b^2$ and $\overline{j b} = -j b$, so

$$
(j b)^{-1} = \frac{\overline{j b}}{N(j b)} = \frac{-j b}{-b^2} = \frac{j}{b},
$$

and indeed $(j b)(j/b) = b^2 j^2/b^2 = 1$. There are no zero divisors on $j\mathbb{R}_{\mathbb{D}}$.

### The Null Lines

The zero divisors lie on neither eigenspace but on the two diagonal lines

$$
\mathbb{R}\Pi_1 = \mathbb{R}(1+j), \qquad \mathbb{R}\Pi_2 = \mathbb{R}(1-j),
$$

on each of which $N$ vanishes identically. These lines are not fixed by the conjugation; it swaps them, $\overline{\Pi_1} = \Pi_2$. They are the two isotropic lines of the form $g$, and their union is the null cone $\mathcal{N}$.

### Summary of the Distribution

| subspace | dimension | restricted $N$ | invertible elements | zero divisors |
|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{D}}$ | $1$ | $a^2$, positive definite | all nonzero, spacelike | none |
| $j\mathbb{R}_{\mathbb{D}}$ | $1$ | $-b^2$, negative definite | all nonzero, timelike | none |
| $\mathbb{R}\Pi_1$ | $1$ | $0$ | none but $0$ | all nonzero |
| $\mathbb{R}\Pi_2$ | $1$ | $0$ | none but $0$ | all nonzero |

So the two eigenspaces of the conjugation are totally invertible, while the two null lines are totally singular; the null cone meets the two eigenspaces only at the origin, exactly as in the biquaternion case where the null cone meets the pure reality slices only at the apex.

## The Relation to the Idempotent Decomposition

The invertibility criterion is the idempotent decomposition seen on the multiplicative side. Under $\mathbb{D} \cong \mathbb{R}\oplus\mathbb{R}$,

$$
Z \longmapsto (Z_+, Z_-), \qquad \mathbb{D}^\times \longmapsto \mathbb{R}^\times\times\mathbb{R}^\times,
$$

and an element is a unit exactly when both idempotent coordinates are nonzero. The inverse is the componentwise inverse, and the norm form is the product of the two coordinates. The group of units is thus the direct product of the two copies of $\mathbb{R}^\times$, and its four components are the four sign combinations of the two coordinates. This is the two-dimensional analogue of the biquaternion relation between the norm form and the Hermitian decomposition: there the units form $GL(2,\mathbb{C})$; here they form $\mathbb{R}^\times\times\mathbb{R}^\times$, the maximal torus of the four-dimensional case in the real picture.

## Comparison with the Complex and Biquaternion Cases

| algebra | norm form | definite? | units | components |
|---|---|---|---|---|
| $\mathbb{C}$ | $a^2+b^2$, real | yes, positive | all nonzero | $1$ (connected) |
| $\mathbb{D}$ | $a^2-b^2$, real | no, signature $(1,1)$ | $N \neq 0$ | $4$ |
| $\mathbb{B}$ | $\sum_\mu Q_\mu^2$, complex | no | $N \neq 0$, $\mathbb{B}^\times \cong GL(2,\mathbb{C})$ | $1$ (connected) |

The complex case is the definite one: its norm form is positive-definite, every nonzero element is a unit, and the unit group is connected. The split-complex case is the indefinite two-dimensional one: the norm form is real of signature $(1,1)$, its zero set is the pair of null lines, and the unit group has four components and is non-compact. The biquaternion case is the indefinite four-dimensional complexification: its norm form is complex-valued, its zero set is a six-real-dimensional cone, and its unit group is the connected $GL(2,\mathbb{C})$, with compact retract $U(2)$; the details are in *Biquaternion Norm and Invertibility*. The split-complex algebra is the smallest member of the family in which the norm form is indefinite and the unit group disconnected, and it exhibits both phenomena without the non-commutativity of the four-dimensional algebra.

## Summary

The norm form of a split-complex number is $N(Z) = Z\bar{Z} = a^2-b^2$, a non-degenerate quadratic form of signature $(1,1)$, multiplicative under multiplication of the algebra. It is not definite: it vanishes on the isotropic cone $\mathcal{N} = \mathbb{R}\Pi_1\cup\mathbb{R}\Pi_2$, the union of the two null lines. Its absolute-value square root $\rho = \sqrt{|N(Z)|} = \sqrt{|Z_+Z_-|}$ is multiplicative and absolutely homogeneous, positive exactly on the units, and it splits the algebra into the two regimes $N>0$ (spacelike) and $N<0$ (timelike).

An element is a unit exactly when its norm form does not vanish, and then $Z^{-1} = \bar Z/N(Z) = Z_+^{-1}\Pi_1 + Z_-^{-1}\Pi_2$. The group of units is $\mathbb{D}^\times = \{N \neq 0\} \cong \mathbb{R}^\times\times\mathbb{R}^\times$, an abelian group with four connected components and non-compact, in contrast with the compact connected unit circle of $\mathbb{C}$ and with the connected $GL(2,\mathbb{C})$ of $\mathbb{B}$. The elements are classified as spacelike, null or timelike by the sign of the norm form, the classification being multiplicative; the null class consists of the zero divisors together with the origin. On the two eigenspaces of the conjugation the restricted norm form is definite, so the null cone meets each of them only at the origin; all zero divisors lie on the two null lines.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $Z = a + j b$ | General split complex number |
| $\bar{Z} = a - j b$ | Split complex conjugate |
| $N(Z) = Z\bar{Z} = a^2-b^2$ | Norm form, signature $(1,1)$ |
| $g(Z,W) = a c-b d$ | Polarisation of $N$, the split bilinear form |
| $Z_\pm = a\pm b$ | Idempotent coordinates, $Z = Z_+\Pi_1 + Z_-\Pi_2$ |
| $\Pi_\pm = (1\pm j)/2$ | Idempotents |
| $\mathcal{N} = \{N=0\}$ | Isotropic cone, the two null lines $\mathbb{R}\Pi_\pm$ |
| $\rho = \sqrt{|N(Z)|} = \sqrt{|Z_+Z_-|}$ | Modulus, multiplicative and absolutely homogeneous |
| $\|Z\|_E = \sqrt{a^2+b^2}$ | Euclidean norm |
| $\langle Z,W\rangle = a c+b d$ | Euclidean inner product |
| $\mathbb{D}^\times = \{N \neq 0\}$ | Group of units |
| $\mathbb{D}^\times_0$ | Identity component, $\{Z_+>0, Z_->0\}$ |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split complex numbers as a Clifford algebra and their norm form.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the classification of real composition and division algebras.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the signature, the isotropic cone and the theory of indefinite quadratic forms.
- Benson Farb and R. Keith Dennis, *Noncommutative Algebra* (Springer, 1993), for invertibility, zero divisors and the group of units in a finite-dimensional algebra.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric reading of the norm form and the null lines.
