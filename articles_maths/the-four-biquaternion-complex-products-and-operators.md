
# __The Four Biquaternion Complex Products and Operators__

## Introduction

The four complex products of $\mathbb{B}$ are four rules that pair two elements, and the corpus gives each of them an operator family: the plain bilinear product the *Association* family, the general quaternionic bilinear product the *Signed Inner Conjugation* family, the general plain sesquilinear product the *Hermitian Adjoint* family, and the general quaternionic sesquilinear product the Krein form, which carries its own indefinite theory rather than a family of the four-adjoint kind. A reader may conclude from that list that the product *decides* the operator, and may then ask whether the product decides whether an element acts as a rotation or as a reflection. **It does not.** The four products have the same multiplication table of the units; they differ only in which conjugation is inserted into which slot of the pair. What they decide is the *pairing*, hence the adjoint, hence the name of the family. The action — a rotation, a reflection, an inner automorphism — is decided by the element and by the inserted sign, and the inserted sign is a choice among the involutions that the algebra already carries.

This article states that division of labour precisely, with the matrices of one element read through all four insertions.

The answer to the question of the title is therefore a negative one, and it agrees with the intuition that the algebra and its product come first and the operator is obtained from them by choosing the element and the insertion. The qualification is that the choice is not arbitrary: on the vector subspace the plain product cannot produce a reflection, only its negative, so that one insertion is *forced* by the algebra and not merely preferred.

The four products, their relations and their comparison are *The Four Biquaternion Complex Products*, *Relations Between the Four Biquaternion Products* and *Comparison Between the Four Biquaternion Products*; the four pairings and their Gram matrices are *The Four Pairings of the Biquaternion Algebra*; the four adjoints and the reading of the family names are *The Four Adjoints of the Biquaternion Algebra in Examples*; the conjugations and their group are *The Group of Involutions*; the Clifford reading of the conjugations is *The Clifford Algebra Representation*; the signed sandwich and its reflection formula are *The Signed Sandwich on a Clifford Algebra* and *Two-Sided Operators with the Signed Product*. The article is pure algebra.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$ and $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$; $i$ is the central scalar imaginary; a general element is $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The three conjugations used are the natural conjugation $\tilde Q^{\natural}=Q_0e_0-Q_1e_1-Q_2e_2-Q_3e_3$, the coefficient conjugation $\bar{\tilde Q}=\overline{Q_0}e_0+\overline{Q_1}e_1+\overline{Q_2}e_2+\overline{Q_3}e_3$, and the Hermitian conjugation $\tilde Q^{*}=\tilde Q^{\natural\bar{\bar{\cdot}}}=\overline{Q_0}e_0-\overline{Q_1}e_1-\overline{Q_2}e_2-\overline{Q_3}e_3$. The vector subspace is $V=\mathbb{C}\{e_1,e_2,e_3\}$, the norm is $N(\tilde Q)=\tilde Q\tilde Q^{\natural}$, an element is a unit exactly when $N(\tilde Q)\ne0$, and $\mathrm{Sc}$ is the scalar part.

## The Four Products Are One Multiplication with Two Insertions

### The Four Rules

**Definition (the four products).** The four products are

$$
\tilde P\tilde Q ,
\qquad
\tilde P^{\natural}\tilde Q ,
\qquad
\tilde P\tilde Q^{*} ,
\qquad
\tilde P^{\natural}\tilde Q^{*} ,
$$

the plain bilinear, the general quaternionic bilinear, the general plain sesquilinear and the general quaternionic sesquilinear product.

**Proposition (one table, two insertions).** The four rules multiply the coordinates on the same products $e_\mu e_\nu$ of the basis. They differ in one point alone: whether the coordinates of each of the two elements are used as they stand or taken from the conjugated element, the two elements being treated independently of one another. Equivalently, the four products are the four members of the orbit

$$
\bigl\{K_1(\tilde P)\,K_2(\tilde Q)\;:\;K_1\in\{\mathrm{id},{}^{\natural}\},\;K_2\in\{\mathrm{id},{}^{*}\}\bigr\}
$$

of a single rule under the insertion of a conjugation into the first slot and a conjugation into the second.

