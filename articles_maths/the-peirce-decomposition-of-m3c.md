# __The Peirce Decomposition of $M_3(\mathbb{C})$__

## Introduction

A complete family of three orthogonal idempotents cuts the algebra $M_{3}(\mathbb{C})$ into nine lines, one for each ordered pair of members. Each line is the set of elements that the two idempotents select on the left and on the right, the product of two lines is either zero or a third line, and the whole multiplication of the algebra is the table of those lines. This is the **Peirce decomposition** of the algebra relative to the family.

The family is the one supplied by a root $H$ with $H^{3}=I$ and simple spectrum: the three Lagrange projectors $P_{1},P_{2},P_{3}$ of *Roots of Unity and the Lagrange Idempotents*. The decomposition is therefore root-first, like the frame itself. It uses the product and the idempotents alone.

The Peirce decomposition is a **direct-sum decomposition of the algebra**. Its summands are subspaces of $M_{3}(\mathbb{C})$; their elements are matrices. They are not a list of spinors, and no Peirce line is a spinor. The module that carries the spin chain is the minimal left ideal $M_{3}P_{k}$, a three-dimensional space, treated in *The Modules and the Minimal Left Ideals*; for $n=3$ that module carries spin one, and only the case $n=2$ is spinorial. The distinction is stated once here and used throughout the category.

The article assumes the algebra and its matrix units of *The Matrix Algebra $M_{3}(\mathbb{C})$*, and the idempotents of *Roots of Unity and the Lagrange Idempotents*. The coarse split by a single idempotent is §*The Coarse Split by a Rank-One Idempotent*; the corner $QM_{3}Q\cong M_{2}(\mathbb{C})$ is *The $M_{2}$ Corner of $M_{3}(\mathbb{C})$*; the two-parameter gauge of the off-diagonal lines is *The Frame, the Simple Nilpotents and the Gauge* and *The Two-Parameter Gauge*.

## The Peirce Lines

**Definition.** Let $P_{1},P_{2},P_{3}$ be a complete orthogonal family of idempotents of $M_{3}(\mathbb{C})$. For $k,l\in\{1,2,3\}$ the **Peirce line** $A_{kl}$ is

$$
A_{kl}=P_{k}M_{3}(\mathbb{C})P_{l}=\{P_{k}AP_{l}:A\in M_{3}(\mathbb{C})\}.
$$

The **Peirce decomposition** of the algebra relative to the family is the sum of the nine lines.

**Proposition.** The nine Peirce lines are one-dimensional complex subspaces, and

$$
M_{3}(\mathbb{C})=\bigoplus_{k,l=1}^{3}A_{kl}.
$$

**Proof.** Conjugate the family to the standard one. The three idempotents of a complete orthogonal family are of rank one and sum to $I$; choosing a basis $v_{1},v_{2},v_{3}$ with $P_{k}v_{l}=\delta_{kl}v_{l}$ identifies $P_{k}$ with $E_{kk}$, and then

$$
P_{k}AP_{l}=E_{kk}AE_{ll}=a_{kl}E_{kl},
$$

so $A_{kl}=\mathbb{C}E_{kl}$ and has dimension one. The conjugation by the change of basis carries the lines of the standard frame to the lines of the given frame and preserves dimensions.

For the directness, write the identity $I=\sum_{k}P_{k}$ and expand

$$
A=\Bigl(\sum_{k}P_{k}\Bigr)A\Bigl(\sum_{l}P_{l}\Bigr)=\sum_{k,l}P_{k}AP_{l},
$$

so the lines span. If $\sum_{k,l}A_{kl}=0$ with $A_{kl}\in A_{kl}$, multiply on the left by $P_{r}$ and on the right by $P_{s}$: every term with $k\neq r$ or $l\neq s$ vanishes, and the surviving term is $A_{rs}=0$. So the sum is direct.

**The two readings of a Peirce line.** The line $A_{kl}$ is at once the set of elements with left idempotent $P_{k}$ and right idempotent $P_{l}$:

$$
A\in A_{kl}\iff P_{k}A=A\text{ and }AP_{l}=A .
$$

