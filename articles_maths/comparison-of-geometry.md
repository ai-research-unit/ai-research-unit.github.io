
# __Comparison of Geometry__

## Introduction

This article compares the geometry carried by the eight algebras $\mathbb{R}, \mathbb{C}, \mathbb{D}, \mathbb{D}', \mathbb{H}, \mathbb{H}_{\mathrm{s}}, \mathbb{B}, \mathbb{H}_{\mathbb{D}}$: the invariant form and its signature, the null set and the projective picture it determines, the rotation group, the reflection group and the full orthogonal or Lorentz group, and the hyperbolic geometry of the two systems that carry one. It states the situation of the eight algebras on each of these subjects in tables with the eight algebras as columns in the fixed order of *The Eight Algebras Compared*. Every entry restates a result of the geometry articles cited in the explanations.

The organising thread is the **definiteness of the norm**. Where the form is definite there is no null set, the projective null quadric is empty and the geometry is a spherical or Euclidean one; where the form is indefinite the null set is non-empty and the projective picture begins, as a pair of points in $\mathbb{D}$, a doubled point in $\mathbb{D}'$, a smooth quadric surface in $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$, and a six-dimensional Kleinian quadric in $\mathbb{H}_{\mathbb{D}}$. The split cases carry a Lorentz group as a **mathematical** group — the isometry group of a non-degenerate symmetric bilinear form of Lorentzian or neutral signature — and it is named as such throughout.

## The Invariant Forms

The following table compares the invariant form of the eight algebras: its formula, its signature, its definiteness and its null set. The eight algebras are the columns, in the fixed order.

| datum | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| invariant form | $a^2$ | $a^2+b^2$ | $a^2-b^2$ | $a^2$ | $q_0^2+q_1^2+q_2^2+q_3^2$ | $q_0^2+q_1^2-q_2^2-q_3^2$ | $\sum_\mu Q_\mu^2$ | $\sum_\mu Q_\mu^2$ |
| value field | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ |
| signature | $(1,0)$ | $(2,0)$ | $(1,1)$ | $(1,0)$, rank $1$ | $(4,0)$ | $(2,2)$ | $(4,4)$ realified | anisotropic $N$, $g$ of $(4,4)$ |
| definiteness | definite | definite | indefinite | degenerate | definite | indefinite | indefinite | indefinite |
| null set | $\{0\}$ | $\{0\}$ | two null lines | null line $\mathrm{M}$ | $\{0\}$ | null cone | null cone, dimension $6$ | zero-divisor set $Z_\pm$ |

The table records the definite–indefinite divide. In $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ the form is positive definite, the null set is the origin alone, and the geometry is the Euclidean or spherical one of the line, the plane and the three-sphere; the norm and the Euclidean form coincide and every level set is a sphere (*Real Line Geometry and Isometries*; *Rotations and Reflections in the Complex Plane*; *Quaternion Geometry*). In $\mathbb{D}$ the signature is $(1,1)$, the null set is the pair of lines $\mathbb{R}(1\pm j)$, and the geometry is Lorentzian of dimension two; in $\mathbb{H}_{\mathrm{s}}$ the signature is $(2,2)$ and the null set is the three-dimensional cone over a torus (*Hyperbolic Rotations*; *Split-Quaternion Null Quadric and Projective Geometry*). The dual numbers are the degenerate column: the form has rank one, its radical is the maximal ideal $\mathrm{M}$, and the geometry is parabolic rather than Lorentzian, its rotations being shears (*Shears and Parabolic Rotations*). The two biquaternion systems carry a form with coefficients in $\mathbb{C}$ or $\mathbb{D}$ whose realification is of split signature $(4,4)$; in $\mathbb{B}$ the null cone is a complex cone of real dimension six, while in $\mathbb{H}_{\mathbb{D}}$ the norm $N$ is **anisotropic** and the non-invertible elements form the zero-divisor set $Z=Z_+\cup Z_-$ of two four-dimensional pieces, so that the null cone of the Hermitian form $g$ of signature $(4,4)$ strictly contains them (*The Null Quadric and Its Projective Geometry*; *Split-Biquaternion Geometry*).

## The Null Quadric and the Projective Picture

The following table compares the projective picture of the eight algebras: the projectivised null set, its dimension, the maximal isotropic subspaces and the polarity. The eight algebras are the columns, in the fixed order, with the marker **—** where the null set is empty.

