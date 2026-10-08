# __Direct Products of Sesqualgebras__

## Introduction

The direct product of two sesqualgebras is the module $A \times B$ with the componentwise product and the componentwise involution. It is a sesqualgebra over the same datum, and its two components are cut out by two central Hermitian idempotents. This article reads that construction: the componentwise structure and its scalar rules, the idempotents that cut the product, the criterion that a splitting of a sesqualgebra into two two-sided ideals comes from a central idempotent, the Hermitian condition that makes the two ideals stable under the involution and lets that involution descend to the factors, and the reason the direct product is the product of the category and not its coproduct.

The construction is the analogue for sesqualgebras of *Tensor Products of Algebras* in the bilinear layer, and it is the simplest way of manufacturing new sesqualgebras out of old ones: no quotient, no completion and no universal property is needed, and every statement is componentwise. Its one genuinely sesquilinear feature is the involution: the component idempotents are Hermitian for free because the unit is Hermitian, but the central idempotents that cut a splitting of an arbitrary sesqualgebra need not be, and it is exactly the Hermitian central ones that cut the splittings for which the involution descends to the two factors.

The setting is that of *Sesqualgebras*: $R$ is a commutative ring with $1$, $\varsigma$ is an involution of $R$, and a sesqualgebra over $(R,\varsigma)$ is an $R$-module $A$ with a product that is $R$-linear in the first variable and $\varsigma$-semilinear in the second. The datum is part of the structure, and both factors of a direct product are taken over the same datum. The involution of the algebra, the two halves and the derived operation are *Hermitian and Skew-Hermitian Elements* and *The Sesquilinear Product*; the idempotents and the Peirce decomposition of the bilinear case are *Unital Algebras*, §*Idempotents and the Peirce Decomposition*; the Hermitian idempotents are *Hermitian Idempotents and the Peirce Decomposition*; the two-sided ideals are *Ideals and Quotients of a Sesqualgebra*; and the comparison with the tensor product and the free product is *Tensor Products of Algebras*.

---

## The Componentwise Structure

### The Product and the Involution

**Definition.** Let $A$ and $B$ be sesqualgebras over the same datum $(R,\varsigma)$. Their **direct product** $A \times B$ is the $R$-module of the pairs $(a,b)$ with the componentwise product

$$
(a,b)(c,d) = (ac, bd)
$$

and the componentwise involution

$$
(a,b)^{*} = (a^{*}, b^{*}) .
$$

**Theorem.** $A \times B$ is a sesqualgebra over $(R,\varsigma)$, its product is $R$-linear in the first variable and $\varsigma$-semilinear in the second, and its involution is a $\varsigma$-semilinear involution of order two. The derived operation is componentwise, $(a,b) \star (c,d) = (a \star c, b \star d)$.

**Proof.** The product is additive in each variable because the two products are, and it is associative because the two products are. For the scalars, let $\lambda \in R$ and $(a,b), (c,d) \in A \times B$. Then

$$
\lambda (a,b) = (\lambda a, \lambda b) , \qquad (a,b)(\lambda(c,d)) = (a,b)(\lambda c, \lambda d) = \bigl(a(\lambda c),\, b(\lambda d)\bigr) = \bigl(\varsigma(\lambda)ac,\, \varsigma(\lambda)bd\bigr) ,
$$

using the first scalar rule in $A$ and in $B$, so the second rule of *Sesqualgebras* holds componentwise and $A \times B$ is a sesqualgebra. The involution is additive, of order two and anti-multiplicative componentwise:

$$
\bigl((a,b)(c,d)\bigr)^{*} = (ac, bd)^{*} = \bigl((ac)^{*}, (bd)^{*}\bigr) = (c^{*}a^{*}, d^{*}b^{*}) = (c,d)^{*}(a,b)^{*} ,
$$

and it is $\varsigma$-semilinear because $\bigl(\lambda(a,b)\bigr)^{*} = (\varsigma(\lambda)a^{*}, \varsigma(\lambda)b^{*}) = \varsigma(\lambda)(a,b)^{*}$. The derived operation is $x \star y = xy^{*}$ computed in each component. $\square$

