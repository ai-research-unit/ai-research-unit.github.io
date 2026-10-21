
# __Split-Complex Norm and Invertibility__

## Introduction

This article treats the multiplicative size of a split-complex number: the **norm** $\langle Q\rangle_{\natural} = Q\bar{Q} = q^2-q'^2$, its multiplicativity, the region on which it vanishes, and the invertibility criterion it supplies. It is the two-dimensional member of the family of articles on the norm; the higher-dimensional case has a complex-valued norm that can vanish on a large cone, while here the form is real and indefinite of signature $(1,1)$, and its vanishing set is a pair of lines.

The organisation is as follows. The norm is defined and shown multiplicative; it is shown **not** to be definite, and its square root $|N|^{1/2}$ is shown to be a modulus only up to a sign, which produces the two regimes that recur throughout the category. The Euclidean form is then separated from the norm, as in the four-dimensional case, and the invertibility of an element is reduced to the non-vanishing of the norm. The group of units, its four components and its non-compactness are established, the elements are classified in three ways, and the distribution of the invertible elements among the distinguished subspaces is tabulated.

The conventions are those of *Split-Complex Algebra*: the basis is $1$, $j$, with $j^2 = +1$, a general element is $Q = q + j q'$ with $q = \operatorname{Re}Q$ and $q' = \operatorname{Im}Q$, the conjugate is $\bar{Q} = q-j q'$, and the idempotent basis is $\Pi_\pm = \tfrac12(1\pm j)$ with $Q = Q_+\Pi_+ + Q_-\Pi_-$, $Q_\pm = q\pm q'$. The modulus $\rho = \sqrt{|\langle Q\rangle_{\natural}|}$ is defined in this article as the positive scale carried by the polar factorisation.

## The Norm

### Definition

The **norm** of a split-complex number $Q = q + j q'$ is

$$
\langle Q\rangle_{\natural} = Q \bar{Q} = (q+j q')(q-j q') = q^2 - q'^2.
$$

It is a **quadratic form** on the real vector space $\mathbb{D} \cong \mathbb{R}^2$: it is homogeneous of degree two, $\langle \lambda Q\rangle_{\natural} = \lambda^2 \langle Q\rangle_{\natural}$ for $\lambda \in \mathbb{R}$, and its polarisation is the symmetric bilinear form

$$
g(Q, B) = \frac{1}{2}\big(\langle Q+B\rangle_{\natural} - \langle Q\rangle_{\natural} - \langle B\rangle_{\natural}\big) = q b - q' b', \qquad Q = q+j q', \; B = b+j b',
$$

whose matrix in the basis $\{1, j\}$ is $\operatorname{diag}(1, -1)$ and whose signature is $(1,1)$. In the idempotent coordinates the norm is the product

$$
\langle Q\rangle_{\natural} = Q_+ Q_-,
$$

which is the reason the norm vanishes exactly when one idempotent coordinate vanishes.

### Multiplicativity

**Theorem.** The norm is multiplicative:

$$
\langle Q B\rangle_{\natural} = \langle Q\rangle_{\natural} \langle B\rangle_{\natural}, \qquad Q, B \in \mathbb{D}.
$$

**Proof.** Write $Q = q+j q'$ and $B = b+j b'$. Then $QB = (q b+q' b') + (q b'+q' b)j$, so

$$
\langle QB\rangle_{\natural} = (q b+q' b')^2 - (q b'+q' b)^2 = q^2b^2 + 2qbq'b' + q'^2b'^2 - q^2b'^2 - 2qbq'b' - q'^2b^2 = (q^2-q'^2)(b^2-b'^2),
$$

which is $\langle Q\rangle_{\natural}\langle B\rangle_{\natural}$. Equivalently, in the idempotent basis multiplication is componentwise, so $\langle QB\rangle_{\natural} = (Q_+B_+)(Q_-B_-) = (Q_+Q_-)(B_+B_-)$.

The identity $(q^2-q'^2)(b^2-b'^2) = (q b+q' b')^2 - (q b'+q' b)^2$ is the hyperbolic form of the two-dimensional Brahmagupta–Fibonacci identity. Multiplicativity makes $\langle\cdot,\cdot\rangle_{\natural}$ a group homomorphism on the units,

$$
N : \mathbb{D}^\times \longrightarrow \mathbb{R}^\times,
$$

a fact used repeatedly below.

### The Norm Is Not Definite

