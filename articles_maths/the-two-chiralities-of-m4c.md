# __The Two Chiralities of $M_4(\mathbb{C})$__

## Introduction

**The chirality involution $\Gamma=H^2$ splits the carrier $\mathbb{C}^4$ into two planes, and the algebra into two chiral blocks and two mass blocks of dimension four each.** The split is the $2+2$ split: each chirality is a two-dimensional space, and the mass block is the four-dimensional space of maps from one chirality to the other. The involution is the $\mathbb{Z}/2$ quotient of the $\mathbb{Z}/4$ grading of the root.

The article defines $\Gamma$, proves that it is an involution with the $2+2$ spectrum, identifies the two chiralities, states the block decomposition of the algebra, distinguishes the chirality split of the carrier from the even/odd split of the algebra, and explains why the chiralities are not minimal left ideals. It also compares the Peirce $\mathfrak{sl}_2$, which mixes the chiralities, with the chiral $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$, which preserves them.

The root is *Roots of Unity and the Lagrange Idempotents of $M_4(\mathbb{C})$*; the Peirce corners are *The Peirce Decomposition of $M_4(\mathbb{C})$*; the rank-two split is *The Rank-Two Split of $M_4(\mathbb{C})$*; the mass block and the polar decomposition are *The Mass Block and the Chiral Polar Decomposition of $M_4(\mathbb{C})$*; the two $\mathfrak{su}_2$'s are *The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$*.

## The Chirality Involution

**Definition.** The **chirality involution** of the root $H$ is

$$
\Gamma=H^2 .
$$

**Theorem.** The element $\Gamma$ is an involution:

$$
\Gamma^2=I.
$$

It has eigenvalues $+1$ on $V_1\oplus V_3$ and $-1$ on $V_2\oplus V_4$, where $V_k$ is the spectral line of $\zeta_k=i^{k-1}$. Its trace is $0$, and each eigenspace has dimension $2$. In the spectral projectors,

$$
\Gamma=P_1-P_2+P_3-P_4.
$$

**Proof.** $\Gamma^2=H^4=I$. On $V_k$, $\Gamma$ acts by $\zeta_k^2$, which is $+1$ for $k=1,3$ and $-1$ for $k=2,4$. The trace is $1-1+1-1=0$. Each eigenspace is the sum of two spectral lines, hence has dimension $2$. The displayed formula is the spectral resolution $H^2=\sum_k\zeta_k^2P_k$.

**The standard model.** For $H_0=\operatorname{diag}(1,i,-1,-i)$,

$$
\Gamma_0=H_0^2=\operatorname{diag}(1,-1,1,-1)=E_{11}-E_{22}+E_{33}-E_{44}.
$$

The matrix is diagonal with two $+1$'s and two $-1$'s. It is not the root: $\Gamma_0^2=I$, while $H_0^4=I$ and $H_0^2=\Gamma_0\ne I$.

**The chirality is an involution, not a grading by the root.** The root $H$ has order four; $\Gamma$ has order two. The map $H\mapsto\Gamma$ is not injective. It forgets the decomposition of each chiral plane into its two spectral lines: on the $+1$ eigenspace of $\Gamma$ the root restricts with eigenvalues $+1,-1$, and on the $-1$ eigenspace with $i,-i$. The fibre is the product of the two spaces of ordered decompositions, each an open subset of $\mathbb{P}^1\times\mathbb{P}^1$, of complex dimension four (real dimension eight); it is not a finite set. The image has dimension $8$, so the root set has dimension $12$.

## The Two Chiralities

**Definition.** The **chirality projectors** are

$$
P_+=\frac12(I+\Gamma)=P_1+P_3,\qquad
P_-=\frac12(I-\Gamma)=P_2+P_4 .
$$

The **two chiralities** are the images

$$
\mathbb{C}^2_+=\operatorname{im}P_+=\operatorname{im}P_1\oplus\operatorname{im}P_3,
\qquad
\mathbb{C}^2_-=\operatorname{im}P_-=\operatorname{im}P_2\oplus\operatorname{im}P_4 .
$$

**Proposition.** The projectors $P_+,P_-$ are idempotent, orthogonal and complete, of rank $2$ each:

