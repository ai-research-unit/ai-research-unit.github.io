# __Square Roots of One and the Idempotents of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra $\mathbb{H}^{\bullet}$ is the real space $\mathbb{H}$ under the Jordan product

$$
\tilde p\bullet\tilde q=\tfrac12\bigl(\tilde p\tilde q+\tilde q\tilde p\bigr)
$$

of *Introduction to the Symmetric Plain Algebra of Quaternions*, the symmetrisation of the general plain bilinear product of *Introduction to the General Plain Algebra of Quaternions*, and the operation named $\mathrm{SPA}$ in *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*. The square of the block is the **plain square**, $\tilde p\bullet\tilde p=\tilde p^2$: the symmetrisation moves only the antisymmetric part of the product, and that part vanishes on the diagonal (*The Symmetric and Antisymmetric Parts of an Algebra Product*).

The article treats two subjects, and in this order. The first is the square roots of the central value $+e_0$, the elements $\tilde\xi\in\mathbb{H}$ with $\tilde\xi\bullet\tilde\xi=e_0$. The second is the idempotents of the block, the elements $\tilde\pi$ with $\tilde\pi\bullet\tilde\pi=\tilde\pi$. The two subjects are one subject, because the **halving map**

$$
\tilde\xi\longmapsto\tilde\pi=\tfrac12(e_0+\tilde\xi),\qquad \tilde\xi\bullet\tilde\xi=e_0,
$$

is a bijection from the roots of $+e_0$ onto the idempotents, with inverse $\tilde\xi=2\tilde\pi-e_0$. The reason is a two-line computation, and it uses only that the product is real-bilinear and commutative with unit $e_0$: if $\tilde\xi\bullet\tilde\xi=e_0$ then $\tilde\pi\bullet\tilde\pi=\tfrac14(e_0+2\tilde\xi+\tilde\xi\bullet\tilde\xi)=\tilde\pi$; and if $\tilde\pi\bullet\tilde\pi=\tilde\pi$ then $(2\tilde\pi-e_0)\bullet(2\tilde\pi-e_0)=4\tilde\pi\bullet\tilde\pi-4\tilde\pi+e_0=e_0$. Every idempotent of the block is read through that map, on the roots of $+e_0$ alone.

The roots of $+e_0$ of the block and the roots of $+e_0$ of the general plain product are the same set, the two squares being equal. Over $\mathbb{R}$ the set is small: the square of a pure element is the negative scalar $-|\vec u|^2e_0$, so the pure branch carries no root of $+e_0$ and the roots are the two central scalars $\pm e_0$ alone. It is this definiteness that collapses the idempotent class of the block to the two trivial elements, while the complex block, whose pure square is indefinite, carries whole families of both.

**The results.** The roots of $+e_0$ are the two central scalars $\pm e_0$, and there are no others; the class is the two-point set, the centre of the level set $\{N=1\}$ of the algebra. The idempotents are the origin and the unit, $\tilde\pi\in\{0,e_0\}$; the halving map $\tilde\xi\mapsto\tfrac12(e_0+\tilde\xi)$ is a bijection carrying the pair $\{\tilde\xi,-\tilde\xi\}$ to the complementary pair $\{\tilde\pi,e_0-\tilde\pi\}$; and the Jordan Peirce decomposition is degenerate, $J_1(e_0)=\mathbb{H}$ and $J_0(0)=\mathbb{H}$, the middle space never opening. The roots of $-e_0$ are one paragraph: over $\mathbb{R}$ the centre has no element of square $-e_0$, the sign cannot be flipped, and the roots of $-e_0$ are read from the same reduction as the pure elements of norm one.

The article is algebraic. It does not treat the roots of the general quadratic $\tilde\xi\bullet\tilde\xi=\tilde q$, which is *Square Roots of a General Element in the Symmetric Plain Algebra*; the roots of $0$ and the nilpotents, which are *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*; the structure of the zero-divisor set, which is *Zero Divisors of the Symmetric Plain Algebra*; or the operator theory of the block, which is *The Multiplication Operators of the Symmetric Plain Algebra*. The last paragraph of §*The Roots of One* records how the roots of $-e_0$ are read; it is a remark, it is used nowhere, and it opens nothing.

