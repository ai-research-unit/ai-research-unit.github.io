
# __The Orthogonal Group and the Involutive Automorphism__

## Introduction

The isometry group of a real quadratic form of signature $(n,m)$ is the orthogonal group $O(n,m)$, and, like the unitary group, it carries a canonical **involutive automorphism**: the conjugation by the diagonal matrix of the form, $\theta(g) = JgJ^{-1}$. Its fixed subgroup is the product $O(n)\times O(m)$ of the two compact orthogonal groups of the definite parts, it is a Cartan involution, and the quotient is the symmetric space of the form — the manifold of negative $m$-planes, which for $n = 1$ is the hyperbolic space of the quadratic form. The construction is the real form of the unitary one: replacing the Hermitian form by a quadratic form replaces the unitary group by the orthogonal group, and the complex structure of the Hermitian case disappears, leaving a symmetric space of dimension $pq$ and rank $\min(n,m)$ with no intrinsic complex structure except in the two cases the next article classifies.

The article treats the orthogonal group of a quadratic form, the involutive automorphism with its fixed subgroup, the symmetric space it defines, and the comparison with the unitary case. The quadratic forms, their diagonalisation and their isometry classification are *Quadratic Forms and Polarisation* and *Bilinear Forms*; the orthogonal group, the reflections, the determinant and the Cartan–Dieudonné theorem are *Isometries and Orthogonal Transformations* and *The Rotation Group and Orientation*; the symmetric space, the symmetric pair, the Cartan involution and the rank are *Riemannian Symmetric Spaces and the Involution*; the homogeneous space $G/K$ is *Transformation Groups*; the Lie algebra is *The Orthogonal Lie Algebra*. The Riemannian geometry, the curvature and the geodesics of the quotient are *Curvature and Geodesics* and *Riemannian Geometry*; the Hermitian instances are *Hermitian Symmetric Spaces and the Group Involution*, later in this group. The involution on the **elements** of the group is read here; the **adjoint** of an operator is the group `- * Operator Theory`.

The article has four sections: the quadratic form and the orthogonal group; the involutive automorphism and its fixed subgroup; the symmetric space; and the worked cases. Throughout, $V = \mathbb{R}^{n}$ with a non-degenerate quadratic form $\mathfrak{Q}$ of signature $(n,m)$, $n+m=N$, $n \geq m \geq 1$ except where the compact case $m = 0$ is named, and $J = \operatorname{diag}(I_n,-I_m)$ is the matrix of the form in a diagonalising basis; $O(n,m) = \{g \in GL_n(\mathbb{R}) : g^{t}Jg = J\}$ and $SO(n,m)$ is its determinant-one subgroup.

## The Quadratic Form and the Orthogonal Group

### The Form and Its Transpose-Adjoint

**Definition.** The **quadratic form** of signature $(n,m)$ on $V$ is $\mathfrak{Q}(x) = \sum_{i \leq n}x_i^2 - \sum_{i>n}x_i^2$ in a suitable basis, with polar form $B(u,v) = \frac12(\mathfrak{Q}(u+v) - \mathfrak{Q}(u) - \mathfrak{Q}(v))$ of matrix $J$; a **definite decomposition** is an orthogonal decomposition $V = V_+\oplus V_-$ with $Q$ positive definite on $V_+$ and negative definite on $V_-$, of dimensions $n$ and $m$.

**Definition.** The **transpose-adjoint** of $T \in \operatorname{End}(V)$ with respect to $Q$ is the map $T^{t}$ with $B(Tu,v) = B(u,T^{t}v)$; it satisfies $(ST)^{t} = T^{t}S^{t}$, $(T^{t})^{t} = T$, and for the diagonal form it is the ordinary transpose with respect to the indefinite pairing, $T^{t} = J^{-1}T^{\mathrm{tr}}J$.

**Proposition.** The isometry group of $Q$ is

$$
O(V,\mathfrak{Q}) = \{T \in GL(V) : \mathfrak{Q}(Tv) = \mathfrak{Q}(v)\} = \{T : T^{t}T = \operatorname{id}\} = \{g : g^{t}Jg = J\},
$$

a real Lie group of dimension $\frac{n(n-1)}{2}$, of which the identity component is $SO_0(n,m)$; for $m = 0$ it is the compact orthogonal group $O(n)$, and for $m \geq 1$ it is noncompact.

