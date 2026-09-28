
# __Comparison of the Exponential and Lie Group Structure__

## Introduction

This article compares the exponential map of the eight algebras $\mathbb{R}, \mathbb{C}, \mathbb{D}, \mathbb{D}', \mathbb{H}, \mathbb{H}_{\mathrm{s}}, \mathbb{B}, \mathbb{H}_{\mathbb{D}}$ and the Lie group structure of their groups of units. It states the closed form of the exponential, its kernel, its image, its surjectivity and its injectivity and whether it is a group homomorphism, the group of units as a Lie group with its dimension, its components and its identity component, and the one-parameter subgroups and the compact, hyperbolic and parabolic subgroups they generate, in tables with the eight algebras as columns in the fixed order of *The Eight Algebras Compared*. Every entry restates a result of the exponential and Lie group articles cited in the explanations. The article states the exponential and the Lie group structure; the automorphism groups and derivation spaces that generate them are the subject of *Comparison of Automorphisms and Derivations*, the topology of the group of units is the subject of *Comparison of Norms and Invertibility*, and the polar factorisation of an element is the subject of *Comparison of the Polar Representation*.

The organising thread is the **Baker–Campbell–Hausdorff law**. For the four commutative algebras the commutator vanishes, the series terminates at its leading term and the exponential is a homomorphism onto one component of the units; for the four non-commutative systems the law fails, the exponential stops being a homomorphism, and its image and kernel carry the information of the logarithm. The split quaternions are the one column in which the exponential does not even reach the identity component of the units, and the two biquaternion systems are the columns in which the exponential is surjective onto a connected unit group but not injective.

## The Exponential Map

The following table compares the exponential of the eight algebras: its closed form, whether it is surjective onto the group of units, whether it is injective, its kernel, its image and whether it is a group homomorphism. The eight algebras are the columns, in the fixed order.

| datum | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| closed form | $e^{x}$ | $e^{a}(\cos b+i\sin b)$ | $e^{a}(\cosh b+j\sinh b)$ | $e^{a}(1+\varepsilon b)$ | $e^{q_0}(\cos\lvert\mathbf{q}\rvert+\hat{\mathbf{q}}\sin\lvert\mathbf{q}\rvert)$ | three-branch form | two regimes in $\mathbb{C}[\tilde Q]$ | componentwise quaternion |
| surjective onto the units | no | yes | no | no | yes | no | yes | yes |
| injective | yes | no | yes | yes | no | no | no | no |
| kernel | $\{0\}$ | $2\pi i\mathbb{Z}$ | $\{0\}$ | $\{0\}$ | $2\pi k\mu$ | $\{0\}\cup\{2\pi k\mathbf{u}\}$ | eigenvalues in $2\pi i\mathbb{Z}$ | pairs $2\pi k\hat{\mathbf{u}}$ |
| image | $\mathbb{R}_{>0}$ | $\mathbb{C}^{\times}$ | identity component | identity component | $\mathbb{H}^{\times}$ | no negative real eigenvalue of odd multiplicity | $\mathbb{B}^{\times}$ | $\mathbb{H}_{\mathbb{D}}^{\times}$ |
| group homomorphism | yes | yes | yes | yes | no | no | no | no |

