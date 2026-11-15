# __The Ternary Product and the Associator of the Complex Space__

## Introduction

The plain product of the complex field is associative, and the sesquilinear product is not. The failure is small and exact: the two groupings of three factors differ by the factor $\bar Q_3-Q_3$. A multiplication that fails to be associative carries a ternary product in place of the missing associativity, and the ternary product of the complex space is $\{Q_1,Q_2,Q_3\}=Q_1\bar Q_2Q_3$, the first grouping followed by the multiplication by the third slot.

The article computes the associator, derives the ternary product from it, proves the two symmetries, the contractions, the Jordan triple identity, and the associator's confinement to the sesquilinear shape. It closes with the comparison to the biquaternion algebra, where the identity holds too but the associator is not confined.

The two binary products are *The Two Products of the Complex Space*; the general passage from an associator to a ternary product is *The Sesquilinear Associator and the Ternary Product*, and the axioms of the structure are *Algebraic J\*-Algebras*. The plain multiplication of the field is *Complex Algebra*. The associator of the biquaternion sesqualgebra is *The Ternary Product and the Associator of the Biquaternion Sesqualgebra*.

**Interpretation.** The element is $Q_1=q_1+iq'_1$, with real coordinates, and the further elements are $Q_2,Q_3,Q_4,Q_5,Q_6$, written the same way. The conjugation is the bar, and the Hermitian conjugation is the same map, ${}^{*}=\bar{\cdot}$. The associator is written with a bracket and the ternary product with braces; a bracket is never an element.

## The Failure of Associativity

**Definition.** The **associator** of the sesquilinear product is

$$
[Q_1,Q_2,Q_3]=(Q_1\bar Q_2)\bar Q_3-Q_1\overline{(Q_2\bar Q_3)}.
$$

**Proposition.** The associator is $Q_1\bar Q_2(\bar Q_3-Q_3)$, that is, $-2i(\operatorname{Im}Q_3)Q_1\bar Q_2$.

*Proof.* Expand the second grouping: $Q_2\bar Q_3$ is a complex number, its conjugate is $\bar Q_2Q_3$, so $Q_1\overline{(Q_2\bar Q_3)}=Q_1\bar Q_2Q_3$. The first grouping is $(Q_1\bar Q_2)\bar Q_3$. The difference is $Q_1\bar Q_2(\bar Q_3-Q_3)$, and $\bar Q_3-Q_3=-2i\operatorname{Im}Q_3$.

**Corollary.** The associator vanishes for every pair $(Q_1,Q_2)$ when the third slot is real, and it vanishes for a non-real third slot exactly when $Q_1\bar Q_2=0$, that is, when $Q_1=0$ or $Q_2=0$.

*Proof.* The factor $\bar Q_3-Q_3$ is zero exactly for real $Q_3$, and the algebra has no zero divisor, so the product $Q_1\bar Q_2(\bar Q_3-Q_3)$ vanishes exactly when one factor does.

**Remark (the plain product has no associator).** The failure is created by the conjugation in the second slot. The plain product $(Q_1Q_2)Q_3=Q_1(Q_2Q_3)$ is associative, and its associator vanishes identically. The two products therefore differ on the one law that generates the whole of this article, and the difference is the conjugation, not the dimension.

**Remark (the size of the failure).** The associator is a single term: the product $Q_1\bar Q_2$ multiplied by the real scalar $-2\operatorname{Im}Q_3$ and by $i$. It is not a sum of two products of different shapes, and it is not the commutator of anything. A multiplication whose associator is one term is as close to associative as a non-associative multiplication can be, and the rest of the article is the exploitation of that.

## The Ternary Product

**Definition.** The **ternary product** is

$$
\{Q_1,Q_2,Q_3\}=(Q_1\bar Q_2)Q_3 .
$$

