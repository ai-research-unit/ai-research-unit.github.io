
# __The Associator and the Ternary Product of the Quaternionic Product__

## Introduction

The product of this group is the **general quaternionic bilinear product**

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q , \qquad \tilde P^{\natural} = P_0 - \mathbf P ,
$$

the second of the four products of the biquaternion algebra $\mathbb{B}$, whose rule is *The Four Biquaternion Complex Products* §*The General Quaternionic Bilinear Product* and whose algebra is *Introduction to the General Quaternionic Algebra of Biquaternions*. The product is $\mathbb{C}$-bilinear and has $e_0$ as a left unit and no right one; the previous two articles read its square, its idempotents and its zero divisors. This article reads its **associativity defect**.

For a bilinear product the defect is the **associator**

$$
[\tilde P,\tilde Q,\tilde R] = (\tilde P\star\tilde Q)\star\tilde R - \tilde P\star(\tilde Q\star\tilde R) ,
$$

a $\mathbb{C}$-trilinear map of three variables that vanishes identically exactly for an associative product (*Non-Associative Algebras and the Property Ladder* §*Algebras, the Associator and Linearisation*). For the associative multiplication $\tilde P\tilde Q$ of the algebra it is identically zero, and the ladder of weaker identities — alternative, flexible, power-associative — is the record of how far an algebra may depart from it. The quaternionic product departs from it at every rung.

The article establishes four things. First, the associator has the closed form

$$
[\tilde P,\tilde Q,\tilde R] = \bigl(\tilde Q^{\natural}\tilde P - \tilde P^{\natural}\tilde Q^{\natural}\bigr)\tilde R ,
$$

which reduces the defect to the insertion of the conjugation and shows at once that it is nonzero. Second, the product satisfies **no** rung of the ladder: it fails the flexible identity, and it fails the weakest rung of all, third-power associativity. Third, the general theory of a bilinear product attaches to its symmetrisation a **ternary product** $\{\tilde P,\tilde Q,\tilde R\}$, the linearisation of the quadratic representation; here that ternary product is computed and found to be central-valued. Fourth, the ternary product is $\mathbb{C}$-linear in each of its three variables — its parities are (linear, linear, linear) — but it fails the five-linear Jordan triple identity, so it is not the triple system that the general theory produces for an associative product.

## The Associator

**Theorem (the associator).** For all $\tilde P,\tilde Q,\tilde R \in \mathbb{B}$,

$$
[\tilde P,\tilde Q,\tilde R] = \bigl(\tilde Q^{\natural}\tilde P - \tilde P^{\natural}\tilde Q^{\natural}\bigr)\tilde R .
$$

**Proof.** Expand the definition and use that ${}^{\natural}$ is an anti-automorphism of order two: $(\tilde P\star\tilde Q)^{\natural} = (\tilde P^{\natural}\tilde Q)^{\natural} = \tilde Q^{\natural}\tilde P$. Therefore

$$
(\tilde P\star\tilde Q)\star\tilde R = \tilde Q^{\natural}\tilde P\tilde R , \qquad \tilde P\star(\tilde Q\star\tilde R) = \tilde P^{\natural}\,\tilde Q^{\natural}\tilde R ,
$$

and the difference is the displayed product on the right. $\square$

The associator is a $\mathbb{C}$-trilinear map, so it is determined by its values on the $64$ triples of basis elements; on those triples it is computed from the multiplication table.

**Theorem (non-associativity).** The quaternionic product is not associative: $[\tilde P,\tilde Q,\tilde R] \neq 0$ on explicit triples. In particular

$$
[e_1,e_0,e_0] = \bigl(e_0^{\natural}e_1 - e_1^{\natural}e_0^{\natural}\bigr)e_0 = \bigl(e_1 + e_1\bigr)e_0 = 2e_1 ,
$$

and $24$ of the $64$ triples of basis elements give a nonzero associator.

**Proof.** The computation displayed uses $e_0^{\natural} = e_0$ and $e_1^{\natural} = -e_1$; the count is the enumeration of the $64$ triples against the closed form. $\square$

