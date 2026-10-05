# __The Six Subspaces and the Units__

## Introduction

An element of the biquaternion algebra is a **unit** if it has a two-sided inverse in the algebra. The algebra is associative with a unit and of finite dimension, and its units are characterized by a central element, the norm. Write $Q^{\natural} = Q_0e_0 - Q_1e_1 - Q_2e_2 - Q_3e_3$ for quaternion conjugation, and

$$
N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 ,
$$

so that $N(\tilde{Q})$ is central, is the sum of the squares of the four complex coefficients, and is the norm of the algebra. Then

$$
\tilde{Q} \tilde{Q}^{\natural} = \tilde{Q}^{\natural}\tilde{Q} = N(\tilde{Q})e_0 , \qquad \tilde{Q}^{-1} = \frac{\tilde{Q}^{\natural}}{N(\tilde{Q})} \quad \text{when } N(\tilde{Q}) \neq 0 .
$$

**Theorem (invertibility).** An element $\tilde{Q}$ is a unit if and only if $N(\tilde{Q}) \neq 0$; if $N(\tilde{Q}) = 0$ and $\tilde{Q} \neq 0$, then $\tilde{Q}$ is a zero divisor, since $\tilde{Q}\tilde{Q}^{\natural} = 0$ exhibits a nonzero element multiplied by $\tilde{Q}$ into zero.

The norm is multiplicative, $N(\tilde{P}\tilde{Q}) = N(\tilde{P})N(\tilde{Q})$, so the units are closed under the product and form a group with the identity $e_0$. This article records which elements of each of the six distinguished subspaces are units, and which of the six contain no nonzero zero divisor at all. The six subspaces are those of *Introduction to the Six Subspaces*; the algebra's own treatment of the norm, of invertibility and of the unit group is in *Biquaternion Norm and Invertibility* and in *Biquaternion Zero Divisors*, and only the restriction to the six is here.

Writing an element of each subspace in its coordinates and evaluating $N$ gives the criterion of the following table. Here $A \in \mathbb{C}$ is a complex number and $\mathbf{p}, \mathbf{q} \in \mathbb{R}^3$ are **real** vectors, for which $(\mathbf{p},\mathbf{p})$ is the sum of the squares of the three real coordinates; for a complex vector $\mathbf{P}$ the symbol $(\mathbf{P},\mathbf{P})$ is the complex dot product, the sum of the squares of the three complex coordinates without conjugation.

| subspace | element | $N$ | it is a unit exactly when |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Ae_0$ | $A^2$ | $A \neq 0$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathbf{P}$ | $(\mathbf{P},\mathbf{P})$ | $(\mathbf{P},\mathbf{P}) \neq 0$ |
| $\mathbb{H}_{\mathbb{B}}$ | $h$ | $h_0^2 + h_1^2 + h_2^2 + h_3^2$ | $h \neq 0$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $ih$ | $-(h_0^2 + h_1^2 + h_2^2 + h_3^2)$ | $h \neq 0$ |
| $\mathbb{M}_+$ | $a_0e_0 + i\mathbf{p}$ | $a_0^2 - (\mathbf{p},\mathbf{p})$ | $a_0^2 \neq (\mathbf{p},\mathbf{p})$ |
| $\mathbb{M}_-$ | $ib_0e_0 + \mathbf{q}$ | $(\mathbf{q},\mathbf{q}) - b_0^2$ | $(\mathbf{q},\mathbf{q}) \neq b_0^2$ |

**Theorem (the three without a zero divisor).** The centre, the quaternion subspace and the anti-quaternion subspace contain no nonzero zero divisor: every nonzero element of any of the three is a unit. The vector subspace, the Hermitian subspace and the anti-Hermitian subspace each contain nonzero zero divisors.

**Proof.** In the first three the norm vanishes only at the zero element: $A^2 = 0$ forces $A = 0$ in the centre, and the real sum of squares $h_0^2 + h_1^2 + h_2^2 + h_3^2$, with its negative, forces $h = 0$ in the quaternion and the anti-quaternion subspaces. In the last three the norm is a difference, so it vanishes on nonzero elements: $e_1 + ie_2$ in the vector subspace, $e_0 + ie_1$ in the Hermitian subspace and $ie_0 + e_1$ in the anti-Hermitian subspace, each computed below.

## The Centre Subspace

The norm of a central element is the square of its complex coordinate:

$$
N(Ae_0) = A^2 , \qquad (Ae_0)^{-1} = A^{-1}e_0 \ (A \neq 0) .
$$

