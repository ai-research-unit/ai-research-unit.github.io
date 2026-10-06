# __The Unitary Group as a Topological Group__

## Introduction

The unitary elements of an associative algebra with involution form a group $U(A) = \{u : uu^{*} = u^{*}u = 1\}$, and when the algebra carries a norm the group carries the subspace topology and becomes an object of the topological layer. This article reads that object. Its structure is that of a topological group with a distinguished closed subgroup of $A^{\times}$, and in finite dimension, under the $\mathrm{C}^{*}$-condition on the norm, that of a compact Lie group whose Lie algebra is the skew-Hermitian part; its global structure is read by the components, and the group of the components is the first of the invariants that the topological K-theory of the bilinear layer computes.

Three facts organise the article. The unitary group is **closed** in the algebra, being the common zero set of the two continuous maps $u \mapsto uu^{*}$ and $u \mapsto u^{*}u$; consequently it is complete; it is bounded, hence compact in finite dimension, exactly when the norm is a $\mathrm{C}^{*}$-norm, and it is unbounded in general, as the remark of §*The Finite-Dimensional Case* shows. It is a **topological group** in the subspace topology, the product being the restriction of the jointly continuous product of the algebra and the inversion being the restriction of the continuous involution, $u^{-1} = u^{*}$; the general theory of topological groups then applies, and the component of the identity is a closed normal subgroup whose quotient is totally disconnected, open exactly when the group is locally path-connected. And in **finite dimension**, under the $\mathrm{C}^{*}$-condition, it is a compact Lie group, a closed subgroup of the general linear group, with the skew-Hermitian part as its Lie algebra; the exponential of *The Exponential Map on a Banach Sesquialgebra* is the chart that exhibits the correspondence, and it explains why the components of $U(A)$ are the obstruction to the exponential being surjective.

The article proves the closedness, the topological-group and the completeness statements, treats the components and the finite-dimensional and commutative cases, reads the Lie structure and the homotopy of the finite models, and names the relation to the topological K-theory, which it defers. The group itself, its stability under the involution and the inner $*$-automorphisms it induces are *Units and the Unitary Elements*; the Lie algebra of the skew-Hermitian part and its brackets are *The Unitary Lie Algebra*; the exponential and its image are *The Exponential Map on a Banach Sesquialgebra*; the normed and complete objects are *Banach Sesquialgebras*; and the general theory of topological groups is *Topological Groups*. Throughout, $(\mathbb{K},\varsigma)$ is $\mathbb{R}$ or $\mathbb{C}$ with its continuous involution, and $A$ is a unital normed sesquialgebra of the standard model, that is a unital normed algebra over $\mathbb{K}$ with an isometric $\varsigma$-semilinear involution $*$ and the derived product $x \star y = xy^{*}$; when a statement needs completeness, $A$ is a Banach algebra in this sense, and when a statement needs finite dimension it is said so.

## The Group and Its Topology

### The Closedness

**Theorem (the unitary group is closed).** $U(A)$ is a closed subset of $A$, and it is closed in $A^{\times}$ for the subspace topology.

*Proof.* The maps $\varphi(u) = uu^{*}$ and $\psi(u) = u^{*}u$ are continuous, since the product is jointly continuous and the involution is continuous, and $U(A) = \varphi^{-1}(\{1\}) \cap \psi^{-1}(\{1\})$. The preimage of a closed set under a continuous map is closed, and the intersection of two closed sets is closed. Since $U(A) \subseteq A^{\times}$, closedness in $A$ implies closedness in the subspace $A^{\times}$. $\square$

**Corollary (completeness).** If $A$ is a Banach algebra then $U(A)$ is complete as a metric space, and it is a closed subgroup of $A^{\times}$.

*Proof.* A closed subset of a complete metric space is complete. The subgroup statement is the group structure of *Units and the Unitary Elements*, §*The Group Structure*, together with the closedness just proved. $\square$

### The Topological Group

**Theorem (the unitary group is a topological group).** With the subspace topology of $A$, the group $U(A)$ is a topological group: the product $U(A) \times U(A) \to U(A)$ and the inversion $U(A) \to U(A)$ are continuous.

*Proof.* The product of the algebra is jointly continuous on $A \times A$ because the norm is submultiplicative, $\lVert xy - x_{0}y_{0}\rVert \leq \lVert x - x_{0}\rVert\lVert y\rVert + \lVert x_{0}\rVert\lVert y - y_{0}\rVert$, by *Banach Sesquialgebras*, §*The Submultiplicative Estimate*; its restriction to the subgroup is the product of the group and is continuous. The inversion is $u \mapsto u^{-1} = u^{*}$, which is the restriction of the continuous involution, hence continuous. $\square$