*Proof.* Reading the four definitions side by side, the products $e_\mu e_\nu$ of the basis and the order of the factors are the same in all four; the only difference is the source of $P_\mu$ in the first factor and of $Q_\nu$ in the second. $\square$

**Remark (why "complex products").** The word *complex* records the base field and not a second multiplication: the multiplication of the units is that of $\mathbb{H}$ extended to $\mathbb{C}$, and the four rules move over it. There is no product among the four that is not the plain one with an insertion.

### One Multiplication Table, Four Pairings

**Theorem (the scalar parts are the four pairings).** The scalar parts of the four products are the four pairings of the algebra,

$$
\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q),\quad
\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q),\quad
\langle\tilde P,\tilde Q\rangle_{\ast}=\mathrm{Sc}(\tilde P\tilde Q^{*}),\quad
\langle\tilde P,\tilde Q\rangle_{\natural\ast}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*}),
$$

with Gram matrices in the basis $e_0,e_1,e_2,e_3$ equal to $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$, $\mathrm{I}_4$, $\mathrm{I}_4$ and $\mathrm{E}$.

*Proof.* $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ with $\varepsilon=(1,-1,-1,-1)$, and on the basis units the two insertions act by $e_\mu^{\natural}=\varepsilon_\mu e_\mu$ and $e_\mu^{*}=\varepsilon_\mu e_\mu$, the coefficients being real and equal to $1$. The Gram matrix is therefore $\varepsilon$ exactly when the first slot carries the sign $\natural$, and $1$ when it does not, that is $\mathrm{E},\mathrm{I}_4,\mathrm{I}_4,\mathrm{E}$. The four pairings are distinct as maps — two are bilinear and two sesquilinear in the second argument, and no two agree on complex coefficients — while two pairs of them share a Gram matrix, a Gram matrix seeing the basis units alone, on which the conjugations act by a sign. $\square$

**Corollary (a product is a pairing, not an operator).** The four products endow $\mathbb{B}$ with the four pairings and nothing else. Each of them is a bilinear or a sesquilinear *form*, and a form does not act on the algebra; it pairs two of its elements. Whatever acts is a map, and a map has to be built.

## What the Products Decide and What the Choice Decides

### The Products Decide the Four Adjoints

**Theorem (the four adjoints are decided by the four products).** For the left multiplication $L_{\tilde A}$ the adjoints of the four pairings are

$$
(L_{\tilde A})^{\approx}=R_{\tilde A},\qquad
(L_{\tilde A})^{N}=L_{\tilde A^{\natural}},\qquad
(L_{\tilde A})^{\ast}=L_{\tilde A^{\ast}},\qquad
(L_{\tilde A})^{\natural\ast}=R_{\bar{\tilde A}},
$$

and for the two-sided operator $(L_{\tilde A}R_{\tilde B})^{\approx}=L_{\tilde B}R_{\tilde A}$, $(L_{\tilde A}R_{\tilde B})^{N}=L_{\tilde A^{\natural}}R_{\tilde B^{\natural}}$, $(L_{\tilde A}R_{\tilde B})^{\ast}=L_{\tilde A^{\ast}}R_{\tilde B^{\ast}}$, $(L_{\tilde A}R_{\tilde B})^{\natural\ast}=L_{\bar{\tilde B}}R_{\bar{\tilde A}}$.

*Proof.* *The Four Adjoints of the Biquaternion Algebra in Examples*, where all sixteen cases are verified on the pairs of basis elements. $\square$

So the product *does* decide something of the first importance: which adjoint exists, and therefore which of the four operator families has a coherent adjoint theory. That is the whole content of the naming rule of the corpus, and it is a statement about *forms*.

### The Operator Is Not Decided

**Remark (the missing inputs).** The four products share the table of the units, so no two of them can differ in the way an operator differs from another. To write down an operator one has still to supply

1. an **element** $\tilde A$ of the algebra, and
2. an **insertion**: which involution, if any, is put on the element, and on which side.

The products do not supply 1, and they supply the *repertoire* of 2 without choosing from it. That is the sense in which the operator is chosen by the modeller: given the algebra with its product, one chooses $\natural$, or $\bar{\cdot}$, or ${}^{*}$, or none, and therefore the operator.

## One Element, Four Operators

### The Four Operators of $e_1$

