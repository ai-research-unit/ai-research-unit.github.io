# __Square Roots of an Element__

## Introduction

This article solves the square-root problem in the biquaternion algebra $\mathbb{B}$: given $\tilde Q\in\mathbb{B}$, find every $\tilde{Ζ}\in\mathbb{B}$ with

$$
\tilde{Ζ}^2 = \tilde Q .
$$

The method needs no Clifford algebra, no norm and no form. It is the same vector–scalar split that solves the three central cases $\tilde{Ζ}^2=-1,0,+1$ in *Idempotents* and *Nilpotents*, carried one step further: the split turns the equation into one vector equation and one scalar equation, and the scalar equation is a quadratic in the square $x=Ζ_t^2$ of the scalar part of a root. The roots are then read off the solutions of that quadratic, and the answer is a finite set — generically four elements, falling to two — or a four-parameter family, or empty.

**The results.** For a radicand with non-vanishing vector part the roots come in pairs $\pm\tilde{Ζ}$: there are **four roots** generically, **two** in the two degenerate rows, and **none** for the rootless row $(\vec Q,\vec Q) = 0$, $n = 0$, $Q_t = 0$. For a complex scalar radicand $\tilde Q = Q_t e_t$ the roots are the two scalars $\pm\sqrt{Q_t}\,e_t$ together with a **four-parameter family** of pure $\vec{Ζ}$ with $(\vec{Ζ},\vec{Ζ}) = -Q_t$. The three central values recover the three sets of *Idempotents* and *Nilpotents*. Each case below states its answer first and then proves it.

The article is algebraic. The biquaternion algebra also carries a Clifford structure, treated in *Biquaternion Versors and the Orthogonal Group*; that structure is not used here. The three central values of *Idempotents* and *Nilpotents* are recovered as the case of a complex scalar $\tilde Q$, in §*The Three Central Values*, which checks this method against the direct computations of those articles. The zero-divisor cone, of which the nonzero roots of $0$ are a part, is *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*, named here only where the classification touches it. The polar and exponential decompositions that the answer must be consistent with are *The Polar Decomposition of an N-Regular Biquaternion*.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked.

Throughout, the quaternion basis is $e_t=1,\vec e_x,\vec e_y,\vec e_z$, the scalar imaginary is $i$, and a general biquaternion is $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with $Q_k\in\mathbb{C}$. The quaternion conjugate is $\tilde Q^{\natural}$, the complex conjugate is denoted $\bar{\tilde Q}$, and the Hermitian conjugate is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$.

The equation $\tilde{Ζ}^2=\tilde Q$ names a product, so the root is relative to it. The plain square $\tilde{Ζ}\tilde{Ζ}$ and the general definition with the roots of a central value are *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots*; throughout this article the square is the one of the general plain bilinear product $\tilde{Ζ}\tilde{Ζ}$, the multiplication of the biquaternion algebra, and the other three general products and their root problems are *Square Roots of a General Element in the General Plain Sesqualgebra*, *Square Roots of a General Element in the General Quaternionic Algebra* and *Square Roots of a General Element in the General Quaternionic Sesqualgebra*.

## The Reduction

Write the root and the radicand in scalar and vector parts,

$$
\tilde{Ζ} = Ζ_te_t + \vec{Ζ}, \qquad \vec{Ζ}=Ζ_x\vec e_x+Ζ_y\vec e_y+Ζ_z\vec e_z,
$$

$$
\tilde Q = Q_te_t + \vec Q, \qquad \vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,
$$

with all coefficients in $\mathbb{C}$. The product formula for biquaternions gives the square of $\tilde{Ζ}$ as

$$
\tilde{Ζ}^2 = \bigl(Ζ_t^2-(\vec{Ζ},\vec{Ζ})\bigr)e_t + 2Ζ_t\vec{Ζ}, \qquad (\vec{Ζ},\vec{Ζ})=Ζ_x^2+Ζ_y^2+Ζ_z^2 .
$$

Equating $\tilde{Ζ}^2$ to $\tilde Q$, component by component, splits the single equation into two:

$$
2Ζ_t\vec{Ζ} = \vec Q \qquad\text{(the vector part)},
$$

