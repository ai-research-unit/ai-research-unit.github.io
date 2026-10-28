# __The Mass Block and the Chiral Polar Decomposition of $M_4(\mathbb{C})$__

## Introduction

**The mass block is the four-dimensional space of maps from the right chirality to the left chirality, and its chiral polar decomposition separates a $*$-unitary mixing from two singular values.** The block is

$$
\mathcal{B}=P_+M_4P_-=\operatorname{Hom}(\mathbb{C}^2_-,\mathbb{C}^2_+)\cong M_2(\mathbb{C}),
$$

and an element $M\in\mathcal{B}$ is a **mass operator**

$$
M:\mathbb{C}^2_-\longrightarrow\mathbb{C}^2_+ .
$$

The chiral gauge acts by $M\mapsto U_LMU_R^{-1}$ with $U_L,U_R\in U(2)$. The singular values $\sigma_1,\sigma_2$ are the two invariants of the orbit; the determinant is a phase times their product; the rank counts the massless modes.

The article defines the mass block, proves the singular value and polar decompositions, identifies the invariants and the orbits, explains the determinant phase and the rank, and states why the off-diagonal block is the only coupling of the chiralities. The rank-two split is *The Rank-Two Split of $M_4(\mathbb{C})$*; the chirality is *The Two Chiralities of $M_4(\mathbb{C})$*; the three-parameter gauge is *The Three-Parameter Gauge and the Chiral Polar Decomposition of $M_4(\mathbb{C})$*; the full polar decomposition is *The Polar Decomposition of $M_4(\mathbb{C})$*.

## The Mass Block

**Definition.** The **mass block** is the corner

$$
\mathcal{B}=P_+M_4P_-=\{P_+XP_-:X\in M_4\}.
$$

In the block form of the chirality decomposition,

$$
X=\begin{pmatrix}X_{++}&X_{+-}\\X_{-+}&X_{--}\end{pmatrix},
\qquad
X_{+-}\in\mathcal{B},\quad X_{-+}\in\mathcal{C},
$$

the mass block is the upper-right block. The opposite block $\mathcal{C}=P_-M_4P_+$ is the **conjugate mass block**.

**Proposition.** The mass block is four-dimensional, and it is isomorphic to $\operatorname{Hom}(\mathbb{C}^2_-,\mathbb{C}^2_+)$ and to $M_2(\mathbb{C})$ as a vector space. It is a bimodule: $\mathcal{A}=P_+M_4P_+$ acts on the left and $\mathcal{D}=P_-M_4P_-$ acts on the right:

$$
\mathcal{A}\times\mathcal{B}\longrightarrow\mathcal{B},\qquad
(A,M)\longmapsto AM,
$$

$$
\mathcal{B}\times\mathcal{D}\longrightarrow\mathcal{B},\qquad
(M,D)\longmapsto MD.
$$

**Proof.** In a basis adapted to the chirality decomposition, $\mathcal{B}$ is the upper-right $2\times2$ block. It has four entries. The left action of the upper-left block and the right action of the lower-right block are the ordinary matrix products of $2\times2$ matrices.

**The mass operator.** An element $M\in\mathcal{B}$ is a linear map from the right chirality to the left chirality. It is not an endomorphism of a single space, and it is not an algebra element with a product of its own. It is a block of an algebra element, and its product with the opposite block is an endomorphism of one chirality:

$$
\mathcal{B}\times\mathcal{C}\longrightarrow\mathcal{A},\qquad
(M,N)\longmapsto MN,
$$

$$
\mathcal{C}\times\mathcal{B}\longrightarrow\mathcal{D},\qquad
(N,M)\longmapsto NM.
$$

The products $MN$ and $NM$ are the only places where the two chiralities interact in the multiplication.

## The Chiral Gauge

**Definition.** The **chiral gauge group** is

$$
G_{\mathrm{ch}}=U(2)_L\times U(2)_R,
$$

acting on the mass block by

$$
M\longmapsto U_LMU_R^{-1}=U_LMU_R^{*}.
$$

The first factor acts on the target chirality, the second on the source.

**Proposition.** The action is well defined and preserves the block. The determinant transforms by

$$
\det(U_LMU_R^{*})=\det U_L\det M\det U_R^{-1},
$$

and the adjoint $M^*$ transforms by

$$
(U_LMU_R^{*})^*=U_RM^*U_L^{*}.
$$

