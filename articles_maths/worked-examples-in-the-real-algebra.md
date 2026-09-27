
# __Worked Examples in the Real Algebra__

## Introduction

This article is the computed companion to the structural articles of the real algebra. Where *Real Algebra* states the definitions and proves the general properties, and *Real Norm and Invertibility*, *Real Automorphisms and Derivations* and *Real Exponential and Lie Group Structure* develop them, the present article exhibits every one of those structures on explicit elements, so that the general statements can be read against a concrete computation. It is the first rung of the ladder that the worked-example articles of the complex, quaternion and biquaternion algebras continue.

The elements used throughout are

$$
x = -\tfrac{3}{4}, \qquad y = \tfrac{7}{2},
$$

chosen because their arithmetic is exact and their norm forms are small squares: $N(x) = \tfrac{9}{16}$ and $N(y) = \tfrac{49}{4}$, so that the inverse and the sign decomposition display rational data, and because the two have opposite signs, so that the sign trichotomy is visible on the worked pair. Where a statement needs a degenerate example, the elements $0$, $1$ and $-1$ are used. The conventions are those of *Real Algebra*: the basis is $e_0 = 1$, the sole involution is the identity $\operatorname{id}$, and the norm form is $N(x) = x\,x = x^2$.

Every numerical value below is exact and rational; no decimal is used.

## The Algebra on Concrete Elements

**Sum, difference and product.** With $x = -\tfrac{3}{4}$ and $y = \tfrac{7}{2}$,

$$
x + y = -\tfrac{3}{4} + \tfrac{14}{4} = \tfrac{11}{4}, \qquad y - x = \tfrac{14}{4} + \tfrac{3}{4} = \tfrac{17}{4},
$$

and, applying the field multiplication,

$$
x y = -\tfrac{3}{4}\cdot\tfrac{7}{2} = -\tfrac{21}{8}, \qquad y x = \tfrac{7}{2}\cdot\bigl(-\tfrac{3}{4}\bigr) = -\tfrac{21}{8},
$$

the two orders agreeing, the concrete form of commutativity.

**Powers and the norm under multiplication.** The squares are

$$
x^2 = \bigl(-\tfrac{3}{4}\bigr)^2 = \tfrac{9}{16}, \qquad y^2 = \bigl(\tfrac{7}{2}\bigr)^2 = \tfrac{49}{4},
$$

with

$$
N(xy) = \bigl(-\tfrac{21}{8}\bigr)^2 = \tfrac{441}{64} = \tfrac{9}{16}\cdot\tfrac{49}{4} = N(x)\,N(y),
$$

the multiplicativity of the norm form on a concrete product. In particular $N(xy) \neq 0$, so the product of the two nonzero worked elements is again nonzero, as the field property requires.

**Associativity and distributivity** are illustrated by the two products above agreeing and by $(x+y)^2 = x^2 + 2xy + y^2$, a computation of the same rules which needs no separate display.

## The Involution on Concrete Elements

The real algebra carries one involution, the identity.

**The identity.** $\operatorname{id}(x) = x = -\tfrac{3}{4}$ and $\operatorname{id}(y) = y = \tfrac{7}{2}$. The identity fixes every element, and it is the only involution of $\mathbb{R}$: an $\mathbb{R}$-algebra involution is a field automorphism of $\mathbb{R}$, and there is no nontrivial one, so there is no analogue here of the conjugation of $\mathbb{C}$ or of the quaternion conjugation of $\mathbb{H}$ and $\mathbb{B}$. The absence is the mathematical content of the unitary case.

It is an involution, and the norm form is invariant under it:

$$
\operatorname{id}\bigl(\operatorname{id}(x)\bigr) = x, \qquad N(\operatorname{id} x) = N(x),
$$

the invariance being trivial since $\operatorname{id}$ is the identity map.

| element | $\operatorname{id}$ | $\operatorname{id}$ applied twice |
|---|---|---|
| $x = -\tfrac{3}{4}$ | $-\tfrac{3}{4}$ | $-\tfrac{3}{4}$ |
| $y = \tfrac{7}{2}$ | $\tfrac{7}{2}$ | $\tfrac{7}{2}$ |
| $xy = -\tfrac{21}{8}$ | $-\tfrac{21}{8}$ | $-\tfrac{21}{8}$ |

## The Fixed-Point Subspace on Concrete Elements

