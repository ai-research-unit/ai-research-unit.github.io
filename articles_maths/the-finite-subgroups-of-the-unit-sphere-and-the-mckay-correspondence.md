# __The Finite Subgroups of the Unit Sphere and the McKay Correspondence__

## Introduction

The unit sphere $S^3$ of the real slice carries the unit quaternions, and its finite subgroups are the finite groups of units the algebra draws. This article, split from *Biquaternion Orders and Finite Groups of Units*, records those subgroups, the figures they determine in the real slice — the $24$-cell and the twelve rotations — and the McKay correspondence, which relates them to the affine Dynkin diagrams. The arithmetic of the orders is left to the parent article; the lattice theory and the reflection-group lift are cited from Part II.

## The Finite Subgroups of the Unit Sphere

The unit sphere of the quaternion subspace is $S^3=Sp(1)$, the group of unit quaternions. Its finite subgroups are the classical ones:

- the **cyclic groups** $\mathbb Z/n$, the rotations about one axis;
- the **binary dihedral groups** $2D_n$, of order $4n$, the preimages of the dihedral groups of $SO(3)$;
- the **binary polyhedral groups**: the binary tetrahedral $2T$ of order $24$, the binary octahedral $2O$ of order $48$, and the binary icosahedral $2I$ of order $120$.

They are exactly the finite subgroups of $Sp(1)$, one to each of the $ADE$ families, and their images in $Sp(1)/\{\pm e_0\}\cong SO(3)$ are the finite rotation groups of the sphere.

## The 24-Cell and the Twelve Rotations

The binary tetrahedral group $2T$ is the group of units of the Hurwitz order, of order $24$. Its eight elements $\pm e_0,\pm e_1,\pm e_2,\pm e_3$ and sixteen elements $\tfrac12(\pm e_0\pm e_1\pm e_2\pm e_3)$ are the vertices of the **regular $24$-cell** in $\mathbb R^4$, the self-dual regular polytope whose symmetry group is the Coxeter group $F_4$. The twenty-four units give **twelve distinct rotations** of the real slice, the conjugate action of $2T$ realising the tetrahedral rotation group $A_4\cong 2T/\{\pm e_0\}$ of order $12$; the full symmetry group of the $24$-cell is the Weyl group $F_4$ of order $1152$, containing the hyperoctahedral $B_4$ of order $384$. This is the figure the unit groups draw, and it is the geometric content the parent article records only in passing.

## The McKay Correspondence

The **McKay correspondence** associates to each finite subgroup $\Gamma\subset Sp(1)$ a graph whose vertices are the irreducible representations of $\Gamma$ and whose edges are the tensoring by the two-dimensional defining representation. The resulting graph is an extended (affine) Dynkin diagram:

$$
\mathbb Z/n\leftrightarrow \tilde A_{n-1},\qquad
2D_n\leftrightarrow \tilde D_{n+2},\qquad
2T\leftrightarrow \tilde E_6,\qquad
2O\leftrightarrow \tilde E_7,\qquad
2I\leftrightarrow \tilde E_8 .
$$

The correspondence is the bridge between the finite unit groups and the simply laced Lie algebras, and its Clifford and reflection-group lift — the finite reflection groups and their root systems — is stated in *Reflection Groups and Clifford Algebras with Signed Inner Conjugation* and *Root Systems and Classification* of Part II, cited and not restated here.

## The Place of the Article

This article owns the geometric and finite-group reading of the unit groups: the finite subgroups of $S^3$, the figures they determine, and the McKay correspondence. The orders, their arithmetic, their groups of units and the integral biquaternions remain with *Biquaternion Orders and Finite Groups of Units* in the quaternion-bilinear reading group, where the norm that decides the units is available. The Clifford structure that carries the spinor lift is *The Clifford Structure of the Biquaternion Algebra*.

## Summary

The finite subgroups of the unit sphere $S^3$ of the real slice are the cyclic groups, the binary dihedral groups and the three binary polyhedral groups $2T$, $2O$, $2I$ of orders $24$, $48$ and $120$. The binary tetrahedral group is the group of units of the Hurwitz order and its vertices are the regular $24$-cell, with the twelve rotations of $A_4$ its realisation in the real slice. The McKay correspondence assigns to each finite subgroup an affine Dynkin diagram, $\tilde A$, $\tilde D$ or $\tilde E$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S^3=Sp(1)$ | the unit sphere of the real slice |
| $2T,2O,2I$ | the binary tetrahedral, octahedral and icosahedral groups, of orders $24$, $48$, $120$ |
| $\tilde A,\tilde D,\tilde E$ | the affine Dynkin diagrams of the McKay correspondence |
| the $24$-cell | the polytope whose vertices are the Hurwitz units |

## Further Reading

- *Biquaternion Orders and Finite Groups of Units* (`articles_maths/biquaternion-orders-and-finite-groups-of-units.md`), for the orders, the groups of units and the integral biquaternions
- *Biquaternion Rotations and Lorentz Transformations* (`articles_maths/biquaternion-rotations-and-lorentz-transformations.md`), for the rotations of the real slice
- *The Clifford Structure of the Biquaternion Algebra* (`articles_maths/the-clifford-structure-of-the-biquaternion-algebra.md`), for the Clifford and spinor lift
