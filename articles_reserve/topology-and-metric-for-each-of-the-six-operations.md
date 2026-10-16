# __Topology and Metric for Each of the Six Operations__

## Introduction

The chapter closes where the six products of *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* meet the topology of the algebra. For each product one reads the scalar part of the square, polarises it into a symmetric bilinear form, and so obtains the metric that the product carries; the six rows fall into two classes, a definite one and an indefinite one, and the antisymmetric products carry the zero form. This is the only place in the chapter where the six products are read metrically; the products themselves, and their laws, are the articles cited and are not re-proved here.

**Boundaries.** The six products and their laws are *The 6 Products of the Quaternioid Real Space* and *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the two forms of the space are *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*; the norm is *Norm and Invertibility in the Quaternion Algebra*; the metric of the quaternion space is *Quaternion Metrics*, above this article in this category; the space and its topology are *Introduction to Topology on the Quaternions* and *Quaternion Topology*, above this article in this category.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$ with basis $e_0=1,e_1,e_2,e_3$; an element is $\tilde q=q_0e_0+\vec q$ with $\vec q=\sum_kq_ke_k$. The **quaternion form** is $N(\tilde q)=q_0^{2}+|\vec q|^{2}$ and the **plain form** is $B(\tilde q)=q_0^{2}-|\vec q|^{2}$; the **quaternion conjugation** is $\tilde q^{\natural}=q_0e_0-\vec q$, the bar is the identity. The six products are those of the table of *The 6 Products of the Quaternioid Real Space*, and for a product $\star$ the **metric form** is the polarisation of the scalar part at the two equal arguments,

$$
\Phi_\star(\tilde p,\tilde q)=\mathrm{Sc}\bigl(\tilde p\star\tilde q\bigr)\ \text{symmetrised},\qquad
Q_\star(\tilde q)=\mathrm{Sc}\bigl(\tilde q\star\tilde q\bigr),\qquad
2\Phi_\star(\tilde p,\tilde q)=Q_\star(\tilde p+\tilde q)-Q_\star(\tilde p)-Q_\star(\tilde q).
$$

## The Scalar Part and the Two Facts

**Proposition (the value at the two equal arguments).** For the six products the scalar part at the two equal arguments is

| $\star$ | the algebra | $\mathrm{SPA}$ | $\mathrm{APA}$ | $\mathrm{GQA}$ | $\mathrm{SQA}$ | $\mathrm{AQA}$ |
|---|---|---|---|---|---|---|
| $Q_\star(\tilde q)=\mathrm{Sc}(\tilde q\star\tilde q)$ | $B(\tilde q)$ | $B(\tilde q)$ | $0$ | $N(\tilde q)$ | $N(\tilde q)$ | $0$ |

*Proof.* For the plain products $\tilde q\tilde q=\tilde q^{2}=(q_0^{2}-|\vec q|^{2})e_0+2q_0\vec q$, whose scalar part is $B(\tilde q)$; the symmetric plain product has the same square, $\tfrac12(\tilde q\tilde q+\tilde q\tilde q)=\tilde q^{2}$. For the antisymmetric plain product, $\tfrac12(\tilde q\tilde q-\tilde q\tilde q)=0$. For the quaternionic products $\tilde q^{\natural}\tilde q=N(\tilde q)e_0$ and $\tfrac12(\tilde q^{\natural}\tilde q+\tilde q^{\natural}\tilde q)=N(\tilde q)e_0$, and the antisymmetric quaternionic product is $\tfrac12(\tilde q^{\natural}\tilde q-\tilde q^{\natural}\tilde q)=0$.

**Corollary (two facts distribute the six).** Only two quadratic forms occur on the diagonal, the plain form $B$ and the quaternion form $N$, together with the zero form; and the pairing of each product is the polarisation of the diagonal, so the metric of a quaternion product is intrinsic to it.

*Proof.* The table lists the three possibilities, and the polarisation of a quadratic form is the unique symmetric bilinear form with it on the diagonal.

## The Six, One by One

**The algebra — quaternion algebra.** The metric form is the plain form $B$, of signature $(1,3)$, indefinite. The **unit set** $\{B=1\}$ is the two-sheeted hyperboloid of the timelike vectors, noncompact; the **null set** $\{B=0\}$ is the quadratic cone of the isotropic directions, of real dimension $3$. This is the Lorentz form of the algebra, and the plain product is the product whose quadratic invariant it is.

**$\mathrm{SPA}$ — symmetric plain algebra.** The diagonal is the same square, so the metric is again $B$ of signature $(1,3)$; the unit set and the null set are the same hyperboloid and cone. The symmetric plain product is the Jordan product of the same indefinite form.

**$\mathrm{APA}$ — antisymmetric plain algebra.** The diagonal vanishes identically, so the metric form is the zero form; the unit set is empty and the null set is the whole algebra. The product is alternating, every element is square-zero, and it carries no metric.

