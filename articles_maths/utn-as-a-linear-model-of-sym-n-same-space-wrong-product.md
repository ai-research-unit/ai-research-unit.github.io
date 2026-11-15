# __$UT_n$ as a Linear Model of $\operatorname{Sym}_n$: Same Space, Wrong Product__

## Introduction

**The triangular algebra and the symmetric half have the same dimension $n(n+1)/2$ and are linearly isomorphic by symmetrisation, but the isomorphism carries the associative product of $UT_n$ to something that is not the Jordan product of $\operatorname{Sym}_n$, so the two algebras are the same vector space with two incompatible products.**

The article proves the isomorphism $U\mapsto\tfrac12(U+U^{\mathsf T})$, exhibits the failure of multiplicativity with explicit numbers, compares the two trace forms and their radicals, shows that the projection onto the symmetric half is not a Peirce projection $A\mapsto EAE$, and reads the difference through the nilpotents and the cone. It assumes *$UT_n$ as the Complement of the Antisymmetric Part (Transpose Case)* for the two spaces and *The Jordan Algebra $\operatorname{Sym}_n$* for the Jordan structure. It defers the Peirce theory to *The Peirce Decomposition and the Two Halves* and the cone to *The Cone of Positive Semidefinite Matrices*.

## Two Algebras on One Dimension

**The two spaces have the same dimension and are both subspaces of $M_n(\mathbb{R})$.** A symmetric matrix is determined by its entries on and above the diagonal, and an upper triangular matrix by the same number of entries, so

$$
\dim\operatorname{Sym}_n=\dim UT_n=\frac{n(n+1)}{2}=3,6,10,15\quad(n=2,3,4,5).
$$

The two spaces are different subspaces of the same $n^{2}$-dimensional space: their intersection is the diagonal, of dimension $n$, since a matrix that is both symmetric and upper triangular is diagonal.

**The products are different in kind.** $\operatorname{Sym}_n$ carries the Jordan product $X\circ Y=\tfrac12(XY+YX)$, which is commutative and not closed under the ordinary product; $UT_n$ carries the ordinary product, which is associative and not commutative. So the two algebras have the same carrier dimension and no product in common, and the question of the article is what a linear identification between them can and cannot preserve.

**The spectra are as different as the products.** Every element of $\operatorname{Sym}_n$ has real spectrum and is diagonalisable by an orthogonal change of basis; an element of $UT_n$ has spectrum equal to its diagonal, and a strictly upper triangular element has spectrum $\{0\}$ and is nilpotent. So the two spaces have the same dimension and opposite spectral behaviour, and the difference is visible in every element rather than only in the algebra laws.

## The Linear Isomorphism by Symmetrisation

**The symmetrisation map is a linear isomorphism.** Put

$$
S(U)=\tfrac12\big(U+U^{\mathsf T}\big).
$$

For $U\in UT_n$ the matrix $S(U)$ is symmetric, and $S$ is injective on $UT_n$: if $S(U)=0$ then $U$ is upper triangular and antisymmetric, hence zero by the computation of *$UT_n$ as the Complement of the Antisymmetric Part (Transpose Case)*. Since the two spaces have the same dimension, $S$ is an isomorphism, and its inverse on the units is

$$
S^{-1}(E_{ii})=E_{ii},\qquad S^{-1}(E_{ij}+E_{ji})=E_{ij}\quad(i<j).
$$

The rank of $S$ on $UT_n$ was computed as $3,6,15,36$ at $n=2,3,5,8$, equal to $\dim\operatorname{Sym}_n$ in each case.

**The inverse is the projection onto the upper triangle.** The map $U\mapsto S(U)$ forgets nothing on $UT_n$, and its inverse takes a symmetric matrix to its upper triangular part, with the diagonal kept whole and each off-diagonal pair halved and sent to the upper entry. So the linear identification between the two spaces is the identity on the diagonal and the choice of one of the two off-diagonal entries.

**A linear isomorphism of this kind is not canonical and cannot be, because the two spaces sit differently inside $M_n$.** The symmetric half is the fixed space of an involution and is defined by a symmetry of the whole algebra; the triangular algebra is defined by a flag and by a choice of basis. The isomorphism $S$ uses both structures, and that is why it preserves nothing but the dimension.

## The Products Do Not Agree

**Symmetrisation does not carry the product to the Jordan product.** For $U,V\in UT_n$,

$$
S(UV)\neq S(U)\circ S(V)\qquad\text{in general,}
$$

