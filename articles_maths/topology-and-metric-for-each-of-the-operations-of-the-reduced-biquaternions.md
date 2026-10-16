# __Topology and Metric for Each of the Operations__

## Introduction

Each of the four general products of the reduced biquaternion algebra carries a scalar-part form, and each form gives a real quantity on the space, the **modulus of the form at the difference of two elements**. This article collects the four quantities and asks, for each, whether it is a metric. Only the general quaternionic sesquilinear form $\langle\cdot,\cdot\rangle_{\natural*}$ gives a genuine metric, $d(T,W)=\sqrt{\langle T-W\rangle_{\natural*}}$; the other three give **degenerate or indefinite** quantities, which vanish on non-zero differences or violate the triangle inequality, and the failures are exactly the sets the algebra is known for: the zero divisors, the isotropic sets of the bilinear forms and the null set of the indefinite form. The four products, however, are all continuous and all induce the **same** topology, the Euclidean one: the products differ in their metric-like quantities, not in their topology. The multiplication is **commutative**, **has zero divisors** and is **not a division algebra**, and the three degenerate quantities are the metrical shadow of the zero divisors.

**Conventions.** The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$, $ji=ij$; the element is $T=A+Bj$ with $A=a+ia'$, $\langle\cdot\rangle=b+ib'$; the idempotent coordinates are $q_1=A+B$, $q_2=A-B$. The four products and the forms $\langle\cdot,\cdot\rangle, \langle\cdot,\cdot\rangle_{\natural}, \langle\cdot,\cdot\rangle_{*}, \langle\cdot,\cdot\rangle_{\natural*}$ are *The Four Products, Their Forms and Their Algebraic Norms*, and the forms are *The Forms of the General Plain Algebra of the Reduced Biquaternions*. The element glyph is $T$, without a tilde.

**Boundaries.** The topology and the Euclidean norm are *Topology in the Space of Reduced Biquaternions*; the metric properties of the Euclidean space and the unit group are *The Euclidean Topology of the Reduced Biquaternion Algebra*; the zero divisors are *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*; the analysis built on the metric is *Reduced Biquaternion Analysis*. The biquaternion counterpart is *Topology and Metric for Each of the Operations* of the biquaternion category.

## The Four Candidate Metrical Quantities

**For each product, take the modulus of the form at the difference of two elements.**

**Definition.** For a product with scalar-part form $F$, define
$$
\delta_{F}(T,W)=\bigl\lvert F(T-W,\,T-W)\bigr\rvert^{1/2}=\bigl\lvert F(T-W)\bigr\rvert^{1/2},
$$
where $F(X)$ is the algebraic norm of the form. The four quantities are $\delta_{B}$, $\delta_{N}$, $\delta_{H}$ and $\delta_{K}$.

**Theorem (the four quantities).** Each $\delta_{F}$ is real, non-negative, symmetric, $\delta_{F}(T,T)=0$, and homogeneous in the sense $\delta_{F}(\lambda T,\lambda W)=\lvert\lambda\rvert\delta_{F}(T,W)$ for real $\lambda$; the four differ in whether they are positive definite and in whether they satisfy the triangle inequality.

*Proof.* The algebraic norms are $\langle\cdot\rangle=A^{2}+B^{2}$, $\langle\cdot\rangle_{\natural}=A^{2}-B^{2}$, $\langle\cdot\rangle_{*}=\lvert A\rvert^{2}-\lvert B\rvert^{2}$ and $\langle\cdot\rangle_{\natural*}=\lvert A\rvert^{2}+\lvert B\rvert^{2}$; their moduli are real and non-negative, vanish at $T=W$ because the form vanishes at the zero difference, are symmetric because the two bilinear forms are symmetric and the two sesquilinear forms are Hermitian, and are homogeneous of degree two in the difference, whence the square root is homogeneous of degree one.

## The Euclidean Metric

**The quantity of $\langle\cdot\rangle_{\natural*}$ is the Euclidean metric.**

**Theorem (the metric).** $\delta_{K}(T,W)=\lVert T-W\rVert$ is a metric on $\mathbb{B}_{\mathrm{r}}$: positive definite, symmetric, and satisfying the triangle inequality; it is the metric of *The Euclidean Topology of the Reduced Biquaternion Algebra*, complete and compatible with the Euclidean topology.

*Proof.* $\langle\cdot\rangle_{\natural*}$ is positive definite, so $\langle X\rangle_{\natural*}>0$ for $X\neq0$ and $\langle X\rangle_{\natural*}=0$ exactly for $X=0$, which gives the positive definiteness of $\delta_{K}$; symmetry and the triangle inequality are those of the Euclidean norm of the coordinate quadruple, by the second theorem of the next section.

## The Degenerate and Indefinite Quantities

**The quantities of $\langle\cdot\rangle$, $\langle\cdot\rangle_{\natural}$ and $\langle\cdot\rangle_{*}$ are not metrics, each failing in its own way.**

**Theorem (the failures).** $\delta_{B}$, $\delta_{H}$ and $\delta_{N}$ are not metrics: each vanishes at a pair of distinct elements, and each violates the triangle inequality.

