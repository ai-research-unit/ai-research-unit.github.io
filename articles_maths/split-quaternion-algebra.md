
# __Split-Quaternion Algebra__

## Introduction

This article introduces the split-quaternion algebra as an algebraic structure. It defines the algebra, identifies it with the Clifford algebra $\mathrm{Cl}_{1,1}$ and with the matrix algebra $M_2(\mathbb{R})$, describes the conjugations and their fixed-point subspaces, the norm form of signature $(2,2)$, the idempotents and the distinguished subspaces, and the Lie algebra structure. It closes with a comparison with the quaternions $\mathbb{H}$ and with the split-biquaternions $\mathbb{H}_{\mathbb{D}}$.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. The quaternion algebra and its norm form are assumed from *Quaternion Algebra*; the split-complex algebra and its idempotents from *Split-Complex Algebra*; the Clifford algebra $\mathrm{Cl}_{p,q}$ and its low-dimensional classification from *Clifford Algebras in Finite Dimensions* and *The Number Systems as Clifford Algebras*; the matrix algebra $M_2(\mathbb{R})$, its determinant, its centre and its ideals from *Matrix Algebras*. The rotations, the Lorentz group and the hyperbolic geometry that the algebra carries are not treated here; they belong to *Split-Quaternion Rotations and the Lorentz Group*, *Split-Quaternion Geometry* and *Split-Quaternions and Hyperbolic Geometry*.

## The Split-Quaternion Algebra

### Definition

The **split-quaternion algebra** $\mathbb{H}_{\mathrm{s}}$ is the four-dimensional real algebra with basis

$$
1, \qquad e_1, \qquad e_2, \qquad e_3,
$$

and multiplication rules

$$
e_1^2 = -1, \qquad e_2^2 = +1, \qquad e_3 = e_1 e_2, \qquad e_1 e_2 = -e_2 e_1.
$$

A general split-quaternion is written in developed form as

$$
x = a + b e_1 + c e_2 + d e_3, \qquad a, b, c, d \in \mathbb{R},
$$

or, more compactly, as

$$
x = \sum_{\mu=0}^{3} x_\mu e_\mu, \qquad e_0 = 1, \quad x_0 = a, \quad x_1 = b, \quad x_2 = c, \quad x_3 = d.
$$

The real number $a$ is the **scalar part**, and the triple $(b, c, d)$ is the **vector part**. We also write

$$
x = a + \mathbf{v}, \qquad \mathbf{v} = b e_1 + c e_2 + d e_3,
$$

and we write $\operatorname{Sc}(x) = a$ and $\operatorname{Vec}(x) = \mathbf{v}$ for the two components.

The four elements $1, e_1, e_2, e_3$ are linearly independent over $\mathbb{R}$ by definition, so $\dim_{\mathbb{R}} \mathbb{H}_{\mathrm{s}} = 4$. The unit is $1$, and every element is a real linear combination of the basis elements.

### The Multiplication Table

The rules of the definition determine the whole multiplication table. From $e_3 = e_1 e_2$ and $e_1 e_2 = -e_2 e_1$ one computes

$$
e_3^2 = e_1 e_2 e_1 e_2 = -e_1^2 e_2^2 = -(-1)(+1) = +1,
$$

$$
e_2 e_3 = e_2 e_1 e_2 = -e_1 e_2^2 = -e_1, \qquad e_3 e_2 = e_1 e_2 e_2 = +e_1,
$$

$$
e_3 e_1 = e_1 e_2 e_1 = -e_1^2 e_2 = +e_2, \qquad e_1 e_3 = e_1 e_1 e_2 = -e_2.
$$

The products are collected in the following table, whose entry in row $i$ and column $j$ is $e_i e_j$.

| | $1$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $1$ | $1$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $e_1$ | $-1$ | $e_3$ | $-e_2$ |
| $e_2$ | $e_2$ | $-e_3$ | $+1$ | $-e_1$ |
| $e_3$ | $e_3$ | $e_2$ | $e_1$ | $+1$ |

The table is read off from the definition; the entry $e_1 e_3 = -e_2$, for instance, is the identity $e_1 e_3 = e_1 e_1 e_2 = -e_2$.

### Basic Properties

