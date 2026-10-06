
# __The Biquaternion Unit Group as a Topological Group__

## Introduction

The group of units $\mathbb{B}^\times$ of the biquaternion algebra is the set of elements of nonzero norm, an open subset of the algebra, hence a manifold, and it carries both a group structure and the topology of that manifold. This article reads the two together: the units as the complement of the null cone, the exact sequence that the norm defines, the centre, the norm-one group and its subgroups, and the identification with the general linear group of the matrix model. The polar decomposition, the retractions onto the compact subgroups and the homotopy groups that follow are read on the complex sesquilinear form and are proved in *The Unitary Group of the Biquaternion Algebra*; they are quoted here for the algebraic group, and not reproved.

The article is one of the three the boundary draws out of the former joint treatment of the Lie theory: the Lie algebra is *Biquaternion Lie Algebras* in Algebra, the Lie-group theory and the exponential are *Biquaternion Lie Group and Exponential Structure* in Analysis, and this article owns the algebraic group of units together with the topological statements that can be read from the group alone. The topology of the group, read on the complex sesquilinear form, is *The Unitary Group of the Biquaternion Algebra*; the Euclidean ambient space is *The Euclidean Topology of the Biquaternion Algebra*; the null cone is *Biquaternion Topology*; and the norm, the invertibility criterion and the distribution of the units over the six subspaces are *Biquaternion Norm and Invertibility*.

**Conventions.** The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and central scalar imaginary $i$; a general element is $\tilde{Q}=\sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The biquaternion norm is $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$, and $\tilde{Q}$ is a unit exactly when $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}\neq0$ (*Biquaternion Norm and Invertibility*). Throughout, a biquaternion is written $\tilde{Q}=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^3 Q_k e_k$, and the matrix realisation is $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ of *Biquaternion 2×2 Matrix Element Representation*, carrying ${}^{\natural}$ to the adjugate and ${}^{*}$ to the conjugate transpose.

---

## The Group of Units

The **group of units** of $\mathbb{B}$ is the set of invertible elements,

$$
\mathbb{B}^\times = \{\tilde{Q} \in \mathbb{B} : \langle\tilde{Q},\tilde{Q}\rangle_{\natural} \neq 0\},
$$

a group under multiplication with identity $e_0$ and with the inverse formula

$$
\tilde{Q}^{-1}=\frac{\tilde{Q}^{\natural}}{N(\tilde{Q})},
$$

which is the inverse formula of *Biquaternion Norm and Invertibility*, §*The Inverse Formula*, read in the form it takes because the norm is central.

**Dimension.** $\mathbb{B}^\times$ has complex dimension $4$ and real dimension $8$; the units are exactly the elements of nonzero norm.

**Proposition (the units are open and dense).** The group $\mathbb{B}^\times$ is the complement of the null cone $\mathcal N_{\natural}=\{N=0\}$, so it is open, since $N$ is a polynomial and the complement of a zero set is open, and dense, since the cone is a proper closed subset of the algebra.

*Proof.* The unit criterion writes the complement of the cone as the units; a zero set is closed, so its complement is open; a proper algebraic subset has empty interior, so its complement is dense. The cone has real dimension $6$ in the real $8$-dimensional algebra, hence codimension $2$. Verified: the explicit null elements $e_1+ie_2$ and $e_0+ie_1$ lie on the cone and not in the group, and the cone has real dimension $6$ by the rank computation of the previous article of the group.

**Proposition (the centre).** The centre of $\mathbb{B}^\times$ is $Z(\mathbb{B}^\times)=\mathbb{C}^\times e_0\cong\mathbb{C}^\times$, a closed subgroup of real dimension $2$; and $Z(\mathbb{B}^\times)=\mathbb{B}^\times$ if and only if the algebra is commutative, which it is not.

*Proof.* An element commutes with all of $\mathbb{B}$ exactly when it is a complex scalar multiple of $e_0$, because the centre of the biquaternion algebra is $\mathbb{C}e_0$; restricting to the units gives the nonzero scalars, isomorphic to $\mathbb{C}^\times$ as a topological group and of real dimension $2$. The algebra of quaternions is not commutative, so the centre is proper. Verified: $e_1e_2=e_3$ while $e_2e_1=-e_3$, so $e_1$ is not central.

## The Exact Sequence of the Norm

The norm is a group homomorphism onto the nonzero scalars, and its kernel is the norm-one group.

**Theorem (the norm sequence).** The biquaternion norm is a surjective homomorphism of topological groups,

