
# __Unitary Groups and Their Involution__

## Introduction

A Hermitian form on a complex space is diagonalisable, and the diagonal form records only its **signature**: the pair $(n,m)$ of the dimensions of a maximal positive-definite and a maximal negative-definite subspace. The unitary group $U(V,h)$ of the form therefore contains, for a form of index $m$, a largest compact subgroup $K$ — the isometries that preserve the definite part — and the **Cartan involution** of the pair is the involutive automorphism whose fixed subgroup is $K$. It is the involution of the unitary group as a structure, and the quotient $U(V,h)/K$ is the symmetric space it defines. The involution is not a property of the abstract group alone: it is determined by the form, up to conjugation, and the signature is exactly the invariant that classifies it.

The article treats the unitary groups of Hermitian forms of all indices, the Cartan involution and its fixed subgroup, the symmetric space they define, and the classification of the involution by the signature. It is the general form of *The Unitary Group and the Hermitian Symmetric Space*, the previous article, which treated the standard form and its bounded realisation; the bounded domain, which is special to the indefinite case, is not repeated. The unitary group of a Hermitian form, its determinant and its special subgroup are *The Unitary and Symplectic Groups*; the Hermitian forms, their diagonalisation and their classification are *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*; the symmetric space, the symmetric pair, the Cartan involution and the rank are *Riemannian Symmetric Spaces and the Involution*; the homogeneous space $G/K$ and the isotropy representation are *Transformation Groups*; the Lie algebra is *The Orthogonal Lie Algebra* and *Lie Groups*. The invariant metric and the Hermitian geometry of the quotient are *Hermitian Symmetric Spaces and the Bergman Metric*, below this Part, named and not used. The article reads the involution on the **elements** of the group; the **adjoint** of an operator and the `*`-structures it defines are the group `- * Operator Theory`.

The article has four sections: the Hermitian space and its unitary group; the involution and its fixed subgroup; the symmetric space; and the worked cases. Throughout, $V$ is a finite-dimensional complex space with a non-degenerate Hermitian form $h$ of index $m$ and signature $(n,m)$, $n+m = \dim V$; the form is real-valued on $V$ when the field is $\mathbb{R}$ and the reference to the Hermitian case is dropped.

## The Hermitian Space and Its Unitary Group

### The Hermitian Adjoint

**Definition.** The **Hermitian adjoint** of a linear map $T \in \operatorname{End}(V)$ with respect to $h$ is the unique map $T^{*}$ with

$$
h(Tu, v) = h(u, T^{*}v) \quad \text{for all } u, v \in V;
$$

the existence and uniqueness are the non-degeneracy of $h$, identifying $V$ with its conjugate dual.

**Proposition.** The adjoint satisfies $(ST)^{*} = T^{*}S^{*}$, $(T^{*})^{*} = T$, $(\lambda T)^{*} = \overline{\lambda}\,T^{*}$ and $\operatorname{id}^{*} = \operatorname{id}$; it is a conjugate-linear involution of the endomorphism algebra, and for the standard form with matrix $J$ it is $T^{*} = J^{-1}T^{\dagger}J$.

**Proof.** The identities are the defining relation applied twice and the conjugate-linearity of $h$ in the first argument; the matrix formula is the change of the inner product to the standard one.

### The Unitary Group

**Definition.** The **unitary group** of $(V,h)$ is the group of isometries

$$
U(V,h) = \{T \in GL(V) : h(Tu, Tv) = h(u, v)\} = \{T : T^{*}T = \operatorname{id}\},
$$

and it is a real Lie group; the **special unitary group** $SU(V,h)$ is the kernel of the determinant.

**Proposition.** A Hermitian form is diagonalisable: there is a basis in which $h$ has the matrix $J = \operatorname{diag}(I_n, -I_m)$, where $(n,m)$ is the signature; hence every unitary group is conjugate to the model group

$$
U(n,m) = \{g : g^{\dagger}Jg = J\},
$$

and the isomorphism class depends only on the signature. For $m = 0$ the group is the compact unitary group $U(n)$; for $m \geq 1$ it is noncompact.

