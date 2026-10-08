# __Simple Sesqualgebras and Minimal Ideals__

## Introduction

An algebra is **simple** when its only two-sided ideals are the zero ideal and the algebra itself. The notion is stated with a product, and in a sesqualgebra there are two: the sesquilinear product $\star$, which the two scalar rules fix, and the product of the underlying algebra, written by juxtaposition. The choice matters, and this article fixes it at the start. A second notion sits beside simplicity: the algebra is **invariant-simple** when its only $\ast$-ideals are $0$ and $A$, an invariant ideal being one that the involution preserves.

For the sesquilinear product the two notions coincide, and that is the first result below. Simple implies invariant-simple at once, because a $\ast$-ideal is a two-sided ideal. The converse is the substance: in the derived model $x \star y = xy^{*}$ with a unit, a two-sided $\star$-ideal is carried to itself by the involution, so it is already an invariant ideal and cannot separate the two notions from inside. The unit does the work, and the argument is the observation that $1 \star i = i^{*}$ places the conjugate of every element of the ideal back in the ideal.

The two **products** behave differently, and this is the second point. The sesquilinear product and the product by juxtaposition impose different conditions on an ideal — $A \star I = AI^{*}$ against $AI$ — so an algebra that is simple for its own product need not be simple for the product by juxtaposition. The invariant ideals are the part the two products share, since a $\ast$-ideal is two-sided for both.

**Setting.** Throughout, $A$ is a unital associative $R$-algebra with a unit $1 \neq 0$, $\varsigma$ is an involution of $R$, and $*$ is a $\varsigma$-semilinear involution of $A$. The sesquilinear product is the derived operation $x \star y = xy^{*}$ of *The Sesquilinear Product*, so that $A$ is a sesqualgebra in the sense of *Sesqualgebras*, and it is the product that the word ideal refers to unless the contrary is said; the unit is used and its use is flagged where it occurs. The product by juxtaposition is the algebra product, the two-sided ideals of which are called **algebra ideals** where the distinction is needed. The $\ast$-ideal, the conjugate image $I^{*}$ and the smallest $\ast$-ideal $I + I^{*}$ through a two-sided ideal are those of *Ideals and Quotients of a Sesqualgebra*; the idempotents, the Hermitian idempotents and the corners $eAe$ are those of *Hermitian Idempotents and the Peirce Decomposition*; the primitive idempotents and the minimal one-sided ideals are those of *Biquaternion Ideals and the Peirce Decomposition* and *List of Rings by Their Idempotents*; and the centre and the zero divisors are those of *The Centre and the Zero Divisors of a Sesqualgebra*.

## Two Notions of Simplicity

### The Definitions

**Definition.** The algebra $A$ is **simple** when its only two-sided $\star$-ideals are $0$ and $A$. It is **invariant-simple** when its only $\ast$-ideals are $0$ and $A$. A $\ast$-ideal is a two-sided algebra ideal $I$ with $I^{*} \subseteq I$, equivalently $I^{*} = I$, in the terminology of *Ideals and Quotients of a Sesqualgebra*.

### Simple Implies Invariant-Simple

**Proposition.** If $A$ is simple then $A$ is invariant-simple.

**Proof.** A $\ast$-ideal is a two-sided ideal, so a proper $\ast$-ideal is a proper two-sided ideal. If the only two-sided ideals are $0$ and $A$, the only $\ast$-ideals are $0$ and $A$. $\square$

**Remark.** The proof uses the definition of the $\ast$-ideal and nothing else, and on its own it is weaker than the equivalence proved next. The obstruction it does not touch is the map $I \mapsto I^{*}$, which sends a two-sided ideal to a two-sided ideal and might a priori send it to a different one; the point of the next theorem is that in the derived model this cannot happen.

### The Two Notions Coincide in the Derived Model

The converse of the proposition needs one computation, and the unit supplies it.

**Lemma.** A $\ast$-ideal is a two-sided $\star$-ideal.

**Proof.** For a $\ast$-stable $I$ one has $A \star I = AI^{*} = AI \subseteq I$ and $I \star A = IA^{*} = IA \subseteq I$, because $I$ is a two-sided algebra ideal. $\square$

**Theorem.** In the derived model $x \star y = xy^{*}$ with a unit $1$, every two-sided $\star$-ideal is stable under the involution; consequently $A$ is invariant-simple if and only if $A$ is simple.