The form $\langle\cdot,\cdot\rangle_{\natural}$ takes both signs and vanishes on a pair of lines. Its sign partitions $\mathbb{D}$ into three regions, which are the three regions of the Lorentzian plane:

| region | condition | sign of $\langle Q\rangle_{\natural}$ | contains |
|---|---|---|---|
| timelike | $\lvert q\rvert > \lvert q'\rvert$ | positive | the two sectors through $\pm 1$ |
| null | $\lvert q\rvert = \lvert q'\rvert$ | zero | the null cone, the zero-divisor set |
| spacelike | $\lvert q\rvert < \lvert q'\rvert$ | negative | the two sectors through $\pm j$ |

The **isotropic cone**, or null cone, is

$$
\mathcal{N} = \{Q \in \mathbb{D} : \langle Q\rangle_{\natural} = 0\} = \{Q = q+j q' : q = \pm q'\} = \mathbb{R}\Pi_+ \cup \mathbb{R}\Pi_-,
$$

the union of the two null lines through the origin. Since $\langle\cdot,\cdot\rangle_{\natural}$ is a nonzero quadratic form that vanishes on a nonzero vector, it is not definite, not semidefinite, and not anisotropic; its square root $\sqrt{N}$ is therefore not a norm, and even $|N|^{1/2}$ fails to be a norm because it vanishes on the nonzero elements of $\mathcal{N}$. The form $\langle\cdot,\cdot\rangle_{\natural}$ is therefore indefinite, and neither $\langle\cdot,\cdot\rangle_{\natural}$ nor $|N|^{1/2}$ is a norm on $\mathbb{D}$.

### The Associated Clifford Algebra

The quadratic space $(\mathbb{D},N)$ has Clifford algebra $\mathrm{Cl}(1,1)$, generated by an orthonormal pair $u, v$ with $u^2=+1$ and $v^2=-1$; in the basis $\{1,j\}$ one may take $u=1$ and $v=j$. Writing $\omega=uv$ for the volume element,

$$
\omega^2=uvuv=-u^2v^2=-(1)(-1)=+1,
$$

so the **even part** is generated by $1$ and $\omega$ with $\omega^2=+1$:

$$
\mathrm{Cl}^+(1,1)=\langle 1,\omega\rangle\cong\mathbb{R}\oplus\mathbb{R}\cong\mathbb{D}, \qquad \mathrm{Cl}(1,1)\cong M_2(\mathbb{R}).
$$

So the split-complex algebra is the even Clifford algebra of its own norm, and the full Clifford algebra is the algebra of real $2\times2$ matrices. The two isotropic lines are the two eigenspaces of $\omega$, and the spectral projections of $\omega$ are multiplication by the idempotents $\Pi_\pm$.

### The Modulus and the Two Regimes

**Definition.** The **modulus** of $Q$ is

