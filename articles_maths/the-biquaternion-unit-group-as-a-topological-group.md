
# __The Biquaternion Unit Group as a Topological Group__

## Introduction

The group of units $\mathbb{B}^\times$ of the biquaternion algebra is the $\natural$-regular set, the set of invertible elements, an open subset of the algebra, hence a manifold, and it carries both a group structure and the topology of that manifold. This article reads the two together: the units as the complement of the null cone, the centre, the determinant and the matrix model of the general linear group, the compact subgroups, and the homotopy type of the group. The polar decomposition, the retractions onto the compact subgroups and the homotopy groups that follow are proved in *The Unitary Group of the Biquaternion Algebra*; they are quoted here for the algebraic group, and not reproved.

The article is one of the three the boundary draws out of the former joint treatment of the Lie theory: the Lie algebra is *Symmetric and Antisymmetric Decomposition of the Four General Products* in Algebra, the Lie-group theory and the exponential are *Biquaternion Lie Group and Exponential Structure* in Analysis, and this article owns the algebraic group of units together with the topological statements that can be read from the group alone. The topology of the group is *The Unitary Group of the Biquaternion Algebra*; the Euclidean ambient space is *The Euclidean Topology of the Biquaternion Algebra*; the zero divisors and their cone are *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*; and the invertibility criterion and the distribution of the units over the remarkable subspaces are *N-Regularity and N-Degeneracy in the Biquaternion Algebra*.

## The Group of Units

The **group of units** of $\mathbb{B}$, equivalently the **$\natural$-regular set**, is the set of invertible elements,

$$
\mathbb{B}^\times = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}\ \text{is invertible}\} = \{\tilde{Q}\in\mathbb{B}:\langle\tilde{Q}\rangle_{\natural}\neq0\},
$$

a group under multiplication with identity $e_t$, the inverse of a unit being a rational function of its coefficients (*N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Criterion*).

**Dimension.** $\mathbb{B}^\times$ has complex dimension $4$ and real dimension $8$; the units are exactly the $\natural$-regular elements, so the $\natural$-degenerate elements are the null cone, the origin together with the zero divisors, and the cone is exactly the complement of the group.

**Proposition (the units are open and dense).** The group $\mathbb{B}^\times$ is the complement of the **null cone** $\mathcal{N}$ of the norm, the set of non-units, so it is open, the cone being a zero set of a polynomial, and dense, the cone being a proper closed subset of the algebra.

*Proof.* The unit criterion writes the complement of the cone as the units; a zero set is closed, so its complement is open; a proper algebraic subset has empty interior, so its complement is dense. The cone has real dimension $6$ in the real $8$-dimensional algebra, hence codimension $2$.

**Proposition (the centre).** The centre of $\mathbb{B}^\times$ is $Z(\mathbb{B}^\times)=\mathbb{C}^\times e_t\cong\mathbb{C}^\times$, a closed subgroup of real dimension $2$; and $Z(\mathbb{B}^\times)=\mathbb{B}^\times$ if and only if the algebra is commutative, which it is not.

*Proof.* An element commutes with all of $\mathbb{B}$ exactly when it is a complex scalar multiple of $e_t$, because the centre of the biquaternion algebra is $\mathbb{C}e_t$; restricting to the units gives the nonzero scalars, isomorphic to $\mathbb{C}^\times$ as a topological group and of real dimension $2$. The algebra of quaternions is not commutative, so the centre is proper.

**The eigenvalue map.** For a unit $\tilde Q$, both eigenvalues $\lambda_\pm=Q_t\pm iB$ are non-zero, because $\lambda_+\lambda_-=\langle\tilde Q\rangle_{\natural}\neq0$. For a fixed choice of $B$ the ordered pair is a map
$$
\mathbb{B}^\times\longrightarrow(\mathbb{C}^\times)^2,\qquad \tilde Q\longmapsto(\lambda_+,\lambda_-),
$$
and the other choice of root exchanges the two coordinates. The map is surjective: given $\mu_\pm\neq0$, the element $\tilde Q=\frac{\mu_++\mu_-}{2}e_t+\frac{\mu_+-\mu_-}{2i}\vec e_z$ has spectrum $\{\mu_+,\mu_-\}$, the order depending on the choice of $B$. It is not injective: two units with the same eigenvalues differ by the direction of the vector part when $B\neq0$, and by a nilpotent part when $B=0$. It is not a group homomorphism: $\vec e_x$ and $\vec e_y$ both have eigenvalues $(i,-i)$, while $\vec e_x\vec e_y=\vec e_z$ has $(i,-i)$, not $(-1,-1)$.

