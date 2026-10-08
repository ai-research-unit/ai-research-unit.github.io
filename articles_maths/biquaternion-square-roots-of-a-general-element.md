# __Biquaternion Square Roots of a General Element__

## Introduction

This article solves the square-root problem in the biquaternion algebra $\mathbb{B}$: given $\tilde Q\in\mathbb{B}$, find every $\tilde P\in\mathbb{B}$ with

$$
\tilde P^2 = \tilde Q .
$$

The method needs no Clifford algebra, no norm and no form. It is the same vector–scalar split that solves the three central cases $\tilde P^2=-1,0,+1$ in *Biquaternion Square Roots of Minus One, Zero and Plus One*, carried one step further: the split turns the equation into one vector equation and one scalar equation, and the scalar equation is a quadratic in the square $x=P_0^2$ of the scalar part of a root. The roots are then read off the solutions of that quadratic, and the answer is a finite set — generically four elements, falling to two — or a four-parameter family, or empty.

The article is algebraic. The biquaternion algebra also carries a Clifford structure, treated in *The Clifford Algebra Representation*; that structure is not used here. The three central values of *Biquaternion Square Roots of Minus One, Zero and Plus One* are recovered as the case of a complex scalar $\tilde Q$, in §*The Three Central Values*, which checks this method against the direct computation of that article. The zero-divisor cone, of which the nonzero roots of $0$ are a part, is *Biquaternion Zero Divisors*, named here only where the classification touches it. The polar and exponential decompositions that the answer must be consistent with are *Biquaternion Polar Element Representation*.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked.

Throughout, the quaternion basis is $e_0=1,e_1,e_2,e_3$, the scalar imaginary is $i$, and a general biquaternion is $\tilde Q=Q_0e_0+Q_1e_1+Q_2e_2+Q_3e_3$ with $Q_k\in\mathbb{C}$. The quaternion conjugate is $\tilde Q^{\natural}$, the complex conjugate is denoted $\bar{\tilde Q}$, and the Hermitian conjugate is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$.

## The Reduction

Write the root and the radicand in scalar and vector parts,

$$
\tilde P = P_0e_0 + \boldsymbol{P}, \qquad \boldsymbol{P}=P_1e_1+P_2e_2+P_3e_3,
$$

$$
\tilde Q = Q_0e_0 + \boldsymbol{Q}, \qquad \boldsymbol{Q}=Q_1e_1+Q_2e_2+Q_3e_3,
$$

with all coefficients in $\mathbb{C}$. The product formula for biquaternions gives the square of $\tilde P$ as

$$
\tilde P^2 = \bigl(P_0^2-(\boldsymbol{P},\boldsymbol{P})\bigr)e_0 + 2P_0\boldsymbol{P}, \qquad (\boldsymbol{P},\boldsymbol{P})=P_1^2+P_2^2+P_3^2 .
$$

Equating $\tilde P^2$ to $\tilde Q$, component by component, splits the single equation into two:

$$
2P_0\boldsymbol{P} = \boldsymbol{Q} \qquad\text{(the vector part)},
$$

$$
P_0^2-(\boldsymbol{P},\boldsymbol{P}) = Q_0 \qquad\text{(the scalar part)} .
$$

The vector equation involves only the vector part $\boldsymbol{Q}$ of the radicand, and it decides the shape of the answer. It has two outcomes.

**Case A — the radicand has non-vanishing vector part ($\boldsymbol{Q}\neq0$).** Then $P_0\neq0$ and $\boldsymbol{P}=\boldsymbol{Q}/(2P_0)$: a root is fixed by its scalar part, and the problem collapses onto the scalar equation. This case is §*The Roots with Non-Vanishing Vector Part*.

**Case B — the radicand is a complex scalar ($\boldsymbol{Q}=0$).** Then $2P_0\boldsymbol{P}=0$, which forces $\boldsymbol{P}=0$ or $P_0=0$: a root is either a complex scalar or pure. This case is §*The Roots of a Complex Scalar*.

Two data are used throughout. The **complex square of the vector part** is

$$
(\boldsymbol{Q},\boldsymbol{Q}) = Q_1^2+Q_2^2+Q_3^2 ,
$$

and the **conjugate scalar** is

$$
n = Q_0^2+Q_1^2+Q_2^2+Q_3^2 = Q_0^2+(\boldsymbol{Q},\boldsymbol{Q}) .
$$

The conjugate scalar is not a norm here: it is the algebraic identity

$$
\tilde Q\tilde Q^{\natural} = \bigl(Q_0^2+Q_1^2+Q_2^2+Q_3^2\bigr)e_0 = n\,e_0 ,
$$

