# __The Antisymmetric Sector, the Pfaffian and the Klein Quadric of $M_4(\mathbb{C})$__

## Introduction

The antisymmetric matrices of order four form a six-dimensional subspace $\Lambda^{2}\mathbb{C}^{4}$ of $M_4(\mathbb{C})$, closed under the commutator and isomorphic to the Lie algebra $\mathfrak{so}(4,\mathbb{C})$. On this sector the determinant has a square root: the **Pfaffian**

$$
\mathrm{Pf}(A)=a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23},
$$

a quadratic form in the entries with $\mathrm{Pf}(A)^{2}=\det A$. The vanishing of the Pfaffian is the condition for the corresponding two-form to be decomposable, and the six coordinates $p_{ij}$ of a decomposable two-form are the **Plücker coordinates** of a line in $\mathbb{P}^{3}$. The Pfaffian quadric in $\mathbb{P}^{5}$ is therefore the Grassmannian of lines in $\mathbb{P}^{3}$, the **Klein quadric**, a smooth quadric of dimension four with two rulings.

This article states the identification, the Pfaffian and its invariance, the rank criterion, the Hodge star and the self-dual splitting, the Klein quadric and the Plücker relation, and the two rulings. The determinant and the singular set of the full algebra are *The Forms, the Norms and the Singular Set of $M_4(\mathbb{C})$*; the two chiral $\mathfrak{su}_2$'s of the frame are *The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$*, and the relation between them and the splitting below is stated, not reproved.

## The Antisymmetric Sector

**Definition.** Let $\Lambda^{2}\mathbb{C}^{4}$ be the space of antisymmetric bilinear forms on $\mathbb{C}^{4}$, identified with the matrices $A$ with $A^{\mathsf T}=-A$.

**Proposition.** The space $\Lambda^{2}\mathbb{C}^{4}$ has dimension $6$, with basis $e_{i}\wedge e_{j}$ for $1\le i<j\le4$, and the matrix of $A=\sum_{i<j}a_{ij}e_{i}\wedge e_{j}$ has entries $A_{ij}=a_{ij}$ and $A_{ji}=-a_{ij}$.

**Proof.** An antisymmetric matrix is determined by its entries above the diagonal, of which there are $\binom{4}{2}=6$; the matrices $e_{i}\wedge e_{j}=E_{ij}-E_{ji}$ are linearly independent and span the space.

**The Lie algebra.** The commutator of two antisymmetric matrices is antisymmetric:

$$
[A,B]^{\mathsf T}=(AB-BA)^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}-A^{\mathsf T}B^{\mathsf T}=BA-AB=-[A,B].
$$

So $\Lambda^{2}\mathbb{C}^{4}$ is a Lie subalgebra of $\mathfrak{gl}_4(\mathbb{C})$, isomorphic to $\mathfrak{so}(4,\mathbb{C})$, of dimension $6$.

**The exponentials.** For antisymmetric $A$ the exponential $\exp A$ is orthogonal, $\exp(A)^{\mathsf T}\exp(A)=I$: the series commutes with transposition and $A^{\mathsf T}=-A$ gives $\exp(A)^{\mathsf T}=\exp(-A)=\exp(A)^{-1}$. The image is the identity component $SO(4,\mathbb{C})$.

## The Pfaffian

**Definition.** For an antisymmetric $A$ the **Pfaffian** is

$$
\mathrm{Pf}(A)=a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}.
$$

**Theorem.** $\mathrm{Pf}(A)^{2}=\det A$.

**Proof.** Expand $\det A$ by the Leibniz formula and collect the terms. Of the $24$ permutations, the twelve that pair the indices $\{1,2\}$ with $\{3,4\}$ contribute $a_{12}a_{34}$, those that pair $\{1,3\}$ with $\{2,4\}$ contribute $-a_{13}a_{24}$, and those that pair $\{1,4\}$ with $\{2,3\}$ contribute $a_{14}a_{23}$; each group enters with the same sign pattern in the two squares, and the cross terms cancel by antisymmetry. Equivalently, the identity is the case $n=2$ of the general Pfaffian expansion, and it is checked directly on the basis: $\mathrm{Pf}(e_{1}\wedge e_{2}+e_{3}\wedge e_{4})=1$ and $\det=1$.

**The invariance.** For $U\in GL_4(\mathbb{C})$,

$$
\mathrm{Pf}(UAU^{\mathsf T})=\det(U)\,\mathrm{Pf}(A).
$$