**Proof.** Diagonalisability is Sylvester's law of inertia, *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*; the model form is the diagonal one. Compactness for $m=0$ is that $U(n)$ is closed and bounded; noncompactness for $m \geq 1$ is exhibited below by an unbounded one-parameter subgroup.

## The Involution and Its Fixed Subgroup

### The Choice of a Definite Subspace

**Definition.** A **definite decomposition** of $(V,h)$ is an orthogonal decomposition $V = V_+\oplus V_-$ with $h$ positive definite on $V_+$ and negative definite on $V_-$; the signature is $(n,m)$ with $\dim V_+ = n$ and $\dim V_- = m$.

**Proposition.** Definite decompositions exist, they are permuted transitively by $U(V,h)$, and the **stabiliser of a definite decomposition** is the compact subgroup

$$
K = U(V_+)\times U(V_-) = \{T \in U(V,h) : T(V_+) = V_+,\ T(V_-) = V_-\},
$$

a maximal compact subgroup of $U(V,h)$; maximal compact subgroups are conjugate.

**Proof.** Existence is the diagonalisation; transitivity is Witt's theorem, which extends an isometry of a subspace to an isometry of the whole form. The stabiliser of the decomposition preserves each of $V_{\pm}$, hence is a product of unitary groups of the definite parts, hence compact; it is maximal because any compact subgroup has a fixed vector in $V$ and iterating fixes a maximal positive subspace and a maximal negative one, so it can be conjugated into $K$. That all maximal compact subgroups are conjugate is the standard theorem for a real Lie group with finitely many components.

### The Cartan Involution

**Theorem (the involution).** Let $K$ be the stabiliser of a definite decomposition. Then there is a unique involutive automorphism $\theta$ of $U(V,h)$ with

$$
U(V,h)^{\theta} = K, \qquad \theta(T) = T \text{ on } K, \qquad d\theta = -1 \text{ on } \mathfrak{n},
$$

the **Cartan involution** of the pair; for the standard form it is $\theta(g) = JgJ^{-1}$. It is defined up to conjugacy, and two Cartan involutions are conjugate by an element of $U(V,h)$, through the conjugacy of the maximal compact subgroups.

**Proof.** In the model, the conjugation by $J$ is the inner automorphism $g \mapsto JgJ^{-1}$, an involution because $J^2 = I$, with fixed subgroup the block-diagonal matrices $K = U(n)\times U(m)$ and differential $+1$ on $\mathfrak{k}$ and $-1$ on $\mathfrak{n}$; a general form is conjugated to the model by the diagonalisation, and conjugating the involution by the change of basis gives an involution of $U(V,h)$ with the same properties. Uniqueness up to conjugacy follows from the conjugacy of the maximal compact subgroups.

**Remark.** The involution is on the **elements** of the group, in the sense of the group `- * Theory`: it is an automorphism of order two, its fixed subgroup is the compact $K$, and its differential splits the Lie algebra into the $+1$-eigenspace $\mathfrak{k}$ and the $-1$-eigenspace $\mathfrak{n}$. It is the differential of the **geodesic symmetry** of the symmetric space at the base point, *Riemannian Symmetric Spaces and the Involution*. The **adjoint** of an operator on $V$ is a different involution, on the operators, and is not taken here.

### The Fixed Subgroup and the Noncompactness

**Proposition.** The fixed subgroup $K$ is a maximal compact subgroup of $U(V,h)$; the quotient $U(V,h)/K$ is a symmetric space of noncompact type when $m \geq 1$ and a point when $m = 0$; the Cartan decomposition

$$
\mathfrak{u}(V,h) = \mathfrak{k}\oplus\mathfrak{n}, \qquad
\mathfrak{n} = \{X \in \mathfrak{u}(V,h) : \theta(X) = -X\},
$$

has $[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k}$, $[\mathfrak{k},\mathfrak{n}]\subseteq\mathfrak{n}$, $[\mathfrak{n},\mathfrak{n}]\subseteq\mathfrak{k}$, and $\mathfrak{n}$ is a real vector space of dimension $2pq$.

