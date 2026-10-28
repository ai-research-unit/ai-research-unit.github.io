# __The Two Chiralities__

## Introduction

The cube of a root of order six is an involution:

$$
\Gamma=H^3,\qquad \Gamma^2=I_6,\qquad \operatorname{tr}\Gamma=0 .
$$

Its eigenvalues $+1$ and $-1$ have multiplicity three each, so the carrier splits as

$$
\mathbb{C}^6=V_+\oplus V_-,
\qquad
V_+=V_1\oplus V_3\oplus V_5,\quad
V_-=V_2\oplus V_4\oplus V_6 .
$$

This is the **$3+3$ chiral split**. The chiral blocks of the algebra are the two $M_3$ corners, and the off-diagonal block between them is the **mass block**, of dimension $3\cdot3=9$.

The involution is one of the three quotient gradings of the $\mathbb{Z}/6$ grading: $\Gamma$ is the $\mathbb{Z}/2$ quotient, the square $H^2$ gives the $\mathbb{Z}/3$ quotient, and $H$ itself gives the full $\mathbb{Z}/6$. The article develops the split, the three gradings, the mass block, and the contrast with the $2+2$ split of $M_4$ and the $1+1$ split of the biquaternion algebra.

It assumes the root and its Lagrange projectors of *Roots of Unity and the Lagrange Idempotents*. It uses no form and no topology. The mass block's polar decomposition is *The Mass Block and the Chiral Polar Decomposition*; the block corners are *The $M_3\oplus M_3$ and $M_2\oplus M_4$ Corners*; the spin chain is *The Spin Chain and the Adjoint Decomposition*.

## The Chirality Involution

### Definition and Spectrum

**Definition.** Let $H$ be a root of order six. The **chirality involution** is

$$
\Gamma=H^3 .
$$

**Theorem.** $\Gamma$ is an involution with eigenvalues $+1$ and $-1$, each of multiplicity three:

$$
\Gamma^2=I_6,\qquad
\Gamma\neq\pm I_6,\qquad
\operatorname{tr}\Gamma=0 .
$$

In the Lagrange projectors,

$$
\Gamma=\sum_{k=1}^{6}(-1)^{k-1}P_k
=P_1-P_2+P_3-P_4+P_5-P_6 .
$$

**Proof.** For each eigenvalue $\zeta_k=\zeta^{k-1}$ of $H$, $\zeta_k^3=(-1)^{k-1}$. The spectral formula gives $\Gamma=\sum_k\zeta_k^3P_k=\sum_k(-1)^{k-1}P_k$; the three odd-indexed projectors contribute $+1$ and the three even-indexed ones $-1$. The square is $\sum_kP_k=I_6$, and the trace is $3-3=0$.

**Corollary (the chiral projectors).**

$$
\Pi_+=\frac{I_6+\Gamma}{2}=P_1+P_3+P_5,
\qquad
\Pi_-=\frac{I_6-\Gamma}{2}=P_2+P_4+P_6,
$$

with

$$
\Pi_\pm^2=\Pi_\pm,\qquad
\Pi_+\Pi_-=0,\qquad
\Pi_++\Pi_-=I_6,\qquad
\operatorname{rank}\Pi_\pm=3 .
$$

**Proof.** A polynomial in $\Gamma$ with $L(\pm1)=1$ and $L(\mp1)=0$ is the projector onto the corresponding eigenspace. The trace of a rank-three projector is three.

### The Chiral Eigenspaces

**Definition.** The **chiral halves** of the carrier are

$$
V_+=\operatorname{im}\Pi_+=\ker(\Gamma-I_6),
\qquad
V_-=\operatorname{im}\Pi_-=\ker(\Gamma+I_6).
$$

**Proposition.**

$$
V_+=\bigoplus_{j=0}^{2}V_{2j+1}=\mathbb{C}v_1\oplus\mathbb{C}v_3\oplus\mathbb{C}v_5,
\qquad
V_-=\bigoplus_{j=0}^{2}V_{2j+2}=\mathbb{C}v_2\oplus\mathbb{C}v_4\oplus\mathbb{C}v_6,
$$

and $\mathbb{C}^6=V_+\oplus V_-$, with $\dim V_\pm=3$.

**Proof.** $\Gamma$ acts on $V_k$ by $(-1)^{k-1}$; so $V_k\subseteq V_+$ for $k$ odd and $V_k\subseteq V_-$ for $k$ even. The six lines are independent and their dimensions sum to six.

