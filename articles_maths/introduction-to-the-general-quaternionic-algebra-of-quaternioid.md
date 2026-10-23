# __Introduction to the General Quaternionic Algebra__

## Introduction

The quaternion algebra $\mathbb{H}$ is the four-dimensional real algebra with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, the multiplication rules $\vec e_x^2 = \vec e_y^2 = \vec e_z^2 = \vec e_x\vec e_y\vec e_z = -e_t$ and the conjugation $\tilde q^{\natural} = q_t - \vec q$; the basis, the table, the scalar–vector splitting and the conjugation are those of *Quaternion Algebra*, and they are used here without restatement. A quaternion is written $\tilde q = q_te_t + \vec q$ with $\vec q = q_x\vec e_x + q_y\vec e_y + q_z\vec e_z$, the glyph of the quaternion layer. The real space $\mathbb{H}$ carries, beside the algebra product of the *Quaternions* category, the companion products set out in *The 6 Products of the Quaternioid Real Space* and named in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*. This article introduces the algebra carried by the second of its two bilinear operations, the **general quaternionic bilinear product**

$$
\tilde q_1 \star \tilde q_2 = \tilde q_1^{\natural}\tilde q_2 .
$$

The algebra $(\mathbb{H}, +, \star)$ is the **general quaternionic algebra of quaternions**, and it is the object of this block.

This article does three things. It fixes the product and its coordinate rule. It records the two defects that decide the whole block: the product is **not associative**, and it has $e_t$ as a **left unit and no right unit**, so the algebra is left-unital and not unital. It then places the algebra among the companion structures of the space. The element theory is read in the five Common Theory articles that follow (*Norm and Invertibility in the General Quaternionic Algebra*, *Square Roots of One and the Idempotents of the General Quaternionic Algebra*, *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*, *Square Roots of a General Element in the General Quaternionic Algebra* and *The Specificities of the General Quaternionic Algebra*, all below this article in this category), the defect theory in *The Associator and the Ternary Product of the Quaternionic Product*, below this article in this category, the form in *The Isotropic Structure of the General Quaternionic Algebra*, below this article in this category, and the operator and matrix readings in *Two-Sided Operators on the General Quaternionic Algebra* and *One-Sided Operators on the General Quaternionic Algebra*, both below this article in this category.

## The General Quaternionic Bilinear Product

### Definition

**Definition.** For $\tilde q_1 = q_{1t}e_t + q_{1x}\vec e_x + q_{1y}\vec e_y + q_{1z}\vec e_z$ and $\tilde q_2 = q_{2t}e_t + q_{2x}\vec e_x + q_{2y}\vec e_y + q_{2z}\vec e_z$ in $\mathbb{H}$, the **general quaternionic bilinear product** is

$$
\tilde q_1 \star \tilde q_2 = \tilde q_1^{\natural}\tilde q_2 , \qquad \tilde q_1^{\natural} = q_{1t} - \vec q_1 = q_{1t} - q_{1x}\vec e_x - q_{1y}\vec e_y - q_{1z}\vec e_z .
$$

The product carries the star throughout the corpus; the bare juxtaposition is reserved for the associative multiplication $\tilde q_1\tilde q_2$ of $(\mathbb{H}, +, \cdot)$, the plain product of the general plain algebra of the same space, and the two are never interchanged.

### The Coordinate Rule

**Proposition (the coordinate rule).** With $\vec q_1, \vec q_2$ the vector parts and $\vec q_1 \times \vec q_2$ the cross product,

$$
\boxed{\;\tilde q_1 \star \tilde q_2 = \bigl(q_{1t}q_{2t} + \vec q_1 \cdot \vec q_2\bigr)e_t + q_{1t}\vec q_2 - q_{2t}\vec q_1 - \vec q_1 \times \vec q_2\;}.
$$

*Proof.* Expand $\tilde q_1^{\natural}\tilde q_2 = (q_{1t} - \vec q_1)(q_{2t} + \vec q_2) = q_{1t}q_{2t} - \vec q_1\vec q_2 + q_{1t}\vec q_2 - q_{2t}\vec q_1$ and substitute the product of two pure quaternions, $\vec q_1\vec q_2 = -\,\vec q_1 \cdot \vec q_2 + \vec q_1 \times \vec q_2$ (*Quaternion Algebra*).

**Proposition (bilinearity and the exchange law).** The product is $\mathbb{R}$-bilinear. It is neither commutative nor anticommutative. The two orderings are exchanged by the conjugation,

$$
\boxed{\;\tilde q_2 \star \tilde q_1 = (\tilde q_1 \star \tilde q_2)^{\natural}\;}.
$$

*Proof.* Bilinearity is that of the plain product and of the conjugation. For the exchange law, $(\tilde q_1^{\natural}\tilde q_2)^{\natural} = \tilde q_2^{\natural}\tilde q_1^{\natural\natural} = \tilde q_2^{\natural}\tilde q_1$, because the conjugation is an anti-automorphism of order two.