in which $\tilde Q^{\natural}$ is the quaternion conjugate. This uses only the product and the conjugate, both of which the algebra carries before any form is introduced.

## The Roots with Non-Vanishing Vector Part

Assume $\boldsymbol{Q}\neq0$. Then $2P_0\boldsymbol{P}=\boldsymbol{Q}$ forces $P_0\neq0$, and the vector equation determines the vector part of every root,

$$
\boldsymbol{P} = \frac{\boldsymbol{Q}}{2P_0} .
$$

Substituting this into the scalar equation gives

$$
P_0^2-\frac{(\boldsymbol{Q},\boldsymbol{Q})}{4P_0^2} = Q_0 .
$$

Put

$$
x = P_0^2 .
$$

Since $(\boldsymbol{Q}/(2P_0),\boldsymbol{Q}/(2P_0)) = (\boldsymbol{Q},\boldsymbol{Q})/(4x)$, the scalar equation becomes the **reduced quadratic**

$$
4x^2 - 4Q_0x - (\boldsymbol{Q},\boldsymbol{Q}) = 0 .
$$

Its discriminant is

$$
16Q_0^2 + 16(\boldsymbol{Q},\boldsymbol{Q}) = 16n ,
$$

so its two solutions are

$$
x_+ = \frac{Q_0+\sqrt{n}}{2}, \qquad x_- = \frac{Q_0-\sqrt{n}}{2},
$$

where $\sqrt{n}$ is either square root of the complex number $n$; the choice of square root only exchanges $x_+$ and $x_-$.

**Proposition (the roots with non-vanishing vector part).** Let $\boldsymbol{Q}\neq0$, and let $x_+$ and $x_-$ be the two solutions of the reduced quadratic. For each solution $x\in\{x_+,x_-\}$ with $x\neq0$, and for each of the two square roots $P_0=\pm\sqrt{x}$, the element

$$
\tilde P = P_0e_0 + \frac{\boldsymbol{Q}}{2P_0}
$$

is a square root of $\tilde Q$, and every square root of $\tilde Q$ with $\boldsymbol{Q}\neq0$ arises this way.

**Proof.** The derivation above shows that a root with $\boldsymbol{Q}\neq0$ has $P_0\neq0$, has $\boldsymbol{P}=\boldsymbol{Q}/(2P_0)$, and has $x=P_0^2$ solving the reduced quadratic. Conversely, given such an $x$ and $P_0=\pm\sqrt{x}\neq0$, the two equations hold by construction, so $\tilde P^2=\tilde Q$. The two values $P_0=+\sqrt{x}$ and $P_0=-\sqrt{x}$ give opposite roots, so each nonzero solution contributes the pair $\pm\tilde P$. $\square$

**Corollary (the number of roots).** The solution $x=0$ occurs if and only if $(\boldsymbol{Q},\boldsymbol{Q})=0$, since the quadratic reads $-(\boldsymbol{Q},\boldsymbol{Q})=0$ at $x=0$. Hence there are **four roots** when $(\boldsymbol{Q},\boldsymbol{Q})\neq0$ and $n\neq0$, the two solutions being then distinct and nonzero; **two roots** when $(\boldsymbol{Q},\boldsymbol{Q})\neq0$ and $n=0$, the quadratic having the double nonzero solution $x=Q_0/2$; **two roots** when $(\boldsymbol{Q},\boldsymbol{Q})=0$ and $Q_0\neq0$, the solutions being $0$ and $Q_0$ and only $x=Q_0$ contributing; and **no roots** when $(\boldsymbol{Q},\boldsymbol{Q})=0$ and $Q_0=0$, the only solution being $x=0$.

## The Roots of a Complex Scalar

Assume $\boldsymbol{Q}=0$, so that $\tilde Q=Q_0e_0$ lies in the centre $\mathbb{C}e_0$. The vector equation is $2P_0\boldsymbol{P}=0$, and since $\mathbb{C}$ is a field this forces $\boldsymbol{P}=0$ or $P_0=0$. The two sub-cases are disjoint and exhaustive.

**Sub-case 1 — the root is a complex scalar ($\boldsymbol{P}=0$).** Then $\tilde P=P_0e_0$ and the scalar equation reduces to $P_0^2=Q_0$. **The roots in this case are the two elements**

$$
\tilde P = +\sqrt{Q_0}\,e_0, \qquad \tilde P = -\sqrt{Q_0}\,e_0,
$$

which coincide as the single root $\tilde P=0$ when $Q_0=0$.

