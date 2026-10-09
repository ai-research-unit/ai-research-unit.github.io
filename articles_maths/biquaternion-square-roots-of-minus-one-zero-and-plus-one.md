# __Biquaternion Square Roots of Minus One, Zero and Plus One__

## Introduction

This article determines the square roots of the three central values $-1$, $0$ and $+1$ in the biquaternion algebra $\mathbb{B}$, that is, the elements $\tilde P \in \mathbb{B}$ satisfying

$$
\tilde P^2 = -1, \qquad \tilde P^2 = 0, \qquad \tilde P^2 = +1.
$$

It relates to *Biquaternion Idempotents and Projections* through the bijection between the roots of $-1$ and the idempotents established in §*The Relation to the Idempotents*. The goal here is to state the classification precisely and to prove it. The classification of $\tilde P^2 = \tilde Q$ for an arbitrary $\tilde Q \in \mathbb{B}$, by the same vector–scalar split and free of Clifford algebras, is the subject of *Biquaternion Square Roots of a General Element*; the three cases treated here are its degenerate data, and the algorithm is deliberately not reproduced, since these three sets are small enough to be found directly.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is assumed from the article on biquaternion algebra, together with its four conjugations and its six distinguished subspaces.

Throughout this article, the quaternion basis is written $e_0 = 1, e_1, e_2, e_3$, and the scalar imaginary is written $i$, so that it does not collide with the quaternion units. A general biquaternion is written

$$
\tilde{P} = P_0 e_0 + P_1 e_1 + P_2 e_2 + P_3 e_3, \qquad P_k \in \mathbb{C}.
$$

The quaternion conjugate is denoted $\tilde{P}^{\natural}$, the complex conjugate is denoted $\bar{\tilde{P}}$, and the Hermitian conjugate is denoted $\tilde{P}^{*} = \overline{\tilde{P}^{\natural}}$. Throughout, $\boldsymbol{p}$ and $\boldsymbol{p}'$ denote the real and imaginary parts of the vector part of a root, and two pure real quaternions are said to **anticommute** when $\boldsymbol{p}\boldsymbol{p}' + \boldsymbol{p}'\boldsymbol{p} = 0$.

Throughout, the square $\tilde{P}^2$ is taken in the general plain bilinear product $\tilde{P}\tilde{P}$, the multiplication of the algebra. The other three products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* have different squares, and therefore different roots. In the general quaternionic bilinear product the square is always the central element $N(\tilde{P})e_0$, so that the roots of a central value $\lambda$ are the single equation $N(\tilde{P}) = \lambda$. In the general plain sesquilinear product the scalar part of the square is $\sum_\mu\lvert P_\mu\rvert^2$, which is never negative, so that product has **no** root of $-1$ at all and its only root of $0$ is $\tilde{P} = 0$. In the general quaternionic sesquilinear product the scalar part of the square is the Krein value $\lvert P_0\rvert^2 - \sum_k\lvert P_k\rvert^2$, on which roots of all three values occur, $e_k^2 = -e_0$ for instance. The classification of this article is therefore the classification of the roots for the general plain bilinear product; the four squares and the four idempotent sets are set side by side in *Comparison Between the Four General Products*.

## The Problem and Its Reduction

The three problems of this article — the equations $\tilde P^2 = -1$, $\tilde P^2 = 0$ and $\tilde P^2 = +1$ — share one reduction, carried out once here and applied three times. In the components $P_k$ of the general biquaternion fixed above, the root splits as

$$
\tilde P = P_0 e_0 + \boldsymbol{P}, \qquad \boldsymbol{P} = P_1 e_1 + P_2 e_2 + P_3 e_3,
$$

where $P_0 e_0$ is the **complex scalar part** and $\boldsymbol{P}$ the **complex vector part**. The square of $\tilde P$ is given by the product formula for biquaternions:

$$
\tilde P^2 = \bigl(P_0^2 - (\boldsymbol{P}, \boldsymbol{P})\bigr) e_0 + 2P_0\boldsymbol{P}, \qquad (\boldsymbol{P}, \boldsymbol{P}) = P_1^2 + P_2^2 + P_3^2.
$$

The scalar part of $\tilde P^2$ is $(P_0^2 - (\boldsymbol{P}, \boldsymbol{P})) e_0$ and the vector part is $2P_0\boldsymbol{P}$, so equating $\tilde P^2$ to a central value splits the equation into a vector part and a scalar part.

## The Roots of Minus One

### Statement

A **root of $-1$** in $\mathbb{B}$ is an element $\tilde P \in \mathbb{B}$ satisfying

$$
\tilde P^2 = -1.
$$

The problem is to find all such elements.

### Reduction to Two Cases

Equating $\tilde P^2$ to $-1 = -e_0$ requires

$$
2P_0\boldsymbol{P} = 0, \qquad P_0^2 - (\boldsymbol{P}, \boldsymbol{P}) = -1.
$$

The first equation is a vector equation. Since $\mathbb{B}$ is a free $\mathbb{C}$-module and $\mathbb{C}$ is a field, the equation $P_0\boldsymbol{P} = 0$ holds if and only if $P_0 = 0$ or $\boldsymbol{P} = 0$. So the roots of $-1$ split into two cases.

**Case A — the root is a complex scalar ($\boldsymbol{P} = 0$).** Then $\tilde P = P_0 e_0$, and the scalar equation becomes $P_0^2 = -1$, so $P_0 = \pm i$. **The roots in this case are the two complex scalars**

$$
\tilde P = +i, \qquad \tilde P = -i,
$$

the **trivial roots**.

**Case B — the root is pure ($P_0 = 0$).** Then $\tilde P = \boldsymbol{P} = P_1 e_1 + P_2 e_2 + P_3 e_3$ has vanishing scalar part, and the scalar equation becomes

$$
(\boldsymbol{P}, \boldsymbol{P}) = P_1^2 + P_2^2 + P_3^2 = 1 .
$$

**The roots in this case are the pure biquaternions of complex square $1$**, the **pure roots**, found in the next section.

The two cases are disjoint: a trivial root has vanishing vector part and so lies only in Case A, while a pure root has vanishing scalar part and so lies only in Case B.

### The Pure Roots

We now solve the equation $(\boldsymbol{P}, \boldsymbol{P}) = 1$ for the pure biquaternion $\boldsymbol{P} = P_1 e_1 + P_2 e_2 + P_3 e_3$.

Write each complex coefficient as $P_k = p_k + i p'_k$ with $p_k, p'_k \in \mathbb{R}$, so that the complex vector part splits into its real and imaginary parts,

$$
\boldsymbol{P} = \boldsymbol{p} + i\boldsymbol{p}', \qquad \boldsymbol{p} = p_1 e_1 + p_2 e_2 + p_3 e_3, \qquad \boldsymbol{p}' = p'_1 e_1 + p'_2 e_2 + p'_3 e_3 .
$$

Then

