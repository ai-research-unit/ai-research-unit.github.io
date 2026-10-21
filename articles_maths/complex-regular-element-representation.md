
# __Complex Regular Element Representation__

## Introduction

The complex algebra $\mathbb{C}$ is two-dimensional over $\mathbb{R}$ and one-dimensional over itself. This article presents its **regular representation**, the algebra acting on itself on the left, and the $2 \times 2$ real matrix of that action in the basis $1$, $i$. The matrix is the Cayley matrix of complex multiplication, and its image is the algebra of conformal $2 \times 2$ real matrices, the matrices of the shape $qI + q'J$. The article is the base case of the regular-representation articles of the corpus.

The conventions are those of *Complex Algebra*: basis $1$, $i$ with $i^2 = -1$, a general element $Q = q + i q'$, norm $N(Q) = Q\bar Q = q^2+q'^2$, and complex conjugation $\bar Q$. The word *representation* is used in both senses: the concrete realization of the algebra by matrices, and the technical action of the algebra on a vector space. The article owns the left matrix, its multiplicativity, the identification with the conformal matrices, the determinant and the trace; the complex-linear one-dimensional representation and the classification of the modules over a field are the subject of *Complex Element Representations* and are cited once.

## The Left Regular Representation

**Definition.** The **left regular representation** of $\mathbb{C}$ is the map

$$
L : \mathbb{C} \longrightarrow \operatorname{End}_{\mathbb{R}}(\mathbb{C}), \qquad L_{Q}(Q_1) = Q Q_1 .
$$

For each $Q$, the map $Q_1 \mapsto QQ_1$ is $\mathbb{R}$-linear because multiplication is bilinear, so $L_{Q}$ is an $\mathbb{R}$-linear endomorphism of the two-dimensional real space $\mathbb{C}$. Writing each endomorphism as a matrix in the basis $1, i$, the same symbol $\mathsf{M}_2(Q)$ denotes the matrix acting on the column $(q_1, q'_1)^{\mathsf{T}}$ of $Q_1 = q_1 + i q'_1$.

**Proposition (the regular matrix is the Cayley matrix).** In the basis $1, i$,

$$
\mathsf{M}_2(Q) = \begin{pmatrix} q & -q' \\ q' & q \end{pmatrix} = q I + q' J, \qquad J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad J^2 = -I .
$$

**Proof.** The columns are the images $L_{Q}(e_m) = Q e_m$ expressed in the basis. For $m = 0$, $Q\cdot 1 = Q = q + i q'$, giving the first column $(q, q')^{\mathsf{T}}$. For $m = 1$, $Q i = (q+i q') i = q i + i^2 q' = -q' + i q$, giving the second column $(-q', q)^{\mathsf{T}}$. The basis element $i$ therefore acts by $J$, and $J^2 = -I$ is the matrix form of $i^2 = -1$.

The matrix has only two independent entries, the two real coordinates of $Q$; it is the **Cayley matrix** of complex multiplication. The identity matrix is $\mathsf{M}_2(1)$, and multiplication by $i$ is $\mathsf{M}_2(i) = J$, the **complex structure** of the plane.

**Example.** For $Q = 3+4i$ the Cayley matrix is

$$
\mathsf{M}_2(Q) = \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}, \qquad \mathsf{M}_2(Q)\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \end{pmatrix},
$$

so the column of $1$ is the column of $Q$ itself. For the pair $Q = 3+4i$ and $Q_1 = 1-2i$ the two matrices are

$$
\mathsf{M}_2(Q) = \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}, \qquad \mathsf{M}_2(Q_1) = \begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix}.
$$

**Multiplicativity.** The matrix product is

$$
\mathsf{M}_2(Q)\mathsf{M}_2(Q_1) = \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix}
= \begin{pmatrix} 3+8 & 6-4 \\ 4-6 & 8+3 \end{pmatrix} = \begin{pmatrix} 11 & 2 \\ -2 & 11 \end{pmatrix} = \mathsf{M}_2(QQ_1),
$$

the matrix of the product $QQ_1 = 11-2i$; the reversed order gives $\mathsf{M}_2(Q_1)\mathsf{M}_2(Q) = \mathsf{M}_2(QQ_1)$ as well, the concrete form of commutativity.