## The Determinant and the Matrix Model

The determinant of the matrix model is a group homomorphism onto the nonzero scalars, and its kernel is the determinant-one group.

**Theorem (the determinant sequence).** The determinant is a surjective homomorphism of topological groups,

$$
\boxed{\; 1\longrightarrow\mathbb{B}^\times_1=\{\tilde{Q}:\det\mathsf{M}_2(\tilde{Q})=1\}\longrightarrow\mathbb{B}^\times\xrightarrow{\ \det\ }\mathbb{C}^\times\longrightarrow 1 \;},
$$

and the real dimension of the group is the sum $6+2=8$.

*Proof.* Multiplicativity of the determinant makes $\det$ a homomorphism, and its kernel is by definition the determinant-one group; surjectivity holds because $\det\mathsf{M}_2(Ae_t)=A^{2}$ and every nonzero complex number is a square, so the image is all of $\mathbb{C}^\times$. The determinant has nonzero gradient off the null cone, and the dimension count $6+2=8$ follows from the level set of a submersion on the complement of the critical locus.

**Remark (no splitting along the centre).** The sequence does not split by the central circle: the restriction of $\det$ to $\mathbb{C}^\times e_t$ is the squaring map $A\mapsto A^{2}$, which is two-to-one, and not an isomorphism. A splitting is supplied instead by the real directions.

**Proposition (the matrix identifications).** Under the isomorphism $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ of *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure* the determinant gives

$$
\boxed{\; \mathbb{B}^\times\cong GL_2(\mathbb{C}),\qquad \mathbb{B}^\times_1\cong SL_2(\mathbb{C}),\qquad \mathbb{C}^\times e_t\cong \mathbb{C}^\times I \;},
$$

and the determinant sequence is that of the general linear group.

*Proof.* The realisation sends $e_t\mapsto I$ and $\vec e_\mu\mapsto-i\sigma_\mu$, so $\mathsf{M}_2(\tilde{Q})=\begin{pmatrix}Q_t-iQ_z & -iQ_x-Q_y\\ -iQ_x+Q_y & Q_t+iQ_z\end{pmatrix}$, whose determinant is $(Q_t-iQ_3)(Q_t+iQ_3)-(-iQ_1-Q_y)(-iQ_1+Q_y)=Q_t^2+Q_z^2+Q_x^2+Q_y^2$; the algebra isomorphism restricts to an isomorphism of the unit groups because an element is invertible exactly when its image is, and the condition defining $\mathbb{B}^\times_1$ is $\det=1$.

## The Determinant-One Group

**Definition.** The **determinant-one group** is the level set

$$
\mathbb{B}^\times_1=\{\tilde{Q}\in\mathbb{B}:\det\mathsf{M}_2(\tilde{Q})=1\},
$$

the kernel of the determinant.

**Proposition (a closed subgroup of real dimension six).** The determinant-one group is a closed subgroup of $\mathbb{B}^\times$ of real dimension $6$; it is non-compact, it is the fibre of the determinant sequence, and it is isomorphic to $SL_2(\mathbb{C})$ through $\mathsf{M}_2$.

*Proof.* It is the kernel of a continuous homomorphism, hence closed and normal; the dimension is the dimension of the fibre of the determinant, namely $8-2=6$; it is not compact because the curve $\tilde{Q}(t)=\cosh t\,e_t+i\sinh t\,\vec e_x$ lies in it and is unbounded; and it is the preimage of $I$ under the determinant identification.

**Its subgroups.** The determinant-one group contains

- the **unit quaternions** $S^3=\{\tilde{q}\in\mathbb{H}_{\mathbb{B}}:\tilde{q}\tilde{q}^{*}=e_t\}$, the compact part, which is a maximal compact subgroup of $\mathbb{B}^\times_1$;
- the centre $\{\pm e_t\}$ of order two, which is the common part of $S^3$ and of the centre circle $\mathrm{U}(1)e_t$; it lies in every finite subgroup of $S^3$ of even order, in particular in every binary polyhedral group, and not in the cyclic groups of odd order;
- the **centre circle** $S^1=\mathrm{U}(1)e_t\subset\mathbb{B}^\times$, of elements $Ae_t$ with $|A|=1$, which does not lie in $\mathbb{B}^\times_1$ because $\det\mathsf{M}_2(Ae_t)=A^{2}\in S^1$ is not $1$ in general.