**Associative.** Split-quaternion multiplication is associative. It suffices to check the associativity of the generating products, since the product is defined by bilinear extension of the table; the four elements $1, e_1, e_2, e_3$ satisfy the relations of the Clifford algebra $\mathrm{Cl}_{1,1}$, and every Clifford algebra is associative.

**Non-commutative.** Split-quaternion multiplication is not commutative: $e_1 e_2 = e_3$ while $e_2 e_1 = -e_3$. The centre is computed in *The Centre and Simplicity* below, and it is one-dimensional.

**Not a division algebra.** The element $1 + e_2$ is nonzero and

$$
(1 + e_2)(1 - e_2) = 1 - e_2^2 = 0,
$$

so $1 + e_2$ and $1 - e_2$ are nonzero zero divisors. The algebra therefore has zero divisors and is not a division algebra. Frobenius' theorem, recalled in *Normed Division Algebras and the Hurwitz Theorem*, states that the only finite-dimensional associative real division algebras are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$; the split-quaternion algebra is a fourth four-dimensional associative real algebra, and the failure of the division property is exactly the appearance of the zero divisors above. The zero divisor set is the subject of *Split-Quaternion Zero Divisors*.

## The Identification with $\mathrm{Cl}_{1,1}$ and $M_2(\mathbb{R})$

### The Clifford Algebra

The corpus's convention is that $\mathrm{Cl}_{p,q}$ is the Clifford algebra of a form with $p$ generators of square $+1$ and $q$ generators of square $-1$. The generators $e_1$ and $e_2$ of $\mathbb{H}_{\mathrm{s}}$ have squares $-1$ and $+1$ and anticommute, and the remaining basis element is their product. This is precisely the presentation of $\mathrm{Cl}_{1,1}$, so

$$
\mathbb{H}_{\mathrm{s}} \cong \mathrm{Cl}_{1,1}.
$$

The dictionary of the number systems, stated in *The Number Systems as Clifford Algebras*, records the same identification and records also that $\mathrm{Cl}_{1,1} \cong \mathrm{Cl}_{2,0}$, so the same algebra is the Clifford algebra of the definite form of signature $(2,0)$ and of the indefinite form of signature $(1,1)$. The two signs give the same algebra because the class of $\mathrm{Cl}_{p,q}$ in the eightfold table depends on $p - q$ modulo $8$, and $0 - 2$ and $1 - 1$ are congruent modulo $8$ in their effect.

### The Matrix Model

The following map is the algebra's most useful presentation.

**Theorem (The Matrix Model).** The map $\Phi : \mathbb{H}_{\mathrm{s}} \to M_2(\mathbb{R})$ defined on the basis by

$$
\Phi(1) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad
\Phi(e_1) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad
\Phi(e_2) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
\Phi(e_3) = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix},
$$

is an algebra isomorphism. On a general element it reads

$$
\Phi(a + b e_1 + c e_2 + d e_3) = \begin{pmatrix} a - d & c - b \\ b + c & a + d \end{pmatrix}.
$$

**Proof.** The four displayed images are linearly independent, so the linear extension $\Phi$ is injective; the domain and the target both have real dimension $4$, so $\Phi$ is bijective. It remains to check that $\Phi$ is multiplicative. Since multiplication is bilinear, it suffices to check the generating products. Write $J = \Phi(e_1)$, $K = \Phi(e_2)$, $D = \Phi(e_3)$. A direct computation gives

$$
J^2 = -I, \qquad K^2 = I, \qquad JK = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} = D, \qquad KJ = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = -D,
$$

where $I$ is the identity matrix. These are exactly the relations $e_1^2 = -1$, $e_2^2 = +1$, $e_1 e_2 = e_3$, $e_2 e_1 = -e_3$, and the remaining products follow from them as in the multiplication table. Hence $\Phi(xy) = \Phi(x)\Phi(y)$ for all $x, y$. $\square$

The theorem is the algebraic content of the identification

$$
\mathbb{H}_{\mathrm{s}} \cong \mathrm{Cl}_{1,1} \cong M_2(\mathbb{R}).
$$

The matrix model is developed for its own sake in *Split-Quaternion Matrix Representations*, where it is shown to be unique up to conjugacy. Two features are used throughout the category and are recorded here.