**Remark (the halves are not ideals).** Each chiral half is a three-dimensional subspace of the carrier. It is not a left ideal of $M_6$, not a minimal left ideal, and not a corner of the algebra. The minimal left ideals of $M_6$ are the six-dimensional columns. **The chiral halves live in the carrier; the chiral blocks live in the algebra.**

### The Chiral Blocks

**Theorem (the block decomposition).** Relative to $\mathbb{C}^6=V_+\oplus V_-$, every $A\in M_6(\mathbb{C})$ has a unique block form

$$
A=\begin{pmatrix}A_{++}&A_{+-}\\A_{-+}&A_{--}\end{pmatrix},
$$

with

$$
A_{++}\in\operatorname{End}(V_+)\cong M_3,\quad
A_{--}\in\operatorname{End}(V_-)\cong M_3,\quad
A_{+-}\in\operatorname{Hom}(V_-,V_+)\cong\mathbb{C}^{3\times3},\quad
A_{-+}\in\operatorname{Hom}(V_+,V_-)\cong\mathbb{C}^{3\times3}.
$$

The four blocks have dimension $9$ each, and

$$
36=9+9+9+9 .
$$

**Proof.** A linear map from a direct sum to a direct sum is a $2\times2$ matrix of maps between the summands. The dimension of $\operatorname{Hom}(V_\pm,V_\pm)$ is $3\cdot3=9$, and of $\operatorname{Hom}(V_\mp,V_\pm)$ is also $9$.

**Corollary (the corner identifications).**

$$
\Pi_+M_6\Pi_+=M_3(V_+),\qquad
\Pi_-M_6\Pi_-=M_3(V_-),\qquad
\Pi_+M_6\Pi_-=\operatorname{Hom}(V_-,V_+),\qquad
\Pi_-M_6\Pi_+=\operatorname{Hom}(V_+,V_-).
$$

**Proof.** These are the four corners of the idempotent $\Pi_+$, by *The Peirce Decomposition*, with the rank $p=3$.

**Definition.** The block $A_{+-}=\Pi_+A\Pi_-$ is the **mass block**. It maps the negative chiral half into the positive one, and it is a $3\times3$ matrix. Its partner $A_{-+}$ is the conjugate mass block, mapping $V_+$ to $V_-$.

**Remark (the mass block has dimension 9).** The number is the product of the two chiral dimensions, $3\cdot3=9$. For $M_4$ it is $2\cdot2=4$; for the biquaternion algebra $M_2$ it is $1\cdot1=1$. **The mass block is the off-diagonal square of the chiral split.**

## The Three Gradings

### The $\mathbb{Z}/6$ Grading

Let $P_1,\dots,P_6$ be the Lagrange projectors and $A_{kl}=P_kM_6P_l$ the Peirce lines.

**Theorem.** The algebra decomposes as

$$
M_6(\mathbb{C})=\bigoplus_{r=0}^{5}A_r,
\qquad
A_r=\bigoplus_{k-l\equiv r\pmod6}A_{kl},
\qquad
\dim A_r=6,
$$

and $A_rA_s\subseteq A_{r+s}$.

**Proof.** The Peirce line $A_{kl}$ has degree $k-l$; a product $A_{kl}A_{mn}$ is either zero or $A_{kn}$, of degree $(k-l)+(m-n)$, and the degree is additive modulo six. For fixed $r$ and each $k$ there is exactly one $l=k-r$, so $A_r$ is the sum of six lines.

**Theorem (the grading automorphism).** Conjugation by $H$ preserves the decomposition and acts on $A_r$ by the scalar $\zeta^r$:

$$
HAH^{-1}=\zeta^rA
\qquad
(A\in A_r).
$$

**Proof.** On the line $A_{kl}=\mathbb{C}E_{kl}$, $HE_{kl}H^{-1}=(\zeta_k/\zeta_l)E_{kl}=\zeta^{k-l}E_{kl}=\zeta^rE_{kl}$.

**Remark (the automorphism, not the derivation).** The grading is the eigenspace decomposition of the automorphism $\operatorname{Ad}_H(A)=HAH^{-1}$, not of the derivation $\operatorname{ad}_H(A)=HA-AH$. On $A_{kl}$ the derivation acts by $\zeta_k-\zeta_l$, which is not a sixth root of unity; the automorphism acts by the root $\zeta^{k-l}$. **The grading is a symmetry of the algebra, and it is inner.**

