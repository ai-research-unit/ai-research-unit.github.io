# __Introduction to the General Quaternionic Algebra__

## Introduction

The quaternion algebra $\mathbb{H}$ is the four-dimensional real algebra with basis $e_0 = 1, e_1, e_2, e_3$, the multiplication rules $e_1^2 = e_2^2 = e_3^2 = e_1e_2e_3 = -e_0$ and the conjugation $\tilde q^{\natural} = q_0 - \vec q$; the basis, the table, the scalar–vector splitting and the conjugation are those of *Quaternion Algebra*, and they are used here without restatement. A quaternion is written $\tilde q = q_0e_0 + \vec q$ with $\vec q = q_1e_1 + q_2e_2 + q_3e_3$, the glyph of the quaternion layer. The real space $\mathbb{H}$ carries six operations, set out in *The 6 Products of the Quaternion Real Space* and structured in *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*. This article introduces the algebra carried by the second of its two bilinear operations, the **general quaternionic bilinear product**

$$
\tilde p \star \tilde q = \tilde p^{\natural}\tilde q .
$$

The algebra $(\mathbb{H}, +, \star)$ is the **general quaternionic algebra of quaternions**, and it is the object of this block.

This article does three things. It fixes the product and its coordinate rule. It records the two defects that decide the whole block: the product is **not associative**, and it has $e_0$ as a **left unit and no right unit**, so the algebra is left-unital and not unital. It then places the algebra among the six operations of the space. The element theory is read in the five Common Theory articles that follow (*Norm and Invertibility in the General Quaternionic Algebra*, *Square Roots of One and the Idempotents of the General Quaternionic Algebra*, *Square Roots of Zero and the Nilpotents of the General Quaternionic Algebra*, *Square Roots of a General Element in the General Quaternionic Algebra* and *The Specificities of the General Quaternionic Algebra*, all below this article in this category), the defect theory in *The Associator and the Ternary Product of the Quaternionic Product*, below this article in this category, the form in *The Isotropic Structure of the General Quaternionic Algebra*, below this article in this category, and the operator and matrix readings in *Two-Sided Operators on the General Quaternionic Algebra of Quaternions* and *One-Sided Operators on the General Quaternionic Algebra of Quaternions*, both below this article in this category.

## The General Quaternionic Bilinear Product

### Definition

**Definition.** For $\tilde p = p_0e_0 + p_1e_1 + p_2e_2 + p_3e_3$ and $\tilde q = q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3$ in $\mathbb{H}$, the **general quaternionic bilinear product** is

$$
\tilde p \star \tilde q = \tilde p^{\natural}\tilde q , \qquad \tilde p^{\natural} = p_0 - \vec p = p_0 - p_1e_1 - p_2e_2 - p_3e_3 .
$$

The product carries the star throughout the corpus; the bare juxtaposition is reserved for the associative multiplication $\tilde p\tilde q$ of $(\mathbb{H}, +, \cdot)$, the plain product of the general plain algebra of the same space, and the two are never interchanged.

### The Coordinate Rule

**Proposition (the coordinate rule).** With $\vec p, \vec q$ the vector parts and $\vec p \times \vec q$ the cross product,

$$
\tilde p \star \tilde q = \bigl(p_0q_0 + \vec p \cdot \vec q\bigr)e_0 + p_0\vec q - q_0\vec p - \vec p \times \vec q .
$$

*Proof.* Expand $\tilde p^{\natural}\tilde q = (p_0 - \vec p)(q_0 + \vec q) = p_0q_0 - \vec p\vec q + p_0\vec q - q_0\vec p$ and substitute the product of two pure quaternions, $\vec p\vec q = -\,\vec p \cdot \vec q + \vec p \times \vec q$ (*Quaternion Algebra*).

**Proposition (bilinearity and the exchange law).** The product is $\mathbb{R}$-bilinear. It is neither commutative nor anticommutative. The two orderings are exchanged by the conjugation,

$$
\tilde q \star \tilde p = (\tilde p \star \tilde q)^{\natural} .
$$

*Proof.* Bilinearity is that of the plain product and of the conjugation. For the exchange law, $(\tilde p^{\natural}\tilde q)^{\natural} = \tilde q^{\natural}\tilde p^{\natural\natural} = \tilde q^{\natural}\tilde p$, because the conjugation is an anti-automorphism of order two.

**Remark (the product against the plain one).** The coordinate rule separates the product into the plain product and a correction. For pure $\tilde p$ and pure $\tilde q$ one has $\tilde p \star \tilde q = -\,\tilde p\tilde q$, while a general element obeys

