# __Square Roots of Zero and the Nilpotents of the General Plain Algebra__

## Introduction

Of the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, exactly one makes the underlying complex space of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ an associative unital $\mathbb{C}$-algebra; the algebra is *Introduction to the General Plain Algebra of Biquaternions*, and its multiplication is the general plain bilinear product of two biquaternions, $\tilde P\tilde Q$, the product being the one of the algebra. That product is the one read throughout this article.

The article treats two subjects, and in this order. The first is the square roots of the central value $0$, the elements $\tilde\Xi\in\mathbb{B}$ with

$$
\tilde\Xi^2=0 .
$$

The second is the nilpotents of the algebra, the nonzero elements whose square vanishes. The two subjects are one: the roots of $0$ are the element $0$ together with the square-zero elements, and the nonzero square-zero elements are exactly the nilpotents. The roots of $+1$ and the idempotents are the companion article *Square Roots of One and the Idempotents of the General Plain Algebra*; the roots of the general quadratic $\tilde\Xi^2=\tilde Q$ are *Square Roots of a General Element in the General Plain Algebra*.

**The results.** The roots of $0$ are the origin together with the nilpotent cone, the pure biquaternions whose complex vector part is isotropic, a four-real-parameter family. The nilpotents are exactly the nonzero pure elements with $P_0=0$ and $P_1^2+P_2^2+P_3^2=0$; they form the nilpotent cone of complex dimension two and real dimension four inside the vector subspace, and lie in no other remarkable subspace. Every nilpotent has index two, so $\tilde P^3=0$ exactly when $\tilde P^2=0$. Each nonzero nilpotent annihilates itself and is a two-sided zero divisor, the pure family of the zero-divisor set; no nilpotent is an idempotent, the two classes meeting only at $0$; and under the $2\times2$ matrix model the nilpotents are the nonzero trace-free singular matrices.

The article is algebraic. The zero-divisor set, its two families and the criterion on the central square are *Zero Divisors of the General Plain Algebra*; the roots of $+1$ and the idempotents are *Square Roots of One and the Idempotents of the General Plain Algebra*; the minimal ideals the nilpotents generate are *Ideals and Peirce Decomposition of the General Plain Algebra*; and the same class read against the four general products is *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$, and central scalar imaginary $i$, $i^2=-1$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu=Q_0e_0+\mathbf Q$ with $Q_\mu\in\mathbb{C}$ and $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$. The natural conjugation is $\tilde Q^{\natural}=Q_0-\mathbf Q$ and the star is $\tilde Q^{*}=\overline{Q_0}-\overline{\mathbf Q}$. The general plain bilinear form of two vector parts is

$$
(\mathbf P,\mathbf Q)=\sum_{k=1}^{3}P_kQ_k,
$$

and the square of a pure element is $\mathbf Q^2=-(\mathbf Q,\mathbf Q)e_0$. The **central square** is

