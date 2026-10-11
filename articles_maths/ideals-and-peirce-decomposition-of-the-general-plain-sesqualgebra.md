# __Ideals and Peirce Decomposition of the General Plain Sesqualgebra__

## Introduction

The general plain sesquilinear product $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ makes the biquaternion space $\mathbb{B}$ a sesqualgebra, and the two structures this article puts side by side on that multiplication are the **ideals** and the **Peirce decomposition**. In the algebra of *Ideals and Peirce Decomposition of the General Plain Algebra* the two are one subject, because a Peirce corner is a one-sided ideal; here they separate, and the separation is the point.

The **ideals** of the multiplication are the two trivial ones on the left and on both sides at once, but on the right they are as many as the algebra's: a right $\star$-ideal is exactly a right algebra ideal, so the right-sided lattice is untouched by the passage from the algebra to the multiplication, while the left-sided and the two-sided lattices collapse to the two-element chain. The asymmetry is the conjugate sitting in the second slot, and it is the first thing this article establishes. The two-sided simplicity of the multiplication is *The Biquaternion Sesqualgebra Is Simple*; the one-sided statement there treats the two sides alike, and the computation below shows they are not alike. The algebra's lattice has, on each side, a projective line of minimal ideals, and those minimal ideals are exactly the sums of two Peirce lines; the Peirce decomposition then says which of them the multiplication keeps and which it destroys, the right ones being kept and the left ones destroyed.

The **Peirce decomposition** is the algebra's. The four spaces $\tilde\Pi_i\mathbb{B}\tilde\Pi_j$ of a projection need associativity, which the multiplication does not have, and the multiplication contributes to them a **table and nothing else**: the product of two spaces lands in the space whose two indices must agree, and the two indices that must agree sit on the right in the sesquilinear table whereas they sit in the middle in the algebra table. The table is therefore the **transpose** of the algebra's in the second factor, its index rule is not the parity grading of the algebra, and the elements that index it are the **projections**, the Hermitian idempotents, which are exactly the idempotents of the multiplication by *Idempotents of the General Plain Sesqualgebra*. The general form of the transposed table is *Hermitian Idempotents and the Peirce Decomposition*; what is added here is the biquaternion instance, the four lines in the coefficients of the block, the transport through the matrix model, the form the involution takes on the two mixed lines, and the failure of the two-sided conditions of the multiplication to reproduce the four spaces.

**Boundaries.** The multiplication, its scalar rules and its idempotents are *Introduction to the General Plain Sesqualgebra of Biquaternions*; the projections and their complementary pairs are *Idempotents of the General Plain Sesqualgebra*; the ideals of a general sesqualgebra are *Ideals and Quotients of a Sesqualgebra*, and the two notions of simplicity are *Simple Sesqualgebras and Minimal Ideals*; the ideals of the block are *The Biquaternion Sesqualgebra Is Simple*, whose two-sided theorem this article quotes and whose one-sided theorem it corrects on the right; the transposed Peirce table of a derived operation is *Hermitian Idempotents and the Peirce Decomposition*; the algebra's ideal theory, its Peirce decomposition and its minimal one-sided ideals are *Ideals and Peirce Decomposition of the General Plain Algebra*; the model in which the four lines are the four matrix entries is *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*; and the general definition of the idempotent, the projection and the Peirce decomposition is *Definitions for the Study of the 12 Algebraic Structures*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$, with $e_0$ the unit and $e_1e_2=e_3$, and $i$ is the central scalar imaginary. Juxtaposition is the **plain** product $\tilde P\tilde Q$ of *Introduction to the General Plain Algebra of Biquaternions*, $\star$ is the multiplication of this block, $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$, and ${}^{*}={}^{\natural}\circ\bar{\cdot}$ is the Hermitian conjugation of *Biquaternions as a Vector Space over $\mathbb{C}$*. A **projection** is a Hermitian idempotent, and the projections are exactly the $\star$-idempotents; they are written

$$
\tilde\Pi_1(\hat\mu)=\tfrac12\bigl(e_0+i\hat\mu\bigr),\qquad \tilde\Pi_2(\hat\mu)=e_0-\tilde\Pi_1(\hat\mu)=\tfrac12\bigl(e_0-i\hat\mu\bigr),
$$

with $\hat\mu$ a real vector of the vector subspace and $(\hat\mu,\hat\mu)=1$. The pair $\tilde\Pi_1(\hat\mu),\tilde\Pi_2(\hat\mu)$ is the **complementary pair** of *Idempotents of the General Plain Sesqualgebra*. The matrix model $\mathsf{M}_2$ is the algebra isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ of *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, with $\mathsf{M}_2(e_0)=\mathrm{I}_2$ and $\mathsf{M}_2(e_k)=-i\sigma_k$ on the three quaternion units.

## The Ideals

### The Three Lattices