$$
Ζ_t^2-(\vec{Ζ},\vec{Ζ}) = Q_t \qquad\text{(the scalar part)} .
$$

The vector equation involves only the vector part $\vec Q$ of the radicand, and it decides the shape of the answer. It has two outcomes.

**Case A — the radicand has non-vanishing vector part ($\vec Q\neq0$).** Then $Ζ_t\neq0$ and $\vec{Ζ}=\vec Q/(2Ζ_t)$: a root is fixed by its scalar part, and the problem collapses onto the scalar equation. This case is §*The Roots with Non-Vanishing Vector Part*.

**Case B — the radicand is a complex scalar ($\vec Q=0$).** Then $2Ζ_t\vec{Ζ}=0$, which forces $\vec{Ζ}=0$ or $Ζ_t=0$: a root is either a complex scalar or pure. This case is §*The Roots of a Complex Scalar*.

Two data are used throughout. The **complex square of the vector part** is

$$
(\vec Q,\vec Q) = Q_x^2+Q_y^2+Q_z^2 ,
$$

and the **conjugate scalar** is

$$
n = Q_t^2+Q_x^2+Q_y^2+Q_z^2 = Q_t^2+(\vec Q,\vec Q) .
$$

The conjugate scalar is not a norm here: it is the algebraic identity

$$
\tilde Q\tilde Q^{\natural} = \bigl(Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr)e_t = n\,e_t ,
$$

in which $\tilde Q^{\natural}$ is the quaternion conjugate. This uses only the product and the conjugate, both of which the algebra carries before any form is introduced.

## The Roots with Non-Vanishing Vector Part

**For a radicand with non-vanishing vector part the roots come in opposite pairs $\pm\tilde{Ζ}$: four roots when $(\vec Q,\vec Q)\neq0$ and $n\neq0$, two roots in the two degenerate rows, and none when $(\vec Q,\vec Q)=0$, $n=0$ and $Q_t=0$.**

Assume $\vec Q\neq0$. Then $2Ζ_t\vec{Ζ}=\vec Q$ forces $Ζ_t\neq0$, and the vector equation determines the vector part of every root,

$$
\vec{Ζ} = \frac{\vec Q}{2Ζ_t} .
$$

Substituting this into the scalar equation gives

$$
Ζ_t^2-\frac{(\vec Q,\vec Q)}{4Ζ_t^2} = Q_t .
$$

Put

$$
x = Ζ_t^2 .
$$

Since $(\vec Q/(2Ζ_t),\vec Q/(2Ζ_t)) = (\vec Q,\vec Q)/(4x)$, the scalar equation becomes the **reduced quadratic**

$$
4x^2 - 4Q_tx - (\vec Q,\vec Q) = 0 .
$$

Its discriminant is

$$
16Q_t^2 + 16(\vec Q,\vec Q) = 16n ,
$$

so its two solutions are

$$
\boxed{\;
x_+ = \frac{Q_t+\sqrt{n}}{2}, \qquad x_- = \frac{Q_t-\sqrt{n}}{2}
\;},
$$

where $\sqrt{n}$ is either square root of the complex number $n$; the choice of square root only exchanges $x_+$ and $x_-$.

**Proposition (the roots with non-vanishing vector part).** Let $\vec Q\neq0$, and let $x_+$ and $x_-$ be the two solutions of the reduced quadratic. For each solution $x\in\{x_+,x_-\}$ with $x\neq0$, and for each of the two square roots $Ζ_t=\pm\sqrt{x}$, the element

$$
\boxed{\;
\tilde{Ζ} = Ζ_te_t + \frac{\vec Q}{2Ζ_t}
\;}
$$

is a square root of $\tilde Q$, and every square root of $\tilde Q$ with $\vec Q\neq0$ arises this way.

**Proof.** The derivation above shows that a root with $\vec Q\neq0$ has $Ζ_t\neq0$, has $\vec{Ζ}=\vec Q/(2Ζ_t)$, and has $x=Ζ_t^2$ solving the reduced quadratic. Conversely, given such an $x$ and $Ζ_t=\pm\sqrt{x}\neq0$, the two equations hold by construction, so $\tilde{Ζ}^2=\tilde Q$. The two values $Ζ_t=+\sqrt{x}$ and $Ζ_t=-\sqrt{x}$ give opposite roots, so each nonzero solution contributes the pair $\pm\tilde{Ζ}$.