The fixed-point subspace of the identity involution is the whole algebra, and there is no anti-fixed subspace, because the only candidate involution is trivial.

**The fixed subspace.** An element is fixed exactly when it equals itself, which is always true. For the worked pair,

$$
\operatorname{id}(x) = x, \qquad \operatorname{id}(y) = y,
$$

so both $x$ and $y$ lie in the fixed subspace $\mathbb{R}_{\mathbb{R}}$; indeed every real number does. The fixed subspace is the whole algebra, $\mathbb{R}_{\mathbb{R}} = \mathbb{R}$, a real vector space of dimension $1$.

**The anti-fixed subspace is empty.** An element is anti-fixed exactly when $\operatorname{id}(a) = -a$, i.e. $a = -a$, i.e. $2a = 0$, i.e. $a = 0$. The anti-fixed subspace is therefore the zero subspace $\{0\}$, and it is not a subspace of positive dimension:

$$
\{a \in \mathbb{R} : \operatorname{id}(a) = -a\} = \{0\}.
$$

This is the concrete form of the absence of the imaginary direction: $\mathbb{C}$ has the imaginary axis $i\mathbb{R}_{\mathbb{C}}$ as its anti-fixed subspace, and $\mathbb{R}$ has only $0$.

## The Decompositions, Worked

**The eigencomponents of the identity.** Because the involution is trivial, the two eigenprojections coincide on the fixed subspace and the anti-fixed component vanishes:

$$
x_+ = \tfrac{1}{2}\bigl(x + \operatorname{id}(x)\bigr) = \tfrac{1}{2}(x+x) = x = -\tfrac{3}{4} \in \mathbb{R}_{\mathbb{R}},
$$

$$
x_- = \tfrac{1}{2}\bigl(x - \operatorname{id}(x)\bigr) = \tfrac{1}{2}(x-x) = 0 .
$$

The result is the trivial decomposition $\mathbb{R} = \mathbb{R}_{\mathbb{R}} \oplus \{0\}$ in which the second summand has dimension $0$. This is the **real decomposition** of *Real Algebra*, and its triviality is the statement that the general involution decomposition has one summand here.

**The Cartesian decomposition.** The decomposition of an element into a fixed part plus an anti-fixed part, $\tfrac{1}{2}(a+\operatorname{id}a) + \tfrac{1}{2}(a-\operatorname{id}a)$, reduces on the worked elements to

$$
x = -\tfrac{3}{4} + 0, \qquad y = \tfrac{7}{2} + 0,
$$

with both anti-fixed parts zero.

## The Norm Criterion for a Unit, Worked

**Criterion.** A real number is a unit exactly when its norm form is nonzero, equivalently when the number is nonzero. The worked elements are checked one by one.

**A negative unit.** $x = -\tfrac{3}{4} \neq 0$, so by the theorem $x$ is a unit; its inverse is

$$
x^{-1} = \frac{1}{N(x)}\,x = \frac{x}{x^2} = \frac{-\tfrac{3}{4}}{\tfrac{9}{16}} = -\tfrac{3}{4}\cdot\tfrac{16}{9} = -\tfrac{4}{3},
$$

and the verification is exact:

$$
x\,x^{-1} = \bigl(-\tfrac{3}{4}\bigr)\bigl(-\tfrac{4}{3}\bigr) = \tfrac{12}{12} = 1 .
$$

**A positive unit.** $y = \tfrac{7}{2} \neq 0$, so $y$ is a unit, with

$$
y^{-1} = \frac{y}{y^2} = \frac{\tfrac{7}{2}}{\tfrac{49}{4}} = \tfrac{7}{2}\cdot\tfrac{4}{49} = \tfrac{2}{7}, \qquad y\,y^{-1} = \tfrac{7}{2}\cdot\tfrac{2}{7} = 1 .
$$

**A non-unit.** $0$ has $N(0) = 0$ and is not invertible: if $0\cdot w = 1$ then $0 = 1$, a contradiction. The zero-divisor class is empty, so $0$ is the only non-unit.

**The unit group on the worked pair.** Both $x$ and $y$ lie in $\mathbb{R}^\times$; the worked non-unit is only $0$. The distribution over the single subspace is the table of *Real Norm and Invertibility*, and on the worked elements it reads

