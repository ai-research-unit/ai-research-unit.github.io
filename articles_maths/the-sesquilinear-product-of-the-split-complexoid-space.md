# __The Sesquilinear Product of the Split-Complexoid Space__

## Introduction

The underlying real space of the split-complex algebra carries a second multiplication beside the plain one. It is

$$
Q_1 \star Q_2 = Q_1\bar Q_2 ,
$$

the product whose second slot is read through the conjugation, and it is the **general plain sesquilinear product** of the space: $\mathbb{D}$-linear in the first argument, $\bar\cdot$-semilinear in the second, additive in each. This article builds the **sesqualgebra** it defines. Unlike the plain product it is neither associative nor two-sidedly unital, and the structure that survives is the one that does not need associativity: the right unit alone, the associator, the ternary product, the two families of one-sided multiplications, the sandwich, the adjoint with respect to the Hermitian form, and the commutator with its symmetrisation.

The results are simpler than in the four-dimensional case and sharper than in the complex one. The product has a right unit and no left one, and its associator is

$$
(Q_1 \star Q_2) \star Q_3 - Q_1 \star (Q_2 \star Q_3) = Q_1\bar Q_2\,(\bar Q_3 - Q_3),
$$

which vanishes exactly when the third factor is real; the ternary product $\{Q_1,Q_2,Q_3\} = Q_1\bar Q_2 Q_3$ restores the Jordan triple identity and makes $\mathbb{D}$ an algebraic $J^{*}$-algebra. The right multiplications $R_Q$ generate the opposite monoid of the multiplicative monoid of $\mathbb{D}$, while the left ones $L_Q$ do not close; the sandwich $X \mapsto Q_1X\bar Q_2$ decomposes into one ordinary and one sesquilinear multiplication and is adjoint to the sandwich with the parameters exchanged; and the commutator $Q_1\bar Q_2 - Q_2\bar Q_1 = 2(q'_1q_2 - q_1q'_2)j$ lies on the split imaginary line, its halved antisymmetrisation is the area form and its symmetrisation is the scalar form $q_1q_2 - q'_1q'_2$ that the norm polarises. The bracket defined by the commutator satisfies the Jacobi identity.

**Placement.** The article opens the split-complex general-plain-sesqualgebra block, after the general-plain-algebra block; the two products as a family and the collapse to two are *The Two Products of the Split-Complexoid Space*, and the slot reading of the two products, with the two pairings and the two adjoints they carry, is *Relations and Comparison Between the Two Products of the Split-Complexoid Space*, above this article in this category. The form theory of the second slot — $\langle\cdot,\cdot\rangle_{*}$ as a form on the regular module, the positivity cone, the modules and the Witt group — is *The Hermitian Form and the Cone of the Split-Complexoid Algebra*, below this article in this category. The multiply-unrelated material is *Split-Complex Algebra*, which owns the plain product, and *Norm and Invertibility in the General Split-Complex Algebra*.

**Conventions.** The algebra is $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, basis $1$, $j$, $j^2 = +1$, general element $Q = q+jq'$, conjugate $\bar Q = q-jq'$, idempotents $\Pi_1 = \tfrac12(1+j)$ and $\Pi_2 = \tfrac12(1-j)$, idempotent coordinates $q_+ = q+q'$ and $q_- = q-q'$. The product is written with a star, $Q_1 \star Q_2 = Q_1\bar Q_2$, and never with a bare juxtaposition, which is reserved for the plain product; the conjugation is never written as an operator symbol. The involution of the algebra is the bar, the coefficients being real and the idempotent swap coinciding with it, so the symbol $*$ of the general theory is realised here by the bar alone; the words **linear** and **conjugate-linear** are read over the ring $(\mathbb{D},\bar\cdot)$, in the sense of the two scalar rules below.

## The Product and Its Two Slots

### The Rule

**Definition.** The **sesquilinear multiplication** of the split-complex space is

$$
\star \; : \; \mathbb{D} \times \mathbb{D} \longrightarrow \mathbb{D}, \qquad
(Q_1,Q_2) \longmapsto Q_1 \star Q_2 = Q_1\bar Q_2 ,
$$

the general plain sesquilinear product of *The Two Products of the Split-Complexoid Space*. On the coordinates,

$$
Q_1 \star Q_2 = (q_1+jq'_1)(q_2-jq'_2) = (q_1q_2-q'_1q'_2) + (q'_1q_2-q_1q'_2)j .
$$