$$
P_+^2=P_+,\qquad P_-^2=P_-,\qquad P_+P_-=0,\qquad P_++P_-=I.
$$

The carrier splits as

$$
\mathbb{C}^4=\mathbb{C}^2_+\oplus\mathbb{C}^2_-,
$$

and $\Gamma$ acts as $+1$ on $\mathbb{C}^2_+$ and $-1$ on $\mathbb{C}^2_-$.

**Proof.** $P_\pm$ are the spectral projectors of the involution $\Gamma$ for the eigenvalues $\pm1$. The images are the eigenspaces, of dimension $2$ each. The algebraic identities follow from $\Gamma^2=I$.

**The chirality basis.** In the standard frame, the chirality $+$ is spanned by $e_1,e_3$ and the chirality $-$ by $e_2,e_4$. In a general frame, the two planes are the sums of the corresponding spectral lines. The two planes are not orthogonal for the standard Hermitian form unless the spectral projectors are Hermitian, which fails for a general root; they are complementary, and the decomposition $\mathbb{C}^4=\mathbb{C}^2_+\oplus\mathbb{C}^2_-$ is a direct sum, not an orthogonal sum.

**The two chiralities are not minimal left ideals.** A minimal left ideal of $M_4(\mathbb{C})$ is a space $M_4P_k$, of dimension $4$. The chirality $\mathbb{C}^2_+$ has dimension $2$ and is a subspace of the carrier. It is not stable under left multiplication by an arbitrary matrix: the left module $M_4\cdot\mathbb{C}^2_+$ is all of $\mathbb{C}^4$, because $M_4$ acts transitively on nonzero vectors. The chirality is a subspace of the carrier, not an ideal of the algebra.

## The Chiral Blocks of the Algebra

Relative to the decomposition $\mathbb{C}^4=\mathbb{C}^2_+\oplus\mathbb{C}^2_-$, every matrix has a block form

$$
A=\begin{pmatrix}
A_{++}&A_{+-}\\
A_{-+}&A_{--}
\end{pmatrix},
\qquad
A_{++}\in M_2(\mathbb{C}),\quad
A_{--}\in M_2(\mathbb{C}),
$$

with $A_{+-}:\mathbb{C}^2_-\to\mathbb{C}^2_+$ and $A_{-+}:\mathbb{C}^2_+\to\mathbb{C}^2_-$. Define the four **chiral corners**

$$
\mathcal{A}=P_+M_4P_+,\qquad
\mathcal{B}=P_+M_4P_-,\qquad
\mathcal{C}=P_-M_4P_+,\qquad
\mathcal{D}=P_-M_4P_- .
$$

**Theorem.** The algebra is the direct sum

$$
M_4(\mathbb{C})=\mathcal{A}\oplus\mathcal{B}\oplus\mathcal{C}\oplus\mathcal{D},
$$

with

$$
\dim_\mathbb{C}\mathcal{A}=4,\qquad
\dim_\mathbb{C}\mathcal{B}=4,\qquad
\dim_\mathbb{C}\mathcal{C}=4,\qquad
\dim_\mathbb{C}\mathcal{D}=4.
$$

The diagonal corners are matrix algebras,

$$
\mathcal{A}\cong M_2(\mathbb{C}),\qquad
\mathcal{D}\cong M_2(\mathbb{C}),
$$

and the off-diagonal corners are the spaces of maps between the two planes,

$$
\mathcal{B}\cong\operatorname{Hom}(\mathbb{C}^2_-,\mathbb{C}^2_+)\cong M_2(\mathbb{C}),
\qquad
\mathcal{C}\cong\operatorname{Hom}(\mathbb{C}^2_+,\mathbb{C}^2_-)\cong M_2(\mathbb{C}).
$$

**Proof.** Choose a basis adapted to the decomposition, with the first two vectors in $\mathbb{C}^2_+$ and the last two in $\mathbb{C}^2_-$. In that basis $P_+=\operatorname{diag}(I_2,0)$ and $P_-=\operatorname{diag}(0,I_2)$, and the four corners are the four $2\times2$ blocks of the block matrix. Each block has four complex entries; the dimensions are $4+4+4+4=16$. The diagonal blocks are closed under multiplication and are full $2\times2$ matrix algebras; the off-diagonal blocks are the spaces of linear maps between the two planes, each isomorphic to $M_2(\mathbb{C})$ as a vector space.

