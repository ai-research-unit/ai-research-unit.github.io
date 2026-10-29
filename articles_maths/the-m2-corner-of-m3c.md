# __The $M_2$ Corner of $M_3(\mathbb{C})$__

## Introduction

Let $P$ be a rank-two idempotent of $M_{3}(\mathbb{C})$ and $Q=I-P$ its complement. The **compression** of the algebra to $P$ is the set

$$
P M_{3}(\mathbb{C})P=\{PAP:A\in M_{3}(\mathbb{C})\}.
$$

It is closed under multiplication, its unit is $P$, and it is isomorphic to $M_{2}(\mathbb{C})$. The isomorphism is not an equality: the corner lives inside $M_{3}$ with the unit $P$ rather than $I$, its trace is the ambient trace restricted to it, and its determinant is the determinant of the compressed endomorphism, not the restriction of $\det A$. The corner is a unital $*$-algebra exactly when $P$ is Hermitian; for a non-Hermitian idempotent the ambient star carries the corner to a different corner.

This article states the compression, the isomorphism $P M_{3}P\cong M_{2}(\mathbb{C})$, the inherited trace and determinant, the $*$-condition, the embedding $M_{2}\to M_{3}$, the one-dimensional complement, and the failure of the involution for a non-Hermitian idempotent. The rank-two split of the whole algebra, with corners $4+2+2+1$, is *The Rank-Two Split of $M_3(\mathbb{C})$*. The Peirce decomposition by three idempotents is *The Peirce Decomposition of $M_{3}(\mathbb{C})$*.

## The Compression

**Definition.** Let $P\in M_{3}(\mathbb{C})$ satisfy $P^{2}=P$ and $\operatorname{rank}P=2$, and put $Q=I-P$. The **compression** of $M_{3}$ to $P$ is

$$
B=P M_{3}P=\{PAP:A\in M_{3}(\mathbb{C})\}.
$$

**Proposition.** $B$ is a subalgebra of $M_{3}(\mathbb{C})$ with unit $P$. It is closed under the product, $P$ is its two-sided identity, and $B$ has complex dimension $4$.

**Proof.** For $X=PAP$ and $Y=PBP$, the product is $XY=PAP\,PBP=P(APB)P\in B$, because $P^{2}=P$. The element $P=PIP$ lies in $B$, and $PX=P(PAP)=PAP=X$ and $XP=(PAP)P=X$, so $P$ is the unit. For the dimension, choose a basis of $\mathbb{C}^{3}$ adapted to the decomposition $\mathbb{C}^{3}=\operatorname{im}P\oplus\ker P$, with the first two vectors in $\operatorname{im}P$ and the third in $\ker P$; in this basis $P=\operatorname{diag}(1,1,0)$, and $PAP$ is the matrix with the upper-left $2\times2$ block of $A$ and all other entries zero. The upper-left block is an arbitrary $2\times2$ matrix, so $B$ is four-dimensional.

**The corner is not an ideal.** $B$ is a subalgebra with its own unit, but it is not a two-sided ideal of $M_{3}$: $E_{13}\in M_{3}$ and $P E_{13}\notin B$ when $P$ has the standard form, for instance. The algebra $M_{3}$ is simple, so it has no nontrivial two-sided ideals at all. The corner is a subalgebra, not a quotient and not an ideal.

**The corner is a compression, not a restriction.** An element of $B$ is a matrix in $M_{3}$ that happens to lie in the corner. The map $A\mapsto PAP$ is not injective on $M_{3}$; its image is $B$, and the kernel is the set of matrices whose upper-left block vanishes, of dimension $5$. The compression keeps the part of $A$ that acts on $\operatorname{im}P$ and discards the rest.

## The Corner Is $M_2(\mathbb{C})$

**Theorem.** Let $P$ be a rank-two idempotent and $B=P M_{3}P$. The map

$$
\Phi:B\longrightarrow\operatorname{End}_{\mathbb{C}}(\operatorname{im}P),\qquad X\longmapsto X|_{\operatorname{im}P},
$$

is an isomorphism of $\mathbb{C}$-algebras with unit $P\mapsto\mathrm{id}_{\operatorname{im}P}$. Consequently

$$
B\cong M_{2}(\mathbb{C}).
$$