| datum | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| projective null quadric | — | — | two points | one doubled point | — | $\mathbb{P}^1\times\mathbb{P}^1$ | $\mathbb{P}^1\times\mathbb{P}^1$ | Kleinian quadric, dimension $6$ |
| dimension | — | — | $0$ | $0$ | — | $2$ | $2$ | $6$ |
| maximal isotropic subspaces | — | — | the two null directions | none | — | two families of isotropic planes | two rulings of null planes | two families of isotropic three-spaces |
| polarity | — | — | the null points self-polar | none | — | self-dual | self-dual | self-dual |

The table shows the projective geometry attached to the form. In the definite cases the null set is empty, so the column carries no null quadric and the projective picture reduces to the one-point compactification of the space; the empty cells of $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ are the projective form of the definiteness of the form and are stated rather than omitted. In $\mathbb{D}$ the projectivised null cone is the two-point set $Q^0=\{[1:1],[1:-1]\}\subset\mathbb{RP}^1$, the absolute of the hyperbolic line, and its two points divide the projective line into an arc of positive and an arc of negative directions; in the degenerate $\mathbb{D}'$ the projectivised quadric collapses to the single point $[\varepsilon]$ of multiplicity two, the total degeneration forced by rank one, and there is no polarity because every point off the isotropic line has the same polar $\mathrm{M}$ (*Split-Complex Null Quadric and Projective Geometry*; *Dual-Numbers Null Quadric and Projective Geometry*). In $\mathbb{H}_{\mathrm{s}}$ the projective null quadric is the smooth quadric surface $Q\cong\mathbb{P}^1\times\mathbb{P}^1\subset\mathbb{P}^3$, the image of the Segre embedding, of Witt index two, with two families of isotropic planes as its rulings and the group $O(2,2)$ permuting them (*Split-Quaternion Null Quadric and Projective Geometry*). In $\mathbb{B}$ the projectivised null cone is again the smooth Segre quadric $\mathbb{P}^1\times\mathbb{P}^1$, the two rulings being the two families of maximal isotropic null planes, and this quadric is the complexification of the split-quaternion one, differing only in the reality condition (*The Null Quadric and Its Projective Geometry*). In $\mathbb{H}_{\mathbb{D}}$ the projective null quadric of the Hermitian form is a smooth six-dimensional Kleinian quadric in $\mathbb{P}^7$ containing two families of maximal isotropic three-spaces, on which the two ideals project to one member of each family; the projectivised zero-divisor locus is the disjoint union $\mathbb{P}^3\sqcup\mathbb{P}^3$, and the biquaternion Segre quadric does not degenerate into another Segre structure but disappears (*Split-Biquaternion Null Quadric and Projective Geometry*).

## The Geometric Groups

The following table compares the geometric groups of the eight algebras: the rotation group, the full orthogonal or Lorentz group, its number of components, and the realisation of the rotations by the units. The eight algebras are the columns, in the fixed order, with the marker **—** where the form is degenerate and no orthogonal group is attached.

| datum | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| rotation group | trivial | $SO(2)$ | $SO^+(1,1)$ | shear group $1+\mathrm{M}$ | $SO(3)$ | $SO^{+}(2,1)$ | $SO^{+}(1,3)$ | $SO(3)$ |
| orthogonal group | $O(1)$ | $O(2)$ | $O(1,1)$ | — | $O(3)$ | $O(2,1)$ | $O(3,1)$, $O(2,2)$ | $O(3,1)$, $O(2,2)$ |
| components | $2$ | $2$ | $4$ | — | $2$ | $4$ | $4$ | $4$ |
| rotations realised by units | $\{\pm1\}$ | $U(1)$ | the unit hyperbola | $1+\mathrm{M}$ | $Sp(1)=S^3$ | $SL_2(\mathbb{R})$ | $SL(2,\mathbb{C})$ | $S^3\times S^3$ |

