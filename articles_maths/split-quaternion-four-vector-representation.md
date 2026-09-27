
# __Split-Quaternion Four-Vector Representation__

## Introduction

The split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$ is the four-dimensional real algebra with basis $1, e_1, e_2, e_3$, where $e_1^2 = -1$, $e_2^2 = e_3^2 = +1$, $e_3 = e_1 e_2$ and $e_1 e_2 = -e_2 e_1$. A general element is written

$$
\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3, \qquad q_0, q_1, q_2, q_3 \in \mathbb{R}.
$$

The algebra, its three involutions, its distinguished subspaces and its norm form are those of the companion articles *Split-Quaternion Algebra* and *Split-Quaternion Scalar and Vector Subspaces*, and nothing of that structure is re-derived here except where the coordinate realization requires it.

This article presents the **four-vector realization** of $\mathbb{H}_{\mathrm{s}}$: the split-quaternion read off as its list of four real coefficients. The word *representation* is used in the sense of a concrete realization of the algebra as computable objects, the sense in which *Split-Quaternion Other Algebraic Representations* uses it, and not in the technical sense of a vector space carrying an algebra homomorphism into its endomorphisms. The technical sense is the subject of *Split-Quaternion Representations*. The article owns the coefficient space, the column and the dual row, the component form of the product, the three involutions in coordinates, the distinguished subspaces as coordinate conditions, and the norm form with its signatures. It introduces no physical vocabulary.

## The Coefficient Space

**Definition.** The **four-vector** of a split-quaternion $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ is the ordered quadruple

$$
\tilde q^\mu = (q_0, q_1, q_2, q_3), \qquad \tilde q^0 = q_0, \quad (\tilde q^1, \tilde q^2, \tilde q^3) = (q_1, q_2, q_3),
$$

where $\tilde q^0$ is the **scalar component** and $\tilde q^1, \tilde q^2, \tilde q^3$ are the **vector components**. Unlike the biquaternion case, every component is a real number, because $\mathbb{H}_{\mathrm{s}}$ has no central imaginary unit and no complex structure.

**Proposition.** The map $\tilde q \mapsto \tilde q^\mu$ is an $\mathbb{R}$-linear isomorphism from $\mathbb{H}_{\mathrm{s}}$ onto $\mathbb{R}^4$. Consequently the coefficient space has real dimension $4$.

**Proof.** The map sends the basis $1, e_1, e_2, e_3$ to the standard basis of $\mathbb{R}^4$ and is extended by linearity; it is bijective on bases. $\square$

The coefficient space $\mathbb{R}^4$ is **not** the simple module of $\mathbb{H}_{\mathrm{s}}$. The simple module has real dimension $2$ and is the subject of *Split-Quaternion Matrix Representations*; the coefficient space is the algebra itself, of real dimension $4$. The number $4$ recurs as the size of the matrix of the regular action on this space, and it is the same four for a different reason: the algebra has real dimension $4$, so the matrix of its left action on itself is $4 \times 4$.

## The Column and the Dual Row

**Definition.** The **column** of $\tilde q$ is the $4 \times 1$ matrix

$$
X = \begin{pmatrix} q_0 \\ q_1 \\ q_2 \\ q_3 \end{pmatrix},
$$

and the **row** is its transpose $X^{\mathsf{T}} = (q_0\ q_1\ q_2\ q_3)$.

The row is the **dual** object: the norm form $N$ is a non-degenerate quadratic form on $\mathbb{R}^4$, and its polarisation $B(\tilde q, y) = q_0 q_0' + q_1 q_1' - q_2 q_2' - q_3 q_3'$ provides a bilinear pairing that identifies the coefficient space with its dual, sending $y$ to the linear functional $\tilde q \mapsto B(\tilde q, y)$. In the coordinate basis this identification is multiplication by the matrix $\operatorname{diag}(1,1,-1,-1)$:

$$
B(\tilde q, y) = X^{\mathsf{T}} G Y, \qquad G = \operatorname{diag}(1,1,-1,-1).
$$

So the row is the dual vector paired with the column through $G$, and the two are equals only because the pairing is non-degenerate; when $G$ is replaced by the identity the pairing is the Euclidean one and the dual is the plain transpose.

## Multiplication in Components

Since $\tilde q \mapsto \tilde q^\mu$ is a linear isomorphism and the product is bilinear, the product of two split-quaternions is determined by its value on the basis. The **multiplication table** of the basis, whose entry in row $i$ and column $j$ is $e_i e_j$, is

| | $1$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $1$ | $1$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $e_1$ | $-1$ | $e_3$ | $-e_2$ |
| $e_2$ | $e_2$ | $-e_3$ | $+1$ | $-e_1$ |
| $e_3$ | $e_3$ | $e_2$ | $e_1$ | $+1$ |

**Proposition.** For $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ and $y = q_0' e_0 + q_1' e_1 + q_2' e_2 + q_3' e_3$, the product has components

$$
\tilde q y = (q_0 q_0' - q_1 q_1' + q_2 q_2' + q_3 q_3') + (q_0 q_1' + q_0' q_1 - q_2 q_3' + q_2' q_3)\,e_1
$$

$$
+ (q_0 q_2' + q_0' q_2 + q_1 q_3' - q_1' q_3)\,e_2 + (q_0 q_3' + q_0' q_3 + q_1 q_2' - q_1' q_2)\,e_3 .
$$

**Proof.** Expand the product bilinearly and read each surviving basis product from the table; for instance the $e_1$-coefficient collects $q_0 q_1'$ from $1 \cdot e_1$, $q_0' q_1$ from $e_1 \cdot 1$, $-q_2 q_3'$ from $e_2 \cdot e_3 = -e_1$, and $q_2' q_3$ from $e_3 \cdot e_2 = e_1$. $\square$

The scalar component of the product, $q_0 q_0' - q_1 q_1' + q_2 q_2' + q_3 q_3'$, is exactly the bilinear form $B(\tilde q,\bar{y})$ evaluated against the conjugate; the remaining coefficients are the antisymmetric remainder. In particular the product is **not** componentwise, and the sign pattern of the scalar component is that of the form $B$ read against the conjugated coordinates.

## The Three Involutions in Coordinates

The three involutions act on the four-vector by independent sign changes of the last three components:

| involution | $\tilde q^0 = q_0$ | $\tilde q^1 = q_1$ | $\tilde q^2 = q_2$ | $\tilde q^3 = q_3$ |
|---|---|---|---|---|
| conjugation $\bar{\cdot}$ | $+$ | $-$ | $-$ | $-$ |
| principal $\alpha$ | $+$ | $-$ | $-$ | $+$ |
| reversal $\rho$ | $+$ | $+$ | $+$ | $-$ |

Thus $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ has four-vector $(q_0,-q_1,-q_2,-q_3)$; $\alpha(\tilde q) = q_0 - q_1 e_1 - q_2 e_2 + q_3 e_3$ has $(q_0,-q_1,-q_2,q_3)$; and $\rho(\tilde q) = q_0 + q_1 e_1 + q_2 e_2 - q_3 e_3$ has $(q_0,q_1,q_2,-q_3)$. The scalar component is fixed by all three. The composition $\bar{\cdot} = \alpha\rho$ is the composition of the sign flips, and the three act on the vector triple $(q_1,q_2,q_3)$ by the sign patterns $(-,-,-)$, $(-,-,+)$, $(+,+,-)$, the subgroup of *Split-Quaternion Involution Lattice*.

## The Distinguished Subspaces in Coordinates

The four distinguished subspaces are cut out by coordinate conditions:

| subspace | coordinate condition | four-vectors |
|---|---|---|
| $S$ | $\tilde q^1 = \tilde q^2 = \tilde q^3 = 0$ | $(q_0,0,0,0)$ |
| $V$ | $\tilde q^0 = 0$ | $(0,q_1,q_2,q_3)$ |
| $\mathbb{D}_2$ | $\tilde q^1 = \tilde q^3 = 0$ | $(q_0,0,q_2,0)$ |
| $\mathbb{D}_3$ | $\tilde q^1 = \tilde q^2 = 0$ | $(q_0,0,0,q_3)$ |

So the scalar subspace is the first coordinate axis, the vector subspace is the hyperplane $\tilde q^0 = 0$, and the two split-complex planes are the coordinate planes $(q_0,q_2)$ and $(q_0,q_3)$. The fourth coordinate plane, $(q_0,q_1)$, is the definite plane $\mathbb{R}[e_1] \cong \mathbb{C}$, which is not among the four distinguished subspaces. The involutions of the previous section preserve each of these coordinate conditions, as the sign table shows.

## The Norm Form

The norm form of $\tilde q$ is

$$
N(\tilde q) = \tilde q\bar{\tilde q} = q_0^2 + q_1^2 - q_2^2 - q_3^2,
$$

of **signature $(2,2)$**, with polarisation $B(\tilde q,y) = q_0 q_0' + q_1 q_1' - q_2 q_2' - q_3 q_3'$ and matrix $G = \operatorname{diag}(1,1,-1,-1)$ in the coordinate basis. It is indefinite and non-degenerate, the scalar and $e_1$ directions being positive and the $e_2, e_3$ directions negative. Under the matrix model it is the determinant, $N(\tilde q) = \det \Phi(\tilde q)$.

The restrictions to the distinguished subspaces read off the coordinates:

| subspace | restriction of $N$ | signature |
|---|---|---|
| $S$ | $q_0^2$ | positive definite |
| $V$ | $q_1^2 - q_2^2 - q_3^2$ | $(2,1)$ |
| $\mathbb{D}_2$ | $q_0^2 - q_2^2$ | $(1,1)$ |
| $\mathbb{D}_3$ | $q_0^2 - q_3^2$ | $(1,1)$ |

Only the scalar restriction is definite; the others are indefinite, and their null sets are the zero-divisor sets of the respective subspaces.

## The Unit Criterion in Coordinates

**Theorem.** The four-vector $(q_0,q_1,q_2,q_3)$ is **invertible** if and only if

$$
N(\tilde q) = q_0^2 + q_1^2 - q_2^2 - q_3^2 \neq 0,
$$

and then $\tilde q^{-1} = \bar{\tilde q}/N(\tilde q) = \dfrac{q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3}{q_0^2+q_1^2-q_2^2-q_3^2}$. Equivalently, the element is a unit if and only if the determinant of the matrix model is nonzero.

**Proof.** The identity $\tilde q\bar{\tilde q} = N(\tilde q)$ gives $\tilde q \cdot (\bar{\tilde q}/N(\tilde q)) = 1$ whenever $N(\tilde q) \neq 0$; conversely, if $N(\tilde q) = 0$ with $\tilde q \neq 0$, then $\tilde q\bar{\tilde q} = 0$ with $\bar{\tilde q} \neq 0$, so $\tilde q$ is a zero divisor and cannot be a unit. $\square$

The non-invertible nonzero four-vectors are exactly those on the **null cone** $q_0^2 + q_1^2 = q_2^2 + q_3^2$; on the vector subspace $q_0 = 0$ this is the light cone $q_1^2 = q_2^2 + q_3^2$ of the Minkowski form, and in the split-complex plane $\mathbb{D}_2$ it is the pair of isotropic lines $q_0 = \pm q_2$.

## The Analogue of the Four-Vector Representation of $\mathbb{B}$