**Remark.** The proof uses the involution twice: to identify the inversion with a continuous map of the ambient algebra, and to make the inversion an isometry, $\lVert u^{*}\rVert = \lVert u\rVert$. The identification of the inversion with the involution is the reason the unitary group is more than an abstract group with a topology, and it is the sense in which the involution is the structure that the group respects.

### The Finite-Dimensional Case

**Theorem (compactness in finite dimension).** Let $A$ be a finite-dimensional unital normed algebra over $\mathbb{K}$ whose norm satisfies the $\mathrm{C}^{*}$-condition $\lVert x^{*}x\rVert = \lVert x\rVert^{2}$. Then $U(A)$ is compact, and in particular $\lVert u\rVert = 1$ for every unitary $u$.

*Proof.* In finite dimension over a complete valued field every norm is equivalent, the unit sphere is compact, and a closed bounded subset is compact, by *Normed and Banach Spaces*, §*Finite Dimension and Compactness*. For a unitary $u$ the $\mathrm{C}^{*}$-condition and $u^{*}u = 1$ give $\lVert u\rVert^{2} = \lVert u^{*}u\rVert = \lVert 1\rVert = 1$, so $U(A)$ is contained in the unit sphere and is bounded; it is closed by the theorem of §*The Closedness*. Hence it is compact. $\square$

**Remark (the isometric involution bounds the unitary group below, not above).** The $\mathrm{C}^{*}$-condition is not a decoration. On $A = \mathbb{K}^{2}$ with the componentwise product, the involution $\sigma(a,b) = (b,a)$ and the max norm, the involution is an isometric algebra involution and the norm is submultiplicative with $\lVert 1\rVert = 1$, so $A$ is a finite-dimensional object of the standard model; yet $(t, t^{-1})$ is unitary of norm $t$ for every $t \neq 0$, so $U(A)$ is unbounded and not compact. From $u^{*}u = 1$ and the isometry of the involution one gets only $1 = \lVert u^{*}u\rVert \leq \lVert u\rVert^{2}$, that is $\lVert u\rVert \geq 1$; the upper bound $\lVert u\rVert \leq 1$ is exactly what the $\mathrm{C}^{*}$-condition adds. For $M_{n}(\mathbb{C})$ with the operator norm both bounds hold and the containment of $U(A)$ in the unit sphere is strict, the unit sphere containing non-unitary matrices as well.

## Connectedness and the Components

### The Component of the Identity

**Theorem (the component of the identity is a closed normal subgroup).** Let $U(A)_{0}$ be the component of the identity of $U(A)$. Then $U(A)_{0}$ is a closed normal subgroup of $U(A)$, and the quotient $U(A)/U(A)_{0}$ is totally disconnected, so that it is the group of the connected components of $U(A)$. The component is open when $U(A)$ is locally path-connected; in particular it is open in finite dimension and for a unital $\mathrm{C}^{*}$-algebra, whose unitary group is a Banach–Lie group.

*Proof.* These are the general facts of *Topological Groups*, §*Connectedness* and §*Quotients*: in a topological group the component of the identity is a closed subgroup, it is normal because the inner automorphisms are homeomorphisms fixing the identity, and the quotient is totally disconnected with the components for its elements. The theorem of §*The Topological Group* supplies the hypothesis that $U(A)$ is a topological group; a closed subgroup with open component has the discrete quotient, and a locally path-connected group has open components, which is the case in finite dimension by the chart of the corollary below and for the unitary group of a unital $\mathrm{C}^{*}$-algebra. $\square$

**Proposition (the exponential runs in the component).** The image of the skew-Hermitian part under the exponential is contained in $U(A)_{0}$, and the subgroup of $U(A)$ generated by $\exp(S(A))$ is contained in $U(A)_{0}$.

*Proof.* This is *The Exponential Map on a Banach Sesquialgebra*, §*The Exponential into the Unitary Group*, together with the fact that a subgroup containing a connected subset containing the identity lies in the component of the identity. $\square$

### The Finite-Dimensional Case

**Theorem (the Lie group).** Let $A$ be a finite-dimensional unital normed algebra over $\mathbb{K}$. Then $U(A)$ is a Lie group, a closed subgroup of the general linear group $GL(A)$ of the underlying vector space, and its Lie algebra is the skew-Hermitian part $S(A)$ of *Hermitian and Skew-Hermitian Elements*, under the commutator; it is compact when the norm satisfies the $\mathrm{C}^{*}$-condition.

