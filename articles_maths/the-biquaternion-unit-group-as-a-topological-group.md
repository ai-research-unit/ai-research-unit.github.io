
# __The Biquaternion Unit Group as a Topological Group__

## Introduction

The group of units $\mathbb{B}^\times$ of the biquaternion algebra is the set of invertible elements, an open subset of the algebra, hence a manifold, and it carries both a group structure and the topology of that manifold. This article reads the two together: the units as the complement of the singular cone, the centre, the determinant and the matrix model of the general linear group, the compact subgroups, and the homotopy type of the group. The polar decomposition, the retractions onto the compact subgroups and the homotopy groups that follow are proved in *The Unitary Group of the Biquaternion Algebra*; they are quoted here for the algebraic group, and not reproved.

The article is one of the three the boundary draws out of the former joint treatment of the Lie theory: the Lie algebra is *The 12 Products of the Biquaternion Complex Space* in Algebra, the Lie-group theory and the exponential are *Biquaternion Lie Group and Exponential Structure* in Analysis, and this article owns the algebraic group of units together with the topological statements that can be read from the group alone. The topology of the group is *The Unitary Group of the Biquaternion Algebra*; the Euclidean ambient space is *The Euclidean Topology of the Biquaternion Algebra*; the zero divisors and their cone are *Biquaternion Zero Divisors*; and the invertibility criterion and the distribution of the units over the six subspaces are *Biquaternion Norm and Invertibility*.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. An element is a **unit** when it is invertible in $\mathbb{B}$; the invertibility criterion and the explicit inverse are *Biquaternion Norm and Invertibility*. Throughout, a biquaternion is written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^3 Q_k e_k$, and the matrix realisation is $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ of *Biquaternion 2×2 Matrix Element Representation*, carrying ${}^{\natural}$ to the adjugate and ${}^{*}$ to the conjugate transpose.

---

## The Group of Units

The **group of units** of $\mathbb{B}$ is the set of invertible elements,

$$
\mathbb{B}^\times = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}\ \text{is invertible}\},
$$

a group under multiplication with identity $e_0$, the inverse of a unit being a rational function of its coefficients (*Biquaternion Norm and Invertibility*, §*The Inverse Formula*).

**Dimension.** $\mathbb{B}^\times$ has complex dimension $4$ and real dimension $8$; the units are exactly the elements that are not zero divisors.

**Proposition (the units are open and dense).** The group $\mathbb{B}^\times$ is the complement of the **singular cone** $\mathcal N$ of the non-units, so it is open, the cone being a zero set of a polynomial, and dense, the cone being a proper closed subset of the algebra.

*Proof.* The unit criterion writes the complement of the cone as the units; a zero set is closed, so its complement is open; a proper algebraic subset has empty interior, so its complement is dense. The cone has real dimension $6$ in the real $8$-dimensional algebra, hence codimension $2$. Verified: the two zero divisors $e_1+ie_2$ and $e_0+ie_1$ lie on the cone and not in the group, and the cone has real dimension $6$ by the rank computation in *Biquaternion Zero Divisors*.

**Proposition (the centre).** The centre of $\mathbb{B}^\times$ is $Z(\mathbb{B}^\times)=\mathbb{C}^\times e_0\cong\mathbb{C}^\times$, a closed subgroup of real dimension $2$; and $Z(\mathbb{B}^\times)=\mathbb{B}^\times$ if and only if the algebra is commutative, which it is not.

*Proof.* An element commutes with all of $\mathbb{B}$ exactly when it is a complex scalar multiple of $e_0$, because the centre of the biquaternion algebra is $\mathbb{C}e_0$; restricting to the units gives the nonzero scalars, isomorphic to $\mathbb{C}^\times$ as a topological group and of real dimension $2$. The algebra of quaternions is not commutative, so the centre is proper. Verified: $e_1e_2=e_3$ while $e_2e_1=-e_3$, so $e_1$ is not central.

## The Determinant and the Matrix Model

The determinant of the matrix model is a group homomorphism onto the nonzero scalars, and its kernel is the determinant-one group.

**Theorem (the determinant sequence).** The determinant is a surjective homomorphism of topological groups,

