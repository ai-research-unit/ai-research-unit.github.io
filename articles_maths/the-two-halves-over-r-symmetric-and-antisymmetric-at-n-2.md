# __The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$__

## Introduction

**The real matrices split as the symmetric part of dimension $3$ and the antisymmetric part of dimension $1$, and the small dimension of the second half decides every formula on the first.**

The article proves the split $M_2(\mathbb{R})=\operatorname{Sym}_2(\mathbb{R})\oplus\Lambda^{2}\mathbb{R}^{2}$, exhibits the antisymmetric half as the line $\mathbb{R}J$, computes the bracket of two symmetric matrices as a cross product on that line, shows that the adjoint of $J$ is a complex structure on the traceless symmetric plane, and reads the cone and the idempotents of the symmetric half. It assumes *The Involutions of $M_2(\mathbb{C})$ over $\mathbb{R}$ and over $\mathbb{C}$* for the transpose and its fixed space, and *The Two Base Fields: $M_2(\mathbb{R})$ inside $M_2(\mathbb{C})$* for the real algebra.

It defers the product rules to *The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$ at $n=2$*, the orthogonal-complement statement to *The Two Halves as Orthogonal Complements at $n=2$*, and the same split over $\mathbb{C}$ to *The Two Halves over $\mathbb{C}$: Hermitian and Skew-Hermitian at $n=2$*. In the biquaternion language the two halves are the vectors and the bivectors, which is *Subspaces and Decompositions of the Biquaternion Algebra*.

## The Split over $\mathbb{R}$

**Theorem.** Every real matrix is the sum of a symmetric and an antisymmetric one, in exactly one way:

$$
M_2(\mathbb{R})=\operatorname{Sym}_2(\mathbb{R})\oplus\Lambda^{2}\mathbb{R}^{2},\qquad \dim=3+1=4.
$$

**Proof.** $A=H+K$ with $H=\tfrac12(A+A^{\mathsf T})$ and $K=\tfrac12(A-A^{\mathsf T})$; the two pieces are fixed and negated by the transpose. If $H+K=0$ with $H$ symmetric and $K$ skew, then transposing gives $H-K=0$, so both vanish.

**The two halves are the eigenspaces of the transpose.** The map $\tau(A)=A^{\mathsf T}$ has $+1$ on $\operatorname{Sym}_2$ and $-1$ on $\Lambda^{2}\mathbb{R}^{2}$, so the split is the eigenspace decomposition and the projections are the two halves of the formula above.

**The dimensions are counted directly.** A symmetric matrix has three free entries and an antisymmetric one has a single entry, because $a_{11}=a_{22}=0$ and $a_{12}=-a_{21}$.

## The Symmetric Half and Its Coordinates

**Definition.** The **traceless symmetric** matrices form the plane

$$
\mathfrak{p}=\left\{\begin{pmatrix}a&b\\ b&-a\end{pmatrix}\right\},
$$

of dimension $2$, and $\operatorname{Sym}_2(\mathbb{R})=\mathbb{R}I\oplus\mathfrak{p}$.

**Proposition.** The three matrices

$$
I=\begin{pmatrix}1&0\\ 0&1\end{pmatrix},\qquad
\sigma_{3}=\begin{pmatrix}1&0\\ 0&-1\end{pmatrix},\qquad
\sigma_{1}=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}
$$

form a basis of $\operatorname{Sym}_2(\mathbb{R})$, and each has square $I$.

**Proof.** They are symmetric and independent, and there are three of them in a space of dimension three. The squares are immediate, and $\sigma_{3},\sigma_{1}$ are traceless.

**The Cayley–Hamilton identity in the symmetric half.** For symmetric $S$ of order two,

$$
S^{2}=\operatorname{tr}(S)\,S-\det(S)\,I .
$$

**Proof.** This is Cayley–Hamilton, valid for every matrix of order two, and it needs no symmetry. It is the reason a symmetric matrix of order two is determined by its trace, its determinant and one direction.

**The traceless part squares to a scalar.** For $u\in\mathfrak{p}$ one has $u^{2}=-\det(u)I$, so $u^{2}$ is a multiple of the identity; the two eigenvalues of $u$ are $\pm\sqrt{-\det u}$.

