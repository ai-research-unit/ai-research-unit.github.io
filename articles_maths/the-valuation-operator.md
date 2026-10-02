
# __The Valuation Operator__

## Introduction

A valuation of a field is a multiplicative operator in the strict sense: it is a homomorphism from the multiplicative group of the field onto an ordered abelian group, extended to zero by a point at infinity, and the additive inequality it satisfies is the statement that it converts addition into a minimum. This article treats the valuation as an operator for itself: it fixes it, computes its kernel as the units of the valuation ring and its image as the value group, shows that it is continuous when the value group is discrete and that it extends to the completion with the same image, and develops the **tropical reading**, in which the valuation is exactly a monoid homomorphism from the field under multiplication to the tropical semiring of the value group with the operations minimum and addition.

The article assumes the absolute value, the valuation $v : F \to \Gamma \cup \{\infty\}$, the value group, the valuation ring, the maximal ideal and the residue field from *Absolute Values, Valuations and Completions*; the completion of a valued field and the persistence of its value group from the same article; the linear and metric topologies of the valuation ring and the closure of zero from *Topological Rings and Fields*; the completion operator and its functoriality from *The Completion Operator*; and the residue operator, whose kernel is the maximal ideal, from *The Residue Operator of a Valued Field*. The structure of the multiplicative group of a local field and the ramification are *Local Fields*, and are named only. No measure and no form occurs.

Throughout, $F$ is a field, $\lvert \cdot \rvert$ a non-Archimedean absolute value, $v$ the associated valuation into the ordered abelian group $\Gamma$, written additively, with $v(0) = \infty$; $\mathcal{O} = \{x : v(x) \geq 0\}$ is the valuation ring, $\mathrm{M} = \{x : v(x) > 0\}$ its maximal ideal, $k = \mathcal{O}/\mathrm{M}$ the residue field, and $\widehat{F}$ the completion with value group $\Gamma_{\widehat{F}}$.

## The Valuation as an Operator

**Definition.** The **valuation** of $(F, \lvert \cdot \rvert)$ is the map

$$
v : F \longrightarrow \Gamma \cup \{\infty\}, \qquad v(x) = -\log_c \lvert x \rvert \ \ (x \neq 0), \qquad v(0) = \infty ,
$$

for a fixed real $c > 1$, with the conventions $\gamma + \infty = \infty$ and $\gamma < \infty$ for $\gamma \in \Gamma$. It satisfies, for all $x, y \in F$,

$$
v(xy) = v(x) + v(y), \qquad v(x + y) \geq \min\{v(x), v(y)\}, \qquad v(x) = \infty \iff x = 0 .
$$

**Proposition (it is a homomorphism on the multiplicative group).** The restriction $v : F^\times \to \Gamma$ is a surjective group homomorphism from the multiplicative group of $F$ onto the value group, and the extension by $v(0) = \infty$ is the unique way of making it defined on all of $F$ while keeping the multiplicative law with $\infty + \gamma = \infty$.

**Proof.** The law $v(xy) = v(x) + v(y)$ is the multiplicativity of the absolute value under $-\log_c$, and it makes $v$ a homomorphism from the multiplicative monoid of the nonzero elements into the additive group $\Gamma$; it is surjective onto $\Gamma = v(F^\times)$ by definition. The value $\infty$ is forced at $0$ because $0$ has no multiplicative inverse and the only element that can satisfy the laws is the absorbing one.

**Proposition (the kernel is the units of the valuation ring).** The kernel of the homomorphism $v : F^\times \to \Gamma$ is the unit group of the valuation ring,

$$
\ker v = \mathcal{O}^\times = \{ x : v(x) = 0 \} ,
$$

and the residue operator restricts to a homomorphism $\mathcal{O}^\times \to k^\times$ with kernel the principal units; in particular $F^\times/\mathcal{O}^\times \cong \Gamma$.

**Proof.** $v(x) = 0$ is $\lvert x \rvert = 1$, which is the condition for $x$ and $x^{-1}$ both to lie in $\mathcal{O}$, that is $x \in \mathcal{O}^\times$. The first isomorphism theorem then gives $F^\times/\mathcal{O}^\times \cong \Gamma$, and the residue statement is *The Residue Operator of a Valued Field*.

## The Kernel and the Valuation Ring

**Proposition (the valuation ring is a sublevel set).** The valuation ring, its maximal ideal and the multiplicative group are the level sets of the valuation:

$$
\mathcal{O} = \{ x : v(x) \geq 0 \}, \qquad \mathrm{M} = \{ x : v(x) > 0 \}, \qquad F^\times = \{ x : v(x) < \infty \},
$$

and the valuation is order reversing for the divisibility: $v(y) \leq v(x)$ exactly when $y$ divides $x$ in $\mathcal{O}$, and $v(x) < v(y)$ exactly when $x$ divides $y$ in $\mathcal{O}$.