**Sub-case 2 — the root is pure ($P_0=0$).** Then $\tilde P=\boldsymbol{P}=P_1e_1+P_2e_2+P_3e_3$ and the scalar equation reduces to

$$
(\boldsymbol{P},\boldsymbol{P}) = P_1^2+P_2^2+P_3^2 = -Q_0 .
$$

**The roots in this case are the pure biquaternions of complex square $-Q_0$.** Writing $P_k=p_k+ip'_k$ with $p_k,p'_k\in\mathbb{R}$, the condition is the pair of real equations

$$
p_1^2+p_2^2+p_3^2-p_1'^2-p_2'^2-p_3'^2 = -\operatorname{Re}Q_0, \qquad p_1p'_1+p_2p'_2+p_3p'_3 = -\tfrac12\operatorname{Im}Q_0,
$$

six real coefficients carrying two constraints, hence a **four-real-parameter family**. For $Q_0\neq0$ the family is nonempty: taking $P_2=P_3=0$ leaves $P_1^2=-Q_0$, which is solved by $P_1=\sqrt{-Q_0}$. For $Q_0=0$ the family is the **pure null cone** $(\boldsymbol{P},\boldsymbol{P})=0$, whose nonzero elements are the nilpotents.

So when $\boldsymbol{Q}=0$ the root set is the two complex scalars $\pm\sqrt{Q_0}e_0$ — one element when $Q_0=0$ — together with this four-real-parameter family.

## The Classification

Collecting the two cases, every $\tilde Q\in\mathbb{B}$ falls into exactly one of the following rows.

| condition on $\tilde Q=Q_0e_0+\boldsymbol{Q}$ | number of roots |
|---|---|
| $\boldsymbol{Q}\neq0$, $(\boldsymbol{Q},\boldsymbol{Q})\neq0$, $n\neq0$ | four |
| $\boldsymbol{Q}\neq0$, $(\boldsymbol{Q},\boldsymbol{Q})\neq0$, $n=0$ | two |
| $\boldsymbol{Q}\neq0$, $(\boldsymbol{Q},\boldsymbol{Q})=0$, $Q_0\neq0$ | two |
| $\boldsymbol{Q}\neq0$, $n=0$, $Q_0=0$ | none |
| $\boldsymbol{Q}=0$ | a four-parameter family |

The generic case is four roots. The complex square $(\boldsymbol{Q},\boldsymbol{Q})$ of the vector part decides whether a solution $x$ is lost at $x=0$; the conjugate scalar $n$ decides whether the two solutions of the reduced quadratic are distinct; and the vector part $\boldsymbol{Q}$ itself decides which of the two cases applies.

**The roots in each case.** Reading the same rows:

**No roots.** If $\boldsymbol{Q}\neq0$, $n=0$ and $Q_0=0$, then $\tilde Q$ has no square root and the root set is $\varnothing$.

**Two roots.** If $\boldsymbol{Q}\neq0$ and either $(\boldsymbol{Q},\boldsymbol{Q})\neq0$ and $n=0$, or $(\boldsymbol{Q},\boldsymbol{Q})=0$ and $Q_0\neq0$, then the root set is a single pair $\tilde P=\pm\bigl(\sqrt{x}\,e_0+\boldsymbol{Q}/(2\sqrt{x})\bigr)$, with $x=Q_0/2$ in the first instance and $x=Q_0$ in the second.

**Four roots.** If $\boldsymbol{Q}\neq0$, $(\boldsymbol{Q},\boldsymbol{Q})\neq0$ and $n\neq0$, then the root set is two pairs, one for each solution of the reduced quadratic:

$$
\tilde P = \pm\Bigl(\sqrt{x_+}\,e_0+\frac{\boldsymbol{Q}}{2\sqrt{x_+}}\Bigr), \qquad \tilde P = \pm\Bigl(\sqrt{x_-}\,e_0+\frac{\boldsymbol{Q}}{2\sqrt{x_-}}\Bigr).
$$

**A complex scalar.** If $\tilde Q$ is a complex scalar, $\tilde Q=Q_0e_0$, then the root set is the two elements $\pm\sqrt{Q_0}e_0$ together with the four-real-parameter family of pure $\boldsymbol{P}$ with $(\boldsymbol{P},\boldsymbol{P})=-Q_0$.

## The Three Central Values

The classification specialises to the three central values $\tilde Q=-1,0,+1$ of *Biquaternion Square Roots of Minus One, Zero and Plus One* and reproduces them; the agreement is the check that this method and the direct computation of that article are the same computation.