- $\delta_{N}$ vanishes exactly when $T-W$ is a zero divisor or zero, that is on the set $\{N=0\}$, the union of the two idempotent lines;
- $\delta_{B}$ vanishes exactly when $T-W$ lies in the isotropic set $\{B=0\}$, a real two-dimensional cone in the space;
- $\delta_{H}$ vanishes exactly when $T-W$ lies in the null set $\{H=0\}$, an indefinite quadric cone.

*Proof.* The vanishing of $\delta_{F}(T,W)$ with $T\neq W$ is the vanishing of $F(T-W)$ at a non-zero element, which is precisely the isotropic set of the form $F$; the sets are those computed in *The Forms of the General Plain Algebra of the Reduced Biquaternions*, and $\langle\cdot,\cdot\rangle_{\natural}$ vanishes exactly on the zero divisors of *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*.

**Theorem (the failure of the triangle inequality).** Each of the three quantities violates the triangle inequality, with a witness on its own null set.

*Proof.* Take $U=0$. For $\delta_{B}$: with $T=1+ij$ and $W=1-ij$ one has $\langle T\rangle=A^{2}+B^{2}=1+i^{2}=0$ and $\langle W\rangle=0$, while $T-W=2ij$ has $\langle 2ij\rangle=0+(2i)^{2}=-4$, so $\delta_{B}(T,W)=2$ while $\delta_{B}(T,0)+\delta_{B}(0,W)=0+0=0$, and the triangle inequality fails. For $\delta_{H}$: with $T=1+j$ and $W=1-j$ one has $\langle T\rangle_{*}=1-1=0$ and $\langle W\rangle_{*}=0$, while $T-W=2j$ has $\langle 2j\rangle_{*}=0-4=-4$, so $\delta_{H}(T,W)=2>0+0$. For $\delta_{N}$: with $T=1+j$ and $W=1-j$ one has $q_1=2,q_2=0$ for $T$ and $q_1=0,q_2=2$ for $W$, so $\langle T\rangle_{\natural}=\langle W\rangle_{\natural}=0$, while $T-W=2j$ has $\langle 2j\rangle_{\natural}=0-(2)^{2}=-4$, so $\delta_{N}(T,W)=2>0+0$.

**Corollary (the failure is exactly the zero divisors and the isotropic sets).** The three quantities fail as metrics precisely on the sets where their forms vanish, and those sets are non-trivial: the zero-divisor set for $\langle\cdot,\cdot\rangle_{\natural}$, the isotropic cone for $\langle\cdot,\cdot\rangle$ and the null quadric for $\langle\cdot,\cdot\rangle_{*}$. The Euclidean quantity $\langle\cdot,\cdot\rangle_{\natural*}$ has no such set, its form being positive definite, and it is the only one of the four that is a metric.

*Proof.* A non-negative symmetric homogeneous function vanishing at distinct points or failing the triangle inequality is not a metric; the failures are exhibited on the null sets, and $\langle\cdot\rangle_{\natural*}$ has no null set other than the origin.

## The Isometries of Each Quantity

**The three conjugations preserve all four quantities.**

**Theorem.** The bar, the natural sign and the star preserve each of the four algebraic norms in modulus,
$$
\lvert F(\bar T)\rvert=\lvert F(T^{\natural})\rvert=\lvert F(T^{*})\rvert=\lvert F(T)\rvert
$$
for $F=B,N,H,K$; hence each involution is an isometry of $\mathbb{B}_{\mathrm{r}}$ for each of the four quantities, and the three form a Klein four-group of isometries.

*Proof.* The natural sign negates the second complex coordinate, which leaves $A^{2}+B^{2}$, $A^{2}-B^{2}$, $\lvert A\rvert^{2}-\lvert B\rvert^{2}$ and $\lvert A\rvert^{2}+\lvert B\rvert^{2}$ unchanged; the bar conjugates both coordinates, which conjugates the complex-valued $\langle T\rangle$ and $\langle T\rangle_{\natural}$ and leaves the real-valued $\langle T\rangle_{*}$ and $\langle T\rangle_{\natural*}$ unchanged; the star is the composite, and the modulus is invariant under conjugation. The group is that of *The Two Involutions and the Group of Involutions*.

## The Level Sets of Each Product

**Each product has a unit set, the level set of its norm at the central value.**

| form | the level set | shape |
|---|---|---|
| $\langle\cdot,\cdot\rangle$ | $\langle T\rangle=1$, that is $a^{2}-a'^{2}+b^{2}-b'^{2}+2i(aa'+bb')=1$ | a complex quadric of real dimension two |
| $\langle\cdot\rangle_{\natural}$ | $\langle T\rangle_{\natural}=1$, that is $q_1q_2=1$ | a real hyperboloid, the unit set of the invertibility criterion |
| $\langle\cdot\rangle_{*}$ | $\langle T\rangle_{*}=1$, that is $a^{2}+a'^{2}-b^{2}-b'^{2}=1$ | a one-sheeted hyperboloid of signature $(2,2)$ |
| $\langle\cdot\rangle_{\natural*}$ | $\langle T\rangle_{\natural*}=1$, that is $a^{2}+a'^{2}+b^{2}+b'^{2}=1$ | the Euclidean sphere $S^{3}$ |