**Proof.** Let $I$ be a two-sided $\star$-ideal. Since $1 \in A$ and $1 \star i = i^{*}$ for $i \in I$, the conjugate of every element of $I$ lies in $A \star I \subseteq I$, so $I^{*} \subseteq I$; applying the involution, which is of order two, gives $I = (I^{*})^{*} \subseteq I^{*}$, hence $I^{*} = I$. With $I$ stable, the two $\star$-conditions read $AI \subseteq I$ and $IA \subseteq I$, so $I$ is a two-sided algebra ideal as well, that is, a $\ast$-ideal. Every two-sided $\star$-ideal is therefore a $\ast$-ideal, and by the lemma the two classes of two-sided ideals coincide. An invariant-simple algebra has no proper $\ast$-ideal, hence no proper two-sided $\star$-ideal, hence is simple; the converse is the proposition. $\square$

**Remark.** The unit is what makes the theorem work: it supplies the single product $1 \star i = i^{*}$ that drags the conjugate into the ideal. In the abstract sesqualgebra of *Ideals and Quotients of a Sesqualgebra*, where the product is not tied to the involution, the corresponding step is unavailable and a two-sided ideal need not be stable; the example of the principal ideal $(x - i)$ there is the witness. The derived model is thus the case in which the second scalar rule is strong enough to close that gap, and the coincidence of the two notions of simplicity is a consequence of the model, not of the definitions.

### Simple for Which Product

By the theorem the two-sided $\star$-ideals are the $\ast$-ideals, so the invariant ideals are common to the two readings; what can differ is the lattice of algebra ideals.

**Example.** The algebra ideals can be strictly more numerous. In $\mathbb{F}_2 \times \mathbb{F}_2$ with the exchange involution the two-sided $\star$-ideals are $0$ and $A$ alone, so the algebra is simple and invariant-simple, while the two-sided algebra ideals are four and include the proper ideals $\mathbb{F}_2 \times 0$ and $0 \times \mathbb{F}_2$. The algebra is therefore simple for its own product and not simple for the product by juxtaposition, which fixes the choice of product in the definition. The computation is that of the commutative case: the two-sided $\star$-ideals are the stable algebra ideals, namely $0$ and $A$, and the algebra ideals of a product of two fields are the four listed.

### The One-Sided Case

**Definition.** A **left $\star$-ideal** is an $R$-submodule $I$ with $A \star I \subseteq I$; a **right $\star$-ideal** has $I \star A \subseteq I$; a **two-sided $\star$-ideal** has both. Since $A \star I = AI^{*}$ and $I \star A = IA^{*}$, these are the conditions $AI^{*} \subseteq I$ and $IA^{*} \subseteq I$.

**Proposition.** In the derived model with a unit, a one-sided $\star$-ideal is stable: if $I$ is a left $\star$-ideal or a right $\star$-ideal then $I^{*} = I$.

**Proof.** For a left $\star$-ideal, $i^{*} = 1 \star i \in A \star I \subseteq I$ for $i \in I$, so $I^{*} \subseteq I$ and hence $I = I^{*}$ as above. For a right $\star$-ideal the same computation is read on the other side: $i^{*} = i^{*} \star 1 \in I \star A \subseteq I$, using $1^{*} = 1$. $\square$

**Remark.** The definitions differ from the algebra ideals by the conjugate on the ideal rather than on the algebra: $I$ is a left $\star$-ideal when $AI^{*} \subseteq I$, not when $AI \subseteq I$. The identities $1 \star i = i^{*}$ and $i^{*} \star 1 = i^{*}$ that stabilise the one-sided ideals are the same ones that drive the theorem above, and they are also what makes the $\ast$-ideals insensitive to the choice of product.

## Minimal Ideals

### The Definition

**Definition.** A nonzero left $\star$-ideal is **minimal** when it contains no other nonzero left $\star$-ideal; the same definition is made for the right ideals and the two-sided ideals.

### Primitive Idempotents

**Recall.** An idempotent $e \neq 0$ is **primitive** when it is not a sum of two nonzero orthogonal idempotents. In a semisimple algebra the primitive idempotents are exactly the idempotents $e$ for which $Ae$ is a minimal left ideal, equivalently $eA$ is a minimal right ideal, equivalently the corner $eAe$ is a division algebra, in the form of *Biquaternion Ideals and the Peirce Decomposition*.

**Theorem.** Let $A$ be semisimple and let $e$ be a primitive idempotent. Then $Ae$ is a minimal left ideal and the conjugate image $(Ae)^{*} = e^{*}A$ is a minimal right ideal, and the involution matches the two collections: it sends the minimal left ideal $Ae$ to the minimal right ideal $e^{*}A$, and the minimal right ideal $eA$ to the minimal left ideal $Ae^{*}$.