**Remark.** Nothing in the proof mixes the two components, and the whole theorem is the observation that the axioms of *Sesqualgebras* are equational and are therefore inherited by a componentwise product. The direct product is the cheapest construction of the category and the only one of the three classical products, the direct product, the tensor product and the free product, that needs no universal property at all.

### The Projections

**Proposition.** The two projections $\pi_{1}(a,b) = a$ and $\pi_{2}(a,b) = b$ are morphisms of sesqualgebras over the same datum, they commute with the involution, and they are the two components of the identity of $A \times B$.

**Proof.** Each projection is additive, multiplicative and $R$-linear, since the operations are componentwise, and each commutes with the involution because $\pi_{i}\bigl((a,b)^{*}\bigr) = \pi_{i}(a^{*}, b^{*}) = (\pi_{i}(a,b))^{*}$; hence each is a $*$-homomorphism. The pair $(\pi_{1},\pi_{2})$ is the identity in the sense that an element is recovered from its two components. $\square$

**Remark.** The direct product is characterised by these projections: a morphism $f : C \to A \times B$ is the same datum as the pair of morphisms $(\pi_{1} \circ f, \pi_{2} \circ f)$, and this is the universal property that makes $A \times B$ the product of $A$ and $B$ in the category of the sesqualgebras over $(R,\varsigma)$. The characterisation is by the maps *into* $A \times B$, and that is what the coproduct does not have: the coproduct is characterised by the maps *out of* it, and it is a different object, as the next section records.

## The Component Idempotents

### The Idempotents of the Product

**Definition.** In $A \times B$ write

$$
e_{1} = (1,0) , \qquad e_{2} = (0,1).
$$

**Proposition.** The elements $e_{1}$ and $e_{2}$ are idempotents, they are orthogonal, $e_{1}e_{2} = e_{2}e_{1} = 0$, they are central, and they are Hermitian, with $e_{1} + e_{2} = 1$.

**Proof.** $e_{1}^{2} = (1,0)^{2} = (1,0) = e_{1}$ and $e_{2}^{2} = e_{2}$; $e_{1}e_{2} = (1,0)(0,1) = (0,0)$ and $e_{2}e_{1} = 0$; the centre of $A \times B$ is $Z(A) \times Z(B)$, so each $e_{i}$ is central because $1$ is central in its factor and $0$ is central in the other; and $e_{1}^{*} = (1^{*}, 0^{*}) = (1,0) = e_{1}$, likewise for $e_{2}$, because the unit is Hermitian by *Units and the Unitary Elements*, §*The Unit is Hermitian*. $\square$

**Remark.** The idempotents are Hermitian for the same reason the unit is: the involution fixes $1$, and it therefore fixes $(1,0)$ and $(0,1)$. This is not an accident of the construction but the reason the construction is compatible with the involution at all, and it is what makes the two components of the product genuine sesqualgebras and not merely algebras.

### The Two Halves of the Product

**Proposition.** The involution of $A \times B$ acts componentwise on the two halves, so that

$$
H(A \times B) = H(A) \times H(B) , \qquad S(A \times B) = S(A) \times S(B) .
$$

**Proof.** An element $(a,b)$ is fixed by the involution exactly when $a^{*} = a$ and $b^{*} = b$, that is exactly when $a \in H(A)$ and $b \in H(B)$; the skew-Hermitian case is the same computation with a minus sign. $\square$

**Remark.** The Hermitian Jordan algebra of *The Hermitian Jordan Algebra* and the unitary Lie algebra of *The Unitary Lie Algebra* are therefore the direct products of the corresponding objects of the factors, $J(A \times B) = J(A) \times J(B)$ and $\mathfrak{u}(A \times B) = \mathfrak{u}(A) \times \mathfrak{u}(B)$, with the componentwise products. The example of the complex matrices below is the case $M_n(\mathbb{C}) \oplus M_m(\mathbb{C})$ of that statement.

## The Splitting into Ideals

### The Criterion