**The trace is twice the scalar part.** For every $x$,

$$
\operatorname{tr} \Phi(x) = 2a = 2 \operatorname{Sc}(x).
$$

The trace therefore detects the scalar part, and the traceless matrices are the image of the vector subspace.

**The determinant is the norm form.** For every $x$,

$$
\det \Phi(x) = (a - d)(a + d) - (c - b)(b + c) = a^2 - d^2 - (c^2 - b^2) = a^2 + b^2 - c^2 - d^2.
$$

The quadratic form $N(x) = a^2 + b^2 - c^2 - d^2$ is introduced again in *Quadratic Forms* below, and the identity $\det \Phi(x) = N(x)$ is the reason the matrix model is the correct tool for the invertibility theory.

## Conjugations and Fixed-Point Subspaces

### The Conjugation

**Definition.** The **split-quaternion conjugation** is the map

$$
\bar{x} = a - b e_1 - c e_2 - d e_3 .
$$

It negates the three vector basis elements and fixes the scalars.

**Proposition.** The conjugation is an involutive algebra anti-automorphism: it is $\mathbb{R}$-linear, it satisfies $\overline{xy} = \bar{y}\, \bar{x}$ and $\overline{\bar{x}} = x$, and its fixed-point set is the scalar line $\mathbb{R}$.

**Proof.** Linearity and the second identity are immediate from the definition. For the anti-automorphism property it suffices to check the generators: $\overline{e_1 e_2} = \overline{e_3} = -e_3$, while $\bar{e}_2 \bar{e}_1 = (-e_2)(-e_1) = e_2 e_1 = -e_3$, and the other products are similar. The fixed points satisfy $b e_1 + c e_2 + d e_3 = -(b e_1 + c e_2 + d e_3)$, hence $b = c = d = 0$. $\square$

In the matrix model the conjugation is the adjugate, a fact recorded and used in *Split-Quaternion Matrix Representations*:

$$
\Phi(\bar{x}) = \operatorname{adj} \Phi(x).
$$

### The Two Eigenspaces

Since $\bar{\cdot}$ is an involutive linear map, the algebra decomposes into its $+1$ and $-1$ eigenspaces:

$$
\mathbb{H}_{\mathrm{s}} = S \oplus V, \qquad
S = \{x : \bar{x} = x\} = \mathbb{R} \cdot 1, \qquad
V = \{x : \bar{x} = -x\} = \operatorname{span}\{e_1, e_2, e_3\}.
$$

The **scalar subspace** $S$ is one-dimensional and is a subalgebra isomorphic to $\mathbb{R}$; it is the centre, as *The Centre and Simplicity* below shows. The **vector subspace** $V$ is three-dimensional, it is not a subalgebra, and it is the natural home of the geometry of the system. Every element decomposes uniquely as

$$
x = \tfrac{1}{2}(x + \bar{x}) + \tfrac{1}{2}(x - \bar{x}),
$$

the first summand lying in $S$ and the second in $V$.

### The Other Two Involutions

Two further involutions act on the algebra, and they are recorded here because the subspaces of *Split-Quaternion Analysis on Subspaces* are cut out by them. The **principal involution** $\alpha$ is the algebra automorphism defined on the generators by

$$
\alpha(e_1) = -e_1, \qquad \alpha(e_2) = -e_2, \qquad \alpha(e_3) = e_3,
$$

and the **reversal** $\rho$ is the algebra anti-automorphism defined by

$$
\rho(e_1) = e_1, \qquad \rho(e_2) = e_2, \qquad \rho(e_3) = -e_3 .
$$

Both are involutions, they commute, and their composite is the conjugation: $\bar{x} = \alpha(\rho(x)) = \rho(\alpha(x))$. Because they commute, each preserves the eigenspaces of the other, and the algebra decomposes into their common eigenspaces. The two involutions do not separate $e_1$ from $e_2$, however: $\alpha$ acts as $-1$ on the whole plane $\operatorname{span}\{e_1,e_2\}$, and $\rho$ acts as $+1$ on that plane, so the common eigenspaces are

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{R} \cdot 1 \oplus \operatorname{span}\{e_1,e_2\} \oplus \mathbb{R} e_3,
$$