**Proof.** The determinant is multiplicative, and $\det U_R^{-1}=(\det U_R)^{-1}$. The adjoint reverses the order: $(U_LMU_R^*)^*=U_RM^*U_L^*$.

**The compact gauge and the complex gauge.** The group $G_{\mathrm{ch}}$ is compact. Its complexification is $GL(2)_L\times GL(2)_R$, acting by $M\mapsto SM T^{-1}$ with $S,T\in GL(2,\mathbb{C})$. The compact orbits are the singular value orbits; the complex orbits are the rank orbits. The two classifications are different, and the article uses both.

## The Singular Value Decomposition

**Theorem (SVD).** Every $M\in\operatorname{Hom}(\mathbb{C}^2_-,\mathbb{C}^2_+)$ has a decomposition

$$
M=U\Sigma V^*,
$$

where

$$
U\in U(\mathbb{C}^2_+),\qquad V\in U(\mathbb{C}^2_-),\qquad
\Sigma=\operatorname{diag}(\sigma_1,\sigma_2):\mathbb{C}^2_-\to\mathbb{C}^2_+,
$$

with

$$
\sigma_1\ge\sigma_2\ge0.
$$

The numbers $\sigma_1,\sigma_2$ are the **singular values** of $M$. They are uniquely determined by $M$, and they are the non-negative square roots of the eigenvalues of $M^*M$.

**Proof.** The operator $M^*M$ is positive semidefinite on $\mathbb{C}^2_-$. By the spectral theorem it has an orthonormal eigenbasis $v_1,v_2$ with eigenvalues $\sigma_1^2\ge\sigma_2^2\ge0$. Set $V=(v_1,v_2)$ and $\Sigma=\operatorname{diag}(\sigma_1,\sigma_2)$. For $\sigma_k>0$, set $u_k=Mv_k/\sigma_k$; the vectors $u_k$ are orthonormal because

$$
\langle u_j,u_k\rangle=\frac{\langle Mv_j,Mv_k\rangle}{\sigma_j\sigma_k}
=\frac{\langle v_j,M^*Mv_k\rangle}{\sigma_j\sigma_k}
=\delta_{jk}.
$$

Extend the $u_k$ with $\sigma_k>0$ to an orthonormal basis of $\mathbb{C}^2_+$, and let $U$ be the corresponding $*$-unitary. Then $Mv_k=\sigma_ku_k$ for every $k$, so $M=U\Sigma V^*$. The uniqueness of the singular values is the uniqueness of the eigenvalues of $M^*M$.

**The polar decomposition.** The SVD gives the **chiral polar decomposition**

$$
M=WP,\qquad
W=UV^*:\mathbb{C}^2_-\to\mathbb{C}^2_+,\qquad
P=V\Sigma V^*:\mathbb{C}^2_-\to\mathbb{C}^2_- .
$$

The factor $W$ is $*$-unitary (an isometry between the two chiral planes), and $P$ is positive semidefinite. Equivalently,

$$
M=U\Sigma V^*=(UV^*)(V\Sigma V^*).
$$

The factor $P=|M|=\sqrt{M^*M}$ is the **mass modulus**, and $W$ is the **chiral phase**. The decomposition is unique when $M$ is invertible; when $M$ is singular, $W$ is not unique on the kernel of $M$, and $P$ is unique.

**The matrices.** For

$$
M=\begin{pmatrix}3&0\\0&2\end{pmatrix},
$$

the singular values are $3,2$, and $M=WP$ with $W=I$, $P=\operatorname{diag}(3,2)$. For

$$
M=\begin{pmatrix}0&3\\2&0\end{pmatrix},
$$

the singular values are $3,2$ and

$$
M=\begin{pmatrix}1&0\\0&1\end{pmatrix}
\begin{pmatrix}3&0\\0&2\end{pmatrix}
\begin{pmatrix}0&1\\1&0\end{pmatrix},
$$

so $U=I$, $\Sigma=\operatorname{diag}(3,2)$, $V=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, and $W=UV^*=\begin{pmatrix}0&1\\1&0\end{pmatrix}$. For

$$
M=\begin{pmatrix}1&1\\0&1\end{pmatrix},
$$

the singular values are

$$
\sigma_1=\frac{1+\sqrt5}{2}=\varphi,\qquad
\sigma_2=\frac{\sqrt5-1}{2}=\frac1\varphi,
$$

the golden ratio and its inverse. The singular values are the positive square roots of the eigenvalues $(3\pm\sqrt5)/2$ of $M^*M$.