**The multiplication table.** In block form,

$$
\begin{pmatrix}A&B\\C&D\end{pmatrix}
\begin{pmatrix}A'&B'\\C'&D'\end{pmatrix}
=
\begin{pmatrix}
AA'+BC'&AB'+BD'\\
CA'+DC'&CB'+DD'
\end{pmatrix}.
$$

The products $BC'\subseteq\mathcal{A}$ and $CB'\subseteq\mathcal{D}$ return to the diagonal. The off-diagonal blocks are **bimodules**: $\mathcal{B}$ is a left $\mathcal{A}$-module and a right $\mathcal{D}$-module, and $\mathcal{C}$ is a left $\mathcal{D}$-module and a right $\mathcal{A}$-module. The algebra is not the direct sum of $\mathcal{A}$ and $\mathcal{D}$ as algebras; the blocks $\mathcal{B}$ and $\mathcal{C}$ are nonzero and multiply back into the diagonal. This is the rank-two Peirce split of *The Rank-Two Split of $M_4(\mathbb{C})$*.

**The mass block.** The corner

$$
\mathcal{B}=P_+M_4P_-=\operatorname{Hom}(\mathbb{C}^2_-,\mathbb{C}^2_+)
$$

is the **mass block**. It is four-dimensional, and its elements are the maps from the right chirality to the left chirality. The opposite corner $\mathcal{C}$ is the conjugate mass block. The two together are the off-diagonal part of the algebra, of dimension $8$. The mass block is the subject of *The Mass Block and the Chiral Polar Decomposition of $M_4(\mathbb{C})$*.

**The traces.** The trace of $A$ is the sum of the traces of the diagonal blocks:

$$
\operatorname{tr}A=\operatorname{tr}A_{++}+\operatorname{tr}A_{--}.
$$

The off-diagonal blocks are traceless as blocks: they contribute nothing to the trace. The determinant is the determinant of the full $4\times4$ block matrix; on an invertible $A$ the Schur complement formula gives

$$
\det A=\det(A_{++}-A_{+-}A_{--}^{-1}A_{-+})\det A_{--}.
$$

The formula shows that the mass block enters the determinant through the combination $A_{+-}A_{--}^{-1}A_{-+}$.

## The Even and Odd Parts

**The chirality involution acts on the algebra by conjugation.** Let

$$
\operatorname{Ad}_\Gamma(X)=\Gamma X\Gamma^{-1}=\Gamma X\Gamma .
$$

Because $\Gamma^2=I$, the operator $\operatorname{Ad}_\Gamma$ is an involution of $M_4$. Its $+1$ eigenspace is the **centraliser** of $\Gamma$:

$$
M_4^{+}=\{X:\Gamma X=X\Gamma\},
$$

and its $-1$ eigenspace is

$$
M_4^{-}=\{X:\Gamma X=-X\Gamma\}.
$$

**Proposition.** The centraliser is the block-diagonal part,

$$
M_4^{+}=\mathcal{A}\oplus\mathcal{D},
\qquad \dim_\mathbb{C}=8,
$$

and the $-1$ eigenspace is the off-diagonal part,

$$
M_4^{-}=\mathcal{B}\oplus\mathcal{C},
\qquad \dim_\mathbb{C}=8.
$$

**Proof.** Write $X$ in block form. The condition $\Gamma X=X\Gamma$ with $\Gamma=\operatorname{diag}(I_2,-I_2)$ reads

$$
\begin{pmatrix}X_{++}&-X_{+-}\\-X_{-+}&X_{--}\end{pmatrix}
=
\begin{pmatrix}X_{++}&X_{+-}\\X_{-+}&X_{--}\end{pmatrix},
$$

so $X_{+-}=X_{-+}=0$. The condition $\Gamma X=-X\Gamma$ gives $X_{++}=X_{--}=0$.

**The relation to the $\mathbb{Z}/4$ grading.** Recall