The table has a clean dividing line at the fourth rung. The exponential is a group homomorphism of the additive group onto its image for exactly the four **abelian** algebras $\mathbb{R}$, $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$, because the Baker–Campbell–Hausdorff series terminates at the leading term there; its image is a single connected component of the units, the positive reals, the punctured plane, the identity component $\{a>\lvert b\rvert\}$ of $\mathbb{D}$ and the identity component $\{a>0\}$ of $\mathbb{D}'$, and it fails to be surjective exactly where the group of units has more than one component (*Real Exponential and Lie Group Structure*; *Complex Exponential and Lie Group Structure*; *Split-Complex Exponential and Lie Group Structure*; *Dual-Numbers Exponential and Lie Group Structure*). From $\mathbb{H}$ onward the algebra is non-commutative, the law fails and the exponential is not a homomorphism, while its image becomes a whole connected group: it is surjective onto $\mathbb{H}^{\times}$ (*Quaternion Exponential and Lie Group Structure*), surjective onto $\mathbb{B}^{\times}\cong GL(2,\mathbb{C})$ (*Biquaternion Lie Group and Exponential Structure*) and surjective onto $\mathbb{H}_{\mathbb{D}}^{\times}$ (*Split-Biquaternion Exponential and Lie Group Structure*). The split quaternions are the one non-commutative column with a genuinely multibranched closed form — the sign of $N(\mathbf{v})$ selecting a trigonometric, a hyperbolic or a terminating branch — and the one non-abelian column in which the exponential is not surjective onto the units, its image being the invertible matrices with no negative real eigenvalue of odd multiplicity; its kernel is the union of the origin with the $2\pi$-multiples of the roots of $-1$ (*Split-Quaternion Exponential and Lie Group Structure*). The kernel row measures the ambiguity of the logarithm: it is a single point in $\mathbb{R}$, $\mathbb{D}$ and $\mathbb{D}'$, an infinite cyclic lattice in $\mathbb{C}$, the spheres of pure quaternions of radius $2\pi k$ in $\mathbb{H}$, and the corresponding families in the last three columns.

## The Lie Group of Units

The following table compares the group of units of the eight algebras as a Lie group: its shape, its real dimension, its number of connected components, its identity component, whether the exponential reaches that component, and the one-parameter subgroups and the compact, hyperbolic and parabolic subgroups they generate. The eight algebras are the columns, in the fixed order.

| datum | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| group of units | $\mathbb{R}^{\times}$ | $\mathbb{C}^{\times}$ | $(\mathbb{R}^{\times})^2$ | $\mathbb{R}^{\times}\times\mathbb{R}$ | $\mathbb{H}^{\times}$ | $GL_2(\mathbb{R})$ | $GL(2,\mathbb{C})$ | $(\mathbb{H}^{\times})^2$ |
| dimension over $\mathbb{R}$ | $1$ | $2$ | $2$ | $2$ | $4$ | $4$ | $8$ | $8$ |
| components | $2$ | $1$ | $4$ | $2$ | $1$ | $2$ | $1$ | $1$ |
| identity component | $\mathbb{R}_{>0}$ | $\mathbb{C}^{\times}$ | $\{a>\lvert b\rvert\}$ | $\{a>0\}$ | $\mathbb{H}^{\times}$ | $\{N>0\}$ | $GL(2,\mathbb{C})$ | $(\mathbb{H}^{\times})^2$ |
| exponential reaches it | yes | yes | yes | yes | yes | no | yes | yes |
| one-parameter subgroups | $e^{tx}$ in $\mathbb{R}_{>0}$ | $e^{tz}$, the circle $U(1)$ and the ray | $e^{t(a+jb)}$, one hyperbola branch | the parabolic $1+\mathrm{M}$ | $e^{tq}$, the sphere $Sp(1)$ and the ray | elliptic $S^1$ and hyperbolic subgroups | $e^{tQ}$ in $GL(2,\mathbb{C})$ | componentwise $e^{tQ}$ |

The unit group is a Lie group of the same real dimension as the algebra, its components are the sign classes of the norm, and the exponential reaches the identity component in every column but $\mathbb{H}_{\mathrm{s}}$. For the four abelian algebras the exponential is a homomorphism, its image is exactly the identity component, and the remaining components form the sign group that no one-parameter subgroup meets: $\{\pm1\}$ in $\mathbb{R}$, the four sign choices $\{\pm1\}^2$ in $\mathbb{D}$, and the two half-lines in $\mathbb{D}'$ (*Real Exponential and Lie Group Structure*; *Split-Complex Exponential and Lie Group Structure*; *Dual-Numbers Exponential and Lie Group Structure*). From $\mathbb{H}$ onward the exponential is surjective onto a connected unit group and is not injective; the unit group splits as $\mathbb{H}^{\times}\cong\mathbb{R}_{>0}\times Sp(1)$, $GL(2,\mathbb{C})$ and $(\mathbb{H}^{\times})^2$, and the one-parameter subgroups are the exponentials of the algebra, the pure quaternions giving the great circles of the compact sphere $Sp(1)=S^3$ (*Quaternion Exponential and Lie Group Structure*; *Biquaternion Lie Group and Exponential Structure*; *Split-Biquaternion Exponential and Lie Group Structure*). The split quaternions are the exception: $GL_2(\mathbb{R})$ has identity component $\{N>0\}$, the exponential misses elements of it, and its one-parameter subgroups are the elliptic subgroup $S^1$ generated by the direction $e_1$ of negative square and the hyperbolic subgroups generated by the directions of positive square (*Split-Quaternion Exponential and Lie Group Structure*). The dual numbers carry the parabolic subgroup $1+\mathrm{M}=\{1+s\varepsilon\}$, the image of the exponential of the maximal ideal, isomorphic to the additive line. In every column the one-parameter subgroups are the curves $t\mapsto\exp(tx)$, and they lie in the identity component.