**Proof.** Both sides are quadratic in $A$ and multiplicative in $U$; the identity is checked on the basis, where $U(e_{i}\wedge e_{j})U^{\mathsf T}=(Ue_{i})\wedge(Ue_{j})$ and the Pfaffian of a decomposable form $u\wedge v$ is the determinant of the $2\times2$ matrix of coordinates of $u$ and $v$ in a completion to a basis, which scales by $\det U$. For $U\in SO(4)$ the Pfaffian is invariant; for $U$ with $\det U=-1$ it changes sign.

**The rank criterion.** An antisymmetric matrix has even rank. For $A\in\Lambda^{2}\mathbb{C}^{4}$,

$$
\operatorname{rank}A=0\iff A=0,\qquad
\operatorname{rank}A=2\iff \mathrm{Pf}(A)=0,\ A\ne0,\qquad
\operatorname{rank}A=4\iff \mathrm{Pf}(A)\ne0.
$$

**Proof.** The rank is even because the matrix is skew for the symmetric form, and the only even ranks in dimension four are $0,2,4$. If the rank is four, the matrix is invertible and $\det A\ne0$, so $\mathrm{Pf}(A)\ne0$. If the rank is two, the kernel has dimension two; choosing a basis adapted to the kernel, the matrix has the form $u\wedge v$ in the remaining two dimensions, of rank two and Pfaffian zero. If the rank is zero the matrix vanishes. The converses follow from the same normal form.

**The normal form.** Every nonzero antisymmetric matrix of rank two is $A=u\wedge v$ for two independent vectors $u,v$; every antisymmetric matrix of rank four is congruent to $e_{1}\wedge e_{2}+e_{3}\wedge e_{4}$, with Pfaffian $1$.

## The Hodge Star and the Self-Dual Splitting

**Definition.** With the standard symmetric form on $\mathbb{C}^{4}$, the **Hodge star** on $\Lambda^{2}$ is the linear map defined on the basis by

$$
*(e_{1}\wedge e_{2})=e_{3}\wedge e_{4},\qquad
*(e_{1}\wedge e_{3})=-e_{2}\wedge e_{4},\qquad
*(e_{1}\wedge e_{4})=e_{2}\wedge e_{3},
$$

and extended antisymmetrically.

**Proposition.** $*^{2}=I$, and $*$ is symmetric for the form $\langle\omega,\eta\rangle$ defined by $\omega\wedge\eta=\langle\omega,*\eta\rangle\,e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}$.

**Proof.** The three displayed values give $*^{2}=1$ on a basis, and the symmetry is the identity $\omega\wedge\eta=\eta\wedge\omega$ together with $*^{2}=1$.

**The splitting.** The eigenvalues of $*$ are $+1$ and $-1$, and the eigenspaces

$$
\Lambda^{2}_{+}=\{\omega:*\omega=\omega\},\qquad
\Lambda^{2}_{-}=\{\omega:*\omega=-\omega\}
$$

have dimension $3$ each. A basis of $\Lambda^{2}_{+}$ is

$$
e_{1}\wedge e_{2}+e_{3}\wedge e_{4},\qquad
e_{1}\wedge e_{3}-e_{2}\wedge e_{4},\qquad
e_{1}\wedge e_{4}+e_{2}\wedge e_{3},
$$

and a basis of $\Lambda^{2}_{-}$ is obtained by changing the signs of the second terms.

**The Lie algebra.** The splitting is a splitting of Lie algebras:

$$
\mathfrak{so}(4,\mathbb{C})=\Lambda^{2}_{+}\oplus\Lambda^{2}_{-}\cong\mathfrak{sl}_2(\mathbb{C})\oplus\mathfrak{sl}_2(\mathbb{C}).
$$

**Proof.** The star commutes with the bracket, because it is an isometry of the form and the bracket is built from the metric; hence the two eigenspaces are Lie subalgebras. Each is three-dimensional, and the only three-dimensional simple complex Lie algebra is $\mathfrak{sl}_2$. The two summands commute, since $[\Lambda^{2}_{+},\Lambda^{2}_{-}]\subseteq\Lambda^{2}_{+}\cap\Lambda^{2}_{-}=0$.

**The Pfaffian on the two halves.** For $\omega\in\Lambda^{2}_{+}$,

$$
\omega\wedge\omega=\langle\omega,*\omega\rangle\,e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4}=\langle\omega,\omega\rangle\,e_{1}\wedge e_{2}\wedge e_{3}\wedge e_{4},
$$