**Remark (the product against the plain one).** The coordinate rule separates the product into the plain product and a correction. For pure $\tilde q_1$ and pure $\tilde q_2$ one has $\tilde q_1 \star \tilde q_2 = -\,\tilde q_1\tilde q_2$, while a general element obeys

$$
\tilde q_1 \star \tilde q_2 = 2q_{1t}\,\tilde q_2 - \tilde q_1\tilde q_2 ,
$$

so the quaternionic product is the plain product altered by the term $2q_{1t}\tilde q_2$, which depends on the first factor through its scalar coordinate alone. The two laws agree on the scalar line and separate as soon as the first factor is not central.

## The Failure of Associativity

**Definition.** The **associator** of the product is the trilinear map

$$
[\tilde q_1,\tilde q_2,\tilde q_3] = (\tilde q_1 \star \tilde q_2) \star \tilde q_3 - \tilde q_1 \star (\tilde q_2 \star \tilde q_3) .
$$

**Theorem (the associator).** For all $\tilde q_1,\tilde q_2,\tilde q_3 \in \mathbb{H}$,

$$
\boxed{\;[\tilde q_1,\tilde q_2,\tilde q_3] = \bigl(\tilde q_2^{\natural}\tilde q_1 - \tilde q_1^{\natural}\tilde q_2^{\natural}\bigr)\tilde q_3\;}.
$$

In particular the product is **not associative**: $[\vec e_x,e_t,e_t] = 2\vec e_x$, and $24$ of the $64$ triples of basis elements give a nonzero associator.

*Proof.* By the exchange law $(\tilde q_1 \star \tilde q_2)^{\natural} = \tilde q_2^{\natural}\tilde q_1$, so $(\tilde q_1 \star \tilde q_2) \star \tilde q_3 = (\tilde q_1^{\natural}\tilde q_2)^{\natural}\tilde q_3 = \tilde q_2^{\natural}\tilde q_1\tilde q_3$, while $\tilde q_1 \star (\tilde q_2 \star \tilde q_3) = \tilde q_1^{\natural}(\tilde q_2^{\natural}\tilde q_3) = \tilde q_1^{\natural}\tilde q_2^{\natural}\tilde q_3$; the difference is the displayed product. At $(\vec e_x,e_t,e_t)$ the coefficient is $e_t^{\natural}\vec e_x - \vec e_x^{\natural}e_t^{\natural} = \vec e_x + \vec e_x = 2\vec e_x$, since $\vec e_x^{\natural} = -\vec e_x$. The count is the enumeration of the $64$ triples against the closed form.

**Remark.** The mechanism is visible in the closed form. The associator would vanish if the conjugation could be moved across the factor $\tilde q_1$ at no cost, but the conjugation is an anti-automorphism and reverses the order of the factors, so it cannot. Associativity for the quaternionic product is therefore not a mild extra property that happens to fail; it is the property that the conjugation in the first slot forbids. The defect is studied in full, with the weaker laws and the ternary product it generates, in *The Associator and the Ternary Product of the Quaternionic Product*, below this article in this category.

## The Left Unit

**Theorem (the one-sided unit).** The element $e_t$ is a left unit of the product and not a right one:

$$
\boxed{\;e_t \star \tilde q = \tilde q , \qquad \tilde q \star e_t = \tilde q^{\natural}\;}.
$$

There is no right unit: no $\tilde u \in \mathbb{H}$ satisfies $\tilde q \star \tilde u = \tilde q$ for every $\tilde q$.

*Proof.* $e_t \star \tilde q = e_t^{\natural}\tilde q = e_t\tilde q = \tilde q$ and $\tilde q \star e_t = \tilde q^{\natural}e_t = \tilde q^{\natural}$. For the non-existence, the condition at $\tilde q = e_t$ reads $\tilde u = e_t$, and at $\tilde q = \vec e_x$ it reads $\vec e_x^{\natural}\tilde u = \vec e_x$, that is $\tilde u = -\vec e_x$; the two requirements are incompatible.

**Corollary.** The algebra is **left-unital and not unital**, and the asymmetry is total: there is no right unit, hence no two-sided unit, hence no unit in the algebraists' sense. The two-sided inverse of the unital theory is absent with it, and inversion in this block is the theory of the two one-sided equations, which is the subject of *Norm and Invertibility in the General Quaternionic Algebra*, below this article in this category; the outcome is that the two one-sided inverses exist and coincide, while the group of units of the plain algebra does not survive.

**Remark.** The asymmetry is not an accident of the conjugation. The mirror law $\tilde q_1 \star' \tilde q_2 = \tilde q_1\tilde q_2^{\natural}$ has $e_t$ as a right unit and no left one, and the two laws are exchanged by the conjugation; the quaternion space therefore carries one law of each handedness, and this article's law is the left-handed one. The manufacturing of a right unit out of the twisted right multiplications is *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, below this article in this category.

## The Other Five Operations

The real space $\mathbb{H}$ carries, beside the algebra product of the *Quaternions* category, the companion products of *The 6 Products of the Quaternioid Real Space*, which the category organises into three structures in *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*. This article's product is one of the two bilinear ones; the other is the algebra product $\tilde q_1\tilde q_2$, the multiplication of the quaternion algebra, and it is the only associative and the only unital one of them.

