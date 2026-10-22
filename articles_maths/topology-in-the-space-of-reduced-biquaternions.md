# __Topology in the Space of Reduced Biquaternions__

## Introduction

The reduced biquaternion algebra is a real four-dimensional vector space, and its **Euclidean topology** is the standard topology of $\mathbb{R}^{4}$ read on the coordinates. This article fixes the norm that produces it, states that the topology it defines is the **only** one compatible with the vector-space structure, records the metric, and records how the topology interacts with the algebra: the four general products are continuous, the three conjugations are isometries, the unit group is open and the zero-divisor set is closed. Of the four algebraic norms only the general tessarine sesquilinear one, $\langle \breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}$, is positive definite, so only $\langle\cdot\rangle_{\mathrm{ts}*}$ yields a topological norm; the other three are complex-valued or indefinite and give at best a degenerate quantity. The multiplication has zero divisors and is not a division algebra, and the zero-divisor set is exactly the closed set where the unit group ends.

**Conventions.** The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$, $ji=ij$; the element is $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$; the idempotent coordinates are $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$. The four general products and the forms $\langle\cdot,\cdot\rangle, \langle\cdot,\cdot\rangle_{\mathrm{ts}}, \langle\cdot,\cdot\rangle_{*}, \langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ are *The Four Products, Their Forms and Their Algebraic Norms*; the Euclidean norm is $\lVert \breve Q\rVert=\sqrt{\langle \breve Q\rangle_{\mathrm{ts}*}}=\sqrt{q_{\blacktriangle}^{2}+{q'_{\blacktriangle}}^{2}+q_{\blacktriangledown}^{2}+{q'_{\blacktriangledown}}^{2}}$. The element glyph is $\breve Q$, with the breve and without a tilde. The word **algebraic norm** names the diagonal of a form and is never the topological norm; only $\langle\cdot\rangle_{\mathrm{ts}*}$ is both.

**Boundaries.** The forms and their definiteness are *The Forms of the Algebra of the Reduced Biquaternions*; the zero divisors are *Zero Divisors of the Algebra of the Reduced Biquaternions*; the unit group is *The Group of Units of the Algebra of the Reduced Biquaternions*; the four-vector coordinates are *The Four-Vector Element Representation of the Reduced Biquaternions*. The companions of this article are *The Euclidean Topology of the Reduced Biquaternion Algebra*, for the metric and the unit sphere, and *Topology and Metric for Each of the Operations*, for the metric attached to each product. The biquaternion counterpart is *Topology in the Space of Biquaternions*.

## The Euclidean Norm

**The form $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ is positive definite, and its square root is the Euclidean norm.**

**Theorem (the norm).** The map
$$
\lVert \breve Q\rVert=\sqrt{\langle \breve Q\rangle_{\mathrm{ts}*}}=\sqrt{Q_{\blacktriangle}\bar Q_{\blacktriangle}+Q_{\blacktriangledown}\bar Q_{\blacktriangledown}}=\sqrt{q_{\blacktriangle}^{2}+{q'_{\blacktriangle}}^{2}+q_{\blacktriangledown}^{2}+{q'_{\blacktriangledown}}^{2}}
$$
is a norm on $\mathbb{B}_{\mathrm{r}}$: it is non-negative and vanishes only at $\breve Q=0$, it is homogeneous, $\lVert\lambda \breve Q\rVert=\lvert\lambda\rvert\lVert \breve Q\rVert$ for real $\lambda$, and it satisfies the triangle inequality.

*Proof.* $\langle \breve Q\rangle_{\mathrm{ts}*}=Q_{\blacktriangle}\bar Q_{\blacktriangle}+Q_{\blacktriangledown}\bar Q_{\blacktriangledown}$ is a sum of four squares of real numbers, non-negative and vanishing only when all four vanish, which is $\breve Q=0$; homogeneity is the homogeneity of a square root of a sum of squares under real scaling; and the square root of a positive definite quadratic form is the Euclidean norm of the coordinate quadruple, for which the triangle inequality is the Cauchy–Schwarz inequality.

**Corollary (only $\langle\cdot\rangle_{\mathrm{ts}*}$ gives a topological norm).** Of the four algebraic norms, only $\langle\cdot\rangle_{\mathrm{ts}*}$ is positive definite, so only $\langle\cdot\rangle_{\mathrm{ts}*}$ yields a topological norm; the complex-valued $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\mathrm{ts}}$ and the indefinite $\langle\cdot\rangle_{*}$ do not. Their moduli $\lvert B\rvert,\lvert N\rvert,\lvert H\rvert$ are real and non-negative but vanish on non-zero elements, so no square root of them is a norm; the metric question is taken up in *Topology and Metric for Each of the Operations*.

