
# __The Four General Products and Operators__

## Introduction

The four general products of $\mathbb{B}$ are four rules that pair two elements, and the corpus gives each of them an operator family: the plain bilinear product the *Association* family, the general plain sesquilinear product the *Hermitian Adjoint* family, the general quaternionic bilinear product the *Signed Inner Conjugation* family, and the general quaternionic sesquilinear product the Krein form, which carries its own indefinite theory rather than a family of the four-adjoint kind. A reader may conclude from that list that the product *decides* the operator, and may then ask whether the product decides whether an element acts as a rotation or as a reflection. **It does not.** The four general products have the same multiplication table of the units; they differ only in which conjugation is inserted into which slot of the pair. What they decide is the *pairing*, hence the adjoint, hence the name of the family. The action — a rotation, a reflection, an inner automorphism — is decided by the element and by the inserted sign, and the inserted sign is a choice among the involutions that the algebra already carries.

This article states that division of labour precisely, with the matrices of one element read through all four insertions. It closes the group *The Four General Products* and carries the passage from a product to an operator.

The answer to the question of the title is therefore a negative one, and it agrees with the intuition that the algebra and its product come first and the operator is obtained from them by choosing the element and the insertion. The qualification is that the choice is not arbitrary: on the vector subspace the plain product cannot produce a reflection, only its negative, so that one insertion is *forced* by the algebra and not merely preferred.

The four general products, their relations and their comparison are *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, *Relations Between the Four General Products* and *Comparison Between the Four General Products*; the four pairings and their Gram matrices are *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*; the four adjoints and the reading of the family names are *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples*; the conjugations and their group are *The Group of Involutions*; the signed sandwich and its reflection formula are *The Signed Sandwich on a Clifford Algebra* and *Two-Sided Operators with the Signed Product*. The article is pure algebra.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, $\vec e_y\vec e_z=\vec e_x$, $\vec e_z\vec e_x=\vec e_y$; $i$ is the central scalar imaginary; a general element is $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$. The three conjugations used are the natural conjugation $\tilde Q^{\natural}=Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z$, the coefficient conjugation $\bar{\tilde Q}=\overline{Q_t}e_t+\overline{Q_x}\vec e_x+\overline{Q_y}\vec e_y+\overline{Q_z}\vec e_z$, and the Hermitian conjugation $\tilde Q^{*}=\tilde Q^{\natural\bar{\bar{\cdot}}}=\overline{Q_t}e_t-\overline{Q_x}\vec e_x-\overline{Q_y}\vec e_y-\overline{Q_z}\vec e_z$. The vector subspace is $V=\mathbb{C}\{\vec e_x,\vec e_y,\vec e_z\}$, the norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$, an element is a unit exactly when $\langle\tilde Q\rangle_{\natural}\ne0$, and $\mathrm{Sc}$ is the scalar part.

## The Four General Products Are One Multiplication with Two Insertions

### The Four Rules

**Definition (the four general products).** The four general products are

$$
\tilde Q_1\tilde Q_2 ,
\qquad
\tilde Q_1\tilde Q_2^{*} ,
\qquad
\tilde Q_1^{\natural}\tilde Q_2 ,
\qquad
\tilde Q_1^{\natural}\tilde Q_2^{*} ,
$$

the plain bilinear, the general plain sesquilinear, the general quaternionic bilinear and the general quaternionic sesquilinear product.

**Proposition (one table, two insertions).** The four rules multiply the coordinates on the same products $e_\mu e_\nu$ of the basis. They differ in one point alone: whether the coordinates of each of the two elements are used as they stand or taken from the conjugated element, the two elements being treated independently of one another. Equivalently, the four general products are the four members of the orbit

$$
\bigl\{K_1(\tilde Q_1)\,K_2(\tilde Q_2)\;:\;K_1\in\{\mathrm{id},{}^{\natural}\},\;K_2\in\{\mathrm{id},{}^{*}\}\bigr\}
$$

of a single rule under the insertion of a conjugation into the first slot and a conjugation into the second.

*Proof.* Reading the four definitions side by side, the products $e_\mu e_\nu$ of the basis and the order of the factors are the same in all four; the only difference is the source of $Q_{1,\mu}$ in the first factor and of $Q_{2,\nu}$ in the second.