$$
M_4=\mathcal{M}^{(0)}\oplus\mathcal{M}^{(1)}\oplus\mathcal{M}^{(2)}\oplus\mathcal{M}^{(3)},
\qquad
\operatorname{Ad}_H(X)=\zeta^rX\quad\text{on }\mathcal{M}^{(r)}.
$$

Because $\operatorname{Ad}_\Gamma=\operatorname{Ad}_H^2$, the involution acts on $\mathcal{M}^{(r)}$ by $\zeta^{2r}=(-1)^r$. Hence

$$
M_4^{+}=\mathcal{M}^{(0)}\oplus\mathcal{M}^{(2)},
\qquad
M_4^{-}=\mathcal{M}^{(1)}\oplus\mathcal{M}^{(3)}.
$$

The chirality is the $\mathbb{Z}/2$ quotient of the $\mathbb{Z}/4$ grading. The even part is the centraliser of $\Gamma$; the odd part is the mass block and its opposite.

**Two different $2+2$ splits.** The carrier split

$$
\mathbb{C}^4=\mathbb{C}^2_+\oplus\mathbb{C}^2_-
$$

is the decomposition into the eigenspaces of $\Gamma$. The algebra split

$$
M_4=M_4^{+}\oplus M_4^{-}
$$

is the decomposition into the eigenspaces of $\operatorname{Ad}_\Gamma$. They are related but not the same: the first splits vectors, the second splits operators. The chiral corners $\mathcal{A},\mathcal{B},\mathcal{C},\mathcal{D}$ refine the second: $\mathcal{A}\oplus\mathcal{D}$ is the even part, $\mathcal{B}\oplus\mathcal{C}$ the odd part, and each of the four corners has dimension four.

## The Root and the Chirality

**The map $H\mapsto\Gamma=H^2$ has complex four-dimensional fibres over its image.** Fix an involution $\Gamma$ with spectrum $(1,1,-1,-1)$. Its $+1$ eigenspace $\mathbb{C}^2_+$ and its $-1$ eigenspace $\mathbb{C}^2_-$ are determined. A root $H$ with $H^2=\Gamma$ must preserve each eigenspace, act on $\mathbb{C}^2_+$ with eigenvalues $+1,-1$ on two lines, and act on $\mathbb{C}^2_-$ with eigenvalues $i,-i$ on two lines. The data are:

- a decomposition of $\mathbb{C}^2_+$ into two ordered lines, a space of dimension $2$;
- a decomposition of $\mathbb{C}^2_-$ into two ordered lines, a space of dimension $2$;
- a choice of which line in $\mathbb{C}^2_+$ carries $+1$ and which carries $-1$, two choices;
- a choice of which line in $\mathbb{C}^2_-$ carries $i$ and which carries $-i$, two choices.

Once the two line decompositions are fixed, the eigenvalue assignment has four choices. The fibre is the $2+2=4$-dimensional space of decompositions, and the four choices are discrete labels inside it.

**The dimensions.** The image of the map is the conjugacy class of involutions with spectrum $(1,1,-1,-1)$. Its dimension is

$$
\dim PGL_4-\dim P(GL_2\times GL_2)=15-(4+4-1)=15-7=8.
$$

The fibre has dimension $4$, so the root set has dimension

$$
8+4=12,
$$

which is the count of *Roots of Unity and the Lagrange Idempotents of $M_4(\mathbb{C})$*. For a fixed unordered pair of line decompositions the four eigenvalue assignments are discrete labels; they do not add to the dimension of the fibre.

**The chirality is not the root.** The root has order four and determines $\Gamma$; $\Gamma$ has order two and does not determine the root. The chirality is the invariant that survives the squaring, and the root is a square root of the chirality. The two chiralities are the eigenspaces of the surviving involution; the root is the finer data that splits each chirality into two lines with the eigenvalues $\pm1$ or $\pm i$.

## The Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ and the Peirce $\mathfrak{su}_2$

**The chiral algebra preserves $\Gamma$.** The block-diagonal traceless endomorphisms

$$
\mathfrak{sl}_2(\mathbb{C})_+\oplus\mathfrak{sl}_2(\mathbb{C})_-
=\left\{\begin{pmatrix}A&0\\0&D\end{pmatrix}:\operatorname{tr}A=\operatorname{tr}D=0\right\}
$$

