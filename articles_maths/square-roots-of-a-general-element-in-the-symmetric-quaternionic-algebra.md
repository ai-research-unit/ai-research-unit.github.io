# __Square Roots of a General Element in the Symmetric Quaternionic Algebra__

## Introduction

A square root of an element $\tilde Q$ in a product is an element with $\tilde\Xi\star\tilde\Xi=\tilde Q$, and the roots of a central value are the special case $\tilde Q=\lambda e_0$ (*Definitions for the Study of the 12 Algebraic Structures* §*Powers, the Square and the Roots*). In the parent plain algebra the problem has a rich classification — roots with non-vanishing vector part, roots of a central value, the reduction of the general element to its scalar part (*Square Roots of a General Element in the General Plain Algebra*). In the symmetric quaternionic block the problem **collapses**: the square of an element is always central,

$$
\tilde\Xi\star\tilde\Xi=N(\tilde\Xi)e_0,
$$

so a square root exists only for the elements of the central line. This article states the collapse, computes the root set of a central radicand, classifies the two possible cases, and works the examples. The absence of the general case is the content, and the article is short because the absence is stated and not filled.

**Boundaries.** The three special radicands are *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra*; the square-zero elements, that is the case $\tilde Q=0$, are *Nilpotents of the Symmetric Quaternionic Algebra*; the diagonal and the non-isotropic class are *Norm and Invertibility in the Symmetric Quaternionic Algebra*; the general definitions are the definitions article; the parent's classification, which the block collapses, is *Square Roots of a General Element in the General Plain Algebra*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$, and central scalar imaginary $i$; a general element is $\tilde Q=Q_0e_0+\mathbf Q$. The **symmetric quaternionic multiplication** is $\tilde\Xi\star\tilde Q=N(\tilde\Xi,\tilde Q)e_0$ with $N(\tilde\Xi,\tilde Q)=\Xi_0Q_0+(\mathbf\Xi,\mathbf Q)$, and its diagonal is $N(\tilde\Xi)=\sum_{\mu=0}^{3}\Xi_\mu^2$; the operation is also written $\bullet$. The centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$.

## The Reduction

**Theorem (the square of the block is always central).** For every $\tilde\Xi$,

$$
\tilde\Xi\star\tilde\Xi=N(\tilde\Xi)e_0\in\mathbb{C}_{\mathbb{B}},
$$

so the image of the square map of the block is the central line.

*Proof.* The product is $\tilde\Xi\star\tilde\Xi=N(\tilde\Xi,\tilde\Xi)e_0$ by the definition of the block, and $N(\tilde\Xi,\tilde\Xi)=N(\tilde\Xi)$ is a scalar.

**Corollary (the obstruction to a square root).** The equation $\tilde\Xi\star\tilde\Xi=\tilde Q$ has a solution only for the **central** radicands $\tilde Q=\lambda e_0$; for a non-central $\tilde Q$ the root set is empty. In particular the block has no element whose square is a vector, and the case of the general theory that treats the roots with non-vanishing vector part does not occur here: there are neither roots of that shape nor a second case to distinguish.

## The Roots of a Central Value

**Theorem (the root set of a central value).** Let $\lambda\in\mathbb{C}$ and let $\tilde Q=\lambda e_0$. The root set

$$
\mathcal{R}(\lambda)=\{\tilde\Xi:\tilde\Xi\star\tilde\Xi=\lambda e_0\}=\{\tilde\Xi:N(\tilde\Xi)=\lambda\}
$$

is nonempty for every $\lambda$, and it is the level set of the diagonal at $\lambda$: the cone $\{N=0\}$ minus the origin when $\lambda=0$, and an affine hyperquadric of complex dimension three when $\lambda\neq0$.

*Proof.* The reduction gives $N(\tilde\Xi)=\lambda$. Nonemptiness: for $\lambda\neq0$ choose a square root $\mu$ of $\lambda$ complex and take $\tilde\Xi=\mu e_0$, whose $N$ is $\mu^2=\lambda$; for $\lambda=0$ take an isotropic element such as $e_0+ie_1$, whose $N=1-1=0$. The description of the level sets is the one of *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra*.

**Proposition (the counting on a line).** On a complex line $\mathbb{C}\tilde A$ through the origin, the equation reads $t^2N(\tilde A)=\lambda$, so the number of roots of the central value $\lambda\neq0$ on the line is two when $N(\tilde A)\neq0$ and zero when $N(\tilde A)=0$; the roots of $0$ on the line are the line minus the origin when $N(\tilde A)=0$, and there are none when $N(\tilde A)\neq0$, the origin being excluded as a root and the equation $t^2N(\tilde A)=0$ then reading $t=0$.

*Proof.* $N(t\tilde A)=t^2N(\tilde A)$ by the homogeneity of the diagonal; for $\lambda\neq0$ and $N(\tilde A)\neq0$ the two values $t=\pm\sqrt{\lambda/N(\tilde A)}$ are nonzero and distinct, and for $N(\tilde A)=0$ the equation $0=\lambda\neq0$ is impossible; for $\lambda=0$ the equation is $t^2N(\tilde A)=0$, solved by every $t\neq0$ when $N(\tilde A)=0$ and by no nonzero $t$ otherwise, the origin being excluded as a root.

**Corollary (the root set of a central value, restated).** For $\lambda\neq0$ the root set is stable under $\tilde\Xi\mapsto-\tilde\Xi$ and under the natural conjugation, which preserve $N$, while the star and the Hermitian conjugation carry it onto the root set of $\overline{\lambda}$; and it contains the two central roots $\pm\mu e_0$ with $\mu^2=\lambda$. For $\lambda=0$ the root set is the punctured isotropic cone, and its elements are exactly the square-zero elements, the roots of $0$ of the block.

