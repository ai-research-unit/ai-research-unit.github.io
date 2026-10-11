# __The Associator and the Ternary Product of the Quaternionic Product__

## Introduction

The product of this block is the **general quaternionic bilinear product**

$$
\tilde p \star \tilde q = \tilde p^{\natural}\tilde q , \qquad \tilde p^{\natural} = p_0 - \mathbf p ,
$$

the second of the two bilinear products of the quaternion real space, whose rule is *The Two General Products of the Quaternion $\mathbb{R}$ Space* and whose algebra is *Introduction to the General Quaternionic Algebra of Quaternions*. The product is $\mathbb{R}$-bilinear and has $e_0$ as a left unit and no right one; the element theory of its square, its zero divisors, its roots and its idempotents is the Common Theory of the block. This article reads its **associativity defect**.

For a bilinear product the defect is the **associator**

$$
[\tilde p,\tilde q,\tilde r] = (\tilde p \star \tilde q) \star \tilde r - \tilde p \star (\tilde q \star \tilde r) ,
$$

an $\mathbb{R}$-trilinear map of three variables that vanishes identically exactly for an associative product (*Non-Associative Algebras and the Property Ladder*). For the plain multiplication $\tilde p\tilde q$ of the algebra it is identically zero, and the ladder of weaker identities — alternative, flexible, power-associative — records how far an algebra may depart from it. The quaternionic product departs at every rung.

The article establishes four things. First, the associator has the closed form $(\tilde q^{\natural}\tilde p - \tilde p^{\natural}\tilde q^{\natural})\tilde r$, which reduces the defect to the insertion of the conjugation and yields a coordinate form linear in the first factor; on the basis it is the table of the sixteen coefficients $[e_\mu,e_\nu,\cdot]$. Second, the product satisfies **no** rung of the ladder: it fails flexibility and it fails third-power associativity, the weakest rung of all. Third, the general theory of a bilinear product attaches to its symmetrisation a **ternary product**, the linearisation of the quadratic representation; here that ternary product is computed and found to be central-valued. Fourth, the ternary product is $\mathbb{R}$-linear in each of its three variables — its parities are (linear, linear, linear) — but it fails the five-linear Jordan triple identity, so it is not the triple system that the general theory produces for an associative product.

## The Associator

**Theorem (the associator).** For all $\tilde p,\tilde q,\tilde r \in \mathbb{H}$,

$$
[\tilde p,\tilde q,\tilde r] = \bigl(\tilde q^{\natural}\tilde p - \tilde p^{\natural}\tilde q^{\natural}\bigr)\tilde r .
$$

*Proof.* Expand the definition and use that ${}^{\natural}$ is an anti-automorphism of order two: $(\tilde p\star\tilde q)^{\natural} = (\tilde p^{\natural}\tilde q)^{\natural} = \tilde q^{\natural}\tilde p^{\natural\natural} = \tilde q^{\natural}\tilde p$. Therefore

$$
(\tilde p\star\tilde q)\star\tilde r = \tilde q^{\natural}\tilde p\tilde r , \qquad \tilde p\star(\tilde q\star\tilde r) = \tilde p^{\natural}\,\tilde q^{\natural}\tilde r ,
$$

and the difference is the displayed product on the right.

**Theorem (the coordinate form).** With $\mathbf p, \mathbf q$ the vector parts and $\mathbf p \cdot \mathbf q$ their Euclidean inner product,

$$
\tilde q^{\natural}\tilde p - \tilde p^{\natural}\tilde q^{\natural} = 2\bigl((\mathbf p \cdot \mathbf q)e_0 + q_0\mathbf p\bigr) .
$$

*Proof.* Expand $\tilde q^{\natural}\tilde p = (q_0 - \mathbf q)(p_0 + \mathbf p)$ and $\tilde p^{\natural}\tilde q^{\natural} = (p_0 - \mathbf p)(q_0 - \mathbf q)$ in the plain product using $\mathbf q\mathbf p = -\,\mathbf q \cdot \mathbf p + \mathbf q \times \mathbf p$, and subtract: the two cross products cancel and the two copies of each remaining term add to twice their common value.