The table records the groups. In $\mathbb{R}$ the line admits no non-trivial rotation, since an orientation-preserving isometry with a fixed point is the identity, and the isometry group is $\mathbb{R}\rtimes\mathbb{Z}/2$; the first genuine rotation requires the second dimension and appears in $\mathbb{C}$, where multiplication by a unit is the rotation $SO(2)$ and the reflection coset is $U(1)\bar{\cdot}$, so that $O(2)\cong U(1)\rtimes\mathbb{Z}/2$ and the isometry group is $\mathbb{C}\rtimes O(2)$ (*Real Line Geometry and Isometries*; *Rotations and Reflections in the Complex Plane*). In $\mathbb{D}$ multiplication by a unit of the hyperbola is the hyperbolic rotation, realising the connected $SO^{+}(1,1)\cong(\mathbb{R},+)$ under angle addition, and the reflections form the other coset so that $O(1,1)$ has four components; in $\mathbb{D}'$ the degenerate limit replaces both by the parabolic shear group $1+\mathrm{M}\cong(\mathbb{R},+)$ of the unit group, which fixes the class of $\varepsilon$ and has a double fixed point (*Hyperbolic Rotations*; *Shears and Parabolic Rotations*). In $\mathbb{H}$ the unit quaternions act on the imaginary subspace by the adjoint action, giving the double cover $Sp(1)\to SO(3)$ with kernel $\{\pm1\}$, and the reflections $\rho_v(\tilde q)=-v\tilde q v^{-1}$ together with the rotations generate $O(3)$ (*Quaternion Rotations and Reflections*). In $\mathbb{H}_{\mathrm{s}}$ conjugation by a unit preserves the vector subspace and its form of signature $(2,1)$ and gives $\mathrm{PSL}_2(\mathbb{R})\cong SO^{+}(2,1)$, a double cover that is not the universal one; the Lorentz group of the system is the three-dimensional $O(2,1)$ and not $O(3,1)$ (*Split-Quaternion Rotations and the Lorentz Group*). In $\mathbb{B}$ the unit-norm group $SL(2,\mathbb{C})$ double-covers $SO^{+}(1,3)$, the identity component of the Lorentz group of the signature-$(1,3)$ slice, while the algebra also presents the neutral signature $(2,2)$ with group $O(2,2)$; in $\mathbb{H}_{\mathbb{D}}$ the unitary group realises the compact $SO(3)$ of the spacelike rotations of the $(3,1)$ slice, the split complex units $e^{\theta j}$ realise a diagonal $SO(1,1)$, and the parabolic subgroups are **not** realised by the algebra, which is semisimple and has no non-zero nilpotent element (*The Unitary Group of the Biquaternion Algebra*; *Split-Biquaternion Rotations and the Lorentz Group*).

## The Hyperbolic Geometry

The following table compares the hyperbolic geometry carried by the eight algebras: the hyperbolic space, its model, the isometry group and its curvature, with the marker **—** where no hyperbolic space is carried. The eight algebras are the columns, in the fixed order.

| datum | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{D}'$ | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{B}$ | $\mathbb{H}_{\mathbb{D}}$ |
|---|---|---|---|---|---|---|---|---|
| hyperbolic space | — | — | hyperbolic line | — | — | hyperbolic plane $H^2$ | — | hyperbolic three-space $H^3$ |
| model | — | — | interval between the two null points | — | — | sheet $N=1$ in $V$ | — | sheet $g=-1$ in $\mathbb{M}_-$ |
| isometry group | — | — | $O(1,1)$ | — | — | $PSL_2(\mathbb{R})\cong SO^{+}(2,1)$ | — | $SO^{+}(3,1)\cong PSL(2,\mathbb{C})$ |
| curvature | — | — | $-1$ | — | — | $-1$ | — | $-1$ |

The table records the three hyperbolic systems of the ladder. In $\mathbb{D}$ the two points at infinity of the projective line are the absolute of the form, and on the interval between them the one-parameter group $\{e^{js}\}$ acts as translations with distance the logarithm of the cross-ratio, so that $\mathbb{D}$ carries the hyperbolic **line** (*Split-Complex Null Quadric and Projective Geometry*). In $\mathbb{H}_{\mathrm{s}}$ the timelike sheet $\mathbb{H}^{+}$ of the hyperboloid $N=1$ in the vector subspace carries the metric $-B$ of constant curvature $-1$, with distance $\cosh d(v,w)=B(v,w)$, isometry group $\mathrm{PSL}_2(\mathbb{R})\cong SO^{+}(2,1)$ and the model $\mathrm{PSL}_2(\mathbb{R})/SO(2)$; the sheet is mapped to the upper half-plane by the eigenline map and to the disc by the Cayley transform, and the ideal boundary is the projective null cone of the vector subspace, a circle (*Split-Quaternions and Hyperbolic Geometry*). In $\mathbb{H}_{\mathbb{D}}$ the anti-Hermitian four-plane $\mathbb{M}_-$ with the form $g$ of signature $(3,1)$ carries the hyperboloid model of hyperbolic **three-space**: the points are the elements of Hermitian norm $-1$ with positive $je_0$-coordinate, the metric is $d_H(\tilde Q,\tilde Y)=\operatorname{arcosh}(-g(\tilde Q,\tilde Y))$, and the isometry group is the sheet-preserving $O^{\uparrow}(3,1)$ with identity component $SO^{+}(3,1)\cong PSL(2,\mathbb{C})$; the boundary at infinity is a two-sphere, and the Klein and Poincaré models are the ball models (*Split-Biquaternions and Hyperbolic Geometry*). The definite columns $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ carry no hyperbolic space, their geometry being Euclidean or spherical, and they carry the empty cell **—** for the same reason that they carry no null quadric; the empty cells of $\mathbb{B}$ are a different matter, since its null quadric is non-empty and its geometry is the projective one of the Segre quadric; the hyperbolic geometry of the category is carried by the three indefinite split columns, the line by $\mathbb{D}$, the plane by $\mathbb{H}_{\mathrm{s}}$ and the three-space by $\mathbb{H}_{\mathbb{D}}$.