**Remark (why this and not another).** The binary product has two groupings of three factors and they differ; the ternary product is the first grouping completed by the plain multiplication. It is the construction of *The Sesquilinear Associator and the Ternary Product*: for a derived operation $Q_1\star Q_2=Q_1\bar Q_2$ the triple is $(Q_1\star Q_2)\star Q_3^{*}$, and on $\mathbb{C}$ the last factor $Q_3^{*}$ is $\bar Q_3$, whose conjugate is $Q_3$ again. The triple is therefore a product of three elements of the algebra in the plain multiplication, with the middle one conjugated.

**Proposition (parity).** The ternary product is additive in each variable, $\mathbb{C}$-linear in the first and the third slots, and conjugate-linear in the middle slot.

*Proof.* Read the definition: a scalar multiplying $Q_1$ or $Q_3$ passes through the plain multiplication, and a scalar multiplying $Q_2$ meets the bar.

## The Two Symmetries

### The Outer Symmetry

**Proposition.** The ternary product is symmetric in its two outer slots: $\{Q_1,Q_2,Q_3\}=\{Q_3,Q_2,Q_1\}$.

*Proof.* Both sides equal $Q_1\bar Q_2Q_3$, the multiplication being commutative.

**Remark.** This symmetry is the one the general article calls the plain symmetry, and it fails on any non-commutative algebra. On $\mathbb{B}$ it fails at $(\vec e_x,\vec e_y,e_t)$, where the two sides are $-\vec e_z$ and $\vec e_z$. Here it holds, and it holds for the reason the whole article keeps meeting: the algebra is commutative.

### The Hermitian Symmetry

**Proposition.** The ternary product satisfies $\{Q_1,Q_2,Q_3\}^{*}=\{Q_3^{*},Q_2^{*},Q_1^{*}\}$, that is, $\overline{\{Q_1,Q_2,Q_3\}}=\{\bar Q_3,\bar Q_2,\bar Q_1\}$.

*Proof.* The conjugate of $Q_1\bar Q_2Q_3$ is $\bar Q_1Q_2\bar Q_3$, and $\{\bar Q_3,\bar Q_2,\bar Q_1\}=\bar Q_3\overline{\bar Q_2}\bar Q_1=\bar Q_3Q_2\bar Q_1$, which is the same by commutativity.

**Remark.** The Hermitian symmetry is the general one and it carries the conjugates of the three slots; the outer symmetry is the extra one that the commutative base supplies. The pair of propositions is the whole statement of the symmetries: one is general, the other is an accident of the field, and both hold here.

## The Contractions

**Proposition.** Inserting the unit in a slot recovers a binary product:

$$
\{Q_1,1,Q_3\}=Q_1Q_3, \qquad \{Q_1,Q_2,1\}=Q_1\bar Q_2, \qquad \{1,Q_2,Q_3\}=\bar Q_2Q_3 .
$$

*Proof.* The first and the third are read at $\bar 1=1$, the second at the third slot $1$.

**Remark (the triple names no new object).** The three contractions recover the plain product, the sesquilinear product and the sesquilinear product with the conjugation in the first slot. Every binary operation of the space is therefore a contraction of the triple, and the triple adds no operation to the two. What it adds is a law: the two binary products carry no associativity identity, and the triple carries the Jordan triple identity. The triple is not a richer product; it is the same product read at the arity where an identity exists.

## The Jordan Triple Identity

**Definition.** The ternary product satisfies the **Jordan triple identity** when

$$
\{Q_1,Q_2,\{Q_4,Q_5,Q_6\}\}=\{\{Q_1,Q_2,Q_4\},Q_5,Q_6\}-\{Q_4,\{Q_2,Q_1,Q_5\},Q_6\}+\{Q_4,Q_5,\{Q_1,Q_2,Q_6\}\}
$$

for all choices of the six elements.

**Theorem.** The ternary product of $\mathbb{C}$ satisfies the Jordan triple identity.

