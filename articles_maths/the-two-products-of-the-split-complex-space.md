# __The Two Products of the Split-Complex Space__

## Introduction

The split-complex space carries two products: the plain one, $AC$, and the sesquilinear one, $A\bar C$. The ring has one nontrivial involution, the bar, and no vector part, so a product read off the ring is fixed by where the bar sits: on neither slot, which gives $AC$, or on one, which gives $A\bar C$ and its conjugate $\bar AC$. This article writes the two on the coordinates and on the idempotent coordinates, states what fixes each of them, computes their laws and their pairings, and isolates the point that separates the split case from the complex one.

The separation is not the count. Over the complex field the same two products exist, and exactly two products are built from a commutative ring with one involution in either case. The separation is the **values**: over $\mathbb{C}$ the sesquilinear product is positive definite and its diagonal is a modulus, while over $\mathbb{C}_{\mathrm{spl}}$ it is indefinite, vanishes on two lines, and reads as a componentwise multiplication in the idempotent coordinates.

The algebra is *Split-Complex Algebra*, the idempotents *Square Roots of One and the Idempotents of the Split-Complex Algebra*, the law of the second product *The Specificities of the Split-Complex Algebra*. The two products continue in *The Ternary Product and the Associator of the Split-Complex Space* and in *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*.

## The Two Products

**Proposition.** The space carries exactly two products, the plain $AC$ and the sesquilinear $A\bar C$.

*Proof.* The bar is the only nontrivial involution of the ring, so a product of the space has the bar on neither slot or on one of them. On neither it is $AC$; on the second it is $A\bar C$; on the first it is $\bar AC=\overline{A\bar C}$, the conjugate of the second, and a conjugate is not a new operation. The two remaining products are distinct because they differ on the split imaginary line.

On the coordinates, for $A=a+bj$ and $C=c+dj$,

$$
\boxed{\; AC=(ac+bd)+(ad+bc)j, \qquad A\bar C=(ac-bd)+(bc-ad)j \;}
$$

for $A=a+bj$ and $C=c+dj$. The first is the multiplication of the ring; the second is the ring multiplication composed with the conjugation in the second slot.

## The Two Products on the Coordinates

### The Plain Product

The plain product has the coordinates

$$
AC=(ac+bd)+(ad+bc)j ,
$$

and it is the product of the ring: commutative, associative, with the two-sided unit $1$. Its real part is $ac+bd$ and its split imaginary part is $ad+bc$, the two entries of a multiplication of the form $\begin{pmatrix}a&b\\b&a\end{pmatrix}\begin{pmatrix}c&d\\d&c\end{pmatrix}$.

### The Sesquilinear Product

The sesquilinear product has the coordinates

$$
A\bar C=(ac-bd)+(bc-ad)j ,
$$

because $(a+bj)(c-dj)=ac-ad\,j+bc\,j-bd\,j^2$ and $j^2=1$. The real part is the Minkowski pairing $ac-bd$ and the split imaginary part is the area $bc-ad$; the second product is the first read in the metric of inertia $(1,1)$.

**The two scalar rules.** $A\bar C$ is $\mathbb{C}_{\mathrm{spl}}$-linear in the first slot and $\bar\cdot$-semilinear in the second: for $\lambda\in\mathbb{C}_{\mathrm{spl}}$,

$$
(\lambda A)\bar C=\lambda(A\bar C), \qquad A\overline{\lambda C}=\bar\lambda\,(A\bar C) .
$$

The second rule is the conjugation of the scalar and it is the reason the product is called sesquilinear. In the plain product both slots are linear.

### The Idempotent Coordinates: the Second Product Componentwise

In the idempotent coordinates $Q_\pm=q\pm q'$ the two products are diagonal, and the second one exchanges the index:

$$
(AC)_\pm=A_\pm C_\pm, \qquad (A\bar C)_\pm=A_\pm C_\mp .
$$

**Proof.** $A=A_+\Pi_++A_-\Pi_-$ and $\bar C=C_-\Pi_++C_+\Pi_-$, since $\overline{\Pi_\pm}=\Pi_\mp$, and the idempotents are orthogonal and absorb: multiplying componentwise gives the two formulas.

