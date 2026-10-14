# __The Sesquilinear Product of the Split-Complex Space__

## Introduction

The underlying real space of the split-complex algebra carries a second multiplication beside the plain one. It is

$$
A \star C = A\bar C ,
$$

the product whose second slot is read through the conjugation, and it is the **general plain sesquilinear product** of the space: $\mathbb{D}$-linear in the first argument, $\bar\cdot$-semilinear in the second, additive in each. This article builds the **sesqualgebra** it defines. Unlike the plain product it is neither associative nor two-sidedly unital, and the structure that survives is the one that does not need associativity: the right unit alone, the associator, the ternary product, the two families of one-sided multiplications, the sandwich, the adjoint with respect to the Hermitian form, and the commutator with its symmetrisation.

The results are simpler than in the four-dimensional case and sharper than in the complex one. The product has a right unit and no left one, and its associator is

$$
(A \star C) \star D - A \star (C \star D) = A\bar C\,(\bar D - D),
$$

which vanishes exactly when the third factor is real; the ternary product $\{A,C,D\} = A\bar C D$ restores the Jordan triple identity and makes $\mathbb{D}$ an algebraic $J^{*}$-algebra. The right multiplications $R_A$ generate the opposite monoid of the multiplicative monoid of $\mathbb{D}$, while the left ones $L_A$ do not close; the sandwich $A \mapsto BA\bar C$ decomposes into one ordinary and one sesquilinear multiplication and is adjoint to the sandwich with the parameters exchanged; and the commutator $A\bar C - C\bar A = 2(a'c - ac')j$ lies on the split imaginary line, its halved antisymmetrisation is the area form and its symmetrisation is the scalar form $ac - a'c'$ that the norm polarises. The bracket defined by the commutator satisfies the Jacobi identity.

**Placement.** The article opens the split-complex general-plain-sesqualgebra block, after the general-plain-algebra block; the two products as a family and the collapse to two are *The Two Products of the Split-Complex Space*, and the slot reading of the two products, with the two pairings and the two adjoints they carry, is *Relations and Comparison Between the Two Products of the Split-Complex Space*, above this article in this category. The form theory of the second slot — $H$ as a form on the regular module, the positivity cone, the modules and the Witt group — is *The Hermitian Form and the Cone of the Split-Complex Algebra*, below this article in this category. The multiply-unrelated material is *Split-Complex Algebra*, which owns the plain product, and *Split-Complex Norm and Invertibility*.

**Conventions.** The algebra is $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, basis $1$, $j$, $j^2 = +1$, general element $A = a+ja'$, conjugate $\bar A = a-ja'$, idempotents $\Pi_{1,2} = \tfrac12(1\pm j)$, idempotent coordinates $A_\pm = a\pm a'$. The product is written with a star, $A \star C = A\bar C$, and never with a bare juxtaposition, which is reserved for the plain product; the conjugation is never written as an operator symbol. The involution of the algebra is the bar, the coefficients being real and the idempotent swap coinciding with it, so the symbol $*$ of the general theory is realised here by the bar alone; the words **linear** and **conjugate-linear** are read over the ring $(\mathbb{D},\bar\cdot)$, in the sense of the two scalar rules below.

## The Product and Its Two Slots

### The Rule

**Definition.** The **sesquilinear multiplication** of the split-complex space is

$$
\star \; : \; \mathbb{D} \times \mathbb{D} \longrightarrow \mathbb{D}, \qquad
(A,C) \longmapsto A \star C = A\bar C ,
$$

the general plain sesquilinear product of *The Two Products of the Split-Complex Space*. On the coordinates,

$$
A \star C = (a+ja')(c-jc') = (ac-a'c') + (a'c-ac')j .
$$

### The Two Scalar Rules

**Proposition.** The multiplication is additive in each variable; it is $\mathbb{D}$-linear in the first and $\bar\cdot$-semilinear in the second:

$$
(\lambda A) \star C = \lambda\,(A \star C), \qquad
A \star (\lambda C) = \bar\lambda\,(A \star C), \qquad \lambda \in \mathbb{D}.
$$