**Conventions.** The algebra is $\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$, so that $e_k^2=-e_0$ and $e_je_k=-e_ke_j$ for $j\neq k$. An element is $\tilde q=q_0e_0+\vec q$ with $\vec q=\sum_{k=1}^{3}q_ke_k$ and $q_\mu\in\mathbb{R}$; $\vec p\cdot\vec q=\sum_kp_kq_k$ is the Euclidean dot product of the vector parts, and the plain square is $\tilde q^2=(q_0^2-|\vec q|^2)e_0+2q_0\vec q$. The **norm** is $N(\tilde q)=\tilde q\tilde q^{\natural}=q_0^2+|\vec q|^2$; the natural sign ${}^{\natural}$ is the quaternion conjugation, the bar is the identity because $\mathbb{R}$ has no nontrivial involution, and the star coincides with the natural sign. The scalar line $\mathbb{R}e_0$ is the centre and the vector subspace is $\mathrm{Vect}(\mathbb{H})=\operatorname{Im}\mathbb{H}$ (*Introduction to the Remarkable Subspaces of the Quaternions*). The left multiplication is $L^{\bullet}_{\tilde p}\tilde q=\tilde p\bullet\tilde q$. A root of a central value is written $\tilde\xi$ (§*The Root Convention* of *Conventions in Mathematics*), an idempotent $\tilde\pi$ (§*The Idempotent Convention*), and a generic element $\tilde p$ or $\tilde q$.

The equations name a product, so the roots and the idempotents are relative to it. The general definition of the power, the square and the root of a central value, and the general definition of an idempotent, are *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, §*The Element Vocabulary*. Throughout this article the square is the one of the symmetric plain product, which is the plain square; the other five structures over the same space carry roots and idempotents of their own.

## The Roots of One

**The roots of $+e_0$ are exactly the two central scalars $\pm e_0$; there are no others, and the class is the two-point set.**

A **root of $+e_0$** is an element $\tilde\xi\in\mathbb{H}$ with $\tilde\xi\bullet\tilde\xi=e_0$, the square being the one of the symmetric plain product.

### The Reduction

Write the root in scalar and vector parts,

$$
\tilde\xi=\xi_0e_0+\vec\xi,\qquad \vec\xi=\xi_1e_1+\xi_2e_2+\xi_3e_3,\qquad \xi_k\in\mathbb{R}.
$$

The square of the block is the plain square, so equating $\tilde\xi^2$ to the central element $\lambda e_0$ splits the equation into a vector part and a scalar part. **Proposition (the central reduction).** For $\tilde\xi=\xi_0e_0+\vec\xi$ and $\lambda\in\mathbb{R}$,

$$
\tilde\xi\bullet\tilde\xi=\lambda e_0\qquad\Longleftrightarrow\qquad
\begin{cases}
2\xi_0\vec\xi=0,\\[2pt]
\xi_0^2-|\vec\xi|^2=\lambda .
\end{cases}
$$

*Proof.* The plain square is $\tilde\xi^2=(\xi_0^2-|\vec\xi|^2)e_0+2\xi_0\vec\xi$, and the element is central exactly when its vector part vanishes, which is the displayed pair.

Since $\mathbb{R}$ is a field, the vector equation holds exactly when $\xi_0=0$ or $\vec\xi=0$. **Only the scalar equation survives on each branch**: the root is pure, $\vec\xi=0$ failing, or it is a real scalar, $\vec\xi=0$. The reduction is the one of *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra* at $\lambda=0$ and of *Square Roots of a General Element in the Symmetric Plain Algebra* for a general radicand.

### The Pure Case Is Empty

In the pure case $\tilde\xi=\vec\xi$ and the scalar equation reads $-|\vec\xi|^2=\lambda$. For $\lambda=+1$ this is