### The $\mathbb{Z}/2$ Quotient

**Theorem.** The map $\mathbb{Z}/6\to\mathbb{Z}/2$, $r\mapsto r\bmod2$, gives the decomposition

$$
M_6(\mathbb{C})=A_{\text{even}}\oplus A_{\text{odd}},
\qquad
A_{\text{even}}=\bigoplus_{r\text{ even}}A_r,
\qquad
A_{\text{odd}}=\bigoplus_{r\text{ odd}}A_r,
$$

with

$$
\dim A_{\text{even}}=\dim A_{\text{odd}}=18,
\qquad
A_{\text{even}}A_{\text{even}}\subseteq A_{\text{even}},\quad
A_{\text{even}}A_{\text{odd}}\subseteq A_{\text{odd}},\quad
A_{\text{odd}}A_{\text{odd}}\subseteq A_{\text{even}}.
$$

**Proof.** The parity of $r+s$ is the sum of the parities. The dimensions are $3\cdot6=18$ each.

**Theorem (the $\mathbb{Z}/2$ grading is the chirality).** Conjugation by $\Gamma$ acts as $+1$ on $A_{\text{even}}$ and as $-1$ on $A_{\text{odd}}$:

$$
\Gamma A\Gamma=(-1)^rA
\qquad
(A\in A_r).
$$

**Proof.** $\Gamma=H^3$, so $\Gamma A\Gamma=H^3AH^{-3}=\zeta^{3r}A=(-1)^rA$.

**Corollary.** The fixed subalgebra of $\operatorname{Ad}_\Gamma$ is $A_{\text{even}}$, and it is exactly the block-diagonal subalgebra of the chiral split:

$$
A_{\text{even}}=M_3(V_+)\oplus M_3(V_-),
\qquad
A_{\text{odd}}=\operatorname{Hom}(V_-,V_+)\oplus\operatorname{Hom}(V_+,V_-).
$$

**Proof.** $A_{\text{even}}$ consists of the lines $A_{kl}$ with $k-l$ even, that is with $k$ and $l$ of the same parity, that is with both indices in $\{1,3,5\}$ or both in $\{2,4,6\}$. These are the two diagonal chiral blocks. The odd part is the two off-diagonal blocks.

**Corollary (the massless subalgebra).** The massless elements $A_{+-}=A_{-+}=0$ form the subalgebra $A_{\text{even}}\cong M_3\oplus M_3$, of dimension $18$. The mass block and its partner add the remaining $9+9=18$ dimensions.

### The $\mathbb{Z}/3$ Quotient

**Theorem.** The map $\mathbb{Z}/6\to\mathbb{Z}/3$, $r\mapsto r\bmod3$, gives the decomposition

$$
M_6(\mathbb{C})=B_0\oplus B_1\oplus B_2,
\qquad
B_s=\bigoplus_{r\equiv s\pmod3}A_r,
$$

with

$$
\dim B_0=\dim B_1=\dim B_2=12,
\qquad
B_sB_t\subseteq B_{s+t\bmod3}.
$$

**Proof.** Each $B_s$ is the sum of two graded pieces $A_r$, each of dimension six. The product rule is the product rule of the quotient group $\mathbb{Z}/3$.

**Theorem (the $\mathbb{Z}/3$ grading automorphism).** Conjugation by $H^2$ acts on $B_s$ by $\omega^s$, where $\omega=\zeta^2$ is a primitive cube root of unity:

$$
H^2AH^{-2}=\omega^sA
\qquad
(A\in B_s).
$$

**Proof.** $H^2AH^{-2}=\zeta^{2r}A=\omega^rA$ for $A\in A_r$.

**Theorem (the fixed algebra of the $\mathbb{Z}/3$ quotient).** The fixed subalgebra $B_0$ is isomorphic to $M_2(\mathbb{C})\oplus M_2(\mathbb{C})\oplus M_2(\mathbb{C})$:

$$
B_0=A_0\oplus A_3
=\left\langle E_{11},E_{44},E_{14},E_{41}\right\rangle
\oplus\left\langle E_{22},E_{55},E_{25},E_{52}\right\rangle
\oplus\left\langle E_{33},E_{66},E_{36},E_{63}\right\rangle,
$$

the three $2\times2$ blocks on the pairs of opposite lines $(1,4),(2,5),(3,6)$. In particular $\dim B_0=12$.

