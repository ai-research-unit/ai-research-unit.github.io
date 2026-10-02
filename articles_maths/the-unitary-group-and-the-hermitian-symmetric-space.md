
# __The Unitary Group and the Hermitian Symmetric Space__

## Introduction

The isometry group of a non-degenerate Hermitian form of signature $(p,q)$ is the unitary group $U(p,q)$, and the quotient of it by the stabiliser of a maximal negative-definite subspace is a **Hermitian symmetric space**: a symmetric space in which the geodesic symmetry at each point is complex-linear, so that the space carries an invariant complex structure and the symmetry group acts by holomorphic transformations. The unitary group is the case of the classical groups in which the symmetric space has a complex structure built in, and it is the source of the bounded symmetric domains: the space $U(p,q)/(U(p)\times U(q))$ is a bounded domain in $\mathbb{C}^{pq}$, the **matrix unit ball** $\{Z : Z^{\dagger}Z < I\}$, by the Harish-Chandra embedding, and the group acts on it by fractional linear transformations.

The article treats the group, the involution that defines the symmetric space, the space itself as the manifold of negative subspaces, and the bounded realisation. The unitary group of a Hermitian form, its determinant and its special subgroup are *The Unitary and Symplectic Groups*; the Hermitian forms and their classification are *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*; the symmetric space, the symmetric pair, the Cartan involution and the rank are *Riemannian Symmetric Spaces and the Involution*; the homogeneous space $G/K$, its isotropy representation and its invariant connections are *Transformation Groups*; the Lie group structure and the Lie algebra are *Lie Groups* and *The Orthogonal Lie Algebra*. The invariant Kähler metric of the domain, the Bergman kernel and the boundary theory are *Hermitian Symmetric Spaces and the Bergman Metric* and *Kähler Geometry*, below this Part, and are named but not developed here; the curvature of the domain is *Curvature and Geodesics*. The involution on the **elements** of the group is what this article reads; the **adjoint** of an operator and the `*`-structures it defines are the group `- * Operator Theory` of this category and are not used.

The article has four sections: the Hermitian form and the unitary group; the involution and the symmetric space; the bounded realisation; and the worked cases. Throughout, $p, q \geq 1$, $V = \mathbb{C}^{p+q}$ is the standard module with the Hermitian form $h$ of signature $(p,q)$ and matrix $J = \operatorname{diag}(I_p, -I_q)$, and $U(p,q) = \{g \in GL_{p+q}(\mathbb{C}) : g^{\dagger}Jg = J\}$; the compact case $q = 0$ is the ordinary unitary group $U(n) = U(n,0)$ of *The Unitary and Symplectic Groups*.

## The Hermitian Form and the Unitary Group

### The Indefinite Hermitian Form

**Definition.** The **Hermitian form of signature** $(p,q)$ on $V = \mathbb{C}^{p+q}$ is

$$
h(z, w) = \sum_{i=1}^{p} \overline{z_i}\, w_i - \sum_{j=p+1}^{p+q} \overline{z_j}\, w_j,
$$

conjugate-linear in the first argument, linear in the second, and Hermitian; its matrix is $J = \operatorname{diag}(I_p, -I_q)$ and its **signature** is the pair of the dimensions of a maximal positive-definite and a maximal negative-definite subspace, $p$ and $q$. The form is non-degenerate of index $q$, and over $\mathbb{R}$ the same construction with the identity conjugation gives the quadratic form $Q$ of signature $(p,q)$.

**Proposition.** The form $h$ is non-degenerate, the maximal $h$-negative subspaces have dimension $q$, the maximal positive ones dimension $p$, and the orthogonal complement of a negative subspace is positive and of dimension $p$. The group of linear isomorphisms preserving $h$ is

$$
U(p,q) = \{g \in GL_{p+q}(\mathbb{C}) : h(gz, gw) = h(z, w) \text{ for all } z, w\} = \{g : g^{\dagger} J g = J\},
$$

a real Lie group of dimension $(p+q)^2$; the **special unitary group** $SU(p,q)$ is the kernel of the determinant, and the centre of $U(p,q)$ is the group of scalars $\lambda I$ with $\lvert\lambda\rvert = 1$.