This is the structural fact of the split case. The plain product is the pair of the two real multiplications, and the sesquilinear product is the same pair with the components crossed. Both are diagonal in the idempotent basis, and no real basis diagonalises the multiplication of $\mathbb{C}$.

## The Two Exchanges and the Absence of an Antisymmetric Part

### Each Product Is Fixed by Its Own Exchange

**Theorem.** The plain product is fixed by the interchange of its slots and the sesquilinear product is fixed by the adapted exchange:

$$
\tfrac12\bigl(AC+CA\bigr)=AC, \qquad \tfrac12\bigl(A\bar C+\overline{C\bar A}\bigr)=A\bar C .
$$

**Proof.** The ring is commutative, so $AC=CA$ and the first sum is $2AC$. For the second, $\overline{C\bar A}=\overline{C}\,A=A\bar C$ again by commutativity, so the sum is $2A\bar C$.

The two identities say that each product is symmetric for the exchange proper to it, and they are the whole of the symmetry theory of the pair. The adapted exchange of the second identity carries the conjugation on the outer slot, which is the exchange the sesquilinear product respects.

### The Antisymmetric Part Is Zero

The antisymmetric part of a product is the difference of the product and its exchanged copy, halved. Both halves vanish:

$$
\tfrac12\bigl(AC-CA\bigr)=0, \qquad \tfrac12\bigl(A\bar C-\overline{C\bar A}\bigr)=0 .
$$

**There is no antisymmetric part.** This is the degenerate case of *The Conjugate-Symmetric and Anti-Conjugate-Symmetric Parts of a Sesquilinear Product*: that article splits a general sesquilinear product into a conjugate-symmetric and an anti-conjugate-symmetric part, and here the second part is zero and the first is the product.

### What $A\bar C-C\bar A$ Is, and What It Is Not

The difference of the sesquilinear product and its transpose is not an antisymmetric part, and it is worth naming what it is:

$$
A\bar C-C\bar A=2(bc-ad)j .
$$

Three reasons keep it out of the symmetry theory. It is not $\mathbb{C}_{\mathrm{spl}}$-linear in the first slot: replacing $A$ by $\lambda A$ multiplies the first term by $\lambda$ and the second by $\bar\lambda$, so the difference is multiplied by neither. It is not the difference of a product and its exchanged copy, the exchange of the sesquilinear product being $\overline{C\bar A}$ and not $C\bar A$. And it takes its values on the split imaginary line, while an antisymmetric part of a product over a commutative ring would take its values in the ring. It is the **area form** of the plane, the determinant $bc-ad$ read as a vector, and it belongs to the section on the sesquilinear product, not to the section on the involution.

## The Laws

### Associativity and the Two-Sided Unit for the Plain Product

The plain product is associative and unital on both sides, because it is the multiplication of an associative ring: $(AC)D=A(CD)$ and $1A=A1=A$. In idempotent coordinates both laws are the associativity and the unit of $\mathbb{R}$ read twice.

### The Right Unit Alone for the Sesquilinear Product

The sesquilinear product has a right unit and no left one:

$$
A\bar 1=A, \qquad 1\bar A=\bar A\neq A \ \text{for} \ A\notin\mathbb{R} .
$$

So the element $1$ is a right unit, and the left unit fails on every element off the real line. In idempotent coordinates the failure is the crossing of the index: the right unit has both coordinates $1$, and the left multiplication by $1$ exchanges them.

### The Associativity Defect

The sesquilinear product is not associative, and the defect is computed in *The Ternary Product and the Associator of the Split-Complex Space*:

$$
(A\bar C)\bar D-A(\overline{C\bar D})=A\bar C\,(\bar D-D) ,
$$

which vanishes exactly when $D$ is real. The defect is confined to the third slot, and it is a defect of the second product alone; the plain product has none.

## The Two Pairings

Each product is also a pairing of two elements with a value in the ring, and the two pairings carry the names $P$ and $H$:

$$
P(A,C)=AC, \qquad H(A,C)=A\bar C .
$$

$P$ is symmetric and $H$ is conjugate-symmetric, by the two exchanges above. The two pairings are the object of *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*, where their realified inertias are computed, and of *The Hermitian Form, the Double Cone and the Reversed Cauchy-Schwarz Inequality*, where the cone of $H$ is read.