and the form $\langle\cdot,\cdot\rangle$ is nondegenerate on the three-dimensional space. The restriction of the Pfaffian quadric to $\mathbb{P}(\Lambda^{2}_{+})$ is therefore a smooth conic, and the same holds on $\mathbb{P}(\Lambda^{2}_{-})$. The two conics are the **chiral conics** of the antisymmetric sector.

## The Klein Quadric

**The Plücker coordinates.** A decomposable two-form $\omega=u\wedge v$ has coordinates

$$
p_{ij}=u_{i}v_{j}-u_{j}v_{i},\qquad 1\le i<j\le4,
$$

the **Plücker coordinates** of the line $\mathbb{P}(\langle u,v\rangle)\subset\mathbb{P}^{3}$. They satisfy the **Plücker relation**

$$
p_{12}p_{34}-p_{13}p_{24}+p_{14}p_{23}=0,
$$

which is exactly the vanishing of the Pfaffian.

**Theorem (the Klein quadric).** The image of the map

$$
\operatorname{Gr}(2,4)\longrightarrow\mathbb{P}(\Lambda^{2}\mathbb{C}^{4})=\mathbb{P}^{5},\qquad
\langle u,v\rangle\longmapsto[u\wedge v],
$$

is the quadric $Q=\{\mathrm{Pf}=0\}$. The map is an isomorphism onto $Q$, and $Q$ is a smooth quadric of dimension $4$.

**Proof.** The map is well defined: a change of basis of $\langle u,v\rangle$ multiplies $u\wedge v$ by the determinant, so the class in $\mathbb{P}^{5}$ is unchanged. It is injective: the line is recovered as the projectivisation of the span of the vectors whose wedge with $\omega$ vanishes, a two-dimensional subspace for a nonzero decomposable $\omega$. Its image lies in $Q$ by the Plücker relation. Conversely, every nonzero $\omega$ with $\mathrm{Pf}(\omega)=0$ has rank two by the rank criterion, hence is decomposable, $\omega=u\wedge v$, and lies in the image. The quadric $Q$ is defined by a nondegenerate quadratic form in six variables, so it is smooth, and its dimension is $5-1=4$. The Grassmannian $\operatorname{Gr}(2,4)$ has dimension $2(4-2)=4$, consistent with the isomorphism.

**The cone.** The affine cone over $Q$ is the set of decomposable two-forms, including zero; it is the determinantal variety of rank-two antisymmetric matrices, of dimension $5$.

**The two rulings.** Through every point of $Q$ pass two planes contained in $Q$:

- the plane of the lines through a fixed point $P\in\mathbb{P}^{3}$;
- the plane of the lines contained in a fixed plane $H\subset\mathbb{P}^{3}$.

Each family is parametrised by a $\mathbb{P}^{3}$, the dual $\mathbb{P}^{3}$ for the second, and the two families are the **rulings** of $Q$. Two points of $Q$ lie on a common line of $Q$ exactly when the corresponding lines of $\mathbb{P}^{3}$ meet.

**Proof.** The lines through a fixed point $P$ form a $\mathbb{P}^{2}$ in $\mathbb{P}^{3}$, and their Plücker points satisfy the two linear equations $P\wedge\omega=0$, which define a plane in $\mathbb{P}^{5}$; that plane lies in $Q$ because every form in it is decomposable. The same argument applies to the lines in a fixed plane, with the dual equations. The two planes through a point of $Q$ are obtained by taking $P$ on the line and $H$ containing the line. The incidence statement is the Klein correspondence: two lines meet exactly when the corresponding two-forms have a common vector, which is the condition that their Plücker points are joined by a line lying in $Q$.

## The Place of the Sector in $M_4(\mathbb{C})$

**The trace form.** On the antisymmetric sector the trace form is nondegenerate, and in the basis $e_{i}\wedge e_{j}$ it is diagonal:

$$
\operatorname{tr}\bigl((e_{i}\wedge e_{j})(e_{k}\wedge e_{l})\bigr)=-2\,\delta_{ik}\delta_{jl},
$$

so $\operatorname{tr}(A^{2})=-2\sum_{i<j}a_{ij}^{2}$ for $A=\sum a_{ij}e_{i}\wedge e_{j}$. The Killing form of $\mathfrak{so}(4,\mathbb{C})$ is a multiple of this form. On the real sector the trace form is negative definite, which is the compactness of $\mathfrak{so}(4,\mathbb{R})$.