**Proof.** The bracket relations are the statements that $\theta$ is an automorphism and $\mathfrak{k}$ and $\mathfrak{n}$ are its eigenspaces; $\mathfrak{k}$ is compact because it is the Lie algebra of the compact group $K$. The dimension of $\mathfrak{n}$ is the dimension of the off-diagonal block in the model, $2pq$. The noncompactness for $m\geq1$ is the one-parameter subgroup $\exp(tX)$ with $X \in \mathfrak{n}$ a nonzero diagonal entry, which is unbounded.

## The Symmetric Space

### The Quotient

**Definition.** The **symmetric space** of the unitary group is the homogeneous space

$$
X = U(V,h)/K,
$$

with base point $o = eK$ and tangent space $T_oX = \mathfrak{n}$; the **geodesic symmetry** at $o$ is $s_o(gK) = \theta(g)K$.

**Proposition.** The space $X$ is diffeomorphic to the manifold of $h$-negative subspaces of dimension $m$,

$$
X \cong \{W \leq V : \dim W = m,\ h|_W < 0\},
$$

via $gK \mapsto gV_-$; it is connected, simply connected, of dimension $2pq$ and rank $\min(n,m)$, and it is a symmetric space of noncompact type in the sense of *Riemannian Symmetric Spaces and the Involution*.

**Proof.** The stabiliser of $V_-$ is $K$, so the orbit is the quotient; the map is bijective by the transitivity of $U(V,h)$ on the negative $m$-subspaces, which is Witt's theorem. The rank is the maximal dimension of an abelian subspace of $\mathfrak{n}$, which for the model is $\min(n,m)$, achieved by the diagonal entries of the off-diagonal block. The space is simply connected because $K$ is connected and the pair is the noncompact dual, *Riemannian Symmetric Spaces and the Involution*.

### The Classification by the Signature

**Theorem.** The Cartan involution of $U(V,h)$, up to conjugacy, is determined by the signature $(n,m)$ alone, and the conjugacy classes of the involutions with compact fixed subgroup of the unitary groups correspond to the signatures; the family of symmetric spaces obtained is

$$
X_{n,m} = U(n,m)/(U(n)\times U(m)), \qquad 1 \leq m \leq n,\ \ n+m = \dim V,
$$

with $X_{n,m} \cong X_{m,n}$ under the exchange of the form with its negative.

**Proof.** By the diagonalisation, two forms of the same signature are isometric, so their unitary groups are conjugate in $GL(V)$ and their Cartan involutions are conjugate; conversely the signature is recovered from the dimensions of the two definite parts of the decomposition fixed by the involution, which is the rank and the dimension of the space. The symmetry $X_{n,m}\cong X_{m,n}$ is the interchange $h \leftrightarrow -h$.

**Remark.** The signature is the geometric datum, and it satisfies the boundary test of the part: a different Hermitian form of the same dimension gives a different symmetric space and a different involution. The compact case $m=0$ has $X$ a point and the involution the identity; the split case $n=m$ has maximal rank and is the case of the Siegel disc of the previous article.

## Worked Cases

**Example (the compact unitary group).** Let $m = 0$. Then $U(V,h) = U(n)$ is compact, $K = U(n)$ and $X$ is a point; the Cartan involution is the identity (up to conjugacy there is no noncompact direction), and the involution is trivial. The example shows that the involution is the identity exactly in the compact case.

**Example (the indefinite unitary group).** Let $(n,m) = (1,n-1)$. Then $U(1,n-1)$ has the symmetric space $X = U(1,n-1)/(U(1)\times U(n-1))$ of rank one and dimension $2(n-1)$, the complex hyperbolic space; the involution is $\theta(g) = JgJ^{-1}$ with $J = \operatorname{diag}(1,-I_{n-1})$, the fixed subgroup is $U(1)\times U(n-1)$, and the geodesic symmetry is complex-antisymmetric. The previous article's bounded realisation identifies $X$ with the unit ball of $\mathbb{C}^{n-1}$.