Every nonzero central element is a unit, so the centre has no nonzero zero divisor, and it is the field $\mathbb{C}_{\mathbb{B}}$. It is the first of the three subspaces of the theorem.

## The Vector Subspace

The norm of a pure vector is the complex dot product of the vector with itself:

$$
N(\mathbf{P}) = (\mathbf{P},\mathbf{P}) = P_1^2 + P_2^2 + P_3^2 .
$$

A pure vector is a unit exactly when $(\mathbf{P},\mathbf{P}) \neq 0$. Since a pure vector satisfies $\mathbf{P}^2 = -(\mathbf{P},\mathbf{P})e_0$, the nonzero non-units of the vector subspace are exactly its **square-zero** elements:

$$
(\mathbf{P},\mathbf{P}) = 0 \iff \mathbf{P}^2 = 0 .
$$

An explicit example is $\mathbf{P} = e_1 + ie_2$, whose square vanishes:

$$
(e_1 + ie_2)^2 = e_1^2 + e_1(ie_2) + (ie_2)e_1 + (ie_2)^2 = -e_0 + ie_3 - ie_3 + e_0 = 0 .
$$

The vector subspace therefore contains nonzero zero divisors, and the condition $(\mathbf{P},\mathbf{P}) = 0$ singles out its nonzero non-units. The conjugation $\mathbf{P}^{\natural} = -\mathbf{P}$ is nonzero whenever $\mathbf{P}$ is, so for a square-zero $\mathbf{P}$ the pair $\mathbf{P}, -\mathbf{P}$ is a pair of nonzero elements of the vector subspace with vanishing product.

## The Quaternion Subspace

On the quaternion subspace the coefficients are real, so the norm is a sum of four squares:

$$
N(h) = h_0^2 + h_1^2 + h_2^2 + h_3^2 , \qquad N(h) = 0 \iff h = 0 .
$$

Every nonzero element of the quaternion subspace is therefore a unit, and the subspace is a **division algebra**, as it must be: it is the image of the real quaternion algebra, which is a division algebra, under $h \mapsto he_0$. The inverse of $h$ is $h^{\natural}/N(h)$ with $N(h) > 0$ real, which is the classical formula. The quaternion subspace is one of the three without a nonzero zero divisor, and the only one of them that is not commutative.

## The Anti-Quaternion Subspace

An element of the anti-quaternion subspace is $i$ times a real quaternion, and the norm is the negative of a sum of four squares:

$$
N(ih) = -N(h) = -(h_0^2 + h_1^2 + h_2^2 + h_3^2) , \qquad N(ih) = 0 \iff h = 0 .
$$

Every nonzero element of the anti-quaternion subspace is therefore a unit, with inverse $(ih)^{-1} = -(i h^{\natural})/N(h)$; the subspace has no nonzero zero divisor although it is not closed under the product. Its elements are the negatives, up to the central unit, of the elements of the quaternion subspace, which is the reason the criterion is the same apart from the sign.

## The Hermitian Subspace

A Hermitian element is $a_0e_0 + i\mathbf{p}$ with $a_0 \in \mathbb{R}$ and $\mathbf{p}$ a real vector, and its norm is the difference

$$
N(a_0e_0 + i\mathbf{p}) = a_0^2 + i^2(p_1^2 + p_2^2 + p_3^2) = a_0^2 - (\mathbf{p},\mathbf{p}) .
$$

A Hermitian element is a unit exactly when $a_0^2 \neq (\mathbf{p},\mathbf{p})$, so the nonzero non-units of the Hermitian subspace are the nonzero solutions of the single equation $a_0^2 = (\mathbf{p},\mathbf{p})$. There are many: $e_0 + ie_1$ is one, and it is a zero divisor with an explicit partner in the same subspace,

$$
(e_0 + ie_1)(e_0 - ie_1) = e_0^2 - (ie_1)^2 = e_0 - e_0 = 0 ,
$$

since $(ie_1)^2 = i^2e_1^2 = -(-e_0) = e_0$ and $e_0$ is central, so that the two middle terms cancel. The Hermitian subspace is therefore one of the three that contain nonzero zero divisors. The non-units of the Hermitian subspace are **not** square-zero: $(e_0 + ie_1)^2 = 2(e_0 + ie_1) \neq 0$. This example is worth keeping, because $\tfrac{1}{2}(e_0 + ie_1)$ is then a nonzero idempotent, its partner $\tfrac{1}{2}(e_0 - ie_1)$ is a second, and the two are orthogonal and sum to $e_0$; the idempotents of the algebra are a theme of their own.

