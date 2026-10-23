
# __Split-Biquaternion Four-Vector Element Representation__

## Introduction

A split biquaternion is an element $\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z$ with four **split complex** coefficients $Q_\mu \in \mathbb{D}$, and this article reads the algebra through those four coefficients: the coefficient space, the column and dual row presentations, the multiplication in components, the four conjugations as coordinate operations, the four distinguished subspaces as coefficient conditions, and the split-biquaternion norm with its two real restrictions. The construction is the split complex analogue of the four-vector representation of the biquaternions; the coefficient arithmetic is that of *Split-Complex Algebra*, and the algebra structure is that of *Split-Biquaternion Algebra*.

The treatment is purely mathematical. No physics is invoked, and no metric is imposed on the coefficient space; the four coefficients are an algebraic device, and the form they carry is the split complex norm.

## The Coefficient Space

**Definition.** The **coefficient space** of $\mathbb{H}_{\mathbb{D}}$ is the free module $\mathbb{D}^4$ of quadruples $(Q_t, Q_x, Q_y, Q_z)$ of split complex numbers, with the corresponding isomorphism

$$
\mathbb{H}_{\mathbb{D}} \longrightarrow \mathbb{D}^4 , \qquad \tilde{Q} = \sum_{\mu\in\{t,x,y,z\}} Q_\mu e_\mu \longmapsto (Q_t, Q_x, Q_y, Q_z) .
$$

Each coefficient splits as $Q_\mu = q_\mu + j q'_\mu$ with real $q_\mu, q'_\mu$, so $\mathbb{D}^4$ is the real vector space $\mathbb{R}^8$ and the **eight real coordinates** of the algebra are $(q_t,q_x,q_y,q_z,q'_t,q'_x,q'_y,q'_z)$.

### Real and Split-Imaginary Parts of the Components

Writing each coefficient through the idempotents $\tilde\Pi_{1,2} = \tfrac{1}{2}(1 \pm j)$ gives $Q_\mu = Q_{\mu +} \tilde\Pi_1 + Q_{\mu -} \tilde\Pi_2$ with

$$
Q_{\mu +} = q_\mu + q'_\mu , \qquad Q_{\mu -} = q_\mu - q'_\mu ,
$$

so the coefficient space is also the sum of two real four-dimensional spaces, the **real part** $q'_\mu = 0$ and the **split-imaginary part** $q_\mu = 0$. The passage from $(q_\mu, q'_\mu)$ to $(Q_{\mu+}, Q_{\mu-})$ is the diagonalisation of the split complex structure.

## The Column and the Row

A split biquaternion is written either as a **column** of its coefficients,

$$
\tilde{Q} = \begin{pmatrix} Q_t \\ Q_x \\ Q_y \\ Q_z \end{pmatrix} ,
$$

or as the **dual row** $\tilde{Q}^{\mathsf{T}}$ of quaternion conjugation, obtained by transposing the column of conjugates; the pairing of a row and a column is the scalar part of the product. Because $\mathbb{D}$ is commutative, no distinction between left and right coefficients arises in the column description, and the linear maps of the algebra are the $4 \times 4$ matrices over $\mathbb{D}$, the split complex analogue of the $M_4(\mathbb{D})$ representation.

## Multiplication in Four-Vector Form

**Proposition.** In components, the product $\tilde Q_3 = \tilde Q_1\tilde Q_2$ is given by

$$
\boxed{\;Q_{3t} = Q_{1t}Q_{2t} - Q_{1x}Q_{2x} - Q_{1y}Q_{2y} - Q_{1z}Q_{2z} , \qquad Q_{3x} = Q_{1t}Q_{2x} + Q_{1x}Q_{2t} + Q_{1y}Q_{2z} - Q_{1z}Q_{2y}\;}
$$

$$
\boxed{\;Q_{3y} = Q_{1t}Q_{2y} - Q_{1x}Q_{2z} + Q_{1y}Q_{2t} + Q_{1z}Q_{2x} , \qquad Q_{3z} = Q_{1t}Q_{2z} + Q_{1x}Q_{2y} - Q_{1y}Q_{2x} + Q_{1z}Q_{2t}\;}
$$

the structure constants being those of the quaternion basis and the coefficients multiplying in the commutative algebra $\mathbb{D}$.

**Proof.** These are the standard quaternion multiplication formulas with the coefficients taken in $\mathbb{D}$; the multiplication is well defined because $\mathbb{D}$ is commutative and central.

### The Multiplication Table of the Basis

The basis elements multiply as in the quaternion case,

| | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