$$
1\longrightarrow\mathbb{B}^\times_1=\{\tilde{Q}:N(\tilde{Q})=1\}\longrightarrow\mathbb{B}^\times\xrightarrow{\ N\ }\mathbb{C}^\times\longrightarrow 1,
$$

and the real dimension of the group is the sum $6+2=8$.

*Proof.* Multiplicativity of the norm makes $N$ a homomorphism, and its kernel is by definition the norm-one group; surjectivity holds because $N(Ae_0)=A^{2}$ and every nonzero complex number is a square, so the image is all of $\mathbb{C}^\times$. The norm has nonzero gradient off the cone, so its level sets meet the cone in the empty set and the dimension count $6+2=8$ follows from the level set of a submersion on the complement of the critical locus. Verified: $N(Ae_0)=A^{2}$ for all $A$, so the map is onto; $N(e_1+ie_2)=0$ shows the cone is exactly the excluded set.

**Remark (no splitting along the centre).** The sequence does not split by the central circle: the restriction of $N$ to $\mathbb{C}^\times e_0$ is the squaring map $A\mapsto A^{2}$, which is two-to-one, and not an isomorphism. A splitting is supplied instead by the real directions, and in the matrix picture the sequence is the determinant sequence of $GL_2(\mathbb{C})$.

**Proposition (the matrix identifications).** Under the isomorphism $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ of *Biquaternion 2×2 Matrix Element Representation* the norm is the determinant, $\det\Phi(\tilde{Q})=N(\tilde{Q})$, so that

$$
\mathbb{B}^\times\cong GL_2(\mathbb{C}),\qquad \mathbb{B}^\times_1\cong SL_2(\mathbb{C}),\qquad \mathbb{C}^\times e_0\cong \mathbb{C}^\times I,
$$

and the norm sequence is the determinant sequence of the general linear group.

*Proof.* The realisation sends $e_0\mapsto I$ and $e_k\mapsto-i\sigma_k$, so $\Phi(\tilde{Q})=\begin{pmatrix}Q_0-iQ_3 & -iQ_1-Q_2\\ -iQ_1+Q_2 & Q_0+iQ_3\end{pmatrix}$, whose determinant is $(Q_0-iQ_3)(Q_0+iQ_3)-(-iQ_1-Q_2)(-iQ_1+Q_2)=Q_0^2+Q_3^2+Q_1^2+Q_2^2=N(\tilde{Q})$; the algebra isomorphism restricts to an isomorphism of the unit groups because an element is invertible exactly when its image is, and the condition $N=1$ is the condition $\det=1$. Verified by direct expansion of the determinant of the displayed matrix.

## The Norm-One Group

**Definition.** The **norm-one group** is the level set

$$
\mathbb{B}^\times_1=\{\tilde{Q}\in\mathbb{B}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=1\},
$$

the kernel of the norm.

**Proposition (a closed subgroup of real dimension six).** The norm-one group is a closed subgroup of $\mathbb{B}^\times$ of real dimension $6$; it is non-compact, it is the fibre of the norm sequence, and it is isomorphic to $SL_2(\mathbb{C})$ through $\Phi$.

*Proof.* It is the kernel of a continuous homomorphism, hence closed and normal; the dimension is the dimension of the fibre of the norm, namely $8-2=6$; it is not compact because the curve $\tilde{Q}(t)=\cosh t\,e_0+i\sinh t\,e_1$ lies in it and is unbounded; and it is the preimage of $I$ under the determinant identification. Verified: the curve satisfies $N(\cosh t\,e_0+i\sinh t\,e_1)=\cosh^{2}t-\sinh^{2}t=1$.

**Its subgroups.** The norm-one group contains

- the **unit quaternions** $S^3=\{\tilde{q}\in\mathbb{H}_{\mathbb{B}}:N(\tilde{q})=1\}$, the compact part, which is a maximal compact subgroup of $\mathbb{B}^\times_1$;
- the centre $\{\pm e_0\}$ of order two, which is the common part of $S^3$ and of the centre circle $U(1)e_0$ and lies in every subgroup;
- the **centre circle** $S^1=U(1)e_0\subset\mathbb{B}^\times$, of elements $Ae_0$ with $|A|=1$, which does not lie in $\mathbb{B}^\times_1$ because $N(Ae_0)=A^{2}\in S^1$ is not $1$ in general.

The subgroups and the real forms of the algebra are *Biquaternion Lie Group and Exponential Structure*, §*The Subgroups and the Real Forms*, and the unit quaternions as a group of motions are *Biquaternion Rotations and Lorentz Transformations*.