**Proof.** The map is well defined: for $X=PAP$ and $v\in\operatorname{im}P$, $Xv=PAPv\in\operatorname{im}P$, so $X$ preserves $\operatorname{im}P$. It is a homomorphism because the restriction of a product is the product of the restrictions. It is injective: if $X|_{\operatorname{im}P}=0$, then $XP=0$; but $X=XP$ for $X=PAP$, so $X=0$. It is surjective: given $T\in\operatorname{End}(\operatorname{im}P)$, extend $T$ to $V$ by $T(\ker P)=0$ and put $X=TP$; then $X=PXP\in B$ and $X|_{\operatorname{im}P}=T$. The unit $P$ restricts to the identity of $\operatorname{im}P$. The endomorphism algebra of a two-dimensional space is $M_{2}(\mathbb{C})$.

**A basis-free form.** If $P=u_{1}v_{1}^{\vee}+u_{2}v_{2}^{\vee}$ with $(u_{1},u_{2})$ a basis of $\operatorname{im}P$ and $(v_{1}^{\vee},v_{2}^{\vee})$ the dual functionals on $\operatorname{im}P$, then the matrix of $X\in B$ in the basis $(u_{1},u_{2})$ is the $2\times2$ array of the numbers $v_{i}^{\vee}(Xu_{j})$. The corner is the algebra of those arrays.

**The isomorphism is not canonical.** It depends on the choice of a basis of $\operatorname{im}P$; a change of basis conjugates the $2\times2$ matrices by the change-of-basis matrix. The corner $B$ itself is canonical, being defined by $P$; the identification with the standard $M_{2}(\mathbb{C})$ is canonical only up to conjugation.

**The standard case.** For $P_{1}=\operatorname{diag}(1,1,0)$ the corner is the set of matrices

$$
\begin{pmatrix}b_{11}&b_{12}&0\\b_{21}&b_{22}&0\\0&0&0\end{pmatrix},
$$

which is $M_{2}(\mathbb{C})$ in the upper-left block. The unit is $P_{1}=\operatorname{diag}(1,1,0)$, not $I$.

## The Inherited Trace and Determinant

**The trace.** The **inherited trace** of the corner is the restriction of the ambient trace:

$$
\operatorname{tr}_{P}(X)=\operatorname{tr}(X),\qquad X\in B.
$$

It is a linear functional on $B$, and it is the trace of the $2\times2$ matrix of $X$ in any basis of $\operatorname{im}P$.

**Proposition.** For $X=PAP\in B$,

$$
\operatorname{tr}_{P}(X)=\operatorname{tr}(PAP)=\operatorname{tr}(PA)=\operatorname{tr}(AP),
$$

and this number is the trace of the compressed endomorphism $X|_{\operatorname{im}P}$.

**Proof.** The trace is cyclic, so $\operatorname{tr}(PAP)=\operatorname{tr}(APP)=\operatorname{tr}(AP)$; the same argument gives $\operatorname{tr}(PA)$. The compressed endomorphism acts on $\operatorname{im}P$ and annihilates $\ker P$ (because $X=XP$ and $P$ annihilates $\ker P$), so the ambient trace, which is the sum over a basis adapted to $\operatorname{im}P\oplus\ker P$, is the trace on $\operatorname{im}P$ plus the zero trace on $\ker P$.

**The determinant.** The **determinant of the compression** is the determinant of the endomorphism $X|_{\operatorname{im}P}$:

$$
\det_{P}(X)=\det\bigl(X|_{\operatorname{im}P}\bigr).
$$

It is multiplicative on $B$, because the restriction map is an algebra isomorphism and the determinant is multiplicative on $M_{2}(\mathbb{C})$. It is **not** the restriction of the ambient determinant: the ambient determinant of $X$ is zero, since $X$ has the one-dimensional kernel $\ker P$ in its kernel, whereas the compression can be invertible.

**Worked example (the two determinants differ).** Let

$$
A=\begin{pmatrix}1&2&3\\4&5&6\\7&8&9\end{pmatrix},
\qquad \det A=0,
$$

and $P_{1}=\operatorname{diag}(1,1,0)$. Then

$$
P_{1}AP_{1}=\begin{pmatrix}1&2&0\\4&5&0\\0&0&0\end{pmatrix},
\qquad
\det_{P_{1}}(P_{1}AP_{1})=\det\begin{pmatrix}1&2\\4&5\end{pmatrix}=5-8=-3\neq0=\det A.
$$