**$\tilde Q=-e_0$ ($Q_0=-1$, $\boldsymbol{Q}=0$).** A complex scalar, so the complex-scalar case. The scalar roots are $\pm\sqrt{-1}\,e_0=\pm ie_0$, the trivial roots of the companion article. The family is $(\boldsymbol{P},\boldsymbol{P})=1$, that is $p_1^2+p_2^2+p_3^2-p_1'^2-p_2'^2-p_3'^2=1$ and $p_1p'_1+p_2p'_2+p_3p'_3=0$, which is exactly the pure roots of $-1$: the real roots are the members with $\boldsymbol{p}'=0$, and the non-trivial roots are the members with $\boldsymbol{p}'\neq0$.

**$\tilde Q=0$ ($Q_0=0$, $\boldsymbol{Q}=0$).** The scalar roots are the single element $\tilde P=0$. The family is the pure null cone $(\boldsymbol{P},\boldsymbol{P})=0$, whose nonzero elements are the nilpotents of the algebra; its structure is *Biquaternion Zero Divisors*.

**$\tilde Q=+e_0$ ($Q_0=+1$, $\boldsymbol{Q}=0$).** The scalar roots are $\pm e_0$. The family is $(\boldsymbol{P},\boldsymbol{P})=-1$: in the notation of the companion article a member is $\boldsymbol{P}=\boldsymbol{p}i-\boldsymbol{p}'$, and its two real conditions, $p_1^2+p_2^2+p_3^2-p_1'^2-p_2'^2-p_3'^2=1$ and $p_1p'_1+p_2p'_2+p_3p'_3=0$, are exactly the conditions on the corresponding root of $-1$. These are the non-trivial roots of $+1$.

The three sets are therefore the degenerate data of the general classification, and this article is where the four-root and two-root cases live.

## Worked Examples

The examples are computed with the classification and verified by squaring; the verification is the multiplication check $\tilde P^2=\tilde Q$.

**A pure imaginary quaternion.** For $\tilde Q=-ie_3$ (that is $-Ik$ in the notation of Acus and Dargys) the vector part is $\boldsymbol{Q}=-ie_3$, with $(\boldsymbol{Q},\boldsymbol{Q})=(-i)^2=-1$ and $n=-1$. Both are nonzero, so there are four roots, from $x_\pm=\pm\sqrt{-1}/2=\pm i/2$. Taking $x_+=i/2$ and $P_0=(1+i)/2$ gives $\boldsymbol{P}=\boldsymbol{Q}/(2P_0)=-\tfrac{1+i}{2}e_3$ and the pair $\pm\tfrac{1+i}{2}(e_0-e_3)$; taking $x_-=-i/2$ and $P_0=(1-i)/2$ gives $\boldsymbol{P}=\tfrac{1-i}{2}e_3$ and the pair $\pm\tfrac{1-i}{2}(e_0+e_3)$. The four roots are

$$
\tilde P = \pm\tfrac{1+i}{2}\bigl(e_0-e_3\bigr), \qquad \tilde P = \pm\tfrac{1-i}{2}\bigl(e_0+e_3\bigr),
$$

in agreement with the roots of $-ie_3$ computed directly, and with the source's $\sqrt{-Ik}$.

**A complex scalar.** For $\tilde Q=-1+i$ (that is $-1+I$) the radicand is a complex scalar with $Q_0=-1+i$, so the row is the four-parameter one. The isolated roots are $\pm\sqrt{-1+i}\,e_0$. Since

$$
\sqrt{-1+i} = \sqrt{\tfrac{\sqrt2-1}{2}} + i\sqrt{\tfrac{\sqrt2+1}{2}},
$$

the isolated roots are

$$
\tilde P = \pm\Bigl(\sqrt{\tfrac{\sqrt2-1}{2}} + i\sqrt{\tfrac{\sqrt2+1}{2}}\Bigr)e_0,
$$

and the family is $(\boldsymbol{P},\boldsymbol{P})=1-i$, that is $p_1^2+p_2^2+p_3^2-p_1'^2-p_2'^2-p_3'^2=1$ and $p_1p'_1+p_2p'_2+p_3p'_3=-\tfrac12$. Squaring the displayed root gives $-1+i$.

**A rootless element.** For $\tilde Q=e_1-ie_3$ (that is $i-Ik$) the vector part is $\boldsymbol{Q}=e_1-ie_3$, with $(\boldsymbol{Q},\boldsymbol{Q})=1+(-i)^2=0$ and $n=0$. The row is the rootless one, and $\tilde Q$ has no square root. The element is itself a nilpotent,

