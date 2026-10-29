# __Zero Divisors and Units__

## Introduction

Multiplication makes every element of the algebra act on the algebra, on the left and on the right. This article studies what the action kills.

For $\tilde Q_1\in\mathbb{B}$, the set of elements that left multiplication by $\tilde Q_1$ sends to zero is a complex subspace of $\mathbb{B}$, and so is the set of elements that right multiplication sends to zero. The two are the **annihilators** of $\tilde Q_1$. Their dimensions are the invariant that separates the elements: an element that kills nothing is a unit, an element that kills something is a zero divisor, and there is no third case.

The article computes the two annihilators in coordinates, proves that a non-zero element has annihilators of dimension $0$ or $2$ and never anything else, exhibits a basis in each case, identifies the two-sided annihilator, and closes with the unit criterion. The article is form-free: it uses the product and the coefficients of *The Element, the Coordinates and the Conjugations*, and the square of *The Square of an Element*. The degenerate condition $Q_{1t}^2+B_1^2=0$ appears as the condition for a linear system to have a solution, not as a norm.

## The Two Annihilators

**Definition.** The **right annihilator** and the **left annihilator** of $\tilde Q_1$ are

$$
\mathrm{Ann}_r(\tilde Q_1)=\{\tilde Q_2\in\mathbb{B}:\tilde Q_1\tilde Q_2=0\},\qquad
\mathrm{Ann}_l(\tilde Q_1)=\{\tilde Q_2\in\mathbb{B}:\tilde Q_2\tilde Q_1=0\}.
$$

The right annihilator is the kernel of left multiplication by $\tilde Q_1$; the left annihilator is the kernel of right multiplication. Both contain $0$ and are closed under addition and under multiplication by a complex scalar, so both are complex subspaces of $\mathbb{B}$.

Write $\tilde Q_1=Q_{1t}e_t+\vec Q_1$ and $\tilde Q_2=Q_{2t}e_t+\vec Q_2$, with

$$
(\vec Q_1,\vec Q_2)=Q_{1x}Q_{2x}+Q_{1y}Q_{2y}+Q_{1z}Q_{2z},\qquad
B_1^2=(\vec Q_1,\vec Q_1)=Q_{1x}^2+Q_{1y}^2+Q_{1z}^2 .
$$

The scalar–vector form of the product gives

$$
\tilde Q_1\tilde Q_2=\bigl(Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr)e_t+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2,
$$

$$
\tilde Q_2\tilde Q_1=\bigl(Q_{1t}Q_{2t}-(\vec Q_1,\vec Q_2)\bigr)e_t+Q_{1t}\vec Q_2+Q_{2t}\vec Q_1-\vec Q_1\times\vec Q_2 .
$$

The two products have the same scalar part and differ only in the sign of the cross term. The annihilators therefore differ only in the sign carried by one of their equations, and this is the source of every symmetry below.

## The Right Annihilator

The equation $\tilde Q_1\tilde Q_2=0$ is the pair

$$
Q_{1t}Q_{2t}=(\vec Q_1,\vec Q_2),\qquad
Q_{1t}\vec Q_2+Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2=0 .
$$

**Non-pure case.** Suppose first that $Q_{1t}\neq0$. Then $Q_{2t}=(\vec Q_1,\vec Q_2)/Q_{1t}$, and the vector equation becomes

$$
Q_{1t}^2\vec Q_2+(\vec Q_1,\vec Q_2)\vec Q_1+Q_{1t}\,\vec Q_1\times\vec Q_2=0 .
$$

Taking the dot product of this equation with $\vec Q_1$ kills the cross term, because $\vec Q_1\times\vec Q_2$ is orthogonal to $\vec Q_1$, and gives

$$
\bigl(Q_{1t}^2+B_1^2\bigr)(\vec Q_1,\vec Q_2)=0 .
$$