**Corollary (the number of roots).** The solution $x=0$ occurs if and only if $(\vec Q,\vec Q)=0$, since the quadratic reads $-(\vec Q,\vec Q)=0$ at $x=0$. Hence there are **four roots** when $(\vec Q,\vec Q)\neq0$ and $n\neq0$, the two solutions being then distinct and nonzero; **two roots** when $(\vec Q,\vec Q)\neq0$ and $n=0$, the quadratic having the double nonzero solution $x=Q_t/2$; **two roots** when $(\vec Q,\vec Q)=0$ and $Q_t\neq0$, the solutions being $0$ and $Q_t$ and only $x=Q_t$ contributing; and **no roots** when $(\vec Q,\vec Q)=0$ and $Q_t=0$, the only solution being $x=0$.

## The Roots of a Complex Scalar

**For a complex scalar radicand $\tilde Q = Q_t e_t$ the roots are the two scalars $\pm\sqrt{Q_t}\,e_t$ together with the four-parameter family of pure $\vec{Ζ}$ with $(\vec{Ζ},\vec{Ζ}) = -Q_t$.**

Assume $\vec Q=0$, so that $\tilde Q=Q_te_t$ lies in the centre $\mathbb{C}e_t$. The vector equation is $2Ζ_t\vec{Ζ}=0$, and since $\mathbb{C}$ is a field this forces $\vec{Ζ}=0$ or $Ζ_t=0$. The two sub-cases are disjoint and exhaustive.

**Sub-case 1 — the root is a complex scalar ($\vec{Ζ}=0$).** Then $\tilde{Ζ}=Ζ_te_t$ and the scalar equation reduces to $Ζ_t^2=Q_t$. **The roots in this case are the two elements**

$$
\tilde{Ζ} = +\sqrt{Q_t}\,e_t, \qquad \tilde{Ζ} = -\sqrt{Q_t}\,e_t,
$$

which coincide as the single root $\tilde{Ζ}=0$ when $Q_t=0$.

**Sub-case 2 — the root is pure ($Ζ_t=0$).** Then $\tilde{Ζ}=\vec{Ζ}=Ζ_x\vec e_x+Ζ_y\vec e_y+Ζ_z\vec e_z$ and the scalar equation reduces to

$$
(\vec{Ζ},\vec{Ζ}) = Ζ_x^2+Ζ_y^2+Ζ_z^2 = -Q_t .
$$

**The roots in this case are the pure biquaternions of complex square $-Q_t$.** Writing $Ζ_k=\zeta_k+i\zeta'_k$ with $\zeta_k,\zeta'_k\in\mathbb{R}$, the condition is the pair of real equations

