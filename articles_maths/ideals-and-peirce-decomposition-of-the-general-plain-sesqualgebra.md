# __Ideals and Peirce Decomposition of the General Plain Sesqualgebra__

## Introduction

The general plain sesquilinear product $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ makes the biquaternion space $\mathbb{B}$ a sesqualgebra, and the two structures this article puts side by side on that multiplication are the **ideals** and the **Peirce decomposition**. In the algebra of *Ideals and Peirce Decomposition of the General Plain Algebra* the two are one subject, because a Peirce corner is a one-sided ideal; here they separate, and the separation is the point.

The **ideals** of the multiplication are the two trivial ones on the left and on both sides at once, but on the right they are as many as the algebra's: a right $\star$-ideal is exactly a right algebra ideal, so the right-sided lattice is untouched by the passage from the algebra to the multiplication, while the left-sided and the two-sided lattices collapse to the two-element chain. The asymmetry is the conjugate sitting in the second slot, and it is the first thing this article establishes. The two-sided simplicity of the multiplication is *The Biquaternion Sesqualgebra Is Simple*; the one-sided statement there treats the two sides alike, and the computation below shows they are not alike. The algebra's lattice has, on each side, a projective line of minimal ideals, and those minimal ideals are exactly the sums of two Peirce lines; the Peirce decomposition then says which of them the multiplication keeps and which it destroys, the right ones being kept and the left ones destroyed. The surviving lattice is not idle: its points are the sets $R_w=\{\tilde X:w\tilde X=0\}$, any two of them are complementary so that each pair carries a Peirce decomposition of the block, and each single one is a Hermitian line space on which the multiplication acts as a full $2\times2$ matrix algebra. The section *The Right Ideals and the Matrix Representations* proves this and reads both structures off the lattice.

The **Peirce decomposition** is the algebra's. The four spaces $\tilde\Pi_i\mathbb{B}\tilde\Pi_j$ of a projection need associativity, which the multiplication does not have, and the multiplication contributes to them a **table and nothing else**: the product of two spaces lands in the space whose two indices must agree, and the two indices that must agree sit on the right in the sesquilinear table whereas they sit in the middle in the algebra table. The table is therefore the **transpose** of the algebra's in the second factor, its index rule is not the parity grading of the algebra, and the elements that index it are the **projections**, the Hermitian idempotents, which are exactly the idempotents of the multiplication by *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*; and the decompositions are as many as the complete orthogonal pairs of those projections: one degenerate decomposition and a real projective plane of them (§*As Many Decompositions as the Hermitian Roots of One*). The general form of the transposed table is *Hermitian Idempotents and the Peirce Decomposition*; what is added here is the biquaternion instance, the four lines in the coefficients of the block, the transport through the matrix model, the form the involution takes on the two mixed lines, and the failure of the two-sided conditions of the multiplication to reproduce the four spaces.

**Boundaries.** The multiplication, its scalar rules and its idempotents are *Introduction to the General Plain Sesqualgebra of Biquaternions*; the projections and their complementary pairs are *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*; the ideals of a general sesqualgebra are *Ideals and Quotients of a Sesqualgebra*, and the two notions of simplicity are *Simple Sesqualgebras and Minimal Ideals*; the ideals of the block are *The Biquaternion Sesqualgebra Is Simple*, whose two-sided theorem this article quotes and whose one-sided theorem it corrects on the right; the transposed Peirce table of a derived operation is *Hermitian Idempotents and the Peirce Decomposition*; the algebra's ideal theory, its Peirce decomposition and its minimal one-sided ideals are *Ideals and Peirce Decomposition of the General Plain Algebra*; the model in which the four lines are the four matrix entries is *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*; the Hermitian module whose restriction of the scalar form is carried by the right ideals is *Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint*; and the general definition of the idempotent, the projection and the Peirce decomposition is *Definitions for the Study of the 12 Algebraic Structures*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$, with $e_0$ the unit and $e_1e_2=e_3$, and $i$ is the central scalar imaginary. Juxtaposition is the **plain** product $\tilde P\tilde Q$ of *Introduction to the General Plain Algebra of Biquaternions*, $\star$ is the multiplication of this block, $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$, and ${}^{*}={}^{\natural}\circ\bar{\cdot}$ is the Hermitian conjugation of *Biquaternions as a Vector Space over $\mathbb{C}$*. A **projection** is a Hermitian idempotent, and the projections are exactly the $\star$-idempotents; they are written

$$
\tilde\Pi_+(\tilde\Xi)=\tfrac12\bigl(e_0+\tilde\Xi\bigr),\qquad \tilde\Pi_-(\tilde\Xi)=e_0-\tilde\Pi_+(\tilde\Xi)=\tfrac12\bigl(e_0-\tilde\Xi\bigr),
$$

with $\tilde\Xi=i\hat n$, where $\hat n$ is a real vector of the vector subspace with $(\hat n,\hat n)=1$. The pair $\tilde\Pi_+(\tilde\Xi),\tilde\Pi_-(\tilde\Xi)$ is the **complementary pair** of *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*, and it is the pair $\tilde\Pi_\pm(\tilde\Xi)=\tfrac12(e_0\pm\tilde\Xi)$ of the Hermitian root $\tilde\Xi=i\hat n$, the notation of that article's §*The Two Idempotents of a Root*. The matrix model $\mathsf{M}_2$ is the algebra isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ of *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, with $\mathsf{M}_2(e_0)=\mathrm{I}_2$ and $\mathsf{M}_2(e_k)=-i\sigma_k$ on the three quaternion units.

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