act on $\mathbb{C}^2_+$ and $\mathbb{C}^2_-$ separately. They commute with $\Gamma$, they have dimension $3+3=6$, and each chirality is a highest-weight-$\tfrac12$ module for one of the two factors. The compact real form is $\mathfrak{su}_2\oplus\mathfrak{su}_2$.

**The Peirce algebra mixes the chiralities.** The generators $J_3,J_\pm$ of the principal $\mathfrak{sl}_2$ are

$$
J_3=\operatorname{diag}\left(\frac32,\frac12,-\frac12,-\frac32\right),
\qquad
J_+=\sqrt3E_{12}+2E_{23}+\sqrt3E_{34}.
$$

The Cartan $J_3$ is diagonal, hence commutes with $\Gamma$; the raising and lowering operators do not. For example,

$$
J_+e_2=\sqrt3e_1,\qquad J_+e_4=\sqrt3e_3,
$$

and $e_2,e_4$ have chirality $-1$ while $e_1,e_3$ have chirality $+1$. The Peirce $\mathfrak{sl}_2$ is irreducible on $\mathbb{C}^4$, so it has no invariant subspace that is one chirality. It is not contained in the chiral $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$, and the chiral algebra is not contained in it: they are different three- and six-dimensional subalgebras of $\mathfrak{sl}_4$.

**The two chains.** The Peirce chain is the weight chain of the highest-weight-$\tfrac32$ module; it runs through both chiralities. The chiral chain is the pair of highest-weight-$\tfrac12$ chains, one in each chirality; it preserves $\Gamma$ and does not mix. The first is the chain of the flag; the second is the chain of the two planes. The comparison, with the branching rules, is *The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$*.

## The Biquaternion Case

**At $n=2$ the matrix-model chirality is the root itself, and it is not the biquaternion chirality.** The biquaternion algebra is $M_2(\mathbb{C})$, the root $H$ has order two, $H^2=I$, and the general formula $\Gamma=H^2$ degenerates: the matrix-model chirality is $\Gamma=H$. This $\Gamma$ grades the carrier into the two eigenspaces of the Peirce root. Those eigenspaces are lines; they are the two weight lines of the frame, and each minimal left ideal, a column, contains one line of each sign. They are not the two Peirce copies. The chirality of the biquaternion Dirac field is the separate central sign $\chi=ij$ of *Chirality: The Conjugate Pair*, which grades $S$ against $S^{\mathrm{c}}$; it is not an eigenspace of $H$.

The two matrix-model chiralities are the two eigenspaces of $H$, which are lines. The chiral blocks are

$$
\mathcal{A}=P_+M_2P_+,\quad
\mathcal{B}=P_+M_2P_-,\quad
\mathcal{C}=P_-M_2P_+,\quad
\mathcal{D}=P_-M_2P_-,
$$

each of dimension $1$, and the mass block is a line. The chiral algebra is the Cartan of $M_2$, of dimension $1$, not a product of two $\mathfrak{su}_2$'s. The product $\mathfrak{su}_2\times\mathfrak{su}_2$ is a feature of the four-dimensional carrier, where each chirality is a plane.

**The degeneration.** At $n=2$ the two matrix-model chiralities are lines, and the mass block is a line. At $n=4$ the two chiralities are planes and the mass block is four-dimensional. The passage from $n=2$ to $n=4$ replaces the two lines by two planes and the one mass line by a four-dimensional mass block. The chirality involution survives, but its eigenspaces grow.

## Summary

The chirality involution is $\Gamma=H^2$, an involution with eigenvalues $+1$ on $V_1\oplus V_3$ and $-1$ on $V_2\oplus V_4$, trace zero, and two eigenspaces of dimension two. The carrier splits as $\mathbb{C}^4=\mathbb{C}^2_+\oplus\mathbb{C}^2_-$, and the algebra splits into four chiral corners of dimension four each:

$$
M_4(\mathbb{C})=\mathcal{A}\oplus\mathcal{B}\oplus\mathcal{C}\oplus\mathcal{D},
\qquad 4+4+4+4=16,
$$