*Proof.* $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\mathrm{ts}}$ take complex values and vanish on the isotropic sets of the two bilinear forms; $\langle\cdot,\cdot\rangle_{*}$ is indefinite of signature $(2,2)$ and vanishes on its null set; a norm must vanish only at the origin, which none of the three does.

## The Topological Norm: Equivalence and Uniqueness

**All norms on the finite-dimensional space are equivalent, so the topology they give is unique.**

**Theorem (equivalence).** Any two norms on $\mathbb{B}_{\mathrm{r}}$ are equivalent: there are constants such that each is bounded by a constant multiple of the other, so they define the same open sets, the same convergent sequences and the same continuous functions.

*Proof.* On a finite-dimensional real vector space every norm is equivalent to the Euclidean one, by the compactness of the unit sphere; the space here is $\mathbb{R}^{4}$ through the coordinates $(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown})$.

**Corollary (the topology is the standard one).** The topology of $\mathbb{B}_{\mathrm{r}}$ is the standard topology of $\mathbb{R}^{4}$, independent of the norm chosen; it is metrisable, and the metric of $\langle\cdot\rangle_{\mathrm{ts}*}$,
$$
d(\breve Q_{1},\breve Q_{2})=\lVert \breve Q_{1}-\breve Q_{2}\rVert=\sqrt{\langle \breve Q_{1}-\breve Q_{2}\rangle_{\mathrm{ts}*}},
$$
is one of the compatible metrics. The space is complete and locally compact.

*Proof.* The coordinate map $\breve Q\mapsto(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown})$ is an isomorphism of real vector spaces onto $\mathbb{R}^{4}$, and it is a homeomorphism for the two Euclidean norms; the completeness and the local compactness are those of $\mathbb{R}^{4}$.

## The Topology

**Definition.** The **Euclidean topology** of $\mathbb{B}_{\mathrm{r}}$ is the topology induced by the norm $\lVert\cdot\rVert$; the **open ball** of centre $\breve Q$ and radius $r>0$ is $B(\breve Q,r)=\{\breve Q_{2}:\lVert \breve Q-\breve Q_{2}\rVert<r\}$, and the **closed ball** is its closure.

**Theorem (the basic properties).** The space is connected and path-connected, indeed contractible, as a real vector space; it is not compact; and it is homeomorphic to $\mathbb{R}^{4}$, hence to the open ball and to the open four-dimensional cube.

*Proof.* Every vector space is contractible by the straight-line homotopy to the origin, hence connected and path-connected; the space is unbounded, so it is not compact; and the norm gives a homeomorphism with $\mathbb{R}^{4}$ by the coordinate map.

**Corollary (the one-point compactification).** The one-point compactification of the space is the four-sphere $S^{4}$; the spheres and the balls of the norm are the images of the standard ones under the coordinate homeomorphism.

*Proof.* The one-point compactification of $\mathbb{R}^{n}$ is $S^{n}$, here $n=4$; and the norm balls are the standard Euclidean balls read in the coordinates.

## The Algebra Structure

**The four products are continuous, and the three conjugations are isometries.**

**Theorem (continuity of the products).** The four general products, as maps $\mathbb{B}_{\mathrm{r}}\times\mathbb{B}_{\mathrm{r}}\to\mathbb{B}_{\mathrm{r}}$, are continuous; so is the addition, and so is the multiplication by a scalar. The algebra is a topological algebra for the Euclidean topology.

*Proof.* Each product is bilinear or sesquilinear over $\mathbb{C}$ with constant coordinates, hence a continuous map of the finite-dimensional space, by the continuity of the polynomial and conjugate-polynomial coordinate functions; the addition is continuous as the addition of $\mathbb{R}^{4}$.

**Theorem (the involutions are isometries).** The bar, the tessarine sign and the star preserve the norm and the metric,
$$
\lVert\bar{\breve Q}\rVert=\lVert \breve Q_{\mathrm{ts}}\rVert=\lVert \breve Q^{*}\rVert=\lVert \breve Q\rVert,
$$
so each is an isometry of $\mathbb{B}_{\mathrm{r}}$ onto itself, and the three form a Klein four-group of isometries.

*Proof.* $\langle \breve Q\rangle_{\mathrm{ts}*}=Q_{\blacktriangle}\bar Q_{\blacktriangle}+Q_{\blacktriangledown}\bar Q_{\blacktriangledown}$; the bar replaces $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$ by their conjugates, leaving the two moduli; the tessarine sign negates $Q_{\blacktriangledown}$, leaving the two moduli; the star is their composite, so it too preserves them. The metric is $\lVert \breve Q-\breve Q_{2}\rVert$, and each involution is linear or antilinear and preserves the norm, hence the metric; the Klein group is *The Two Involutions and the Group of Involutions*.