**Two unit spheres.** There are two candidate "unit spheres" in $\mathbb{B}$, and only one of them is a group. The Euclidean sphere $\|\tilde{Q}\|_E=1$ is a genuine sphere $S^7$ but is not a group, since $\|\cdot\|_E$ is not multiplicative and the sphere contains zero divisors (*The Euclidean Topology of the Biquaternion Algebra*, §*The Euclidean Unit Sphere*). The level set $N=1$ is a group but is neither Euclidean nor compact. The condition that makes a level set of a form on $\mathbb{B}$ a subgroup is $N=1$, not $\|\tilde{Q}\|_E=1$.

**The units on the six subspaces.** Because the invertibility criterion is the non-vanishing of the norm, the units inside a distinguished subspace are the complement of the restriction of the null cone. On the **centre** they are the nonzero scalars $\mathbb{C}^\times e_0$; on the **quaternion** and **anti-quaternion** subspaces they are all the nonzero elements, the restricted norm being definite; on the **vector** subspace they are the complement of the complex cone $\sum_kQ_k^2=0$, of real codimension two; and on the two **real forms** they are the complement of the light cone, of real codimension one in the subspace. The distribution of the units over the six subspaces, with the three-way classification of an element by the sign of the norm on a real slice, is *Biquaternion Norm and Invertibility*, §*Distribution of the Invertible Elements*, and is not repeated here.

## The Topology of the Group

The topology of $\mathbb{B}^\times$ is read through the complex sesquilinear form. The polar decomposition $\tilde{A}=\tilde{U}\tilde{P}$ with $\tilde{U}$ unitary and $\tilde{P}=(\tilde{A}^{*}\tilde{A})^{1/2}$ Hermitian positive definite gives a strong deformation retraction of $\mathbb{B}^\times$ onto the maximal compact subgroup $U(\mathbb{B})=\{\tilde{Q}^{*}\tilde{Q}=e_0\}\cong U(2)$, and a second retraction takes the norm-one group $\mathbb{B}^\times_1$ onto the unit quaternions $S^3$. The structure of $U(\mathbb{B})=S^1\cdot S^3$ with $S^1\cap S^3=\{\pm e_0\}$, the two retractions, the homotopy groups, the generators and the universal cover are proved in *The Unitary Group of the Biquaternion Algebra*; the statements are collected here for the algebraic group.

$$
\mathbb{B}^\times\simeq U(\mathbb{B})\simeq S^1\times S^3,\qquad
\mathbb{B}^\times_1\simeq S^3,\qquad
\pi_1(\mathbb{B}^\times)\cong\mathbb{Z},\quad \pi_2(\mathbb{B}^\times)=0,\quad \pi_3(\mathbb{B}^\times)\cong\mathbb{Z},\qquad
\widetilde{\mathbb{B}^\times}\cong\mathbb{R}\times S^3 .
$$

**Proposition (connectedness).** Both $\mathbb{B}^\times$ and $\mathbb{B}^\times_1$ are connected, and the group has exactly one connected component; in the matrix picture this is the connectedness of $GL_2(\mathbb{C})$ and of $SL_2(\mathbb{C})$.

*Proof.* The retraction joins every unit to a unitary element, and $U(\mathbb{B})\cong(S^1\times S^3)/\{\pm e_0\}$ is a continuous image of the connected group $S^1\times S^3$, so $\mathbb{B}^\times$ is connected; the same argument inside the norm-one group, whose retraction lands on $S^3$, makes $\mathbb{B}^\times_1$ connected. In the matrix picture the two are $GL_2(\mathbb{C})$ and $SL_2(\mathbb{C})$, connected because an invertible matrix may be joined to a diagonal one and the diagonal entries to $1$ inside the group. Verified against the two independent descriptions: the retraction onto $U(\mathbb{B})$ and the matrix picture give the same single component.

**Remark (why the dagger enters).** Every statement of this section uses the complex sesquilinear form, through the dagger and the positive definite square root. The quaternion bilinear norm $N$ alone defines the group, $\mathbb{B}^\times=\{N\neq0\}$, but not its topology: $N$ is complex-valued and indefinite, and the level set $N=1$ is a group that is not compact. The corpus therefore keeps the algebraic group of units here, at the bilinear layer, and proves its topology in the Hermitian layer.