**The determinant.** The determinant of an antisymmetric matrix is the square of its Pfaffian, so on the sector the determinant is a perfect square. The singular set of the sector is the Pfaffian quadric, of dimension $4$ in $\mathbb{P}^{5}$, and not a hypersurface of the same type as the singular set $\{\det=0\}$ of the full algebra.

**The chiral reading.** The two three-dimensional halves $\Lambda^{2}_{\pm}$ are the two chiral pieces of the rotation algebra, and each is an $\mathfrak{sl}_2$. The frame of the algebra carries another pair of $\mathfrak{su}_2$'s, the Peirce chain and the chiral pair of *The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$*; the two pairs are different subalgebras. The star splitting is attached to the metric and the antisymmetric sector, the Peirce splitting to the idempotents and the frame.

**The rank and the idempotents.** An antisymmetric matrix is never an idempotent except zero, and its rank is even; the rank stratification of the sector is $0$, $2$ and $4$, against the five spectral strata of the full algebra. The two stratifications meet at the zero matrix only.

## Summary

The antisymmetric sector $\Lambda^{2}\mathbb{C}^{4}$ is six-dimensional, is the Lie algebra $\mathfrak{so}(4,\mathbb{C})$, and carries the Pfaffian, a quadratic form whose square is the determinant. The Pfaffian vanishes exactly on the forms of rank at most two and is nonzero exactly on the invertible ones; its invariance under congruence is the invariance of the determinant up to the square of $\det U$. The Hodge star splits the sector into the self-dual and anti-self-dual three-spaces, and the Lie algebra into $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$; the Pfaffian restricts to a smooth conic on each chiral plane. In $\mathbb{P}^{5}$ the Pfaffian quadric is the Klein quadric, isomorphic to the Grassmannian of lines in $\mathbb{P}^{3}$, with two rulings by planes. The sector is the even-rank part of the algebra, and its determinant is a square.

| Quantity | Value |
|---|---|
| $\dim\Lambda^{2}\mathbb{C}^{4}$ | $6$ |
| $\dim\Lambda^{2}_{\pm}$ | $3$ |
| Rank of an antisymmetric matrix | $0,2,4$ |
| $\mathrm{Pf}(e_{1}\wedge e_{2}+e_{3}\wedge e_{4})$ | $1$ |
| $\dim\operatorname{Gr}(2,4)=Q$ | $4$ |
| Ambient projective space | $\mathbb{P}^{5}$ |
| Rulings | two, each parametrised by $\mathbb{P}^{3}$ |
| Chiral conics | two smooth conics |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda^{2}\mathbb{C}^{4}$ | the space of antisymmetric matrices, identified with two-forms |
| $e_{i}\wedge e_{j}$ | the basis matrix $E_{ij}-E_{ji}$ |
| $\mathrm{Pf}(A)$ | the Pfaffian $a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}$ |
| $*$ | the Hodge star on $\Lambda^{2}$ |
| $\Lambda^{2}_{\pm}$ | the self-dual and anti-self-dual eigenspaces of $*$ |
| $p_{ij}$ | the Plücker coordinates of a decomposable two-form |
| $Q=\{\mathrm{Pf}=0\}$ | the Klein quadric in $\mathbb{P}^{5}$ |
| $\operatorname{Gr}(2,4)$ | the Grassmannian of two-planes in $\mathbb{C}^{4}$ |

## Further Reading

- [The Forms, the Norms and the Singular Set of $M_4(\mathbb{C})$](the-forms-the-norms-and-the-singular-set-of-m4c.html), for the determinant and the singular set of the full algebra.
- [The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$](the-peirce-su2-and-the-chiral-su2-su2-of-m4c.html), for the other pair of chiral subalgebras.
- [The Geometry of the Idempotents of $M_4(\mathbb{C})$](the-geometry-of-the-idempotents-of-m4c.html), for the Grassmannians and the flag variety.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_4(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m4c.html), for the Grassmannians $\operatorname{Gr}(1,4)$ and $\operatorname{Gr}(2,4)$.
- [The Determinant and Alternating Forms](the-determinant-and-alternating-forms.html), for the determinant and the exterior algebra.
- Werner Greub, *Multilinear Algebra* (Springer, 1978), for the Pfaffian and the Hodge star.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Klein quadric and the Grassmannians.