**Proof.** The equivalence of the three definitions is the polarisation identity and the definition of the adjoint; the group is closed in $GL_n(\mathbb{R})$ and cut out by the algebraic equation $g^{t}Jg = J$, of dimension $\binom{n}{2}$ because the equation is symmetric in the pairs of indices; compactness for $m=0$ is boundedness, and noncompactness for $m\ge1$ is exhibited below by an unbounded one-parameter subgroup. The determinant is $\pm1$ on the group, by the same computation as in the definite case.

### The Two Families

**Proposition.** The pair $(O(V,\mathfrak{Q}), Q)$ depends only on the signature: two forms of the same signature are isometric, and their isometry groups are conjugate in $GL(V)$. The cases $m = 0$ and $n = m = 1$, and the general indefinite case $n \geq m \geq 1$, are distinguished by the topology: $O(n)$ is compact, $O(1,1)$ has two noncompact one-parameter subgroups, and $O(n,m)$ with $n > 1$ has a nonabelian simple identity component.

**Proof.** The first statement is Sylvester's law of inertia, *Quadratic Forms and Polarisation*; the compactness dichotomy is as above; the simplicity of the identity component of $SO(n,m)$ for $n+m \geq 3$ is the standard classification of the simple real Lie algebras of type $B$ and $D$, *The Orthogonal Lie Algebra*. The split case $n=m=1$ is the hyperbolic rotation group, *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*.

## The Involutive Automorphism and Its Fixed Subgroup

### The Involutive Automorphism

**Theorem (the involutive automorphism).** The map

$$
\theta : O(V,\mathfrak{Q}) \longrightarrow O(V,\mathfrak{Q}), \qquad \theta(g) = J\,g\,J^{-1},
$$

is an involutive automorphism of $O(V,\mathfrak{Q})$ — the **involutive automorphism** of the pair — and it is a Cartan involution: its fixed subgroup is

$$
O(V,\mathfrak{Q})^{\theta} = \{g : gJ = Jg\} = O(V_+)\times O(V_-) = O(n)\times O(m),
$$

the metrically diagonal matrices, it is the stabiliser of the definite decomposition, and it is a maximal compact subgroup; the differential $d\theta$ is $+1$ on $\mathfrak{k} = \mathfrak{o}(n)\oplus\mathfrak{o}(m)$ and $-1$ on $\mathfrak{n}$, and $\theta$ is unique up to conjugacy.

**Proof.** Conjugation by $J$ is an automorphism of the group of matrices preserving $J$, of order two because $J^2 = I$; a matrix is fixed exactly when it commutes with $J$, and the matrices commuting with $J$ are the block-diagonal ones; such a matrix preserves the form of signature $(n,m)$ exactly when its blocks preserve the definite forms, so the fixed subgroup is $O(n)\times O(m)$, which is compact. Maximality is the fixed-vector argument: a compact subgroup has an invariant positive vector, and iterating, an invariant definite decomposition, so it lies in a conjugate of $K$. The eigen-decomposition of $d\theta$ is the block decomposition of the Lie algebra, as in the unitary case.

**Remark.** The involution is on the **elements** of $G$, an automorphism of order two with the compact fixed subgroup; it is the differential of the geodesic symmetry of the symmetric space, *Riemannian Symmetric Spaces and the Involution*. The **transpose-adjoint** $T \mapsto T^{t}$ of the previous section is a different involution, on the operators, and the **adjoint** of the group `- * Operator Theory` is different again; neither is taken here.

### The Fixed Subgroup and the Cartan Decomposition

**Proposition.** The fixed subgroup $K = O(n)\times O(m)$ is a maximal compact subgroup of $O(V,\mathfrak{Q})$, and the quotient $O(V,\mathfrak{Q})/K$ is connected when the identity components are used; the Cartan decomposition is

$$
\mathfrak{o}(n,m) = \mathfrak{k}\oplus\mathfrak{n}, \qquad \mathfrak{n} = \left\{\begin{pmatrix} 0 & X \\ X^{t} & 0\end{pmatrix} : X \in \mathbb{R}^{n\times m}\right\} \cong \mathbb{R}^{pq},
$$

with $[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k}$, $[\mathfrak{k},\mathfrak{n}]\subseteq\mathfrak{n}$ and $[\mathfrak{n},\mathfrak{n}]\subseteq\mathfrak{k}$, so $\dim_{\mathbb{R}} O(n,m)/K = pq$.

**Proof.** The bracket relations are that $d\theta$ is a Lie algebra automorphism with eigenspaces $\mathfrak{k}$ and $\mathfrak{n}$; the identification of $\mathfrak{n}$ is the block computation, and its dimension is $pq$. Compactness of $K$ is the product of the compact orthogonal groups.