**Remark (why "complex products").** The word *complex* records the base field and not a second multiplication: the multiplication of the units is that of $\mathbb{H}$ extended to $\mathbb{C}$, and the four rules move over it. There is no product among the four that is not the plain one with an insertion.

### One Multiplication Table, Four Pairings

**Theorem (the scalar parts are the four pairings).** The scalar parts of the four general products are the four pairings of the algebra,

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2),\quad
\langle\tilde Q_1,\tilde Q_2\rangle_{\ast}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*}),\quad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2),\quad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural\ast}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*}),
$$

with Gram matrices in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ equal to $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$, $\mathrm{I}_4$, $\mathrm{I}_4$ and $\mathrm{E}$.

*Proof.* $\mathrm{Sc}(e_\mu e_\nu)=\varepsilon_\mu\delta_{\mu\nu}$ with $\varepsilon=(1,-1,-1,-1)$, and on the basis units the two insertions act by $e_\mu^{\natural}=\varepsilon_\mu e_\mu$ and $e_\mu^{*}=\varepsilon_\mu e_\mu$, the coordinates of the units being real, so that the sign $\varepsilon_\mu$ cancels as soon as the unit is read through one of the two insertions. The Gram matrix is therefore $\varepsilon$ exactly when the two insertions agree, that is for the plain product and for the general quaternionic sesquilinear one, and $1$ when they differ, that is $\mathrm{E},\mathrm{I}_4,\mathrm{I}_4,\mathrm{E}$. The four pairings are distinct as maps — two are bilinear and two sesquilinear in the second argument, and no two agree on complex coefficients — while two pairs of them share a Gram matrix, a Gram matrix seeing the basis units alone, on which the conjugations act by a sign.

**Corollary (a product is a pairing, not an operator).** The four general products endow $\mathbb{B}$ with the four pairings and nothing else. Each of them is a bilinear or a sesquilinear *form*, and a form does not act on the algebra; it pairs two of its elements. Whatever acts is a map, and a map has to be built.

## What the Products Decide and What the Choice Decides

### The Products Decide the Four Adjoints

**Theorem (the four adjoints are decided by the four general products).** For the left multiplication $L_{\tilde Q_4}$ the adjoints of the four pairings are

$$
(L_{\tilde Q_4})^{\approx}=R_{\tilde Q_4},\qquad
(L_{\tilde Q_4})^{\ast}=L_{\tilde Q_4^{\ast}},\qquad
(L_{\tilde Q_4})^{N}=L_{\tilde Q_4^{\natural}},\qquad
(L_{\tilde Q_4})^{\natural\ast}=R_{\bar{\tilde Q_4}},
$$

and for the two-sided operator $(L_{\tilde Q_4}R_{\tilde Q_1})^{\approx}=L_{\tilde Q_1}R_{\tilde Q_4}$, $(L_{\tilde Q_4}R_{\tilde Q_1})^{\ast}=L_{\tilde Q_4^{\ast}}R_{\tilde Q_1^{\ast}}$, $(L_{\tilde Q_4}R_{\tilde Q_1})^{N}=L_{\tilde Q_4^{\natural}}R_{\tilde Q_1^{\natural}}$, $(L_{\tilde Q_4}R_{\tilde Q_1})^{\natural\ast}=L_{\bar{\tilde Q_1}}R_{\bar{\tilde Q_4}}$.

*Proof.* *The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples*, where all sixteen cases are verified on the pairs of basis elements.

So the product *does* decide something of the first importance: which adjoint exists, and therefore which of the four operator families has a coherent adjoint theory. That is the whole content of the naming rule of the corpus, and it is a statement about *forms*.

### The Operator Is Not Decided

**Remark (the missing inputs).** The four general products share the table of the units, so no two of them can differ in the way an operator differs from another. To write down an operator one has still to supply

1. an **element** $\tilde Q_4$ of the algebra, and
2. an **insertion**: which involution, if any, is put on the element, and on which side.

The products do not supply 1, and they supply the *repertoire* of 2 without choosing from it. That is the sense in which the operator is chosen by the modeller: given the algebra with its product, one chooses $\natural$, or $\bar{\cdot}$, or ${}^{*}$, or none, and therefore the operator.