so that the four-vector multiplication is the quaternion multiplication generalised by the ring $\mathbb{D}$ of scalars. The four-vector form is thus the standard model of the algebra, and every algebraic operation below is the coordinate reading of an operation of the algebra.

## The Conjugations in Coordinates

On the column $(Q_t,Q_x,Q_y,Q_z)$ the four conjugations act by:

| conjugation | $Q_t$ | $Q_x$ | $Q_y$ | $Q_z$ |
|---|---|---|---|---|
| ${}^{\natural}$ | $Q_t$ | $-Q_x$ | $-Q_y$ | $-Q_z$ |
| $\bar{\cdot}$ | $\bar{Q_t}$ | $\bar{Q_x}$ | $\bar{Q_y}$ | $\bar{Q_z}$ |
| ${}^{*}$ | $\bar{Q_t}$ | $-\bar{Q_x}$ | $-\bar{Q_y}$ | $-\bar{Q_z}$ |
| $\flat$ | $-\bar{Q_t}$ | $\bar{Q_x}$ | $\bar{Q_y}$ | $\bar{Q_z}$ |

That is, quaternion conjugation negates the three vector components and fixes the scalar one; split complex conjugation conjugates every coefficient; Hermitian conjugation is their composite; and anti-Hermitian conjugation is minus the Hermitian conjugate. The patterns in the four real coordinates $q_\mu$ and $q'_\mu$ are the sign patterns tabulated in *Split-Biquaternion Involution Lattice*.

## The Four Distinguished Subspaces

The four distinguished subspaces appear as coefficient conditions:

| subspace | condition on coefficients | real coordinates |
|---|---|---|
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $Q_x = Q_y = Q_z = 0$ | $q_x,q_y,q_z,q'_x,q'_y,q'_z = 0$ |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $Q_\mu \in \mathbb{R}$ for all $\mu$ | $q'_\mu = 0$ for all $\mu$ |
| $\mathbb{M}_+$ | $Q_t \in \mathbb{R}$, $Q_k \in j\mathbb{R}$ | $q'_t = 0$, $q_k = 0$ for $k = 1,2,3$ |
| $\mathbb{M}_-$ | $Q_t \in j\mathbb{R}$, $Q_k \in \mathbb{R}$ | $q_t = 0$, $q'_k = 0$ for $k = 1,2,3$ |

The centre is the set of elements whose vector components vanish; the quaternion subspace is the real part of the coefficient space; the Hermitian subspace has real scalar component and split-imaginary vector components; the anti-Hermitian subspace has split-imaginary scalar component and real vector components. The four coordinate blocks of *Split-Biquaternion Relations Between Subspaces* are the coordinate sets selected by these conditions.

## The Split-Biquaternion Norm

**Proposition.** In the four-vector description the split-biquaternion norm is