**Corollary (the Jordan product on the plane).** For $u,v\in\mathfrak{p}$,

$$
uv+vu=\operatorname{tr}(uv)\,I .
$$

**Proof.** The left-hand side is symmetric, so it is a scalar plus a multiple of a traceless matrix; it suffices to check the identity on the basis $\sigma_{3},\sigma_{1}$, where $\{\sigma_{3},\sigma_{3}\}=\{\sigma_{1},\sigma_{1}\}=2I=\operatorname{tr}(\sigma_{i}^{2})I$ and $\{\sigma_{3},\sigma_{1}\}=0=\operatorname{tr}(\sigma_{3}\sigma_{1})I$. Bilinearity extends it to $\mathfrak{p}$.

**The plane is a copy of $\mathbb{C}$.** The product rule $u^{2}=-\det(u)I$ with $\det(u)\ge0$ on a suitable half makes $\mathfrak{p}$ into a field isomorphic to $\mathbb{C}$; the identification is the content of *The Two Base Fields: $M_2(\mathbb{R})$ inside $M_2(\mathbb{C})$* read inside the traceless plane.

## The Antisymmetric Half Is a Line

**Theorem.** The antisymmetric matrices of order two form the line $\mathbb{R}J$ with

$$
J=\begin{pmatrix}0&1\\ -1&0\end{pmatrix},\qquad J^{2}=-I,\qquad J^{\mathsf T}=-J .
$$

**Proof.** An antisymmetric matrix of order two has $a_{11}=a_{22}=0$ and $a_{21}=-a_{12}$, so it is $a_{12}J$; the square is computed directly.

**The line is a complex structure.** Since $J^{2}=-I$, the matrix $J$ makes $\mathbb{R}^{2}$ into a complex line, and multiplication by $i$ is multiplication by $J$ in the real basis.

**Corollary.** $\Lambda^{2}\mathbb{R}^{2}$ is one-dimensional, hence abelian as a Lie algebra, and it is the Lie algebra $\mathfrak{so}(2)$ of the rotations of the plane.

**Proof.** A one-dimensional Lie algebra has zero bracket. The rotations of the plane are the matrices $\exp(\theta J)=\cos\theta\,I+\sin\theta\,J$, whose derivatives at $0$ are the multiples of $J$.

**The exponential is the whole circle.** Every rotation is $\exp(\theta J)$ for a unique $\theta$ modulo $2\pi$, since $\cos\theta\,I+\sin\theta\,J$ describes the unit circle in the plane spanned by $I$ and $J$.

## The Bracket of Two Symmetric Matrices

**Proposition.** For symmetric $S,T$ the commutator $[S,T]=ST-TS$ is antisymmetric, so it lies in the line $\mathbb{R}J$.

**Proof.** $[S,T]^{\mathsf T}=[T^{\mathsf T},S^{\mathsf T}]=[T,S]=-[S,T]$. Alternatively, $(ST)^{\mathsf T}=TS$, so the commutator changes sign under the transpose.

**Proposition (the value).** For $S=s_{0}I+s_{1}\sigma_{3}+s_{2}\sigma_{1}$ and $T=t_{0}I+t_{1}\sigma_{3}+t_{2}\sigma_{1}$,

$$
[S,T]=2\,(s_{1}t_{2}-s_{2}t_{1})\,J .
$$

**Proof.** The scalars cancel because $I$ commutes with everything, and $[\sigma_{3},\sigma_{1}]=2J$, $[\sigma_{1},\sigma_{3}]=-2J$, while $[\sigma_{3},\sigma_{3}]=[\sigma_{1},\sigma_{1}]=0$. Collecting the two cross terms gives the determinant $s_{1}t_{2}-s_{2}t_{1}$.

**Corollary (the cross product).** The bracket $\Lambda^{2}\operatorname{Sym}_2(\mathbb{R})\to\Lambda^{2}\mathbb{R}^{2}$ is the cross product $\mathbb{R}^{3}\wedge\mathbb{R}^{3}\to\mathbb{R}$ on the coefficient vectors, up to the fixed factor $2$.

