# __Square Roots of One and the Idempotents of the General Plain Algebra__

## Introduction

Of the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, exactly one makes the underlying complex space of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ an associative unital $\mathbb{C}$-algebra; the algebra is *Introduction to the General Plain Algebra of Biquaternions*, and its multiplication is the general plain bilinear product of two biquaternions, $\tilde P\tilde Q$, the product being the one of the algebra. That product is the one read throughout this article.

The article treats two subjects, and in this order. The first is the square roots of the central value $+1$, the elements $\tilde\Xi\in\mathbb{B}$ with

$$
\tilde\Xi^2=e_0 .
$$

The second is the idempotents of the algebra, the elements $\tilde\Pi$ with $\tilde\Pi^2=\tilde\Pi$. The two subjects are one subject, because the **halving map**

$$
\tilde\Xi\longmapsto\tilde\Pi=\tfrac12(e_0+\tilde\Xi),\qquad \tilde\Xi^2=e_0,
$$

is a bijection from the roots of $+1$ onto the idempotents, with inverse $\tilde\Xi=2\tilde\Pi-e_0$. The reason is a two-line computation: if $\tilde\Xi^2=e_0$ then $\tilde\Pi^2=\tfrac14(e_0+2\tilde\Xi+e_0)=\tilde\Pi$, and if $\tilde\Pi^2=\tilde\Pi$ then $(2\tilde\Pi-e_0)^2=4\tilde\Pi^2-4\tilde\Pi+e_0=e_0$. Every idempotent of the algebra is read through that map, on the roots of $+1$ alone, and the families of idempotents are the families of the roots of $+1$ read through it.

**The results.** The roots of $+1$ are the two central scalars $\pm e_0$; the two-real-parameter family $\pm i\boldsymbol\mu$ over the pure real quaternions $\boldsymbol\mu$ with $\boldsymbol\mu^2=-e_0$; and the four-real-parameter family $\boldsymbol\xi+i\boldsymbol\xi'$ with $\boldsymbol\xi\neq0$ and the two real conditions $\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2=-1$ and $\xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3=0$. Every idempotent of the algebra is trivial, $0$ or $e_0$, or of the form $\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$ with $\tilde\Xi$ a root of $+1$; the trivial roots give the trivial idempotents, the family $\pm i\boldsymbol\mu$ gives the Hermitian idempotents, and the non-trivial roots give a four-real-parameter family of idempotents lying in none of the four four-dimensional remarkable subspaces. The map carries the class $\{\tilde\Xi,-\tilde\Xi\}$ to the complementary pair $\{\tilde\Pi,e_0-\tilde\Pi\}$.

The article is algebraic. It does not treat the roots of the general quadratic $\tilde\Xi^2=\tilde Q$, which is *Square Roots of a General Element in the General Plain Algebra*; the roots of $0$ and the nilpotents, which are *Square Roots of Zero and the Nilpotents of the General Plain Algebra*; the structure of the zero-divisor set, which is *Zero Divisors of the General Plain Algebra*; or the ideals the standard idempotents generate, which are *Ideals and Peirce Decomposition of the General Plain Algebra*. The last paragraph of §*The Roots of One* records how the roots of $-1$ are read off the roots of $+1$; it is a remark, it is used nowhere, and it opens nothing.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$, and central scalar imaginary $i$, $i^2=-1$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu=Q_0e_0+\mathbf Q$ with $Q_\mu\in\mathbb{C}$ and $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$. The natural conjugation is $\tilde Q^{\natural}=Q_0-\mathbf Q$ and the star is $\tilde Q^{*}=\overline{Q_0}-\overline{\mathbf Q}$. The general plain bilinear form of two vector parts is

$$
(\mathbf P,\mathbf Q)=\sum_{k=1}^{3}P_kQ_k,
$$

and the square of a pure element is $\mathbf Q^2=-(\mathbf Q,\mathbf Q)e_0$. The remarkable subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$ are *Introduction to the Remarkable Subspaces*. A root of a central value is written $\tilde\Xi$ (§*The Root Convention* of *Conventions in Mathematics*), an idempotent $\tilde\Pi$ (§*The Idempotent Convention*), and a generic element $\tilde P$.

The equations name a product, so the roots and the idempotents are relative to it. The general definition of the power, the square and the root of a central value is *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*, and the general definition of an idempotent, with the orthogonal, complete and primitive families, the projection and the Peirce decomposition, is the same article. Throughout this article the square is the one of the general plain bilinear product, the multiplication of the algebra; the other three general products carry roots and idempotents of their own, and they are *Comparison Between the Four General Products*.