## The Determinant, the Phase and the Rank

**The determinant.** For $M=U\Sigma V^*$,

$$
\det M=\det U\det\Sigma\det V^*
=e^{i(\theta_U-\theta_V)}\sigma_1\sigma_2,
$$

where $e^{i\theta_U}=\det U$ and $e^{i\theta_V}=\det V$. The modulus of the determinant is the product of the singular values:

$$
\lvert\det M\rvert=\sigma_1\sigma_2 .
$$

The argument is the **chiral phase** $\theta_U-\theta_V$. Under the chiral gauge,

$$
\det(U_LMU_R^*)=e^{i(\theta_L-\theta_R)}e^{i(\theta_U-\theta_V)}\sigma_1\sigma_2,
$$

so the phase shifts by the determinant phases of the gauge; the modulus $\sigma_1\sigma_2$ is invariant.

**The special unitary gauge.** Under $SU(2)_L\times SU(2)_R$, the determinant phases of the gauge are $1$, so $\det M$ is invariant. Its modulus is $\sigma_1\sigma_2$, and its phase is the chiral phase, an invariant of $M$ itself, not a gauge artefact. Under the full $U(2)_L\times U(2)_R$, only the modulus is invariant; the phase can be removed by the two determinant factors.

**The rank and the masslessness.** The rank of $M$ is the number of nonzero singular values:

$$
\operatorname{rank}M=
\begin{cases}
2,& \sigma_2>0,\\
1,& \sigma_1>0=\sigma_2,\\
0,& M=0.
\end{cases}
$$

The rank is **the masslessness**: rank $2$ is the generic massive case, rank $1$ has one massless mode, and rank $0$ is fully massless. The rank is invariant under the complex gauge and under the compact gauge. The set

$$
\{M:\det M=0\}=\{M:\operatorname{rank}M\le1\}
$$

is the **massless locus**, a complex hypersurface of complex dimension $3$ in the four-dimensional mass block, with real codimension $2$. Its complement, the rank-two locus, is open and dense.

**The orbits.** The compact gauge orbits are classified by the unordered pair $\{\sigma_1,\sigma_2\}$ of singular values. The complex gauge orbits are classified by the rank. The two classifications fit together: the complex orbit of rank $r$ contains the compact orbits with exactly $r$ positive singular values.

## The Only Coupling of the Chiralities

**The block-diagonal part preserves the chiralities.** An element of $\mathcal{A}\oplus\mathcal{D}$ is block-diagonal. It maps each chirality to itself:

$$
\begin{pmatrix}A&0\\0&D\end{pmatrix}
\begin{pmatrix}v_+\\v_-\end{pmatrix}
=
\begin{pmatrix}Av_+\\Dv_-\end{pmatrix}.
$$

The two chiralities do not mix.

**The off-diagonal part is the coupling.** The only entries that map one chirality to the other are the mass blocks $\mathcal{B}$ and $\mathcal{C}$:

$$
\begin{pmatrix}0&M\\N&0\end{pmatrix}
\begin{pmatrix}v_+\\v_-\end{pmatrix}
=
\begin{pmatrix}Mv_-\\Nv_+\end{pmatrix}.
$$

Without $\mathcal{B}$ and $\mathcal{C}$, the algebra would be the direct sum $\mathcal{A}\oplus\mathcal{D}$ and the chiralities would be independent. The off-diagonal blocks are the only coupling of the chiralities in the multiplication of the algebra, and the mass operator $M$ is the coupling from right to left. The product $MN\in\mathcal{A}$ and $NM\in\mathcal{D}$ are the two ways the coupling returns to the diagonal.

**The mass block is not an ideal.** The mass block is a bimodule, not a two-sided ideal. The products $\mathcal{B}\mathcal{C}$ and $\mathcal{C}\mathcal{B}$ land in the diagonal, and the algebra generated by $\mathcal{B}$ and $\mathcal{C}$ together with the diagonal is the whole algebra. The block is a corner, not a summand.

## The Biquaternion Case and the Comparison

**At $n=2$ the mass block is a line.** For $M_2(\mathbb{C})$, the chirality is the root $H=\operatorname{diag}(1,-1)$, and the mass block is

$$
\mathcal{B}=P_+M_2P_-=\mathbb{C}E_{12},
$$

of dimension $1$. A mass operator is a complex scalar $z$, and its polar decomposition is

