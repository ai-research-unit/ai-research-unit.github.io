# __Square Roots of Zero and the Nilpotents of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra $\mathbb{B}^{\bullet}$ is the complex space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ under the Jordan product

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl(\tilde P\tilde Q+\tilde Q\tilde P\bigr)
$$

of *Introduction to the Symmetric Plain Algebra of Biquaternions*, the symmetrisation of the general plain bilinear product of *Introduction to the General Plain Algebra of Biquaternions*, and the operation named $\mathrm{SPA}$ in *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. The square of the block is the **plain square**, $\tilde Q\bullet\tilde Q=\tilde Q^2$, the antisymmetric part of the product vanishing on the diagonal.

The article treats two subjects, and in this order. The first is the square roots of the central value $0$, the elements $\tilde\Xi\in\mathbb{B}$ with

$$
\tilde\Xi\bullet\tilde\Xi=0 .
$$

The second is the nilpotents of the block, the nonzero elements whose square vanishes. The two subjects are one subject: the roots of $0$ are the element $0$ together with the square-zero elements, and the nonzero square-zero elements are exactly the nilpotents. The roots of $+1$ and the idempotents are the companion article *Square Roots of One and the Idempotents of the Symmetric Plain Algebra*; the roots of the general quadratic $\tilde\Xi\bullet\tilde\Xi=\tilde Q$ are *Square Roots of a General Element in the Symmetric Plain Algebra*.

The roots of $0$ of the block and the roots of $0$ of the general plain product are the same set, the two squares being equal; the criterion is the one of *Square Roots of Zero and the Nilpotents of the General Plain Algebra*, restated here in the block's coordinates and with the block's reading.

**The results.** The roots of $0$ are the origin together with the nilpotent cone, the pure elements whose complex vector part is isotropic, a four-real-parameter family. The nilpotents are exactly the nonzero pure elements with $Q_0=0$ and $(\vec Q,\vec Q)=0$; they form the nilpotent cone, a complex quadric of complex dimension two and real dimension four inside the vector subspace, and they are a proper subset of the block's zero-divisor set, which also contains every non-isotropic pure element. The element is of index two, every nilpotent being square-zero; the block's own reading is the **operator**, and there the index is three: the left multiplication is not square-zero, $L^{\bullet}_{\tilde\Upsilon}{}^{2}\neq0$ and $L^{\bullet}_{\tilde\Upsilon}{}^{3}=0$, its image $\mathrm{span}\{e_0,\tilde\Upsilon\}$ is not contained in its kernel, no flag is produced, and the image and the kernel are not complementary either, meeting in the line $\mathbb{C}\tilde\Upsilon$, so that the splitting $\mathbb{B}=\ker L^{\bullet}_{\tilde\Upsilon}{}^{2}\oplus\mathbb{C}e_2$ takes the place of the flag; the ideal–annihilator coincidence $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$ of the algebra fails.

The article is algebraic. The zero-divisor set, its two families and the criterion on the central square are *Zero Divisors of the Symmetric Plain Algebra*; the roots of $+1$ and the idempotents are *Square Roots of One and the Idempotents of the Symmetric Plain Algebra*; the general root problem is *Square Roots of a General Element in the Symmetric Plain Algebra*; the operator theory of the block is *The Multiplication Operators of the Symmetric Plain Algebra*; and the failure of left alternativity that makes the operator of a nilpotent of index three is *The Specificities of the Symmetric Plain Algebra*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$, and central scalar imaginary $i$, $i^2=-1$. A general element is $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu=Q_0e_0+\vec Q$ with $Q_\mu\in\mathbb{C}$ and $\vec Q=\sum_{k=1}^{3}Q_ke_k$. The general plain bilinear form of two vector parts is

$$
(\vec P,\vec Q)=\sum_{k=1}^{3}P_kQ_k,
$$

and the square of a pure element is $\vec Q^2=-(\vec Q,\vec Q)e_0$. The **central square** is

$$
\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=C(\tilde Q)e_0,\qquad C(\tilde Q)=\sum_{\mu=0}^{3}Q_\mu^2=Q_0^2+(\vec Q,\vec Q),
$$

