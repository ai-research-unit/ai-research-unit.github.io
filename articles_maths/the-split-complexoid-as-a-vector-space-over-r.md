# __The Split-Complexoid as a Vector Space over $\mathbb{R}$__

## Introduction

This article treats the split-complex numbers as a **linear space**: the underlying real plane, the split complex structure that multiplication by $j$ puts on it, the separation of the real-linear self-maps into those that commute with that structure and those that anticommute with it, the self-reading of $\mathbb{D}$ as a module over the ring $\mathbb{D}$ rather than over a field of scalars, and the idempotent coordinates in which the plane is a pair of real lines. The map $J$, multiplication by $j$, satisfies $J^2=+\mathrm{id}$: it is a **product structure**, an involution with two real eigenspaces, and not a complex structure, which would satisfy $J^2=-\mathrm{id}$ and have no real eigenvector. This one sign is the whole difference from the complex reading and the source of everything that follows in the category.

The realification of $\mathbb{D}$ as an algebra over $\mathbb{R}$, with the change of scalars organised and the split statements read against the real ones, is *The Realification and the Effect of the Change of Scalars on the Split-Complexoid*, below this article in this category. The two products on the space are *The Two Products of the Split-Complexoid Space*; the distinguished subspaces are *Split-Complexoid Subspaces*, and their decomposition and comparison is *Decompositions and Comparison of the Remarkable Subspaces of the Split-Complexoid*. The submodules of the self-reading are the ideals of the ring, owned by *Split-Complex Ideals and Peirce Decomposition*. No form and no norm is developed here: the norm $\langle Q\rangle_{*}=Q\bar Q=q^2-q'^2$, its multiplicativity and the invertibility it decides are *Split-Complex Norm and Invertibility*, and the two forms are *The Two Forms and the Two Algebraic Norms of the Split-Complexoid Space*, both below this article in this category.

**Conventions.** The algebra is $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$, with basis $1,j$ and $j^2=+1$; a general element is $Q=q+jq'$, with $q=\operatorname{Re}Q$ and $q'=\operatorname{Im}Q$, and the conjugate is $\bar Q=q-jq'$. The idempotents are $\Pi_1=\tfrac12(1+j)$ and $\Pi_2=\tfrac12(1-j)$, with idempotent coordinates $q_+=q+q'$ and $q_-=q-q'$, and $Q=q_+\Pi_1+q_-\Pi_2$.

## The Vector Space over $\mathbb{R}$

**Definition.** The **real reading** of $\mathbb{D}$ is the underlying additive group with the scalar domain $\mathbb{R}$: the split-complex numbers form a real vector space of dimension two, on the basis

$$
1, \quad j, \qquad j^2 = +1 ,
$$

and every element is the unique real combination $Q = q + jq'$. The additive group is the plane $\mathbb{R}^2$ with coordinates $(q,q')$, and the two basis elements are linearly independent over $\mathbb{R}$.

The dimension is two. It is the first of the two readings, and it must be told from the second, the self-reading over $\mathbb{D}$, in which the set is a module of rank one over a ring rather than a vector space over a field: read over $\mathbb{R}$ the scalars are the reals and the dimension is two, read over $\mathbb{D}$ the scalars are the split-complex numbers and the rank is one.

| scalars | structure | size | basis |
|---|---|---|---|
| $\mathbb{R}$ | vector space, scalars a field | dimension $2$ | $1,\ j$ |
| $\mathbb{D}$ | module, scalars a ring with zero divisors | rank $1$ | $1$ |

Both readings are of the same set, and the second is the stronger structure: every real scalar is a split-complex one, and a submodule of the self-reading is in particular a real subspace.

## The Split Complex Structure

Multiplication by $j$ is a real-linear map of the plane,

$$
J : \mathbb{D} \longrightarrow \mathbb{D}, \qquad J(Q) = jQ ,
$$

whose values on the basis are $J(1)=j$ and $J(j)=j^2=1$, so that its matrix in the basis $\{1,j\}$ is

$$
J = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad J^2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \mathrm{id} .
$$

**Proposition.** The map $J$ is an involution, $J^2=+\mathrm{id}$, of trace $0$ and determinant $-1$; it is diagonalisable over $\mathbb{R}$, with eigenvalues $+1$ and $-1$ and eigenvectors $\Pi_1$ and $\Pi_2$.