*If $Q_{1t}^2+B_1^2\neq0$*, then $(\vec Q_1,\vec Q_2)=0$, hence $Q_{2t}=0$, and the reduced equation reads $Q_{1t}\vec Q_2+\vec Q_1\times\vec Q_2=0$. Crossing this equation with $\vec Q_1$ and using the identity

$$
\vec Q_1\times(\vec Q_1\times\vec Q_2)=\vec Q_1(\vec Q_1,\vec Q_2)-B_1^2\vec Q_2=-B_1^2\vec Q_2
$$

gives $-Q_{1t}^2\vec Q_2-B_1^2\vec Q_2=0$, that is $(Q_{1t}^2+B_1^2)\vec Q_2=0$, and so $\vec Q_2=0$. Therefore

$$
\mathrm{Ann}_r(\tilde Q_1)=0 .
$$

*If $Q_{1t}^2+B_1^2=0$*, then $B_1^2=-Q_{1t}^2\neq0$. Choose the sign of the square root $B_1$ of $B_1^2$ and a complex linear change of the basis $\vec e_x,\vec e_y,\vec e_z$ that preserves the dot and cross products and carries $\vec Q_1$ to $B_1\vec e_x$. The product is built from $e_t$, the dot product and the cross product, so the change preserves it, and only the description of the annihilator changes. Write $\vec Q_2=x\vec e_x+y\vec e_y+z\vec e_z$. The system is

$$
Q_{1t}Q_{2t}=B_1x,\qquad Q_{1t}x+B_1Q_{2t}=0,\qquad Q_{1t}y-B_1z=0,\qquad Q_{1t}z+B_1y=0 .
$$

Under $Q_{1t}^2+B_1^2=0$ the second equation of each pair is a consequence of the first. Hence

$$
Q_{2t}=\frac{B_1}{Q_{1t}}x,\qquad y=\frac{B_1}{Q_{1t}}z,
$$

with $x$ and $z$ free, and

$$
\mathrm{Ann}_r(\tilde Q_1)=\mathbb{C}\,\tilde Q_1^{\natural}\oplus\mathbb{C}\Bigl(\vec e_y-\frac{B_1}{Q_{1t}}\vec e_z\Bigr),
$$

because the generator with $x=1$, $z=0$ is the conjugate read in this frame, up to the non-zero scalar $B_1/Q_{1t}^2$.

**Pure case.** Suppose now that $Q_{1t}=0$. Since $\tilde Q_1\neq0$, its vector part is non-zero, $\vec Q_1\neq0$. The system reads

$$
(\vec Q_1,\vec Q_2)=0,\qquad Q_{2t}\vec Q_1+\vec Q_1\times\vec Q_2=0 .
$$

Crossing the second equation with $\vec Q_1$ gives

$$
\vec Q_1\times(\vec Q_1\times\vec Q_2)=\vec Q_1(\vec Q_1,\vec Q_2)-B_1^2\vec Q_2=-B_1^2\vec Q_2=0 .
$$

*If $B_1^2\neq0$*, then $\vec Q_2=0$, and then $Q_{2t}\vec Q_1=0$ gives $Q_{2t}=0$. Therefore $\mathrm{Ann}_r(\tilde Q_1)=0$.

*If $B_1^2=0$*, the vector part is isotropic. Choose a complex frame with $\vec Q_1=c(\vec e_x+i\vec e_y)$ and $c\neq0$, again by a change of the same kind. Writing $\vec Q_2=x\vec e_x+y\vec e_y+z\vec e_z$, the system is

$$
x+iy=0,\qquad Q_{2t}+iz=0,\qquad iQ_{2t}-z=0,\qquad y-ix=0 .
$$

The first and the last are one equation, $x=-iy$; the second and the third are one equation, $z=iQ_{2t}$. Hence $Q_{2t}$ and $y$ are free and

$$
\mathrm{Ann}_r(\tilde Q_1)=\mathbb{C}\,\tilde Q_1\oplus\mathbb{C}\bigl(e_t+i\vec e_z\bigr).
$$

The element itself belongs to its right annihilator, because $\tilde Q_1^2=-B_1^2e_t=0$.

