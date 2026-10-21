# __Introduction to the Remarkable Subspaces of the Quaternions__

## Introduction

The quaternion algebra $\mathbb{H}$ carries two distinguished real subspaces and no more: the **scalar subspace**, the line of real quaternions, and the **vector subspace**, the three-dimensional space of pure quaternions. The element, the basis and the product are those of *Quaternion Algebra*; the real vector space reading is *Quaternion Algebra*, and the involutions are *Quaternion Involutions and Projections*.

Here there is no central unit and the quaternion norm is definite, so the lattice has two subspaces and the norm is positive. The point of the article is exactly this contrast, and it is stated at the end rather than left to the reader.

The article owns the two subspaces one by one: the defining condition, the coordinate condition, the basis, the dimension, the role, and the two closures. It owns no product theory, no form and no topology; the norm and the invertibility criterion are *Norm and Invertibility in the Quaternion Algebra*, below this article in this category.

## The Natural Sign and the Two Subspaces

Over $\mathbb{R}$ the only conjugation is the natural sign ${}^{\natural}$, and it is the one written below.

The natural sign is an anti-involution, $\tilde q^{\natural}=q_t-\vec q$ with $\tilde q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ and $\vec q=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, and its $\pm1$ eigenspaces are the two remarkable subspaces. There is no fourth real subspace: the only other involutions available act by inner conjugation and move the two subspaces among themselves, and the article records their action in *Comparison of the Remarkable Subspaces of the Quaternions*, below this article in this category.

## The Scalar Subspace

**Definition.** The **scalar subspace** is the fixed space of ${}^{\natural}$,
$$
\mathbb{R}_{\mathbb{H}}=\{\tilde q\in\mathbb{H}:\tilde q^{\natural}=\tilde q\}=\{\tilde q:\vec q=0\}.
$$
Its projection is the scalar part $\mathrm{Sc}(\tilde q)=\tfrac12(\tilde q+\tilde q^{\natural})$.

**Coordinate condition.** $q_x=q_y=q_z=0$; that is, $\mathbb{R}_{\mathbb{H}}=\{q_te_t:q_t\in\mathbb{R}\}\cong\mathbb{R}$.

**Basis and dimension.** Basis $(e_t)$, dimension $1$.

**Role.** The scalar subspace is a subalgebra of $\mathbb{H}$ isomorphic to $\mathbb{R}$; it is the **centre** of the algebra, since it commutes with every element and every central element is scalar; and it is closed under inversion, the inverse of a nonzero scalar being the scalar $1/s$. It is the unique copy of the field in $\mathbb{H}$ up to the choice of a real unit, and it is the base of the algebra as a free module, the whole of $\mathbb{H}$ being a free module of rank four over it.

**Norm.** On $\mathbb{R}_{\mathbb{H}}$ the quaternion norm is the square, $\langle s\rangle_{\natural}=s^2$, and it is positive definite on the line; the nonzero scalars are exactly the units of the line.

## The Vector Subspace

**Definition.** The **vector subspace** is the anti-fixed space of ${}^{\natural}$,
$$
\mathrm{Vect}(\mathbb{H})=\{\tilde q\in\mathbb{H}:\tilde q^{\natural}=-\tilde q\}=\{\tilde q:\mathrm{Sc}(\tilde q)=0\},
$$
also written $\operatorname{Im}\mathbb{H}$. Its projection is the vector part $\vec q=\tfrac12(\tilde q-\tilde q^{\natural})$.

**Coordinate condition.** $q_t=0$; that is, $\mathrm{Vect}(\mathbb{H})=\{q_x\vec e_x+q_y\vec e_y+q_z\vec e_z\}\cong\mathbb{R}^3$.

**Basis and dimension.** Basis $(\vec e_x,\vec e_y,\vec e_z)$, dimension $3$.

**Role (not a subalgebra).** The vector subspace is not closed under the product. For $\vec q_1,\vec q_2$ pure,
$$
\vec q_1\,\vec q_2=-\langle\vec q_1,\vec q_2\rangle+\vec q_1\times\vec q_2,
$$
with $\langle\vec q_1,\vec q_2\rangle=\sum_kq_{1k}q_{2k}$ the inner product and $\vec q_1\times\vec q_2$ the cross product; the scalar part vanishes exactly when $\vec q_1$ and $\vec q_2$ are orthogonal. The symmetric and antisymmetric parts are
$$
\vec q_1\vec q_2+\vec q_2\vec q_1=-2\langle\vec q_1,\vec q_2\rangle, \qquad \vec q_1\vec q_2-\vec q_2\vec q_1=2(\vec q_1\times\vec q_2),
$$
so the cross product is recovered by $\vec q_1\times\vec q_2=\tfrac12(\vec q_1\vec q_2-\vec q_2\vec q_1)$. The subspace is closed under inversion — for pure nonzero $\vec q$ the inverse is $-\vec q/\langle \vec q\rangle_{\natural}$, again pure — but the square $\vec q^2=-\langle \vec q\rangle_{\natural}$ leaves the subspace. The vector subspace is the derived part of the algebra: the products of its elements generate $\mathbb{H}$, and under the commutator bracket it is the Lie algebra $\mathfrak{su}(2)$ of the group of unit quaternions.