and the failure is not a small perturbation: at $n=2,3,4$ the largest entry of the difference $S(UV)-S(U)\circ S(V)$ is $0.84,0.37,1.37$ on random unit-triangular inputs, so the two products disagree at the size of the inputs themselves.

**The reason is that the symmetrisation of a product sees the antisymmetric parts.** Writing $U=S_1+K_1$ and $V=S_2+K_2$ with $S_i$ symmetric and $K_i$ antisymmetric,

$$
S(UV)=\tfrac12\big(UV+(UV)^{\mathsf T}\big)=S_1\circ S_2+K_1\circ K_2+\tfrac12[S_1,K_2]+\tfrac12[K_1,S_2],
$$

which is the symmetric part of a product from *The Symmetric and Antisymmetric Parts of a Product*. The Jordan product $S(U)\circ S(V)=S_1\circ S_2$ keeps only the first term, so the disagreement is exactly the three remaining terms, and it vanishes exactly when $U$ and $V$ are both symmetric, that is when the triangular matrices are diagonal.

**So the isomorphism is not an algebra isomorphism in either direction.** It does not carry the associative product to the Jordan product, and it does not carry the Jordan product to the associative product either, since $\operatorname{Sym}_n$ is not closed under the latter. The two algebras are therefore linearly isomorphic and algebraically unrelated, and the article's title is the exact statement: same space, wrong product.

**What the isomorphism does preserve is the diagonal.** The diagonal is the intersection of the two spaces and the fixed set of both the transpose and the flag, so $S$ is the identity there. Every statement that involves only the diagonal, such as the trace or the determinant of a diagonal element, transfers; every statement that involves an off-diagonal entry does not.

## The Trace Forms and the Radicals

**The trace form is positive definite on one space and degenerate on the other.** On $\operatorname{Sym}_n$,

$$
\operatorname{tr}(XY)=\sum_{i,j}X_{ij}Y_{ij}
$$

is the Euclidean form, of rank $n(n+1)/2$ and radical zero. On $UT_n$ the same formula gives a form of rank $n$ and radical $n_+$ of dimension $n(n-1)/2$, by the computation of *The Antisymmetric Part inside $UT_n$: the Radical as the Commutator*.

**The isomorphism $S$ does not preserve the form.** For $U,V\in UT_n$,

$$
\operatorname{tr}\big(S(U)S(V)\big)\neq\operatorname{tr}(UV)
$$

in general, since the right side sees only the diagonal pairs and the left side sees all the off-diagonal entries as well. So the linear isomorphism carries a form with a large radical to a form with none, and it is therefore not an isometry for any scalar multiple of the two forms.

**The two radicals measure the two failures.** The radical $n_+$ of the trace form on $UT_n$ is the set of elements invisible to the form, and it is also the commutator; the radical zero on $\operatorname{Sym}_n$ is the statement that the form is an inner product and that the cone of squares has an interior. So the degeneracy of the form on the triangular algebra is the same phenomenon as the absence of a cone there.

## Not a Peirce Corner

**The projection onto the symmetric half is defined by the involution, not by a multiplication.** The map

$$
\pi_{+}(A)=\tfrac12\big(A+A^{\mathsf T}\big)
$$

is the spectral projection of the involution $A\mapsto A^{\mathsf T}$ for the eigenvalue $+1$. A Peirce projection of the algebra has the form $A\mapsto EAE$ for an idempotent $E$, and its image is the corner $EM_nE$, which is a subalgebra of dimension $r^{2}$ with unit $E$.

**The two kinds of projection are different, and the dimensions decide it in almost every case.** A Peirce corner has dimension $r^{2}$, a perfect square; the symmetric half has dimension $n(n+1)/2$, which is a perfect square only for $n=1$ and $n=8$, where $8\cdot9/2=36=6^{2}$. So at $n=2,3,4,5,6$ the dimension alone excludes $\operatorname{Sym}_n$ from being a Peirce corner, and at $n=8$ the algebra structure excludes it: a corner is closed under the associative product, and $\operatorname{Sym}_8$ is not.

**The triangular algebra is not a Peirce corner either.** Its dimension is the same $n(n+1)/2$, so the dimension argument excludes $UT_n$ at the same values of $n$; and at every $n$ the structure excludes it, since a corner contains the idempotent $E$ as its unit and $UT_n$ has unit $\mathrm{I}$, whose Peirce corner is the whole algebra. So the split into halves is not a Peirce decomposition of the algebra, and the two subspaces that look alike are alike only in dimension.