Fix the element $\tilde A=e_1$, a unit with $N(e_1)=-e_0$, so that $e_1^{-1}=-e_1$. Read it through the four insertions, using the inverse of the conjugated element in the right factor:

$$
\begin{aligned}
\text{no insertion:}\quad & L_{e_1}R_{e_1^{-1}} & \tilde X&\longmapsto e_1\tilde X e_1^{-1},\\
\text{sign }\natural\text{ on the left:}\quad & L_{e_1^{\natural}}R_{e_1^{-1}} & \tilde X&\longmapsto e_1^{\natural}\tilde X e_1^{-1},\\
\text{star on the right:}\quad & L_{e_1}R_{(e_1^{*})^{-1}} & \tilde X&\longmapsto e_1\tilde X (e_1^{*})^{-1},\\
\text{both:}\quad & L_{e_1^{\natural}}R_{(e_1^{*})^{-1}} & \tilde X&\longmapsto e_1^{\natural}\tilde X(e_1^{*})^{-1}.
\end{aligned}
$$

For $e_1$ the two conjugations are $\natural(e_1)=-e_1$ and $e_1^{*}=-e_1$, so the four operators are two, and in the basis $e_0,e_1,e_2,e_3$ they are

$$
\operatorname{diag}(1,1,-1,-1)
\quad\text{and}\quad
\operatorname{diag}(-1,-1,1,1),
$$

the first for the two insertions that agree (none or both), the second for the sign on the left or the star on the right alone. On the vector subspace $V$ they restrict to

$$
\operatorname{diag}(1,-1,-1)
\quad\text{and}\quad
\operatorname{diag}(-1,1,1).
$$

**Remark (the four insertions collapse).** For a parameter that one of the conjugations fixes, the four operators are fewer than four: the sign insertion is invisible exactly when $\tilde A^{\natural}=\tilde A$, which holds for the central $\tilde A$, and the star insertion is invisible exactly when $\tilde A^{*}=\tilde A$, which holds for the parameters with real central coefficient and purely imaginary vector coefficients, the fixed space $\mathbb{M}_{+}$ of the Hermitian conjugation. For a vector $\tilde A\in V$ with real coefficients the four operators are two, $\pm L_{\tilde A}R_{\tilde A^{-1}}$; for a generic complex vector of $V$ the four are pairwise distinct. The number of distinct operators is therefore a property of the *element*, and not of the product.

## Rotation, Reflection, and Where the Sign Is Read

### The Plain Product Gives Minus the Reflection

**Theorem (the reflection is reached only through the sign).** Let $\tilde A\in V$ be a vector with $N(\tilde A)\ne0$, and let $\rho_{\tilde A}$ be the reflection of $V$ in the hyperplane $\tilde A^{\perp}$ for the polar form of $q=-\sum_kQ_k^{2}$,

$$
\rho_{\tilde A}(\tilde V)=\tilde V-\frac{2B(\tilde V,\tilde A)}{q(\tilde A)}\,\tilde A .
$$

Then the two insertions that read the parameter as it stands keep $V$ stable, and

$$
L_{\tilde A}R_{\tilde A^{-1}}\big|_{V}=-\rho_{\tilde A},\qquad
L_{\tilde A^{\natural}}R_{\tilde A^{-1}}\big|_{V}=\rho_{\tilde A},
$$

with determinant of the restriction $+1$ and $-1$. The two insertions that read the right factor through ${}^{*}$ behave differently, and the proposition below says exactly how.

*Proof.* For $\tilde A\in V$ the sign reads the parameter as $\tilde A^{\natural}=-\tilde A$, so that $L_{\tilde A^{\natural}}R_{\tilde A^{-1}}=-L_{\tilde A}R_{\tilde A^{-1}}$; the identity $L_{\tilde A}R_{\tilde A^{-1}}\big|_{V}=-\rho_{\tilde A}$ is the reflection formula of the Clifford algebra in the convention $q(\tilde A)=B(\tilde A,\tilde A)<0$, equivalently $\tilde A\tilde V+\tilde V\tilde A=2B(\tilde A,\tilde V)$ and $\tilde A^{2}=q(\tilde A)e_0$. Verified on two hundred random complex vectors: both operators keep $V$ stable without exception, and their restrictions are $-\rho_{\tilde A}$ and $\rho_{\tilde A}$ with no exception. $\square$