**Proposition (the ideal lattice of the multiplication).** For the multiplication $\star$ on $\mathbb{B}$: (i) its left ideals are $0$ and $\mathbb{B}$; (ii) its right ideals are exactly the **right algebra ideals**, namely $0$, $\mathbb{B}$ and the complex two-dimensional minimal right ideals $\tilde\Pi\mathbb{B}$ over the primitive idempotents $\tilde\Pi$, a projective line of them; (iii) its two-sided ideals are $0$ and $\mathbb{B}$.

**Proof.** (i) Let $I$ be a left $\star$-ideal, so $\mathbb{B}\star I\subseteq I$, and let $\tilde X\in I$. The right unit gives $\tilde X^{*}=e_0\star\tilde X\in\mathbb{B}\star I\subseteq I$, so $I$ is stable under the involution and $I^{*}=I$. With $I$ stable the $\star$-condition is the algebra condition, $\mathbb{B}\star I=\mathbb{B}I^{*}=\mathbb{B}I\subseteq I$, so $I$ is a stable left algebra ideal; and a stable left ideal is two-sided, because for $i\in I$ and $a\in\mathbb{B}$ one has $ia=(a^{*}i^{*})^{*}\in(\mathbb{B}I)^{*}\subseteq I^{*}=I$. A proper nonzero left ideal of $\mathbb{B}\cong M_2(\mathbb{C})$ is the set of the matrices whose kernel contains a fixed line, by *Ideals and Peirce Decomposition of the General Plain Algebra*, §*The Lattice of Left Ideals*; its conjugate image is a right ideal of the same dimension, and it differs from the left ideal, because a set that is both a left and a right ideal is a two-sided ideal and the only two-sided algebra ideals of $\mathbb{B}$ are $0$ and $\mathbb{B}$. So no proper nonzero left algebra ideal is stable, and the left $\star$-ideals are $0$ and $\mathbb{B}$.

(ii) Because ${}^{*}$ is onto, $I\star\mathbb{B}=I\mathbb{B}^{*}=I\mathbb{B}$, so the condition $I\star\mathbb{B}\subseteq I$ is exactly $I\mathbb{B}\subseteq I$: the right $\star$-ideals are the right algebra ideals, with no stability condition imposed. The right algebra ideals are $0$, $\mathbb{B}$ and the spaces $\tilde\Pi\mathbb{B}$ over the primitive idempotents, the same lattice as on the left, read on the right.

(iii) A two-sided $\star$-ideal is in particular a left $\star$-ideal, hence $0$ or $\mathbb{B}$ by (i).

**Remark (why the two sides differ).** The multiplication is $R$-linear in the first slot and $\varsigma$-semilinear in the second, and it is the unit acting on the **first** slot that produces the conjugate of an element of an ideal, $e_0\star\tilde X=\tilde X^{*}$. On the right there is no such product: the condition reads $I\star\mathbb{B}=I\mathbb{B}$ and the involution never enters, so no stability is forced. The passage from the algebra to the multiplication therefore keeps the whole right-sided lattice and collapses the left-sided and the two-sided lattices to their two trivial elements. The statement is sharper than the two-sided simplicity of *The Biquaternion Sesqualgebra Is Simple*: the multiplication has no proper left ideal, and it has as many proper right ideals as the algebra.

**Remark (the involution does not exchange the two lattices).** The involution carries a left algebra ideal to a right algebra ideal, but it does not carry a right $\star$-ideal to a left $\star$-ideal. The minimal right ideal $\tilde\Pi\mathbb{B}$ is a right $\star$-ideal by (ii), and its conjugate image is the minimal left ideal $\mathbb{B}\tilde\Pi$, which is not a left $\star$-ideal by (i). So the two one-sided lattices are not exchanged by the involution, and the asymmetry of (i) and (ii) is not an artefact of the writing: the involution is part of the multiplication and not only a symmetry of it.

### The Peirce Lines and the Minimal Ideals

The Peirce decomposition of the next section meets the ideal theory at the two diagonal lines, and it is worth stating the meeting before the decomposition is in place.

**Proposition.** Let $\tilde\Pi$ be a projection. The space $\mathbb{B}\tilde\Pi$ of complex dimension two is a minimal left ideal of the algebra, the space $\tilde\Pi\mathbb{B}$ is a minimal right ideal, and under the Peirce splitting of $\tilde\Pi$

$$
\mathbb{B}\tilde\Pi=\tilde\Pi\mathbb{B}\tilde\Pi\oplus\tilde\Pi^{\perp}\mathbb{B}\tilde\Pi ,\qquad
\tilde\Pi\mathbb{B}=\tilde\Pi\mathbb{B}\tilde\Pi\oplus\tilde\Pi\mathbb{B}\tilde\Pi^{\perp} ,
$$

so that the minimal left ideal of the algebra is the sum of one diagonal and one mixed Peirce line, and the minimal right ideal is the sum of the other diagonal line and the other mixed line.

