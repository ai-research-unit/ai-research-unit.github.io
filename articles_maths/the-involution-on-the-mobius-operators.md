
# __The Involution on the Möbius Operators__

## Introduction

The **Möbius operators** are the fractional linear transformations $z \mapsto (az+b)/(cz+d)$ of the Riemann sphere, realised by the matrices of $PGL_2(\mathbb{C})$ up to the scalars, and they carry a distinguished **involution**: the complex conjugation $z \mapsto \bar z$, an anti-holomorphic involution of the sphere that acts on the operators by the conjugation of the matrix, $M \mapsto \bar M$. The operators fixed by the involution are the **real Möbius transformations**, the group $PSL_2(\mathbb{R})$, which is also the adjoint-unitary group of the Hermitian form of signature $(1,1)$ and the isometry group of the hyperbolic plane. The article develops the involution in the **operator built from the involution** layer of this Part: the Möbius operator is the one of *The Möbius Transformation as an Operator*, the involution is the complex conjugation, the adjoint is the one of *The Adjoint under a Hermitian Pairing*, and the article proves the agreement of the fixed group with the projective unitary group rather than assuming it.

The article develops the Möbius operators and the conjugation of the sphere, the action of the conjugation on the group and the fixed subgroup, the real Möbius transformations as the isometries of the hyperbolic plane, the unitary realisation of the real group by the Hermitian form of signature $(1,1)$, and the classification of the real forms of $PSL_2(\mathbb{C})$ as the split and the compact one. The article owns the involution and the real forms of the Möbius group.

The article assumes *The Möbius Transformation as an Operator* for the fractional linear maps, the matrix realisation, the cross ratio and the action on the hyperbolic space; *The Adjoint under a Hermitian Pairing* for the adjoint and the self-adjoint elements; *Real Structures on a Projective Space* for the real structures and the real points; *Unitary Geometry over a Field with Involution* for the Hermitian forms of signature $(1,1)$; and *Hyperbolic Geometry* and *Möbius and Lie Sphere Geometry* for the hyperbolic plane and its isometries. The real forms of a complex Lie group are *Real Forms of a Complex Lie Group and the Cartan Involution* of Part III. No distance beyond the hyperbolic metric and no physics is invoked.

## The Möbius Operators and the Conjugation

### The Operators

**Definition.** The **Möbius operators** are the maps of the Riemann sphere

$$
M_A(z) = \frac{az + b}{cz + d}, \qquad A = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in GL_2(\mathbb{C}) ,
$$

extended to the sphere by $M_A(\infty) = a/c$ and $M_A(-d/c) = \infty$; two matrices give the same map exactly when they differ by a scalar, so the Möbius group is the projective group $PGL_2(\mathbb{C}) = PSL_2(\mathbb{C})$, and it is the group of all the bijections of the sphere preserving the cross ratio. The Möbius operators are the operators of *The Möbius Transformation as an Operator*, and they act on the upper half-plane as the isometries of the hyperbolic plane.

**Proposition.** The Möbius operators form a group under the composition, $M_A \circ M_B = M_{AB}$, the inverse is $M_{A^{-1}}$, and the group acts triply transitively on the sphere; the cross ratio $[z_1:z_2:z_3:z_4]$ is invariant, the circle group of the sphere is preserved, and the classification of the operators by the trace of the matrix is that of the elliptic, parabolic and hyperbolic elements.

**Proof.** The composition of two fractional linear maps is the fractional linear map of the product, computed directly; the triple transitivity is the matching of the three images and the fundamental theorem of the projective line; the invariance of the cross ratio and the classification by the trace are in *The Möbius Transformation as an Operator*. The statement is the standard theory of the Möbius group.

### The Complex Conjugation

**Definition.** The **complex conjugation** is the map of the Riemann sphere

$$
\iota : \hat{\mathbb{C}} \to \hat{\mathbb{C}}, \qquad \iota(z) = \bar{z}, \qquad \iota(\infty) = \infty ;
$$

it is an **anti-Möbius** map (anti-holomorphic, orientation-reversing) and an involution, and its fixed locus is the real projective line