**Proposition (the star insertions leave $V$ in general).** For $\tilde A\in V$ the right factor of the starred insertions is $(\tilde A^{*})^{-1}=-(\bar{\tilde A})^{-1}$, so the two starred operators are $-L_{\tilde A}R_{(\bar{\tilde A})^{-1}}$ and $+L_{\tilde A}R_{(\bar{\tilde A})^{-1}}$. They keep $V$ stable exactly when $\bar{\tilde A}$ is a scalar multiple of $\tilde A$, that is when the coefficient vector of $\tilde A$ is a complex multiple of a real one. When it is, and only then, a determinant on $V$ is defined: it is $-1$ for the star insertion and $+1$ for the both insertion when the coefficient vector is real, the two are exchanged when it is purely imaginary, and for a coefficient vector that is a non-real, non-imaginary complex multiple of a real one the restriction is neither $\pm\rho_{\tilde A}$ nor form-preserving. For a generic complex parameter, $V$ is not preserved and the starred insertions are read on the algebra and not on $V$.

*Proof.* Substituting $\tilde A^{*}=-\bar{\tilde A}$ and $\natural(\tilde A)=-\tilde A$ in the four definitions; the equivalences are verified on two hundred random complex vectors, where the starred operators fail to preserve $V$ in every case, and on the collinear parameters $\tilde A=\mu\,\tilde u$ with $\tilde u$ real and $\mu\in\mathbb{C}$. $\square$

**Remark (the sentence of the corpus, translated).** *The Signed Sandwich on a Clifford Algebra* says that the ordinary sandwich by a vector is the **negative** of the reflection, and that inserting the grade involution *repairs the sign*. The theorem above is that sentence in the biquaternion model: the plain product gives $-\rho_{\tilde A}$, the involution of $V$ whose fixed space has codimension one, and the sign insertion gives $\rho_{\tilde A}$. This is the one place where the algebra forces a choice rather than permitting one.

**Corollary (where a determinant plus one lives).** On the algebra $\mathbb{B}$ itself, of complex dimension four, all four operators have determinant $+1$; the sign shows in the determinant only on the odd-dimensional restriction $V$, or on a real form of odd dimension. A "rotation" and a "reflection" are therefore read on $V$.

*Proof.* The operators are products $L_{\tilde A}R_{\tilde B}$, whose determinant on $\mathbb{B}$ is $\det(L_{\tilde A})\det(R_{\tilde B})$, and for a four-dimensional space the sign $-1$ on a parameter contributes the factor $(-1)^{4}=+1$. Verified on the four matrices of $e_1$. $\square$

### The Sign Is Invisible on the Centre and on Even Parameters

**Proposition.** If $\tilde A$ is central, $\tilde A=a_0e_0$, then the sign insertion changes nothing, $L_{\tilde A^{\natural}}R_{\tilde A^{-1}}=L_{\tilde A}R_{\tilde A^{-1}}$. If $\tilde A\in V$ is a vector, the sign insertion negates the operator, $L_{\tilde A^{\natural}}R_{\tilde A^{-1}}=-L_{\tilde A}R_{\tilde A^{-1}}$.

*Proof.* $\natural$ fixes the centre and negates $V$; left multiplication and right multiplication commute. $\square$

**Theorem (the determinant table).** For a unit $\tilde A$ let $d$ be the determinant of the operator restricted to $V$ for the four insertions, in the order (none, sign on the left, star on the right, both). Then

| $\tilde A$ | none | sign | star | both |
|---|---|---|---|---|
| $e_0$ | $+1$ | $+1$ | $+1$ | $+1$ |
| $i e_0$ | $+1$ | $+1$ | $-1$ | $-1$ |
| $e_1$ | $+1$ | $-1$ | $-1$ | $+1$ |
| $e_1+e_2$ | $+1$ | $-1$ | $-1$ | $+1$ |
| $i e_1$ | $+1$ | $-1$ | $+1$ | $-1$ |
| $e_0+e_1$ | $+1$ | $0$ | $0$ | $+1$ |