$$
|\vec\xi|^2=-1,
$$

a value no real vector attains. **There is no pure root of $+e_0$.** The reason is the definiteness of the Euclidean form of the vector subspace: the square of a pure element is the negative scalar $\vec u\bullet\vec u=-|\vec u|^2e_0$, so a pure element can be a root of a negative central value and never of a positive one.

### The Trivial Roots

In the scalar case $\tilde\xi=\xi_0e_0$ and the scalar equation reads $\xi_0^2=1$, whose roots are the two central elements

$$
\tilde\xi=+e_0,\qquad \tilde\xi=-e_0 .
$$

### Statement of the Theorem

**Theorem.** The roots of $+e_0$ of the block are exactly the two central scalars

$$
\tilde\xi=+e_0,\qquad \tilde\xi=-e_0,
$$

the class being the two-point set $\{+e_0,-e_0\}$.

*Proof.* By the reduction the root is pure or scalar. The pure case is impossible, $|\vec\xi|^2=-1$ having no real solution. The scalar case gives $\xi_0^2=1$, that is $\pm e_0$. The two cases exhaust the equation and the set has two elements.

### Verification

The two elements are roots, $\tilde\xi\bullet\tilde\xi=\tilde\xi^2=(\pm e_0)^2=e_0$, and nothing else is, because the reduction yields only the two branches and the pure branch is empty. The class is the **central part of the level set** $\{N=1\}$ of the algebra: the level set is the elements of norm one, and its central elements are $\pm e_0$.

A worked instance outside the block is the root of the general plain product, which is the same element: the plain square and the block square agree, so the two products share the two roots, and the two-point set is the smallest of the three central classes of the chapter.

### The Roots of One Are Units

A root of $+e_0$ is a **unit** of the block: $\tilde\xi\bullet\tilde\xi=e_0$ reads $\tilde\xi\tilde\xi=e_0$ in the plain product, so $\tilde\xi$ is invertible in the algebra with inverse $\tilde\xi^{-1}=\tilde\xi^{\natural}/N(\tilde\xi)=\pm e_0$, and the inverse is an inverse of the block as well, the two products sharing the unit. The only element that is both a root of $+e_0$ and an idempotent is $e_0$: an element with $\tilde\xi\bullet\tilde\xi=e_0$ and $\tilde\xi\bullet\tilde\xi=\tilde\xi$ has $\tilde\xi=e_0$. The two classes are different sets, and the halving map of §*The Idempotents* is the bijection between them.

### The Comparison with the Plain Product

The roots of $+e_0$ of the block coincide element for element with the roots of $+e_0$ of the general plain product, the two squares being equal; the plain product is a division rule and its roots of $+e_0$ are the same two central scalars. Over the complex block the pure square is indefinite, $\vec U^2=+(\vec U,\vec U)e_0$ taking both signs, and the root set of $+e_0$ there is larger: the pure roots form families and the idempotents they index are the non-trivial ones the real block does not have. **The smallness of the real root and idempotent sets is the definiteness of the Euclidean form**, and it is the whole of the difference between the two blocks at the value $+e_0$.

**The roots of minus one.** For a bilateral product the sign can be flipped by multiplication by a **central imaginary**, an element $i$ of the centre with $i^2=-e_0$, since $(i\tilde\xi)\star(i\tilde\xi)=i^2(\tilde\xi\star\tilde\xi)=-\tilde\xi\star\tilde\xi$; over $\mathbb{R}$ the centre is the scalar line $\mathbb{R}e_0$ and no central element has square $-e_0$, so the mechanism is unavailable and the roots of $-e_0$ are **not** the image of the roots of $+e_0$. They follow from the same reduction: the pure branch of $\lambda=-1$ is $|\vec\xi|^2=1$, a quadric of real dimension two in the vector subspace. The class exists, it is not empty, and it indexes no idempotent; the halving map uses the roots of $+e_0$ alone.

## The Idempotents