## The Roots of One

**The roots of $+1$ are exactly the two central scalars $\pm e_0$, the two-real-parameter family $\pm i\boldsymbol\mu$ over the pure real quaternions $\boldsymbol\mu$ with $\boldsymbol\mu^2=-e_0$, and the four-real-parameter family $\boldsymbol\xi+i\boldsymbol\xi'$ with $\boldsymbol\xi\neq0$ and the two real conditions; there are no others.**

A **root of $+1$** is an element $\tilde\Xi\in\mathbb{B}$ with $\tilde\Xi^2=e_0$, the square being the one of the general plain bilinear product.

### The Reduction

Write the root in scalar and vector parts,

$$
\tilde\Xi=\Xi_0e_0+\boldsymbol\Xi,\qquad \boldsymbol\Xi=\Xi_1e_1+\Xi_2e_2+\Xi_3e_3,\qquad \Xi_k\in\mathbb{C},
$$

and write the complex coefficients as $\Xi_k=\xi_k+i\xi'_k$ with real $\xi_k,\xi'_k$, so that the vector part splits into two real vector parts,

$$
\boldsymbol\Xi=\boldsymbol\xi+i\boldsymbol\xi',\qquad \boldsymbol\xi=\xi_1e_1+\xi_2e_2+\xi_3e_3,\qquad \boldsymbol\xi'=\xi'_1e_1+\xi'_2e_2+\xi'_3e_3 .
$$

The square of a biquaternion is given by the product formula,

$$
\tilde\Xi^2=\bigl(\Xi_0^2-(\boldsymbol\Xi,\boldsymbol\Xi)\bigr)e_0+2\Xi_0\boldsymbol\Xi,\qquad (\boldsymbol\Xi,\boldsymbol\Xi)=\Xi_1^2+\Xi_2^2+\Xi_3^2,
$$

so equating $\tilde\Xi^2$ to $e_0$ splits the equation into a vector part and a scalar part,

$$
2\Xi_0\boldsymbol\Xi=0,
$$

$$
\Xi_0^2-(\boldsymbol\Xi,\boldsymbol\Xi)=1 .
$$

Since $\mathbb{C}$ is a field, the vector equation holds exactly when $\Xi_0=0$ or $\boldsymbol\Xi=0$. The roots of $+1$ therefore split into two disjoint cases: the root is a complex scalar, $\boldsymbol\Xi=0$, or the root is pure, $\Xi_0=0$.

### The Trivial Roots

In the scalar case $\tilde\Xi=\Xi_0e_0$ and the scalar equation reads $\Xi_0^2=1$, so $\Xi_0=\pm1$. The roots in this case are the two elements

$$
\tilde\Xi=+e_0,\qquad \tilde\Xi=-e_0,
$$

the **trivial roots** of $+1$. They are the only roots of $+1$ in the centre $\mathbb{C}e_0$, and the only ones with non-vanishing scalar part.

### The Purely Imaginary Roots

In the pure case $\tilde\Xi=\boldsymbol\Xi$ and the scalar equation reads

$$
(\boldsymbol\Xi,\boldsymbol\Xi)=\Xi_1^2+\Xi_2^2+\Xi_3^2=-1 .
$$

Take first the case in which the vector part is the central imaginary times a real vector, $\boldsymbol\Xi=i\boldsymbol\mu$ with $\boldsymbol\mu$ a pure real quaternion. Since $i$ is central and $\boldsymbol\mu^2=-\|\boldsymbol\mu\|^2e_0$ with $\|\boldsymbol\mu\|^2=\mu_1^2+\mu_2^2+\mu_3^2$, one has

$$
(i\boldsymbol\mu)^2=i^2\boldsymbol\mu^2=(-1)\bigl(-\|\boldsymbol\mu\|^2e_0\bigr)=\|\boldsymbol\mu\|^2e_0,
$$

so such an element is a root of $+1$ exactly when $\|\boldsymbol\mu\|^2=1$, that is when $\boldsymbol\mu^2=-e_0$. The roots in this case are the elements

$$
\tilde\Xi=+i\boldsymbol\mu,\qquad \tilde\Xi=-i\boldsymbol\mu,\qquad \boldsymbol\mu\ \text{a pure real quaternion with}\ \boldsymbol\mu^2=-e_0,
$$