**Proof.** The minimality is *Ideals and Peirce Decomposition of the General Plain Algebra*, §*The Decomposition into Minimal Left and Right Ideals*: a primitive idempotent generates a minimal one-sided ideal, and a projection is primitive. The splittings are the completeness $\tilde\Pi+\tilde\Pi^{\perp}=e_0$ inserted between the two factors, $\mathbb{B}\tilde\Pi=\mathbb{B}(\tilde\Pi+\tilde\Pi^{\perp})\tilde\Pi=\mathbb{B}\tilde\Pi\tilde\Pi+\mathbb{B}\tilde\Pi^{\perp}\tilde\Pi$, which is direct because the two summands lie in the Peirce lines $\mathbb{B}_{11}$ and $\mathbb{B}_{21}$ and those are distinct, and the symmetric computation on the right.

**Corollary (which minimal ideals the multiplication keeps).** A minimal left ideal of the algebra is not a left ideal of the multiplication, while a minimal right ideal is a right ideal of the multiplication: $\mathbb{B}\tilde\Pi$ is destroyed by the multiplication, and $\tilde\Pi\mathbb{B}$ is preserved by it.

**Proof.** The left $\star$-ideals are only $0$ and $\mathbb{B}$ by §*The Three Lattices*, and $\mathbb{B}\tilde\Pi$ is proper and nonzero, so it is not a left $\star$-ideal. The space $\tilde\Pi\mathbb{B}$ is a right algebra ideal, hence a right $\star$-ideal by the same proposition.

**Remark (the reading).** So the Peirce decomposition exhibits the algebra's minimal one-sided ideals as the sums of one diagonal with one mixed line, and the multiplication separates the two families: it consumes the left one and keeps the right one. In the standard pair of the next section the left ideal $\mathbb{B}\tilde\Pi_1$ is the span of the first column of the matrix model and the right ideal $\tilde\Pi_1\mathbb{B}$ the span of its first row; the multiplication sends the first column out of itself, $\mathbb{B}\star\mathbb{B}\tilde\Pi_1=\mathbb{B}\tilde\Pi_1\mathbb{B}=\mathbb{B}$ because the two-sided ideal generated by a nonzero element is the whole algebra, and it keeps the first row inside itself, $\tilde\Pi_1\mathbb{B}\star\mathbb{B}=\tilde\Pi_1\mathbb{B}\mathbb{B}\subseteq\tilde\Pi_1\mathbb{B}$. The collapse on the left and the survival on the right are the Peirce picture of §*The Three Lattices*.

## The Peirce Decomposition

### The Definition

Let $\tilde\Pi$ be a projection, $\tilde\Pi^{\perp}=e_0-\tilde\Pi=\tilde\Pi_2(\hat\mu)$ its complement, and put $\tilde e_1=\tilde\Pi,\tilde e_2=\tilde\Pi^{\perp}$. The four **Peirce spaces** are the intersections

$$
\mathbb{B}_{ij}=\tilde e_i\,\mathbb{B}\,\tilde e_j,\qquad i,j\in\{1,2\},
$$

with respect to the **plain** product. They are the spaces of *Ideals and Peirce Decomposition of the General Plain Algebra*, §*The Peirce Decomposition*, and they need associativity, which the multiplication of the block does not have. The decomposition below is the algebra's; the multiplication supplies the table of its products on them, and that table is the subject of the next subsections.

### The Two Tables

**Theorem (the algebra table, recalled).** For the plain product, $\mathbb{B}_{ij}\mathbb{B}_{kl}\subseteq\delta_{jk}\mathbb{B}_{il}$.

**Proof.** $(\tilde e_ia\tilde e_j)(\tilde e_kb\tilde e_l)=\tilde e_iae_j\tilde e_kb\tilde e_l=\delta_{jk}\tilde e_iab\tilde e_l$, using $\tilde e_j^{2}=\tilde e_j$ and $\tilde e_j\tilde e_k=\delta_{jk}\tilde e_j$ for the complementary pair.

**Theorem (the sesquilinear table).** For the multiplication, $\mathbb{B}_{ij}\star\mathbb{B}_{kl}\subseteq\delta_{jl}\mathbb{B}_{ik}$.

**Proof.** The two projections are Hermitian, so $\tilde e_k^{*}=\tilde e_k$ and $\tilde e_l^{*}=\tilde e_l$, and

$$
(\tilde e_ia\tilde e_j)\star(\tilde e_kb\tilde e_l)=\tilde e_ia\tilde e_j\bigl(\tilde e_kb\tilde e_l\bigr)^{*}=\tilde e_ia\tilde e_j\tilde e_l^{*}b^{*}\tilde e_k^{*}=\tilde e_ia\,\tilde e_j\tilde e_l\,b^{*}\tilde e_k=\delta_{jl}\,\tilde e_iab^{*}\tilde e_k\in\mathbb{B}_{ik}.
$$

**Corollary (the transposition).** The two tables contract different pairs of indices: the algebra table requires the **second index of the first factor** to equal the **first index of the second**, whereas the sesquilinear table requires the **second index of the first factor** to equal the **second index of the second**, the outer indices of the result being the two first indices. The sesquilinear table is the **transpose** of the algebra table in the second factor, which is the reflection the conjugate-linear slot leaves on the decomposition; the general statement is *Hermitian Idempotents and the Peirce Decomposition*, §*The Transposed Table*.