**Proof.** $A_0$ is the diagonal, spanned by the six $E_{ii}$; $A_3$ is spanned by $E_{14},E_{25},E_{36}$ and their transposes. On the pair $(1,4)$ the four units $E_{11},E_{44},E_{14},E_{41}$ span a full $M_2$; the three pairs are independent, and the units of different pairs multiply to zero. So $B_0$ is the direct sum of the three $M_2$'s, of dimension $3\cdot4=12$.

**Corollary (the three opposite pairs).** The $\mathbb{Z}/3$ quotient is the **opposite-pair grading**: the six lines are grouped into the three opposite pairs

$$
\{1,4\},\qquad\{2,5\},\qquad\{3,6\},
$$

each pair spans a two-dimensional subspace, and $B_0$ is the algebra of the three pairs with no mixing. The pieces $B_1$ and $B_2$ are the mixing blocks between the pairs.

**Proof.** The pairs are the orbits of $k\mapsto k+3$; $A_0$ and $A_3$ are exactly the lines that stay inside a pair, so $B_0$ has no mixing. A line $A_{kl}$ with $k-l\equiv1$ or $2$ connects two different pairs, so $B_1,B_2$ are the mixing blocks.

### The Three Gradings Together

**Theorem.** The $\mathbb{Z}/6$ grading is the common refinement of the $\mathbb{Z}/2$ and $\mathbb{Z}/3$ gradings. For each $r$,

$$
A_r=A_{\text{even/odd}}\cap B_{r\bmod3},
$$

according to the parity of $r$. The Chinese remainder theorem $\mathbb{Z}/6\cong\mathbb{Z}/2\times\mathbb{Z}/3$ makes the two quotient gradings independent.

**Proof.** The class of $r$ modulo six is determined by its classes modulo two and modulo three. The intersection of the parity class and the mod-three class is the class modulo six.

**Corollary (the three operators).** The three gradings are the eigenspace decompositions of the three commuting automorphisms

$$
\operatorname{Ad}_H,\qquad
\operatorname{Ad}_{H^2}=\operatorname{Ad}_H^2,\qquad
\operatorname{Ad}_{H^3}=\operatorname{Ad}_H^3,
$$

of orders $6,3,2$. The eigenvalues are the sixth roots, the cube roots and the signs.

**Proof.** These are the powers of $\operatorname{Ad}_H$, which has order six.

| Grading | Group | Pieces | Dimensions | Operator |
|---|---|---|---|---|
| full | $\mathbb{Z}/6$ | $A_0,\dots,A_5$ | $6,6,6,6,6,6$ | $\operatorname{Ad}_H$ |
| chirality | $\mathbb{Z}/2$ | $A_{\text{even}},A_{\text{odd}}$ | $18,18$ | $\operatorname{Ad}_{H^3}=\operatorname{Ad}_\Gamma$ |
| opposite pairs | $\mathbb{Z}/3$ | $B_0,B_1,B_2$ | $12,12,12$ | $\operatorname{Ad}_{H^2}$ |

**Remark (what each quotient sees).** The $\mathbb{Z}/2$ quotient sees the parity of the line, that is the chirality. The $\mathbb{Z}/3$ quotient sees the line modulo three, that is the opposite pair. The full $\mathbb{Z}/6$ sees both at once. **The chirality and the opposite-pair structure are independent: their product is the root.**

## The Mass Block

### The Block Matrix

In the chiral split,

$$
A=\begin{pmatrix}A_{++}&M\\N&A_{--}\end{pmatrix},
\qquad
A_{++},A_{--},M,N\in M_3(\mathbb{C}),
$$

with $M=A_{+-}$ the mass block and $N=A_{-+}$ its partner. The product is the block product

$$
\begin{pmatrix}A_{++}&M\\N&A_{--}\end{pmatrix}
\begin{pmatrix}A_{++}'&M'\\N'&A_{--}'\end{pmatrix}
=
\begin{pmatrix}
A_{++}A_{++}'+MN' & A_{++}M'+MA_{--}'\\
NA_{++}'+A_{--}N' & NM'+A_{--}A_{--}'
\end{pmatrix}.
$$

**Proposition (the trace and the determinant).**

$$
\operatorname{tr}A=\operatorname{tr}A_{++}+\operatorname{tr}A_{--},
\qquad
\det A=\det A_{--}\det\left(A_{++}-MA_{--}^{-1}N\right)
$$

when $A_{--}$ is invertible.