**Proof.** The three level descriptions are the definitions, read through $v = -\log_c\lvert \cdot \rvert$. For divisibility, $y | x$ in $\mathcal{O}$ means $x = yz$ with $z \in \mathcal{O}$, that is $v(x) = v(y) + v(z)$ with $v(z) \geq 0$, which is $v(x) \geq v(y)$.

**Corollary (the valuation sees the ideals).** The nonzero ideals of the valuation ring are the sets $\mathrm{M}_\gamma = \{x : v(x) \geq \gamma\}$ for $\gamma$ in the value group, and when $\Gamma \cong \mathbb{Z}$ they are the powers $\mathrm{M}^n$. The valuation is therefore the operator that labels the ideals of the valuation ring by the value group.

**Proof.** An ideal of $\mathcal{O}$ is determined by the infimum of the values of its elements, which is attained when the value group is discrete; the sets $\mathrm{M}_\gamma$ are ideals and every ideal is one of them. The discrete case is the computation of a discrete valuation ring in *Absolute Values, Valuations and Completions* and *Local Fields*.

## Continuity and the Completion

**Proposition (the valuation is continuous when the value group is discrete).** Give $\Gamma \cup \{\infty\}$ the discrete topology. Then the valuation $v : F \to \Gamma \cup \{\infty\}$ is continuous: its fibres are the spheres $\{x : v(x) = \gamma\}$ and the point $\{0\}$, each of which is open and closed in the ultrametric topology of $F$.

**Proof.** For $\gamma \in \Gamma$ the fibre is $\{x : \lvert x \rvert = c^{-\gamma}\}$, the difference of the closed ball $\{\lvert x \rvert \leq c^{-\gamma}\}$ and the open ball $\{\lvert x \rvert < c^{-\gamma}\}$; in an ultrametric space every ball is open and closed, so the difference of two clopen sets is clopen, hence open, and its complement is a union of fibres, hence open; thus the fibres are open and the map to a discrete space is continuous. The fibre over $\infty$ is $\{0\}$, closed, and open when the absolute value is nontrivial and $\{0\}$ is isolated.

**Theorem (the valuation of the completion).** The valuation extends uniquely to a valuation $\widehat{v}$ of the completion $\widehat{F}$ with the same value group,

$$
\Gamma_{\widehat{F}} = \Gamma , \qquad \widehat{v}\circ \iota = v ,
$$

and the completion has the same valuation ring and maximal ideal up to the canonical identification, $\widehat{\mathcal{O}} = \overline{\iota(\mathcal{O})}$ and $\widehat{\mathrm{M}} = \overline{\iota(\mathrm{M})}$. So the valuation operator commutes with the completion operator.

**Proof.** The completion of a non-Archimedean field preserves the value group, which is the theorem of *Absolute Values, Valuations and Completions*; the extension is defined by continuity of $v$ and is a valuation because the defining laws pass to limits, and it is unique because $\iota(F)$ is dense. The identification of the valuation ring is the persistence of the residue field and the open unit ball.

## The Tropical Reading

The valuation converts the two operations of the field into the two operations of a semiring in which addition is minimum.

**Definition.** The **tropical semiring** of the ordered abelian group $\Gamma$ is the set $\Gamma \cup \{\infty\}$ with the two operations

$$
a \oplus b = \min\{a, b\}, \qquad a \odot b = a + b ,
$$

with neutral elements $\infty$ for $\oplus$ and $0$ for $\odot$.

**Proposition.** The tropical semiring is a commutative semiring: $\oplus$ and $\odot$ are associative and commutative, $\odot$ distributes over $\oplus$, $\infty$ is neutral for $\oplus$ and absorbing for $\odot$, and $0$ is neutral for $\odot$.

**Proof.** The minimum is associative, commutative and idempotent, with neutral element $\infty$; the addition of $\Gamma$ is associative and commutative with neutral element $0$ and, extended by $a + \infty = \infty$, absorbs $\infty$; distributivity is $a + \min\{b, c\} = \min\{a + b, a + c\}$, which is the compatibility of the order of $\Gamma$ with its addition.

**Theorem (the valuation is a tropical homomorphism).** The valuation is a homomorphism from the multiplicative monoid $(F, \cdot)$ to the tropical semiring $(\Gamma \cup \{\infty\}, \oplus, \odot)$:

$$
v(xy) = v(x) \odot v(y), \qquad v(x + y) \geq v(x) \oplus v(y) .
$$

It is exactly multiplicative, and additive up to the inequality forced by cancellation. When the inequality is an equality for all $x, y$ the field is said to have a **splitting** of the valuation; the inequality is strict exactly when the two summands have equal value and cancel.