**Proof.** That $Ae$ is minimal is the recall. Since $*$ is bijective and anti-multiplicative, $(Ae)^{*} = e^{*}A^{*} = e^{*}A$, which is a minimal right ideal by the right-hand form of the recall applied to the primitive idempotent $e^{*}$. The last statement is the same computation with $e$ and $e^{*}$ exchanged. $\square$

**Corollary.** If $e$ is a Hermitian primitive idempotent then $(Ae)^{*} = eA$, so the minimal left ideal $Ae$ and the minimal right ideal $eA$ are conjugate, and the corner $eAe$ is a $\ast$-stable subalgebra that is a division algebra.

**Proof.** For a Hermitian $e$ one has $(Ae)^{*} = eA$ with $e^{*} = e$, the corner is stable by *Hermitian Idempotents and the Peirce Decomposition*, and it is a division algebra by the recall. $\square$

### Minimal Two-Sided Ideals and Central Idempotents

The two-sided case runs along the centre.

**Definition.** An idempotent $z$ is **central** when it commutes with every element. A central idempotent that is primitive as an idempotent is a **central primitive idempotent**; it is the idempotent of a simple direct factor.

**Theorem.** Let $z$ be a central idempotent. Then $Az$ and $A(1-z)$ are two-sided ideals with $A = Az \oplus A(1-z)$, and $Az$ is a $\ast$-ideal if and only if $z$ is Hermitian.

**Proof.** The decomposition is the Peirce decomposition relative to a central idempotent, in *Unital Algebras*, §*Idempotents and the Peirce Decomposition*. Since $z$ is central so is $z^{*}$, and $(Az)^{*} = z^{*}A = Az^{*}$. Suppose $Az = Az^{*}$. Then $z \in Az^{*}$, and every element of $Az^{*}$ is annihilated by $1 - z^{*}$ since $z^{*}$ is central and idempotent; hence $z = z z^{*}$, and symmetrically $z^{*} = z^{*} z$. As $z$ and $z^{*}$ are both central they commute, so $z = z z^{*} = z^{*} z = z^{*}$. Conversely $z^{*} = z$ plainly gives $Az^{*} = Az$. $\square$

**Corollary.** Let $A$ be semisimple. The minimal two-sided ideals of $A$ are the ideals $Az$ generated by the central primitive idempotents $z$, and they are $\ast$-ideals exactly when those idempotents are Hermitian. A $\star$-simple algebra has no proper nonzero two-sided $\star$-ideal, so its only minimal two-sided $\star$-ideal is $A$ itself; it may still have proper two-sided algebra ideals.

**Proof.** The generation of the simple direct factors by central primitive idempotents is the standard structure of a semisimple algebra, recorded in *List of Rings by Their Idempotents*. The stability criterion is the theorem above. $\square$

**Remark.** For a noncentral primitive idempotent $e$, the ideal $AeA$ is a nonzero two-sided algebra ideal, and in an algebra with no proper two-sided algebra ideal it is all of $A$; in general it may be proper, which is a way in which a $\star$-simple algebra can fail to be simple for the algebra product. The left ideal $Ae$ is proper nevertheless, and it stays inside the two-sided lattice only by being one-sided: it is exactly one-sidedness, not size, that lets a minimal ideal escape a simplicity condition stated two-sidedly.

## The Centre and the Zero Divisors

### The Centre

**Theorem.** If $A$ is unital with $1 \neq 0$ and has no proper two-sided algebra ideal, then the centre $Z(A)$ is a field.

**Proof.** The centre is a commutative ring with $1$. For $0 \neq z \in Z(A)$ the set $AzA$ is a nonzero two-sided algebra ideal, so $AzA = A$ and $1 = \sum_i a_i z b_i$ for finitely many $a_i, b_i \in A$. Since $z$ is central, $1 = z \sum_i a_i b_i = \bigl(\sum_i a_i b_i\bigr) z$, so $u = \sum_i a_i b_i$ is a two-sided inverse of $z$. The inverse is central: for any $x$ one has $x u = u z x u = u x z u = u x$, using $z u = u z = 1$. Hence every nonzero central element is a unit with central inverse, so $Z(A)$ is a field. $\square$