a **two-real-parameter family**: three real coefficients of $\boldsymbol\mu$ carrying the single condition $\mu_1^2+\mu_2^2+\mu_3^2=1$. Its members are the only roots of $+1$ that are pure multiples of a real quaternion, and each is Hermitian, $(i\boldsymbol\mu)^{*}=i\boldsymbol\mu$.

### The Non-Trivial Roots

Let now the vector part be genuinely complex, $\boldsymbol\Xi=\boldsymbol\xi+i\boldsymbol\xi'$ with $\boldsymbol\xi,\boldsymbol\xi'$ real pure. Then

$$
(\boldsymbol\Xi,\boldsymbol\Xi)=\sum_{k=1}^{3}(\xi_k+i\xi'_k)^2=\bigl(\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2\bigr)+2i\bigl(\xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3\bigr),
$$

so the single complex equation $(\boldsymbol\Xi,\boldsymbol\Xi)=-1$ is the two real equations

$$
\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2=-1,\qquad \xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3=0 .
$$

The case $\boldsymbol\xi=0$ requires $(\xi'_1)^2+(\xi'_2)^2+(\xi'_3)^2=1$ and is the two-parameter family of the previous paragraph. The remaining case is $\boldsymbol\xi\neq0$: six real coefficients carrying the two constraints, hence a four-real-parameter family. Its elements are the **non-trivial roots** of $+1$,

$$
\tilde\Xi=\boldsymbol\xi+i\boldsymbol\xi',\qquad \boldsymbol\xi\neq0,
$$

$$
\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2=-1,\qquad \xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3=0,
$$

equivalently $\boldsymbol\xi\boldsymbol\xi'+\boldsymbol\xi'\boldsymbol\xi=0$. For such a root the imaginary part is automatically nonzero: if $\boldsymbol\xi'=0$ the first equation would give $\xi_1^2+\xi_2^2+\xi_3^2=-1$, impossible, the three squares being non-negative.

### Statement of the Theorem

**Theorem.** The roots of $+1$ in $\mathbb{B}$ are exactly the elements of the three following families.

**The trivial roots.** The two central elements

$$
\tilde\Xi=+e_0,\qquad \tilde\Xi=-e_0 .
$$

**The purely imaginary roots.** The two-real-parameter family

$$
\tilde\Xi=+i\boldsymbol\mu,\qquad \tilde\Xi=-i\boldsymbol\mu,\qquad \boldsymbol\mu=\mu_1e_1+\mu_2e_2+\mu_3e_3,\ \mu_k\in\mathbb{R},\ \mu_1^2+\mu_2^2+\mu_3^2=1,
$$

equivalently over the pure real quaternions with $\boldsymbol\mu^2=-e_0$; since $i$ is central the family is also written $\tilde\Xi=\pm\boldsymbol\mu i$.

**The non-trivial roots.** The four-real-parameter family

$$
\tilde\Xi=\boldsymbol\xi+i\boldsymbol\xi'=\bigl(\xi_1e_1+\xi_2e_2+\xi_3e_3\bigr)+i\bigl(\xi'_1e_1+\xi'_2e_2+\xi'_3e_3\bigr),\qquad \boldsymbol\xi\neq0,
$$

whose six real coefficients satisfy the two conditions

$$
\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2=-1,\qquad \xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3=0,
$$

equivalently $\boldsymbol\xi\boldsymbol\xi'+\boldsymbol\xi'\boldsymbol\xi=0$.

The three families are disjoint, and together they are all the roots.

### Verification

Each family consists of roots of $+1$.

**Trivial roots.** $(\pm e_0)^2=e_0$.

**Purely imaginary roots.** For $\boldsymbol\mu^2=-e_0$, $(i\boldsymbol\mu)^2=i^2\boldsymbol\mu^2=(-1)(-e_0)=e_0$.

**Non-trivial roots.** Expanding,

$$
\tilde\Xi^2=(\boldsymbol\xi+i\boldsymbol\xi')^2=\boldsymbol\xi^2-(\boldsymbol\xi')^2+i\bigl(\boldsymbol\xi\boldsymbol\xi'+\boldsymbol\xi'\boldsymbol\xi\bigr).
$$

Now $\boldsymbol\xi^2=-\bigl(\xi_1^2+\xi_2^2+\xi_3^2\bigr)e_0$, $(\boldsymbol\xi')^2=-\bigl((\xi'_1)^2+(\xi'_2)^2+(\xi'_3)^2\bigr)e_0$, and the mixed term is a central multiple,