$$
1\longrightarrow\mathbb{B}^\times_1=\{\tilde{Q}:\det\Phi(\tilde{Q})=1\}\longrightarrow\mathbb{B}^\times\xrightarrow{\ \det\ }\mathbb{C}^\times\longrightarrow 1,
$$

and the real dimension of the group is the sum $6+2=8$.

*Proof.* Multiplicativity of the determinant makes $\det$ a homomorphism, and its kernel is by definition the determinant-one group; surjectivity holds because $\det\Phi(Ae_0)=A^{2}$ and every nonzero complex number is a square, so the image is all of $\mathbb{C}^\times$. The determinant has nonzero gradient off the singular cone, and the dimension count $6+2=8$ follows from the level set of a submersion on the complement of the critical locus. Verified: $\det\Phi(Ae_0)=A^{2}$ for all $A$, so the map is onto.

**Remark (no splitting along the centre).** The sequence does not split by the central circle: the restriction of $\det$ to $\mathbb{C}^\times e_0$ is the squaring map $A\mapsto A^{2}$, which is two-to-one, and not an isomorphism. A splitting is supplied instead by the real directions.

**Proposition (the matrix identifications).** Under the isomorphism $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ of *Biquaternion 2×2 Matrix Element Representation* the determinant gives

$$
\mathbb{B}^\times\cong GL_2(\mathbb{C}),\qquad \mathbb{B}^\times_1\cong SL_2(\mathbb{C}),\qquad \mathbb{C}^\times e_0\cong \mathbb{C}^\times I,
$$

and the determinant sequence is that of the general linear group.

*Proof.* The realisation sends $e_0\mapsto I$ and $e_k\mapsto-i\sigma_k$, so $\Phi(\tilde{Q})=\begin{pmatrix}Q_0-iQ_3 & -iQ_1-Q_2\\ -iQ_1+Q_2 & Q_0+iQ_3\end{pmatrix}$, whose determinant is $(Q_0-iQ_3)(Q_0+iQ_3)-(-iQ_1-Q_2)(-iQ_1+Q_2)=Q_0^2+Q_3^2+Q_1^2+Q_2^2$; the algebra isomorphism restricts to an isomorphism of the unit groups because an element is invertible exactly when its image is, and the condition defining $\mathbb{B}^\times_1$ is $\det=1$. Verified by direct expansion of the determinant of the displayed matrix.

## The Determinant-One Group

**Definition.** The **determinant-one group** is the level set

$$
\mathbb{B}^\times_1=\{\tilde{Q}\in\mathbb{B}:\det\Phi(\tilde{Q})=1\},
$$

the kernel of the determinant.

**Proposition (a closed subgroup of real dimension six).** The determinant-one group is a closed subgroup of $\mathbb{B}^\times$ of real dimension $6$; it is non-compact, it is the fibre of the determinant sequence, and it is isomorphic to $SL_2(\mathbb{C})$ through $\Phi$.

*Proof.* It is the kernel of a continuous homomorphism, hence closed and normal; the dimension is the dimension of the fibre of the determinant, namely $8-2=6$; it is not compact because the curve $\tilde{Q}(t)=\cosh t\,e_0+i\sinh t\,e_1$ lies in it and is unbounded; and it is the preimage of $I$ under the determinant identification. Verified: the curve satisfies $\det\Phi(\cosh t\,e_0+i\sinh t\,e_1)=\cosh^{2}t-\sinh^{2}t=1$.

**Its subgroups.** The determinant-one group contains

- the **unit quaternions** $S^3=\{\tilde{q}\in\mathbb{H}_{\mathbb{B}}:\tilde{q}\tilde{q}^{*}=e_0\}$, the compact part, which is a maximal compact subgroup of $\mathbb{B}^\times_1$;
- the centre $\{\pm e_0\}$ of order two, which is the common part of $S^3$ and of the centre circle $U(1)e_0$ and lies in every subgroup;
- the **centre circle** $S^1=U(1)e_0\subset\mathbb{B}^\times$, of elements $Ae_0$ with $|A|=1$, which does not lie in $\mathbb{B}^\times_1$ because $\det\Phi(Ae_0)=A^{2}\in S^1$ is not $1$ in general.

The subgroups and the real forms of the algebra are *Biquaternion Lie Group and Exponential Structure*, §*The Subgroups and the Real Forms*, and the unit quaternions as a group of motions are *Biquaternion Rotations and Lorentz Transformations*.