**Proof.** Non-degeneracy is $\det J = (-1)^q \neq 0$; the dimension claims are Sylvester's law of inertia, *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*. The matrix form of the isometry equation is $g^{\dagger}Jg = J$, which is a real algebraic condition cutting out a closed subgroup of $GL_{p+q}(\mathbb{C})$; its dimension is computed from the Lie algebra below. The determinant has modulus one on $U(p,q)$ by the same computation as in the compact case, and the centre consists of the scalars commuting with $J$.

### The Compact Subgroup

**Definition.** The **standard maximal compact subgroup** of $U(p,q)$ is

$$
K = U(p)\times U(q) = \left\{\begin{pmatrix} A & 0 \\ 0 & D\end{pmatrix} : A \in U(p),\ D \in U(q)\right\},
$$

the isometries preserving the standard positive subspace $\mathbb{C}^p\oplus 0$ and its negative complement.

**Proposition.** $K$ is a maximal compact subgroup of $U(p,q)$, the quotient $U(p,q)/K$ is connected and simply connected, and the **Cartan decomposition** at the level of Lie algebras is

$$
\mathfrak{u}(p,q) = \mathfrak{k}\oplus\mathfrak{p}, \qquad \mathfrak{k} = \mathfrak{u}(p)\oplus\mathfrak{u}(q), \qquad \mathfrak{p} = \left\{\begin{pmatrix} 0 & Z \\ -Z^{\dagger} & 0\end{pmatrix} : Z \in \mathbb{C}^{p\times q}\right\},
$$

with $[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k}$, $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$ and $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}$; $\mathfrak{p}$ is real-isomorphic to $\mathbb{C}^{pq}$ and $\dim_{\mathbb{R}} U(p,q)/K = 2pq$.

**Proof.** The subgroup $K$ is compact, being a product of unitary groups, and maximal because any compact subgroup has a fixed vector, hence a fixed negative subspace, and can therefore be conjugated into $K$; the quotient is connected because $U(p,q)$ is, and simply connected because $K$ is connected and the pair is the noncompact dual of the compact pair computed in *Riemannian Symmetric Spaces and the Involution*. The bracket relations are the standard ones of a symmetric pair, read off the block decomposition; the identification of $\mathfrak{p}$ with $\mathbb{C}^{pq}$ is the entry $Z$.

## The Involution and the Symmetric Space

### The Cartan Involution

**Proposition.** The map

$$
\theta : U(p,q) \longrightarrow U(p,q), \qquad \theta(g) = J\,g\,J^{-1} = J\,g\,J,
$$

is an involutive automorphism of $U(p,q)$, equal to the inverse-conjugate-transpose, $\theta(g) = (g^{\dagger})^{-1}$; its fixed subgroup is $K = U(p)\times U(q)$, and its differential at the identity is $+1$ on $\mathfrak{k}$ and $-1$ on $\mathfrak{p}$.

**Proof.** From $g^{\dagger}Jg = J$ one gets $g^{\dagger} = Jg^{-1}J^{-1}$, whence $(g^{\dagger})^{-1} = JgJ^{-1} = JgJ$ since $J^{-1} = J$; the inner automorphism by $J$ is an automorphism, of order two because $J^2 = I$, and it preserves $U(p,q)$ because $J$ commutes with the defining relation. Its fixed points are the matrices commuting with $J$, which are exactly the block-diagonal ones, and the differential acts by conjugation on the Lie algebra, giving $+1$ on the blocks that commute with $J$ and $-1$ on those that anticommute.

**Remark.** The involution is the **Cartan involution** of the pair $(U(p,q), K)$, and $\theta$ is the differential of the geodesic symmetry of the symmetric space at the base point, *Riemannian Symmetric Spaces and the Involution*. It is an involution on the **elements** of the group, in the sense of the group `- * Theory` of this category; the adjoint of an operator it defines is not taken here.

### The Symmetric Space as a Manifold of Subspaces

**Definition.** The **Hermitian symmetric space** of the unitary group is the homogeneous space

$$
X = U(p,q)/K = U(p,q)/(U(p)\times U(q)),
$$