The compression is invertible in the corner, with inverse the compressed inverse of the $2\times2$ block, even though $A$ is singular in $M_{3}$. The two determinants answer different questions: $\det A$ asks whether $A$ is invertible on $\mathbb{C}^{3}$, and $\det_{P}$ asks whether $A$ is invertible on $\operatorname{im}P$ modulo $\ker P$.

**The trace of the worked example.** $\operatorname{tr}(A)=1+5+9=15$, while $\operatorname{tr}_{P_{1}}(P_{1}AP_{1})=1+5=6$. The inherited trace forgets the third diagonal entry, which lies in the kernel direction; it is the trace of the compressed endomorphism, not the trace of $A$.

**The characteristic polynomial of the compression.** The two eigenvalues of the $2\times2$ block are the eigenvalues of $X|_{\operatorname{im}P}$; they are not eigenvalues of $A$ in general, because $\operatorname{im}P$ need not be invariant. The corner's characteristic polynomial is

$$
\lambda^{2}-\operatorname{tr}_{P}(X)\lambda+\det_{P}(X),
$$

and it is not a factor of the ambient characteristic polynomial unless the compression is block triangular. For the example, $\lambda^{2}-6\lambda-3$, with roots $3\pm2\sqrt3$, while the ambient eigenvalues are $0$ and $(15\pm3\sqrt{33})/2$.

## The Unital Algebra and the Star

**The corner is always a unital algebra, but it is a unital $*$-algebra only when $P$ is Hermitian.**

Let $A^{*}=\bar A^{\mathsf T}$ be the conjugate transpose, as in *The Involution and the Hermitian Structure of $M_3(\mathbb{C})$*. A **unital $*$-algebra** is an algebra with a unit and an involution that fixes the unit.

**Theorem.** Let $P$ be a rank-two idempotent and $B=P M_{3}P$.

1. If $P=P^{*}$, then $B$ is a unital $*$-algebra with unit $P$ and involution the restriction of the star.
2. If $P\neq P^{*}$, then $B$ is not closed under the star: for some $X\in B$, $X^{*}\notin B$.

**Proof.** (1) Let $P=P^{*}$. For $X=PAP\in B$, $X^{*}=P^{*}A^{*}P^{*}=PA^{*}P\in B$; the star is involutive, conjugate-linear and multiplicative on $B$, and it fixes $P$. So $B$ is a $*$-algebra.

(2) Suppose that $B$ is closed under the star. Since $P\in B$, $P^{*}\in B$, so $P^{*}=PBP$ for some $B$, and therefore $P^{*}P=P^{*}$ and $PP^{*}=P^{*}$. Then $E=P-P^{*}$ satisfies

$$
E^{2}=P^{2}-PP^{*}-P^{*}P+(P^{*})^{2}=P-P^{*}-P^{*}+P^{*}=P-P^{*}=E,
$$

so $E$ is an idempotent. Its trace is $\operatorname{tr}P-\operatorname{tr}P^{*}=2-2=0$, because $P$ has rank two and the trace of $P^{*}$ is the conjugate of the trace of $P$. An idempotent of trace zero has rank zero, hence is zero; so $P=P^{*}$, contrary to the hypothesis. Therefore $B$ is not closed under the star when $P\neq P^{*}$.

**The explicit failure.** Let

$$
P=\begin{pmatrix}1&0&-1\\0&1&0\\0&0&0\end{pmatrix}.
$$

Then $P^{2}=P$, $\operatorname{rank}P=2$, and

$$
P^{*}=\begin{pmatrix}1&0&0\\0&1&0\\-1&0&0\end{pmatrix}\neq P.
$$

The corner $B=P M_{3}P$ consists of the matrices with third row zero and third column equal to the negative of the first column, as in §*The Compression*. The matrix $P^{*}$ has third row $(-1,0,0)$, which is not zero, so $P^{*}\notin B$. Taking $X=P\in B$ gives $X^{*}=P^{*}\notin B$. The star does not preserve the corner.

**The Hermitian case in coordinates.** For $P_{1}=\operatorname{diag}(1,1,0)$, the corner is the upper-left block and the star is the conjugate transpose of the block; the corner is the unital $*$-algebra $M_{2}(\mathbb{C})$ with unit $P_{1}$. The unit is $P_{1}$, not $I$, and the involution fixes it.

