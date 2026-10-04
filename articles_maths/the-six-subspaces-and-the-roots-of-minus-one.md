# __The Six Subspaces and the Roots of Minus One__

## Introduction

A **root of $-1$** in $\mathbb{B}$ is an element $\tilde\Xi$ with $\tilde\Xi^2 = -1$, the element $-1$ being understood as $-e_0$. The classification is in *Biquaternion Square Roots of Minus One, Zero and Plus One*, and it has three families: the two **trivial roots** $\pm i$, the **real roots**, which are the pure real quaternions of unit length, a two-parameter family, and the **non-trivial roots**, a four-parameter family of pure elements whose two real vector parts are orthogonal and whose squared lengths differ by one. The subject here is what that classification looks like inside the six distinguished subspaces.

Two of the families are easy to place. Every root except the trivial ones is **pure**, by the classification, so it lies in the vector subspace; and the trivial roots are central scalars, so they lie in the centre. **Every root of $-1$ lies in the centre or in the vector subspace**, and no root lies outside their union.

Which of the six contain one is then decided by a short computation in each case, and the answer is this.

| subspace | the roots of $-1$ in it |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\pm i$, the two trivial roots |
| $\mathrm{Vect}(\mathbb{B})$ | every pure root: the unit real sphere and the four-parameter non-trivial family |
| $\mathbb{H}_{\mathbb{B}}$ | the unit real sphere |
| $i\mathbb{H}_{\mathbb{B}}$ | $\pm i$ |
| $\mathbb{M}_+$ | none |
| $\mathbb{M}_-$ | $\pm i$ and the unit real sphere |

Three features of the table are worth naming before the computations. First, the family appearing in three different subspaces — the **unit real sphere**, the pure real quaternions of length one — is the same set each time, living in the intersection $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$, which is the real vector triple $\operatorname{span}\{e_1, e_2, e_3\}$. Second, the trivial roots $\pm i$ appear in three subspaces as well, this time in $\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$, which is the imaginary axis $\operatorname{span}\{ie_0\}$. Third, $\mathbb{M}_+$ contains no root of $-1$ at all, and the four-parameter family is confined to the vector subspace.

Two facts about the roots are used repeatedly. Every root of $-1$ is a **unit**, with $\tilde\Xi^{-1} = -\tilde\Xi$, so no root is a zero divisor; and the roots are related to the **idempotents** by $\tilde\Pi = \tfrac{1}{2}(e_0 + \tilde\Xi i)$, so that the trivial roots give the idempotents $0$ and $e_0$, the real roots give the Hermitian idempotents of $\mathbb{M}_+$, and the non-trivial roots give the idempotents lying in none of the four four-dimensional subspaces. Both are in *Biquaternion Square Roots of Minus One, Zero and Plus One* and *The Six Subspaces and the Idempotents and Projections*.

## The Centre Subspace

A central element is $\tilde\Xi = Q_0e_0$ with $Q_0 \in \mathbb{C}$, and $\tilde\Xi^2 = Q_0^2e_0 = -e_0$ holds exactly when $Q_0^2 = -1$, that is $Q_0 = \pm i$. So the centre contains the two trivial roots and nothing else:

$$
\tilde\Xi = \pm ie_0 = \pm i .
$$

These are the only roots of $-1$ with a nonvanishing scalar part, and so the only ones that are not pure. They are also the only roots that are not in the vector subspace.

## The Vector Subspace

A pure element is $\tilde\Xi = \mathbf{P} = P_1e_1 + P_2e_2 + P_3e_3$ with complex coefficients, and $\mathbf{P}^2 = -(\mathbf{P},\mathbf{P})e_0$, so $\tilde\Xi^2 = -e_0$ is the single complex equation

$$
(\mathbf{P},\mathbf{P}) = P_1^2 + P_2^2 + P_3^2 = 1 .
$$

This is the equation whose solutions are the **pure roots**, and the whole of them, of both kinds, lies here: the vector subspace contains every root of $-1$ that is not one of the trivial pair. Writing $\mathbf{P} = \boldsymbol{\rho} + i\boldsymbol{\rho}'$ with $\boldsymbol{\rho}, \boldsymbol{\rho}'$ real, the equation is the pair