**Remark.** The hypothesis is simplicity for the product by juxtaposition, and it is strictly stronger than simplicity for $\star$. The algebra $\mathbb{F}_2 \times \mathbb{F}_2$ with the exchange involution is $\star$-simple and invariant-simple, and its centre is $\mathbb{F}_2 \times \mathbb{F}_2$, not a field; the point is that $\mathbb{F}_2 \times 0$ is a proper two-sided algebra ideal even though it is not a $\star$-ideal. For an algebra that is simple for the product by juxtaposition the centre is a field, and it may be larger than the scalars: $M_n(\mathbb{C})$ has centre $\mathbb{C}$, the quaternions have centre $\mathbb{R}$, and an algebra over $R$ whose centre is $R$ is central, in the sense of *Central Simple Algebras and the Brauer Group*.

### The Zero Divisors

**Definition.** An element $x \neq 0$ is a **zero divisor** when there is $y \neq 0$ with $xy = 0$ or $yx = 0$; the one-sided and the two-sided classes and their pairing by the involution are those of *The Centre and the Zero Divisors of a Sesqualgebra*.

**Proposition.** An algebra with no proper two-sided algebra ideal need not be a division algebra and may have zero divisors, and a commutative one is a field and has none.

**Proof.** For the commutative case, the centre of the commutative algebra is the algebra itself, so the theorem above makes it a field. For the failure in the noncommutative case, the matrix model below exhibits two Hermitian idempotents with product $0$. $\square$

**Remark.** Simplicity constrains the two-sided ideals and says nothing about the one-sided ones. A zero divisor is the shadow of a proper one-sided ideal: if $xy = 0$ with $x \neq 0$ and $y \neq 0$, then $x$ is not a unit, and the left annihilator of $y$ is a nonzero left ideal which is proper because it omits $1$. A simple algebra may therefore be a full matrix algebra rather than a division algebra, and the one-sided ideals, not the two-sided ones, are what separate the two cases.

## Examples

### The Matrices with the Conjugate Transpose

**Example.** Let $A = M_n(\mathbb{C})$ with the conjugate transpose $*$, so that $x \star y = xy^{*}$. The algebra has no proper two-sided algebra ideal, being central simple over $\mathbb{C}$ by *Central Simple Algebras and the Brauer Group*; hence it is invariant-simple, and hence simple for the sesquilinear product by the coincidence theorem. The Hermitian idempotents are the matrices with $P^{2} = P = P^{*}$; a minimal left ideal is $Ae$ for $e$ a primitive idempotent, of which $AE_{11}$ is one, and the involution sends $AE_{11}$ to the minimal right ideal $E_{11}A$. For $n \geq 2$ the algebra is not a division algebra: $E_{11}$ and $E_{22}$ are Hermitian idempotents with $E_{11}E_{22} = 0$, so both are zero divisors. The central idempotents are $0$ and $1$ alone, the centre being $\mathbb{C}I_n$, which is why the only two-sided $\star$-ideals are the two trivial ones.

### The Quaternions

**Example.** Let $A = \mathbb{H}$ with the quaternion conjugation and $R = \mathbb{R}$. The algebra is a division algebra, so its only idempotents are $0$ and $1$ by *Hermitian Idempotents and the Peirce Decomposition*; it has no zero divisors and no proper one-sided ideal, hence no proper two-sided ideal. It is therefore simple and invariant-simple, and its only $\ast$-ideals are $0$ and $\mathbb{H}$. The centre is $\mathbb{R}$, so the algebra is central over $\mathbb{R}$; the sesquilinear product $x \star y = x\bar y$ is the derived operation of *The Sesquilinear Product* for this involution, and it is not associative.

### The Biquaternions

**Example.** Let $A = \mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ with $R = \mathbb{C}$, $\varsigma$ the conjugation and $*$ the involution of *Introduction to the General Plain Sesqualgebra of Biquaternions*, which conjugates the coefficient and negates $e_1, e_2, e_3$ while fixing $e_0$. The algebra is simple by *Biquaternion Ideals and the Peirce Decomposition*, and like the matrices it is not a division algebra. The idempotents
$$
\tilde\Pi_1 = \tfrac12(e_0 + i e_3), \qquad \tilde\Pi_2 = \tfrac12(e_0 - i e_3)
$$
of that article are primitive and noncentral, and both are Hermitian for this involution, since $(i e_3)^{*} = e_3^{*} i^{*} = (-e_3)(-i) = i e_3$. They generate the minimal left ideals $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}\tilde\Pi_2$, whose two-sided ideal is all of $\mathbb{B}$ because the algebra is simple. The involution sends $\mathbb{B}\tilde\Pi_j$ to the conjugate image $\tilde\Pi_j\mathbb{B}$, which is a minimal right ideal and a different set: a minimal left ideal $Ae$ is stable only when the idempotent is both Hermitian and central, and $\tilde\Pi_j$ is not central. The centre is $\mathbb{C}$, so the algebra is central over $\mathbb{C}$ but not over $\mathbb{R}$.