## One Element, Four Operators

### The Four Operators of $\vec e_x$

Fix the element $\tilde Q_4=\vec e_x$, a unit with $\langle \vec e_x\rangle_{\natural}=-e_t$, so that $\vec e_x^{-1}=-\vec e_x$. Read it through the four insertions, using the inverse of the conjugated element in the right factor:

$$
\begin{aligned}
\text{no insertion:}\quad & L_{\vec e_x}R_{\vec e_x^{-1}} & \tilde Q_2&\longmapsto \vec e_x\tilde Q_2 \vec e_x^{-1},\\
\text{sign }\natural\text{ on the left:}\quad & L_{\vec e_x^{\natural}}R_{\vec e_x^{-1}} & \tilde Q_2&\longmapsto \vec e_x^{\natural}\tilde Q_2 \vec e_x^{-1},\\
\text{star on the right:}\quad & L_{\vec e_x}R_{(\vec e_x^{*})^{-1}} & \tilde Q_2&\longmapsto \vec e_x\tilde Q_2 (\vec e_x^{*})^{-1},\\
\text{both:}\quad & L_{\vec e_x^{\natural}}R_{(\vec e_x^{*})^{-1}} & \tilde Q_2&\longmapsto \vec e_x^{\natural}\tilde Q_2(\vec e_x^{*})^{-1}.
\end{aligned}
$$

For $\vec e_x$ the two conjugations are $\natural(\vec e_x)=-\vec e_x$ and $\vec e_x^{*}=-\vec e_x$, so the four operators are two, and in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ they are

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

**Remark (the four insertions collapse).** For a parameter that one of the conjugations fixes, the four operators are fewer than four: the sign insertion is invisible exactly when $\tilde Q_4^{\natural}=\tilde Q_4$, which holds for the central $\tilde Q_4$, and the star insertion is invisible exactly when $\tilde Q_4^{*}=\tilde Q_4$, which holds for the parameters with real central coefficient and purely imaginary vector coefficients, the fixed space $\mathbb{M}_{+}$ of the Hermitian conjugation. For a vector $\tilde Q_4\in V$ with real coefficients the four operators are two, $\pm L_{\tilde Q_4}R_{\tilde Q_4^{-1}}$; for a generic complex vector of $V$ the four are pairwise distinct. The number of distinct operators is therefore a property of the *element*, and not of the product.

## Rotation, Reflection, and Where the Sign Is Read

### The Plain Product Gives Minus the Reflection

**Theorem (the reflection is reached only through the sign).** Let $\tilde Q_4\in V$ be a vector with $\langle\tilde Q_4\rangle_{\natural}\ne0$, and let $\rho_{\tilde Q_4}$ be the reflection of $V$ in the hyperplane $\tilde Q_4^{\perp}$ for the polar form of $q=-\sum_kQ_k^{2}$, which on $V$ is the general plain bilinear form $\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)$,

$$
\rho_{\tilde Q_4}(\tilde Q_3)=\tilde Q_3-\frac{2\langle\tilde Q_3,\tilde Q_4\rangle}{\mathfrak{Q}(\tilde Q_4)}\,\tilde Q_4 .
$$

Then the two insertions that read the parameter as it stands keep $V$ stable, and

$$
L_{\tilde Q_4}R_{\tilde Q_4^{-1}}\big|_{V}=-\rho_{\tilde Q_4},\qquad
L_{\tilde Q_4^{\natural}}R_{\tilde Q_4^{-1}}\big|_{V}=\rho_{\tilde Q_4},
$$

with determinant of the restriction $+1$ and $-1$. The two insertions that read the right factor through ${}^{*}$ behave differently, and the proposition below says exactly how.

*Proof.* For $\tilde Q_4\in V$ the sign reads the parameter as $\tilde Q_4^{\natural}=-\tilde Q_4$, so that $L_{\tilde Q_4^{\natural}}R_{\tilde Q_4^{-1}}=-L_{\tilde Q_4}R_{\tilde Q_4^{-1}}$; the identity $L_{\tilde Q_4}R_{\tilde Q_4^{-1}}\big|_{V}=-\rho_{\tilde Q_4}$ is the reflection formula of the Clifford algebra in the convention $\mathfrak{Q}(\tilde Q_4)=\langle\tilde Q_4,\tilde Q_4\rangle<0$, equivalently $\tilde Q_4\tilde Q_3+\tilde Q_3\tilde Q_4=2\langle\tilde Q_4,\tilde Q_3\rangle$ and $\tilde Q_4^{2}=\mathfrak{Q}(\tilde Q_4)e_t$.