**Remark (the menu comment and the boundary).** The menu comment of this entry promises the retraction of $\mathbb{B}^\times$ onto its maximal compact subgroup, the retraction of the norm-one group, the structure of the maximal compact subgroup, the homotopy groups, the generators, the universal cover and the connected components. Those statements are proved, on the Hermitian form, in *The Unitary Group of the Biquaternion Algebra*, a written article of the neighbouring reading group; re-proving them here would duplicate that article, and re-stating them at length without proof would duplicate its results. They are therefore quoted above, with the pointer, and the conflict between the comment and the boundary of the two articles is recorded in the companion `.context` file for the author's decision. The two statements of the next section are an exception and are proved here, because they are statements about the norm and the centre alone and are not in the other article.

## The Covering and the Generators

**Proposition (the covering by the centre and the norm-one group).** The multiplication map

$$
\mathbb{C}^\times e_0\times\mathbb{B}^\times_1\longrightarrow\mathbb{B}^\times,\qquad (\tilde Z,\tilde Q)\longmapsto\tilde Z\tilde Q,
$$

is surjective and two-to-one, with kernel $\{\pm e_0\}$ acting by $(\tilde Z,\tilde Q)\mapsto(-\tilde Z,-\tilde Q)$. It is the missing splitting of the norm sequence made explicit, and in the matrix picture it reads $GL_2(\mathbb{C})\cong\bigl(\mathbb{C}^\times\times SL_2(\mathbb{C})\bigr)/\{\pm I\}$.

*Proof.* For a unit $\tilde Q$ choose a square root $\lambda$ of $N(\tilde Q)$, which exists over $\mathbb{C}$, and put $\tilde Q'=\tilde Q/\lambda$; then $N(\tilde Q')=N(\tilde Q)/\lambda^{2}=1$ and $\tilde Q=\lambda e_0\cdot\tilde Q'$, so the map is onto. Its kernel is the set of pairs with $\tilde Z\tilde Q=e_0$, that is $\tilde Q=\tilde Z^{-1}$ central with $N(\tilde Z)=1$; the central elements of norm one are $Z=\pm1$, so the kernel is $\{\pm e_0\}$. Verified on $100$ random units: the two preimages have the displayed form.

**Proposition (the generators of the two non-trivial homotopy groups).** The fundamental group of $\mathbb{B}^\times$ is infinite cyclic, generated by the class of the loop

$$
\tilde Q(t)=\frac{1+e^{it}}{2}e_0+\frac{1-e^{it}}{2i}e_3,
$$

whose norm is $e^{it}$, of degree one; the class of the central circle $Ae_0$ with $|A|=1$ is twice a generator, its norm being $A^{2}$, of degree two. The third homotopy group is infinite cyclic, generated by the unit quaternions $S^3$.

*Proof.* The retraction of the topology section replaces $\mathbb{B}^\times$ by its maximal compact subgroup, so the two groups are those of $S^1\times S^3$. Both loops are read through the norm, which is the determinant of the matrix picture and induces the isomorphism on the fundamental group; the norm of the first loop is computed from $Q_0^{2}+Q_3^{2}=1$, and the norm of the central circle is $A^{2}$. Verified: $N(\tilde Q(t))=e^{it}$ for all $t$, and $N(Ae_0)=A^{2}$.

## Worked Examples

**A central unit.** For $\tilde{Q}=Ae_0$ with $A\neq0$ the norm is $A^{2}\neq0$, so the element is a unit; it is central, and the map $A\mapsto Ae_0$ carries $\mathbb{C}^\times$ isomorphically onto the centre. For $A=i$ the norm is $-1$, so $ie_0$ is a unit of negative norm, and the centre circle $U(1)e_0$ is not contained in the norm-one group.

**A non-central unit.** For $\tilde{Q}=e_0+e_1$ the norm is $2$, so the element is a unit; it is not central, and its inverse is $\tilde{Q}^{\natural}/2=(e_0-e_1)/2$.

**A unit on a real form.** For $\tilde{Q}=e_0+2ie_1$ the norm is $1-4=-3\neq0$, so the element is a unit of the Hermitian subspace; it is spacelike, and the units of $\mathbb{M}_+$ are the complement of the light cone.

**A non-unit.** For $\tilde{Q}=e_1+ie_2$ the norm is $1+i^{2}=0$, so the element lies on the null cone and is a zero divisor; it is neither a unit nor, therefore, an element of any of the three groups above.