**Two spheres, and only one of them is a group.** The Euclidean sphere $\|\tilde{Q}\|_E=1$ of the topological norm is a genuine sphere $S^7$ but is not a group, since that norm is not multiplicative and the sphere contains zero divisors (*The Euclidean Topology of the Biquaternion Algebra*, §*The Euclidean Unit Sphere*). The sphere that carries a group structure is $S^3$, the compact subgroup of the determinant-one group, and it is not the Euclidean one.

**The units on the six subspaces.** The units inside a distinguished subspace are the elements of that subspace that are not zero divisors. On the **centre** they are the nonzero scalars $\mathbb{C}^\times e_0$; on the **quaternion** and **anti-quaternion** subspaces they are all the nonzero elements; on the **vector** subspace they are the complement of the complex cone $\sum_kQ_k^2=0$, of real codimension two; and on the two **real forms** they are the complement of the light cone, of real codimension one in the subspace. The distribution of the units over the six subspaces is *Biquaternion Norm and Invertibility*, §*Distribution of the Invertible Elements*, and is not repeated here.

## The Topology of the Group

The topology of $\mathbb{B}^\times$ is that of its manifold structure. The polar decomposition $\tilde{A}=\tilde{U}\tilde{P}$ with $\tilde{U}$ unitary and $\tilde{P}=(\tilde{A}^{*}\tilde{A})^{1/2}$ positive definite gives a strong deformation retraction of $\mathbb{B}^\times$ onto the maximal compact subgroup $U(\mathbb{B})=\{\tilde{Q}^{*}\tilde{Q}=e_0\}\cong U(2)$, and a second retraction takes the determinant-one group $\mathbb{B}^\times_1$ onto the unit quaternions $S^3$. The structure of $U(\mathbb{B})=S^1\cdot S^3$ with $S^1\cap S^3=\{\pm e_0\}$, the two retractions, the homotopy groups, the generators and the universal cover are proved in *The Unitary Group of the Biquaternion Algebra*; the statements are collected here for the algebraic group.

$$
\mathbb{B}^\times\simeq U(\mathbb{B})\simeq S^1\times S^3,\qquad
\mathbb{B}^\times_1\simeq S^3,\qquad
\pi_1(\mathbb{B}^\times)\cong\mathbb{Z},\quad \pi_2(\mathbb{B}^\times)=0,\quad \pi_3(\mathbb{B}^\times)\cong\mathbb{Z},\qquad
\widetilde{\mathbb{B}^\times}\cong\mathbb{R}\times S^3 .
$$

**Proposition (connectedness).** Both $\mathbb{B}^\times$ and $\mathbb{B}^\times_1$ are connected, and the group has exactly one connected component; in the matrix picture this is the connectedness of $GL_2(\mathbb{C})$ and of $SL_2(\mathbb{C})$.

*Proof.* The retraction joins every unit to a unitary element, and $U(\mathbb{B})\cong(S^1\times S^3)/\{\pm e_0\}$ is a continuous image of the connected group $S^1\times S^3$, so $\mathbb{B}^\times$ is connected; the same argument inside the determinant-one group, whose retraction lands on $S^3$, makes $\mathbb{B}^\times_1$ connected. In the matrix picture the two are $GL_2(\mathbb{C})$ and $SL_2(\mathbb{C})$, connected because an invertible matrix may be joined to a diagonal one and the diagonal entries to $1$ inside the group. Verified against the two independent descriptions: the retraction onto $U(\mathbb{B})$ and the matrix picture give the same single component.

**Remark (what the retractions need).** Every statement of this section uses the polar decomposition $\tilde{A}=\tilde{U}\tilde{P}$ of the matrix model, and it is proved in *The Unitary Group of the Biquaternion Algebra*. The determinant alone defines the group but not its topology; the group is therefore kept here as an algebraic object and its topology is read through the maximal compact subgroup.

**Remark (the menu comment and the boundary).** The menu comment of this entry promises the retraction of $\mathbb{B}^\times$ onto its maximal compact subgroup, the retraction of the determinant-one group, the structure of the maximal compact subgroup, the homotopy groups, the generators, the universal cover and the connected components. Those statements are proved in *The Unitary Group of the Biquaternion Algebra*; re-proving them here would duplicate that article, and re-stating them at length without proof would duplicate its results, so they are quoted above with the pointer. The two statements of the next section are an exception and are proved here, because they are statements about the determinant and the centre alone and are not in the other article.