Let $\tilde\Pi$ be a projection, $\tilde\Pi^{\perp}=e_0-\tilde\Pi=\tilde\Pi_-(\tilde\Xi)$ its complement, and put $\tilde e_1=\tilde\Pi,\tilde e_2=\tilde\Pi^{\perp}$. The four **Peirce spaces** are the intersections

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

**Proposition (the four lines).** For the complementary pair $\tilde\Pi=\tilde\Pi_+(\tilde\Xi)$, $\tilde\Pi^{\perp}=\tilde\Pi_-(\tilde\Xi)$ the Peirce decomposition of the block is

$$
\mathbb{B}=\tilde\Pi\mathbb{B}\tilde\Pi\oplus\tilde\Pi\mathbb{B}\tilde\Pi^{\perp}\oplus\tilde\Pi^{\perp}\mathbb{B}\tilde\Pi\oplus\tilde\Pi^{\perp}\mathbb{B}\tilde\Pi^{\perp},
$$

with complex one-dimensional summands

$$
\tilde\Pi\mathbb{B}\tilde\Pi=\mathbb{C}\tilde\Pi,\quad
\tilde\Pi\mathbb{B}\tilde\Pi^{\perp}=\mathbb{C}\tilde\Upsilon_1(\hat n),\quad
\tilde\Pi^{\perp}\mathbb{B}\tilde\Pi=\mathbb{C}\tilde\Upsilon_2(\hat n),\quad
\tilde\Pi^{\perp}\mathbb{B}\tilde\Pi^{\perp}=\mathbb{C}\tilde\Pi^{\perp},
$$

where $\tilde\Upsilon_1(\hat n)$ is any nonzero element of the first mixed space and $\tilde\Upsilon_2(\hat n)=\tilde\Upsilon_1(\hat n)^{*}$ is its conjugate in the second. Each summand has real dimension two and the total is eight.

**Proof.** The decomposition, the one-dimensionality of the four summands and the identification of the two mixed spaces as conjugate are *Ideals and Peirce Decomposition of the General Plain Algebra*, §*The Biquaternion Case* and §*From One Idempotent to Its Complement*, transported to the pair $(\tilde\Pi,\tilde\Pi^{\perp})$, a complete orthogonal family by *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*, §*The Complement and the Pairing of the Directions*.

**Example (the standard pair as coordinates).** At the axis $\hat n=\hat e_3$ the projection is the standard idempotent $\tilde\Pi_1(\hat e_3)=\tfrac12(e_0+ie_3)$, its complement is $\tilde\Pi_2(\hat e_3)=\tfrac12(e_0-ie_3)$, and the matrix model sends the four lines to the four matrix units,

$$
\tilde\Pi\longleftrightarrow E_{11},\qquad \tilde\Upsilon_1(\hat e_3)\longleftrightarrow E_{12},\qquad \tilde\Upsilon_2(\hat e_3)\longleftrightarrow E_{21},\qquad \tilde\Pi^{\perp}\longleftrightarrow E_{22},
$$

as the transport of *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* records; the Peirce coordinates of an element are therefore the four entries of its matrix, grouped by the projection instead of by the basis.

**Remark (what is the multiplication's and what is the algebra's).** The four lines are the algebra's: they do not need the multiplication and they do not depend on it. Two things do depend on it. The first is the choice of the idempotent: the pair $(\tilde\Pi,\tilde\Pi^{\perp})$ that indexes the decomposition is made of projections, and the projections are the Hermitian idempotents, which are exactly the idempotents of the multiplication, so the decomposition can be indexed by the multiplication's own idempotents, a supply the algebra's decomposition does not provide. The second is the table, which is the subject of §*The Table in the Standard Pair*.

### As Many Decompositions as the Hermitian Roots of One

**The complete orthogonal pairs of the block are exactly the pairs $\tilde\Pi_+(\tilde\Xi),\tilde\Pi_-(\tilde\Xi)$ of a Hermitian root $\tilde\Xi$ of $+1$, so the Peirce decompositions of the block are in bijection with the Hermitian roots modulo the sign change $\tilde\Xi\sim-\tilde\Xi$: one degenerate decomposition for the class $\{\pm e_0\}$ and a real projective plane of decompositions for the classes of the $\tilde\Xi$, and no other.**

Write the pair of the root in the two signs, $\tilde\Pi_\pm(\tilde\Xi)=\tfrac12(e_0\pm\tilde\Xi)$, as *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*, §*The Two Idempotents of a Root*, and put

$$
\mathbb{B}_{st}=\tilde\Pi_s\,\mathbb{B}\,\tilde\Pi_t,\qquad s,t\in\{+,-\},
$$

for the four corners. They are the four spaces of §*The Definition* taken on the pair $(\tilde\Pi_+,\tilde\Pi_-)$, which is complete and orthogonal by the same article, §*The Arithmetic of the Pair of Idempotents*:

$$
\mathbb{B}=\mathbb{B}_{++}\oplus\mathbb{B}_{+-}\oplus\mathbb{B}_{-+}\oplus\mathbb{B}_{--},
$$

each corner a complex line when the root is not $\pm e_0$, by §*The Biquaternion Cases* read at $\tilde\Pi=\tilde\Pi_+(\tilde\Xi)$, whose complement is $\tilde\Pi_-=\tilde\Pi_-(\tilde\Xi)$.

**The root on the corners.** The two signs are the two eigenvalues of multiplication by the root, and each corner collects one on the left and one on the right,

$$
x\in\mathbb{B}_{st}\iff\tilde\Xi x=s\,x\ \text{ and }\ x\tilde\Xi=t\,x,
$$

so $\mathbb{B}_{st}$ is the joint eigenspace of the operators of left and right multiplication by the root with the eigenvalues $s$ and $t$. The forward implication is the definition of the corner, $\tilde\Pi_s x=x\tilde\Pi_t=x$; the reverse reads $\tilde\Pi_sx=\tfrac12(e_0+s\tilde\Xi)x=\tfrac12(x+s\,sx)=x$ and $\tilde\Pi_sx\tilde\Pi_t=x$. This is the statement of the parent, §*The Biquaternion Case* of *Ideals and Peirce Decomposition of the General Plain Algebra*, and it holds here unchanged: the corners are the algebra's, and the root that indexes them is a Hermitian root, which the multiplication itself supplies.

**The bijection.** A complete orthogonal pair of the block is a pair of orthogonal idempotents summing to $e_0$, and the idempotents of the block are the Hermitian idempotents of the algebra, so $\tilde\Xi=\tilde\Pi_+-\tilde\Pi_-$ is Hermitian and has square $\tilde\Xi^2=\tilde\Pi_+^2-\tilde\Pi_+\tilde\Pi_--\tilde\Pi_-\tilde\Pi_++\tilde\Pi_-^2=\tilde\Pi_++\tilde\Pi_-=e_0$: a Hermitian root of $+1$, whose pair the given pair is. Conversely a Hermitian root gives its pair, and the root is read back, $\tilde\Xi=\tilde\Pi_+-\tilde\Pi_-$, so a complete orthogonal pair determines the root up to the interchange of its two members. That interchange is exactly the replacement of the root by its opposite, $\tilde\Pi_+(-\tilde\Xi)=\tilde\Pi_-(\tilde\Xi)$ and $\tilde\Pi_-(-\tilde\Xi)=\tilde\Pi_+(\tilde\Xi)$. So the classes $\{\tilde\Xi,-\tilde\Xi\}$ of Hermitian roots of $+1$, the complete orthogonal pairs of the block and the Peirce decompositions of the block correspond one to one.

**The count.** The Hermitian roots of $+1$ are $\pm e_0$ and the roots $\tilde\Xi=i\hat n$ over the real unit vectors $\hat n$ (*Square Roots of One and the Idempotents of the General Plain Sesqualgebra*, §*The Hermitian Roots of One*). The class $\{\pm e_0\}$ gives the pair $(e_0,0)$ and the **degenerate decomposition**, whose corners are $\mathbb{B}$ and $0$ rather than four lines. A class $\{\tilde\Xi,-\tilde\Xi\}$ gives the pair $(\tilde\Pi_+(\tilde\Xi),\tilde\Pi_-(\tilde\Xi))$ of §*The Biquaternion Cases*, and the change $\hat n\mapsto-\hat n$ leaves the pair unchanged, two antipodal directions giving the same decomposition; the classes of the non-trivial Hermitian roots are therefore the points of the **real projective plane** of the directions, the same projective plane as the right lattice of §*The Complementary Pairs and the Peirce Decompositions*. So the Peirce decompositions of the block are one degenerate decomposition and a real projective plane of decompositions.

**Remark (the contrast with the algebra, and why).** The parent's decompositions are as many as its roots of $+1$ modulo the sign, in three families: the trivial one, the purely imaginary one and a four-real-parameter one. Here the four-parameter family does not descend, because only the Hermitian roots carry idempotents, the idempotents of the block being exactly the Hermitian idempotents of the algebra: an oblique pair $(e,e_0-e)$ of §*The Complementary Pairs and the Peirce Decompositions*, whose idempotents are not Hermitian, still splits $\mathbb{B}$ and still carries the algebra's table, but it is not a pair of the multiplication and its class is not among the ones counted here. The count is the Peirce reading of the halving map of *Square Roots of One and the Idempotents of the General Plain Sesqualgebra*: the map takes the Hermitian roots onto the idempotents, and the idempotents index the decompositions of the block.

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

**Proof.** $(\tilde e_ia\tilde e_j)^{*}=\tilde e_j^{*}a^{*}\tilde e_i^{*}=\tilde e_ja^{*}\tilde e_i\in\mathbb{B}_{ji}$ because the two projections are Hermitian, and ${}^{*}$ is an involution, so the inclusion is an equality. The standard-pair statement is the definition $\tilde\Upsilon_2(\hat n)=\tilde\Upsilon_1(\hat n)^{*}$.

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