### The Two Scalar Rules

**Proposition.** The multiplication is additive in each variable; it is $\mathbb{D}$-linear in the first and $\bar\cdot$-semilinear in the second:

$$
(\lambda Q_1) \star Q_2 = \lambda\,(Q_1 \star Q_2), \qquad
Q_1 \star (\lambda Q_2) = \bar\lambda\,(Q_1 \star Q_2), \qquad \lambda \in \mathbb{D}.
$$

**Proof.** Additivity and the first rule are the distributivity of $\mathbb{D}$ in the first slot, which is not conjugated. For the second, $Q_1 \star (\lambda Q_2) = Q_1\overline{\lambda Q_2} = Q_1\bar\lambda\bar Q_2 = \bar\lambda\,Q_1\bar Q_2$, using the multiplicativity of the conjugation and the commutativity of $\mathbb{D}$.

These are the two axioms of a sesquilinear product over the ring with involution $(\mathbb{D},\bar\cdot)$ and nothing else: neither associativity nor commutativity nor a two-sided unit is assumed. One word on the base, because on $\mathbb{D}$ the rules are less visible than over $\mathbb{C}$: the base field is $\mathbb{R}$ and the conjugation is $\mathbb{R}$-linear, so over $\mathbb{R}$ alone the map $Q_1\bar Q_2$ is bilinear, and the content of "sesquilinear" is the action of the *ring* $(\mathbb{D},\bar\cdot)$ on its regular module. The second rule is the statement that the second slot is twisted by the ring involution; it is the only place where an involution enters.

### The Multiplication Table

**Proposition.** On the basis elements $1, j$ the multiplication is

| $\star$ | $1$ | $j$ |
|---|---|---|
| $1$ | $1$ | $-j$ |
| $j$ | $j$ | $-1$ |

**Proof.** $1 \star 1 = \bar 1 = 1$, $1 \star j = \bar j = -j$, $j \star 1 = j$, and $j \star j = j\bar j = -j^2 = -1$.

The table is not the multiplication table of the algebra: on the plain product one has $j \cdot j = +1$, while here $j \star j = -1$. The diagonal is $1,-1$ rather than $1,1$, and the first row is the conjugation, $1 \star Q = \bar Q$, while the first column is the identity, $Q \star 1 = Q$. The asymmetry between the two off-diagonal entries is the visible form of the second scalar rule.

### The Right Unit and the Absence of a Two-Sided Unit

**Proposition.** The element $1$ is a **right unit**: $Q \star 1 = Q$ for every $Q$. It is not a left unit: $1 \star Q = \bar Q$, which differs from $Q$ unless $Q$ is real.

**Proof.** $Q \star 1 = Q\bar 1 = Q$, and $1 \star Q = \bar Q$, which equals $Q$ for every $Q$ only if the conjugation is the identity, which it is not; the witness is $1 \star j = -j \neq j$.

**Corollary.** The multiplication has **no two-sided unit**. An element $E$ with $E \star Q = Q$ for all $Q$ would give $E = 1$ from $Q$ real, and then $1 \star Q = Q$ for all $Q$ would force the conjugation to be the identity; so no element is simultaneously a left and a right unit.

The one-sided unit is the mark of a derived operation: the left action by $1$ is the involution, and the right action is the identity. It is not a defect of $\mathbb{D}$ but the consequence of the involution sitting in the second slot, exactly as the general theory of sesqualgebras proves for the standard example. It has a further consequence that recurs below: since $1$ is a right unit, no nonzero element annihilates the whole space on the left, for $Q \star 1 = Q$; the product is faithful on the left.

## The Associator and the Ternary Product

### The Associator

**Definition.** The **associator** of the multiplication is

$$
[Q_1,Q_2,Q_3] = (Q_1 \star Q_2) \star Q_3 - Q_1 \star (Q_2 \star Q_3).
$$

**Theorem.** For all $Q_1,Q_2,Q_3 \in \mathbb{D}$,

$$
[Q_1,Q_2,Q_3] = Q_1\bar Q_2\,(\bar Q_3 - Q_3),
$$

an element of $\mathbb{D}$ that vanishes exactly when $Q_1 = 0$, or $Q_2 = 0$, or $Q_3$ is real.