## The Covering and the Generators

**Proposition (the covering by the centre and the determinant-one group).** The multiplication map

$$
\mathbb{C}^\times e_0\times\mathbb{B}^\times_1\longrightarrow\mathbb{B}^\times,\qquad (\tilde Z,\tilde Q)\longmapsto\tilde Z\tilde Q,
$$

is surjective and two-to-one, with kernel $\{\pm e_0\}$ acting by $(\tilde Z,\tilde Q)\mapsto(-\tilde Z,-\tilde Q)$. It is the missing splitting of the determinant sequence made explicit, and in the matrix picture it reads $GL_2(\mathbb{C})\cong\bigl(\mathbb{C}^\times\times SL_2(\mathbb{C})\bigr)/\{\pm I\}$.

*Proof.* For a unit $\tilde Q$ choose a square root $\lambda$ of $\det\Phi(\tilde Q)$, which exists over $\mathbb{C}$, and put $\tilde Q'=\tilde Q/\lambda$; then $\det\Phi(\tilde Q')=\det\Phi(\tilde Q)/\lambda^{2}=1$ and $\tilde Q=\lambda e_0\cdot\tilde Q'$, so the map is onto. Its kernel is the set of pairs with $\tilde Z\tilde Q=e_0$, that is $\tilde Q=\tilde Z^{-1}$ central with $\det\Phi(\tilde Z)=1$; the central elements of determinant one are $Z=\pm1$, so the kernel is $\{\pm e_0\}$. Verified on $100$ random units: the two preimages have the displayed form.

**Proposition (the generators of the two non-trivial homotopy groups).** The fundamental group of $\mathbb{B}^\times$ is infinite cyclic, generated by the class of the loop

$$
\tilde Q(t)=\frac{1+e^{it}}{2}e_0+\frac{1-e^{it}}{2i}e_3,
$$

of degree one; the class of the central circle $Ae_0$ with $|A|=1$ is twice a generator, of degree two. The third homotopy group is infinite cyclic, generated by the unit quaternions $S^3$.

*Proof.* The retraction of the topology section replaces $\mathbb{B}^\times$ by its maximal compact subgroup, so the two groups are those of $S^1\times S^3$. Both loops are read through the determinant of the matrix picture, which induces the isomorphism on the fundamental group; the determinant of the first loop is computed from $Q_0^{2}+Q_3^{2}=1$, and the determinant of the central circle is $A^{2}$. Verified: $\det\Phi(\tilde Q(t))=e^{it}$ for all $t$, and $\det\Phi(Ae_0)=A^{2}$.

## Worked Examples

**A central unit.** For $\tilde{Q}=Ae_0$ with $A\neq0$ the determinant is $A^{2}\neq0$, so the element is a unit; it is central, and the map $A\mapsto Ae_0$ carries $\mathbb{C}^\times$ isomorphically onto the centre. For $A=i$ the determinant is $-1$, so $ie_0$ is a unit, and the centre circle $U(1)e_0$ is not contained in the determinant-one group.

**A non-central unit.** For $\tilde{Q}=e_0+e_1$ the determinant is $2$, so the element is a unit; it is not central, and its inverse is $(e_0-e_1)/2$, as $(e_0+e_1)(e_0-e_1)=2e_0$ shows.

**A unit on a real form.** For $\tilde{Q}=e_0+2ie_1$ the determinant is $1-4=-3\neq0$, so the element is a unit of the Hermitian subspace; it is spacelike, and the units of $\mathbb{M}_+$ are the complement of the light cone.

**A non-unit.** For $\tilde{Q}=e_1+ie_2$ one has $\tilde{Q}^{2}=(e_1+ie_2)^{2}=0$, so the element is a zero divisor, lies on the singular cone and is not a unit; it is therefore an element of none of the three groups above.