**Proof.** Additivity and the first rule are the distributivity of $\mathbb{D}$ in the first slot, which is not conjugated. For the second, $A \star (\lambda C) = A\overline{\lambda C} = A\bar\lambda\bar C = \bar\lambda\,A\bar C$, using the multiplicativity of the conjugation and the commutativity of $\mathbb{D}$.

These are the two axioms of a sesquilinear product over the ring with involution $(\mathbb{D},\bar\cdot)$ and nothing else: neither associativity nor commutativity nor a two-sided unit is assumed. One word on the base, because on $\mathbb{D}$ the rules are less visible than over $\mathbb{C}$: the base field is $\mathbb{R}$ and the conjugation is $\mathbb{R}$-linear, so over $\mathbb{R}$ alone the map $A\bar C$ is bilinear, and the content of "sesquilinear" is the action of the *ring* $(\mathbb{D},\bar\cdot)$ on its regular module. The second rule is the statement that the second slot is twisted by the ring involution; it is the only place where an involution enters.

### The Multiplication Table

**Proposition.** On the basis elements $1, j$ the multiplication is

| $\star$ | $1$ | $j$ |
|---|---|---|
| $1$ | $1$ | $-j$ |
| $j$ | $j$ | $-1$ |

**Proof.** $1 \star 1 = \bar 1 = 1$, $1 \star j = \bar j = -j$, $j \star 1 = j$, and $j \star j = j\bar j = -j^2 = -1$.

The table is not the multiplication table of the algebra: on the plain product one has $j \cdot j = +1$, while here $j \star j = -1$. The diagonal is $1,-1$ rather than $1,1$, and the first row is the conjugation, $1 \star A = \bar A$, while the first column is the identity, $A \star 1 = A$. The asymmetry between the two off-diagonal entries is the visible form of the second scalar rule.

### The Right Unit and the Absence of a Two-Sided Unit

**Proposition.** The element $1$ is a **right unit**: $A \star 1 = A$ for every $A$. It is not a left unit: $1 \star A = \bar A$, which differs from $A$ unless $A$ is real.

**Proof.** $A \star 1 = A\bar 1 = A$, and $1 \star A = \bar A$, which equals $A$ for every $A$ only if the conjugation is the identity, which it is not; the witness is $1 \star j = -j \neq j$.

**Corollary.** The multiplication has **no two-sided unit**. An element $E$ with $E \star C = C$ for all $C$ would give $E = 1$ from $C$ real, and then $1 \star C = C$ for all $C$ would force the conjugation to be the identity; so no element is simultaneously a left and a right unit.

The one-sided unit is the mark of a derived operation: the left action by $1$ is the involution, and the right action is the identity. It is not a defect of $\mathbb{D}$ but the consequence of the involution sitting in the second slot, exactly as the general theory of sesqualgebras proves for the standard example. It has a further consequence that recurs below: since $1$ is a right unit, no nonzero element annihilates the whole space on the left, for $A \star 1 = A$; the product is faithful on the left.

## The Associator and the Ternary Product

### The Associator

**Definition.** The **associator** of the multiplication is

$$
[A,C,D] = (A \star C) \star D - A \star (C \star D).
$$

**Theorem.** For all $A,C,D \in \mathbb{D}$,

$$
[A,C,D] = A\bar C\,(\bar D - D),
$$

an element of $\mathbb{D}$ that vanishes exactly when $A = 0$, or $C = 0$, or $D$ is real.

**Proof.** The first bracket is $(A\bar C)\bar D = A\bar C\bar D$ and the second is $A\overline{(C\bar D)} = A\bar C D$, so the difference is $A\bar C(\bar D - D)$. The factor $\bar D - D = -2a'_D\,j$ vanishes exactly when $D \in \mathbb{R}_{\mathbb{D}}$, and the product $A\bar C$ vanishes exactly when $A\bar C = 0$, which for the plain product means $A = 0$ or $C = 0$ or one of them is a zero divisor of the algebra; on the products with $A\bar C \neq 0$ the associator is nonzero precisely when $D$ is not real.

**Corollary.** The multiplication is **not associative**. The associativity defect is confined to the second factor's action on the third: the two groupings agree whenever the third argument is real, and differ otherwise.

