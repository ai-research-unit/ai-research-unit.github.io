# __The Cartan Decomposition of $\mathrm{GL}_n(\mathbb{R})$__

## Introduction

**The general linear group is the product of the orthogonal group and the exponentials of the symmetric matrices, and the product is a diffeomorphism.** The statement is the polar decomposition read as a theorem about a group and a subspace: the group factor is compact, the subspace factor is a linear space, and the two are the eigenspaces of one involution.

The article states the decomposition, proves the three bracket relations, identifies the involution $\theta(X)=-X^{\mathsf T}$ and its group form, proves that the product map is a diffeomorphism, discusses the maximal compact subgroup and its two components, computes the restricted roots and the Weyl group, and identifies the quotient with the cone of positive definite matrices. It assumes *The Polar Decomposition from the Two Halves and the Sign of the Determinant* and *The Exponential of the Symmetric Part: Stretches and the Positive Cone*.

## The Statement

**Theorem (Cartan decomposition).** Put $K=\mathrm{O}(n)$ and $\mathfrak{p}=\operatorname{Sym}_n$. Every $g\in\mathrm{GL}_n(\mathbb{R})$ is uniquely

$$
g=k\,\mathrm{e}^{X},\qquad k\in K,\ X\in\mathfrak{p},
$$

and the map $K\times\mathfrak{p}\to\mathrm{GL}_n(\mathbb{R})$, $(k,X)\mapsto k\mathrm{e}^{X}$, is a diffeomorphism.

**The two factors are of different natures.** $K$ is compact and bounded in $M_n(\mathbb{R})$; $\mathrm{e}^{\mathfrak{p}}$ is the cone $\operatorname{Sym}_n^{>0}$, open, convex and unbounded. A compact factor and a linear factor, multiplied once, give the group.

**The count is exact.** $\dim K=n(n-1)/2$ and $\dim\mathfrak{p}=n(n+1)/2$, and their sum is $n^{2}=\dim\mathrm{GL}_n(\mathbb{R})$.

## The Lie Algebra Splits

**The Lie algebra is $\mathfrak{gl}_n(\mathbb{R})=M_n(\mathbb{R})$ with the commutator.** Every matrix is a symmetric plus a skew matrix in exactly one way:

$$
A=\underbrace{\tfrac12(A+A^{\mathsf T})}_{\text{symmetric}}+\underbrace{\tfrac12(A-A^{\mathsf T})}_{\text{skew}} .
$$

So, as vector spaces,

$$
\mathfrak{gl}_n(\mathbb{R})=\mathfrak{k}\oplus\mathfrak{p},\qquad \mathfrak{k}=\mathfrak{so}(n)=\operatorname{Skew}_n,\quad \mathfrak{p}=\operatorname{Sym}_n,
$$

and the sum is direct because a matrix that is both symmetric and skew is zero. The dimensions add, $\frac{n(n-1)}{2}+\frac{n(n+1)}{2}=n^{2}$.

**$\mathfrak{k}$ is a subalgebra and $\mathfrak{p}$ is not.** The skew matrices are closed under the commutator. The symmetric ones are not: the commutator of two symmetric matrices is skew whenever it is nonzero, so $\mathfrak{p}$ is only a subspace.

## The Three Brackets

**Theorem.** The three relations hold:

$$
[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k},\qquad [\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p},\qquad [\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}.
$$

*Proof.* Let $X,Y$ be skew and $S,T$ symmetric. Using $(UV)^{\mathsf T}=V^{\mathsf T}U^{\mathsf T}$ and $X^{\mathsf T}=-X$, $S^{\mathsf T}=S$,

$$
[X,Y]^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}-X^{\mathsf T}Y^{\mathsf T}=YX-XY=-[X,Y],
$$

so $[X,Y]$ is skew. Next,

$$
[X,S]^{\mathsf T}=S^{\mathsf T}X^{\mathsf T}-X^{\mathsf T}S^{\mathsf T}=-SX+XS=[X,S],
$$

so $[X,S]$ is symmetric. Finally,

$$
[S,T]^{\mathsf T}=TS-ST=-[S,T],
$$

so $[S,T]$ is skew. Numerically all three defects are $0$ at $n=3$ on random pairs.

## The Involution

**Definition.** Put $\theta(X)=-X^{\mathsf T}$ for $X\in\mathfrak{gl}_n(\mathbb{R})$.

**$\theta$ is an involutive automorphism.** It is linear, $\theta^{2}=\mathrm{id}$, and

