# __The Cartan Decomposition and the Symmetric Space of $M_4(\mathbb{C})$__

## Introduction

The unit group $GL_4(\mathbb{C})$ is a real Lie group of dimension $32$. Its **Cartan involution** is

$$
\Theta(g)=(g^{*})^{-1},
$$

whose fixed subgroup is the unitary group $U(4)$. At the level of the Lie algebra $\mathfrak{gl}_4(\mathbb{C})$, regarded as a real Lie algebra, the involution is

$$
\theta(X)=-X^{*},
$$

with fixed algebra $\mathfrak{u}(4)$ and $(-1)$-eigenspace the Hermitian matrices. The **Cartan decomposition** is the direct sum

$$
\mathfrak{gl}_4(\mathbb{C})=\mathfrak{u}(4)\oplus\operatorname{Herm}_4,
$$

of real dimensions $16+16=32$, and at the group level it is the polar decomposition

$$
GL_4(\mathbb{C})=U(4)\cdot\operatorname{Herm}_4^{++},
$$

where $\operatorname{Herm}_4^{++}$ is the open cone of positive definite Hermitian matrices. The quotient

$$
GL_4(\mathbb{C})/U(4)\cong\operatorname{Herm}_4^{++}
$$

is a Riemannian symmetric space of non-compact type, of real dimension $16$.

This article states the involution, the decomposition, the symmetric space, its metric and geodesics, and the relation to the compact and indefinite cases. The polar decomposition of a single element is *The Polar Decomposition of $M_4(\mathbb{C})$*; the Hermitian structure and the unitary group are *The Involution and the Hermitian Structure of $M_4(\mathbb{C})$*; the indefinite case is *The Krein Isometry Group and Its Cartan Decomposition*.

## The Cartan Involution

**Definition.** On $GL_4(\mathbb{C})$ the Cartan involution is $\Theta(g)=(g^{*})^{-1}$; on $\mathfrak{gl}_4(\mathbb{C})$ it is $\theta(X)=-X^{*}$.

**Proposition.** $\Theta$ is an involutive automorphism of the group, $\theta$ is an involutive automorphism of the real Lie algebra, and the two are compatible with the exponential.

**Proof.** For the group, $\Theta(gh)=((gh)^{*})^{-1}=(h^{*}g^{*})^{-1}=(g^{*})^{-1}(h^{*})^{-1}=\Theta(g)\Theta(h)$, and $\Theta^{2}(g)=((g^{*})^{-1})^{*}{}^{-1}=g$. For the algebra, $\theta([X,Y])=-[X,Y]^{*}=-[Y^{*},X^{*}]=[-X^{*},-Y^{*}]=[\theta X,\theta Y]$, and $\theta^{2}(X)=-(-X^{*})^{*}=X$. The compatibility is $\Theta(e^{X})=e^{\theta X}$, because $(e^{X})^{*}=e^{X^{*}}$.

**The fixed subgroup.** $\Theta(g)=g$ means $(g^{*})^{-1}=g$, that is, $g^{*}g=I$: the fixed subgroup is $U(4)$.

**The fixed algebra.** $\theta(X)=X$ means $-X^{*}=X$, that is, $X^{*}=-X$: the fixed algebra is $\mathfrak{u}(4)$, of real dimension $16$. The $(-1)$-eigenspace is the space of Hermitian matrices, $\operatorname{Herm}_4=\{X:X^{*}=X\}$, also of real dimension $16$.

**The decomposition.** Every $X\in\mathfrak{gl}_4$ splits uniquely as

$$
X=\underbrace{\tfrac12(X-X^{*})}_{\text{skew-Hermitian}}+\underbrace{\tfrac12(X+X^{*})}_{\text{Hermitian}},
$$

so

$$
\mathfrak{gl}_4(\mathbb{C})=\mathfrak{u}(4)\oplus\operatorname{Herm}_4
$$

as real vector spaces. The summands are the eigenspaces of $\theta$ for the eigenvalues $+1$ and $-1$.

**The bracket relations.** The decomposition is a **Cartan decomposition**:

$$
[\mathfrak{u},\mathfrak{u}]\subseteq\mathfrak{u},\qquad
[\mathfrak{u},\mathfrak{p}]\subseteq\mathfrak{p},\qquad
[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{u},
$$

with $\mathfrak{p}=\operatorname{Herm}_4$. The first is closure of the unitary algebra; the second is the statement that the commutator of a skew-Hermitian and a Hermitian matrix is Hermitian; the third is the statement that the commutator of two Hermitian matrices is skew-Hermitian.

## The Symmetric Space

**Theorem.** The map

$$
GL_4(\mathbb{C})/U(4)\longrightarrow\operatorname{Herm}_4^{++},\qquad
gU(4)\longmapsto (g^{*}g)^{1/2},
$$

is a diffeomorphism onto the open cone of positive definite Hermitian matrices. The cone is a symmetric space of non-compact type, of real dimension $16$.

**Proof.** Every $g\in GL_4$ has a unique polar decomposition $g=UP$ with $U\in U(4)$ and $P$ positive definite Hermitian; the map is well defined and bijective, with inverse $P\mapsto P^{1/2}U(4)$. The cone is open in the real vector space $\operatorname{Herm}_4$, of dimension $16$, and it is a symmetric space: the geodesic symmetry at $P$ is $Q\mapsto PQ^{-1}P$, an involutive isometry. The space is of non-compact type because its identity component is the quotient of the non-compact group $GL_4$ by the maximal compact $U(4)$.

**The group action.** $GL_4$ acts on the cone by $g\cdot P=gPg^{*}$, and the action is transitive with stabiliser $U(4)$ at $P=I$. The involution at the identity is $P\mapsto P^{-1}$.

**The metric.** The trace form

$$
\langle X,Y\rangle=\operatorname{Re}\operatorname{tr}(X^{*}Y)
$$

is a positive definite real inner product on $\mathfrak{gl}_4$, invariant under $U(4)$. It restricts to a $GL_4$-invariant Riemannian metric on the cone by

$$
\langle X,Y\rangle_P=\operatorname{tr}(P^{-1}XP^{-1}Y),\qquad X,Y\in T_P\operatorname{Herm}_4=\operatorname{Herm}_4.
$$

**The geodesics.** The geodesic through $P$ with velocity $H\in\operatorname{Herm}_4$ is

$$
P(t)=P^{1/2}\exp\bigl(tP^{-1/2}HP^{-1/2}\bigr)P^{1/2}.
$$

**Proof.** At $t=0$ the curve is $P$, and its derivative is $P^{1/2}P^{-1/2}HP^{-1/2}P^{1/2}=H$. The curve is the image under the exponential map of the symmetric space, hence a geodesic; the formula is the standard one for the space of positive definite matrices.

**The curvature.** The symmetric space is of non-compact type, so its sectional curvature is non-positive. The flat directions are the directions of the diagonal torus; the negatively curved directions are the off-diagonal Hermitian directions. The space is not of constant curvature except in dimension one.

**The boundary.** The cone $\operatorname{Herm}_4^{++}$ is convex and open in $\operatorname{Herm}_4$; its boundary consists of the positive semidefinite matrices with a nontrivial kernel, stratified by rank. The strata of rank $k$ have dimensions $k^{2}+2k(4-k)$: $16$ for $k=4$ (the open cone) and $15$, $12$, $7$ on the boundary for $k=3,2,1$.

**The proof of the dimension.** A positive semidefinite matrix of rank $k$ has a $k$-dimensional image and a $k$-dimensional positive part: $k^{2}$ parameters for the positive form on the image and $2k(4-k)$ for the choice of the $k$-plane. The total is $2k(4-k)+k^{2}$; at $k=3$ this is $6+9=15$, at $k=2$ it is $8+4=12$, at $k=1$ it is $6+1=7$.

## The Compact and Indefinite Cases

**The compact dual.** The compact dual of $GL_4(\mathbb{C})/U(4)$ is the group manifold $U(4)$ itself: the complexification of the compact group $U(4)$ is $GL_4$, and the symmetric space is the non-compact dual of the group. The compact duals of the indefinite spaces are the Grassmannians: the compact dual of $SU(1,3)/S(U(1)\times U(3))=\mathbb{CH}^{3}$ is $\mathbb{CP}^{3}$, and the compact dual of $SU(2,2)/S(U(2)\times U(2))$ is $\operatorname{Gr}(2,4)$, both of real dimension $6$ and $8$.

**The indefinite case.** For the form $J=\operatorname{diag}(1,1,-1,-1)$ the same construction gives the Cartan decomposition of $\mathfrak{su}(2,2)$ and the symmetric space $SU(2,2)/S(U(2)\times U(2))$ of real dimension $8$. For $J=\operatorname{diag}(1,-1,-1,-1)$ it gives $SU(1,3)/S(U(1)\times U(3))=\mathbb{CH}^{3}$, of real dimension $6$. The three real forms $\mathfrak{su}(4)$, $\mathfrak{su}(2,2)$ and $\mathfrak{su}(1,3)$ are the compact case, the case of the form of signature $(2,2)$ and the case of signature $(1,3)$; their signatures are computed in *The Lie Algebra $\mathfrak{gl}_4(\mathbb{C})$ and $\mathfrak{sl}_4(\mathbb{C})$ of $M_4(\mathbb{C})$*.

**The Iwasawa decomposition.** $GL_4=U(4)\cdot A\cdot N$, with $A$ the positive diagonal matrices, of real dimension $4$, and $N$ the unipotent upper triangular group, of real dimension $12$; the product $AN$ has dimension $16$, the dimension of the symmetric space. The Iwasawa decomposition is the group-level counterpart of the Gram–Schmidt process. For $SL_4$ the diagonal factor has dimension $3$ and the product $AN$ has dimension $15$.

## The Place in the Category

**The involution and the form.** The Cartan involution is the real form of the $*$-structure: it uses the same conjugate transpose as the Hermitian structure of *The Involution and the Hermitian Structure of $M_4(\mathbb{C})$*, but it packages it as an involution of the real Lie algebra. The fixed algebra $\mathfrak{u}(4)$ is the compact real form of $\mathfrak{gl}_4$; the $(-1)$-eigenspace is the space of Hermitian matrices, not the traceless part.

**The polar decomposition.** The group-level Cartan decomposition is the polar decomposition $g=UP$, and the symmetric space is the space of the positive factors. The uniqueness of the polar decomposition is the uniqueness of the decomposition; the freedom on the kernel for singular elements is the boundary of the cone.

**The biquaternion comparison.** For the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ the same construction gives $GL_2(\mathbb{C})/U(2)$, of real dimension $4$, and the cone of positive definite Hermitian $2\times2$ matrices. The passage from $2$ to $4$ doubles the rank of the cone and quadruples its dimension; the Cartan involution is the same formula in both cases.

## Summary

The Cartan involution $\Theta(g)=(g^{*})^{-1}$ has fixed subgroup $U(4)$ and induces $\theta(X)=-X^{*}$ on the real Lie algebra, with fixed algebra $\mathfrak{u}(4)$ and $(-1)$-eigenspace $\operatorname{Herm}_4$. The Cartan decomposition is $\mathfrak{gl}_4=\mathfrak{u}(4)\oplus\operatorname{Herm}_4$, of real dimensions $16+16$, and at the group level the polar decomposition $GL_4=U(4)\cdot\operatorname{Herm}_4^{++}$. The quotient is the cone of positive definite Hermitian matrices, a symmetric space of non-compact type of real dimension $16$, with non-positive curvature and geodesics $P(t)=P^{1/2}\exp(tP^{-1/2}HP^{-1/2})P^{1/2}$. The compact dual is the group manifold $U(4)$; the indefinite analogues are $\mathbb{CH}^{3}$ and $\operatorname{Gr}(2,4)$, with compact duals $\mathbb{CP}^{3}$ and $\operatorname{Gr}(2,4)$.

| Quantity | Value |
|---|---|
| $\dim_\mathbb{R}GL_4(\mathbb{C})$ | $32$ |
| $\dim_\mathbb{R}U(4)$ | $16$ |
| $\dim_\mathbb{R}\operatorname{Herm}_4$ | $16$ |
| $\dim_\mathbb{R}GL_4/U(4)$ | $16$ |
| Rank of the symmetric space | $4$ |
| Compact dual of $GL_4/U(4)$ | $U(4)$ |
| Compact dual of $\mathbb{CH}^{3}$ | $\mathbb{CP}^{3}$, dimension $6$ |
| $SU(2,2)/S(U(2)\times U(2))$ | dimension $8$ |
| $SU(1,3)/S(U(1)\times U(3))$ | dimension $6$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Theta(g)=(g^{*})^{-1}$ | the Cartan involution of the group |
| $\theta(X)=-X^{*}$ | the Cartan involution of the Lie algebra |
| $\mathfrak{u}(4)$ | the skew-Hermitian matrices, the fixed algebra |
| $\operatorname{Herm}_4$ | the Hermitian matrices, the $(-1)$-eigenspace |
| $\operatorname{Herm}_4^{++}$ | the positive definite Hermitian matrices |
| $P(t)$ | the geodesic through $P$ with velocity $H$ |

## Further Reading

- [The Polar Decomposition of $M_4(\mathbb{C})$](the-polar-decomposition-of-m4c.html), for the decomposition of a single element.
- [The Involution and the Hermitian Structure of $M_4(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m4c.html), for the conjugate transpose and the unitary group.
- [The Lie Algebra $\mathfrak{gl}_4(\mathbb{C})$ and $\mathfrak{sl}_4(\mathbb{C})$ of $M_4(\mathbb{C})$](the-lie-algebra-gl4-and-sl4-of-m4c.html), for the real forms and their signatures.
- [The Krein Isometry Group and Its Cartan Decomposition](the-krein-isometry-group-and-its-cartan-decomposition.html), for the indefinite case.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_4(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m4c.html), for the Grassmannians and the flag variety.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the Cartan decomposition and the symmetric spaces.
- Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones* (Oxford, 1994), for the cone of positive definite matrices.