**The idempotents of the block are exactly the origin and the unit, $\tilde\pi\in\{0,e_0\}$; the class is the two-point set, and there is no non-trivial idempotent.**

The **idempotents** of the block are the elements satisfying $\tilde\pi\bullet\tilde\pi=\tilde\pi$, the square being the one of the symmetric plain product. They are the algebraic form of a projection, and the block has only the two trivial ones; what remains of the theory is the halving map from the roots of $+e_0$, the complementary pairs, and a degenerate Peirce decomposition.

### The Definition and the Equation

**Definition (idempotent of a product).** Let $\star$ be a product on $\mathbb{H}$; then $\tilde\pi$ is an **idempotent of $\star$** when $\tilde\pi\star\tilde\pi=\tilde\pi$.

The origin is an idempotent of every product, and a product with a unit has the unit as an idempotent. Throughout this article the product is the symmetric plain product $\bullet$, and the equation is $\tilde\pi\bullet\tilde\pi=\tilde\pi$. Because the square of the block is the plain square, the equation is the equation of the algebra,

$$
\tilde\pi^2=\tilde\pi\qquad\Longleftrightarrow\qquad \tilde\pi\bullet\tilde\pi=\tilde\pi ,
$$

and the idempotents of the block are exactly the idempotents of the plain product. The classification of the plain product applies verbatim; it is restated here in the block's coordinates and with the block's reading.

### The Classification

**Theorem (the idempotents).** The idempotents of the block are exactly the origin and the unit:

$$
\tilde\pi\in\{0,\ e_0\}.
$$

There is no non-trivial idempotent.

*Proof.* Write the equation as $\tilde\pi^2=\tilde\pi$ and factor it as $\tilde\pi(\tilde\pi-e_0)=0$. The plain product of $\mathbb{H}$ is a **division rule**: it has the two-sided unit $e_0$ and no zero divisor, every non-zero element being invertible with $\tilde\pi^{-1}=\tilde\pi^{\natural}/N(\tilde\pi)$ (*Introduction to the General Plain Algebra of Quaternions*). A vanishing product in a division algebra has a vanishing factor, so either $\tilde\pi=0$ or $\tilde\pi-e_0=0$, and the class is the two elements displayed. The same conclusion in the block's coordinates reads the plain square $\tilde\pi^2=(\pi_0^2-|\vec\pi|^2)e_0+2\pi_0\vec\pi$ and the pair $2\pi_0\vec\pi=\vec\pi$, $\pi_0^2-|\vec\pi|^2=\pi_0$: the first forces $(2\pi_0-1)\vec\pi=0$, and $\vec\pi\neq0$ with $\pi_0=\tfrac12$ would give $|\vec\pi|^2=-\tfrac14$, which has no real solution, so $\vec\pi=0$ and $\pi_0\in\{0,1\}$. **The two cases exhaust the equation and no non-trivial idempotent occurs.**

**Remark (why the class collapses over $\mathbb{R}$).** The standard construction of a non-trivial idempotent of a symmetrised product is the element $\tfrac12(e_0+\vec u)$ with $\vec u$ a **pure root of $+e_0$**: the square $\tfrac14(e_0+2\vec u+\vec u^2)$ equals $\tfrac12(e_0+\vec u)$ exactly when $\vec u^2=e_0$. Over $\mathbb{R}$ the square of a pure element is $\vec u\bullet\vec u=-|\vec u|^2e_0$, a non-positive scalar, so it equals $+e_0$ only for $|\vec u|^2=-1$, a value no real vector attains. **There is no pure root of $+e_0$, the construction never closes, and the class is the two trivial idempotents**, the collapse being the algebraic form of the absence of the split.

**Corollary (the class is two-point).** The idempotent class of the block is $\{0,e_0\}$, and the two are orthogonal, $0\bullet e_0=0$.

### The Halving Map

The idempotents of a degree-two block correspond to the **roots of $+e_0$** under the affine map $\tilde\xi\mapsto\tfrac12(e_0+\tilde\xi)$. The map is an involution of the space, and it converts the idempotent equation into the root equation and back.