$$
\hat{\mathbb{C}}^{\iota} = \mathbb{P}^1(\mathbb{R}) = \mathbb{R} \cup \{\infty\} .
$$

**Proposition.** The conjugation is an involution of the sphere reversing the orientation and the cross ratio, $\iota[z_1:z_2:z_3:z_4] = [\bar z_1:\bar z_2:\bar z_3:\bar z_4] = \overline{[z_1:z_2:z_3:z_4]}$; a Möbius operator commutes with the conjugation exactly when it is real, and the cross ratio of four points is real exactly when the four points lie on a circle or a line of the sphere.

**Proof.** The conjugation is additive and reverses the product, hence an involution of the field extended to the sphere; the cross ratio is a rational function with real coefficients under the conjugation, so it is replaced by its complex conjugate; a Möbius operator commutes with the conjugation exactly when its coefficients may be taken real, and the reality of the cross ratio is the classical criterion for the concyclicity. The statement is in *The Möbius Transformation as an Operator* and *Projective Geometry*.

## The Involution on the Group

### The Conjugation of the Operators

**Definition.** The **involution on the Möbius operators** is the map induced by the conjugation of the sphere,

$$
\sigma : PGL_2(\mathbb{C}) \longrightarrow PGL_2(\mathbb{C}), \qquad \sigma(M) = \iota \circ M \circ \iota ,
$$

which on the matrix is the entrywise complex conjugation,

$$
\sigma(M_A) = M_{\bar A}, \qquad \bar A = \begin{pmatrix} \bar a & \bar b \\ \bar c & \bar d \end{pmatrix} .
$$

**Theorem.** The involution $\sigma$ is well defined, it is an **involutive automorphism** of the group (the composition with the conjugation of the base),

$$
\sigma(MN) = \sigma(M)\,\sigma(N) , \qquad \sigma^2 = \mathrm{id} ,
$$

and its fixed elements are the Möbius operators with a real representative matrix; the map is the action of the conjugation of the sphere on the group by the conjugation, and it is the Möbius instance of an involution on the operator layer.

**Proof.** The composition is $\iota M N \iota = (\iota M \iota)(\iota N \iota)$ because $\iota^2 = \mathrm{id}$, so $\sigma$ is multiplicative; the square is the identity, and the matrices fixed up to a scalar are those with a real representative. The statement is the standard conjugation of the matrix group, in *Involutive Bilinear Algebras* and *Real Forms and the Descent of an Algebra*.

### The Fixed Subgroup

**Theorem.** The fixed subgroup of the involution is the **real Möbius group**,

$$
PGL_2(\mathbb{C})^{\sigma} = PGL_2(\mathbb{R}) = PSL_2(\mathbb{R}) ,
$$

the group of the Möbius operators with real coefficients; it is the group of the automorphisms of the real projective line, it preserves the upper and the lower half-planes, and it acts on the upper half-plane as the orientation-preserving isometry group of the hyperbolic plane.

**Proof.** A class fixed by $\sigma$ has a representative matrix with $\bar A = \lambda A$ for a scalar, and multiplying by a scalar of the appropriate modulus gives a real representative; the group of the real matrices modulo the scalars is $PGL_2(\mathbb{R}) = PSL_2(\mathbb{R})$ because the nonzero real squares are positive, and the action on the half-plane is the classical one. The statement is in *The Möbius Transformation as an Operator* and *Hyperbolic Geometry*.

## The Real Möbius Transformations

**Theorem.** The real Möbius group $PSL_2(\mathbb{R})$ acts on the upper half-plane $\mathbb{H}^2 = \{z : \operatorname{Im} z > 0\}$ by the fractional linear maps, and this action is faithful, transitive and preserves the hyperbolic metric $|dz|^2/(\operatorname{Im} z)^2$; the group is the full orientation-preserving isometry group of the hyperbolic plane, and the boundary action on $\mathbb{P}^1(\mathbb{R})$ is the action on the circle at infinity.

**Proof.** The imaginary part transforms by $\operatorname{Im} M_A(z) = \operatorname{Im} z\,/\,|cz+d|^2$ for a real matrix of determinant one, so the half-plane is preserved and the hyperbolic metric is invariant; the transitivity is the matching of a point and a direction, and the faithfulness and the fullness are the standard computation of the isometry group. The statement is in *Hyperbolic Geometry*.

