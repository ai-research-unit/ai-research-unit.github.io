# __The Ternary Product and the Associator of the Split-Complex Space__

## Introduction

The second product of the split-complex space is not associative, and the structure that survives is the ternary one. This article computes the ternary product $\{A,B,C\}=A\bar BC$, its componentwise form in idempotent coordinates, its two symmetries and its contractions to the two binary products; it proves the Jordan triple identity and reads it as the algebraic $J^{*}$-structure of the ring; and it computes the associator $[A,B,C]=A\bar B(\bar C-C)$, the exact set where it vanishes, and the value it takes elsewhere.

The claim of the article is a contrast. The defect of the binary product is confined to one slot and to one factor, $\bar C-C$, which is the anti-fixed part of the third slot; the ternary product repairs the defect exactly, because it puts the three slots in the order that the crossing of the idempotent index requires. The split-complex ring is therefore a $J^{*}$-algebra in the algebraic sense of the term, and it is one for the same reason that it fails to be a field: the idempotent coordinates.

The two binary products are *The Two Products of the Split-Complex Space*; the norm that appears on the diagonal is *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*; the trace of this article through the operators is *The Enveloping Operator Algebra and the Collapse of the Two-Sided Action on the Split-Complex Ring*.

## The Ternary Product

### The Definition

**Definition.** The **ternary product** of the space is

$$
\{A,B,C\}=A\bar B\,C ,
$$

the plain product of the first slot, the conjugation of the second and the plain product of the third.

The definition is the one the second product forces: the triple is $(A\star B)\star\bar C$ with $\star$ the sesquilinear product, and the double conjugation of the third slot returns $C$. Both readings give the same element, and the agreement is the associativity of the plain product.

### The Idempotent Coordinates

**Proposition.** In the idempotent coordinates the ternary product is componentwise, with the index of the middle slot crossed:

$$
\{A,B,C\}_+=A_+\,B_-\,C_+, \qquad \{A,B,C\}_-=A_-\,B_+\,C_- .
$$

**Proof.** $\bar B$ has coordinates $(B_-,B_+)$, since $\overline{B_+}=B_-$. The plain product is componentwise with the index, so the first coordinate of $A\bar BC$ is $A_+B_-C_+$ and the second is $A_-B_+C_-$.

Two consequences follow at once. The first coordinate of the value depends on the first coordinates of the outer slots and on the second coordinate of the middle slot, and the second coordinate on the other three; the two coordinates are computed independently. And the ternary product is the model $xy^{*}z$ of a commutative ring with an involution, read twice.

### The Two Symmetries

**Proposition.** The ternary product is symmetric in its outer slots and Hermitian-symmetric:

$$
\{A,B,C\}=\{C,B,A\}, \qquad \overline{\{A,B,C\}}=\{\bar A,\bar B,\bar C\} .
$$

**Proof.** $A\bar BC=C\bar BA$ by the commutativity of the plain product, and $\overline{A\bar BC}=\bar A\,B\,\bar C=\{\bar A,\bar B,\bar C\}$, since the conjugation is an involutive automorphism.

The outer symmetry and the Hermitian symmetry are the two symmetries the pattern allows: the first slot and the third are interchangeable, and the conjugation acts on the whole triple by acting on the three entries. The middle slot is the one that carries the involution and it is not interchangeable with the others.

### The Contractions to the Two Binary Products

Setting one slot to the unit gives the two binary products back:

$$
\{A,B,1\}=A\bar B, \qquad \{1,B,C\}=\bar B\,C, \qquad \{A,1,C\}=AC .
$$

So the ternary product contracts to the sesquilinear product in the third slot and to the plain product in the middle one, and the two contractions differ by the conjugation of the middle slot. The ternary product is therefore not a third product but the smallest object that contains both.

### The Diagonal

On the diagonal the ternary product returns the norm times the element:

$$
\{A,A,A\}=A\bar A\,A=N(A)\,A .
$$

**Proof.** $A\bar A=N(A)$ is real and central, and $A\bar AA=N(A)A$ by associativity of the plain product.

So the ternary square of an element is the element scaled by its split norm, and it vanishes exactly on the two null lines. The diagonal of the ternary product is the norm, which is why the norm is a ternary object and not only a binary one.

## The Jordan Triple Identity

### The Identity

