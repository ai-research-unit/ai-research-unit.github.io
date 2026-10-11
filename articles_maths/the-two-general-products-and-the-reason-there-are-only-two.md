# __The Two General Products and the Reason There Are Only Two__

## Introduction

The quaternion algebra carries two general products, the general plain $\tilde p\tilde q$ and the general quaternionic $\tilde p^{\natural}\tilde q$, where the four-product family of the biquaternion chapter has four. This article states the general construction, isolates the second slot as the only place where a sesquilinear family can be born, and proves that over $\mathbb{R}$ that slot carries nothing new, so that exactly two products survive. It is the synthesis article of the block and the only place the four-to-two collapse is stated.

The two products themselves are *The Two General Products of the Quaternion $\mathbb{R}$ Space*, and the six products their symmetric and antisymmetric parts generate are *The 6 Products of the Quaternion Real Space*; this article re-derives neither. What it owns is the construction, the theorem on the second slot, the comparison table of the two against the four, and the ladder reading. The forms the products carry are *The 2 Forms over the Quaternion $\mathbb{R}$ Space*; the norms are *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*; both are above this article in this category.

## The General Construction

A **general product** on an algebra $A$ over a base ring $R$ is a bilinear or a sesquilinear map obtained by choosing, independently, how each of its two slots reads its argument: through the identity or through the anti-involution of the algebra on the first side, and through the identity or an involution of $R$ on the second. Writing ${}^{\natural}$ for the anti-involution of the algebra and $\varsigma$ for an involution of $R$, the identity allowed, the products are the four **slot pairings**
$$
(\mathrm{id},\mathrm{id}) ,\quad ({}^{\natural},\mathrm{id}) ,\quad (\mathrm{id},\varsigma) ,\quad ({}^{\natural},\varsigma) ,
$$
the first two **bilinear** and the last two **sesquilinear**, since a slot read through $\varsigma$ is conjugate-linear. The construction is the one of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, applied to the pair (algebra, base ring).

## The Second Slot Is What Makes a Sesqualgebra

**Theorem.** The family $(\mathrm{id},\varsigma)$ and $({}^{\natural},\varsigma)$ is non-empty exactly when the base ring $R$ has a nontrivial involution. That slot is the whole difference between an algebra product and a sesquilinear one.

**Proof.** A product whose second slot is read through $\varsigma$ is conjugate-linear in that slot, so its value is not $R$-bilinear unless $\varsigma=\mathrm{id}$; and a product whose second slot is the identity is $R$-bilinear in both slots. The two families are therefore distinguished exactly by whether $\varsigma$ is the identity, and there are four pairings for every nontrivial $\varsigma$ and only two when $\varsigma=\mathrm{id}$.

## Only the Algebra Family Survives over $\mathbb{R}$

The base ring $\mathbb{R}$ has a single involution, the identity, because an order-two automorphism of a totally ordered field is trivial. Hence $\varsigma=\mathrm{id}$ and the second slot carries no conjugation, the two sesquilinear pairings coincide with the two bilinear ones, and the four pairings reduce to two:
$$
\tilde p\tilde q\quad(\text{general plain, the pair }(\mathrm{id},\mathrm{id})) , \qquad \tilde p^{\natural}\tilde q\quad(\text{general quaternionic, the pair }({}^{\natural},\mathrm{id})) .
$$
There is no third product, and in particular no quaternion analogue of the Hermitian or the Krein product of the biquaternion chapter: those need a complex base.

**Table (two against four).** Writing $\varsigma$ for the base-ring involution and ${}^{\natural}$ for the algebra anti-involution,

| pair | over $\mathbb{R}$ ($\varsigma=\mathrm{id}$) | over $\mathbb{C}$ (the second slot carries the conjugate-linear involution) |
|---|---|---|
| $(\mathrm{id},\mathrm{id})$ | $\tilde p\tilde q$ | $\tilde P\tilde Q$ |
| $({}^{\natural},\mathrm{id})$ | $\tilde p^{\natural}\tilde q$ | $\tilde P^{\natural}\tilde Q$ |
| $(\mathrm{id},\varsigma)$ | coincides with $(\mathrm{id},\mathrm{id})$ | $\tilde P\tilde Q^{*}$ |
| $({}^{\natural},\varsigma)$ | coincides with $({}^{\natural},\mathrm{id})$ | $\tilde P^{\natural}\tilde Q^{*}$ |