**Theorem.** Let $A$ be a unital sesqualgebra. A decomposition $A = I \oplus J$ into two two-sided ideals is the same datum as a central idempotent $e \in A$, through $I = eA$ and $J = (1-e)A$; the idempotents $e$ and $1 - e$ are orthogonal, they sum to $1$, and they give the same splitting with the two ideals exchanged.

**Proof.** If $e$ is a central idempotent then $eA$ and $(1-e)A$ are two-sided ideals, they are additive subgroups whose sum is $A$ because $x = ex + (1-e)x$, and their intersection is zero because $x \in eA \cap (1-e)A$ gives $x = ey = (1-e)z$, hence $x = ex = e(1-e)z = 0$; the ideals are distinct from $A$ exactly when $e \neq 1$. Conversely, if $A = I \oplus J$ with $I$ and $J$ two-sided ideals, write $1 = e + f$ with $e \in I$ and $f \in J$; then $e = e \cdot 1 = e^{2} + ef$ with $e^{2} \in I$ and $ef \in I \cap J = 0$, so $e = e^{2}$, and likewise $f = f^{2}$. For $x \in I$ one has $x = x \cdot 1 = xe + xf$ with $xe \in I$ and $xf \in J$, whence $xe = x$ and $xf = 0$ by the directness of the sum; similarly $ex = x$. Thus $I = eA$, $J = fA$, and the centrality of $e$ follows from $xe = ex$ for every $x \in A$. $\square$

**Remark.** The criterion is the one of *Unital Algebras*, §*Idempotents and the Peirce Decomposition*, and it needs only the unit and the two-sidedness of the ideals. It distinguishes the splittings of an algebra into two ideals from all its idempotents: an idempotent that is not central gives a Peirce decomposition of *Hermitian Idempotents and the Peirce Decomposition* and not a splitting into two ideals, and the central idempotents are exactly the ones that split the algebra.

### The Descent of the Involution

**Theorem.** Let $A$ be a unital sesqualgebra and let $A = I \oplus J$ come from a central idempotent $e$. Then the involution carries $I$ and $J$ to themselves if and only if $e$ is Hermitian, $e^{*} = e$; and when $e$ is Hermitian the two ideals are $*$-ideals, the involution restricts to each, and the factors $eA$ and $(1-e)A$ are sesqualgebras over the same datum with $A \cong eA \times (1-e)A$.

**Proof.** Suppose $e^{*} = e$. For $x = ea \in I = eA$ one has $x^{*} = (ea)^{*} = a^{*}e^{*} = a^{*}e = e\,a^{*}$ by the centrality of $e$, so $x^{*} \in eA = I$ and $I^{*} \subseteq I$; the same computation with $1 - e$ gives $J^{*} \subseteq J$. Conversely, suppose $I^{*} \subseteq I$ and $J^{*} \subseteq J$. Then $e \in I$ gives $e^{*} \in I$, and $1 - e \in J$ gives $(1-e)^{*} \in J$; the involution is additive with $1^{*} = 1$, so $1 = e^{*} + (1-e)^{*}$ is a decomposition of $1$ with the first term in $I$ and the second in $J$. But $1 = e + (1-e)$ is the same decomposition, and the sum $I \oplus J$ is direct, so the components are unique and $e^{*} = e$. When $e$ is Hermitian the two ideals are carried to themselves, each is closed under the restricted product because $e$ is central, and the map $x \mapsto (ex, (1-e)x)$ identifies $A$ with $eA \times (1-e)A$, the involution of $A$ corresponding to the componentwise involution because $e$ and $1 - e$ are fixed by it. $\square$

**Remark.** The Hermitian hypothesis on the idempotent is the whole difference from the bilinear case, and it is not automatic. In the bilinear layer a central idempotent suffices to split the algebra, since there is no involution to respect, as in *Unital Algebras*, §*Idempotents and the Peirce Decomposition*; here a splitting that is to be a direct product of sesqualgebras must be cut by a central **Hermitian** idempotent, otherwise the involution does not descend to the factors and exchanges them instead. The example of the exchange involution below is the smallest case in which a central idempotent fails to be Hermitian.

## The Failure to be a Coproduct

