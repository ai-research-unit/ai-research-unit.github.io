# __Square Roots of One and the Idempotents of the Biquaternion Algebra__

## Introduction

Of the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, exactly one makes the underlying complex space of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ an associative unital $\mathbb{C}$-algebra; the algebra is *Introduction to the Biquaternion Algebra*, and its multiplication is the general plain bilinear product of two biquaternions, $\tilde Q_1\tilde Q_2$, the product being the one of the algebra. That product is the one read throughout this article.

The article treats two subjects, and in this order. The first is the square roots of the central value $+1$, the elements $\tilde\Xi\in\mathbb{B}$ with

$$
\tilde\Xi^2=e_t .
$$

The second is the idempotents of the algebra, the elements $\tilde\Pi$ with $\tilde\Pi^2=\tilde\Pi$. The two subjects are one subject, because the **halving map**

$$
\tilde\Xi\longmapsto\tilde\Pi=\tfrac12(e_t+\tilde\Xi),\qquad \tilde\Xi^2=e_t,
$$

is a bijection from the roots of $+1$ onto the idempotents, with inverse $\tilde\Xi=2\tilde\Pi-e_t$. A root carries two idempotents and not one: with $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi)$ and $\tilde\Pi_-(\tilde\Xi)=\tfrac12(e_t-\tilde\Xi)$, the two are a complete orthogonal pair, $\tilde\Pi_+(\tilde\Xi)+\tilde\Pi_-(\tilde\Xi)=e_t$ and $\tilde\Pi_+(\tilde\Xi)\tilde\Pi_-(\tilde\Xi)=0$, and the root is their difference, $\tilde\Xi=\tilde\Pi_+(\tilde\Xi)-\tilde\Pi_-(\tilde\Xi)$. The reason is a two-line computation: if $\tilde\Xi^2=e_t$ then $\tilde\Pi^2=\tfrac14(e_t+2\tilde\Xi+e_t)=\tilde\Pi$, and if $\tilde\Pi^2=\tilde\Pi$ then $(2\tilde\Pi-e_t)^2=4\tilde\Pi^2-4\tilde\Pi+e_t=e_t$. Every idempotent of the algebra is read through that map, on the roots of $+1$ alone, and the families of idempotents are the families of the roots of $+1$ read through it.

**The results.** The roots of $+1$ are the two central scalars $\pm e_t$; the two-real-parameter family $\pm i\vec u$ over the real unit vectors $\vec u$ with $\vec u^2=-e_t$; and the four-real-parameter family $\vec\xi+i\vec\xi'$ with $\vec\xi\neq0$ and the two real conditions $\xi_x^2+\xi_y^2+\xi_z^2-(\xi'_x)^2-(\xi'_y)^2-(\xi'_z)^2=-1$ and $\xi_x\xi'_x+\xi_y\xi'_y+\xi_z\xi'_z=0$. Every idempotent of the algebra is trivial, $0$ or $e_t$, or of the form $\tilde\Pi=\tfrac12(e_t+\tilde\Xi)$ with $\tilde\Xi$ a root of $+1$; the trivial roots give the trivial idempotents, the family $\pm i\vec u$ gives the Hermitian idempotents, and the non-trivial roots give a four-real-parameter family of idempotents lying in none of the four four-dimensional remarkable subspaces. Each root carries the two idempotents $\tilde\Pi_+=\tfrac12(e_t+\tilde\Xi)$ and $\tilde\Pi_-=\tfrac12(e_t-\tilde\Xi)=e_t-\tilde\Pi_+$, a complete orthogonal pair whose difference is the root; the class $\{\tilde\Xi,-\tilde\Xi\}$ gives the same unordered pair.

The article is algebraic. It does not treat the roots of the general quadratic $\tilde\Xi^2=\tilde Q$, which is *Square Roots of a General Element in the Biquaternion Algebra*; the roots of $0$ and the nilpotents, which are *Square Roots of Zero and the Nilpotents of the Biquaternion Algebra*; the structure of the zero-divisor set, which is *Zero Divisors of the Biquaternion Algebra*; or the ideals the standard idempotents generate, which are *Ideals and Peirce Decomposition of the Biquaternion Algebra*. The last paragraph of §*The Roots of One* records how the roots of $-1$ are read off the roots of $+1$; it is a remark, it is used nowhere, and it opens nothing.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and $\vec e_x\vec e_y=\vec e_z$, and central scalar imaginary $i$, $i^2=-1$. A general element is $\tilde Q=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu=Q_te_t+\vec Q$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=\sum_{k=1}^{3}Q_k\vec e_k$. The natural conjugation is $\tilde Q^{\natural}=Q_t-\vec Q$ and the star is $\tilde Q^{*}=\overline{Q_t}-\overline{\vec Q}$. The general plain bilinear form of two vector parts is

$$
(\vec Q_1,\vec Q_2)=\sum_{k=1}^{3}Q_{1k}Q_{2k},
$$

and the square of a pure element is $\vec Q^2=-(\vec Q,\vec Q)e_t$. The remarkable subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$ are *Introduction to the Remarkable Subspaces*. A root of a central value is written $\tilde\Xi$ (§*The Root Convention* of *Conventions in Mathematics*), an idempotent $\tilde\Pi$ (§*The Idempotent Convention*), the two members of a complete pair with the two signs, $\tilde\Pi_+$ and $\tilde\Pi_-$, the subscript $+$ naming the member attached to $+1$, and a generic element $\tilde Q$.

The equations name a product, so the roots and the idempotents are relative to it. The general definition of the power, the square and the root of a central value is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots*, and the general definition of an idempotent, with the orthogonal, complete and primitive families, the Hermitian idempotent and the Peirce decomposition, is the same article. Throughout this article the square is the one of the general plain bilinear product, the multiplication of the algebra; the other three general products carry roots and idempotents of their own, and they are *Comparison Between the Four General Products*.