the generic norm of the block, written $N(\tilde Q)$ in *Norm and Invertibility in the Symmetric Plain Algebra*. The natural conjugation is $\tilde Q^{\natural}=Q_0-\vec Q$. The remarkable subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$ are *Introduction to the Remarkable Subspaces* and *Remarkable Subspaces under the Symmetric Plain Algebra of Biquaternions*. A root of a central value is written $\tilde\Xi$ (§*The Root Convention* of *Conventions in Mathematics*), a nilpotent $\tilde\Upsilon$ (§*The Nilpotent Convention*), and a generic element $\tilde P$ or $\tilde Q$.

The equations name a product, so the roots and the nilpotents are relative to it. The general definition of the power, the square, the root of a central value and the nilpotent, with the index of nilpotency and the square-zero element, is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots* and §*The Nilpotent*. Throughout this article the square is the one of the symmetric plain product, which is the plain square; the other three general products and their parts carry roots of $0$ and square-zero sets of their own, and they are *Comparison Between the Four General Products*.

## The Roots of Zero

**The roots of $0$ are exactly the origin and the nilpotent cone, the pure elements with $(\vec\Xi,\vec\Xi)=0$, a four-real-parameter family; the nonzero roots are the nilpotents of the block.**

A **root of $0$** is an element $\tilde\Xi\in\mathbb{B}$ with $\tilde\Xi\bullet\tilde\Xi=0$, the square being the one of the symmetric plain product.

### The Reduction

Write the root in scalar and vector parts,

$$
\tilde\Xi=\Xi_0e_0+\vec\Xi,\qquad \vec\Xi=\Xi_1e_1+\Xi_2e_2+\Xi_3e_3,\qquad \Xi_k\in\mathbb{C}.
$$

The square of the block is the plain square, given by the product formula,

$$
\tilde\Xi\bullet\tilde\Xi=\tilde\Xi^2=\bigl(\Xi_0^2-(\vec\Xi,\vec\Xi)\bigr)e_0+2\Xi_0\vec\Xi,\qquad (\vec\Xi,\vec\Xi)=\Xi_1^2+\Xi_2^2+\Xi_3^2,
$$

so equating $\tilde\Xi^2$ to $0$ splits the equation into a vector part and a scalar part,

$$
2\Xi_0\vec\Xi=0,
$$

$$
\Xi_0^2-(\vec\Xi,\vec\Xi)=0 .
$$

Since $\mathbb{C}$ is a field, the vector equation holds exactly when $\Xi_0=0$ or $\vec\Xi=0$. The roots of $0$ therefore split into two disjoint cases: the root is a complex scalar, $\vec\Xi=0$, or the root is pure, $\Xi_0=0$.

### The Zero Element

In the scalar case $\tilde\Xi=\Xi_0e_0$ and the scalar equation reads $\Xi_0^2=0$; since $\mathbb{C}$ is a field, $\Xi_0=0$. The root in this case is the single element

$$
\tilde\Xi=0,
$$

the origin.

### The Null Cone

In the pure case $\tilde\Xi=\vec\Xi$ and the scalar equation reads

$$
(\vec\Xi,\vec\Xi)=\Xi_1^2+\Xi_2^2+\Xi_3^2=0 .
$$

Write the complex coefficients as $\Xi_k=\xi_k+i\xi'_k$ with real $\xi_k,\xi'_k$, so that

$$
\vec\Xi=\vec\xi+i\vec\xi',\qquad \vec\xi=\sum_{k=1}^{3}\xi_ke_k,\qquad \vec\xi'=\sum_{k=1}^{3}\xi'_ke_k .
$$

Then