$$
\boxed{\;
\langle\tilde{Q}\rangle_{\natural} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 = \left(\sum_{\mu} (q_\mu^2 + q'^2_\mu)\right) + 2j\left(\sum_\mu q_\mu q'_\mu\right)
\;},
$$

with real part the square of the Euclidean norm and split-imaginary part twice the inner product of the real and split-imaginary coordinate vectors.

**Proof.** Expand each $Q_\mu^2 = (q_\mu + j q'_\mu)^2 = q_\mu^2 + q'^2_\mu + 2j q_\mu q'_\mu$ and sum over $\mu$.

The real part of the split-biquaternion norm is **positive definite**: it vanishes only when all eight coordinates vanish, that is only for $\tilde{Q} = 0$. The split-biquaternion norm is therefore **anisotropic** as a quadratic map to $\mathbb{D}$ — there is no nonzero element of norm zero — even though the algebra has many zero divisors, whose split-biquaternion norms are nonzero zero divisors of $\mathbb{D}$.

### The Two Real Restrictions

On the two real parts of the coefficient space the split-biquaternion norm is a genuine positive definite quadratic form:

- on the **real part** $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, where $q'_\mu = 0$, it is $N = \sum_\mu q_\mu^2$;
- on the **split-imaginary part** $j\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, where $q_\mu = 0$, it is $N = \sum_\mu q'^2_\mu$.

Both are positive definite; the indefinite form of the algebra is the Hermitian norm $\langle\tilde Q\rangle_{*} = \sum_\mu (q_\mu^2 - q'^2_\mu)$ of signature $(4,4)$, as in *Split-Biquaternion Norm and Invertibility*.

### The Unit Criterion in Coordinates

**Theorem.** A split biquaternion $\tilde{Q}$ is a unit if and only if $\langle\tilde{Q}\rangle_{\natural}$ is a unit of $\mathbb{D}$, that is, if and only if

$$
\boxed{\;
\sum_\mu (q_\mu + q'_\mu)^2 \neq 0 \quad \text{and} \quad \sum_\mu (q_\mu - q'_\mu)^2 \neq 0
\;}.
$$

**Proof.** Under the Peirce decomposition $\langle\tilde{Q}\rangle_{\natural} = N_+ \tilde\Pi_1 + N_- \tilde\Pi_2$ with $N_\pm = \sum_\mu (q_\mu \pm q'_\mu)^2$, the number $\langle\tilde{Q}\rangle_{\natural}$ is a unit of $\mathbb{D} \cong \mathbb{R} \oplus \mathbb{R}$ exactly when both components are nonzero; since each is a sum of squares of reals, this means each is strictly positive.

The criterion shows directly that the **zero divisors** are the elements whose split-biquaternion norm vanishes in exactly one of the two idempotent components, that is the elements with $\sum_\mu (q_\mu+q'_\mu)^2 = 0$ or $\sum_\mu (q_\mu-q'_\mu)^2 = 0$, which are the two four-dimensional subspaces $Z_\pm$ of *Split-Biquaternion Zero Divisors*. In the four-vector picture the zero divisors are thus the coefficient quadruples lying in one of the two real four-dimensional subspaces defined by $\sum_\mu(q_\mu\pm q'_\mu)^2 = 0$.

## Summary

The four-vector representation reads a split biquaternion as a column $(Q_t,Q_x,Q_y,Q_z)$ of four split complex coefficients, with the dual row given by quaternion conjugation and the eight real coordinates $(q_\mu,q'_\mu)$ splitting into a real and a split-imaginary part. The product is the quaternion product in components, with the coefficients multiplying in the commutative algebra $\mathbb{D}$, and the basis table is the quaternion table. The four conjugations act by the sign patterns $Q_t \mapsto \pm Q_t$ or $\pm \bar{Q_t}$, negating the vector components for quaternion conjugation, conjugating all coefficients for split complex conjugation, and combining the two for Hermitian and anti-Hermitian conjugation. The four distinguished subspaces are given by coefficient conditions: vanishing vector coefficients for the centre, real coefficients for the quaternion subspace, real scalar and split-imaginary vector components for $\mathbb{M}_+$, and the reverse for $\mathbb{M}_-$. The split-biquaternion norm is $N = \sum_\mu Q_\mu^2$, with positive definite real part $\sum_\mu(q_\mu^2+q'^2_\mu)$ and split-imaginary part $2\sum_\mu q_\mu q'_\mu$, and it is anisotropic: it vanishes only at the origin, so the zero divisors are exactly the elements whose split-biquaternion norm is a nonzero zero divisor of $\mathbb{D}$, described in coordinates by $\sum_\mu(q_\mu \pm q'_\mu)^2 = 0$ in one idempotent component. The construction is the split complex analogue of the biquaternion four-vector representation, with $\mathbb{D}$ in place of $\mathbb{C}$ and the complexified quadratic form replaced by the split complex norm.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ | Split biquaternion |
| $Q_\mu = q_\mu + j q'_\mu \in \mathbb{D}$ | Split complex coefficient |
| $(Q_t,Q_x,Q_y,Q_z)$ | Column of coefficients; $\mathbb{D}^4 \cong \mathbb{R}^8$ |
| $(q_t,q_x,q_y,q_z,q'_t,q'_x,q'_y,q'_z)$ | The eight real coordinates |
| $Q_{\mu\pm} = q_\mu \pm q'_\mu$ | Idempotent components of a coefficient |
| $P_\mu = (Q_1Q_2)_\mu$ | Components of the product, quaternion structure constants |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ | The four conjugations on the column |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}, \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}, \mathbb{M}_+, \mathbb{M}_-$ | Distinguished subspaces as coefficient conditions |
| $\langle\tilde{Q}\rangle_{\natural} = \sum_\mu Q_\mu^2$ | Split-Biquaternion norm, anisotropic |
| $\langle\tilde Q\rangle_{*} = \sum_\mu(q_\mu^2 - q'^2_\mu)$ | Hermitian norm, signature $(4,4)$ |
| $Z_\pm$ | The two four-dimensional zero divisor subspaces |

## Further Reading

- I. L. Kantor and A. S. Solodovnikov, *Hypercomplex Numbers: An Elementary Introduction to Algebras* (Springer, 1989), for the coefficient description of a hypercomplex algebra and its norm.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997), for the four-component representation of the split biquaternion algebra.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for norms of composition algebras and the coordinate description of their zero divisors.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the componentwise reading of the quaternion product and its conjugations.
