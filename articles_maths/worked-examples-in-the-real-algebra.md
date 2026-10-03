
# __Worked Examples in the Real Algebra__

## Introduction

This article is the computed companion to the algebraic articles of the real algebra. Where *Real Algebra* states the definitions and proves the general properties, the present article exhibits them on explicit elements, so that the general statements can be read against a concrete computation: the field operations, the sole involution and its fixed-point subspace, the associated direct-sum decompositions, and the order with its Archimedean and completeness consequences. It is the first rung of the ladder that the worked-example articles of the complex, quaternion and biquaternion algebras continue.

The elements used throughout are

$$
c = -\tfrac{3}{4}, \qquad d = \tfrac{7}{2},
$$

chosen because their arithmetic is exact, because their squares are the small squares $c^2 = \tfrac{9}{16}$ and $d^2 = \tfrac{49}{4}$, and because they have opposite signs, so that the order of $\mathbb{R}$ is visible on the worked pair. Where a statement needs a degenerate example, the elements $0$, $1$ and $-1$ are used. The conventions are those of *Real Algebra*: the basis is $e_0 = 1$, the sole involution is the identity $\operatorname{id}$, and $\lvert a\rvert$ is the absolute value defined by the order.

Every numerical value below is exact and rational; no decimal is used.

Everything computed below is algebraic. The metrical reading of the algebra — the norm and the modulus of *Real Norm and Invertibility*, the sign decomposition of *Real Polar Element Representation*, and the Cayley matrix of *Real Regular Element Representation* — belongs to the later slots of the system and is not used here.

## The Algebra on Concrete Elements

**Sum, difference and product.** With $c = -\tfrac{3}{4}$ and $d = \tfrac{7}{2}$,

$$
c + d = -\tfrac{3}{4} + \tfrac{14}{4} = \tfrac{11}{4}, \qquad d - c = \tfrac{14}{4} + \tfrac{3}{4} = \tfrac{17}{4},
$$

and, applying the field multiplication,

$$
c d = -\tfrac{3}{4}\cdot\tfrac{7}{2} = -\tfrac{21}{8}, \qquad d c = \tfrac{7}{2}\cdot\bigl(-\tfrac{3}{4}\bigr) = -\tfrac{21}{8},
$$

the two orders agreeing, the concrete form of commutativity.

**Powers and the absence of zero divisors.** The squares are

$$
c^2 = \bigl(-\tfrac{3}{4}\bigr)^2 = \tfrac{9}{16}, \qquad d^2 = \bigl(\tfrac{7}{2}\bigr)^2 = \tfrac{49}{4},
$$

and $c^2 = (-c)^2$ although $c \neq -c$: the square forgets the sign while the element does not. The product of the two nonzero worked elements is again nonzero, $cd = -\tfrac{21}{8} \neq 0$, the concrete form of the absence of zero divisors in a field.

**Associativity and distributivity** are illustrated by the two products above agreeing and by $(c+d)^2 = c^2 + 2cd + d^2$, a computation of the same rules which needs no separate display.

## The Involution on Concrete Elements

The real algebra carries one involution, the identity.

**The identity.** $\operatorname{id}(c) = c = -\tfrac{3}{4}$ and $\operatorname{id}(d) = d = \tfrac{7}{2}$. The identity fixes every element, and it is the only involution of $\mathbb{R}$: an $\mathbb{R}$-algebra involution is a field automorphism of $\mathbb{R}$, and there is no nontrivial one, so there is no analogue here of the conjugation of $\mathbb{C}$ or of the quaternion conjugation of $\mathbb{H}$ and $\mathbb{B}$. The absence is the mathematical content of the unitary case.

It is an involution, $\operatorname{id}(\operatorname{id}(a)) = a$ for every $a$, and the relation is immediate because $\operatorname{id}$ is the identity map.

| element | $\operatorname{id}$ | $\operatorname{id}$ applied twice |
|---|---|---|
| $c = -\tfrac{3}{4}$ | $-\tfrac{3}{4}$ | $-\tfrac{3}{4}$ |
| $d = \tfrac{7}{2}$ | $\tfrac{7}{2}$ | $\tfrac{7}{2}$ |
| $cd = -\tfrac{21}{8}$ | $-\tfrac{21}{8}$ | $-\tfrac{21}{8}$ |

## The Fixed-Point Subspace on Concrete Elements