**Remark.** The alternation of the two signs in the closed form is the whole mechanism: the first term is the plain product with the conjugation inserted in the middle, $(\tilde Q^{\natural}\tilde P)\tilde R$, and the second is the plain product with the conjugation inserted in the first and the second slot, $(\tilde P^{\natural}\tilde Q^{\natural})\tilde R$. The two agree when the conjugation can be moved across the first two factors without cost, that is when $\tilde P^\natural\tilde Q^\natural = \tilde Q^\natural\tilde P$; the associator therefore measures the failure of the two conjugated factors to commute inside the plain product. For the associative multiplication the associator $(\tilde P\tilde Q)\tilde R - \tilde P(\tilde Q\tilde R)$ vanishes identically, by associativity alone; the quaternionic associator does not vanish, because the insertion of ${}^{\natural}$ in the first slot is exactly what associativity cannot absorb.

## The Failure of the Weaker Laws

The associator is the strongest defect; the ladder records the weaker ones, and the quaternionic product fails them all (*Comparison Between the Four Biquaternion Products* §*Alternative, Flexible and Power Associative*).

**Theorem (no rung of the ladder).** The product $\star$ is not alternative, not flexible and not power-associative; it fails even third-power associativity.

**Proof.** The **flexible** identity is $[\tilde P,\tilde Q,\tilde P] = 0$, that is $(\tilde P\star\tilde Q)\star\tilde P = \tilde P\star(\tilde Q\star\tilde P)$. At $\tilde P = e_3$, $\tilde Q = e_0$,

$$
(e_3\star e_0)\star e_3 = (-e_3)\star e_3 = e_3e_3 = -e_0 , \qquad e_3\star(e_0\star e_3) = e_3\star e_3 = e_3^{\natural}e_3 = -e_3^2 = e_0 ,
$$

so the two sides are $-e_0$ and $e_0$ and the identity fails. The **third-power** identity is $(\tilde P\star\tilde P)\star\tilde P = \tilde P\star(\tilde P\star\tilde P)$; at $\tilde P = e_3$ the two sides are $(-e_0)\star e_3 = -e_3$ and $e_3\star(-e_0) = e_3$, so it fails too. Since flexibility implies third-power associativity and is implied by alternativity, and since power-associativity implies third-power associativity (*Non-Associative Algebras and the Property Ladder* §*The Ladder of Identities*), the failure of the weakest rung denies the stronger ones: the product satisfies none. $\square$

**Corollary.** The product is not alternative, and the alternative product of two factors with a third is not controlled by the associator; the identities available in an alternative algebra, and with them a calculus of powers of a single element, are not available here. The product is also not flexible, so the elementary manipulation $(\tilde P\star\tilde Q)\star\tilde P = \tilde P\star(\tilde Q\star\tilde P)$ cannot be used, and the left and the right multiplication operators of the next-but-one article do not commute with one another.

**Remark.** Both witnesses are read off the coordinates alone. In the flexibility witness the scalar parts of the two sides are $-1$ and $+1$; in the third-power witness they are $0$ and $0$, and it is the coefficient of $e_3$ that changes sign. The mechanism is the same in both cases: the square $\tilde Q\star\tilde Q = N(\tilde Q)e_0$ is central, so the lefthand reading of a square multiplies it by the scalar part of the element, whereas the righthand reading passes the element through ${}^{\natural}$ and negates its vector part; the two readings differ as soon as the element is not central.

## The Ternary Product

The general theory of a bilinear product attaches to it, through its symmetrisation, a **ternary** operation (*The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System* §*The Ternary Product*). The **symmetrised product** of the quaternionic multiplication is

$$
\tilde P\circ\tilde Q = \tfrac12\bigl(\tilde P\star\tilde Q + \tilde Q\star\tilde P\bigr) ,
$$

the commutative companion of $\star$; its full reading is the next article, and only its definition and its value are used here.

**Lemma.** The symmetrised product is central-valued:

$$
\tilde P\circ\tilde Q = \beta(\tilde P,\tilde Q)\,e_0 , \qquad \beta(\tilde P,\tilde Q) = P_0Q_0 + (\mathbf P,\mathbf Q) .
$$

**Proof.** The two summands are $\tilde P^{\natural}\tilde Q$ and $\tilde Q^{\natural}\tilde P$, whose vector parts are $P_0\mathbf Q - Q_0\mathbf P - \mathbf P\times\mathbf Q$ and $Q_0\mathbf P - P_0\mathbf Q - \mathbf Q\times\mathbf P$; the cross products cancel against one another by antisymmetry, leaving zero, and the two copies of $P_0\mathbf Q - Q_0\mathbf P$ cancel by the half-sum. The scalar parts are equal and add to $2\beta(\tilde P,\tilde Q)$. $\square$