| element | $N$ | unit? | inverse |
|---|---|---|---|
| $x = -\tfrac{3}{4}$ | $\tfrac{9}{16}$ | yes | $-\tfrac{4}{3}$ |
| $y = \tfrac{7}{2}$ | $\tfrac{49}{4}$ | yes | $\tfrac{2}{7}$ |
| $0$ | $0$ | no | — |

## The Sign Decomposition, Worked

Every nonzero real number is the product of its modulus and its sign, $a = |a|\operatorname{sgn}a$, with $|a| > 0$ and $\operatorname{sgn}a = a/|a| \in \{\pm1\}$.

**On the worked pair.**

$$
x = -\tfrac{3}{4} = \tfrac{3}{4}\cdot(-1), \qquad |x| = \tfrac{3}{4}, \qquad \operatorname{sgn}x = -1,
$$

$$
y = \tfrac{7}{2} = \tfrac{7}{2}\cdot(+1), \qquad |y| = \tfrac{7}{2}, \qquad \operatorname{sgn}y = +1 .
$$

**On the product.** The two factors multiply componentwise, the modulus multiplicatively and the sign additively in the exponent:

$$
xy = -\tfrac{21}{8}, \qquad |xy| = \tfrac{21}{8} = \tfrac{3}{4}\cdot\tfrac{7}{2} = |x|\,|y|,
$$

$$
\operatorname{sgn}(xy) = -1 = (-1)\cdot(+1) = \operatorname{sgn}x\,\operatorname{sgn}y .
$$

**On the degenerate elements.** The elements $1$ and $-1$ are their own signs, $1 = 1\cdot(+1)$ and $-1 = 1\cdot(-1)$, and the origin has no sign: $0$ is the sole element excluded from the decomposition.

## The Order, the Archimedean Property and Completeness, Worked

**The order on the worked pair.** The two worked elements have opposite signs,

$$
x = -\tfrac{3}{4} < 0 < \tfrac{7}{2} = y,
$$

and the norm form is insensitive to the sign while the order is not: $N(x) = N(-x)$ although $x \neq -x$ unless $x = 0$.

**The Archimedean property.** For $a > 0$ and any $b$ there is $n \in \mathbb{N}$ with $na > b$. With $a = |x| = \tfrac{3}{4}$ and $b = |y| = \tfrac{7}{2}$, the inequality $n\cdot\tfrac{3}{4} > \tfrac{7}{2}$ holds exactly when $n > \tfrac{14}{3}$, so the smallest witness is

$$
n = 5, \qquad 5\cdot\tfrac{3}{4} = \tfrac{15}{4} > \tfrac{7}{2}.
$$

No infinitesimal occurs: the multiples of any positive element eventually exceed any bound, which is the Archimedean property checked on the worked numbers.

**Completeness.** Let $S = \{x, 0, y\} = \{-\tfrac{3}{4}, 0, \tfrac{7}{2}\}$. It is non-empty and bounded, and

$$
\sup S = \tfrac{7}{2} = y, \qquad \inf S = -\tfrac{3}{4} = x,
$$

both attained. A bounded set whose supremum is not attained is $T = \{\tfrac{n}{n+1} : n \in \mathbb{N}\}$, for which $\sup T = 1$ and $1 \notin T$; the existence of the supremum is the completeness axiom, and it is the property that distinguishes $\mathbb{R}$ from $\mathbb{Q}$.

**Existence of roots.** The positive elements of the worked pair have the rational square roots

$$
\sqrt{\tfrac{9}{16}} = \tfrac{3}{4} = |x|, \qquad \sqrt{\tfrac{49}{4}} = \tfrac{7}{2} = |y|,
$$

and the root of the first is the modulus of $x$ although $x$ is negative; the existence and uniqueness of the non-negative root is a consequence of completeness.

**Density and the irrational.** Between $x$ and $y$ there lies the rational $\tfrac{1}{2}$, and also the irrational $\sqrt{2}$; the set $\{a \in \mathbb{Q} : a^2 < 2\}$ is bounded above in $\mathbb{R}$ with supremum $\sqrt{2} \notin \mathbb{Q}$, which is the completeness of $\mathbb{R}$ used to manufacture an irrational from a rational set.

## The Place in the Ladder

The real algebra is the first rung of the tensor ladder $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{B}$ of the corpus, and every structure computed above is the one-dimensional case of a structure that the higher rungs enrich.