**Remark (not a grading).** The algebra table is a $\mathbb{Z}/2$-grading, the parity of the two indices being conserved (*Ideals and Peirce Decomposition of the General Plain Algebra*, §*The Decomposition as a Grading*), so the four lines split into the two diagonal ones and the two mixed ones. The sesquilinear table is not a grading: it pairs the spaces by their second index, and the first mixed line has a product with itself in the first diagonal line and no product with the second diagonal line. The multiplication reads the four lines with its own index rule and not through the parity of the algebra.

### The Biquaternion Cases

**Proposition (the four lines).** For the complementary pair $\tilde\Pi=\tilde\Pi_1(\hat\mu)$, $\tilde\Pi^{\perp}=\tilde\Pi_2(\hat\mu)$ the Peirce decomposition of the block is

$$
\mathbb{B}=\tilde\Pi\mathbb{B}\tilde\Pi\oplus\tilde\Pi\mathbb{B}\tilde\Pi^{\perp}\oplus\tilde\Pi^{\perp}\mathbb{B}\tilde\Pi\oplus\tilde\Pi^{\perp}\mathbb{B}\tilde\Pi^{\perp},
$$

with complex one-dimensional summands

$$
\tilde\Pi\mathbb{B}\tilde\Pi=\mathbb{C}\tilde\Pi,\quad
\tilde\Pi\mathbb{B}\tilde\Pi^{\perp}=\mathbb{C}\tilde\Upsilon_1(\hat\mu),\quad
\tilde\Pi^{\perp}\mathbb{B}\tilde\Pi=\mathbb{C}\tilde\Upsilon_2(\hat\mu),\quad
\tilde\Pi^{\perp}\mathbb{B}\tilde\Pi^{\perp}=\mathbb{C}\tilde\Pi^{\perp},
$$

where $\tilde\Upsilon_1(\hat\mu)$ is any nonzero element of the first mixed space and $\tilde\Upsilon_2(\hat\mu)=\tilde\Upsilon_1(\hat\mu)^{*}$ is its conjugate in the second. Each summand has real dimension two and the total is eight.

**Proof.** The decomposition, the one-dimensionality of the four summands and the identification of the two mixed spaces as conjugate are *Ideals and Peirce Decomposition of the General Plain Algebra*, §*The Biquaternion Case* and §*From One Idempotent to Its Complement*, transported to the pair $(\tilde\Pi,\tilde\Pi^{\perp})$, a complete orthogonal family by *Idempotents of the General Plain Sesqualgebra*, §*The Complement and the Pairing of the Directions*.

**Example (the standard pair as coordinates).** At $\hat\mu=\hat e_3$ the projection is the standard idempotent $\tilde\Pi_1(\hat e_3)=\tfrac12(e_0+ie_3)$, its complement is $\tilde\Pi_2(\hat e_3)=\tfrac12(e_0-ie_3)$, and the matrix model sends the four lines to the four matrix units,

$$
\tilde\Pi\longleftrightarrow E_{11},\qquad \tilde\Upsilon_1(\hat e_3)\longleftrightarrow E_{12},\qquad \tilde\Upsilon_2(\hat e_3)\longleftrightarrow E_{21},\qquad \tilde\Pi^{\perp}\longleftrightarrow E_{22},
$$

as the transport of *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* records; the Peirce coordinates of an element are therefore the four entries of its matrix, grouped by the projection instead of by the basis.

**Remark (what is the multiplication's and what is the algebra's).** The four lines are the algebra's: they do not need the multiplication and they do not depend on it. Two things do depend on it. The first is the choice of the idempotent: the pair $(\tilde\Pi,\tilde\Pi^{\perp})$ that indexes the decomposition is made of projections, and the projections are the Hermitian idempotents, which are exactly the idempotents of the multiplication, so the decomposition can be indexed by the multiplication's own idempotents, a supply the algebra's decomposition does not provide. The second is the table, which is the next subsection.

### The Table in the Standard Pair

The four lines of the standard pair are written below by the symbol of their generating element,

$$
\tilde\Pi,\qquad \tilde\Upsilon_1,\qquad \tilde\Upsilon_2,\qquad \tilde\Pi^{\perp},
$$

and each denotes its own complex line. On these four lines the multiplication is the multiplication of the matrix units at the model of §*The Biquaternion Cases*, $E_{ij}\star E_{kl}=E_{ij}E_{lk}=\delta_{jl}E_{ik}$, which is exactly the rule $\delta_{jl}\mathbb{B}_{ik}$.

**Proposition (the table of the standard pair).** The products of the four lines are

| $\star$ | $\tilde\Pi$ | $\tilde\Upsilon_1$ | $\tilde\Upsilon_2$ | $\tilde\Pi^{\perp}$ |
|---|---|---|---|---|
| $\tilde\Pi$ | $\tilde\Pi$ | $0$ | $\tilde\Upsilon_1$ | $0$ |
| $\tilde\Upsilon_1$ | $0$ | $\tilde\Pi$ | $0$ | $\tilde\Upsilon_1$ |
| $\tilde\Upsilon_2$ | $\tilde\Upsilon_2$ | $0$ | $\tilde\Pi^{\perp}$ | $0$ |
| $\tilde\Pi^{\perp}$ | $0$ | $\tilde\Upsilon_2$ | $0$ | $\tilde\Pi^{\perp}$ |