**Proof.** The multiplicative law is $v(xy) = v(x) + v(y)$, which is $\odot$; the additive law is the ultrametric inequality, which is $\geq$ the minimum, that is $\geq \oplus$. Strictness occurs exactly on the cancellation of two terms of equal value, in which case $v(x) = v(y)$ and $v(x+y) > v(x)$, so the two sides differ.

**Remark (what the tropical reading is and is not).** The reading is a translation of the two defining laws into the language of the tropical semiring; it is not a construction of new field elements, the tropical operations being defined on the value group and not on $F$. Its content is that the valuation is a morphism of the multiplicative structure of $F$ into a semiring carried by the values, and that the additive inequality is the exact shadow of the cancellation that a valuation cannot see. The associated absolute value is recovered by $\lvert x \rvert = c^{-v(x)}$ for any $c > 1$, so the tropical data and the multiplicative data determine each other.

## Examples

**Example ($v_p$ on $\mathbb{Q}$).** The $p$-adic valuation $v_p$ has value group $\mathbb{Z}$, kernel the rationals of value $0$, that is the numbers with numerator and denominator prime to $p$; its completion is $\mathbb{Q}_p$ with the same value group and the same residue field $\mathbb{F}_p$.

**Example ($k((t))$ and the order of vanishing).** On $k((t))$ the valuation $v(f)$ is the order of vanishing at $0$, with value group $\mathbb{Z}$, kernel the series with nonzero constant term, and valuation ring $k[[t]]$; the extension to the completion is the identity, the field being already complete.

**Example (a non-discrete value group).** On a field with a dense value group, such as $\mathbb{C}_p$, the valuation has value group $\mathbb{Q}$ embedded in $\mathbb{R}$; the fibres are still clopen for the order topology on $\Gamma$, but there is no uniformiser and the ideals of the valuation ring are not the powers of a single element.

## Summary

The valuation operator is the map $v : F \to \Gamma \cup \{\infty\}$, defined by $v(x) = -\log_c\lvert x \rvert$ and $v(0) = \infty$, satisfying $v(xy) = v(x) + v(y)$ and $v(x+y) \geq \min\{v(x), v(y)\}$. It restricts to a surjective homomorphism $F^\times \to \Gamma$ whose kernel is the unit group $\mathcal{O}^\times$ of the valuation ring, so that $F^\times/\mathcal{O}^\times \cong \Gamma$; the valuation ring, its maximal ideal and the field of nonzero elements are the sublevel and upper level sets $\{v \geq 0\}$, $\{v > 0\}$ and $\{v < \infty\}$, and the valuation orders the elements by divisibility and labels the ideals of the valuation ring by the value group. It is continuous when the value group carries the discrete topology, its fibres being clopen spheres, and it extends to the completion with the same value group, $\Gamma_{\widehat{F}} = \Gamma$, so the valuation operator commutes with the completion operator.

The tropical reading makes the two laws into the statement that $v$ is a homomorphism from the multiplicative monoid of $F$ to the tropical semiring $(\Gamma \cup \{\infty\}, \min, +)$: multiplication becomes addition and addition becomes the minimum, exactly for the products and up to the cancellation inequality for the sums. The tropical reading is a translation of the valuation and not a construction on the field; together with the choice of a base $c > 1$ it is equivalent to the absolute value.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $v$, $\lvert \cdot \rvert$ | The field, its valuation and its absolute value |
| $\Gamma = v(F^\times)$ | The value group, ordered and written additively |
| $v(0) = \infty$ | The point at infinity, greater than every element of $\Gamma$ |
| $\mathcal{O} = \{v \geq 0\}$, $\mathrm{M} = \{v > 0\}$ | Valuation ring and maximal ideal |
| $\ker v = \mathcal{O}^\times$ | The kernel of the valuation on $F^\times$ |
| $F^\times/\mathcal{O}^\times \cong \Gamma$ | The value group as a quotient |
| $\mathrm{M}_\gamma = \{v \geq \gamma\}$ | The ideal of elements of value at least $\gamma$ |
| $\Gamma \cup \{\infty\}, \oplus = \min, \odot = +$ | The tropical semiring of the value group |
| $v(xy) = v(x) \odot v(y)$, $v(x+y) \geq v(x) \oplus v(y)$ | The tropical homomorphism laws |
| $\Gamma_{\widehat{F}} = \Gamma$ | The value group is unchanged by completion |

## Further Reading

- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for valuations, their rings and the extension to a completion.
- Nicolas Bourbaki, *Commutative Algebra, Chapters 1–7* (Springer, 1998), for valuations, value groups and the divisibility order.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for the topology of a valued field and the continuity of the valuation.
- Wim H. Schikhof, *Ultrametric Calculus* (Cambridge University Press, 1984), for the ultrametric structure of a valued field and the behaviour of the valuation on series.
- Diane Maclagan and Bernd Sturmfels, *Introduction to Tropical Geometry* (American Mathematical Society, 2015), for the tropical semiring and the valuation as a tropical homomorphism.