## The Classification

**Theorem (the two cases).** Let $\tilde Q\in\mathbb{B}$. The square-root equation of the block has

1. for a **central** radicand $\tilde Q=\lambda e_0$: the root set $\{\tilde\Xi:N(\tilde\Xi)=\lambda\}$, nonempty, of complex dimension three, and equal to the cone minus the origin when $\lambda=0$;
2. for a **non-central** radicand: no root at all.

There is no third case, and there is no case in which the root set is a finite nonempty set: the equation is one scalar quadratic equation in four unknowns and its solution set is a three-dimensional quadric, or empty.

*Proof.* A root satisfies $\tilde\Xi\star\tilde\Xi=N(\tilde\Xi)e_0$, which is central; comparing with $\tilde Q$ gives the two cases, and the first is the theorem of the preceding section. The dimension is the one of a hypersurface of $\mathbb{C}^4$ cut by one non-degenerate quadratic equation; the set is never a finite nonempty set because a non-degenerate quadratic in four variables has a three-dimensional zero set off its singular cases, and the singular case is the cone $\lambda=0$.

**Remark (the collapse and what causes it).** The parent's classification separates the radicands by the scalar part and treats the non-central radicands by a reduction to a scalar equation with a vector unknown (*Square Roots of a General Element in the General Plain Algebra*). The block needs none of that machinery, and the reason is structural: the product is central-valued, so the square map loses the vector part entirely, and there is no associativity and no unit with which to reconstruct an element from its square. The collapse is the shadow of the centrality of the block, the same property that makes it a rank-one pairing.

## The Worked Examples

**Example (a non-central radicand).** Let $\tilde Q=e_1$. The equation $\tilde\Xi\star\tilde\Xi=e_1$ has no solution, since a square of the block is central and $e_1$ is not. In the parent plain algebra the same equation has solutions (*Square Roots of a General Element in the General Plain Algebra*), and the comparison is the sharpest witness of the collapse.

**Example (a central radicand, $\lambda=1$).** The roots are the level set $N=1$: the four basis elements, the elements $\pm\mu e_0$ with $\mu^2=1$, and the hyperquadric computed in *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra*.

**Example (an imaginary radicand).** Let $\tilde Q=ie_0$, that is $\lambda=i$. A square root of $i$ in $\mathbb{C}$ is $\mu=e^{i\pi/4}$, and $\tilde\Xi=\mu e_0$ is a root: $N(\mu e_0)=\mu^2=i$. The root set is the quadric $\{\tilde\Xi:Q_0^2+(\mathbf\Xi,\mathbf\Xi)=i\}$, of complex dimension three, and it contains the non-central elements as well: for instance any $\tilde\Xi=\Xi_0e_0+\mathbf\Xi$ with $\Xi_0$ a square root of $i-(\mathbf\Xi,\mathbf\Xi)$ is a root.

**Example (the radicand zero).** The roots of $0$ are the punctured isotropic cone, $\{N=0\}\setminus\{0\}$: for instance $e_0+ie_1$, with $\tilde\Xi\star\tilde\Xi=0$ and $\tilde\Xi\neq0$. The element $0$ is not a root, by the definition of a root, and it is the only element whose square is $0$ and that is excluded from the root set.

## Summary

In the symmetric quaternionic block the square of every element is central, $\tilde\Xi\star\tilde\Xi=N(\tilde\Xi)e_0$, so the square-root problem has a solution only for the central radicands $\tilde Q=\lambda e_0$, and for those the root set is the level set $\{\tilde\Xi:N(\tilde\Xi)=\lambda\}$: the punctured isotropic cone for $\lambda=0$, an affine hyperquadric of complex dimension three for $\lambda\neq0$, nonempty in both cases, the sign and the natural conjugation preserving each level set while the star and the Hermitian conjugation exchange the level sets of $\lambda$ and of $\overline{\lambda}$. A non-central radicand has no root, the case of the general theory with a non-vanishing vector part does not occur, and the classification therefore has exactly two cases with three-dimensional solution sets and no finite nonempty case. The three special values $\lambda=-1,0,1$ are treated in the article devoted to them; the parent's general classification, which the block collapses, is the model article of the same slot in the General Plain Algebra.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde\Xi\star\tilde Q=N(\tilde\Xi,\tilde Q)e_0$ | the symmetric quaternionic multiplication |
| $N(\tilde\Xi)=\sum_\mu \Xi_\mu^2$ | the form at the two equal arguments |
| $\tilde\Xi\star\tilde\Xi=N(\tilde\Xi)e_0$ | the square of the block, always central |
| $\mathcal{R}(\lambda)=\{\tilde\Xi:N(\tilde\Xi)=\lambda\}$ | the root set of the central value $\lambda$ |
| $\lambda=0$ | the punctured isotropic cone, the square-zero elements |
| $\lambda\neq0$ | an affine hyperquadric of complex dimension three |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the general definitions of a power, a root of a central value and a square root of an element.
- *Square Roots of a General Element in the General Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-algebra.md`), for the parent's classification, which the block collapses.
- *Square Roots of Minus One, Zero and Plus One in the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-symmetric-quaternionic-algebra.md`), for the three special radicands.
- *Nilpotents of the Symmetric Quaternionic Algebra* (`articles_maths/nilpotents-of-the-symmetric-quaternionic-algebra.md`), for the radicand zero.
- *Norm and Invertibility in the Symmetric Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-quaternionic-algebra.md`), for the diagonal and the three level sets.