**Witness.** On the triple $(j,j,j)$,

$$
(j \star j) \star j = (-1) \star j = j, \qquad
j \star (j \star j) = j \star (-1) = -j,
$$

and the two differ by $2j$. The associator is $[j,j,j] = 2j$.

The shape of the formula is the general one for a derived operation $A\bar C$, with the difference $\bar D - D$ of the two parities of the third factor in place of the associativity that the plain product has. It is the sesquilinear counterpart of the double product's failure, and it is confined to the sesquilinear shape: the plain product of $\mathbb{D}$ is associative.

### The Ternary Product and the Jordan Triple Identity

**Definition.** The **ternary product** attached to the multiplication is

$$
\{A,C,D\} = (A \star C) \star \bar D = A\bar C D ,
$$

the middle slot carrying the involution and the two outer slots not.

**Theorem.** The ternary product is additive in each variable, $\mathbb{D}$-linear in the first and the third and $\bar\cdot$-semilinear in the second, and it satisfies the **Jordan triple identity**

$$
\{A,C,\{D,E,F\}\} = \{\{A,C,D\},E,F\} - \{D,\{C,A,E\},F\} + \{D,E,\{A,C,F\}\} ,
$$

so $\mathbb{D}$ with this ternary product is an **algebraic $J^{*}$-algebra**.

**Proof.** The first clause is the two scalar rules read in the three slots. For the identity, expand both sides with $\{X,Y,Z\} = X\bar Y Z$: the left side is $A\bar C D\bar E F$, and the right side is $A\bar C D\bar E F - D\bar C A\bar E F + D\bar E A\bar C F$; the three terms are products of the six elements with the conjugation on the second factor of each triple, and the identity is the associativity of the plain product together with the commutativity of $\mathbb{D}$, which allow the terms $-D\bar C A\bar E F$ and $+D\bar E A\bar C F$ to cancel against the first. The verification is the model computation $xy^{*}z$ of an associative algebra with a sesquilinear involution, which is the standard example of an algebraic $J^{*}$-algebra; the general theorem is the one the general theory quotes.

So the ternary product is the binary multiplication's surviving form: it is associative-like in the only sense available, since the binary product is not associative, and its identities hold where the binary ones fail. The same identity holds for the same model $PQ^{*}R$ here, with the middle slot conjugated. The failure is the *associativity* of the binary product, recorded above; the ternary product repairs it.

## The Left and Right Multiplications

### The Two Families

**Definition.** The **left** and **right multiplications** by $A \in \mathbb{D}$ are the maps

$$
L_A : X \mapsto A \star X = A\bar X, \qquad
R_A : X \mapsto X \star A = X\bar A .
$$

The right multiplication $R_A$ is $\mathbb{D}$-linear, being a product with $A$ and the conjugation of the fixed factor $A$; the left multiplication $L_A$ is $\bar\cdot$-semilinear, the conjugation falling on the variable. Special values:

$$
L_1 = \overline{\cdot} \quad (\text{the conjugation}), \qquad R_1 = \mathrm{id}.
$$

So the two families do not coincide, and the difference is exactly the involution: $L_A - R_A$ is the involution composed with a multiplication.

### The Opposite Monoid

**Proposition.** The right multiplications compose within themselves, reversing the order,

$$
R_A \circ R_C = R_{CA},
$$

and $\{R_A : A \in \mathbb{D}\}$ is a monoid isomorphic to the opposite monoid $(\mathbb{D},\cdot)^{\mathrm{opp}}$ via $A \mapsto R_A$, with identity $R_1$.

**Proof.** $R_A(R_C X) = (X\bar C)\bar A = X\bar C\bar A = X\overline{AC} = R_{CA}(X)$, using the multiplicativity of the conjugation; the map $A \mapsto R_A$ is then an anti-homomorphism with $A=1$ giving the identity.

**Proposition.** The left multiplications do not compose within themselves: their products are ordinary multiplications,

$$
L_A \circ L_C = M_{A\bar C},
$$

where $M_B(X) = BX$ is the ordinary left multiplication. In particular $L_A \circ L_C$ is $\mathbb{D}$-linear, while each $L_A$ is $\bar\cdot$-semilinear, and the product of two of them is the multiplication by $A\bar C$, the value of the sesquilinear product.

