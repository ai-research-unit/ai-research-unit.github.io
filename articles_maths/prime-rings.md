
# __Prime Rings__

## Introduction

This article is the second rung of the non-commutative chain of *Rings and Fields*, directly above *Semiprime Rings*, and it stands after the commutative half of the category, every rung of which is above it. Throughout, $A$ is a ring with $1 \neq 0$ **not assumed commutative**, and ideals are two-sided unless the contrary is said; the commutative theory of prime ideals is above, in *Commutative Rings*, and the default of the corpus is the commutative ring, not the ring of this article.

A ring is **prime** when the product of two nonzero ideals is never zero. The condition is the ideal-theoretic weakening of the absence of zero divisors, and the article is organised around the exact sense in which it is a weakening: a ring with no zero divisors is prime, a matrix ring is prime with plenty of zero divisors, and a prime ring need not be either. Prime **ideals** are the ideals whose quotients are prime rings, so that the commutative dictionary — prime ideal, quotient is a domain — is replaced by the two-sided one, and the article records where the old dictionary fails. The semiprime rings of the rung above are shown to contain the prime ones properly; the rings with no zero divisors, in the commutative and in the general case, are *Integral Domains*, above this article in this category, and *Non-Commutative Domains*, below it.

---

## Prime Rings

**Definition.** A ring $A$ is **prime** if $IJ \neq 0$ for all nonzero two-sided ideals $I, J \trianglelefteq A$.

Equivalently, $A$ is prime exactly when its zero ideal is prime in the sense of the section on prime ideals below.

**Theorem.** $A$ is prime if and only if for all nonzero $a, b \in A$ there is $x \in A$ with $axb \neq 0$.

**Proof.** Suppose first that $A$ is prime and let $a, b \neq 0$. The two-sided ideals $AaA$ and $AbA$ are nonzero, so their product is nonzero; and

$$
(AaA)(AbA) \subseteq A(aAb)A ,
$$

so $aAb \neq 0$ and there is $x$ with $axb \neq 0$. Conversely, suppose the displayed property holds, let $I, J$ be nonzero ideals and choose $a \in I$, $b \in J$ nonzero. Then $axb \in IJ$ for every $x \in A$, and $axb \neq 0$ for some $x$, so $IJ \neq 0$. $\square$

**Corollary.** A ring in which a product of nonzero elements is nonzero is prime. In particular every ring with no zero divisors is prime, in the commutative and in the general case; the classes themselves are *Integral Domains*, above this article in this category, and *Non-Commutative Domains*, below it.

**Proof.** If $ab \neq 0$ for all nonzero $a$ and $b$, take $x = 1$ in the criterion. $\square$

**Theorem.** Every prime ring is semiprime.

**Proof.** If $A$ is prime and $I \neq 0$ satisfies $I^2 = 0$, then the product of the two nonzero ideals $I$ and $I$ is zero, which contradicts primeness. $\square$

The converse fails, and the standard witness is a product of two rings.

**Proposition.** A direct product $A_1 \times A_2$ of nonzero rings is not prime, while it is semiprime exactly when both factors are semiprime.

**Proof.** The ideals $I = A_1 \times (0)$ and $J = (0) \times A_2$ are nonzero and $IJ = 0$, so the product is not prime. An ideal of a product has square zero exactly when both of its projections do, by the characterisation of the semiprime rings in *Semiprime Rings*, above. $\square$

**Example.** The ring $k \times k$ is semiprime and not prime, and the matrix ring $M_n(F)$ is prime and contains the nonzero nilpotent element $E_{12}$ for $n \geq 2$, so a prime ring need not be reduced; the two conditions of the pair are ordered as

$$
\text{no zero divisors} \implies \text{prime} \implies \text{semiprime} ,
$$

and each implication is strict in the non-commutative case, the first witnessed by $M_n(F)$ and the second by $k \times k$. The class of *reduced* rings, those with no nonzero nilpotent element, lies below semiprime and is not comparable with prime, as the table below records.

---

## Prime Ideals

**Definition.** A proper two-sided ideal $P \subsetneq A$ is **prime** if $IJ \subseteq P$ implies $I \subseteq P$ or $J \subseteq P$ for all two-sided ideals $I, J$, as in *Rings*, above. The set of prime ideals of $A$ is written $\operatorname{Spec} A$; in the commutative case it is the spectrum of *Commutative Rings*, above, considered there as a partially ordered set, and no further structure on it is used in this chain.

**Theorem.** Let $P \subsetneq A$ be two-sided. Then $P$ is prime if and only if the quotient ring $A/P$ is prime.

**Proof.** By the correspondence theorem of *Rings*, above, the two-sided ideals of $A/P$ are exactly the $\pi(I)$ for ideals $I$ of $A$ containing $P$, and $\pi(I)\pi(J) = \pi(IJ)$. Hence $A/P$ has nonzero ideals with zero product exactly when there are ideals $I, J \not\subseteq P$ with $IJ \subseteq P$, that is, exactly when $P$ is not prime. $\square$