## The Roots of One

**The roots of $+1$ are exactly the two central scalars $\pm e_t$, the two-real-parameter family $\pm i\vec u$ over the real unit vectors $\vec u$ with $\vec u^2=-e_t$, and the four-real-parameter family $\vec\xi+i\vec\xi'$ with $\vec\xi\neq0$ and the two real conditions; there are no others.**

A **root of $+1$** is an element $\tilde\Xi\in\mathbb{B}$ with $\tilde\Xi^2=e_t$, the square being the one of the general plain bilinear product.

### The Reduction

Write the root in scalar and vector parts,

$$
\tilde\Xi=\Xi_te_t+\vec\Xi,\qquad \vec\Xi=\Xi_x\vec e_x+\Xi_y\vec e_y+\Xi_z\vec e_z,\qquad \Xi_k\in\mathbb{C},
$$

and write the complex coefficients as $\Xi_k=\xi_k+i\xi'_k$ with real $\xi_k,\xi'_k$, so that the vector part splits into two real vector parts,

$$
\vec\Xi=\vec\xi+i\vec\xi',\qquad \vec\xi=\xi_x\vec e_x+\xi_y\vec e_y+\xi_z\vec e_z,\qquad \vec\xi'=\xi'_x\vec e_x+\xi'_y\vec e_y+\xi'_z\vec e_z .
$$

The square of a biquaternion is given by the product formula,

$$
\tilde\Xi^2=\bigl(\Xi_t^2-(\vec\Xi,\vec\Xi)\bigr)e_t+2\Xi_t\vec\Xi,\qquad (\vec\Xi,\vec\Xi)=\Xi_x^2+\Xi_y^2+\Xi_z^2,
$$

so equating $\tilde\Xi^2$ to $e_t$ splits the equation into a vector part and a scalar part,

$$
2\Xi_t\vec\Xi=0,
$$

$$
\Xi_t^2-(\vec\Xi,\vec\Xi)=1 .
$$

Since $\mathbb{C}$ is a field, the vector equation holds exactly when $\Xi_t=0$ or $\vec\Xi=0$. The roots of $+1$ therefore split into two disjoint cases: the root is a complex scalar, $\vec\Xi=0$, or the root is pure, $\Xi_t=0$.

### The Trivial Roots

In the scalar case $\tilde\Xi=\Xi_te_t$ and the scalar equation reads $\Xi_t^2=1$, so $\Xi_t=\pm1$. The roots in this case are the two elements

$$
\tilde\Xi=+e_t,\qquad \tilde\Xi=-e_t,
$$

the **trivial roots** of $+1$. They are the only roots of $+1$ in the centre $\mathbb{C}e_t$, and the only ones with non-vanishing scalar part.

### The Purely Imaginary Roots

In the pure case $\tilde\Xi=\vec\Xi$ and the scalar equation reads

$$
(\vec\Xi,\vec\Xi)=\Xi_x^2+\Xi_y^2+\Xi_z^2=-1 .
$$

Take first the case in which the vector part is the central imaginary times a real vector, $\vec\Xi=i\vec u$ with $\vec u$ a unit real vector. Since $i$ is central and $\vec u^2=-\|\vec u\|^2e_t$ with $\|\vec u\|^2=u_x^2+u_y^2+u_z^2$, one has

$$
(i\vec u)^2=i^2\vec u^2=(-1)\bigl(-\|\vec u\|^2e_t\bigr)=\|\vec u\|^2e_t,
$$

so such an element is a root of $+1$ exactly when $\|\vec u\|^2=1$, that is when $\vec u^2=-e_t$. The roots in this case are the elements

$$
\tilde\Xi=+i\vec u,\qquad \tilde\Xi=-i\vec u,\qquad \vec u\ \text{a unit real vector with}\ \vec u^2=-e_t,
$$

a **two-real-parameter family**: three real coefficients of $\vec u$ carrying the single condition $u_x^2+u_y^2+u_z^2=1$. Its members are the only roots of $+1$ that are pure multiples of a real quaternion, and each is Hermitian, $(\tilde\Xi)^{*}=\tilde\Xi$.

### The Non-Trivial Roots

Let now the vector part be genuinely complex, $\vec\Xi=\vec\xi+i\vec\xi'$ with $\vec\xi,\vec\xi'$ real pure. Then