$$
\rho = \sqrt{|\langle Q\rangle_{\natural}|} = \sqrt{|q^2-q'^2|}.
$$

It is a non-negative real, positive exactly on $\mathbb{D}^\times = \mathbb{D}\setminus\mathcal{N}$, and zero exactly on the null cone. In the idempotent coordinates it is the **geometric mean** of the two component moduli,

$$
\rho = \sqrt{|Q_+ Q_-|},
$$

because $\langle Q\rangle_{\natural} = Q_+Q_-$.

The modulus is multiplicative:

$$
\rho(QB) = \sqrt{|\langle QB\rangle_{\natural}|} = \sqrt{|\langle Q\rangle_{\natural}|\,|\langle B\rangle_{\natural}|} = \rho(Q)\rho(B).
$$

So $\rho$ is multiplicative and absolutely homogeneous, $\rho(\lambda Q)=|\lambda|\rho(Q)$ for $\lambda\in\mathbb{R}$; it is positive on $\mathbb{D}^\times$ and vanishes on $\mathcal{N}$. It is **not** subadditive, hence not a norm and not a semi-norm: for $Q=1+j$ and $B=1-j$ one has $\rho(Q)=\rho(B)=0$ while $\rho(Q+B)=\rho(2)=2$. The **two regimes** are the two sign classes:

$$
\langle Q\rangle_{\natural} > 0 \ (\text{timelike}), \qquad \langle Q\rangle_{\natural} < 0 \ (\text{spacelike}),
$$

and on each regime the modulus is a genuine scale, while the unit element that accompanies it carries the sign; a single polar factorisation therefore never straddles the two regimes.

### Worked Verification

The multiplicativity is checked on a general pair, not a single example. For $Q = q+j q'$ and $B = b+j b'$ the identity $\langle QB\rangle_{\natural}=\langle Q\rangle_{\natural}\langle B\rangle_{\natural}$ was verified above symbolically; numerically, taking $Q = 2+3j$ and $B = 1+2j$ gives $QB = 8+7j$, so $\langle QB\rangle_{\natural} = 64-49 = 15$, while $\langle Q\rangle_{\natural} = 4-9 = -5$ and $\langle B\rangle_{\natural} = 1-4 = -3$, and $(-5)(-3) = 15$. The modulus is multiplicative: $\rho(QB) = \sqrt{15}$ and $\rho(Q)\rho(B) = \sqrt5\sqrt3 = \sqrt{15}$.

## The Euclidean Form

### Definition

The **Euclidean form** is

$$
\langle Q, Q \rangle = q^2 + q'^2 = \operatorname{Re}(Q^2) = \operatorname{Re}(Q\bar Q) + 2q'^2,
$$

and the associated bilinear pairing of $Q = q+j q'$ and $B = b+j b'$ is

$$
\langle Q, B \rangle = q b + q' b'.
$$

It is the ordinary Euclidean inner product on $\mathbb{R}^2$, positive-definite and symmetric. It is **not** multiplicative, and the Euclidean norm is not preserved by the split-complex product: for $Q = 1+j$ one has $\|Q\|_E^2 = 2$ while $\|Q^2\|_E = \|2+2j\|_E = 2\sqrt2 \neq 2$.

### The Euclidean Norm

The **Euclidean norm** is

$$
\|Q\|_E = \sqrt{\langle Q, Q\rangle} = \sqrt{q^2+q'^2}.
$$

It is a genuine norm on the real vector space $\mathbb{D} \cong \mathbb{R}^2$: positive-definite, subadditive, homogeneous of degree one. It is the norm that turns $\mathbb{D}$ into a topological algebra and that underlies the analysis of *Split-Complex Analysis*; the modulus $\rho$ is a different object, multiplicative but not subadditive and not positive-definite.

### Relation Between the Norm and the Euclidean Form

The two forms are related by

$$
\langle Q\rangle_{\natural} = q^2 - q'^2 = \langle Q, Q\rangle - 2q'^2 = \operatorname{Re}(Q\bar Q), \qquad \|Q\|_E^2 = q^2+q'^2 = \langle Q\rangle_{\natural} + 2q'^2,
$$

and by the idempotent form

$$
Q_+^2 + Q_-^2 = (q+q')^2 + (q-q')^2 = 2(q^2+q'^2) = 2\|Q\|_E^2.
$$

So the Euclidean form is the sum of the norm and twice the square of the imaginary part, and the idempotent form is exactly twice the Euclidean norm squared. There is no Hermitian form here, only the Euclidean one, and the two are related by the diagonal display above.

### The Absence of a Positive-Definite Hermitian Form

There is no positive-definite **Hermitian form** on $\mathbb{D}$ analogous to the one on $\mathbb{C}$, because the conjugation group is too small. The non-trivial involution $\bar{\cdot}$ produces the sesquilinear expression

$$
Q\bar B = (q b - q' b') + (q' b - q b')j, \qquad Q = q+j q', \; B = b+j b',
$$

whose real part is $g(Q,B) = q b - q' b'$, the polarisation of $\langle\cdot\rangle_{\natural}$, and is therefore indefinite of signature $(1,1)$; neither this form nor its negative is definite. Here that slot is empty, and the positive-definite substitute is the Euclidean form $\langle Q,B\rangle = q b + q' b'$ of the preceding section, which does not depend on the algebra structure.

## Invertibility

### Definition

An element $Q \in \mathbb{D}$ is a **unit** if there exists $B \in \mathbb{D}$ with $QB = 1$; then $B$ is the **inverse** of $Q$, written $B = Q^{-1}$. Since $\mathbb{D}$ is commutative, there is no distinction between a left inverse and a right inverse: if $QB = 1$ then $BQ = QB = 1$.

The **group of units** is

$$
\mathbb{D}^\times = \{Q \in \mathbb{D} : Q \text{ is a unit}\}.
$$

### Criterion for Invertibility

**Theorem.** An element $Q \in \mathbb{D}$ is a unit if and only if $\langle Q\rangle_{\natural} \neq 0$. Equivalently, the units are exactly the complement of the null cone.

**Proof.** If $\langle Q\rangle_{\natural} \neq 0$, then

$$
Q \cdot \frac{\bar{Q}}{\langle Q\rangle_{\natural}} = \frac{Q\bar{Q}}{\langle Q\rangle_{\natural}} = \frac{\langle Q\rangle_{\natural}}{\langle Q\rangle_{\natural}} = 1,
$$

so $Q$ is a unit with the inverse displayed in the next paragraph. Conversely, if $QB = 1$, then taking norms gives $\langle Q\rangle_{\natural}\langle B\rangle_{\natural} = \langle 1\rangle_{\natural} = 1$, so $\langle Q\rangle_{\natural} \neq 0$.

In idempotent coordinates the criterion reads: $Q = Q_+\Pi_+ + Q_-\Pi_-$ is a unit iff $Q_+ \neq 0$ and $Q_- \neq 0$, since $\langle Q\rangle_{\natural} = Q_+Q_-$. So the non-units are exactly the elements supported on a single idempotent, that is, the nonzero elements of $\mathbb{R}\Pi_+ \cup \mathbb{R}\Pi_-$; these are the zero divisors of *Split-Complex Zero Divisors*.

### The Inverse Formula

**Proposition.** For a unit $Q = q+j q'$,

$$
Q^{-1} = \frac{\bar{Q}}{\langle Q\rangle_{\natural}} = \frac{q - j q'}{q^2-q'^2}.
$$

**Proof.** The product $Q\bar Q = \langle Q\rangle_{\natural}$ is a nonzero real scalar, so $Q(\bar Q/\langle Q\rangle_{\natural}) = 1$; uniqueness of the inverse in a unital associative algebra gives the formula.

In idempotent coordinates the inverse is componentwise,

$$
Q^{-1} = Q_+^{-1} \Pi_+ + Q_-^{-1} \Pi_-,
$$

which is the inverse of $Q$ under the isomorphism $\mathbb{D} \cong \mathbb{R}\oplus\mathbb{R}$. The inverse map $Q \mapsto Q^{-1}$ is a continuous map $\mathbb{D}^\times \to \mathbb{D}^\times$, since its components $q/(q^2-q'^2)$ and $-q'/(q^2-q'^2)$ are rational functions of $(q,q')$ with non-vanishing denominator on $\mathbb{D}^\times$.

## The Group of Units

### Basic Properties

The set $\mathbb{D}^\times$ is a group under multiplication: it contains $1$; it is closed under multiplication because $\langle QB\rangle_{\natural} = \langle Q\rangle_{\natural}\langle B\rangle_{\natural} \neq 0$ when both factors are units; it is closed under inversion by the formula above; and associativity and commutativity are inherited from the algebra. Since the algebra is commutative, $\mathbb{D}^\times$ is **abelian**.

Under the isomorphism $\mathbb{D} \cong \mathbb{R}\oplus\mathbb{R}$ the group of units corresponds to

$$
\mathbb{D}^\times \cong \mathbb{R}^\times \times \mathbb{R}^\times,
$$

the inverse image of the pairs with both coordinates nonzero. Each factor $\mathbb{R}^\times$ has two connected components, $q>0$ and $q<0$, so the product has four.

### The Four Components

**Theorem.** The group of units $\mathbb{D}^\times$ has exactly **four** connected components, indexed by the signs of the two idempotent coordinates:

$$
\mathbb{D}^\times_0 = \{Q : Q_+ > 0, \; Q_- > 0\}, \qquad \{Q : Q_+ > 0, \; Q_- < 0\},
$$
$$
\{Q : Q_+ < 0, \; Q_- > 0\}, \qquad \{Q : Q_+ < 0, \; Q_- < 0\}.
$$

**Proof.** The map $Q \mapsto (Q_+, Q_-)$ is a homeomorphism of $\mathbb{D}^\times$ onto $\mathbb{R}^\times \times \mathbb{R}^\times$, and $\mathbb{R}^\times$ has two components; a product of two spaces with two components each has four.

The identity component is $\mathbb{D}^\times_0 = \{Q : Q_+>0, Q_->0\} = \{\langle Q\rangle_{\natural}>0, \operatorname{Re}Q>0\}$, the connected component of the identity, and it is isomorphic as a Lie group to $\mathbb{R}^2$; it is the image of the exponential map, treated in *Split-Complex Exponential and Lie Group Structure*.

### Non-Compactness

The group $\mathbb{D}^\times$ is **not compact**: the real units $Q = t$ with $t \geq 1$ form an unbounded subset of $\mathbb{D}^\times$ in the Euclidean norm. Equivalently, the unit hyperbola $\{N = 1\}$ is unbounded, in contrast with the compact unit circle of $\mathbb{C}$. This is the first appearance in the family of a non-compact group of units, and it is forced by the indefiniteness of the norm.

### The Three-Way Classification

Every element falls into exactly one of the three classes of the norm:

| class | condition | unit? | inverse location |
|---|---|---|---|
| timelike | $\langle Q\rangle_{\natural} > 0$ | yes | timelike |
| null | $\langle Q\rangle_{\natural} = 0$ | no | — |
| spacelike | $\langle Q\rangle_{\natural} < 0$ | yes | spacelike |

The classification is preserved by multiplication, since $\langle QB\rangle_{\natural} = \langle Q\rangle_{\natural}\langle B\rangle_{\natural}$: the product of two timelike elements is timelike, and a timelike times a spacelike is spacelike. The zero element is null but not a zero divisor; every other null element is a zero divisor, by the criterion above.

**The algebra is not a division algebra.** The nonzero null elements $\Pi_+$ and $\Pi_-$ are zero divisors, $(1+j)(1-j) = 0$; equivalently $\langle\cdot\rangle_{\natural}$ vanishes on a nonzero vector. So $\mathbb{D}$ is a commutative ring in which not every nonzero element is invertible, and Frobenius's theorem places it outside the list $\mathbb{R}, \mathbb{C}, \mathbb{H}$ of finite-dimensional associative real division algebras.

## Distribution of the Invertible Elements

The two distinguished one-dimensional subspaces of $\mathbb{D}$ are the eigenspaces of the conjugation, $\mathbb{R}_{\mathbb{D}}$ and $j\mathbb{R}_{\mathbb{D}}$. On each the restricted norm is definite, so the null cone meets each only at the origin.

### The Real Subspace $\mathbb{R}_{\mathbb{D}}$

On $\mathbb{R}_{\mathbb{D}}$ the norm is $\langle q\rangle_{\natural} = q^2$, positive definite and vanishing only at $q=0$. Every nonzero real number is a timelike unit, with $N>0$; the units of $\mathbb{R}_{\mathbb{D}}$ are $\mathbb{R}^\times$, the two open rays. There are no zero divisors on $\mathbb{R}_{\mathbb{D}}$.

### The Split Imaginary Subspace $j\mathbb{R}_{\mathbb{D}}$

On $j\mathbb{R}_{\mathbb{D}}$ the norm is $\langle j q'\rangle_{\natural} = -q'^2$, negative definite and vanishing only at $q'=0$. Every nonzero element $j q'$ is a spacelike unit: $\langle j q'\rangle_{\natural} = -q'^2$ and $\overline{j q'} = -j q'$, so

$$
(j q')^{-1} = \frac{\overline{j q'}}{\langle j q'\rangle_{\natural}} = \frac{-j q'}{-q'^2} = \frac{j}{q'},
$$

and indeed $(j q')(j/q') = q'^2 j^2/q'^2 = 1$. There are no zero divisors on $j\mathbb{R}_{\mathbb{D}}$.

### The Null Lines

The zero divisors lie on neither eigenspace but on the two diagonal lines

$$
\mathbb{R}\Pi_+ = \mathbb{R}(1+j), \qquad \mathbb{R}\Pi_- = \mathbb{R}(1-j),
$$

on each of which $\langle\cdot\rangle_{\natural}$ vanishes identically. These lines are not fixed by the conjugation; it swaps them, $\overline{\Pi_+} = \Pi_-$. They are the two isotropic lines of the form $g$, and their union is the null cone $\mathcal{N}$.

### Summary of the Distribution

| subspace | dimension | restricted $\langle\cdot,\cdot\rangle_{\natural}$ | invertible elements | zero divisors |
|---|---|---|---|---|
| $\mathbb{R}_{\mathbb{D}}$ | $1$ | $q^2$, positive definite | all nonzero, timelike | none |
| $j\mathbb{R}_{\mathbb{D}}$ | $1$ | $-q'^2$, negative definite | all nonzero, spacelike | none |
| $\mathbb{R}\Pi_+$ | $1$ | $0$ | none but $0$ | all nonzero |
| $\mathbb{R}\Pi_-$ | $1$ | $0$ | none but $0$ | all nonzero |

So the two eigenspaces of the conjugation are totally invertible, while the two null lines are totally singular; the null cone meets the two eigenspaces only at the origin, as it also does on the pure reality slices.

## The Relation to the Idempotent Decomposition

The invertibility criterion is the idempotent decomposition seen on the multiplicative side. Under $\mathbb{D} \cong \mathbb{R}\oplus\mathbb{R}$,

$$
Q \longmapsto (Q_+, Q_-), \qquad \mathbb{D}^\times \longmapsto \mathbb{R}^\times\times\mathbb{R}^\times,
$$

and an element is a unit exactly when both idempotent coordinates are nonzero. The inverse is the componentwise inverse, and the norm is the product of the two coordinates. The group of units is thus the direct product of the two copies of $\mathbb{R}^\times$, and its four components are the four sign combinations of the two coordinates. The units form $\mathbb{R}^\times\times\mathbb{R}^\times$.

## Summary

The norm of a split-complex number is $\langle Q\rangle_{\natural} = Q\bar{Q} = q^2-q'^2$, a non-degenerate quadratic form of signature $(1,1)$, multiplicative under multiplication of the algebra. It is not definite: it vanishes on the isotropic cone $\mathcal{N} = \mathbb{R}\Pi_+\cup\mathbb{R}\Pi_-$, the union of the two null lines. Its absolute-value square root $\rho = \sqrt{|\langle Q\rangle_{\natural}|} = \sqrt{|Q_+Q_-|}$ is multiplicative and absolutely homogeneous, positive exactly on the units, and it splits the algebra into the two regimes $N>0$ (timelike) and $N<0$ (spacelike).

An element is a unit exactly when its norm does not vanish, and then $Q^{-1} = \bar Q/\langle Q\rangle_{\natural} = Q_+^{-1}\Pi_+ + Q_-^{-1}\Pi_-$. The group of units is $\mathbb{D}^\times = \{N \neq 0\} \cong \mathbb{R}^\times\times\mathbb{R}^\times$, an abelian group with four connected components and non-compact, in contrast with the compact connected unit circle of $\mathbb{C}$. The elements are classified as spacelike, null or timelike by the sign of the norm, the classification being multiplicative; the null class consists of the zero divisors together with the origin. On the two eigenspaces of the conjugation the restricted norm is definite, so the null cone meets each of them only at the origin; all zero divisors lie on the two null lines.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $Q = q + j q'$ | General split complex number |
| $\bar{Q} = q - j q'$ | Split complex conjugate |
| $\langle Q\rangle_{\natural} = Q\bar{Q} = q^2-q'^2$ | Norm, signature $(1,1)$ |
| $g(Q,B) = q b-q' b'$ | Polarisation of $\langle\cdot,\cdot\rangle_{\natural}$, the split bilinear form |
| $\mathrm{Cl}(1,1)\cong M_2(\mathbb{R})$, $\mathrm{Cl}^+(1,1)\cong\mathbb{D}$ | Clifford algebra of the form and its even part |
| $Q_\pm = q\pm q'$ | Idempotent coordinates, $Q = Q_+\Pi_+ + Q_-\Pi_-$ |
| $\Pi_\pm = (1\pm j)/2$ | Idempotents |
| $\mathcal{N} = \{N=0\}$ | Isotropic cone, the two null lines $\mathbb{R}\Pi_\pm$ |
| $\rho = \sqrt{|\langle Q\rangle_{\natural}|} = \sqrt{|Q_+Q_-|}$ | Modulus, multiplicative and absolutely homogeneous |
| $\|Q\|_E = \sqrt{q^2+q'^2}$ | Euclidean norm |
| $\langle Q,B\rangle = q b+q' b'$ | Euclidean inner product |
| $Q\bar B = (q b-q' b')+(q' b-q b')j$ | Sesquilinear form; its real part is $g$, indefinite |
| $\mathbb{D}^\times = \{N \neq 0\}$ | Group of units |
| $\mathbb{D}^\times_0$ | Identity component, $\{Q_+>0, Q_->0\}$ |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split complex numbers as a Clifford algebra and their norm.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the signature, the isotropic cone and the theory of indefinite quadratic forms.
- Benson Farb and R. Keith Dennis, *Noncommutative Algebra* (Springer, 1993), for invertibility, zero divisors and the group of units in a finite-dimensional algebra.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the geometric reading of the norm and the null lines.