The subgroups and the real forms of the algebra are *Biquaternion Lie Group and Exponential Structure*, §*The Subgroups and the Real Forms*, and the unit quaternions as a group of motions are *Biquaternion Rotations and Lorentz Transformations*.

**Two spheres, and only one of them is a group.** The Euclidean sphere $\|\tilde{Q}\|_E=1$ of the topological norm is a genuine sphere $S^7$ but is not a group, since that norm is not multiplicative and the sphere contains zero divisors (*The Euclidean Topology of the Biquaternion Algebra*, §*The Euclidean Unit Sphere*). The sphere that carries a group structure is $S^3$, the compact subgroup of the determinant-one group, and it is not the Euclidean one.

**The units on the remarkable subspaces.** The units inside a remarkable subspace are the $\natural$-regular elements of that subspace, the elements that lie off its null cone; the $\natural$-degenerate elements of the subspace are its origin together with its zero divisors. On the **centre** they are the nonzero scalars $\mathbb{C}^\times e_t$; on the **quaternion** and **anti-quaternion** subspaces they are all the nonzero elements; on the **vector** subspace they are the complement of the complex cone $\sum_kQ_k^2=0$, of real codimension two; and on the two **real forms** they are the complement of the null cone, of real codimension one in the subspace. The distribution of the units over the remarkable subspaces is *Remarkable Subspaces under the General Quaternionic Algebra*, §*The Signatures and the Restriction Matrices*, and is not repeated here.

## The Topology of the Group

The topology of $\mathbb{B}^\times$ is that of its manifold structure. The polar decomposition $\tilde{Q}_1=\tilde Q_0\tilde{Q}_2$ with $\tilde Q_0$ unitary and $\tilde{Q}_2=(\tilde{Q}_1^{*}\tilde{Q}_1)^{1/2}$ positive definite gives a strong deformation retraction of $\mathbb{B}^\times$ onto the maximal compact subgroup $\mathrm{U}(\mathbb{B})=\{\tilde{Q}^{*}\tilde{Q}=e_t\}\cong \mathrm{U}(2)$, and a second retraction takes the determinant-one group $\mathbb{B}^\times_1$ onto the unit quaternions $S^3$. The structure of $\mathrm{U}(\mathbb{B})=S^1\cdot S^3$ with $S^1\cap S^3=\{\pm e_t\}$, the two retractions, the homotopy groups, the generators and the universal cover are proved in *The Unitary Group of the Biquaternion Algebra*; the statements are collected here for the algebraic group.

$$
\boxed{\; \mathbb{B}^\times\simeq \mathrm{U}(\mathbb{B})\simeq S^1\times S^3,\qquad
\mathbb{B}^\times_1\simeq S^3,\qquad
\pi_1(\mathbb{B}^\times)\cong\mathbb{Z},\quad \pi_2(\mathbb{B}^\times)=0,\quad \pi_3(\mathbb{B}^\times)\cong\mathbb{Z},\qquad
(\mathbb{B}^\times)^{\mathrm{cov}}\cong\mathbb{R}\times S^3 \;}.
$$

**Proposition (connectedness).** Both $\mathbb{B}^\times$ and $\mathbb{B}^\times_1$ are connected, and the group has exactly one connected component; in the matrix picture this is the connectedness of $GL_2(\mathbb{C})$ and of $SL_2(\mathbb{C})$.

*Proof.* The retraction joins every unit to a unitary element, and $\mathrm{U}(\mathbb{B})\cong(S^1\times S^3)/\{\pm e_t\}$ is a continuous image of the connected group $S^1\times S^3$, so $\mathbb{B}^\times$ is connected; the same argument inside the determinant-one group, whose retraction lands on $S^3$, makes $\mathbb{B}^\times_1$ connected. In the matrix picture the two are $GL_2(\mathbb{C})$ and $SL_2(\mathbb{C})$, connected because an invertible matrix may be joined to a diagonal one and the diagonal entries to $1$ inside the group.

**Remark (what the retractions need).** Every statement of this section uses the polar decomposition $\tilde{Q}_1=\tilde Q_0\tilde{Q}_2$ of the matrix model, and it is proved in *The Unitary Group of the Biquaternion Algebra*. The determinant alone defines the group but not its topology; the group is therefore kept here as an algebraic object and its topology is read through the maximal compact subgroup.