## Summary

A sesqualgebra is simple when its only two-sided ideals for its own product $\star$ are $0$ and $A$, and invariant-simple when its only $\ast$-ideals are $0$ and $A$. Simplicity implies invariant-simplicity, because a $\ast$-ideal is a two-sided ideal, and in the derived model with a unit the two notions coincide: the product $1 \star i = i^{*}$ forces every two-sided $\star$-ideal to be stable, hence the two-sided $\star$-ideals are exactly the $\ast$-ideals. The two products nevertheless impose different two-sided conditions, and they can therefore have different lattices: the simplest witness is $\mathbb{F}_2 \times \mathbb{F}_2$ with the exchange involution, where the two-sided $\star$-ideals are $0$ and $A$ while the two-sided algebra ideals are four. The one-sided $\star$-ideals carry a conjugate where the algebra ideals do not, $A \star I = AI^{*}$ against $AI$, and they too are stable in the derived model. The minimal left ideals of a semisimple algebra are the ideals $Ae$ generated by the primitive idempotents, the involution sending the minimal left ideal $Ae$ to the minimal right ideal $e^{*}A$; for a Hermitian primitive idempotent the conjugate is $eA$ and the corner $eAe$ is a stable division algebra. The minimal two-sided ideals are generated by the central primitive idempotents, and such an ideal is a $\ast$-ideal exactly when its idempotent is Hermitian. The centre of an algebra with no proper two-sided algebra ideal is a field, and such an algebra may still have zero divisors: $M_n(\mathbb{C})$ with the conjugate transpose has zero divisors and only the two trivial $\ast$-ideals, whereas $\mathbb{H}$ is a division algebra with none. The worked cases are the matrices with the conjugate transpose, the quaternions with the quaternion conjugation, and the biquaternions, whose centre is $\mathbb{C}$ and which is not a division algebra.

## Summary of Notation

| symbol | meaning |
|---|---|
| $x \star y = xy^{*}$ | the sesquilinear product, the derived operation of the algebra |
| $I^{*}$ | the conjugate image of an ideal, $I^{*} = \{x^{*} : x \in I\}$ |
| $I + I^{*}$ | the smallest $\ast$-ideal containing the two-sided ideal $I$ |
| simple | the only two-sided $\star$-ideals are $0$ and $A$ |
| invariant-simple | the only $\ast$-ideals are $0$ and $A$ |
| two-sided $\star$-ideal $\iff$ $\ast$-ideal | the coincidence in the derived model with a unit, from $1 \star i = i^{*}$ |
| $A \star I = AI^{*}$, $I \star A = IA^{*}$ | the left and right $\star$-ideal conditions |
| minimal left $\star$-ideal | a nonzero left $\star$-ideal containing no other nonzero one |
| primitive idempotent | an idempotent that is not a sum of two nonzero orthogonal idempotents |
| $e$ primitive $\iff$ $Ae$ minimal | the minimal left ideals of a semisimple algebra |
| $(Ae)^{*} = e^{*}A$ | the involution sends a minimal left ideal to a minimal right ideal |
| $eAe$ a division algebra | the corner of a primitive idempotent |
| central idempotent $z$ | $z$ commutes with every element; $A = Az \oplus A(1-z)$ |
| $Az$ a $\ast$-ideal $\iff$ $z^{*} = z$ | the stability of the ideal of a central idempotent |
| $Z(A)$ | the centre, a field when there is no proper two-sided algebra ideal |
| zero divisor | a nonzero $x$ with $xy = 0$ or $yx = 0$ for some nonzero $y$ |

## Further Reading

- T. Y. Lam, *A First Course in Noncommutative Rings* (Graduate Texts in Mathematics 131, Springer, 2001), for the simple rings, the minimal one-sided ideals, the primitive idempotents, and the structure of a semisimple ring as a product of simple rings.
- Richard S. Pierce, *Associative Algebras* (Graduate Texts in Mathematics 88, Springer, 1982), for the idempotents, the central idempotents that cut direct factors, and the corners of a primitive idempotent.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the invariant ideals, the ideals preserved by an involution, and the simple rings with involution.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the simple algebras with involution, the Hermitian idempotents that generate invariant minimal ideals, and the central simple case.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the one-sided ideals, the primitive idempotents and the minimal ideals in the structure theory of rings.
