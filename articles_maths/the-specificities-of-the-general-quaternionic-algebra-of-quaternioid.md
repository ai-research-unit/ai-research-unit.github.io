# __The Specificities of the General Quaternionic Algebra__

## Introduction

The general quaternionic algebra of quaternions is the real space $\mathbb{H}$ under the product $\tilde q_1 \star \tilde q_2 = \tilde q_1^{\natural}\tilde q_2$ (*Introduction to the General Quaternionic Algebra*). This article collects the properties that single it out among the three companion structures of the space, and it is the closing article of the Common Theory of the block: the norm, the roots of the central values and the roots of a general element are settled in the three articles before it, and what is left is the list of the structural landmarks.

Four of the landmarks are negative and decide the block: the unit is one-sided, the product is not associative, there are no zero divisors, and there are no nilpotents. Two are the counterparts of the plain algebra: the idempotents are $0$ and $e_t$ and no others, and the two one-sided actions do not combine into a two-sided module structure. Two concern the conjugation, which fixes the scalar line, negates the vector subspace, is an anti-automorphism of the plain product and is **not** one of the quaternionic product. The last section records the position of the algebra among the three companion structures.

## The One-Sided Unit

**Theorem.** The element $e_t$ is a left unit of the product and no right unit exists; the algebra is left-unital and not unital, and the two-sided inverse of a unital algebra is absent.

*Proof.* $\tilde q \star e_t = \tilde q^{\natural}$, which differs from $\tilde q$ for a non-real $\tilde q$; the direct proof of the non-existence of a right unit is in *Introduction to the General Quaternionic Algebra*. The consequences for inversion are *Norm and Invertibility in the General Quaternionic Algebra*: the two one-sided equations have the coincident solution $\zeta(\tilde q) = \tilde q/\langle\tilde q\rangle_{\natural}$, and the units do not form a group.

The symmetric plain algebra is the only one of the three companion structures with a two-sided unit; the antisymmetric plain structure has none, so unitality is rare in the list and *one-sided* unitality is this product's alone.

## The Associator and its Defect

**Theorem.** The product is not associative, and the associator has the closed form

$$
[\tilde q_1,\tilde q_2,\tilde q_3] = \bigl(\tilde q_2^{\natural}\tilde q_1 - \tilde q_1^{\natural}\tilde q_2^{\natural}\bigr)\tilde q_3 ,
$$

nonzero at $[\vec e_x,e_t,e_t] = 2\vec e_x$ and at $24$ of the $64$ basis triples. The product fails every rung of the ladder of weaker identities: it is not alternative, the left alternative law failing already at $(\tilde q_1,\tilde q_2) = (\vec e_x,\vec e_y)$ where $(\tilde q_1 \star \tilde q_1) \star \tilde q_2 = \vec e_y$ against $\tilde q_1 \star (\tilde q_1 \star \tilde q_2) = -\vec e_y$; it is not flexible, and it is not power-associative.

*Proof.* The closed form and the count are computed in *The Associator and the Ternary Product of the Quaternionic Product*, below this article in this category, and the failure of the ladder is there as well; the two facts are repeated here only as landmarks of the block.

**Remark.** The defect is not an accident of the choice of the distinguished element: it comes from the conjugation standing in the first slot, and the same closed form shows why the ladder fails with it. The comparison with the plain product, whose associator vanishes identically and whose ladder is satisfied at every rung, is *Comparison Between the Two General Products*.

## The Absence of Zero Divisors and of Nilpotents

**Theorem.** The product has no zero divisors: $\tilde q_1 \star \tilde q_2 = 0$ forces $\tilde q_1 = 0$ or $\tilde q_2 = 0$. It has no nonzero nilpotent: $\tilde q \star \tilde q = 0$ forces $\tilde q = 0$.

*Proof.* Both follow from the norm, which is multiplicative and definite: $\langle\tilde q_1 \star \tilde q_2\rangle_{\natural} = \langle\tilde q_1\rangle_{\natural}\langle\tilde q_2\rangle_{\natural}$ and $\langle\tilde q \star \tilde q\rangle_{\natural} = \langle\tilde q\rangle_{\natural}^2$ (*Norm and Invertibility in the General Quaternionic Algebra*), so a vanishing product or a vanishing square forces a vanishing norm and hence a vanishing element.