**Theorem.** For all $A,B,C,D,E$,

$$
\{A,B,\{C,D,E\}\}=\{\{A,B,C\},D,E\}-\{C,\{B,A,D\},E\}+\{C,D,\{A,B,E\}\} .
$$

**Proof.** Write every ternary product out and use the associativity and the commutativity of the plain product. The left side is $A\bar B C\bar D E$. The three terms on the right are $A\bar B C\bar D E$, $-C\bar B A\bar D E$ and $C\bar D A\bar B E$, and the middle term cancels against the third up to the order of the factors, which commutativity allows. What is left is the first term.

The identity is the standard one for the triple product $xy^{*}z$ of an associative algebra with an involution, and its verification here uses only that the plain product is associative and commutative. It is an identity of the ternary product and it fails for the binary one, which is not associative.

### The Algebraic $J^{*}$-Structure

**Definition.** An **algebraic $J^{*}$-algebra** is a complex vector space with a conjugation, a triple product additive in each variable, linear in the first and the third, conjugate-linear in the second, symmetric in the outer slots, and satisfying the identity above.

**Theorem.** $\mathbb{C}_{\mathrm{spl}}$ with the ternary product $\{A,B,C\}=A\bar BC$ is an algebraic $J^{*}$-algebra over the involutive ring $\mathbb{R}\subset\mathbb{C}_{\mathrm{spl}}$.

**Proof.** The additivity and the three scalar rules are the scalar rules of the plain product in the first and the third slots and the conjugated rule in the second; the outer symmetry and the identity are the two propositions above. The conjugation is the involution of the ring and it is $\mathbb{R}$-linear.

The structure is the one the corpus calls the algebraic $J^{*}$-structure, and it is the reason the split-complex ring belongs with the Jordan algebras and not with the associative ones: the object that carries an identity is the triple, not the pair.

### What the Ring Satisfies and What It Does Not

The ring is a $J^{*}$-algebra in the algebraic sense and it is not a $JB^{*}$-algebra: the latter needs a complete norm and a positive definite form, and the second product of this ring is indefinite and vanishes on two lines (*The Hermitian Form, the Double Cone and the Reversed Cauchy-Schwarz Inequality*). What survives is the algebraic skeleton, the ternary product and its identity, and the positivity is what is lost.

## The Associator

### The Formula

**Definition.** The **associator** of the sesquilinear product is

$$
[A,B,C]=(A\bar B)\bar C-A(\overline{B\bar C}) .
$$

**Proposition.** $[A,B,C]=A\bar B\,(\bar C-C)$.

**Proof.** $(A\bar B)\bar C=A\bar B\bar C$ and $A(\overline{B\bar C})=A\bar B C$, so the difference is $A\bar B(\bar C-C)$.

The formula separates the two slots: the pair of the first two slots enters as the single factor $A\bar B$, and the third slot enters through its anti-fixed part $\bar C-C=-2c'j$. The defect is therefore a defect of the third slot alone, measured against the pair before it.

### The Vanishing Criterion

**Theorem.** $[A,B,C]=0$ if and only if $C$ is real or $A\bar B=0$.

**Proof.** The product of $A\bar B$ and $\bar C-C$ vanishes in a ring with zero divisors exactly when one of the two factors does. The second factor is $\bar C-C=-2c'j$, which is zero exactly when $C$ is real; the first is zero exactly when $A=0$ or $B=0$ or the two are complementary zero divisors.

On a pair whose product $A\bar B$ is a unit the criterion is exactly the realness of the third slot, and that is the statement to keep: the associator measures the failure of the third slot to be real. The second alternative is the zero-divisor phenomenon of the ring and it has no counterpart over a field.

### The Value

When the associator does not vanish it is a specific element. Since $\bar C-C=-2c'j$,

$$
[A,B,C]=-2c'\,(A\bar B)\,j, \qquad N([A,B,C])=-4c'^2\,N(A)\,N(B) .
$$

**Proof.** The first formula is the substitution of $\bar C-C$; the second is the multiplicativity of the norm, $N(j)=-1$ and $N(\bar B)=N(B)$.