**Proposition.** The direct product is the product of the category of the sesqualgebras over $(R,\varsigma)$ and not its coproduct. For noncommutative factors the coproduct is the free product, and the tensor product is universal only for pairs of maps with commuting images.

**Proof.** The projections exhibit $A \times B$ as the product, and the universal property of the product is the one of the proposition on the projections above. The coproduct carries the maps into a third object, and it is the free product in the category of the associative algebras by *Tensor Products of Algebras*, §*The Universal Property*, with the tensor product as its quotient by the commuting relations; none of these is a componentwise structure. $\square$

**Remark.** The three constructions are distinguished by what they allow: the direct product computes in both factors at once and has no relation to the tensor product in general; the tensor product imposes the relation between the two factors; and the free product imposes none. The comparison is the table

| construction | the product of the pair | the coproduct |
|---|---|---|
| direct product $A \times B$ | $(a,b)(c,d) = (ac,bd)$ | no |
| tensor product $A \otimes_{R} B$ | $(a \otimes b)(a' \otimes b') = aa' \otimes bb'$ | for commuting images |
| free product $A \sqcup B$ | no componentwise form | yes |

and only the direct product is componentwise, which is why only the direct product is characterised by the two central idempotents $e_{1}$ and $e_{2}$.

## Worked Cases

### The Ring $R \times R$ with the Exchange Involution

**Theorem.** Let $A = R \times R$ with the componentwise product and the **exchange involution** $(a,b)^{*} = (b,a)$, over the datum $(R,\mathrm{id})$. Then the idempotent $e = (1,0)$ is central, it is not Hermitian, and

$$
e^{*} = (0,1) = 1 - e \neq e .
$$

**Proof.** The element $e = (1,0)$ is idempotent and central, its complement is $1 - e = (0,1)$, and the exchange involution swaps the two components, so $e^{*} = (0,1) \neq e$. The involution is $(R,\mathrm{id})$-linear and of order two, and it is an anti-automorphism of the componentwise product. $\square$

**Remark.** The example is the smallest in which a central idempotent fails to be Hermitian, and it shows that the two conditions of the descent theorem are independent. The split $R \times R = I \oplus J$ with $I = eR$ and $J = (1-e)R$ is a splitting into two two-sided ideals that the involution does not preserve: it carries $I$ to $J$ and $J$ to $I$, so the two factors are exchanged and the involution does not restrict to either. It is also the case in which the exchange involution and the componentwise involution on the same underlying algebra have different Hermitian parts: for the componentwise involution both $e$ and $1-e$ are Hermitian, while for the exchange involution neither is, and the Hermitian elements are the diagonal pairs $(a,a)$.

**Remark.** The same computation in the field $\mathbb{C} \times \mathbb{C}$ with the exchange involution shows that the Hermitian part can be smaller than expected: $H(\mathbb{C} \times \mathbb{C})$ is the diagonal $\{(z,z)\}$, isomorphic to $\mathbb{C}$ rather than to $\mathbb{C} \times \mathbb{C}$, and the involution fixes the diagonal pointwise while exchanging the two factors. This is the reason the Hermitian condition is stated on the idempotent and not on the splitting: it is the idempotent that decides whether the splitting survives the involution.

### Two Involutive Algebras

**Proposition.** Let $A$ and $B$ be sesqualgebras over the same datum, with their involutions. Then the componentwise involution of $A \times B$ is the only involution of that algebra that restricts to the given involution of each factor and fixes the two component idempotents.

**Proof.** An involution that fixes $e_{1}$ and $e_{2}$ and restricts to the given involutions must send $(a,b) = ae_{1} + be_{2}$ to $a^{*}e_{1} + b^{*}e_{2} = (a^{*}, b^{*})$, which is the componentwise involution. $\square$

**Remark.** The two component involutions are therefore the two restrictions of one involution, and the direct product is the construction that assembles two involutive algebras into one without twisting either. This is what separates it from the tensor product: the tensor product carries the involution $x \otimes y \mapsto x^{*} \otimes y^{*}$ and its own questions of compatibility, whereas the direct product carries the two involutions side by side.

### The Complex Matrices