**Proof.** The first bracket is $(Q_1\bar Q_2)\bar Q_3 = Q_1\bar Q_2\bar Q_3$ and the second is $Q_1\overline{(Q_2\bar Q_3)} = Q_1\bar Q_2 Q_3$, so the difference is $Q_1\bar Q_2(\bar Q_3 - Q_3)$. The factor $\bar Q_3 - Q_3 = -2q'_{3}\,j$ vanishes exactly when $Q_3 \in \mathbb{R}_{\mathbb{D}}$, and the product $Q_1\bar Q_2$ vanishes exactly when $Q_1\bar Q_2 = 0$, which for the plain product means $Q_1 = 0$ or $Q_2 = 0$ or one of them is a zero divisor of the algebra; on the products with $Q_1\bar Q_2 \neq 0$ the associator is nonzero precisely when $Q_3$ is not real.

**Corollary.** The multiplication is **not associative**. The associativity defect is confined to the second factor's action on the third: the two groupings agree whenever the third argument is real, and differ otherwise.

**Witness.** On the triple $(j,j,j)$,

$$
(j \star j) \star j = (-1) \star j = j, \qquad
j \star (j \star j) = j \star (-1) = -j,
$$

and the two differ by $2j$. The associator is $[j,j,j] = 2j$.

The shape of the formula is the general one for a derived operation $Q_1\bar Q_2$, with the difference $\bar Q_3 - Q_3$ of the two parities of the third factor in place of the associativity that the plain product has. It is the sesquilinear counterpart of the double product's failure, and it is confined to the sesquilinear shape: the plain product of $\mathbb{D}$ is associative.

### The Ternary Product and the Jordan Triple Identity

**Definition.** The **ternary product** attached to the multiplication is

$$
\{Q_1,Q_2,Q_3\} = (Q_1 \star Q_2) \star \bar Q_3 = Q_1\bar Q_2 Q_3 ,
$$

the middle slot carrying the involution and the two outer slots not.

**Theorem.** The ternary product is additive in each variable, $\mathbb{D}$-linear in the first and the third and $\bar\cdot$-semilinear in the second, and it satisfies the **Jordan triple identity**

$$
\{Q_1,Q_2,\{Q_3,Q_4,Q_5\}\} = \{\{Q_1,Q_2,Q_3\},Q_4,Q_5\} - \{Q_3,\{Q_2,Q_1,Q_4\},Q_5\} + \{Q_3,Q_4,\{Q_1,Q_2,Q_5\}\} ,
$$

so $\mathbb{D}$ with this ternary product is an **algebraic $J^{*}$-algebra**.

**Proof.** The first clause is the two scalar rules read in the three slots. For the identity, expand both sides with $\{X,Y,Z\} = X\bar Y Z$: the left side is $Q_1\bar Q_2 Q_3\bar Q_4 Q_5$, and the right side is $Q_1\bar Q_2 Q_3\bar Q_4 Q_5 - Q_3\bar Q_2 Q_1\bar Q_4 Q_5 + Q_3\bar Q_4 Q_1\bar Q_2 Q_5$; the three terms are products of the six elements with the conjugation on the second factor of each triple, and the identity is the associativity of the plain product together with the commutativity of $\mathbb{D}$, which allow the terms $-Q_3\bar Q_2 Q_1\bar Q_4 Q_5$ and $+Q_3\bar Q_4 Q_1\bar Q_2 Q_5$ to cancel against the first. The verification is the model computation $xy^{*}z$ of an associative algebra with a sesquilinear involution, which is the standard example of an algebraic $J^{*}$-algebra; the general theorem is the one the general theory quotes.

So the ternary product is the binary multiplication's surviving form: it is associative-like in the only sense available, since the binary product is not associative, and its identities hold where the binary ones fail. The same identity holds for the same model $PQ^{*}R$ here, with the middle slot conjugated. The failure is the *associativity* of the binary product, recorded above; the ternary product repairs it.

## The Left and Right Multiplications

### The Two Families

**Definition.** The **left** and **right multiplications** by $Q \in \mathbb{D}$ are the maps

$$
L_Q : X \mapsto Q \star X = Q\bar X, \qquad
R_Q : X \mapsto X \star Q = X\bar Q .
$$

The right multiplication $R_Q$ is $\mathbb{D}$-linear, being a product with $Q$ and the conjugation of the fixed factor $Q$; the left multiplication $L_Q$ is $\bar\cdot$-semilinear, the conjugation falling on the variable. Special values:

$$
L_1 = \overline{\cdot} \quad (\text{the conjugation}), \qquad R_1 = \mathrm{id}.
$$