**Theorem (the unit sets).** The level sets are the unit sets of the four products relative to their norms, by the unitary convention; the level set of $\langle\cdot\rangle_{\natural*}$ is the compact sphere $S^{3}$, that of $\langle\cdot\rangle_{\natural}$ is the non-compact hyperboloid of the units, and the level sets of $\langle\cdot\rangle$ and $\langle\cdot\rangle_{*}$ are the complex quadric and the indefinite hyperboloid.

*Proof.* Each level set is the norm-one set of its form, as *Conventions in Mathematics*, §*The Unitary Convention*, records; the shapes are those of *The Forms of the General Plain Algebra of the Reduced Biquaternions*, and the compactness of the sphere is the positive definiteness of $\langle\cdot\rangle_{\natural*}$.

## The Four Topologies

**The four products induce one and the same topology, the Euclidean one, and differ only in the metrical quantity.**

**Theorem.** For each of the four products the operation $W\mapsto X\circ W$ by a unit $X$ is a homeomorphism, and the topology attached to the product is the Euclidean topology; hence the four products share the topology of *Topology in the Space of Reduced Biquaternions*.

*Proof.* The topology of a finite-dimensional real vector space is unique, and each product is continuous for it; a continuous bijection with continuous inverse is a homeomorphism, the inverse being the multiplication by $X^{-1}$. The metrical quantities differ, as the table records, but the open sets do not.

**Corollary (the topology does not see the product).** A topological property of the space — compactness, connectedness, the openness of the unit group, the closedness of the zero-divisor set — is the same for all four products; only the metric-like quantity, and with it the notion of length and of angle, is attached to the product. The four products share the topology and the four conjugations, and they are separated by their forms and their metrics.

*Proof.* The listed properties depend only on the topology, which is common; the metric-like quantities are attached each to its form, and they differ by the failures of §*The Degenerate and Indefinite Quantities*.

## Summary

Each of the four general products of the reduced biquaternion algebra carries a metrical quantity $\delta_{F}(T,W)=\lvert F(T-W)\rvert^{1/2}$, and the table of what each is worth is the content of the article.

| product | form | quantity | metric? | unit set |
|---|---|---|---|---|
| $TW$ | $\langle\cdot,\cdot\rangle=A^{2}+B^{2}$ | $\lvert \langle T-W\rangle\rvert^{1/2}$ | no, degenerate | complex quadric $\langle\cdot\rangle=1$ |
| $T^{\natural}W$ | $\langle\cdot\rangle_{\natural}=A^{2}-B^{2}$ | $\lvert \langle T-W\rangle_{\natural}\rvert^{1/2}$ | no, degenerate | hyperboloid $q_1q_2=1$ |
| $TW^{*}$ | $\langle\cdot\rangle_{*}=\lvert A\rvert^{2}-\lvert B\rvert^{2}$ | $\lvert \langle T-W\rangle_{*}\rvert^{1/2}$ | no, indefinite | hyperboloid $\langle\cdot\rangle_{*}=1$ |
| $T^{\natural}W^{*}$ | $\langle\cdot\rangle_{\natural*}=\lvert A\rvert^{2}+\lvert B\rvert^{2}$ | $\sqrt{\langle T-W\rangle_{\natural*}}$ | **yes** | sphere $S^{3}$ |

Only $\langle\cdot\rangle_{\natural*}$ gives a metric, the Euclidean one, positive definite and complete; the other three vanish on non-zero differences or fail the triangle inequality, on the zero-divisor set, the isotropic cone and the null quadric respectively. The three conjugations preserve all four quantities in modulus, forming a Klein group of isometries, and the four products induce the same Euclidean topology: they are separated by their forms and their metric-like quantities, not by their topology. The multiplication is **commutative**, **has zero divisors** and is **not a division algebra**, and the degenerate quantities are the metrical shadow of the zero divisors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\delta_{F}(T,W)=\lvert F(T-W)\rvert^{1/2}$ | the metrical quantity of the form $F$ |
| $d(T,W)=\sqrt{\langle T-W\rangle_{\natural*}}$ | the Euclidean metric, the only genuine one |
| $\{B=0\}$ | the isotropic set of the plain bilinear form |
| $\{H=0\}$ | the null quadric of the indefinite form |
| $\{N=0\}$ | the zero-divisor set |

## Further Reading

- *Topology in the Space of Reduced Biquaternions* (`articles_maths/topology-in-the-space-of-reduced-biquaternions.md`), for the norm and the topology.
- *The Euclidean Topology of the Reduced Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-reduced-biquaternion-algebra.md`), for the Euclidean metric and the unit group.
- *The Forms of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/the-forms-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the four forms and their isotropic sets.
- *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the zero-divisor set.
- *Reduced Biquaternion Analysis* (`articles_maths/reduced-biquaternion-analysis.md`), for the analysis built on the Euclidean metric.
