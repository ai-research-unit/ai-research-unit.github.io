# __Square Roots of a General Element in the Symmetric Quaternionic Algebra__

## Introduction

A square root of an element $\tilde q$ in a product is an element $\tilde x$ with $\tilde x\star\tilde x=\tilde q$. In the parent plain algebra the problem has a rich classification, with roots whose vector part does not vanish and a reduction of the general radicand to its scalar part (*Square Roots of a General Element in the General Plain Algebra*). In the symmetric quaternionic block the problem **collapses**: the square of every element is central,

$$
\tilde x\star\tilde x=N(\tilde x)e_t,
$$

so a square root exists only for the central radicands, and for them the problem is a single level-set equation of the definite form. Over $\mathbb{R}$ the sign of the central value decides everything: a sphere of real dimension three for a positive value, the single point $0$ for the value $0$, and the empty set for a negative value; a noncentral radicand has no root at all. This article states the collapse, computes the root sets, classifies the cases and works the examples. The absence of the general case is the content, and the article is short because the absence is stated and not filled.

**Boundaries.** The special radicands $+1$ and $-1$ are *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra*; the radicand zero and the square-zero elements are *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra*; the diagonal and the non-isotropic class are *Norm and Invertibility in the Symmetric Quaternionic Algebra*; the positivity of the squares and the square root of a positive central element are *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*; the general definitions are *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the parent's classification, which the block collapses, is *Square Roots of a General Element in the General Plain Algebra*.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and $\vec e_x\vec e_y=\vec e_z$; an element is $\tilde x=x_0e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$. The **quaternion conjugation** is $\tilde x^{\natural}=x_0e_t-(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$; the bar is the identity, the star coincides with the natural sign ${}^{\natural}$. The **quaternion form** is $N(\tilde p,\tilde q)=p_0q_t+\vec p\cdot\vec q$, its diagonal is $N(\tilde x)=x_0^{2}+|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|^{2}$, and the **symmetric quaternionic product** is $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_t$. The centre is $\mathbb{R}e_t$; the **unit sphere** of the plain product is $Sp(1)=\{\tilde u:N(\tilde u)=1\}$, the norm-one subgroup of the group of units of the plain product.

## The Reduction

**Theorem (the square of the block is always central).** For every $\tilde x$,

$$
\tilde x\star\tilde x=N(\tilde x)e_t\in\mathbb{R}e_t,
$$

so the image of the square map of the block is the closed half-line $\mathbb{R}_{\geq0}e_t$.

*Proof.* The product is $\tilde x\star\tilde x=N(\tilde x,\tilde x)e_t$ by the definition of the block, and $N(\tilde x,\tilde x)=N(\tilde x)=x_0^{2}+|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|^{2}$ is a real scalar. The image statement is the positivity of $N$, the cone of squares being the closed half-line by *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*.

**Corollary (the obstruction to a square root).** The equation $\tilde x\star\tilde x=\tilde q$ has a solution only for the **central** radicands $\tilde q=\lambda e_t$, $\lambda\in\mathbb{R}$; for a noncentral $\tilde q$ the root set is empty. In particular the block has no element whose square is a vector, and the case of the general theory that treats the roots with a non-vanishing vector part does not occur here: there is neither a root of that shape nor a second case to distinguish.

*Proof.* The left side of the equation is always central, so a matching right side must be central; the two sides of an equation on the same algebra, written in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, have equal coordinates.

## The Roots of a Central Value

**Definition.** For a real number $\lambda$ the **root set of the central value** $\lambda e_t$ is

$$
\mathcal{R}(\lambda)=\{\tilde x:\tilde x\star\tilde x=\lambda e_t\}=\{\tilde x:N(\tilde x)=\lambda\},
$$

the level set of the diagonal of the form at the value $\lambda$.

**Theorem (the root set of a central value).** Let $\lambda\in\mathbb{R}$.

- for $\lambda>0$ the root set is nonempty and is the sphere of radius $\sqrt{\lambda}$,
$$
\mathcal{R}(\lambda)=\{\tilde x:N(\tilde x)=\lambda\}=\sqrt{\lambda}\,Sp(1),
$$
a closed submanifold of real dimension $3$, containing $\pm\sqrt{\lambda}e_t$ and, for every unit vector $\vec q_a$ of the vector subspace, the element $\sqrt{\lambda}\vec q_a$;
- for $\lambda=0$ the root set is the origin alone, $\mathcal{R}(0)=\{0\}$;
- for $\lambda<0$ the root set is empty, $\mathcal{R}(\lambda)=\varnothing$.