Indeed $P_{k}(P_{k}AP_{l})=P_{k}AP_{l}$ and $(P_{k}AP_{l})P_{l}=P_{k}AP_{l}$; conversely $P_{k}A=A$ and $AP_{l}=A$ give $A=P_{k}AP_{l}$. The line is the simultaneous eigenspace of the two multiplication operators $L_{P_{k}}$ and $R_{P_{l}}$ with eigenvalue $1$, and the kernel of the other four combinations.

**The diagonal lines are the idempotents.** $A_{kk}=P_{k}M_{3}P_{k}=\mathbb{C}P_{k}$, because $P_{k}$ has rank one: for $A\in M_{3}$, $P_{k}AP_{k}$ is an endomorphism with image inside the line $\operatorname{im}P_{k}$ and kernel containing $\ker P_{k}$, hence a scalar multiple of $P_{k}$. The scalar is $\operatorname{tr}(P_{k}AP_{k})=\operatorname{tr}(P_{k}A)$.

**The diagonal corners are fields.** Each $A_{kk}$ is a one-dimensional algebra with unit $P_{k}$, hence isomorphic to $\mathbb{C}$; the isomorphism is $P_{k}AP_{k}\mapsto\operatorname{tr}(P_{k}A)$. The three diagonal lines together form the commutative subalgebra

$$
D=A_{11}\oplus A_{22}\oplus A_{33}=\mathbb{C}P_{1}\oplus\mathbb{C}P_{2}\oplus\mathbb{C}P_{3}\cong\mathbb{C}^{3},
$$

which is the algebra of diagonal matrices in the eigenbasis. Its unit is $I$.

**The standard frame.** For the standard root $H_{0}=\operatorname{diag}(1,\omega,\omega^{2})$ the Peirce lines are the coordinate lines

$$
A_{kl}=\mathbb{C}E_{kl},
$$

and the Peirce decomposition is the decomposition of a matrix into its nine entries:

$$
A=\sum_{k,l=1}^{3}a_{kl}E_{kl}
=\begin{pmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{pmatrix}.
$$

The numbers $a_{kl}$ are the **Peirce coordinates** of $A$ in the standard frame. In a general frame they are the coefficients in a normalized system of matrix units adapted to the $P_{k}$, as in §*The Peirce Coordinates* below.

## The Multiplication Rule

**Theorem (the Peirce multiplication).** For all $k,l,m,n\in\{1,2,3\}$,

$$
\boxed{\;A_{kl}A_{mn}\subseteq\delta_{lm}A_{kn}.\;}
$$

**Proof.** An element of $A_{kl}$ is $P_{k}AP_{l}$ and an element of $A_{mn}$ is $P_{m}BP_{n}$. Their product is

$$
P_{k}AP_{l}P_{m}BP_{n}=P_{k}A\,\delta_{lm}P_{l}\,BP_{n}=\delta_{lm}P_{k}(AP_{l}B)P_{n}\in\delta_{lm}A_{kn},
$$

because $P_{l}P_{m}=\delta_{lm}P_{l}$ and $P_{k}(AP_{l}B)P_{n}$ is of the required form.

**The rule read three ways.**

- **Off-diagonal lines are square-zero.** For $k\neq l$, $A_{kl}^{2}\subseteq A_{kl}A_{kl}\subseteq\delta_{lk}A_{kk}=0$. Every element of an off-diagonal line is nilpotent of index two, and the line is a square-zero subalgebra without a unit. It is a subspace of the algebra, not an algebra with a multiplication worth the name.
- **The diagonal lines multiply by scalars.** $A_{kk}A_{kk}\subseteq A_{kk}$, and the product of two elements of the line is the product of their scalars, because $P_{k}^{2}=P_{k}$.
- **The off-diagonal lines are bimodules.** $A_{kl}A_{ll}\subseteq A_{kl}$ and $A_{kk}A_{kl}\subseteq A_{kl}$; the line $A_{kl}$ is a left module over the field $A_{kk}$ and a right module over the field $A_{ll}$, and the two actions agree with the scalars of $\mathbb{C}$ because both fields are copies of $\mathbb{C}$.

**The pairing of opposite lines.** For $k\neq l$ the product map

$$
A_{kl}\times A_{lk}\longrightarrow A_{kk},\qquad (x,y)\longmapsto xy,
$$

is nonzero and therefore, the lines being one-dimensional, a perfect pairing: for every nonzero $x\in A_{kl}$ there is $y\in A_{lk}$ with $xy=P_{k}$. In the standard frame $x=\alpha E_{kl}$ and $y=\beta E_{lk}$ give $xy=\alpha\beta E_{kk}=\alpha\beta P_{k}$, which is nonzero as soon as $\alpha\beta\neq0$. The same computation gives $yx=\alpha\beta P_{l}$, so the two products are the two diagonal idempotents, each with the same scalar.

**Corollary (the multiplication is the matrix-unit rule).** After the choice of a nonzero $E_{kl}\in A_{kl}$ for each pair, normalized by $E_{kl}E_{lk}=P_{k}$, the nine elements satisfy

$$
E_{ij}E_{kl}=\delta_{jk}E_{il},\qquad E_{kk}=P_{k},\qquad \sum_{k}E_{kk}=I,
$$

which is the table of the matrix units of *Matrix Algebras*. The normalization is possible by the perfect pairing, and it is unique up to the gauge of *The Frame, the Simple Nilpotents and the Gauge*.

## The Peirce Table

**The table of the nine lines.** The spaces, their bases in the standard frame, their left and right idempotents, and their dimensions are collected below.

| Space | Standard basis | Left idempotent | Right idempotent | $\dim_{\mathbb{C}}$ |
|---|---|---|---|---|
| $A_{11}$ | $E_{11}$ | $P_{1}$ | $P_{1}$ | $1$ |
| $A_{12}$ | $E_{12}$ | $P_{1}$ | $P_{2}$ | $1$ |
| $A_{13}$ | $E_{13}$ | $P_{1}$ | $P_{3}$ | $1$ |
| $A_{21}$ | $E_{21}$ | $P_{2}$ | $P_{1}$ | $1$ |
| $A_{22}$ | $E_{22}$ | $P_{2}$ | $P_{2}$ | $1$ |
| $A_{23}$ | $E_{23}$ | $P_{2}$ | $P_{3}$ | $1$ |
| $A_{31}$ | $E_{31}$ | $P_{3}$ | $P_{1}$ | $1$ |
| $A_{32}$ | $E_{32}$ | $P_{3}$ | $P_{2}$ | $1$ |
| $A_{33}$ | $E_{33}$ | $P_{3}$ | $P_{3}$ | $1$ |

**The multiplication table.** The entry in row $A_{kl}$ and column $A_{mn}$ is the space containing the products; it is $A_{kn}$ when $l=m$ and $0$ otherwise.

| $\cdot$ | $A_{m1}$ | $A_{m2}$ | $A_{m3}$ |
|---|---|---|---|
| $A_{1l}$ | $\delta_{lm}A_{11}$ | $\delta_{lm}A_{12}$ | $\delta_{lm}A_{13}$ |
| $A_{2l}$ | $\delta_{lm}A_{21}$ | $\delta_{lm}A_{22}$ | $\delta_{lm}A_{23}$ |
| $A_{3l}$ | $\delta_{lm}A_{31}$ | $\delta_{lm}A_{32}$ | $\delta_{lm}A_{33}$ |

The table is the matrix-unit table read in blocks: a product survives exactly when the right index of the first factor equals the left index of the second, and it lands in the line carrying the two outer indices. The nine entries that survive are the nine lines; the other seventy-two products vanish.

**The grading by the index difference.** The line $A_{kl}$ has degree $k-l$ in the $\mathbb{Z}/3$ grading of *Roots of Unity and the Lagrange Idempotents*. The three diagonal lines have degree $0$, the three lines $A_{21},A_{32},A_{13}$ have degree $1$, and the three lines $A_{12},A_{23},A_{31}$ have degree $2$. The multiplication rule refines the graded rule $M^{(r)}M^{(s)}\subseteq M^{(r+s)}$: it keeps the individual lines, not only their degree classes.

## The Peirce Coordinates

**A normalized frame gives coordinates.** Choose $E_{kl}\in A_{kl}$ with $E_{kl}E_{lk}=P_{k}$ and $E_{kl}E_{lm}=E_{km}$ for all indices; such a system exists by §*The Multiplication Rule*, and it is the matrix-unit system of the frame. Every element is then

$$
A=\sum_{k,l=1}^{3}\alpha_{kl}E_{kl},
\qquad \alpha_{kl}\in\mathbb{C},
$$

and the nine numbers $\alpha_{kl}$ are the **Peirce coordinates** of $A$ in that frame. In the standard frame they are the matrix entries $a_{kl}$ of §*The Peirce Lines*.

**The coordinate rule.** The product is

$$
AB=\sum_{k,l}\Bigl(\sum_{m}\alpha_{km}\beta_{ml}\Bigr)E_{kl},
$$

which is the matrix product in the coordinates. The trace and the determinant are the trace and the determinant of the $3\times3$ array,

$$
\operatorname{tr}A=\sum_{k}\alpha_{kk},\qquad
\det A=\sum_{\sigma\in S_{3}}\operatorname{sgn}(\sigma)\prod_{k}\alpha_{k,\sigma(k)} .
$$

The diagonal coordinates $\alpha_{kk}$ are the values of the three idempotents: $P_{k}AP_{k}=\alpha_{kk}P_{k}$.

**The coordinates are not unique.** A change of the normalized frame $E_{kl}\mapsto(t_{k}/t_{l})E_{kl}$ with $t_{k}\in\mathbb{C}^{\times}$ preserves the matrix-unit table and the idempotents, and it changes the coordinates by

$$
\alpha_{kl}\longmapsto \frac{t_{l}}{t_{k}}\alpha_{kl}.
$$

The diagonal coordinates are invariant, and the off-diagonal ones are rescaled by the gauge. The two independent ratios $t_{1}/t_{2}$ and $t_{2}/t_{3}$ are the two parameters of *The Two-Parameter Gauge*; the third ratio is their product. This is the only freedom in the Peirce coordinates, and it is the subject of §*The Gauge* of the next article.

**The characteristic polynomial in the coordinates.** The characteristic polynomial of $A$ is

$$
\chi_{A}(\lambda)=\lambda^{3}-t\lambda^{2}+s\lambda-d,
\qquad
t=\operatorname{tr}A,\quad
s=\tfrac12\bigl(t^{2}-\operatorname{tr}A^{2}\bigr),\quad
d=\det A,
$$

and its coefficients are polynomial in the nine Peirce coordinates. The spectral theory of the cubic is *The Cubic, the Discriminant and the Spectral Strata*; the trace and determinant are invariant under the gauge, because the diagonal coordinates are invariant and the off-diagonal rescaling cancels in the determinant.

## The Coarse Split by a Rank-One Idempotent

**A single rank-one idempotent already cuts the algebra into four corners, but the corners are no longer lines.**

Let $P$ be a rank-one idempotent, not necessarily one of the $P_{k}$, and put $Q=I-P$. Define the four **coarse Peirce corners**

$$
B_{11}=PMP,\qquad B_{12}=PMQ,\qquad B_{21}=QMP,\qquad B_{22}=QMQ.
$$

**Proposition.** The corners have dimensions

$$
\dim B_{11}=1,\qquad \dim B_{12}=2,\qquad \dim B_{21}=2,\qquad \dim B_{22}=4,
$$

and they sum directly to the algebra.

**Proof.** Choose a basis of $\mathbb{C}^{3}$ whose first vector spans $\operatorname{im}P$ and whose other two span $\ker P$; such a basis exists because $P^{2}=P$ gives $\mathbb{C}^{3}=\operatorname{im}P\oplus\ker P$ for a rank-one idempotent. In this basis

$$
P=\begin{pmatrix}1&0&0\\0&0&0\\0&0&0\end{pmatrix},\qquad
Q=\begin{pmatrix}0&0&0\\0&1&0\\0&0&1\end{pmatrix}.
$$

A matrix $A$ written in the same basis as

$$
A=\begin{pmatrix}a&b^{\mathsf T}\\c&D\end{pmatrix},
\qquad a\in\mathbb{C},\quad b,c\in\mathbb{C}^{2},\quad D\in M_{2}(\mathbb{C}),
$$

has its four blocks exactly in the four corners: $PAP=\begin{pmatrix}a&0\\0&0\end{pmatrix}=aP$, $PAQ=\begin{pmatrix}0&b^{\mathsf T}\\0&0\end{pmatrix}$, $QAP=\begin{pmatrix}0&0\\c&0\end{pmatrix}$, $QAQ=\begin{pmatrix}0&0\\0&D\end{pmatrix}$. The dimensions are $1,2,2,4$, and the block decomposition is direct.

**The block multiplication.** In the block form,

$$
\begin{pmatrix}a&b^{\mathsf T}\\c&D\end{pmatrix}
\begin{pmatrix}a'&b'^{\mathsf T}\\c'&D'\end{pmatrix}
=
\begin{pmatrix}aa'+b^{\mathsf T}c'&ab'^{\mathsf T}+b^{\mathsf T}D'\\ca'+Dc'&cb'^{\mathsf T}+DD'\end{pmatrix},
$$

which is the ordinary product of block matrices. The corner $B_{11}$ is the field $\mathbb{C}$, with unit $P$; the corner $B_{22}$ is $M_{2}(\mathbb{C})$, with unit $Q$; the off-diagonal corners $B_{12}$ and $B_{21}$ are the column and the row of dimension two, carrying a left action of $\mathbb{C}$ and a right action of $M_{2}(\mathbb{C})$, and the reverse.

**The corner isomorphisms.** The map

$$
B_{11}\longrightarrow\mathbb{C},\qquad PAP\longmapsto \operatorname{tr}(PA),
$$

is an isomorphism of algebras with unit $P\mapsto1$. The map

$$
B_{22}\longrightarrow M_{2}(\mathbb{C}),\qquad QAQ\longmapsto \text{the matrix of }QAQ\text{ on }\operatorname{im}Q,
$$

is an isomorphism of algebras with unit $Q\mapsto I_{2}$. The two isomorphisms are the readings of the diagonal corners as the field and as the $2\times2$ matrix algebra; the second is the $M_{2}$ corner of *The $M_{2}$ Corner of $M_{3}(\mathbb{C})$*.

**The coarse Peirce table.** The products of the four corners are

| $\cdot$ | $B_{11}$ | $B_{12}$ | $B_{21}$ | $B_{22}$ |
|---|---|---|---|---|
| $B_{11}$ | $B_{11}$ | $B_{12}$ | $0$ | $0$ |
| $B_{12}$ | $0$ | $0$ | $B_{11}$ | $B_{12}$ |
| $B_{21}$ | $B_{21}$ | $B_{22}$ | $0$ | $0$ |
| $B_{22}$ | $0$ | $0$ | $B_{21}$ | $B_{22}$ |

The table is the rule $B_{ij}B_{kl}\subseteq\delta_{jk}B_{il}$ read on the four blocks, and it records the dimensions only implicitly: the entries are subspaces, not numbers. The four diagonal entries of the table are the four corners themselves because $P^{2}=P$ and $Q^{2}=Q$; the vanishing entries are the square-zero products $B_{12}^{2}=0$ and $B_{21}^{2}=0$, and the products $B_{12}B_{21}\subseteq B_{11}$, $B_{21}B_{12}\subseteq B_{22}$.

**Worked example.** Take the standard frame with $P=E_{11}$ and

$$
A=\begin{pmatrix}1&2&3\\4&5&6\\7&8&9\end{pmatrix}.
$$

Then

$$
PAP=\begin{pmatrix}1&0&0\\0&0&0\\0&0&0\end{pmatrix}=1\cdot P,\qquad
PAQ=\begin{pmatrix}0&2&3\\0&0&0\\0&0&0\end{pmatrix},
$$

$$
QAP=\begin{pmatrix}0&0&0\\4&0&0\\7&0&0\end{pmatrix},\qquad
QAQ=\begin{pmatrix}0&0&0\\0&5&6\\0&8&9\end{pmatrix}.
$$

The four blocks have dimensions $1,2,2,4$, and the trace of $A$ is $1+5+9=15$, which is the sum of the traces of the two diagonal blocks, $1+(5+9)$.

**The coarse split is not a direct sum of algebras.** The algebra $M_{3}(\mathbb{C})$ is simple; if it were the direct sum of the two algebras $B_{11}$ and $B_{22}$, the off-diagonal corners $B_{12}$ and $B_{21}$ would vanish, because a direct sum of algebras has no cross terms. They do not vanish: $PAQ\neq0$ for a general $A$. The Peirce decomposition is a direct sum of **vector spaces**, and the diagonal part $B_{11}\oplus B_{22}$ is a subalgebra, but the off-diagonal corners are nonzero bimodules and the whole is not a product of algebras. This is the structural difference between the coarse split and the split of the biquaternion algebra into four lines.

**The coarse split refines to the fine split.** The rank-one idempotent $P$ is one of the three $P_{k}$ only in the standard frame; in general it is a fourth line. The coarse corner $B_{22}=QMQ$ has dimension four and is isomorphic to $M_{2}(\mathbb{C})$; inside it the two idempotents $P_{2}$ and $P_{3}$ of the root cut it into the four lines $A_{22},A_{23},A_{32},A_{33}$. The coarse split is therefore the first step of a two-step refinement: one idempotent gives $1+2+2+4$, and the full family of three gives $1+1+1+1+1+1+1+1+1$. The intermediate corner $M_{2}$ is the biquaternion algebra embedded in $M_{3}$.

## The Comparison with the Biquaternion Four Lines

**In $M_{2}(\mathbb{C})$ the coarse and the fine decompositions coincide, because every idempotent is of rank one or zero.**

For $n=2$ the complete family is a pair $P_{+},P_{-}$ of rank-one idempotents, and the four corners are

$$
B_{++}=\mathbb{C}P_{+},\qquad B_{+-}=\mathbb{C}E_{12},\qquad B_{-+}=\mathbb{C}E_{21},\qquad B_{--}=\mathbb{C}P_{-},
$$

each of dimension one. The multiplication table is the $2\times2$ matrix-unit table, and the algebra is the direct sum of the four lines as a vector space. The coarse split by one idempotent is already the fine split, and the corner $QM_{2}Q$ is one-dimensional. This is the content of *The Peirce Decomposition* of the biquaternion category.

For $n=3$ the fine split has nine lines, and the coarse split by one rank-one idempotent has a four-dimensional corner. The corner $QM_{3}Q$ is $M_{2}(\mathbb{C})$, which is the biquaternion algebra; the coarse split of $M_{3}$ therefore contains the whole $M_{2}$ Peirce decomposition of the biquaternion algebra as its lower-right block. The passage from $n=2$ to $n=3$ is the passage from four lines to nine, mediated by the $M_{2}$ corner.

**The carrier is not a Peirce line.** The minimal left ideal $M_{3}P_{k}$ is the set of matrices whose columns are combinations of the $k$-th column; it is a three-dimensional complex vector space, isomorphic to $\mathbb{C}^{3}$. It is not a Peirce line, which is one-dimensional and lies inside the algebra. The left ideal is the carrier of the defining representation, and under the principal $\mathfrak{su}_{2}$ of *The Spin Chain and the Adjoint Decomposition* it is the spin-one module $\operatorname{Sym}^{2}(\mathbb{C}^{2})$. The Peirce lines are the lines of the algebra; the carrier is a module over it. For $n=2$ the minimal left ideal is two-dimensional and is the spinorial module of the biquaternion algebra; for $n=3$ the carrier is spin one, and there are no spinors.

## Summary

A complete orthogonal family $P_{1},P_{2},P_{3}$ of three rank-one idempotents of $M_{3}(\mathbb{C})$ gives the Peirce decomposition

$$
\boxed{\;M_{3}(\mathbb{C})=\bigoplus_{k,l=1}^{3}A_{kl},\qquad A_{kl}=P_{k}M_{3}(\mathbb{C})P_{l},\qquad \dim_{\mathbb{C}}A_{kl}=1,\;}
$$

with the multiplication rule

$$
A_{kl}A_{mn}\subseteq\delta_{lm}A_{kn}.
$$

The diagonal lines are the idempotents and form a copy of $\mathbb{C}^{3}$; the off-diagonal lines are square-zero and are paired by the products $A_{kl}A_{lk}\subseteq A_{kk}$.

A single rank-one idempotent $P$ gives the coarse split with corners

$$
PMP\oplus PMQ\oplus QMP\oplus QMQ
$$

of dimensions $1+2+2+4$, with $PMP\cong\mathbb{C}$ and $QMQ\cong M_{2}(\mathbb{C})$. The coarse split is a direct sum of vector spaces, not of algebras; the off-diagonal blocks are nonzero bimodules and the algebra is simple.

| Quantity | Value for $M_{3}(\mathbb{C})$ |
|---|---|
| Peirce lines of a complete family | $9$ |
| Dimension of each line | $1$ |
| Coarse corners of a rank-one idempotent | $1+2+2+4$ |
| Coarse corners of a rank-two idempotent | $4+2+2+1$ |
| Diagonal corner | $\mathbb{C}$ |
| Complement corner | $M_{2}(\mathbb{C})$ |

The Peirce spaces are subspaces of the algebra, not spinors. The carrier of the spin chain is the minimal left ideal $M_{3}P_{k}\cong\mathbb{C}^{3}$, of spin one; only the biquaternion case $n=2$ has a spinorial carrier.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P_{1},P_{2},P_{3}$ | the complete family of Lagrange idempotents of a root $H$ |
| $A_{kl}=P_{k}M_{3}P_{l}$ | the Peirce line of the pair $(k,l)$ |
| $E_{kl}$ | a normalized matrix unit in $A_{kl}$, $E_{kl}E_{lm}=E_{km}$ |
| $\alpha_{kl}$ | the Peirce coordinates of $A$ in a normalized frame |
| $P,Q=I-P$ | a rank-one idempotent and its complement |
| $B_{11},B_{12},B_{21},B_{22}$ | the coarse Peirce corners |
| $D$ | the diagonal subalgebra $A_{11}\oplus A_{22}\oplus A_{33}\cong\mathbb{C}^{3}$ |
| $M_{3}P_{k}$ | the minimal left ideal, the carrier $\cong\mathbb{C}^{3}$ |

## Further Reading

- [Roots of Unity and the Lagrange Idempotents](roots-of-unity-and-the-lagrange-idempotents-of-m3c.html), for the root $H$ and the three idempotents.
- [The Matrix Algebra $M_{3}(\mathbb{C})$](the-matrix-algebra-m3c.html), for the matrix units, the product and the simplicity.
- [The $M_{2}$ Corner of $M_{3}(\mathbb{C})$](the-m2-corner-of-m3c.html), for the corner $QM_{3}Q$ as a unital algebra and as a $*$-algebra.
- [The Rank-Two Split](the-rank-two-split-of-m3c.html), for the complementary coarse split $4+2+2+1$.
- [The Frame, the Simple Nilpotents and the Gauge](the-frame-the-simple-nilpotents-and-the-gauge-of-m3c.html), for the normalized matrix units and the gauge.
- [The Modules and the Minimal Left Ideals](the-modules-and-the-minimal-left-ideals-of-m3c.html), for the carrier $M_{3}P_{k}\cong\mathbb{C}^{3}$.
- [The Peirce Decomposition](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the order-two case and the four biquaternion lines.
- [Matrix Algebras](matrix-algebras.html), for the matrix-unit table and the simplicity of $M_{n}$.