**Proof.** $L_A(L_C X) = A\overline{(C\bar X)} = A\bar C X = M_{A\bar C}(X)$.

So the two one-sided families behave differently, and the asymmetry is the one of the general theory: the right family is a monoid, isomorphic to the opposite of the multiplicative monoid of the ring, while the left family is not closed and its products fall back into the ordinary multiplications. This is the split-complex form of the statement that the left and right multiplications fail to coincide and generate an opposite monoid.

### The Sandwich

**Definition.** The **sesquilinear sandwich** by the parameters $B, C \in \mathbb{D}$ is the map

$$
S_{B,C} : X \longmapsto B\,X\,\bar C .
$$

It is the composite of the ordinary left multiplication $M_B(X) = BX$ and the sesquilinear right multiplication $R_C(X) = X\bar C$,

$$
S_{B,C} = M_B \circ R_C = R_C \circ M_B ,
$$

the two orders agreeing because $\mathbb{D}$ is commutative, and it is therefore the split-complex form of the sandwich $A \mapsto BA\bar C$. The parameters specialise as

$$
S_{1,1} = \mathrm{id}, \qquad S_{B,1} = M_B, \qquad S_{1,C} = R_C, \qquad S_{B,C}(1) = B\bar C = B \star C ;
$$

the sandwich at the unit is the product, and the two families of one-sided multiplications are the two degenerate sandwiches.

**Proposition.** The sandwich is $\mathbb{D}$-linear in $X$, and its value at $1$ is the sesquilinear product $B \star C$. Its composite with another sandwich is again a sandwich,

$$
S_{B,C} \circ S_{D,E} = S_{BD,\,CE} .
$$

**Proof.** Direct substitution, using the associativity of the plain product and the multiplicativity of the conjugation: $S_{B,C}(S_{D,E}(X)) = B(DX\bar E)\bar C = (BD)X\bar E\bar C = (BD)X\overline{CE} = S_{BD,CE}(X)$.

So the sandwiches form a monoid under composition, isomorphic to the product of the multiplicative monoid of $\mathbb{D}$ with itself via $(B,C) \mapsto S_{B,C}$; in particular the sandwich $S_{B,C}$ is invertible exactly when both $B$ and $C$ are units, with inverse $S_{B^{-1},C^{-1}}$.

## The Hermitian Form and the Adjoints

**Definition.** The **Hermitian form** of the regular module is

$$
H(A,C) = A \star C = A\bar C .
$$

It is conjugate-symmetric, $H(C,A) = \overline{H(A,C)}$, $\mathbb{D}$-linear in the first slot and $\bar\cdot$-semilinear in the second. It is the canonical form of *The Hermitian Form and the Cone of the Split-Complex Algebra*, below this article in this category, which owns its Gram matrix, its signature, its positivity cone and its modules; here it is used only as the form that defines the adjoints. Its realified scalar part is

$$
\operatorname{Sc} H(A,C) = ac - a'c' ,
$$

the symmetric bilinear form $g$ that the norm polarises, of signature $(1,1)$.

**Definition (adjoint).** For a $\mathbb{D}$-linear map $T$ the **adjoint** is the $\mathbb{D}$-linear map $T^{*}$ with $H(TX,C) = H(X,T^{*}C)$ for all $X,C$; for a $\bar\cdot$-semilinear map $T$ the adjoint is the $\bar\cdot$-semilinear map $T^{*}$ with $H(TX,C) = \overline{H(X,T^{*}C)}$.

**Theorem.** The adjoints of the one-sided multiplications and of the sandwich are

$$
M_B^{*} = M_{\bar B}, \qquad R_C^{*} = M_C, \qquad L_A^{*} = L_A, \qquad S_{B,C}^{*} = S_{C,B} .
$$

In particular the ordinary multiplication by a real element is self-adjoint, $M_t^{*} = M_t$ for $t \in \mathbb{R}$; the left multiplication is self-adjoint; and the sandwich is adjoint to the sandwich with the parameters exchanged.