*Proof.* The group of the invertible elements $A^{\times}$ is an open subset of the finite-dimensional vector space $A$, hence a Lie group, by the Lie-group theory of *The Lie Algebra and the Exponential Map*; the unitary group is a closed subgroup by §*The Closedness*, and a closed subgroup of a Lie group is a Lie subgroup, by the closed subgroup theorem of that article. The Lie algebra of a closed subgroup is the set of the $x \in A$ with $\exp(tx)$ in the subgroup for all real $t$; since $tx$ has the sign of $x$ under the involution, $\exp(tx)$ is unitary for every real $t$ exactly when $x \in S(A)$, by *The Exponential Map on a Banach Sesquialgebra*, §*The Involution and the Exponential*. Hence the Lie algebra is $S(A)$, and the bracket is the commutator, as in *The Unitary Lie Algebra*, §*The Skew-Hermitian Part as a Lie Algebra*. $\square$

**Corollary (the exponential chart).** In finite dimension the exponential restricts to a map $S(A) \to U(A)_{0}$ that is a homeomorphism of a neighbourhood of $0$ onto a neighbourhood of $1$, so $U(A)_{0}$ is generated by $\exp(S(A))$.

*Proof.* The logarithm of *The Exponential Map on a Banach Sesquialgebra*, §*The Logarithm*, inverts the exponential on a neighbourhood of the identity; the inverse of a skew-Hermitian element is skew-Hermitian because the skew-Hermitian part is a real vector space, so the chart takes its values in $S(A)$ and provides a neighbourhood of the identity in $U(A)_{0}$. A connected Lie group is generated by any neighbourhood of the identity, by the Lie-group theory of *The Lie Algebra and the Exponential Map*. $\square$

### The Commutative Case

**Proposition (the commutative case).** If $A$ is commutative then $U(A)$ is abelian, the involution restricts to the inversion, which is an automorphism of $U(A)$, and the Hermitian unitary elements of *Units and the Unitary Elements*, §*The Involution and the Inverse*, are exactly the involutions of the group, $u^{*} = u$ and $u^{2} = 1$; they form a subgroup. They need not represent every component.

*Proof.* The commutativity, the restriction of the involution to the inversion and its being an automorphism are *Units and the Unitary Elements*, §*The Commutative Case*; a commutative group is abelian, which is the first statement. A Hermitian unitary satisfies $u^{*} = u$ and $u u^{*} = 1$, that is $u^{2} = 1$, and the set of such elements is a subgroup of an abelian group. That it need not exhaust the components is the example of §*Examples* on $C(S^{1},\mathbb{C})$, where the component group is $\mathbb{Z}$ and the Hermitian unitaries are only the constants $\pm1$. $\square$

**Remark.** In a commutative algebra the two equations of unitarity collapse to the single one $uu^{*} = 1$, the involution is an honest automorphism of the group, and the Hermitian unitary elements are exactly the involutions of the group. They need not exhaust the component group: for $A = C(S^{1},\mathbb{C})$ the Hermitian unitaries are the constants $\pm1$, while the components are the winding numbers of $\mathbb{Z}$, so the components of a commutative unitary group are in general read by a degree and not by a sign.

## The Lie Structure

### The Lie Algebra of the Skew-Hermitian Elements

**Proposition (the skew-Hermitian part is a real Lie algebra).** The skew-Hermitian part $S(A)$ is a real vector space closed under the commutator, and the map $x \mapsto \mathrm{ad}_{x}$ is a real Lie-algebra representation on $A$.

*Proof.* The set $S(A)$ is the fixed set of the real-linear map $x \mapsto -x^{*}$, hence a real vector space; for $x, y \in S(A)$ one has $[x,y]^{*} = (xy - yx)^{*} = y^{*}x^{*} - x^{*}y^{*} = (-y)(-x) - (-x)(-y) = yx - xy = -[x,y]$, so the bracket is skew-Hermitian. The Jacobi identity holds for associators and the representation property is the Leibniz rule, as in *The Unitary Lie Algebra*, §*The Skew-Hermitian Part as a Lie Algebra*. $\square$

**Remark.** Over $\mathbb{R}$ the skew-Hermitian part is the antisymmetric part and the Lie algebra is that of an orthogonal group; over $\mathbb{C}$ it is the imaginary Hermitian part, $x = iH$ with $H$ Hermitian, and the Lie algebra is that of a unitary group. The passage from the Lie algebra to the group is the exponential, and the theorem of §*The Finite-Dimensional Case* identifies the Lie algebra with the tangent space of the group at the identity.

### The Homotopy of the Finite Models

