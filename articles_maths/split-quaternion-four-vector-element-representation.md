
# __Split-Quaternion Four-Vector Element Representation__

## Introduction

The split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$ is the four-dimensional real algebra with basis $1, \vec e_x, \vec e_y, \vec e_z$, where $\vec e_x^2 = -1$, $\vec e_y^2 = \vec e_z^2 = +1$, $\vec e_z = \vec e_x \vec e_y$ and $\vec e_x \vec e_y = -\vec e_y \vec e_x$. A general element is written

$$
\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z, \qquad q_t, q_x, q_y, q_z \in \mathbb{R}.
$$

The algebra, its three involutions, its distinguished subspaces and its split-quaternion norm are those of the companion articles *Split-Quaternion Algebra* and *Split-Quaternion Scalar and Vector Subspaces*, and nothing of that structure is re-derived here except where the coordinate realization requires it.

This article presents the **four-vector realization** of $\mathbb{H}_{\mathrm{s}}$: the split-quaternion read off as its list of four real coefficients. The word *representation* is used in the sense of a concrete realization of the algebra as computable objects, the sense in which *Split-Quaternion Other Algebraic Element Representations* uses it, and not in the technical sense of a vector space carrying an algebra homomorphism into its endomorphisms. The technical sense is the subject of *Split-Quaternion Element Representations*. The article owns the coefficient space, the column and the dual row, the component form of the product, the three involutions in coordinates, the distinguished subspaces as coordinate conditions, and the split-quaternion norm with its signatures. It introduces no physical vocabulary.

## The Coefficient Space

**Definition.** The **four-vector** of a split-quaternion $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ is the ordered quadruple

$$
\tilde q^\mu = (q_t, q_x, q_y, q_z), \qquad \tilde q^0 = q_t, \quad (\tilde q^1, \tilde q^2, \tilde q^3) = (q_x, q_y, q_z),
$$

where $\tilde q^0$ is the **scalar component** and $\tilde q^1, \tilde q^2, \tilde q^3$ are the **vector components**. Unlike the biquaternion case, every component is a real number, because $\mathbb{H}_{\mathrm{s}}$ has no central imaginary unit and no complex structure.

**Proposition.** The map $\tilde q \mapsto \tilde q^\mu$ is an $\mathbb{R}$-linear isomorphism from $\mathbb{H}_{\mathrm{s}}$ onto $\mathbb{R}^4$. Consequently the coefficient space has real dimension $4$.

**Proof.** The map sends the basis $1, \vec e_x, \vec e_y, \vec e_z$ to the standard basis of $\mathbb{R}^4$ and is extended by linearity; it is bijective on bases.

The coefficient space $\mathbb{R}^4$ is **not** the simple module of $\mathbb{H}_{\mathrm{s}}$. The simple module has real dimension $2$ and is the subject of *Split-Quaternion Matrix Element Representations*; the coefficient space is the algebra itself, of real dimension $4$. The number $4$ recurs as the size of the matrix of the regular action on this space, and it is the same four for a different reason: the algebra has real dimension $4$, so the matrix of its left action on itself is $4 \times 4$.

## The Column and the Dual Row

**Definition.** The **column** of $\tilde q$ is the $4 \times 1$ matrix

$$
X = \begin{pmatrix} q_t \\ q_x \\ q_y \\ q_z \end{pmatrix},
$$

and the **row** is its transpose $X^{\mathsf{T}} = (q_t\ q_x\ q_y\ q_z)$.

The row is the **dual** object: the split-quaternion norm $\langle\cdot\rangle_{\natural}$ is a non-degenerate quadratic form on $\mathbb{R}^4$, and its polarisation $\langle\tilde q_1,\tilde q_2\rangle = q_{1t} q_{2t} + q_{1x} q_{2x} - q_{1y} q_{2y} - q_{1z} q_{2z}$ provides a bilinear pairing that identifies the coefficient space with its dual, sending $\tilde q_2$ to the linear functional $\tilde q_1 \mapsto \langle\tilde q_1,\tilde q_2\rangle$. In the coordinate basis this identification is multiplication by the matrix $\operatorname{diag}(1,1,-1,-1)$:

$$
\langle\tilde q_1,\tilde q_2\rangle = X^{\mathsf{T}} G Y, \qquad G = \operatorname{diag}(1,1,-1,-1).
$$