**Proof.** Compute each defining identity.
- $H(M_B X, C) = (BX)\bar C = BX\bar C$ and $H(X, M_{\bar B} C) = X\overline{\bar B C} = X B\bar C$, equal by commutativity.
- $H(R_C X, D) = (X\bar C)\bar D = X\bar C\bar D$ and $H(X, M_C D) = X\overline{CD} = X\bar C\bar D$, equal.
- $H(L_A X, C) = (A\bar X)\bar C = A\bar X\bar C$ and $\overline{H(X, L_A C)} = \overline{X\overline{A\bar C}} = \bar X A\bar C$, equal, so $L_A$ is self-adjoint.
- Since $S_{B,C} = M_B \circ R_C$, its adjoint is $S_{B,C}^{*} = R_C^{*} \circ M_B^{*} = M_C \circ M_{\bar B} = M_{C\bar B}$; and $S_{C,B}(X) = CX\bar B = C\bar B X = M_{C\bar B}(X)$, so the two agree.

**Examples.** Take $B = 1$ and $C = j$: the sandwich is $S_{1,j}(X) = X\bar j = -Xj$, and its adjoint is $S_{j,1}(X) = jX$, as the theorem requires. Take $B = C = \Pi_1$: the sandwich is

$$
S_{\Pi_1,\Pi_1}(X) = \Pi_1 X \bar\Pi_1 = \Pi_1 X \Pi_2 = 0
$$

for every $X$, since $\bar\Pi_1 = \Pi_2$ and $\Pi_1\Pi_2 = 0$; the zero map is self-adjoint, and indeed $S_{\Pi_1,\Pi_1}^{*} = S_{\Pi_1,\Pi_1}$ because the parameters are equal. Take $B = \Pi_1$ and $C = \Pi_2$: the sandwich is the projection onto the first idempotent line,

$$
S_{\Pi_1,\Pi_2}(X) = \Pi_1 X \bar\Pi_2 = \Pi_1 X \Pi_1 = X_+\Pi_1 ,
$$

and its adjoint is the projection onto the second, $S_{\Pi_2,\Pi_1}(X) = \Pi_2 X \Pi_2 = X_-\Pi_2$. The two projections onto the idempotent lines are therefore mutually adjoint, although they are idempotents of the sandwich monoid and not of the algebra in the same sense.

## The Commutator and the Symmetrisation

**Definition.** The **commutator** of the sesquilinear product is

$$
[A,C] = A \star C - C \star A = A\bar C - C\bar A .
$$

**Theorem.** For all $A = a+ja'$ and $C = c+jc'$,

$$
A\bar C - C\bar A = 2(a'c-ac')\,j = -2(ac'-a'c)\,j ,
$$

an element of the **split imaginary line** $j\mathbb{R}_{\mathbb{D}}$; the coefficient $ac'-a'c$ is the determinant of the coordinate matrix $\left(\begin{smallmatrix}a&a'\\c&c'\end{smallmatrix}\right)$.

**Proof.** $A\bar C = (ac-a'c') + (a'c-ac')j$ and $C\bar A = (ac-a'c') + (ac'-a'c)j$; subtracting, the real parts cancel and the split-imaginary parts add to $2(a'c-ac')j = -2(ac'-a'c)j$.

So the commutator of the sesquilinear product is a hyperbolic vector: it lies on the split imaginary line, the $-1$ eigenspace of the conjugation, and its coefficient is the area form of the plane. This is the exact counterpart of the complex statement, where the commutator lies on the imaginary axis; the difference is the sign of the square, $j^2 = +1$ against $i^2 = -1$, as the comparison section below records.

**Theorem (the symmetrisation and the antisymmetrisation).** The symmetric and antisymmetric halves of the product are

$$
\tfrac12(A\bar C + C\bar A) = ac-a'c' = g(A,C), \qquad
\tfrac12(A\bar C - C\bar A) = (a'c-ac')\,j .
$$

The **symmetrisation** is the real scalar $g(A,C)$, the symmetric bilinear form that the norm polarises, and it does not depend on the product beyond the definition; the **antisymmetrisation** is the element $(a'c-ac')j$ of the split imaginary line. In particular the symmetrisation recovers the scalar form $g(A,C) = ac-a'c'$ from the sesquilinear product, and the antisymmetrisation is the commutator halved.

