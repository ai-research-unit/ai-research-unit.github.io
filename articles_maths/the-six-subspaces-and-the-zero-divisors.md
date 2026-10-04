# __The Six Subspaces and the Zero Divisors__

## Introduction

A nonzero element of the biquaternion algebra is a **zero divisor** if there is a nonzero element that multiplies it to zero. Since the norm $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural}$ is central and multiplicative, a nonzero element is a zero divisor exactly when $N(\tilde{Q}) = 0$, and then $\tilde{Q}^{\natural}$ is an annihilating partner. The criterion is proved in *The Six Subspaces and the Units*, where it is used to decide which of the six subspaces consist of units; the subject here is the zero divisors themselves, and in particular the shape of the set of them inside each of the six.

The bilinearity of the product settles at once how the zero divisors sit among the elements: as $\tilde{Q}$ runs over the zero divisors and $\tilde{X}$ over the whole algebra, the product $\tilde{Q}\tilde{X}$ has norm $N(\tilde{Q})N(\tilde{X}) = 0$ and the same for $\tilde{X}\tilde{Q}$. **The union of the zero divisors with the zero element is closed under multiplication and is carried into itself by multiplication by any element on either side.** The zero divisors are the singular set of the algebra, in the usual sense of that word.

Three of the six subspaces contain no nonzero zero divisor, by *The Six Subspaces and the Units*: the centre, the quaternion subspace and the anti-quaternion subspace, on each of which the coefficients are real and the norm is a sum of squares of one sign. The other three contain them, and the sets are as follows. Here $\mathbf{p}, \mathbf{q} \in \mathbb{R}^3$ are **real** vectors, $a_0, b_0 \in \mathbb{R}$, and $A \in \mathbb{C}$.

| subspace | the zero divisors |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | none |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathbf{P} \neq 0$ with $(\mathbf{P},\mathbf{P}) = 0$ |
| $\mathbb{H}_{\mathbb{B}}$ | none |
| $i\mathbb{H}_{\mathbb{B}}$ | none |
| $\mathbb{M}_+$ | $a_0e_0 + i\mathbf{p} \neq 0$ with $a_0^2 = (\mathbf{p},\mathbf{p})$ |
| $\mathbb{M}_-$ | $ib_0e_0 + \mathbf{q} \neq 0$ with $(\mathbf{q},\mathbf{q}) = b_0^2$ |

The three sets that are nonempty are of two kinds, and the two kinds behave differently under squaring.

**Theorem (the two families).** The zero divisors of the algebra are of exactly two kinds. Those in the vector subspace are **pure**, they are the nonzero solutions of $(\mathbf{P},\mathbf{P}) = 0$, and every one of them is **square-zero**: $\mathbf{P}^2 = -(\mathbf{P},\mathbf{P})e_0 = 0$. Those in the Hermitian and the anti-Hermitian subspaces are **non-pure**, and none of them is square-zero: the square of $a_0e_0 + i\mathbf{p}$ in $\mathbb{M}_+$ is $(a_0^2 + (\mathbf{p},\mathbf{p}))e_0 + 2ia_0\mathbf{p}$, which is nonzero whenever the element is, and the square of $ib_0e_0 + \mathbf{q}$ in $\mathbb{M}_-$ is $-(b_0^2 + (\mathbf{q},\mathbf{q}))e_0 + 2ib_0\mathbf{q}$, likewise nonzero.

**Proof.** The square of a pure vector is $-\mathbf{P}^2$ evaluated in the scalar–vector formula, and $(\mathbf{P},\mathbf{P}) = 0$ makes it vanish. For the two non-pure families the displayed squares are computed from the product formula, and each vanishes only if both its scalar part and its vector part vanish: in $\mathbb{M}_+$ the vector part $2ia_0\mathbf{p}$ vanishes only for $\mathbf{p} = 0$ or $a_0 = 0$, the first giving $a_0 = 0$ and the second $(\mathbf{p},\mathbf{p}) = 0$, that is $\mathbf{p} = 0$; in $\mathbb{M}_-$ the vector part $2ib_0\mathbf{q}$ likewise forces $\mathbf{q} = 0$ or $b_0 = 0$, hence the zero element. So no nonzero zero divisor of $\mathbb{M}_+$ or $\mathbb{M}_-$ is square-zero, and every nonzero zero divisor of the vector subspace is.

The same distinction appears in the relation to the idempotents of the algebra, whose classification is in *The Six Subspaces and the Idempotents and Projections*: **the zero divisors of the two Hermitian subspaces are exactly the nonzero complex multiples of the Hermitian idempotents**, those of $\mathbb{M}_+$ being the real multiples and those of $\mathbb{M}_-$ the purely imaginary ones, while the zero divisors of the vector subspace are multiples of no idempotent.

## The Centre Subspace

A central element is $Ae_0$ and its norm is $A^2$, which vanishes only at $A = 0$:

$$
Ae_0 \neq 0 \implies N(Ae_0) = A^2 \neq 0 .
$$

The centre is a field and contains no nonzero zero divisor, and its only non-unit is $0$. It is the first of the three subspaces of the list above, and the smallest: the zero divisors of the algebra avoid the centre entirely.

## The Vector Subspace

A pure vector $\mathbf{P}$ is a zero divisor exactly when $(\mathbf{P},\mathbf{P}) = 0$, and then it is square-zero, so the vector subspace's zero divisors are precisely the **square-zero elements** of the whole algebra. Writing the complex vector as $\boldsymbol{\rho} + i\boldsymbol{\rho}'$ with $\boldsymbol{\rho}, \boldsymbol{\rho}'$ real,

$$
(\mathbf{P},\mathbf{P}) = (\boldsymbol{\rho},\boldsymbol{\rho}) - (\boldsymbol{\rho}',\boldsymbol{\rho}') + 2i(\boldsymbol{\rho},\boldsymbol{\rho}') ,
$$

so that the condition is the pair of real equations

$$
(\boldsymbol{\rho},\boldsymbol{\rho}) = (\boldsymbol{\rho}',\boldsymbol{\rho}') , \qquad (\boldsymbol{\rho},\boldsymbol{\rho}') = 0 .
$$

**A pure vector is a zero divisor exactly when its two real parts are orthogonal and of equal length.** Writing $\boldsymbol{\rho} = r\hat{u}$ and $\boldsymbol{\rho}' = r\hat{v}$ with $r > 0$ and $\hat{u}, \hat{v}$ an orthonormal pair of directions, the zero divisors of the vector subspace are the elements $r(\hat{u} + i\hat{v})$: a four-parameter family, cut out by two real equations in the six real coordinates. An example is $\mathbf{P} = e_1 + ie_2$, with $\boldsymbol{\rho} = e_1$, $\boldsymbol{\rho}' = e_2$, an orthonormal pair of equal length one, and

$$
(e_1 + ie_2)^2 = 0 .
$$

Every zero divisor of the vector subspace is its own annihilating partner, since $\mathbf{P}^2 = 0$; this is the property that the two Hermitian subspaces do not share, and the reason the pure and the non-pure family are kept apart throughout.

## The Quaternion Subspace

The quaternion subspace is a division algebra, by *The Six Subspaces and the Units*: on it the coefficients are real and the norm is a sum of four squares,

$$
N(h) = h_0^2 + h_1^2 + h_2^2 + h_3^2 ,
$$

which vanishes only at $h = 0$. It therefore contains no nonzero zero divisor, and it is the second of the three subspaces of the list. Among the five subspaces closed under the product or under the symmetrized product it is the one whose non-units are the fewest: only $0$.

## The Anti-Quaternion Subspace

The anti-quaternion subspace is not a subalgebra, and it still contains no nonzero zero divisor: an element is $ih$ with $h$ real, and its norm is the negative of the norm of $h$,

$$
N(ih) = -N(h) = -(h_0^2 + h_1^2 + h_2^2 + h_3^2) ,
$$

which vanishes only at $h = 0$. The third and last of the three subspaces of the list, and the only one of them that is not closed under the product: the anti-quaternion subspace consists of units and zero, and it multiplies into the quaternion subspace without multiplying the zero divisor problem into itself.

## The Hermitian Subspace

A Hermitian element is $a_0e_0 + i\mathbf{p}$ with $a_0 \in \mathbb{R}$ and $\mathbf{p}$ real, and its norm is the difference $a_0^2 - (\mathbf{p},\mathbf{p})$, so the zero divisors are the nonzero solutions of the single equation

$$
a_0^2 = (\mathbf{p},\mathbf{p}) .
$$

Since $(\mathbf{p},\mathbf{p})$ is a sum of real squares, a nonzero solution has $a_0 \neq 0$; indeed $\mathbf{p} = 0$ would give $a_0 = 0$. Every zero divisor of the Hermitian subspace can therefore be written with $a_0$ divided out,

$$
a_0e_0 + i\mathbf{p} = 2a_0 \cdot \tfrac{1}{2}\left(e_0 + i\,\frac{\mathbf{p}}{a_0}\right) , \qquad \left(\frac{\mathbf{p}}{a_0}, \frac{\mathbf{p}}{a_0}\right) = 1 ,
$$

and the second factor is a **Hermitian idempotent**, by *The Six Subspaces and the Idempotents and Projections*. **The zero divisors of the Hermitian subspace are exactly the nonzero real multiples of the Hermitian idempotents**, and the set of them is a cone of two pieces, the two signs of $a_0$ over the same $\mathbf{p}$. An explicit pair is

$$
(e_0 + ie_1)(e_0 - ie_1) = 0 ,
$$

where $e_0 \pm ie_1$ are the two zero divisors and each is the other's annihilating partner; they are $2$ times the idempotents $\tfrac{1}{2}(e_0 \pm ie_1)$. The squares are not zero, by the theorem of the Introduction; $e_0 + ie_1$ has square $2(e_0 + ie_1)$, so it is a zero divisor of square nonzero, and the vector subspace's square-zero elements are not typical of the algebra's zero divisors but peculiar to it.

## The Anti-Hermitian Subspace

An anti-Hermitian element is $ib_0e_0 + \mathbf{q}$ with $b_0 \in \mathbb{R}$ and $\mathbf{q}$ real, and its norm is $(\mathbf{q},\mathbf{q}) - b_0^2$, so the zero divisors are the nonzero solutions of

$$
(\mathbf{q},\mathbf{q}) = b_0^2 .
$$

A nonzero solution has $b_0 \neq 0$, and dividing it out,

$$
ib_0e_0 + \mathbf{q} = 2ib_0 \cdot \tfrac{1}{2}\left(e_0 - i\,\frac{\mathbf{q}}{b_0}\right) , \qquad \left(\frac{\mathbf{q}}{b_0}, \frac{\mathbf{q}}{b_0}\right) = 1 ,
$$

so that **the zero divisors of the anti-Hermitian subspace are exactly the nonzero purely imaginary multiples of the Hermitian idempotents**; the idempotent is the one of the Hermitian subspace, and only the multiplier is imaginary. This is the precise sense in which the two Hermitian subspaces share their zero divisors: the same family of idempotents, multiplied by a real number in the one case and by a purely imaginary number in the other, with the result in $\mathbb{M}_+$ and in $\mathbb{M}_-$ respectively. An explicit pair is

$$
(ie_0 + e_1)(ie_0 - e_1) = 0 ,
$$

with $ie_0 \pm e_1$ the two zero divisors, of square $-2e_0 + 2ie_1$ and $-2e_0 - 2ie_1$, neither zero.

## Summary

A nonzero element of the biquaternion algebra is a zero divisor exactly when its norm vanishes, and the union of the zero divisors with $0$ is closed under multiplication and stable under multiplication by any element on either side. Three of the six distinguished subspaces contain no nonzero zero divisor, the centre, the quaternion subspace and the anti-quaternion subspace, on each of which the coefficients are real and the norm is a sum of squares of one sign; the quaternion subspace is a division algebra. The zero divisors of the vector subspace are the nonzero solutions of $(\mathbf{P},\mathbf{P}) = 0$, equivalently the pure vectors whose two real parts are orthogonal and of equal length; every one of them is square-zero, and they form a four-parameter family. The zero divisors of the Hermitian subspace are the nonzero solutions of $a_0^2 = (\mathbf{p},\mathbf{p})$, exactly the nonzero real multiples of the Hermitian idempotents; those of the anti-Hermitian subspace are the nonzero solutions of $(\mathbf{q},\mathbf{q}) = b_0^2$, exactly the nonzero purely imaginary multiples of the same idempotents. So the zero divisors of the algebra are of two kinds, the pure ones of the vector subspace, which are square-zero, and the non-pure ones of the two Hermitian subspaces, which are not, and the non-pure ones are the complex multiples of the idempotents. The annihilators of a zero divisor, the ideals they generate, the Peirce decomposition and the relation to the radical are the business of *Biquaternion Ideals and Peirce Decomposition*; the criterion used throughout is proved in *The Six Subspaces and the Units*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $N(\tilde{Q})$ | the norm $\tilde{Q}\tilde{Q}^{\natural}$, central |
| $\boldsymbol{\rho}, \boldsymbol{\rho}'$ | the real and imaginary parts of a complex vector |
| $a_0, b_0, \mathbf{p}, \mathbf{q}$ | the real scalar parts and the real vectors of $\mathbb{M}_\pm$ |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section
- *The Six Subspaces and the Units* (`articles_maths/the-six-subspaces-and-the-units.md`), for the criterion and for which of the six consist of units
- *The Six Subspaces and the Idempotents and Projections* (`articles_maths/the-six-subspaces-and-the-idempotents-and-projections.md`), for the idempotents that the non-pure zero divisors are multiples of
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the zero divisors of the whole algebra, the pure and the non-pure family and the bivector form of the pure ones
- *The Six Subspaces and the Ideals* (`articles_maths/the-six-subspaces-and-the-ideals.md`), for the annihilators of the zero divisors, which are minimal one-sided ideals, and for the ideals the nilpotents generate
- *The Six Subspaces and the Forms* (`articles_maths/the-six-subspaces-and-the-forms.md`), for the isotropic lines, which are exactly the lines spanned by the zero divisors of the vector, Hermitian and anti-Hermitian subspaces
- *The Six Subspaces and the Analysis* (`articles_maths/the-six-subspaces-and-the-analysis.md`), for the null cone as the set on which the second-order operator of the subspace is not elliptic
