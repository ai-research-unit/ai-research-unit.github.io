
# __The Ternary Product of the Complexoid Space__

## Introduction

The sesquilinear product $A\star C = A\bar C$ of the complex space has an associator $[A,B,C] = A\bar B(\bar C - C)$ that does not vanish, so the operation is not a binary multiplication in the strict sense. But the same operation carries a **ternary** product which is the natural companion of a Jordan structure:

$$
\{A,B,C\} = A\,\bar B\,C .
$$

This article develops that three-variable operation on its own: its linearity and conjugate-linearity, its two symmetries, the identity it satisfies, its contractions to the two binary products, and the $J^{*}$-algebra it defines. It is the rank-one, commutative model of the general theory, and it is the article the GPS block of *Complexoid Algebraic Structures* reads for the triple structure.

The ternary product is already met twice: as the derived operation of the general plain sesqualgebra, and as the ternary product of the quaternionic product in the quaternion analogue. What this article adds is the isolated treatment: the operation as an object, its identities, and the reason the commutative base is degenerate. The general theory is *Jordan Triples with an Involution*, *Algebraic J\*-Algebras* and *Introduction to the General Plain Sesqualgebra*; the sesquilinear product itself is *The Sesquilinear Product of the Complexoid Space*.

**Conventions.** $A,B,C,D,E$ are elements of $\mathbb{C}$, $A = a+ia'$; $\bar\cdot$ is the conjugation; the sesquilinear product is $A\star B = A\bar B$; the field product is juxtaposition. The ternary product is written with braces and is the value of a $J^{*}$-triple.

## Definition and Linearity

**Definition.** The **ternary product** of the complex space is the operation

$$
\{\,\cdot\,,\cdot\,,\cdot\,\} : \mathbb{C}\times\mathbb{C}\times\mathbb{C}\longrightarrow\mathbb{C}, \qquad \{A,B,C\} = A\bar B C = (A\star B)\,C = A\,(\bar B C).
$$

It is a composition of the field product with one conjugation in the middle slot; the middle slot is the only slot the conjugation touches.

**Theorem.** The ternary product is **$\mathbb{C}$-linear in the first and third slots** and **conjugate-linear in the second**:

$$
\{zA,B,C\} = z\{A,B,C\}, \qquad \{A,zB,C\} = \bar z\{A,B,C\}, \qquad \{A,B,zC\} = z\{A,B,C\}
$$

for every $z\in\mathbb{C}$.

**Proof.** Each slot enters the expression $A\bar BC$ exactly once, the first and third plainly and the second under the conjugation; scalar multiplication in the first and third slots passes through, and in the second slot passes through as its conjugate.

**Corollary.** The ternary product is additive in each slot; it is a $\mathbb{C}$-trilinear-$\bar{\,}$ map, that is, a $\mathbb{C}$-linear map of $\mathbb{C}\times\bar{\mathbb{C}}\times\mathbb{C}$.

## The Two Symmetries

**Theorem.** The ternary product is **symmetric in the outer slots** and **Hermitian-symmetric**:

$$
\{A,B,C\} = \{C,B,A\}, \qquad\qquad \overline{\{A,B,C\}} = \{\bar A,\bar B,\bar C\} .
$$

In particular it is *not* symmetric in the first and second slots: $\{A,B,C\} = \{B,A,C\}$ holds exactly when $C = 0$ or the product $A\bar B$ is real.

**Proof.** Outer symmetry is commutativity of the field, $A\bar BC = C\bar BA$; Hermitian symmetry is conjugation applied to all three entries, $\overline{A\bar BC} = \bar A B\bar C = \{\bar A,\bar B,\bar C\}$. For the last statement, $\{A,B,C\} - \{B,A,C\} = (A\bar B - B\bar A)C$, which vanishes exactly when $C = 0$ or $A\bar B = B\bar A$; the second condition says that $A\bar B$ equals its own conjugate, that is, is real.

## The Jordan Triple Identity

**Theorem (flatness).** On the commutative base the ternary product is **flat**: the two bracketings of a triple-system product coincide,

$$
\{A,B,\{C,D,E\}\} = \{\{A,B,C\},D,E\} .
$$

**Proof.** With $\{X,Y,Z\} = X\bar YZ$, the left side is $A\bar B(C\bar DE)$ and the right side is $(A\bar BC)\bar DE$; both are the single product $A\bar BC\bar DE$, since the association of commuting scalars is immaterial.

