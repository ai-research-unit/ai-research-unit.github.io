# __The Lie Algebra $\operatorname{Skew}_4\cong\mathfrak{so}(4)$__

## Introduction

**The antisymmetric matrices form a Lie algebra of dimension $6$, isomorphic to $\mathfrak{so}(4)$ and to the second exterior power of the space, and at order four it splits into two three-dimensional ideals, each a copy of $\mathfrak{sl}_2$, carried by the self-dual and the anti-self-dual two-forms; the split is the algebra behind the two rotation angles.**

The article proves the closure under the commutator, identifies $\operatorname{Skew}_4$ with $\Lambda^{2}\mathbb{C}^{4}$ through the two-form $x^{\mathsf T}Ky$, constructs the self-dual and anti-self-dual bases explicitly, computes the two ideals and their orthogonality for the Killing form, and reads the two summands as the left and the right multiplications by the three vector units of the biquaternion algebra. It closes with the exponentiation onto $\mathrm{SO}(4,\mathbb{C})$ and with the contrast against the abelian case at order two.

It assumes *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=4$* and *The Symmetric and Antisymmetric Parts of a Product at $n=4$*. The case $n=2$ is *The Lie Algebra $\operatorname{Skew}_2$: One Dimension, Hence Abelian*; the form is *The Killing Form, Its Radical and the Triangular Case*; the biquaternion side is *The Lie Algebra of the Antisymmetric Plain Algebra of the Biquaternions*.

## The Algebra and the Dimension

**Theorem.** $\operatorname{Skew}_4$ is closed under the commutator and has dimension $6$.

**Proof.** For antisymmetric $X,Y$, $(XY-YX)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}-X^{\mathsf T}Y^{\mathsf T}=YX-XY$, so the commutator is antisymmetric. An antisymmetric matrix has zero diagonal and is determined by its six entries above it.

**Corollary.** $\operatorname{Skew}_4=\mathfrak{so}(4)$ is the Lie algebra of the orthogonal group, $\mathfrak{so}(4)=\{X:X+X^{\mathsf T}=0\}$.

**Proof.** The Lie algebra of the group preserving a bilinear form is the set of endomorphisms skew for it; the standard form gives the antisymmetric matrices.

**Proposition.** The trace pairing on $\operatorname{Skew}_4$ is negative definite: for $X,Y$ antisymmetric, $\operatorname{tr}(XY)=-2\sum_{i<j}x_{ij}y_{ij}$.

**Proof.** $\operatorname{tr}(XY)=\sum_{ij}x_{ij}y_{ji}=-\sum_{ij}x_{ij}y_{ij}=-2\sum_{i<j}x_{ij}y_{ij}$ using antisymmetry.

**The units.** The six elements $e_{ij}=E_{ij}-E_{ji}$ for $i<j$ form a basis, with the brackets

$$
[e_{12},e_{13}]=-e_{23},\qquad [e_{12},e_{23}]=e_{13},\qquad [e_{13},e_{23}]=-e_{12},
$$

$$
[e_{12},e_{14}]=-e_{24},\qquad [e_{12},e_{24}]=e_{14},\qquad [e_{14},e_{24}]=-e_{12},
$$

and the four analogous triples $\{1,2,3\}$, $\{1,2,4\}$, $\{1,3,4\}$, $\{2,3,4\}$.

**Proof.** Compute in the matrix units: $[E_{12}-E_{21},E_{13}-E_{31}]=-E_{23}-E_{32}=-e_{23}$ and the other two by the same expansion.

## Two-Forms

**Definition.** For $K\in\operatorname{Skew}_4$ let $\omega_K(x,y)=x^{\mathsf T}Ky$; this is an alternating bilinear form.

**Theorem.** $\omega$ is an isomorphism of $\operatorname{Skew}_4$ onto $\Lambda^{2}(\mathbb{C}^{4})^{\ast}$, and $\Lambda^{2}\mathbb{C}^{4}$ has dimension $6$.

**Proof.** An alternating form is determined by its values on pairs of basis vectors, and the values $\omega_{ij}$ for $i<j$ are the entries of $K$ above the diagonal; the dimension of $\Lambda^{2}$ of a four-dimensional space is $\binom{4}{2}=6$.

**Corollary.** $\operatorname{Skew}_4\cong\Lambda^{2}\mathbb{C}^{4}$ as vector spaces, and the commutator corresponds to a bilinear operation on two-forms.

**Proof.** Both spaces have dimension $6$, and the identification is the displayed one.

**The pairing with two-forms.** $\operatorname{tr}(XY)=-\sum_{i<j}2x_{ij}y_{ij}$ says that the trace pairing is, up to a factor, the standard pairing of two-forms on the coordinate pairs, with a negative sign.

**Proof.** The displayed computation in coordinates.

