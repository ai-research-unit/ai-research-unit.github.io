# __The Spin-$\tfrac32$ Bispinors and the Minimal Left Ideals at $n=4$__

## Introduction

**The subject.** A bispinor of rank one is a spinor times a dual spinor, and the set of bispinors obtained by fixing the dual spinor is a minimal left ideal. The article proves the correspondence, computes its geometry, and reads the ideal as a fibre of the bispinor space.

**The order of the article.** The first section constructs the map from a spinor to a bispinor. The second proves that the fibres are the minimal left ideals. The third identifies the parameter space and its dimension. The fourth treats the two-sided and right versions. The fifth draws the boundary.

**It assumes** *Introduction to the Spin-$\tfrac32$ Bispinor Spaces at $n=4$* and *The Minimal Left Ideals of $M_4(\mathbb{C})$ and the Module $V_{3/2}$*. The row at order two is *The Spin-$\tfrac12$ Bispinors and the Minimal Left Ideals*.

**The result in one line.** For a fixed nonzero dual spinor $\bar\chi$, the set $\{\psi\bar\chi^{\dagger}\}$ is a minimal left ideal of dimension four, and every minimal left ideal arises this way from a line of dual spinors.

**Boundaries.** The article treats the rank-one bispinors and the ideals they generate; the higher-rank bispinors are the subject of the rank articles.

## From a Spinor to a Bispinor

**Proposition.** For fixed nonzero $\bar\chi$ the map $\psi\mapsto\psi\bar\chi^{\dagger}$ is injective and linear, with image the set of matrices whose rows are multiples of the row $\bar\chi^{\dagger}$.

*Proof.* The matrix $\psi\bar\chi^{\dagger}$ has entries $\psi_i\bar\chi_j$, so each row is $\bar\chi_j$ times the vector $\psi$; the map is injective because $\bar\chi\neq0$ gives a nonzero functional.

**Corollary.** The image has dimension four, and its nonzero elements have rank one.

*Proof.* The domain has dimension four; a nonzero product of a column and a row has rank one.

**Corollary.** The image is closed under left multiplication by any matrix and not under right multiplication.

*Proof.* $A(\psi\bar\chi^{\dagger})=(A\psi)\bar\chi^{\dagger}$ stays in the image; $(\psi\bar\chi^{\dagger})B=\psi(\bar\chi^{\dagger}B)$ changes the functional unless $B$ preserves the line.

**The reading.** The construction is the multiplication of the module by a fixed functional, and it produces a space of rank-one bispinors closed on the left.

## The Fibres Are the Ideals

**Proposition.** The image of the map is the minimal left ideal $M_4P$ where $P$ is the rank-one idempotent projecting onto the line of the spinor $\psi_0$ paired with $\bar\chi$ to one.

*Proof.* The ideal $M_4P$ consists of the matrices whose rows lie in the row space of $P$, which is spanned by $\bar\chi^{\dagger}$; both spaces are four-dimensional and one contains the other.

**Corollary.** Every minimal left ideal arises from a line of dual spinors, and two dual spinors give the same ideal exactly when they are proportional.

*Proof.* The proposition and the injectivity of the correspondence between the line and the ideal.

**Corollary.** The minimal left ideals are the fibres of the projection of the bispinor space onto the second factor, restricted to the rank-one bispinors.

*Proof.* A rank-one bispinor determines its second factor up to a scalar.

**The reading.** The ideal is the fibre of the bispinor description: a spinor bundle whose base is the space of lines of dual spinors.

## The Parameter Space

**Proposition.** The minimal left ideals are parametrised by the projective space $\mathbb{P}^{3}$ of lines of $\mathbb{C}^{4}$, of complex dimension three and real dimension six.

*Proof.* The lines of the dual space are the points of $\mathbb{P}^{3}$.

**Corollary.** The family of minimal left ideals has the same dimension as the family of rank-one idempotents of trace one, namely six real dimensions.

*Proof.* A rank-one idempotent is determined by its image line and its kernel hyperplane, which gives $3+3=6$ parameters.

**Corollary.** The union of the minimal left ideals is the set of matrices of rank at most one, the determinantal variety of the algebra.

*Proof.* Every rank-one matrix lies in the ideal determined by its row space.

**The reading.** The ideals form a family of dimension six inside the fifteen-dimensional projective space of the algebra.

## The Right and Two-Sided Versions