$$
\theta([X,Y])=-[X,Y]^{\mathsf T}=-[Y^{\mathsf T},X^{\mathsf T}]=[X^{\mathsf T},Y^{\mathsf T}]=[\theta X,\theta Y],
$$

using $[U,V]^{\mathsf T}=[V^{\mathsf T},U^{\mathsf T}]$; numerically the defect is $0$ at $n=3$.

**The eigenspaces are the two summands.** A matrix with $\theta(X)=X$ satisfies $-X^{\mathsf T}=X$ and is skew; a matrix with $\theta(X)=-X$ satisfies $X^{\mathsf T}=X$ and is symmetric. Hence

$$
\mathfrak{k}=\{X:\theta(X)=X\},\qquad \mathfrak{p}=\{X:\theta(X)=-X\}.
$$

**Theorem (the group involution).** The map $\Theta(g)=(g^{\mathsf T})^{-1}$ is an involutive automorphism of $\mathrm{GL}_n(\mathbb{R})$ whose fixed set is $K=\mathrm{O}(n)$, and its derivative at the identity is $\theta$.

*Proof.* $\Theta(gh)=(h^{\mathsf T}g^{\mathsf T})^{-1}=(g^{\mathsf T})^{-1}(h^{\mathsf T})^{-1}=\Theta(g)\Theta(h)$ and $\Theta^{2}(g)=g$. A fixed point satisfies $(g^{\mathsf T})^{-1}=g$, that is $g^{\mathsf T}g=\mathrm{I}$, that is $g\in\mathrm{O}(n)$. The derivative at $\mathrm{I}$ in the direction $X$ is $-X^{\mathsf T}$.

**The two eigenspaces are what make the decomposition unique.** $\mathfrak{k}$ and $\mathfrak{p}$ are subspaces of a linear space, so $\exp$ is injective on $\mathfrak{p}$, and the involution separates the two factors of the polar decomposition.

## The Diffeomorphism

**Theorem.** The product map $K\times\mathfrak{p}\to\mathrm{GL}_n(\mathbb{R})$ is a diffeomorphism.

*Proof.* It is the polar decomposition. For $g$ put $P=(g^{\mathsf T}g)^{1/2}$, positive definite, and $k=gP^{-1}$, orthogonal. Then $k\in K$, $X=\log P\in\mathfrak{p}$, and $g=k\mathrm{e}^{X}$. Uniqueness is the uniqueness of the polar decomposition together with the bijection $\exp:\operatorname{Sym}_n\to\operatorname{Sym}_n^{>0}$. Both maps $g\mapsto(k,X)$ and $(k,X)\mapsto k\mathrm{e}^{X}$ are smooth.

**The inverse is explicit.** From $g=k\mathrm{e}^{X}$ one reads $\mathrm{e}^{2X}=g^{\mathsf T}g$, so $X=\tfrac12\log(g^{\mathsf T}g)$.

**The two components.** For $\det g>0$ the factor $k$ lies in $\mathrm{SO}(n)$, and $\mathrm{GL}_n(\mathbb{R})^{+}$ is diffeomorphic to $\mathrm{SO}(n)\times\operatorname{Sym}_n$. For $\det g<0$ it lies in the other component of $\mathrm{O}(n)$. The choice $K=\mathrm{O}(n)$ covers both components at the price of a disconnected $K$.

## The Maximal Compact Subgroup

**Theorem.** $\mathrm{O}(n)$ is a maximal compact subgroup of $\mathrm{GL}_n(\mathbb{R})$, and every compact subgroup is conjugate to a subgroup of it.

*Proof.* Let $H$ be compact. Averaging the standard inner product over $H$ gives the invariant positive definite form $\langle x,y\rangle_H=\int_H\langle hx,hy\rangle\,\mathrm{d}h$. In an orthonormal basis of this form every $h\in H$ is orthogonal, so $H\subseteq\mathrm{O}(n)$ after a change of basis. If in addition $\mathrm{O}(n)\subseteq H$, the form is invariant under $\mathrm{O}(n)$, hence a positive multiple of the standard one, and the basis is orthonormal for the standard form too; then $H\subseteq\mathrm{O}(n)$ in the original basis, so $H=\mathrm{O}(n)$.

