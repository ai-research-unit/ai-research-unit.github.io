
# __Ore Domains and Division Rings of Fractions__

## Introduction

This article is the fourth rung of the non-commutative chain of *Rings and Fields*, directly above *Non-Commutative Domains* and below *Division Rings*. Throughout, $A$ is a ring with $1 \neq 0$ **not assumed commutative**, and the default base of the corpus, the commutative ring, is not the base here.

In the commutative chain every integral domain sits inside its fraction field, constructed in *Localization and the Fraction Field*, above. That construction forms pairs of elements and inverts the denominator, and the whole difficulty of transferring it is what a common denominator should be when the ring is not commutative: the left multiples of one element and the right multiples of another need not meet, and when they do not, no ordered pair can be put over a common denominator. The condition that makes the construction work is the **Ore condition**, and a domain satisfying it is an **Ore domain**; its fraction field is replaced by a **division ring of fractions**. The article states the condition in its left, right and oriented forms and records the standard theorem that the two forms agree for a domain, constructs the division ring of fractions and proves its universal property, and then treats the two families of examples that decide the theory. The first is the **Malcev–Neumann** construction, which builds a division ring containing the group ring of an ordered group **combinatorially**, as coefficientwise-finite sums whose support is well ordered; the group ring of an ordered group is an Ore domain, and its division ring of fractions embeds in this Malcev–Neumann division ring. The second is the Weyl algebra, whose division ring of fractions is the standard non-commutative division ring infinite-dimensional over its centre. The free algebra is the standard domain that fails the condition, and it is shown to fail it for the simplest possible reason.

The construction below is purely combinatorial: the only structure used is the well-ordering of the supports, every series written is a sum whose every coefficient is a finite sum of ring elements, and neither a completion nor a convergent infinite sum is involved anywhere.

---

## The Ore Condition

**Definition.** A domain $A$ satisfies the **left Ore condition** if for all nonzero $a, b \in A$ there exist nonzero $x, y \in A$ with $xa = yb$; equivalently, if $Aa \cap Ab \neq 0$ for all nonzero $a$ and $b$. It satisfies the **right Ore condition** if for all nonzero $a, b$ there exist nonzero $x, y$ with $ax = by$; equivalently, if $aA \cap bA \neq 0$.

The equation $xa = yb$ is the **oriented form** of the left condition: it exhibits the two left multipliers $x$ and $y$ on the two sides of a common left multiple and so orients the equality. In the commutative case the condition holds trivially, since $ba = ab$ is a nonzero common left multiple of $a$ and $b$, so every commutative domain is an Ore domain in both senses, and the interest of the condition lies entirely in the non-commutative case.

**Definition.** A **left Ore domain** is a domain satisfying the left Ore condition, a **right Ore domain** is a domain satisfying the right Ore condition, and an **Ore domain** is a domain satisfying both.

**Theorem (Ore, standard).** A domain satisfies the left Ore condition if and only if it satisfies the right Ore condition. Hence every left Ore domain is a right Ore domain, and conversely.

**Proof.** This is the left–right symmetry theorem of Ore, cited here from the literature rather than re-derived. It is what licenses the single name above: the construction of the next section writes left fractions and uses the left-handed form of the condition, and by the theorem the same construction can be read in right fractions. $\square$

**Remark.** The symmetry theorem is not a triviality of definitions: the left condition constrains intersections of left ideals and the right condition intersections of right ideals, and neither inclusion $Aa \cap Ab \neq 0$ nor $aA \cap bA \neq 0$ implies the other by a one-line manipulation. The theorem is used below only to pass from one to the other within a single domain.

**Example.** Every commutative integral domain is an Ore domain. The Weyl algebra $A_1(k)$ and the group ring of an ordered group are non-commutative examples, treated below. The free algebra $k\langle x_1, x_2\rangle$ is not an Ore domain, and the last section of the article shows why in one line.

**Theorem (Goldie, standard).** A Noetherian domain, left or right, is an Ore domain.

**Proof.** This is the standard consequence of the ascending chain condition for one-sided ideals, due to Goldie and cited from the literature rather than reproduced here. The argument exhibits, from two nonzero elements with no nonzero common left multiple, a strictly increasing chain of left ideals, which the Noetherian hypothesis forbids. $\square$

**Corollary.** The Weyl algebra $A_1(k)$ over a field $k$ of characteristic zero is an Ore domain, being a Noetherian domain.

---

## The Division Ring of Fractions