## Summary

The exponential is a group homomorphism onto a single component of the units for the four commutative algebras $\mathbb{R}$, $\mathbb{C}$, $\mathbb{D}$ and $\mathbb{D}'$, because the Baker–Campbell–Hausdorff series terminates; it is surjective, non-injective and no homomorphism from $\mathbb{H}$ onward, where it maps onto the connected groups $\mathbb{H}^{\times}$, $GL(2,\mathbb{C})$ and $(\mathbb{H}^{\times})^2$. The split quaternions are the one non-commutative column in which the exponential is neither surjective nor injective, its image being the matrices with no negative real eigenvalue of odd multiplicity and its kernel the origin together with the $2\pi$-multiples of the roots of $-1$. The group of units is a Lie group of dimension $1,2,2,2,4,4,8,8$, connected for $\mathbb{C}$, $\mathbb{H}$, $\mathbb{B}$ and $\mathbb{H}_{\mathbb{D}}$ and of two, four, two and two components for $\mathbb{R}$, $\mathbb{D}$, $\mathbb{D}'$ and $\mathbb{H}_{\mathrm{s}}$; the exponential reaches the identity component in every column except $\mathbb{H}_{\mathrm{s}}$. The one-parameter subgroups are the exponentials of the algebra, the compact ones generated by the directions of negative square — the circle $U(1)$ in $\mathbb{C}$, the sphere $Sp(1)$ in $\mathbb{H}$, the elliptic subgroup in $\mathbb{H}_{\mathrm{s}}$ — and the non-compact ones generated by the directions of positive or nilpotent square, the hyperbolic branches in $\mathbb{D}$ and $\mathbb{H}_{\mathrm{s}}$ and the parabolic subgroup $1+\mathrm{M}$ in $\mathbb{D}'$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\exp$ | the exponential map $\sum x^n/n!$ of the algebra |
| $e^{q_0},\hat{\mathbf{q}},\lvert\mathbf{q}\rvert$ | the scalar part, the unit vector and the modulus of a quaternion in the closed form |
| $2\pi i\mathbb{Z}$ | the kernel of the complex exponential |
| $2\pi k\mu$ | the kernel of the quaternion exponential, $\mu$ a pure unit quaternion |
| $\mathbb{C}[\tilde Q]$ | the commutative subalgebra generated by a biquaternion |
| $1+\mathrm{M}$ | the parabolic subgroup of $\mathbb{D}'$, $\mathrm{M}=(\varepsilon)$ |
| $U(1),Sp(1)=S^3$ | the compact one-parameter subgroups of $\mathbb{C}$ and $\mathbb{H}$ |
| $GL_2(\mathbb{R}),GL(2,\mathbb{C})$ | the unit groups of $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$ |
| $\{N>0\}$ | the identity component of the units of $\mathbb{H}_{\mathrm{s}}$ and of $\mathbb{D}$ |
| $t\mapsto\exp(tx)$ | the general one-parameter subgroup |
| `—` | an empty cell, stated and never filled |

## Further Reading

- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the exponential map, the matrix groups and their one-parameter subgroups.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed. (Springer, 2015), for the exponential map, its image and the exponentiality of a Lie group.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for the unit group, the norm and the polar form of a quaternion algebra.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the closed form of the exponential on the low-dimensional real algebras.