each entry being the line named, and $0$ where the two second indices disagree.

**Proof.** The rule $\delta_{jl}\mathbb{B}_{ik}$ is read on the four values of the pair of indices: the line $\mathbb{B}_{ij}$ has first index $i\in\{1,2\}$ and second index $j$, with $\mathbb{B}_{11}=\mathbb{C}\tilde\Pi$, $\mathbb{B}_{12}=\mathbb{C}\tilde\Upsilon_1$, $\mathbb{B}_{21}=\mathbb{C}\tilde\Upsilon_2$, $\mathbb{B}_{22}=\mathbb{C}\tilde\Pi^{\perp}$, and the product lies in $\mathbb{B}_{ik}$ when $j=l$ and vanishes otherwise. The matrix form is the same computation on the units, using $E_{ij}^{\dagger}=E_{ji}$ and $E_{ij}E_{kl}=\delta_{jk}E_{il}$.

**Remark (against the algebra table).** On the same four lines the algebra table reads $\delta_{jk}\mathbb{B}_{il}$ and gives a different pattern, for instance $\tilde\Upsilon_1\tilde\Upsilon_2\subseteq\mathbb{C}\tilde\Pi$ and $\tilde\Upsilon_1\tilde\Upsilon_1=0$, whereas the multiplication gives $\tilde\Upsilon_1\star\tilde\Upsilon_2=0$ and $\tilde\Upsilon_1\star\tilde\Upsilon_1\subseteq\mathbb{C}\tilde\Pi$. The two mixed lines are the place where the two tables are most visibly exchanged, and this is the biquaternion instance of the observation of *Hermitian Idempotents and the Peirce Decomposition*, §*The Products of the Derived Table*, that the ordinary product of the two mixed spaces is the corner while the derived product vanishes.

### The Involution on the Peirce Spaces

**Theorem (the exchange).** Let $\tilde\Pi$ be a projection. The involution exchanges the two indices of each Peirce space, $(\mathbb{B}_{ij})^{*}=\mathbb{B}_{ji}$; it fixes each diagonal corner and exchanges the two mixed lines, and in the standard pair it carries the first mixed line to the second and back.

**Proof.** $(\tilde e_ia\tilde e_j)^{*}=\tilde e_j^{*}a^{*}\tilde e_i^{*}=\tilde e_ja^{*}\tilde e_i\in\mathbb{B}_{ji}$ because the two projections are Hermitian, and ${}^{*}$ is an involution, so the inclusion is an equality. The standard-pair statement is the definition $\tilde\Upsilon_2(\hat\mu)=\tilde\Upsilon_1(\hat\mu)^{*}$.

**Corollary (the table is transpose-Hermitian).** The involution acts on the block's product by reversing the two factors, $(\tilde X\star\tilde Y)^{*}=\tilde Y\star\tilde X$, an identity of *Introduction to the General Plain Sesqualgebra of Biquaternions*. So the entry $\mathbb{B}_{ij}\star\mathbb{B}_{jl}\subseteq\mathbb{B}_{il}$ is carried to $\mathbb{B}_{lj}\star\mathbb{B}_{ji}\subseteq\mathbb{B}_{li}$, and on the standard pair, where the involution fixes the two corners and exchanges the two mixed lines, the conjugate of the entry in the row $\tilde A$ and the column $\tilde B$ is the entry in the row $\tilde B$ and the column $\tilde A$. The table is therefore **transpose-Hermitian**, and the display above is invariant under the transposition of its rows and columns combined with the exchange of the labels of the two mixed lines.

**Remark (the reading of the two symmetries).** The algebra's table is symmetric under the exchange of the two factors alone, because the plain product is associative and the reversal of an entry is the entry itself; the multiplication's table is not, and its symmetry trades the reversal of the factors against the exchange of the two mixed lines under the involution. This is the same trade that the identity $(\tilde X\star\tilde Y)^{*}=\tilde Y\star\tilde X$ makes at the level of the multiplication, and it is the transpose form of the observation of *The Sesquilinear Commutator and the Symmetrised Product on the Biquaternions*.

**Remark (why the Hermitian condition is needed).** The exchange uses $\tilde e^{*}=\tilde e$ on both projections, so it is a statement about Hermitian idempotents. For a non-Hermitian idempotent $\tilde e$ of the algebra the involution carries $\tilde e$ to a different idempotent $\tilde e^{*}$ that is not the complement, the corner $\tilde e\mathbb{B}\tilde e$ is not carried to itself, and the four spaces of $\tilde e$ are not closed under the involution as a set; the general statement is *Hermitian Idempotents and the Peirce Decomposition*, §*Why the Hermitian Condition is Needed*. That the idempotent be Hermitian is exactly that it be an idempotent of the multiplication, so the exchange is available precisely on the pairs that the multiplication indexes.