**Corollary (the unit group is open and the zero divisors closed).** The unit group $\mathbb{B}_{\mathrm{r}}^{\times}$ is open, and its complement, the zero-divisor set, is closed; the zero-divisor set has empty interior, so the unit group is dense.

*Proof.* The zero-divisor set is $\{\langle \breve Q\rangle_{\mathrm{ts}}=0\}=\{Q_{+}=0\}\cup\{Q_{-}=0\}$, the union of two real planes through the origin, which is closed as the vanishing set of the continuous functions $Q_{+}$ and $Q_{-}$; a plane has empty interior, and a finite union of sets of empty interior has empty interior, so the unit group is dense. The openness is the complement of a closed set.

## The Relation to the Four Products

**Each product is continuous and induces the same topology, the Euclidean one.**

**Theorem.** For each of the four products $\circ$, the operation $\breve Q_{2}\mapsto \breve Q\circ \breve Q_{2}$ is a homeomorphism of $\mathbb{B}_{\mathrm{r}}$ onto itself when $\breve Q$ is a unit, and the topology attached to the product is the Euclidean topology; the four products give one and the same topology.

*Proof.* A continuous bijection of $\mathbb{R}^{4}$ whose inverse is the multiplication by $\breve Q^{-1}$, also continuous, is a homeomorphism; and the topology is the unique vector-space topology, so all four agree. The differences between the four are in the metric-like quantities they carry, not in the topology, as *Topology and Metric for Each of the Operations* records.

**Corollary (the product degenerates exactly at the zero divisors).** For a zero divisor $\breve Q$ the map $\breve Q_{2}\mapsto \breve Q \breve Q_{2}$ is continuous but not injective and not surjective, its image being one of the two idempotent lines for the plain product; so the failure of the product is concentrated on the closed zero-divisor set.

*Proof.* Multiplication by a zero divisor has a non-trivial kernel and an image of dimension smaller than four; the extreme case is an element of an idempotent line, whose image is that line.

## Summary

The reduced biquaternion algebra carries the Euclidean topology of $\mathbb{R}^{4}$ through the norm $\lVert \breve Q\rVert=\sqrt{\langle \breve Q\rangle_{\mathrm{ts}*}}=\sqrt{q_{\blacktriangle}^{2}+{q'_{\blacktriangle}}^{2}+q_{\blacktriangledown}^{2}+{q'_{\blacktriangledown}}^{2}}$, and only the form $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ is positive definite, so only $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ gives a topological norm. All norms are equivalent, so the topology is unique, metrisable, complete and locally compact; the space is contractible and its one-point compactification is $S^{4}$. The four products are continuous, the three conjugations are isometries forming a Klein four-group, and the unit group is open and dense while the zero-divisor set is closed with empty interior. Each of the four products is continuous and induces the same Euclidean topology; the differences between the products lie in the metric-like quantities, not in the topology. The multiplication **has zero divisors** and is **not a division algebra**, and the zero-divisor set is exactly the boundary of the unit group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lVert \breve Q\rVert=\sqrt{\langle \breve Q\rangle_{\mathrm{ts}*}}$ | the Euclidean norm, from the positive definite form $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$ |
| $d(\breve Q_{1},\breve Q_{2})=\lVert \breve Q_{1}-\breve Q_{2}\rVert$ | the metric |
| $B(\breve Q,r)$ | the open ball of centre $\breve Q$ and radius $r$ |
| $\mathbb{B}_{\mathrm{r}}^{\times}$ | the unit group, open and dense |
| $\{Q_{+}=0\}\cup\{Q_{-}=0\}$ | the zero-divisor set, closed with empty interior |

## Further Reading

- [The Forms of the Algebra of the Reduced Biquaternions](the-forms-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the definiteness of $\langle\cdot,\cdot\rangle_{\mathrm{ts}*}$.
- [The Four Products, Their Forms and Their Algebraic Norms](the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.html), for the four products and the norms.
- [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the two lines.
- [The Euclidean Topology of the Reduced Biquaternion Algebra](the-euclidean-topology-of-the-reduced-biquaternion-algebra.html), for the metric, the unit sphere and the unit group as a topological group.
- [Topology and Metric for Each of the Operations](topology-and-metric-for-each-of-the-operations-of-the-reduced-biquaternions.html), for the metric of each product.
- [Topology in the Space of Biquaternions](topology-in-the-space-of-biquaternions.html), for the non-commutative companion.