**The involution of the biquaternion algebra.** The biquaternion algebra is $\mathbb{B}\cong M_{2}(\mathbb{C})$, and its star is the conjugate transpose in its matrix model. The corner $B$ with a Hermitian $P$ is a copy of that $*$-algebra inside $M_{3}$, with unit $P$. For a non-Hermitian $P$ the copy is only an algebra: the ambient star carries it to the corner of $P^{*}$, and the involution of $\mathbb{B}$ does not descend to the corner. This is the precise sense in which the involution fails to descend; it is not a failure of the algebra structure, which is always $M_{2}(\mathbb{C})$.

## The Complement and the Embedding

**The complement.** The idempotent $Q=I-P$ has rank one, and its corner is

$$
Q M_{3}Q=\mathbb{C}Q,
$$

a one-dimensional algebra with unit $Q$. The algebra splits as a vector space into the four coarse Peirce corners

$$
M_{3}=PMP\oplus PMQ\oplus QMP\oplus QMQ,
$$

of dimensions $4+2+2+1$. The corner $PMP$ is the $M_{2}$ corner; the corner $QMQ$ is the field $\mathbb{C}$; the mixed corners $PMQ$ and $QMP$ are two-dimensional and carry the bimodule structure of *The Rank-Two Split of $M_3(\mathbb{C})$*.

**The direct sum is not an algebra direct sum.** The complement $\mathbb{C}Q$ is a subalgebra, and $PMP$ is a subalgebra, but their sum is not the whole algebra and the cross terms $PMQ,QMP$ are nonzero. If $M_{3}$ were the direct sum of the two corner algebras, the mixed corners would vanish, contradicting the simplicity of $M_{3}$. The Peirce decomposition is a vector-space decomposition with a multiplication rule, not a product of algebras.

**The embedding.** Choose a basis of $\mathbb{C}^{3}$ adapted to $\mathbb{C}^{3}=\operatorname{im}P\oplus\ker P$. In this basis the map

$$
\iota:M_{2}(\mathbb{C})\longrightarrow M_{3}(\mathbb{C}),\qquad
B\longmapsto\begin{pmatrix}B&0\\0&0\end{pmatrix},
$$

is an injective algebra homomorphism with image $PMP$, and it is unital onto the corner: $\iota(I_{2})=P$. It is not unital into $M_{3}$, because $\iota(I_{2})=P\neq I$. The unit of the ambient algebra is not the unit of the corner.

**The complement as a quotient direction.** The projection $Q$ is the unit of the complement; the mixed corners are the off-diagonal blocks that connect the two units. The element $Q$ is the image of the identity under the other corner embedding $\mathbb{C}\to M_{3}$, $1\mapsto Q$. The two corner embeddings are the two diagonal blocks of the coarse Peirce decomposition.

**Worked example of the four blocks.** With $P=P_{1}=\operatorname{diag}(1,1,0)$ and $A$ as in §*The Inherited Trace and Determinant*,

$$
PAP=\begin{pmatrix}1&2&0\\4&5&0\\0&0&0\end{pmatrix},\qquad
PAQ=\begin{pmatrix}0&0&3\\0&0&6\\0&0&0\end{pmatrix},
$$

$$
QAP=\begin{pmatrix}0&0&0\\0&0&0\\7&8&0\end{pmatrix},\qquad
QAQ=\begin{pmatrix}0&0&0\\0&0&0\\0&0&9\end{pmatrix}=9Q.
$$

The four blocks have dimensions $4,2,2,1$; the corner $PMP$ is the $M_{2}$ corner, and the corner $QMQ$ is the line $\mathbb{C}Q$. The element $A$ is the sum of the four blocks.

## The Non-Hermitian Idempotent

**A non-Hermitian idempotent gives the same algebra with a different unit and a different star.**

Take

$$
P=\begin{pmatrix}1&0&-1\\0&1&0\\0&0&0\end{pmatrix},
\qquad
P^{2}=P,\qquad \operatorname{rank}P=2,\qquad P^{*}\neq P.
$$

Its image is $\operatorname{span}\{e_{1},e_{2}\}$ and its kernel is $\operatorname{span}\{e_{1}+e_{3}\}$, so $\mathbb{C}^{3}=\operatorname{im}P\oplus\ker P$. In the adapted basis $(e_{1},e_{2},e_{1}+e_{3})$ the idempotent is $\operatorname{diag}(1,1,0)$, and the corner is again a copy of $M_{2}(\mathbb{C})$.

**The compression of the example.** With $A$ as above,

$$
PAP=\begin{pmatrix}-6&-6&6\\4&5&-4\\0&0&0\end{pmatrix}.
$$