**Remark (the component group of a topological group, named and deferred).** The components of $U(A)$ are counted by the group $\pi_{0}(U(A)) = U(A)/U(A)_{0}$, which is a quotient of the group of the Hermitian unitary elements when $A$ is commutative. In the finite-dimensional models it is finite: for $M_{n}(\mathbb{C})$ with the conjugate transpose the group $U(n)$ is connected, by the theorem of *The Exponential Map on a Banach Sesquialgebra*, §*Examples*, so $\pi_{0}$ is trivial; for $M_{n}(\mathbb{R})$ with the transpose the group $O(n)$ has two components, $SO(n)$ and its complement, so $\pi_{0} = \mathbb{Z}/2$, the obstruction being the determinant; for $\mathbb{H}$ with the quaternion conjugation the group $S^{3}$ is connected, so $\pi_{0}$ is trivial. The homotopy of the stable groups, $\pi_{1}(U(n)) = \mathbb{Z}$ and the Bott periodicity that makes the stable fundamental group trivial, is the business of the topological K-theory, deferred below.

### The Relation to the Topological K-Theory

**Theorem (the components of the unitary group and the invertible group).** Let $A$ be a unital Banach algebra over $\mathbb{C}$ with a continuous involution. Then the inclusion $U(A) \hookrightarrow A^{\times}$ induces a bijection on the components in the sense that $\pi_{0}(U(A)) \to \pi_{0}(A^{\times})$ is surjective, and it is a bijection when $A$ is a $\mathrm{C}^{*}$-algebra.

*Proof.* This is the polar decomposition of *K-Theory of Operator Algebras*, §*Homotopy of Unitaries and the Stabilization of the Algebra*, quoted here and not re-proved: for a $\mathrm{C}^{*}$-algebra every invertible element is the product of a unitary and a positive invertible element, and the positive invertible elements form a connected set containing the identity, so each component of $A^{\times}$ meets $U(A)$ in exactly one component. $\square$

**Remark (named and deferred).** The group of the components of $U(A)$ is the first invariant of the topological K-theory of the bilinear layer: $K_1(A)$ is defined as $\pi_{0}$ of the stable invertible group, the unitaries suffice to compute it, and the index map and the six-term exact sequence are built on the map $\pi_{0}(U(A)) \to K_{1}(A)$ of the theorem. The whole of that theory is *K-Theory of Operator Algebras*, §*The Group $K_1(A)$*, and it is deferred; the article records only that the components of the unitary group are the invariant that the theory reads, and that the layering of this category ends at the door of that theory.

## Examples

### The Complex Matrices

**Example (the complex matrices, verdict: $U(n)$ is connected).** Let $A = M_{n}(\mathbb{C})$ with the operator norm, the conjugation and the conjugate transpose. The unitary group is $U(n)$, compact and connected; it is a Lie group with Lie algebra the skew-Hermitian matrices $\mathfrak{u}(n)$, and the exponential is onto, by the spectral theorem; $\pi_{0}$ is trivial and $\pi_{1}(U(n)) = \mathbb{Z}$. The example is the standard compact Lie group of the layer, and the one in which the correspondence between the group, its algebra and the exponential is exact.

**Example (the real matrices, verdict: two components).** Let $A = M_{n}(\mathbb{R})$ with the operator norm and the transpose. The unitary group is $O(n)$, compact with two components, and $U(A)_{0} = SO(n)$; the determinant is an isomorphism $\pi_{0}(O(n)) \to \mathbb{Z}/2$, realised by the Hermitian unitary element $-I$, whose determinant is $(-1)^{n}$ and which lies in the nontrivial component exactly for odd $n$, by *The Exponential Map on a Banach Sesquialgebra*, §*The Failure of Surjectivity*. The example is the orthogonal counterpart of the previous one, and the witness that the component group is a genuine invariant.

### The Field and the Quaternions

**Example (the field, verdict: the circle).** Let $A = \mathbb{C}$ with the modulus and the conjugation. Then $U(A) = S^{1}$ is a compact connected abelian Lie group, its Lie algebra is $i\mathbb{R}$, and the exponential $i\theta \mapsto e^{i\theta}$ is onto and a local diffeomorphism. The Hermitian unitary elements are $\pm1$, both in $U(A)$, and the group is its own identity component; the component group is trivial, and the fundamental group is $\mathbb{Z}$.

**Example (the quaternions, verdict: the sphere).** Let $A = \mathbb{H}$ over $\mathbb{R}$ with the quaternion conjugation. Then $U(A) = S^{3}\cong \mathrm{SU}(2)$ is a compact connected simply connected Lie group, with Lie algebra the pure imaginary quaternions; the exponential is onto by *The Exponential Map on a Banach Sesquialgebra*, §*Examples*, and the component group and the fundamental group are both trivial. The example is the compact case in which the exponential is surjective and the Lie correspondence is as sharp as it is in the complex matrices.