So the two families do not coincide, and the difference is exactly the involution: $L_Q - R_Q$ is the involution composed with a multiplication.

### The Opposite Monoid

**Proposition.** The right multiplications compose within themselves, reversing the order,

$$
R_{Q_1} \circ R_{Q_2} = R_{Q_2Q_1},
$$

and $\{R_Q : Q \in \mathbb{D}\}$ is a monoid isomorphic to the opposite monoid $(\mathbb{D},\cdot)^{\mathrm{opp}}$ via $Q \mapsto R_Q$, with identity $R_1$.

**Proof.** $R_{Q_1}(R_{Q_2} X) = (X\bar Q_2)\bar Q_1 = X\bar Q_2\bar Q_1 = X\overline{Q_1Q_2} = R_{Q_2Q_1}(X)$, using the multiplicativity of the conjugation; the map $Q \mapsto R_Q$ is then an anti-homomorphism with $Q=1$ giving the identity.

**Proposition.** The left multiplications do not compose within themselves: their products are ordinary multiplications,

$$
L_{Q_1} \circ L_{Q_2} = M_{Q_1\bar Q_2},
$$

where $M_Q(X) = QX$ is the ordinary left multiplication. In particular $L_{Q_1} \circ L_{Q_2}$ is $\mathbb{D}$-linear, while each $L_Q$ is $\bar\cdot$-semilinear, and the product of two of them is the multiplication by $Q_1\bar Q_2$, the value of the sesquilinear product.

**Proof.** $L_{Q_1}(L_{Q_2} X) = Q_1\overline{(Q_2\bar X)} = Q_1\bar Q_2 X = M_{Q_1\bar Q_2}(X)$.

So the two one-sided families behave differently, and the asymmetry is the one of the general theory: the right family is a monoid, isomorphic to the opposite of the multiplicative monoid of the ring, while the left family is not closed and its products fall back into the ordinary multiplications. This is the split-complex form of the statement that the left and right multiplications fail to coincide and generate an opposite monoid.

### The Sandwich

**Definition.** The **sesquilinear sandwich** by the parameters $Q_1, Q_2 \in \mathbb{D}$ is the map

$$
S_{Q_1,Q_2} : X \longmapsto Q_1\,X\,\bar Q_2 .
$$

It is the composite of the ordinary left multiplication $M_{Q_1}(X) = Q_1X$ and the sesquilinear right multiplication $R_{Q_2}(X) = X\bar Q_2$,

$$
S_{Q_1,Q_2} = M_{Q_1} \circ R_{Q_2} = R_{Q_2} \circ M_{Q_1} ,
$$

the two orders agreeing because $\mathbb{D}$ is commutative, and it is therefore the split-complex form of the sandwich $X \mapsto Q_1X\bar Q_2$. The parameters specialise as

$$
S_{1,1} = \mathrm{id}, \qquad S_{Q_1,1} = M_{Q_1}, \qquad S_{1,Q_2} = R_{Q_2}, \qquad S_{Q_1,Q_2}(1) = Q_1\bar Q_2 = Q_1 \star Q_2 ;
$$

the sandwich at the unit is the product, and the two families of one-sided multiplications are the two degenerate sandwiches.

**Proposition.** The sandwich is $\mathbb{D}$-linear in $X$, and its value at $1$ is the sesquilinear product $Q_1 \star Q_2$. Its composite with another sandwich is again a sandwich,

$$
S_{Q_1,Q_2} \circ S_{Q_3,Q_4} = S_{Q_1Q_3,\,Q_2Q_4} .
$$

**Proof.** Direct substitution, using the associativity of the plain product and the multiplicativity of the conjugation: $S_{Q_1,Q_2}(S_{Q_3,Q_4}(X)) = Q_1(Q_3X\bar Q_4)\bar Q_2 = (Q_1Q_3)X\bar Q_4\bar Q_2 = (Q_1Q_3)X\overline{Q_2Q_4} = S_{Q_1Q_3,Q_2Q_4}(X)$.

So the sandwiches form a monoid under composition, isomorphic to the product of the multiplicative monoid of $\mathbb{D}$ with itself via $(Q_1,Q_2) \mapsto S_{Q_1,Q_2}$; in particular the sandwich $S_{Q_1,Q_2}$ is invertible exactly when both $Q_1$ and $Q_2$ are units, with inverse $S_{Q_1^{-1},Q_2^{-1}}$.

## The Hermitian Form and the Adjoints