In the basis $(e_{1},e_{2})$ of $\operatorname{im}P$ the compressed matrix is

$$
\begin{pmatrix}-6&-6\\4&5\end{pmatrix},
\qquad
\det_{P}(PAP)=-30+24=-6,
\qquad
\operatorname{tr}_{P}(PAP)=-1.
$$

The ambient trace of $PAP$ is also $-1$, and the ambient determinant of $PAP$ is $0$ because the third row vanishes. The compressed determinant is $-6$, nonzero: the compression is invertible in the corner.

**The star does not preserve the corner.** The star of $P$ is

$$
P^{*}=\begin{pmatrix}1&0&0\\0&1&0\\-1&0&0\end{pmatrix},
$$

which has a nonzero third row and therefore does not lie in $PMP$. The corner of $P$ and the corner of $P^{*}$ are two different four-dimensional subspaces of $M_{3}$; the star exchanges them. The algebra structure is unchanged, but the $*$-structure is not defined on the corner of $P$.

**The Hermitian idempotent next to it.** The Hermitian idempotent with the same image is the orthogonal projection onto $\operatorname{span}\{e_{1},e_{2}\}$, namely $P_{1}=\operatorname{diag}(1,1,0)$. The corner of $P_{1}$ is the upper-left block; the corner of $P$ is a different subspace, but the two corners are isomorphic as algebras and the isomorphism is the change of basis from the adapted basis of $P$ to the standard one. The Hermitian corner is the one that carries the star.

## Summary

For a rank-two idempotent $P$ of $M_{3}(\mathbb{C})$, the compression

$$
\boxed{\;P M_{3}(\mathbb{C})P\cong M_{2}(\mathbb{C}),\qquad \text{unit }P,\qquad \dim_{\mathbb{C}}=4\;}
$$

is a unital algebra, with inherited trace $\operatorname{tr}_{P}(PAP)=\operatorname{tr}(PA)$ and determinant $\det_{P}(PAP)=\det(PAP|_{\operatorname{im}P})$. The determinant of the compression is not the restriction of the ambient determinant: the example $A$ of determinant $0$ has a compression of determinant $-3$ (or $-6$ for the non-Hermitian idempotent).

The corner is a unital $*$-algebra exactly when $P=P^{*}$. For a non-Hermitian idempotent the star carries $PMP$ to $P^{*}MP^{*}$, and the involution does not descend to the corner. The complement is $\mathbb{C}(I-P)$, of dimension one, and the four coarse corners have dimensions $4+2+2+1$.

| Quantity | Value for the rank-two corner |
|---|---|
| Algebra | $M_{2}(\mathbb{C})$ |
| Unit | $P$ |
| Complex dimension | $4$ |
| Inherited trace | $\operatorname{tr}(PAP)=\operatorname{tr}(PA)$ |
| Inherited determinant | $\det(PAP|_{\operatorname{im}P})$ |
| Unital $*$-algebra | iff $P=P^{*}$ |
| Complement | $\mathbb{C}(I-P)$, dimension $1$ |
| Coarse corners | $4+2+2+1$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P$ | a rank-two idempotent |
| $Q=I-P$ | the complementary rank-one idempotent |
| $PMP$ | the compression, the $M_{2}$ corner |
| $\operatorname{tr}_{P}$ | the inherited trace, the restriction of the ambient trace |
| $\det_{P}$ | the determinant of the compressed endomorphism |
| $P^{*}$ | the conjugate transpose of $P$ |
| $\iota:M_{2}\to M_{3}$ | the block embedding with image $PMP$ |

## Further Reading

- [The Peirce Decomposition of $M_3(\mathbb{C})$](the-peirce-decomposition-of-m3c.html), for the coarse split and the Peirce lines.
- [The Rank-Two Split of $M_3(\mathbb{C})$](the-rank-two-split-of-m3c.html), for the four corners $4+2+2+1$ and the mass block.
- [The Matrix Algebra $M_3(\mathbb{C})$](the-matrix-algebra-m3c.html), for the trace, the determinant and the unit group.
- [The Involution and the Hermitian Structure of $M_3(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m3c.html), for the star and the positive definite form.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the biquaternion algebra as $M_{2}(\mathbb{C})$.
- [Matrix Algebras](matrix-algebras.html), for the algebra $M_{2}(\mathbb{C})$ and its matrix units.