**Proof.** $A\bar C + C\bar A = 2(ac-a'c')$ and $A\bar C - C\bar A = 2(a'c-ac')j$, from the theorem above.

**Theorem (the bracket).** The commutator defines an antisymmetric $\mathbb{R}$-bilinear bracket $[A,C] = A\bar C - C\bar A$ on the two-dimensional real space, valued in $j\mathbb{R}_{\mathbb{D}}$ and non-degenerate in the sense that its centre is $\{0\}$. With it, $\mathbb{D}$ is the two-dimensional non-abelian Lie algebra, and the **Jacobi identity** holds:

$$
[[A,C],D] + [[C,D],A] + [[D,A],C] = 0 \qquad \text{for all } A,C,D \in \mathbb{D}.
$$

**Proof.** Antisymmetry is $[C,A] = C\bar A - A\bar C = -[A,C]$. Bilinearity over $\mathbb{R}$ is additivity together with $[A,\lambda C] = A\overline{\lambda C} - (\lambda C)\bar A = \lambda(A\bar C - C\bar A) = \lambda[A,C]$ for real $\lambda$, since $\bar\lambda = \lambda$. Write $[A,C] = -2\omega(A,C)\,j$ with the area form $\omega(A,C) = ac'-a'c$; since $j$ is central and $[j,D] = j\bar D - D\bar j = 2j\,\operatorname{Sc}(D)$, the cyclic sum is

$$
-4j\big(\omega(A,C)\operatorname{Sc}(D) + \omega(C,D)\operatorname{Sc}(A) + \omega(D,A)\operatorname{Sc}(C)\big),
$$

and the parenthesis is $ac'd - a'cd + cd'a - c'da + da'c - d'ac = 0$, the six terms cancelling in pairs. So the identity holds. The centre is the kernel of the area form, which is $\{0\}$ because $\omega$ is non-degenerate.

**Remark.** The Jacobi identity is not an accident of $\mathbb{D}$ and not a coincidence of the computation. On a **two-dimensional** real space every antisymmetric bilinear bracket satisfies the identity, whatever its values: a contributing triple must repeat an argument, and the two resulting terms are opposite. The failure of the Jacobi identity is a phenomenon of dimension at least three, and the split-complex space is too small to exhibit it. What plays the role of a failed identity here is the **associator** of the binary product, $[A,C,D] = A\bar C(\bar D-D)$; the ternary product repairs that, as the section above shows.

## Comparison with the Complex Case

The same construction over the complex field reads:

| | $\mathbb{C}$ | $\mathbb{D}$ |
|---|---|---|
| product | $A\bar C$, definite Hermitian | $A\bar C$, indefinite Hermitian |
| symmetrisation | $ac+a'c'$, the Euclidean form | $ac-a'c' = g$, signature $(1,1)$ |
| commutator | $2i(a'c-ac')$, on the imaginary axis $i\mathbb{R}$ | $2(a'c-ac')j$, on the split imaginary line $j\mathbb{R}$ |
| square of the unit direction | $i^2 = -1$ (rotation) | $j^2 = +1$ (hyperbolic) |
| associator | $A\bar C(\bar D-D)$ | $A\bar C(\bar D-D)$ |
| right unit | $1$, no left unit | $1$, no left unit |
| ternary product | $A\bar C D$, Jordan triple | $A\bar C D$, Jordan triple |

The associator, the right unit and the ternary product are the same formulas in the two cases, because they use only the associativity of the base and the multiplicativity of the conjugation. The difference is entirely in the **form** and in the **direction of the commutator**. In $\mathbb{C}$ the symmetrisation recovers the positive-definite Euclidean form $ac+a'c'$, and the commutator lies on the imaginary axis, the direction of the rotation $i$ with $i^2 = -1$; in $\mathbb{D}$ the symmetrisation recovers the indefinite form $ac-a'c'$ of signature $(1,1)$, and the commutator lies on the split imaginary line, the direction of the hyperbolic unit $j$ with $j^2 = +1$. The two signs are the same sign: the flip of the square of the unit is the flip of the definiteness of the form, because the norm and the form are built from the same product by the same conjugation.