**Definition.** The **Hermitian form** of the regular module is

$$
\langle Q_1,Q_2\rangle_{*} = Q_1 \star Q_2 = Q_1\bar Q_2 .
$$

It is conjugate-symmetric, $\langle Q_2,Q_1\rangle_{*} = \overline{\langle Q_1,Q_2\rangle_{*}}$, $\mathbb{D}$-linear in the first slot and $\bar\cdot$-semilinear in the second. It is the canonical form of *The Hermitian Form and the Cone of the Split-Complexoid Algebra*, below this article in this category, which owns its Gram matrix, its signature, its positivity cone and its modules; here it is used only as the form that defines the adjoints. Its realified scalar part is

$$
\operatorname{Sc} \langle Q_1,Q_2\rangle_{*} = q_1q_2 - q'_1q'_2 ,
$$

the symmetric bilinear form $g$ that the norm polarises, of signature $(1,1)$.

**Definition (adjoint).** For a $\mathbb{D}$-linear map $T$ the **adjoint** is the $\mathbb{D}$-linear map $T^{*}$ with $\langle TX,Y\rangle_{*} = \langle X,T^{*}Y\rangle_{*}$ for all $X,Y$; for a $\bar\cdot$-semilinear map $T$ the adjoint is the $\bar\cdot$-semilinear map $T^{*}$ with $\langle TX,Y\rangle_{*} = \overline{\langle X,T^{*}Y\rangle_{*}}$.

**Theorem.** The adjoints of the one-sided multiplications and of the sandwich are

$$
M_Q^{*} = M_{\bar Q}, \qquad R_Q^{*} = M_Q, \qquad L_Q^{*} = L_Q, \qquad S_{Q_1,Q_2}^{*} = S_{Q_2,Q_1} .
$$

In particular the ordinary multiplication by a real element is self-adjoint, $M_t^{*} = M_t$ for $t \in \mathbb{R}$; the left multiplication is self-adjoint; and the sandwich is adjoint to the sandwich with the parameters exchanged.

**Proof.** Compute each defining identity.
- $\langle M_Q X, Q_1\rangle_{*} = (QX)\bar Q_1 = QX\bar Q_1$ and $\langle X, M_{\bar Q} Q_1\rangle_{*} = X\overline{\bar Q Q_1} = X Q\bar Q_1$, equal by commutativity.
- $\langle R_Q X, Q_1\rangle_{*} = (X\bar Q)\bar Q_1 = X\bar Q\bar Q_1$ and $\langle X, M_Q Q_1\rangle_{*} = X\overline{QQ_1} = X\bar Q\bar Q_1$, equal.
- $\langle L_Q X, Q_1\rangle_{*} = (Q\bar X)\bar Q_1 = Q\bar X\bar Q_1$ and $\overline{\langle X, L_Q Q_1\rangle_{*}} = \overline{X\overline{Q\bar Q_1}} = \bar X Q\bar Q_1$, equal, so $L_Q$ is self-adjoint.
- Since $S_{Q_1,Q_2} = M_{Q_1} \circ R_{Q_2}$, its adjoint is $S_{Q_1,Q_2}^{*} = R_{Q_2}^{*} \circ M_{Q_1}^{*} = M_{Q_2} \circ M_{\bar Q_1} = M_{Q_2\bar Q_1}$; and $S_{Q_2,Q_1}(X) = Q_2X\bar Q_1 = Q_2\bar Q_1 X = M_{Q_2\bar Q_1}(X)$, so the two agree.

**Examples.** Take $Q_1 = 1$ and $Q_2 = j$: the sandwich is $S_{1,j}(X) = X\bar j = -Xj$, and its adjoint is $S_{j,1}(X) = jX$, as the theorem requires. Take $Q_1 = Q_2 = \Pi_1$: the sandwich is

$$
S_{\Pi_1,\Pi_1}(X) = \Pi_1 X \bar\Pi_1 = \Pi_1 X \Pi_2 = 0
$$

for every $X$, since $\bar\Pi_1 = \Pi_2$ and $\Pi_1\Pi_2 = 0$; the zero map is self-adjoint, and indeed $S_{\Pi_1,\Pi_1}^{*} = S_{\Pi_1,\Pi_1}$ because the parameters are equal. Take $Q_1 = \Pi_1$ and $Q_2 = \Pi_2$, and write $X=x_+\Pi_1+x_-\Pi_2$: the sandwich is the projection onto the first idempotent line,

