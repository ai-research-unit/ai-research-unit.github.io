# __Square Roots of One and the Idempotents of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra $\mathbb{B}^{\bullet}$ is the complex space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ under the Jordan product

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr)
$$

of *Introduction to the Symmetric Plain Algebra of Biquaternions*, the symmetrisation of the general plain bilinear product of *Introduction to the General Plain Algebra of Biquaternions*, and the operation named $\mathrm{SPA}$ in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. The square of the block is the **plain square**,

$$
\tilde Q\bullet\tilde Q=\tilde Q^2 :
$$

the symmetrisation moves only the antisymmetric part of the product, and that part vanishes on the diagonal (*The Symmetric and Antisymmetric Parts of an Algebra Product*).

The article treats two subjects, and in this order. The first is the square roots of the central value $+1$, the elements $\tilde\Xi\in\mathbb{B}$ with

$$
\tilde\Xi\bullet\tilde\Xi=e_0 .
$$

The second is the idempotents of the block, the elements $\tilde\Pi$ with

$$
\tilde\Pi\bullet\tilde\Pi=\tilde\Pi .
$$

The two subjects are one subject, because the **halving map**

$$
\tilde\Xi\longmapsto\tilde\Pi=\tfrac12(e_0+\tilde\Xi),\qquad \tilde\Xi\bullet\tilde\Xi=e_0,
$$

is a bijection from the roots of $+1$ onto the idempotents, with inverse $\tilde\Xi=2\tilde\Pi-e_0$. The reason is a two-line computation, and it uses only that the product is $\mathbb{C}$-bilinear and commutative with unit $e_0$: if $\tilde\Xi\bullet\tilde\Xi=e_0$ then $\tilde\Pi\bullet\tilde\Pi=\tfrac14(e_0+2\tilde\Xi+\tilde\Xi\bullet\tilde\Xi)=\tilde\Pi$; and if $\tilde\Pi\bullet\tilde\Pi=\tilde\Pi$ then $(2\tilde\Pi-e_0)\bullet(2\tilde\Pi-e_0)=4\tilde\Pi\bullet\tilde\Pi-4\tilde\Pi+e_0=e_0$. Every idempotent of the block is read through that map, on the roots of $+1$ alone, and the families of idempotents are the families of the roots of $+1$ read through it.

The roots of $+1$ of the block and the roots of $+1$ of the general plain product are the same set, the two squares being equal; the classification is the one of *Square Roots of One and the Idempotents of the General Plain Algebra*, restated here in the block's coordinates and with the block's reading. What the block adds to the classification is the reading of the pure roots as the indices of its idempotents, and of the non-trivial idempotents as its isotropic elements.

**The results.** The roots of $+1$ are the two central scalars $\pm e_0$; the two-real-parameter family $\pm i\vec n$ over the pure real quaternions $\vec n$ with $\vec n^2=-e_0$; and the four-real-parameter family $\vec\xi+i\vec\xi'$ with $\vec\xi\neq0$ and the two real conditions $\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2=-1$ and $\xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3=0$. Every idempotent of the block is trivial, $0$ or $e_0$, or of the form $\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$ with $\tilde\Xi$ a root of $+1$; the halving map is a bijection, carrying the class $\{\tilde\Xi,-\tilde\Xi\}$ to the complementary pair $\{\tilde\Pi,e_0-\tilde\Pi\}$. The Hermitian idempotents, the projections, are the images of the purely imaginary roots and form a two-real-parameter family in the Hermitian subspace; the non-trivial idempotents are isotropic, of vanishing central square, hence zero divisors with annihilator the line $\mathbb{C}(e_0-\tilde\Xi)$; and the block is not left-alternative, so a non-trivial idempotent gives **no** projector, only the unit does, and the Jordan theory gives the cubic Peirce identity $L^{\bullet}_{\tilde\Pi}(2L^{\bullet}_{\tilde\Pi}-\mathrm{id})(L^{\bullet}_{\tilde\Pi}-\mathrm{id})=0$ and the decomposition $\mathbb{B}=\mathbb{C}\tilde\Pi\oplus\mathbb{B}_{1/2}\oplus\mathbb{C}(e_0-\tilde\Pi)$ with $\dim_{\mathbb{C}}\mathbb{B}_{1/2}=2$. The roots of $-1$ are one paragraph, read off the roots of $+1$ by multiplication by $i$.

