# __Square Roots of Zero and the Nilpotents of the Biquaternion Algebra__

## Introduction

Of the four general products of *The Four General Products and Their Relations*, exactly one makes the underlying complex space of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ an associative unital $\mathbb{C}$-algebra; the algebra is *The Biquaternion Algebra and Its Vector Spaces*, and its multiplication is the general plain bilinear product of two biquaternions, $\tilde Q_1\tilde Q_2$, the product being the one of the algebra. That product is the one read throughout this article.

The article treats two subjects, and in this order. The first is the square roots of the central value $0$, the elements $\tilde\Xi\in\mathbb{B}$ with

$$
\tilde\Xi^2=0 .
$$

The second is the nilpotents of the algebra, the nonzero elements whose square vanishes. The two subjects are one: the roots of $0$ are the element $0$ together with the square-zero elements, and the nonzero square-zero elements are exactly the nilpotents. The roots of $+1$ and the idempotents are the companion article *Square Roots of One and the Idempotents of the Biquaternion Algebra*; the roots of the general quadratic $\tilde\Xi^2=\tilde Q$ are *Square Roots of a General Element in the Biquaternion Algebra*.

**The results.** The roots of $0$ are the origin together with the nilpotent cone, the pure biquaternions whose complex vector part is isotropic, a four-real-parameter family. The nilpotents are exactly the nonzero pure elements with $Q_{1t}=0$ and $Q_{1x}^2+Q_{1y}^2+Q_{1z}^2=0$; they form the nilpotent cone of complex dimension two and real dimension four inside the vector subspace, and lie in no other remarkable subspace. Every nilpotent has index two, so $\tilde Q_1^3=0$ exactly when $\tilde Q_1^2=0$. Each nonzero nilpotent annihilates itself and is a two-sided zero divisor, the pure family of the zero-divisor set; no nilpotent is an idempotent, the two classes meeting only at $0$; and under the $2\times2$ matrix model the nilpotents are the nonzero trace-free singular matrices.

The article is algebraic. The zero-divisor set, its two families and the criterion on the central square are *Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*; the roots of $+1$ and the idempotents are *Square Roots of One and the Idempotents of the Biquaternion Algebra*; the minimal ideals the nilpotents generate are *Ideals and Peirce Decompositions of the Biquaternion Algebra*; and the same class read against the four general products is *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

$$
(\vec Q_1,\vec Q_2)=\sum_{k=1}^{3}Q_{1k}Q_{2k},
$$

and the square of a pure element is $\vec Q^2=-(\vec Q,\vec Q)e_t$. The **central square** is

$$
\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=C(\tilde Q)e_t,\qquad C(\tilde Q)=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^2.
$$

The remarkable subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$ are *Introduction to the Remarkable Subspaces*. A root of a central value is written $\tilde\Xi$ (§*The Root Convention* of *Conventions in Mathematics*), a nilpotent $\tilde\Upsilon$ (§*The Nilpotent Convention*), and a generic element $\tilde Q$.

The equations name a product, so the roots and the nilpotents are relative to it. The general definition of the power, the square, the root of a central value and the nilpotent, with the index of nilpotency and the square-zero element, is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots*. Throughout this article the square is the one of the general plain bilinear product, the multiplication of the algebra; the other three general products carry roots of $0$ and square-zero sets of their own, and they are *The Four General Products and Their Relations*.

## The Roots of Zero

**The roots of $0$ are exactly the origin and the nilpotent cone, the pure biquaternions with $(\vec\Xi,\vec\Xi)=0$, a four-real-parameter family; the nonzero roots are the nilpotents.**

A **root of $0$** is an element $\tilde\Xi\in\mathbb{B}$ with $\tilde\Xi^2=0$, the square being the one of the general plain bilinear product.

### The Reduction

Write the root in scalar and vector parts,

$$
\tilde\Xi=\Xi_te_t+\vec\Xi,\qquad \vec\Xi=\Xi_x\vec e_x+\Xi_y\vec e_y+\Xi_z\vec e_z,\qquad \Xi_k\in\mathbb{C}.
$$

The square of a biquaternion is given by the product formula,

$$
\tilde\Xi^2=\bigl(\Xi_t^2-(\vec\Xi,\vec\Xi)\bigr)e_t+2\Xi_t\vec\Xi,\qquad (\vec\Xi,\vec\Xi)=\Xi_x^2+\Xi_y^2+\Xi_z^2,
$$

so equating $\tilde\Xi^2$ to $0$ splits the equation into a vector part and a scalar part,

$$
2\Xi_t\vec\Xi=0,
$$

