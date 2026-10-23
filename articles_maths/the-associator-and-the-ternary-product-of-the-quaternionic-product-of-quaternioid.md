# __The Associator and the Ternary Product of the Quaternionic Product__

## Introduction

The product of this block is the **general quaternionic bilinear product**

$$
\tilde q_1 \star \tilde q_2 = \tilde q_1^{\natural}\tilde q_2 , \qquad \tilde q_1^{\natural} = q_{1t} - \vec q_1 ,
$$

the second of the two bilinear products of the quaternion real space, whose rule is *The Two General Products of the Quaternioid $\mathbb{R}$ Space* and whose algebra is *Introduction to the General Quaternionic Algebra*. The product is $\mathbb{R}$-bilinear and has $e_t$ as a left unit and no right one; the element theory of its square, its zero divisors, its roots and its idempotents is the Common Theory of the block. This article reads its **associativity defect**.

For a bilinear product the defect is the **associator**

$$
[\tilde q_1,\tilde q_2,\tilde q_3] = (\tilde q_1 \star \tilde q_2) \star \tilde q_3 - \tilde q_1 \star (\tilde q_2 \star \tilde q_3) ,
$$

an $\mathbb{R}$-trilinear map of three variables that vanishes identically exactly for an associative product (*Non-Associative Algebras and the Property Ladder*). For the plain multiplication $\tilde q_1\tilde q_2$ of the algebra it is identically zero, and the ladder of weaker identities — alternative, flexible, power-associative — records how far an algebra may depart from it. The quaternionic product departs at every rung.

The article establishes four things. First, the associator has the closed form $(\tilde q_2^{\natural}\tilde q_1 - \tilde q_1^{\natural}\tilde q_2^{\natural})\tilde q_3$, which reduces the defect to the insertion of the conjugation and yields a coordinate form linear in the first factor; on the basis it is the table of the sixteen coefficients $[e_\mu,e_\nu,\cdot]$. Second, the product satisfies **no** rung of the ladder: it fails flexibility and it fails third-power associativity, the weakest rung of all. Third, the general theory of a bilinear product attaches to its symmetrisation a **ternary product**, the linearisation of the quadratic representation; here that ternary product is computed and found to be central-valued. Fourth, the ternary product is $\mathbb{R}$-linear in each of its three variables — its parities are (linear, linear, linear) — but it fails the five-linear Jordan triple identity, so it is not the triple system that the general theory produces for an associative product.

## The Associator

**Theorem (the associator).** For all $\tilde q_1,\tilde q_2,\tilde q_3 \in \mathbb{H}$,

$$
\boxed{\;[\tilde q_1,\tilde q_2,\tilde q_3] = \bigl(\tilde q_2^{\natural}\tilde q_1 - \tilde q_1^{\natural}\tilde q_2^{\natural}\bigr)\tilde q_3\;}.
$$

*Proof.* Expand the definition and use that ${}^{\natural}$ is an anti-automorphism of order two: $(\tilde q_1\star\tilde q_2)^{\natural} = (\tilde q_1^{\natural}\tilde q_2)^{\natural} = \tilde q_2^{\natural}\tilde q_1^{\natural\natural} = \tilde q_2^{\natural}\tilde q_1$. Therefore

$$
(\tilde q_1\star\tilde q_2)\star\tilde q_3 = \tilde q_2^{\natural}\tilde q_1\tilde q_3 , \qquad \tilde q_1\star(\tilde q_2\star\tilde q_3) = \tilde q_1^{\natural}\,\tilde q_2^{\natural}\tilde q_3 ,
$$

and the difference is the displayed product on the right.

**Theorem (the coordinate form).** With $\vec q_1, \vec q_2$ the vector parts and $\vec q_1 \cdot \vec q_2$ their Euclidean inner product,

$$
\boxed{\;\tilde q_2^{\natural}\tilde q_1 - \tilde q_1^{\natural}\tilde q_2^{\natural} = 2\bigl((\vec q_1 \cdot \vec q_2)e_t + q_{2t}\vec q_1\bigr)\;}.
$$