**$\mathrm{GQA}$ — general quaternionic algebra.** The diagonal is $N(\tilde q)e_0$, so the metric form is the quaternion form $N$, positive definite of signature $(4,0)$. The **unit set** $\{N=1\}$ is the unit sphere $S^3$, compact; the **null set** $\{N=0\}$ is the single point $\{0\}$. The left-multiplication product is the product whose quadratic invariant is the definite form.

**$\mathrm{SQA}$ — symmetric quaternionic algebra.** The diagonal is the same $N(\tilde q)e_0$, so the metric is again $N$ of signature $(4,0)$, with unit set $S^3$ and null set $\{0\}$; the product is the symmetric half of the quaternionic row, and it too carries the definite metric.

**$\mathrm{AQA}$ — antisymmetric quaternionic algebra.** The diagonal vanishes, so the metric form is zero, the unit set is empty and the null set is the whole algebra; the product is alternating and carries no metric.

## The Table of the Six

| product | quadratic diagonal $Q_\star$ | metric form | signature | unit set $\{Q_\star=1\}$ | null set $\{Q_\star=0\}$ |
|---|---|---|---|---|---|
| the algebra | $B$ | $B$ | $(1,3)$ indefinite | hyperboloid, noncompact | the cone, dim $3$ |
| $\mathrm{SPA}$ | $B$ | $B$ | $(1,3)$ indefinite | hyperboloid, noncompact | the cone, dim $3$ |
| $\mathrm{APA}$ | $0$ | $0$ | totally degenerate | empty | all of $\mathbb{H}$ |
| $\mathrm{GQA}$ | $N$ | $N$ | $(4,0)$ definite | $S^3$, compact | $\{0\}$ |
| $\mathrm{SQA}$ | $N$ | $N$ | $(4,0)$ definite | $S^3$, compact | $\{0\}$ |
| $\mathrm{AQA}$ | $0$ | $0$ | totally degenerate | empty | all of $\mathbb{H}$ |

**Theorem (the two classes).** Four of the six products carry a nonzero metric and two carry the zero form; among the four, two are definite, the quaternionic products $\mathrm{GQA}$ and $\mathrm{SQA}$, and two are indefinite of signature $(1,3)$, the plain products, the algebra and $\mathrm{SPA}$. The definite class has the compact unit sphere $S^3$ and the trivial null set; the indefinite class has a noncompact unit hyperboloid and a null cone of real dimension $3$; the degenerate class has no unit set and its null set is the whole algebra.

*Proof.* The statements are read from the table; the signatures are those of $B$ and $N$, the eigenvalues of the Gram matrices being $+1,-1,-1,-1$ and $+1,+1,+1,+1$; definiteness is *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*, and the compactness and the dimensions of the sets are *Introduction to Topology on the Quaternions*.

**Remark (the metric is a property of the product, not of the space).** The six products live on the same algebra and the same topology; what separates them metrically is the scalar part of their squares. The two quaternionic products differ algebraically, one non-associative with a left unit and one commutative without a unit, and agree metrically, because both have the same diagonal $N$; the two plain products differ algebraically, one associative and one Jordan, and agree metrically, because both have the diagonal $B$. The metric sees the row and not the symmetry.

## Summary

For each of the six products the scalar part of the square is a quadratic form, and its polarisation is the metric the product carries. The two plain products, general and symmetric, carry the indefinite form $B$ of signature $(1,3)$, with a noncompact unit hyperboloid and a null cone of real dimension three; the two quaternionic products, general and symmetric, carry the definite form $N$ of signature $(4,0)$, with the compact unit sphere $S^3$ and the null set $\{0\}$; the two antisymmetric products carry the zero form, with empty unit set and the whole algebra as null set. The metric depends on the row of the catalogue and not on the symmetry within it: the quaternionic pair shares $N$ and the plain pair shares $B$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $Q_\star(\tilde q)=\mathrm{Sc}(\tilde q\star\tilde q)$ | the scalar part at the two equal arguments of a product |
| $\Phi_\star$ | the metric form, the polarisation of $Q_\star$ |
| $B(\tilde q)=q_0^{2}-|\vec q|^{2}$ | the plain form, signature $(1,3)$ |
| $N(\tilde q)=q_0^{2}+|\vec q|^{2}$ | the quaternion form, signature $(4,0)$ |
| $S^3=\{N=1\}$, $\{B=1\}$, $\{B=0\}$ | the unit sphere, the unit hyperboloid, the null cone |
| $0$ | the metric form of the two antisymmetric products |

## Further Reading

- *The 6 Products of the Quaternioid Real Space* (`articles_maths/the-6-products-of-the-quaternioid-real-space.md`) and *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-algebraic-structures-over-the-quaternioid-r-space.md`), for the six products
- *The 2 Forms over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternioid-r-space.md`), for the signatures and the isotropy of $B$ and $N$
- *Quaternion Metrics* (`articles_maths/quaternion-metrics.md`), for the metric of the quaternion space
- *Introduction to Topology on the Quaternions* (`articles_maths/introduction-to-topology-on-the-quaternions.md`), for the sphere, the punctured space and the group of units