**Theorem (the Jordan triple identity).** The ternary product satisfies the **Jordan triple identity**

$$
\{A,B,\{C,D,E\}\} = \{\{A,B,C\},D,E\} - \{C,\{B,A,D\},E\} + \{C,D,\{A,B,E\}\} .
$$

**Proof.** Expand with $\{X,Y,Z\} = X\bar YZ$. The left side is $A\bar BC\bar DE$. On the right the three terms are

$$
\{\{A,B,C\},D,E\} = A\bar BC\bar DE, \qquad
\{C,\{B,A,D\},E\} = C\bar BA\bar DE, \qquad
\{C,D,\{A,B,E\}\} = C\bar DA\bar BE .
$$

Because $\mathbb{C}$ is commutative, each of the three products is the same scalar product $A\bar BC\bar DE$ rearranged, so the right side is $T - T + T = T$ and equals the left side.

**Remark.** The identity is a theorem of the operation, proved here directly; it is the axiom of a Jordan triple established in *Jordan Triples with an Involution* for the general triple system, and it was additionally verified on random complex triples and quintuples, where it held on every sample.

**Corollary.** On $\mathbb{C}$ the Jordan triple identity holds by an accident of commutativity: the flatness above makes the two correction terms cancel against the first. On a **non-commutative** base the flatness fails and the two correction terms are indispensable. That is the situation of the quaternion analogue, where the ternary product of the quaternionic product carries a non-vanishing associator defect, treated in *The Associator and the Ternary Product of the Quaternionic Product*.

## The Contractions to the Two Products

**Theorem.** Each of the two binary products of the complex space is a contraction of the ternary product:

$$
\{A,1,C\} = AC, \qquad\qquad \{A,B,1\} = A\bar B, \qquad\qquad \{1,B,C\} = \bar BC .
$$

**Proof.** Substitute the unit in the appropriate slot; the conjugation is the identity on $1$.

**Corollary.** The ternary product **contains both** the field product and the sesquilinear product: the field product is the ternary product with the middle slot at the unit, the sesquilinear product is the ternary product with the last slot at the unit. Neither binary product determines the other, and the ternary product determines both.

**Theorem.** For $A$ fixed, the ternary product's outer-slot contraction is the rank-one map

$$
C \longmapsto \{A,C,A\} = A^2\bar C ,
$$

which is $\mathbb{C}$-**antilinear** and whose square is the scalar map $\lvert A\rvert^4\operatorname{id}$.

**Proof.** $\{A,C,A\} = A\bar CA = A^2\bar C$, conjugate-linear in $C$ because conjugation is. Applying it twice, $C\mapsto A^2\bar C\mapsto A^2\overline{A^2\bar C} = A^2\bar A^2 C = \lvert A\rvert^4 C$.

## The $J^{*}$-Algebra Structure

**Definition.** A **$J^{*}$-algebra** (a Jordan triple with an involution) is a complex vector space $V$ with a map $\{\,\cdot\,,\cdot\,,\cdot\,\} : V\times V\times V\to V$ that is $\mathbb{C}$-linear in the first and third slots and conjugate-linear in the second, that is symmetric in the outer slots, and that satisfies the Jordan triple identity.

**Theorem.** With the ternary product above, $\mathbb{C}$ is a $J^{*}$-algebra; it is the **rank-one** example, of complex dimension one.

**Proof.** The three defining properties are the linearity theorem, the outer-symmetry theorem and the Jordan-identity theorem. That the dimension is one and the associated Hermitian form $H(A) = \lvert A\rvert^2$ has rank one is *The Hermitian Form and the Positivity of the Complexoid Algebra*.

**Remark.** The norm condition that promotes an algebraic $J^{*}$-algebra to a Banach $J^{*}$-algebra — the continuity of the triple product and the identity $\lVert\{A,A,A\}\rVert = \lVert A\rVert^3$ in a suitable norm — is a separate layer, and belongs to *Banach Sesqualgebras* and *Fr\'echet and Locally Convex Sesqualgebras*; the algebraic structure treated here is complete without it.