of dimensions $1, 2, 1$, the sign pair $(\alpha,\rho)$ being $(+,+)$ on $\mathbb{R}\cdot 1$, $(-,+)$ on $\operatorname{span}\{e_1,e_2\}$ and $(+,-)$ on $\mathbb{R}e_3$. This is the finest decomposition produced by the three involutions: on $\operatorname{span}\{e_1,e_2\}$ all three act as $-1$, so no eigenspace of any of them splits that plane. The eigenspaces of the involutions taken one at a time are the ones used in *Split-Quaternion Analysis on Subspaces*: the principal involution has $+1$ on $\operatorname{span}\{1,e_3\}$ and $-1$ on $\operatorname{span}\{e_1,e_2\}$; the reversal has $+1$ on $\operatorname{span}\{1,e_1,e_2\}$ and $-1$ on $\mathbb{R}e_3$; and the conjugation has $+1$ on $\mathbb{R}\cdot 1$ and $-1$ on $V$.

## Quadratic Forms

### The Norm Form

**Definition.** The **norm form** of a split-quaternion $x$ is

$$
N(x) = x \bar{x} = \bar{x} x = a^2 + b^2 - c^2 - d^2 .
$$

The two products agree because $\bar{x}$ is an anti-automorphism and $x\bar{x} = \overline{x\bar{x}}$.

**Proposition.** The norm form is a quadratic form of **signature $(2,2)$**. It is multiplicative,

$$
N(xy) = N(x) N(y),
$$

and under the matrix model it is the determinant: $N(x) = \det \Phi(x)$.

**Proof.** The signature is read from the diagonal form $\operatorname{diag}(+1, +1, -1, -1)$ in the basis $1, e_1, e_2, e_3$. Multiplicativity follows from the anti-automorphism property:

$$
N(xy) = xy \overline{xy} = xy\, \bar{y} \bar{x} = x N(y) \bar{x} = N(y) x \bar{x} = N(x)N(y),
$$

where $N(y)$ is a real scalar and therefore central. The determinant identity is the computation of the preceding section. $\square$

The norm form is **indefinite**: it is positive on $\mathbb{R} \cdot 1 \oplus \mathbb{R} e_1$, negative on $\mathbb{R} e_2 \oplus \mathbb{R} e_3$, and it vanishes on a three-dimensional cone. This is in sharp contrast with the quaternion norm, which is positive definite, and it is the algebraic origin of every difference between the two theories.

### The Bilinear Form

**Definition.** The **bilinear form** polarised from $N$ is

$$
B(x, y) = \tfrac{1}{2}\big(N(x + y) - N(x) - N(y)\big).
$$

In the basis $1, e_1, e_2, e_3$ its matrix is $\operatorname{diag}(+1, +1, -1, -1)$, and on developed elements

$$
B(x, y) = a a' + b b' - c c' - d d',
$$

for $x = a + be_1 + ce_2 + de_3$ and $y = a' + b'e_1 + c'e_2 + d'e_3$. The form $B$ is symmetric and bilinear, it satisfies $B(x,x) = N(x)$, and it is non-degenerate of signature $(2,2)$.

### The Restricted Form on the Vector Subspace

The restriction of $N$ to $V$ is

$$
N(b e_1 + c e_2 + d e_3) = b^2 - c^2 - d^2,
$$

a form of **signature $(2,1)$**: one direction of square $+1$ and two of square $-1$. It is the three-dimensional Minkowski form written in the basis $e_1, e_2, e_3$. Its null cone in $V$ is the set

$$
b^2 = c^2 + d^2,
$$

a cone over a pair of lines, and every nonzero element of it is a nonzero nilpotent, since for $x \in V$ one has $x^2 = -N(x)$ and therefore $x^2 = 0$ exactly when $N(x) = 0$. The signature $(2,1)$ of this restriction, and not $(3,1)$, is the root of the geometry of the category: the group of the algebra acts on $V$ as the Lorentz group of a three-dimensional form, and the hyperbolic geometry the system carries is the hyperbolic plane. This is developed in *Split-Quaternion Rotations and the Lorentz Group*, *Split-Quaternion Geometry* and *Split-Quaternions and Hyperbolic Geometry*.

## The Idempotents and the Split-Complex Subspaces

### The Idempotents

**Definition.** The two elements

