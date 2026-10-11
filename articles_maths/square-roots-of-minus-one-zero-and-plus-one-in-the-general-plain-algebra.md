# __Square Roots of Minus One, Zero and Plus One in the General Plain Algebra__

## Introduction

This article determines the square roots of the three central values $-1$, $0$ and $+1$ in the biquaternion algebra $\mathbb{B}$, that is, the elements $\tilde\Xi \in \mathbb{B}$ satisfying

$$
\tilde\Xi^2 = -1, \qquad \tilde\Xi^2 = 0, \qquad \tilde\Xi^2 = +1.
$$

It relates to *Idempotents of the General Plain Algebra* through the bijection between the roots of $-1$ and the idempotents established in §*The Relation to the Idempotents*. The goal here is to state the classification precisely and to prove it. The classification of $\tilde\Xi^2 = \tilde Q$ for an arbitrary $\tilde Q \in \mathbb{B}$, by the same vector–scalar split and free of Clifford algebras, is the subject of *Square Roots of a General Element in the General Plain Algebra*; the three cases treated here are its degenerate data, and the algorithm is deliberately not reproduced, since these three sets are small enough to be found directly.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra. The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is assumed from the article on biquaternion algebra, together with its four conjugations and its remarkable subspaces.

Throughout this article, the quaternion basis is written $e_0 = 1, e_1, e_2, e_3$, and the scalar imaginary is written $i$, so that it does not collide with the quaternion units. A general biquaternion is written

$$
\tilde\Xi = \Xi_0 e_0 + \Xi_1 e_1 + \Xi_2 e_2 + \Xi_3 e_3, \qquad \Xi_k \in \mathbb{C}.
$$

The quaternion conjugate is denoted $\tilde\Xi^{\natural}$, the complex conjugate is denoted $\bar{\tilde\Xi}$, and the Hermitian conjugate is denoted $\tilde\Xi^{*} = \overline{\tilde\Xi^{\natural}}$. Throughout, $\boldsymbol{\xi}$ and $\boldsymbol{\xi}'$ denote the real and imaginary parts of the vector part of a root, and two pure real quaternions are said to **anticommute** when $\boldsymbol{\xi}\boldsymbol{\xi}' + \boldsymbol{\xi}'\boldsymbol{\xi} = 0$.

## The Problem and Its Reduction

The three problems of this article — the equations $\tilde\Xi^2 = -1$, $\tilde\Xi^2 = 0$ and $\tilde\Xi^2 = +1$ — share one reduction, carried out once here and applied three times. In the components $\Xi_k$ of the general biquaternion fixed above, the root splits as

$$
\tilde\Xi = \Xi_0 e_0 + \boldsymbol\Xi, \qquad \boldsymbol\Xi = \Xi_1 e_1 + \Xi_2 e_2 + \Xi_3 e_3,
$$

where $\Xi_0 e_0$ is the **complex scalar part** and $\boldsymbol\Xi$ the **complex vector part**. The square of $\tilde\Xi$ is given by the product formula for biquaternions:

$$
\tilde\Xi^2 = \bigl(\Xi_0^2 - (\boldsymbol\Xi, \boldsymbol\Xi)\bigr) e_0 + 2\Xi_0\boldsymbol\Xi, \qquad (\boldsymbol\Xi, \boldsymbol\Xi) = \Xi_1^2 + \Xi_2^2 + \Xi_3^2.
$$

The scalar part of $\tilde\Xi^2$ is $(\Xi_0^2 - (\boldsymbol\Xi, \boldsymbol\Xi)) e_0$ and the vector part is $2\Xi_0\boldsymbol\Xi$, so equating $\tilde\Xi^2$ to a central value splits the equation into a vector part and a scalar part.

## The Roots of Minus One

### Statement

A **root of $-1$** in $\mathbb{B}$ is an element $\tilde\Xi \in \mathbb{B}$ satisfying

$$
\tilde\Xi^2 = -1.
$$

The problem is to find all such elements.

### Reduction to Two Cases

Equating $\tilde\Xi^2$ to $-1 = -e_0$ requires

$$
2\Xi_0\boldsymbol\Xi = 0, \qquad \Xi_0^2 - (\boldsymbol\Xi, \boldsymbol\Xi) = -1.
$$