$$
(\vec\Xi,\vec\Xi)=\sum_{k=1}^{3}(\xi_k+i\xi'_k)^2=\bigl(\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2\bigr)+2i\bigl(\xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3\bigr),
$$

so the single complex equation $(\vec\Xi,\vec\Xi)=0$ is the two real equations

$$
\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2=0,\qquad \xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3=0 .
$$

Six real coefficients carry two constraints, so the roots in this case form a **four-real-parameter family**, the **null cone** of the pure subspace; equivalently its two real vector parts $\vec\xi$ and $\vec\xi'$ are orthogonal and satisfy $\vec\xi\cdot\vec\xi=\vec\xi'\cdot\vec\xi'$. Its nonzero elements are the nilpotents of the block.

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

that is, writing $\Xi_k=\xi_k+i\xi'_k$, the pair of real equations $\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2=0$ and $\xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3=0$. Its nonzero elements are the nilpotents of the block.

### Verification

For a pure $\tilde\Xi$ with $(\vec\Xi,\vec\Xi)=0$ the scalar part of $\tilde\Xi^2$ is $-(\vec\Xi,\vec\Xi)=0$ and the vector part is $2\Xi_0\vec\Xi=0$, since $\Xi_0=0$; so such an element is a root of $0$. The scalar case gives only the origin, and the two cases are exhaustive by the reduction, because the vector equation forces $\Xi_0=0$ or $\vec\Xi=0$.

A worked instance is

$$
\tilde\Xi=e_1+ie_2,\qquad (e_1+ie_2)^2=e_1^2+i^2e_2^2+i(e_1e_2+e_2e_1)=-e_0+e_0+0=0 .
$$

### The Roots of Zero and the Nilpotents

The nonzero roots of $0$ are exactly the **nilpotents** of the block. This is the criterion of §*The Criterion*: an element has vanishing square exactly when it is pure with isotropic vector part, $P_0=0$ and $(\vec P,\vec P)=0$, which is the defining equation of the null cone above with the origin removed. The roots of $0$ are therefore the origin together with the nilpotent cone, and the remainder of this article studies that cone.

The nonzero roots of $0$ are **not units**. A root of $0$ other than $0$ is a nilpotent, hence a square-zero element, and a square-zero element is a zero divisor: it annihilates itself, and a unit is never a zero divisor. This is the behaviour opposite to the roots of $+1$, which are units of the block; the roots of the three central values and their invertibility are read value by value in *Square Roots of One and the Idempotents of the Symmetric Plain Algebra* and *Square Roots of a General Element in the Symmetric Plain Algebra*.

## The Nilpotents

**The nilpotents of the block are exactly the nonzero pure elements with isotropic vector part, $P_0=0$ and $P_1^2+P_2^2+P_3^2=0$; they form the nilpotent cone of complex dimension two and real dimension four inside the vector subspace, they are a proper subset of the block's zero-divisor set, and each one's operator has index three.**

The **nilpotents** of the block are the nonzero elements whose square vanishes. The class is small and rigid, and it is the same class as that of the general plain algebra, the two squares being equal. A nilpotent has vanishing scalar part, so it is a pure biquaternion; its vector part is isotropic for the general plain bilinear form; and those two conditions together are equivalent to the vanishing of the square. Each nonzero nilpotent annihilates itself, $\tilde\Upsilon\bullet\tilde\Upsilon=0$, and is therefore a zero divisor of a particularly simple kind, its own two-sided annihilating partner. The nilpotents are the isotropic elements of the pure family of the block's zero-divisor set: the pure family is the whole vector subspace with the origin removed, and its isotropic elements are exactly these nilpotents, while the other family of the zero-divisor set is the isotropic elements with non-vanishing scalar part, the complex multiples of the non-trivial idempotents.

### The Definition

**Definition.** A **nilpotent** of the symmetric plain algebra is a nonzero element $\tilde\Upsilon\in\mathbb{B}$ with vanishing square,

$$
\tilde\Upsilon\bullet\tilde\Upsilon=0 .
$$

The element $0$ is a square-zero element, and it is not a nilpotent. The equation names a product, and the notion is relative to it; the general definition, with the index of nilpotency and the square-zero element, is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Nilpotent*. Throughout this article the product is the symmetric plain product, which has the plain square; where another of the four general products is meant it is named.

The element is of **index two**: its square vanishes while it does not, and since $\tilde\Upsilon\bullet\tilde\Upsilon^{\bullet2}=\tilde\Upsilon^{\bullet2}\bullet\tilde\Upsilon=0$ every higher power vanishes as well. §*Index Two* shows conversely that a vanishing cube already forces a vanishing square, so the block carries no nilpotent of higher index, and the two clauses of the definition are exhaustive: the nilpotents are exactly the nonzero square-zero elements, with no further stratification.

The star preserves nilpotency, since conjugation is multiplicative and carries a vanishing square to a vanishing square,

$$
(\tilde\Upsilon^{*})^{\bullet2}=(\tilde\Upsilon^{\bullet2})^{*}=0,\qquad (\tilde\Upsilon^{\natural})^{\bullet2}=(\tilde\Upsilon^{\bullet2})^{\natural}=0 .
$$

The nilpotents are thus a conjugation-stable class, and a statement about one nilpotent is a statement about its two conjugates.

### The Criterion

**An element is a nilpotent exactly when it is pure and its vector part is isotropic, $P_0=0$ and $(\vec P,\vec P)=0$; every nilpotent is then a zero divisor and its element-powers stop at the second.**

The square of a general element closes in two terms, one central and one along the vector part, because the vector part is a pure quaternion combination and its own square is central:

$$
\tilde Q^2=\bigl[Q_0^2-(\vec Q,\vec Q)\bigr]e_0+2Q_0\vec Q .
$$

**Theorem (the criterion for a nilpotent).** For $\tilde P\in\mathbb{B}$ the following are equivalent: $\tilde P\bullet\tilde P=0$; $\tilde P$ is pure, $P_0=0$, and its vector part is isotropic, $(\vec P,\vec P)=0$; and $P_0=0$ and $C(\tilde P)=0$. The nonzero solutions are exactly the nilpotents.

**Proof.** The displayed formula expands the square. If $P_0\neq0$ then the vector part $2P_0\vec P$ vanishes only for $\vec P=0$, and then the scalar part is $P_0^2\neq0$; so a square-zero element is pure. For a pure $\tilde P$ the formula reads $\tilde P^2=-(\vec P,\vec P)e_0$, a central element, which vanishes exactly when $(\vec P,\vec P)=0$. Finally, for pure $\tilde P$ the central square is $C(\tilde P)=P_0^2+(\vec P,\vec P)=(\vec P,\vec P)$, so the two conditions agree.

**Corollary.** Every nilpotent is pure, and every nilpotent is a zero divisor. Its only nonzero power relation is $\tilde\Upsilon^{\bullet2}=0$, the central zero, so its element-powers stop at the second.

The criterion separates the class sharply: the nilpotents are the elements of the vector subspace, the kernel of the scalar part, whose vector part is isotropic for the general plain bilinear form. An element with a nonzero scalar part is never nilpotent.

### The Nilpotent Cone

**The nilpotents form the cone $\{P_1^2+P_2^2+P_3^2=0\}$ in the vector subspace, of complex dimension two and real dimension four; its nonzero elements are $r(\hat p+i\hat p')$ with $r>0$ and $\hat p,\hat p'$ orthogonal real unit vectors.**

The set of nilpotents is the vanishing set of the two conditions of the criterion, and it is a cone. The vector part of a nilpotent is a complex vector $\vec P=(P_1,P_2,P_3)$, and its coefficients split into a real and an imaginary part, $P_k=p_k+ip'_k$ with real $p_k,p'_k$, so that the vector part splits into two real vector parts carrying the central imaginary on the second,

$$
\vec P=\vec p+i\vec p',\qquad \vec p=\sum_{k=1}^{3}p_ke_k,\qquad \vec p'=\sum_{k=1}^{3}p'_ke_k .
$$

The single complex equation $(\vec P,\vec P)=P_1^2+P_2^2+P_3^2=0$ is then the two real equations

$$
\vec p\cdot\vec p=\vec p'\cdot\vec p',\qquad \vec p\cdot\vec p'=0,
$$

that is $\sum_kp_k^2=\sum_k(p'_k)^2$ and $\sum_kp_kp'_k=0$: the two real parts of a nilpotent are orthogonal and have equal sum of squares.

**Proposition (the cone).** The nilpotents form the **nilpotent cone**

$$
\{\tilde\Upsilon=P_1e_1+P_2e_2+P_3e_3 : P_1^2+P_2^2+P_3^2=0\},
$$

a complex cone of complex dimension two and real dimension four, a four-real-parameter family. Its nonzero elements are written

$$
\tilde\Upsilon=\vec p+i\vec p',\qquad \vec p\cdot\vec p=\vec p'\cdot\vec p',\qquad \vec p\cdot\vec p'=0,
$$

and equivalently, with $r>0$ and $\hat p,\hat p'$ the two orthogonal real unit directions, so that $r^2=\vec p\cdot\vec p=\vec p'\cdot\vec p'$,

$$
\tilde\Upsilon=r(\hat p+i\hat p'),\qquad r>0,\qquad \hat p\cdot\hat p=\hat p'\cdot\hat p'=1,\qquad \hat p\cdot\hat p'=0 .
$$

**Proof.** The first is the criterion. The complex equation cuts a complex-quadric cone in $\mathbb{C}^3$, of complex dimension two; as a real cone it is the two real equations displayed, whose independence away from the origin gives real dimension four. For the parametrisation, the two real equations say that the real part $\vec p$ and the imaginary part $\vec p'$ are orthogonal and have equal sum of squares, which is the stated form; conversely such a pair satisfies both.

The cone is stable under complex scaling, $\tilde\Upsilon\mapsto\lambda\tilde\Upsilon$ for $\lambda\in\mathbb{C}$, because the isotropy condition is homogeneous of degree two; it is stable under the star, which conjugates the two real parts; and the natural conjugation sends $\tilde\Upsilon$ to $-\tilde\Upsilon$. The parameter $r$ is fixed by $r^2=\vec p\cdot\vec p=\vec p'\cdot\vec p'$, and the pair $(\hat p,\hat p')$ is determined up to the simultaneous sign change $(\hat p,\hat p')\mapsto(-\hat p,-\hat p')$.

### Index Two

**Every nilpotent is of index two: $\tilde P^{\bullet3}=0$ exactly when $\tilde P^{\bullet2}=0$, and the block carries no nilpotent of index three or more.**

**Theorem (no higher index).** For the block, $\tilde P^{\bullet3}=0$ exactly when $\tilde P^{\bullet2}=0$. Every nilpotent is of index two, and the block carries none of index three or more.

**Proof.** The cube is read from the displayed square by the same computation as for the algebra,

$$
\tilde P^{\bullet3}=P_0\bigl[P_0^2-3(\vec P,\vec P)\bigr]e_0+\bigl[3P_0^2-(\vec P,\vec P)\bigr]\vec P ,
$$

since the block's powers are the plain powers. If $\vec P=0$ then $\tilde P=P_0e_0$ and $\tilde P^{\bullet3}=P_0^3e_0$, which vanishes only for $P_0=0$, that is for $\tilde P=0$, and then $\tilde P^{\bullet2}=0$ as well. If $\vec P\neq0$ then the vanishing of the vector part of $\tilde P^{\bullet3}$ forces $(\vec P,\vec P)=3P_0^2$, and the scalar part is then $P_0[P_0^2-3\cdot3P_0^2]=-8P_0^3$, which vanishes only for $P_0=0$, whereupon $(\vec P,\vec P)=0$. In both cases $\tilde P^{\bullet3}=0$ gives $P_0=0$ and $(\vec P,\vec P)=0$, which is $\tilde P^{\bullet2}=0$. The converse is immediate.

The theorem is the reason the word "nilpotent" needs no index qualifier for the element. It also fixes the shape of the element-powers: a nilpotent has the two-term power string $\tilde\Upsilon,\tilde\Upsilon^{\bullet2}=0$ and no longer one, whereas a non-pure zero divisor has the infinite string $\tilde P^{\bullet k}=2^{k-1}P_0^{k-1}\tilde P$ of *Zero Divisors of the Symmetric Plain Algebra*.

### The Operator of a Nilpotent

**For a nilpotent the left multiplication is not square-zero but has index three, $L^{\bullet}_{\tilde\Upsilon}{}^{2}\neq0$ and $L^{\bullet}_{\tilde\Upsilon}{}^{3}=0$; its image is not contained in its kernel, so it produces no flag, and image and kernel are not complementary either, meeting in the line $\mathbb{C}\tilde\Upsilon$; the splitting $\mathbb{B}=\ker L^{\bullet}_{\tilde\Upsilon}{}^{2}\oplus\mathbb{C}e_2$ takes the place of the flag; and the ideal–annihilator coincidence $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$ of the algebra fails, image and annihilator being different two-dimensional subspaces that meet in the line $\mathbb{C}\tilde\Upsilon$.**

The index of the element and the index of its operator are different, and the two are never conflated: the element $\tilde\Upsilon$ is square-zero, of index two, while the operator $L^{\bullet}_{\tilde\Upsilon}$ is of index three. The reason is that the block is not left-alternative: left alternativity is the identity $L^{\bullet}_{\tilde X}{}^{2}=L^{\bullet}_{\tilde X^{\bullet2}}$, which would make the operator of a square-zero element square-zero, and the block fails it (*The Specificities of the Symmetric Plain Algebra*).

#### The Square-Zero Element Does Not Give a Square-Zero Operator

**Proposition.** For a nilpotent $\tilde\Upsilon$ the left multiplication is not square-zero: $L^{\bullet}_{\tilde\Upsilon}{}^{2}\neq0$, and its index is three,

$$
L^{\bullet}_{\tilde\Upsilon}{}^{2}\neq0,\qquad L^{\bullet}_{\tilde\Upsilon}{}^{3}=0 .
$$

**Proof.** On the witness $\tilde\Upsilon=e_1+ie_2$ the products are $\tilde\Upsilon\bullet e_0=\tilde\Upsilon$, $\tilde\Upsilon\bullet e_1=-e_0$, $\tilde\Upsilon\bullet e_2=-ie_0$, $\tilde\Upsilon\bullet e_3=0$; so $\mathrm{im}\,L^{\bullet}_{\tilde\Upsilon}=\mathrm{span}\{e_0,\tilde\Upsilon\}$, the image of the second power is $\mathrm{span}\{L^{\bullet}_{\tilde\Upsilon}e_0,L^{\bullet}_{\tilde\Upsilon}\tilde\Upsilon\}=\mathrm{span}\{\tilde\Upsilon,0\}=\mathbb{C}\tilde\Upsilon$, a line, and the third power is zero.

In the algebra the same witness has $L_{\tilde\Upsilon}^{2}=L_{\tilde\Upsilon^{\bullet2}}=L_{0}=0$, because the operator of a square is the square of the operator, which is left alternativity. The block is not left-alternative and the identity fails; the operator of a square-zero element has the index three of a regular nilpotent and not the index two of a square-zero one.

#### The Absence of the Flag

**Corollary (no flag).** The image of $L^{\bullet}_{\tilde\Upsilon}$ is not contained in its kernel:

$$
\mathrm{im}\,L^{\bullet}_{\tilde\Upsilon}=\mathrm{span}\{e_0,\tilde\Upsilon\}\not\subseteq\ker L^{\bullet}_{\tilde\Upsilon},\qquad e_0\notin\ker L^{\bullet}_{\tilde\Upsilon}.
$$

**Proof.** The image is $\mathrm{span}\{e_0,\tilde\Upsilon\}$ and $L^{\bullet}_{\tilde\Upsilon}e_0=\tilde\Upsilon\neq0$, so the unit is not in the kernel; the containment that would place the image inside the kernel therefore fails.

So the block produces **no flag** $\{0\}\subseteq\mathrm{im}\,L\subseteq\ker L\subseteq\mathbb{B}$ from a nilpotent. The image and the kernel are two distinct subspaces of dimension two, but they are **not** complementary: on the witness the image is $\mathrm{span}\{e_0,\tilde\Upsilon\}$ and the kernel is $\mathrm{span}\{e_3,-ie_1+e_2\}=\mathrm{span}\{e_3,\tilde\Upsilon\}$, because $-ie_1+e_2=-i\tilde\Upsilon$, so their intersection is the line $\mathbb{C}\tilde\Upsilon$ and their sum is the hyperplane $\mathrm{span}\{e_0,e_3,\tilde\Upsilon\}$,

$$
\mathrm{im}\,L^{\bullet}_{\tilde\Upsilon}\cap\ker L^{\bullet}_{\tilde\Upsilon}=\mathbb{C}\tilde\Upsilon,\qquad \mathrm{im}\,L^{\bullet}_{\tilde\Upsilon}+\ker L^{\bullet}_{\tilde\Upsilon}=\mathrm{span}\{e_0,e_3,\tilde\Upsilon\}.
$$

The intersection is not trivial because $\tilde\Upsilon=L^{\bullet}_{\tilde\Upsilon}e_0$ lies in the image and $L^{\bullet}_{\tilde\Upsilon}\tilde\Upsilon=\tilde\Upsilon\bullet\tilde\Upsilon=0$ places it in the kernel. The operator is a single Jordan chain with three terms over that hyperplane, and the direct splitting that takes the place of the flag is

$$
\mathbb{B}=\ker L^{\bullet}_{\tilde\Upsilon}{}^{2}\oplus\mathbb{C}e_2,\qquad \ker L^{\bullet}_{\tilde\Upsilon}{}^{2}=\mathrm{span}\{e_0,e_3,\tilde\Upsilon\},\qquad L^{\bullet}_{\tilde\Upsilon}{}^{2}e_2=-i\tilde\Upsilon\neq0.
$$

#### The Failure of the Ideal–Annihilator Coincidence

In the algebra the left ideal generated by a nilpotent coincides with its annihilator, $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$. In the block the analogue fails.

**Proposition.** The image of $L^{\bullet}_{\tilde\Upsilon}$, the set $\mathbb{B}\bullet\tilde\Upsilon$, is $\mathrm{span}\{e_0,\tilde\Upsilon\}$, a two-dimensional subspace, and it is not the annihilator $\ker L^{\bullet}_{\tilde\Upsilon}$, which is the different two-dimensional subspace $\mathrm{span}\{e_3,-ie_1+e_2\}$; the two are not complementary, their intersection being the line $\mathbb{C}\tilde\Upsilon$.

**Proof.** The image is computed above; the annihilator is computed in *Zero Divisors of the Symmetric Plain Algebra*, where the pure family has a kernel equal to the pure orthogonal complement of the vector part, for $\tilde\Upsilon=e_1+ie_2$ the subspace $\mathrm{span}\{e_3,-ie_1+e_2\}$. The unit is in the image and not in the kernel, so the image is not contained in the kernel; the intersection is the line $\mathbb{C}\tilde\Upsilon$, since the image of the unit is $\tilde\Upsilon$ and $L^{\bullet}_{\tilde\Upsilon}\tilde\Upsilon=\tilde\Upsilon\bullet\tilde\Upsilon=0$.

The coincidence $\mathbb{B}\tilde\Upsilon=I_{\tilde\Upsilon}$ of the algebra is a theorem of its associativity, and the block, being non-associative, does not carry it.

### The Relation to the Other Notions

**A nilpotent is a zero divisor that annihilates itself, belonging to the pure family of the block's zero-divisor set, with annihilator the two-dimensional pure orthogonal complement of its vector part; it is never a non-trivial idempotent, the two classes meeting only at $0$; and the nilpotents are exactly the nonzero roots of $0$.**

**Nilpotents and the zero divisors.** A nilpotent is a zero divisor with $\tilde\Upsilon\bullet\tilde\Upsilon=0$, and it belongs to the pure family of *Zero Divisors of the Symmetric Plain Algebra*, whose annihilator is the two-dimensional orthogonal complement of its vector part, a plane that contains the conjugate line, since $\tilde\Upsilon\bullet\tilde\Upsilon=0$, but is not it. Unlike the isotropic family with non-vanishing scalar part, whose annihilator is a line spanned by the natural conjugate, its annihilator is a plane. The nilpotents are a proper subset of the block's zero-divisor set: the pure element $e_1$ is pure and non-isotropic and is still a zero divisor, since $e_1\bullet e_2=0$.

**Nilpotents and the idempotents.** A nilpotent is a nonzero pure element, so it cannot be a non-trivial idempotent, which has scalar part $\tfrac12$; the only element that is both a square-zero element and an idempotent is the origin. The two classes meet at the origin and nowhere else.

**Nilpotents and the roots.** The nilpotents are exactly the nonzero roots of $0$ of the block, and the roots of $0$ are the origin and them; this is the degeneracy of the general square-root problem at the central value $0$ (*Square Roots of a General Element in the Symmetric Plain Algebra*).

## Summary

The square of the block is the plain square, so the roots of $0$ of the block are exactly the roots of $0$ of the general plain algebra, the origin together with the nilpotent cone, the pure elements $\tilde\Xi=\Xi_1e_1+\Xi_2e_2+\Xi_3e_3$ with $\Xi_1^2+\Xi_2^2+\Xi_3^2=0$, a four-real-parameter family; writing $\Xi_k=\xi_k+i\xi'_k$, the two real equations are $\xi_1^2+\xi_2^2+\xi_3^2-(\xi'_1)^2-(\xi'_2)^2-(\xi'_3)^2=0$ and $\xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3=0$, and a worked instance is $e_1+ie_2$.

The nonzero roots of $0$ are exactly the nilpotents of the block, the nonzero elements of vanishing square. The criterion is $P_0=0$ and $(\vec P,\vec P)=0$, so every nilpotent is pure and its vector part is isotropic for the general plain bilinear form; the class is the nilpotent cone, a complex cone of complex dimension two and real dimension four, parametrised as $r(\hat p+i\hat p')$ over orthogonal pairs of real unit vectors, and it is a proper subset of the block's zero-divisor set, which also contains every non-isotropic pure element. The element is of index two: $\tilde P^{\bullet3}=0$ exactly when $\tilde P^{\bullet2}=0$; the operator is of index three, and the two are never conflated.

Every nilpotent annihilates itself, so it is a two-sided zero divisor and the ideal it generates is its own annihilator in the algebra, a coincidence the block fails; the nilpotents are the isotropic elements of the pure family of the zero-divisor set, the other family being the isotropic elements with non-vanishing scalar part, and the two classes of nilpotents and idempotents meet only at $0$. The star preserves the nilpotent set, the natural conjugation sends $\tilde\Upsilon$ to $-\tilde\Upsilon$, and the block's own reading is the operator: no square-zero operator, no flag, an image $\mathrm{span}\{e_0,\tilde\Upsilon\}$ not contained in the kernel and meeting the kernel in the line $\mathbb{C}\tilde\Upsilon$, and the splitting $\mathbb{B}=\ker L^{\bullet}_{\tilde\Upsilon}{}^{2}\oplus\mathbb{C}e_2$ in place of the flag. Of the remarkable subspaces only the vector subspace contains a nilpotent, and it contains all of them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q$ | the symmetric plain product, the multiplication of the block |
| $\tilde\Xi$ | a root of $0$, $\tilde\Xi\bullet\tilde\Xi=0$ |
| $\tilde\Xi=\Xi_0e_0+\vec\Xi$, $\vec\Xi=\vec\xi+i\vec\xi'$ | scalar and vector parts of a root; $\vec\xi,\vec\xi'$ real pure |
| $(\vec P,\vec Q)=\sum_kP_kQ_k$ | general plain bilinear form of two vector parts |
| $C(\tilde P)=\sum_\mu P_\mu^2=\tilde P\tilde P^{\natural}$ | the central square, the generic norm $N$ |
| $\tilde\Upsilon$ | a nilpotent, $\tilde\Upsilon\neq0$ and $\tilde\Upsilon^{\bullet2}=0$ |
| $\tilde\Upsilon=r(\hat p+i\hat p')$ | the parametrisation of the cone over orthogonal real unit pairs |
| $\mathcal N=\{\tilde\Upsilon\neq0:(\tilde\Upsilon,\tilde\Upsilon)=0\}$ | the nilpotent cone of the block |
| $\mathrm{im}\,L^{\bullet}_{\tilde\Upsilon}=\mathrm{span}\{e_0,\tilde\Upsilon\}$ | the image, of dimension two |
| $\ker L^{\bullet}_{\tilde\Upsilon}$ | the annihilator, of dimension two, orthogonal to the vector part |
| $\mathrm{im}\,L^{\bullet}_{\tilde\Upsilon}\cap\ker L^{\bullet}_{\tilde\Upsilon}=\mathbb{C}\tilde\Upsilon$ | the image and the kernel meet in a line, not complementarily |
| $\mathbb{B}=\ker L^{\bullet}_{\tilde\Upsilon}{}^{2}\oplus\mathbb{C}e_2$ | the splitting in place of the flag |
| $L^{\bullet}_{\tilde\Upsilon}{}^{3}=0$, $L^{\bullet}_{\tilde\Upsilon}{}^{2}\neq0$ | the index-three operator of the nilpotent |
| $\tilde P$, $\tilde Q$ | the generic element of a statement that holds for every element |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots* and §*The Nilpotent*, for the general definition of a root of a central value and of the nilpotent, with the index of nilpotency and the square-zero element.
- *Square Roots of Zero and the Nilpotents of the General Plain Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-plain-algebra.md`), for the criterion, the cone and the flag calculus of the algebra, which the block does not have.
- *Square Roots of One and the Idempotents of the Symmetric Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-symmetric-plain-algebra.md`), for the roots of $+1$ and the idempotents, the other two central element classes.
- *Square Roots of a General Element in the Symmetric Plain Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-symmetric-plain-algebra.md`), for the roots of the general quadratic $\tilde\Xi\bullet\tilde\Xi=\tilde Q$, of which the roots of $0$ here are one case.
- *Zero Divisors of the Symmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-algebra.md`), for the two parts of the zero-divisor set, the pure part being exactly these nilpotents together with the non-isotropic pure elements.
- *The Specificities of the Symmetric Plain Algebra* (`articles_maths/the-specificities-of-the-symmetric-plain-algebra.md`), for the left alternativity whose failure makes the operator of a nilpotent of index three.
- *The Multiplication Operators of the Symmetric Plain Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-plain-algebra.md`), for the operator theory of the block.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416.