| structure | $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{H}$ | $\mathbb{B}$ |
|---|---|---|---|---|
| involution | identity only | complex conjugation | quaternion conjugation | quaternion and complex |
| fixed subspace | the whole algebra | the real line | the real line | Hermitian subspace |
| anti-fixed subspace | $\{0\}$ | the imaginary line | the pure quaternions | anti-Hermitian subspace |
| norm form | $x^2$, real definite | $a^2+b^2$, real definite | sum of four squares | complex indefinite |
| unit group | $\mathbb{R}_{>0}\times\{\pm1\}$ | $\mathbb{R}_{>0}\times U(1)$ | $\mathbb{R}_{>0}\times S^3$ | $GL_2(\mathbb{C})$ |

The real column is the base case that the other worked-example articles continue: *Worked Examples in the Complex Algebra* adds the nontrivial conjugation and the circle, *Worked Examples in the Split-Quaternion Algebra* adds the indefinite form and its two regimes, and *Worked Examples in the Biquaternion Algebra* adds the complex norm form and its zero divisors. Each of them reuses the identities computed here — the multiplicativity $N(ab) = N(a)N(b)$ and the inverse formula $a^{-1} = a/N(a)$ — in the case where the involution is no longer trivial and the norm form is no longer definite.

## Summary

On the worked pair $x = -\tfrac{3}{4}$ and $y = \tfrac{7}{2}$ the real algebra is exhibited concretely: the sum $\tfrac{11}{4}$, the difference $\tfrac{17}{4}$, the product $xy = -\tfrac{21}{8}$, and the multiplicativity $N(xy) = \tfrac{441}{64} = N(x)N(y)$.

The only involution is the identity, so its fixed-point subspace is the whole algebra and its anti-fixed subspace is $\{0\}$; the involution decomposition is trivial. Both worked elements are units, with inverses $x^{-1} = -\tfrac{4}{3}$ and $y^{-1} = \tfrac{2}{7}$ obtained from the norm criterion, and $0$ is the only non-unit. The sign decomposition gives $x = \tfrac{3}{4}\cdot(-1)$ and $y = \tfrac{7}{2}\cdot(+1)$, and the modulus and sign multiply componentwise on $xy$.

On the order, the worked pair straddles the origin, the Archimedean witness for $|x|$ against $|y|$ is $n = 5$, and the completeness axiom is checked on the bounded sets $\{x,0,y\}$ and $\{\tfrac{n}{n+1}\}$, whose suprema are $\tfrac{7}{2}$ and $1$. The article is the first rung of the ladder continued by the complex, quaternion and biquaternion worked-example articles.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{R}$ | the real algebra, the complete ordered field, basis $e_0 = 1$ |
| $x = -\tfrac{3}{4}$, $y = \tfrac{7}{2}$ | the worked elements |
| $\operatorname{id}$ | the identity involution, the sole involution |
| $\mathbb{R}_{\mathbb{R}}$ | the fixed subspace of $\operatorname{id}$, the whole algebra |
| $\{0\}$ | the anti-fixed subspace of $\operatorname{id}$ |
| $N(a) = a^2$ | the norm form |
| $\lvert a\rvert = \sqrt{N(a)}$ | the modulus |
| $\operatorname{sgn} a = a/\lvert a\rvert$ | the sign, an element of $\{\pm1\}$ |
| $a = \lvert a\rvert\operatorname{sgn} a$ | the sign decomposition |
| $a^{-1} = a/N(a)$ | the inverse of a nonzero element |
| $\sup S$, $\inf S$ | the supremum and infimum of a bounded set |

## Further Reading

- Edmund Landau, *Grundlagen der Analysis* (Akademische Verlagsgesellschaft, 1930), for the ordered-field axioms, the Archimedean property and the completeness of $\mathbb{R}$.
- Walter Rudin, *Principles of Mathematical Analysis*, 3rd edition (McGraw-Hill, 1976), for worked computations with suprema, roots and the density of the rationals.
- Israel Nathan Herstein, *Topics in Algebra*, 2nd edition (Wiley, 1975), for the inverse formula and the group of units.
- John B. Fraleigh, *A First Course in Abstract Algebra*, 7th edition (Addison–Wesley, 2003), for concrete field computations and the sign of an element.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the place of the real algebra in the ladder of the division algebras.