The first equation is a vector equation. Since $\mathbb{B}$ is a free $\mathbb{C}$-module and $\mathbb{C}$ is a field, the equation $\Xi_0\boldsymbol\Xi = 0$ holds if and only if $\Xi_0 = 0$ or $\boldsymbol\Xi = 0$. So the roots of $-1$ split into two cases.

**Case A — the root is a complex scalar ($\boldsymbol\Xi = 0$).** Then $\tilde\Xi = \Xi_0 e_0$, and the scalar equation becomes $\Xi_0^2 = -1$, so $\Xi_0 = \pm i$. **The roots in this case are the two complex scalars**

$$
\tilde\Xi = +i, \qquad \tilde\Xi = -i,
$$

the **trivial roots**.

**Case B — the root is pure ($\Xi_0 = 0$).** Then $\tilde\Xi = \boldsymbol\Xi = \Xi_1 e_1 + \Xi_2 e_2 + \Xi_3 e_3$ has vanishing scalar part, and the scalar equation becomes

$$
(\boldsymbol\Xi, \boldsymbol\Xi) = \Xi_1^2 + \Xi_2^2 + \Xi_3^2 = 1 .
$$

**The roots in this case are the pure biquaternions of complex square $1$**, the **pure roots**, found in the next section.

The two cases are disjoint: a trivial root has vanishing vector part and so lies only in Case A, while a pure root has vanishing scalar part and so lies only in Case B.

### The Pure Roots

We now solve the equation $(\boldsymbol\Xi, \boldsymbol\Xi) = 1$ for the pure biquaternion $\boldsymbol\Xi = \Xi_1 e_1 + \Xi_2 e_2 + \Xi_3 e_3$.

Write each complex coefficient as $\Xi_k = \xi_k + i \xi'_k$ with $\xi_k, \xi'_k \in \mathbb{R}$, so that the complex vector part splits into its real and imaginary parts,

$$
\boldsymbol\Xi = \boldsymbol{\xi} + i\boldsymbol{\xi}', \qquad \boldsymbol{\xi} = \xi_1 e_1 + \xi_2 e_2 + \xi_3 e_3, \qquad \boldsymbol{\xi}' = \xi'_1 e_1 + \xi'_2 e_2 + \xi'_3 e_3 .
$$

Then