*Proof.* Expand $\tilde q_2^{\natural}\tilde q_1 = (q_{2t} - \vec q_2)(q_{1t} + \vec q_1)$ and $\tilde q_1^{\natural}\tilde q_2^{\natural} = (q_{1t} - \vec q_1)(q_{2t} - \vec q_2)$ in the plain product using $\vec q_2\vec q_1 = -\,\vec q_2 \cdot \vec q_1 + \vec q_2 \times \vec q_1$, and subtract: the two cross products cancel and the two copies of each remaining term add to twice their common value.

**Remark.** The coordinate form is the measure of the defect, and it is short. The associator coefficient vanishes exactly when $(\vec q_1 \cdot \vec q_2)e_t + q_{2t}\vec q_1 = 0$, that is when $\vec q_1 = 0$ — the first factor central — or when $q_{2t} = 0$ with $\vec q_1$ orthogonal to $\vec q_2$ in the three-dimensional Euclidean sense. In every other case the defect is present, and it is proportional to the first factor.

**Theorem (the sixteen coefficients).** The associator is determined by its values on the basis triples. Writing $C_{\mu\nu}$ for the element with $[e_\mu,e_\nu,\tilde q_3] = C_{\mu\nu}\tilde q_3$, the coefficients are

| $C_{\mu\nu}$ | $\nu = t$ | $\nu = x$ | $\nu = y$ | $\nu = z$ |
|---|---|---|---|---|
| $\mu = t$ | $0$ | $0$ | $0$ | $0$ |
| $\mu = x$ | $2\vec e_x$ | $2e_t$ | $0$ | $0$ |
| $\mu = y$ | $2\vec e_y$ | $0$ | $2e_t$ | $0$ |
| $\mu = z$ | $2\vec e_z$ | $0$ | $0$ | $2e_t$ |

Six of the sixteen coefficients are nonzero: $C_{\mu t} = 2e_\mu$ for $\mu \neq t$ and $C_{\mu\mu} = 2e_t$ for $\mu \neq t$. Consequently $24$ of the $64$ triples of basis elements give a nonzero associator, each nonzero coefficient contributing the four values of the third slot.

*Proof.* The table is the coordinate formula read on the basis: $\vec q_1 \cdot \vec q_2$ is nonzero only for $\mu = \nu \neq t$, where it is $1$, and $q_{2t}$ is nonzero only for $\nu = t$, where it is $1$ and $C_{\mu t} = 2e_\mu$. The count is $6 \times 4 = 24$.

**Corollary (non-associativity).** The product is not associative: $[\vec e_x,e_t,e_t] = 2\vec e_x$, and the defect is detected on the basis alone.

## The Failure of the Weaker Laws

The associator is the strongest defect; the ladder records the weaker ones, and the quaternionic product fails them all (*Non-Associative Algebras and the Property Ladder*).

**Theorem (no rung of the ladder).** The product $\star$ is not alternative, not flexible and not power-associative; it fails even third-power associativity.

*Proof.* The **flexible** identity is $[\tilde q_1,\tilde q_2,\tilde q_1] = 0$. At $\tilde q_1 = \vec e_z$, $\tilde q_2 = e_t$,

$$
(\vec e_z \star e_t) \star \vec e_z = (-\vec e_z) \star \vec e_z = (-\vec e_z)^{\natural}\vec e_z = \vec e_z\vec e_z = -e_t , \qquad \vec e_z \star (e_t \star \vec e_z) = \vec e_z \star \vec e_z = \vec e_z^{\natural}\vec e_z = -\vec e_z^2 = e_t ,
$$

so the two sides are $-e_t$ and $e_t$. The **third-power** identity is $(\tilde q \star \tilde q) \star \tilde q = \tilde q \star (\tilde q \star \tilde q)$; at $\tilde q = \vec e_z$ one has $\tilde q \star \tilde q = \langle \vec e_z\rangle_{\natural}e_t = e_t$, so the left side is $e_t \star \vec e_z = e_t^{\natural}\vec e_z = \vec e_z$ while the right side is $\vec e_z \star e_t = \vec e_z^{\natural} = -\vec e_z$, and the identity fails. Since flexibility implies third-power associativity and is implied by alternativity, and since power-associativity implies third-power associativity, the failure of the weakest rung denies the stronger ones: the product satisfies none.