$$
u_+ = \tfrac{1}{2}(1 + e_2), \qquad u_- = \tfrac{1}{2}(1 - e_2)
$$

are the **split-quaternion idempotents**.

**Theorem.** The elements $u_+$ and $u_-$ satisfy

$$
u_+^2 = u_+, \qquad u_-^2 = u_-, \qquad u_+ u_- = u_- u_+ = 0, \qquad u_+ + u_- = 1,
$$

and they are not central. Moreover

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{H}_{\mathrm{s}} u_+ \oplus \mathbb{H}_{\mathrm{s}} u_-
$$

is a direct sum of two minimal left ideals of real dimension $2$, and the corresponding statement holds on the right, $\mathbb{H}_{\mathrm{s}} = u_+ \mathbb{H}_{\mathrm{s}} \oplus u_- \mathbb{H}_{\mathrm{s}}$. The decomposition is a decomposition of left modules and not of algebras: the subalgebra generated by $u_+$ and $u_-$ is two-dimensional and is not the whole algebra.

**Proof.** The four identities are the computation

$$
u_+^2 = \tfrac{1}{4}(1 + 2e_2 + e_2^2) = \tfrac{1}{4}(2 + 2e_2) = u_+,
$$

and its analogue for $u_-$, together with $u_+u_- = \tfrac14(1 - e_2^2) = 0$ and $u_+ + u_- = 1$. For non-centrality, $e_1 u_+ = \tfrac12(e_1 + e_3)$ while $u_+ e_1 = \tfrac12(e_1 - e_3)$, so $e_1 u_+ \neq u_+ e_1$. An element $x u_+$ of the first summand is fixed by right multiplication by $u_+$, since $x u_+ u_+ = x u_+$, and the map $x \mapsto x u_+$ has image of dimension $2$ because its kernel is $\mathbb{H}_{\mathrm{s}} u_-$. The sum $\mathbb{H}_{\mathrm{s}} u_+ + \mathbb{H}_{\mathrm{s}} u_-$ is all of $\mathbb{H}_{\mathrm{s}}$, since $x = x(u_+ + u_-)$, and the intersection is zero: if $x u_+ = y u_-$ then multiplying on the right by $u_+$ gives $x u_+ = 0$. Hence the sum is direct, and both summands are minimal because $M_2(\mathbb{R})$ has minimal left ideals of dimension $2$ and the model preserves minimality. The final claim holds because $u_+ u_- = 0$ and the span of $u_+, u_-$ has dimension $2$. $\square$

### The Split-Complex Subspaces

The line $\mathbb{R} \cdot 1$ together with either of the two square-$+1$ generators spans a copy of the split-complex algebra inside $\mathbb{H}_{\mathrm{s}}$:

$$
\mathbb{D}_2 = \operatorname{span}\{1, e_2\} \cong \mathbb{D}, \qquad
\mathbb{D}_3 = \operatorname{span}\{1, e_3\} \cong \mathbb{D},
$$

where $\mathbb{D} = \mathbb{R}[j]/(j^2-1)$ is the split-complex algebra of *Split-Complex Algebra*. Both are commutative subalgebras, both have the two idempotents $\tfrac12(1 \pm e_2)$ and $\tfrac12(1 \pm e_3)$ respectively, and both carry the zero divisors $1 \pm e_2$ and $1 \pm e_3$. The whole algebra is generated by $\mathbb{D}_2$ together with the single element $e_1$:

$$
\mathbb{H}_{\mathrm{s}} = \mathbb{D}_2 \oplus \mathbb{D}_2 e_1 , \qquad e_1 d = \bar{d} e_1 \ \ (d \in \mathbb{D}_2),
$$

which exhibits $\mathbb{H}_{\mathrm{s}}$ as a two-dimensional module over the split-complex algebra with a conjugation-twisted multiplication. The idempotents $u_\pm$ of the algebra are the idempotents of the subalgebra $\mathbb{D}_2$; they are non-central in $\mathbb{H}_{\mathrm{s}}$ precisely because $e_1$ does not commute with $e_2$.

## The Centre and Simplicity

**Theorem (The Centre).** The centre of $\mathbb{H}_{\mathrm{s}}$ is the scalar line:

$$
Z(\mathbb{H}_{\mathrm{s}}) = \{x : xy = yx \ \text{for all} \ y\} = \mathbb{R} \cdot 1 .
$$

**Proof.** The scalars are central. Conversely, suppose $x = a + \mathbf{v}$ is central. Commuting $x$ with $e_1$ gives

$$
0 = x e_1 - e_1 x .
$$

The scalar part of $x$ commutes with everything, so the condition is $\mathbf{v} e_1 - e_1 \mathbf{v} = 0$. Writing $\mathbf{v} = b e_1 + c e_2 + d e_3$ and using the table,

$$
\mathbf{v} e_1 = -b - c e_3 + d e_2, \qquad e_1 \mathbf{v} = -b + c e_3 - d e_2,
$$

so $\mathbf{v} e_1 - e_1 \mathbf{v} = -2c e_3 + 2d e_2 = 0$, giving $c = d = 0$. Commuting with $e_2$ similarly gives $b = 0$. Hence $\mathbf{v} = 0$ and $x = a$ is scalar. $\square$

**Theorem (Simplicity).** The split-quaternion algebra is **simple**: it has no two-sided ideal other than $0$ and the algebra itself. It is therefore semisimple, and as a left module over itself it is the direct sum of two isomorphic minimal left ideals, namely $\mathbb{H}_{\mathrm{s}} u_+$ and $\mathbb{H}_{\mathrm{s}} u_-$.

**Proof.** Under the isomorphism $\Phi$ the statement becomes the corresponding statement for $M_2(\mathbb{R})$, which is proved in *Matrix Algebras*: a nonzero two-sided ideal of $M_2(\mathbb{R})$ contains a nonzero matrix, hence a matrix unit after multiplying by elementary matrices on the left and on the right, and the matrix units generate the whole algebra. The minimal left ideals are $\mathbb{H}_{\mathrm{s}} u_\pm$ by the theorem on the idempotents, and they are isomorphic because they are the images of the two factors of a simple algebra. $\square$

The algebra is thus **associative, non-commutative, simple**, with centre $\mathbb{R}$, and it is **not** a division algebra. The combination is worth naming: a simple algebra with zero divisors over $\mathbb{R}$ is necessarily a full matrix algebra over a division algebra, and here that division algebra is $\mathbb{R}$ itself, of size $2$.

## The Lie Algebra Structure

The algebra carries the commutator bracket $[x, y] = xy - yx$, which makes it a real Lie algebra. The bracket of two elements of $V$ lies in $V$, since

$$
[e_1, e_2] = 2 e_3, \qquad [e_2, e_3] = -2 e_1, \qquad [e_3, e_1] = 2 e_2 .
$$

So $V$ is a three-dimensional Lie subalgebra of $\mathbb{H}_{\mathrm{s}}$. Under the matrix model it is the subspace of traceless $2 \times 2$ real matrices,

$$
\Phi(V) = \mathfrak{sl}_2(\mathbb{R}),
$$

and $\Phi$ restricted to $V$ is a Lie algebra isomorphism

$$
V \cong \mathfrak{sl}_2(\mathbb{R}) .
$$

The bracket above is the bracket of the special linear Lie algebra in the basis $e_3 = \mathrm{diag}(-1,1)$, $e_2 = \begin{pmatrix}0&1\\1&0\end{pmatrix}$, $e_1 = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$. This is the algebraic origin of the relation between the split-quaternions and the Lorentz group of signature $(2,1)$: the vector subspace is a Lie algebra of infinitesimal Lorentz transformations, and the exponential of the bracket gives the rotations of *Split-Quaternion Rotations and the Lorentz Group*.

The scalar line $S$ is the centre of $\mathbb{H}_{\mathrm{s}}$ and therefore contributes nothing to the bracket. The full Lie algebra $\mathbb{H}_{\mathrm{s}}$ is the abelian extension $\mathfrak{sl}_2(\mathbb{R}) \oplus \mathbb{R}$, i.e. the direct sum of the bracket algebra on $V$ and a central scalar line.

## Comparison with $\mathbb{H}$ and with $\mathbb{H}_{\mathbb{D}}$

### Comparison with the Quaternions

The split-quaternions and the quaternions are the two real forms of the same complexified algebra, and they differ in the sign of one generator. The following table collects the contrast; the quaternion column is supported by *Quaternion Algebra*.

| | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ |
|---|---|---|
| basis and squares | $e_1^2=e_2^2=e_3^2=-1$ | $e_1^2=-1$, $e_2^2=e_3^2=+1$ |
| norm form | $q_0^2+q_1^2+q_2^2+q_3^2$, signature $(4,0)$ | $a^2+b^2-c^2-d^2$, signature $(2,2)$ |
| zero divisors | none | the null cone of $N$ |
| nonzero nilpotents | none | yes |
| division algebra | yes | no |
| centre | $\mathbb{R}$ | $\mathbb{R}$ |
| vector subspace | $\mathbb{R}^3$, $\mathfrak{so}(3)$ | $V$, $\mathfrak{sl}_2(\mathbb{R})$, form of signature $(2,1)$ |
| scalar group attached | $Sp(1) \cong SU(2)$ | $\mathrm{SL}_2(\mathbb{R})$ |

The decisive difference is the sign of the norm form. The quaternion norm is positive definite, so the unit sphere is compact and the group of unit quaternions is $Sp(1) \cong SU(2)$, double-covering $\mathrm{SO}(3)$. The split-quaternion norm is indefinite of signature $(2,2)$, so the unit set is non-compact, the group of norm-one elements is $\mathrm{SL}_2(\mathbb{R})$, and the group it double-covers is the Lorentz group of signature $(2,1)$. The change of a single sign turns a compact three-sphere into a non-compact three-dimensional group and the rotations of three-space into the Lorentz transformations of the hyperbolic plane.

### Comparison with the Split-Biquaternions

The name *split quaternions* is used in the classical literature for the four-dimensional algebra $\mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ of this article, and it is not the algebra that the corpus writes $\mathbb{H}_{\mathbb{D}}$. The corpus reserves $\mathbb{H}_{\mathbb{D}}$ for the eight-dimensional tensor product $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$, the **split-biquaternions**; the distinction is stated once, in *The Number Systems as Clifford Algebras*, and is recorded again in *Examples of Algebras* and in *List of Algebras by Dimension*. The two algebras must not be identified, and the following table records why.

| | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|
| dimension over $\mathbb{R}$ | $4$ | $8$ |
| isomorphic to | $\mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ | $\mathrm{Cl}_{0,3} \cong \mathbb{H} \oplus \mathbb{H}$ |
| simple | yes | no |
| centre | $\mathbb{R}$ | $\mathbb{D}$ |
| idempotents | non-central only | central, $e_\pm$ |
| nonzero nilpotents | yes | no |

The two rows that separate the algebras most sharply are the last two. A nilpotent is an element $x \neq 0$ with $x^2 = 0$, and the split-quaternion algebra has them: $(e_1 + e_3)^2 = e_1^2 + e_1e_3 + e_3e_1 + e_3^2 = -1 + 0 + 1 = 0$, since $e_1 e_3 = -e_3 e_1$. An algebra that is a product of two division algebras, as $\mathbb{H}_{\mathbb{D}}$ is by the dictionary of *The Number Systems as Clifford Algebras*, has no nilpotents at all, because a nilpotent would have a nilpotent component in one of the factors and a division algebra has none. Simultaneously, the split-quaternion algebra is **simple**, while a product of two algebras is not. A **simple** algebra with nilpotents and non-central idempotents is therefore entirely different from a **semisimple, non-simple** product of two division algebras with central idempotents and no nilpotents.

The eight-dimensional relative of the corpus is treated later in Part V, under Split-Biquaternions; nothing in it is used here. What is stated here is stated from the algebra of this article and from the conventions: a four-dimensional simple real algebra with an isotropic determinant form, on the one hand, and the eight-dimensional $\mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ of the notation table, on the other.

## Summary

The split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$ is the four-dimensional real algebra with basis $1, e_1, e_2, e_3$, the products $e_1^2 = -1$, $e_2^2 = e_3^2 = +1$, the anticommutation $e_1 e_2 = -e_2 e_1$ and $e_3 = e_1 e_2$. It is associative, non-commutative and simple, with centre $\mathbb{R}$, and it is not a division algebra: $1 + e_2$ and $1 - e_2$ are nonzero and multiply to zero.