**Proposition (the star insertions leave $V$ in general).** For $\tilde Q_4\in V$ the right factor of the starred insertions is $(\tilde Q_4^{*})^{-1}=-(\bar{\tilde Q_4})^{-1}$, so the two starred operators are $-L_{\tilde Q_4}R_{(\bar{\tilde Q_4})^{-1}}$ and $+L_{\tilde Q_4}R_{(\bar{\tilde Q_4})^{-1}}$. They keep $V$ stable exactly when $\bar{\tilde Q_4}$ is a scalar multiple of $\tilde Q_4$, that is when the coefficient vector of $\tilde Q_4$ is a complex multiple of a real one. When it is, and only then, a determinant on $V$ is defined: it is $-1$ for the star insertion and $+1$ for the both insertion when the coefficient vector is real, the two are exchanged when it is purely imaginary, and for a coefficient vector that is a non-real, non-imaginary complex multiple of a real one the restriction is neither $\pm\rho_{\tilde Q_4}$ nor form-preserving. For a generic complex parameter, $V$ is not preserved and the starred insertions are read on the algebra and not on $V$.

*Proof.*

**Remark (the sentence of the corpus, translated).** *The Signed Sandwich on a Clifford Algebra* says that the ordinary sandwich by a vector is the **negative** of the reflection, and that inserting the grade involution *repairs the sign*. The theorem above is that sentence in the biquaternion model: the plain product gives $-\rho_{\tilde Q_4}$, the involution of $V$ whose fixed space has codimension one, and the sign insertion gives $\rho_{\tilde Q_4}$. This is the one place where the algebra forces a choice rather than permitting one.

**Corollary (where a determinant plus one lives).** On the algebra $\mathbb{B}$ itself, of complex dimension four, all four operators have determinant $+1$; the sign shows in the determinant only on the odd-dimensional restriction $V$, or on a real form of odd dimension. A "rotation" and a "reflection" are therefore read on $V$.

*Proof.* The operators are products $L_{\tilde Q_4}R_{\tilde Q_1}$, whose determinant on $\mathbb{B}$ is $\det(L_{\tilde Q_4})\det(R_{\tilde Q_1})$, and for a four-dimensional space the sign $-1$ on a parameter contributes the factor $(-1)^{4}=+1$.

### The Sign Is Invisible on the Centre and on Even Parameters

**Proposition.** If $\tilde Q_4$ is central, $\tilde Q_4=a_0e_t$, then the sign insertion changes nothing, $L_{\tilde Q_4^{\natural}}R_{\tilde Q_4^{-1}}=L_{\tilde Q_4}R_{\tilde Q_4^{-1}}$. If $\tilde Q_4\in V$ is a vector, the sign insertion negates the operator, $L_{\tilde Q_4^{\natural}}R_{\tilde Q_4^{-1}}=-L_{\tilde Q_4}R_{\tilde Q_4^{-1}}$.

*Proof.* $\natural$ fixes the centre and negates $V$; left multiplication and right multiplication commute.

**Theorem (the determinant table).** For a unit $\tilde Q_4$ let $d$ be the determinant of the operator restricted to $V$ for the four insertions, in the order (none, sign on the left, star on the right, both). Then

| $\tilde Q_4$ | none | sign | star | both |
|---|---|---|---|---|
| $e_t$ | $+1$ | $+1$ | $+1$ | $+1$ |
| $i e_t$ | $+1$ | $+1$ | $-1$ | $-1$ |
| $\vec e_x$ | $+1$ | $-1$ | $-1$ | $+1$ |
| $\vec e_x+\vec e_y$ | $+1$ | $-1$ | $-1$ | $+1$ |
| $i \vec e_x$ | $+1$ | $-1$ | $+1$ | $-1$ |
| $e_t+\vec e_x$ | $+1$ | $0$ | $0$ | $+1$ |