$$
\boldsymbol\xi\boldsymbol\xi'+\boldsymbol\xi'\boldsymbol\xi=-2\bigl(\xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3\bigr)e_0=0,
$$

by the second condition. Hence

$$
\tilde\Xi^2=-\bigl(\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2\bigr)e_0=-(-1)e_0=e_0,
$$

by the first condition.

### Status of the Roots

Counting the free real parameters: the trivial roots are two isolated elements, the purely imaginary roots are a two-real-parameter family, and the non-trivial roots are a four-real-parameter family.

Every root except the trivial ones is pure, hence lies in the six-real-dimensional vector subspace of pure biquaternions; the trivial roots lie in the centre. A root of $+1$ is a **unit**: $\tilde\Xi^2=e_0$ reads $\tilde\Xi\tilde\Xi=e_0$, so $\tilde\Xi$ is invertible with inverse

$$
\tilde\Xi^{-1}=\tilde\Xi,
$$

and a unit is not a zero divisor. The single element common to the roots of $+1$ and the idempotents is $e_0$: an element that is both a root of $+1$ and an idempotent satisfies $\tilde\Xi^2=e_0$ and $\tilde\Xi^2=\tilde\Xi$, hence $\tilde\Xi=e_0$.

**The roots of minus one.** For this product the central imaginary turns the roots of $+1$ into the roots of $-1$: if $\tilde\Xi^2=e_0$ then $(i\tilde\Xi)^2=i^2\tilde\Xi^2=-e_0$, because $i$ is central, and since $i$ is invertible the map $\tilde\Xi\mapsto i\tilde\Xi$ is a bijection from the roots of $+1$ onto the roots of $-1$. The three families above are carried to the three families of the roots of $-1$: the two central scalars $\pm i$; the family $\pm\boldsymbol\mu$ over the pure real quaternions with $\boldsymbol\mu^2=-e_0$; and the family $-\boldsymbol\xi'+i\boldsymbol\xi$ with the same two real conditions. The mechanism is not universal. It needs a central scalar of square $-1$ that can be moved past the two slots of the product; in a sesquilinear product, where the second slot conjugates, scalar multiplication cannot flip the sign this way, and the roots of $-1$ are then read from the roots of $+1$ by no such map, or are absent altogether. The roots of $-1$ are quoted here and are used nowhere in this article.

## The Idempotents

**Every idempotent of $\mathbb{B}$ is trivial, $0$ or $e_0$, or of the form $\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$ with $\tilde\Xi$ a root of $+1$; the halving map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ is a bijection from the roots of $+1$ onto the idempotents; and the non-trivial idempotents form a four-real-parameter family.**

The **idempotents** of $\mathbb{B}$ are the elements satisfying $\tilde\Pi^2=\tilde\Pi$, the square being the one of the general plain bilinear product. They are the algebraic form of a projection, and in $\mathbb{B}$ they do four separate jobs at once: they give the direct sum decompositions of the algebra into left ideals, and in particular the two minimal left ideals; they classify the non-pure zero divisors, every one of which is a complex multiple of an idempotent; they are in bijection with the roots of $+1$ through the halving map, so their classification is the classification of those roots; and they drive the Peirce decomposition of the algebra. The definition and the families are the general ones of *Definitions for the Study of the 12 Algebraic Structures*, read here in the general plain bilinear product.

### The Definition

**Definition.** An element $\tilde\Pi$ of $\mathbb{B}$ is an **idempotent of the general plain algebra** when

$$
\tilde\Pi^2=\tilde\Pi .
$$

The element $0$ is an idempotent, and so is the unit $e_0$; the two are the **trivial idempotents**. The equation names a product, and the notion is relative to it: throughout this article the product is the general plain bilinear product, the multiplication of the algebra, and another product is named where it is meant. The idempotents of the other three general products are not these, and the four sets are tabulated in *Comparison Between the Four General Products*.

Idempotents encode direct summands of the algebra: an idempotent $\tilde\Pi$ and its complement $e_0-\tilde\Pi$ split the underlying $\mathbb{C}$-module,

$$
\mathbb{B}=\mathbb{B}\tilde\Pi\oplus\mathbb{B}(e_0-\tilde\Pi),\qquad \mathbb{B}=\tilde\Pi\mathbb{B}\oplus(e_0-\tilde\Pi)\mathbb{B},
$$