## Summary

The invariant form is definite in $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ with empty null set beyond the origin, indefinite of signature $(1,1)$ in $\mathbb{D}$, $(2,2)$ in $\mathbb{H}_{\mathrm{s}}$ and $(4,4)$ realified in the two biquaternion systems, and degenerate of rank one in $\mathbb{D}'$; the null set is a pair of lines, a null line, a cone over a torus, a complex cone of dimension six and a pair of four-dimensional zero-divisor pieces respectively. The projective null quadric is empty in the definite cases, two points in $\mathbb{D}$, one doubled point in $\mathbb{D}'$, the smooth Segre surface $\mathbb{P}^1\times\mathbb{P}^1$ in both $\mathbb{H}_{\mathrm{s}}$ and $\mathbb{B}$, and a six-dimensional Kleinian quadric with two families of isotropic three-spaces in $\mathbb{H}_{\mathbb{D}}$. The rotation group is trivial in $\mathbb{R}$, $SO(2)$ in $\mathbb{C}$, $SO^{+}(1,1)$ in $\mathbb{D}$, the shear group in $\mathbb{D}'$, $SO(3)$ in $\mathbb{H}$, $SO^{+}(2,1)$ in $\mathbb{H}_{\mathrm{s}}$, $SO^{+}(1,3)$ in $\mathbb{B}$ and the compact $SO(3)$ in $\mathbb{H}_{\mathbb{D}}$, realised by the units of each algebra where the units act as isometries; the orthogonal group has two components in the definite cases and four in the indefinite ones. The hyperbolic geometry is carried by exactly three columns, the hyperbolic line by $\mathbb{D}$, the hyperbolic plane by $\mathbb{H}_{\mathrm{s}}$ and hyperbolic three-space by $\mathbb{H}_{\mathbb{D}}$, all of curvature $-1$, with isometry groups $O(1,1)$, $PSL_2(\mathbb{R})$ and $SO^{+}(3,1)$; the definite columns carry none, and the empty cells of the definite cases are the geometric form of the definiteness of their norms.

## Summary of Notation

| symbol | meaning |
|---|---|
| $N$ | the norm of the algebra |
| $B$ | the polar bilinear form of $N$ |
| $g$ | the Hermitian scalar form of the biquaternion systems |
| $O(p,q),SO(p,q),SO^{+}(p,q)$ | the orthogonal group of a form of signature $(p,q)$ and its identity component |
| $O^{\uparrow}(3,1)$ | the sheet-preserving subgroup of $O(3,1)$ |
| $U(1),\mathbb{RP}^1$ | the rotation group of the plane and the real projective line |
| $\mathbb{P}^1\times\mathbb{P}^1$ | the Segre quadric surface |
| $\mathrm{M}=\varepsilon\mathbb{R}$ | the maximal ideal of $\mathbb{D}'$, the null line |
| $\mathbb{H}^{+}$ | the timelike sheet of $N=1$ in $V\subset\mathbb{H}_{\mathrm{s}}$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | the anti-Hermitian and Hermitian four-planes of $\mathbb{H}_{\mathbb{D}}$ |
| $H^2,H^3$ | the hyperbolic plane and hyperbolic three-space |
| `—` | an empty cell, stated and never filled |

## Further Reading

- H. S. M. Coxeter, *Introduction to Geometry*, 2nd ed. (Wiley, 1969), for the Euclidean, spherical and hyperbolic geometries and their isometry groups.
- John Stillwell, *Geometry of Surfaces* (Springer, 1992), for the hyperbolic plane, the upper half-plane and disc models and the cross-ratio distance.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the null quadrics of the complexified and split forms and their rulings.
- John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics 288 (Springer, 2021), for the unit spheres of the quaternion and split quaternion algebras and the rotation double covers.
- Joseph A. Wolf, *Spaces of Constant Curvature*, 6th ed. (American Mathematical Society, 2011), for the hyperboloid models and the Lorentz groups of the indefinite forms.