$$
(e_1-ie_3)^2 = e_1^2+(-i)^2e_3^2-i\bigl(e_1e_3+e_3e_1\bigr) = -1+1+0 = 0 .
$$

This is the example of Acus and Dargys.

**Four roots of a non-scalar.** For $\tilde Q=-(2+i)e_3$ (that is $-(2+I)k$) the vector part is $\boldsymbol{Q}=-(2+i)e_3$, with $(\boldsymbol{Q},\boldsymbol{Q})=(2+i)^2=3+4i$ and $n=3+4i$, both nonzero, so there are four roots. Since $\sqrt{3+4i}=2+i$, the two solutions are $x_\pm=\pm\tfrac{2+i}{2}$, and the four roots are

$$
\tilde P = \pm\bigl(1.0291+0.2429\,i\bigr)\bigl(e_0-e_3\bigr), \qquad \tilde P = \pm\bigl(0.2429-1.0291\,i\bigr)\bigl(e_0+e_3\bigr),
$$

whose squares are $-(2+i)e_3$; the second pair is the first multiplied by $-i$, with $e_0-e_3$ exchanged for $e_0+e_3$.

**A nilpotent root of $0$.** For $\tilde Q=0$ the scalar root is $\tilde P=0$ and the family is the pure null cone; $\tilde P=e_1+ie_2$ is one of its members, with

$$
(e_1+ie_2)^2 = e_1^2+i^2e_2^2+i\bigl(e_1e_2+e_2e_1\bigr) = -1+1+0 = 0 .
$$

## Summary

For a general $\tilde Q\in\mathbb{B}$ the square roots are found from the vector–scalar split $\tilde Q=Q_0e_0+\boldsymbol{Q}$ and $\tilde P=P_0e_0+\boldsymbol{P}$, which turns $\tilde P^2=\tilde Q$ into the vector equation $2P_0\boldsymbol{P}=\boldsymbol{Q}$ and the scalar equation $P_0^2-(\boldsymbol{P},\boldsymbol{P})=Q_0$.

When $\boldsymbol{Q}\neq0$, a root has $P_0\neq0$ and $\boldsymbol{P}=\boldsymbol{Q}/(2P_0)$, and $x=P_0^2$ solves the reduced quadratic $4x^2-4Q_0x-(\boldsymbol{Q},\boldsymbol{Q})=0$, whose discriminant is $16n$ with $n=Q_0^2+(\boldsymbol{Q},\boldsymbol{Q})$; each nonzero solution $x$ contributes the pair $\tilde P=\pm\bigl(\sqrt{x}\,e_0+\boldsymbol{Q}/(2\sqrt{x})\bigr)$.

When $\boldsymbol{Q}=0$, the radicand is a complex scalar and the roots are the two elements $\pm\sqrt{Q_0}e_0$ (one when $Q_0=0$) together with the four-real-parameter family of pure $\boldsymbol{P}$ with $(\boldsymbol{P},\boldsymbol{P})=-Q_0$.

The number of roots is: **four** when $(\boldsymbol{Q},\boldsymbol{Q})\neq0$ and $n\neq0$; **two** when $(\boldsymbol{Q},\boldsymbol{Q})\neq0$ and $n=0$, or when $(\boldsymbol{Q},\boldsymbol{Q})=0$ and $Q_0\neq0$; **none** when $n=0$ and $Q_0=0$ with $\boldsymbol{Q}\neq0$; and the **four-parameter family** when and only when $\tilde Q$ is a complex scalar.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\tilde Q$ | The element whose square roots are sought |
| $\tilde P$ | A square root of $\tilde Q$ |
| $\boldsymbol{Q}=Q_1e_1+Q_2e_2+Q_3e_3$ | Vector part of $\tilde Q$ |
| $(\boldsymbol{Q},\boldsymbol{Q})=Q_1^2+Q_2^2+Q_3^2$ | Complex square of the vector part |
| $n=Q_0^2+(\boldsymbol{Q},\boldsymbol{Q})$ | The scalar of $\tilde Q\tilde Q^{\natural}=ne_0$ |
| $x=P_0^2$ | Square of the scalar part of a root |
| $x_\pm=\tfrac12\bigl(Q_0\pm\sqrt{n}\bigr)$ | The two solutions of the reduced quadratic |

## Further Reading

- A. Acus and A. Dargys, *Square roots of complexified quaternions*, arXiv:2601.08391 (2026), for the square-root problem of complexified quaternions and the worked examples reproduced here.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the central case.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the nilpotent cone.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic properties of the biquaternions.