**The Peirce decomposition of $\operatorname{Sym}_n$ is a decomposition of the half, not of the algebra.** The three Peirce spaces of an idempotent of $\operatorname{Sym}_n$ have dimensions $r(r+1)/2$, $r(n-r)$ and $(n-r)(n-r+1)/2$, and they sum to $n(n+1)/2$; the Peirce decomposition of the algebra has four parts and sums to $n^{2}$. The two decompositions are different objects, and the article's comparison is the smallest case of that difference.

## The Case $n=2$

**At $n=2$ the isomorphism is an explicit map between two three-dimensional spaces.** With the basis $E_{11},E_{12},E_{22}$ of $UT_2$ and the basis $\mathrm{I},\sigma_1,\sigma_3$ of $\operatorname{Sym}_2$,

$$
S(E_{11})=\tfrac12(\mathrm{I}+\sigma_3),\qquad S(E_{22})=\tfrac12(\mathrm{I}-\sigma_3),\qquad S(E_{12})=\tfrac12\sigma_1,
$$

so the isomorphism is the identity on the diagonal and halves the off-diagonal unit. The three images are a basis, and the computation confirms that the matrix of $S$ is invertible.

**The products are compared on one example.** Take $U=E_{12}$ and $V=E_{12}$, so that $UV=0$. Then $S(UV)=0$, while $S(U)\circ S(V)=\tfrac14\sigma_1\circ\sigma_1=\tfrac14\mathrm{I}\neq0$. So the product of the images is nonzero although the image of the product is zero, and the failure is a factor of a quarter of the identity.

**The biquaternion reading names the two structures.** The idempotents $\tilde\Pi_\pm=\tfrac12(e_t\pm\tilde{Ζ})$ are a basis of the diagonal of $\operatorname{Sym}_2$, and the corner $\mathbb{B}_{+-}$ is the off-diagonal line, so $S$ identifies the corner with the off-diagonal symmetric line. The two companion nilpotents $\vec\Upsilon_{+-}$ and $\vec\Upsilon_{-+}$ are the two directions of that corner, and their product is the idempotent $\tilde\Pi_+$: an associative product with no Jordan counterpart, which is exactly the failure that the article measures.

## Summary

The triangular algebra and the symmetric half have the same dimension $n(n+1)/2$ and are linearly isomorphic by symmetrisation $U\mapsto\tfrac12(U+U^{\mathsf T})$, with inverse the upper triangular part. The isomorphism is not an algebra isomorphism: $S(UV)$ differs from $S(U)\circ S(V)$ by the three mixed terms of the product formula, and it is the identity only on the diagonal. The trace form is positive definite on $\operatorname{Sym}_n$ and degenerate with radical $n_+$ on $UT_n$, and the isomorphism preserves neither form. The projection onto the symmetric half is the spectral projection of the transpose, not a Peirce projection $A\mapsto EAE$, and the dimension $n(n+1)/2$ is a perfect square only at $n=1,8$, so the two spaces are not corners of the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S(U)=\tfrac12(U+U^{\mathsf T})$ | the symmetrisation, a linear isomorphism $UT_n\to\operatorname{Sym}_n$ |
| $n(n+1)/2$ | the common dimension of the two spaces |
| $X\circ Y=\tfrac12(XY+YX)$ | the Jordan product of the symmetric half |
| $n_+$ | the radical of the trace form on $UT_n$ |
| $\pi_{+}=\tfrac12(1+T^{\mathsf T})$ | the spectral projection of the transpose |
| $EM_nE$ | a Peirce corner, of dimension $r^{2}$ |
| $8\cdot9/2=36=6^{2}$ | the only case beyond $n=1$ where the dimension is a square |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for Peirce corners and their dimensions.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (AMS, 1968), for the Jordan product and the cone of squares.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the upper triangular part and the QR decomposition of a matrix.
- [$UT_n$ as the Complement of the Antisymmetric Part (Transpose Case)](utn-as-the-complement-of-the-antisymmetric-part-transpose-case.html), for the two spaces as complements.
- [The Jordan Algebra $\operatorname{Sym}_n$](the-jordan-algebra-sym-n.html), for the product that the isomorphism fails to carry.
- [The Antisymmetric Part inside $UT_n$: the Radical as the Commutator](the-antisymmetric-part-inside-utn-the-radical-as-the-commutator.html), for the radical of the trace form on the triangular algebra.