**Proposition (the halving bijection).** The map $\tilde\xi\mapsto\tilde\pi=\tfrac12(e_0+\tilde\xi)$ is a bijection from the roots of $+e_0$ onto the idempotents, with inverse $\tilde\xi=2\tilde\pi-e_0$, and it carries the pair $\{\tilde\xi,-\tilde\xi\}$ to the complementary pair $\{\tilde\pi,e_0-\tilde\pi\}$.

*Proof.* The equivalence $\tilde\pi\bullet\tilde\pi=\tilde\pi\Longleftrightarrow(2\tilde\pi-e_0)\bullet(2\tilde\pi-e_0)=e_0$ is the two-line computation of the introduction, read in both directions. *Injective and surjective:* if $\tilde\xi$ is a root of $+e_0$ then $\tilde\pi=\tfrac12(e_0+\tilde\xi)$ is an idempotent, and every idempotent arises so, its inverse image being $\tilde\xi=2\tilde\pi-e_0$; the two maps are inverse to each other, using the bilinearity, the commutativity and $\tilde\xi\bullet\tilde\xi=e_0$. *The pair:* $\tilde\pi(-\tilde\xi)=\tfrac12(e_0-\tilde\xi)=e_0-\tilde\pi(\tilde\xi)$.

**Corollary (the correspondence).** The roots of $+e_0$ being the two points $\pm e_0$, the correspondence is

$$
0\longleftrightarrow-e_0,\qquad e_0\longleftrightarrow+e_0,
$$

so the two-point idempotent class is the image of the two-point root class, and the count of the idempotents of the block equals the count of the roots of $+e_0$, two on each side.

**Remark (the roots of $-e_0$ index no idempotent).** The roots of $-e_0$ are the pure elements with $|\vec\xi|^2=1$, a quadric of the vector subspace, and they do not index idempotents: the map $\vec u\mapsto\tfrac12(e_0+\vec u)$ sends such a root to an element whose square is $\tfrac14(1-|\vec u|^2)e_0+\tfrac12\vec u=\tfrac12\vec u$, a pure element and not an idempotent. Only the roots of $+e_0$ serve, and over $\mathbb{R}$ there are two of them.

### The Complementary Idempotent

**Proposition (the complementary idempotent).** If $\tilde\pi$ is an idempotent of the block, then so is $e_0-\tilde\pi$, and the two are **orthogonal**:

$$
(e_0-\tilde\pi)^{\bullet2}=e_0-\tilde\pi,\qquad \tilde\pi\bullet(e_0-\tilde\pi)=0 .
$$

*Proof.* $(e_0-\tilde\pi)\bullet(e_0-\tilde\pi)=e_0-2\tilde\pi+\tilde\pi^{\bullet2}=e_0-\tilde\pi$, using $\tilde\pi^{\bullet2}=\tilde\pi$; and $\tilde\pi\bullet(e_0-\tilde\pi)=\tilde\pi-\tilde\pi^{\bullet2}=0$.

**Corollary (the complement swaps the two idempotents).** For the two idempotents of the block the map $\tilde\pi\mapsto e_0-\tilde\pi$ is the exchange

$$
0\longleftrightarrow e_0,
$$

and $0\bullet e_0=0$. The complement is available because $e_0$ is the unit, and it is the reason the two-point class is stable under it; the origin and the unit are orthogonal idempotents.

### The Jordan Peirce Decomposition

**Theorem (the cubic Peirce identity).** For every idempotent $\tilde\pi$ of the block the left multiplication satisfies

$$
2(L^{\bullet}_{\tilde\pi})^3-3(L^{\bullet}_{\tilde\pi})^2+L^{\bullet}_{\tilde\pi}=0,
\qquad\text{that is}\qquad L^{\bullet}_{\tilde\pi}\bigl(2L^{\bullet}_{\tilde\pi}-\mathrm{id}\bigr)\bigl(L^{\bullet}_{\tilde\pi}-\mathrm{id}\bigr)=0 .
$$