So the row is the dual vector paired with the column through $G$, and the two are equals only because the pairing is non-degenerate; when $G$ is replaced by the identity the pairing is the Euclidean one and the dual is the plain transpose.

## Multiplication in Components

Since $\tilde q \mapsto \tilde q^\mu$ is a linear isomorphism and the product is bilinear, the product of two split-quaternions is determined by its value on the basis. The **multiplication table** of the basis, whose entry in row $\mu$ and column $\nu$ is $e_\mu e_\nu$, is

| | $1$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $1$ | $1$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-1$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $+1$ | $-\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $\vec e_x$ | $+1$ |

**Proposition.** For $\tilde q_1 = q_{1t} e_t + q_{1x} \vec e_x + q_{1y} \vec e_y + q_{1z} \vec e_z$ and $\tilde q_2 = q_{2t} e_t + q_{2x} \vec e_x + q_{2y} \vec e_y + q_{2z} \vec e_z$, the product has components

$$
\tilde q_1 \tilde q_2 = (q_{1t} q_{2t} - q_{1x} q_{2x} + q_{1y} q_{2y} + q_{1z} q_{2z}) + (q_{1t} q_{2x} + q_{2t} q_{1x} - q_{1y} q_{2z} + q_{2y} q_{1z})\,\vec e_x
$$

$$
+ (q_{1t} q_{2y} + q_{2t} q_{1y} + q_{1x} q_{2z} - q_{2x} q_{1z})\,\vec e_y + (q_{1t} q_{2z} + q_{2t} q_{1z} + q_{1x} q_{2y} - q_{2x} q_{1y})\,\vec e_z .
$$

**Proof.** Expand the product bilinearly and read each surviving basis product from the table; for instance the $\vec e_x$-coefficient collects $q_{1t} q_{2x}$ from $1 \cdot \vec e_x$, $q_{2t} q_{1x}$ from $\vec e_x \cdot 1$, $-q_{1y} q_{2z}$ from $\vec e_y \cdot \vec e_z = -\vec e_x$, and $q_{2y} q_{1z}$ from $\vec e_z \cdot \vec e_y = \vec e_x$.

The scalar component of the product, $q_{1t} q_{2t} - q_{1x} q_{2x} + q_{1y} q_{2y} + q_{1z} q_{2z}$, is exactly the bilinear form $\langle\tilde q_1,\tilde q_2^{\natural}\rangle$ evaluated against the conjugate; the remaining coefficients are the antisymmetric remainder. In particular the product is **not** componentwise, and the sign pattern of the scalar component is that of the form $\langle\cdot,\cdot\rangle_{\natural}$ read against the conjugated coordinates.

## The Three Involutions in Coordinates

The three involutions act on the four-vector by independent sign changes of the last three components:

| involution | $\tilde q^0 = q_t$ | $\tilde q^1 = q_x$ | $\tilde q^2 = q_y$ | $\tilde q^3 = q_z$ |
|---|---|---|---|---|
| conjugation ${}^{\natural}$ | $+$ | $-$ | $-$ | $-$ |
| principal $\alpha$ | $+$ | $-$ | $-$ | $+$ |
| reversal $\rho$ | $+$ | $+$ | $+$ | $-$ |

Thus $\tilde{q}^{\natural} = q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z$ has four-vector $(q_t,-q_x,-q_y,-q_z)$; $\alpha(\tilde q) = q_t - q_x \vec e_x - q_y \vec e_y + q_z \vec e_z$ has $(q_t,-q_x,-q_y,q_z)$; and $\rho(\tilde q) = q_t + q_x \vec e_x + q_y \vec e_y - q_z \vec e_z$ has $(q_t,q_x,q_y,-q_z)$. The scalar component is fixed by all three. The composition ${}^{\natural} = \alpha\rho$ is the composition of the sign flips, and the three act on the vector triple $(q_x,q_y,q_z)$ by the sign patterns $(-,-,-)$, $(-,-,+)$, $(+,+,-)$, the subgroup of *Split-Quaternion Involution Lattice*.

## The Distinguished Subspaces in Coordinates

The four distinguished subspaces are cut out by coordinate conditions:

| subspace | coordinate condition | four-vectors |
|---|---|---|
| $S$ | $\tilde q^1 = \tilde q^2 = \tilde q^3 = 0$ | $(q_t,0,0,0)$ |
| $V$ | $\tilde q^0 = 0$ | $(0,q_x,q_y,q_z)$ |
| $\mathbb{D}_2$ | $\tilde q^1 = \tilde q^3 = 0$ | $(q_t,0,q_y,0)$ |
| $\mathbb{D}_3$ | $\tilde q^1 = \tilde q^2 = 0$ | $(q_t,0,0,q_z)$ |

So the scalar subspace is the first coordinate axis, the vector subspace is the hyperplane $\tilde q^0 = 0$, and the two split-complex planes are the coordinate planes $(q_t,q_y)$ and $(q_t,q_z)$. The fourth coordinate plane, $(q_t,q_x)$, is the definite plane $\mathbb{R}[\vec e_x] \cong \mathbb{C}$, which is not among the four distinguished subspaces. The involutions of the previous section preserve each of these coordinate conditions, as the sign table shows.

## The Split-Quaternion Norm

The split-quaternion norm of $\tilde q$ is

$$
\langle\tilde q\rangle_{\natural} = \tilde q\tilde{q}^{\natural} = q_t^2 + q_x^2 - q_y^2 - q_z^2,
$$

of **signature $(2,2)$**, with polarisation $\langle\tilde q_1,\tilde q_2\rangle = q_{1t} q_{2t} + q_{1x} q_{2x} - q_{1y} q_{2y} - q_{1z} q_{2z}$ and matrix $G = \operatorname{diag}(1,1,-1,-1)$ in the coordinate basis. It is indefinite and non-degenerate, the scalar and $\vec e_x$ directions being positive and the $\vec e_y, \vec e_z$ directions negative. Under the matrix model it is the determinant, $\langle\tilde q\rangle_{\natural} = \det \mathsf{M}_2(\tilde q)$.

The restrictions to the distinguished subspaces read off the coordinates:

| subspace | restriction of $\langle\cdot\rangle_{\natural}$ | signature |
|---|---|---|
| $S$ | $q_t^2$ | positive definite |
| $V$ | $q_x^2 - q_y^2 - q_z^2$ | $(2,1)$ |
| $\mathbb{D}_2$ | $q_t^2 - q_y^2$ | $(1,1)$ |
| $\mathbb{D}_3$ | $q_t^2 - q_z^2$ | $(1,1)$ |

Only the scalar restriction is definite; the others are indefinite, and their null sets are the zero-divisor sets of the respective subspaces.

## The Unit Criterion in Coordinates

**Theorem.** The four-vector $(q_t,q_x,q_y,q_z)$ is **invertible** if and only if

$$
\langle\tilde q\rangle_{\natural} = q_t^2 + q_x^2 - q_y^2 - q_z^2 \neq 0,
$$

and then $\tilde q^{-1} = \tilde{q}^{\natural}/\langle\tilde q\rangle_{\natural} = \dfrac{q_t e_t - q_x \vec e_x - q_y \vec e_y - q_z \vec e_z}{q_t^2+q_x^2-q_y^2-q_z^2}$. Equivalently, the element is a unit if and only if the determinant of the matrix model is nonzero.

**Proof.** The identity $\tilde q\tilde{q}^{\natural} = \langle\tilde q\rangle_{\natural}$ gives $\tilde q \cdot (\tilde{q}^{\natural}/\langle\tilde q\rangle_{\natural}) = 1$ whenever $\langle\tilde q\rangle_{\natural} \neq 0$; conversely, if $\langle\tilde q\rangle_{\natural} = 0$ with $\tilde q \neq 0$, then $\tilde q\tilde{q}^{\natural} = 0$ with $\tilde{q}^{\natural} \neq 0$, so $\tilde q$ is a zero divisor and cannot be a unit.

The non-invertible nonzero four-vectors are exactly those on the **null cone** $q_t^2 + q_x^2 = q_y^2 + q_z^2$; on the vector subspace $q_t = 0$ this is the null cone $q_x^2 = q_y^2 + q_z^2$ of the Minkowski form, and in the split-complex plane $\mathbb{D}_2$ it is the pair of isotropic lines $q_t = \pm q_y$.

## The Analogue of the Four-Vector Representation of $\mathbb{B}$