and every such decomposition arises from an idempotent. A **primitive** idempotent, one that is not a sum of two nonzero orthogonal idempotents, generates a minimal left ideal. The general statements, with the orthogonal, complete and primitive families, the projection and the Peirce decomposition, are *Definitions for the Study of the 12 Algebraic Structures*.

### The Standard Idempotents of $\mathbb{B}$

**The algebra carries the standard orthogonal idempotents $\tilde\Pi_1=\tfrac12(e_0+ie_3)$ and $\tilde\Pi_2=\tfrac12(e_0-ie_3)$, with $\tilde\Pi_1\tilde\Pi_2=0$ and $\tilde\Pi_1+\tilde\Pi_2=e_0$; each is primitive, and they generate the two minimal left ideals.**

Put

$$
\tilde\Pi_1=\frac{e_0+ie_3}{2},\qquad \tilde\Pi_2=\frac{e_0-ie_3}{2}.
$$

Both are of the form $\tfrac12(e_0+\tilde\Xi)$ with $\tilde\Xi=\pm ie_3$, and $ie_3$ is a root of $+1$, since $(ie_3)^2=i^2e_3^2=(-1)(-1)=e_0$. Hence $\tilde\Pi_1^2=\tilde\Pi_1$ and $\tilde\Pi_2^2=\tilde\Pi_2$ by the halving map, and

$$
\tilde\Pi_1\tilde\Pi_2=\tilde\Pi_2\tilde\Pi_1=\frac{e_0-(ie_3)^2}{4}=0,\qquad \tilde\Pi_1+\tilde\Pi_2=e_0 .
$$

So $\tilde\Pi_1$ and $\tilde\Pi_2$ are orthogonal idempotents summing to the unit. They are not central, since $e_1$ anticommutes with $ie_3$ and so does not commute with either. Each is primitive, and these two are the standard idempotents of the algebra.

Left multiplication by $e_3$ and by $e_2$ acts on them as

$$
e_3\tilde\Pi_1=-i\tilde\Pi_1,\qquad e_3\tilde\Pi_2=i\tilde\Pi_2,\qquad e_2\tilde\Pi_1=ie_1\tilde\Pi_1,
$$

the first because $e_3\tilde\Pi_1=(e_3+ie_3^2)/2=(e_3-i)/2=-i\tilde\Pi_1$, and similarly for $\tilde\Pi_2$. The relations reduce the four products $e_\mu\tilde\Pi_1$ to $\tilde\Pi_1$ and $e_1\tilde\Pi_1$, so that $\{\tilde\Pi_1,e_1\tilde\Pi_1\}$ is a $\mathbb{C}$-basis of the minimal left ideal $\mathbb{B}\tilde\Pi_1$. The two ideals, their direct-sum decomposition of $\mathbb{B}$, their bases and their module structure are *Ideals and Peirce Decomposition of the General Plain Algebra*.

### The Classification of the Idempotents

**Every idempotent of $\mathbb{B}$ is either trivial ($0$ or $e_0$) or of the form $\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$ with $\tilde\Xi^2=e_0$; there are no others.**

**Theorem.** Every idempotent of $\mathbb{B}$ is either trivial ($0$ or $e_0$) or of the form

$$
\tilde\Pi=\tfrac12 e_0+\tfrac12\tilde\Xi,
$$

where $\tilde\Xi\in\mathbb{B}$ is a root of $+1$, that is $\tilde\Xi^2=e_0$. There are no other idempotents in $\mathbb{B}$.

**Proof.** Write $\tilde\Pi=\Pi_0e_0+\boldsymbol\Pi$ with $\Pi_0\in\mathbb{C}$ and $\boldsymbol\Pi$ pure. Then

$$
\tilde\Pi^2=\bigl(\Pi_0^2-(\boldsymbol\Pi,\boldsymbol\Pi)\bigr)e_0+2\Pi_0\boldsymbol\Pi,
$$

and equating this to $\tilde\Pi=\Pi_0e_0+\boldsymbol\Pi$ gives the two equations

$$
\Pi_0^2-(\boldsymbol\Pi,\boldsymbol\Pi)=\Pi_0,\qquad 2\Pi_0\boldsymbol\Pi=\boldsymbol\Pi .
$$

If $\boldsymbol\Pi=0$ then $\Pi_0^2=\Pi_0$, so $\Pi_0=0$ or $\Pi_0=1$, giving the trivial idempotents. If $\boldsymbol\Pi\neq0$ then the second equation gives $\Pi_0=1/2$, and substituting into the first gives