**Example (the split signature).** Let $n = m = n$. Then $U(n,n)$ has the symmetric space $U(n,n)/(U(n)\times U(n))$ of rank $n$ and dimension $2n^2$, the Siegel disc in the bounded realisation; the involution $\theta(g) = JgJ^{-1}$ with $J = \operatorname{diag}(I_n,-I_n)$ is conjugation by $J$, and the maximal abelian subspace of $\mathfrak{n}$ is the diagonal, of dimension $n$. The signature $(n,n)$ is the largest rank among the unitary symmetric spaces of dimension $2n^2$.

**Example (the real form).** Let the field be $\mathbb{R}$ with the identity involution; the Hermitian form is then quadratic and the unitary group is the orthogonal group of signature $(n,m)$, $O(n,m)$. The involution $\theta(g) = JgJ^{-1}$ is again the Cartan involution, $\mathfrak{n}$ has dimension $pq$, and the symmetric space is $O(n,m)/(O(n)\times O(m))$. This is the model of *The Orthogonal Group and the Involutive Automorphism*, the next article, and shows that the construction is not special to the complex case.

## Summary

The unitary group $U(V,h)$ of a Hermitian form of signature $(n,m)$ is the group of isometries $\{T : T^{*}T = \operatorname{id}\}$ of the Hermitian adjoint; a Hermitian form is diagonalisable, so the group is conjugate to the model $U(n,m) = \{g : g^{\dagger}Jg = J\}$ and depends only on the signature. A definite decomposition $V = V_+\oplus V_-$ has the stabiliser $K = U(V_+)\times U(V_-)$, a maximal compact subgroup, and the pair has a Cartan involution $\theta$, unique up to conjugacy, with fixed subgroup $K$ and differential $+1$ on $\mathfrak{k}$ and $-1$ on $\mathfrak{n}$; for the model it is $\theta(g) = JgJ^{-1}$. The quotient $U(V,h)/K$ is the symmetric space of the negative $m$-subspaces, of dimension $2pq$ and rank $\min(n,m)$, with geodesic symmetry $s_o(gK) = \theta(g)K$; it is a point exactly in the compact case $m = 0$. The involution up to conjugacy is classified by the signature, and the unitary family of symmetric spaces is $U(n,m)/(U(n)\times U(m))$ with $X_{n,m}\cong X_{m,n}$. The invariant metric and the Hermitian geometry are *Hermitian Symmetric Spaces and the Bergman Metric*, below this Part. The involution here is on the elements of the group; the adjoint of an operator is the group `- * Operator Theory`.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $h$, $(n,m)$ | Hermitian form and its signature |
| $T^{*}$ | the Hermitian adjoint of $T$, $h(Tu,v) = h(u,T^{*}v)$ |
| $U(V,h)$, $SU(V,h)$ | unitary and special unitary groups of $(V,h)$ |
| $J = \operatorname{diag}(I_n,-I_m)$ | the matrix of the diagonalised form |
| $U(n,m)$ | the model unitary group, $\{g : g^{\dagger}Jg = J\}$ |
| $V = V_+\oplus V_-$ | a definite decomposition |
| $K = U(V_+)\times U(V_-)$ | the maximal compact subgroup; the fixed subgroup |
| $\theta$ | the Cartan involution; $\theta(g) = JgJ^{-1}$ in the model |
| $\mathfrak{k}\oplus\mathfrak{n}$ | the Cartan decomposition; eigen-$\pm1$ spaces of $d\theta$ |
| $X = U(V,h)/K$ | the symmetric space; the negative $m$-subspaces |
| $s_o(gK) = \theta(g)K$ | the geodesic symmetry at the base point |
| $X_{n,m}$ | $U(n,m)/(U(n)\times U(m))$, classified by the signature |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the Cartan involution, the Cartan decomposition and the symmetric space of a real Lie group.
- Sigurdur Helgason, *Groups and Geometric Analysis* (Academic Press, 1984), for the unitary groups of Hermitian forms and their symmetric spaces.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, second edition, 2002), for the classification of the symmetric spaces of the classical groups by the signature.
- Joseph A. Wolf, *Spaces of Constant Curvature* (American Mathematical Society, sixth edition, 2011), for the symmetric spaces of the unitary family and their rank.
- Ichiro Satake, *Algebraic Structures of Symmetric Domains* (Princeton University Press, 1980), for the unitary symmetric domains and their classification.