The algebra is the Clifford algebra $\mathrm{Cl}_{1,1}$ of a form of signature $(1,1)$, and it is isomorphic to the matrix algebra $M_2(\mathbb{R})$ by an explicit map $\Phi$ whose determinant is the norm form and whose trace is twice the scalar part. The norm form $N(x) = a^2 + b^2 - c^2 - d^2$ has signature $(2,2)$ and is multiplicative; restricted to the vector subspace $V$ it is the Minkowski form of signature $(2,1)$, and the group of the algebra acts on $V$ through $\mathfrak{sl}_2(\mathbb{R})$.

The conjugation $\bar{x} = a - be_1 - ce_2 - de_3$ is an involutive anti-automorphism whose fixed-point subspaces are the scalar line $S$ and the vector space $V$. The principal involution and the reversal commute and cut the algebra into the scalar line, the plane $\operatorname{span}\{e_1,e_2\}$ and the line $\mathbb{R}e_3$. The idempotents $u_\pm = \tfrac12(1 \pm e_2)$ are non-central, sum to $1$, multiply to zero, and split the algebra as a direct sum of two minimal left ideals, and not as an algebra. The split-complex subalgebras $\operatorname{span}\{1,e_2\}$ and $\operatorname{span}\{1,e_3\}$ are copies of $\mathbb{D}$ and carry the zero divisors of the algebra.

The system is not the eight-dimensional $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ of the notation table, which is neither simple nor free of nilpotents; the two are distinguished once, in *The Number Systems as Clifford Algebras*.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra, $\mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ | this article |
| $1, e_1, e_2, e_3$ | the basis, with $e_1^2=-1$, $e_2^2=e_3^2=+1$, $e_3=e_1e_2$ | this article |
| $x = a + be_1 + ce_2 + de_3$ | a general split-quaternion | this article |
| $a = \operatorname{Sc}(x)$ | the scalar part | this article |
| $\mathbf{v} = \operatorname{Vec}(x)$ | the vector part | this article |
| $S = \mathbb{R}\cdot1$ | the scalar subspace | this article |
| $V = \operatorname{span}\{e_1,e_2,e_3\}$ | the vector subspace | this article |
| $\bar{x} = a - be_1 - ce_2 - de_3$ | the split-quaternion conjugation | this article |
| $\alpha$ | the principal involution, $e_1,e_2 \mapsto -e_1,-e_2$, $e_3 \mapsto e_3$ | this article |
| $\rho$ | the reversal, $e_1,e_2 \mapsto e_1,e_2$, $e_3 \mapsto -e_3$ | this article |
| $\Phi$ | the isomorphism $\mathbb{H}_{\mathrm{s}} \to M_2(\mathbb{R})$ | *Split-Quaternion Matrix Representations* |
| $N(x) = x\bar{x} = a^2+b^2-c^2-d^2$ | the norm form, signature $(2,2)$ | *Split-Quaternion Norm and Invertibility* |
| $B(x,y)$ | the polarised bilinear form | *Split-Quaternion Norm and Invertibility* |
| $u_\pm = \tfrac12(1 \pm e_2)$ | the non-central idempotents | this article |
| $\mathbb{D}_2 = \operatorname{span}\{1,e_2\}$, $\mathbb{D}_3 = \operatorname{span}\{1,e_3\}$ | the split-complex subalgebras | this article |
| $[x,y] = xy - yx$ | the commutator bracket | this article |
| $\mathfrak{sl}_2(\mathbb{R})$ | the Lie algebra $\Phi(V)$ of traceless matrices | this article |
| $\mathbb{D}$ | the split-complex numbers, $j^2=+1$ | *Split-Complex Algebra* |
| $\mathbb{H}$ | the real quaternions | *Quaternion Algebra* |
| $\mathbb{H}_{\mathbb{D}}$ | the split-biquaternions, $\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$, a later Part V system | *The Number Systems as Clifford Algebras* |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first appearance of the algebra as the even part of a Clifford algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the low-dimensional classification $\mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$ and the coquaternion terminology.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the identification of the classical groups of the algebra with the matrix groups.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the split forms of the composition algebras and the place of the algebra among them.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the isotropic forms and their maximal totally isotropic subspaces.