*Proof.* The identity is the polynomial identity of an idempotent in a Jordan algebra (*Jordan Algebras*); in the block it is immediate at the only two idempotents. At $\tilde\pi=e_0$ the operator is the identity, $L^{\bullet}_{e_0}=\mathrm{id}$, and $2-3+1=0$; at $\tilde\pi=0$ the operator vanishes, $L^{\bullet}_{0}=0$, and the identity is $0=0$.

**Theorem (the decomposition).** Let $\tilde\pi$ be an idempotent and let

$$
J_{\lambda}(\tilde\pi)=\{\tilde x\in\mathbb{H}:\ \tilde\pi\bullet\tilde x=\lambda\tilde x\},\qquad \lambda\in\bigl\{0,\tfrac12,1\bigr\}.
$$

Then the decomposition is **trivial**:

$$
J_1(e_0)=\mathbb{H},\quad J_{1/2}(e_0)=J_0(e_0)=0;
\qquad
J_0(0)=\mathbb{H},\quad J_1(0)=J_{1/2}(0)=0 .
$$

*Proof.* $L^{\bullet}_{e_0}=\mathrm{id}$ has the single eigenvalue $1$ with multiplicity four, so its Peirce space is the whole space and the other two vanish; $L^{\bullet}_{0}=0$ has the single eigenvalue $0$ with multiplicity four, and the roles are exchanged.

**Remark (the would-be shape does not occur).** A non-trivial idempotent of a degree-two Jordan algebra of this kind would split the space into three Peirce spaces of dimensions $1,2,1$, with a two-dimensional middle space. The block has no such idempotent, so **the middle space never occurs and the Peirce calculus is degenerate**. There is no projector calculus of a non-trivial idempotent, no corner subalgebra and no ideal lattice, because over $\mathbb{R}$ the idempotent that would carry them does not exist: the objects are absent, and the calculus is empty with them. The specific-theory companion is *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, and the element-class reading is *The Specificities of the Symmetric Plain Algebra*.

### The Reading on the Remarkable Subspaces

Over $\mathbb{R}$ the remarkable subspaces are the scalar line, which is the centre, and the vector subspace (*Introduction to the Remarkable Subspaces of the Quaternions*).

**The centre.** The scalar line $\mathbb{R}e_0$ is the centre of the block, and its elements are the central elements $\lambda e_0$. A scalar element is idempotent exactly when $\lambda^2=\lambda$, that is when $\lambda\in\{0,1\}$, so the centre contains the two idempotents $0$ and $e_0$ and no other. Every idempotent of the block is central, the class being $\{0,e_0\}$.

**The vector subspace.** A non-zero pure element $\vec u$ has the square

$$
\vec u\bullet\vec u=\vec u^2=-|\vec u|^2e_0,
$$

a non-zero scalar, so it can equal the pure element $\vec u$ only if both vanish: **the vector subspace contains no idempotent but the origin**, and the unit $e_0$ is the only idempotent outside it.

## Summary

The square of the block is the plain square, so the roots of $+e_0$ of the block are exactly the roots of $+e_0$ of the general plain algebra. Over $\mathbb{R}$ the class is small: the roots of $+e_0$ are the two central scalars $\pm e_0$, because the pure branch would need $|\vec\xi|^2=-1$ and the square of a pure element is the non-positive scalar $-|\vec u|^2e_0$. Every root of $+e_0$ is a unit of the block, and the only element that is both a root of $+e_0$ and an idempotent is $e_0$. The roots of $-e_0$ are quoted in a closing paragraph: over $\mathbb{R}$ the centre has no element of square $-e_0$, so the sign-flip is unavailable, and the class is the pure elements with $|\vec\xi|^2=1$, a quadric of real dimension two, which is used nowhere.