**Remark.** The coordinate form is the measure of the defect, and it is short. The associator coefficient vanishes exactly when $(\mathbf p \cdot \mathbf q)e_0 + q_0\mathbf p = 0$, that is when $\mathbf p = 0$ — the first factor central — or when $q_0 = 0$ with $\mathbf p$ orthogonal to $\mathbf q$ in the three-dimensional Euclidean sense. In every other case the defect is present, and it is proportional to the first factor.

**Theorem (the sixteen coefficients).** The associator is determined by its values on the basis triples. Writing $C_{\mu\nu}$ for the element with $[\tilde e_\mu,\tilde e_\nu,\tilde r] = C_{\mu\nu}\tilde r$, the coefficients are

| $C_{\mu\nu}$ | $\nu = 0$ | $\nu = 1$ | $\nu = 2$ | $\nu = 3$ |
|---|---|---|---|---|
| $\mu = 0$ | $0$ | $0$ | $0$ | $0$ |
| $\mu = 1$ | $2e_1$ | $2e_0$ | $0$ | $0$ |
| $\mu = 2$ | $2e_2$ | $0$ | $2e_0$ | $0$ |
| $\mu = 3$ | $2e_3$ | $0$ | $0$ | $2e_0$ |

Six of the sixteen coefficients are nonzero: $C_{\mu 0} = 2e_\mu$ for $\mu \neq 0$ and $C_{\mu\mu} = 2e_0$ for $\mu \neq 0$. Consequently $24$ of the $64$ triples of basis elements give a nonzero associator, each nonzero coefficient contributing the four values of the third slot.

*Proof.* The table is the coordinate formula read on the basis: $\mathbf p \cdot \mathbf q$ is nonzero only for $\mu = \nu \neq 0$, where it is $1$, and $q_0$ is nonzero only for $\nu = 0$, where it is $1$ and $C_{\mu 0} = 2e_\mu$. The count is $6 \times 4 = 24$.

**Corollary (non-associativity).** The product is not associative: $[e_1,e_0,e_0] = 2e_1$, and the defect is detected on the basis alone.

## The Failure of the Weaker Laws

The associator is the strongest defect; the ladder records the weaker ones, and the quaternionic product fails them all (*Non-Associative Algebras and the Property Ladder*).

**Theorem (no rung of the ladder).** The product $\star$ is not alternative, not flexible and not power-associative; it fails even third-power associativity.

*Proof.* The **flexible** identity is $[\tilde p,\tilde q,\tilde p] = 0$. At $\tilde p = e_3$, $\tilde q = e_0$,

$$
(e_3 \star e_0) \star e_3 = (-e_3) \star e_3 = (-e_3)^{\natural}e_3 = e_3e_3 = -e_0 , \qquad e_3 \star (e_0 \star e_3) = e_3 \star e_3 = e_3^{\natural}e_3 = -e_3^2 = e_0 ,
$$

so the two sides are $-e_0$ and $e_0$. The **third-power** identity is $(\tilde p \star \tilde p) \star \tilde p = \tilde p \star (\tilde p \star \tilde p)$; at $\tilde p = e_3$ one has $\tilde p \star \tilde p = N(e_3)e_0 = e_0$, so the left side is $e_0 \star e_3 = e_0^{\natural}e_3 = e_3$ while the right side is $e_3 \star e_0 = e_3^{\natural} = -e_3$, and the identity fails. Since flexibility implies third-power associativity and is implied by alternativity, and since power-associativity implies third-power associativity, the failure of the weakest rung denies the stronger ones: the product satisfies none.

**Corollary.** The product is not alternative, and the alternative product of two factors with a third is not controlled by the associator; the identities available in an alternative algebra, and with them a calculus of powers of a single element, are not available here. The product is also not flexible, so the manipulation $(\tilde p \star \tilde q) \star \tilde p = \tilde p \star (\tilde q \star \tilde p)$ cannot be used, and the left and the right multiplication operators of the operator articles of the block do not commute with one another.