For $A = M_n(\mathbb{C})$ and $B = M_m(\mathbb{C})$ with the conjugate transpose, the direct product $A \times B$ is isomorphic to the algebra of the block-diagonal matrices $\mathrm{diag}(U,V)$ of the two sizes, with the conjugate transpose acting on each block, and its component idempotents are the two block projections of the pair $(1,0)$ and $(0,1)$. Its Hermitian part is the pairs of Hermitian matrices of the two sizes and its skew-Hermitian part the pairs of skew-Hermitian ones. Each factor is simple, so the centre of $A \times B$ is the algebra of the pairs of scalar matrices and the central idempotents are only $(0,0)$, $(1,0)$, $(0,1)$ and $(1,1)$: the central Hermitian idempotents are exactly the component idempotents, and the splittings they cut are the two that recover the factors, $A \times B = (A \times 0) \oplus (0 \times B)$. The remaining Hermitian idempotents are the pairs of orthogonal projections, and a general pair such as $\bigl(\mathrm{diag}(1,0,\dots,0), \mathrm{diag}(1,0,\dots,0)\bigr)$ is idempotent and Hermitian and **not** central: it does not cut a direct product, it gives the Peirce decomposition of *Hermitian Idempotents and the Peirce Decomposition*, and this is exactly the distinction that the criterion above draws.

## Summary

The direct product $A \times B$ of two sesqualgebras over the same datum is the module of the pairs with the componentwise product and the componentwise involution, a sesqualgebra over that datum, with componentwise derived operation. It is characterised by the two projections, it is the product of the category and not its coproduct, and its two components are cut by the central Hermitian idempotents $e_{1} = (1,0)$ and $e_{2} = (0,1)$, which are Hermitian because the unit is. The two halves of the product are the products of the two halves, $H(A \times B) = H(A) \times H(B)$ and $S(A \times B) = S(A) \times S(B)$, and the Hermitian Jordan algebra and the unitary Lie algebra are the direct products of the corresponding objects of the factors.

A splitting $A = I \oplus J$ of a unital sesqualgebra into two two-sided ideals is the same datum as a central idempotent, and the involution descends to the two ideals exactly when that idempotent is Hermitian, in which case $A \cong eA \times (1-e)A$ as sesqualgebras. This Hermitian condition is the whole difference from the bilinear theory of *Unital Algebras*, and it is not automatic: for $R \times R$ with the exchange involution the idempotent $(1,0)$ is central and not Hermitian, and the involution exchanges the two factors instead of descending to them.

## Summary of Notation

| symbol | meaning |
|---|---|
| $A \times B$ | the direct product, the pairs with the componentwise product |
| $(a,b)(c,d) = (ac,bd)$ | the componentwise product |
| $(a,b)^{*} = (a^{*}, b^{*})$ | the componentwise involution |
| $\pi_{1}, \pi_{2}$ | the two projections, the components of the identity |
| $e_{1} = (1,0)$, $e_{2} = (0,1)$ | the component idempotents, central and Hermitian |
| $H(A \times B) = H(A) \times H(B)$ | the Hermitian part of the product |
| $S(A \times B) = S(A) \times S(B)$ | the skew-Hermitian part of the product |
| $A = I \oplus J$ | a splitting into two two-sided ideals |
| $e$ central idempotent | the datum of the splitting, $I = eA$, $J = (1-e)A$ |
| $e^{*} = e$ | the Hermitian condition that lets the involution descend |
| $(a,b)^{*} = (b,a)$ | the exchange involution of $R \times R$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the direct product of algebras, the product in a category of algebras and the projections.
- Serge Lang, *Algebra* (Springer, third edition, 2002), for the direct product and the decomposition of a ring by central idempotents.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, second edition, 1992), for the decomposition of a ring by a complete family of orthogonal central idempotents.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the involutions of a direct product and the central idempotents fixed by them.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involution of a product of algebras and the descent to the factors.
- The companion articles of this series: *Sesqualgebras*, *Ideals and Quotients of a Sesqualgebra*, *Hermitian Idempotents and the Peirce Decomposition*, *The Hermitian Jordan Algebra*, *The Unitary Lie Algebra*, *Tensor Products of Algebras* and *Unital Algebras*.