**Determinant and trace.** $\det \mathsf{M}_2(Q) = 3\cdot 3 - (-4)\cdot 4 = 25 = N(Q)$ and $\operatorname{tr}\mathsf{M}_2(Q) = 6 = 2\operatorname{Re} Q$; likewise $\det \mathsf{M}_2(Q_1) = 1\cdot 1 - 2\cdot(-2) = 5 = N(Q_1)$ and $\operatorname{tr}\mathsf{M}_2(Q_1) = 2 = 2\operatorname{Re} Q_1$.

**The unit factor.** $\mathsf{M}_2(u) = \tfrac15 \mathsf{M}_2(Q) = \begin{pmatrix} 0.6 & -0.8 \\ 0.8 & 0.6 \end{pmatrix}$ has determinant $0.36+0.64 = 1$ and lies in $SO(2)$, the rotation through $\theta = \arctan(4/3)$; the factorisation $\mathsf{M}_2(Q) = 5\,\mathsf{M}_2(u)$ is the polar decomposition of the conformal matrix $\mathsf{M}_2(Q)$ into a scalar and a rotation.

**Transposition.** $\mathsf{M}_2(Q)^{\mathsf{T}} = \begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix} = \mathsf{M}_2(\bar Q)$, since $\bar Q = 3-4i$; more generally $\mathsf{M}_2(Q)^{\mathsf{T}} = \mathsf{M}_2(\bar Q)$, the matrix form of the involution.

## The Left Representation Is a Homomorphism

**Theorem (multiplicativity).** For all $Q, Q_1 \in \mathbb{C}$,

$$
\mathsf{M}_2(Q)\,\mathsf{M}_2(Q_1) = \mathsf{M}_2(QQ_1).
$$

Hence $\mathsf{M}_2$ is an $\mathbb{R}$-algebra homomorphism and the space $\mathbb{C}$ is a left $\mathbb{C}$-module under it. It is **faithful**: if $\mathsf{M}_2(Q) = 0$ then $Q = L_{Q}(1) = 0$.

**Proof.** Both sides are $\mathbb{R}$-linear in the second factor and are computed on the basis. For every $m$, associativity gives

$$
L_{Q}\bigl(L_{Q_1}(e_m)\bigr) = Q(Q_1 e_m) = (QQ_1) e_m = L_{QQ_1}(e_m),
$$

so the two matrices agree on a basis.

**Example (a concrete check).** For $Q = 3+4i$ and $Q_1 = 1-2i$ the product is $QQ_1 = 11-2i$, and

$$
\mathsf{M}_2(Q)\mathsf{M}_2(Q_1) = \begin{pmatrix} 3 & -4 \\ 4 & 3 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix} = \begin{pmatrix} 11 & 2 \\ -2 & 11 \end{pmatrix} = \mathsf{M}_2(QQ_1),
$$

the reversed order giving the same matrix, as the algebra is commutative.

## The Right Regular Representation and Commutativity

**Definition.** The **right regular representation** of $\mathbb{C}$ is the map

$$
R : \mathbb{C} \longrightarrow \operatorname{End}_{\mathbb{R}}(\mathbb{C}), \qquad R_{Q}(Q_1) = Q_1 Q .
$$

**Proposition.** $\mathsf{M}_2^{R} = \mathsf{M}_2$.

**Proof.** The algebra is commutative, so $Q_1 Q = Q Q_1$ for all $Q_1$, hence the two endomorphisms agree on every element.

The right regular representation therefore carries no information beyond the left one, and it is not a second realization. The left and right regular representations coincide, and there is no anti-homomorphism to compare with the transpose. The slot is empty because the algebra is commutative, and the emptiness is the statement.

## Transposition and Conjugation

**Proposition.** For every complex number $Q$,

$$
\mathsf{M}_2(Q)^{\mathsf{T}} = \mathsf{M}_2(\bar Q),
$$

where the transpose is taken in the basis $1, i$.