*Proof.* Every one of the four terms equals the same product $Q_1\bar Q_2Q_4\bar Q_5Q_6$. The left-hand side is $Q_1\bar Q_2(Q_4\bar Q_5Q_6)$; the first term on the right is $(Q_1\bar Q_2Q_4)\bar Q_5Q_6$; the second is $Q_4\overline{(Q_2\bar Q_1Q_5)}Q_6=Q_4\bar Q_2Q_1\bar Q_5Q_6$; the third is $Q_4\bar Q_5(Q_1\bar Q_2Q_6)$. The multiplication is associative and commutative, so the four readings of the same string of five factors coincide, and the identity reduces to the tautology that four equal numbers are equal.

**Remark (the general warrant).** The identity is not special to $\mathbb{C}$. *Algebraic J\*-Algebras* proves it for the middle model $Q_1Q_2^{*}Q_3$ of any associative complex algebra with a conjugate-linear involution, by a finite expansion in the associativity of the product and in the anti-multiplicativity of the involution. The proof above is shorter only because commutativity collapses the expansion to one term. The theorem is therefore a special case of a general one, and the special case is worth stating because it exhibits the reason: commutativity.

**Remark (the quadratic representation).** The case of the two outer slots equal is the quadratic representation, and here it is

$$
\{Q_1,Q_2,Q_1\}=Q_1\bar Q_2Q_1=Q_1^{2}\overline{Q_2} .
$$

The operator is therefore the conjugation followed by the multiplication by $Q_1^{2}$, and it is not a scalar multiple of the identity: the conjugation is conjugate-linear and the identity is not. Two readings fix its size. It multiplies the Hermitian norm by the fourth power of the modulus, $H(\{Q_1,Q_2,Q_1\})=|Q_1|^{4}H(Q_2)$, and it carries $Q_1$ to $|Q_1|^{2}Q_1$, so the line of $Q_1$ is preserved and scaled by the squared modulus. In a general algebra the quadratic representation is an operator-valued quadratic map, and the rank-one degeneration is visible here in the fact that the operator depends on $Q_1$ only through $Q_1^{2}$: one operator, determined by one square.

## The Algebraic J*-Structure

**Definition.** An **algebraic $J^{*}$-algebra** is an associative complex algebra $A$ with a conjugate-linear involution ${}^{*}$ such that the middle model $\{Q_1,Q_2,Q_3\}=Q_1Q_2^{*}Q_3$ satisfies the Jordan triple identity and the parity of the axioms; the axioms are those of *Algebraic J\*-Algebras*.

**Theorem.** $\mathbb{C}$ with the bar and the ternary product $\{Q_1,Q_2,Q_3\}=Q_1\bar Q_2Q_3$ is an algebraic $J^{*}$-algebra.

*Proof.* The parity is the proposition of §*The Two Symmetries*, and the identity is the theorem of §*The Jordan Triple Identity*.

**Remark (the structure names no binary product).** The axioms of the structure speak of one operation of three arguments and of one involution. No multiplication of two arguments occurs in them. The binary products are recovered from the triple by inserting the unit, and two different insertions give the two products of the space. The structure is therefore blind to which binary product produced it, and that blindness is the point: the two products of the complex space are two shadows of one triple.

**Remark (flatness).** The triple system is one-dimensional over $\mathbb{C}$. A triple system of higher rank carries a space of tripotents and a Peirce decomposition; here the only tripotents are $0$ and $1$, and the Peirce decomposition is the trivial one, in agreement with the degenerate Peirce decomposition of the field recorded in *The Classes of Element of the Complex Algebra*.

## The Associator Confined to the Shape

**Theorem.** The associator of the sesquilinear product is a real scalar multiple of the product $Q_1\bar Q_2$: it is $Q_1\bar Q_2$ multiplied by $-2i\operatorname{Im}Q_3$.

*Proof.* This is the proposition of §*The Failure of Associativity*.