The article is algebraic. It does not treat the roots of the general quadratic $\tilde\Xi\bullet\tilde\Xi=\tilde Q$, which is *Square Roots of a General Element in the Symmetric Plain Algebra*; the roots of $0$ and the nilpotents, which are *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra*; the structure of the zero-divisor set, which is *Zero Divisors of the Symmetric Plain Algebra*; or the operator theory of the block, which is *The Multiplication Operators of the Symmetric Plain Algebra*. The last paragraph of §*The Roots of One* records how the roots of $-1$ are read off the roots of $+1$; it is a remark, it is used nowhere, and it opens nothing.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$, and central scalar imaginary $i$, $i^2=-1$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu=Q_0e_0+\vec Q$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=\sum_{k=1}^{3}Q_ke_k$. The general plain bilinear form of two vector parts is

$$
(\vec P,\vec Q)=\sum_{k=1}^{3}P_kQ_k,
$$

and the square of a pure element is $\vec Q^2=-(\vec Q,\vec Q)e_0$. The **central square** is

$$
\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=C(\tilde Q)e_0,\qquad C(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^2=Q_0^2+(\vec Q,\vec Q),
$$

the generic norm of the block, written $N(\tilde Q)$ in *Norm and Invertibility in the Symmetric Plain Algebra*. The natural conjugation is $\tilde Q^{\natural}=Q_0-\vec Q$ and the star is $\tilde Q^{*}=\overline{Q_0}-\overline{\vec Q}$. The remarkable subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$ are *Introduction to the Remarkable Subspaces* and *Remarkable Subspaces under the Symmetric Plain Algebra of Biquaternions*. A root of a central value is written $\tilde\Xi$ (§*The Root Convention* of *Conventions in Mathematics*), an idempotent $\tilde\Pi$ (§*The Idempotent Convention*), and a generic element $\tilde Q$.

The equations name a product, so the roots and the idempotents are relative to it. The general definition of the power, the square and the root of a central value, and the general definition of an idempotent, with the orthogonal, complete and primitive families, the projection and the Peirce decomposition, are *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots* and §*The Idempotent, the Projection and the Peirce Decomposition*. Throughout this article the square is the one of the symmetric plain product, which is the plain square; the other three general products and their parts carry roots and idempotents of their own, and they are *Comparison Between the Four General Products*.

## The Roots of One

**The roots of $+1$ are exactly the two central scalars $\pm e_0$, the two-real-parameter family $\pm i\vec n$ over the pure real quaternions $\vec n$ with $\vec n^2=-e_0$, and the four-real-parameter family $\vec\xi+i\vec\xi'$ with $\vec\xi\neq0$ and the two real conditions $\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2=-1$ and $\vec\xi\cdot\vec\xi'=0$; there are no others.**

A **root of $+1$** is an element $\tilde\Xi\in\mathbb{B}$ with $\tilde\Xi\bullet\tilde\Xi=e_0$, the square being the one of the symmetric plain product.

### The Reduction

Write the root in scalar and vector parts,

$$
\tilde\Xi=\Xi_0e_0+\vec\Xi,\qquad \vec\Xi=\Xi_1e_1+\Xi_2e_2+\Xi_3e_3,\qquad \Xi_k\in\mathbb{C}.
$$

The square of the block is the plain square, given by the product formula,

$$
\tilde\Xi\bullet\tilde\Xi=\tilde\Xi^2=\bigl(\Xi_0^2-(\vec\Xi,\vec\Xi)\bigr)e_0+2\Xi_0\vec\Xi,\qquad (\vec\Xi,\vec\Xi)=\Xi_1^2+\Xi_2^2+\Xi_3^2,
$$

so equating $\tilde\Xi^2$ to $e_0$ splits the equation into a vector part and a scalar part,

$$
2\Xi_0\vec\Xi=0,
$$

$$
\Xi_0^2-(\vec\Xi,\vec\Xi)=1 .
$$

Since $\mathbb{C}$ is a field, the vector equation holds exactly when $\Xi_0=0$ or $\vec\Xi=0$. The roots of $+1$ therefore split into two disjoint cases: the root is a complex scalar, $\vec\Xi=0$, or the root is pure, $\Xi_0=0$.

### The Trivial Roots

In the scalar case $\tilde\Xi=\Xi_0e_0$ and the scalar equation reads $\Xi_0^2=1$; the roots are the two central elements

$$
\tilde\Xi=+e_0,\qquad \tilde\Xi=-e_0 .
$$

### The Purely Imaginary Roots

In the pure case $\tilde\Xi=\vec\Xi$ and the scalar equation reads $(\vec\Xi,\vec\Xi)=-1$. Write the complex coefficients as $\Xi_k=\xi_k+i\xi'_k$ with real $\xi_k,\xi'_k$, so that the vector part splits into two real vector parts carrying the central imaginary on the second,

$$
\vec\Xi=\vec\xi+i\vec\xi',\qquad \vec\xi=\sum_{k=1}^{3}\xi_ke_k,\qquad \vec\xi'=\sum_{k=1}^{3}\xi'_ke_k .
$$

The subfamily with vanishing real part, $\vec\xi=0$, has $\vec\Xi=i\vec\xi'$ and $(\vec\Xi,\vec\Xi)=-\vec\xi'^2$, so the condition is $\vec\xi'^2=1$: the roots of this subfamily are

$$
\tilde\Xi=\pm i\vec n,\qquad \vec n\ \text{a pure real quaternion with}\ \vec n^2=-e_0,
$$

a two-real-parameter family, the **purely imaginary roots**. They are the elements $i\vec n$ with $\vec n$ a real unit vector, the sign being absorbed by $\vec n\mapsto-\vec n$.

### The Non-Trivial Roots

The remaining pure roots are those with $\vec\xi\neq0$. With $\vec\Xi=\vec\xi+i\vec\xi'$ the condition $(\vec\Xi,\vec\Xi)=-1$ is the single complex equation

$$
\vec\xi^2-\vec\xi'^2+2i\,\vec\xi\cdot\vec\xi'=-1,
$$

that is the two real equations

$$
\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2=-1,\qquad \xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3=0 .
$$

Six real coefficients carry two constraints, so the roots with $\vec\xi\neq0$ form a **four-real-parameter family**, the **non-trivial roots**; the condition $\vec\xi\neq0$ is exactly the separation from the purely imaginary family, whose real part vanishes. The two pure families together are the set of pure $\tilde\Xi$ with $(\vec\Xi,\vec\Xi)=-1$, that is the pure elements $\vec u$ with $\vec u^2=e_0$.

### Statement of the Theorem

**Theorem.** The roots of $+1$ in $\mathbb{B}$ are exactly the following.

**The trivial roots.** The two central elements

$$
\tilde\Xi=+e_0,\qquad \tilde\Xi=-e_0 .
$$

**The purely imaginary roots.** The two-real-parameter family

$$
\tilde\Xi=\pm i\vec n,\qquad \vec n=n_1e_1+n_2e_2+n_3e_3\ \text{real},\quad n_1^2+n_2^2+n_3^2=1 .
$$

**The non-trivial roots.** The four-real-parameter family

$$
\tilde\Xi=\vec\xi+i\vec\xi',\qquad \vec\xi\neq0,\qquad
\vec\xi^2-\vec\xi'^2=-1,\quad \vec\xi\cdot\vec\xi'=0,
$$

written in coordinates as the two real equations above. The two pure families together are the pure elements $\tilde\Xi$ with $(\vec\Xi,\vec\Xi)=-1$.

### Verification

For a pure $\tilde\Xi$ with $(\vec\Xi,\vec\Xi)=-1$ the scalar part of $\tilde\Xi^2$ is $-(\vec\Xi,\vec\Xi)=1$ and the vector part is $2\Xi_0\vec\Xi=0$, since $\Xi_0=0$; so such an element is a root of $+1$. The scalar case gives only $\pm e_0$, and the two cases are exhaustive by the reduction, because the vector equation forces $\Xi_0=0$ or $\vec\Xi=0$.

A worked instance of the purely imaginary family is

$$
\tilde\Xi=ie_1,\qquad (ie_1)^2=i^2e_1^2=(-1)(-e_0)=e_0,
$$

and a worked instance of the non-trivial family is

$$
\tilde\Xi=e_1+\sqrt2\,ie_2,\qquad (\vec\Xi,\vec\Xi)=1-2=-1,\qquad \tilde\Xi^2=-(\vec\Xi,\vec\Xi)e_0=e_0 .
$$

### Status of the Roots

Counting the free real parameters: the trivial roots are two isolated elements, the purely imaginary roots are a two-real-parameter family, and the non-trivial roots are a four-real-parameter family.

Every non-trivial root is pure, hence lies in the vector subspace; the trivial roots lie in the centre. A root of $+1$ is a **unit** of the block: $\tilde\Xi\bullet\tilde\Xi=e_0$ reads $\tilde\Xi\tilde\Xi=e_0$ in the plain product, so $\tilde\Xi$ is invertible in the algebra with inverse

$$
\tilde\Xi^{-1}=\tilde\Xi,
$$

and the inverse is an inverse of the block as well, the two products having the same unit. Every **pure** root, however, is a **zero divisor** of the block: the pure family of the block's zero-divisor set is the whole vector subspace, so every nonzero pure element annihilates a complex plane (*Zero Divisors of the Symmetric Plain Algebra*). The block therefore has invertible roots of $+1$ at which it is not regular, which the algebra does not; the trivial roots $\pm e_0$ lie in the centre and are units that are not zero divisors. The only element that is both a root of $+1$ and an idempotent is $e_0$: an element with $\tilde\Xi\bullet\tilde\Xi=e_0$ and $\tilde\Xi\bullet\tilde\Xi=\tilde\Xi$ has $\tilde\Xi=e_0$.

**The roots of minus one.** The roots of $-1$ are the elements $i\tilde\Xi$ with $\tilde\Xi$ a root of $+1$: the product is $\mathbb{C}$-bilinear with central $i$, so $(i\tilde\Xi)\bullet(i\tilde\Xi)=i^2(\tilde\Xi\bullet\tilde\Xi)=-e_0$, and $\tilde\Xi\mapsto i\tilde\Xi$ is a bijection because $i$ is invertible. The three families of the roots of $+1$ are carried to the central $\pm ie_0$, to the pure real quaternions $\pm\vec n$ with $\vec n^2=-e_0$, and to the family $-\vec\xi'+i\vec\xi$ with the same two real conditions; equivalently the roots of $-1$ are the central $\pm ie_0$ together with the pure elements $\tilde\Xi$ with $(\vec\Xi,\vec\Xi)=1$. The mechanism needs the central scalar of square $-1$ moved past the two slots, which the bilinearity of the block allows and a product conjugating one slot does not (*Comparison Between the Four General Products*). The roots of $-1$ are quoted here and are used nowhere in this article.

## The Idempotents

**Every idempotent of the block is trivial, $0$ or $e_0$, or of the form $\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$ with $\tilde\Xi$ a root of $+1$; the halving map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ is a bijection from the roots of $+1$ onto the idempotents; the non-trivial idempotents form a four-real-parameter family and are isotropic.**

The **idempotents** of the block are the elements satisfying $\tilde\Pi\bullet\tilde\Pi=\tilde\Pi$, the square being the one of the symmetric plain product. They are the algebraic form of a projection, and in the block they do three jobs at once: they are in bijection with the roots of $+1$ through the halving map, so their classification is the classification of those roots; they give the direct sum decomposition of the underlying space into a Peirce pair and the Jordan Peirce spaces; and their non-trivial members are exactly the isotropic idempotents, the scalar family of the block's zero divisors. The definition and the families are the general ones of *Definitions for the Study of the 12 Algebraic Structures*, read here in the symmetric plain product.

### The Definition

**Definition.** An element $\tilde\Pi$ of $\mathbb{B}$ is an **idempotent of the symmetric plain algebra** when

$$
\tilde\Pi\bullet\tilde\Pi=\tilde\Pi .
$$

The element $0$ is an idempotent, and so is the unit $e_0$; the two are the **trivial idempotents**. The equation names a product, and the notion is relative to it: throughout this article the product is the symmetric plain product $\bullet$, and another product is named where it is meant. Because the square of the block is the plain square, the equation is the plain equation,

$$
\tilde\Pi^{2}=\tilde\Pi\qquad\Longleftrightarrow\qquad \tilde\Pi\bullet\tilde\Pi=\tilde\Pi ,
$$

and the idempotents of the block are exactly the idempotents of the general plain product. The classification of the algebra applies verbatim; it is restated here in the block's coordinates and with the block's reading. The idempotents of the other three general products and of the parts are not these, and the sets are tabulated in *Comparison Between the Four General Products*.

### The Classification

**The idempotents of the block are exactly the two trivial ones $0$ and $e_0$ and the non-trivial family $\tilde\Pi=\tfrac12(e_0+\vec u)$ with $\vec u$ pure, $\vec u\neq0$ and $\vec u^2=e_0$, a four-real-parameter family; the map $\vec u\mapsto\tfrac12(e_0+\vec u)$ is a bijection from the pure roots of $+1$ onto the non-trivial idempotents.**

**Theorem (the idempotents).** The idempotents of the block are exactly the following.

**The two trivial idempotents.**

$$
\tilde\Pi=0,\qquad \tilde\Pi=e_0 .
$$

**The non-trivial idempotents.** The elements

$$
\tilde\Pi=\tfrac12\bigl(e_0+\vec u\bigr),\qquad \vec u\in\mathrm{Vect}(\mathbb{B}),\quad \vec u\neq0,\quad \vec u^2=e_0 ,
$$

a four-real-parameter family.

**Proof.** Write $\tilde\Pi=\Pi_0e_0+\vec\Pi$ and use the plain square $\tilde\Pi^2=\bigl[\Pi_0^2-(\vec\Pi,\vec\Pi)\bigr]e_0+2\Pi_0\vec\Pi$. The equation $\tilde\Pi^2=\tilde\Pi$ is the pair

$$
2\Pi_0\vec\Pi=\vec\Pi,\qquad \Pi_0^2-(\vec\Pi,\vec\Pi)=\Pi_0 .
$$

The first forces $(2\Pi_0-1)\vec\Pi=0$: either $\vec\Pi=0$, and the second gives $\Pi_0^2=\Pi_0$, that is $\tilde\Pi=0$ or $\tilde\Pi=e_0$; or $\Pi_0=\tfrac12$, and then $(\vec\Pi,\vec\Pi)=-\tfrac14$, that is $\vec\Pi=\tfrac12\vec u$ with $\vec u$ pure and $(\vec u,\vec u)=-1$, which is $\vec u^2=e_0$. The two cases are exhaustive.

The pure $\vec u$ with $\vec u^2=e_0$ are the pure roots of $+1$, classified in §*The Roots of One*; the condition $\vec u\neq0$ excludes the value that would give the element $\tfrac12e_0$, which is not idempotent. The non-trivial family is therefore a four-real-parameter family, and it is disjoint from the trivial idempotents.

### The Halving Map and the Bijection With the Roots of One

**The map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ is a bijection from the roots of $+1$ onto the idempotents, carrying the class $\{\tilde\Xi,-\tilde\Xi\}$ to the complementary pair $\{\tilde\Pi,e_0-\tilde\Pi\}$.**

**Theorem.** The map

$$
\tilde\Xi\longmapsto\tilde\Pi(\tilde\Xi),\qquad \tilde\Pi(\tilde\Xi)=\tfrac12(e_0+\tilde\Xi),
$$

is a **bijection** from the set of roots of $+1$ onto the set of idempotents of the block.

**Proof.** *Well defined:* if $\tilde\Xi\bullet\tilde\Xi=e_0$, then

$$
\tilde\Pi(\tilde\Xi)\bullet\tilde\Pi(\tilde\Xi)=\tfrac14(e_0+\tilde\Xi)\bullet(e_0+\tilde\Xi)=\tfrac14(e_0+2\tilde\Xi+\tilde\Xi\bullet\tilde\Xi)=\tfrac12(e_0+\tilde\Xi)=\tilde\Pi(\tilde\Xi),
$$

using bilinearity, commutativity and $\tilde\Xi\bullet\tilde\Xi=e_0$. *Injective:* $\tilde\Pi(\tilde\Xi)=\tilde\Pi(\tilde\Xi')$ gives $\tilde\Xi=\tilde\Xi'$. *Surjective:* the classification theorem says every idempotent is trivial or $\tfrac12(e_0+\vec u)$ with $\vec u$ a pure root of $+1$, and the trivial idempotents are $\tilde\Pi(\pm e_0)$.

Consequently the **complementary pairs** $\{\tilde\Pi,e_0-\tilde\Pi\}$ of idempotents are in bijection with the roots of $+1$ modulo the sign identification $\tilde\Xi\sim-\tilde\Xi$, since

$$
\tilde\Pi(-\tilde\Xi)=\tfrac12(e_0-\tilde\Xi)=e_0-\tilde\Pi(\tilde\Xi).
$$

The inverse of the halving map is $\tilde\Xi=2\tilde\Pi-e_0$.

### The Families of Idempotents

Substituting the classification of the roots of $+1$ into the halving map gives the families of idempotents.

- For the trivial roots $\tilde\Xi=\pm e_0$: $\tilde\Pi=\tfrac12(e_0\pm e_0)$ is $e_0$ or $0$. These are the **trivial idempotents**.
- For the purely imaginary roots $\tilde\Xi=\pm i\vec n$: $\tilde\Pi=\tfrac12 e_0\pm\tfrac12 i\vec n$. Since $i\vec n$ is fixed by the star for a pure real $\vec n$, these idempotents are **Hermitian**, $\tilde\Pi^{*}=\tilde\Pi$, and they are the **projections** of the block; they lie in the Hermitian subspace $\mathbb{M}_+$, and they form a two-real-parameter family. An idempotent fixed by the star is an orthogonal projection, orthogonality being read from the Hermitian form of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (*Definitions for the Study of the 12 Algebraic Structures*, §*The Idempotent, the Projection and the Peirce Decomposition*).
- For the non-trivial roots $\tilde\Xi=\vec\xi+i\vec\xi'$ with $\vec\xi\neq0$ and the two real conditions of §*The Non-Trivial Roots*: $\tilde\Pi=\tfrac12 e_0+\tfrac12(\vec\xi+i\vec\xi')$. Its vector part carries both a nonzero real part $\vec\xi$ and a nonzero imaginary part $\vec\xi'$, so the idempotent lies in none of the four four-dimensional subspaces $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_{-}$ (*Remarkable Subspaces under the Symmetric Plain Algebra of Biquaternions*).

The idempotents inherit the size of the root set. Since the halving map is a bijection and the trivial roots are isolated, the Hermitian idempotents form a two-real-parameter family and the remaining non-trivial idempotents form a four-real-parameter family. Every non-trivial idempotent is a zero divisor, as §*The Idempotents and the Zero Divisors* shows, so the non-trivial idempotents lie in the zero-divisor set of *Zero Divisors of the Symmetric Plain Algebra*, while the trivial idempotents $0$ and $e_0$ are outside it, $e_0$ being a unit.

### The Complementary Idempotent

**Proposition.** If $\tilde\Pi$ is an idempotent, then so is $e_0-\tilde\Pi$, and the two are orthogonal:

$$
(e_0-\tilde\Pi)^{\bullet2}=e_0-\tilde\Pi,\qquad \tilde\Pi\bullet(e_0-\tilde\Pi)=0 .
$$

**Proof.** $(e_0-\tilde\Pi)\bullet(e_0-\tilde\Pi)=e_0-2\tilde\Pi+\tilde\Pi^{\bullet2}=e_0-\tilde\Pi$, using $\tilde\Pi^{\bullet2}=\tilde\Pi$; and $\tilde\Pi\bullet(e_0-\tilde\Pi)=\tilde\Pi-\tilde\Pi^{\bullet2}=0$.

So an idempotent and its complement split the underlying $\mathbb{C}$-space,

$$
\mathbb{B}=\mathbb{C}\tilde\Pi\oplus\mathbb{C}(e_0-\tilde\Pi)\ \oplus\ \mathbb{B}_{1/2},
$$

the middle space being the one of §*The Jordan Peirce Decomposition*; the block is commutative, so there is no distinction of left and right in the decomposition, and the orthogonality $\tilde\Pi\bullet(e_0-\tilde\Pi)=0$ is the vanishing of the cross piece.

### The Idempotents and the Zero Divisors

**Every non-trivial idempotent has vanishing central square, $C(\tfrac12(e_0+\vec u))=0$, hence is isotropic and a zero divisor whose annihilator is the complex line $\mathbb{C}(e_0-\vec u)$, while the trivial idempotents $0$ and $e_0$ are not zero divisors; conversely every non-pure zero divisor is the complex multiple $2Q_0\tilde\Pi$ of a non-trivial idempotent.**

**Proposition (the idempotents are isotropic).** Every non-trivial idempotent has vanishing central square,

$$
C\bigl(\tfrac12(e_0+\vec u)\bigr)=\tfrac14\bigl(1+(\vec u,\vec u)\bigr)=0 ,
$$

while the unit has $C(e_0)=1\neq0$ and the origin is the trivial idempotent excluded by the definition of a zero divisor.

The non-trivial idempotents are therefore **isotropic** and, by the criterion of *Zero Divisors of the Symmetric Plain Algebra*, they are zero divisors: the annihilator of $\tfrac12(e_0+\vec u)$ is the complex line

$$
\mathbb{C}\,(e_0-\vec u)=\mathbb{C}\,\tilde\Pi^{\natural},
$$

the line spanned by the natural conjugate. The trivial idempotents $0$ and $e_0$ are not zero divisors, the origin being excluded by the definition and the unit being invertible. Conversely, a non-pure zero divisor — a zero divisor with $Q_0\neq0$ — satisfies $\tilde Q\bullet\tilde Q=2Q_0\tilde Q$ and is a complex multiple of a non-trivial idempotent,

$$
\tilde Q=2Q_0\tilde\Pi,\qquad \tilde\Pi=\frac{\tilde Q}{2Q_0};
$$

the derivation and the two families of the zero-divisor set are *Zero Divisors of the Symmetric Plain Algebra*.

### The Absence of the Associative Peirce Calculus

**Proposition (no non-trivial idempotent gives a projector).** For a non-trivial idempotent $\tilde\Pi$ the left multiplication is not a projector, $L^{\bullet}_{\tilde\Pi}\circ L^{\bullet}_{\tilde\Pi}\neq L^{\bullet}_{\tilde\Pi}$; only the unit $e_0$ gives the identity operator.

**Proof.** On the witness $\tilde\Pi=\tfrac12(e_0+ie_1)$ the operator $L^{\bullet}_{\tilde\Pi}$ has the three distinct eigenvalues $0,\tfrac12,1$ (below), so $L^{\bullet}_{\tilde\Pi}(L^{\bullet}_{\tilde\Pi}-\mathrm{id})\neq0$. The reason is structural: the identity $L^{\bullet}_{\tilde X}{}^{2}=L^{\bullet}_{\tilde X^{\bullet2}}$ at every $\tilde X$ is left alternativity, the block is not left-alternative, and the chain $L^{\bullet}_{\tilde\Pi}{}^{2}=L^{\bullet}_{\tilde\Pi^{\bullet2}}=L^{\bullet}_{\tilde\Pi}$ that makes an idempotent a projector therefore breaks at its second step (*The Specificities of the Symmetric Plain Algebra*).

**The absence is stated and not filled.** The block has no projector calculus of the non-trivial idempotents, no corner subalgebras of the associative kind, and no ideal lattice generated by an idempotent: those are theorems of a left-alternative structure and the block is not one. What it has is the decomposition the Jordan theory allows, which is the next subsection.

### The Jordan Peirce Decomposition

**Theorem (the cubic Peirce identity).** For every idempotent $\tilde\Pi$ of the block the left multiplication satisfies

$$
2L^{\bullet}_{\tilde\Pi}{}^{3}-3L^{\bullet}_{\tilde\Pi}{}^{2}+L^{\bullet}_{\tilde\Pi}=0,
\qquad\text{that is}\qquad L^{\bullet}_{\tilde\Pi}\bigl(2L^{\bullet}_{\tilde\Pi}-\mathrm{id}\bigr)\bigl(L^{\bullet}_{\tilde\Pi}-\mathrm{id}\bigr)=0 .
$$

**Proof.** The identity is the polynomial identity of an idempotent in a Jordan algebra; in the block it is the statement that the eigenvalues of $L^{\bullet}_{\tilde\Pi}$ lie in $\{0,\tfrac12,1\}$, which is recomputed below on the witness and follows in general from the multiplication by $\tilde\Pi$ being a degree-two derivation of the quadric.

**Theorem (the decomposition).** Let $\tilde\Pi$ be a non-trivial idempotent and let

$$
\mathbb{B}_{\lambda}=\{\tilde Y\in\mathbb{B}:\ \tilde\Pi\bullet\tilde Y=\lambda\tilde Y\},\qquad \lambda\in\{0,\tfrac12,1\}.
$$

Then $\mathbb{B}=\mathbb{B}_{1}\oplus\mathbb{B}_{1/2}\oplus\mathbb{B}_{0}$ and the three spaces are:

$$
\mathbb{B}_{1}=\mathbb{C}\tilde\Pi,\qquad \mathbb{B}_{0}=\mathbb{C}(e_0-\tilde\Pi),\qquad \dim_{\mathbb{C}}\mathbb{B}_{1/2}=2 .
$$

**Proof.** By the cubic identity the operator $L^{\bullet}_{\tilde\Pi}$ has the minimal polynomial $t(t-\tfrac12)(t-1)$ with distinct roots, so it is diagonalisable and the three eigenspaces add to the whole space. The eigenvalue $1$ is realised by $\tilde\Pi$ and the eigenvalue $0$ by $e_0-\tilde\Pi$; the trace $\operatorname{Tr}L^{\bullet}_{\tilde\Pi}=4\Pi_0=2$ is the sum of the eigenvalues counted with multiplicity, so $1+0+\tfrac12\dim\mathbb{B}_{1/2}=2$ and the middle space has dimension two.

The middle space is the Jordan analogue of the two mixed Peirce spaces of an associative algebra; it is a single space and not a pair, because the product is commutative, and it is a bimodule and not a subalgebra. The decomposition is the **Jordan Peirce decomposition** of the block relative to $\tilde\Pi$, and it is the form the Jordan theory allows; the deeper theory of the Peirce spaces is *The Multiplication Operators of the Symmetric Plain Algebra*.

## Summary

The square of the block is the plain square, so the roots of $+1$ of the block are exactly the roots of $+1$ of the general plain algebra, and the classification transfers without change. The roots of $+1$ are the two central scalars $\pm e_0$; the two-real-parameter family $\pm i\vec n$ over the pure real quaternions with $\vec n^2=-e_0$; and the four-real-parameter family $\vec\xi+i\vec\xi'$ with $\vec\xi\neq0$, $\vec\xi^2-\vec\xi'^2=-1$ and $\vec\xi\cdot\vec\xi'=0$; the two pure families together are the pure elements $\vec u$ with $\vec u^2=e_0$. Every root of $+1$ is a unit, and every pure root is a zero divisor, so the block has invertible roots of $+1$ that are not regular. The roots of $-1$ are the elements $i\tilde\Xi$ over the roots of $+1$: the central $\pm ie_0$, the pure real unit quaternions, and the family $-\vec\xi'+i\vec\xi$.

The idempotents of the block are the idempotents of the plain product, the two squares being equal. They are the origin, the unit, and the four-real-parameter family $\tfrac12(e_0+\vec u)$ with $\vec u$ pure and $\vec u^2=e_0$; the halving map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ is a bijection from the roots of $+1$ onto the idempotents, with inverse $\tilde\Xi=2\tilde\Pi-e_0$, and it carries $\{\tilde\Xi,-\tilde\Xi\}$ to $\{\tilde\Pi,e_0-\tilde\Pi\}$. The Hermitian idempotents, the projections, are the images of the purely imaginary roots and lie in $\mathbb{M}_+$; the non-Hermitian non-trivial idempotents lie in none of the four four-dimensional subspaces. Every non-trivial idempotent is isotropic, $C=0$, and is a zero divisor whose annihilator is the line spanned by its natural conjugate, while the two trivial idempotents are not zero divisors; conversely every non-pure zero divisor is $2Q_0$ times a non-trivial idempotent. An idempotent and its complement $e_0-\tilde\Pi$ are orthogonal idempotents. The block is not left-alternative, so a non-trivial idempotent does **not** give a projector and there is no associative Peirce calculus, no corner subalgebra and no ideal lattice; only the unit gives the identity operator. What survives is the Jordan theory: the cubic Peirce identity $L^{\bullet}_{\tilde\Pi}(2L^{\bullet}_{\tilde\Pi}-\mathrm{id})(L^{\bullet}_{\tilde\Pi}-\mathrm{id})=0$ and the decomposition $\mathbb{B}=\mathbb{C}\tilde\Pi\oplus\mathbb{B}_{1/2}\oplus\mathbb{C}(e_0-\tilde\Pi)$ with a two-dimensional middle space.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q$ | the symmetric plain product, the multiplication of the block |
| $\tilde\Xi$ | a root either of $+1$, $\tilde\Xi\bullet\tilde\Xi=e_0$, or of $-1$ when invoked in the remark |
| $\pm e_0$, $\pm i\vec n$, $\vec\xi+i\vec\xi'$ | the trivial, purely imaginary and non-trivial roots of $+1$ |
| $(\vec\Xi,\vec\Xi)=\Xi_1^2+\Xi_2^2+\Xi_3^2$ | the complex square of the vector part, deciding the pure families |
| $C(\tilde Q)=\sum_\mu Q_\mu^2=\tilde Q\tilde Q^{\natural}$ | the central square, the generic norm $N$ |
| $\tilde\Pi$ | an idempotent of the block, $\tilde\Pi^{\bullet2}=\tilde\Pi$ |
| $\tfrac12(e_0+\vec u)$, $\vec u^2=e_0$ pure | the non-trivial idempotents |
| $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$, $\tilde\Xi=2\tilde\Pi-e_0$ | the halving bijection from the roots of $+1$ onto the idempotents |
| $e_0-\tilde\Pi$ | the complementary idempotent, orthogonal to $\tilde\Pi$ |
| $2L^{\bullet}_{\tilde\Pi}{}^{3}-3L^{\bullet}_{\tilde\Pi}{}^{2}+L^{\bullet}_{\tilde\Pi}=0$ | the cubic Peirce identity |
| $\mathbb{B}_{1}\oplus\mathbb{B}_{1/2}\oplus\mathbb{B}_{0}$ | the Jordan Peirce decomposition, of dimensions $1,2,1$ |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots* and §*The Idempotent, the Projection and the Peirce Decomposition*, for the product-relative definitions.
- *Square Roots of One and the Idempotents of the General Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra.md`), for the classification of the roots of $+1$ and of the idempotents the block restates.
- *Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-plain-algebra.md`), for the roots of $0$, the companion central value.
- *Square Roots of a General Element in the Symmetric Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-symmetric-plain-algebra.md`), for the general root problem $\tilde\Xi\bullet\tilde\Xi=\tilde Q$.
- *Zero Divisors of the Symmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-algebra.md`), for the pure family of the zero divisors and the isotropic idempotents.
- *The Specificities of the Symmetric Plain Algebra* (`articles_maths/the-specificities-of-the-symmetric-plain-algebra.md`), for the left alternativity the block fails and the Jordan law it satisfies.
- *The Multiplication Operators of the Symmetric Plain Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-algebra.md`), for the Peirce spaces and the structure algebra.
- *Remarkable Subspaces under the Symmetric Plain Algebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-symmetric-plain-algebra-of-biquaternions.md`), for the Hermitian subspace and the placement of the idempotents.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the cubic Peirce identity and the Peirce decomposition of a Jordan algebra.