## The Point That Separates the Split Case from the Complex One

### The Count Is the Same

On $\mathbb{C}$ the space also carries two products, $AC$ and $A\bar C$, for the same reason: a commutative ring with one involution offers the bar on neither slot, on the second, or on the first, and the last reading is the conjugate of the second. The count of two is the count of the complex case, so it does not separate anything.

### The Values Differ

What separates the two cases is the value of the second product on the diagonal,

$$
A\bar A=a^2-b^2 \ \text{here}, \qquad A\bar A=\lvert A\rvert^2\ \text{on}\ \mathbb{C},
$$

and the value of the first,

$$
A^2=(a^2+b^2)+2ab\,j\ \text{here}, \qquad A^2=(a^2-b^2)+2ab\,i\ \text{on}\ \mathbb{C} .
$$

Over $\mathbb{C}$ the sesquilinear square is positive definite and vanishes only at the origin; here it is indefinite and vanishes on two lines. Over $\mathbb{C}$ the plain square takes every complex value; here it takes the values of the forward cone $a^2\ge b^2$ and no others, which is *The Square Map of the Split-Complex Space*. The two products are the same two maps in both cases, and their values are exchanged in the sense that the definite one and the indefinite one swap places.

### The Second Product Is Componentwise

The reason the values differ is the idempotent coordinates. Over $\mathbb{C}$ the multiplication by an element is not diagonal in any real basis, so no coordinate reads a product componentwise. Here the idempotent basis diagonalises both products, the plain one with the index and the sesquilinear one against it, and every computation of the category is a computation with two real numbers. That is the whole of the difference, and it is why the split algebra is read as $\mathbb{R}\times\mathbb{R}$ and the complex field is not.

## Summary

The split-complex space carries two products, the plain $AC=(ac+bd)+(ad+bc)j$ and the sesquilinear $A\bar C=(ac-bd)+(bc-ad)j$, and no third, the bar being the only involution and the reading with the bar in the first slot being the conjugate of the sesquilinear product. The count of two is the count the complex field also has.

Each product is fixed by its own exchange, the interchange for the plain product and the adapted exchange $A\star C\mapsto\overline{C\star A}$ for the sesquilinear one, so both antisymmetric parts vanish identically. There is no antisymmetric part on the split-complex space. The difference $A\bar C-C\bar A=2(bc-ad)j$ is not an antisymmetric part: it is the area form, it is not linear in the first slot, and it belongs to the section on the sesquilinear product.

The plain product is associative and two-sidedly unital; the sesquilinear one has a right unit and no left unit, and its associativity defect is $A\bar C(\bar D-D)$. The two forms $P(A,C)=AC$ and $H(A,C)=A\bar C$ are symmetric and conjugate-symmetric. The point that separates the split case from the complex one is the value and not the count: $A\bar A=a^2-b^2$ is indefinite here and definite there, and the idempotent coordinates make the second product componentwise, which is why the split algebra is $\mathbb{R}\times\mathbb{R}$ read twice.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $AC=(ac+bd)+(ad+bc)j$ | The plain product, the multiplication of the ring |
| $A\bar C=(ac-bd)+(bc-ad)j$ | The sesquilinear product, the second slot conjugated |
| $(AC)_\pm=A_\pm C_\pm$ | The plain product in idempotent coordinates |
| $(A\bar C)_\pm=A_\pm C_\mp$ | The sesquilinear product in idempotent coordinates |
| $A\bar C-C\bar A=2(bc-ad)j$ | The area form, not an antisymmetric part |
| $P(A,C)=AC$, $H(A,C)=A\bar C$ | The two forms |
| $A\bar C(\bar D-D)$ | The associativity defect of the sesquilinear product |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for a product with an involution in the second slot, the sesquilinear laws and the unit.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, Colloquium Publications 44, 1998), for the products attached to an algebra with an involution and their behaviour over a commutative ring.
- Tonny A. Springer and Ferdinand D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups* (Springer, 2000), for the sesquilinear products of composition algebras and their isotopy.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the split-complex algebra as a Clifford algebra and the two products as the two Clifford products of its even part.