**The Pfaffian.** For $K\in\operatorname{Skew}_4$ the determinant is a perfect square, $\det K=\operatorname{Pf}(K)^{2}$, with $\operatorname{Pf}(K)=k_{12}k_{34}-k_{13}k_{24}+k_{14}k_{23}$.

**Proof.** Expansion of the determinant of a general antisymmetric $4\times4$ matrix; every term that is not of this shape cancels in pairs.

## The Self-Dual Split

**Definition.** With $e_{ij}=E_{ij}-E_{ji}$, the **self-dual** triple and the **anti-self-dual** triple are

$$
\omega_1=e_{12}+e_{34},\quad \omega_2=e_{13}-e_{24},\quad \omega_3=e_{14}+e_{23},
$$

$$
\tau_1=e_{12}-e_{34},\quad \tau_2=e_{13}+e_{24},\quad \tau_3=e_{14}-e_{23}.
$$

**Theorem.** Each triple spans a three-dimensional Lie subalgebra isomorphic to $\mathfrak{sl}_2$, the two are ideals, they commute with one another, and

$$
\mathfrak{so}(4)=\mathfrak{sl}_2\oplus\mathfrak{sl}_2,\qquad 6=3+3.
$$

**Proof.** The brackets close inside each triple, with opposite signs:

$$
[\omega_1,\omega_2]=-2\omega_3,\quad [\omega_2,\omega_3]=-2\omega_1,\quad [\omega_3,\omega_1]=-2\omega_2,
$$

$$
[\tau_1,\tau_2]=2\tau_3,\quad [\tau_2,\tau_3]=2\tau_1,\quad [\tau_3,\tau_1]=2\tau_2 .
$$

Each is the bracket table of $\mathfrak{sl}_2$, computed by expanding the four terms of each product and using $[e_{12},e_{34}]=0$ for disjoint pairs. A bracket of an $\omega$ with a $\tau$ cancels term by term: the three disjoint pairs $e_{12},e_{34}$; $e_{13},e_{24}$; $e_{14},e_{23}$ commute, so every mixed bracket vanishes. Two commuting ideals summing to the algebra give the direct sum.

**The sign difference.** The two triples obey the same table with opposite overall sign, which is the exact sense in which the self-dual and the anti-self-dual copies of $\mathfrak{sl}_2$ are mirror images: an isomorphism of one onto the other reverses the bracket.

**Corollary.** $\mathfrak{so}(4)$ is semisimple and not simple.

**Proof.** It is a direct sum of two nonzero semisimple algebras, so it is semisimple and has a proper nonzero ideal.

**The Hodge star.** The linear map $\star$ on $\Lambda^{2}$ with $\star e_{12}=e_{34}$, $\star e_{13}=-e_{24}$, $\star e_{14}=e_{23}$ satisfies $\star^{2}=\mathrm{id}$; its eigenspaces are the two triples.

**Proof.** Apply the definition twice to each basis element; the self-dual triple is fixed and the anti-self-dual one is negated, as the signs in the definitions show.

**Corollary.** The decomposition $\Lambda^{2}=\Lambda^{2}_{+}\oplus\Lambda^{2}_{-}$ is the eigenspace split of an involution, hence the split of $\mathfrak{so}(4)$ into two ideals.

**Proof.** An involution of a Lie algebra acts by the sign $+1$ on its fixed set, which is a subalgebra, and by $-1$ on the complement, and the two eigenspaces bracket into the $+1$ eigenspace; here the bracket of the two three-spaces is zero, so each is an ideal.

## The Biquaternion Reading

**The left family.** In the axis-free basis $e_t,e_x,e_y,e_z$ the left multiplications by the three vector units are

$$
L(e_x)=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\quad
L(e_y)=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\quad
L(e_z)=\begin{pmatrix}0&0&0&-1\\0&0&1&0\\0&-1&0&0\\1&0&0&0\end{pmatrix}.
$$

**Theorem.** These three matrices are antisymmetric, they lie in the self-dual triple with the signs $L(e_x)=-\omega_1$, $L(e_y)=-\omega_2$, $L(e_z)=-\omega_3$, and their brackets are $[L(e_x),L(e_y)]=2L(e_z)$ and cyclically.

**Proof.** Each column is the image of a basis element: $L(e_x)$ sends $e_t\mapsto e_x$, $e_x\mapsto-e_t$, $e_y\mapsto e_z$, $e_z\mapsto-e_y$. Reading the columns gives the displayed matrices, which are antisymmetric by inspection; comparing with the definitions gives $L(e_x)=-\omega_1$, $L(e_y)=-\omega_2$, $L(e_z)=-\omega_3$. The bracket identity follows from $L(ab)=L(a)L(b)$ and $e_xe_y-e_ye_x=2e_z$.

**Corollary.** The right multiplications $R(e_x),R(e_y),R(e_z)$ span the anti-self-dual triple, with $R(e_x)=-\tau_1$, $R(e_y)=-\tau_2$, $R(e_z)=-\tau_3$, and their brackets are $[R(e_x),R(e_y)]=-2R(e_z)$.