$$
\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=C(\tilde Q)e_0,\qquad C(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^2 .
$$

The remarkable subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$ are *Introduction to the Remarkable Subspaces*. A root of a central value is written $\tilde\Xi$ (§*The Root Convention* of *Conventions in Mathematics*), a nilpotent $\tilde\Upsilon$ (§*The Nilpotent Convention*), and a generic element $\tilde P$ or $\tilde Q$.

The equations name a product, so the roots and the nilpotents are relative to it. The general definition of the power, the square, the root of a central value and the nilpotent, with the index of nilpotency and the square-zero element, is *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*. Throughout this article the square is the one of the general plain bilinear product, the multiplication of the algebra; the other three general products carry roots of $0$ and square-zero sets of their own, and they are *Comparison Between the Four General Products*.

## The Roots of Zero

**The roots of $0$ are exactly the origin and the nilpotent cone, the pure biquaternions with $(\boldsymbol\Xi,\boldsymbol\Xi)=0$, a four-real-parameter family; the nonzero roots are the nilpotents.**

A **root of $0$** is an element $\tilde\Xi\in\mathbb{B}$ with $\tilde\Xi^2=0$, the square being the one of the general plain bilinear product.

### The Reduction

Write the root in scalar and vector parts,

$$
\tilde\Xi=\Xi_0e_0+\boldsymbol\Xi,\qquad \boldsymbol\Xi=\Xi_1e_1+\Xi_2e_2+\Xi_3e_3,\qquad \Xi_k\in\mathbb{C}.
$$

The square of a biquaternion is given by the product formula,

$$
\tilde\Xi^2=\bigl(\Xi_0^2-(\boldsymbol\Xi,\boldsymbol\Xi)\bigr)e_0+2\Xi_0\boldsymbol\Xi,\qquad (\boldsymbol\Xi,\boldsymbol\Xi)=\Xi_1^2+\Xi_2^2+\Xi_3^2,
$$

so equating $\tilde\Xi^2$ to $0$ splits the equation into a vector part and a scalar part,

$$
2\Xi_0\boldsymbol\Xi=0,
$$

$$
\Xi_0^2-(\boldsymbol\Xi,\boldsymbol\Xi)=0 .
$$

Since $\mathbb{C}$ is a field, the vector equation holds exactly when $\Xi_0=0$ or $\boldsymbol\Xi=0$. The roots of $0$ therefore split into two disjoint cases: the root is a complex scalar, $\boldsymbol\Xi=0$, or the root is pure, $\Xi_0=0$.

### The Zero Element

In the scalar case $\tilde\Xi=\Xi_0e_0$ and the scalar equation reads $\Xi_0^2=0$; since $\mathbb{C}$ is a field, $\Xi_0=0$. The root in this case is the single element

$$
\tilde\Xi=0,
$$

the origin.

### The Null Cone

In the pure case $\tilde\Xi=\boldsymbol\Xi$ and the scalar equation reads

$$
(\boldsymbol\Xi,\boldsymbol\Xi)=\Xi_1^2+\Xi_2^2+\Xi_3^2=0 .
$$

Write the complex coefficients as $\Xi_k=\xi_k+i\xi'_k$ with real $\xi_k,\xi'_k$, so that

$$
\boldsymbol\Xi=\boldsymbol\xi+i\boldsymbol\xi',\qquad \boldsymbol\xi=\xi_1e_1+\xi_2e_2+\xi_3e_3,\qquad \boldsymbol\xi'=\xi'_1e_1+\xi'_2e_2+\xi'_3e_3 .
$$

Then

$$
(\boldsymbol\Xi,\boldsymbol\Xi)=\sum_{k=1}^{3}(\xi_k+i\xi'_k)^2=\bigl(\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2\bigr)+2i\bigl(\xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3\bigr),
$$

so the single complex equation $(\boldsymbol\Xi,\boldsymbol\Xi)=0$ is the two real equations

$$
\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2=0,\qquad \xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3=0 .
$$

Six real coefficients carry two constraints, so the roots in this case form a **four-real-parameter family**, the **null cone** of the pure subspace; equivalently its two real vector parts $\boldsymbol\xi$ and $\boldsymbol\xi'$ are orthogonal and satisfy $\boldsymbol\xi\cdot\boldsymbol\xi=\boldsymbol\xi'\cdot\boldsymbol\xi'$. Its nonzero elements are the nilpotents of the algebra.

### Statement of the Theorem

**Theorem.** The roots of $0$ in $\mathbb{B}$ are exactly the following.

**The origin.** The element

$$
\tilde\Xi=0 .
$$

**The null cone.** The pure biquaternions of vanishing complex square, a four-real-parameter family,

$$
\tilde\Xi=\Xi_1e_1+\Xi_2e_2+\Xi_3e_3,\qquad \Xi_1^2+\Xi_2^2+\Xi_3^2=0,
$$

that is, writing $\Xi_k=\xi_k+i\xi'_k$, the pair of real equations $\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2=0$ and $\xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3=0$. Its nonzero elements are the nilpotents of the algebra.

### Verification

For a pure $\tilde\Xi$ with $(\boldsymbol\Xi,\boldsymbol\Xi)=0$ the scalar part of $\tilde\Xi^2$ is $-(\boldsymbol\Xi,\boldsymbol\Xi)=0$ and the vector part is $2\Xi_0\boldsymbol\Xi=0$, since $\Xi_0=0$; so such an element is a root of $0$. The scalar case gives only the origin, and the two cases are exhaustive by the reduction, because the vector equation forces $\Xi_0=0$ or $\boldsymbol\Xi=0$.

A worked instance is

$$
\tilde\Xi=e_1+ie_2,\qquad (e_1+ie_2)^2=e_1^2+i^2e_2^2+i(e_1e_2+e_2e_1)=-1+1+0=0 .
$$

### The Roots of Zero and the Nilpotents

The nonzero roots of $0$ are exactly the **nilpotents** of the algebra. This is the criterion of §*The Criterion*: an element has vanishing square exactly when it is pure with isotropic vector part, $P_0=0$ and $(\mathbf P,\mathbf P)=0$, which is the defining equation of the null cone above with the origin removed. The roots of $0$ are therefore the origin together with the nilpotent cone, and the remainder of this article studies that cone.

The nonzero roots of $0$ are **not units**. A root of $0$ other than $0$ is a nilpotent, hence a square-zero element, and a square-zero element is a zero divisor: it annihilates itself, and a unit is never a zero divisor. This is the behaviour opposite to the roots of $+1$, which are units of the algebra; the roots of the three central values and their invertibility are read value by value in *Square Roots of One and the Idempotents of the General Plain Algebra* and *Square Roots of a General Element in the General Plain Algebra*.

## The Nilpotents

**The nilpotents of the plain algebra are exactly the nonzero pure elements with isotropic vector part, $P_0=0$ and $P_1^2+P_2^2+P_3^2=0$; they form the nilpotent cone of complex dimension two and real dimension four inside the vector subspace; every nilpotent has index two; and no nilpotent is an idempotent.**

The **nilpotents** of the general plain algebra are the nonzero elements whose square vanishes. The class is small and rigid. A nilpotent has vanishing scalar part, so it is a pure biquaternion; its vector part is isotropic for the general plain bilinear form; and those two conditions together are equivalent to the vanishing of the square. Nothing of the kind happens at index three: an element whose cube vanishes already has vanishing square, so the algebra carries no nilpotent of higher index. Each nonzero nilpotent annihilates itself, $\tilde\Upsilon\tilde\Upsilon=0$, and is therefore a zero divisor of a particularly simple kind, its own two-sided annihilating partner. The nilpotents are exactly the pure family of the zero divisors of *Zero Divisors of the General Plain Algebra*, the other family being the complex multiples of the non-trivial idempotents.

### The Definition

**Definition.** A **nilpotent** of the general plain algebra is an element $\tilde\Upsilon\in\mathbb{B}$ with vanishing square,

$$
\tilde\Upsilon^2=0 .
$$

The element $0$ is a nilpotent, the trivial one, and the article is concerned with the nonzero ones. A nilpotent is of **index two**: its square vanishes while it does not, and no higher power is needed. The equation names a product, and the notion is relative to it; the general definition, with the index of nilpotency and the square-zero element, is *Definitions for the Study of the 12 Algebraic Structures*, §*Powers, the Square and the Roots*. Throughout this article the product is the general plain bilinear product, the multiplication of the algebra, and where another of the four general products is meant it is named.

The square is the only power that has to be checked. Since $\tilde\Upsilon^3=\tilde\Upsilon\tilde\Upsilon^2=\tilde\Upsilon^2\tilde\Upsilon$, a square-zero element has every higher power zero, and §*Index Two* shows conversely that a vanishing cube already forces a vanishing square. Index two is therefore the only index the algebra carries, and the two clauses of the definition are exhaustive: the nilpotents are exactly the nonzero square-zero elements, with no further stratification.

The star and the natural conjugation preserve nilpotency, since conjugation is multiplicative and carries a vanishing square to a vanishing square,

$$
(\tilde\Upsilon^{*})^2=(\tilde\Upsilon^2)^{*}=0,\qquad (\tilde\Upsilon^{\natural})^2=(\tilde\Upsilon^2)^{\natural}=0 .
$$

The nilpotents are thus a conjugation-stable class, and a statement about one nilpotent is a statement about its two conjugates.

### The Criterion

**An element is a nilpotent exactly when it is pure and its vector part is isotropic, $P_0=0$ and $(\mathbf P,\mathbf P)=0$; every nilpotent is then a zero divisor and its powers stop at the second.**

The square of a general element closes in two terms, one central and one along the vector part, because the vector part is a pure quaternion combination and its own square is central:

$$
\tilde Q^2=\bigl[Q_0^2-(\mathbf Q,\mathbf Q)\bigr]e_0+2Q_0\mathbf Q .
$$

**Theorem (the criterion for a nilpotent).** For $\tilde P\in\mathbb{B}$ the following are equivalent: $\tilde P^2=0$; $\tilde P$ is pure, $P_0=0$, and its vector part is isotropic, $(\mathbf P,\mathbf P)=0$; and $P_0=0$ and $C(\tilde P)=0$.

**Proof.** The displayed formula expands the square. If $P_0\neq0$ then the vector part $2P_0\mathbf P$ vanishes only for $\mathbf P=0$, and then the scalar part is $P_0^2\neq0$; so a nilpotent is pure. For a pure $\tilde P$ the formula reads $\tilde P^2=-(\mathbf P,\mathbf P)e_0$, a central element, which vanishes exactly when $(\mathbf P,\mathbf P)=0$. Finally, for pure $\tilde P$ the central square is $C(\tilde P)=P_0^2+(\mathbf P,\mathbf P)=(\mathbf P,\mathbf P)$, so the two conditions agree.

**Corollary.** Every nilpotent is pure, and every nonzero nilpotent is a zero divisor. Its only nonzero power relation is $\tilde\Upsilon^2=0$, the central zero, so its powers stop at the second.

The criterion separates the class sharply: the nilpotents are the elements of the vector subspace, the kernel of the scalar part, whose vector part is isotropic for the general plain bilinear form. An element with a nonzero scalar part is never nilpotent.

### The Nilpotent Cone

**The nilpotents form the cone $\{P_1^2+P_2^2+P_3^2=0\}$ in the vector subspace, of complex dimension two and real dimension four; its nonzero elements are $r(\hat{\mathbf p}+i\hat{\mathbf p}')$ with $r>0$ and $\hat{\mathbf p},\hat{\mathbf p}'$ orthogonal real unit vectors.**

The set of nilpotents is the vanishing set of the two conditions of the criterion, and it is a cone. The vector part of a nilpotent is a complex vector $\mathbf P=(P_1,P_2,P_3)$, and its coefficients split into a real and an imaginary part, $P_k=p_k+ip'_k$ with real $p_k,p'_k$, so that the vector part splits into two real vector parts carrying the central imaginary on the second,

$$
\mathbf P=\mathbf p+i\mathbf p',\qquad \mathbf p=\sum_{k=1}^{3}p_ke_k,\qquad \mathbf p'=\sum_{k=1}^{3}p'_ke_k .
$$

The single complex equation $(\mathbf P,\mathbf P)=P_1^2+P_2^2+P_3^2=0$ is then the two real equations

$$
\mathbf p\cdot\mathbf p=\mathbf p'\cdot\mathbf p',\qquad \mathbf p\cdot\mathbf p'=0,
$$

that is $\sum_kp_k^2=\sum_k(p'_k)^2$ and $\sum_kp_kp'_k=0$: the two real parts of a nilpotent are orthogonal and have equal sum of squares.

**Proposition (the cone).** The nilpotents form the **nilpotent cone**

$$
\{\tilde\Upsilon=P_1e_1+P_2e_2+P_3e_3 : P_1^2+P_2^2+P_3^2=0\},
$$

a complex cone of complex dimension two and real dimension four, a four-real-parameter family. Its nonzero elements are written

$$
\tilde\Upsilon=\mathbf p+i\mathbf p',\qquad \mathbf p\cdot\mathbf p=\mathbf p'\cdot\mathbf p',\qquad \mathbf p\cdot\mathbf p'=0,
$$

and equivalently, with $r>0$ and $\hat{\mathbf p},\hat{\mathbf p}'$ the two orthogonal real unit directions, so that $r^2=\mathbf p\cdot\mathbf p=\mathbf p'\cdot\mathbf p'$,

$$
\tilde\Upsilon=r(\hat{\mathbf p}+i\hat{\mathbf p}'),\qquad r>0,\qquad \hat{\mathbf p}\cdot\hat{\mathbf p}=\hat{\mathbf p}'\cdot\hat{\mathbf p}'=1,\qquad \hat{\mathbf p}\cdot\hat{\mathbf p}'=0 .
$$

**Proof.** The first is the criterion. The complex equation cuts a complex-quadric cone in $\mathbb{C}^3$, of complex dimension two; as a real cone it is the two real equations displayed, whose independence away from the origin gives real dimension four. For the parametrisation, the two real equations say that the real part $\mathbf p$ and the imaginary part $\mathbf p'$ are orthogonal and have equal sum of squares, which is the stated form; conversely such a pair satisfies both.

The cone is stable under complex scaling, $\tilde\Upsilon\mapsto\lambda\tilde\Upsilon$ for $\lambda\in\mathbb{C}$, because the isotropy condition is homogeneous of degree two; it is stable under the star, which conjugates the two real parts; and the natural conjugation sends $\tilde\Upsilon$ to $-\tilde\Upsilon$. The parameter $r$ is fixed by $r^2=\mathbf p\cdot\mathbf p=\mathbf p'\cdot\mathbf p'$, and the pair $(\hat{\mathbf p},\hat{\mathbf p}')$ is determined up to the simultaneous sign change $(\hat{\mathbf p},\hat{\mathbf p}')\mapsto(-\hat{\mathbf p},-\hat{\mathbf p}')$.

### Index Two

**Every nilpotent has index two: $\tilde P^3=0$ exactly when $\tilde P^2=0$, and the algebra carries no nilpotent of index three or more.**

**Theorem (no higher index).** For the general plain algebra, $\tilde P^3=0$ exactly when $\tilde P^2=0$. Every nilpotent is of index two, and the algebra carries none of index three or more.

**Proof.** The cube follows from the displayed square,

$$
\tilde P^3=\tilde P\,\tilde P^2=P_0\bigl[P_0^2-3(\mathbf P,\mathbf P)\bigr]e_0+\bigl[3P_0^2-(\mathbf P,\mathbf P)\bigr]\mathbf P .
$$

If $\mathbf P=0$ then $\tilde P=P_0e_0$ and $\tilde P^3=P_0^3e_0$, which vanishes only for $P_0=0$, that is for $\tilde P=0$, and then $\tilde P^2=0$ as well. If $\mathbf P\neq0$ then the vanishing of the vector part of $\tilde P^3$ forces $(\mathbf P,\mathbf P)=3P_0^2$, and the scalar part is then $P_0[P_0^2-3\cdot3P_0^2]=-8P_0^3$, which vanishes only for $P_0=0$, whereupon $(\mathbf P,\mathbf P)=0$. In both cases $\tilde P^3=0$ gives $P_0=0$ and $(\mathbf P,\mathbf P)=0$, which is $\tilde P^2=0$. The converse is immediate.

The theorem is the reason the word "nilpotent" needs no index qualifier here. It also fixes the shape of the powers of an element: a nilpotent has the two-term power string $\tilde\Upsilon,\tilde\Upsilon^2=0$ and no longer one, whereas a non-pure zero divisor has the infinite string $\tilde P^k=2^{k-1}P_0^{k-1}\tilde P$ of *Zero Divisors of the General Plain Algebra*.

### The Nilpotents and the Zero Divisors

**Every nonzero nilpotent is a two-sided zero divisor that annihilates itself: the pair $(\tilde\Upsilon,\tilde\Upsilon)$ is a pair of nonzero elements with vanishing product, and the nilpotents are the pure family of the zero-divisor set.**

A nonzero nilpotent is a zero divisor, and in the strongest possible way: it annihilates itself.

**Proposition.** A nonzero nilpotent $\tilde\Upsilon$ satisfies $\tilde\Upsilon\tilde\Upsilon=0$ on both sides, so it lies in its own left annihilator and in its own right annihilator; the pair $(\tilde\Upsilon,\tilde\Upsilon)$ is a pair of nonzero elements with vanishing product, and $\tilde\Upsilon$ is a two-sided zero divisor.

**Proof.** The relation $\tilde\Upsilon^2=0$ is the product of $\tilde\Upsilon$ with itself, on either side, which is exactly the statement.

This is the property that singles the nilpotents out among the zero divisors. A non-pure zero divisor $\tilde P$ with $P_0\neq0$ has $\tilde P^2=2P_0\tilde P\neq0$, so it never annihilates itself; it annihilates only the complementary idempotent direction, and its annihilator is a plane transverse to it. A nilpotent, by contrast, is its own annihilating partner: the minimal left ideal it generates is its own annihilator, $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$, whereas for a non-pure zero divisor the ideal generated and the annihilator are distinct and complementary (*Ideals and Peirce Decomposition of the General Plain Algebra*).

The nilpotents are one of the two families of the zero-divisor set, and the family split is the vanishing of the scalar part: *Zero Divisors of the General Plain Algebra* calls the elements with $P_0=0$ the **pure** family and those with $P_0\neq0$ the **non-pure** family, and the pure family is exactly the nonzero nilpotents. The zero-divisor set of the algebra is the union of the two, a complex cone of complex dimension three and real dimension six, of which the nilpotent cone is the two-dimensional complex part carried by the vector subspace and the non-pure family is the rest.

### The Nilpotents and the Idempotents

**No element is both an idempotent and a nonzero nilpotent; the two classes meet only at $0$.**

The two named element classes of the algebra, nilpotents and idempotents, do not mix.

**Theorem.** No element of $\mathbb{B}$ is both an idempotent and a nonzero nilpotent. The two classes meet only at $0$.

**Proof.** If $\tilde X^2=\tilde X$ and $\tilde X^2=0$ then $\tilde X=0$.

The disjointness is the two-family statement in another dress. The zero-divisor set splits into the nilpotents, whose square vanishes, and the complex multiples of the non-trivial idempotents, whose square is $2P_0\tilde P$ and does not vanish; the non-trivial idempotents themselves are the second family with the scalar part fixed to $\tfrac12$, and they are the elements of the algebra that are simultaneously idempotent and a zero divisor (*Square Roots of One and the Idempotents of the General Plain Algebra*). A nilpotent is a zero divisor that is never an idempotent; a non-trivial idempotent is a zero divisor that is never nilpotent; and the trivial idempotents $0$ and $e_0$ are the only idempotents of the algebra that are not zero divisors, $e_0$ being a unit.

### The Conjugations

**The conjugations act on the nilpotent cone as real-linear bijections of the cone onto itself: the natural, the star and the Hermitian conjugation each send a nilpotent to a nilpotent, and the star fixes no nonzero nilpotent, so it pairs the nilpotents two by two.**

The conjugations act on the nilpotent cone in a simple way, and the action is worth recording because the two families of the zero divisors are separated by it.

| conjugation | effect on a nilpotent $\tilde\Upsilon=r(\hat{\mathbf p}+i\hat{\mathbf p}')$ |
|---|---|
| natural, ${}^{\natural}$ | $-\tilde\Upsilon=-r(\hat{\mathbf p}+i\hat{\mathbf p}')$, a nilpotent |
| star, ${}^{*}$ | $\overline{\tilde\Upsilon}=r(\hat{\mathbf p}-i\hat{\mathbf p}')$, a nilpotent |
| Hermitian, ${}^{\natural}\circ{}^{*}={}^{*}\circ{}^{\natural}$ | $-\overline{\tilde\Upsilon}=-r(\hat{\mathbf p}-i\hat{\mathbf p}')$, a nilpotent |
| reversal | the reversed element and the three above according to the layer |

The star fixes no nonzero nilpotent: a star-fixed element has real coefficients, and a pure real vector $\mathbf p$ with $\mathbf p\cdot\mathbf p=p_1^2+p_2^2+p_3^2=0$ vanishes, since the three squares are non-negative. So the star pairs the nilpotents two by two. The class is a cone, and each conjugation is a real-linear bijection of the cone onto itself.

The real and imaginary parts make the same point. Writing $\tilde\Upsilon=\mathbf p+i\mathbf p'$ with $\mathbf p,\mathbf p'$ real pure vectors, the nilpotency is the pair of real equations of §*The Nilpotent Cone*: the two real parts of a nilpotent are orthogonal and have equal sum of squares. This is a real condition, and the class is real-algebraically defined even though the algebra is complex.

### The Matrix Model

**Under the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ the nilpotents are exactly the nonzero matrices that are trace-free and singular, equivalently the nonzero rank-one matrices conjugate to the Jordan block $\begin{pmatrix}0&1\\0&0\end{pmatrix}$.**

In the model $\mathbb{B}\cong M_2(\mathbb{C})$ of *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, the criterion becomes the linear algebra of a trace-free singular matrix.

**Theorem.** Under the isomorphism $\mathsf M_2$ with $\mathsf M_2(\tilde P)=P_0\mathrm I_2-iP_1\sigma_1-iP_2\sigma_2-iP_3\sigma_3$, the following coincide: $\tilde P$ is a nilpotent; $\mathsf M_2(\tilde P)$ is a nonzero nilpotent matrix; and $\mathsf M_2(\tilde P)$ is trace-free, $\operatorname{tr}\mathsf M_2(\tilde P)=2P_0=0$, and singular, $\det\mathsf M_2(\tilde P)=C(\tilde P)=0$.

**Proof.** The trace is $2P_0$ and the determinant is $C(\tilde P)$; the criterion is $P_0=0$ and $C(\tilde P)=0$, which is the stated pair. A nonzero two-by-two complex matrix that is singular and trace-free has only the eigenvalue $0$ and is nilpotent, and conversely a nilpotent matrix is singular and trace-free.

So the nilpotents are the nonzero rank-one trace-free complex matrices, that is the matrices conjugate to the single Jordan block $\begin{pmatrix}0&1\\0&0\end{pmatrix}$, the strictly triangular form. The two standard nilpotents are the off-diagonal Peirce units

$$
\tilde\Upsilon_1=\frac{ie_1-e_2}{2},\qquad \tilde\Upsilon_2=\frac{ie_1+e_2}{2},
$$

with $\tilde\Upsilon_1^2=\tilde\Upsilon_2^2=0$, which are exchanged by the star and which, together with the two primitive idempotents $\tilde\Pi_1,\tilde\Pi_2$, form a $\mathbb{C}$-basis of $\mathbb{B}$ with the multiplication table $\tilde\Upsilon_1\tilde\Upsilon_2=\tilde\Pi_1$ and $\tilde\Upsilon_2\tilde\Upsilon_1=\tilde\Pi_2$ (*Ideals and Peirce Decomposition of the General Plain Algebra*). Every nilpotent is a complex multiple of a conjugate of one of these two, and the cone is the orbit of $\tilde\Upsilon_1$ under the group of invertible elements.

### The Nilpotents and the Ideals

**For a nonzero nilpotent the one-sided ideal it generates equals its one-sided annihilator on each side, $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$ and $\tilde\Upsilon\mathbb{B}=J_{\tilde\Upsilon}$; each is a minimal one-sided ideal of real dimension four, and the ideal and the annihilator coincide exactly for the nilpotents.**

The nilpotents are the elements on which the ideal theory of the algebra is simplest, because the ideal they generate and the annihilator they determine coincide.

**Theorem.** Let $\tilde\Upsilon\neq0$ be a nilpotent and let $I_{\tilde\Upsilon}=\{\tilde X:\tilde X\tilde\Upsilon=0\}$ and $J_{\tilde\Upsilon}=\{\tilde X:\tilde\Upsilon\tilde X=0\}$ be its left and right annihilators. Then $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$ and $\tilde\Upsilon\mathbb{B}=J_{\tilde\Upsilon}$; each is a minimal one-sided ideal of real dimension four, and the two coincide exactly for the nilpotents.

**Proof.** If $\tilde\Upsilon^2=0$ then $(\tilde X\tilde\Upsilon)\tilde\Upsilon=\tilde X\tilde\Upsilon^2=0$ for every $\tilde X$, so $\mathbb{B}\tilde\Upsilon\subseteq I_{\tilde\Upsilon}$; both are nonzero proper left ideals and both are minimal of real dimension four, hence equal. The right statement is the mirror image. The converse, that coincidence forces nilpotency, is the statement for the other class in *Introduction to the Remarkable Subspaces*.

The deeper ideal theory, the Peirce decomposition, the minimal left and right ideals $\mathbb{B}\tilde\Pi_1,\mathbb{B}\tilde\Pi_2$ and the module structure of the algebra over itself, is *Ideals and Peirce Decomposition of the General Plain Algebra* and *Modules over the General Plain Algebra of Biquaternions*; the nilpotents enter it as the off-diagonal units $\tilde\Upsilon_1,\tilde\Upsilon_2$.

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

The general plain bilinear product of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* is the multiplication of the algebra $\mathbb{B}$ of *Introduction to the General Plain Algebra of Biquaternions*. The square roots of $0$ in that product are the origin together with the nilpotent cone, the pure biquaternions $\tilde\Xi=\Xi_1e_1+\Xi_2e_2+\Xi_3e_3$ with $\Xi_1^2+\Xi_2^2+\Xi_3^2=0$, a four-real-parameter family; writing $\Xi_k=\xi_k+i\xi'_k$, the two real equations are $\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2=0$ and $\xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3=0$, and a worked instance is $e_1+ie_2$.

The nonzero roots of $0$ are exactly the nilpotents of the algebra, the nonzero elements of vanishing square. The criterion is $P_0=0$ and $(\mathbf P,\mathbf P)=0$, so every nilpotent is pure and its vector part is isotropic for the general plain bilinear form; the class is the nilpotent cone, a complex cone of complex dimension two and real dimension four, parametrised as $r(\hat{\mathbf p}+i\hat{\mathbf p}')$ over orthonormal pairs of real unit vectors. The algebra has no nilpotent of index three: $\tilde P^3=0$ exactly when $\tilde P^2=0$, so index two is the only index, and the powers of a nilpotent stop at the second.

Every nonzero nilpotent annihilates itself, so it is a two-sided zero divisor and the ideal it generates is its own annihilator; the nilpotents are the pure family of the zero-divisor set, the non-pure family being the complex multiples of the non-trivial idempotents, and the two classes meet only at $0$. The star preserves the nilpotent set and fixes none of it, the natural conjugation sends $\tilde\Upsilon$ to $-\tilde\Upsilon$, and in the model $M_2(\mathbb{C})$ the nilpotents are the nonzero trace-free singular matrices, the conjugates of the strictly triangular Jordan block, with the two off-diagonal Peirce units as the standard pair. Of the remarkable subspaces only the vector subspace contains one, and it contains all of them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_1e_2=e_3$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\tilde\Xi$ | A root of $0$, $\tilde\Xi^2=0$ |
| $\tilde\Xi=\Xi_0e_0+\boldsymbol\Xi$, $\boldsymbol\Xi=\boldsymbol\xi+i\boldsymbol\xi'$ | Scalar and vector parts of a root; $\boldsymbol\xi,\boldsymbol\xi'$ real pure |
| $(\mathbf P,\mathbf Q)=\sum_kP_kQ_k$ | General plain bilinear form of two vector parts |
| $C(\tilde P)=\sum_\mu P_\mu^2$ | The central square, $\tilde P\tilde P^{\natural}=C(\tilde P)e_0$ |
| $\tilde\Upsilon$ | A nilpotent, $\tilde\Upsilon^2=0$ |
| $\tilde\Upsilon_1,\tilde\Upsilon_2$ | The two off-diagonal Peirce units $\tfrac{ie_1-e_2}{2}$, $\tfrac{ie_1+e_2}{2}$ |
| $\{\tilde\Upsilon\}$ | The nilpotent cone, $\{P_0=0,\ (\mathbf P,\mathbf P)=0\}$ |
| $\mathbf p,\mathbf p'$ | The two real vector parts of a nilpotent, $\tilde\Upsilon=\mathbf p+i\mathbf p'$, orthogonal and of equal sum of squares |
| $r(\hat{\mathbf p}+i\hat{\mathbf p}')$ | The parametrisation of the cone over orthonormal real unit pairs |
| $\tilde P$, $\tilde Q$ | The generic element of a statement that holds for every element |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the general definition of a root of a central value and of the nilpotent, with the index of nilpotency and the square-zero element.
- *Square Roots of One and the Idempotents of the General Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-algebra.md`), for the roots of $+1$ and the idempotents, the other two central element classes.
- *Square Roots of a General Element in the General Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-general-plain-algebra.md`), for the roots of the general quadratic $\tilde\Xi^2=\tilde Q$, of which the roots of $0$ here are one case.
- *Zero Divisors of the General Plain Algebra* (`articles_maths/zero-divisors-of-the-general-plain-algebra.md`), for the two families of the zero-divisor set, the pure family being exactly these nilpotents.
- *Ideals and Peirce Decomposition of the General Plain Algebra* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra.md`), for the off-diagonal units $\tilde\Upsilon_1,\tilde\Upsilon_2$, the minimal ideals they generate and the Peirce basis.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_maths/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), for the isomorphism $\mathsf M_2$, the trace and determinant, and the triangular Jordan form.
- *Introduction to the Remarkable Subspaces* (`articles_maths/introduction-to-the-remarkable-subspaces.md`), for the vector subspace, the nilpotent cone it carries and the absence of a nilpotent in the other five subspaces.
- *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/zero-divisors-in-the-12-algebraic-structures-over-the-biquaternion-c-space.md`), for the same class read against the four general products, where only the plain product has this square-zero set.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), for the algebraic properties of the biquaternions.