$$
(\boldsymbol{P}, \boldsymbol{P}) = P_1^2 + P_2^2 + P_3^2 = (p_1 + ip'_1)^2 + (p_2 + ip'_2)^2 + (p_3 + ip'_3)^2
= \bigl(p_1^2 + p_2^2 + p_3^2 - p_1'^2 - p_2'^2 - p_3'^2\bigr) + 2i\bigl(p_1p'_1 + p_2p'_2 + p_3p'_3\bigr).
$$

Equating the real and imaginary parts to $1$ and $0$:

$$
p_1^2 + p_2^2 + p_3^2 - p_1'^2 - p_2'^2 - p_3'^2 = 1, \qquad p_1p'_1 + p_2p'_2 + p_3p'_3 = 0.
$$

The first equation gives $p_1^2 + p_2^2 + p_3^2 = 1 + p_1'^2 + p_2'^2 + p_3'^2 \geq 1 > 0$, so the triple $(p_1, p_2, p_3)$ is nonzero.

**Sub-case B1 — the root is real ($\boldsymbol{p}' = 0$).** The imaginary part of the root vanishes, so the second equation $p_1p'_1 + p_2p'_2 + p_3p'_3 = 0$ holds automatically, and the first equation reduces to the single condition

$$
p_1^2 + p_2^2 + p_3^2 = 1 .
$$

The root is the pure real quaternion, with three real coefficients,

$$
\tilde P = \boldsymbol{p} = p_1e_1 + p_2e_2 + p_3e_3, \qquad p_1, p_2, p_3 \in \mathbb{R},
$$

and squaring it term by term,

$$
\boldsymbol{p}^2 = p_1^2e_1^2 + p_2^2e_2^2 + p_3^2e_3^2 + p_1p_2\bigl(e_1e_2 + e_2e_1\bigr) + p_1p_3\bigl(e_1e_3 + e_3e_1\bigr) + p_2p_3\bigl(e_2e_3 + e_3e_2\bigr) = -\bigl(p_1^2 + p_2^2 + p_3^2\bigr)e_0 = -e_0 = -1,
$$

because $e_k^2 = -1$ and each cross term vanishes, $e_je_k + e_ke_j = 0$ for $j \neq k$. So every pure real quaternion satisfying that one condition is a root.

The condition $p_1^2 + p_2^2 + p_3^2 = 1$ is the **real unit vectors** in the three real coordinates $(p_1, p_2, p_3)$: three real coefficients carrying one constraint, hence two free real parameters. **The roots in this case are the pure real quaternions of unit length**, the **real roots** — the roots of $-1$ lying in the real subspace $\mathbb{H}$ of $\mathbb{B}$, that is, the classical imaginary units of the quaternions.

The two signs describe one set and not two: if $\boldsymbol{p}$ is a root then so is $-\boldsymbol{p}$, because $(-\boldsymbol{p})^2 = \boldsymbol{p}^2 = -1$, and the set of real unit vectors already contains both. The family is therefore written in the redundant form

$$
\tilde P = \pm\boldsymbol{p}, \qquad \boldsymbol{p} = p_1e_1 + p_2e_2 + p_3e_3, \qquad p_1^2 + p_2^2 + p_3^2 = 1,
$$

the sign being the image of the root under $\boldsymbol{p} \mapsto -\boldsymbol{p}$.

**Sub-case B2 — the root is genuinely complex ($\boldsymbol{p}' \neq 0$).** Then $p_1^2 + p_2^2 + p_3^2 \geq 1 > 0$ and $p_1'^2 + p_2'^2 + p_3'^2 > 0$. The square of a pure real quaternion is a scalar,

$$
\boldsymbol{p}^2 = -\bigl(p_1^2 + p_2^2 + p_3^2\bigr) e_0, \qquad \boldsymbol{p}'^2 = -\bigl(p_1'^2 + p_2'^2 + p_3'^2\bigr) e_0,
$$

and the mixed product is a scalar multiple of $e_0$,

$$
\boldsymbol{p}\boldsymbol{p}' + \boldsymbol{p}'\boldsymbol{p} = -2\bigl(p_1p'_1 + p_2p'_2 + p_3p'_3\bigr) e_0 = 0
$$

by the second equation, so the two pure real quaternions $\boldsymbol{p}$ and $\boldsymbol{p}'$ anticommute. **The roots in this case are the elements**

$$
\tilde P = \boldsymbol{p} + i\boldsymbol{p}' = \bigl(p_1e_1 + p_2e_2 + p_3e_3\bigr) + i\bigl(p'_1e_1 + p'_2e_2 + p'_3e_3\bigr),
$$

whose six real coefficients satisfy the two conditions

$$
p_1^2 + p_2^2 + p_3^2 - p_1'^2 - p_2'^2 - p_3'^2 = 1, \qquad p_1p'_1 + p_2p'_2 + p_3p'_3 = 0,
$$

a four-real-parameter family, the **non-trivial roots**.

### Statement of the Theorem

**Theorem.** The roots of $-1$ in $\mathbb{B}$ are exactly the elements of the three following families.

**The trivial roots.** The two elements

$$
\tilde P = +i, \qquad \tilde P = -i .
$$

**The real roots.** The pure real quaternions of unit length, a two-real-parameter family,

$$
\tilde P = \boldsymbol{p} = p_1e_1 + p_2e_2 + p_3e_3, \qquad p_1^2 + p_2^2 + p_3^2 = 1 ;
$$

the sign is absorbed, so the family is also written $\tilde P = \pm\boldsymbol{p}$.

**The non-trivial roots.** The four-real-parameter family

$$
\tilde P = \boldsymbol{p} + i\boldsymbol{p}' = \bigl(p_1e_1+p_2e_2+p_3e_3\bigr) + i\bigl(p'_1e_1+p'_2e_2+p'_3e_3\bigr),
$$

whose six real coefficients satisfy the two conditions

$$
p_1^2 + p_2^2 + p_3^2 - p_1'^2 - p_2'^2 - p_3'^2 = 1, \qquad p_1p'_1 + p_2p'_2 + p_3p'_3 = 0,
$$

equivalently $\boldsymbol{p}\boldsymbol{p}' + \boldsymbol{p}'\boldsymbol{p} = 0$, and whose imaginary part $\boldsymbol{p}'$ is nonzero.

The three families are disjoint, and together they are all the roots.

### Verification

We verify that each of the three families consists of roots of $-1$.

**Trivial root.** $(\pm i)^2 = -1$ since $i^2 = -1$. ✓

**Real roots.** For a pure real quaternion $\boldsymbol{p}$ with $\boldsymbol{p}^2 = -1$, $(\pm \boldsymbol{p})^2 = \boldsymbol{p}^2 = -1$. ✓

**Non-trivial roots.** Compute

$$
\tilde P^2 = (\boldsymbol{p} + i\boldsymbol{p}')^2 = \boldsymbol{p}^2 + i\bigl(\boldsymbol{p}\boldsymbol{p}' + \boldsymbol{p}'\boldsymbol{p}\bigr) + \boldsymbol{p}'^2 i^2 = \boldsymbol{p}^2 - \boldsymbol{p}'^2 + i\bigl(\boldsymbol{p}\boldsymbol{p}' + \boldsymbol{p}'\boldsymbol{p}\bigr).
$$

Now $\boldsymbol{p}^2 = -(p_1^2 + p_2^2 + p_3^2)e_0$, $\boldsymbol{p}'^2 = -(p_1'^2 + p_2'^2 + p_3'^2)e_0$ and $\boldsymbol{p}\boldsymbol{p}' + \boldsymbol{p}'\boldsymbol{p} = -2(p_1p'_1 + p_2p'_2 + p_3p'_3)e_0 = 0$, so

$$
\tilde P^2 = -\bigl(p_1^2 + p_2^2 + p_3^2 - p_1'^2 - p_2'^2 - p_3'^2\bigr) e_0 = -e_0 = -1 . ✓
$$

### Degenerate Cases

The three families are related as follows.

**The real roots as the case $\boldsymbol{p}' = 0$.** In the non-trivial family $\boldsymbol{p}'$ is nonzero. If that condition is relaxed to $\boldsymbol{p}' = 0$, the two constraints reduce to the single equation $p_1^2 + p_2^2 + p_3^2 = 1$, and $\tilde P = \boldsymbol{p}$ is a real root. The real roots are therefore the case $\boldsymbol{p}' = 0$ of the non-trivial formula, and not a separate construction.

**The trivial roots as a separate family.** The trivial roots $\tilde P = \pm i$ have vanishing vector part. The real roots (with $\boldsymbol{P} = \boldsymbol{p} \neq 0$) and the non-trivial roots (with $\boldsymbol{P} = \boldsymbol{p} + i\boldsymbol{p}'$, whose real part $\boldsymbol{p}$ is nonzero since $p_1^2 + p_2^2 + p_3^2 = 1 + p_1'^2 + p_2'^2 + p_3'^2 \geq 1$) all have nonvanishing vector part. So the roots with vanishing vector part are exactly $\pm i$, and they form a separate family.

### Status of the Roots

Counting the free real parameters: the trivial roots are two isolated elements, the real roots are a two-real-parameter family (three real coefficients carrying one constraint), and the non-trivial roots are a four-real-parameter family (six real coefficients carrying two constraints).

All roots except the trivial ones are **pure** (their scalar part vanishes), hence lie in the six-real-dimensional vector subspace of pure biquaternions. The roots are neither idempotents ($\tilde P^2 = -1 \neq \tilde P$) nor zero divisors (§*The Roots as Invertible Elements*).

## The Roots of Zero

### Reduction to Two Cases

A **root of $0$** is an element $\tilde P \in \mathbb{B}$ with $\tilde P^2 = 0$. With $\tilde P = P_0 e_0 + \boldsymbol{P}$ the square is $\tilde P^2 = (P_0^2 - (\boldsymbol{P},\boldsymbol{P}))e_0 + 2P_0\boldsymbol{P}$ (§*The Problem and Its Reduction*), and equating it to $0$ gives

$$
2P_0\boldsymbol{P} = 0, \qquad P_0^2 - (\boldsymbol{P},\boldsymbol{P}) = 0 .
$$

The first equation is the same vector equation as for the roots of $-1$, and again forces $P_0 = 0$ or $\boldsymbol{P} = 0$.

**Case A — the root is a complex scalar ($\boldsymbol{P} = 0$).** Then $\tilde P = P_0 e_0$ and $P_0^2 = 0$; since $\mathbb{C}$ is a field, $P_0 = 0$. **The root in this case is the single element**

$$
\tilde P = 0 .
$$

**Case B — the root is pure ($P_0 = 0$).** Then $\tilde P = \boldsymbol{P}$ and $(\boldsymbol{P},\boldsymbol{P}) = 0$, that is

$$
\tilde P = P_1e_1 + P_2e_2 + P_3e_3, \qquad P_1^2 + P_2^2 + P_3^2 = 0 .
$$

**The roots in this case are the pure biquaternions of vanishing complex square**, a four-real-parameter family; writing $P_k = p_k + ip'_k$, the condition is the pair of real equations $p_1^2+p_2^2+p_3^2-p_1'^2-p_2'^2-p_3'^2 = 0$ and $p_1p'_1+p_2p'_2+p_3p'_3 = 0$.

### Statement of the Theorem

**Theorem.** The roots of $0$ in $\mathbb{B}$ are exactly the following.

**The zero element.**

$$
\tilde P = 0 .
$$

**The nilpotent cone.** The pure biquaternions of vanishing complex square, a four-real-parameter family,

$$
\tilde P = P_1e_1 + P_2e_2 + P_3e_3, \qquad P_1^2 + P_2^2 + P_3^2 = 0,
$$

that is, writing $P_k = p_k + ip'_k$, the pair of real equations $p_1^2+p_2^2+p_3^2-p_1'^2-p_2'^2-p_3'^2 = 0$ and $p_1p'_1+p_2p'_2+p_3p'_3 = 0$. Its nonzero elements are the nilpotents of the algebra.

### Verification

For a pure $\tilde P$ with $(\boldsymbol{P},\boldsymbol{P}) = 0$ the scalar part of $\tilde P^2$ is $-(\boldsymbol{P},\boldsymbol{P}) = 0$ and the vector part is $2P_0\boldsymbol{P} = 0$, and the two cases are exhaustive by the reduction above. ✓

The nonzero roots of $0$ are exactly the **nilpotents** of the algebra, and they form the **nilpotent cone** of the pure subspace. An example is $\tilde P = e_1 + ie_2$, for which

$$
(e_1+ie_2)^2 = e_1^2 + i^2e_2^2 + i(e_1e_2+e_2e_1) = -1 + 1 + 0 = 0 .
$$

The set is the **nilpotent** family of the zero-divisor set of $\mathbb{B}$; the whole zero-divisor set — the elements of vanishing norm, which splits into these nilpotents and the non-pure zero divisors — its two families and the criterion in terms of the scalar part, are the subject of *Biquaternion Zero Divisors*. It is named here only to complete the list of the three central values, and not developed.

## The Roots of Plus One

### Statement of the Theorem

A **root of $+1$** is an element $\tilde P_+ \in \mathbb{B}$ satisfying $\tilde P_+^2 = 1$. The roots of $+1$ are related to the roots of $-1$ by

$$
\tilde P_+ = \tilde P i,
$$

where $\tilde P$ is a root of $-1$. **The roots of $+1$ are exactly the following three families.**

**The trivial roots.** The two elements

$$
\tilde P_+ = +1, \qquad \tilde P_+ = -1,
$$

the images of $\tilde P = \pm i$. They are the only roots of $+1$ that lie in the centre $\mathbb{C}$.

**The real roots.** The images of the real roots of $-1$: the elements

$$
\tilde P_+ = \pm\boldsymbol{p}i, \qquad \boldsymbol{p} = p_1e_1 + p_2e_2 + p_3e_3, \qquad p_1^2 + p_2^2 + p_3^2 = 1,
$$

where $\boldsymbol{p}$ is a pure real quaternion of unit length. Each one is a root of $+1$, since

$$
(\boldsymbol{p}i)^2 = \boldsymbol{p}^2 i^2 = (-1)(-1) = 1 .
$$

Spelled out, the family is $\tilde P_+ = \pm(p_1e_1 + p_2e_2 + p_3e_3)i$ with $p_1^2 + p_2^2 + p_3^2 = 1$: the same real unit vectors of the roots of $-1$, mapped by $\boldsymbol{p} \mapsto \boldsymbol{p}i$. It is a **two-real-parameter family**, and its elements are the only roots of $+1$ that are pure multiples of a real quaternion.

**The non-trivial roots.** The four-real-parameter family

$$
\tilde P_+ = (\boldsymbol{p} + i\boldsymbol{p}') i = \boldsymbol{p}i - \boldsymbol{p}', \qquad \boldsymbol{p}' \neq 0,
$$

whose six real coefficients satisfy $p_1^2 + p_2^2 + p_3^2 - p_1'^2 - p_2'^2 - p_3'^2 = 1$ and $p_1p'_1 + p_2p'_2 + p_3p'_3 = 0$.

### Verification

That $\tilde P_+ = \tilde P i$ is a root of $+1$ follows from

$$
(\tilde P i)^2 = \tilde P^2 i^2 = (-1)(-1) = 1,
$$

and the map $\tilde P \mapsto \tilde P i$ is a bijection from the roots of $-1$ to the roots of $+1$: it is injective since $i$ is invertible, and if $\tilde P_+^2 = 1$ then $\tilde P = -\tilde P_+ i$ satisfies $\tilde P^2 = -1$ and $\tilde P i = \tilde P_+$. ✓

The roots of $+1$ are not used in the classification of the idempotents, but they appear in the theory of the biquaternion exponential and in the theory of the biquaternion logarithm.

## The Three Sets Compared

The three root sets are related by their invertibility. The roots of $-1$ and of $+1$ are **units**: a root $\tilde P$ of $\pm 1$ satisfies $\tilde P^{-1} = \pm\tilde P$, in $\mathbb{B}^\times$. The nonzero roots of $0$ are the exception: they are nilpotents, hence zero divisors and not units. So of the three central values only $0$ has non-unit roots.

The three sets also differ in kind. The roots of $-1$ are two isolated elements together with a two-parameter family and a four-parameter family; the roots of $+1$ are the bijective image of that set under $\tilde P \mapsto \tilde P i$; and the roots of $0$ are the single element $0$ together with one four-parameter family, the nilpotent cone. In particular the roots of $0$ contain no unit, and the only non-pure roots of the three values are the trivial ones, $\pm i$ for $-1$ and $\pm 1$ for $+1$.

## The Relation to the Idempotents

The classification of the roots of $-1$ gives the classification of the idempotents of $\mathbb{B}$: the map

$$
\tilde P \longmapsto \tilde\Pi_+(\tilde P) = \tfrac{1}{2}(e_0 + \tilde P i)
$$

is a bijection from the set of roots of $-1$ onto the set of idempotents, under which the complementary pairs $\{\tilde\Pi, e_0 - \tilde\Pi\}$ correspond to the classes $\{\tilde P, -\tilde P\}$, and under which the three families of roots give the trivial idempotents, the Hermitian idempotents in $\mathbb{M}_+$, and the idempotents lying in none of the four four-dimensional subspaces. The construction of the idempotent, the proof of the bijection and the projection interpretation are the subject of *Biquaternion Idempotents and Projections*.

## The Relation to the Zero Divisors

### The Idempotents as Zero Divisors

Every non-trivial idempotent is a zero divisor, $\tilde\Pi(e_0 - \tilde\Pi) = 0$ with both factors nonzero (the construction of $\tilde\Pi$ is in *Biquaternion Idempotents and Projections*). The trivial idempotents $0$ and $e_0$ are not zero divisors: $0$ is excluded by the definition, and $e_0$ is a unit.

### The Roots as Invertible Elements

A root of $-1$ is a unit and **not** a zero divisor. Indeed, $\tilde P^2 = -1$ gives

$$
\tilde P\,(-\tilde P) = (-\tilde P)\,\tilde P = e_0,
$$

so $\tilde P$ is invertible, with inverse $\tilde P^{-1} = -\tilde P$. A unit is not a zero divisor: if $\tilde P \tilde Q = 0$ for some $\tilde Q$, then $\tilde Q = (-\tilde P)(\tilde P \tilde Q) = 0$, and the same argument applies to $\tilde Q\tilde P = 0$. Hence the roots of $-1$ lie in the group of units $\mathbb{B}^\times$. The central scalar $\tilde P \tilde P^{\natural}$ is $-1$ for the trivial roots and $+1$ for a pure root.

## Summary

This article determines the square roots of the three central values $-1$, $0$ and $+1$ in the biquaternion algebra, by one reduction applied three times: writing $\tilde P = P_0 e_0 + \boldsymbol{P}$ and using the product formula $\tilde P^2 = (P_0^2 - (\boldsymbol{P},\boldsymbol{P}))e_0 + 2P_0\boldsymbol{P}$, the vector part forces $P_0 = 0$ or $\boldsymbol{P} = 0$, and the scalar part then gives the equation of the value.

The square roots of $-1$ are exactly:

1. **Trivial roots:** $\tilde P = \pm i$.
2. **Real roots:** $\tilde P = \pm\boldsymbol{p}$, where $\boldsymbol{p}$ is a pure real quaternion with $\boldsymbol{p}^2 = -1$.
3. **Non-trivial roots:** $\tilde P = \boldsymbol{p} + i\boldsymbol{p}'$, where $\boldsymbol{p}' \neq 0$ and the two real conditions $p_1^2 + p_2^2 + p_3^2 - p_1'^2 - p_2'^2 - p_3'^2 = 1$ and $p_1p'_1 + p_2p'_2 + p_3p'_3 = 0$ hold.

The scalar case gives the trivial roots. The pure case reduces to $(\boldsymbol{P}, \boldsymbol{P}) = 1$, which splits into the real and non-trivial families according to whether the imaginary part $\boldsymbol{p}'$ of the pure biquaternion vanishes. The trivial roots are the two elements $\pm i$. The real roots are the family $\pm\boldsymbol{p}$ cut out by the single constraint $p_1^2 + p_2^2 + p_3^2 = 1$, leaving two free real parameters. The non-trivial roots are the elements $\boldsymbol{p} + i\boldsymbol{p}'$ cut out by the two constraints $p_1^2 + p_2^2 + p_3^2 - p_1'^2 - p_2'^2 - p_3'^2 = 1$ and $p_1p'_1 + p_2p'_2 + p_3p'_3 = 0$, four free real parameters in all. All roots except the trivial ones are pure, hence lie in the six-real-dimensional vector subspace of pure biquaternions.

The square roots of $0$ are the element $0$ together with the pure biquaternions $\tilde P = P_1e_1+P_2e_2+P_3e_3$ with $P_1^2+P_2^2+P_3^2=0$, a four-real-parameter nilpotent cone whose nonzero elements are the nilpotents of the algebra, for example $e_1+ie_2$. Unlike the roots of $-1$ and $+1$, which are units, the nonzero roots of $0$ are zero divisors; the full structure of the cone, and the classification of the zero divisors it is part of, are in *Biquaternion Zero Divisors*, and the classification of $\tilde P^2=\tilde Q$ for a general $\tilde Q$ is in *Biquaternion Square Roots of a General Element*.

The square roots of $+1$ are obtained from the roots of $-1$ by multiplication by $i$: $\tilde P_+ = \tilde P i$. They are not used in the idempotent classification, but they appear in the theory of the biquaternion exponential.

The classification of the roots of $-1$ gives the classification of the idempotents of $\mathbb{B}$, which are of the form $\tfrac{1}{2} e_0 \pm \tfrac{1}{2} \tilde P i$. The map $\tilde P \mapsto \tilde\Pi_+(\tilde P) = \tfrac{1}{2}(e_0 + \tilde P i)$ is a bijection from the roots of $-1$ to the idempotents; complementary pairs of idempotents correspond to roots modulo the sign identification $\tilde P \sim -\tilde P$. The non-trivial idempotents form a four-real-parameter family, and are used in the classification of the non-pure zero divisors. The roots themselves are units, and they lie in the group of units $\mathbb{B}^\times$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis |
| $i$ | Scalar imaginary |
| $\tilde P$ | A biquaternion; here the root of $-1$ or of $0$ |
| $\tilde P_+$ | The root of $+1$ |
| $\tilde Q$ | A second biquaternion, the element whose roots are sought in the general problem |
| $P_k = p_k + ip'_k$, $k=0,\dots,3$ | Complex components of the root, $P_k \in \mathbb{C}$; the scalar part is $P_0 e_0$ |
| $\boldsymbol{P} = P_1e_1+P_2e_2+P_3e_3$ | Complex vector part of the root |
| $\boldsymbol{p}, \boldsymbol{p}'$ | Its real and imaginary parts, $\boldsymbol{P} = \boldsymbol{p} + i\boldsymbol{p}'$ |
| $\tilde\Pi = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \tilde P i$ | Idempotent |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original discovery of the biquaternions.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the original classification.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the relation to the idempotents and the zero divisors.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the constraint verification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic properties of the biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- A. Acus and A. Dargys, *Square roots of complexified quaternions*, arXiv:2601.08391 (2026), for the square roots of an arbitrary complexified quaternion, the subject of *Biquaternion Square Roots of a General Element*.