$$
\tilde p \star \tilde q = 2p_0\,\tilde q - \tilde p\tilde q ,
$$

so the quaternionic product is the plain product altered by the term $2p_0\tilde q$, which depends on the first factor through its scalar coordinate alone. The two laws agree on the scalar line and separate as soon as the first factor is not central.

## The Failure of Associativity

**Definition.** The **associator** of the product is the trilinear map

$$
[\tilde p,\tilde q,\tilde r] = (\tilde p \star \tilde q) \star \tilde r - \tilde p \star (\tilde q \star \tilde r) .
$$

**Theorem (the associator).** For all $\tilde p,\tilde q,\tilde r \in \mathbb{H}$,

$$
[\tilde p,\tilde q,\tilde r] = \bigl(\tilde q^{\natural}\tilde p - \tilde p^{\natural}\tilde q^{\natural}\bigr)\tilde r .
$$

In particular the product is **not associative**: $[e_1,e_0,e_0] = 2e_1$, and $24$ of the $64$ triples of basis elements give a nonzero associator.

*Proof.* By the exchange law $(\tilde p \star \tilde q)^{\natural} = \tilde q^{\natural}\tilde p$, so $(\tilde p \star \tilde q) \star \tilde r = (\tilde p^{\natural}\tilde q)^{\natural}\tilde r = \tilde q^{\natural}\tilde p\tilde r$, while $\tilde p \star (\tilde q \star \tilde r) = \tilde p^{\natural}(\tilde q^{\natural}\tilde r) = \tilde p^{\natural}\tilde q^{\natural}\tilde r$; the difference is the displayed product. At $(e_1,e_0,e_0)$ the coefficient is $e_0^{\natural}e_1 - e_1^{\natural}e_0^{\natural} = e_1 + e_1 = 2e_1$, since $e_1^{\natural} = -e_1$. The count is the enumeration of the $64$ triples against the closed form.

**Remark.** The mechanism is visible in the closed form. The associator would vanish if the conjugation could be moved across the factor $\tilde p$ at no cost, but the conjugation is an anti-automorphism and reverses the order of the factors, so it cannot. Associativity for the quaternionic product is therefore not a mild extra property that happens to fail; it is the property that the conjugation in the first slot forbids. The defect is studied in full, with the weaker laws and the ternary product it generates, in *The Associator and the Ternary Product of the Quaternionic Product*, below this article in this category.

## The Left Unit

**Theorem (the one-sided unit).** The element $e_0$ is a left unit of the product and not a right one:

$$
e_0 \star \tilde q = \tilde q , \qquad \tilde q \star e_0 = \tilde q^{\natural} .
$$

There is no right unit: no $\tilde u \in \mathbb{H}$ satisfies $\tilde q \star \tilde u = \tilde q$ for every $\tilde q$.

*Proof.* $e_0 \star \tilde q = e_0^{\natural}\tilde q = e_0\tilde q = \tilde q$ and $\tilde q \star e_0 = \tilde q^{\natural}e_0 = \tilde q^{\natural}$. For the non-existence, the condition at $\tilde q = e_0$ reads $\tilde u = e_0$, and at $\tilde q = e_1$ it reads $e_1^{\natural}\tilde u = e_1$, that is $\tilde u = -e_1$; the two requirements are incompatible.

**Corollary.** The algebra is **left-unital and not unital**, and the asymmetry is total: there is no right unit, hence no two-sided unit, hence no unit in the algebraists' sense. The two-sided inverse of the unital theory is absent with it, and inversion in this block is the theory of the two one-sided equations, which is the subject of *Norm and Invertibility in the General Quaternionic Algebra*, below this article in this category; the outcome is that the two one-sided inverses exist and coincide, while the group of units of the plain algebra does not survive.

**Remark.** The asymmetry is not an accident of the conjugation. The mirror law $\tilde p \star' \tilde q = \tilde p\tilde q^{\natural}$ has $e_0$ as a right unit and no left one, and the two laws are exchanged by the conjugation; the quaternion space therefore carries one law of each handedness, and this article's law is the left-handed one. The manufacturing of a right unit out of the twisted right multiplications is *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, below this article in this category.

## The Other Five Operations

The real space $\mathbb{H}$ carries six operations (*The 6 Products of the Quaternion Real Space*) and they organise into six algebraic structures (*The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*). This article's product is one of the two bilinear ones. The other is the plain product $\tilde p\tilde q$, the multiplication of the general plain algebra of the same space, and it is the only associative and the only unital one of the six.