**Remark (the boundary).** The retraction of $\mathbb{B}^\times$ onto its maximal compact subgroup, the retraction of the determinant-one group, the structure of the maximal compact subgroup, the homotopy groups, the generators, the universal cover and the connected components are proved in *The Unitary Group of the Biquaternion Algebra* and are quoted here. The two statements of the next section are proved here, because they concern the determinant and the centre alone and are not in the other article.

## The Covering and the Generators

**Proposition (the covering by the centre and the determinant-one group).** The multiplication map

$$
\mathbb{C}^\times e_t\times\mathbb{B}^\times_1\longrightarrow\mathbb{B}^\times,\qquad (Ze_t,\tilde Q)\longmapsto Ze_t\tilde Q,
$$

is surjective and two-to-one, with kernel $\{\pm e_t\}$ acting by $(Ze_t,\tilde Q)\mapsto(-Ze_t,-\tilde Q)$. It is the missing splitting of the determinant sequence made explicit, and in the matrix picture it reads $GL_2(\mathbb{C})\cong\bigl(\mathbb{C}^\times\times SL_2(\mathbb{C})\bigr)/\{\pm I\}$.

*Proof.* For a unit $\tilde Q_1$ choose a square root $\lambda$ of $\det\mathsf{M}_2(\tilde Q_1)$, which exists over $\mathbb{C}$, and put $\tilde Q_2=\tilde Q_1/\lambda$; then $\det\mathsf{M}_2(\tilde Q_2)=\det\mathsf{M}_2(\tilde Q_1)/\lambda^{2}=1$ and $\tilde Q_1=\lambda e_t\cdot\tilde Q_2$, so the map is onto. Its kernel is the set of pairs with $Ze_t\tilde Q_1=e_t$, that is $\tilde Q_1=Z^{-1}e_t$ central with $\det\mathsf{M}_2(Ze_t)=1$; the central elements of determinant one are $Z=\pm1$, so the kernel is $\{\pm e_t\}$.

**Proposition (the generators of the two non-trivial homotopy groups).** The fundamental group of $\mathbb{B}^\times$ is infinite cyclic, generated by the class of the loop

$$
\tilde Q(t)=\frac{1+\exp(it)}{2}e_t+\frac{1-\exp(it)}{2i}\vec e_z,
$$

of degree one; the class of the central circle $Ae_t$ with $|A|=1$ is twice a generator, of degree two. The third homotopy group is infinite cyclic, generated by the unit quaternions $S^3$.

*Proof.* The retraction of the topology section replaces $\mathbb{B}^\times$ by its maximal compact subgroup, so the two groups are those of $S^1\times S^3$. Both loops are read through the determinant of the matrix picture, which induces the isomorphism on the fundamental group; the determinant of the first loop is computed from $Q_t^{2}+Q_z^{2}=1$, and the determinant of the central circle is $A^{2}$.

## Worked Examples

**A central unit.** For $\tilde{Q}=Ae_t$ with $A\neq0$ the determinant is $A^{2}\neq0$, so the element is a unit; it is central, and the map $A\mapsto Ae_t$ carries $\mathbb{C}^\times$ isomorphically onto the centre. For $A=i$ the determinant is $-1$, so $ie_t$ is a unit, and the centre circle $\mathrm{U}(1)e_t$ is not contained in the determinant-one group.

**A non-central unit.** For $\tilde{Q}=e_t+\vec e_x$ the determinant is $2$, so the element is a unit; it is not central, and its inverse is $(e_t-\vec e_x)/2$, as $(e_t+\vec e_x)(e_t-\vec e_x)=2e_t$ shows.

**A unit on a real form.** For $\tilde{Q}=e_t+2i\vec e_x$ the determinant is $1-4=-3\neq0$, so the element is a unit of the Hermitian subspace; it is spacelike, and the units of $\mathbb{M}_+$ are the complement in $\mathbb{M}_+$ of its null cone.

**A non-unit.** For $\tilde{Q}=\vec e_x+i\vec e_y$ one has $\tilde{Q}^{2}=(\vec e_x+i\vec e_y)^{2}=0$, so the element is $\natural$-degenerate, a zero divisor on the null cone, and is not a unit; it is therefore an element of none of the three groups above.

**A generator of the fundamental group.** For $\tilde Q(t)=\tfrac{1+\exp(it)}{2}e_t+\tfrac{1-\exp(it)}{2i}\vec e_z$ the determinant is $\det\mathsf{M}_2(\tilde Q(t))=\exp(it)$, so the loop closes at $t=2\pi$ and runs once around the omitted origin of $\mathbb{C}^\times$; it generates $\pi_1(\mathbb{B}^\times)\cong\mathbb{Z}$. The central circle $Ae_t$ with $|A|=1$ has determinant $A^{2}$ and is therefore twice a generator, not a generator itself.