## The Right Ideals and the Matrix Representations

The right $\star$-ideals are the nontrivial half of the lattice of §*The Three Lattices*, and they carry more than their own definition: they index the Peirce decompositions of the block and they index its $2\times2$ matrix representations. This section writes them out and reads both structures off them.

### The Explicit Right Ideals

**Proposition (the right ideals, explicitly).** Under the model $\mathbb{B}\cong M_2(\mathbb{C})$ the proper nonzero right $\star$-ideals are the sets

$$
R_w=\{\tilde X:w\tilde X=0\},\qquad 0\neq w\in\mathbb{C}^2,
$$

one for each line $\mathbb{C}w$ of the row space; equivalently $R_w=\tilde\Pi\mathbb{B}$ for the rank-one projection $\tilde\Pi$ onto the line $\ker w$ of $\mathbb{C}^2$. Two forms give the same ideal exactly when they are proportional, $R_w=R_{w'}\iff w'\in\mathbb{C}^{\times}w$, so the right lattice is a projective line of minimal right ideals, one point for each projection $\tilde\Pi=\tilde\Pi_+(\tilde\Xi)$.

**Proof.** The set $R_w$ is a right ideal because $w(\tilde X\tilde Y)=(w\tilde X)\tilde Y=0$. Its elements are the matrices whose columns lie in the line $\ker w$, so $\dim_{\mathbb{C}}R_w=2$, and it is minimal: a nonzero element has a nonzero column, $\tilde X=uc^{\mathrm{T}}$ with $u$ spanning $\ker w$ and $c\neq0$, and then $\tilde X\mathbb{B}=\{u(c^{\mathrm{T}}\tilde Y):\tilde Y\}=\{u c'^{\mathrm{T}}\}=R_w$. If $u$ is a unit vector spanning $\ker w$ and $\tilde\Pi=uu^{\dagger}$, then $\tilde\Pi\tilde X=\tilde X$ exactly for the matrices with columns in $\ker w$, so $R_w=\tilde\Pi\mathbb{B}$; and $R_w=R_{w'}$ forces $\ker w=\ker w'$, hence $w'$ proportional to $w$.

**Example (the standard pair).** The form $w=(0,1)$ imposes the vanishing of the second row, so $R_{(0,1)}=E_{11}M_2$ is the span of the first row of the model, the minimal right ideal $\tilde\Pi_1(\hat e_3)\mathbb{B}$; the form $w=(1,0)$ imposes the vanishing of the first row and gives the span of the second row, $\tilde\Pi_2(\hat e_3)\mathbb{B}$. The two are the points of the lattice that the matrix model singles out.

### The Complementary Pairs and the Peirce Decompositions

**Theorem (two distinct right ideals are complementary).** Let $w,w'$ be nonzero and not proportional. Then $R_w\cap R_{w'}=\{0\}$ and $\mathbb{B}=R_w\oplus R_{w'}$.

**Proof.** An element of the intersection annihilates $w$ and $w'$ on the left; the two are independent, hence span the row space, so $y\tilde X=0$ for every row $y$ and $\tilde X=0$. The two spaces have complex dimension two by the proposition, and $\dim_{\mathbb{C}}\mathbb{B}=4$, so their sum is direct and total.

**Corollary (an idempotent for each ordered pair).** Let $w,w'$ be nonzero and not proportional, and let $u$ span $\ker w$. Then

$$
\tilde e_{w,w'}=\frac{u\,w'}{w'u}
$$

is an idempotent with $\tilde e_{w,w'}\mathbb{B}=R_w$, and the complementary idempotent $e_0-\tilde e_{w,w'}$ generates $R_{w'}$.

**Proof.** $\tilde e^{2}=u(w'u)w'/(w'u)^{2}=\tilde e$; $w\tilde e=0$ gives $\operatorname{im}\tilde e\subseteq\ker w$, and $\tilde e\neq0$ has rank one, so $\operatorname{im}\tilde e=\ker w$ and $\tilde e\mathbb{B}=R_w$; and $\tilde e\tilde X=u(w'\tilde X)/(w'u)$ vanishes exactly for the $\tilde X$ with $w'\tilde X=0$, so the complementary idempotent generates $R_{w'}$.

**Corollary (a Peirce decomposition for each pair).** For the complete orthogonal family $(\tilde e,e_0-\tilde e)$ the four Peirce spaces are complex lines and

$$
\mathbb{B}=\tilde e\mathbb{B}\tilde e\oplus\tilde e\mathbb{B}(e_0-\tilde e)\oplus(e_0-\tilde e)\mathbb{B}\tilde e\oplus(e_0-\tilde e)\mathbb{B}(e_0-\tilde e),
$$

with the **algebra table** $\mathbb{B}_{ij}\mathbb{B}_{kl}\subseteq\delta_{jk}\mathbb{B}_{il}$ of §*The Two Tables*. So every unordered pair of distinct points of the right lattice carries a Peirce decomposition of the block.

**Proof.** $e_0-\tilde e$ is the complementary idempotent of the corollary, and the decomposition with the algebra table is the algebra's, §*The Definition* and §*The Two Tables*.

**Theorem (the pairs that are Hermitian).** The idempotent $\tilde e_{w,w'}$ is Hermitian if and only if $w\perp w'$, and then the pair $(\tilde e,\tilde e^{\perp})$ is the complementary pair of projections of the conventions.

**Proof.** If $w\perp w'$ take $u=w'^{*}/\|w'\|^{2}$, so that $w'u=1$ and $\tilde e=w'^{*}w'/\|w'\|^{2}$, the orthogonal projection onto the line $\mathbb{C}w'^{*}=\ker w$, Hermitian. Conversely a Hermitian idempotent is the orthogonal projection onto its image, so a Hermitian $\tilde e_{w,w'}$ has $\operatorname{im}\tilde e=(\ker\tilde e)^{\perp}$, that is, $\ker w=(\ker w')^{\perp}$, which says $w\perp w'$.

**Corollary (the two tables on a pair).** For $w\perp w'$ the decomposition of the previous corollary is the Peirce decomposition of the block of §*The Biquaternion Cases*, and the **sesquilinear table** $\mathbb{B}_{ij}\star\mathbb{B}_{kl}\subseteq\delta_{jl}\mathbb{B}_{ik}$ holds on its four lines. For an oblique pair $w\not\perp w'$ the four lines still split the space and still obey the algebra table, but the sesquilinear table fails.

**Proof.** The proof of the transposed table uses $\tilde e_k^{*}=\tilde e_k$ for the two idempotents; that holds exactly when the pair is Hermitian, by the theorem.

**Remark (the reading).** The transposed table of §*The Two Tables*, and with it the whole sesquilinear Peirce theory, is therefore available exactly at the pairs of **orthogonal** right ideals, which are the pairs of projections of the block; an oblique pair gives a non-Hermitian complete family, on which the algebra's decomposition survives and the multiplication's table does not.

### The Matrix Representations from the Right Ideals

**Proposition (the right ideal as a Hermitian space).** Let $w\neq0$ and let $u$ be a unit vector spanning $\ker w$. Then $R_w$ is a complex two-dimensional Hermitian space for the restriction of the scalar form $\langle\tilde X,\tilde Y\rangle=\mathrm{Sc}(\tilde X^{*}\tilde Y)$, positive definite, with the two matrices $ue_1^{\mathrm{T}},ue_2^{\mathrm{T}}$ as an orthogonal basis of Gram matrix $\tfrac12\mathrm{I}_2$.

**Theorem (the right action).** The right action

$$
\varphi\colon\mathbb{B}\longrightarrow\operatorname{End}_{\mathbb{C}}(R_w),\qquad\varphi(\beta)(\tilde X)=\tilde X\beta,
$$

is an anti-isomorphism of complex algebras, $\varphi(\beta\gamma)=\varphi(\gamma)\varphi(\beta)$, and it satisfies

$$
\langle\tilde X\beta,\tilde Y\rangle=\langle\tilde X,\tilde Y\beta^{*}\rangle ,
$$

so $\varphi(\beta^{*})$ is the adjoint of $\varphi(\beta)$ for the form of the proposition.

**Proof.** $(\tilde X\beta)\gamma=\tilde X(\beta\gamma)$ gives the reversal. For the adjoint, $\operatorname{tr}=2\,\mathrm{Sc}$ on the scalar part and the trace is cyclic, so

$$
\langle\tilde X\beta,\tilde Y\rangle=\tfrac12\operatorname{tr}\bigl((\tilde X\beta)^{\dagger}\tilde Y\bigr)=\tfrac12\operatorname{tr}\bigl(\beta^{\dagger}\tilde X^{\dagger}\tilde Y\bigr)=\tfrac12\operatorname{tr}\bigl(\tilde X^{\dagger}\tilde Y\beta^{\dagger}\bigr)=\langle\tilde X,\tilde Y\beta^{*}\rangle .
$$

The injectivity of $\varphi$: $\varphi(\beta)=0$ means $\tilde X\beta=0$ for every $\tilde X\in R_w$, so $R_w\mathbb{B}\beta=R_w\beta=0$, that is, the product of the two nonzero right ideals $R_w$ and $\mathbb{B}\beta$ is zero, which a simple algebra does not allow; hence $\beta=0$. The dimensions agree, $\dim_{\mathbb{C}}\mathbb{B}=4=\dim_{\mathbb{C}}\operatorname{End}_{\mathbb{C}}(R_w)$, so $\varphi$ is onto.

**Corollary (the matrix representation).** Let $\tau$ be the transpose of the model, $\mathsf{M}_2(\tau(\beta))=\mathsf{M}_2(\beta)^{\mathrm{T}}$, an anti-automorphism of $\mathbb{B}$ with $\tau(\beta^{*})=\tau(\beta)^{*}$. Then

$$
\rho(\beta)\colon\tilde X\longmapsto\tilde X\,\tau(\beta)
$$

is an isomorphism of complex algebras of $\mathbb{B}$ onto $\operatorname{End}_{\mathbb{C}}(R_w)\cong M_2(\mathbb{C})$ with $\rho(\beta^{*})=\rho(\beta)^{*}$, hence an isomorphism of **sesqualgebras**

$$
\rho\colon(\mathbb{B},\star,{}^{*})\longrightarrow\bigl(M_2(\mathbb{C}),\,(A,B)\mapsto AB^{\dagger},\,{}^{\dagger}\bigr).
$$

**Proof.** $\rho=\varphi\circ\tau$ is multiplicative because the two reversals cancel, and it carries the involution to the adjoint because $\tau$ commutes with it and $\varphi$ does so in the sense above; and $\rho(\beta\star\gamma)=\rho(\beta\gamma^{*})=\rho(\beta)\rho(\gamma^{*})=\rho(\beta)\rho(\gamma)^{*}$.

**Corollary (one realization for each point of the lattice).** The block therefore has a $2\times2$ matrix realization for each point of the projective line of its right $\star$-ideals: the matrix of a parameter $\beta$ is the coordinate matrix of the operator $\tilde X\mapsto\tilde X\tau(\beta)$ in the basis $ue_i^{\mathrm{T}}$ of $R_w$, and the standard model $\mathsf{M}_2$ of *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* is the member of the family at the standard pair $R_w=\tilde\Pi_1(\hat e_3)\mathbb{B}$.

**Remark (the family is one orbit).** The constructions at two different points of the lattice differ by a $*$-automorphism of $M_2(\mathbb{C})$, and the $*$-automorphisms of $M_2(\mathbb{C})$ are the conjugations by the unitary group; the family of realizations is therefore a single unitary-conjugacy orbit, indexed by the projective line of the right ideals.

**Remark (why the transpose, and the contrast with the left ideals).** The ideal is a **right** module, so the multiplication acts on the right and its action reverses the order; the transpose is what turns the anti-isomorphism into an isomorphism, and the involution is what makes the transpose respect it. The mirror construction on the **left** ideals $\mathbb{B}\tilde\Pi$ needs no transpose, because left multiplication is multiplicative, but those ideals are not $\star$-ideals by §*The Three Lattices* (i), so they carry no part of the sesquilinear structure: the representatives of the multiplication sit on the right, and the left ideals, which the multiplication destroys, lie outside.

**Remark (already inside the module theory).** The space $R_w$ with its form is the simple Hermitian module of *Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint*, where the Gram matrix is $\frac12\mathrm{I}_2$ and the action is a $*$-representation; what this section adds is the **index set**, one simple module and one realization for each point of the right lattice, the two descriptions meeting at the standard pair.

## Worked Verification

The claims of the article were recomputed on the matrix model $\mathsf{M}_2$ at no more than one hundred elements per claim.

- **The ideal asymmetry.** On the matrix model the right ideal $\{M:\text{the column space of }M\text{ lies in a fixed line}\}$ was checked to satisfy $I\star\mathbb{B}=I\mathbb{B}^{*}=I\mathbb{B}\subseteq I$ on a hundred samples, and its non-stable companion $\{M:\text{the first row of }M\text{ vanishes}\}$ likewise; the mirror left ideal $\{M:\text{the first column of }M\text{ vanishes}\}$ violates the left condition $\mathbb{B}\star I\subseteq I$ on every sample, and the closure $e_0\star\mathbb{B}\tilde\Pi_1\subseteq\mathbb{B}\tilde\Pi_1$ fails while $\tilde\Pi_1\mathbb{B}\star\mathbb{B}\subseteq\tilde\Pi_1\mathbb{B}$ holds with zero residual.
- **The two tables.** For the standard pair the sixteen inclusions $\mathbb{B}_{ij}\star\mathbb{B}_{kl}\subseteq\delta_{jl}\mathbb{B}_{ik}$ were checked on the four lines with residual zero, and the entry $\mathbb{B}_{12}\star\mathbb{B}_{21}$ vanishes identically against $\mathbb{B}_{12}\mathbb{B}_{21}=\mathbb{B}_{11}$ for the algebra; the algebra inclusions $\mathbb{B}_{ij}\mathbb{B}_{kl}\subseteq\delta_{jk}\mathbb{B}_{il}$ were checked at the same time.
- **The Peirce splitting.** For a hundred random elements the four-fold sum $\tilde\Pi\tilde X\tilde\Pi+\tilde\Pi\tilde X\tilde\Pi^{\perp}+\tilde\Pi^{\perp}\tilde X\tilde\Pi+\tilde\Pi^{\perp}\tilde X\tilde\Pi^{\perp}$ reproduces $\tilde X$ with zero residual, and each summand lies in the line named.
- **The exchange.** The involution carries each mixed line to the other on a hundred elements and fixes each diagonal corner.
- **The $\star$-Peirce pieces.** At the standard pair, $\mathbb{R}\tilde\Pi$ satisfies the four conditions of $\mathbb{A}_{11}$ on a hundred real samples while $i\tilde\Pi$ fails them; $\tilde\Pi^{\perp}$, $\tilde\Upsilon_1$ and $i\tilde\Upsilon_1$ lie in $\mathbb{A}_{00}$; $\tilde\Upsilon_2$ lies in none of the four; and the four pieces span real dimension five.
- **The corners and the mixed squares.** The closures $\mathbb{B}_{11}\star\mathbb{B}_{11}\subseteq\mathbb{B}_{11}$ and $\mathbb{B}_{22}\star\mathbb{B}_{22}\subseteq\mathbb{B}_{22}$, the annihilation $\mathbb{B}_{12}\star\mathbb{B}_{21}=0=\mathbb{B}_{21}\star\mathbb{B}_{12}$, and the off-diagonal squares $\mathbb{B}_{12}\star\mathbb{B}_{12}=\mathbb{B}_{11}$, $\mathbb{B}_{21}\star\mathbb{B}_{21}=\mathbb{B}_{22}$ were each verified with zero residual, and the corner product $\lambda\tilde\Pi\star\mu\tilde\Pi=\lambda\overline\mu\tilde\Pi$ was checked on a hundred pairs of complex scalars.
- **The right ideals and their complements.** For the pairs of forms $(1,0),(0,1)$, $(1,0),(1,1)$ and $(1,2),(3,1)$ the intersection $R_w\cap R_{w'}$ was found of complex dimension zero and the sum of dimension four; the idempotent $\tilde e_{w,w'}$ was idempotent with $\tilde e+\tilde e^{\perp}=\mathrm{I}_2$, $\tilde e\mathbb{B}=R_w$ and $\tilde e^{\perp}\mathbb{B}=R_{w'}$ on a hundred samples each; and it was Hermitian exactly for the orthogonal pair $(1,0),(0,1)$, the oblique pairs giving non-Hermitian idempotents.
- **The two tables on the pairs.** On the Hermitian pair the transposed sesquilinear inclusions hold on the four lines with zero residual, while on the oblique pair the mixed products violate them on every sample whereas the algebra inclusions hold for both pairs.
- **The corners of the pair of a root.** For the Hermitian roots $e_0$, $-e_0$, $ie_1$ and $i(e_2+e_3)/\sqrt2$ the four corners $\tilde\Pi_s\mathbb{B}\tilde\Pi_t$ of §*As Many Decompositions as the Hermitian Roots of One* were found of complex dimension one each, the root was checked to act on each as the two signs $s$ and $t$, the product rule $\mathbb{B}_{st}\mathbb{B}_{uv}\subseteq\delta_{tu}\mathbb{B}_{sv}$ was checked on eight index pairs, the root and its opposite were checked to give the same unordered pair, and the degenerate pair $(e_0,0)$ was checked to give the corners $\mathbb{B}$ and $0$ rather than four lines.
- **The realization.** The right action $\varphi(\beta)(\tilde X)=\tilde X\beta$ reversed the product on a hundred pairs, satisfied $\varphi(\beta^{*})=\varphi(\beta)^{*}$ for the restricted form on every sample, and its image spanned the four-dimensional $\operatorname{End}_{\mathbb{C}}(R_w)$; the assignment $\rho(\beta)=\varphi(\beta^{\mathrm{T}})$ was multiplicative and $*$-equivariant and carried $\star$ to the composition with the adjoint on a hundred pairs; and the restriction of the scalar form to $R_w$ had Gram matrix $\tfrac12\mathrm{I}_2$ in the basis $ue_i^{\mathrm{T}}$.

## Summary

The multiplication has no proper left ideal and no proper two-sided ideal: those two lattices are the two-element chain. Its right ideals, on the other hand, are exactly the right algebra ideals, so on the right the lattice is the algebra's, with a projective line of minimal right ideals $\tilde\Pi\mathbb{B}$ of complex dimension two. The asymmetry is the conjugate in the second slot: the unit acting on the first slot produces the conjugate of an element of a left ideal, $e_0\star\tilde X=\tilde X^{*}$, and on the right the condition reads $I\star\mathbb{B}=I\mathbb{B}\subseteq I$ with the involution absent. The involution carries a left algebra ideal to a right one but does not carry a right $\star$-ideal to a left $\star$-ideal, so the two one-sided lattices are not exchanged by it.

The Peirce decomposition is the algebra's: for a projection the four spaces $\tilde\Pi_i\mathbb{B}\tilde\Pi_j$ split $\mathbb{B}$ into four complex lines, the involution exchanges the two mixed lines and fixes the two corners, each corner is a sesqualgebra whose product is the conjugate product of $\mathbb{C}$, and the two mixed lines annihilate each other while each squares into a corner. The multiplication contributes the **table**: the product of two spaces lands in the space whose first index comes from the first factor and whose second index comes from the second, so the two indices that must agree sit on the right, and the table is the transpose of the algebra's in the second factor. The algebra's minimal one-sided ideals are the sums of one diagonal with one mixed line, and the multiplication keeps the right family and destroys the left one. The four spaces defined by the two-sided conditions of the multiplication are not the Peirce spaces and do not decompose $\mathbb{B}$; the multiplication reads the algebra's decomposition with its own index rule. The pair that indexes a decomposition is the pair $\tilde\Pi_\pm(\tilde\Xi)=\tfrac12(e_0\pm\tilde\Xi)$ of a Hermitian root of $+1$, and the decompositions of the block are as many as those roots modulo the sign: one degenerate decomposition and a real projective plane of them.

The proper right $\star$-ideals are the sets $R_w=\{\tilde X:w\tilde X=0\}$, one for each point of the projective line, and they index both structures. Any two distinct ones are complementary, and each pair carries an idempotent $\tilde e_{w,w'}$, so every unordered pair of points carries a Peirce decomposition of the block; the pair is Hermitian exactly when the two forms are orthogonal, which is exactly when the transposed sesquilinear table is available. Each single right ideal is a positive definite Hermitian line space of Gram matrix $\tfrac12\mathrm{I}_2$, and the right multiplication on it is a $*$-equivariant anti-isomorphism of $\mathbb{B}$; the transpose converts it into an isomorphism of **sesqualgebras** onto $\bigl(M_2(\mathbb{C}),(A,B)\mapsto AB^{\dagger},{}^{\dagger}\bigr)$, so the block has a $2\times2$ matrix realization for each point of the lattice, the standard model being the member at the standard pair. The transpose is needed because the ideal is a right module; the mirror construction on the left ideals, which are not $\star$-ideals, needs none and carries nothing.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, read here with the sesquilinear multiplication |
| $e_0,e_1,e_2,e_3$ | complex basis; $e_0$ the unit, $e_k$ the quaternion units, $e_1e_2=e_3$ |
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the general plain sesquilinear product, the multiplication of the block |
| ${}^{*}$ | the Hermitian conjugation, the conjugate-linear involution |
| $\tilde\Pi=\tilde\Pi_+(\tilde\Xi)=\tfrac12(e_0+\tilde\Xi)$ | a projection, a Hermitian idempotent, a $\star$-idempotent |
| $\tilde\Pi^{\perp}=e_0-\tilde\Pi=\tilde\Pi_-(\tilde\Xi)$ | the complementary projection |
| $\mathbb{B}_{ij}=\tilde e_i\mathbb{B}\tilde e_j$ | the four Peirce spaces of the complementary pair |
| $\tilde\Pi_\pm(\tilde\Xi)=\tfrac12(e_0\pm\tilde\Xi)$, $\mathbb{B}_{st}=\tilde\Pi_s\mathbb{B}\tilde\Pi_t$ | the pair of a Hermitian root of $+1$ and the corners it indexes, $s,t\in\{+,-\}$ |
| $\mathbb{B}\tilde\Pi$, $\tilde\Pi\mathbb{B}$ | the minimal left and right ideals of the algebra; the right one is a right $\star$-ideal, the left one is not a left $\star$-ideal |
| $\mathbb{C}\tilde\Upsilon_1$, $\mathbb{C}\tilde\Upsilon_2$ | the two mixed Peirce lines, mutually conjugate |
| $\mathbb{A}_{ij}$ | the four $\star$-Peirce pieces of the two-sided conditions |
| $R_w=\{\tilde X:w\tilde X=0\}$ | the proper right $\star$-ideals, one for each point of the projective line; $R_w=\tilde\Pi\mathbb{B}$ |
| $\tilde e_{w,w'}=uw'/(w'u)$ | the idempotent of an ordered pair of distinct right ideals, Hermitian exactly when $w\perp w'$ |
| $\varphi(\beta)(\tilde X)=\tilde X\beta$ | the right action on $R_w$, a $*$-equivariant algebra anti-isomorphism onto $\operatorname{End}_{\mathbb{C}}(R_w)$ |
| $\tau$, $\rho=\varphi\circ\tau$ | the transpose of the model and the resulting $*$-isomorphism of sesqualgebras onto $M_2(\mathbb{C})$ |
| $\mathsf{M}_2$, $E_{ij}$ | the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$ and its units, $E_{ij}E_{kl}=\delta_{jk}E_{il}$ |

## Further Reading

- *Introduction to the General Plain Sesqualgebra of Biquaternions* — the multiplication, its scalar rules and its idempotents.
- *Square Roots of One and the Idempotents of the General Plain Sesqualgebra* — the projections, the complementary pair and the pair of a Hermitian root that indexes the decompositions.
- *The Biquaternion Sesqualgebra Is Simple* — the two-sided simplicity of the multiplication and the minimal one-sided ideals of the algebra; its one-sided theorem is corrected on the right by §*The Three Lattices*.
- *Hermitian Idempotents and the Peirce Decomposition* — the transposed Peirce table of a derived operation and the corner as a sesqualgebra.
- *Ideals and Quotients of a Sesqualgebra* — the ideals of a general sesqualgebra.
- *Simple Sesqualgebras and Minimal Ideals* — the two notions of simplicity and the one-sided case.
- *Ideals and Peirce Decomposition of the General Plain Algebra* — the twin in the algebra, with the Peirce corners and the minimal one-sided ideals.
- *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* — the model in which the four lines are the four matrix entries.
- *Zero Divisors of the General Plain Sesqualgebra* — the elements of the mixed lines.
- *Hermitian Modules over the Biquaternion Algebra with Hermitian Adjoint* — the simple Hermitian module $\mathbb{B}\tilde\Pi_+$, its Gram matrix $\frac12\mathrm{I}_2$ and the $*$-representation, of which §*The Matrix Representations from the Right Ideals* gives the index set.
- *Ideals and Quotients of a Sesqualgebra* — the ideals of a general sesqualgebra.
- *Definitions for the Study of the 12 Algebraic Structures* — the idempotent, the projection and the Peirce decomposition.