On a pair of units with a third slot off the real line the associator is a non-zero element of negative norm: it points in the spacelike direction, in the cone opposite to the cone of squares, and its size is $2\lvert c'\rvert\sqrt{\lvert N(A)N(B)\rvert}$. The value need not lie on the split imaginary line: with $A=j$, $B=1$, $C=j$ it is $-2$, a real number, because the factor $A\bar B=j$ turns the factor $j$ into $-1$. What is invariant is the norm, which is negative whenever the first two slots are units and the third is not real.

### The Confinement to the Sesquilinear Shape

The defect belongs to the second product and not to the first. The plain product is associative, so its associator vanishes identically, and the associator of the sesquilinear product is the only one in the category. In idempotent coordinates the defect is

$$
[A,B,C]_\pm=\mp\,(C_+-C_-)\,A_\pm B_\mp ,
$$

so the two coordinates of the associator are opposite multiples of the same scalar $C_+-C_-=2c'$, and the vanishing is the vanishing of that scalar or of the products $A_\pm B_\mp$. The associator therefore has one degree of freedom where the ternary product has two, and the missing degree is exactly what the third slot's realness removes.

## The Comparison with the Complex Case

### The Two Components Coincide

Over $\mathbb{C}$ the same formulas hold with $i^2=-1$: the ternary product is $\{A,B,C\}=A\bar BC$, the Jordan triple identity holds, and the associator is $A\bar B(\bar C-C)$, which vanishes exactly when the third slot is real. What is absent is the second component. The complex field has no idempotent split, so the two coordinates of the split case become one, the index crossing becomes invisible, and "componentwise" degenerates to a single entry. The formulas coincide and their reading does not: here every identity is two real identities, there it is one.

### Against the Biquaternion Case

On $\mathbb{B}$ the ternary product has more slots to fail in, the associator has four terms rather than one, and the structure is *The Associator and the Ternary Product of the Quaternionic Product of the Biquaternions*. The split case is the one where the four products collapse to two and the associator collapses to a single factor $\bar C-C$, so the article there is a theory and the article here is a computation.

## Summary

The ternary product $\{A,B,C\}=A\bar BC$ is componentwise in the idempotent coordinates, with the middle index crossed, $\{A,B,C\}_\pm=A_\pm B_\mp C_\pm$; it is symmetric in its outer slots, Hermitian-symmetric, contracts to the sesquilinear product in the third slot and to the plain product in the middle one, and its diagonal is $\{A,A,A\}=N(A)A$. It satisfies the Jordan triple identity, so $\mathbb{C}_{\mathrm{spl}}$ is an algebraic $J^{*}$-algebra over its involutive ring, and it is not a $JB^{*}$-algebra because the form is indefinite.

The associator is $[A,B,C]=A\bar B(\bar C-C)$, a defect of the third slot alone; it vanishes exactly when the third slot is real or when $A\bar B=0$, and its value is $-2c'(A\bar B)j$ of norm $-4c'^2N(A)N(B)$, a spacelike element on a pair of units. It is confined to the sesquilinear shape, the plain product being associative. Over $\mathbb{C}$ the formulas are the same and the two components of the split case coincide into one; over $\mathbb{B}$ the associator has four terms where here it has one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\{A,B,C\}=A\bar BC$ | The ternary product |
| $\{A,B,C\}_\pm=A_\pm B_\mp C_\pm$ | The ternary product in idempotent coordinates |
| $\{A,A,A\}=N(A)A$ | The diagonal, the norm times the element |
| $[A,B,C]=A\bar B(\bar C-C)$ | The associator of the sesquilinear product |
| $-2c'(A\bar B)j$ | The value of the associator when it does not vanish |
| $-4c'^2N(A)N(B)$ | The split norm of the associator |
| $\bar C-C=-2c'j$ | The anti-fixed part of the third slot, the source of the defect |
| $J^{*}$ | The algebraic structure the ternary product defines |

## Further Reading

- Erhard Neher, *Jordan Triple Systems by the Grid Approach* (Springer, Lecture Notes in Mathematics 1280, 1987), for Jordan triples, the triple identity and the grid description of the split cases.
- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis* (Cambridge University Press, 2012), for algebraic $J^{*}$-algebras, the triple product $xy^{*}z$ and the passage to the normed case.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, Universitext, 2004), for the quadratic and triple products of a Jordan structure and the role of the unit.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, Colloquium Publications 39, 1968), for the Jordan triple systems attached to an associative algebra with an involution.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the associator of a non-associative product and the Peirce coordinates that compute it.