### The Corners

**Theorem (the corner).** Let $\tilde\Pi$ be a projection. The corner $\tilde\Pi\mathbb{B}\tilde\Pi$ is stable under the multiplication, it contains $\tilde\Pi$, and with the restricted multiplication and the restricted involution it is a sesqualgebra whose right $\star$-unit is $\tilde\Pi$; in the block the corner is the complex line $\mathbb{C}\tilde\Pi$ and its multiplication is $\lambda\tilde\Pi\star\mu\tilde\Pi=\lambda\overline{\mu}\,\tilde\Pi$, the multiplication of $\mathbb{C}$ read with the conjugate.

**Proof.** The general statement is *Hermitian Idempotents and the Peirce Decomposition*, §*The Corner as a Sesqualgebra*: for $u=\tilde\Pi a\tilde\Pi$ and $v=\tilde\Pi b\tilde\Pi$ the conjugate is $v^{*}=\tilde\Pi b^{*}\tilde\Pi$ and $u\star v=\tilde\Pi ab^{*}\tilde\Pi$ lies in the corner, which is stable under ${}^{*}$ and contains $\tilde\Pi$, with $u\star\tilde\Pi=u$ and no left unit in general. In the block the corner is the line $\mathbb{C}\tilde\Pi$ by §*The Biquaternion Cases*, and the formula $\lambda\tilde\Pi\star\mu\tilde\Pi=\lambda\overline{\mu}\tilde\Pi$ is the product read on it.

**Remark (the two diagonal corners and the mixed lines).** The two diagonal corners are the complex lines $\mathbb{C}\tilde\Pi$ and $\mathbb{C}\tilde\Pi^{\perp}$, each a sesqualgebra whose product is the conjugate product of the scalars and each its own conjugate image. The two mixed lines are conjugate to each other and are not corners: they carry no idempotent and no unit, and a nonzero element of one of them is a zero divisor of the multiplication, by *Zero Divisors of the General Plain Sesqualgebra*. The pair of mixed lines generates the two corners under the multiplication, since the first mixed line squares into the first corner and the second into the second by the table.

### The Two-Sided Conditions Do Not Decompose

An associative algebra presents its Peirce decomposition by the conditions $\tilde e\tilde X=\tilde X$ and $\tilde X\tilde e=\tilde X$ on the two-sided pieces. Carried to the multiplication those conditions do not cut the four spaces out of $\mathbb{B}$, and the failure is worth stating because it is the reason the decomposition has to be read on the algebra.

**Definition.** For a projection $\tilde\Pi$ the four **$\star$-Peirce pieces** are the sets

$$
\mathbb{A}_{11}=\{\tilde X:\tilde\Pi\star\tilde X=\tilde X,\ \tilde X\star\tilde\Pi=\tilde X\},\qquad
\mathbb{A}_{10}=\{\tilde X:\tilde\Pi\star\tilde X=\tilde X,\ \tilde X\star\tilde\Pi=0\},
$$

$$
\mathbb{A}_{01}=\{\tilde X:\tilde\Pi\star\tilde X=0,\ \tilde X\star\tilde\Pi=\tilde X\},\qquad
\mathbb{A}_{00}=\{\tilde X:\tilde\Pi\star\tilde X=0,\ \tilde X\star\tilde\Pi=0\}.
$$

**Theorem.** Let $\tilde\Pi$ be a projection with complement $\tilde\Pi^{\perp}$. Then

$$
\mathbb{A}_{11}=\mathbb{R}\,\tilde\Pi,\qquad \mathbb{A}_{00}=\mathbb{C}\tilde\Upsilon_1\oplus\mathbb{C}\tilde\Pi^{\perp},\qquad \mathbb{A}_{10}=\mathbb{A}_{01}=\{0\},
$$

in the notation of the four lines; the four pieces span a real subspace of dimension five and do not decompose $\mathbb{B}$; and every nonzero element of the second mixed line $\mathbb{C}\tilde\Upsilon_2$ lies in none of the four.