The remaining operations of the six are the companions of the two bilinear laws: the mirror of this article's law, $\tilde q^{\natural}\tilde p$, and the symmetrised and antisymmetrised products $\tfrac12(\tilde p \star \tilde q + \tilde q \star \tilde p)$ and $\tfrac12(\tilde p \star \tilde q - \tilde q \star \tilde p)$, which carry the Symmetric and the Antisymmetric quaternionic algebras of the chapter. The full comparison is *Comparison Between the Two General Products*, the reading on the distinguished subspaces is *The Remarkable Subspaces under the Six Operations*, below this article in this category, and the theory of the two forms is *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, above this article in this category; this article records only the orientation.

## The Place of the Algebra among the Two Bilinear Laws

The quaternionic product and the plain product are the two bilinear laws on one and the same space, and they share the norm and little else. The table collects the separating features; the fuller comparison is the owner's, and it is cited rather than reproduced.

| feature | plain $\tilde p\tilde q$ | quaternionic $\tilde p^{\natural}\tilde q$ |
|---|---|---|
| commutative | no | no |
| two-sided unit | $e_0$ | none |
| left unit | $e_0$ | $e_0$ |
| right unit | $e_0$ | none |
| associative | yes | no |
| zero divisors | none | none |
| quadratic form | $N$, multiplicative | $N$, multiplicative |

**Proposition (the isolated features).** The quaternionic product is characterised among the operations of the space by the conjunction of three properties: it is left-unital and not right-unital; it is not associative; and it has no zero divisors. The plain product has the two-sided unit and is associative; the companion operations are either not unital or not zero-divisor-free.

*Proof.* The unitality and the non-associativity are the two theorems above; the absence of zero divisors is the multiplicativity and the definiteness of the norm (*Norm and Invertibility in the General Quaternionic Algebra*, below this article in this category). For the companions: the symmetrised product is central-valued, $\tfrac12(\tilde p \star \tilde q + \tilde q \star \tilde p) = \beta(\tilde p,\tilde q)e_0$, so it has zero divisors, $e_1 \bullet e_2 = 0$; the antisymmetrised product vanishes as soon as the two arguments are equal, so neither companion is zero-divisor-free.

## Summary

The general quaternionic algebra of quaternions is the real space $\mathbb{H}$ under the product $\tilde p \star \tilde q = \tilde p^{\natural}\tilde q$, with the coordinate rule $(p_0q_0 + \vec p \cdot \vec q)e_0 + p_0\vec q - q_0\vec p - \vec p \times \vec q$ and the exchange law $\tilde q \star \tilde p = (\tilde p \star \tilde q)^{\natural}$. The product is not associative, its associator being $(\tilde q^{\natural}\tilde p - \tilde p^{\natural}\tilde q^{\natural})\tilde r$, nonzero at $(e_1,e_0,e_0)$ and at $24$ of the $64$ basis triples. The element $e_0$ is a left unit and not a right unit, and no right unit exists, so the algebra is left-unital and not unital and the inversion theory of the block is the theory of the two one-sided equations. The quaternion space carries two bilinear laws, $\tilde p\tilde q$ and $\tilde p^{\natural}\tilde q$, with four companion operations beside them; the quaternionic product is the left-unital, non-associative, zero-divisor-free member.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra, the real space of the block |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the identity, $e_k^2 = -e_0$ |
| $\tilde p = \sum_\mu p_\mu e_\mu$ | a general element and its four real coordinates |
| $\vec p = \sum_k p_ke_k$ | the vector part, an element of $\mathbb{R}^3$ |
| $\tilde p^{\natural} = p_0 - \vec p$ | the conjugation |
| $\tilde p \star \tilde q = \tilde p^{\natural}\tilde q$ | the general quaternionic bilinear product |
| $[\tilde p,\tilde q,\tilde r]$ | the associator of the product |
| $N$ | the quaternionic bilinear algebraic norm, *Norm and Invertibility in the General Quaternionic Algebra*, below this article in this category |
| $\beta(\tilde p,\tilde q) = p_0q_0 + \vec p \cdot \vec q$ | the polar form of $N$ |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the associator and the ladder of weaker identities.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the symmetrisation of a bilinear product and the ternary product it carries.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for a product with an anti-automorphism inserted in a slot.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the arithmetic of the quaternion units and the multiplicative norm.