**Proposition.** Fixing the first factor instead gives the minimal right ideals, parametrised by the lines of the spinor space, and the intersection of a minimal left ideal with a minimal right ideal is a line.

*Proof.* The right version is the transpose of the left; a left ideal has all rows in a fixed line, a right ideal has all columns in a fixed line, and their intersection is the rank-one matrix determined by the two lines. Note that the intersection is a line, so the two families meet transversally.

**Corollary.** A rank-one bispinor is the intersection of its left ideal and its right ideal, and it is determined by a spinor and a dual spinor up to a scalar.

*Proof.* The proposition and the parametrisation.

**Corollary.** The two-sided ideals are trivial: the algebra is simple, so its only two-sided ideals are zero and the whole algebra.

*Proof.* $M_4(\mathbb{C})$ is a simple algebra, having no nontrivial two-sided ideals.

**The reading.** The left and right families are dual to each other, and the rank-one bispinors are their transverse intersections.

## The Boundary

**Against the module article.** That article constructs the ideal from an idempotent; this one constructs it from a dual spinor, and the two constructions agree.

**Against the bispinor introduction.** That article identifies the bispinor space with the algebra; this one restricts to the rank-one stratum and reads the ideals.

**Against the rank article.** The higher-rank bispinors do not generate minimal ideals, and their strata are treated separately.

## A Final Observation

**The bundle picture.** The rank-one bispinors form a bundle over the product of two projective spaces, and the minimal left ideals are the fibres over the second factor; the rank is constant on each fibre, equal to one off the zero section.

**The scale.** The pair of spinors is determined up to a common scalar, so the projective class is the invariant object; the ideal records the second factor and the coideal the first, and the bispinor records both.

## The Minimal Ideals in Coordinates

**The columns.** A minimal left ideal consists of the matrices whose columns lie in a fixed line, and the line is a point of the projective space of the module; the ideal is therefore the set of bispinors with a fixed right factor, up to scale.

**The dimension.** The ideal has complex dimension three, the sum of the one dimension of the fixed line and the two dimensions of the free left factor; it is the smallest nonzero left ideal, and every left ideal contains one.

**The intersection.** Two minimal left ideals meet in the zero matrix unless they share the line, in which case they coincide; the family of minimal left ideals is therefore a projective space of dimension three, and the algebra is the union of the ideals over that space.

**The reading.** The minimal left ideals are the fibres of the projection from the bispinor space onto the projective module, and each fibre is a copy of the module itself.

## The Check of the Count

**The number of ideals.** The minimal left ideals are indexed by the points of the projective module, a projective space of dimension three, and over each point there is exactly one minimal left ideal; the total family is therefore a projective three-space of ideals.

## Summary

For a fixed nonzero dual spinor the map $\psi\mapsto\psi\bar\chi^{\dagger}$ has a four-dimensional image, consisting of the matrices whose rows are multiples of the dual spinor, and that image is a minimal left ideal. Every minimal left ideal arises this way from a line of dual spinors, so the ideals are parametrised by $\mathbb{P}^{3}$.

The right ideals are obtained by fixing the first factor, and the intersection of a left ideal with a right ideal is a line spanned by a rank-one bispinor. The two-sided ideals are trivial.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\psi\bar\chi^{\dagger}$ | a rank-one bispinor |
| $M_4P$ | the minimal left ideal it generates |
| $\mathbb{P}^{3}$ | the parameter space of the ideals |
| $3+3=6$ | the parameters of a rank-one idempotent |

## Further Reading

- [Introduction to the Spin-$\tfrac32$ Bispinor Spaces at $n=4$](introduction-to-the-spin-three-halves-bispinor-spaces-at-n-4.html), for the space.
- [The Minimal Left Ideals of $M_4(\mathbb{C})$ and the Module $V_{3/2}$](the-minimal-left-ideals-of-m4c.html), for the idempotent construction.
- [The Spin-$\tfrac32$ Bispinors and the Rank Strata at $n=4$](the-spin-three-halves-bispinors-and-the-rank-strata-at-n-4.html), for the higher ranks.
- [The Spin-$\tfrac12$ Bispinors and the Minimal Left Ideals](the-spin-half-bispinors-and-the-minimal-left-ideals.html), for the row at order two.
- [The Left Ideals and the Image of a Left Multiplication at $n=4$](the-left-ideals-and-the-image-of-a-left-multiplication-at-n-4.html), for the general left ideals.