**The two components.** $\mathrm{O}(n)$ has two, $\mathrm{SO}(n)$ and $\mathrm{O}^{-}(n)=\{Q:\det Q=-1\}$, and $\mathrm{O}^{-}(n)=J\,\mathrm{SO}(n)$ for any $J\in\mathrm{O}^{-}(n)$. Only the first is a subgroup, and only the first is the identity component of the ambient group.

**The maximal compact subgroup of the identity component is $\mathrm{SO}(n)$.** For $\mathrm{GL}_n(\mathbb{R})^{+}$ the compact factor is connected, and the decomposition reads $\mathrm{GL}_n(\mathbb{R})^{+}=\mathrm{SO}(n)\exp(\operatorname{Sym}_n)$.

## The Restricted Roots

**The maximal abelian subspace of $\mathfrak{p}$ is the diagonal.** Commuting symmetric matrices are simultaneously diagonalisable, so

$$
\mathfrak{a}=\{\operatorname{diag}(x_1,\dots,x_n):x_i\in\mathbb{R}\}
$$

is a maximal abelian subspace of $\operatorname{Sym}_n$, of dimension $n$.

**The joint eigenspaces are the coordinate lines.** For $H=\operatorname{diag}(x)$ and the matrix unit $E_{ij}$,

$$
[H,E_{ij}]=(x_i-x_j)E_{ij},
$$

exactly at $n=3$ for all nine pairs. So the restricted roots are the functionals $\alpha_{ij}(x)=x_i-x_j$ with $i\ne j$, each with root space $\mathbb{R}E_{ij}$ of multiplicity one, and the centraliser of $\mathfrak{a}$ is $\mathfrak{a}$ itself.

**The root system is that of $A_{n-1}$.** The roots are the $n(n-1)$ ordered differences, the positive ones are the $\binom n2$ with $i<j$, and every root vanishes on the line $x_1=\dots=x_n$, which is the centre. The system is that of $\mathfrak{sl}_n(\mathbb{R})$, not a larger one.

**The Weyl group is $S_n$.** It is the normaliser of $\mathfrak{a}$ in $K$ modulo its centraliser, and the permutation matrices are orthogonal and conjugate $\mathfrak{a}$ to itself. So $W=S_n$, of order $n!$, acting by permuting the indices.

## The Symmetric Space

**Theorem.** The quotient $\mathrm{GL}_n(\mathbb{R})/K$ is diffeomorphic to $\operatorname{Sym}_n^{>0}$, through $gK\mapsto gg^{\mathsf T}$.

*Proof.* The map is well defined, since $(gk)(gk)^{\mathsf T}=gg^{\mathsf T}$ for $k\in K$. It is surjective, because every $P\in\operatorname{Sym}_n^{>0}$ is $gg^{\mathsf T}$ with $g=P^{1/2}$. It is injective, because $gg^{\mathsf T}=hh^{\mathsf T}$ gives $(h^{-1}g)(h^{-1}g)^{\mathsf T}=\mathrm{I}$, so $h^{-1}g\in K$. Both the map and its inverse are smooth.

**The dimension is $n(n+1)/2$, and the count closes.** The quotient has the dimension of $\mathfrak{p}$, the cone has the dimension of $\operatorname{Sym}_n$, and

$$
n^{2}=\frac{n(n-1)}{2}+\frac{n(n+1)}{2}.
$$

**The space is a symmetric space.** The involution $\Theta$ acts on the quotient, and the geodesic symmetry at the base point is $P\mapsto P^{-1}$ on the cone. The cone with the metric $\langle U,V\rangle_P=\operatorname{tr}(P^{-1}UP^{-1}V)$ is the Riemannian symmetric space of the pair $(\mathrm{GL}_n,\mathrm{O}(n))$.

**The flat factor.** The scalar line $\{x\mathrm{I}\}$ lies in $\mathfrak{a}$ but is fixed by $K$, so the cone splits as $\mathbb{R}\times\{P:\det P=1\}$: a line of pure scaling and the stretches of unit determinant, which form the symmetric space of $\mathrm{SL}_n(\mathbb{R})$.

## The Case at $n=2$

**The two summands explicitly.** $\mathfrak{k}=\mathfrak{so}(2)$ is the line of matrices $\begin{pmatrix}0&-t\\t&0\end{pmatrix}$, and $\mathfrak{p}=\operatorname{Sym}_2$ is the three-dimensional space $\begin{pmatrix}x&y\\y&z\end{pmatrix}$. The dimensions are $1+3=4=\dim M_2(\mathbb{R})$.

**The stretch has a closed form.** For $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ invertible, put $M=A^{\mathsf T}A$ and $\delta=|\det A|$. Then