$$
z=e^{i\theta}\lvert z\rvert .
$$

There is one singular value $\lvert z\rvert$, one phase $e^{i\theta}$, and the rank is $1$ for $z\ne0$ and $0$ for $z=0$. The two singular values of the four-dimensional mass block degenerate to one modulus; the chiral phase is the only phase. The comparison with the three-parameter gauge of the $M_4$ frame is *The Three-Parameter Gauge and the Chiral Polar Decomposition of $M_4(\mathbb{C})$*.

**The general pattern.** For $M_{2m}(\mathbb{C})$ with the chirality split into two $m$-dimensional planes, the mass block is $M_m(\mathbb{C})$, and its chiral polar decomposition has $m$ singular values. For $m=1$ there is one modulus; for $m=2$ there are two; for $m=3$ there are three. The two singular values of the $M_4$ mass block are the first nontrivial case.

## Summary

The mass block $\mathcal{B}=P_+M_4P_-\cong\operatorname{Hom}(\mathbb{C}^2_-,\mathbb{C}^2_+)\cong M_2(\mathbb{C})$ is the four-dimensional space of maps from the right chirality to the left. The chiral gauge $U(2)_L\times U(2)_R$ acts by $M\mapsto U_LMU_R^*$. Every $M$ has a singular value decomposition $M=U\Sigma V^*$ with two singular values $\sigma_1\ge\sigma_2\ge0$, and a chiral polar decomposition $M=WP$ with $W=UV^*$ $*$-unitary and $P=V\Sigma V^*$ positive semidefinite. The determinant is $e^{i(\theta_U-\theta_V)}\sigma_1\sigma_2$; its modulus is the product of the singular values, and its phase is the chiral phase. The rank counts the massless modes: rank $2$ is massive, rank $1$ has one massless mode, rank $0$ is fully massless. The massless locus is a complex hypersurface of dimension $3$ and real codimension $2$. The off-diagonal block is the only coupling of the chiralities; the diagonal part preserves them. At $n=2$ the mass block is a line and the polar decomposition is the polar form of a complex scalar.

$$
\boxed{\ M=U\Sigma V^*,\quad \sigma_1\ge\sigma_2\ge0,\quad \lvert\det M\rvert=\sigma_1\sigma_2,\quad \operatorname{rank}M\in\{0,1,2\},\quad \dim_\mathbb{C}\mathcal{B}=4.\ }
$$

| Object | Dimension or value |
|---|---|
| Mass block $\mathcal{B}$ | $4$ complex |
| Mass operator $M$ | $2\times2$ |
| Singular values | $2$ |
| Chiral gauge $U(2)\times U(2)$ | $4+4=8$ real |
| Massive locus (rank $2$) | open dense |
| Massless locus (rank $\le1$) | $3$ complex |
| Fully massless (rank $0$) | $0$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{B}=P_+M_4P_-$ | the mass block |
| $\mathcal{C}=P_-M_4P_+$ | the conjugate mass block |
| $M:\mathbb{C}^2_-\to\mathbb{C}^2_+$ | a mass operator |
| $U_L,U_R$ | the chiral gauge unitaries |
| $\sigma_1,\sigma_2$ | the singular values |
| $W=UV^*$ | the chiral phase, a $*$-unitary between the planes |
| $P=V\Sigma V^*$ | the mass modulus, positive on $\mathbb{C}^2_-$ |
| $\theta_U,\theta_V$ | the determinant phases of $U,V$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the singular value decomposition, the polar decomposition and the determinant.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the variational characterization of singular values and the operator norms.
- [The Rank-Two Split of $M_4(\mathbb{C})$](the-rank-two-split-of-m4c.html), for the corners and the mass block.
- [The Two Chiralities of $M_4(\mathbb{C})$](the-two-chiralities-of-m4c.html), for the chirality decomposition and the chiral blocks.
- [The Three-Parameter Gauge and the Chiral Polar Decomposition of $M_4(\mathbb{C})$](the-three-parameter-gauge-and-the-chiral-polar-decomposition-of-m4c.html), for the gauge and the scalar case.
- [The Polar Decomposition of $M_4(\mathbb{C})$](the-polar-decomposition-of-m4c.html), for the full $U(4)$ polar decomposition.
- [The Forms, the Norms and the Singular Set of $M_4(\mathbb{C})$](the-forms-the-norms-and-the-singular-set-of-m4c.html), for the norm and the determinant.