**Remark.** The two facts are the specification of the block against the four companion operations. The symmetrised product has zero divisors, two orthogonal pure elements being one, $\vec e_x \bullet \vec e_y = 0$; the two antisymmetric products are alternating, so every element has square zero there. The plain product and the quaternionic product are the two without zero divisors, and they are exactly the two **division** structures of the list. The zero divisors of the symmetric plain and symmetric quaternionic algebras are *Zero Divisors in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and the corresponding article of the symmetric quaternionic block, both below this article in this category.

## The Idempotents

**Theorem.** The idempotents of the product, the elements $\tilde\pi$ with $\tilde\pi \star \tilde\pi = \tilde\pi$, are exactly $0$ and $e_t$.

*Proof.* The square is $\tilde\pi \star \tilde\pi = \langle\tilde\pi\rangle_{\natural}e_t$, a real scalar; equality with $\tilde\pi$ forces $\tilde\pi = p_te_t$ with $p_t^2 = p_t$, hence $p_t = 0$ or $p_t = 1$.

**Corollary.** The two idempotents are central, they are the idempotents of the plain product as well, and there is no minimal idempotent and no nontrivial projective decomposition in this block: the product is a division structure and its only idempotents are the two degenerate ones.

*Proof.* The idempotents are central because the scalars are; they are idempotent for the plain product too by the same computation with $\tilde\pi^2$ in place of $\tilde\pi \star \tilde\pi$; a minimal idempotent would be a nonzero idempotent outside the centre, and there is none (*Idempotents of the General Plain Algebra*).

## The Two One-Sided Actions

**Theorem (the left action).** The left multiplications $L_{\tilde p}(\tilde q_4) = \tilde p \star \tilde q_4 = \tilde p^{\natural}\tilde q_4$ satisfy $L_{\tilde p}L_{\tilde q} = L_{\tilde q\tilde p}$, so the family $\{L_{\tilde p}\}$ is closed under composition and is a monoid isomorphic to the opposite algebra $\mathbb{H}^{\mathrm{opp}}$; the assignment $\tilde p \mapsto L_{\tilde p}$ is injective.

**Theorem (the right side).** The honest right multiplications $\tilde q_4 \mapsto \tilde q_4 \star \tilde p$ do **not** close under composition. The twisted right multiplications $\varrho_{\tilde p}(\tilde q_4) = \tilde q_4\tilde p^{\natural}$ do close, with the direct law $\varrho_{\tilde p}\varrho_{\tilde q} = \varrho_{\tilde p\tilde q}$, so that $\{\varrho_{\tilde p}\} \cong \mathbb{H}$ on the right; the two families do not commute in general.

*Proof.* All three statements are computed in *The Left Multiplications of the Quaternionic Product and the Opposite Monoid*, below this article in this category, and again by the operator articles of the block (*One-Sided Operators on the General Quaternionic Algebra*, below this article in this category). The reason for the asymmetry is the same as the reason for the missing right unit: the conjugation sits in the first slot, so a product read from the right conjugates the wrong factor.

**Corollary.** The algebra carries a left action on itself and a twisted right action, and it carries no two-sided module structure over itself; the failure is the operator form of the missing right unit, and it is the sense in which the product is left-handed.

## The Involution

**Theorem (the two eigenspaces).** The conjugation is an involution of the algebra, $\tilde q^{\natural\natural} = \tilde q$; it fixes the scalar line and negates the vector subspace, which are its two eigenspaces, of dimensions one and three.

*Proof.* The coordinate expression $q_t - \vec q$ gives both statements at once.

**Theorem (what the conjugation reverses, and what it does not).** The conjugation is an anti-automorphism of the **plain** product, $(\tilde q_1\tilde q_2)^{\natural} = \tilde q_2^{\natural}\tilde q_1^{\natural}$, and it is **not** an anti-automorphism of the quaternionic product: $(\tilde q_1 \star \tilde q_2)^{\natural} = \tilde q_2^{\natural}\tilde q_1$ and $\tilde q_2^{\natural} \star \tilde q_1^{\natural} = \tilde q_2\tilde q_1^{\natural}$, and the two differ for a non-central factor. What holds instead is the exchange law