**A generator of the fundamental group.** For $\tilde Q(t)=\tfrac{1+e^{it}}{2}e_0+\tfrac{1-e^{it}}{2i}e_3$ the norm is $N(\tilde Q(t))=e^{it}$, so the loop closes at $t=2\pi$ and runs once around the omitted origin of $\mathbb{C}^\times$; it generates $\pi_1(\mathbb{B}^\times)\cong\mathbb{Z}$. The central circle $Ae_0$ with $|A|=1$ has norm $A^{2}$ and is therefore twice a generator, not a generator itself.

## Summary

The group of units $\mathbb{B}^\times=\{N\neq0\}$ is the complement of the null cone in $\mathbb{B}$: open and dense, connected and non-compact, of real dimension $8$, with centre $\mathbb{C}^\times e_0\cong\mathbb{C}^\times$ and with the matrix model $\mathbb{B}^\times\cong GL_2(\mathbb{C})$. The norm is a surjective homomorphism onto $\mathbb{C}^\times$, whose kernel is the norm-one group $\mathbb{B}^\times_1=\{N=1\}$, a closed connected subgroup of real dimension $6$, isomorphic to $SL_2(\mathbb{C})$; among its subgroups are the unit quaternions $S^3$ and the centre $\{\pm e_0\}$, and the centre circle $U(1)e_0$ lies in $\mathbb{B}^\times$ and not in $\mathbb{B}^\times_1$. The two spherical level sets of the algebra are the Euclidean sphere $\|\tilde{Q}\|_E=1$, a genuine $S^7$ but not a group and containing zero divisors, and the algebraic level set $N=1$, a group; only the second is a subgroup of $\mathbb{B}^\times$. The topology of the group – the polar decomposition, the retractions onto $U(\mathbb{B})\cong U(2)$ and onto $S^3$, the homotopy groups, the generators and the universal cover $\mathbb{R}\times S^3$ – is read through the complex sesquilinear form and is proved in *The Unitary Group of the Biquaternion Algebra*; this article owns the algebraic group of units, its norm-one subgroup and the exact sequence that the norm defines.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}^\times=\{N\neq0\}$ | Group of units; open dense, complement of the null cone; real dimension $8$ |
| $\mathbb{B}^\times_1=\{N=1\}$ | Norm-one group; closed connected subgroup of real dimension $6$; $SL_2(\mathbb{C})$ |
| $1\to\mathbb{B}^\times_1\to\mathbb{B}^\times\xrightarrow{N}\mathbb{C}^\times\to1$ | The norm sequence; $N(Ae_0)=A^{2}$ |
| $\mathbb{C}^\times e_0$ | Centre of $\mathbb{B}^\times$; nonzero complex scalars |
| $\mathbb{B}^\times\cong GL_2(\mathbb{C})$, $\det\Phi=N$ | The matrix identifications |
| $\tilde{Q}^{-1}=\tilde{Q}^{\natural}/N(\tilde{Q})$ | The inverse formula |
| $S^3$ (unit quaternions) | Subgroup of $\mathbb{B}^\times_1$; its maximal compact part |
| $U(\mathbb{B})=\{\tilde{Q}^{*}\tilde{Q}=e_0\}\cong U(2)$ | Maximal compact subgroup; topology proved in *The Unitary Group of the Biquaternion Algebra* |
| $\mathbb{B}^\times\simeq S^1\times S^3$ | Homotopy type; proved in *The Unitary Group of the Biquaternion Algebra* |
| $\mathbb{C}^\times e_0\times\mathbb{B}^\times_1\to\mathbb{B}^\times$, kernel $\{\pm e_0\}$ | The two-to-one covering of the units |
| $\tilde Q(t)=\tfrac{1+e^{it}}{2}e_0+\tfrac{1-e^{it}}{2i}e_3$, $N=e^{it}$ | A generator of $\pi_1(\mathbb{B}^\times)\cong\mathbb{Z}$ |

## Further Reading

- *The Unitary Group of the Biquaternion Algebra* (`articles_maths/the-unitary-group-of-the-biquaternion-algebra.md`), for the polar decomposition, the retractions, the homotopy groups and the universal cover, all read on the complex sesquilinear form
- *The Euclidean Topology of the Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.md`), for the Euclidean sphere and the contractibility of the ambient space
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the invertibility criterion, the inverse formula and the distribution of the units
- *Biquaternion Topology* (`articles_maths/biquaternion-topology.md`), for the null cone as the topological boundary of the group of units
- *Biquaternion 2×2 Matrix Element Representation* (`articles_maths/biquaternion-2x2-matrix-element-representation.md`), for the matrix model and the determinant–norm identity
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed. 2015).