**Definition.** A **division ring of fractions** of a domain $A$ is a division ring $D$ together with an injective ring homomorphism $A \to D$ such that every element of $D$ can be written as a left fraction $a^{-1}b$ with $a, b \in A$ and $a \neq 0$. The construction is written $\operatorname{Frac}(A)$, extending the notation of the commutative *Localization and the Fraction Field*, above.

**Theorem (Ore).** Every Ore domain has a division ring of fractions, and any two are isomorphic by an isomorphism fixing $A$.

**Proof.** Let $A$ be an Ore domain and let $S$ be the set of pairs $(a, b)$ with $a \neq 0$. Call two pairs equivalent, written $(a, b) \sim (c, d)$, when there are nonzero $x, y \in A$ with $xa = yc$ and $xb = yd$; such $x, y$ exist by the Ore condition, and the relation is an equivalence: it is reflexive and symmetric at once, and transitivity follows by merging two common left multiples with the Ore condition. Write the class of $(a, b)$ as $a^{-1}b$, and let $D$ be the set of classes.

*Addition.* Given $a^{-1}b$ and $c^{-1}d$, choose nonzero $x, y$ with $xa = yc$, and put

$$
a^{-1}b + c^{-1}d = (xa)^{-1}(xb + yd) .
$$

The right-hand side depends only on the two classes: replacing $(xa, xb)$ by an equivalent pair changes both terms of the numerator in the same way, and applying the equivalence to the sum shows it is well defined.

*Multiplication.* Given $a^{-1}b$ and $c^{-1}d$, apply the Ore condition to the pair $b, c$ and choose nonzero $x, y$ with $xb = yc$, so that $bc^{-1} = x^{-1}y$ in the sense of the classes, and put

$$
(a^{-1}b)(c^{-1}d) = (xa)^{-1}(yd) .
$$

This is again well defined, and the ring axioms follow from the ring axioms of $A$ after rewriting sums over common left denominators and products over the two kinds of common multiple.

*The embedding.* The map $A \to D$ sending $b$ to $1^{-1}b$ is a ring homomorphism, and it is injective by the cancellation criterion of *Non-Commutative Domains*, above: if $1^{-1}b = 0 = 1^{-1}0$ then $(1, b) \sim (1, 0)$ gives nonzero $x, y$ with $x = y$ and $xb = 0$, hence $b = 0$.

*Units.* Let $a^{-1}b \neq 0$, so $b \neq 0$. Taking $c = b$ and $d = a$ in the multiplication formula with $x = y = 1$ gives $(a^{-1}b)(b^{-1}a) = a^{-1}a = 1$, and the symmetric computation gives $1$ on the other side. Hence every nonzero element of $D$ is a unit and $D$ is a division ring. Uniqueness follows from the universal property. $\square$

**Theorem (universal property).** Let $A$ be an Ore domain, let $D$ be a division ring and let $\varphi : A \to D$ be a homomorphism with $\varphi(a) \neq 0$ whenever $a \neq 0$. Then $\varphi$ extends uniquely to a homomorphism $\operatorname{Frac}(A) \to D$.

**Proof.** An extension must send $a^{-1}b$ to $\varphi(a)^{-1}\varphi(b)$, so there is at most one. For existence, the formula is well defined on classes: if $xa = yc$ and $xb = yd$ in $A$ with $x, y$ nonzero, then applying $\varphi$ gives $\varphi(x)\varphi(a) = \varphi(y)\varphi(c)$ and $\varphi(x)\varphi(b) = \varphi(y)\varphi(d)$ in $D$, whence $\varphi(a)^{-1}\varphi(b) = \varphi(c)^{-1}\varphi(d)$ by inversion of the nonzero elements. Preservation of sums and products is the two identities used in the construction. Hence there is one extension. $\square$

**Corollary.** If $A$ is a commutative domain then $\operatorname{Frac}(A)$ is the fraction field of *Localization and the Fraction Field*, above, and the construction above specialises to it; the Ore domains are exactly the domains for which the fraction construction can be carried out with left and right fractions interchanged freely.

**Remark.** Not every domain has a division ring of fractions; a domain that has none may still embed in a division ring. The free algebra is the standard example of the first kind, and its embedding in Cohn's free field is cited in the last section. Such an embedding is not a division ring of fractions in the sense of the definition above, since its elements are not all left fractions.

---

## Malcev–Neumann Series

The ore domains of the two sections above are abstract. The first concrete family is built from an ordered group, and the construction is purely combinatorial: every element is a function on the group whose support is well ordered, and every coefficient written below is a finite sum of field elements.

**Definition.** A group $G$ is **ordered** if it carries a total order invariant under multiplication on both sides, so that $g < h$ implies $xg < xh$ and $gx < hx$ for all $x \in G$.