The fixed-point subspace of the identity involution is the whole algebra, and there is no anti-fixed subspace, because the only candidate involution is trivial.

**The fixed subspace.** An element is fixed exactly when it equals itself, which is always true. For the worked pair,

$$
\operatorname{id}(c) = c, \qquad \operatorname{id}(d) = d,
$$

so both $c$ and $d$ lie in the fixed subspace $\mathbb{R}_{\mathbb{R}}$; indeed every real number does. The fixed subspace is the whole algebra, $\mathbb{R}_{\mathbb{R}} = \mathbb{R}$, a real vector space of dimension $1$.

**The anti-fixed subspace is empty.** An element is anti-fixed exactly when $\operatorname{id}(a) = -a$, i.e. $a = -a$, i.e. $2a = 0$, i.e. $a = 0$. The anti-fixed subspace is therefore the zero subspace $\{0\}$, and it is not a subspace of positive dimension:

$$
\{a \in \mathbb{R} : \operatorname{id}(a) = -a\} = \{0\}.
$$

This is the concrete form of the absence of the imaginary direction: $\mathbb{C}$ has the imaginary axis $i\mathbb{R}_{\mathbb{C}}$ as its anti-fixed subspace, and $\mathbb{R}$ has only $0$.

## The Decompositions, Worked

**The eigencomponents of the identity.** Because the involution is trivial, the two eigenprojections coincide on the fixed subspace and the anti-fixed component vanishes:

$$
c_+ = \tfrac{1}{2}\bigl(c + \operatorname{id}(c)\bigr) = \tfrac{1}{2}(c+c) = c = -\tfrac{3}{4} \in \mathbb{R}_{\mathbb{R}},
$$

$$
c_- = \tfrac{1}{2}\bigl(c - \operatorname{id}(c)\bigr) = \tfrac{1}{2}(c-c) = 0 .
$$

The result is the trivial decomposition $\mathbb{R} = \mathbb{R}_{\mathbb{R}} \oplus \{0\}$ in which the second summand has dimension $0$. This is the **real decomposition** of *Real Algebra*, and its triviality is the statement that the general involution decomposition has one summand here.

**The Cartesian decomposition.** The decomposition of an element into a fixed part plus an anti-fixed part, $\tfrac{1}{2}(a+\operatorname{id}a) + \tfrac{1}{2}(a-\operatorname{id}a)$, reduces on the worked elements to

$$
c = -\tfrac{3}{4} + 0, \qquad d = \tfrac{7}{2} + 0,
$$

with both anti-fixed parts zero.

## The Order, the Archimedean Property and Completeness, Worked

**The order on the worked pair.** The two worked elements have opposite signs,

$$
c = -\tfrac{3}{4} < 0 < \tfrac{7}{2} = d,
$$

and the order separates the two elements while the field structure alone does not: $c < 0 < d$, yet the two have positive squares.

**The Archimedean property.** For $a > 0$ and any $b$ there is $n \in \mathbb{N}$ with $na > b$. With $a = \lvert c\rvert = \tfrac{3}{4}$ and $b = \lvert d\rvert = \tfrac{7}{2}$, the inequality $n\cdot\tfrac{3}{4} > \tfrac{7}{2}$ holds exactly when $n > \tfrac{14}{3}$, so the smallest witness is

$$
n = 5, \qquad 5\cdot\tfrac{3}{4} = \tfrac{15}{4} > \tfrac{7}{2}.
$$

No infinitesimal occurs: the multiples of any positive element eventually exceed any bound, which is the Archimedean property checked on the worked numbers.

**Completeness.** Let $S = \{c, 0, d\} = \{-\tfrac{3}{4}, 0, \tfrac{7}{2}\}$. It is non-empty and bounded, and

$$
\sup S = \tfrac{7}{2} = d, \qquad \inf S = -\tfrac{3}{4} = c,
$$

both attained. A bounded set whose supremum is not attained is $T = \{\tfrac{n}{n+1} : n \in \mathbb{N}\}$, for which $\sup T = 1$ and $1 \notin T$; the existence of the supremum is the completeness axiom, and it is the property that distinguishes $\mathbb{R}$ from $\mathbb{Q}$.

**Existence of roots.** The positive elements of the worked pair have the rational square roots

$$
\sqrt{\tfrac{9}{16}} = \tfrac{3}{4} = \lvert c\rvert, \qquad \sqrt{\tfrac{49}{4}} = \tfrac{7}{2} = \lvert d\rvert,
$$