The biquaternion article *The Four-Vector Element Representation of Biquaternions* reads $\tilde Q = \sum_\mu Q_\mu e_\mu$ as a quadruple of **complex** coefficients, so that the coefficient space is $\mathbb{C}^4$ of real dimension $8$; two of its remarkable subspaces are read from the real and imaginary parts of the coefficients, and the split-quaternion norm becomes a complex quadratic form with a positive-definite Euclidean companion. The split-quaternion case is the real, split analogue: the coefficient space is $\mathbb{R}^4$ of real dimension $4$, the coefficients are real, all four distinguished subspaces are read directly from coordinate conditions, and the split-quaternion norm is a single real form of signature $(2,2)$ with no complex companion. The structural parallel is exact — a quadruple, a column, a dual row, the component product, the involutions as sign flips, and the split-quaternion norm in coordinates — but every object is real and indefinite here where it is complex in $\mathbb{B}$. Nothing biquaternion-specific — the central imaginary unit $i$, the real-imaginary splitting of the coefficients, the complex definite companion — is imported.

## Summary

The four-vector realization reads a split-quaternion $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ as the quadruple $(q_t,q_x,q_y,q_z) \in \mathbb{R}^4$, an $\mathbb{R}$-linear isomorphism $\mathbb{H}_{\mathrm{s}} \to \mathbb{R}^4$ with no complex structure. The column $X$ is the quadruple written vertically and the row $X^{\mathsf{T}}$ is its dual under the non-degenerate pairing $\langle\cdot,\cdot\rangle_{\natural}$ with matrix $G = \operatorname{diag}(1,1,-1,-1)$.

The product is computed in components by the displayed formula, whose scalar part is $\langle\tilde q_1,\tilde q_2^{\natural}\rangle$ and whose vector part is the antisymmetric remainder. The three involutions act by independent sign flips of $(q_x,q_y,q_z)$: conjugation by $(-,-,-)$, the principal involution by $(-,-,+)$, and the reversal by $(+,+,-)$, with the scalar component always fixed. The distinguished subspaces are the coordinate conditions $q_t$-axis ($S$), $\tilde q^0=0$ ($V$), and the $(q_t,q_y)$-, $(q_t,q_z)$-planes ($\mathbb{D}_2, \mathbb{D}_3$). The split-quaternion norm is $q_t^2 + q_x^2 - q_y^2 - q_z^2$ of signature $(2,2)$, restricting to $q_t^2$, $q_x^2-q_y^2-q_z^2$, $q_t^2-q_y^2$ and $q_t^2-q_z^2$ on the four subspaces, and it gives the unit criterion $N \neq 0$ with $\tilde q^{-1} = \tilde{q}^{\natural}/N$. This is the real, indefinite analogue of the complex four-vector representation of $\mathbb{B}$.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $\tilde q = q_t e_t + q_x \vec e_x + q_y \vec e_y + q_z \vec e_z$ | a general split-quaternion | *Split-Quaternion Algebra* |
| $\tilde q^\mu = (q_t,q_x,q_y,q_z)$ | the four-vector of $\tilde q$ | this article |
| $\tilde q^0 = q_t$, $(\tilde q^1,\tilde q^2,\tilde q^3) = (q_x,q_y,q_z)$ | the scalar and vector components | this article |
| $X$, $X^{\mathsf{T}}$ | the column and the dual row | this article |
| $G = \operatorname{diag}(1,1,-1,-1)$ | the matrix of the polarised form in coordinates | this article |
| $\langle\tilde q\rangle_{\natural} = q_t^2+q_x^2-q_y^2-q_z^2$ | the split-quaternion norm, signature $(2,2)$ | *Split-Quaternion Norm and Invertibility* |
| $\langle\tilde q_1,\tilde q_2\rangle$ | the polarised bilinear form | *Split-Quaternion Norm and Invertibility* |
| ${}^{\natural}, \alpha, \rho$ | the three involutions as sign flips | *Split-Quaternion Subspaces and the Involutions* |
| $S, V, \mathbb{D}_2, \mathbb{D}_3$ | the distinguished subspaces as coordinate conditions | *Split-Quaternion Relations Between Subspaces* |
| $\tilde q^{-1} = \tilde{q}^{\natural}/\langle\tilde q\rangle_{\natural}$ | the inverse of a unit | *Split-Quaternion Norm and Invertibility* |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the coefficient space of a Clifford algebra and the coordinate form of its product.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the coordinate multiplication tables and the matrix generators of the low-dimensional algebras.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the coordinate descriptions of the split forms.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for polarisation, the matrix of a bilinear form, and the inertia law.