## The Anti-Hermitian Subspace

An anti-Hermitian element is $ib_0e_0 + \mathbf{q}$ with $b_0 \in \mathbb{R}$ and $\mathbf{q}$ a real vector, and its norm is

$$
N(ib_0e_0 + \mathbf{q}) = (ib_0)^2 + q_1^2 + q_2^2 + q_3^2 = -b_0^2 + (\mathbf{q},\mathbf{q}) .
$$

An anti-Hermitian element is a unit exactly when $(\mathbf{q},\mathbf{q}) \neq b_0^2$, and the nonzero non-units are the nonzero solutions of $(\mathbf{q},\mathbf{q}) = b_0^2$. The subspace is the mirror image of the Hermitian one, the sign of the norm reversed, and $ie_0 + e_1$ is an explicit non-unit, with the partner in the same subspace

$$
(ie_0 + e_1)(ie_0 - e_1) = (ie_0)^2 - (ie_0)e_1 + e_1(ie_0) - e_1^2 = -e_0 - ie_1 + ie_1 + e_0 = 0 .
$$

The anti-Hermitian subspace is the third of the three that contain nonzero zero divisors. Its non-units are not square-zero either: the square of $ib_0e_0 + \mathbf{q}$ is $-(b_0^2 + (\mathbf{q},\mathbf{q}))e_0 + 2ib_0\mathbf{q}$, which vanishes only at the zero element, since $\mathbf{q} \neq 0$ and $b_0 \neq 0$ together force $2ib_0\mathbf{q} \neq 0$. So the Hermitian and the anti-Hermitian non-units alike have nonzero square, and among the six the only subspace with a nonzero square-zero element is the vector subspace.

## Summary

An element of the biquaternion algebra is a unit exactly when the central norm $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural}$ is nonzero, and then its inverse is $\tilde{Q}^{\natural}/N(\tilde{Q})$. Restricted to the six distinguished subspaces, the criterion is $A \neq 0$ on the centre, $(\mathbf{P},\mathbf{P}) \neq 0$ on the vector subspace, $h \neq 0$ on the quaternion subspace, $h \neq 0$ on the anti-quaternion subspace, $a_0^2 \neq (\mathbf{p},\mathbf{p})$ on the Hermitian subspace and $(\mathbf{q},\mathbf{q}) \neq b_0^2$ on the anti-Hermitian subspace. Three of the six — the centre, the quaternion subspace and the anti-quaternion subspace — contain no nonzero zero divisor, because on each of them the coefficients are real and the norm is a sum of squares of a single sign; the quaternion subspace is a division algebra and the centre a field. The other three — the vector subspace, the Hermitian subspace and the anti-Hermitian subspace — each contain a nonzero element whose norm vanishes, and on the vector subspace those elements are exactly the square-zero ones, $e_1 + ie_2$ being an example, while on the Hermitian subspace the pair $e_0 \pm ie_1$ and on the anti-Hermitian subspace the pair $ie_0 \pm e_1$ multiply to zero. The units form a group under the product, the norm being multiplicative on the algebra; the structure of that group is *Biquaternion Norm and Invertibility*, and the zero divisors are *Biquaternion Zero Divisors*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $\tilde{Q}^{\natural}$ | quaternion conjugation $Q_0e_0 - Q_1e_1 - Q_2e_2 - Q_3e_3$ |
| $N(\tilde{Q})$ | the norm $\tilde{Q}\tilde{Q}^{\natural}$, central |
| $A, \mathbf{P}, h, \mathbf{p}, \mathbf{q}$ | a complex scalar, a complex vector, a real quaternion, and two real vectors |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section
- *The Four Biquaternion Complex Products* (`articles_maths/the-four-biquaternion-complex-products.md`), for the product formula
- *Decomposition of the Multiplication* (`articles_maths/decomposition-of-the-multiplication.md`), for the square of a pure vector
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm, the inverse formula and the unit group of the whole algebra
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the elements of vanishing norm in the whole algebra
- *The Six Subspaces and the Zero Divisors* (`articles_maths/the-six-subspaces-and-the-zero-divisors.md`), for the zero divisors themselves subspace by subspace, the pure and the non-pure family and the identification of the non-pure ones with the idempotents
- *The Six Subspaces and the Idempotents and Projections* (`articles_maths/the-six-subspaces-and-the-idempotents-and-projections.md`), for the idempotents that the non-pure zero divisors are multiples of