$$
(\boldsymbol\Pi,\boldsymbol\Pi)=-\tfrac14 .
$$

Put $\tilde\Xi=2\boldsymbol\Pi$. Then $\tilde\Xi$ is pure and

$$
(\tilde\Xi,\tilde\Xi)=\sum_{k=1}^{3}(2\Pi_k)^2=4(\boldsymbol\Pi,\boldsymbol\Pi)=-1,
$$

so $\tilde\Xi^2=-(\tilde\Xi,\tilde\Xi)e_0=e_0$: the element $\tilde\Xi$ is a root of $+1$, and $\boldsymbol\Pi=\tilde\Xi/2$, whence $\tilde\Pi=\tfrac12 e_0+\tfrac12\tilde\Xi$. The sign choice arises from replacing $\tilde\Xi$ by $-\tilde\Xi$, which is again a root of $+1$.

The trivial idempotents correspond to the trivial roots $\tilde\Xi=\pm e_0$: the two elements $\tfrac12(e_0+\tilde\Xi)$ are then $e_0$ and $0$.

### The Halving Map and the Bijection With the Roots of One

**The map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ is a bijection from the roots of $+1$ onto the idempotents, carrying the class $\{\tilde\Xi,-\tilde\Xi\}$ to the complementary pair $\{\tilde\Pi,e_0-\tilde\Pi\}$.**

**Theorem.** The map

$$
\tilde\Xi\longmapsto\tilde\Pi(\tilde\Xi),\qquad \tilde\Pi(\tilde\Xi)=\tfrac12(e_0+\tilde\Xi),
$$

is a **bijection** from the set of roots of $+1$ onto the set of idempotents of $\mathbb{B}$.

**Proof.** *Well defined:* if $\tilde\Xi^2=e_0$, then

$$
\tilde\Pi(\tilde\Xi)^2=\tfrac14(e_0+\tilde\Xi)^2=\tfrac14(e_0+2\tilde\Xi+\tilde\Xi^2)=\tfrac14(2e_0+2\tilde\Xi)=\tfrac12(e_0+\tilde\Xi)=\tilde\Pi(\tilde\Xi).
$$