**Proof.** Work at the standard pair in the matrix model, so that $\tilde\Pi=E_{11}$ and the multiplication is $\tilde X\mapsto E_{11}\tilde X^{\dagger}$. The condition $\tilde X\star\tilde\Pi=\tilde X$ reads $\tilde XE_{11}=\tilde X$, that is, $\tilde X$ is supported in the first line of columns, $\tilde X=\bigl(\begin{smallmatrix}a&0\\ b&0\end{smallmatrix}\bigr)$, and the condition $\tilde\Pi\star\tilde X=\tilde X$ reads $E_{11}\tilde X^{\dagger}=\tilde X$, that is, $\bigl(\begin{smallmatrix}\overline a&\overline b\\ 0&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}a&0\\ b&0\end{smallmatrix}\bigr)$, which forces $b=0$ and $a$ real; hence $\mathbb{A}_{11}=\mathbb{R}E_{11}$. The condition $\tilde X\star\tilde\Pi=0$ reads $\tilde XE_{11}=0$, that is, $\tilde X=\bigl(\begin{smallmatrix}0&a\\ 0&b\end{smallmatrix}\bigr)$, the matrices with vanishing first column, and for such a matrix the product $E_{11}\tilde X^{\dagger}$ has vanishing second column, so it vanishes identically; hence $\mathbb{A}_{00}$ is that whole space, $\mathbb{C}E_{12}\oplus\mathbb{C}E_{22}$. Each of the two remaining pieces asks one of the products to vanish and the other to reproduce the element, which the two displays show to be impossible away from zero, so both are $\{0\}$. The mixed element $E_{21}$ has $E_{11}\star E_{21}=E_{11}E_{12}=E_{12}$, which is neither $0$ nor $E_{21}$, so it satisfies none of the four conditions; and the span of $\mathbb{R}E_{11}$, $\mathbb{C}E_{12}$, $\mathbb{C}E_{22}$ has real dimension $1+2+2=5$, less than $\dim_{\mathbb{R}}\mathbb{B}=8$, an element of $\mathbb{C}E_{21}$ completing it, so the pieces do not decompose.

**Remark (the index asymmetry).** The failure is the index rule of the table. For $\tilde X\in\mathbb{B}_{kl}$ the two products are $\tilde\Pi\star\tilde X\in\delta_{1l}\mathbb{B}_{1k}$ and $\tilde X\star\tilde\Pi\in\delta_{l1}\mathbb{B}_{k1}$, by the sesquilinear table, so both vanish as soon as the second index $l$ of $\tilde X$ is $2$: the whole of the second mixed line and of the second corner falls into $\mathbb{A}_{00}$, whereas the first mixed line falls into no piece at all. The multiplication reads the four lines through its own table, and the two-sided conditions are not the invariant that picks them out.

**Remark (the consequence).** So the Peirce decomposition of the block is the algebra's decomposition with the multiplication's table: the four spaces are the corners of the algebra, they are exchanged by the involution, their products obey the transposed rule, and the pieces defined by the two-sided conditions of the multiplication are not those spaces and do not split the space. The same phenomenon, with the general matrix model in place of the block, is the worked example of *Hermitian Idempotents and the Peirce Decomposition*, §*Two-by-Two Cases*.

## Worked Verification

The claims of the article were recomputed on the matrix model $\mathsf{M}_2$ at no more than one hundred elements per claim.

- **The ideal asymmetry.** On the matrix model the right ideal $\{M:\text{the row space of }M\text{ lies in a fixed line}\}$ was checked to satisfy $I\star\mathbb{B}=I\mathbb{B}^{*}=I\mathbb{B}\subseteq I$ on a hundred samples, and its non-stable companion $\{M:\text{the first row of }M\text{ vanishes}\}$ likewise; the mirror left ideal $\{M:\text{the first column of }M\text{ vanishes}\}$ violates the left condition $\mathbb{B}\star I\subseteq I$ on every sample, and the closure $e_0\star\mathbb{B}\tilde\Pi_1\subseteq\mathbb{B}\tilde\Pi_1$ fails while $\tilde\Pi_1\mathbb{B}\star\mathbb{B}\subseteq\tilde\Pi_1\mathbb{B}$ holds with zero residual.
- **The two tables.** For the standard pair the sixteen inclusions $\mathbb{B}_{ij}\star\mathbb{B}_{kl}\subseteq\delta_{jl}\mathbb{B}_{ik}$ were checked on the four lines with residual zero, and the entry $\mathbb{B}_{12}\star\mathbb{B}_{21}$ vanishes identically against $\mathbb{B}_{12}\mathbb{B}_{21}=\mathbb{B}_{11}$ for the algebra; the algebra inclusions $\mathbb{B}_{ij}\mathbb{B}_{kl}\subseteq\delta_{jk}\mathbb{B}_{il}$ were checked at the same time.
- **The Peirce splitting.** For a hundred random elements the four-fold sum $\tilde\Pi\tilde X\tilde\Pi+\tilde\Pi\tilde X\tilde\Pi^{\perp}+\tilde\Pi^{\perp}\tilde X\tilde\Pi+\tilde\Pi^{\perp}\tilde X\tilde\Pi^{\perp}$ reproduces $\tilde X$ with zero residual, and each summand lies in the line named.
- **The exchange.** The involution carries each mixed line to the other on a hundred elements and fixes each diagonal corner.
- **The $\star$-Peirce pieces.** At the standard pair, $\mathbb{R}\tilde\Pi$ satisfies the four conditions of $\mathbb{A}_{11}$ on a hundred real samples while $i\tilde\Pi$ fails them; $\tilde\Pi^{\perp}$, $\tilde\Upsilon_1$ and $i\tilde\Upsilon_1$ lie in $\mathbb{A}_{00}$; $\tilde\Upsilon_2$ lies in none of the four; and the four pieces span real dimension five.
- **The corners and the mixed squares.** The closures $\mathbb{B}_{11}\star\mathbb{B}_{11}\subseteq\mathbb{B}_{11}$ and $\mathbb{B}_{22}\star\mathbb{B}_{22}\subseteq\mathbb{B}_{22}$, the annihilation $\mathbb{B}_{12}\star\mathbb{B}_{21}=0=\mathbb{B}_{21}\star\mathbb{B}_{12}$, and the off-diagonal squares $\mathbb{B}_{12}\star\mathbb{B}_{12}=\mathbb{B}_{11}$, $\mathbb{B}_{21}\star\mathbb{B}_{21}=\mathbb{B}_{22}$ were each verified with zero residual, and the corner product $\lambda\tilde\Pi\star\mu\tilde\Pi=\lambda\overline\mu\tilde\Pi$ was checked on a hundred pairs of complex scalars.