and the non-negative root of the first is the absolute value of $c$ although $c$ is negative; the existence and uniqueness of the non-negative root is a consequence of completeness.

**Density and the irrational.** Between $c$ and $d$ there lies the rational $\tfrac{1}{2}$, and also the irrational $\sqrt{2}$; the set $\{a \in \mathbb{Q} : a^2 < 2\}$ is bounded above in $\mathbb{R}$ with supremum $\sqrt{2} \notin \mathbb{Q}$, which is the completeness of $\mathbb{R}$ used to manufacture an irrational from a rational set.

## The Place in the Ladder

The real algebra is the first rung of the tensor ladder $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{B}$ of the corpus, and every structure computed above is the one-dimensional case of a structure that the higher rungs enrich.

| structure | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{H}$ | $\mathbb{B}$ |
|---|---|---|---|---|
| involution | identity only | complex conjugation | quaternion conjugation | quaternion and complex |
| fixed subspace | the whole algebra | the real line | the real line | Hermitian subspace |
| anti-fixed subspace | $\{0\}$ | the imaginary line | the pure quaternions | anti-Hermitian subspace |
| nonzero elements invertible | yes, a field | yes, a field | yes, a division algebra | no, there are zero divisors |

The real column is the base case that the other worked-example articles continue: *Worked Examples in the Complex Algebra* adds the nontrivial conjugation and the circle, *Worked Examples in the Split-Quaternion Algebra* adds the indefinite form and its two regimes, and *Worked Examples in the Biquaternion Algebra* adds the complex norm and its zero divisors. Each of them reuses the algebraic identities computed here — commutativity, the triviality of the involution decomposition, and the invertibility of every nonzero element — in the case where the involution is no longer trivial and the algebra is no longer a field.

## Summary

On the worked pair $c = -\tfrac{3}{4}$ and $d = \tfrac{7}{2}$ the real algebra is exhibited concretely: the sum $\tfrac{11}{4}$, the difference $\tfrac{17}{4}$, and the product $cd = -\tfrac{21}{8}$ with $dc = cd$, the concrete form of commutativity.

The only involution is the identity, so its fixed-point subspace is the whole algebra and its anti-fixed subspace is $\{0\}$; the involution decomposition is the trivial $\mathbb{R} = \mathbb{R}_{\mathbb{R}} \oplus \{0\}$. Both worked elements are units — their inverses are the field inverses $c^{-1} = -\tfrac{4}{3}$ and $d^{-1} = \tfrac{2}{7}$ — and $0$ is the only non-unit, the concrete form of the field property.

On the order, the worked pair straddles the origin, the Archimedean witness for $\lvert c\rvert$ against $\lvert d\rvert$ is $n = 5$, and the completeness axiom is checked on the bounded sets $\{c,0,d\}$ and $\{\tfrac{n}{n+1}\}$, whose suprema are $\tfrac{7}{2}$ and $1$. The article is the first rung of the ladder continued by the complex, quaternion and biquaternion worked-example articles.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}$ | the real algebra, the complete ordered field, basis $e_0 = 1$ |
| $c = -\tfrac{3}{4}$, $d = \tfrac{7}{2}$ | the worked elements |
| $\operatorname{id}$ | the identity involution, the sole involution |
| $\mathbb{R}_{\mathbb{R}}$ | the fixed subspace of $\operatorname{id}$, the whole algebra |
| $\{0\}$ | the anti-fixed subspace of $\operatorname{id}$ |
| $\lvert a\rvert$ | the absolute value, defined by the order |
| $a^{-1} = 1/a$ | the inverse of a nonzero element |
| $\sup S$, $\inf S$ | the supremum and infimum of a bounded set |

## Further Reading

- Edmund Landau, *Grundlagen der Analysis* (Akademische Verlagsgesellschaft, 1930), for the ordered-field axioms, the Archimedean property and the completeness of $\mathbb{R}$.
- Walter Rudin, *Principles of Mathematical Analysis*, 3rd edition (McGraw-Hill, 1976), for worked computations with suprema, roots and the density of the rationals.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for field computations and the invertibility of the nonzero elements.
- John B. Fraleigh, *A First Course in Abstract Algebra*, 7th edition (Addison–Wesley, 2003), for concrete field computations and the order of a field.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the place of the real algebra in the ladder of the division algebras.