**Remark (what confinement means).** The associator has the shape of the sesquilinear product with one extra factor, and that factor is a purely imaginary scalar. It cannot produce a term of a different shape, it cannot mix the two products, and it cannot be non-zero for a real third slot. In the terminology of the general article the associator is **confined to the shape** of the product it belongs to.

**Remark (the vanishing criterion).** The associator vanishes exactly when the third slot is real, or when the first product vanishes. The first alternative is the generic one; the second is the degenerate case that every product has and that no algebra avoids. A reader who wants a clean criterion should read the vanishing set as the union of the real third slot and the degenerate pair.

## The Comparison with the Biquaternion Sesqualgebra

On $\mathbb{B}$ the ternary product is $\tilde Q_1\tilde Q_2^{*}\tilde Q_4$, the same middle model, and the Jordan triple identity holds there too; the biquaternion algebra is an algebraic $J^{*}$-algebra for the same reason the complex algebra is. The similarity stops at the associator. On $\mathbb{B}$ the associator is $\tilde Q_1(\tilde Q_2^{*}\tilde Q_4^{*}-\tilde Q_4\tilde Q_2^{*})$, a difference of two products of different shapes, not a scalar multiple of one product; and the outer symmetry fails, because $\mathbb{B}$ is not commutative. So the complex case is the biquaternion case with two degenerations at once: the associator collapses to the shape, and the outer symmetry comes back. Both degenerations have the same cause, and the cause is the commutativity of the field.

## Summary

The sesquilinear product is not associative, and its associator is $[Q_1,Q_2,Q_3]=Q_1\bar Q_2(\bar Q_3-Q_3)$, confined to the shape of the product and vanishing exactly on the real third slot, apart from the degenerate pair. The ternary product is $\{Q_1,Q_2,Q_3\}=Q_1\bar Q_2Q_3$, $\mathbb{C}$-linear in the outer slots and conjugate-linear in the middle, symmetric in the outer slots and Hermitian-symmetric in all three; its contractions recover both binary products, so it adds no operation. It satisfies the Jordan triple identity, as the general middle-model theorem requires and as the commutativity of the field makes immediate, and $\mathbb{C}$ with this triple is an algebraic $J^{*}$-algebra whose axioms name no binary product. The quadratic representation is the conjugation followed by the multiplication by $Q_1^{2}$, which scales the Hermitian norm by $|Q_1|^{4}$. Against the biquaternion algebra the identity survives and the confinement of the associator does not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_1,Q_2,Q_3$ | complex elements, with real coordinates |
| $\bar Q$, ${}^{*}=\bar{\cdot}$ | the conjugation, the Hermitian conjugation |
| $[Q_1,Q_2,Q_3]$ | the associator $(Q_1\bar Q_2)\bar Q_3-Q_1\overline{(Q_2\bar Q_3)}$ |
| $Q_1\bar Q_2(\bar Q_3-Q_3)$ | the value of the associator |
| $\{Q_1,Q_2,Q_3\}=Q_1\bar Q_2Q_3$ | the ternary product |
| $\{Q_1,Q_2,Q_3\}^{*}=\{Q_3^{*},Q_2^{*},Q_1^{*}\}$ | the Hermitian symmetry |
| $\{Q_1,1,Q_3\}$, $\{Q_1,Q_2,1\}$ | the contractions to the two binary products |
| Jordan triple identity | the defining law of the algebraic $J^{*}$-algebra |

## Further Reading

- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis*, Cambridge Tracts in Mathematics 190 (Cambridge University Press, 2012), for $J^{*}$-algebras, the triple product $xy^{*}z$ and the Jordan triple identity.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the triple identity, the quadratic representation and the passage between the binary and the ternary operations.
- Ottmar Loos, *Jordan Pairs*, Lecture Notes in Mathematics 460 (Springer, 1975), for triple systems, their symmetries and the operator forms of the triple product.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras*, Colloquium Publications 39 (American Mathematical Society, 1968), for the algebraic theory of triple systems and its identities.