**Proof.** The same computation with the multiplication on the other side; the reversal of the order turns $e_xe_y=e_z$ into $e_ye_x=-e_z$, which is the sign difference between the two triples.

**What this says.** The two $\mathfrak{sl}_2$ summands of $\mathfrak{so}(4)$ are exactly the two one-sided families of the biquaternion algebra, restricted to the vector units: the left family spans the self-dual forms and the right family the anti-self-dual ones, and the two families commute. The decomposition of $\mathfrak{so}(4)$ into two ideals is therefore the decomposition of the two-sided structure into its left and right halves, read on the six-dimensional space.

**The two angles.** An element $K=K_++K_-$ has a component in each summand, and the two components rotate two independent planes; the two angles of a rotation at order four are the sizes of $K_+$ and $K_-$.

**Proof.** Each summand is a copy of $\mathfrak{so}(3)$, acting on a three-dimensional space of two-forms, and a single element of it has one angular magnitude; the two magnitudes are independent.

## The Form and the Exponentiation

**Proposition.** The Killing form of $\mathfrak{so}(4)$ is $K(X,Y)=8\operatorname{tr}(XY)$, negative definite, and the two summands are orthogonal for it.

**Proof.** On $\mathfrak{gl}_4$ the Killing form is $8\operatorname{tr}(XY)-2\operatorname{tr}X\operatorname{tr}Y$, and $\operatorname{tr}X=0$ on the antisymmetric half. Orthogonality is $\operatorname{tr}(K_+K_-)=0$, the product of a self-dual and an anti-self-dual form having zero trace.

**Corollary.** Each summand carries its own Casimir, and the two Casimirs are the two independent invariants of the algebra.

**Proof.** The Killing form restricted to each ideal is nondegenerate, and a simple algebra has one invariant symmetric form up to scale.

**Theorem.** The exponential maps $\mathfrak{so}(4,\mathbb{C})$ onto $\mathrm{SO}(4,\mathbb{C})$.

**Proof.** Every element of $\mathrm{SO}(4,\mathbb{C})$ is conjugate to a block-diagonal matrix of two rotations by angles $\theta_1,\theta_2$, and a rotation by $\theta$ is the exponential of $\theta e_{12}$; conjugating back exponentiates the conjugate.

**The contrast at order two.** $\mathfrak{so}(2)$ is one-dimensional and abelian, so it has one angle, one Casimir and no ideals; at order four the algebra is six-dimensional, semisimple, with two angles, two Casimirs and two ideals.

**Proof.** At order two there is a single two-form direction and every bracket vanishes; the four statements of richness follow from the split $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$.

## Summary

The antisymmetric matrices form a six-dimensional Lie algebra, isomorphic to $\mathfrak{so}(4)$ and to the space of two-forms on a four-dimensional space, with the trace pairing negative definite on it and the Pfaffian as the square root of the determinant.

At order four the algebra splits into two three-dimensional ideals, each a copy of $\mathfrak{sl}_2$, given by the self-dual and the anti-self-dual two-forms. The two ideals commute, are orthogonal for the Killing form $8\operatorname{tr}(XY)$, and carry the two independent invariants and the two rotation angles.

In the axis-free frame the two ideals are the spans of the left and of the right multiplications by the three vector units of the biquaternion algebra, with explicit matrices, so the self-dual split is the left–right split of the two-sided structure. The exponential covers $\mathrm{SO}(4,\mathbb{C})$, and the contrast with the one-dimensional abelian case at order two is the measure of what the fourth order adds.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e_{ij}=E_{ij}-E_{ji}$ | the six antisymmetric units |
| $\omega_1,\omega_2,\omega_3$ | the self-dual triple |
| $\tau_1,\tau_2,\tau_3$ | the anti-self-dual triple |
| $\star$ | the Hodge star on $\Lambda^{2}$ |
| $\operatorname{Pf}$ | the Pfaffian, $\det K=\operatorname{Pf}(K)^{2}$ |
| $L(e_k)$, $R(e_k)$ | left and right multiplications by the vector units |

## Further Reading

- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for $\Lambda^{2}$ and the exceptional isomorphisms in low dimension.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for $\mathfrak{so}(4)$ and its two ideals.
- [The Killing Form, Its Radical and the Triangular Case](the-killing-form-its-radical-and-the-triangular-case.html), for the form computed here.
- [The Lie Algebra of the Antisymmetric Plain Algebra of the Biquaternions](the-lie-algebra-of-the-antisymmetric-plain-algebra-of-the-biquaternions.html), for the biquaternion side of the same algebra.
- [The Lie Algebra $\operatorname{Skew}_2$: One Dimension, Hence Abelian](the-lie-algebra-skew-2-one-dimension-hence-abelian.html), for the case that this article generalises.