**Zero element.** Finally $\mathrm{Ann}_r(0)=\mathbb{B}$.

## The Left Annihilator

The natural conjugation relates the two annihilators. Indeed, for every $\tilde Q_2$,

$$
\tilde Q_2\tilde Q_1=0\iff(\tilde Q_2\tilde Q_1)^{\natural}=0\iff\tilde Q_1^{\natural}\tilde Q_2^{\natural}=0,
$$

because ${}^{\natural}$ reverses the product and is an involution. Hence

$$
\mathrm{Ann}_l(\tilde Q_1)=\natural\bigl(\mathrm{Ann}_r(\tilde Q_1^{\natural})\bigr),
$$

and the two annihilators always have the same dimension. The conjugation is complex-linear and bijective, so it carries a basis to a basis.

The left annihilator is governed by the same system with the sign of the cross term reversed. In the two degenerate cases, in the frames of the preceding section, the same computation gives

$$
\mathrm{Ann}_l(\tilde Q_1)=\mathbb{C}\,\tilde Q_1^{\natural}\oplus\mathbb{C}\Bigl(\vec e_y+\frac{B_1}{Q_{1t}}\vec e_z\Bigr)
\quad(Q_{1t}\neq0,\ Q_{1t}^2+B_1^2=0),
$$

$$
\mathrm{Ann}_l(\tilde Q_1)=\mathbb{C}\,\tilde Q_1\oplus\mathbb{C}\bigl(e_t-i\vec e_z\bigr)
\quad(Q_{1t}=0,\ B_1^2=0),
$$

and $\mathrm{Ann}_l(\tilde Q_1)=0$ in the two non-degenerate cases, $\mathrm{Ann}_l(0)=\mathbb{B}$.

In the non-pure degenerate case the two annihilators are the planes spanned by the same vector $\tilde Q_1^{\natural}$ and by $\vec e_y\mp(B_1/Q_{1t})\vec e_z$; the two second generators differ in the sign of the coefficient of $\vec e_z$ and are not proportional, since $B_1\neq0$. The planes are therefore distinct. In the pure degenerate case they are the planes spanned by $\tilde Q_1$ and by $e_t\pm i\vec e_z$, again distinct, since $e_t$ lies in neither annihilator: $\tilde Q_1e_t=\tilde Q_1\neq0$ and $e_t\tilde Q_1=\tilde Q_1\neq0$.

## The Two-Sided Annihilator

The **two-sided annihilator** is the intersection of the two,

$$
\mathrm{Ann}(\tilde Q_1)=\mathrm{Ann}_l(\tilde Q_1)\cap\mathrm{Ann}_r(\tilde Q_1)=\{\tilde Q_2:\tilde Q_1\tilde Q_2=\tilde Q_2\tilde Q_1=0\}.
$$

**Theorem.** For $\tilde Q_1\neq0$,

$$
\dim\mathrm{Ann}(\tilde Q_1)=
\begin{cases}
0, & Q_{1t}^2+B_1^2\neq0,\\
1, & Q_{1t}^2+B_1^2=0.
\end{cases}
$$

In the second case $\mathrm{Ann}(\tilde Q_1)=\mathbb{C}\,\tilde Q_1^{\natural}$.

*Proof.* If $Q_{1t}^2+B_1^2\neq0$ both annihilators vanish and so does their intersection. If $Q_{1t}^2+B_1^2=0$ and $Q_{1t}\neq0$, the two annihilators are the distinct planes of the preceding section, and their intersection is their common line $\mathbb{C}\tilde Q_1^{\natural}$. If $Q_{1t}=0$ and $B_1^2=0$, the two annihilators are the distinct planes spanned by $\tilde Q_1$ and by $e_t\pm i\vec e_z$; their intersection is $\mathbb{C}\tilde Q_1$, and $\tilde Q_1^{\natural}=-\tilde Q_1$. QED.