with base point $o = eK$, and the **geodesic symmetry** at $o$ is $s_o(gK) = \theta(g)K$.

**Proposition.** The space $X$ is the manifold of $h$-negative subspaces of dimension $q$,

$$
X \cong \{W \leq V : \dim W = q,\ h|_W < 0\},
$$

by $gK \mapsto gW_0$ with $W_0 = 0\oplus\mathbb{C}^q$; it is a symmetric space of noncompact type, simply connected, of dimension $2pq$ and rank $\min(p,q)$; the symmetry $s_o$ is an involutive isometry with the isolated fixed point $o$, and the symmetries at the other points are its conjugates, so $X$ is a symmetric space in the sense of *Riemannian Symmetric Spaces and the Involution*.

**Proof.** The stabiliser of $W_0$ is $K$, so the orbit of $W_0$ is $U(p,q)/K$; the map is injective because $U(p,q)$ acts transitively on the negative $q$-subspaces, and surjective by the same transitivity, which is Witt's theorem in the Hermitian case. The symmetry statement is that $\theta$ is an involutive automorphism with fixed subgroup $K$, the general construction of a symmetric space from a symmetric pair; the rank is $\min(p,q)$ because a maximal abelian subspace of $\mathfrak{p}$ is parametrised by the diagonal of a $p\times q$ matrix, whose rank is at most $\min(p,q)$.

### The Complex Structure

**Proposition.** The space $X$ carries a $U(p,q)$-invariant complex structure $J_o$ on the tangent space $T_oX = \mathfrak{p}$ given by the multiplication by $i$ on the entry $Z \in \mathbb{C}^{pq}$, and it extends to an integrable invariant almost complex structure on $X$; the geodesic symmetry $s_o$ is complex-antisymmetric, and the involution $\theta$ is the "complex" symmetry of the Hermitian symmetric space.

**Proof.** The isotropy representation of $K$ on $\mathfrak{p}$ is the action $Z \mapsto AZD^{-1}$, which is complex-linear, so the multiplication by $i$ commutes with the isotropy and defines an invariant almost complex structure; the integrability is the vanishing of the Nijenhuis tensor, which holds because $\mathfrak{p}$ is a complex vector space and the structure comes from a complex Lie algebra grading, the general theory of Hermitian symmetric spaces in *Riemannian Symmetric Spaces and the Involution* and *Kähler Geometry*. The antisymmetry of $s_o$ is the statement that $\theta$ acts as $-1$ on $\mathfrak{p}$, which anticommutes with the complex structure of the noncompact dual.

**Remark.** The complex structure is what distinguishes this symmetric space from the orthogonal one: the tangent space $\mathfrak{p}$ is a complex vector space and the geodesic symmetry is complex-antisymmetric, so $X$ is a Hermitian symmetric space, later in this Part.

## The Bounded Realisation

### The Matrix Unit Ball

**Definition.** The **matrix unit ball** of type $(p,q)$ is the bounded domain

$$
D = \bigl\{Z \in \mathbb{C}^{p\times q} : I_q - Z^{\dagger}Z > 0\bigr\},
$$

the set of $p\times q$ matrices $Z$ whose Hermitian square satisfies $Z^{\dagger}Z < I_q$; it is an open bounded convex domain in $\mathbb{C}^{pq}$, the **generalised unit disc**.

**Proposition.** The domain $D$ is bounded, open and convex; it contains $0$ and its boundary is $\{Z : Z^{\dagger}Z = I_q\}$ together with a smooth part; for $p = 1$ it is the unit ball of $\mathbb{C}^q$.

**Proof.** The condition $Z^{\dagger}Z < I_q$ is open because the eigenvalues of $Z^{\dagger}Z$ are continuous in $Z$; boundedness is $\lVert Z\rVert^2 = \lambda_{\max}(Z^{\dagger}Z) < 1$; convexity is the concavity of the map $Z \mapsto I_q - Z^{\dagger}Z$ on the Hermitian matrices, a standard fact of matrix analysis. For $p = 1$ the matrix $Z^{\dagger}Z$ is the scalar $\lvert z\rvert^2$ and the condition is $\lvert z\rvert < 1$.

### The Harish-Chandra Embedding