The additive groups $\mathbb{Z}^n$ with the lexicographic order and the free groups of any rank are ordered groups; these are standard facts, cited from the literature. A subset $S \subseteq G$ is **well ordered** if every nonempty subset of $S$ has a least element.

**Definition.** Let $k$ be a field and let $G$ be an ordered group. A **Malcev–Neumann series** is a function $f : G \to k$ whose **support**

$$
\operatorname{supp}(f) = \{g \in G : f(g) \neq 0\}
$$

is well ordered. The set of all Malcev–Neumann series is written $k((G))$. Addition is coefficientwise, and multiplication is the convolution

$$
(fh)(g) = \sum_{uv = g} f(u)h(v) ,
$$

the sum being over the pairs $(u, v) \in G \times G$ with $uv = g$.

**Lemma (Malcev–Neumann, standard).** Let $f$ and $h$ be Malcev–Neumann series. Then at each $g \in G$ there are only finitely many pairs $(u, v)$ with $uv = g$, $f(u) \neq 0$ and $h(v) \neq 0$; the product $fh$ defined by the convolution is a Malcev–Neumann series; and if the support of $h$ lies strictly above the identity, then so does the support of every power of $h$, and

$$
(1 - h)(1 + h + h^2 + h^3 + \cdots) = 1 ,
$$

the series being a Malcev–Neumann series.

**Proof.** All three statements are the standard combinatorial lemmas of the construction, cited from Malcev and from B. H. Neumann. The first holds because a pair $(u, v)$ with $uv = g$ is determined by $u$, the equation giving $v = u^{-1}g$, so the admissible $u$ form a subset of the well-ordered set $\operatorname{supp}(f)$ and the corresponding $v$ form a subset of $\operatorname{supp}(h)$. If there were infinitely many, then the $u$, being an infinite subset of a well-ordered set, would contain an infinite strictly increasing sequence $u_1 < u_2 < \cdots$, and then $v_i = u_i^{-1}g$ would be an infinite strictly decreasing sequence in $\operatorname{supp}(h)$, which its well-ordering forbids. The second follows from the first and the same well-ordering argument applied to the set of products $uv$. The third is the telescoping identity, which reduces to the first statement applied to the powers of $h$; the support of a power of an element with support above the identity stays above the identity, since the elements above the identity form a subsemigroup. $\square$

**Theorem (Malcev–Neumann).** Let $k$ be a field and $G$ an ordered group. Then $k((G))$ is a division ring, and the finitely supported series form a subring isomorphic to the group ring $k[G]$.

**Proof.** The ring axioms hold coefficientwise on the sums and products of the lemma, and the finitely supported series are closed under both operations and contain the identity, which is the function taking the value $1$ at the identity of $G$; assigning to a group element the function taking the value $1$ at that element and $0$ elsewhere is an injective homomorphism $k[G] \to k((G))$. For the units, let $f \neq 0$ and let $g_0$ be the least element of $\operatorname{supp}(f)$, which exists by the well-ordering, and put $c = f(g_0) \neq 0$. Define

$$
h = 1 - (cg_0)^{-1}f .
$$

Then $h(1) = 1 - c^{-1}f(g_0) = 0$, and for $x$ below the identity, $g_0x$ is below $g_0$, hence outside the support of $f$, so $h(x) = 0$ as well. Therefore the support of $h$ lies strictly above the identity, and the third part of the lemma applies:

$$
f^{-1} = (1 + h + h^2 + h^3 + \cdots)(cg_0)^{-1} ,
$$

which lies in $k((G))$; indeed $f = cg_0(1 - h)$, the identity $(1 - h)(1 + h + h^2 + \cdots) = 1$ is the telescoping identity of the lemma, and $cg_0$ is invertible with inverse $c^{-1}g_0^{-1}$. So every nonzero element $f$ has a right inverse $g$, and then $g \neq 0$ and $g$ has a right inverse $h$, whence

$$
f = f \cdot 1 = f(gh) = (fg)h = h ,
$$

so $gf = gh = 1$ as well and $g$ is a two-sided inverse. Hence every nonzero element of $k((G))$ is a unit. $\square$

**Corollary.** Let $G$ be an ordered group. Then $k[G]$ is an Ore domain, and the inclusion $k[G] \to k((G))$ extends by the universal property to an embedding $\operatorname{Frac}(k[G]) \to k((G))$ of division rings over $k[G]$.