**Proof.** Transposing $\mathsf{M}_2(Q) = \begin{pmatrix} q & -q' \\ q' & q \end{pmatrix}$ gives $\begin{pmatrix} q & q' \\ -q' & q \end{pmatrix}$, which is $\mathsf{M}_2(q - i q') = \mathsf{M}_2(\bar Q)$.

Transposition is therefore complex conjugation in the matrix picture: it is the matrix form of the involution, and the antisymmetric matrix $\mathsf{M}_2(Q) - \mathsf{M}_2(\bar Q)$ changes sign under it. The same theorem holds here with the single involution of the field.

## The Module Structure: Irreducibility

The regular representation is the algebra acting on itself, and over $\mathbb{C}$ the module $\mathbb{C}$ is one-dimensional. Since $\mathbb{C}$ is a field, its only submodules are $\{0\}$ and $\mathbb{C}$ itself:

**Proposition.** The regular module is **simple** (irreducible), and the regular representation has no proper nonzero invariant subspace.

**Proof.** A submodule is a left ideal of the field $\mathbb{C}$, and a field has no proper nonzero ideals. Equivalently, $\mathsf{M}_2(Q_1)$ spans the whole module for every nonzero $Q_1$.

The algebra is a field, its regular module is simple, and there is no Peirce decomposition, no idempotent splitting and no centralizer larger than the image itself. The endomorphism algebra of the regular module is $\operatorname{End}_{\mathbb{C}}(\mathbb{C}) = \mathbb{C}$, the image of $\mathsf{M}_2$.

## The Determinant and the Trace

**Proposition.** For $Q = q+i q'$,

$$
\det \mathsf{M}_2(Q) = q^2 + q'^2 = N(Q), \qquad \operatorname{tr}\mathsf{M}_2(Q) = 2q = 2 \operatorname{Re} Q .
$$

**Proof.** $\det \mathsf{M}_2(Q) = q\cdot q - (-q')\cdot q' = q^2 + q'^2$, and $\operatorname{tr}\mathsf{M}_2(Q) = q + q = 2q$.

The determinant is the norm, and the trace is twice the real part, which is also the algebra trace $\operatorname{Tr}(Q)$ of $\mathbb{C}$ over $\mathbb{R}$. The regular module is one-dimensional over $\mathbb{C}$ and the determinant is the norm itself. The determinant also shows that $\mathsf{M}_2(Q)$ is invertible exactly when $Q \neq 0$, matching the invertibility criterion of *Complex Norm and Invertibility*.

**Corollary.** $\mathsf{M}_2(Q)$ is orientation-preserving for $Q \neq 0$, since $\det \mathsf{M}_2(Q) = N(Q) > 0$.

## The Images of the Distinguished Subspaces

The two distinguished subspaces $\mathbb{R}_{\mathbb{C}}$ and $i\mathbb{R}_{\mathbb{C}}$ of the algebra have the following images under $\mathsf{M}_2$:

| subspace | image | matrix characterization |
|---|---|---|
| $\mathbb{R}_{\mathbb{C}}$ | scalar matrices | $\mathsf{M}_2(q) = q I$, $q \in \mathbb{R}$ |
| $i\mathbb{R}_{\mathbb{C}}$ | traceless skew-symmetric matrices | $\mathsf{M}_2(i q') = q' J$, $q' \in \mathbb{R}$, $\mathsf{M}_2(iq')^{\mathsf{T}} = -\mathsf{M}_2(iq')$ |

The real subspace is the line of scalar matrices, a copy of $\mathbb{R}$ inside $M_2(\mathbb{R})$; the imaginary subspace is the line of skew-symmetric matrices, and $J^2 = -I$ is the matrix form of $i^2 = -1$. The image of $\mathbb{R}_{\mathbb{C}}$ is closed under matrix multiplication; the image of $i\mathbb{R}_{\mathbb{C}}$ is not, since the product of the two multiples $(q'J)(cJ) = -q'c\,I$ of $J$ is a scalar matrix, mirroring $(iq')(ic) = -q'c$ in the algebra. Under the transpose the two lines are distinguished: $\mathsf{M}_2(Q)^{\mathsf{T}} = \mathsf{M}_2(\bar Q)$ negates the imaginary subspace and fixes the real one.

## The Identification with the Conformal Matrices

The image of the regular representation is the algebra

$$
M_2(\mathbb{C}) = \left\{ \begin{pmatrix} q & -q' \\ q' & q \end{pmatrix} : q, q' \in \mathbb{R} \right\} = \{ qI + q'J : q, q' \in \mathbb{R} \},
$$

the set of real matrices of the shape $qI + q'J$.

**Proposition.** The matrices of the shape $qI + q'J$ are exactly the real $2 \times 2$ matrices commuting with $J$, equivalently the $\mathbb{R}$-linear maps $\mathbb{R}^2 \to \mathbb{R}^2$ that are complex-linear under the identification $\mathbb{R}^2 \cong \mathbb{C}$. They form a field isomorphic to $\mathbb{C}$ under $\mathsf{M}_2$, and the nonzero ones are the **conformal** or **similarity** matrices of the plane: each is the composition of a scaling by $r = \sqrt{N(Q)} > 0$ and a rotation by $\theta = \arg Q$.

**Proof.** A matrix $M = \begin{pmatrix} p & n \\ s & t \end{pmatrix}$ commutes with $J$ exactly when $s = -n$ and $p = t$, which is the shape $qI+q'J$; this is the condition that it be the real matrix of a $\mathbb{C}$-linear map. The map $\mathsf{M}_2$ is an injective algebra homomorphism by multiplicativity and faithfulness, and its image is therefore a field isomorphic to $\mathbb{C}$. In the polar form $Q = r\exp(i\theta)$ with $r>0$, the matrix factors as

$$
\mathsf{M}_2(Q) = r \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix},
$$

a positive scalar times an element of $SO(2)$; that is, a similarity of ratio $r$ and angle $\theta$.

The image $M_2(\mathbb{C})$ is the field of conformal matrices, and its group of nonzero elements is the group of orientation-preserving similarities of the plane fixing the origin; it is isomorphic to $\mathbb{C}^\times \cong \mathbb{R}_{>0} \times SO(2)$. The determinant is the square of the ratio and the trace is twice the real part of the complex number, so the polar decomposition $Q = ru$ is the polar decomposition of the conformal matrix into a scalar and a rotation, as developed in *Modulus–Unit Polar Decomposition of Complex Numbers* and *Rotations and Reflections in the Complex Plane*.

## The Image of the Unit Circle

**Proposition.** The image of the unit circle under $\mathsf{M}_2$ is the rotation group of the plane. For $u = \exp(i\theta) \in \mathrm{U}(1)$,

$$
\mathsf{M}_2(u) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} = R_\theta, \qquad \det R_\theta = \cos^2\theta + \sin^2\theta = 1, \qquad \operatorname{tr} R_\theta = 2\cos\theta,
$$

and $R_\theta$ is orthogonal, $R_\theta^{\mathsf{T}}R_\theta = I$, with determinant $+1$. The map $u \mapsto \mathsf{M}_2(u)$ is an isomorphism of Lie groups $\mathrm{U}(1) \to SO(2)$.

**Proof.** Substituting $Q = \exp(i\theta)$ into $\mathsf{M}_2(Q) = qI+q'J$ with $q = \cos\theta$, $q' = \sin\theta$ gives the display, and orthogonality with determinant $+1$ is immediate from it. The map is a homomorphism by multiplicativity, $\mathsf{M}_2(uv) = \mathsf{M}_2(u)\mathsf{M}_2(v)$, it is injective by faithfulness, and it is surjective because every element of $SO(2)$ is such a matrix for exactly one $\theta \in \mathbb{R}/2\pi\mathbb{Z}$.

The rotation matrix is therefore the matrix form of multiplication by a unit, and the product rule $R_\theta R_\varphi = R_{\theta+\varphi}$ is multiplicativity read on the circle. Because $\mathsf{M}_2(i) = J$, the regular representation carries the exponential of the algebra to the exponential of matrices,

$$
\exp(\theta J) = \sum_{n \ge 0} \frac{\theta^n J^n}{n!} = \cos\theta\, I + \sin\theta\, J = R_\theta,
$$

so the skew-symmetric matrices $\theta J$ form the one-dimensional abelian Lie algebra $\mathrm{SO}(2) \cong \mathbb{R}$ and $\exp : \mathrm{SO}(2) \to SO(2)$ is surjective with kernel $2\pi\mathbb{Z}$. The determinant of a rotation is $N(u) = 1$ and its trace is $2\operatorname{Re} u$, the specialisation of the determinant and trace formulas to the unit circle.

The reflections are the other coset. Since $\mathsf{M}_2(Q)^{\mathsf{T}} = \mathsf{M}_2(\bar Q)$, the transpose realises the involution, and the matrix of the reflection $S_u(Q) = u\bar Q$ in the basis $\{1, i\}$ is the product $\mathsf{M}_2(u)E$ with $E = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ the matrix of complex conjugation; with $u = \exp(2i\alpha)$ it is

$$
\mathsf{M}_2(u) E = \begin{pmatrix} \cos 2\alpha & \sin 2\alpha \\ \sin 2\alpha & -\cos 2\alpha \end{pmatrix},
$$

of determinant $-1$, trace $0$ and eigenvalues $+1$ and $-1$, on the fixed line and the perpendicular line of the reflection. The reflection matrices therefore exhaust the nontrivial coset $\mathsf{M}_2(\mathrm{U}(1))E$ of $SO(2)$ in $O(2) = \mathsf{M}_2(\mathrm{U}(1)) \cup \mathsf{M}_2(\mathrm{U}(1))E$.

## Summary

The left regular representation of $\mathbb{C}$, defined by $L_{Q}(Q_1) = QQ_1$, is the algebra acting on itself on the left, and in the basis $1, i$ its matrix is the Cayley matrix

$$
\mathsf{M}_2(Q) = \begin{pmatrix} q & -q' \\ q' & q \end{pmatrix} = qI + q'J, \qquad J^2 = -I .
$$

It is a faithful $\mathbb{R}$-algebra homomorphism, $\mathsf{M}_2(Q)\mathsf{M}_2(Q_1) = \mathsf{M}_2(QQ_1)$; its transpose is the matrix of the conjugate, $\mathsf{M}_2(Q)^{\mathsf{T}} = \mathsf{M}_2(\bar Q)$; its determinant is the norm and its trace is twice the real part. The image is the field of conformal $2 \times 2$ real matrices, the nonzero elements of which are the orientation-preserving similarities of the plane, and the polar decomposition of $Q$ is the decomposition of its matrix into a scalar and a rotation. On the distinguished subspaces the image is the line of scalar matrices for $\mathbb{R}_{\mathbb{C}}$ and the line of skew-symmetric matrices for $i\mathbb{R}_{\mathbb{C}}$, and on the unit circle it is the rotation group: $\mathsf{M}_2$ carries $\mathrm{U}(1)$ isomorphically onto $SO(2)$, $u = \exp(i\theta)$ to the rotation matrix $R_\theta$, and the reflections $S_u(Q) = u\bar Q$ to the coset $\mathsf{M}_2(\mathrm{U}(1))E$ of $SO(2)$ in $O(2)$.

Because the algebra is commutative, the right regular representation coincides with the left and the left-right distinction is empty. Because the algebra is a field, the regular module is simple: there is no reduction into two minimal left ideals, no squared determinant and no nontrivial centralizer, and their absence is the commutativity and the divisibility of $\mathbb{C}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}$ | the complex algebra, basis $1$, $i$, $i^2 = -1$ |
| $Q = q + i q'$ | a complex number |
| $L_{Q}(Q_1) = QQ_1$ | the left regular representation |
| $R_{Q}(Q_1) = Q_1Q$ | the right regular representation, equal to $\mathsf{M}_2$ |
| $\mathsf{M}_2(Q) = qI + q'J$ | the Cayley matrix of $Q$ |
| $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ | the complex structure, $J^2 = -I$ |
| $N(Q) = q^2+q'^2$ | the norm, $\det \mathsf{M}_2(Q) = N(Q)$ |
| $\operatorname{tr}\mathsf{M}_2(Q) = 2\operatorname{Re}Q$ | the trace of the regular matrix |
| $M_2(\mathbb{C})$ | the image, the field of conformal matrices $\cong \mathbb{C}$ |
| $\mathbb{R}_{\mathbb{C}}, i\mathbb{R}_{\mathbb{C}}$ | the distinguished subspaces, imaged as the scalar and the skew-symmetric matrices |
| $\mathrm{U}(1) = \{u : \lvert u\rvert = 1\}$ | the unit circle, imaged as the rotation group |
| $R_\theta = \mathsf{M}_2(\exp(i\theta))$ | the rotation matrix, the image of a unit |
| $E = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ | the matrix of complex conjugation; the reflections are $\mathsf{M}_2(\mathrm{U}(1))E$ |
| $SO(2)$ | the rotation factor of the conformal group |
| $S_u(Q) = u\bar Q$, $u \in \mathrm{U}(1)$ | a reflection of the plane, matrix $\mathsf{M}_2(u)E$ |
| $O(2) = \mathsf{M}_2(\mathrm{U}(1)) \cup \mathsf{M}_2(\mathrm{U}(1))E$ | the orthogonal group, rotations and reflections |
| $\mathrm{SO}(2) \cong \mathbb{R}$ | the skew-symmetric matrices $\theta J$, the Lie algebra of $SO(2)$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the regular representation of an algebra and its endomorphism algebra.
- Charles B. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Interscience, 1962), for the regular module and its decomposition into minimal left ideals.
- Frank B. Anderson and Kent R. Fuller, *Rings and Categories of Modules*, 2nd edition (Springer, 1992), for the regular module over a field and the simplicity of the regular representation of a division ring.
- Tristan Needham, *Visual Complex Analysis* (Oxford University Press, 1997), for the conformal-matrix reading of multiplication by a complex number.