**Proof.** The trace is the sum of the traces of the diagonal blocks. The determinant is the Schur complement formula of *The $M_3\oplus M_3$ and $M_2\oplus M_4$ Corners*.

### The Gauge on the Mass Block

**Definition.** The **relative chiral scale** is the class of

$$
\operatorname{diag}(tI_3,sI_3),\qquad t,s\in\mathbb{C}^\times,
$$

modulo the overall scalar; it is parameterised by $t/s$.

**Proposition.** Under the relative chiral scale, the mass block is multiplied by $t/s$:

$$
M\longmapsto\frac{t}{s}M .
$$

The traceless diagonal tori of the two chiral blocks act by left and right multiplication.

**Proof.** Conjugation by $\operatorname{diag}(tI_3,sI_3)$ sends the block $M$ to $tMs^{-1}=(t/s)M$; the traceless parts act inside $M_3(V_+)$ and $M_3(V_-)$, hence by left and right multiplication on $M$.

**Corollary (the gauge invariant of the mass block).** The singular values of $M$ are all multiplied by $\lvert t/s\rvert$; their ratios are invariant under the relative scale, and the left and right unitary actions do not change them.

**Proof.** The singular values of $(t/s)M$ are $\lvert t/s\rvert$ times those of $M$; left and right multiplication by unitaries preserves them.

### The Massless Algebra

**Theorem.** The set of elements with vanishing mass block is the subalgebra

$$
\left\{\begin{pmatrix}A_{++}&0\\0&A_{--}\end{pmatrix}\right\}
\cong M_3(\mathbb{C})\oplus M_3(\mathbb{C}),
$$

of dimension $18$. The full algebra is obtained by adding the mass block $M$ (dimension $9$) and its partner $N$ (dimension $9$).

**Proof.** The block-diagonal matrices are closed under multiplication; the two off-diagonal blocks are independent $3\times3$ spaces.

**Remark (the mass is not an ideal).** The mass block $M$ alone is not an ideal: the product of a mass block with a partner can return a diagonal block, and the diagonal blocks act on the mass block from both sides. **The mass block is a bimodule over the massless algebra, and the mass term is the extension that makes $M_6$ simple.**

## The Contrast with $M_4$

### The $2+2$ Split

Let $H_4$ be a root of order four and $\Gamma_4=H_4^2$. Then $\Gamma_4$ is an involution with eigenvalues $\pm1$, each of multiplicity two, and the chiral split is $2+2$:

$$
\mathbb{C}^4=V_+\oplus V_-,
\qquad
\dim V_\pm=2,
\qquad
M_4(\mathbb{C})=M_2(V_+)\oplus\operatorname{Hom}(V_-,V_+)\oplus\operatorname{Hom}(V_+,V_-)\oplus M_2(V_-),
$$

with corner dimensions

$$
4+4+4+4=16
$$

and mass block of dimension $2\cdot2=4$.

**Proof.** The same block computation with $3$ replaced by $2$: the corners are $2^2,2\cdot2,2\cdot2,2^2$.

### The $1+1$ Split of the Biquaternion Algebra

For $M_2(\mathbb{C})$ with a root $H_2$ of order two, $\Gamma_2=H_2$ itself, the split is $1+1$, and the corner dimensions are

$$
1+1+1+1=4,
$$

with mass block of dimension $1$. The two chiralities are the two coordinate lines. The two minimal left ideals of $M_2$ are the two columns, each of dimension two, and each column contains one of the lines.

**Proof.** The two eigenspaces are the two coordinate lines; the columns of $M_2$ are the two minimal left ideals, each of dimension two, and each contains one of the lines. In the $1+1$ split the two lines are the two chiral halves.

### The Pattern

**Theorem (the chiral split of $M_{2m}$).** For $M_{2m}(\mathbb{C})$ with a root of order $2m$ and $\Gamma=H^m$, the chiral split is $m+m$, the four corners have dimensions

$$
m^2+m^2+m^2+m^2=4m^2=(2m)^2,
$$

and the mass block has dimension $m^2$.

**Proof.** The same computation with $3$ replaced by $m$.

**Corollary.** The three cases are

| Algebra | $m$ | Split | Mass block | Massless algebra |
|---|---|---|---|---|
| $M_2$ | $1$ | $1+1$ | $1$ | $\mathbb{C}\oplus\mathbb{C}$ |
| $M_4$ | $2$ | $2+2$ | $4$ | $M_2\oplus M_2$ |
| $M_6$ | $3$ | $3+3$ | $9$ | $M_3\oplus M_3$ |