**Corollary.** The product is not alternative, and the alternative product of two factors with a third is not controlled by the associator; the identities available in an alternative algebra, and with them a calculus of powers of a single element, are not available here. The product is also not flexible, so the manipulation $(\tilde q_1 \star \tilde q_2) \star \tilde q_1 = \tilde q_1 \star (\tilde q_2 \star \tilde q_1)$ cannot be used, and the left and the right multiplication operators of the operator articles of the block do not commute with one another.

**Remark.** Both witnesses are read off the coordinates alone, and the mechanism is the same in both: the square $\tilde q \star \tilde q = \langle\tilde q\rangle_{\natural}e_t$ is central, so the left-hand reading of a square multiplies it by the scalar part of the element, whereas the right-hand reading passes the element through ${}^{\natural}$ and negates its vector part; the two readings differ as soon as the element is not central.

## The Ternary Product

The general theory of a bilinear product attaches to it, through its symmetrisation, a **ternary** operation (*The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*). The **symmetrised product** of the quaternionic multiplication is

$$
\tilde q_1 \bullet \tilde q_2 = \tfrac12\bigl(\tilde q_1 \star \tilde q_2 + \tilde q_2 \star \tilde q_1\bigr) ,
$$

the commutative companion of $\star$, written with the bare bullet as in the symmetric quaternionic block (*The Specificities of the Symmetric Quaternionic Algebra*, below this article in this category); its full reading is *The Symmetrised Quaternionic Product and the Hermitian Subspace*, below this article in this category, and only its definition and its value are used here.

**Lemma.** The symmetrised product is central-valued:

$$
\boxed{\;\tilde q_1 \bullet \tilde q_2 = \beta(\tilde q_1,\tilde q_2)\,e_t , \qquad \beta(\tilde q_1,\tilde q_2) = q_{1t}q_{2t} + \vec q_1 \cdot \vec q_2\;}.
$$

*Proof.* The two summands are $\tilde q_1^{\natural}\tilde q_2$ and $\tilde q_2^{\natural}\tilde q_1$, whose vector parts are $q_{1t}\vec q_2 - q_{2t}\vec q_1 - \vec q_1 \times \vec q_2$ and $q_{2t}\vec q_1 - q_{1t}\vec q_2 - \vec q_2 \times \vec q_1$; the cross products cancel by antisymmetry, the two copies of $q_{1t}\vec q_2 - q_{2t}\vec q_1$ cancel in the half-sum, and the scalar parts add to $2\beta(\tilde q_1,\tilde q_2)$.

**Definition.** The **ternary product** of the quaternionic multiplication is the ternary operation generated by the symmetrisation,

$$
\{\tilde q_1,\tilde q_2,\tilde q_3\} = (\tilde q_1 \bullet \tilde q_2) \bullet \tilde q_3 + (\tilde q_3 \bullet \tilde q_2) \bullet \tilde q_1 - (\tilde q_1 \bullet \tilde q_3) \bullet \tilde q_2 .
$$

**Theorem (the ternary product).** For all $\tilde q_1,\tilde q_2,\tilde q_3 \in \mathbb{H}$,

$$
\boxed{\;\{\tilde q_1,\tilde q_2,\tilde q_3\} = \Bigl(\beta(\tilde q_1,\tilde q_2)\,q_{3t} + \beta(\tilde q_3,\tilde q_2)\,q_{1t} - \beta(\tilde q_1,\tilde q_3)\,q_{2t}\Bigr)e_t\;}.
$$

In particular the ternary product is central-valued, and it depends only on the scalar coordinates $q_{1t},q_{2t},q_{3t}$ and on the pairings $\beta$ among the three arguments.