**Theorem.** A proper two-sided ideal $P$ is prime if and only if for all $a, b \notin P$ there is $x \in A$ with $axb \notin P$.

**Proof.** Apply the criterion for a prime ring to the quotient $A/P$: the elements outside $P$ are exactly the nonzero elements of the quotient. $\square$

**Corollary.** The zero ideal $(0)$ is prime if and only if $A$ is prime; and a ring with no zero divisors has $(0)$ prime.

**Proof.** The first statement is the definition with $P = (0)$; the second follows from the corollary of the criterion above. $\square$

**Remark.** The commutative case is the familiar one: if $A$ is commutative, $P$ is prime exactly when $ab \in P$ implies $a \in P$ or $b \in P$, and $A/P$ is then a domain, in the terminology of *Integral Domains*, above this article in this category. In the general case the second half of that statement is false, and the next section shows how.

**Proposition.** Let $I \trianglelefteq A$. Then the prime ideals of $A/I$ are exactly the ideals $P/I$ with $P$ a prime ideal of $A$ containing $I$.

**Proof.** The correspondence theorem of *Rings*, above, gives the bijection between the ideals of $A/I$ and the ideals of $A$ containing $I$, and it preserves products, so $P$ is prime exactly when $P/I$ is. The case $I = P$ gives the criterion for a ring to be prime in terms of its zero ideal. $\square$

### Minimal Primes

**Definition.** A prime ideal $P$ is **minimal over an ideal** $I$ if $P \supseteq I$ and no prime ideal strictly between $I$ and $P$ exists; $P$ is a **minimal prime** of $A$ if it is minimal over $(0)$.

**Theorem.** Every prime ideal contains a minimal prime ideal, and the intersection of the minimal primes of $A$ is $\operatorname{Nil}_*(A)$.

**Proof.** Let $P_{\lambda}$ be a chain of prime ideals under inclusion and let $I, J$ be two-sided ideals with $IJ \subseteq \bigcap_{\lambda} P_{\lambda}$, so that for every $\lambda$ we have $I \subseteq P_{\lambda}$ or $J \subseteq P_{\lambda}$. Suppose neither $I$ nor $J$ is contained in the intersection, and choose $\mu$ with $I \not\subseteq P_{\mu}$ and $\nu$ with $J \not\subseteq P_{\nu}$; then $J \subseteq P_{\mu}$ and $I \subseteq P_{\nu}$. Since the family is a chain, one of $P_{\mu}, P_{\nu}$ contains the other. If $P_{\mu} \subseteq P_{\nu}$ then $J \subseteq P_{\mu} \subseteq P_{\nu}$, contradicting $J \not\subseteq P_{\nu}$; if $P_{\nu} \subseteq P_{\mu}$ then $I \subseteq P_{\nu} \subseteq P_{\mu}$, contradicting $I \not\subseteq P_{\mu}$. Hence the intersection of a chain of prime ideals is prime.

Zorn's lemma applied to the prime ideals *contained in* a given prime ideal, ordered by reverse inclusion, now produces one minimal among them: a chain in this order is a descending chain of primes, its intersection is prime by the argument just given, and it lies below the given prime. Hence every prime ideal contains a minimal prime. The intersection of the minimal primes is contained in every prime, hence in $\operatorname{Nil}_*(A)$; and it contains $\operatorname{Nil}_*(A)$, which lies in every prime ideal. The two intersections therefore coincide. $\square$

**Corollary.** $\operatorname{Nil}_*(A)$ is the intersection of the minimal prime ideals, and $A$ is semiprime exactly when its minimal primes intersect in zero.

**Proof.** The first statement is the theorem; the second is the criterion $\operatorname{Nil}_*(A) = 0$ of *Semiprime Rings*, above. $\square$

### The Failure of the Commutative Correspondence

**Theorem.** If $A/P$ has no zero divisors then $P$ is prime; the converse fails, and the failure is total: there are prime ideals whose quotients have as many zero divisors as a matrix ring.

**Proof.** If $A/P$ has no zero divisors then it is prime, by the corollary above, hence $P$ is prime. For the failure, take $A = M_n(F)$ with $n \geq 2$ and $P = (0)$: the ring is prime, by the example below, while $E_{12} \neq 0$ and $E_{12}^2 = 0$ show that it has zero divisors. $\square$

**Example ($M_n(F)$).** The only two-sided ideals of $M_n(F)$ are $(0)$ and the whole ring, by *Rings*, above. Hence the product of two nonzero ideals is the whole ring, which is nonzero, so $M_n(F)$ is prime for every $n \geq 1$, and for $n = 1$ it is the field $F$. For $n \geq 2$ it has zero divisors and nonzero nilpotent elements, so it is prime, semiprime and not reduced; and $(0)$ is its only proper prime ideal, so $\operatorname{Spec} M_n(F)$ has a single point.