$$
\Xi_t^2-(\vec\Xi,\vec\Xi)=0 .
$$

Since $\mathbb{C}$ is a field, the vector equation holds exactly when $\Xi_t=0$ or $\vec\Xi=0$. The roots of $0$ therefore split into two disjoint cases: the root is a complex scalar, $\vec\Xi=0$, or the root is pure, $\Xi_t=0$.

### The Zero Element

In the scalar case $\tilde\Xi=\Xi_te_t$ and the scalar equation reads $\Xi_t^2=0$; since $\mathbb{C}$ is a field, $\Xi_t=0$. The root in this case is the single element

$$
\tilde\Xi=0,
$$

the origin.

### The Null Cone

In the pure case $\tilde\Xi=\vec\Xi$ and the scalar equation reads

$$
(\vec\Xi,\vec\Xi)=\Xi_x^2+\Xi_y^2+\Xi_z^2=0 .
$$

Write the complex coefficients as $\Xi_k=\xi_k+i\xi'_k$ with real $\xi_k,\xi'_k$, so that

$$
\vec\Xi=\vec\xi+i\vec\xi',\qquad \vec\xi=\xi_x\vec e_x+\xi_y\vec e_y+\xi_z\vec e_z,\qquad \vec\xi'=\xi'_x\vec e_x+\xi'_y\vec e_y+\xi'_z\vec e_z .
$$

Then