**Norm.** On $\mathrm{Vect}(\mathbb{H})$ the quaternion norm is the square of the Euclidean norm, $\langle \vec q\rangle_{\natural}=|\vec q|^2=\langle\vec q,\vec q\rangle$, and it is positive definite on the three-space. Its unit sphere is the sphere of roots of $-1$: $\langle \vec q\rangle_{\natural}=1$ is $\vec q^2=-1$, the sphere of unit imaginary quaternions that carry the inner involutions of *Quaternion Involutions and Projections*.

Together with the decomposition $\tilde q=\mathrm{Sc}(\tilde q)+\vec q$ the two restrictions give the orthogonal sum
$$
\langle\tilde q\rangle_{\natural}=\langle\mathrm{Sc}(\tilde q)\rangle_{\natural}+\langle \vec q\rangle_{\natural}=q_t^2+|\vec q|^2,
$$
the two subspaces being orthogonal for the associated inner product; this is *Norm and Invertibility in the Quaternion Algebra*, below this article in this category, read on the two blocks. Invertibility is non-vanishing norm, by *Norm and Invertibility in the Quaternion Algebra*, below this article in this category: every nonzero element of either subspace is a unit, the scalar line and the vector space both meeting the singular set only at zero.

## The Two-Subspace Lattice and the Absence of the Full Lattice

**Proposition.** In the quaternion algebra the distinguished real subspaces are exactly two, the scalar line and the vector space, and they are supplementary,
$$
\mathbb{H}=\mathbb{R}_{\mathbb{H}}\oplus\mathrm{Vect}(\mathbb{H}), \qquad \mathbb{R}_{\mathbb{H}}\cap\mathrm{Vect}(\mathbb{H})=0, \qquad 1+3=4.
$$
Every other subspace distinguished by the involutions is $0$, $\mathbb{H}$, or one of these two.

**Proof.** The only non-trivial involution of $\mathbb{H}$ available on elements is ${}^{\natural}$, whose $\pm1$ eigenspaces are the two; the inner involutions are automorphisms that permute the vector lines and do not define new fixed spaces beyond the axis plane $\mathbb{C}_\nu=\mathbb{R}e_t\oplus\mathbb{R}\nu$ and its orthogonal complement $\nu^\perp$, which depend on the chosen axis and are not invariant objects of the algebra.



The additive decomposition carried by the two subspaces, and the polar decomposition the norm adds to it, are *Decompositions Along the Remarkable Subspaces of the Quaternions*, below this article in this category.

## Summary

The quaternion algebra has two remarkable real subspaces. The scalar line $\mathbb{R}_{\mathbb{H}}$ is the fixed space of the natural sign, of dimension one, a subalgebra and the centre, closed under inversion, on which the norm is the square. The vector space $\mathrm{Vect}(\mathbb{H})$ is the anti-fixed space, of dimension three, not a subalgebra, with product $\vec q_1\vec q_2=-\langle\vec q_1,\vec q_2\rangle+\vec q_1\times\vec q_2$; it is closed under inversion, its square is the negative norm, and its unit sphere is the sphere of roots of $-1$. The two are supplementary and orthogonal for the norm, and $\langle\tilde q\rangle_{\natural}=q_t^2+|\vec q|^2$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}_{\mathbb{H}}$ | the scalar subspace, the fixed space of ${}^{\natural}$, dimension one |
| $\mathrm{Vect}(\mathbb{H})$ | the vector subspace, the anti-fixed space of ${}^{\natural}$, dimension three |
| $\mathrm{Sc}(\tilde q)=\tfrac12(\tilde q+\tilde q^{\natural})$ | the scalar-part projection |
| $\vec q=\tfrac12(\tilde q-\tilde q^{\natural})$ | the vector-part projection |
| $\langle\vec q_1,\vec q_2\rangle$ | the inner product $\sum_kq_{1k}q_{2k}$ on $\mathrm{Vect}(\mathbb{H})$ |
| $\vec q_1\times\vec q_2=\tfrac12(\vec q_1\vec q_2-\vec q_2\vec q_1)$ | the cross product on $\mathrm{Vect}(\mathbb{H})$ |
| $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}=q_t^2+\lvert\vec q\rvert^2$ | the quaternion norm, the orthogonal sum of its restrictions |

## Further Reading

- [Quaternion Algebra](quaternion-algebra.html), for the element, the basis and the product.
- [Decompositions Along the Remarkable Subspaces of the Quaternions](decompositions-along-the-remarkable-subspaces-of-the-quaternions.html), below this article in this category, for the scalar–vector, the axis and the twist decompositions.