**Proof.** $J^2(Q)=j(jQ)=j^2Q=Q$ since $j^2=+1$, so $J^2=\mathrm{id}$. The diagonal entries of the matrix sum to $0$ and its determinant is $-1$. The vectors $\Pi_1=\tfrac12(1+j)$ and $\Pi_2=\tfrac12(1-j)$ satisfy $j\Pi_1=\Pi_1$ and $j\Pi_2=-\Pi_2$, so in the basis $\{\Pi_1,\Pi_2\}$ the matrix of $J$ is $\operatorname{diag}(1,-1)$.

So $J$ is a **product structure**: a linear involution with two real eigenspaces, the real line $\mathbb{R}_{\mathbb{D}}$ and the split imaginary line $j\mathbb{R}_{\mathbb{D}}$. On $\mathbb{C}$ the corresponding map is the multiplication by the imaginary unit, $J_\mathbb{C}(z)=iz$, with

$$
J_\mathbb{C}^2 = -\mathrm{id},
$$

a **complex structure**: it has no real eigenvalue, no real eigenvector, and its two eigenvalues $+i$ and $-i$ are exchanged by conjugation. The two maps differ by one sign, and that sign is the whole difference of the two readings:

| | $\mathbb{C}$ | $\mathbb{D}$ |
|---|---|---|
| generator | $i$, $i^2=-1$ | $j$, $j^2=+1$ |
| structure $J$ | complex structure | product structure |
| $J^2$ | $-\mathrm{id}$ | $+\mathrm{id}$ |
| real eigenvalues | none | $+1,-1$ |
| invariant lines | none over $\mathbb{R}$ | $\mathbb{R}_{\mathbb{D}}$, $j\mathbb{R}_{\mathbb{D}}$ |

**Remark (the contrast with complexification).** The complex field is obtained from $\mathbb{R}$ by adjoining a root of $x^2+1$, which is irreducible over $\mathbb{R}$, and the result is again a field. Adjoining instead a root of $x^2-1$ gives $\mathbb{D}$, and $x^2-1=(x-1)(x+1)$ already splits over $\mathbb{R}$: the new element $j$ is not a new kind of number but a reflection with $j^2=+1$, and the algebra it generates is $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$, not a field. Consistently, extending the scalars of $\mathbb{D}$ to $\mathbb{C}$ gives $\mathbb{C}\otimes_\mathbb{R}\mathbb{D}\cong\mathbb{C}\times\mathbb{C}$, a product of two fields and not a field, whereas extending $\mathbb{C}$ itself gives $\mathbb{C}\otimes_\mathbb{R}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ as well. There is no complexification of $\mathbb{D}$ that stays a field; the split algebra carries its own scalar extension, and it is developed in *The Realification and the Effect of the Change of Scalars on the Split-Complexoid*, below this article in this category.

## Linear and Antilinear Maps

The two readings of the plane are separated by one operator, and the separation is a commutation condition.

**Proposition (linearity is the commutator with $J$).** A real-linear map $T$ of $\mathbb{D}$ is $\mathbb{D}$-linear exactly when it commutes with $J$, and conjugate-linear over $\mathbb{D}$ exactly when it anticommutes with it:

$$
T(Q_1Q_2) = Q_1\,T(Q_2) \text{ for all } Q_1,Q_2 \iff TJ = JT, \qquad T(Q_1Q_2) = \bar Q_1\,T(Q_2) \text{ for all } Q_1,Q_2 \iff TJ = -JT .
$$