**Remark.** Both witnesses are read off the coordinates alone, and the mechanism is the same in both: the square $\tilde q \star \tilde q = N(\tilde q)e_0$ is central, so the left-hand reading of a square multiplies it by the scalar part of the element, whereas the right-hand reading passes the element through ${}^{\natural}$ and negates its vector part; the two readings differ as soon as the element is not central.

## The Ternary Product

The general theory of a bilinear product attaches to it, through its symmetrisation, a **ternary** operation (*The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*). The **symmetrised product** of the quaternionic multiplication is

$$
\tilde p \bullet \tilde q = \tfrac12\bigl(\tilde p \star \tilde q + \tilde q \star \tilde p\bigr) ,
$$

the commutative companion of $\star$, written with the bare bullet as in the symmetric quaternionic block (*The Specificities of the Symmetric Quaternionic Algebra*, below this article in this category); its full reading is *The Symmetrised Quaternionic Product and the Hermitian Subspace*, below this article in this category, and only its definition and its value are used here.

**Lemma.** The symmetrised product is central-valued:

$$
\tilde p \bullet \tilde q = \beta(\tilde p,\tilde q)\,e_0 , \qquad \beta(\tilde p,\tilde q) = p_0q_0 + \mathbf p \cdot \mathbf q .
$$

*Proof.* The two summands are $\tilde p^{\natural}\tilde q$ and $\tilde q^{\natural}\tilde p$, whose vector parts are $p_0\mathbf q - q_0\mathbf p - \mathbf p \times \mathbf q$ and $q_0\mathbf p - p_0\mathbf q - \mathbf q \times \mathbf p$; the cross products cancel by antisymmetry, the two copies of $p_0\mathbf q - q_0\mathbf p$ cancel in the half-sum, and the scalar parts add to $2\beta(\tilde p,\tilde q)$.

**Definition.** The **ternary product** of the quaternionic multiplication is the ternary operation generated by the symmetrisation,

$$
\{\tilde p,\tilde q,\tilde r\} = (\tilde p \bullet \tilde q) \bullet \tilde r + (\tilde r \bullet \tilde q) \bullet \tilde p - (\tilde p \bullet \tilde r) \bullet \tilde q .
$$

**Theorem (the ternary product).** For all $\tilde p,\tilde q,\tilde r \in \mathbb{H}$,

$$
\{\tilde p,\tilde q,\tilde r\} = \Bigl(\beta(\tilde p,\tilde q)\,r_0 + \beta(\tilde r,\tilde q)\,p_0 - \beta(\tilde p,\tilde r)\,q_0\Bigr)e_0 .
$$

In particular the ternary product is central-valued, and it depends only on the scalar coordinates $p_0,q_0,r_0$ and on the pairings $\beta$ among the three arguments.

*Proof.* By the lemma each inner symmetrisation is a central multiple of $e_0$. For a central element $\lambda e_0$ one has $(\lambda e_0) \bullet \tilde x = \lambda\,(e_0 \bullet \tilde x) = \lambda x_0e_0$, because $e_0 \bullet \tilde x = \tfrac12(e_0 \star \tilde x + \tilde x \star e_0) = \tfrac12(\tilde x + \tilde x^{\natural}) = x_0e_0$. Applying this to the three terms gives $\beta(\tilde p,\tilde q)r_0e_0$, $\beta(\tilde r,\tilde q)p_0e_0$ and $-\beta(\tilde p,\tilde r)q_0e_0$, whose sum is displayed.

**Example.** At $\tilde p = \tilde q = \tilde r = e_0$ every pairing is $1$ and every scalar coordinate is $1$, so the value is $(1+1-1)e_0 = e_0$; at $\tilde p = \tilde q = \tilde r = e_3$ the pairings are still $1$ but the scalar coordinates vanish, so the value is $0$. The ternary product does not vanish on every triple of nonzero elements: its value is the displayed scalar combination, and it vanishes exactly when $\beta(\tilde p,\tilde q)r_0 + \beta(\tilde r,\tilde q)p_0 = \beta(\tilde p,\tilde r)q_0$.