**Corollary (the conjugation and the hyperbolic reflection).** The conjugation $\iota$ is not in the Möbius group, but it is an isometry of the hyperbolic plane, and it is the reflection in the geodesic $i\mathbb{R}_{>0}$; it fixes that geodesic pointwise, it reverses the orientation, and it is the geodesic reflection of *Geodesic Reflection as an Operator* in the Poincaré model. The subgroup of the Möbius operators commuting with $\iota$ is the real Möbius group, and the fixed geodesic is the imaginary axis.

**Proof.** The conjugation is an anti-holomorphic isometry of the half-plane metric; its fixed set is the intersection of the fixed locus $\mathbb{R}\cup\{\infty\}$ with the half-plane, which is empty on the boundary but the geodesic between the two fixed boundary points $0$ and $\infty$ is the imaginary axis, fixed pointwise by $\iota$. The statement is in *Hyperbolic Geometry*.

## The Adjoint and the Unitary Realisation

### The Hermitian Form of Signature $(1,1)$

**Definition.** Let $J$ be the Hermitian form on $\mathbb{C}^2$ of signature $(1,1)$ with the matrix

$$
J = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} ;
$$

the **unitary group** of the form is

$$
U(1,1) = \{A \in GL_2(\mathbb{C}) : A^{*} J A = J\} ,
$$

with $A^* = \bar{A}^{\mathsf T}$ the conjugate transpose, and the special unitary group $SU(1,1)$ is the subgroup of determinant one; the projective group is $PU(1,1) = U(1,1)/\{\pm 1\}$.

**Theorem.** The adjoint of a matrix $A$ with respect to $J$ is $A^{\dagger} = J^{-1}A^{*}J$, the unitary elements are those with $A^{\dagger} = A^{-1}$, and the projective unitary group of the form of signature $(1,1)$ is the real Möbius group,

$$
PU(1,1) = PSU(1,1) \cong PSL_2(\mathbb{R}) ,
$$

so the fixed subgroup of the conjugation and the projective unitary group of the Hermitian form coincide, and the adjoint realises the involution on the operators.

**Proof.** The adjoint is the sandwich of the conjugate transpose by $J$ by *The Adjoint under a Hermitian Pairing*; the isomorphism $PSU(1,1) \cong PSL_2(\mathbb{R})$ is given by an explicit change of basis over $\mathbb{R}$ that carries the form of signature $(1,1)$ to the determinant form on the real matrices, and it is the standard isomorphism of the classical groups. The statement is in *Unitary Geometry over a Field with Involution*.

**Remark (the agreement of the two involutions).** The involution of the article is the conjugation of the base acting on the operators, and the adjoint is the involution of the operators induced by the Hermitian form; the fixed subgroup of the first is the real Möbius group and the projective unitary group of the second is the same group, so the two structures agree on this group. The agreement is the statement that the representation is a $*$-representation in the projective sense, and it is proved by the isomorphism above and not assumed.

## The Real Forms of $PSL_2(\mathbb{C})$

**Definition.** A **real form** of a complex group $G$ is a subgroup $G_0$ for which the complexification is $G$, equivalently the fixed subgroup of an antilinear involution; the real forms of $PSL_2(\mathbb{C})$ are the fixed subgroups of the antilinear involutions of the group.

**Theorem.** The complex group $PSL_2(\mathbb{C})$ has exactly two real forms up to conjugacy:

- the **split** form $PSL_2(\mathbb{R})$, the fixed subgroup of the complex conjugation of the article, with the real points of the real projective line, and with the hyperbolic plane as its symmetric space;
- the **compact** form $PSU(2) = PSU_2 \cong SO(3)$, the fixed subgroup of the quaternionic involution, with no real point in the projective line of the standard structure and with the sphere as its symmetric space.

The two forms correspond to the two classes of the Galois cohomology $H^1(\mathbb{C}/\mathbb{R}, PSL_2(\mathbb{C}))$, and the split form is the one of the involution of the article.