**Proof.** The scalar $s_{1}t_{2}-s_{2}t_{1}$ is the third component of the cross product of the coefficient vectors when the trace coefficient is the third coordinate, and the commutator depends only on the traceless parts. On the normalised traceless pair $\sigma_{3},\sigma_{1}$ the value is $2J$, and it is $-2J$ in the reversed order, which is the factor quoted in the general statement of the sign.

**Corollary.** Two symmetric matrices commute exactly when their traceless parts are dependent.

**Proof.** The scalar $s_{1}t_{2}-s_{2}t_{1}$ vanishes exactly when the two traceless coefficient vectors are proportional.

## The Adjoint of $J$: a Complex Structure on the Traceless Plane

**Proposition.** The map $S\mapsto[S,J]$ preserves $\operatorname{Sym}_2(\mathbb{R})$, kills $I$, and satisfies

$$
(\operatorname{ad}J)^{2}=-4\,\mathrm{id}
$$

on the traceless plane $\mathfrak{p}$.

**Proof.** $[\sigma_{3},J]=2\sigma_{1}$ and $[\sigma_{1},J]=-2\sigma_{3}$, so $[S,J]=2s_{1}\sigma_{1}-2s_{2}\sigma_{3}$, which is traceless and symmetric; applying the same rule again multiplies each coefficient by $-4$. The identity commutes with $J$.

**Corollary.** The traceless symmetric plane carries a complex structure, so it is a real two-dimensional space with a chosen $i$, and the bracket with $J$ is twice that structure with a sign.

**Corollary.** $\operatorname{Sym}_2(\mathbb{R})=\mathbb{R}I\oplus\mathfrak{p}$ is the decomposition of the symmetric half into the fixed line of $\operatorname{ad}J$ and the plane on which $\operatorname{ad}J$ is a complex structure.

**This is the $\mathfrak{k}$-$\mathfrak{p}$ split of $\mathfrak{sl}_2(\mathbb{R})$.** The pair $\mathfrak{k}=\mathbb{R}J$, $\mathfrak{p}=\mathfrak{p}$ satisfies $[\mathfrak{k},\mathfrak{k}]=0$, $[\mathfrak{k},\mathfrak{p}]\subseteq\mathfrak{p}$ and $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}$, which is the definition of a symmetric pair at order two, and it is *Symmetric Pairs and Cartan Pairs: the Reductivity Criterion at $n=2$*.

## The Symmetric Half and the Minkowski Form

**Proposition.** The pairing $\langle S,T\rangle=\operatorname{tr}(ST)$ on $\operatorname{Sym}_2(\mathbb{R})$ has signature $(3,0)$: it is positive definite.

**Proof.** $S$ symmetric has real eigenvalues $\lambda_{1},\lambda_{2}$, and $\operatorname{tr}(S^{2})=\lambda_{1}^{2}+\lambda_{2}^{2}\ge0$ with equality only for $S=0$; polarising gives positive definiteness.

**Proposition.** On the whole space $M_2(\mathbb{R})$ the same pairing has signature $(3,1)$: it is positive on the symmetric half and negative on the antisymmetric line.

**Proof.** $\operatorname{tr}(K^{2})=-2k^{2}$ on $K=kJ$, and the two halves are orthogonal because $\operatorname{tr}(HK)=0$ for $H$ symmetric and $K$ skew. The signature is $(3,1)$, the Minkowski signature.

**Corollary.** The antisymmetric line is the unique negative direction of the trace form, and it is a timelike line.

**The trace form is $\operatorname{tr}(X^{\mathsf T}Y)$.** On the real matrices the Hilbert–Schmidt form and the trace form of this article coincide, which is *The Hilbert–Schmidt Form at $n=2$*.

## The Cone and the Idempotents of the Symmetric Half

**Definition.** The **cone** is $\{S\in\operatorname{Sym}_2(\mathbb{R}): S\ \text{positive semidefinite}\}$.

**Proposition.** $S$ is positive semidefinite exactly when $\operatorname{tr}S\ge0$ and $\det S\ge0$.