**Definition.** The **ternary product** of the quaternionic multiplication is the ternary operation generated by the symmetrisation,

$$
\{\tilde P,\tilde Q,\tilde R\} = (\tilde P\circ\tilde Q)\circ\tilde R + (\tilde R\circ\tilde Q)\circ\tilde P - (\tilde P\circ\tilde R)\circ\tilde Q .
$$

**Theorem (the ternary product).** For all $\tilde P,\tilde Q,\tilde R \in \mathbb{B}$,

$$
\{\tilde P,\tilde Q,\tilde R\} = \Bigl(\beta(\tilde P,\tilde Q)\,R_0 + \beta(\tilde R,\tilde Q)\,P_0 - \beta(\tilde P,\tilde R)\,Q_0\Bigr)e_0 .
$$

In particular the ternary product is central-valued, and it depends only on the scalar coordinates $P_0,Q_0,R_0$ and on the pairings $\beta$ among the three arguments.

**Proof.** By the lemma each inner symmetrisation is a central multiple of $e_0$. For a central element $\lambda e_0$ one has $(\lambda e_0)\circ\tilde X = \lambda\,(e_0\circ\tilde X) = \lambda X_0e_0$, because $e_0\circ\tilde X = \tfrac12(e_0\star\tilde X + \tilde X\star e_0) = \tfrac12(\tilde X + \tilde X^{\natural}) = X_0e_0$. Applying this to the three terms gives $\beta(\tilde P,\tilde Q)R_0e_0$, $\beta(\tilde R,\tilde Q)P_0e_0$ and $-\beta(\tilde P,\tilde R)Q_0e_0$, whose sum is displayed. $\square$

**Example.** At $\tilde P = \tilde Q = \tilde R = e_0$ every pairing is $1$ and every scalar coordinate is $1$, so the value is $(1+1-1)e_0 = e_0$; at $\tilde P = \tilde Q = \tilde R = e_3$ the pairings are still $1$ but the scalar coordinates vanish, so the value is $0$. The ternary product does not vanish on every triple of nonzero elements; its value is the displayed scalar combination, and it vanishes exactly when $\beta(\tilde P,\tilde Q)R_0 + \beta(\tilde R,\tilde Q)P_0 = \beta(\tilde P,\tilde R)Q_0$.

## The Parities and the Triple Identity

**Proposition (the parities).** The ternary product is $\mathbb{C}$-linear in each of its three variables: $\{\lambda\tilde P,\tilde Q,\tilde R\} = \lambda\{\tilde P,\tilde Q,\tilde R\} = \{\tilde P,\lambda\tilde Q,\tilde R\} = \{\tilde P,\tilde Q,\lambda\tilde R\}$ for $\lambda \in \mathbb{C}$. Its parities are (linear, linear, linear), and $\{\cdot,\cdot,\cdot\}$ is a $\mathbb{C}$-trilinear map $\mathbb{B}\times\mathbb{B}\times\mathbb{B} \to \mathbb{B}$.

**Proof.** The symmetrisation $\circ$ is $\mathbb{C}$-bilinear because $\star$ is and ${}^{\natural}$ is $\mathbb{C}$-linear, and the ternary product is built from $\circ$ by composition and addition, hence is $\mathbb{C}$-trilinear. This is the bilinear case of the parity bookkeeping of *Algebraic J\*-Algebras*, where the middle slot of a sesquilinear ternary product carries the conjugation; here no slot does. $\square$

**Proposition (outer symmetry).** $\{\tilde P,\tilde Q,\tilde R\} = \{\tilde R,\tilde Q,\tilde P\}$.

**Proof.** Immediate from the formula: the roles of $P_0$ and $R_0$ are exchanged, and $\beta$ is symmetric. $\square$

The general theory attaches to a bilinear product whose symmetrisation is a Jordan product a ternary operation that satisfies the five-linear **Jordan triple identity** (*The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System* §*The Triple Identities*). Here the symmetrisation is not a Jordan product — the next article exhibits its failure of the Jordan identity — and the triple identity goes with it.

**Theorem (the triple identity fails).** The Jordan triple identity