The zero entries are the starred insertions of a mixed parameter, whose operator does not preserve $V$, so that the restricted determinant is $0$ and is not a rotation-reflection marker; the star and both columns are read on $V$ only for the rows whose parameter has a real or purely imaginary coefficient vector.

*Proof.* The rows are the computed determinants; the first row is the identity on $V$; the second row shows that a central imaginary parameter, on which the sign is invisible, is still separated by the conjugate-linear insertion, $(\tilde A^{*})^{-1}=i e_0$, which gives $-e_0$ on the left factor and hence $-\mathrm{id}$ on $V$; the third and fourth rows are the theorem above; the fifth row is a purely imaginary vector, on which the star insertion coincides with the plain one and the both insertion with the sign, so that the determinants are those of the third row read with the two insertions exchanged; the last row is a mixed parameter, whose starred operators do not keep $V$ stable. $\square$

**Remark (the two central rows).** The proposition and the table together show the two independent choices: the *sign* $\natural$ is invisible on the centre and reads only the odd part, while the *star* is invisible on the real directions and reads the coefficient imaginary. Neither is a property of the product; both are properties of the insertion into the chosen element.

## Which Involution Is "the Sign" Is Itself a Choice

**Remark (the corpus fixes the sign by a formula).** The biquaternion corpus calls $\natural$ the sign and uses it throughout, but the map that plays the role of the sign is a choice among the involutions of the algebra. The identification $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, $\gamma_k\mapsto ie_k$, has the grades $\text{grade }0=\mathbb{R}e_0$, $\text{grade }1=\mathrm{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\}$, $\text{grade }2=\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$, $\text{grade }3=\mathbb{R}ie_0$, and in that reading (*The Clifford Algebra Representation*)

| map on $\mathbb{B}$ | Clifford partner | signs on grades $0,1,2,3$ | coefficient sign vector on $e_0,e_1,e_2,e_3$ |
|---|---|---|---|
| quaternion conjugation $\natural$ | Clifford conjugation $\alpha(X^{r})$ | $+,-,-,+$ | $(1,-1,-1,-1)$ |
| complex conjugation $\bar{\cdot}$ | grade involution $\alpha$ | $+,-,+,-$ | fixes $e_1,e_2,e_3$, reverses $i$ |
| Hermitian conjugation ${}^{*}$ | reversion $X^{r}$ | $+,+,-,-$ | $-1$ on $e_1,e_2,e_3$ and $-1$ on $ie_0$ |

So the corpus's "sign" is the map with the sign vector $(1,-1,-1,-1)$, and it is *not* the grade involution of that Clifford reading: the grade involution is the coefficient conjugation, and on $V$, which is the grade-two part there, it is the identity. Two consequences follow, and both answer the question of the title. First, the corpus's choice of $\natural$ as the sign is a convention of the biquaternion model, fixed by the coefficient formula and not by an abstract parity. Second, the reflection theorem is nevertheless not a convention: with the sign $\natural$ it holds, and with the grade involution, which is trivial on $V$, it fails.

**Remark (parameter or argument).** The sign may be inserted in the **parameter**, $L_{\tilde A^{\natural}}R_{\tilde A^{-1}}$, which is the *signed inner conjugation* of the corpus, or in the **argument**, $\tilde X\mapsto\tilde A\,\tilde X^{\natural}\,\tilde A^{-1}$, which is the *signed sandwich* of *The Signed Sandwich on a Clifford Algebra*. On the vector subspace the two agree, because both act by the sign $-\mathrm{id}$ there; on the whole algebra they differ, and the general corpus keeps the two families apart on purpose, the one twisting the parameter and the other the argument.

## Summary