On $\mathbb{D}$ the base involution of the coefficient ring is trivial and the ring is commutative, so the formulas simplify: the two halves of the product are a scalar and a split-imaginary element rather than a central scalar and a vector part, and the sandwich monoid is commutative.

## Summary

The split-complex space carries the sesquilinear product $A \star C = A\bar C$, $\mathbb{D}$-linear in the first slot and $\bar\cdot$-semilinear in the second; it is the derived operation of the algebra with its conjugation, and it is neither associative nor two-sidedly unital. The element $1$ is a right unit and not a left one, and there is no two-sided unit. The associator is $[A,C,D] = A\bar C(\bar D-D)$, nonzero exactly when the third factor is not real, with the witness $[j,j,j] = 2j$; the ternary product $\{A,C,D\} = A\bar C D$ restores the Jordan triple identity and makes $\mathbb{D}$ an algebraic $J^{*}$-algebra.

The right multiplications satisfy $R_A \circ R_C = R_{CA}$ and form the opposite monoid of $(\mathbb{D},\cdot)$; the left multiplications satisfy $L_A \circ L_C = M_{A\bar C}$ and do not close, and $L_1$ is the conjugation while $R_1$ is the identity. The sandwich $S_{B,C}(X) = BX\bar C$ is the composite of an ordinary and a sesquilinear multiplication, and the sandwiches form a monoid with $S_{B,C} \circ S_{D,E} = S_{BD,CE}$. With respect to the Hermitian form $H(A,C) = A\bar C$, the adjoints are $M_B^{*} = M_{\bar B}$, $R_C^{*} = M_C$, $L_A^{*} = L_A$ and $S_{B,C}^{*} = S_{C,B}$; the two projections onto the idempotent lines are mutually adjoint.

The commutator is $A\bar C - C\bar A = 2(a'c-ac')j$, an element of the split imaginary line, and its halves are the scalar form $g(A,C) = ac-a'c'$ and the element $(a'c-ac')j$. The bracket is the two-dimensional non-abelian Lie algebra and its Jacobi identity holds, automatically in two dimensions; the obstruction of the binary product is its associator, and the ternary product removes it. Against the complex case the formulas of the associator, unit and ternary product coincide, while the form is definite there and indefinite here and the commutator lies on the rotation axis there and on the hyperbolic line here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split-complex algebra |
| $A = a + ja'$ | General split-complex number |
| $A \star C = A\bar C$ | The sesquilinear product |
| $M_B(X) = BX$ | Ordinary left multiplication |
| $L_A(X) = A\bar X$ | Left multiplication of $\star$, $\bar\cdot$-semilinear |
| $R_C(X) = X\bar C$ | Right multiplication of $\star$, $\mathbb{D}$-linear |
| $[A,C,D] = (A\star C)\star D - A\star(C\star D) = A\bar C(\bar D-D)$ | Associator |
| $\{A,C,D\} = A\bar C D$ | Ternary product, an algebraic $J^{*}$-algebra |
| $S_{B,C}(X) = BX\bar C = M_B R_C$ | Sesquilinear sandwich |
| $H(A,C) = A\bar C$ | Hermitian form, used for the adjoints |
| $M_B^{*} = M_{\bar B}$, $R_C^{*} = M_C$, $L_A^{*} = L_A$, $S_{B,C}^{*} = S_{C,B}$ | Adjoints |
| $[A,C] = A\bar C - C\bar A = 2(a'c-ac')j$ | Commutator, on the split imaginary line |
| $g(A,C) = \tfrac12(A\bar C + C\bar A) = ac-a'c'$ | Symmetrisation, the scalar form polarised by the norm |

## Further Reading

- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, Grundlehren der mathematischen Wissenschaften 294, 1991), for sesquilinear products, forms and adjoints over a ring with involution.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, Colloquium Publications 39, 1968), for the Jordan triple identity and the algebraic $J^{*}$-algebras of the model $xy^{*}z$.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the associator, the one-sided multiplications and the structural use of the derived operation.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for semilinear maps, modules over a ring with involution and the conjugate structure.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the split-complex plane, its area form and its hyperbolic unit.