$$
\{x,y,\{u,v,w\}\} = \{\{x,y,u\},v,w\} - \{u,\{y,x,v\},w\} + \{u,v,\{x,y,w\}\}
$$

fails for the ternary product of the quaternionic multiplication. At $(x,y,u,v,w) = (e_0,e_0,e_1,e_0,e_1)$ the left-hand side is $-e_0$ and the right-hand side is $e_0$.

**Proof.** The value $\{u,v,w\} = \{e_1,e_0,e_1\}$ is $-e_0$, since $\beta(e_1,e_1) = 1$ and the other pairings vanish; then $\{x,y,\{u,v,w\}\} = \{e_0,e_0,-e_0\}$ has the coefficient $\beta(e_0,e_0)(-1) = -1$, so the left side is $-e_0$. On the right, $\{x,y,u\} = \{e_0,e_0,e_1\} = 0$, so the first and the second group vanish, while $\{y,x,v\} = \{e_0,e_0,e_0\} = e_0$ and $\{u,v,\{x,y,w\}\} = \{e_1,e_0,\{e_0,e_0,e_1\}\} = \{e_1,e_0,0\} = 0$; hence the right side is $\{u,\{y,x,v\},w\} = \{e_1,e_0,e_1\} = -e_0$, taken with the minus sign of the middle term. The two sides are $-e_0$ and $+e_0$. $\square$

**Remark.** The two failures are not independent. The ternary product is the linearisation of the quadratic representation $U_{\tilde P}\tilde Q = \tilde P\circ(\tilde Q\circ\tilde P)$ of the symmetrisation, and the Jordan triple identity for the ternary product is the linearised form of the Jordan identity for the symmetrisation; since the symmetrisation is not a Jordan algebra, neither identity can hold. The detailed failure of the Jordan identity, at $\tilde P = \tilde Q = e_3$, is the next article; the witness above is the same failure read one level up, on five variables instead of three.

## Summary

The quaternionic product is not associative, and its associator has the closed form $(\tilde Q^{\natural}\tilde P - \tilde P^{\natural}\tilde Q^{\natural})\tilde R$, nonzero at $(e_1,e_0,e_0)$ and at $24$ of the $64$ basis triples. The product satisfies no rung of the ladder of weaker identities: it fails flexibility at $(e_3,e_0)$ and it fails the weakest rung, third-power associativity, at $e_3$, so it is not alternative, not flexible and not power-associative. The general theory of a bilinear product attaches a ternary operation to its symmetrisation; here the symmetrisation is the central-valued $\tilde P\circ\tilde Q = \beta(\tilde P,\tilde Q)e_0$, and the ternary product is central-valued, $\mathbb{C}$-linear in its three variables, symmetric in its outer two, and fails the five-linear Jordan triple identity at $(e_0,e_0,e_1,e_0,e_1)$. The associative multiplication is the contrast throughout: its associator vanishes identically, it satisfies every rung of the ladder, and its ternary product is a Jordan triple system.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the identity, $e_k^2 = -e_0$ |
| $\tilde P = \sum_\mu P_\mu e_\mu$ | an element and its four complex coordinates |
| $\mathbf P = \sum_{k=1}^{3}P_ke_k$ | the vector part |
| $(\mathbf P,\mathbf Q)$ | the complex bilinear dot product $\sum_k P_kQ_k$ |
| $\mathbf P\times\mathbf Q$ | the complex bilinear cross product |
| ${}^{\natural}$ | the natural conjugation $\tilde P^{\natural} = P_0 - \mathbf P$ |
| $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product, the multiplication of this group |
| $[\tilde P,\tilde Q,\tilde R] = (\tilde P\star\tilde Q)\star\tilde R - \tilde P\star(\tilde Q\star\tilde R)$ | the associator of the product |
| $\tilde P\circ\tilde Q = \tfrac12(\tilde P\star\tilde Q+\tilde Q\star\tilde P)$ | the symmetrised product |
| $\beta(\tilde P,\tilde Q) = P_0Q_0+(\mathbf P,\mathbf Q)$ | its central coefficient |
| $\{\tilde P,\tilde Q,\tilde R\}$ | the ternary product of the symmetrisation |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the associator, the flexible law and power-associativity.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the ternary product as the linearisation of the quadratic representation and for the Jordan triple identity.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the associator of a multiplication on a module and its trilinearity.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the associator of a product with an anti-automorphism inserted in a slot.