**Proof.** Write $S=aI+u$ with $u$ traceless; the eigenvalues are $a\pm\sqrt{-\det u}$. Both are nonnegative exactly when $a\ge\sqrt{-\det u}$, which is equivalent to $a\ge0$ and $a^{2}+\det u\ge0$, that is to $\operatorname{tr}S\ge0$ and $\det S\ge0$ because $\det S=a^{2}+\det u$ and $\operatorname{tr}S=2a$.

**Corollary (the sharp cone).** The cone is the set of squares of symmetric matrices, and its boundary is the set of rank-one symmetric matrices plus the origin.

**Proof.** A square $S^{2}$ has nonnegative eigenvalues; conversely a positive semidefinite symmetric matrix has a symmetric square root $\sqrt{S}$, so it is a square. The boundary is where $\det S=0$, which for symmetric matrices means rank one or zero.

**The cone is the set of squares.** It is $\{X^{\mathsf T}X:X\ \text{real}\}$, which is the same set as the positive semidefinite half. In the biquaternion language it is the positive cone of *The Polar Decomposition of a Biquaternion*, transported through the identification of the trace form with $N$.

**The idempotents of the symmetric half.** A symmetric idempotent of order two satisfies $S^{2}=S$, so its eigenvalues are $0$ or $1$; writing $S=\tfrac12(I+u)$ with $u$ traceless symmetric, the condition $S^{2}=S$ becomes $u^{2}=I$, that is $\operatorname{tr}(u^{2})=2$.

**Corollary.** The symmetric idempotents of order two are exactly the matrices $\tfrac12(I+u)$ with $u$ traceless symmetric and $\det u=-1$; they form the unit circle $a^{2}+b^{2}=1$ in the traceless plane, the real equator of the sphere of the rank-one projections.

## Summary

The real matrices split into the symmetric half of dimension $3$ and the antisymmetric line $\mathbb{R}J$ of dimension $1$, the two eigenspaces of the transpose. The symmetric half is spanned by $I,\sigma_{3},\sigma_{1}$, obeys Cayley–Hamilton, and its traceless plane contains a copy of $\mathbb{C}$ through $u^{2}=-\det(u)I$.

Two symmetric matrices bracket to a multiple of $J$, and the multiple is $2(s_{1}t_{2}-s_{2}t_{1})$, the cross product of the traceless coefficient vectors; the pair $\sigma_{3},\sigma_{1}$ returns $\pm2J$. The adjoint of $J$ preserves the symmetric half, kills $I$ and is a complex structure on the traceless plane, giving the symmetric pair $\mathfrak{k}=\mathbb{R}J$, $\mathfrak{p}=\mathfrak{p}$ of $\mathfrak{sl}_2(\mathbb{R})$. The trace form is positive on the symmetric half and negative on the line, of signature $(3,1)$; the cone of the symmetric half is $\{\operatorname{tr}\ge0,\det\ge0\}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Sym}_2(\mathbb{R})$ | the fixed space of the transpose, dimension $3$ |
| $\Lambda^{2}\mathbb{R}^{2}$ | the antisymmetric line $\mathbb{R}J$ |
| $J$ | the complex structure $\begin{pmatrix}0&1\\ -1&0\end{pmatrix}$ |
| $\mathfrak{p}$ | the traceless symmetric plane |
| $\mathfrak{k}$ | the antisymmetric line as a Lie algebra |
| $\sigma_{3},\sigma_{1}$ | the traceless symmetric basis matrices |
| $\operatorname{ad}J$ | the map $S\mapsto[S,J]$ |
| cone | $\{S:\operatorname{tr}S\ge0,\ \det S\ge0\}$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the symmetric-skew split and the definiteness of the trace pairing.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the pair $\mathfrak{k},\mathfrak{p}$ and the symmetric-space correspondence.
- [The Involutions of $M_2(\mathbb{C})$ over $\mathbb{R}$ and over $\mathbb{C}$](the-involutions-of-m2c-over-r-and-over-c.html), for the transpose whose eigenspaces these halves are.
- [The Two Base Fields: $M_2(\mathbb{R})$ inside $M_2(\mathbb{C})$](the-two-base-fields-m2r-inside-m2c.html), for the real algebra and its complex structure.
- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the vectors and the bivectors in the biquaternion language.