$$
S_{\Pi_1,\Pi_2}(X) = \Pi_1 X \bar\Pi_2 = \Pi_1 X \Pi_1 = x_+\Pi_1 ,
$$

and its adjoint is the projection onto the second, $S_{\Pi_2,\Pi_1}(X) = \Pi_2 X \Pi_2 = x_-\Pi_2$. The two projections onto the idempotent lines are therefore mutually adjoint, although they are idempotents of the sandwich monoid and not of the algebra in the same sense.

## The Commutator and the Symmetrisation

**Definition.** The **commutator** of the sesquilinear product is

$$
[Q_1,Q_2] = Q_1 \star Q_2 - Q_2 \star Q_1 = Q_1\bar Q_2 - Q_2\bar Q_1 .
$$

**Theorem.** For all $Q_1 = q_1+jq'_1$ and $Q_2 = q_2+jq'_2$,

$$
Q_1\bar Q_2 - Q_2\bar Q_1 = 2(q'_1q_2-q_1q'_2)\,j = -2(q_1q'_2-q'_1q_2)\,j ,
$$

an element of the **split imaginary line** $j\mathbb{R}_{\mathbb{D}}$; the coefficient $q_1q'_2-q'_1q_2$ is the determinant of the coordinate matrix $\left(\begin{smallmatrix}q_1&q'_1\\q_2&q'_2\end{smallmatrix}\right)$.

**Proof.** $Q_1\bar Q_2 = (q_1q_2-q'_1q'_2) + (q'_1q_2-q_1q'_2)j$ and $Q_2\bar Q_1 = (q_1q_2-q'_1q'_2) + (q_1q'_2-q'_1q_2)j$; subtracting, the real parts cancel and the split-imaginary parts add to $2(q'_1q_2-q_1q'_2)j = -2(q_1q'_2-q'_1q_2)j$.

So the commutator of the sesquilinear product is a hyperbolic vector: it lies on the split imaginary line, the $-1$ eigenspace of the conjugation, and its coefficient is the area form of the plane. This is the exact counterpart of the complex statement, where the commutator lies on the imaginary axis; the difference is the sign of the square, $j^2 = +1$ against $i^2 = -1$, as the comparison section below records.

**Theorem (the symmetrisation and the antisymmetrisation).** The symmetric and antisymmetric halves of the product are

$$
\tfrac12(Q_1\bar Q_2 + Q_2\bar Q_1) = q_1q_2-q'_1q'_2 = g(Q_1,Q_2), \qquad
\tfrac12(Q_1\bar Q_2 - Q_2\bar Q_1) = (q'_1q_2-q_1q'_2)\,j .
$$

The **symmetrisation** is the real scalar $g(Q_1,Q_2)$, the symmetric bilinear form that the norm polarises, and it does not depend on the product beyond the definition; the **antisymmetrisation** is the element $(q'_1q_2-q_1q'_2)j$ of the split imaginary line. In particular the symmetrisation recovers the scalar form $g(Q_1,Q_2) = q_1q_2-q'_1q'_2$ from the sesquilinear product, and the antisymmetrisation is the commutator halved.

**Proof.** $Q_1\bar Q_2 + Q_2\bar Q_1 = 2(q_1q_2-q'_1q'_2)$ and $Q_1\bar Q_2 - Q_2\bar Q_1 = 2(q'_1q_2-q_1q'_2)j$, from the theorem above.

**Theorem (the bracket).** The commutator defines an antisymmetric $\mathbb{R}$-bilinear bracket $[Q_1,Q_2] = Q_1\bar Q_2 - Q_2\bar Q_1$ on the two-dimensional real space, valued in $j\mathbb{R}_{\mathbb{D}}$ and non-degenerate in the sense that its centre is $\{0\}$. With it, $\mathbb{D}$ is the two-dimensional non-abelian Lie algebra, and the **Jacobi identity** holds:

$$
[[Q_1,Q_2],Q_3] + [[Q_2,Q_3],Q_1] + [[Q_3,Q_1],Q_2] = 0 \qquad \text{for all } Q_1,Q_2,Q_3 \in \mathbb{D}.
$$