**Example.** The ring of integers $\mathbb{Z}$ is prime, and every nonzero prime ideal of $\mathbb{Z}$ has a quotient with no zero divisors; the matrix example above is the standard demonstration that this behaviour is special to the commutative case.

**Theorem.** Let $S$ be a ring and $n \geq 1$. Then the matrix ring $M_n(S)$ is prime if and only if $S$ is prime.

**Proof.** Every two-sided ideal of $M_n(S)$ has the form $M_n(I)$ for a two-sided ideal $I \trianglelefteq S$, and $M_n(I)M_n(J) = M_n(IJ)$: the containment $M_n(I)M_n(J) \subseteq M_n(IJ)$ is immediate from the definition of the matrix product, the entries of a product of a matrix over $I$ and a matrix over $J$ being sums of products $uv$ with $u \in I$ and $v \in J$, and the reverse containment follows from $E_{i1} M E_{1j}$ picking out the $(i,j)$ entry of a matrix $M$. Hence $M_n(I)M_n(J) = 0$ if and only if $IJ = 0$, so $M_n(S)$ has two nonzero ideals with zero product exactly when $S$ does. $\square$

**Corollary.** $M_n(S)$ is semiprime if and only if $S$ is semiprime, and $M_n(S)$ has no zero divisors only when $n = 1$.

**Proof.** The first statement repeats the proof above with $I = J$; the second is the computation $E_{12}E_{12} = 0$ for $n \geq 2$. $\square$

**Remark.** Two further differences from the commutative case are worth recording. First, in the commutative case a proper ideal is maximal exactly when its quotient is a field, so that maximal ideals are prime; in the general case a maximal two-sided ideal is prime, by *Rings*, above, but its quotient only has no nonzero proper two-sided ideals, and $M_n(F)$ is the quotient of itself by $(0)$ and shows that this is weaker than being a field. Second, the intersection of the prime ideals is the lower nilradical of *Semiprime Rings*, above, whose computation in the non-commutative case uses the strong nilpotence of that article and not the elementwise nilpotence of the commutative case.

---

## The Centre of a Prime Ring

**Proposition.** The centre $Z(A)$ of a prime ring is a commutative ring with no zero divisors.

**Proof.** Let $z, w \in Z(A)$ with $zw = 0$. The ideals $AzA$ and $AwA$ are two-sided, because $z$ and $w$ are central, and

$$
(AzA)(AwA) \subseteq A(zAw)A \subseteq AzwA = 0 .
$$

Since $A$ is prime, one of the two ideals is zero, and an ideal generated by a central element is zero only when that element is zero: hence $z = 0$ or $w = 0$. $\square$

**Corollary.** If $A$ is prime then $Z(A)$ is an integral domain, and $A$ is an algebra over the field $Z(A)$ when $Z(A)$ is a field. The centre of a prime ring and the structure of a division ring over its centre are taken up in *Division Rings*, below this article in this category.

**Proof.** The centre is a commutative ring with no zero divisors by the proposition, and it is a field exactly when every nonzero central element is invertible in $A$; the algebra structure is the multiplication by central elements. $\square$

**Example.** For $A = M_n(F)$ the centre is the ring of scalar matrices, isomorphic to $F$, and it is a field. For a commutative domain $R$, the centre is $R$ itself.

---

## Examples and Non-Examples

**Example (rings with no zero divisors are prime).** Let $A$ be a ring in which $ab \neq 0$ whenever $a, b \neq 0$. If $I$ and $J$ are nonzero ideals and $a \in I$, $b \in J$ are nonzero, then $ab \in IJ$ is nonzero, so $IJ \neq 0$ and $A$ is prime. The quaternion division ring $\mathbb{H}$, the free algebra $k\langle x_1, x_2\rangle$, the Weyl algebra $A_1(k)$ and the group ring of an ordered group — conjecturally, of any torsion-free group, by Kaplansky's zero divisor conjecture — are all of this kind, and are treated in *Non-Commutative Domains* and *Ore Domains and Division Rings of Fractions*, below this article in this category.

**Example (prime, not with no zero divisors).** $M_n(F)$ for $n \geq 2$, as above: prime, and its zero divisors are all the non-invertible matrices.

**Example (semiprime, not prime).** $k \times k$, and more generally any product of two nonzero rings; also the ring $k[x,y]/(xy)$, whose two nonzero ideals $(x)$ and $(y)$ have zero product. This is the example that separates the two rungs of the chain.

### The Chain of Classes