**Theorem (bounded realisation).** The map

$$
\Phi : U(p,q)/K \longrightarrow D, \qquad gK \longmapsto Z = (g \cdot 0),
$$

where $g = \begin{pmatrix} A & B \\ C & D\end{pmatrix}$ acts by the fractional linear transformation

$$
Z \longmapsto (AZ + B)(CZ + D)^{-1},
$$

is a $U(p,q)$-equivariant bijection of the symmetric space onto the matrix unit ball; it is the **Harish-Chandra embedding** of the symmetric space as a bounded domain, and $U(p,q)$ acts on $D$ by biholomorphisms.

**Proof.** The fractional linear transformation is defined on the set where $CZ + D$ is invertible, which contains $D$ because $I_q - Z^{\dagger}Z > 0$ implies the invertibility of $CZ + D$ for $g \in U(p,q)$, by the identity $h(g\cdot z, g\cdot w) = h(z, w)$ read at $Z$; the map decreases $\lVert Z\rVert$ or preserves the ball, so $D$ is stable. It is a bijection onto $D$ because the stabiliser of $0$ in $U(p,q)$ is exactly the block-diagonal $K$ — the condition $\theta$-invariance at $Z = 0$ forces the off-diagonal block $B$ to vanish — so the orbit of $0$ is a copy of $U(p,q)/K$ inside $D$, and it exhausts $D$ because every matrix $Z$ with $Z^{\dagger}Z < I_q$ is reached by a fractional linear transformation of $U(p,q)$. This is the Harish-Chandra embedding of *Riemannian Symmetric Spaces and the Involution*, quoted.

**Remark.** The realisation is the geometric reason the symmetric space of a unitary group is special: it is a bounded domain, its group acts by biholomorphisms, and the Bergman metric, the Bergman kernel and the boundary behaviour of the domain are the subject of *Hermitian Symmetric Spaces and the Bergman Metric* and *The Bergman Operator*, below this Part and written in parallel. The embedding also exhibits the symmetric space as the **bounded symmetric domain** of the Hermitian case.

## Worked Cases

**Example (the Poincaré disc).** Let $p = q = 1$. Then $U(1,1)/(U(1)\times U(1))$ is the unit disc $\{z \in \mathbb{C} : \lvert z\rvert < 1\}$, the geodesic symmetry is $z \mapsto -z$ at the origin, the involution is $\theta(g) = JgJ$, and the group $SU(1,1)$ is isomorphic to $SL(2, \mathbb{R})$ and acts by Möbius transformations. The example is the smallest Hermitian symmetric space and the one that shows the bounded realisation directly.

**Example (complex hyperbolic space).** Let $p = 1$, $q = n$. Then $X = U(1,n)/(U(1)\times U(n))$ is the unit ball $B^n \subseteq \mathbb{C}^n$, the **complex hyperbolic space** $\mathbb{C}H^n$ of complex dimension $n$, with the group $U(1,n)$ acting by fractional linear transformations and the boundary the sphere $S^{2n-1}$. The Hermitian symmetric space has rank one, its geodesic symmetry is complex-antisymmetric, and it is the complex counterpart of the real hyperbolic space of *Curvature and Geodesics*.

**Example (the Siegel disc).** Let $p = q = n$. Then $X = U(n,n)/(U(n)\times U(n))$ is the matrix unit ball $D = \{Z \in \mathbb{C}^{n\times n} : Z^{\dagger}Z < I\}$, of rank $n$ and dimension $2n^2$, the **Siegel disc**. The space is the bounded realisation of the symmetric space of the unitary group of a form of split signature, and its boundary carries the Shilov boundary, the unitary group $U(n)$ embedded as the set $Z^{\dagger}Z = I$, which is named in *Hermitian Symmetric Spaces and the Bergman Metric*, below this Part.

**Example (the compact case).** Let $q = 0$. Then $U(n,0) = U(n)$, $K = U(n)$, and the quotient is a point: the compact form of a Hermitian symmetric space of the unitary family has no noncompact factor, the group already being compact, and the symmetric space is degenerate. The noncompact case $q \geq 1$ is the one that carries the bounded domain and the invariant metric, and it is the case of the article.