**Proof.** Antisymmetry is $[Q_2,Q_1] = Q_2\bar Q_1 - Q_1\bar Q_2 = -[Q_1,Q_2]$. Bilinearity over $\mathbb{R}$ is additivity together with $[Q_1,\lambda Q_2] = Q_1\overline{\lambda Q_2} - (\lambda Q_2)\bar Q_1 = \lambda(Q_1\bar Q_2 - Q_2\bar Q_1) = \lambda[Q_1,Q_2]$ for real $\lambda$, since $\bar\lambda = \lambda$. Write $[Q_1,Q_2] = -2\omega(Q_1,Q_2)\,j$ with the area form $\omega(Q_1,Q_2) = q_1q'_2-q'_1q_2$; since $j$ is central and $[j,Q_3] = j\bar Q_3 - Q_3\bar j = 2j\,\operatorname{Sc}(Q_3)$, the cyclic sum is

$$
-4j\big(\omega(Q_1,Q_2)\operatorname{Sc}(Q_3) + \omega(Q_2,Q_3)\operatorname{Sc}(Q_1) + \omega(Q_3,Q_1)\operatorname{Sc}(Q_2)\big),
$$

and the parenthesis is $q_1q'_2q_3 - q'_1q_2q_3 + q_2q'_3q_1 - q'_2q_3q_1 + q_3q'_1q_2 - q'_3q_1q_2 = 0$, the six terms cancelling in pairs. So the identity holds. The centre is the kernel of the area form, which is $\{0\}$ because $\omega$ is non-degenerate.

**Remark.** The Jacobi identity is not an accident of $\mathbb{D}$ and not a coincidence of the computation. On a **two-dimensional** real space every antisymmetric bilinear bracket satisfies the identity, whatever its values: a contributing triple must repeat an argument, and the two resulting terms are opposite. The failure of the Jacobi identity is a phenomenon of dimension at least three, and the split-complex space is too small to exhibit it. What plays the role of a failed identity here is the **associator** of the binary product, $[Q_1,Q_2,Q_3] = Q_1\bar Q_2(\bar Q_3-Q_3)$; the ternary product repairs that, as the section above shows.

## Comparison with the Complex Case

The same construction over the complex field reads:

| | $\mathbb{C}$ | $\mathbb{D}$ |
|---|---|---|
| product | $A\bar C$, definite Hermitian | $Q_1\bar Q_2$, indefinite Hermitian |
| symmetrisation | $ac+a'c'$, the Euclidean form | $q_1q_2-q'_1q'_2 = g$, signature $(1,1)$ |
| commutator | $2i(a'c-ac')$, on the imaginary axis $i\mathbb{R}$ | $2(q'_1q_2-q_1q'_2)j$, on the split imaginary line $j\mathbb{R}$ |
| square of the unit direction | $i^2 = -1$ (rotation) | $j^2 = +1$ (hyperbolic) |
| associator | $A\bar C(\bar D-D)$ | $Q_1\bar Q_2(\bar Q_3-Q_3)$ |
| right unit | $1$, no left unit | $1$, no left unit |
| ternary product | $A\bar C D$, Jordan triple | $Q_1\bar Q_2 Q_3$, Jordan triple |

The associator, the right unit and the ternary product are the same formulas in the two cases, because they use only the associativity of the base and the multiplicativity of the conjugation. The difference is entirely in the **form** and in the **direction of the commutator**. In $\mathbb{C}$ the symmetrisation recovers the positive-definite Euclidean form $ac+a'c'$, and the commutator lies on the imaginary axis, the direction of the rotation $i$ with $i^2 = -1$; in $\mathbb{D}$ the symmetrisation recovers the indefinite form $q_1q_2-q'_1q'_2$ of signature $(1,1)$, and the commutator lies on the split imaginary line, the direction of the hyperbolic unit $j$ with $j^2 = +1$. The two signs are the same sign: the flip of the square of the unit is the flip of the definiteness of the form, because the norm and the form are built from the same product by the same conjugation.

On $\mathbb{D}$ the base involution of the coefficient ring is trivial and the ring is commutative, so the formulas simplify: the two halves of the product are a scalar and a split-imaginary element rather than a central scalar and a vector part, and the sandwich monoid is commutative.

## Summary

The split-complex space carries the sesquilinear product $Q_1 \star Q_2 = Q_1\bar Q_2$, $\mathbb{D}$-linear in the first slot and $\bar\cdot$-semilinear in the second; it is the derived operation of the algebra with its conjugation, and it is neither associative nor two-sidedly unital. The element $1$ is a right unit and not a left one, and there is no two-sided unit. The associator is $[Q_1,Q_2,Q_3] = Q_1\bar Q_2(\bar Q_3-Q_3)$, nonzero exactly when the third factor is not real, with the witness $[j,j,j] = 2j$; the ternary product $\{Q_1,Q_2,Q_3\} = Q_1\bar Q_2 Q_3$ restores the Jordan triple identity and makes $\mathbb{D}$ an algebraic $J^{*}$-algebra.