The zero entries are the starred insertions of a mixed parameter, whose operator does not preserve $V$, so that the restricted determinant is $0$ and is not a rotation-reflection marker; the star and both columns are read on $V$ only for the rows whose parameter has a real or purely imaginary coefficient vector.

*Proof.* The rows are the computed determinants; the first row is the identity on $V$; the second row shows that a central imaginary parameter, on which the sign is invisible, is still separated by the conjugate-linear insertion, $(\tilde Q_4^{*})^{-1}=i e_t$, which gives $-e_t$ on the left factor and hence $-\mathrm{id}$ on $V$; the third and fourth rows are the theorem above; the fifth row is a purely imaginary vector, on which the star insertion coincides with the plain one and the both insertion with the sign, so that the determinants are those of the third row read with the two insertions exchanged; the last row is a mixed parameter, whose starred operators do not keep $V$ stable.

**Remark (the two central rows).** The proposition and the table together show the two independent choices: the *sign* $\natural$ is invisible on the centre and reads only the odd part, while the *star* is invisible on the real directions and reads the coefficient imaginary. Neither is a property of the product; both are properties of the insertion into the chosen element.

## Which Involution Is "the Sign" Is Itself a Choice

**Remark (the corpus fixes the sign by a formula).** The biquaternion corpus calls $\natural$ the sign and uses it throughout, but the map that plays the role of the sign is a choice among the involutions of the algebra. The identification $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, $\gamma_k\mapsto i\vec e_k$, has the grades $\text{grade }0=\mathbb{R}e_t$, $\text{grade }1=\mathrm{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$, $\text{grade }2=\mathrm{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$, $\text{grade }3=\mathbb{R}ie_t$, and in that reading

| map on $\mathbb{B}$ | Clifford partner | signs on grades $0,1,2,3$ | coefficient sign vector on $e_t,\vec e_x,\vec e_y,\vec e_z$ |
|---|---|---|---|
| quaternion conjugation $\natural$ | Clifford conjugation $\alpha(X^{r})$ | $+,-,-,+$ | $(1,-1,-1,-1)$ |
| complex conjugation $\bar{\cdot}$ | grade involution $\alpha$ | $+,-,+,-$ | fixes $\vec e_x,\vec e_y,\vec e_z$, reverses $i$ |
| Hermitian conjugation ${}^{*}$ | reversion $X^{r}$ | $+,+,-,-$ | $-1$ on $\vec e_x,\vec e_y,\vec e_z$ and $-1$ on $ie_t$ |

So the corpus's "sign" is the map with the sign vector $(1,-1,-1,-1)$, and it is *not* the grade involution of that Clifford reading: the grade involution is the coefficient conjugation, and on $V$, which is the grade-two part there, it is the identity. Two consequences follow, and both answer the question of the title. First, the corpus's choice of $\natural$ as the sign is a convention of the biquaternion model, fixed by the coefficient formula and not by an abstract parity. Second, the reflection theorem is nevertheless not a convention: with the sign $\natural$ it holds, and with the grade involution, which is trivial on $V$, it fails.

**Remark (parameter or argument).** The sign may be inserted in the **parameter**, $L_{\tilde Q_4^{\natural}}R_{\tilde Q_4^{-1}}$, which is the *signed inner conjugation* of the corpus, or in the **argument**, $\tilde Q_2\mapsto\tilde Q_4\,\tilde Q_2^{\natural}\,\tilde Q_4^{-1}$, which is the *signed sandwich* of *The Signed Sandwich on a Clifford Algebra*. On the vector subspace the two agree, because both act by the sign $-\mathrm{id}$ there; on the whole algebra they differ, and the general corpus keeps the two families apart on purpose, the one twisting the parameter and the other the argument.

## Summary

The four general products of the biquaternion algebra are one multiplication with a conjugation inserted independently into each of the two slots. They therefore share the multiplication table of the units, and they determine the four pairings — their scalar parts — and with the pairings the four adjoints and the names of the four operator families. They do not determine an operator. An operator needs an element, and it needs an insertion: which involution, if any, is put on the element and on which side, and whether the sign goes into the parameter or into the argument. The element $\vec e_x$ read through the four insertions gives two operators, $\operatorname{diag}(1,1,-1,-1)$ and $\operatorname{diag}(-1,-1,1,1)$, and on the vector subspace they are $-\rho_{\vec e_x}$ and $\rho_{\vec e_x}$: the plain product gives $-\rho_{\vec e_x}$, and the reflection is reached only through the sign. On the four-dimensional algebra both have determinant $+1$, so rotation and reflection are read on the vector subspace. Finally, which map plays the role of the sign is itself chosen: the biquaternion corpus fixes it as the natural conjugation $\natural$, whose sign vector is $(1,-1,-1,-1)$, and that is a convention of the model, whereas the identity "the reflection needs the sign" is a theorem. The answer to the question is therefore: no, the product does not decide between a rotation and a reflection; the algebra and its product come first, and the operator is obtained from them by choosing the element and the insertion.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q_1\tilde Q_2$, $\tilde Q_1\tilde Q_2^{*}$, $\tilde Q_1^{\natural}\tilde Q_2$, $\tilde Q_1^{\natural}\tilde Q_2^{*}$ | the four general products: one table, the two insertions |
| $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\ast}$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{\natural\ast}$ | their scalar parts, the four pairings, Gram matrices $\mathrm{E},\mathrm{I}_4,\mathrm{I}_4,\mathrm{E}$ |
| ${}^{\approx}$, ${}^{*}$, ${}^{N}$, ${}^{\natural\ast}$ | the four adjoints, decided by the four general products |
| $\natural$, $\bar{\cdot}$, ${}^{*}$ | the sign, the coefficient conjugation, the Hermitian conjugation; $\natural$ has sign vector $(1,-1,-1,-1)$ |
| $L_{\tilde Q_4}R_{\tilde Q_1}$ | a two-sided operator; $L_{\tilde Q_4}R_{\tilde Q_4^{-1}}$ the inner automorphism of the plain product |
| $L_{\tilde Q_4^{\natural}}R_{\tilde Q_4^{-1}}$, $\tilde Q_2\mapsto\tilde Q_4\tilde Q_2^{\natural}\tilde Q_4^{-1}$ | the sign inserted in the parameter, and in the argument |
| $\rho_{\tilde Q_4}$ | the reflection of $V$ in $\tilde Q_4^{\perp}$; the plain product gives $-\rho_{\tilde Q_4}$, the sign gives $\rho_{\tilde Q_4}$ |
| $\operatorname{diag}(1,1,-1,-1)$, $\operatorname{diag}(-1,-1,1,1)$ | the two operators of $\vec e_x$, and their restrictions $\operatorname{diag}(1,-1,-1)$, $\operatorname{diag}(-1,1,1)$ to $V$ |

## Further Reading

- [The Four General Products of the Biquaternion $\mathbb{C}$ Space](the-four-general-products-of-the-biquaternion-c-space.html), for the four rules and the statement that they differ in one point alone
- [Comparison Between the Four General Products](comparison-between-the-four-general-products.html), for the table of the four rules side by side
- [The 4 Forms over the Biquaternion $\mathbb{C}$ Space](the-4-forms-over-the-biquaternion-c-space.html), for the four forms, their Gram matrices, their signatures and their isometry groups
- [The Four Adjoints of the Two Algebras and the Two Sesqualgebras in Examples](the-four-adjoints-of-the-two-algebras-and-the-two-sesqualgebras-in-examples.html), for the four adjoints on explicit operators and the naming rule of the operator families
- [The Group of Involutions](the-group-of-involutions.html), for the four conjugations and their group
- [The Signed Sandwich on a Clifford Algebra](the-signed-sandwich-on-a-clifford-algebra.html), for the ordinary sandwich, its minus sign and the repair by the grade involution
- [Two-Sided Operators with the Signed Product](two-sided-operators-with-the-signed-product.html), for the signed family, its twisted composition law and its coset structure
- [Two-Sided Operators on the General Quaternionic Algebra](two-sided-operators-on-the-general-quaternionic-algebra.html), for the parameter insertion in the biquaternion model
- [Remarkable Subspaces and the Four General Products](remarkable-subspaces-and-the-four-general-products.html), for the four general products read on the remarkable real subspaces
- [Biquaternion Versors and the Orthogonal Group](biquaternion-versors-and-the-orthogonal-group.html), for the parity, the determinant and the Lorentz group