$$
(\vec\Xi,\vec\Xi)=\sum_{k=1}^{3}(\xi_k+i\xi'_k)^2=\bigl(\xi_x^2+\xi_y^2+\xi_z^2-(\xi'_x)^2-(\xi'_y)^2-(\xi'_z)^2\bigr)+2i\bigl(\xi_x\xi'_x+\xi_y\xi'_y+\xi_z\xi'_z\bigr),
$$

so the single complex equation $(\vec\Xi,\vec\Xi)=-1$ is the two real equations

$$
\xi_x^2+\xi_y^2+\xi_z^2-(\xi'_x)^2-(\xi'_y)^2-(\xi'_z)^2=-1,\qquad \xi_x\xi'_x+\xi_y\xi'_y+\xi_z\xi'_z=0 .
$$

The case $\vec\xi=0$ requires $(\xi'_x)^2+(\xi'_y)^2+(\xi'_z)^2=1$ and is the two-parameter family of the previous paragraph. The remaining case is $\vec\xi\neq0$: six real coefficients carrying the two constraints, hence a four-real-parameter family. Its elements are the **non-trivial roots** of $+1$,

$$
\tilde\Xi=\vec\xi+i\vec\xi',\qquad \vec\xi\neq0,
$$

$$
\xi_x^2+\xi_y^2+\xi_z^2-(\xi'_x)^2-(\xi'_y)^2-(\xi'_z)^2=-1,\qquad \xi_x\xi'_x+\xi_y\xi'_y+\xi_z\xi'_z=0,
$$

equivalently $\vec\xi\vec\xi'+\vec\xi'\vec\xi=0$. For such a root the imaginary part is automatically nonzero: if $\vec\xi'=0$ the first equation would give $\xi_x^2+\xi_y^2+\xi_z^2=-1$, impossible, the three squares being non-negative.

### Statement of the Theorem

**Theorem.** The roots of $+1$ in $\mathbb{B}$ are exactly the elements of the three following families.

**The trivial roots.** The two central elements

$$
\tilde\Xi=+e_t,\qquad \tilde\Xi=-e_t .
$$

**The purely imaginary roots.** The two-real-parameter family

$$
\tilde\Xi=+i\vec u,\qquad \tilde\Xi=-i\vec u,\qquad \vec u=u_x\vec e_x+u_y\vec e_y+u_z\vec e_z,\ u_k\in\mathbb{R},\ u_x^2+u_y^2+u_z^2=1,
$$

equivalently over the real unit vectors with $\vec u^2=-e_t$; since $i$ is central the family is also written $\tilde\Xi=\pm\vec u i$.

**The non-trivial roots.** The four-real-parameter family

$$
\tilde\Xi=\vec\xi+i\vec\xi'=\bigl(\xi_x\vec e_x+\xi_y\vec e_y+\xi_z\vec e_z\bigr)+i\bigl(\xi'_x\vec e_x+\xi'_y\vec e_y+\xi'_z\vec e_z\bigr),\qquad \vec\xi\neq0,
$$

whose six real coefficients satisfy the two conditions

$$
\xi_x^2+\xi_y^2+\xi_z^2-(\xi'_x)^2-(\xi'_y)^2-(\xi'_z)^2=-1,\qquad \xi_x\xi'_x+\xi_y\xi'_y+\xi_z\xi'_z=0,
$$

equivalently $\vec\xi\vec\xi'+\vec\xi'\vec\xi=0$.

The three families are disjoint, and together they are all the roots.

### Verification

Each family consists of roots of $+1$.

**Trivial roots.** $(\pm e_t)^2=e_t$.

**Purely imaginary roots.** For $\vec u^2=-e_t$, $(i\vec u)^2=i^2\vec u^2=(-1)(-e_t)=e_t$.

**Non-trivial roots.** Expanding,

$$
\tilde\Xi^2=(\vec\xi+i\vec\xi')^2=\vec\xi^2-(\vec\xi')^2+i\bigl(\vec\xi\vec\xi'+\vec\xi'\vec\xi\bigr).
$$

Now $\vec\xi^2=-\bigl(\xi_x^2+\xi_y^2+\xi_z^2\bigr)e_t$, $(\vec\xi')^2=-\bigl((\xi'_x)^2+(\xi'_y)^2+(\xi'_z)^2\bigr)e_t$, and the mixed term is a central multiple,

$$
\vec\xi\vec\xi'+\vec\xi'\vec\xi=-2\bigl(\xi_x\xi'_x+\xi_y\xi'_y+\xi_z\xi'_z\bigr)e_t=0,
$$

by the second condition. Hence

$$
\tilde\Xi^2=-\bigl(\xi_x^2+\xi_y^2+\xi_z^2-(\xi'_x)^2-(\xi'_y)^2-(\xi'_z)^2\bigr)e_t=-(-1)e_t=e_t,
$$

by the first condition.

### Status of the Roots

Counting the free real parameters: the trivial roots are two isolated elements, the purely imaginary roots are a two-real-parameter family, and the non-trivial roots are a four-real-parameter family.

Every root except the trivial ones is pure, hence lies in the six-real-dimensional vector subspace of pure biquaternions; the trivial roots lie in the centre. A root of $+1$ is a **unit**: $\tilde\Xi^2=e_t$ reads $\tilde\Xi\tilde\Xi=e_t$, so $\tilde\Xi$ is invertible with inverse

$$
\tilde\Xi^{-1}=\tilde\Xi,
$$

and a unit is not a zero divisor. The single element common to the roots of $+1$ and the idempotents is $e_t$: an element that is both a root of $+1$ and an idempotent satisfies $\tilde\Xi^2=e_t$ and $\tilde\Xi^2=\tilde\Xi$, hence $\tilde\Xi=e_t$.

**The roots of minus one.** For this product the central imaginary turns the roots of $+1$ into the roots of $-1$: if $\tilde\Xi^2=e_t$ then $(i\tilde\Xi)^2=i^2\tilde\Xi^2=-e_t$, because $i$ is central, and since $i$ is invertible the map $\tilde\Xi\mapsto i\tilde\Xi$ is a bijection from the roots of $+1$ onto the roots of $-1$. The three families above are carried to the three families of the roots of $-1$: the two central scalars $\pm i$; the family $\pm\vec u$ over the real unit vectors with $\vec u^2=-e_t$; and the family $-\vec\xi'+i\vec\xi$ with the same two real conditions. The mechanism is not universal. It needs a central scalar of square $-1$ that can be moved past the two slots of the product; in a sesquilinear product, where the second slot conjugates, scalar multiplication cannot flip the sign this way, and the roots of $-1$ are then read from the roots of $+1$ by no such map, or are absent altogether. The roots of $-1$ are quoted here and are used nowhere in this article.

## The Idempotents

**Every idempotent of $\mathbb{B}$ is trivial, $0$ or $e_t$, or of the form $\tilde\Pi=\tfrac12(e_t+\tilde\Xi)$ with $\tilde\Xi$ a root of $+1$; a root carries the two idempotents $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi)$ and $\tilde\Pi_-(\tilde\Xi)=\tfrac12(e_t-\tilde\Xi)=e_t-\tilde\Pi_+(\tilde\Xi)$, a complete orthogonal pair whose difference is the root; the halving map $\tilde\Xi\mapsto\tfrac12(e_t+\tilde\Xi)$ is a bijection from the roots of $+1$ onto the idempotents; and the non-trivial idempotents form a four-real-parameter family.**

The **idempotents** of $\mathbb{B}$ are the elements satisfying $\tilde\Pi^2=\tilde\Pi$, the square being the one of the general plain bilinear product. They correspond to projectors under multiplication, and in $\mathbb{B}$ they do four separate jobs at once: they give the direct sum decompositions of the algebra into left ideals, and in particular the two minimal left ideals; they classify the non-pure zero divisors, every one of which is a complex multiple of an idempotent; they are in bijection with the roots of $+1$ through the halving map, each root carrying a complete orthogonal pair, so their classification is the classification of those roots; and they drive the Peirce decomposition of the algebra. The definition and the families are the general ones of *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, read here in the general plain bilinear product.

### The Definition

**Definition.** An element $\tilde\Pi$ of $\mathbb{B}$ is an **idempotent of the biquaternion algebra** when

$$
\tilde\Pi^2=\tilde\Pi .
$$

The element $0$ is an idempotent, and so is the unit $e_t$; the two are the **trivial idempotents**. The equation names a product, and the notion is relative to it: throughout this article the product is the general plain bilinear product, the multiplication of the algebra, and another product is named where it is meant. The idempotents of the other three general products are not these, and the four sets are tabulated in *Comparison Between the Four General Products*.

Idempotents encode direct summands of the algebra: an idempotent $\tilde\Pi$ and its complement $e_t-\tilde\Pi$ split the underlying $\mathbb{C}$-module,

$$
\mathbb{B}=\mathbb{B}\tilde\Pi\oplus\mathbb{B}(e_t-\tilde\Pi),\qquad \mathbb{B}=\tilde\Pi\mathbb{B}\oplus(e_t-\tilde\Pi)\mathbb{B},
$$

and every such decomposition arises from an idempotent. A **primitive** idempotent, one that is not a sum of two nonzero orthogonal idempotents, generates a minimal left ideal. The general statements, with the orthogonal, complete and primitive families, the Hermitian idempotent and the Peirce decomposition, are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

### The Two Idempotents of a Root

**A root $\tilde\Xi$ of $+1$ carries the two idempotents $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi)$ and $\tilde\Pi_-(\tilde\Xi)=\tfrac12(e_t-\tilde\Xi)=e_t-\tilde\Pi_+(\tilde\Xi)$; the two are idempotent by the same computation, and the root is their difference, $\tilde\Xi=\tilde\Pi_+(\tilde\Xi)-\tilde\Pi_-(\tilde\Xi)$.**

Let $\tilde\Xi$ be a root of $+1$, so that $\tilde\Xi^2=e_t$. The **two idempotents of the root** are the elements

$$
\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi),\qquad \tilde\Pi_-(\tilde\Xi)=\tfrac12(e_t-\tilde\Xi).
$$

The pair is written with the two signs rather than with two numbers, as §*The Idempotent Convention* of *Conventions in Mathematics* provides for a complete pair: the subscript $+$ names the member attached to $+1$, the subscript $-$ the member attached to $-1$.

They are complementary, $\tilde\Pi_+(\tilde\Xi)+\tilde\Pi_-(\tilde\Xi)=e_t$, and each is idempotent:

$$
\tilde\Pi_+(\tilde\Xi)^2=\tfrac14(e_t+\tilde\Xi)^2=\tfrac14(e_t+2\tilde\Xi+\tilde\Xi^2)=\tfrac14(2e_t+2\tilde\Xi)=\tilde\Pi_+(\tilde\Xi),
$$

$$
\tilde\Pi_-(\tilde\Xi)^2=\tfrac14(e_t-\tilde\Xi)^2=\tfrac14(e_t-2\tilde\Xi+\tilde\Xi^2)=\tfrac14(2e_t-2\tilde\Xi)=\tilde\Pi_-(\tilde\Xi).
$$

The complementarity reads $\tilde\Pi_-(\tilde\Xi)=e_t-\tilde\Pi_+(\tilde\Xi)$, and the difference of the two recovers the root,

$$
\tilde\Pi_+(\tilde\Xi)-\tilde\Pi_-(\tilde\Xi)=\tilde\Xi .
$$

The trivial roots give the trivial pairs: the pair of $+e_t$ is $(e_t,0)$ and the pair of $-e_t$ is $(0,e_t)$. Every root therefore carries exactly two idempotents, and the next section computes what the two do together.

### The Arithmetic of the Pair of Idempotents

**The pair of a root is complete, $\tilde\Pi_+ + \tilde\Pi_-=e_t$; the root is its difference, $\tilde\Pi_+ - \tilde\Pi_-=\tilde\Xi$; the pair is orthogonal, $\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0$; and multiplication by the root is the sign change of the pair, $+1$ on $\tilde\Pi_+$ and $-1$ on $\tilde\Pi_-$.**

Throughout this section $\tilde\Xi$ is a root of $+1$ and $\tilde\Pi_+=\tilde\Pi_+(\tilde\Xi)$, $\tilde\Pi_-=\tilde\Pi_-(\tilde\Xi)$ its two idempotents, as in §*The Two Idempotents of a Root*.

**Addition.** The pair is **complete**: the two idempotents sum to the unit,

$$
\tilde\Pi_+ + \tilde\Pi_-=\tfrac12(e_t+\tilde\Xi)+\tfrac12(e_t-\tilde\Xi)=e_t .
$$

**Subtraction.** The two idempotents differ by the root,

$$
\tilde\Pi_+ - \tilde\Pi_-=\tfrac12(e_t+\tilde\Xi)-\tfrac12(e_t-\tilde\Xi)=\tilde\Xi,
$$

so that the root is read on the pair as $\tilde\Xi=\tilde\Pi_+ - \tilde\Pi_-$, equivalently $\tilde\Xi=2\tilde\Pi_+ - e_t$. Each idempotent is the complement of the other, and replacing the root by $-\tilde\Xi$ interchanges them,

$$
\tilde\Pi_+(-\tilde\Xi)=\tilde\Pi_-(\tilde\Xi),\qquad \tilde\Pi_-(-\tilde\Xi)=\tilde\Pi_+(\tilde\Xi).
$$

**Multiplication.** The pair is **orthogonal**,

$$
\tilde\Pi_+\tilde\Pi_-=\tfrac14(e_t+\tilde\Xi)(e_t-\tilde\Xi)=\tfrac14(e_t-\tilde\Xi^2)=0,
$$

and equally $\tilde\Pi_-\tilde\Pi_+=0$. With the idempotence of the two, the four products are the multiplication table

| $\cdot$ | $\tilde\Pi_+$ | $\tilde\Pi_-$ |
|---|---|---|
| $\tilde\Pi_+$ | $\tilde\Pi_+$ | $0$ |
| $\tilde\Pi_-$ | $0$ | $\tilde\Pi_-$ |

so the $\mathbb{C}$-span $\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\tilde\Pi_-$ is a commutative subalgebra isomorphic to $\mathbb{C}\times\mathbb{C}$, with the componentwise product $(s\tilde\Pi_+ + t\tilde\Pi_-)(s'\tilde\Pi_+ + t'\tilde\Pi_-)=ss'\tilde\Pi_+ + tt'\tilde\Pi_-$, and the root is the element $(+1,-1)$ of that algebra.

Multiplication by the root is diagonal on the pair. On the left,

$$
\tilde\Xi\tilde\Pi_+=\tfrac12(\tilde\Xi+\tilde\Xi^2)=\tfrac12(e_t+\tilde\Xi)=\tilde\Pi_+,\qquad \tilde\Xi\tilde\Pi_-=\tfrac12(\tilde\Xi-\tilde\Xi^2)=-\tfrac12(e_t-\tilde\Xi)=-\tilde\Pi_-,
$$

and on the right $\tilde\Pi_+\tilde\Xi=\tilde\Pi_+$ and $\tilde\Pi_-\tilde\Xi=-\tilde\Pi_-$. Left multiplication by the root therefore acts by $+1$ on the right ideal $\tilde\Pi_+\mathbb{B}$ and by $-1$ on $\tilde\Pi_-\mathbb{B}$, and right multiplication by the root acts by $+1$ on the left ideal $\mathbb{B}\tilde\Pi_+$ and by $-1$ on $\mathbb{B}\tilde\Pi_-$. Since the pair is complete, every element splits on both sides,

$$
\mathbb{B}=\tilde\Pi_+\mathbb{B}\oplus\tilde\Pi_-\mathbb{B},\qquad \mathbb{B}=\mathbb{B}\tilde\Pi_+\oplus\mathbb{B}\tilde\Pi_-,
$$

and these are exactly the eigenspace decompositions of the two multiplications; the operator of left multiplication by the root is an involution, its square being the identity because $\tilde\Xi^2=e_t$.

### The Standard Idempotents of $\mathbb{B}$

**The algebra carries the standard orthogonal idempotents $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)$ and $\tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$, the two idempotents of the root $i\vec e_z$, with $\tilde\Pi_+\tilde\Pi_-=0$ and $\tilde\Pi_+ + \tilde\Pi_-=e_t$; each is primitive, and they generate the two minimal left ideals.**

Put

$$
\tilde\Pi_+=\frac{e_t+i\vec e_z}{2},\qquad \tilde\Pi_-=\frac{e_t-i\vec e_z}{2}.
$$

They are the pair of the root $\tilde\Xi=i\vec e_z$, that is $\tilde\Pi_+=\tilde\Pi_+(i\vec e_z)$ and $\tilde\Pi_-=\tilde\Pi_-(i\vec e_z)$ in the notation of §*The Two Idempotents of a Root*, and $i\vec e_z$ is a root of $+1$, since $(i\vec e_z)^2=i^2\vec e_z^2=(-1)(-1)=e_t$. Hence $\tilde\Pi_+^2=\tilde\Pi_+$ and $\tilde\Pi_-^2=\tilde\Pi_-$ by §*The Two Idempotents of a Root*, and

$$
\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=\frac{e_t-(i\vec e_z)^2}{4}=0,\qquad \tilde\Pi_+ + \tilde\Pi_-=e_t .
$$

So $\tilde\Pi_+$ and $\tilde\Pi_-$ are orthogonal idempotents summing to the unit. They are not central, since $\vec e_x$ anticommutes with $i\vec e_z$ and so does not commute with either. Each is primitive, and these two are the standard idempotents of the algebra.

Left multiplication by $\vec e_z$ and by $\vec e_y$ acts on them as

$$
\vec e_z\tilde\Pi_+=-i\tilde\Pi_+,\qquad \vec e_z\tilde\Pi_-=i\tilde\Pi_-,\qquad \vec e_y\tilde\Pi_+=i\vec e_x\tilde\Pi_+,
$$

the first because $\vec e_z\tilde\Pi_+=(\vec e_z+i\vec e_z^2)/2=(\vec e_z-i)/2=-i\tilde\Pi_+$, and similarly for $\tilde\Pi_-$. The relations reduce the four products $e_\mu\tilde\Pi_+$ to $\tilde\Pi_+$ and $\vec e_x\tilde\Pi_+$, so that $\{\tilde\Pi_+,\vec e_x\tilde\Pi_+\}$ is a $\mathbb{C}$-basis of the minimal left ideal $\mathbb{B}\tilde\Pi_+$. The two ideals, their direct-sum decomposition of $\mathbb{B}$, their bases and their module structure are *Ideals and Peirce Decomposition of the Biquaternion Algebra*.

### The Classification of the Idempotents

**Every idempotent of $\mathbb{B}$ is either trivial ($0$ or $e_t$) or of the form $\tilde\Pi=\tfrac12(e_t+\tilde\Xi)$ with $\tilde\Xi^2=e_t$; there are no others.**

**Theorem.** Every idempotent of $\mathbb{B}$ is either trivial ($0$ or $e_t$) or of the form

$$
\tilde\Pi=\tfrac12 e_t+\tfrac12\tilde\Xi,
$$

where $\tilde\Xi\in\mathbb{B}$ is a root of $+1$, that is $\tilde\Xi^2=e_t$. There are no other idempotents in $\mathbb{B}$.

**Proof.** Write $\tilde\Pi=\Pi_te_t+\vec\Pi$ with $\Pi_t\in\mathbb{C}$ and $\vec\Pi$ pure. Then

$$
\tilde\Pi^2=\bigl(\Pi_t^2-(\vec\Pi,\vec\Pi)\bigr)e_t+2\Pi_t\vec\Pi,
$$

and equating this to $\tilde\Pi=\Pi_te_t+\vec\Pi$ gives the two equations

$$
\Pi_t^2-(\vec\Pi,\vec\Pi)=\Pi_t,\qquad 2\Pi_t\vec\Pi=\vec\Pi .
$$

If $\vec\Pi=0$ then $\Pi_t^2=\Pi_t$, so $\Pi_t=0$ or $\Pi_t=1$, giving the trivial idempotents. If $\vec\Pi\neq0$ then the second equation gives $\Pi_t=1/2$, and substituting into the first gives

$$
(\vec\Pi,\vec\Pi)=-\tfrac14 .
$$

Put $\tilde\Xi=2\vec\Pi$. Then $\tilde\Xi$ is pure and

$$
(\tilde\Xi,\tilde\Xi)=\sum_{k=1}^{3}(2\Pi_k)^2=4(\vec\Pi,\vec\Pi)=-1,
$$

so $\tilde\Xi^2=-(\tilde\Xi,\tilde\Xi)e_t=e_t$: the element $\tilde\Xi$ is a root of $+1$, and $\vec\Pi=\tilde\Xi/2$, whence $\tilde\Pi=\tfrac12 e_t+\tfrac12\tilde\Xi$. The sign choice arises from replacing $\tilde\Xi$ by $-\tilde\Xi$, which is again a root of $+1$.

The trivial idempotents correspond to the trivial roots $\tilde\Xi=\pm e_t$: the two elements $\tfrac12(e_t+\tilde\Xi)$ are then $e_t$ and $0$.

### The Correspondence With the Roots of One

**The halving map $\tilde\Xi\mapsto\tfrac12(e_t+\tilde\Xi)$ is a bijection from the roots of $+1$ onto the idempotents; the pair map $\tilde\Xi\mapsto(\tilde\Pi_+(\tilde\Xi),\tilde\Pi_-(\tilde\Xi))$ is a bijection from the roots of $+1$ onto the ordered complete orthogonal pairs of idempotents; and the class $\{\tilde\Xi,-\tilde\Xi\}$ gives the same unordered pair.**

**Theorem (the halving map).** The map

$$
\tilde\Xi\longmapsto\tilde\Pi_+(\tilde\Xi),\qquad \tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi),
$$

is a **bijection** from the set of roots of $+1$ onto the set of idempotents of $\mathbb{B}$.

**Proof.** *Well defined:* if $\tilde\Xi^2=e_t$, then $\tilde\Pi_+(\tilde\Xi)^2=\tilde\Pi_+(\tilde\Xi)$ by §*The Two Idempotents of a Root*. *Injective:* $\tilde\Pi_+(\tilde\Xi)=\tilde\Pi_+(\tilde\Xi')$ gives $\tilde\Xi=\tilde\Xi'$, since $\tilde\Xi=2\tilde\Pi_+(\tilde\Xi)-e_t$. *Surjective:* the classification theorem says every idempotent is $\tfrac12(e_t+\tilde\Xi)$ or $\tfrac12(e_t-\tilde\Xi)$ for some root $\tilde\Xi$ of $+1$; the first is $\tilde\Pi_+(\tilde\Xi)$, and the second is $\tilde\Pi_-(\tilde\Xi)=\tilde\Pi_+(-\tilde\Xi)$, while $-\tilde\Xi$ is again a root of $+1$.

**Theorem (the pair map).** The map

$$
\tilde\Xi\longmapsto\bigl(\tilde\Pi_+(\tilde\Xi),\tilde\Pi_-(\tilde\Xi)\bigr)
$$

is a **bijection** from the set of roots of $+1$ onto the set of ordered pairs $(\tilde\Pi_+,\tilde\Pi_-)$ of idempotents that are complete and orthogonal, $\tilde\Pi_+ + \tilde\Pi_-=e_t$ and $\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0$.

**Proof.** *Well defined:* the pair of a root is complete and orthogonal by §*The Arithmetic of the Pair of Idempotents*. *Injective:* the root is recovered from the pair, $\tilde\Xi=\tilde\Pi_+ - \tilde\Pi_-$, so two roots with the same pair are equal. *Surjective:* an ordered complete orthogonal pair $(\tilde\Pi_+,\tilde\Pi_-)$ gives the element $\tilde\Xi=\tilde\Pi_+ - \tilde\Pi_-$, and

$$
\tilde\Xi^2=\tilde\Pi_+^2-\tilde\Pi_+\tilde\Pi_- - \tilde\Pi_-\tilde\Pi_+ + \tilde\Pi_-^2=\tilde\Pi_+ + \tilde\Pi_-=e_t,
$$

so $\tilde\Xi$ is a root of $+1$ and the pair is its pair.

Consequently the **complementary pairs** $\{\tilde\Pi,e_t-\tilde\Pi\}$ of idempotents, unordered, are in bijection with the roots of $+1$ modulo the sign identification $\tilde\Xi\sim-\tilde\Xi$, since

$$
\tilde\Pi_-(\tilde\Xi)=\tfrac12(e_t-\tilde\Xi)=e_t-\tilde\Pi_+(\tilde\Xi)=\tilde\Pi_+(-\tilde\Xi).
$$

The inverse of the halving map is $\tilde\Xi=2\tilde\Pi-e_t$, and the root is the difference of its pair, $\tilde\Xi=\tilde\Pi_+ - \tilde\Pi_-$.

### The Families of Idempotents

Substituting the classification of the roots of $+1$ into the halving map gives the families of idempotents.

- For the trivial root $\tilde\Xi=\pm e_t$: $\tilde\Pi=\tfrac12(e_t\pm e_t)$ is $e_t$ or $0$. These are the **trivial idempotents**.
- For the purely imaginary root $\tilde\Xi=\pm i\vec u$: $\tilde\Pi=\tfrac12 e_t\pm\tfrac12 i\vec u$. Since $i\vec u$ is Hermitian for a real unit vector $\vec u$ with $\vec u^2=-e_t$, these are the **Hermitian idempotents**, and they lie in the Hermitian subspace $\mathbb{M}_+$; they are the spectral idempotents of the spectral theorem for a Hermitian element, treated in *Biquaternion Spectral Theory*. A Hermitian idempotent is self-adjoint, orthogonality being read from the Hermitian form of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*.
- For the non-trivial root $\tilde\Xi=\vec\xi+i\vec\xi'$, with $\vec\xi\neq0$ and the two real conditions of §*The Non-Trivial Roots*: $\tilde\Pi=\tfrac12 e_t+\tfrac12(\vec\xi+i\vec\xi')$. Its vector part $\tfrac12(\vec\xi+i\vec\xi')$ carries both a nonzero real part $\vec\xi$ and a nonzero imaginary part $\vec\xi'$, so the idempotent lies in none of the four four-dimensional subspaces $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$.

The idempotents inherit the size of the root set. Since the halving map is a bijection and the trivial roots are isolated, the Hermitian idempotents form a two-real-parameter family and the remaining (non-trivial) idempotents form a four-real-parameter family. Every non-trivial idempotent is a zero divisor, as §*Idempotents and the Non-Pure Zero Divisors* shows, so the non-trivial idempotents lie in the zero-divisor set of *Zero Divisors of the Biquaternion Algebra*, while the trivial idempotents $0$ and $e_t$ are outside it, $e_t$ being a unit.

### Idempotents and Their Projectors

**Every idempotent is the member attached to $+1$ of the pair of a root, and its complement the member attached to $-1$; a Hermitian idempotent is self-adjoint for the Hermitian form of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, and it lies in $\mathbb{M}_+$.**

Every idempotent is the member attached to $+1$ of the pair of a root: for $\tilde\Pi$ idempotent the element $\tilde\Xi=2\tilde\Pi-e_t$ is a root of $+1$, and $\tilde\Pi_+(\tilde\Xi)=\tilde\Pi$ while $\tilde\Pi_-(\tilde\Xi)=e_t-\tilde\Pi$. The **complement** $e_t-\tilde\Pi$ is therefore the member attached to $-1$ of the same pair, an idempotent orthogonal to $\tilde\Pi$ by §*The Arithmetic of the Pair of Idempotents*, and the direct sum decomposition of the underlying $\mathbb{C}$-module,

$$
\mathbb{B}=\tilde\Pi\mathbb{B}\oplus(e_t-\tilde\Pi)\mathbb{B},\qquad \mathbb{B}=\mathbb{B}\tilde\Pi\oplus\mathbb{B}(e_t-\tilde\Pi),
$$

is the one read there at a single root. This is the algebraic content of the statement that idempotents correspond to projectors under multiplication: multiplication by the idempotent is the projector, its complement gives the complementary projector, and the algebra splits into the image of one and the image of the other.

A **Hermitian idempotent**, $\tilde\Pi^{*}=\tilde\Pi$, is **self-adjoint** with respect to the Hermitian form of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, which this article names and does not use; it is the kind occurring in the spectral decomposition of a Hermitian element. Since $\tilde\Pi^{*}=\overline{\tilde\Pi^{\natural}}$, the Hermitian idempotents are the members of the second family of §*The Families of Idempotents*, and they lie in $\mathbb{M}_+$.

### Idempotents and the Non-Pure Zero Divisors

**Every non-trivial idempotent is a zero divisor, and conversely every non-pure zero divisor is the complex multiple $\tilde Q=2Q_t\tilde\Pi$ of a non-trivial idempotent.**

A non-trivial idempotent is a zero divisor, since

$$
\tilde\Pi(e_t-\tilde\Pi)=\tilde\Pi-\tilde\Pi^2=0,
$$

and both factors are nonzero unless $\tilde\Pi$ is $0$ or $e_t$. Conversely, every non-pure zero divisor — every zero divisor with $Q_t\neq0$ — is a complex multiple of a non-trivial idempotent,

$$
\tilde Q=2Q_t\tilde\Pi,\qquad \tilde\Pi=\frac{\tilde Q}{2Q_t}.
$$

The derivation, from the square relation $\tilde Q^2=2Q_t\tilde Q$ that the non-pure family satisfies, together with the structure of the two families of the zero-divisor set and their distribution among the remarkable subspaces, is *Zero Divisors of the Biquaternion Algebra*.

## Summary

The general plain bilinear product of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* is the multiplication of the algebra $\mathbb{B}$ of *Introduction to the Biquaternion Algebra*. The square roots of $+1$ in that product are, by the vector–scalar split and the product formula $\tilde\Xi^2=(\Xi_t^2-(\vec\Xi,\vec\Xi))e_t+2\Xi_t\vec\Xi$:

1. **Trivial roots:** $\tilde\Xi=\pm e_t$.
2. **Purely imaginary roots:** $\tilde\Xi=\pm i\vec u$, where $\vec u$ is a unit real vector with $\vec u^2=-e_t$, a two-real-parameter family.
3. **Non-trivial roots:** $\tilde\Xi=\vec\xi+i\vec\xi'$ with $\vec\xi\neq0$ and the two real conditions $\xi_x^2+\xi_y^2+\xi_z^2-(\xi'_x)^2-(\xi'_y)^2-(\xi'_z)^2=-1$ and $\xi_x\xi'_x+\xi_y\xi'_y+\xi_z\xi'_z=0$, a four-real-parameter family.

All roots except the trivial ones are pure. Every root of $+1$ is a unit, with $\tilde\Xi^{-1}=\tilde\Xi$. The roots of $-1$ are read off the roots of $+1$ by the central imaginary, $\tilde\Xi\mapsto i\tilde\Xi$, a bijection that turns the three families into the two central scalars $\pm i$, the pure real family $\pm\vec u$, and the family $-\vec\xi'+i\vec\xi$; the mechanism needs a central scalar of square $-1$ and is not universal.

The idempotents are the trivial elements $0$ and $e_t$ and the elements $\tilde\Pi=\tfrac12(e_t\pm\tilde\Xi)$ with $\tilde\Xi$ a root of $+1$. Each root carries the two idempotents $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi)$ and $\tilde\Pi_-(\tilde\Xi)=\tfrac12(e_t-\tilde\Xi)=e_t-\tilde\Pi_+(\tilde\Xi)$, a complete orthogonal pair: their sum is $e_t$, their product is $0$, their difference is the root, and multiplication by the root acts by $+1$ on $\tilde\Pi_+$ and $-1$ on $\tilde\Pi_-$, so that the pair splits the algebra into the eigenspaces of that multiplication. The halving map $\tilde\Xi\mapsto\tfrac12(e_t+\tilde\Xi)$ is a bijection from the roots of $+1$ onto the idempotents, with inverse $\tilde\Xi=2\tilde\Pi-e_t$, and the class $\{\tilde\Xi,-\tilde\Xi\}$ gives the complementary pair $\{\tilde\Pi_+,\tilde\Pi_-\}$. The three families of roots give the trivial idempotents, the Hermitian idempotents in $\mathbb{M}_+$ (a two-real-parameter family), and the idempotents lying in none of the four four-dimensional subspaces (a four-real-parameter family). The standard pair $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)$ and $\tilde\Pi_-=\tfrac12(e_t-i\vec e_z)$ is orthogonal, sums to $e_t$, and generates the two minimal left ideals. An idempotent and its complement split the algebra, $\mathbb{B}=\tilde\Pi\mathbb{B}\oplus(e_t-\tilde\Pi)\mathbb{B}$, the algebraic form of a projector and its complementary projector, and every non-pure zero divisor is the complex multiple $2Q_t\tilde\Pi$ of a non-trivial idempotent, developed in *Zero Divisors of the Biquaternion Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\tilde\Xi$ | A root of $+1$, $\tilde\Xi^2=e_t$ |
| $\tilde\Xi=\Xi_te_t+\vec\Xi$, $\vec\Xi=\vec\xi+i\vec\xi'$ | Scalar and vector parts of a root; $\vec\xi,\vec\xi'$ real pure |
| $(\vec Q_1,\vec Q_2)=\sum_kQ_{1k}Q_{2k}$ | General plain bilinear form of two vector parts |
| $\tilde\Pi$ | An idempotent, $\tilde\Pi^2=\tilde\Pi$ |
| $\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_t+\tilde\Xi)$ | The idempotent of the root $\tilde\Xi$ attached to $+1$; $\tilde\Xi\mapsto\tilde\Pi_+(\tilde\Xi)$ is a bijection |
| $\tilde\Pi_-(\tilde\Xi)=\tfrac12(e_t-\tilde\Xi)=e_t-\tilde\Pi_+(\tilde\Xi)$ | The idempotent of the root $\tilde\Xi$ attached to $-1$; the pair is complete and orthogonal, with $\tilde\Pi_+ - \tilde\Pi_-=\tilde\Xi$ |
| $\tilde\Pi_+(i\vec e_z)=\tfrac12(e_t+i\vec e_z)$, $\tilde\Pi_-(i\vec e_z)=\tfrac12(e_t-i\vec e_z)$ | The standard orthogonal idempotents, the pair of the root $i\vec e_z$ |
| $\mathbb{B}\tilde\Pi_+$, $\mathbb{B}\tilde\Pi_-$ | The two minimal left ideals |
| $\mathbb{M}_+$ | Hermitian subspace, containing the Hermitian idempotents |
| $\tilde Q$ | The generic element of a statement that holds for every element |

## Further Reading

- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), for the general definition of a root of a central value, of a square and of an idempotent, with the orthogonal, complete and primitive families, the Hermitian idempotent and the Peirce decomposition.
- [Square Roots of a General Element in the Biquaternion Algebra](square-roots-of-a-general-element-in-the-biquaternion-algebra.html), for the roots of the general quadratic $\tilde\Xi^2=\tilde Q$, of which the roots of $+1$ here are one case.
- [Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html), for the roots of $0$ and the nilpotents, the second central value.
- [Zero Divisors of the Biquaternion Algebra](zero-divisors-of-the-biquaternion-algebra.html), for the two families of the zero-divisor set, of which the non-trivial idempotents are the non-pure one.
- [Ideals and Peirce Decomposition of the Biquaternion Algebra](ideals-and-peirce-decomposition-of-the-biquaternion-algebra.html), for the minimal left ideals the standard idempotents generate and the Peirce decomposition they drive.
- [Comparison Between the Four General Products](comparison-between-the-four-general-products.html), for the roots and the idempotents of the other three general products.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents and minimal left ideals in Clifford algebras.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), for the idempotents of the biquaternion algebra.