$$
(\vec\Xi,\vec\Xi)=\sum_{k=1}^{3}(\xi_k+i\xi'_k)^2=\bigl(\xi_x^2+\xi_y^2+\xi_z^2-(\xi'_x)^2-(\xi'_y)^2-(\xi'_z)^2\bigr)+2i\bigl(\xi_x\xi'_x+\xi_y\xi'_y+\xi_z\xi'_z\bigr),
$$

so the single complex equation $(\vec\Xi,\vec\Xi)=0$ is the two real equations

$$
\xi_x^2+\xi_y^2+\xi_z^2-(\xi'_x)^2-(\xi'_y)^2-(\xi'_z)^2=0,\qquad \xi_x\xi'_x+\xi_y\xi'_y+\xi_z\xi'_z=0 .
$$

Six real coefficients carry two constraints, so the roots in this case form a **four-real-parameter family**, the **null cone** of the pure subspace; equivalently its two real vector parts $\vec\xi$ and $\vec\xi'$ are orthogonal and satisfy $\vec\xi\cdot\vec\xi=\vec\xi'\cdot\vec\xi'$. Its nonzero elements are the nilpotents of the algebra.

### Statement of the Theorem

**Theorem.** The roots of $0$ in $\mathbb{B}$ are exactly the following.

**The origin.** The element

$$
\tilde\Xi=0 .
$$

**The null cone.** The pure biquaternions of vanishing complex square, a four-real-parameter family,

$$
\boxed{\;
\tilde\Xi=\Xi_x\vec e_x+\Xi_y\vec e_y+\Xi_z\vec e_z,\qquad \Xi_x^2+\Xi_y^2+\Xi_z^2=0
\;},
$$

that is, writing $\Xi_k=\xi_k+i\xi'_k$, the pair of real equations $\xi_x^2+\xi_y^2+\xi_z^2-(\xi'_x)^2-(\xi'_y)^2-(\xi'_z)^2=0$ and $\xi_x\xi'_x+\xi_y\xi'_y+\xi_z\xi'_z=0$. Its nonzero elements are the nilpotents of the algebra.

### Verification

For a pure $\tilde\Xi$ with $(\vec\Xi,\vec\Xi)=0$ the scalar part of $\tilde\Xi^2$ is $-(\vec\Xi,\vec\Xi)=0$ and the vector part is $2\Xi_t\vec\Xi=0$, since $\Xi_t=0$; so such an element is a root of $0$. The scalar case gives only the origin, and the two cases are exhaustive by the reduction, because the vector equation forces $\Xi_t=0$ or $\vec\Xi=0$.

A worked instance is

$$
\tilde\Xi=\vec e_x+i\vec e_y,\qquad (\vec e_x+i\vec e_y)^2=\vec e_x^2+i^2\vec e_y^2+i(\vec e_x\vec e_y+\vec e_y\vec e_x)=-1+1+0=0 .
$$

### The Roots of Zero and the Nilpotents

The nonzero roots of $0$ are exactly the **nilpotents** of the algebra. This is the criterion of §*The Criterion*: an element has vanishing square exactly when it is pure with isotropic vector part, $Q_{1t}=0$ and $(\vec Q_1,\vec Q_1)=0$, which is the defining equation of the null cone above with the origin removed. The roots of $0$ are therefore the origin together with the nilpotent cone, and the remainder of this article studies that cone.

The nonzero roots of $0$ are **not units**. A root of $0$ other than $0$ is a nilpotent, hence a square-zero element, and a square-zero element is a zero divisor: it annihilates itself, and a unit is never a zero divisor. This is the behaviour opposite to the roots of $+1$, which are units of the algebra; the roots of the three central values and their invertibility are read value by value in *Square Roots of One and the Idempotents of the Biquaternion Algebra* and *Square Roots of a General Element in the Biquaternion Algebra*.

## The Nilpotents

**The nilpotents of the plain algebra are exactly the nonzero pure elements with isotropic vector part, $Q_{1t}=0$ and $Q_{1x}^2+Q_{1y}^2+Q_{1z}^2=0$; they form the nilpotent cone of complex dimension two and real dimension four inside the vector subspace; every nilpotent has index two; and no nilpotent is an idempotent.**

The **nilpotents** of the biquaternion algebra are the nonzero elements whose square vanishes. The class is small and rigid. A nilpotent has vanishing scalar part, so it is a pure biquaternion; its vector part is isotropic for the general plain bilinear form; and those two conditions together are equivalent to the vanishing of the square. Nothing of the kind happens at index three: an element whose cube vanishes already has vanishing square, so the algebra carries no nilpotent of higher index. Each nonzero nilpotent annihilates itself, $\tilde\Upsilon\tilde\Upsilon=0$, and is therefore a zero divisor of a particularly simple kind, its own two-sided annihilating partner. The nilpotents are exactly the pure family of the zero divisors of *Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*, the other family being the complex multiples of the non-trivial idempotents.

### The Definition

**Definition.** A **nilpotent** of the biquaternion algebra is an element $\tilde\Upsilon\in\mathbb{B}$ with vanishing square,

$$
\tilde\Upsilon^2=0 .
$$

The element $0$ is a nilpotent, the trivial one, and the article is concerned with the nonzero ones. A nilpotent is of **index two**: its square vanishes while it does not, and no higher power is needed. The equation names a product, and the notion is relative to it; the general definition, with the index of nilpotency and the square-zero element, is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots*. Throughout this article the product is the general plain bilinear product, the multiplication of the algebra, and where another of the four general products is meant it is named.

The square is the only power that has to be checked. Since $\tilde\Upsilon^3=\tilde\Upsilon\tilde\Upsilon^2=\tilde\Upsilon^2\tilde\Upsilon$, a square-zero element has every higher power zero, and §*Index Two* shows conversely that a vanishing cube already forces a vanishing square. Index two is therefore the only index the algebra carries, and the two clauses of the definition are exhaustive: the nilpotents are exactly the nonzero square-zero elements, with no further stratification.

The star and the natural conjugation preserve nilpotency, since conjugation is multiplicative and carries a vanishing square to a vanishing square,

$$
(\tilde\Upsilon^{*})^2=(\tilde\Upsilon^2)^{*}=0,\qquad (\tilde\Upsilon^{\natural})^2=(\tilde\Upsilon^2)^{\natural}=0 .
$$

The nilpotents are thus a conjugation-stable class, and a statement about one nilpotent is a statement about its two conjugates.

### The Criterion

**An element is a nilpotent exactly when it is pure and its vector part is isotropic, $Q_{1t}=0$ and $(\vec Q_1,\vec Q_1)=0$; every nilpotent is then a zero divisor and its powers stop at the second.**

The square of a general element closes in two terms, one central and one along the vector part, because the vector part is a pure quaternion combination and its own square is central:

$$
\tilde Q^2=\bigl[Q_t^2-(\vec Q,\vec Q)\bigr]e_t+2Q_t\vec Q .
$$

**Theorem (the criterion for a nilpotent).** For $\tilde Q_1\in\mathbb{B}$ the following are equivalent: $\tilde Q_1^2=0$; $\tilde Q_1$ is pure, $Q_{1t}=0$, and its vector part is isotropic, $(\vec Q_1,\vec Q_1)=0$; and $Q_{1t}=0$ and $C(\tilde Q_1)=0$.

**Proof.** The displayed formula expands the square. If $Q_{1t}\neq0$ then the vector part $2Q_{1t}\vec Q_1$ vanishes only for $\vec Q_1=0$, and then the scalar part is $Q_{1t}^2\neq0$; so a nilpotent is pure. For a pure $\tilde Q_1$ the formula reads $\tilde Q_1^2=-(\vec Q_1,\vec Q_1)e_t$, a central element, which vanishes exactly when $(\vec Q_1,\vec Q_1)=0$. Finally, for pure $\tilde Q_1$ the central square is $C(\tilde Q_1)=Q_{1t}^2+(\vec Q_1,\vec Q_1)=(\vec Q_1,\vec Q_1)$, so the two conditions agree.

**Corollary.** Every nilpotent is pure, and every nonzero nilpotent is a zero divisor. Its only nonzero power relation is $\tilde\Upsilon^2=0$, the central zero, so its powers stop at the second.

The criterion separates the class sharply: the nilpotents are the elements of the vector subspace, the kernel of the scalar part, whose vector part is isotropic for the general plain bilinear form. An element with a nonzero scalar part is never nilpotent.

### The Nilpotent Cone

**The nilpotents form the cone $\{Q_{1x}^2+Q_{1y}^2+Q_{1z}^2=0\}$ in the vector subspace, of complex dimension two and real dimension four; its nonzero elements are $r(\vec u_p+i\vec u_{p'})$ with $r>0$ and $\vec u_p,\vec u_{p'}$ orthogonal real unit vectors.**

The set of nilpotents is the vanishing set of the two conditions of the criterion, and it is a cone. The vector part of a nilpotent is a complex vector $\vec Q_1=(Q_{1x},Q_{1y},Q_{1z})$, and its coefficients split into a real and an imaginary part, $Q_{1k}=p_k+ip'_k$ with real $p_k,p'_k$, so that the vector part splits into two real vector parts carrying the central imaginary on the second,

$$
\vec Q_1=\vec p+i\vec p',\qquad \vec p=\sum_{k=1}^{3}p_k\vec e_k,\qquad \vec p'=\sum_{k=1}^{3}p'_k\vec e_k .
$$

The single complex equation $(\vec Q_1,\vec Q_1)=Q_{1x}^2+Q_{1y}^2+Q_{1z}^2=0$ is then the two real equations

$$
\vec p\cdot\vec p=\vec p'\cdot\vec p',\qquad \vec p\cdot\vec p'=0,
$$

that is $\sum_kp_k^2=\sum_k(p'_k)^2$ and $\sum_kp_kp'_k=0$: the two real parts of a nilpotent are orthogonal and have equal sum of squares.

**Proposition (the cone).** The nilpotents form the **nilpotent cone**

$$
\boxed{\;
\{\tilde\Upsilon=Q_{1x}\vec e_x+Q_{1y}\vec e_y+Q_{1z}\vec e_z : Q_{1x}^2+Q_{1y}^2+Q_{1z}^2=0\}
\;},
$$

a complex cone of complex dimension two and real dimension four, a four-real-parameter family. Its nonzero elements are written

$$
\tilde\Upsilon=\vec p+i\vec p',\qquad \vec p\cdot\vec p=\vec p'\cdot\vec p',\qquad \vec p\cdot\vec p'=0,
$$

and equivalently, with $r>0$ and $\vec u_p,\vec u_{p'}$ the two orthogonal real unit directions, so that $r^2=\vec p\cdot\vec p=\vec p'\cdot\vec p'$,

$$
\boxed{\;
\tilde\Upsilon=r(\vec u_p+i\vec u_{p'}),\qquad r>0,\qquad \vec u_p\cdot\vec u_p=\vec u_{p'}\cdot\vec u_{p'}=1,\qquad \vec u_p\cdot\vec u_{p'}=0
\;}.
$$

**Proof.** The first is the criterion. The complex equation cuts a complex-quadric cone in $\mathbb{C}^3$, of complex dimension two; as a real cone it is the two real equations displayed, whose independence away from the origin gives real dimension four. For the parametrisation, the two real equations say that the real part $\vec p$ and the imaginary part $\vec p'$ are orthogonal and have equal sum of squares, which is the stated form; conversely such a pair satisfies both.

The cone is stable under complex scaling, $\tilde\Upsilon\mapsto\lambda\tilde\Upsilon$ for $\lambda\in\mathbb{C}$, because the isotropy condition is homogeneous of degree two; it is stable under the star, which conjugates the two real parts; and the natural conjugation sends $\tilde\Upsilon$ to $-\tilde\Upsilon$. The parameter $r$ is fixed by $r^2=\vec p\cdot\vec p=\vec p'\cdot\vec p'$, and the pair $(\vec u_p,\vec u_{p'})$ is determined up to the simultaneous sign change $(\vec u_p,\vec u_{p'})\mapsto(-\vec u_p,-\vec u_{p'})$.

### Index Two

**Every nilpotent has index two: $\tilde Q_1^3=0$ exactly when $\tilde Q_1^2=0$, and the algebra carries no nilpotent of index three or more.**

**Theorem (no higher index).** For the biquaternion algebra, $\tilde Q_1^3=0$ exactly when $\tilde Q_1^2=0$. Every nilpotent is of index two, and the algebra carries none of index three or more.

**Proof.** The cube follows from the displayed square,

$$
\tilde Q_1^3=\tilde Q_1\,\tilde Q_1^2=Q_{1t}\bigl[Q_{1t}^2-3(\vec Q_1,\vec Q_1)\bigr]e_t+\bigl[3Q_{1t}^2-(\vec Q_1,\vec Q_1)\bigr]\vec Q_1 .
$$

If $\vec Q_1=0$ then $\tilde Q_1=Q_{1t}e_t$ and $\tilde Q_1^3=Q_{1t}^3e_t$, which vanishes only for $Q_{1t}=0$, that is for $\tilde Q_1=0$, and then $\tilde Q_1^2=0$ as well. If $\vec Q_1\neq0$ then the vanishing of the vector part of $\tilde Q_1^3$ forces $(\vec Q_1,\vec Q_1)=3Q_{1t}^2$, and the scalar part is then $Q_{1t}[Q_{1t}^2-3\cdot3Q_{1t}^2]=-8Q_{1t}^3$, which vanishes only for $Q_{1t}=0$, whereupon $(\vec Q_1,\vec Q_1)=0$. In both cases $\tilde Q_1^3=0$ gives $Q_{1t}=0$ and $(\vec Q_1,\vec Q_1)=0$, which is $\tilde Q_1^2=0$. The converse is immediate.

The theorem is the reason the word "nilpotent" needs no index qualifier here. It also fixes the shape of the powers of an element: a nilpotent has the two-term power string $\tilde\Upsilon,\tilde\Upsilon^2=0$ and no longer one, whereas a non-pure zero divisor has the infinite string $\tilde Q^k=2^{k-1}Q_t^{k-1}\tilde Q$ of *Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*.

### The Nilpotents and the Zero Divisors

**Every nonzero nilpotent is a two-sided zero divisor that annihilates itself: the pair $(\tilde\Upsilon,\tilde\Upsilon)$ is a pair of nonzero elements with vanishing product, and the nilpotents are the pure family of the zero-divisor set.**

A nonzero nilpotent is a zero divisor, and in the strongest possible way: it annihilates itself.

**Proposition.** A nonzero nilpotent $\tilde\Upsilon$ satisfies $\tilde\Upsilon\tilde\Upsilon=0$ on both sides, so it lies in its own left annihilator and in its own right annihilator; the pair $(\tilde\Upsilon,\tilde\Upsilon)$ is a pair of nonzero elements with vanishing product, and $\tilde\Upsilon$ is a two-sided zero divisor.

**Proof.** The relation $\tilde\Upsilon^2=0$ is the product of $\tilde\Upsilon$ with itself, on either side, which is exactly the statement.

This is the property that singles the nilpotents out among the zero divisors. A non-pure zero divisor $\tilde Q$ with $Q_t\neq0$ has $\tilde Q^2=2Q_t\tilde Q\neq0$, so it never annihilates itself; it annihilates only the complementary idempotent direction, and its annihilator is a plane transverse to it. A nilpotent, by contrast, is its own annihilating partner: the minimal left ideal it generates is its own annihilator, $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$, whereas for a non-pure zero divisor the ideal generated and the annihilator are distinct and complementary (*Ideals and Peirce Decompositions of the Biquaternion Algebra*).

The nilpotents are one of the two families of the zero-divisor set, and the family split is the vanishing of the scalar part: *Norm Regularity and Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors* calls the elements with $Q_t=0$ the **pure** family and those with $Q_t\neq0$ the **non-pure** family, and the pure family is exactly the nonzero nilpotents. The zero-divisor set of the algebra is the union of the two, a complex cone of complex dimension three and real dimension six, of which the nilpotent cone is the two-dimensional complex part carried by the vector subspace and the non-pure family is the rest.

### The Nilpotents and the Idempotents

**No element is both an idempotent and a nonzero nilpotent; the two classes meet only at $0$.**

The two named element classes of the algebra, nilpotents and idempotents, do not mix.

**Theorem.** No element of $\mathbb{B}$ is both an idempotent and a nonzero nilpotent. The two classes meet only at $0$.

**Proof.** If $\tilde Q^2=\tilde Q$ and $\tilde Q^2=0$ then $\tilde Q=0$.

The disjointness is the two-family statement in another dress. The zero-divisor set splits into the nilpotents, whose square vanishes, and the complex multiples of the non-trivial idempotents, whose square is $2Q_t\tilde Q$ and does not vanish; the non-trivial idempotents themselves are the second family with the scalar part fixed to $\tfrac12$, and they are the elements of the algebra that are simultaneously idempotent and a zero divisor (*Square Roots of One and the Idempotents of the Biquaternion Algebra*). A nilpotent is a zero divisor that is never an idempotent; a non-trivial idempotent is a zero divisor that is never nilpotent; and the trivial idempotents $0$ and $e_t$ are the only idempotents of the algebra that are not zero divisors, $e_t$ being a unit.

### The Conjugations

**The conjugations act on the nilpotent cone as real-linear bijections of the cone onto itself: the natural, the star and the Hermitian conjugation each send a nilpotent to a nilpotent, and the star fixes no nonzero nilpotent, so it pairs the nilpotents two by two.**

The conjugations act on the nilpotent cone in a simple way, and the action is worth recording because the two families of the zero divisors are separated by it.

| conjugation | effect on a nilpotent $\tilde\Upsilon=r(\vec u_p+i\vec u_{p'})$ |
|---|---|
| natural, ${}^{\natural}$ | $-\tilde\Upsilon=-r(\vec u_p+i\vec u_{p'})$, a nilpotent |
| star, ${}^{*}$ | $\overline{\tilde\Upsilon}=r(\vec u_p-i\vec u_{p'})$, a nilpotent |
| Hermitian, ${}^{\natural}\circ{}^{*}={}^{*}\circ{}^{\natural}$ | $-\overline{\tilde\Upsilon}=-r(\vec u_p-i\vec u_{p'})$, a nilpotent |
| reversal | the reversed element and the three above according to the layer |

The star fixes no nonzero nilpotent: a star-fixed element has real coefficients, and a pure real vector $\vec p$ with $\vec p\cdot\vec p=p_1^2+p_2^2+p_3^2=0$ vanishes, since the three squares are non-negative. So the star pairs the nilpotents two by two. The class is a cone, and each conjugation is a real-linear bijection of the cone onto itself.

The real and imaginary parts make the same point. Writing $\tilde\Upsilon=\vec p+i\vec p'$ with $\vec p,\vec p'$ real pure vectors, the nilpotency is the pair of real equations of §*The Nilpotent Cone*: the two real parts of a nilpotent are orthogonal and have equal sum of squares. This is a real condition, and the class is real-algebraically defined even though the algebra is complex.

### The Matrix Model

**Under the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ the nilpotents are exactly the nonzero matrices that are trace-free and singular, equivalently the nonzero rank-one matrices conjugate to the Jordan block $\begin{pmatrix}0&1\\0&0\end{pmatrix}$.**

In the model $\mathbb{B}\cong M_2(\mathbb{C})$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, the criterion becomes the linear algebra of a trace-free singular matrix.

**Theorem.** Under the isomorphism $\mathsf M_2$ with $\mathsf M_2(\tilde Q_1)=Q_{1t}\mathrm I_2-iQ_{1x}\sigma_1-iQ_{1y}\sigma_2-iQ_{1z}\sigma_3$, the following coincide: $\tilde Q_1$ is a nilpotent; $\mathsf M_2(\tilde Q_1)$ is a nonzero nilpotent matrix; and $\mathsf M_2(\tilde Q_1)$ is trace-free, $\operatorname{tr}\mathsf M_2(\tilde Q_1)=2Q_{1t}=0$, and singular, $\det\mathsf M_2(\tilde Q_1)=C(\tilde Q_1)=0$.

**Proof.** The trace is $2Q_{1t}$ and the determinant is $C(\tilde Q_1)$; the criterion is $Q_{1t}=0$ and $C(\tilde Q_1)=0$, which is the stated pair. A nonzero two-by-two complex matrix that is singular and trace-free has only the eigenvalue $0$ and is nilpotent, and conversely a nilpotent matrix is singular and trace-free.

So the nilpotents are the nonzero rank-one trace-free complex matrices, that is the matrices conjugate to the single Jordan block $\begin{pmatrix}0&1\\0&0\end{pmatrix}$, the strictly triangular form. The two standard nilpotents are the off-diagonal Peirce units

$$
\vec\Upsilon_x=\frac{i\vec e_x-\vec e_y}{2},\qquad \vec\Upsilon_y=\frac{i\vec e_x+\vec e_y}{2},
$$

with $\vec\Upsilon_x^2=\vec\Upsilon_y^2=0$, which are exchanged by the star and which, together with the two primitive idempotents $\tilde\Pi_+,\tilde\Pi_-$, form a $\mathbb{C}$-basis of $\mathbb{B}$ with the multiplication table $\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+$ and $\vec\Upsilon_y\vec\Upsilon_x=\tilde\Pi_-$ (*Ideals and Peirce Decompositions of the Biquaternion Algebra*). Every nilpotent is a complex multiple of a conjugate of one of these two, and the cone is the orbit of $\vec\Upsilon_x$ under the group of invertible elements.

### The Nilpotents and the Ideals

**For a nonzero nilpotent the one-sided ideal it generates equals its one-sided annihilator on each side, $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$ and $\tilde\Upsilon\mathbb{B}=J_{\tilde\Upsilon}$; each is a minimal one-sided ideal of real dimension four, and the ideal and the annihilator coincide exactly for the nilpotents.**

The nilpotents are the elements on which the ideal theory of the algebra is simplest, because the ideal they generate and the annihilator they determine coincide.

**Theorem.** Let $\tilde\Upsilon\neq0$ be a nilpotent and let $I_{\tilde\Upsilon}=\{\tilde Q_2:\tilde Q_2\tilde\Upsilon=0\}$ and $J_{\tilde\Upsilon}=\{\tilde Q_2:\tilde\Upsilon\tilde Q_2=0\}$ be its left and right annihilators. Then $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$ and $\tilde\Upsilon\mathbb{B}=J_{\tilde\Upsilon}$; each is a minimal one-sided ideal of real dimension four, and the two coincide exactly for the nilpotents.

**Proof.** If $\tilde\Upsilon^2=0$ then $(\tilde Q_2\tilde\Upsilon)\tilde\Upsilon=\tilde Q_2\tilde\Upsilon^2=0$ for every $\tilde Q_2$, so $\mathbb{B}\tilde\Upsilon\subseteq I_{\tilde\Upsilon}$; both are nonzero proper left ideals and both are minimal of real dimension four, hence equal. The right statement is the mirror image. The converse, that coincidence forces nilpotency, is the statement for the other class in *Introduction to the Remarkable Subspaces*.

The deeper ideal theory, the Peirce decomposition, the minimal left and right ideals $\mathbb{B}\tilde\Pi_+,\mathbb{B}\tilde\Pi_-$ and the module structure of the algebra over itself, is *Ideals and Peirce Decompositions of the Biquaternion Algebra* and *Modules over the Biquaternion Algebra*; the nilpotents enter it as the off-diagonal units $\vec\Upsilon_x,\vec\Upsilon_y$.

### The Nilpotents and the Remarkable Subspaces

**The nilpotent cone lies in the vector subspace and in no other remarkable subspace: the centre, the quaternion subspace, the anti-quaternion subspace, $\mathbb{M}_+$ and $\mathbb{M}_-$ contain no nilpotent.**

Since a nilpotent is pure, its scalar part vanishes, and the vanishing of the scalar part is the defining condition of the vector subspace $\mathrm{Vect}(\mathbb{B})$, the kernel of the scalar part (*Introduction to the Remarkable Subspaces*). The nilpotents therefore lie in $\mathrm{Vect}(\mathbb{B})$ and nowhere else.

| remarkable subspace | nilpotents |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$, the centre | none |
| $\mathbb{H}_{\mathbb{B}}$, the quaternion subspace | none |
| $i\mathbb{H}_{\mathbb{B}}$, the anti-quaternion subspace | none |
| $\mathrm{Vect}(\mathbb{B})$, the vector subspace | the nilpotent cone, of real dimension four |
| $\mathbb{M}_+$, the Hermitian subspace | none |
| $\mathbb{M}_-$, the anti-Hermitian subspace | none |

The entries are forced: the centre, the quaternion subspace and the anti-quaternion subspace consist of units and $0$ and carry no zero divisor; in the two Hermitian subspaces the square of an element is $2a_0\tilde Q$ and the Hermitian part of a nilpotent is $0$, so a Hermitian nilpotent vanishes. The vector subspace is thus the only remarkable subspace with a nonzero nilpotent, and every nonzero nilpotent lies in it. The vector subspace is not a subalgebra, but it is exactly the union of the scalar multiples of the nilpotents together with the origin, as the criterion shows.

## Summary

The general plain bilinear product of *The Four General Products and Their Relations* is the multiplication of the algebra $\mathbb{B}$ of *The Biquaternion Algebra and Its Vector Spaces*. The square roots of $0$ in that product are the origin together with the nilpotent cone, the pure biquaternions $\tilde\Xi=\Xi_x\vec e_x+\Xi_y\vec e_y+\Xi_z\vec e_z$ with $\Xi_x^2+\Xi_y^2+\Xi_z^2=0$, a four-real-parameter family; writing $\Xi_k=\xi_k+i\xi'_k$, the two real equations are $\xi_x^2+\xi_y^2+\xi_z^2-(\xi'_x)^2-(\xi'_y)^2-(\xi'_z)^2=0$ and $\xi_x\xi'_x+\xi_y\xi'_y+\xi_z\xi'_z=0$, and a worked instance is $\vec e_x+i\vec e_y$.

The nonzero roots of $0$ are exactly the nilpotents of the algebra, the nonzero elements of vanishing square. The criterion is $Q_{1t}=0$ and $(\vec Q_1,\vec Q_1)=0$, so every nilpotent is pure and its vector part is isotropic for the general plain bilinear form; the class is the nilpotent cone, a complex cone of complex dimension two and real dimension four, parametrised as $r(\vec u_p+i\vec u_{p'})$ over orthonormal pairs of real unit vectors. The algebra has no nilpotent of index three: $\tilde Q_1^3=0$ exactly when $\tilde Q_1^2=0$, so index two is the only index, and the powers of a nilpotent stop at the second.

Every nonzero nilpotent annihilates itself, so it is a two-sided zero divisor and the ideal it generates is its own annihilator; the nilpotents are the pure family of the zero-divisor set, the non-pure family being the complex multiples of the non-trivial idempotents, and the two classes meet only at $0$. The star preserves the nilpotent set and fixes none of it, the natural conjugation sends $\tilde\Upsilon$ to $-\tilde\Upsilon$, and in the model $M_2(\mathbb{C})$ the nilpotents are the nonzero trace-free singular matrices, the conjugates of the strictly triangular Jordan block, with the two off-diagonal Peirce units as the standard pair. Of the remarkable subspaces only the vector subspace contains one, and it contains all of them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\tilde\Xi$ | A root of $0$, $\tilde\Xi^2=0$ |
| $\tilde\Xi=\Xi_te_t+\vec\Xi$, $\vec\Xi=\vec\xi+i\vec\xi'$ | Scalar and vector parts of a root; $\vec\xi,\vec\xi'$ real pure |
| $(\vec Q_1,\vec Q_2)=\sum_kQ_{1k}Q_{2k}$ | General plain bilinear form of two vector parts |
| $C(\tilde Q_1)=\sum_\mu Q_{1\mu}^2$ | The central square, $\tilde Q_1\tilde Q_1^{\natural}=C(\tilde Q_1)e_t$ |
| $\tilde\Upsilon$ | A nilpotent, $\tilde\Upsilon^2=0$ |
| $\vec\Upsilon_x,\vec\Upsilon_y$ | The two off-diagonal Peirce units $\tfrac{i\vec e_x-\vec e_y}{2}$, $\tfrac{i\vec e_x+\vec e_y}{2}$ |
| $\{\tilde\Upsilon\}$ | The nilpotent cone, $\{Q_{1t}=0,\ (\vec Q_1,\vec Q_1)=0\}$ |
| $\vec p,\vec p'$ | The two real vector parts of a nilpotent, $\tilde\Upsilon=\vec p+i\vec p'$, orthogonal and of equal sum of squares |
| $r(\vec u_p+i\vec u_{p'})$ | The parametrisation of the cone over orthonormal real unit pairs |
| $\tilde Q$ | The generic element of a statement that holds for every element |
| $\tilde Q_1$ | The element of the nilpotent criterion |
| $\tilde Q_2$ | The free element of the annihilator sets |

## Further Reading

- [Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.html), for the general definition of a root of a central value and of the nilpotent, with the index of nilpotency and the square-zero element.
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the roots of $+1$ and the idempotents, the other two central element classes.
- [Square Roots of a General Element in the Biquaternion Algebra](square-roots-of-a-general-element-in-the-biquaternion-algebra.html), for the roots of the general quadratic $\tilde\Xi^2=\tilde Q$, of which the roots of $0$ here are one case.
- [Norm Regularity and Degeneracy in the Biquaternion Algebra](norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the two families of the zero-divisor set, the pure family being exactly these nilpotents.
- [Ideals and Peirce Decompositions of the Biquaternion Algebra](ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), for the off-diagonal units $\vec\Upsilon_x,\vec\Upsilon_y$, the minimal ideals they generate and the Peirce basis.
- [Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions](introduction-to-the-2x2-matrix-element-representation-of-biquaternions.html), for the isomorphism $\mathsf M_2$, the trace and determinant, and the triangular Jordan form.
- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html), for the vector subspace, the nilpotent cone it carries and the absence of a nilpotent in the other five subspaces.
- [Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](zero-divisors-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the same class read against the four general products, where only the plain product has this square-zero set.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), for the algebraic properties of the biquaternions.