**Remark.** The dimension $pq$ is half the unitary dimension $2pq$ and half the complex dimension $pq$; the real form removes one of the two copies of $\mathbb{C}^{pq}$ that the Hermitian case carries. The rank $\min(n,m)$ is the same as in the unitary case.

## The Symmetric Space

### The Quotient

**Definition.** The **symmetric space** of the quadratic form is

$$
X = O(n,m)/(O(n)\times O(m)), \qquad \text{or} \qquad X_0 = SO_0(n,m)/(SO(n)\times SO(m)),
$$

with base point $o = eK$ and tangent space $T_oX = \mathfrak{n} \cong \mathbb{R}^{pq}$; the **geodesic symmetry** at $o$ is $s_o(gK) = \theta(g)K$.

**Proposition.** The space $X$ is the manifold of $Q$-negative subspaces of dimension $m$,

$$
X \cong \{W \leq V : \dim W = m,\ Q|_W < 0\},
$$

by $gK \mapsto gV_-$; it is a symmetric space of noncompact type, of dimension $pq$ and rank $\min(n,m)$, and the stabiliser of a negative subspace is a conjugate of $K$.

**Proof.** The stabiliser of $V_-$ is $K$, so the orbit is the quotient; the map is bijective by Witt's extension theorem for quadratic forms, *Bilinear Forms*; the rank is the maximal dimension of an abelian subspace of $\mathfrak{n}$, which is $\min(n,m)$ for the diagonal block; the symmetric space axioms are the existence of the involutive geodesic symmetry at each point, which is $s_o$ conjugated, *Riemannian Symmetric Spaces and the Involution*.

### The Compact Dual

**Proposition.** The **compact dual** of $X$ is the Grassmannian

$$
X^c = O(n+m)/(O(n)\times O(m)),
$$

the manifold of all $m$-planes of $V$; it is the compact symmetric space with the same isotropy and the opposite curvature, and $X$ and $X^c$ are related by the Cartan duality of *Riemannian Symmetric Spaces and the Involution*. The negative subspaces form an open subset of $X^c$, and the inclusion is the dual embedding.

**Proof.** The Grassmannian is the orbit of any $m$-plane under $O(n+m)$, with stabiliser $O(n)\times O(m)$, hence the compact homogeneous space; the curvature of $X^c$ is nonnegative and that of $X$ nonpositive, the two being the two real forms of the same complexification, *Riemannian Symmetric Spaces and the Involution*. The identification of the negative subspaces with an open subset is the definiteness condition on a $m$-plane.

### The Rank-One Case

**Proposition.** For $m = 1$, the space $X = O(n,1)/(O(n)\times O(1))$ is the **hyperbolic space** $H^n$ of constant negative curvature, realised as the hyperboloid $\{x : \mathfrak{Q}(x) = -1\}$ in $V$ with the induced metric; the involution $\theta$ is the conjugation by $J$ and the geodesic symmetry at the base point is $\theta$ itself. For $n = 1$, $m$ arbitrary, $X = H^m$ again, and the group $SO_0(1,q)$ is the Möbius group of $H^m$.

**Proof.** The hyperboloid is the orbit of a negative unit vector, and the stabiliser of the vector is $O(n)$; the induced metric on the hyperboloid has constant curvature $-1$, *Curvature and Geodesics*, and the geodesic symmetry is the restriction of the linear map $\theta$, which is the reflection in the tangent space at the base point. The two cases $n=1$ and $m=1$ are swapped by the exchange $Q \leftrightarrow -Q$.

**Remark.** The rank-one case is the hyperbolic geometry of *Curvature and Geodesics*, and it shows the geometric content of the signature: the form of signature $(n,1)$ is exactly the hyperbolic space, and the form of higher index gives the higher-rank symmetric space whose geodesics lie in flat totally geodesic submanifolds of the rank.

## Worked Cases

**Example (the compact orthogonal group).** Let $m = 0$. Then $O(V,\mathfrak{Q}) = O(n)$, $K = O(n)$ and $X$ is a point; the involutive automorphism is the identity up to conjugacy, and the compact dual is the group itself. The compact case is the degenerate end of the family.

**Example (the hyperbolic plane).** Let $n = m = 1$. Then $O(1,1)$ is the hyperbolic rotation group, $K = O(1)\times O(1)$ is finite, and $X = O(1,1)/(O(1)\times O(1))$ is the hyperbolic line $\mathbb{R}$, the geodesic through the origin; the involution $\theta(g) = JgJ^{-1}$ fixes the two one-parameter subgroups of diagonal matrices up to inverse, and the geodesic symmetry is $t \mapsto -t$ at the origin. The example is the smallest noncompact symmetric space of the orthogonal family.