**Proof.** The real forms of $PSL_2(\mathbb{C})$ are classified by the antilinear involutions, and the two classes are distinguished by the real points of the corresponding structure on the projective line; the split form is the fixed group of the conjugation and the compact form is the fixed group of the quaternionic structure, and the cohomological classification is the standard one. The statement is in *Real Structures on a Projective Space* and *Real Forms of a Complex Lie Group and the Cartan Involution*.

**Remark (the trace classification and the involution).** The real Möbius group classifies its elements by the trace into the elliptic, parabolic and hyperbolic types, and the involution $\sigma$ acts on the classes by the conjugation of the trace, which is the real number unchanged; the classification of *The Möbius Transformation as an Operator* is thus compatible with the involution, and the real types are the ones whose square length in the hyperbolic metric is measured by the trace.

## Summary

The Möbius operators are the fractional linear transformations of the Riemann sphere, realised by the matrices of $PGL_2(\mathbb{C})$ up to the scalars, and the **complex conjugation** $\iota(z) = \bar z$ is an anti-Möbius involution of the sphere fixing the real projective line pointwise. The conjugation acts on the group by $\sigma(M_A) = M_{\bar A}$, an involutive automorphism of the group of the operators, and its fixed subgroup is the **real Möbius group** $PSL_2(\mathbb{R})$, the group of the real fractional linear maps, which acts on the upper half-plane as the isometry group of the hyperbolic plane and whose involution action on the plane is the reflection in the imaginary axis. The adjoint with respect to the Hermitian form of signature $(1,1)$ gives the unitary group $U(1,1)$, and the projective unitary group of the form is the real Möbius group, $PU(1,1) \cong PSU(1,1) \cong PSL_2(\mathbb{R})$, so the fixed subgroup of the involution and the projective unitary group coincide and the representation is a projective $*$-representation; the agreement is proved and not assumed. The complex group has exactly two real forms up to conjugacy, the split $PSL_2(\mathbb{R})$ of the conjugation and the compact $PSU(2) \cong SO(3)$ of the quaternionic involution, corresponding to the two classes of the Galois cohomology.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_A(z) = (az+b)/(cz+d)$ | Möbius operator of the matrix $A$ |
| $PGL_2(\mathbb{C}) = PSL_2(\mathbb{C})$ | Möbius group of the sphere |
| $\iota(z) = \bar z$ | Complex conjugation, an anti-Möbius involution |
| $\mathbb{P}^1(\mathbb{R})$ | Real projective line, the fixed locus of $\iota$ |
| $\sigma(M_A) = M_{\bar A}$ | Involution on the Möbius operators |
| $PGL_2(\mathbb{C})^{\sigma} = PSL_2(\mathbb{R})$ | Real Möbius group, the fixed subgroup |
| $J = \operatorname{diag}(1,-1)$ | Hermitian form of signature $(1,1)$ |
| $A^{\dagger} = J^{-1}A^{*}J$ | Adjoint with respect to $J$ |
| $U(1,1)$, $SU(1,1)$, $PU(1,1)$ | Unitary groups of the form of signature $(1,1)$ |
| $PU(1,1) \cong PSL_2(\mathbb{R})$ | Agreement of the unitary and the real Möbius groups |
| $PSU(2) \cong SO(3)$ | Compact real form of $PSL_2(\mathbb{C})$ |
| $\mathbb{H}^2 = \{z : \operatorname{Im} z > 0\}$ | Upper half-plane of the hyperbolic plane |

## Further Reading

- Alan F. Beardon, *The Geometry of Discrete Groups* (Springer, 1983), for the Möbius transformations, the real group and the hyperbolic plane.
- John B. Conway, *Functions of One Complex Variable*, 2nd ed. (Springer, 1978), for the fractional linear maps and the Riemann sphere.
- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds*, 2nd ed. (Springer, 2006), for the isometry groups and the half-plane and ball models.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1955), for the classical groups and the isomorphism $PSU(1,1) \cong PSL_2(\mathbb{R})$.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (Academic Press, 1978), for the real forms and the symmetric spaces.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions and the unitary groups.