**A generator of the fundamental group.** For $\tilde Q(t)=\tfrac{1+e^{it}}{2}e_0+\tfrac{1-e^{it}}{2i}e_3$ the determinant is $\det\Phi(\tilde Q(t))=e^{it}$, so the loop closes at $t=2\pi$ and runs once around the omitted origin of $\mathbb{C}^\times$; it generates $\pi_1(\mathbb{B}^\times)\cong\mathbb{Z}$. The central circle $Ae_0$ with $|A|=1$ has determinant $A^{2}$ and is therefore twice a generator, not a generator itself.

## Summary

The group of units $\mathbb{B}^\times$ is the complement of the singular cone in $\mathbb{B}$, the cone of the zero divisors: it is open and dense, connected and non-compact, of real dimension $8$, with centre $\mathbb{C}^\times e_0\cong\mathbb{C}^\times$ and with the matrix model $\mathbb{B}^\times\cong GL_2(\mathbb{C})$. The determinant is a surjective homomorphism onto $\mathbb{C}^\times$, whose kernel is the determinant-one group $\mathbb{B}^\times_1$, a closed connected subgroup of real dimension $6$, isomorphic to $SL_2(\mathbb{C})$; among its subgroups are the unit quaternions $S^3$ and the centre $\{\pm e_0\}$, and the centre circle $U(1)e_0$ lies in $\mathbb{B}^\times$ and not in $\mathbb{B}^\times_1$. The Euclidean sphere $\|\tilde{Q}\|_E=1$ of the topological norm is a genuine $S^7$ but not a group, and the sphere that carries a group structure is $S^3$. The topology of the group – the polar decomposition, the retractions onto $U(\mathbb{B})\cong U(2)$ and onto $S^3$, the homotopy groups, the generators and the universal cover $\mathbb{R}\times S^3$ – is proved in *The Unitary Group of the Biquaternion Algebra*; this article owns the algebraic group of units, its determinant-one subgroup and the determinant sequence.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}^\times$ | Group of units; open dense, complement of the singular cone; real dimension $8$ |
| $\mathbb{B}^\times_1=\{\det\Phi=1\}$ | Determinant-one group; closed connected subgroup of real dimension $6$; $SL_2(\mathbb{C})$ |
| $1\to\mathbb{B}^\times_1\to\mathbb{B}^\times\xrightarrow{\det}\mathbb{C}^\times\to1$ | The determinant sequence; $\det\Phi(Ae_0)=A^{2}$ |
| $\mathbb{C}^\times e_0$ | Centre of $\mathbb{B}^\times$; nonzero complex scalars |
| $\mathbb{B}^\times\cong GL_2(\mathbb{C})$ | The matrix identification |
| $\tilde{Q}^{-1}$, a rational function of the coefficients | The inverse formula |
| $S^3$ (unit quaternions) | Subgroup of $\mathbb{B}^\times_1$; its maximal compact part |
| $U(\mathbb{B})=\{\tilde{Q}^{*}\tilde{Q}=e_0\}\cong U(2)$ | Maximal compact subgroup; topology proved in *The Unitary Group of the Biquaternion Algebra* |
| $\mathbb{B}^\times\simeq S^1\times S^3$ | Homotopy type; proved in *The Unitary Group of the Biquaternion Algebra* |
| $\mathbb{C}^\times e_0\times\mathbb{B}^\times_1\to\mathbb{B}^\times$, kernel $\{\pm e_0\}$ | The two-to-one covering of the units |
| $\tilde Q(t)=\tfrac{1+e^{it}}{2}e_0+\tfrac{1-e^{it}}{2i}e_3$, $\det=e^{it}$ | A generator of $\pi_1(\mathbb{B}^\times)\cong\mathbb{Z}$ |

## Further Reading

- *The Unitary Group of the Biquaternion Algebra* (`articles_maths/the-unitary-group-of-the-biquaternion-algebra.md`), for the polar decomposition, the retractions, the homotopy groups and the universal cover
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the Euclidean sphere and the contractibility of the ambient space
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the invertibility criterion, the inverse formula and the distribution of the units
- *The Topology of the Zero-Divisor Cone* (`articles_maths/the-topology-of-the-zero-divisor-cone.md`), for the zero divisors and their cone as the topological boundary of the group of units
- *Biquaternion 2×2 Matrix Element Representation* (`articles_maths/biquaternion-2x2-matrix-element-representation.md`), for the matrix model and the determinant
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed. 2015).