**Example (the hyperbolic space).** Let $m = 1$, $n = n-1$. Then $X = O(n,1)/(O(n)\times O(1))$ is hyperbolic $n$-space $H^n$, of rank one and dimension $N$; the involutive automorphism fixes $O(n)\times O(1)$, the isotropy of a point of the hyperboloid, and the geodesic symmetry is the conjugation by $J$. The isometry group $SO_0(n,1)$ acts transitively on $H^n$, and the stabiliser of a point is $SO(n)$; this is the model space of *Curvature and Geodesics*.

**Example (the higher-rank case).** Let $n = m = n$. Then $X = O(n,n)/(O(n)\times O(n))$ is the Grassmannian of Lagrangian $n$-planes of the split form, of dimension $n^2$ and rank $n$; the involution $\theta(g) = JgJ^{-1}$ with $J = \operatorname{diag}(I_n,-I_n)$ is the conjugation by $J$, the fixed subgroup is $O(n)\times O(n)$, and a maximal abelian subspace of $\mathfrak{n}$ is the diagonal, of dimension $N$. The example is the orthogonal analogue of the Siegel disc and has no complex structure for $n > 2$.

## Summary

The orthogonal group $O(V,\mathfrak{Q})$ of a quadratic form of signature $(n,m)$ is the isometry group $\{T : T^{t}T = \operatorname{id}\}$ of the transpose-adjoint, a real Lie group of dimension $\binom{n}{2}$ conjugate to the model $O(n,m) = \{g : g^{t}Jg = J\}$ with $J = \operatorname{diag}(I_n,-I_m)$; the map $\theta(g) = JgJ^{-1}$ is an involutive automorphism, unique up to conjugacy, with fixed subgroup the maximal compact $O(n)\times O(m)$ and differential $+1$ on $\mathfrak{k} = \mathfrak{o}(n)\oplus\mathfrak{o}(m)$ and $-1$ on $\mathfrak{n}\cong\mathbb{R}^{pq}$. The quotient $O(n,m)/(O(n)\times O(m))$ is the symmetric space of the negative $m$-planes, of dimension $pq$ and rank $\min(n,m)$, with compact dual the real Grassmannian $O(n+m)/(O(n)\times O(m))$; for $m = 1$ it is hyperbolic $n$-space, and for $n = m = 1$ the hyperbolic line. The construction is the real form of the unitary one: the dimension is halved, the complex structure is absent in general, and only the Hermitian orthogonal cases carry one, *Hermitian Symmetric Spaces and the Group Involution*, the next article. The involution here is on the elements of the group; no adjoint is taken.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q$, $B$, $(n,m)$ | quadratic form, its polar form and its signature |
| $J = \operatorname{diag}(I_n,-I_m)$ | the matrix of the diagonalised form |
| $T^{t}$ | the transpose-adjoint, $B(Tu,v) = B(u,T^{t}v)$ |
| $O(V,\mathfrak{Q})$, $SO(V,\mathfrak{Q})$ | orthogonal and rotation groups of $Q$ |
| $O(n,m)$, $SO_0(n,m)$ | the model group and its identity component |
| $V = V_+\oplus V_-$ | a definite decomposition |
| $\theta(g) = JgJ^{-1}$ | the involutive automorphism (Cartan involution) |
| $K = O(n)\times O(m)$ | the fixed subgroup; a maximal compact subgroup |
| $\mathfrak{k}\oplus\mathfrak{n}$ | the Cartan decomposition; $\mathfrak{n}\cong\mathbb{R}^{pq}$ |
| $X = O(n,m)/(O(n)\times O(m))$ | the symmetric space of negative $m$-planes |
| $X^c = O(n+m)/(O(n)\times O(m))$ | the compact dual, the real Grassmannian |
| $H^n = O(n,1)/(O(n)\times O(1))$ | hyperbolic space, the rank-one case |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the orthogonal groups, the Cartan involution and the symmetric spaces of the quadratic forms.
- Joseph A. Wolf, *Spaces of Constant Curvature* (American Mathematical Society, sixth edition, 2011), for the rank-one orthogonal symmetric spaces and the hyperbolic model.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, second edition, 2002), for the Cartan decomposition of the orthogonal Lie algebras and the classification of the symmetric spaces by the signature.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1971), for the orthogonal groups, the Witt theorem and the geometry of the Grassmannians.
- O. Timothy O'Meara, *Introduction to Quadratic Forms* (Springer, 1973), for the isometry classification of quadratic forms and the signature invariants.