The four complex products of the biquaternion algebra are one multiplication with a conjugation inserted independently into each of the two slots. They therefore share the multiplication table of the units, and they determine the four pairings — their scalar parts — and with the pairings the four adjoints and the names of the four operator families. They do not determine an operator. An operator needs an element, and it needs an insertion: which involution, if any, is put on the element and on which side, and whether the sign goes into the parameter or into the argument. The element $e_1$ read through the four insertions gives two operators, $\operatorname{diag}(1,1,-1,-1)$ and $\operatorname{diag}(-1,-1,1,1)$, and on the vector subspace they are $-\rho_{e_1}$ and $\rho_{e_1}$: the plain product gives $-\rho_{e_1}$, and the reflection is reached only through the sign. On the four-dimensional algebra both have determinant $+1$, so rotation and reflection are read on the vector subspace. Finally, which map plays the role of the sign is itself chosen: the biquaternion corpus fixes it as the natural conjugation $\natural$, whose sign vector is $(1,-1,-1,-1)$, and that is a convention of the model, whereas the identity "the reflection needs the sign" is a theorem. The answer to the question is therefore: no, the product does not decide between a rotation and a reflection; the algebra and its product come first, and the operator is obtained from them by choosing the element and the insertion.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\tilde Q$, $\tilde P^{\natural}\tilde Q$, $\tilde P\tilde Q^{*}$, $\tilde P^{\natural}\tilde Q^{*}$ | the four products: one table, the two insertions |
| $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{\ast}$, $\langle\cdot,\cdot\rangle_{\natural\ast}$ | their scalar parts, the four pairings, Gram matrices $\mathrm{E},\mathrm{I}_4,\mathrm{I}_4,\mathrm{E}$ |
| ${}^{\approx}$, ${}^{N}$, ${}^{*}$, ${}^{\natural\ast}$ | the four adjoints, decided by the four products |
| $\natural$, $\bar{\cdot}$, ${}^{*}$ | the sign, the coefficient conjugation, the Hermitian conjugation; $\natural$ has sign vector $(1,-1,-1,-1)$ |
| $L_{\tilde A}R_{\tilde B}$ | a two-sided operator; $L_{\tilde A}R_{\tilde A^{-1}}$ the inner automorphism of the plain product |
| $L_{\tilde A^{\natural}}R_{\tilde A^{-1}}$, $\tilde X\mapsto\tilde A\tilde X^{\natural}\tilde A^{-1}$ | the sign inserted in the parameter, and in the argument |
| $\rho_{\tilde A}$ | the reflection of $V$ in $\tilde A^{\perp}$; the plain product gives $-\rho_{\tilde A}$, the sign gives $\rho_{\tilde A}$ |
| $\operatorname{diag}(1,1,-1,-1)$, $\operatorname{diag}(-1,-1,1,1)$ | the two operators of $e_1$, and their restrictions $\operatorname{diag}(1,-1,-1)$, $\operatorname{diag}(-1,1,1)$ to $V$ |

## Further Reading

- *The Four Biquaternion Complex Products* (`articles_maths/the-four-biquaternion-complex-products.md`), for the four rules and the statement that they differ in one point alone
- *Comparison Between the Four Biquaternion Products* (`articles_maths/comparison-between-the-four-biquaternion-products.md`), for the table of the four rules side by side
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four forms, their Gram matrices and their adjoints
- *The Four Adjoints of the Biquaternion Algebra in Examples* (`articles_maths/the-four-adjoints-of-the-biquaternion-algebra-in-examples.md`), for the four adjoints on explicit operators and the naming rule of the operator families
- *The Group of Involutions* (`articles_maths/the-group-of-involutions.md`), for the four conjugations and their group
- *The Clifford Algebra Representation* (`articles_maths/the-clifford-algebra-representation.md`), for the grades and the dictionary between the conjugations and the Clifford anti-involutions
- *The Signed Sandwich on a Clifford Algebra* (`articles_maths/the-signed-sandwich-on-a-clifford-algebra.md`), for the ordinary sandwich, its minus sign and the repair by the grade involution
- *Two-Sided Operators with the Signed Product* (`articles_maths/two-sided-operators-with-the-signed-product.md`), for the signed family, its twisted composition law and its coset structure
- *Two-Sided Operators on the General Quaternionic Algebra of Biquaternions* (`articles_maths/two-sided-operators-on-the-general-quaternionic-algebra-of-biquaternions.md`), for the parameter insertion in the biquaternion model
- *The Six Subspaces and the Four Complex Products* (`articles_maths/the-six-subspaces-and-the-four-complex-products.md`), for the four products read on the six distinguished real subspaces
- *Biquaternion Versors and the Orthogonal Group* (`articles_maths/biquaternion-versors-and-the-orthogonal-group.md`), for the parity, the determinant and the Lorentz group