The right multiplications satisfy $R_{Q_1} \circ R_{Q_2} = R_{Q_2Q_1}$ and form the opposite monoid of $(\mathbb{D},\cdot)$; the left multiplications satisfy $L_{Q_1} \circ L_{Q_2} = M_{Q_1\bar Q_2}$ and do not close, and $L_1$ is the conjugation while $R_1$ is the identity. The sandwich $S_{Q_1,Q_2}(X) = Q_1X\bar Q_2$ is the composite of an ordinary and a sesquilinear multiplication, and the sandwiches form a monoid with $S_{Q_1,Q_2} \circ S_{Q_3,Q_4} = S_{Q_1Q_3,Q_2Q_4}$. With respect to the Hermitian form $\langle Q_1,Q_2\rangle_{*} = Q_1\bar Q_2$, the adjoints are $M_Q^{*} = M_{\bar Q}$, $R_Q^{*} = M_Q$, $L_Q^{*} = L_Q$ and $S_{Q_1,Q_2}^{*} = S_{Q_2,Q_1}$; the two projections onto the idempotent lines are mutually adjoint.

The commutator is $Q_1\bar Q_2 - Q_2\bar Q_1 = 2(q'_1q_2-q_1q'_2)j$, an element of the split imaginary line, and its halves are the scalar form $g(Q_1,Q_2) = q_1q_2-q'_1q'_2$ and the element $(q'_1q_2-q_1q'_2)j$. The bracket is the two-dimensional non-abelian Lie algebra and its Jacobi identity holds, automatically in two dimensions; the obstruction of the binary product is its associator, and the ternary product removes it. Against the complex case the formulas of the associator, unit and ternary product coincide, while the form is definite there and indefinite here and the commutator lies on the rotation axis there and on the hyperbolic line here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split-complex algebra |
| $Q = q + jq'$ | General split-complex number |
| $Q_1 \star Q_2 = Q_1\bar Q_2$ | The sesquilinear product |
| $M_Q(X) = QX$ | Ordinary left multiplication |
| $L_Q(X) = Q\bar X$ | Left multiplication of $\star$, $\bar\cdot$-semilinear |
| $R_Q(X) = X\bar Q$ | Right multiplication of $\star$, $\mathbb{D}$-linear |
| $[Q_1,Q_2,Q_3] = (Q_1\star Q_2)\star Q_3 - Q_1\star(Q_2\star Q_3) = Q_1\bar Q_2(\bar Q_3-Q_3)$ | Associator |
| $\{Q_1,Q_2,Q_3\} = Q_1\bar Q_2 Q_3$ | Ternary product, an algebraic $J^{*}$-algebra |
| $S_{Q_1,Q_2}(X) = Q_1X\bar Q_2 = M_{Q_1} R_{Q_2}$ | Sesquilinear sandwich |
| $\langle Q_1,Q_2\rangle_{*} = Q_1\bar Q_2$ | Hermitian form, used for the adjoints |
| $M_Q^{*} = M_{\bar Q}$, $R_Q^{*} = M_Q$, $L_Q^{*} = L_Q$, $S_{Q_1,Q_2}^{*} = S_{Q_2,Q_1}$ | Adjoints |
| $[Q_1,Q_2] = Q_1\bar Q_2 - Q_2\bar Q_1 = 2(q'_1q_2-q_1q'_2)j$ | Commutator, on the split imaginary line |
| $g(Q_1,Q_2) = \tfrac12(Q_1\bar Q_2 + Q_2\bar Q_1) = q_1q_2-q'_1q'_2$ | Symmetrisation, the scalar form polarised by the norm |

## Further Reading

- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, Grundlehren der mathematischen Wissenschaften 294, 1991), for sesquilinear products, forms and adjoints over a ring with involution.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, Colloquium Publications 39, 1968), for the Jordan triple identity and the algebraic $J^{*}$-algebras of the model $xy^{*}z$.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the associator, the one-sided multiplications and the structural use of the derived operation.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for semilinear maps, modules over a ring with involution and the conjugate structure.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the split-complex plane, its area form and its hyperbolic unit.