The four conditions that meet at this rung are tabulated below, with a ring satisfying each and a ring failing it. The first three are defined for a general ring, and the fourth, reducedness, is the commutative rung of *Reduced Rings and the Nilradical*, above.

| Condition | Definition | Example | Non-example |
|---|---|---|---|
| no zero divisors | $ab = 0$ forces $a = 0$ or $b = 0$; the class is *Non-Commutative Domains*, below this article, and *Integral Domains*, above it | $\mathbb{H}$ | $M_n(F)$, $n \geq 2$: $E_{12}^2 = 0$ |
| prime | $IJ \neq 0$ for all nonzero two-sided ideals $I, J$ | $M_n(F)$, any $n \geq 1$ | $k \times k$: $(k \times 0)(0 \times k) = 0$ |
| semiprime | no nonzero nilpotent two-sided ideal | $k \times k$ | $k[x]/(x^2)$: $(x)$ has square zero |
| reduced | no nonzero nilpotent element | $k[x,y]/(xy)$ | $\mathbb{Z}/4\mathbb{Z}$: $2 \neq 0$ and $2^2 = 0$ |

The implications $\text{no zero divisors} \implies \text{prime} \implies \text{semiprime}$ hold, and each is strict, by the first two rows. Reducedness implies semiprimality, since a nilpotent ideal consists of nilpotent elements, and the example $M_2(F)$ of the second row shows that the converse fails outside the commutative case; in the commutative case reducedness and semiprimality coincide, by *Semiprime Rings*, above. Reducedness and primality are incomparable, the ring $k \times k$ being reduced and not prime, and $M_n(F)$ for $n \geq 2$ prime and not reduced.

**Remark.** The implication from prime to semiprime has no counterexample: a prime ring that is not semiprime would be a product of two nonzero ideals equal to zero, which is exactly what primality forbids. The separating example is therefore the semiprime ring $k \times k$, which is not prime.

**Example (an ideal prime in the two-sided sense and not in the elementwise one).** Let $A = M_2(F)$ and let $P = (0)$. The elementwise condition "$ab \in P$ implies $a \in P$ or $b \in P$" fails, since $E_{12} \neq 0$ and $E_{12}^2 = 0$; the ideal $P$ is nevertheless prime in the two-sided sense, by the example above. Hence the elementwise definition of primality from the commutative case is strictly stronger than the two-sided definition, and it is the two-sided definition that survives without commutativity.

---

## Summary

A ring is prime when the product of two nonzero two-sided ideals is nonzero, equivalently when for all nonzero $a, b$ there is $x$ with $axb \neq 0$. A ring without zero divisors is prime, a matrix ring $M_n(F)$ with $n \geq 2$ is prime and has zero divisors, and a product of two nonzero rings is semiprime and not prime; so the chain of classes is: no zero divisors, then prime, then semiprime, with both implications strict in the non-commutative case. A two-sided ideal is prime exactly when its quotient ring is prime, and exactly when for all $a, b$ outside it there is $x$ with $axb$ outside it; the commutative correspondence between prime ideals and domains holds in one direction only, $M_n(F)$ by its zero ideal being the counterexample. The centre of a prime ring has no zero divisors, so it is a domain in the commutative sense when it is nonzero.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | A ring with $1 \neq 0$, not assumed commutative; the base of this article |
| prime ring | A ring with $IJ \neq 0$ for all nonzero two-sided ideals $I, J$ |
| prime ideal | A proper two-sided ideal with $IJ \subseteq P \Rightarrow I \subseteq P$ or $J \subseteq P$ |
| semiprime | Having no nonzero nilpotent two-sided ideal, of *Semiprime Rings* |
| reduced | Having no nonzero nilpotent element, of *Reduced Rings and the Nilradical* |
| $\operatorname{Spec} A$ | The set of prime ideals of $A$; in the commutative case the poset of *Commutative Rings* |
| $Z(A)$ | The centre of $A$ |
| $aAb$, $axb$ | The two-sided product test for primeness |
| $M_n(F)$, $E_{ij}$ | The matrix ring and its matrix units; $M_n(F)$ is prime for every $n \geq 1$ |
| $k \times k$ | A product of two nonzero rings: semiprime and not prime |
| $k[x,y]/(xy)$ | A commutative semiprime ring that is not prime |
| $\mathbb{Z}$ | The model prime ring whose quotients by nonzero primes have no zero divisors |

## Further Reading

- I. N. Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for prime rings, prime ideals and the two-sided dictionary.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the prime ideals of a general ring and the topology on them.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the chain from domains to prime to semiprime rings and the matrix-ring counterexamples.
- T. Y. Lam, *Exercises in Classical Ring Theory* (Springer, 2nd ed. 2003), for the standard examples of prime rings that are not domains.
- Louis H. Rowen, *Ring Theory, Volume 1* (Academic Press, 1988), for prime rings, their centres and the prime spectrum.