**Proof.** The group ring is the subring of finitely supported series; it has no zero divisors by *Non-Commutative Domains*, above, and that it satisfies the Ore condition is the standard fact that the group ring of an orderable group is an Ore domain, cited from the literature. Hence $\operatorname{Frac}(k[G])$ exists, and the inclusion of $k[G]$ into the division ring $k((G))$ is injective, so the universal property of $\operatorname{Frac}(k[G])$ provides the embedding. $\square$

**Remark.** The embedding is proper in general, and it need not be an isomorphism: the division ring of fractions of a group ring is the smallest division ring containing it, whereas $k((G))$ also contains series that are not fractions of finitely supported ones. The case $G = \mathbb{Z}$ below exhibits the two rings explicitly. What the construction supplies for the purpose of this chain is not an identification of $k((G))$ with a fraction ring, but a division ring into which an Ore domain embeds, and the two examples of the rung are of that kind.

**Example ($G = \mathbb{Z}$).** With the usual order, the Malcev–Neumann series over $\mathbb{Z}$ are the sums $\sum_{n \geq n_0} c_n t^n$ for an indeterminate $t$, so $k((\mathbb{Z})) = k((t))$ is the field of Laurent series, and the group ring $k[\mathbb{Z}] = k[t, t^{-1}]$ is the ring of Laurent polynomials, whose fraction field is $k(t)$, embedded in $k((t))$ by expanding each rational function at the origin. This is the commutative instance of the whole construction, and it shows the two division rings of the corollary to be distinct here.

**Example ($G$ free).** If $G$ is a free group of rank at least two, it is ordered and $k[G]$ is an Ore domain whose division ring of fractions embeds in the Malcev–Neumann division ring $k((G))$. The group ring of a free group is thus the standard non-commutative example in which the construction succeeds, in contrast with the free algebra of the last section, which is the monoid algebra of the free monoid on the same number of generators and fails the condition.

---

## The Weyl Algebra and Its Division Ring of Fractions

**Theorem.** The Weyl algebra $A_1(k)$ over a field $k$ of characteristic zero is a Noetherian domain, hence an Ore domain, and its division ring of fractions is written $D_1(k)$ and called the **first Weyl field**.

**Proof.** The algebra $A_1(k)$ is the skew polynomial ring $k[x][y; \delta]$ with the derivation $\delta(x) = -1$, which is to say $yx - xy = \delta(x) = -1$; the Hilbert basis theorem for skew polynomial rings gives that it is left and right Noetherian, cited here as standard, and it is a domain by *Non-Commutative Domains*, above. By the Noetherian criterion of the first section it is an Ore domain, so Ore's theorem applies and $D_1(k) = \operatorname{Frac}(A_1(k))$ exists. The field $D_1(k)$ is infinite-dimensional over its centre, which is $k$: the standard computation of the centre of the Weyl algebra gives $Z(A_1(k)) = k$, and the powers of $y$ are linearly independent over $k$ inside $A_1(k) \subseteq D_1(k)$. $\square$

**Example.** The first Weyl field is the standard division ring that is infinite-dimensional over its centre, and $A_1(k)$ is the standard Ore domain that is not a group ring and not commutative. It is one of the two kinds of example of *Division Rings*, below this article in this category, the other being finite-dimensional over its centre.

**Example.** The centre of $A_1(k)$ is $k$, since $k$ has characteristic zero and $A_1(k)$ has the basis $x^i y^j$ of *Non-Commutative Domains*, above: an element central in $A_1(k)$ is fixed by the inner derivations $z \mapsto zx - xz$ and $z \mapsto zy - yz$, and the first lowers the power of $y$ while the second lowers the power of $x$, so a central element must be a constant. Hence $D_1(k)$ is an algebra over $k$ and $k$ is its centre.

---

## The Free Algebra Is Not an Ore Domain

**Theorem.** The free algebra $k\langle x_1, x_2\rangle$ satisfies neither the left nor the right Ore condition: $Ax_1 \cap Ax_2 = 0$ and $x_1A \cap x_2A = 0$.

**Proof.** An element of $Ax_1$ is a $k$-linear combination of words ending in $x_1$, and an element of $Ax_2$ is a combination of words ending in $x_2$, as noted in *Non-Commutative Domains*, above, where the free algebra is defined and shown to be a domain. No word ends in both letters, so a combination lying in both ideals is zero; the right-handed statement is the same argument read from the other end. $\square$

**Corollary.** The free algebra has no division ring of fractions, and the failure is witnessed by the two generators: they have no nonzero common left multiple and no nonzero common right multiple.