*Proof.* The equality $\mathcal{R}(\lambda)=\{\tilde x:N(\tilde x)=\lambda\}$ is the reduction of the preceding section. The form is a sum of four squares, $N(\tilde x)=x_0^{2}+x_1^{2}+x_2^{2}+x_3^{2}\geq0$, with equality only at $\tilde x=0$; this gives the value $0$ and the negative values at once. For $\lambda>0$ the element $\sqrt{\lambda}e_t$ is a root, and for every root the element $\tilde u=\tilde x/\sqrt{\lambda}$ satisfies $N(\tilde u)=N(\tilde x)/\lambda=1$ by the homogeneity $N(t\tilde x)=t^{2}N(\tilde x)$, so $\tilde x=\sqrt{\lambda}\tilde u$ with $\tilde u\in Sp(1)$; conversely every such element is a root. The set $\{N=1\}$ is the unit sphere of the definite form, of real dimension $3$, and it contains $\pm e_t$ and every unit vector of the vector subspace.

**Proposition (the counting on a line).** On a real line $\mathbb{R}\tilde a$ through the origin, spanned by a fixed nonzero element $\tilde a$, the equation reads $t^{2}N(\tilde a)=\lambda$. Since $N(\tilde a)>0$, the roots of a positive value $\lambda$ on the line are the two points $t=\pm\sqrt{\lambda/N(\tilde a)}$; the roots of $0$ on the line are the single point $t=0$; and a negative value has no root on the line.

*Proof.* The homogeneity of the diagonal gives $N(t\tilde a)=t^{2}N(\tilde a)$; the line is a one-dimensional real space and the equation is a quadratic in the single unknown $t$; for $\lambda>0$ the two roots $\pm\sqrt{\lambda/N(\tilde a)}$ are distinct and real, since $N(\tilde a)>0$, and for $\lambda<0$ there is no real root; for $\lambda=0$ the only root is $t=0$, since $N(\tilde a)\neq0$.

**Corollary (symmetries of the root set).** For $\lambda>0$ the root set is stable under $\tilde x\mapsto-\tilde x$ and under the natural conjugation, both of which preserve $N$; it is the orbit of $\sqrt{\lambda}e_t$ under $Sp(1)$. For $\lambda=0$ the root set is the single point $\{0\}$, fixed by both.

*Proof.* The two maps preserve the sum of squares, hence the level set; the orbit description is the theorem. For $\lambda=0$ the set is $\{0\}$ and both maps fix the origin.

## The Classification

**Theorem (the two cases).** Let $\tilde q\in\mathbb{H}$. The square-root equation of the block has

1. for a **central** radicand $\tilde q=\lambda e_t$ with $\lambda\geq0$: the root set $\mathcal{R}(\lambda)$ of the preceding section, nonempty, of real dimension $3$ for $\lambda>0$ and the single point $\{0\}$ for $\lambda=0$;
2. for a **central** radicand $\tilde q=\lambda e_t$ with $\lambda<0$, and for every **noncentral** radicand: no root at all.

Solvability is therefore exactly the condition that the radicand be central with a nonnegative scalar part.

*Proof.* A root satisfies $\tilde x\star\tilde x=N(\tilde x)e_t$, which is central; comparing with $\tilde q$ gives the two cases, and the first is the theorem of the preceding section. There is no third case, and outside the value $0$ the root set is never a finite nonempty set: the equation is one scalar quadratic equation in four real unknowns, and its solution set is a three-dimensional sphere or empty.

**Remark (the collapse and what causes it).** The parent's classification separates the radicands by the scalar part and treats the noncentral radicands by a reduction to a scalar equation with a vector unknown (*Square Roots of a General Element in the General Plain Algebra*). The block needs none of that machinery, and the reason is structural: the product is central valued, so the square map loses the vector part entirely, and there is no associativity and no unit with which to reconstruct an element from its square. The collapse is the shadow of the centrality of the block, the same property that makes it a rank-one pairing.