**Proof.** Let $T$ be real-linear. Then $T(JQ_2)=T(jQ_2)$ and $J(TQ_2)=jT(Q_2)$, so the identity $T(jQ_2)=jT(Q_2)$ is exactly $TJ=JT$; real-linearity then gives $T(Q_1Q_2)=T(q_1Q_2+jq'_1Q_2)=q_1T(Q_2)+j q'_1T(Q_2)=Q_1\,T(Q_2)$ for every $Q_1=q_1+jq'_1$, and conversely $TJ=JT$ gives $T(jQ_2)=jT(Q_2)$, hence the same identity for every $Q_1$. The conjugate-linear case is the same computation with the sign reversed: $T(jQ_2)=-jT(Q_2)$, and then $T(Q_1Q_2)=q_1T(Q_2)-jq'_1T(Q_2)=\bar Q_1\,T(Q_2)$.

**The two block shapes.** Writing a real-linear map in the basis as a matrix $T=\begin{pmatrix} p & u \\ r & s \end{pmatrix}$, the two conditions are read off the two products

$$
TJ = \begin{pmatrix} u & p \\ s & r \end{pmatrix}, \qquad JT = \begin{pmatrix} r & s \\ p & u \end{pmatrix},
$$

and equality or opposite equality fixes the entries:

| class | condition | matrix shape | trace | meaning |
|---|---|---|---|---|
| $\mathbb{D}$-linear | $TJ = JT$ | $\begin{pmatrix} p & u \\ u & p \end{pmatrix}$ | $2p$ | multiplication by $p+ju$ |
| conjugate-linear | $TJ = -JT$ | $\begin{pmatrix} p & u \\ -u & -p \end{pmatrix}$ | $0$ | composition of the conjugation with a $\mathbb{D}$-linear map |

The commuting shape is symmetric with equal diagonal entries, and it is exactly the image of multiplication by the element $p+ju$, the regular matrix of *Split-Complex Regular Element Representation*; the two classes are the $\mathbb{D}$-linear and the conjugate-linear maps of the plane.

**Remark.** Composing the conjugation $\kappa(Q)=\bar Q$, whose matrix is $\operatorname{diag}(1,-1)$, with a $\mathbb{D}$-linear map on either side gives a conjugate-linear map, and every conjugate-linear map arises so: $\kappa$ anticommutes with $J$, so $\kappa T$ and $T\kappa$ anticommute with $J$ when $T$ commutes with it. The real-linear self-maps form $\operatorname{End}_\mathbb{R}(\mathbb{D})\cong M_2(\mathbb{R})$, of real dimension four, and the $\mathbb{D}$-linear ones form the two-dimensional subspace $M_2(\mathbb{D})=\{qI+q'J\}$, the image of $\mathbb{D}$.

## The Self-Interpretation over $\mathbb{D}$

Read over the ring $\mathbb{D}$ itself, the set is a **free module of rank one** on the single basis element $1$: every element is $Q\cdot 1$ for a unique $Q\in\mathbb{D}$, and the module is $\mathbb{D}$ acting on itself. This is the second reading of the table above, and it is not a vector space, because the scalars form a ring and not a field.

The difference is concrete. A vector space over a field has every nonzero element invertible as a scalar, so every nonzero vector generates; here the scalars include the zero divisors, so a nonzero element of the module need not generate it. Exactly as in the ring, the element $\Pi_1$ is a nonzero scalar that annihilates $\Pi_2$, and $\Pi_1\cdot\mathbb{D}=\mathbb{R}\Pi_1$ is a proper nonzero submodule. The submodules of the rank-one module are the ideals of the ring,

$$
0, \quad \mathbb{R}\Pi_1, \quad \mathbb{R}\Pi_2, \quad \mathbb{D},
$$

the two idempotent lines and the two trivial submodules; each idempotent line is closed under multiplication by every scalar, and it is minimal. This is the two-dimensional case of the ideal theory owned by *Split-Complex Ideals and Peirce Decomposition*, and the submodules are the same two lines as the subspaces of *Split-Complexoid Subspaces*: the module theory and the subspace theory meet at the idempotent lines.

**Remark.** The module is free of rank one, so it has a basis, but the basis element is not interchangeable with every nonzero element: an element $Q\cdot 1$ is again a basis exactly when $Q$ is a unit, by the invertibility criterion $\langle Q\rangle_{*}\neq 0$ of *Split-Complex Norm and Invertibility*. A zero divisor such as $\Pi_1$ spans only its own line. This is the sense in which the self-reading is a module and not a vector space: the failure is the same failure of division that makes the ring not a field.

## The Idempotent Coordinates

The idempotent basis diagonalises the structure $J$ and splits the plane into two real lines. With

$$
\Pi_1 = \tfrac12(1+j), \quad \Pi_2 = \tfrac12(1-j), \qquad \Pi_1^2=\Pi_1, \quad \Pi_2^2=\Pi_2, \quad \Pi_1\Pi_2=0, \quad \Pi_1+\Pi_2=1,
$$

every element is written $Q=q_+\Pi_1+q_-\Pi_2$ with $q_+=q+q'$ and $q_-=q-q'$, and the change of coordinates from the basis $\{1,j\}$ is the invertible real map

$$
q_+ = q+q', \qquad q_- = q-q', \qquad q = \tfrac12(q_++q_-), \qquad q' = \tfrac12(q_+-q_-).
$$

So the plane is a **pair of real lines**,

$$
\mathbb{D} = \mathbb{R}\Pi_1 \oplus \mathbb{R}\Pi_2,
$$

and in these coordinates the structure is diagonal, $J(q_+\Pi_1+q_-\Pi_2)=q_+\Pi_1-q_-\Pi_2$, hence $J=\operatorname{diag}(1,-1)$. The two coordinate lines are exactly its two eigenspaces, and the coordinates in which they separate are the reason $J$ is a product structure and not a complex structure. The same coordinates carry the multiplication, which is componentwise, and they are developed as a representation in *Split-Complex Two-Component Element Representation*.

## Summary

The split-complex numbers form a real vector space of dimension two on the basis $1,j$, and they also form a free module of rank one over the ring $\mathbb{D}$ itself. Multiplication by $j$ is the real-linear map $J$ of matrix $\begin{pmatrix}0&1\\1&0\end{pmatrix}$, an involution with $J^2=+\mathrm{id}$, diagonalisable over $\mathbb{R}$ with eigenvalues $+1$ and $-1$; it is a **product structure**, against the complex structure $J_\mathbb{C}^2=-\mathrm{id}$ of the complex field, and the difference is the sign of the square of the generator. The algebra is the split analogue of $\mathbb{C}$: adjoining a root of the split polynomial $x^2-1$ gives a product of two copies of $\mathbb{R}$ and not a field, and its scalar extension to $\mathbb{C}$ is likewise not a field.

A real-linear map of the plane is $\mathbb{D}$-linear exactly when it commutes with $J$, and conjugate-linear exactly when it anticommutes. The commuting maps have the block shape $\begin{pmatrix}p&u\\u&p\end{pmatrix}$ and are the multiplications by an element of $\mathbb{D}$; the anticommuting ones have the shape $\begin{pmatrix}p&u\\-u&-p\end{pmatrix}$, are of trace zero, and are the compositions of the conjugation with a $\mathbb{D}$-linear map. Read over the ring, the module of rank one has for submodules the two idempotent lines and the two trivial ones, and it fails to be a vector space for the same reason the ring fails to be a field, the presence of zero divisors. In the idempotent coordinates $Q=q_+\Pi_1+q_-\Pi_2$ the plane is the direct sum of the two real lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$, and $J=\operatorname{diag}(1,-1)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$ | the split-complex algebra, $j^2=+1$ |
| $Q=q+jq'$ | general element, $q=\operatorname{Re}Q$, $q'=\operatorname{Im}Q$ |
| $\bar Q=q-jq'$ | the conjugation |
| $J(Q)=jQ$ | the real-linear product structure, $J^2=+\mathrm{id}$, matrix $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ |
| $TJ=JT$ / $TJ=-JT$ | $\mathbb{D}$-linearity / conjugate-linearity of a real-linear $T$ |
| $\begin{pmatrix}p&u\\u&p\end{pmatrix}$, $\begin{pmatrix}p&u\\-u&-p\end{pmatrix}$ | the two block shapes of the two classes |
| $\kappa(Q)=\bar Q$ | the conjugation as a real-linear map, matrix $\operatorname{diag}(1,-1)$ |
| $M_2(\mathbb{D})=\{qI+q'J\}$ | the $\mathbb{D}$-linear maps, image of the regular representation |
| $\Pi_1=\tfrac12(1+j)$, $\Pi_2=\tfrac12(1-j)$ | the idempotents, eigenvectors of $J$ |
| $q_+=q+q'$, $q_-=q-q'$ | idempotent coordinates, $Q=q_+\Pi_1+q_-\Pi_2$ |
| $\mathbb{R}\Pi_1,\mathbb{R}\Pi_2$ | the two coordinate lines, the submodules of the self-reading |

## Further Reading

- Israel Nathan Herstein, *Topics in Algebra* (Wiley, 2nd ed. 1975), for vector spaces, modules over a ring, and the distinction the zero divisor draws between them.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for free modules of finite rank, submodules and the failure of the field condition.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split-complex algebra as the even Clifford algebra $\mathrm{Cl}_{1,0}$ and its product structure.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the two invariant lines of the split-complex plane and the idempotent coordinates.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the regular representation and the identification of an algebra of endomorphisms with a matrix algebra.