**Remark.** The free algebra nevertheless embeds in a division ring. Cohn's free field is the universal division ring containing the free algebra, defined by the property that every homomorphism from the free algebra to a division ring that is injective on the generators extends uniquely to it, and it is cited here from the literature. The embedding is not a division ring of fractions in the sense of this article, because its construction is not the localisation of the free algebra at its nonzero elements and its elements are not all left fractions $a^{-1}b$ with $a$ and $b$ in the free algebra; the distinction between the two notions is exactly the Ore condition.

---

## Summary

A domain satisfies the left Ore condition when any two nonzero elements have a nonzero common left multiple, the right condition being the same with the order of multiplication reversed in the oriented form; the two conditions are equivalent for a domain by the standard symmetry theorem, and a domain satisfying them is an Ore domain. Every commutative integral domain is an Ore domain, every Noetherian domain is one, and the free algebra is not, because its principal left ideals $Ax_1$ and $Ax_2$ meet only in zero. Every Ore domain has a division ring of fractions $\operatorname{Frac}(A)$, the ring of left fractions $a^{-1}b$, unique up to isomorphism over $A$ and characterised by the universal property that every injective homomorphism from $A$ to a division ring extends uniquely to it; in the commutative case it is the fraction field of *Localization and the Fraction Field*, above. The Malcev–Neumann construction gives the division ring $k((G))$ of coefficientwise-finite series with well-ordered support over an ordered group $G$, in which inversion is an explicit geometric series; the group ring $k[G]$ is an Ore domain and its division ring of fractions embeds in $k((G))$, the two coinciding only in special cases, and the Laurent series $k((t))$ over $G = \mathbb{Z}$ are the commutative instance. The Weyl algebra $A_1(k)$ is a Noetherian domain, so an Ore domain, and its division ring of fractions is the first Weyl field $D_1(k)$, infinite-dimensional over its centre $k$. The free algebra is the standard non-Ore domain, and it still embeds in a division ring by Cohn's construction, which is not a division ring of fractions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | A ring with $1 \neq 0$, not assumed commutative; the base of this article |
| left Ore condition | $Aa \cap Ab \neq 0$ for all nonzero $a, b$; oriented form $xa = yb$ with $x,y$ nonzero |
| right Ore condition | $aA \cap bA \neq 0$ for all nonzero $a, b$; oriented form $ax = by$ with $x,y$ nonzero |
| Ore domain | A domain satisfying both Ore conditions |
| $\operatorname{Frac}(A)$ | The division ring of fractions, the ring of left fractions $a^{-1}b$; the fraction field in the commutative case |
| ordered group | A group with a total order invariant on both sides |
| well ordered | Every nonempty subset has a least element |
| $k((G))$ | The Malcev–Neumann division ring of coefficientwise-finite series on the ordered group $G$ |
| $\operatorname{supp}(f)$ | The support of a series, required to be well ordered |
| $k[G]$ | The group ring of an ordered group $G$, an Ore domain whose division ring of fractions embeds in $k((G))$ |
| $k((t))$, $k[t, t^{-1}]$ | The Laurent series and Laurent polynomials, the case $G = \mathbb{Z}$ |
| $A_1(k)$, $D_1(k)$ | The Weyl algebra, a Noetherian Ore domain, and the first Weyl field $\operatorname{Frac}(A_1(k))$ |
| $Z(A_1(k)) = k$ | The centre of the Weyl algebra, so that $D_1(k)$ is infinite-dimensional over it |
| $k\langle x_1, x_2\rangle$ | The free algebra, not an Ore domain: $Ax_1 \cap Ax_2 = 0$ |

## Further Reading

- P. M. Cohn, *Free Rings and Their Relations* (Academic Press, 2nd ed. 1985), for the free field, the failure of the Ore condition in the free algebra, and the theory of free ideal rings.
- K. R. Goodearl and R. B. Warfield, *An Introduction to Noncommutative Noetherian Rings* (Cambridge University Press, 2nd ed. 2004), for the Ore condition, Ore's theorem, Goldie's theorem and the Weyl algebra.
- A. I. Malcev, *On the embedding of group algebras in division algebras* (Doklady Akademii Nauk SSSR, 1948), for the Malcev–Neumann construction and its combinatorial convergence.
- B. H. Neumann, *On ordered division rings* (Transactions of the American Mathematical Society, 1949), for the well-ordered supports of the series and the division ring of fractions of a group ring.
- Ø. Ore, *Linear equations in non-commutative fields* (Annals of Mathematics, 1931), for the Ore condition, its symmetry and the division ring of fractions.
- T. Y. Lam, *Lectures on Modules and Rings* (Springer, 1999), for the Ore conditions, Noetherian domains and the construction of the quotient division ring.