*Proof.* By the lemma each inner symmetrisation is a central multiple of $e_t$. For a central element $\lambda e_t$ one has $(\lambda e_t) \bullet \tilde q = \lambda\,(e_t \bullet \tilde q) = \lambda q_te_t$, because $e_t \bullet \tilde q = \tfrac12(e_t \star \tilde q + \tilde q \star e_t) = \tfrac12(\tilde q + \tilde q^{\natural}) = q_te_t$. Applying this to the three terms gives $\beta(\tilde q_1,\tilde q_2)q_{3t}e_t$, $\beta(\tilde q_3,\tilde q_2)q_{1t}e_t$ and $-\beta(\tilde q_1,\tilde q_3)q_{2t}e_t$, whose sum is displayed.

**Example.** At $\tilde q_1 = \tilde q_2 = \tilde q_3 = e_t$ every pairing is $1$ and every scalar coordinate is $1$, so the value is $(1+1-1)e_t = e_t$; at $\tilde q_1 = \tilde q_2 = \tilde q_3 = \vec e_z$ the pairings are still $1$ but the scalar coordinates vanish, so the value is $0$. The ternary product does not vanish on every triple of nonzero elements: its value is the displayed scalar combination, and it vanishes exactly when $\beta(\tilde q_1,\tilde q_2)q_{3t} + \beta(\tilde q_3,\tilde q_2)q_{1t} = \beta(\tilde q_1,\tilde q_3)q_{2t}$.

## The Parities and the Triple Identity

**Proposition (the parities).** The ternary product is $\mathbb{R}$-linear in each of its three variables: $\{\lambda\tilde q_1,\tilde q_2,\tilde q_3\} = \lambda\{\tilde q_1,\tilde q_2,\tilde q_3\} = \{\tilde q_1,\lambda\tilde q_2,\tilde q_3\} = \{\tilde q_1,\tilde q_2,\lambda\tilde q_3\}$ for $\lambda \in \mathbb{R}$. Its parities are (linear, linear, linear), and $\{\cdot,\cdot,\cdot\}$ is an $\mathbb{R}$-trilinear map $\mathbb{H} \times \mathbb{H} \times \mathbb{H} \to \mathbb{H}$.

*Proof.* The symmetrisation $\bullet$ is $\mathbb{R}$-bilinear because $\star$ is and ${}^{\natural}$ is $\mathbb{R}$-linear, and the ternary product is built from $\bullet$ by composition and addition, hence is $\mathbb{R}$-trilinear. This is the bilinear case of the parity bookkeeping of *Algebraic J\*-Algebras*; here no slot carries a conjugation.

**Proposition (outer symmetry).** $\{\tilde q_1,\tilde q_2,\tilde q_3\} = \{\tilde q_3,\tilde q_2,\tilde q_1\}$.

*Proof.* Immediate from the formula: the roles of $q_{1t}$ and $q_{3t}$ are exchanged, and $\beta$ is symmetric.

The general theory attaches to a bilinear product whose symmetrisation is a Jordan product a ternary operation that satisfies the five-linear **Jordan triple identity** (*The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*). Here the symmetrisation is not a Jordan product — *The Symmetrised Quaternionic Product and the Hermitian Subspace*, below this article in this category, exhibits its failure of the Jordan identity — and the triple identity goes with it.

**Theorem (the triple identity fails).** The Jordan triple identity

$$
\{x,y,\{u,v,w\}\} = \{\{x,y,u\},v,w\} - \{u,\{y,x,v\},w\} + \{u,v,\{x,y,w\}\}
$$

fails for the ternary product of the quaternionic multiplication. At $(x,y,u,v,w) = (e_t,e_t,\vec e_x,e_t,\vec e_x)$ the left-hand side is $-e_t$ and the right-hand side is $e_t$.

*Proof.* The value $\{u,v,w\} = \{\vec e_x,e_t,\vec e_x\}$ is $-e_t$, since $\beta(\vec e_x,\vec e_x) = 1$ and the other pairings vanish; then $\{x,y,\{u,v,w\}\} = \{e_t,e_t,-e_t\}$ has the coefficient $\beta(e_t,e_t)(-1) = -1$, so the left side is $-e_t$. On the right, $\{x,y,u\} = \{e_t,e_t,\vec e_x\} = 0$, so the first group vanishes, while $\{y,x,v\} = \{e_t,e_t,e_t\} = e_t$ and $\{u,v,\{x,y,w\}\} = \{\vec e_x,e_t,\{e_t,e_t,\vec e_x\}\} = \{\vec e_x,e_t,0\} = 0$; hence the right side is $\{u,\{y,x,v\},w\} = \{\vec e_x,e_t,\vec e_x\}$, taken with the minus sign of the middle term, that is $e_t$. The two sides are $-e_t$ and $+e_t$.