## Summary

The unitary group of the Hermitian form $h(z,w) = \sum_{i\le p}\overline{z_i}w_i - \sum_{i>p}\overline{z_i}w_i$ of signature $(p,q)$ is $U(p,q) = \{g : g^{\dagger}Jg = J\}$ with $J = \operatorname{diag}(I_p,-I_q)$; it is a real Lie group of dimension $(p+q)^2$ with special subgroup $SU(p,q)$ and standard maximal compact subgroup $K = U(p)\times U(q)$. The map $\theta(g) = JgJ^{-1} = (g^{\dagger})^{-1}$ is an involutive automorphism with fixed subgroup $K$ and differential $+1$ on $\mathfrak{k} = \mathfrak{u}(p)\oplus\mathfrak{u}(q)$ and $-1$ on $\mathfrak{p}\cong\mathbb{C}^{pq}$; the quotient $X = U(p,q)/K$ is the symmetric space of the negative $q$-subspaces of $V$, a simply connected symmetric space of noncompact type, dimension $2pq$ and rank $\min(p,q)$, and the isotropy representation makes its tangent space a complex vector space, so $X$ is a Hermitian symmetric space with complex-antisymmetric geodesic symmetry. The Harish-Chandra embedding realises $X$ as the matrix unit ball $D = \{Z \in \mathbb{C}^{p\times q} : Z^{\dagger}Z < I_q\}$, a bounded convex domain in $\mathbb{C}^{pq}$ on which $U(p,q)$ acts by fractional linear transformations; the Poincaré disc, the complex hyperbolic space and the Siegel disc are the cases $(1,1)$, $(1,n)$ and $(n,n)$. The invariant Kähler metric, the Bergman kernel and the boundary theory belong to *Hermitian Symmetric Spaces and the Bergman Metric*, below this Part. The involution here is on the elements of the group; no adjoint is taken.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $p, q$ | the signature of the Hermitian form |
| $h$ | the Hermitian form of signature $(p,q)$ on $\mathbb{C}^{p+q}$ |
| $J = \operatorname{diag}(I_p,-I_q)$ | the matrix of $h$; the involution defining the group |
| $U(p,q)$ | the unitary group of $h$, $\{g : g^{\dagger}Jg = J\}$ |
| $SU(p,q)$ | the special unitary group, the kernel of the determinant |
| $K = U(p)\times U(q)$ | the standard maximal compact subgroup; the block-diagonal matrices |
| $\theta(g) = JgJ^{-1} = (g^{\dagger})^{-1}$ | the Cartan involution of the pair |
| $\mathfrak{k}\oplus\mathfrak{p}$ | the Cartan decomposition; $\mathfrak{p}\cong\mathbb{C}^{pq}$ the isotropy complement |
| $X = U(p,q)/K$ | the Hermitian symmetric space; the negative $q$-subspaces of $V$ |
| $s_o(gK) = \theta(g)K$ | the geodesic symmetry at the base point |
| $D = \{Z : Z^{\dagger}Z < I_q\}$ | the matrix unit ball; the bounded realisation |
| $\Phi$ | the Harish-Chandra embedding $X \to D$ |
| $Z \mapsto (AZ+B)(CZ+D)^{-1}$ | the fractional linear action of $U(p,q)$ on $D$ |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the symmetric space of a unitary group, the Cartan involution, the rank and the Harish-Chandra embedding.
- Ottmar Loos, *Bounded Symmetric Domains and Jordan Pairs* (University of California, Irvine, 1977), for the bounded realisation, the matrix unit ball and the Jordan-theoretic classification of the domains.
- Audrey Terras, *Harmonic Analysis on Symmetric Spaces and Applications II* (Springer, 1988), for the Siegel disc and the bounded domains of the classical groups, with the invariant metrics.
- Elie Cartan, "Sur les domaines bornés homogènes de l'espace de $n$ variables complexes", *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg* **11** (1935), 116–162, for the original bounded-domain realisation of the Hermitian symmetric spaces.
- Ichiro Satake, *Algebraic Structures of Symmetric Domains* (Princeton University Press, 1980), for the Hermitian symmetric domains and their realisation.