**Remark (the associated Jordan algebra).** The ternary product's symmetrisation in the outer slots returns the Jordan structure of the base: the binary product $A\odot C = \{A,1,C\} + \{C,1,A\}$ is $A\odot C = 2\operatorname{Re}(A\bar C) = A\bar C + C\bar A$, the real part of the Hermitian form, which is the commutative Jordan product of the field's real structure. The ternary layer is thus the operator-algebraic refinement of the Jordan layer, exactly as for a $J^{*}$-algebra in *Jordan Algebras of Sesqualgebras*.

## Summary

The complex space carries a ternary product $\{A,B,C\} = A\bar BC$, $\mathbb{C}$-linear in the first and third slots and conjugate-linear in the second, symmetric in the outer slots and Hermitian-symmetric, and satisfying the Jordan triple identity; with these properties the space is a rank-one $J^{*}$-algebra. The operation is the composition of the sesquilinear product with the field product, $\{A,B,C\} = (A\star B)C$, and it contains both binary products as contractions: $\{A,1,C\} = AC$ is the field product and $\{A,B,1\} = A\bar B$ is the sesquilinear product, so the ternary operation is the finer object from which the two are read.

On the commutative base the triple system is flat, $\{A,B,\{C,D,E\}\} = \{\{A,B,C\},D,E\}$, so the two correction terms of the Jordan triple identity vanish and the identity is satisfied by an accident of commutativity. On a non-commutative base the flatness fails and the correction terms are essential, which is the reason the quaternion analogue of the ternary product carries a non-vanishing associator defect. The symmetrisation of the ternary product in the outer slots returns the real Jordan product $A\odot C = 2\operatorname{Re}(A\bar C)$.

| Structure | Definition | Linearity in the slots |
|---|---|---|
| Field product | $\{A,1,C\} = AC$ | bilinear |
| Sesquilinear product | $\{A,B,1\} = A\bar B$ | $1$ linear, $2$ conjugate-linear |
| Ternary product | $\{A,B,C\} = A\bar BC$ | $1,3$ linear, $2$ conjugate-linear |
| Outer contraction | $\{A,C,A\} = A^2\bar C$ | conjugate-linear |
| Jordan symmetrisation | $A\odot C = \{A,1,C\}+\{C,1,A\}$ | bilinear, symmetric |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\{A,B,C\} = A\bar BC$ | the ternary product |
| $A\star B = A\bar B$ | the sesquilinear product |
| $\bar\cdot$ | complex conjugation |
| $\{A,B,C\} = \{C,B,A\}$ | outer symmetry |
| $\overline{\{A,B,C\}} = \{\bar A,\bar B,\bar C\}$ | Hermitian symmetry |
| $\{A,1,C\}$, $\{A,B,1\}$ | the contractions to the two binary products |
| $J^{*}$-algebra | a Jordan triple with an involution |

## Further Reading

- [The Sesquilinear Product of the Complexoid Space](the-sesquilinear-product-of-the-complexoid-space.html), for the sesquilinear product, its associator and its first reading of the ternary product.
- [The Associator and the Ternary Product of the Quaternionic Product](the-associator-and-the-ternary-product-of-the-quaternionic-product-of-quaternioid.html), for the non-commutative analogue, where the associator defect does not vanish.
- [Introduction to the General Plain Sesqualgebra](introduction-to-the-general-plain-sesqualgebra.html), for the sesqualgebra as a general structure and its ternarisation.
- [Jordan Triples with an Involution](jordan-triples-with-an-involution.html) and *Algebraic J\*-Algebras*, for the axioms of a $J^{*}$-algebra, the Jordan triple identity and the rank-one example.
- [Jordan Algebras of Sesqualgebras](jordan-algebras-of-sesqualgebras.html) and [Hermitian Squares and the Algebraic Positive Cone](hermitian-squares-and-the-algebraic-positive-cone.html), for the Jordan layer and the positive cone attached to the involution.
- [Banach Sesqualgebras](banach-sesqualgebras.html) and [Fréchet and Locally Convex Sesqualgebras](frechet-and-locally-convex-sesqualgebras.html), for the norm conditions that make the algebraic $J^{*}$-algebra a topological one.
- [The Hermitian Form and the Positivity of the Complexoid Algebra](the-hermitian-form-and-the-positivity-of-the-complexoid-algebra.html) and [The Two Forms and the Two Algebraic Norms of the Complexoid Space](the-two-forms-and-the-two-algebraic-norms-of-the-complexoid-space.html), for the Hermitian form and the two algebraic norms of the base.