*Injective:* $\tilde\Pi(\tilde\Xi)=\tilde\Pi(\tilde\Xi')$ gives $\tilde\Xi=\tilde\Xi'$. *Surjective:* the classification theorem says every idempotent is $\tfrac12(e_0\pm\tilde\Xi)$ for some root $\tilde\Xi$ of $+1$, and $\tfrac12(e_0-\tilde\Xi)=\tilde\Pi(-\tilde\Xi)$, while $-\tilde\Xi$ is again a root of $+1$.

Consequently the **complementary pairs** $\{\tilde\Pi,e_0-\tilde\Pi\}$ of idempotents are in bijection with the roots of $+1$ modulo the sign identification $\tilde\Xi\sim-\tilde\Xi$, since

$$
\tilde\Pi(-\tilde\Xi)=\tfrac12(e_0-\tilde\Xi)=e_0-\tilde\Pi(\tilde\Xi).
$$

The inverse of the halving map is $\tilde\Xi=2\tilde\Pi-e_0$.

### The Families of Idempotents

Substituting the classification of the roots of $+1$ into the halving map gives the families of idempotents.

- For the trivial root $\tilde\Xi=\pm e_0$: $\tilde\Pi=\tfrac12(e_0\pm e_0)$ is $e_0$ or $0$. These are the **trivial idempotents**.
- For the purely imaginary root $\tilde\Xi=\pm i\boldsymbol\mu$: $\tilde\Pi=\tfrac12 e_0\pm\tfrac12 i\boldsymbol\mu$. Since $i\boldsymbol\mu$ is Hermitian for a pure real quaternion $\boldsymbol\mu$ with $\boldsymbol\mu^2=-e_0$, these are the **Hermitian idempotents**, and they lie in the Hermitian subspace $\mathbb{M}_+$; they are the projections of the spectral theorem for a Hermitian element, treated in *Biquaternion Spectral Theory*. A Hermitian idempotent is an orthogonal projection, orthogonality being read from the Hermitian form of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*.
- For the non-trivial root $\tilde\Xi=\boldsymbol\xi+i\boldsymbol\xi'$, with $\boldsymbol\xi\neq0$ and the two real conditions of §*The Non-Trivial Roots*: $\tilde\Pi=\tfrac12 e_0+\tfrac12(\boldsymbol\xi+i\boldsymbol\xi')$. Its vector part $\tfrac12(\boldsymbol\xi+i\boldsymbol\xi')$ carries both a nonzero real part $\boldsymbol\xi$ and a nonzero imaginary part $\boldsymbol\xi'$, so the idempotent lies in none of the four four-dimensional subspaces $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$.

The idempotents inherit the size of the root set. Since the halving map is a bijection and the trivial roots are isolated, the Hermitian idempotents form a two-real-parameter family and the remaining (non-trivial) idempotents form a four-real-parameter family. Every non-trivial idempotent is a zero divisor, as §*Idempotents and the Non-Pure Zero Divisors* shows, so the non-trivial idempotents lie in the zero-divisor set of *Zero Divisors of the General Plain Algebra*, while the trivial idempotents $0$ and $e_0$ are outside it, $e_0$ being a unit.

### Idempotents as Projections

**An idempotent and its complement split the algebra, $\mathbb{B}=\tilde\Pi\mathbb{B}\oplus(e_0-\tilde\Pi)\mathbb{B}$, and equally on the other side; a Hermitian idempotent is an orthogonal projection, and it lies in $\mathbb{M}_+$.**

An idempotent $\tilde\Pi$ satisfies $\tilde\Pi^2=\tilde\Pi$, so its **complement** $e_0-\tilde\Pi$ is again an idempotent and

$$
\tilde\Pi(e_0-\tilde\Pi)=\tilde\Pi-\tilde\Pi^2=0 .
$$

The pair $\{\tilde\Pi,e_0-\tilde\Pi\}$ therefore gives a direct sum decomposition of the underlying $\mathbb{C}$-module,

$$
\mathbb{B}=\tilde\Pi\mathbb{B}\oplus(e_0-\tilde\Pi)\mathbb{B},
$$

and equally $\mathbb{B}=\mathbb{B}\tilde\Pi\oplus\mathbb{B}(e_0-\tilde\Pi)$ on the other side. This is the algebraic content of the statement that idempotents correspond to projections: the idempotent is the projection, its complement is the complementary projection, and the algebra splits into the image of one and the image of the other.

A **Hermitian idempotent**, $\tilde\Pi^{*}=\tilde\Pi$, is an **orthogonal** projection with respect to the Hermitian form of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*, which this article names and does not use; it is the kind occurring in the spectral decomposition of a Hermitian element. Since $\tilde\Pi^{*}=\overline{\tilde\Pi^{\natural}}$, the Hermitian idempotents are the members of the second family of §*The Families of Idempotents*, and they lie in $\mathbb{M}_+$.

### Idempotents and the Non-Pure Zero Divisors

**Every non-trivial idempotent is a zero divisor, and conversely every non-pure zero divisor is the complex multiple $\tilde Q=2Q_0\tilde\Pi$ of a non-trivial idempotent.**

A non-trivial idempotent is a zero divisor, since

$$
\tilde\Pi(e_0-\tilde\Pi)=\tilde\Pi-\tilde\Pi^2=0,
$$

and both factors are nonzero unless $\tilde\Pi$ is $0$ or $e_0$. Conversely, every non-pure zero divisor — every zero divisor with $Q_0\neq0$ — is a complex multiple of a non-trivial idempotent,

$$
\tilde Q=2Q_0\tilde\Pi,\qquad \tilde\Pi=\frac{\tilde Q}{2Q_0}.
$$

The derivation, from the square relation $\tilde Q^2=2Q_0\tilde Q$ that the non-pure family satisfies, together with the structure of the two families of the zero-divisor set and their distribution among the remarkable subspaces, is *Zero Divisors of the General Plain Algebra*.

## Summary

The general plain bilinear product of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* is the multiplication of the algebra $\mathbb{B}$ of *Introduction to the General Plain Algebra of Biquaternions*. The square roots of $+1$ in that product are, by the vector–scalar split and the product formula $\tilde\Xi^2=(\Xi_0^2-(\boldsymbol\Xi,\boldsymbol\Xi))e_0+2\Xi_0\boldsymbol\Xi$:

1. **Trivial roots:** $\tilde\Xi=\pm e_0$.
2. **Purely imaginary roots:** $\tilde\Xi=\pm i\boldsymbol\mu$, where $\boldsymbol\mu$ is a pure real quaternion with $\boldsymbol\mu^2=-e_0$, a two-real-parameter family.
3. **Non-trivial roots:** $\tilde\Xi=\boldsymbol\xi+i\boldsymbol\xi'$ with $\boldsymbol\xi\neq0$ and the two real conditions $\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2=-1$ and $\xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3=0$, a four-real-parameter family.

All roots except the trivial ones are pure. Every root of $+1$ is a unit, with $\tilde\Xi^{-1}=\tilde\Xi$. The roots of $-1$ are read off the roots of $+1$ by the central imaginary, $\tilde\Xi\mapsto i\tilde\Xi$, a bijection that turns the three families into the two central scalars $\pm i$, the pure real family $\pm\boldsymbol\mu$, and the family $-\boldsymbol\xi'+i\boldsymbol\xi$; the mechanism needs a central scalar of square $-1$ and is not universal.

The idempotents are the trivial elements $0$ and $e_0$ and the elements $\tilde\Pi=\tfrac12(e_0\pm\tilde\Xi)$ with $\tilde\Xi$ a root of $+1$; the halving map $\tilde\Xi\mapsto\tfrac12(e_0+\tilde\Xi)$ is a bijection from the roots of $+1$ onto the idempotents, with inverse $\tilde\Xi=2\tilde\Pi-e_0$, and it carries the class $\{\tilde\Xi,-\tilde\Xi\}$ to the complementary pair $\{\tilde\Pi,e_0-\tilde\Pi\}$. The three families of roots give the trivial idempotents, the Hermitian idempotents in $\mathbb{M}_+$ (a two-real-parameter family), and the idempotents lying in none of the four four-dimensional subspaces (a four-real-parameter family). The standard pair $\tilde\Pi_1=\tfrac12(e_0+ie_3)$ and $\tilde\Pi_2=\tfrac12(e_0-ie_3)$ is orthogonal, sums to $e_0$, and generates the two minimal left ideals. An idempotent and its complement split the algebra, $\mathbb{B}=\tilde\Pi\mathbb{B}\oplus(e_0-\tilde\Pi)\mathbb{B}$, the algebraic form of a projection and its complementary projection, and every non-pure zero divisor is the complex multiple $2Q_0\tilde\Pi$ of a non-trivial idempotent, developed in *Zero Divisors of the General Plain Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_1e_2=e_3$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\tilde\Xi$ | A root of $+1$, $\tilde\Xi^2=e_0$ |
| $\tilde\Xi=\Xi_0e_0+\boldsymbol\Xi$, $\boldsymbol\Xi=\boldsymbol\xi+i\boldsymbol\xi'$ | Scalar and vector parts of a root; $\boldsymbol\xi,\boldsymbol\xi'$ real pure |
| $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$ | General plain bilinear form of two vector parts |
| $\tilde\Pi$ | An idempotent, $\tilde\Pi^2=\tilde\Pi$ |
| $\tilde\Pi(\tilde\Xi)=\tfrac12(e_0+\tilde\Xi)$ | The idempotent of the root $\tilde\Xi$; $\tilde\Xi\mapsto\tilde\Pi(\tilde\Xi)$ is a bijection |
| $\tilde\Pi_1=\tfrac12(e_0+ie_3)$, $\tilde\Pi_2=\tfrac12(e_0-ie_3)$ | The standard orthogonal idempotents, $\tilde\Pi_1+\tilde\Pi_2=e_0$ |
| $\mathbb{B}\tilde\Pi_1$, $\mathbb{B}\tilde\Pi_2$ | The two minimal left ideals |
| $\mathbb{M}_+$ | Hermitian subspace, containing the Hermitian idempotents |
| $\tilde P$ | The generic element of a statement that holds for every element |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the general definition of a root of a central value, of a square and of an idempotent, with the orthogonal, complete and primitive families, the projection and the Peirce decomposition.
- *Square Roots of a General Element in the General Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-algebra.md`), for the roots of the general quadratic $\tilde\Xi^2=\tilde Q$, of which the roots of $+1$ here are one case.
- *Square Roots of Zero and the Nilpotents of the General Plain Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-plain-algebra.md`), for the roots of $0$ and the nilpotents, the second central value.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the two families of the zero-divisor set, of which the non-trivial idempotents are the non-pure one.
- *Ideals and Peirce Decomposition of the General Plain Algebra* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra.md`), for the minimal left ideals the standard idempotents generate and the Peirce decomposition they drive.
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the roots and the idempotents of the other three general products.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for idempotents and minimal left ideals in Clifford algebras.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), for the idempotents of the biquaternion algebra.