## The Worked Examples

**Example (a noncentral radicand).** Let $\tilde q=\vec e_x$. The equation $\tilde x\star\tilde x=\vec e_x$ has no solution, since a square of the block is central and $\vec e_x$ is not. The block's only possible radicands are the multiples of $e_t$, and on this example the collapse is at its sharpest: in the parent plain algebra the same equation has roots, and the comparison is the witness of the collapse (*Square Roots of a General Element in the General Plain Algebra*).

**Example (the central value $\lambda=1$).** The roots are the unit sphere $N=1$, that is $Sp(1)$: the elements $\pm e_t$, the three units $\vec e_x,\vec e_y,\vec e_z$ and their negatives, and every element $x_0e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ with $x_0^{2}+|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|^{2}=1$. The root set is computed in *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra*.

**Example (the central value $\lambda=4$).** The roots are the level set $N=4$, the sphere $2\,Sp(1)$: it contains $\pm2e_t$, the elements $2\vec e_k$, and every element with $x_0^{2}+|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|^{2}=4$. Nothing in the root set is a root of the value $1$, the two level sets being disjoint.

**Example (the central value $\lambda=\tfrac14$).** The roots are the sphere $\tfrac12 Sp(1)$, of radius $\tfrac12$: it contains $\pm\tfrac12e_t$ and the elements with $N=\tfrac14$.

**Example (the radicand zero).** The roots of $0$ are the single element $0$: $\mathcal{R}(0)=\{0\}$, because the form is definite and $N(\tilde x)=0$ only at the origin. This is the whole difference from the complex chapter, where the roots of $0$ form the punctured isotropic cone; over $\mathbb{R}$ the isotropic cone collapses to the origin, and $0$ is the unique root of $0$, not a family.

**Example (the central value $\lambda=-1$).** The roots of $-e_t$ are none: a square of the block is a nonnegative multiple of $e_t$, so no element squares to the negative central element.

## Summary

In the symmetric quaternionic block the square of every element is central, $\tilde x\star\tilde x=N(\tilde x)e_t$, so the square-root problem has a solution only for the central radicands $\tilde q=\lambda e_t$, and solvability is exactly $\lambda\geq0$. For $\lambda>0$ the root set is the sphere $\sqrt{\lambda}Sp(1)$ of real dimension three, the orbit of $\sqrt{\lambda}e_t$ under the unit sphere of the plain product; for $\lambda=0$ it is the single point $\{0\}$; for $\lambda<0$ it is empty. A noncentral radicand has no root, the case of the general theory with a non-vanishing vector part does not occur, and the classification therefore has exactly two cases, with no finite nonempty root set apart from the point at the value $0$. The sign of the central value, which the complex chapter could always absorb by a complex square root, is the whole classification over $\mathbb{R}$; the special values $\lambda=1$ and $\lambda=-1$ are treated in *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* and the value $\lambda=0$ in *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde x\star\tilde x=N(\tilde x)e_t$ | the square of the block, always central |
| $\mathcal{R}(\lambda)=\{\tilde x:N(\tilde x)=\lambda\}$ | the root set of the central value $\lambda e_t$ |
| $\mathcal{R}(\lambda)=\sqrt{\lambda}Sp(1)$, $\lambda>0$ | the sphere of real dimension $3$ |
| $\mathcal{R}(0)=\{0\}$ | the single root of the value $0$ |
| $\mathcal{R}(\lambda)=\varnothing$, $\lambda<0$ | the negative central values have no root |
| noncentral radicand | no root |
| $Sp(1)=\{\tilde u:N(\tilde u)=1\}$ | the unit sphere of the plain product, the norm-one subgroup of the parent's group of units |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the general definitions of a power and of a square root of a central value
- *Square Roots of a General Element in the Quaternion Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-quaternion-algebra.md`), for the parent's classification, which the block collapses
- *Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the special radicands $+1$ and $-1$
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the cone of squares and the square root of a positive central element
- *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the radicand zero and the square-zero elements
- *Norm and Invertibility in the Symmetric Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the diagonal and the non-isotropic class
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the unit sphere of the quaternions and its role as a group of units.
- Michael Spivak, *Calculus on Manifolds* (Benjamin, 1965), for the level sets of a smooth function and the sphere as a submanifold.