## The Parities and the Triple Identity

**Proposition (the parities).** The ternary product is $\mathbb{R}$-linear in each of its three variables: $\{\lambda\tilde p,\tilde q,\tilde r\} = \lambda\{\tilde p,\tilde q,\tilde r\} = \{\tilde p,\lambda\tilde q,\tilde r\} = \{\tilde p,\tilde q,\lambda\tilde r\}$ for $\lambda \in \mathbb{R}$. Its parities are (linear, linear, linear), and $\{\cdot,\cdot,\cdot\}$ is an $\mathbb{R}$-trilinear map $\mathbb{H} \times \mathbb{H} \times \mathbb{H} \to \mathbb{H}$.

*Proof.* The symmetrisation $\bullet$ is $\mathbb{R}$-bilinear because $\star$ is and ${}^{\natural}$ is $\mathbb{R}$-linear, and the ternary product is built from $\bullet$ by composition and addition, hence is $\mathbb{R}$-trilinear. This is the bilinear case of the parity bookkeeping of *Algebraic J\*-Algebras*, where the middle slot of a sesquilinear ternary product carries the conjugation; here no slot does.

**Proposition (outer symmetry).** $\{\tilde p,\tilde q,\tilde r\} = \{\tilde r,\tilde q,\tilde p\}$.

*Proof.* Immediate from the formula: the roles of $p_0$ and $r_0$ are exchanged, and $\beta$ is symmetric.

The general theory attaches to a bilinear product whose symmetrisation is a Jordan product a ternary operation that satisfies the five-linear **Jordan triple identity** (*The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*). Here the symmetrisation is not a Jordan product — *The Symmetrised Quaternionic Product and the Hermitian Subspace*, below this article in this category, exhibits its failure of the Jordan identity — and the triple identity goes with it.

**Theorem (the triple identity fails).** The Jordan triple identity

$$
\{x,y,\{u,v,w\}\} = \{\{x,y,u\},v,w\} - \{u,\{y,x,v\},w\} + \{u,v,\{x,y,w\}\}
$$

fails for the ternary product of the quaternionic multiplication. At $(x,y,u,v,w) = (e_0,e_0,e_1,e_0,e_1)$ the left-hand side is $-e_0$ and the right-hand side is $e_0$.

*Proof.* The value $\{u,v,w\} = \{e_1,e_0,e_1\}$ is $-e_0$, since $\beta(e_1,e_1) = 1$ and the other pairings vanish; then $\{x,y,\{u,v,w\}\} = \{e_0,e_0,-e_0\}$ has the coefficient $\beta(e_0,e_0)(-1) = -1$, so the left side is $-e_0$. On the right, $\{x,y,u\} = \{e_0,e_0,e_1\} = 0$, so the first group vanishes, while $\{y,x,v\} = \{e_0,e_0,e_0\} = e_0$ and $\{u,v,\{x,y,w\}\} = \{e_1,e_0,\{e_0,e_0,e_1\}\} = \{e_1,e_0,0\} = 0$; hence the right side is $\{u,\{y,x,v\},w\} = \{e_1,e_0,e_1\}$, taken with the minus sign of the middle term, that is $e_0$. The two sides are $-e_0$ and $+e_0$.

**Remark.** The two failures are not independent. The ternary product is the linearisation of the quadratic representation $U_{\tilde p}\tilde q = \tilde p \bullet (\tilde q \bullet \tilde p)$ of the symmetrisation, and the Jordan triple identity for the ternary product is the linearised form of the Jordan identity for the symmetrisation; since the symmetrisation is not a Jordan algebra, neither identity can hold. The detailed failure of the Jordan identity, at $x = y = e_1$, is the next article; the witness above is the same failure read one level up, on five variables instead of three.

## The Comparison with the Biquaternion Case