**Remark (the contrast).** In $M_2$ the chiral halves are lines and minimal left ideals; in $M_4$ they are planes and the chiral blocks are $M_2$; in $M_6$ they are three-spaces and the chiral blocks are $M_3$. The mass block grows as $m^2$, and the massless algebra grows as $2m^2$. **The biquaternion case is the case where the chiral half is one-dimensional; it is the exception, not the model.**

## Summary

The chirality involution of a root of order six is $\Gamma=H^3$, with eigenvalues $\pm1$ of multiplicity three each. The carrier splits as $3+3$,

$$
\mathbb{C}^6=V_+\oplus V_-,
\qquad
V_+=V_1\oplus V_3\oplus V_5,\quad
V_-=V_2\oplus V_4\oplus V_6,
$$

and the algebra splits into four $3\times3$ blocks, of dimensions $9+9+9+9=36$. The off-diagonal block $M=A_{+-}$ is the mass block, of dimension $9$.

$$
\boxed{\ \Gamma=H^3,\quad 3+3,\quad \text{mass block }3\times3\text{ of dimension }9 .\ }
$$

The $\mathbb{Z}/6$ grading has six pieces of dimension six; its $\mathbb{Z}/2$ quotient is the chirality, with pieces $A_{\text{even}}\cong M_3\oplus M_3$ and $A_{\text{odd}}$, of dimensions $18+18$; its $\mathbb{Z}/3$ quotient is the opposite-pair grading, with pieces $B_0\cong M_2\oplus M_2\oplus M_2$, $B_1$, $B_2$, of dimensions $12+12+12$. The two quotients are independent and their common refinement is the full grading.

| Object | Data |
|---|---|
| $\Gamma$ | $H^3$, involution, trace $0$ |
| Chiral split | $3+3$ |
| Chiral blocks | $M_3\oplus M_3$, dimension $18$ |
| Mass block | $3\times3$, dimension $9$ |
| $\mathbb{Z}/6$ pieces | $6\times6$ |
| $\mathbb{Z}/2$ pieces | $18+18$ |
| $\mathbb{Z}/3$ pieces | $12+12+12$ |
| $M_4$ contrast | $2+2$, mass block $4$ |
| $M_2$ contrast | $1+1$, mass block $1$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Gamma=H^3$ | the chirality involution |
| $\Pi_\pm=(I_6\pm\Gamma)/2$ | the chiral projectors, of rank $3$ |
| $V_\pm$ | the chiral halves of the carrier |
| $A_{++},A_{--}$ | the two chiral blocks, both $M_3$ |
| $M=A_{+-}$ | the mass block, a $3\times3$ matrix |
| $A_r$ | the $\mathbb{Z}/6$ graded pieces, $\dim A_r=6$ |
| $A_{\text{even}},A_{\text{odd}}$ | the $\mathbb{Z}/2$ pieces, $\dim=18$ |
| $B_0,B_1,B_2$ | the $\mathbb{Z}/3$ pieces, $\dim=12$ |

## Further Reading

- [Roots of Unity and the Lagrange Idempotents](roots-of-unity-and-the-lagrange-idempotents-of-m6c.html), for the root and the chirality involution.
- [The Peirce Decomposition](the-peirce-decomposition-of-m6c.html), for the four corners of an idempotent.
- [The $M_3\oplus M_3$ and $M_2\oplus M_4$ Corners](the-m3-m3-and-m2-m4-corners-of-m6c.html), for the block form and the mass block in the corners.
- [The Mass Block and the Chiral Polar Decomposition](the-mass-block-and-the-chiral-polar-decomposition-of-m6c.html), for the polar decomposition of the mass block.
- [The Spin Chain and the Adjoint Decomposition](the-spin-chain-and-the-adjoint-decomposition-of-m6c.html), for the chain that mixes the two chiralities.
- [The Two Chiralities of $M_4(\mathbb{C})$](the-two-chiralities-of-m4c.html), for the $2+2$ split.
- [The Two Chiralities of the Biquaternion Algebra](the-two-chiralities-of-the-biquaternion-algebra.html), for the $1+1$ split and the minimal left ideals.
- [The Modules and the Minimal Left Ideals](the-modules-and-the-minimal-left-ideals-of-m6c.html), for the columns of $M_6$.
- [Gradings and Filtrations](gradings-and-filtrations.html), for the general theory of group gradings and their quotients.