**Remark.** The two failures are not independent. The ternary product is the linearisation of the quadratic representation $U_{\tilde q_1}\tilde q_2 = \tilde q_1 \bullet (\tilde q_2 \bullet \tilde q_1)$ of the symmetrisation, and the Jordan triple identity for the ternary product is the linearised form of the Jordan identity for the symmetrisation; since the symmetrisation is not a Jordan algebra, neither identity can hold. The detailed failure of the Jordan identity, at $x = y = \vec e_x$, is the next article; the witness above is the same failure read one level up, on five variables instead of three.

## Summary

The quaternionic product is not associative, and its associator has the closed form $(\tilde q_2^{\natural}\tilde q_1 - \tilde q_1^{\natural}\tilde q_2^{\natural})\tilde q_3$, with the coordinate form $2((\vec q_1 \cdot \vec q_2)e_t + q_{2t}\vec q_1)\tilde q_3$; the sixteen coefficients $[e_\mu,e_\nu,\cdot]$ have six nonzero entries and $24$ of the $64$ basis triples are nonzero. The product satisfies no rung of the ladder of weaker identities: it fails flexibility at $(\vec e_z,e_t)$ and it fails the weakest rung, third-power associativity, so it is not alternative, not flexible and not power-associative. The general theory attaches a ternary operation to the symmetrisation; here the symmetrisation is the central-valued $\tilde q_1 \bullet \tilde q_2 = \beta(\tilde q_1,\tilde q_2)e_t$, and the ternary product is central-valued, $\mathbb{R}$-linear in its three variables, symmetric in its outer two, and fails the five-linear Jordan triple identity at $(e_t,e_t,\vec e_x,e_t,\vec e_x)$. The plain multiplication is the contrast throughout: its associator vanishes identically, it satisfies every rung of the ladder, and its ternary product is a Jordan triple system.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra, the real space of the block |
| $\tilde q = \sum_\mu q_\mu e_\mu$ | an element and its four real coordinates |
| $\vec q = \sum_k q_k\vec e_k$ | the vector part |
| $\vec q_1 \cdot \vec q_2$ | the Euclidean inner product of the vector parts |
| $\vec q_1 \times \vec q_2$ | the cross product of the vector parts |
| ${}^{\natural}$ | the conjugation $\tilde q^{\natural} = q_t - \vec q$ |
| $\tilde q_1 \star \tilde q_2 = \tilde q_1^{\natural}\tilde q_2$ | the general quaternionic bilinear product |
| $[\tilde q_1,\tilde q_2,\tilde q_3] = (\tilde q_1 \star \tilde q_2) \star \tilde q_3 - \tilde q_1 \star (\tilde q_2 \star \tilde q_3)$ | the associator of the product |
| $C_{\mu\nu}$ | the associator coefficients, $[e_\mu,e_\nu,\tilde q_3] = C_{\mu\nu}\tilde q_3$ |
| $\tilde q_1 \bullet \tilde q_2 = \tfrac12(\tilde q_1 \star \tilde q_2 + \tilde q_2 \star \tilde q_1)$ | the symmetrised product |
| $\beta(\tilde q_1,\tilde q_2) = q_{1t}q_{2t} + \vec q_1 \cdot \vec q_2$ | its central coefficient |
| $\{\tilde q_1,\tilde q_2,\tilde q_3\}$ | the ternary product of the symmetrisation |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the associator, the flexible law and power-associativity.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the ternary product as the linearisation of the quadratic representation and for the Jordan triple identity.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the associator of a multiplication on a module and its trilinearity.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the associator of a product with an anti-automorphism inserted in a slot.