$$
(\boldsymbol\Xi, \boldsymbol\Xi) = \Xi_1^2 + \Xi_2^2 + \Xi_3^2 = (\xi_1 + i\xi'_1)^2 + (\xi_2 + i\xi'_2)^2 + (\xi_3 + i\xi'_3)^2
= \bigl(\xi_1^2 + \xi_2^2 + \xi_3^2 - \xi'^2_1 - \xi'^2_2 - \xi'^2_3\bigr) + 2i\bigl(\xi_1\xi'_1 + \xi_2\xi'_2 + \xi_3\xi'_3\bigr).
$$

Equating the real and imaginary parts to $1$ and $0$:

$$
\xi_1^2 + \xi_2^2 + \xi_3^2 - \xi'^2_1 - \xi'^2_2 - \xi'^2_3 = 1, \qquad \xi_1\xi'_1 + \xi_2\xi'_2 + \xi_3\xi'_3 = 0.
$$

The first equation gives $\xi_1^2 + \xi_2^2 + \xi_3^2 = 1 + \xi'^2_1 + \xi'^2_2 + \xi'^2_3 \geq 1 > 0$, so the triple $(\xi_1, \xi_2, \xi_3)$ is nonzero.

**Sub-case B1 — the root is real ($\boldsymbol{\xi}' = 0$).** The imaginary part of the root vanishes, so the second equation $\xi_1\xi'_1 + \xi_2\xi'_2 + \xi_3\xi'_3 = 0$ holds automatically, and the first equation reduces to the single condition

$$
\xi_1^2 + \xi_2^2 + \xi_3^2 = 1 .
$$

The root is the pure real quaternion, with three real coefficients,

$$
\tilde\Xi = \boldsymbol{\xi} = \xi_1e_1 + \xi_2e_2 + \xi_3e_3, \qquad \xi_1, \xi_2, \xi_3 \in \mathbb{R},
$$

and squaring it term by term,

$$
\boldsymbol{\xi}^2 = \xi_1^2e_1^2 + \xi_2^2e_2^2 + \xi_3^2e_3^2 + \xi_1\xi_2\bigl(e_1e_2 + e_2e_1\bigr) + \xi_1\xi_3\bigl(e_1e_3 + e_3e_1\bigr) + \xi_2\xi_3\bigl(e_2e_3 + e_3e_2\bigr) = -\bigl(\xi_1^2 + \xi_2^2 + \xi_3^2\bigr)e_0 = -e_0 = -1,
$$

because $e_k^2 = -1$ and each cross term vanishes, $e_je_k + e_ke_j = 0$ for $j \neq k$. So every pure real quaternion satisfying that one condition is a root.

The condition $\xi_1^2 + \xi_2^2 + \xi_3^2 = 1$ is the **real unit vectors** in the three real coordinates $(\xi_1, \xi_2, \xi_3)$: three real coefficients carrying one constraint, hence two free real parameters. **The roots in this case are the pure real quaternions of unit length**, the **real roots** — the roots of $-1$ lying in the real subspace $\mathbb{H}$ of $\mathbb{B}$, that is, the classical imaginary units of the quaternions.

The two signs describe one set and not two: if $\boldsymbol{\xi}$ is a root then so is $-\boldsymbol{\xi}$, because $(-\boldsymbol{\xi})^2 = \boldsymbol{\xi}^2 = -1$, and the set of real unit vectors already contains both. The family is therefore written in the redundant form

$$
\tilde\Xi = \pm\boldsymbol{\xi}, \qquad \boldsymbol{\xi} = \xi_1e_1 + \xi_2e_2 + \xi_3e_3, \qquad \xi_1^2 + \xi_2^2 + \xi_3^2 = 1,
$$

the sign being the image of the root under $\boldsymbol{\xi} \mapsto -\boldsymbol{\xi}$.

**Sub-case B2 — the root is genuinely complex ($\boldsymbol{\xi}' \neq 0$).** Then $\xi_1^2 + \xi_2^2 + \xi_3^2 \geq 1 > 0$ and $\xi'^2_1 + \xi'^2_2 + \xi'^2_3 > 0$. The square of a pure real quaternion is a scalar,

$$
\boldsymbol{\xi}^2 = -\bigl(\xi_1^2 + \xi_2^2 + \xi_3^2\bigr) e_0, \qquad \boldsymbol{\xi}'^2 = -\bigl(\xi'^2_1 + \xi'^2_2 + \xi'^2_3\bigr) e_0,
$$

and the mixed product is a scalar multiple of $e_0$,

$$
\boldsymbol{\xi}\boldsymbol{\xi}' + \boldsymbol{\xi}'\boldsymbol{\xi} = -2\bigl(\xi_1\xi'_1 + \xi_2\xi'_2 + \xi_3\xi'_3\bigr) e_0 = 0
$$

by the second equation, so the two pure real quaternions $\boldsymbol{\xi}$ and $\boldsymbol{\xi}'$ anticommute. **The roots in this case are the elements**

$$
\tilde\Xi = \boldsymbol{\xi} + i\boldsymbol{\xi}' = \bigl(\xi_1e_1 + \xi_2e_2 + \xi_3e_3\bigr) + i\bigl(\xi'_1e_1 + \xi'_2e_2 + \xi'_3e_3\bigr),
$$

whose six real coefficients satisfy the two conditions

$$
\xi_1^2 + \xi_2^2 + \xi_3^2 - \xi'^2_1 - \xi'^2_2 - \xi'^2_3 = 1, \qquad \xi_1\xi'_1 + \xi_2\xi'_2 + \xi_3\xi'_3 = 0,
$$

a four-real-parameter family, the **non-trivial roots**.

### Statement of the Theorem

**Theorem.** The roots of $-1$ in $\mathbb{B}$ are exactly the elements of the three following families.

**The trivial roots.** The two elements

$$
\tilde\Xi = +i, \qquad \tilde\Xi = -i .
$$

**The real roots.** The pure real quaternions of unit length, a two-real-parameter family,

$$
\tilde\Xi = \boldsymbol{\xi} = \xi_1e_1 + \xi_2e_2 + \xi_3e_3, \qquad \xi_1^2 + \xi_2^2 + \xi_3^2 = 1 ;
$$

the sign is absorbed, so the family is also written $\tilde\Xi = \pm\boldsymbol{\xi}$.

**The non-trivial roots.** The four-real-parameter family

$$
\tilde\Xi = \boldsymbol{\xi} + i\boldsymbol{\xi}' = \bigl(\xi_1e_1+\xi_2e_2+\xi_3e_3\bigr) + i\bigl(\xi'_1e_1+\xi'_2e_2+\xi'_3e_3\bigr),
$$

whose six real coefficients satisfy the two conditions

$$
\xi_1^2 + \xi_2^2 + \xi_3^2 - \xi'^2_1 - \xi'^2_2 - \xi'^2_3 = 1, \qquad \xi_1\xi'_1 + \xi_2\xi'_2 + \xi_3\xi'_3 = 0,
$$

equivalently $\boldsymbol{\xi}\boldsymbol{\xi}' + \boldsymbol{\xi}'\boldsymbol{\xi} = 0$, and whose imaginary part $\boldsymbol{\xi}'$ is nonzero.

The three families are disjoint, and together they are all the roots.

### Verification

We verify that each of the three families consists of roots of $-1$.

**Trivial root.** $(\pm i)^2 = -1$ since $i^2 = -1$.

**Real roots.** For a pure real quaternion $\boldsymbol{\xi}$ with $\boldsymbol{\xi}^2 = -1$, $(\pm \boldsymbol{\xi})^2 = \boldsymbol{\xi}^2 = -1$.

**Non-trivial roots.** Compute

$$
\tilde\Xi^2 = (\boldsymbol{\xi} + i\boldsymbol{\xi}')^2 = \boldsymbol{\xi}^2 + i\bigl(\boldsymbol{\xi}\boldsymbol{\xi}' + \boldsymbol{\xi}'\boldsymbol{\xi}\bigr) + \boldsymbol{\xi}'^2 i^2 = \boldsymbol{\xi}^2 - \boldsymbol{\xi}'^2 + i\bigl(\boldsymbol{\xi}\boldsymbol{\xi}' + \boldsymbol{\xi}'\boldsymbol{\xi}\bigr).
$$

Now $\boldsymbol{\xi}^2 = -(\xi_1^2 + \xi_2^2 + \xi_3^2)e_0$, $\boldsymbol{\xi}'^2 = -(\xi'^2_1 + \xi'^2_2 + \xi'^2_3)e_0$ and $\boldsymbol{\xi}\boldsymbol{\xi}' + \boldsymbol{\xi}'\boldsymbol{\xi} = -2(\xi_1\xi'_1 + \xi_2\xi'_2 + \xi_3\xi'_3)e_0 = 0$, so

$$
\tilde\Xi^2 = -\bigl(\xi_1^2 + \xi_2^2 + \xi_3^2 - \xi'^2_1 - \xi'^2_2 - \xi'^2_3\bigr) e_0 = -e_0 = -1 .
$$

### Degenerate Cases

The three families are related as follows.

**The real roots as the case $\boldsymbol{\xi}' = 0$.** In the non-trivial family $\boldsymbol{\xi}'$ is nonzero. If that condition is relaxed to $\boldsymbol{\xi}' = 0$, the two constraints reduce to the single equation $\xi_1^2 + \xi_2^2 + \xi_3^2 = 1$, and $\tilde\Xi = \boldsymbol{\xi}$ is a real root. The real roots are therefore the case $\boldsymbol{\xi}' = 0$ of the non-trivial formula, and not a separate construction.

**The trivial roots as a separate family.** The trivial roots $\tilde\Xi = \pm i$ have vanishing vector part. The real roots (with $\boldsymbol\Xi = \boldsymbol{\xi} \neq 0$) and the non-trivial roots (with $\boldsymbol\Xi = \boldsymbol{\xi} + i\boldsymbol{\xi}'$, whose real part $\boldsymbol{\xi}$ is nonzero since $\xi_1^2 + \xi_2^2 + \xi_3^2 = 1 + \xi'^2_1 + \xi'^2_2 + \xi'^2_3 \geq 1$) all have nonvanishing vector part. So the roots with vanishing vector part are exactly $\pm i$, and they form a separate family.

### Status of the Roots

Counting the free real parameters: the trivial roots are two isolated elements, the real roots are a two-real-parameter family (three real coefficients carrying one constraint), and the non-trivial roots are a four-real-parameter family (six real coefficients carrying two constraints).

All roots except the trivial ones are **pure** (their scalar part vanishes), hence lie in the six-real-dimensional vector subspace of pure biquaternions. The roots are neither idempotents ($\tilde\Xi^2 = -1 \neq \tilde\Xi$) nor zero divisors (§*The Roots as Invertible Elements*).

## The Roots of Zero

### Reduction to Two Cases

A **root of $0$** is an element $\tilde\Xi \in \mathbb{B}$ with $\tilde\Xi^2 = 0$. With $\tilde\Xi = \Xi_0 e_0 + \boldsymbol\Xi$ the square is $\tilde\Xi^2 = (\Xi_0^2 - (\boldsymbol\Xi,\boldsymbol\Xi))e_0 + 2\Xi_0\boldsymbol\Xi$ (§*The Problem and Its Reduction*), and equating it to $0$ gives

$$
2\Xi_0\boldsymbol\Xi = 0, \qquad \Xi_0^2 - (\boldsymbol\Xi,\boldsymbol\Xi) = 0 .
$$

The first equation is the same vector equation as for the roots of $-1$, and again forces $\Xi_0 = 0$ or $\boldsymbol\Xi = 0$.

**Case A — the root is a complex scalar ($\boldsymbol\Xi = 0$).** Then $\tilde\Xi = \Xi_0 e_0$ and $\Xi_0^2 = 0$; since $\mathbb{C}$ is a field, $\Xi_0 = 0$. **The root in this case is the single element**

$$
\tilde\Xi = 0 .
$$

**Case B — the root is pure ($\Xi_0 = 0$).** Then $\tilde\Xi = \boldsymbol\Xi$ and $(\boldsymbol\Xi,\boldsymbol\Xi) = 0$, that is

$$
\tilde\Xi = \Xi_1e_1 + \Xi_2e_2 + \Xi_3e_3, \qquad \Xi_1^2 + \Xi_2^2 + \Xi_3^2 = 0 .
$$

**The roots in this case are the pure biquaternions of vanishing complex square**, a four-real-parameter family; writing $\Xi_k = \xi_k + i\xi'_k$, the condition is the pair of real equations $\xi_1^2+\xi_2^2+\xi_3^2-\xi'^2_1-\xi'^2_2-\xi'^2_3 = 0$ and $\xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3 = 0$.

### Statement of the Theorem

**Theorem.** The roots of $0$ in $\mathbb{B}$ are exactly the following.

**The zero element.**

$$
\tilde\Xi = 0 .
$$

**The nilpotent cone.** The pure biquaternions of vanishing complex square, a four-real-parameter family,

$$
\tilde\Xi = \Xi_1e_1 + \Xi_2e_2 + \Xi_3e_3, \qquad \Xi_1^2 + \Xi_2^2 + \Xi_3^2 = 0,
$$

that is, writing $\Xi_k = \xi_k + i\xi'_k$, the pair of real equations $\xi_1^2+\xi_2^2+\xi_3^2-\xi'^2_1-\xi'^2_2-\xi'^2_3 = 0$ and $\xi_1\xi'_1+\xi_2\xi'_2+\xi_3\xi'_3 = 0$. Its nonzero elements are the nilpotents of the algebra.

### Verification

For a pure $\tilde\Xi$ with $(\boldsymbol\Xi,\boldsymbol\Xi) = 0$ the scalar part of $\tilde\Xi^2$ is $-(\boldsymbol\Xi,\boldsymbol\Xi) = 0$ and the vector part is $2\Xi_0\boldsymbol\Xi = 0$, and the two cases are exhaustive by the reduction above.

The nonzero roots of $0$ are exactly the **nilpotents** of the algebra, written $\tilde\Upsilon$ where the nilpotency is the point (§*The nilpotent convention* of *Conventions in Mathematics*), and they form the **nilpotent cone** of the pure subspace. An example is $\tilde\Xi = e_1 + ie_2$, for which

$$
(e_1+ie_2)^2 = e_1^2 + i^2e_2^2 + i(e_1e_2+e_2e_1) = -1 + 1 + 0 = 0 .
$$

The set is the **nilpotent** family of the zero-divisor set of $\mathbb{B}$; the whole zero-divisor set — the elements on which the central square $\tilde Q\tilde Q^{\natural}$ vanishes, which splits into these nilpotents and the non-pure zero divisors — its two families and the criterion in terms of the scalar part, are the subject of *Zero Divisors of the General Plain Algebra*. It is named here only to complete the list of the three central values, and not developed.

## The Roots of Plus One

### Statement of the Theorem

A **root of $+1$** is an element $\tilde\Xi_+ \in \mathbb{B}$ satisfying $\tilde\Xi_+^2 = 1$. The roots of $+1$ are related to the roots of $-1$ by

$$
\tilde\Xi_+ = \tilde\Xi i,
$$

where $\tilde\Xi$ is a root of $-1$. **The roots of $+1$ are exactly the following three families.**

**The trivial roots.** The two elements

$$
\tilde\Xi_+ = +1, \qquad \tilde\Xi_+ = -1,
$$

the images of $\tilde\Xi = \pm i$. They are the only roots of $+1$ that lie in the centre $\mathbb{C}$.

**The real roots.** The images of the real roots of $-1$: the elements

$$
\tilde\Xi_+ = \pm\boldsymbol{\xi}i, \qquad \boldsymbol{\xi} = \xi_1e_1 + \xi_2e_2 + \xi_3e_3, \qquad \xi_1^2 + \xi_2^2 + \xi_3^2 = 1,
$$

where $\boldsymbol{\xi}$ is a pure real quaternion of unit length. Each one is a root of $+1$, since

$$
(\boldsymbol{\xi}i)^2 = \boldsymbol{\xi}^2 i^2 = (-1)(-1) = 1 .
$$

Spelled out, the family is $\tilde\Xi_+ = \pm(\xi_1e_1 + \xi_2e_2 + \xi_3e_3)i$ with $\xi_1^2 + \xi_2^2 + \xi_3^2 = 1$: the same real unit vectors of the roots of $-1$, mapped by $\boldsymbol{\xi} \mapsto \boldsymbol{\xi}i$. It is a **two-real-parameter family**, and its elements are the only roots of $+1$ that are pure multiples of a real quaternion.

**The non-trivial roots.** The four-real-parameter family

$$
\tilde\Xi_+ = (\boldsymbol{\xi} + i\boldsymbol{\xi}') i = \boldsymbol{\xi}i - \boldsymbol{\xi}', \qquad \boldsymbol{\xi}' \neq 0,
$$

whose six real coefficients satisfy $\xi_1^2 + \xi_2^2 + \xi_3^2 - \xi'^2_1 - \xi'^2_2 - \xi'^2_3 = 1$ and $\xi_1\xi'_1 + \xi_2\xi'_2 + \xi_3\xi'_3 = 0$.

### Verification

That $\tilde\Xi_+ = \tilde\Xi i$ is a root of $+1$ follows from

$$
(\tilde\Xi i)^2 = \tilde\Xi^2 i^2 = (-1)(-1) = 1,
$$

and the map $\tilde\Xi \mapsto \tilde\Xi i$ is a bijection from the roots of $-1$ to the roots of $+1$: it is injective since $i$ is invertible, and if $\tilde\Xi_+^2 = 1$ then $\tilde\Xi = -\tilde\Xi_+ i$ satisfies $\tilde\Xi^2 = -1$ and $\tilde\Xi i = \tilde\Xi_+$.

The roots of $+1$ are not used in the classification of the idempotents, but they appear in the theory of the biquaternion exponential and in the theory of the biquaternion logarithm.

## The Three Sets Compared

The three root sets are related by their invertibility. The roots of $-1$ and of $+1$ are **units**: a root $\tilde\Xi$ of $\pm 1$ satisfies $\tilde\Xi^{-1} = \pm\tilde\Xi$, in $\mathbb{B}^\times$. The nonzero roots of $0$ are the exception: they are nilpotents, hence zero divisors and not units. So of the three central values only $0$ has non-unit roots.

The three sets also differ in kind. The roots of $-1$ are two isolated elements together with a two-parameter family and a four-parameter family; the roots of $+1$ are the bijective image of that set under $\tilde\Xi \mapsto \tilde\Xi i$; and the roots of $0$ are the single element $0$ together with one four-parameter family, the nilpotent cone. In particular the roots of $0$ contain no unit, and the only non-pure roots of the three values are the trivial ones, $\pm i$ for $-1$ and $\pm 1$ for $+1$.

## The Relation to the Idempotents

The classification of the roots of $-1$ gives the classification of the idempotents of $\mathbb{B}$: the map

$$
\tilde\Xi \longmapsto \tilde\Pi_1(\tilde\Xi) = \tfrac{1}{2}(e_0 + \tilde\Xi i)
$$

is a bijection from the set of roots of $-1$ onto the set of idempotents, under which the complementary pairs $\{\tilde\Pi, e_0 - \tilde\Pi\}$ correspond to the classes $\{\tilde\Xi, -\tilde\Xi\}$, and under which the three families of roots give the trivial idempotents, the Hermitian idempotents in $\mathbb{M}_+$, and the idempotents lying in none of the four four-dimensional subspaces. The construction of the idempotent, the proof of the bijection and the projection interpretation are the subject of *Idempotents of the General Plain Algebra*.

## The Relation to the Zero Divisors

### The Idempotents as Zero Divisors

Every non-trivial idempotent is a zero divisor, $\tilde\Pi(e_0 - \tilde\Pi) = 0$ with both factors nonzero (the construction of $\tilde\Pi$ is in *Idempotents of the General Plain Algebra*). The trivial idempotents $0$ and $e_0$ are not zero divisors: $0$ is excluded by the definition, and $e_0$ is a unit.

### The Roots as Invertible Elements

A root of $-1$ is a unit and **not** a zero divisor. Indeed, $\tilde\Xi^2 = -1$ gives

$$
\tilde\Xi\,(-\tilde\Xi) = (-\tilde\Xi)\,\tilde\Xi = e_0,
$$

so $\tilde\Xi$ is invertible, with inverse $\tilde\Xi^{-1} = -\tilde\Xi$. A unit is not a zero divisor: if $\tilde\Xi \tilde Q = 0$ for some $\tilde Q$, then $\tilde Q = (-\tilde\Xi)(\tilde\Xi \tilde Q) = 0$, and the same argument applies to $\tilde Q\tilde\Xi = 0$. Hence the roots of $-1$ lie in the group of units $\mathbb{B}^\times$. The central scalar $\tilde\Xi \tilde\Xi^{\natural}$ is $-1$ for the trivial roots and $+1$ for a pure root.

## Summary

This article determines the square roots of the three central values $-1$, $0$ and $+1$ in the biquaternion algebra, by one reduction applied three times: writing $\tilde\Xi = \Xi_0 e_0 + \boldsymbol\Xi$ and using the product formula $\tilde\Xi^2 = (\Xi_0^2 - (\boldsymbol\Xi,\boldsymbol\Xi))e_0 + 2\Xi_0\boldsymbol\Xi$, the vector part forces $\Xi_0 = 0$ or $\boldsymbol\Xi = 0$, and the scalar part then gives the equation of the value.

The square roots of $-1$ are exactly:

1. **Trivial roots:** $\tilde\Xi = \pm i$.
2. **Real roots:** $\tilde\Xi = \pm\boldsymbol{\xi}$, where $\boldsymbol{\xi}$ is a pure real quaternion with $\boldsymbol{\xi}^2 = -1$.
3. **Non-trivial roots:** $\tilde\Xi = \boldsymbol{\xi} + i\boldsymbol{\xi}'$, where $\boldsymbol{\xi}' \neq 0$ and the two real conditions $\xi_1^2 + \xi_2^2 + \xi_3^2 - \xi'^2_1 - \xi'^2_2 - \xi'^2_3 = 1$ and $\xi_1\xi'_1 + \xi_2\xi'_2 + \xi_3\xi'_3 = 0$ hold.

The scalar case gives the trivial roots. The pure case reduces to $(\boldsymbol\Xi, \boldsymbol\Xi) = 1$, which splits into the real and non-trivial families according to whether the imaginary part $\boldsymbol{\xi}'$ of the pure biquaternion vanishes. The trivial roots are the two elements $\pm i$. The real roots are the family $\pm\boldsymbol{\xi}$ cut out by the single constraint $\xi_1^2 + \xi_2^2 + \xi_3^2 = 1$, leaving two free real parameters. The non-trivial roots are the elements $\boldsymbol{\xi} + i\boldsymbol{\xi}'$ cut out by the two constraints $\xi_1^2 + \xi_2^2 + \xi_3^2 - \xi'^2_1 - \xi'^2_2 - \xi'^2_3 = 1$ and $\xi_1\xi'_1 + \xi_2\xi'_2 + \xi_3\xi'_3 = 0$, four free real parameters in all. All roots except the trivial ones are pure, hence lie in the six-real-dimensional vector subspace of pure biquaternions.

The square roots of $0$ are the element $0$ together with the pure biquaternions $\tilde\Xi = \Xi_1e_1+\Xi_2e_2+\Xi_3e_3$ with $\Xi_1^2+\Xi_2^2+\Xi_3^2=0$, a four-real-parameter nilpotent cone whose nonzero elements are the nilpotents of the algebra, for example $e_1+ie_2$. Unlike the roots of $-1$ and $+1$, which are units, the nonzero roots of $0$ are zero divisors; the full structure of the cone, and the classification of the zero divisors it is part of, are in *Zero Divisors of the General Plain Algebra*, and the classification of $\tilde\Xi^2=\tilde Q$ for a general $\tilde Q$ is in *Square Roots of a General Element in the General Plain Algebra*.

The square roots of $+1$ are obtained from the roots of $-1$ by multiplication by $i$: $\tilde\Xi_+ = \tilde\Xi i$. They are not used in the idempotent classification, but they appear in the theory of the biquaternion exponential.

The classification of the roots of $-1$ gives the classification of the idempotents of $\mathbb{B}$, which are of the form $\tfrac{1}{2} e_0 \pm \tfrac{1}{2} \tilde\Xi i$. The map $\tilde\Xi \mapsto \tilde\Pi_1(\tilde\Xi) = \tfrac{1}{2}(e_0 + \tilde\Xi i)$ is a bijection from the roots of $-1$ to the idempotents; complementary pairs of idempotents correspond to roots modulo the sign identification $\tilde\Xi \sim -\tilde\Xi$. The non-trivial idempotents form a four-real-parameter family, and are used in the classification of the non-pure zero divisors. The roots themselves are units, and they lie in the group of units $\mathbb{B}^\times$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis |
| $i$ | Scalar imaginary |
| $\tilde\Xi$ | A biquaternion; here the root of $-1$ or of $0$ |
| $\tilde\Xi_+$ | The root of $+1$ |
| $\tilde Q$ | A second biquaternion, the element whose roots are sought in the general problem |
| $\Xi_k = \xi_k + i\xi'_k$, $k=0,\dots,3$ | Complex components of the root, $\Xi_k \in \mathbb{C}$; the scalar part is $\Xi_0 e_0$ |
| $\boldsymbol\Xi = \Xi_1e_1+\Xi_2e_2+\Xi_3e_3$ | Complex vector part of the root |
| $\boldsymbol{\xi}, \boldsymbol{\xi}'$ | Its real and imaginary parts, $\boldsymbol\Xi = \boldsymbol{\xi} + i\boldsymbol{\xi}'$ |
| $\tilde\Pi = \tfrac{1}{2} e_0 \pm \tfrac{1}{2} \tilde\Xi i$ | Idempotent |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original discovery of the biquaternions.
- S. J. Sangwine, "Biquaternion (complexified quaternion) roots of $-1$", *Advances in Applied Clifford Algebras* **16** (2006) 63–68, for the original classification.
- S. J. Sangwine and D. Alfsmann, "Determination of the biquaternion divisors of zero, including the idempotents and nilpotents", *Advances in Applied Clifford Algebras* **20** (2010) 401–416, for the relation to the idempotents and the zero divisors.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the constraint verification.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, Dordrecht, 1997), for the algebraic properties of the biquaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- A. Acus and A. Dargys, *Square roots of complexified quaternions*, arXiv:2601.08391 (2026), for the square roots of an arbitrary complexified quaternion, the subject of *Square Roots of a General Element in the General Plain Algebra*.