$$
(\tilde q_1 \star \tilde q_2)^{\natural} = \tilde q_2 \star \tilde q_1 ,
$$

so the conjugation carries the product to the mirror product and back, and the two products of the block are exchanged by it.

*Proof.* $(\tilde q_1^{\natural}\tilde q_2)^{\natural} = \tilde q_2^{\natural}\tilde q_1^{\natural\natural} = \tilde q_2^{\natural}\tilde q_1 = \tilde q_2 \star \tilde q_1$, while $\tilde q_2^{\natural} \star \tilde q_1^{\natural} = \tilde q_2^{\natural\natural}\tilde q_1^{\natural} = \tilde q_2\tilde q_1^{\natural}$; the two agree only when $\tilde q_2^{\natural}\tilde q_1 = \tilde q_2\tilde q_1^{\natural}$, that is only for central factors.

**Remark.** The distinction is worth the separate theorem because the anti-automorphism property is what the plain algebra uses everywhere and what the quaternionic product denies. It is the second appearance of the same phenomenon: the conjugation in the first slot reverses what it touches, and the exchange law is the exact record of how.

## The Relation to the Other Five

**Theorem (the position).** Among the three companion structures of the quaternion real space, the general quaternionic algebra is the only one that is left-unital and not right-unital; it is not associative, it has no zero divisors and it has two idempotents.

*Proof.* The unit statement is the first section; the non-associativity the second; the absence of zero divisors the third; the idempotents the fourth. The companions are excluded by the shared list of facts: the symmetric plain product has zero divisors, the antisymmetric plain product is alternating with every element square-zero, and the algebra product is associative with a two-sided unit.

| structure | product | character |
|---|---|---|
| symmetric plain (SPA) | $\tfrac12(\tilde q_1\tilde q_2+\tilde q_2\tilde q_1)$ | commutative, Jordan, no unit, zero divisors |
| antisymmetric plain (APA) | $\tfrac12(\tilde q_1\tilde q_2-\tilde q_2\tilde q_1)$ | alternating, Lie, no unit |
| general quaternionic (GQA) | $\tilde q_1^{\natural}\tilde q_2$ | not associative, left unit only, division |

**Remark.** The table is the chapter's, and the articles that own it are *The 6 Products of the Quaternioid Real Space* and *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; it is reproduced here for the relation only.

## Summary

The general quaternionic algebra is left-unital and not unital; its product is not associative and fails every weaker rung; it has no zero divisors and no nonzero nilpotents; its only idempotents are $0$ and $e_t$; its left multiplications form a monoid isomorphic to the opposite algebra, its honest right multiplications do not close, and its twisted right multiplications close with the direct law, so the algebra is left-handed; its conjugation fixes the scalar line, negates the vector subspace, is an anti-automorphism of the plain product and not of its own, and satisfies instead the exchange law $(\tilde q_1 \star \tilde q_2)^{\natural} = \tilde q_2 \star \tilde q_1$. Among the three companion structures of the space it is the one left-unital, non-associative, zero-divisor-free member.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde q_1 \star \tilde q_2 = \tilde q_1^{\natural}\tilde q_2$ | the general quaternionic bilinear product |
| $e_t$ | the left unit, and not a right one |
| $[\tilde q_1,\tilde q_2,\tilde q_3]$ | the associator |
| $L_{\tilde p}(\tilde q_4) = \tilde p^{\natural}\tilde q_4$ | the left multiplication, law $L_{\tilde p}L_{\tilde q} = L_{\tilde q\tilde p}$ |
| $\varrho_{\tilde p}(\tilde q_4) = \tilde q_4\tilde p^{\natural}$ | the twisted right multiplication, law $\varrho_{\tilde p}\varrho_{\tilde q} = \varrho_{\tilde p\tilde q}$ |
| $\tilde\pi$ | an idempotent, here $0$ or $e_t$ |
| $\natural$ | the conjugation, fixing the scalar line and negating the vector subspace |

## Further Reading

- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the unit, the associator and the ladder of a nonassociative algebra.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for a product with a scalar-valued symmetrisation and the division phenomenon.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for an anti-automorphism of a product and the effect of placing it in a slot.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the division property of the quaternion algebra.