with $\mathcal{A},\mathcal{D}\cong M_2(\mathbb{C})$ and $\mathcal{B},\mathcal{C}$ the mass blocks. The even part $\mathcal{A}\oplus\mathcal{D}$ is the centraliser of $\Gamma$, of dimension eight; the odd part $\mathcal{B}\oplus\mathcal{C}$ is the mass block and its opposite, of dimension eight. The chirality is the $\mathbb{Z}/2$ quotient of the $\mathbb{Z}/4$ grading. The two chiralities are subspaces of the carrier, not minimal left ideals; the minimal left ideals of $M_4$ are the four-dimensional spaces $M_4P_k$. The chiral $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ preserves $\Gamma$ and acts as highest-weight-$\tfrac12$ on each chirality; the Peirce $\mathfrak{sl}_2$ is irreducible and mixes the chiralities. At $n=2$ the matrix-model chirality is the root itself and its two eigenspaces are lines; the biquaternion chirality is the central sign $\chi=ij$ of *Chirality: The Conjugate Pair*.

$$
\boxed{\ \Gamma=H^2,\quad \Gamma^2=I,\quad \operatorname{tr}\Gamma=0,\quad \mathbb{C}^4=\mathbb{C}^2_+\oplus\mathbb{C}^2_-,\quad M_4=\mathcal{A}\oplus\mathcal{B}\oplus\mathcal{C}\oplus\mathcal{D},\quad 4+4+4+4=16.\ }
$$

| Object | Dimension |
|---|---|
| Chirality $+$ | $2$ |
| Chirality $-$ | $2$ |
| Chiral corner $\mathcal{A}$ | $4$ |
| Chiral corner $\mathcal{D}$ | $4$ |
| Mass block $\mathcal{B}$ | $4$ |
| Mass block $\mathcal{C}$ | $4$ |
| Even part $\mathcal{A}\oplus\mathcal{D}$ | $8$ |
| Odd part $\mathcal{B}\oplus\mathcal{C}$ | $8$ |
| Chiral $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ | $6$ |
| Peirce $\mathfrak{sl}_2$ | $3$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Gamma=H^2$ | the chirality involution |
| $P_\pm=\frac12(I\pm\Gamma)$ | the chirality projectors, rank two |
| $\mathbb{C}^2_\pm=\operatorname{im}P_\pm$ | the two chiralities |
| $\mathcal{A}=P_+M_4P_+$ | the left chiral block, $\cong M_2(\mathbb{C})$ |
| $\mathcal{D}=P_-M_4P_-$ | the right chiral block, $\cong M_2(\mathbb{C})$ |
| $\mathcal{B}=P_+M_4P_-$ | the mass block |
| $\mathcal{C}=P_-M_4P_+$ | the conjugate mass block |
| $M_4^{+}$ | the centraliser of $\Gamma$, the even part |
| $M_4^{-}$ | the odd part, the mass block and its opposite |
| $\mathcal{M}^{(r)}$ | the graded piece of the $\mathbb{Z}/4$ grading |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for idempotents, Peirce decompositions and the centraliser of an involution.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for block matrices, Schur complements and the determinant.
- [Roots of Unity and the Lagrange Idempotents of $M_4(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-m4c.html), for the root and the involution $\Gamma=H^2$.
- [The Peirce Decomposition of $M_4(\mathbb{C})$](the-peirce-decomposition-of-m4c.html), for the sixteen corners of the root.
- [The Rank-Two Split of $M_4(\mathbb{C})$](the-rank-two-split-of-m4c.html), for the corners of the rank-two idempotent $P_+$.
- [The Mass Block and the Chiral Polar Decomposition of $M_4(\mathbb{C})$](the-mass-block-and-the-chiral-polar-decomposition-of-m4c.html), for the mass block and its polar decomposition.
- [The Peirce $\mathfrak{su}_2$ and the Chiral $\mathfrak{su}_2\times\mathfrak{su}_2$ of $M_4(\mathbb{C})$](the-peirce-su2-and-the-chiral-su2-su2-of-m4c.html), for the two chains.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the biquaternion case $n=2$.