$$
P=\frac{M+\delta\,\mathrm{I}}{\sqrt{\operatorname{tr}M+2\delta}},
$$

which is symmetric positive definite and agrees with the spectral square root to $2\times10^{-16}$. The rotation is $Q=AP^{-1}$, with $\det Q=\operatorname{sgn}\det A$.

**The roots at $n=2$.** $\mathfrak{a}$ is the diagonal, of dimension two, and the only roots are $\pm(x_1-x_2)$: one positive root, of multiplicity one, plus the central line $x_1=x_2$. The Weyl group is $S_2=\{\pm1\}$, acting by swapping the diagonal entries. So

$$
\mathfrak{gl}_2(\mathbb{R})=\mathfrak{a}\oplus\mathbb{R}E_{12}\oplus\mathbb{R}E_{21},
$$

of dimensions $2+1+1=4$, and the two root lines are exchanged by the Weyl group.

**The quotient at $n=2$.** The cone is three-dimensional, the flat factor is the scaling line, and the remaining two dimensions are those of $\mathrm{SL}_2(\mathbb{R})/\mathrm{SO}(2)$. The decomposition is a diffeomorphism between the circle times a three-dimensional cone and the four-dimensional group; the reconstruction residual at $n=2$ is $2\times10^{-16}$.

## Summary

The Cartan decomposition of $\mathrm{GL}_n(\mathbb{R})$ is $G=K\exp(\mathfrak{p})$ with $K=\mathrm{O}(n)$ and $\mathfrak{p}=\operatorname{Sym}_n$, and the product map is a diffeomorphism from $K\times\mathfrak{p}$ onto $G$. At the level of the Lie algebra, $\mathfrak{gl}_n(\mathbb{R})=\mathfrak{k}\oplus\mathfrak{p}$ with $\mathfrak{k}=\mathfrak{so}(n)$, and the three brackets $[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k}$, $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$, $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}$ hold. The splitting is the eigenspace splitting of the involution $\theta(X)=-X^{\mathsf T}$, whose group form $\Theta(g)=(g^{\mathsf T})^{-1}$ fixes exactly $\mathrm{O}(n)$. The maximal abelian subspace of $\mathfrak{p}$ is the diagonal, the restricted roots are the differences $x_i-x_j$ with multiplicity one, and the Weyl group is $S_n$. The quotient $G/K$ is the cone of positive definite matrices, of dimension $n(n+1)/2$, and the count $n^{2}=n(n-1)/2+n(n+1)/2$ closes the article. At $n=2$ the summands have dimensions $1$ and $3$, the positive root is $x_1-x_2$, and the stretch is $(A^{\mathsf T}A+|\det A|\mathrm{I})/\sqrt{\operatorname{tr}(A^{\mathsf T}A)+2|\det A|}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K=\mathrm{O}(n)$ | The maximal compact subgroup |
| $\mathfrak{k}=\mathfrak{so}(n)$ | The skew matrices, the Lie algebra of $K$ |
| $\mathfrak{p}=\operatorname{Sym}_n$ | The symmetric matrices, the second summand |
| $\theta(X)=-X^{\mathsf T}$ | The Cartan involution on the Lie algebra |
| $\Theta(g)=(g^{\mathsf T})^{-1}$ | Its group form |
| $\mathfrak{a}$ | The diagonal matrices in $\mathfrak{p}$ |
| $\alpha_{ij}(x)=x_i-x_j$ | The restricted roots |
| $W=S_n$ | The Weyl group |
| $G/K\cong\operatorname{Sym}_n^{>0}$ | The symmetric space, of dimension $n(n+1)/2$ |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the Cartan decomposition and the restricted root system.
- Armand Borel, *Linear Algebraic Groups* (Springer, 1991), for the maximal compact subgroup and the polar decomposition in a reductive group.
- [The Polar Decomposition from the Two Halves and the Sign of the Determinant](the-polar-decomposition-from-the-two-halves-and-the-sign-of-the-determinant.html), for the uniqueness of the factors used here.
- [The Exponential of the Symmetric Part: Stretches and the Positive Cone](the-exponential-of-the-symmetric-part-stretches-and-the-positive-cone.html), for the cone, its dimension and its geodesics.
- [The Involutions of the First Kind: Transpose and Symplectic](the-involutions-of-the-first-kind-transpose-and-symplectic.html), for $\theta$ and the two halves it cuts.