The biquaternion article *Biquaternion Four-Vector Representation* reads $\tilde q = \sum_\mu Q_\mu e_\mu$ as a quadruple of **complex** coefficients, so that the coefficient space is $\mathbb{C}^4$ of real dimension $8$; two of its six distinguished subspaces are read from the real and imaginary parts of the coefficients, and the norm form becomes a complex quadratic form with a positive-definite Euclidean companion. The split-quaternion case is the real, split analogue: the coefficient space is $\mathbb{R}^4$ of real dimension $4$, the coefficients are real, all four distinguished subspaces are read directly from coordinate conditions, and the norm form is a single real form of signature $(2,2)$ with no complex companion. The structural parallel is exact — a quadruple, a column, a dual row, the component product, the involutions as sign flips, and the norm form in coordinates — but every object is real and indefinite here where it is complex in $\mathbb{B}$. Nothing biquaternion-specific — the central imaginary unit $i$, the real-imaginary splitting of the coefficients, the complex definite companion — is imported.

## Summary

The four-vector realization reads a split-quaternion $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ as the quadruple $(q_0,q_1,q_2,q_3) \in \mathbb{R}^4$, an $\mathbb{R}$-linear isomorphism $\mathbb{H}_{\mathrm{s}} \to \mathbb{R}^4$ with no complex structure. The column $X$ is the quadruple written vertically and the row $X^{\mathsf{T}}$ is its dual under the non-degenerate pairing $B$ with matrix $G = \operatorname{diag}(1,1,-1,-1)$.

The product is computed in components by the displayed formula, whose scalar part is $B(\tilde q,\bar{y})$ and whose vector part is the antisymmetric remainder. The three involutions act by independent sign flips of $(q_1,q_2,q_3)$: conjugation by $(-,-,-)$, the principal involution by $(-,-,+)$, and the reversal by $(+,+,-)$, with the scalar component always fixed. The distinguished subspaces are the coordinate conditions $q_0$-axis ($S$), $\tilde q^0=0$ ($V$), and the $(q_0,q_2)$-, $(q_0,q_3)$-planes ($\mathbb{D}_2, \mathbb{D}_3$). The norm form is $q_0^2 + q_1^2 - q_2^2 - q_3^2$ of signature $(2,2)$, restricting to $q_0^2$, $q_1^2-q_2^2-q_3^2$, $q_0^2-q_2^2$ and $q_0^2-q_3^2$ on the four subspaces, and it gives the unit criterion $N \neq 0$ with $\tilde q^{-1} = \bar{\tilde q}/N$. This is the real, indefinite analogue of the complex four-vector representation of $\mathbb{B}$.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | a general split-quaternion | *Split-Quaternion Algebra* |
| $\tilde q^\mu = (q_0,q_1,q_2,q_3)$ | the four-vector of $\tilde q$ | this article |
| $\tilde q^0 = q_0$, $(\tilde q^1,\tilde q^2,\tilde q^3) = (q_1,q_2,q_3)$ | the scalar and vector components | this article |
| $X$, $X^{\mathsf{T}}$ | the column and the dual row | this article |
| $G = \operatorname{diag}(1,1,-1,-1)$ | the matrix of the polarised form in coordinates | this article |
| $N(\tilde q) = q_0^2+q_1^2-q_2^2-q_3^2$ | the norm form, signature $(2,2)$ | *Split-Quaternion Norm and Invertibility* |
| $B(\tilde q,y)$ | the polarised bilinear form | *Split-Quaternion Norm and Invertibility* |
| $\bar{\cdot}, \alpha, \rho$ | the three involutions as sign flips | *Split-Quaternion Subspaces and the Involutions* |
| $S, V, \mathbb{D}_2, \mathbb{D}_3$ | the distinguished subspaces as coordinate conditions | *Split-Quaternion Relations Between Subspaces* |
| $\tilde q^{-1} = \bar{\tilde q}/N(\tilde q)$ | the inverse of a unit | *Split-Quaternion Norm and Invertibility* |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the coefficient space of a Clifford algebra and the coordinate form of its product.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the coordinate multiplication tables and the matrix generators of the low-dimensional algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the coordinate descriptions of the split forms.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for polarisation, the matrix of a bilinear form, and the inertia law.