Thus the elements that annihilate a zero divisor on both sides form one complex line. In the pure case that line is spanned by the element itself, which therefore squares to zero; in the non-pure case it is spanned by the conjugate, and the element does not annihilate itself.

## The Zero Divisors

**Definition.** An element $\tilde Q_1$ is a **zero divisor** when $\tilde Q_1\neq0$ and at least one of its annihilators is non-zero; equivalently, when there is a non-zero $\tilde Q_2$ with $\tilde Q_1\tilde Q_2=0$ or $\tilde Q_2\tilde Q_1=0$.

By the computations of the two preceding sections, the two annihilators have the same dimension, so the two alternatives are equivalent. The criterion is the following.

**Theorem.** Let $\tilde Q_1\neq0$. Then $\tilde Q_1$ is a zero divisor if and only if

$$
Q_{1t}^2+B_1^2=0 .
$$

Both annihilators then have complex dimension $2$, the two-sided annihilator has complex dimension $1$, and the two one-sided annihilators are distinct.

*Proof.* If $Q_{1t}\neq0$, the right annihilator is zero exactly when $Q_{1t}^2+B_1^2\neq0$ and is a plane when $Q_{1t}^2+B_1^2=0$. If $Q_{1t}=0$, the right annihilator is zero when $B_1^2\neq0$ and a plane when $B_1^2=0$; and $Q_{1t}=0$ makes $Q_{1t}^2+B_1^2=B_1^2$. The claims about the dimensions are those of the explicit bases. QED.

The zero divisors split into two families.

**The pure family.** $Q_{1t}=0$ and $B_1^2=0$, with $\vec Q_1\neq0$. The element is pure and isotropic, it annihilates itself on both sides, and $\tilde Q_1^2=0$. Its annihilators are the planes through the line $\mathbb{C}\tilde Q_1$. These elements are the non-zero square-zero elements of the algebra; they are treated in *Nilpotents*.

**The non-pure family.** $Q_{1t}\neq0$ and $Q_{1t}^2+B_1^2=0$, so $B_1^2=-Q_{1t}^2\neq0$. The element does not annihilate itself: $\tilde Q_1^2=2Q_{1t}(Q_{1t}e_t+\vec Q_1)\neq0$, because $Q_{1t}\neq0$ and $\vec Q_1\neq0$. Its two annihilators are distinct planes meeting in the line $\mathbb{C}\tilde Q_1^{\natural}$. The conjugate is the common annihilator: it is the first generator of each of the two bases above, and it lies in both annihilators.

**The cone.** The condition $Q_{1t}^2+B_1^2=0$ is one complex equation in the four complex coordinates of $\tilde Q_1$, and its gradient $(2Q_{1t},2Q_{1x},2Q_{1y},2Q_{1z})$ vanishes only at the origin. The zero-divisor set is therefore a complex cone of complex dimension $3$, of real dimension $6$, smooth away from the origin, with the pure family as the subcone $Q_{1t}=0$ of complex dimension $2$, of real dimension $4$.

**Products.** Let $\tilde Q_1$ be a zero divisor with a non-zero element $\tilde Q_3$ in its left annihilator, $\tilde Q_3\tilde Q_1=0$. For every $\tilde Q_2$,

$$
\tilde Q_3(\tilde Q_1\tilde Q_2)=(\tilde Q_3\tilde Q_1)\tilde Q_2=0,
$$

so $\tilde Q_1\tilde Q_2$ is annihilated on the left by $\tilde Q_3$: a product of a zero divisor with any element is a zero divisor or zero. The same argument on the other side shows that a product with an element on the left, $\tilde Q_2\tilde Q_1$, is a zero divisor or zero. In particular no product of two zero divisors is a unit.

## The Units

**Definition.** An element $\tilde U$ is a **unit** when there is an element $\tilde V$ with

$$
\tilde U\tilde V=\tilde V\tilde U=e_t .
$$

**Proposition.** For $\tilde Q_1\neq0$ the following are equivalent: $\tilde Q_1$ is a unit; $\mathrm{Ann}_r(\tilde Q_1)=0$; $\mathrm{Ann}_l(\tilde Q_1)=0$; $Q_{1t}^2+B_1^2\neq0$.