The remaining companion products are the companions of the two bilinear laws: the mirror of this article's law, $\tilde q_2^{\natural}\tilde q_1$, and the symmetrised and antisymmetrised products $\tfrac12(\tilde q_1 \star \tilde q_2 + \tilde q_2 \star \tilde q_1)$ and $\tfrac12(\tilde q_1 \star \tilde q_2 - \tilde q_2 \star \tilde q_1)$, which carry the Symmetric and the Antisymmetric quaternionic algebras of the chapter. The full comparison is *Comparison Between the Two General Products*, the reading on the distinguished subspaces is *Remarkable Subspaces and the Two General Products*, below this article in this category, and the theory of the two forms is *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*, above this article in this category; this article records only the orientation.

## The Place of the Algebra among the Two Bilinear Laws

The quaternionic product and the plain product are the two bilinear laws on one and the same space, and they share the norm and little else. The table collects the separating features; the fuller comparison is the owner's, and it is cited rather than reproduced.

| feature | plain $\tilde q_1\tilde q_2$ | quaternionic $\tilde q_1^{\natural}\tilde q_2$ |
|---|---|---|
| commutative | no | no |
| two-sided unit | $e_t$ | none |
| left unit | $e_t$ | $e_t$ |
| right unit | $e_t$ | none |
| associative | yes | no |
| zero divisors | none | none |
| quadratic form | $\langle\cdot,\cdot\rangle_{\natural}$, multiplicative | $\langle\cdot,\cdot\rangle_{\natural}$, multiplicative |

**Proposition (the isolated features).** The quaternionic product is characterised among the operations of the space by the conjunction of three properties: it is left-unital and not right-unital; it is not associative; and it has no zero divisors. The plain product has the two-sided unit and is associative; the companion operations are either not unital or not zero-divisor-free.

*Proof.* The unitality and the non-associativity are the two theorems above; the absence of zero divisors is the multiplicativity and the definiteness of the norm (*Norm and Invertibility in the General Quaternionic Algebra*, below this article in this category). For the companions: the symmetrised product is central-valued, $\tfrac12(\tilde q_1 \star \tilde q_2 + \tilde q_2 \star \tilde q_1) = \beta(\tilde q_1,\tilde q_2)e_t$, so it has zero divisors, $\vec e_x \bullet \vec e_y = 0$; the antisymmetrised product vanishes as soon as the two arguments are equal, so neither companion is zero-divisor-free.

## Summary

The general quaternionic algebra of quaternions is the real space $\mathbb{H}$ under the product $\tilde q_1 \star \tilde q_2 = \tilde q_1^{\natural}\tilde q_2$, with the coordinate rule $(q_{1t}q_{2t} + \vec q_1 \cdot \vec q_2)e_t + q_{1t}\vec q_2 - q_{2t}\vec q_1 - \vec q_1 \times \vec q_2$ and the exchange law $\tilde q_2 \star \tilde q_1 = (\tilde q_1 \star \tilde q_2)^{\natural}$. The product is not associative, its associator being $(\tilde q_2^{\natural}\tilde q_1 - \tilde q_1^{\natural}\tilde q_2^{\natural})\tilde q_3$, nonzero at $(\vec e_x,e_t,e_t)$ and at $24$ of the $64$ basis triples. The element $e_t$ is a left unit and not a right unit, and no right unit exists, so the algebra is left-unital and not unital and the inversion theory of the block is the theory of the two one-sided equations. The quaternion space carries two bilinear laws, $\tilde q_1\tilde q_2$ and $\tilde q_1^{\natural}\tilde q_2$, with four companion operations beside them; the quaternionic product is the left-unital, non-associative, zero-divisor-free member.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra, the real space of the block |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, $e_t$ the identity, $\vec e_k^2 = -e_t$ |
| $\tilde q = \sum_\mu q_\mu e_\mu$ | a general element and its four real coordinates |
| $\vec q = \sum_k q_k\vec e_k$ | the vector part, an element of $\mathbb{R}^3$ |
| $\tilde q^{\natural} = q_t - \vec q$ | the conjugation |
| $\tilde q_1 \star \tilde q_2 = \tilde q_1^{\natural}\tilde q_2$ | the general quaternionic bilinear product |
| $[\tilde q_1,\tilde q_2,\tilde q_3]$ | the associator of the product |
| $\langle\cdot\rangle_{\natural}$ | the quaternionic bilinear algebraic norm, *Norm and Invertibility in the General Quaternionic Algebra*, below this article in this category |
| $\beta(\tilde q_1,\tilde q_2) = q_{1t}q_{2t} + \vec q_1 \cdot \vec q_2$ | the polar form of $\langle\cdot,\cdot\rangle_{\natural}$ |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the associator and the ladder of weaker identities.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the symmetrisation of a bilinear product and the ternary product it carries.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for a product with an anti-automorphism inserted in a slot.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the arithmetic of the quaternion units and the multiplicative norm.