$$
(\boldsymbol{\rho},\boldsymbol{\rho}) - (\boldsymbol{\rho}',\boldsymbol{\rho}') = 1 , \qquad (\boldsymbol{\rho},\boldsymbol{\rho}') = 0 ,
$$

whose solutions with $\boldsymbol{\rho}' = 0$ are the **real roots**, the vectors $\boldsymbol{\rho}$ of length one, a two-parameter family, and whose solutions with $\boldsymbol{\rho}' \neq 0$ are the **non-trivial roots**, a four-parameter family, the two real parts orthogonal and their squared lengths differing by one,

$$
(\boldsymbol{\rho},\boldsymbol{\rho}) = (\boldsymbol{\rho}',\boldsymbol{\rho}') + 1 , \qquad (\boldsymbol{\rho},\boldsymbol{\rho}') = 0 .
$$

The vector subspace is the only one of the six in which all three central equations have solutions: roots of $-1$ as units, the nilpotents $\mathbf{P}^2 = 0$ as the pure solutions of $(\mathbf{P},\mathbf{P}) = 0$, and roots of $+1$ as the pure solutions of $(\mathbf{P},\mathbf{P}) = -1$. So $\mathrm{Vect}(\mathbb{B})$ carries roots of $-1$ as units and roots of $0$ as zero divisors at the same time, the two opposite kinds of element of the algebra meeting in this one subspace.

## The Quaternion Subspace

A real quaternion is $\tilde\Xi = h_0e_0 + \boldsymbol{\rho}$ with $h_0 \in \mathbb{R}$ and $\boldsymbol{\rho}$ a **real** vector, and its square is $(h_0^2 - (\boldsymbol{\rho},\boldsymbol{\rho}))e_0 + 2h_0\boldsymbol{\rho}$. Setting this equal to $-e_0$ gives the pair

$$
2h_0\boldsymbol{\rho} = 0 , \qquad h_0^2 - (\boldsymbol{\rho},\boldsymbol{\rho}) = -1 .
$$

The first equation gives $\boldsymbol{\rho} = 0$ or $h_0 = 0$. With $\boldsymbol{\rho} = 0$ the second reads $h_0^2 = -1$, impossible for a real $h_0$; with $h_0 = 0$ it reads $(\boldsymbol{\rho},\boldsymbol{\rho}) = 1$. So the roots of $-1$ in the quaternion subspace are

$$
\tilde\Xi = \boldsymbol{\rho} , \qquad \boldsymbol{\rho} \in \mathbb{R}^3 , \quad (\boldsymbol{\rho},\boldsymbol{\rho}) = 1 ,
$$

the **unit real sphere** and nothing else. These are the classical imaginary units of the quaternions, and their absence of a scalar part is what excludes the trivial roots: $\pm i$ has vanishing vector part and is not a real quaternion.

## The Anti-Quaternion Subspace

An element of $i\mathbb{H}_{\mathbb{B}}$ is $\tilde\Xi = ih$ with $h = h_0e_0 + \boldsymbol{\rho}$ a real quaternion, and $\tilde\Xi^2 = -h^2 = ((\boldsymbol{\rho},\boldsymbol{\rho}) - h_0^2)e_0 - 2h_0\boldsymbol{\rho}$. Setting this equal to $-e_0$ gives

$$
2h_0\boldsymbol{\rho} = 0 , \qquad (\boldsymbol{\rho},\boldsymbol{\rho}) - h_0^2 = -1 .
$$

The first equation again forces $\boldsymbol{\rho} = 0$ or $h_0 = 0$. With $h_0 = 0$ the second reads $(\boldsymbol{\rho},\boldsymbol{\rho}) = -1$, impossible for a real vector; with $\boldsymbol{\rho} = 0$ it reads $h_0^2 = 1$, so $h_0 = \pm 1$ and

$$
\tilde\Xi = \pm i .
$$

**The anti-quaternion subspace contains the two trivial roots and no others.** The sign is the opposite of the quaternion subspace's, and it is exactly the sign that admits $\pm i$ here and excludes the unit real sphere: the imaginary unit $i = ie_0$ lies in $i\mathbb{H}_{\mathbb{B}}$, while it does not lie in $\mathbb{H}_{\mathbb{B}}$.

## The Hermitian Subspace

A Hermitian element is $\tilde\Xi = a_0e_0 + i\mathbf{p}$ with $a_0 \in \mathbb{R}$ and $\mathbf{p}$ a real vector, and its square is $(a_0^2 + (\mathbf{p},\mathbf{p}))e_0 + 2ia_0\mathbf{p}$. Setting this equal to $-e_0$ gives

$$
2a_0\mathbf{p} = 0 , \qquad a_0^2 + (\mathbf{p},\mathbf{p}) = -1 .
$$

The second equation is a sum of two real squares equal to $-1$ unless both terms vanish, and then it reads $0 = -1$. **The Hermitian subspace contains no root of $-1$.** No separate discussion of the two cases is needed: $a_0^2 + (\mathbf{p},\mathbf{p})$ is a sum of squares of real numbers, hence nonnegative, and $-1$ is not.

This is the sharpest of the two negative cases, because the Hermitian subspace is where the idempotents live. The idempotents are built from the roots, $\tilde\Pi = \tfrac{1}{2}(e_0 + \tilde\Xi i)$, but it is $\tilde\Xi i$, not $\tilde\Xi$, that lies in $\mathbb{M}_+$ when $\tilde\Xi$ is a real root: $\tilde\Xi i$ is then a root of $+1$ of the Hermitian subspace, and the roots of $+1$ in $\mathbb{M}_+$ are $\pm e_0$ and the imaginary unit vectors $i\mathbf{p}$ with $\mathbf{p}$ of length one, which is exactly the statement that the idempotents of $\mathbb{M}_+$ are $0$, $e_0$ and $\tfrac{1}{2}(e_0 + i\mathbf{u})$ over real unit vectors. So the roots of $-1$ do not touch $\mathbb{M}_+$; their images under multiplication by $i$ are what $\mathbb{M}_+$ is made of.

## The Anti-Hermitian Subspace

An anti-Hermitian element is $\tilde\Xi = ib_0e_0 + \mathbf{q}$ with $b_0 \in \mathbb{R}$ and $\mathbf{q}$ a real vector, and its square is $-(b_0^2 + (\mathbf{q},\mathbf{q}))e_0 + 2ib_0\mathbf{q}$. Setting this equal to $-e_0$ gives

$$
2b_0\mathbf{q} = 0 , \qquad b_0^2 + (\mathbf{q},\mathbf{q}) = 1 .
$$

The first equation gives $\mathbf{q} = 0$ or $b_0 = 0$, and both alternatives are now possible. With $\mathbf{q} = 0$ the second reads $b_0^2 = 1$, giving the trivial roots $\pm i$; with $b_0 = 0$ it reads $(\mathbf{q},\mathbf{q}) = 1$, giving the unit real sphere. So the anti-Hermitian subspace contains

$$
\tilde\Xi = \pm i \qquad \text{and} \qquad \tilde\Xi = \mathbf{q} , \quad \mathbf{q} \in \mathbb{R}^3 , \quad (\mathbf{q},\mathbf{q}) = 1 ,
$$

both families at once. It is the only one of the six besides the vector subspace to contain roots of $-1$ of both the trivial and the pure kind, and it is the meeting place of the two: the trivial roots lie in $\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$ and the real roots in $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$.

## The Other Two Central Values

The same computation can be read at the other two central values, and the result is a companion table.

**The roots of $0$** are $0$ and the **nilpotent cone**, by *Biquaternion Square Roots of Minus One, Zero and Plus One*; the nonzero ones are the pure solutions of $(\mathbf{P},\mathbf{P}) = 0$, so they lie in the vector subspace and nowhere else. Each of the six contains $0$, and only the vector subspace contains any other root of $0$.

**The roots of $+1$** are the images $\tilde\Xi i$ of the roots of $-1$, the map $\tilde\Xi \mapsto \tilde\Xi i$ being a bijection. Multiplication by $i$ carries the six to the six — it fixes the centre and the vector subspace and interchanges $\mathbb{H}_{\mathbb{B}}$ with $i\mathbb{H}_{\mathbb{B}}$, and $\mathbb{M}_+$ with $\mathbb{M}_-$ — so the table for $+1$ is the table for $-1$ transported by that interchange:

| subspace | the roots of $+1$ in it |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\pm 1$ |
| $\mathrm{Vect}(\mathbb{B})$ | the images of the pure roots |
| $\mathbb{H}_{\mathbb{B}}$ | $\pm 1$ |
| $i\mathbb{H}_{\mathbb{B}}$ | the imaginary unit quaternions $i\mathbf{p}$ with $(\mathbf{p},\mathbf{p}) = 1$ |
| $\mathbb{M}_+$ | $\pm 1$ and the imaginary unit quaternions |
| $\mathbb{M}_-$ | none |

So of the four four-dimensional subspaces, $\mathbb{M}_-$ is the one that carries roots of $-1$ and no root of $+1$, $\mathbb{M}_+$ is the one that carries roots of $+1$ and no root of $-1$, and $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ are exchanged by the multiplication by $i$ that trades the two values. The centre carries the trivial roots of both.

## Summary

A root of $-1$ is an element of square $-e_0$, of which the algebra has three families: the two trivial roots $\pm i$, the unit real sphere, and the four-parameter non-trivial family of pure elements whose real vector parts are orthogonal and whose squared lengths differ by one. Every root of $-1$ lies in the centre or in the vector subspace, and every root except the trivial pair is pure. The centre contains the two trivial roots and no others; the vector subspace contains every pure root, hence the whole of the unit real sphere and the whole of the non-trivial family, and it is the only subspace in which the roots of $-1$ meet the nilpotents, the roots of $0$; the quaternion subspace contains the unit real sphere and no other root, the trivial roots being excluded for want of a vector part; the anti-quaternion subspace contains the trivial roots and no other, the sphere being excluded by the sign; the Hermitian subspace contains no root of $-1$ at all, because its elements square to a sum of real squares; and the anti-Hermitian subspace contains both the trivial roots and the unit real sphere. The unit real sphere lies in the triple intersection $\mathrm{Vect}(\mathbb{B}) \cap \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$, which is the real vector triple, and the trivial roots lie in $\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-$, which is the imaginary axis. Every root of $-1$ is a unit, and none is a zero divisor; the idempotents are built from the roots by $\tilde\Pi = \tfrac{1}{2}(e_0 + \tilde\Xi i)$, the trivial roots giving the trivial idempotents, the real roots the Hermitian idempotents of $\mathbb{M}_+$, and the non-trivial roots the idempotents lying in none of the four four-dimensional subspaces. The classification itself, and the parallel treatment of the roots of $0$ and of $+1$, are the business of *Biquaternion Square Roots of Minus One, Zero and Plus One*; what is added here is the restriction to the six.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $\tilde\Xi$ | a root of a central value |
| $\boldsymbol{\rho}, \boldsymbol{\rho}'$ | the real and imaginary parts of a complex vector |
| $h_0, a_0, b_0, \mathbf{p}, \mathbf{q}$ | real scalar parts and real vectors of $\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_\pm$ |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section
- *The Six Subspaces and the Idempotents and Projections* (`articles_maths/the-six-subspaces-and-the-idempotents-and-projections.md`), for the idempotents the roots build
- *The Six Subspaces and the Zero Divisors* (`articles_maths/the-six-subspaces-and-the-zero-divisors.md`), for the nilpotents, which are the roots of $0$ in the vector subspace
- *The Six Subspaces and the Ideals* (`articles_maths/the-six-subspaces-and-the-ideals.md`), for the units and the minimal ideals that the elements of the vector subspace generate
- *Biquaternion Square Roots of Minus One, Zero and Plus One* (`articles_maths/biquaternion-square-roots-of-minus-one-zero-and-plus-one.md`), for the three classifications in the whole algebra
- *Biquaternion Idempotents and Projections* (`articles_maths/biquaternion-idempotents-and-projections.md`), for the bijection between the roots and the idempotents