*Proof.* A unit has trivial annihilators, because multiplying $\tilde Q_1\tilde Q_2=0$ on the left by its inverse gives $\tilde Q_2=0$, and similarly on the right.

Conversely, suppose $\mathrm{Ann}_r(\tilde Q_1)=0$. Left multiplication by $\tilde Q_1$ is then injective, and on the finite-dimensional complex space $\mathbb{B}$ it is bijective. Let $\tilde V$ be the preimage of $e_t$, so that $\tilde Q_1\tilde V=e_t$. Then $\tilde Q_1(\tilde V\tilde Q_1-e_t)=\tilde Q_1\tilde V\tilde Q_1-\tilde Q_1=0$, so $\tilde V\tilde Q_1-e_t$ lies in the right annihilator, which is zero, and $\tilde V\tilde Q_1=e_t$. Hence $\tilde Q_1$ is a unit. The same argument with the left annihilator gives the same conclusion, and the two annihilators have equal dimension.

The last equivalence is the theorem of the preceding section: the annihilator is non-zero exactly when $Q_{1t}^2+B_1^2=0$. QED.

So the non-zero elements split into the units and the zero divisors, according as $Q_{1t}^2+B_1^2$ is non-zero or zero, and the units are exactly the elements with trivial annihilators. The criterion is a condition on the annihilator, not a normalisation: $B_1^2$ alone does not decide, since

$$
\tilde Q_1=e_t+\vec e_x+i\vec e_y
$$

has $B_1^2=1+i^2=0$ and is a unit, with $Q_{1t}^2+B_1^2=1$.

## Summary

- $\mathrm{Ann}_r(\tilde Q_1)=\{\tilde Q_2:\tilde Q_1\tilde Q_2=0\}$ is the kernel of left multiplication; $\mathrm{Ann}_l(\tilde Q_1)=\{\tilde Q_2:\tilde Q_2\tilde Q_1=0\}$ is the kernel of right multiplication; they are complex subspaces of equal dimension.
- For $\tilde Q_1\neq0$ the common dimension is $0$ when $Q_{1t}^2+B_1^2\neq0$ and $2$ when $Q_{1t}^2+B_1^2=0$; it is never $1$ or $3$.
- In the degenerate case the two annihilators are distinct planes and their intersection, the two-sided annihilator, is the line $\mathbb{C}\tilde Q_1^{\natural}$.
- The zero divisors are the non-zero elements with $Q_{1t}^2+B_1^2=0$; they form a complex cone of complex dimension $3$, with the pure isotropic elements (the square-zero elements) as the subcone $Q_{1t}=0$ of complex dimension $2$.
- The units are the non-zero elements with a trivial annihilator, that is $Q_{1t}^2+B_1^2\neq0$; they are the complement of the zero-divisor cone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathrm{Ann}_r(\tilde Q_1)$ | the set of $\tilde Q_2$ with $\tilde Q_1\tilde Q_2=0$; the kernel of left multiplication |
| $\mathrm{Ann}_l(\tilde Q_1)$ | the set of $\tilde Q_2$ with $\tilde Q_2\tilde Q_1=0$; the kernel of right multiplication |
| $\mathrm{Ann}(\tilde Q_1)$ | the intersection of the two, the two-sided annihilator |
| $B_1^2=Q_{1x}^2+Q_{1y}^2+Q_{1z}^2$ | the square of the complex length of $\vec Q_1$ |
| $Q_{1t}^2+B_1^2=0$ | the degenerate condition, the zero-divisor criterion |

## Further Reading

- [The Element, the Coordinates and the Conjugations](the-element-the-coordinates-and-the-conjugations.html), for the product and the conjugate.
- [The Square of an Element](the-square-of-an-element.html), for the square and the pure isotropic case.
- [Nilpotents](nilpotents.html), for the pure family of the zero divisors.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra and the basis.