The idempotents of the block are the idempotents of the plain product, the two squares being equal. They are the origin and the unit, $\tilde\pi\in\{0,e_0\}$, a two-point class with no non-trivial member; the reason is that a non-trivial idempotent needs a pure root of $+e_0$, and the pure square is the non-positive scalar $-|\vec u|^2e_0$, which never equals $+e_0$. The complement $e_0-\tilde\pi$ is an idempotent and is orthogonal to $\tilde\pi$, and it exchanges the origin and the unit. The halving map $\tilde\xi\mapsto\tfrac12(e_0+\tilde\xi)$ is a bijection from the roots of $+e_0$ onto the idempotents, with inverse $\tilde\xi=2\tilde\pi-e_0$, carrying the pair $\{\tilde\xi,-\tilde\xi\}$ to the complementary pair; on the two roots $\pm e_0$ it is the correspondence $0\leftrightarrow-e_0$, $e_0\leftrightarrow+e_0$. The cubic Peirce identity holds at both idempotents, the Peirce decomposition is trivial, $J_1(e_0)=\mathbb{H}$ and $J_0(0)=\mathbb{H}$, and the would-be middle space of dimension two never opens. On the remarkable subspaces every idempotent is central, and the vector subspace contains no idempotent but the origin.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde p\bullet\tilde q$ | the symmetric plain product, the multiplication of the block |
| $\tilde\xi$ | a root either of $+e_0$, $\tilde\xi\bullet\tilde\xi=e_0$, or of $-e_0$ in the closing remark |
| $\{+e_0,-e_0\}$ | the roots of $+e_0$, the two-point class |
| $|\vec\xi|^2=1$ | the roots of $-e_0$, a quadric of the vector subspace |
| $\tilde\pi$ | an idempotent of the block, $\tilde\pi^{\bullet2}=\tilde\pi$ |
| $\{0,e_0\}$ | the idempotents, the two-point class |
| $\vec u\bullet\vec u=-|\vec u|^2e_0$ | the pure square, never a root of $+e_0$ |
| $\tilde\xi\mapsto\tfrac12(e_0+\tilde\xi)$, $\tilde\xi=2\tilde\pi-e_0$ | the halving bijection from the roots of $+e_0$ onto the idempotents |
| $e_0-\tilde\pi$ | the complementary idempotent, orthogonal to $\tilde\pi$ |
| $2(L^{\bullet}_{\tilde\pi})^3-3(L^{\bullet}_{\tilde\pi})^2+L^{\bullet}_{\tilde\pi}=0$ | the cubic Peirce identity |
| $J_1(e_0)=\mathbb{H}$, $J_0(0)=\mathbb{H}$ | the trivial Peirce decomposition |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, §*The Element Vocabulary*, for the product-relative definition of an idempotent.
- *Introduction to the Symmetric Plain Algebra of Quaternions*, for the product, the unit and the square.
- *Introduction to the General Plain Algebra of Quaternions*, for the division property of the plain product that leaves only the two trivial idempotents.
- *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-plain-algebra-of-quaternioid.md`), for the roots of $0$, the companion central value.
- *Square Roots of a General Element in the Symmetric Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-symmetric-plain-algebra-of-quaternioid.md`), for the general root problem $\tilde\xi\bullet\tilde\xi=\tilde q$, of which the roots of $+e_0$ here are one case.
- *Square Roots of One and the Idempotents of the General Plain Algebra*, for the roots of $-e_0$ and their finer structure, which the block shares with the plain product.
- *Zero Divisors of the Symmetric Plain Algebra*, for the idempotents read against the zero divisors, which carry no non-trivial one.
- *Norm and Invertibility in the Symmetric Plain Algebra*, for the norm, the level set $\{N=1\}$ and the invertibility of the non-zero elements.
- *The Square, the Idempotents and the Jordan Inverse of the Symmetric Plain Algebra*, for the specific-theory reading of the same class and its Peirce decomposition.
- *The Specificities of the Symmetric Plain Algebra*, for the degeneracy of the class and the definiteness of the norm that produces it.
- *The Multiplication Operators of the Symmetric Plain Algebra*, for the operator whose powers enter the Peirce identity.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the halving map, the cubic Peirce identity and the Peirce decomposition of a Jordan algebra.