The second slot is an involution of the base ring; it is the identity over $\mathbb{R}$, so the two lower rows of the left column collapse onto the two upper rows, and it is nontrivial over $\mathbb{C}$, where the biquaternion chapter reads that slot through the star, the conjugate-linear involution of $\mathbb{B}$ restricting to the coefficientwise conjugation on the coefficients, as the right column records.

The left column is the collapse, its four rows standing for the two products $\tilde p\tilde q$ and $\tilde p^{\natural}\tilde q$; the right column is the four of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*.

## The Ladder Reading

The number of general products is read on the ladder
$$
\mathbb{R}\subset\mathbb{C}\subset\mathbb{H}\subset\mathbb{B} ,
$$
the base ring being $\mathbb{R}$ for the first three rungs and $\mathbb{C}$ for the last. On each rung the products are the slot pairings, the algebra's anti-involution contributing the first slot:

| rung | algebra, base | products | count |
|---|---|---|---|
| $\mathbb{R}$ | $\mathbb{R}$ over $\mathbb{R}$ | $\tilde p\tilde q$ | $1$ |
| $\mathbb{C}$ | $\mathbb{C}$ over $\mathbb{R}$ | $zw$, $\bar z w$ | $2$ |
| $\mathbb{H}$ | $\mathbb{H}$ over $\mathbb{R}$ | $\tilde p\tilde q$, $\tilde p^{\natural}\tilde q$ | $2$ |
| $\mathbb{B}$ | $\mathbb{B}$ over $\mathbb{C}$ | the four pairings | $4$ |

The count doubles at the last rung because only there does the base ring carry an involution; $\mathbb{H}$ sits on the real rung beside $\mathbb{C}$ and carries two products like it, and the real $\mathbb{R}$ carries one because its only anti-involution is the identity. This is the whole reason there are two products on $\mathbb{H}$ and four on $\mathbb{B}$.

## Summary

A general product is a slot pairing of an anti-involution of the algebra with an involution of the base ring. The second slot is what separates a sesquilinear product from a bilinear one, and it is empty over $\mathbb{R}$ because the real field has only the trivial involution. The four pairings therefore collapse to two, the general plain $\tilde p\tilde q$ and the general quaternionic $\tilde p^{\natural}\tilde q$, and the comparison with the biquaternion four is the second-slot collapse read column by column. On the ladder $\mathbb{R}\subset\mathbb{C}\subset\mathbb{H}\subset\mathbb{B}$ the counts are $1,2,2,4$, the doubling occurring at the two complexification steps $\mathbb{R}\to\mathbb{C}$ and $\mathbb{H}\to\mathbb{B}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| ${}^{\natural}$ | the quaternion conjugation, the anti-involution of the algebra |
| $\varsigma$ | the involution of the base ring; over $\mathbb{R}$, $\varsigma=\mathrm{id}$ |
| $(\mathrm{id},\mathrm{id})$, $({}^{\natural},\mathrm{id})$, $(\mathrm{id},\varsigma)$, $({}^{\natural},\varsigma)$ | the four slot pairings, the last two sesquilinear |
| $\tilde p\tilde q$, $\tilde p^{\natural}\tilde q$ | the two general products over $\mathbb{R}$ |
| $\mathbb{R}\subset\mathbb{C}\subset\mathbb{H}\subset\mathbb{B}$ | the ladder, with product counts $1,2,2,4$ |

## Further Reading

- *The Two General Products of the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-two-general-products-of-the-quaternion-r-space.md`), for the two products in coordinates.
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the construction on the biquaternion rung.
- *The 6 Products of the Quaternion Real Space* (`articles_maths/the-6-products-of-the-quaternion-real-space.md`), for the six products the two generate.
- *The Complexification and the Effect of the Change of Scalars on the Quaternions* (`articles_maths/the-complexification-and-the-effect-of-the-change-of-scalars-on-the-quaternions.md`), for the passage $\mathbb{H}\to\mathbb{B}$.