## Summary

The group of units $\mathbb{B}^\times$ is the $\natural$-regular set, the complement of the $\natural$-degenerate null cone: it is open and dense, connected and non-compact, of real dimension $8$, with centre $\mathbb{C}^\times e_t\cong\mathbb{C}^\times$ and with the matrix model $\mathbb{B}^\times\cong GL_2(\mathbb{C})$. The determinant is a surjective homomorphism onto $\mathbb{C}^\times$, whose kernel is the determinant-one group $\mathbb{B}^\times_1$, a closed connected subgroup of real dimension $6$, isomorphic to $SL_2(\mathbb{C})$; among its subgroups are the unit quaternions $S^3$ and the centre $\{\pm e_t\}$, and the centre circle $\mathrm{U}(1)e_t$ lies in $\mathbb{B}^\times$ and not in $\mathbb{B}^\times_1$. The Euclidean sphere $\|\tilde{Q}\|_E=1$ of the topological norm is a genuine $S^7$ but not a group, and the sphere that carries a group structure is $S^3$. The topology of the group – the polar decomposition, the retractions onto $\mathrm{U}(\mathbb{B})\cong \mathrm{U}(2)$ and onto $S^3$, the homotopy groups, the generators and the universal cover $\mathbb{R}\times S^3$ – is proved in *The Unitary Group of the Biquaternion Algebra*; this article owns the algebraic group of units, its determinant-one subgroup and the determinant sequence.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}^\times$ | Group of units; open dense, complement of the null cone; real dimension $8$ |
| $\mathbb{B}^\times_1=\{\det\mathsf{M}_2=1\}$ | Determinant-one group; closed connected subgroup of real dimension $6$; $SL_2(\mathbb{C})$ |
| $1\to\mathbb{B}^\times_1\to\mathbb{B}^\times\xrightarrow{\det}\mathbb{C}^\times\to1$ | The determinant sequence; $\det\mathsf{M}_2(Ae_t)=A^{2}$ |
| $\mathbb{C}^\times e_t$ | Centre of $\mathbb{B}^\times$; nonzero complex scalars |
| $\mathbb{B}^\times\cong GL_2(\mathbb{C})$ | The matrix identification |
| $\tilde{Q}^{-1}$, a rational function of the coefficients | The inverse formula |
| $S^3$ (unit quaternions) | Subgroup of $\mathbb{B}^\times_1$; its maximal compact part |
| $\mathrm{U}(\mathbb{B})=\{\tilde{Q}^{*}\tilde{Q}=e_t\}\cong \mathrm{U}(2)$ | Maximal compact subgroup; topology proved in *The Unitary Group of the Biquaternion Algebra* |
| $\mathbb{B}^\times\simeq S^1\times S^3$ | Homotopy type; proved in *The Unitary Group of the Biquaternion Algebra* |
| $\mathbb{C}^\times e_t\times\mathbb{B}^\times_1\to\mathbb{B}^\times$, kernel $\{\pm e_t\}$ | The two-to-one covering of the units |
| $\tilde Q(t)=\tfrac{1+\exp(it)}{2}e_t+\tfrac{1-\exp(it)}{2i}\vec e_z$, $\det=\exp(it)$ | A generator of $\pi_1(\mathbb{B}^\times)\cong\mathbb{Z}$ |

## Further Reading

- [The Unitary Group of the Biquaternion Algebra](the-unitary-group-of-the-biquaternion-algebra.html), for the polar decomposition, the retractions, the homotopy groups and the universal cover
- [The Euclidean Topology of the Biquaternion Algebra](the-euclidean-topology-of-the-biquaternion-algebra.html), for the Euclidean sphere and the contractibility of the ambient space
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the invertibility criterion, the inverse formula and the distribution of the units
- [The Topology of the Zero-Divisor Cone](the-topology-of-the-zero-divisor-cone.html), for the zero divisors and their cone as the topological boundary of the group of units
- [$M_2(\mathbb{C})$ Representation : $GL_2(\mathbb{C})$, $SL_2(\mathbb{C})$ and the Determinant](m2c-representation-gl2-sl2-and-the-determinant.html), for the matrix model and the determinant
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An Elementary Introduction* (Springer, 2nd ed. 2015).