### The Functions

**Example (the functions on the circle, verdict: components by winding).** Let $A = C(S^{1},\mathbb{C})$ with the supremum norm and the involution $\sigma(f) = \bar f$. Then $U(A) = C(S^{1},S^{1})$ is a compact abelian topological group under the pointwise product, and its components are the classes of the functions of a fixed winding number; the component group is $\mathbb{Z}$. The element $f_{0}(z) = z$ is unitary of winding one, it is not in $U(A)_{0}$, and it is not an exponential, by *The Exponential Map on a Banach Sesquialgebra*, §*The Failure of Surjectivity*. The example is the infinite-dimensional model in which the component group is infinite and is computed by a degree rather than by a finite group.

## Summary

The **unitary group** $U(A)$ of a unital normed sesquialgebra of the standard model is closed in $A$, being the common zero set of the continuous maps $u \mapsto uu^{*}$ and $u \mapsto u^{*}u$, hence complete when $A$ is complete, and bounded, hence compact in finite dimension, exactly when the norm is a $\mathrm{C}^{*}$-norm. It is a **topological group** in the subspace topology, the product being the restriction of the jointly continuous product and the inversion being the continuous involution $u \mapsto u^{*}$; the **component of the identity** $U(A)_{0}$ is a closed normal subgroup and the quotient is totally disconnected. In finite dimension it is a **Lie group**, a closed subgroup of the general linear group, compact under the $\mathrm{C}^{*}$-condition, with the **skew-Hermitian part** as its Lie algebra under the commutator, and the exponential of the algebra is the chart that reaches $U(A)_{0}$ and no further: its failure of surjectivity is exactly the failure of $U(A)$ to be connected, and it is displayed by the unitary $-I$ of $M_{n}(\mathbb{R})$ for odd $n$ and by the unitary of winding one of $C(S^{1},\mathbb{C})$. The component group $\pi_{0}(U(A)) = U(A)/U(A)_{0}$ is the invariant that the **topological K-theory** of the bilinear layer reads, since $K_1(A)$ is $\pi_{0}$ of the stable invertible group and the unitaries suffice to compute it; the theory and the index map are named and deferred. The worked cases are the connected compact groups $U(n)$, $S^{1}$ and $S^{3}$, the two-component group $O(n)$, and the group of the continuous circle-valued functions, whose components are the winding numbers.

## Summary of Notation

| symbol | meaning |
|---|---|
| $U(A) = \{u : uu^{*} = u^{*}u = 1\}$ | the unitary group, closed in $A$ |
| $A^{\times}$ | the group of the invertible elements, in which $U(A)$ is a closed subgroup |
| $U(A)_{0}$ | the component of the identity, a closed normal subgroup |
| $\pi_{0}(U(A)) = U(A)/U(A)_{0}$ | the component group, totally disconnected |
| $\exp(S(A)) \subseteq U(A)_{0}$ | the image of the Lie algebra lies in the component of the identity |
| $S(A)$ | the skew-Hermitian part, the Lie algebra in finite dimension |
| $U(n) = U(M_{n}(\mathbb{C}))$, $\pi_{0} = 0$ | the connected compact model |
| $O(n) = U(M_{n}(\mathbb{R}))$, $\pi_{0} = \mathbb{Z}/2$ | the two-component model, obstruction $\det$ |
| $S^{1} = U(\mathbb{C})$, $S^{3} = U(\mathbb{H})$ | the connected compact models of the field and the quaternions |
| $C(S^{1},S^{1})$, $\pi_{0} = \mathbb{Z}$ | the functions, components by winding |
| $K_1(A) = \pi_{0}(GL_{\infty}(A))$ | the invariant of the bilinear layer, named and deferred |

## Further Reading

- Taqdir Husain, *Introduction to Topological Groups* (Saunders, 1966), for the component of the identity, the totally disconnected quotient and the general theory of topological groups.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the group of the units of a Banach algebra and its open-set topology.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the unitary group of a $\mathrm{C}^{*}$-algebra and its components.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the closed subgroup theorem, the Lie algebra of a Lie group and the finite-dimensional models.
- Dale Husemoller, *Fibre Bundles* (Springer, third edition, 1994), for the homotopy of the classical groups and the Bott periodicity named in the article.
- Max Karoubi, *K-Theory: An Introduction* (Springer, 1978), for the topological K-theory, the group $K_{1}$ and the index map that the closing section defers.