## Summary

The multiplication has no proper left ideal and no proper two-sided ideal: those two lattices are the two-element chain. Its right ideals, on the other hand, are exactly the right algebra ideals, so on the right the lattice is the algebra's, with a projective line of minimal right ideals $\tilde\Pi\mathbb{B}$ of complex dimension two. The asymmetry is the conjugate in the second slot: the unit acting on the first slot produces the conjugate of an element of a left ideal, $e_0\star\tilde X=\tilde X^{*}$, and on the right the condition reads $I\star\mathbb{B}=I\mathbb{B}\subseteq I$ with the involution absent. The involution carries a left algebra ideal to a right one but does not carry a right $\star$-ideal to a left $\star$-ideal, so the two one-sided lattices are not exchanged by it.

The Peirce decomposition is the algebra's: for a projection the four spaces $\tilde\Pi_i\mathbb{B}\tilde\Pi_j$ split $\mathbb{B}$ into four complex lines, the involution exchanges the two mixed lines and fixes the two corners, each corner is a sesqualgebra whose product is the conjugate product of $\mathbb{C}$, and the two mixed lines annihilate each other while each squares into a corner. The multiplication contributes the **table**: the product of two spaces lands in the space whose first index comes from the first factor and whose second index comes from the second, so the two indices that must agree sit on the right, and the table is the transpose of the algebra's in the second factor. The algebra's minimal one-sided ideals are the sums of one diagonal with one mixed line, and the multiplication keeps the right family and destroys the left one. The four spaces defined by the two-sided conditions of the multiplication are not the Peirce spaces and do not decompose $\mathbb{B}$; the multiplication reads the algebra's decomposition with its own index rule.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, read here with the sesquilinear multiplication |
| $e_0,e_1,e_2,e_3$ | complex basis; $e_0$ the unit, $e_k$ the quaternion units, $e_1e_2=e_3$ |
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the general plain sesquilinear product, the multiplication of the block |
| ${}^{*}$ | the Hermitian conjugation, the conjugate-linear involution |
| $\tilde\Pi=\tilde\Pi_1(\hat\mu)=\tfrac12(e_0+i\hat\mu)$ | a projection, a Hermitian idempotent, a $\star$-idempotent |
| $\tilde\Pi^{\perp}=e_0-\tilde\Pi=\tilde\Pi_2(\hat\mu)$ | the complementary projection |
| $\mathbb{B}_{ij}=\tilde e_i\mathbb{B}\tilde e_j$ | the four Peirce spaces of the complementary pair |
| $\mathbb{B}\tilde\Pi$, $\tilde\Pi\mathbb{B}$ | the minimal left and right ideals of the algebra; the right one is a right $\star$-ideal, the left one is not a left $\star$-ideal |
| $\mathbb{C}\tilde\Upsilon_1$, $\mathbb{C}\tilde\Upsilon_2$ | the two mixed Peirce lines, mutually conjugate |
| $\mathbb{A}_{ij}$ | the four $\star$-Peirce pieces of the two-sided conditions |
| $\mathsf{M}_2$, $E_{ij}$ | the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ and its units, $E_{ij}E_{kl}=\delta_{jk}E_{il}$ |

## Further Reading

- *Introduction to the General Plain Sesqualgebra of Biquaternions* — the multiplication, its scalar rules and its idempotents.
- *Idempotents of the General Plain Sesqualgebra* — the projections and the complementary pair.
- *The Biquaternion Sesqualgebra Is Simple* — the two-sided simplicity of the multiplication and the minimal one-sided ideals of the algebra; its one-sided theorem is corrected on the right by §*The Three Lattices*.
- *Hermitian Idempotents and the Peirce Decomposition* — the transposed Peirce table of a derived operation and the corner as a sesqualgebra.
- *Ideals and Quotients of a Sesqualgebra* — the ideals of a general sesqualgebra.
- *Simple Sesqualgebras and Minimal Ideals* — the two notions of simplicity and the one-sided case.
- *Ideals and Peirce Decomposition of the General Plain Algebra* — the twin in the algebra, with the Peirce corners and the minimal one-sided ideals.
- *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* — the model in which the four lines are the four matrix entries.
- *Zero Divisors of the General Plain Sesqualgebra* — the elements of the mixed lines.
- *Definitions for the Study of the 12 Algebraic Structures* — the idempotent, the projection and the Peirce decomposition.