**Proposition.** The closed form of the associator, the coordinate form, the table of the sixteen coefficients and the formula of the ternary product are the same over $\mathbb{C}$ as over $\mathbb{R}$, the structure constants of the law being the same; the difference is in what the formulas allow. Over $\mathbb{R}$ the ternary product is central-valued with a definite pairing $\beta$ and the associator coefficient vanishes on the thin set described above; over the biquaternion space $\mathbb{B}$ the same formulas hold, the pairing $\beta$ is the complex bilinear form rather than a definite one, and the ternary product is the object of *The Associator and the Ternary Product of the Quaternionic Product* of that chapter.

*Proof.* The product $\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q$ of the biquaternion chapter restricts to the quaternionic product on the real quaternion subspace, and the associator and the symmetrisation are defined by the same formulas; the coefficient tables agree because the multiplication table of the units is the same.

**Remark (where the article's objects are read again).** The two-sided operators generated by the left and right multiplications of the product, and with them the operator form of the associator, are *Two-Sided Operators on the General Quaternionic Algebra of Quaternions*, below this article in this category; the ternary product read in the two matrix models of the block is *The General Quaternionic Algebra in the 2×2 Matrix Element Representation $M_2(\mathbb{C})$* and *The General Quaternionic Algebra in the 4×4 Matrix Element Representation $M_4(\mathbb{R})_L$*, both below this article in this category, where the associator becomes a matrix identity.

## Summary

The quaternionic product is not associative, and its associator has the closed form $(\tilde q^{\natural}\tilde p - \tilde p^{\natural}\tilde q^{\natural})\tilde r$, with the coordinate form $2((\mathbf p \cdot \mathbf q)e_0 + q_0\mathbf p)\tilde r$; the sixteen coefficients $[e_\mu,e_\nu,\cdot]$ have six nonzero entries and $24$ of the $64$ basis triples are nonzero. The product satisfies no rung of the ladder of weaker identities: it fails flexibility at $(e_3,e_0)$ and it fails the weakest rung, third-power associativity, so it is not alternative, not flexible and not power-associative. The general theory attaches a ternary operation to the symmetrisation; here the symmetrisation is the central-valued $\tilde p \bullet \tilde q = \beta(\tilde p,\tilde q)e_0$, and the ternary product is central-valued, $\mathbb{R}$-linear in its three variables, symmetric in its outer two, and fails the five-linear Jordan triple identity at $(e_0,e_0,e_1,e_0,e_1)$. The plain multiplication is the contrast throughout: its associator vanishes identically, it satisfies every rung of the ladder, and its ternary product is a Jordan triple system.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra, the real space of the block |
| $\tilde p = \sum_\mu p_\mu e_\mu$ | an element and its four real coordinates |
| $\mathbf p = \sum_k p_ke_k$ | the vector part |
| $\mathbf p \cdot \mathbf q$ | the Euclidean inner product of the vector parts |
| $\mathbf p \times \mathbf q$ | the cross product of the vector parts |
| ${}^{\natural}$ | the conjugation $\tilde p^{\natural} = p_0 - \mathbf p$ |
| $\tilde p \star \tilde q = \tilde p^{\natural}\tilde q$ | the general quaternionic bilinear product |
| $[\tilde p,\tilde q,\tilde r] = (\tilde p \star \tilde q) \star \tilde r - \tilde p \star (\tilde q \star \tilde r)$ | the associator of the product |
| $C_{\mu\nu}$ | the associator coefficients, $[e_\mu,e_\nu,\tilde r] = C_{\mu\nu}\tilde r$ |
| $\tilde p \bullet \tilde q = \tfrac12(\tilde p \star \tilde q + \tilde q \star \tilde p)$ | the symmetrised product |
| $\beta(\tilde p,\tilde q) = p_0q_0 + \mathbf p \cdot \mathbf q$ | its central coefficient |
| $\{\tilde p,\tilde q,\tilde r\}$ | the ternary product of the symmetrisation |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the associator, the flexible law and power-associativity.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the ternary product as the linearisation of the quadratic representation and for the Jordan triple identity.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the associator of a multiplication on a module and its trilinearity.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the associator of a product with an anti-automorphism inserted in a slot.