$$
\zeta_x^2+\zeta_y^2+\zeta_z^2-(\zeta'_x)^2-(\zeta'_y)^2-(\zeta'_z)^2 = -\operatorname{Re}Q_t, \qquad \zeta_x\zeta'_x+\zeta_y\zeta'_y+\zeta_z\zeta'_z = -\tfrac12\operatorname{Im}Q_t,
$$

six real coefficients carrying two constraints, hence a **four-real-parameter family**. For $Q_t\neq0$ the family is nonempty: taking $Ζ_y=Ζ_z=0$ leaves $Ζ_x^2=-Q_t$, which is solved by $Ζ_x=\sqrt{-Q_t}$. For $Q_t=0$ the family is the **pure null cone** $(\vec{Ζ},\vec{Ζ})=0$, whose nonzero elements are the nilpotents.

So when $\vec Q=0$ the root set is the two complex scalars $\pm\sqrt{Q_t}e_t$ — one element when $Q_t=0$ — together with this four-real-parameter family.

## The Classification

**Every radicand falls into exactly one of the rows below: four roots generically, two roots in the two degenerate rows, no roots for the rootless row, and a four-parameter family for a complex scalar.**

Collecting the two cases, every $\tilde Q\in\mathbb{B}$ falls into exactly one of the following rows.

| condition on $\tilde Q=Q_te_t+\vec Q$ | number of roots |
|---|---|
| $\vec Q\neq0$, $(\vec Q,\vec Q)\neq0$, $n\neq0$ | four |
| $\vec Q\neq0$, $(\vec Q,\vec Q)\neq0$, $n=0$ | two |
| $\vec Q\neq0$, $(\vec Q,\vec Q)=0$, $Q_t\neq0$ | two |
| $\vec Q\neq0$, $n=0$, $Q_t=0$ | none |
| $\vec Q=0$ | a four-parameter family |

The generic case is four roots. The complex square $(\vec Q,\vec Q)$ of the vector part decides whether a solution $x$ is lost at $x=0$; the conjugate scalar $n$ decides whether the two solutions of the reduced quadratic are distinct; and the vector part $\vec Q$ itself decides which of the two cases applies.

**The roots in each case.** Reading the same rows:

**No roots.** If $\vec Q\neq0$, $n=0$ and $Q_t=0$, then $\tilde Q$ has no square root and the root set is $\varnothing$.

**Two roots.** If $\vec Q\neq0$ and either $(\vec Q,\vec Q)\neq0$ and $n=0$, or $(\vec Q,\vec Q)=0$ and $Q_t\neq0$, then the root set is a single pair $\tilde{Ζ}=\pm\bigl(\sqrt{x}\,e_t+\vec Q/(2\sqrt{x})\bigr)$, with $x=Q_t/2$ in the first instance and $x=Q_t$ in the second.

**Four roots.** If $\vec Q\neq0$, $(\vec Q,\vec Q)\neq0$ and $n\neq0$, then the root set is two pairs, one for each solution of the reduced quadratic:

$$
\boxed{\;
\tilde{Ζ} = \pm\Bigl(\sqrt{x_+}\,e_t+\frac{\vec Q}{2\sqrt{x_+}}\Bigr), \qquad \tilde{Ζ} = \pm\Bigl(\sqrt{x_-}\,e_t+\frac{\vec Q}{2\sqrt{x_-}}\Bigr)
\;}.
$$

**A complex scalar.** If $\tilde Q$ is a complex scalar, $\tilde Q=Q_te_t$, then the root set is the two elements $\pm\sqrt{Q_t}e_t$ together with the four-real-parameter family of pure $\vec{Ζ}$ with $(\vec{Ζ},\vec{Ζ})=-Q_t$.

## The Three Central Values

**The three central values reproduce the three sets of the companion articles: the roots of $-1$ and of $+1$ in the first, the roots of $0$ in the second.**

The classification specialises to the three central values $\tilde Q=-1,0,+1$ of the companion articles *Idempotents* and *Nilpotents*, and reproduces them; the agreement is the check that this method and the direct computations of those articles are the same computation.

**$\tilde Q=-e_t$ ($Q_t=-1$, $\vec Q=0$).** A complex scalar, so the complex-scalar case. The scalar roots are $\pm\sqrt{-1}\,e_t=\pm ie_t$, the trivial roots of the companion articles. The family is $(\vec{Ζ},\vec{Ζ})=1$, that is $\zeta_x^2+\zeta_y^2+\zeta_z^2-(\zeta'_x)^2-(\zeta'_y)^2-(\zeta'_z)^2=1$ and $\zeta_x\zeta'_x+\zeta_y\zeta'_y+\zeta_z\zeta'_z=0$, which is exactly the pure roots of $-1$: the real roots are the members with $\vec\zeta'=0$, and the non-trivial roots are the members with $\vec\zeta'\neq0$.

**$\tilde Q=0$ ($Q_t=0$, $\vec Q=0$).** The scalar roots are the single element $\tilde{Ζ}=0$. The family is the pure null cone $(\vec{Ζ},\vec{Ζ})=0$, whose nonzero elements are the nilpotents of the algebra; its structure is *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*.

**$\tilde Q=+e_t$ ($Q_t=+1$, $\vec Q=0$).** The scalar roots are $\pm e_t$. The family is $(\vec{Ζ},\vec{Ζ})=-1$: in the notation of the companion articles a member is $\vec{Ζ}=\vec\zeta+i\vec\zeta'$, and its two real conditions, $\zeta_x^2+\zeta_y^2+\zeta_z^2-(\zeta'_x)^2-(\zeta'_y)^2-(\zeta'_z)^2=1$ and $\zeta_x\zeta'_x+\zeta_y\zeta'_y+\zeta_z\zeta'_z=0$, are exactly the conditions on the corresponding root of $-1$. These are the non-trivial roots of $+1$.

The three sets are therefore the degenerate data of the general classification, and this article is where the four-root and two-root cases live.

## Worked Examples

The examples are computed with the classification and verified by squaring; the verification is the multiplication check $\tilde{Ζ}^2=\tilde Q$.

**A pure imaginary quaternion.** For $\tilde Q=-i\vec e_z$ (that is $-Ik$ in the notation of Acus and Dargys) the vector part is $\vec Q=-i\vec e_z$, with $(\vec Q,\vec Q)=(-i)^2=-1$ and $n=-1$. Both are nonzero, so there are four roots, from $x_\pm=\pm\sqrt{-1}/2=\pm i/2$. Taking $x_+=i/2$ and $Ζ_t=(1+i)/2$ gives $\vec{Ζ}=\vec Q/(2Ζ_t)=-\tfrac{1+i}{2}\vec e_z$ and the pair $\pm\tfrac{1+i}{2}(e_t-\vec e_z)$; taking $x_-=-i/2$ and $Ζ_t=(1-i)/2$ gives $\vec{Ζ}=\tfrac{1-i}{2}\vec e_z$ and the pair $\pm\tfrac{1-i}{2}(e_t+\vec e_z)$. The four roots are

$$
\tilde{Ζ} = \pm\tfrac{1+i}{2}\bigl(e_t-\vec e_z\bigr), \qquad \tilde{Ζ} = \pm\tfrac{1-i}{2}\bigl(e_t+\vec e_z\bigr),
$$

in agreement with the roots of $-i\vec e_z$ computed directly, and with the source's $\sqrt{-Ik}$.

**A complex scalar.** For $\tilde Q=-1+i$ (that is $-1+I$) the radicand is a complex scalar with $Q_t=-1+i$, so the row is the four-parameter one. The isolated roots are $\pm\sqrt{-1+i}\,e_t$. Since

$$
\sqrt{-1+i} = \sqrt{\tfrac{\sqrt2-1}{2}} + i\sqrt{\tfrac{\sqrt2+1}{2}},
$$

the isolated roots are

$$
\tilde{Ζ} = \pm\Bigl(\sqrt{\tfrac{\sqrt2-1}{2}} + i\sqrt{\tfrac{\sqrt2+1}{2}}\Bigr)e_t,
$$

and the family is $(\vec{Ζ},\vec{Ζ})=1-i$, that is $\zeta_x^2+\zeta_y^2+\zeta_z^2-(\zeta'_x)^2-(\zeta'_y)^2-(\zeta'_z)^2=1$ and $\zeta_x\zeta'_x+\zeta_y\zeta'_y+\zeta_z\zeta'_z=-\tfrac12$. Squaring the displayed root gives $-1+i$.

**A rootless element.** For $\tilde Q=\vec e_x-i\vec e_z$ (that is $i-Ik$) the vector part is $\vec Q=\vec e_x-i\vec e_z$, with $(\vec Q,\vec Q)=1+(-i)^2=0$ and $n=0$. The row is the rootless one, and $\tilde Q$ has no square root. The element is itself a nilpotent,

$$
(\vec e_x-i\vec e_z)^2 = \vec e_x^2+(-i)^2\vec e_z^2-i\bigl(\vec e_x \vec e_z+\vec e_z \vec e_x\bigr) = -1+1+0 = 0 .
$$

This is the example of Acus and Dargys.

**Four roots of a non-scalar.** For $\tilde Q=-(2+i)\vec e_z$ (that is $-(2+I)k$) the vector part is $\vec Q=-(2+i)\vec e_z$, with $(\vec Q,\vec Q)=(2+i)^2=3+4i$ and $n=3+4i$, both nonzero, so there are four roots. Since $\sqrt{3+4i}=2+i$, the two solutions are $x_\pm=\pm\tfrac{2+i}{2}$, and the four roots are

$$
\tilde{Ζ} = \pm\bigl(1.0291+0.2429\,i\bigr)\bigl(e_t-\vec e_z\bigr), \qquad \tilde{Ζ} = \pm\bigl(0.2429-1.0291\,i\bigr)\bigl(e_t+\vec e_z\bigr),
$$

whose squares are $-(2+i)\vec e_z$; the second pair is the first multiplied by $-i$, with $e_t-\vec e_z$ exchanged for $e_t+\vec e_z$.

**A nilpotent root of $0$.** For $\tilde Q=0$ the scalar root is $\tilde{Ζ}=0$ and the family is the pure null cone; $\tilde{Ζ}=\vec e_x+i\vec e_y$ is one of its members, with

$$
(\vec e_x+i\vec e_y)^2 = \vec e_x^2+i^2\vec e_y^2+i\bigl(\vec e_x \vec e_y+\vec e_y \vec e_x\bigr) = -1+1+0 = 0 .
$$

## Summary

For a general $\tilde Q\in\mathbb{B}$ the square roots are found from the vector–scalar split $\tilde Q=Q_te_t+\vec Q$ and $\tilde{Ζ}=Ζ_te_t+\vec{Ζ}$, which turns $\tilde{Ζ}^2=\tilde Q$ into the vector equation $2Ζ_t\vec{Ζ}=\vec Q$ and the scalar equation $Ζ_t^2-(\vec{Ζ},\vec{Ζ})=Q_t$.

When $\vec Q\neq0$, a root has $Ζ_t\neq0$ and $\vec{Ζ}=\vec Q/(2Ζ_t)$, and $x=Ζ_t^2$ solves the reduced quadratic $4x^2-4Q_tx-(\vec Q,\vec Q)=0$, whose discriminant is $16n$ with $n=Q_t^2+(\vec Q,\vec Q)$; each nonzero solution $x$ contributes the pair $\tilde{Ζ}=\pm\bigl(\sqrt{x}\,e_t+\vec Q/(2\sqrt{x})\bigr)$.

When $\vec Q=0$, the radicand is a complex scalar and the roots are the two elements $\pm\sqrt{Q_t}e_t$ (one when $Q_t=0$) together with the four-real-parameter family of pure $\vec{Ζ}$ with $(\vec{Ζ},\vec{Ζ})=-Q_t$.

The number of roots is: **four** when $(\vec Q,\vec Q)\neq0$ and $n\neq0$; **two** when $(\vec Q,\vec Q)\neq0$ and $n=0$, or when $(\vec Q,\vec Q)=0$ and $Q_t\neq0$; **none** when $n=0$ and $Q_t=0$ with $\vec Q\neq0$; and the **four-parameter family** when and only when $\tilde Q$ is a complex scalar.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\tilde Q$ | The element whose square roots are sought |
| $\tilde{Ζ}$ | A square root of $\tilde Q$ |
| $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | Vector part of $\tilde Q$ |
| $(\vec Q,\vec Q)=Q_x^2+Q_y^2+Q_z^2$ | Complex square of the vector part |
| $n=Q_t^2+(\vec Q,\vec Q)$ | The scalar of $\tilde Q\tilde Q^{\natural}=ne_t$ |
| $x=Ζ_t^2$ | Square of the scalar part of a root |
| $x_\pm=\tfrac12\bigl(Q_t\pm\sqrt{n}\bigr)$ | The two solutions of the reduced quadratic |

## Further Reading

- [Idempotents](idempotents.html), for the case $\tilde Q=+e_t$, the idempotents and their geometry.
- [Nilpotents](nilpotents.html), for the case $\tilde Q=0$ and the nilpotent cone.
- [Peirce Decompositions of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the Peirce decomposition attached to a root of $+1$.
- [Square Roots of a General Element in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space](square-roots-of-a-general-element-in-the-algebraic-structures-over-the-biquaternion-c-space.html), for the same problem read in all twelve products.
- A. Acus and A. Dargys, *Square roots of complexified quaternions*, arXiv:2601.08391 (2026), for the square-root problem of complexified quaternions and the worked examples reproduced here.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the central case.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the nilpotent cone.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic properties of the biquaternions.
