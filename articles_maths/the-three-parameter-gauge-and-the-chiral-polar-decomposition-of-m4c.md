# __The Three-Parameter Gauge and the Chiral Polar Decomposition__

## Introduction

**The frame carries a three-parameter complex torus, one parameter per simple nilpotent, and the mass block carries a chiral polar decomposition with two singular values; the two are different structures.** The gauge is a complex rescaling of the frame; the polar decomposition is a factorization over the compact unitary group. The gauge has three complex parameters; the polar decomposition of the mass block has two real singular values and one phase. The article compares them and records the degeneration at $n=2$, where the gauge has a single parameter $\lambda$.

The article recalls the three-parameter gauge and its action on the mass block, proves the blockwise polar decomposition of a block-diagonal element and the antidiagonal case, states the general $U(4)$ polar factor, and compares the chiral polar decomposition with the single $\lambda$ of the biquaternion algebra.

The frame and the gauge are *The Frame, the Simple Nilpotents and the Gauge*; the mass block is *The Mass Block and the Chiral Polar Decomposition*; the full polar decomposition is *The Polar Decomposition*; the exponential form is *The Exponential Polar Decomposition*.

## The Three-Parameter Gauge

**The gauge torus.** Fix a frame $(v_1,v_2,v_3,v_4)$ and the matrix units

$$
E_{ij}=v_iv_j^{\vee}.
$$

The **gauge group** is the torus

$$
T=(\mathbb{C}^\times)^4/\mathbb{C}^\times\cong(\mathbb{C}^\times)^3,
$$

acting by

$$
v_i\longmapsto t_iv_i,\qquad
v_j^{\vee}\longmapsto t_j^{-1}v_j^{\vee},
$$

so that

$$
E_{ij}\longmapsto\frac{t_i}{t_j}E_{ij}.
$$

The overall scalar is divided out because it acts trivially on every $E_{ij}$.

**One parameter per simple nilpotent.** Write

$$
\lambda_1=\frac{t_1}{t_2},\qquad
\lambda_2=\frac{t_2}{t_3},\qquad
\lambda_3=\frac{t_3}{t_4}.
$$

Then

$$
E_{12}\longmapsto\lambda_1E_{12},\qquad
E_{23}\longmapsto\lambda_2E_{23},\qquad
E_{34}\longmapsto\lambda_3E_{34}.
$$

The parameters $\lambda_1,\lambda_2,\lambda_3$ are independent and coordinatise the torus. There are three, one per simple nilpotent, not four: the fourth ratio $t_4/t_1$ is the inverse of the product $\lambda_1\lambda_2\lambda_3$.

**The composites are fixed by the cocycle.** The composite units transform by the products:

$$
E_{13}=E_{12}E_{23}\longmapsto\lambda_1\lambda_2E_{13},
$$

$$
E_{24}=E_{23}E_{34}\longmapsto\lambda_2\lambda_3E_{24},
$$

$$
E_{14}=E_{12}E_{23}E_{34}\longmapsto\lambda_1\lambda_2\lambda_3E_{14}.
$$

The weights of the composites are determined by the weights of the simple nilpotents and the product rule. There is no fourth independent scalar: the product $\lambda_1\lambda_2\lambda_3$ is not a new parameter, it is the weight of the top composite. The cocycle condition

$$
\lambda_1\lambda_2\lambda_3\cdot\lambda_3^{-1}\lambda_2^{-1}\lambda_1^{-1}=1
$$

is the statement that the product around the cycle is trivial.

**The count.** The root has $12$ complex parameters and the gauge has $3$, for

$$
12+3=15=\dim_\mathbb{C}PGL_4.
$$

The gauge is the fibre of the frame bundle over the root; the three parameters are the rescalings of the frame that leave the root's spectral data unchanged. The count is the orbit–stabiliser count of *The Adjoint Action, the Orbits and the Flag Variety*.

## The Gauge on the Mass Block

**The mass block in the frame basis.** The mass block is

$$
\mathcal{B}=P_+M_4P_-=\operatorname{span}\{E_{12},E_{14},E_{32},E_{34}\},
$$

with the ordered basis $(E_{12},E_{14},E_{32},E_{34})$. A mass operator is

$$
M=aE_{12}+bE_{14}+cE_{32}+dE_{34}
=\begin{pmatrix}a&b\\c&d\end{pmatrix},
$$

where the rows are the chirality $+$ indices $1,3$ and the columns are the chirality $-$ indices $2,4$.

**Proposition.** Under the gauge,

$$
E_{12}\longmapsto\lambda_1E_{12},\qquad
E_{14}\longmapsto\lambda_1\lambda_2\lambda_3E_{14},
$$

$$
E_{32}\longmapsto\lambda_2^{-1}E_{32},\qquad
E_{34}\longmapsto\lambda_3E_{34}.
$$

Equivalently,

$$
\begin{pmatrix}a&b\\c&d\end{pmatrix}
\longmapsto
\begin{pmatrix}
\lambda_1a&\lambda_1\lambda_2\lambda_3b\\
\lambda_2^{-1}c&\lambda_3d
\end{pmatrix}
=
\begin{pmatrix}\lambda_1&0\\0&\lambda_2^{-1}\end{pmatrix}
\begin{pmatrix}a&b\\c&d\end{pmatrix}
\begin{pmatrix}1&0\\0&\lambda_2\lambda_3\end{pmatrix}.
$$

The action is $M\mapsto D_+MD_-^{-1}$ with $D_+=\operatorname{diag}(\lambda_1,\lambda_2^{-1})$ and $D_-=\operatorname{diag}(1,(\lambda_2\lambda_3)^{-1})$; the determinant product $\det D_+\det D_-^{-1}$ is $\lambda_1\lambda_3$.

**Proof.** The weights are the ratios $t_i/t_j$ for $i\in\{1,3\}$ and $j\in\{2,4\}$, expressed through $\lambda_1=t_1/t_2$, $\lambda_2=t_2/t_3$, $\lambda_3=t_3/t_4$. The matrix form is the entrywise computation.

**The determinant weight.** The determinant of the mass matrix is $ad-bc$. The two terms have the same weight:

$$
ad\longmapsto\lambda_1\lambda_3\,ad,\qquad
bc\longmapsto\lambda_1\lambda_2\lambda_3\cdot\lambda_2^{-1}\,bc=\lambda_1\lambda_3\,bc.
$$

Hence

$$
\det M\longmapsto\lambda_1\lambda_3\det M.
$$

The weight of the determinant is $\lambda_1\lambda_3$, not the product $\lambda_1\lambda_2\lambda_3$ of all three. The middle parameter $\lambda_2$ cancels between the two terms. This is the mass-block form of the cocycle.

**The gauge is complex, not unitary.** The parameters $\lambda_k$ are nonzero complex numbers. The gauge changes the singular values of $M$: for a diagonal mass matrix the two singular values are multiplied by $\lvert\lambda_1\rvert$ and $\lvert\lambda_3\rvert$. The compact subgroup

$$
U(1)^3=\{(\lambda_1,\lambda_2,\lambda_3):\lvert\lambda_k\rvert=1\}
$$

preserves the singular values and only changes the phases. The full compact chiral group $U(2)_L\times U(2)_R$ is larger; the three-parameter torus is its diagonal subgroup, and the polar decomposition is adapted to the full compact group, not to the complex torus.

## The Blockwise Polar Decomposition

**The block-diagonal case.** Let

$$
A=\begin{pmatrix}A_+&0\\0&A_-\end{pmatrix}
$$

be block-diagonal, with $A_+\in M_2(\mathbb{C})$ on the chirality $+$ and $A_-\in M_2(\mathbb{C})$ on the chirality $-$. The polar decompositions of the two blocks are

$$
A_+=U_+P_+,\qquad A_-=U_-P_-,
$$

with $U_\pm\in U(2)$ and $P_\pm$ positive semidefinite. Then

$$
A=UP,\qquad
U=\begin{pmatrix}U_+&0\\0&U_-\end{pmatrix}\in U(2)\times U(2),
\qquad
P=\begin{pmatrix}P_+&0\\0&P_-\end{pmatrix}.
$$

The polar factor is block-diagonal, and the singular values of $A$ are the four singular values of $A_+$ and $A_-$, two from each block. The chiralities decouple: the polar decomposition is the direct sum of the two chiral polar decompositions.

**The antidiagonal case.** Let

$$
A=\begin{pmatrix}0&M\\N&0\end{pmatrix},
\qquad
M:\mathbb{C}^2_-\to\mathbb{C}^2_+,\quad
N:\mathbb{C}^2_+\to\mathbb{C}^2_- .
$$

Then

$$
A^*A=\begin{pmatrix}N^*N&0\\0&M^*M\end{pmatrix},
$$

so the positive factor is

$$
P=\begin{pmatrix}\lvert N\rvert&0\\0&\lvert M\rvert\end{pmatrix},
\qquad
\lvert N\rvert=\sqrt{N^*N},\quad
\lvert M\rvert=\sqrt{M^*M}.
$$

On the invertible blocks, the polar factor is

$$
U=AP^{-1}=
\begin{pmatrix}
0&M\lvert M\rvert^{-1}\\
N\lvert N\rvert^{-1}&0
\end{pmatrix}.
$$

The blocks $M\lvert M\rvert^{-1}$ and $N\lvert N\rvert^{-1}$ are the unitary chiral phases of $M$ and $N$. The full polar decomposition of an antidiagonal matrix is the direct sum of the two chiral polar decompositions, one for each off-diagonal block.

**The general case.** For a general block matrix

$$
A=\begin{pmatrix}A_+&M\\N&A_-\end{pmatrix},
$$

the polar factor $U=A(A^*A)^{-1/2}$ is not block-diagonal and not block-antidiagonal. It mixes the chiralities, and the blockwise decomposition is only the special case in which $M=N=0$. The general $U(4)$ polar factor is the subject of the next section.

## The General Element and the $U(4)$ Polar Factor

**Theorem.** Every $A\in M_4(\mathbb{C})$ has a polar decomposition

$$
A=UP,
$$

with $U\in U(4)$ and $P$ positive semidefinite. If $A$ is invertible, the decomposition is unique, with

$$
P=(A^*A)^{1/2},\qquad U=A(A^*A)^{-1/2}.
$$

If $A$ is singular, $P$ is unique and $U$ is unique on the range of $P$ and arbitrary on its kernel.

**Proof.** The operator $A^*A$ is positive semidefinite, so it has a unique positive semidefinite square root $P$. On the range of $P$, define $U(Pv)=Av$; this is well defined and isometric because

$$
\lVert Av\rVert^2=\langle Av,Av\rangle=\langle v,A^*Av\rangle=\langle v,P^2v\rangle=\lVert Pv\rVert^2.
$$

Extend $U$ isometrically from the range of $P$ to its orthogonal complement, which is the kernel of $P$, with values in the kernel of $A^*$. The dimensions agree, because $\operatorname{rank}P=\operatorname{rank}A$, so the extension exists and $U$ is unitary. Then $A=UP$. Uniqueness on the invertible elements follows because $P$ is determined by $A^*A$ and $U=AP^{-1}$.

**The chiral polar decomposition is different.** The decomposition $M=U\Sigma V^*$ of the mass block uses two unitaries, one on each chirality, and a diagonal map between them. It is the polar decomposition of a map between two different Hilbert spaces, not of an endomorphism of one space. The full $U(4)$ polar factor of the block matrix is an endomorphism of $\mathbb{C}^4$; it mixes the chiralities in general, and it is not the pair $(U_L,U_R)$ of the mass block.

**The relation.** For the antidiagonal block matrix $A=\begin{pmatrix}0&M\\N&0\end{pmatrix}$, the two decompositions agree: the $U(4)$ polar factor is the block-antidiagonal matrix built from the chiral phases of $M$ and $N$, and the positive factor is the block-diagonal matrix of the two mass moduli. For a general block matrix, the two decompositions are different.

## The Chiral Polar Decomposition of the Mass Block

**The decomposition.** Every $M\in\mathcal{B}$ has

$$
M=U\Sigma V^*,
\qquad
U\in U(2)_L,\quad V\in U(2)_R,\quad
\Sigma=\operatorname{diag}(\sigma_1,\sigma_2),
$$

with $\sigma_1\ge\sigma_2\ge0$. The **chiral polar decomposition** is

$$
M=WP,\qquad
W=UV^*:\mathbb{C}^2_-\to\mathbb{C}^2_+,\quad
P=V\Sigma V^*:\mathbb{C}^2_-\to\mathbb{C}^2_- .
$$

The factor $W$ is the unitary phase, and $P$ is the mass modulus. The two singular values $\sigma_1,\sigma_2$ are the invariants of the compact chiral gauge; the phase of $\det M$ is the remaining invariant under the special unitary gauge.

**The gauge weights of the polar data.** Under the three-parameter gauge, the mass block transforms by $M\mapsto D_+MD_-^{-1}$ with $D_+=\operatorname{diag}(\lambda_1,\lambda_2^{-1})$ and $D_-=\operatorname{diag}(1,(\lambda_2\lambda_3)^{-1})$. The singular values are invariant exactly when the gauge lies in the compact subgroup $U(1)^3$, that is, when $\lvert\lambda_1\rvert=\lvert\lambda_2\rvert=\lvert\lambda_3\rvert=1$; a complex rescaling changes the moduli. The determinant transforms by $\lambda_1\lambda_3$. The chiral phase transforms by the phase of $\lambda_1\lambda_3$. The two singular values and the phase are therefore **not** the three gauge parameters: the gauge is complex, and it changes the moduli.

**The invariant count.** The mass block has complex dimension $4$, hence real dimension $8$. The three-parameter gauge has complex dimension $3$, hence real dimension $6$. The quotient has real dimension $2$. On the generic rank-two locus the quotient is parametrised by one complex invariant, the cross ratio $ad/(bc)$ of the four entries; as two real invariants, it is the modulus and the argument of the cross ratio. The two singular values are two real invariants of the **compact** gauge, but they are not invariant under the complex gauge; the quotient invariants are the combinations that survive the complex rescalings. The phase of $\det M$ is not a quotient invariant.

## The Single $\lambda$ of $\mathbb{B}$

**At $n=2$ the gauge is one-dimensional.** The biquaternion algebra is $\mathbb{B}=M_2(\mathbb{C})$. The frame is $(v_1,v_2)$, the gauge is

$$
T=(\mathbb{C}^\times)^2/\mathbb{C}^\times\cong\mathbb{C}^\times,
\qquad
\lambda=\frac{t_1}{t_2},
$$

and the only simple nilpotent is $E_{12}$, with

$$
E_{12}\longmapsto\lambda E_{12}.
$$

The mass block is the line $\mathbb{C}E_{12}$, and the mass operator is a complex scalar $z$. The gauge acts by

$$
z\longmapsto\lambda z.
$$

**The polar decomposition of the scalar.** The polar decomposition is

$$
z=e^{i\theta}\lvert z\rvert .
$$

The modulus $\lvert z\rvert$ is invariant under the compact gauge $U(1)\times U(1)$, and the phase $e^{i\theta}$ is removed by the compact gauge. The complex gauge $\lambda\in\mathbb{C}^\times$ is transitive on the nonzero masses: for $z\ne0$, choose $\lambda=1/z$ to send $z$ to $1$. The only invariant of the complex gauge is whether $z$ is zero.

**The comparison.** In $\mathbb{B}$ the gauge has one complex parameter $\lambda$, the mass block has one complex entry $z$, and the gauge is transitive on the nonzero locus. The polar decomposition has one modulus and one phase; the modulus is the compact invariant, and the phase is a gauge artefact. In $M_4$ the gauge has three complex parameters $\lambda_1,\lambda_2,\lambda_3$, the mass block has four complex entries, and the gauge is not transitive: its orbits have complex dimension $3$ and the quotient has complex dimension $1$. The polar decomposition has two singular values and one phase; the two singular values are compact invariants, and the phase is a compact artefact. The coincidence of counts at $n=2$ — one complex gauge parameter, one complex mass — does not persist: at $n=4$ the three gauge parameters are not the two singular values plus the phase.

**The single $\lambda$ is the degeneration.** The three parameters $\lambda_1,\lambda_2,\lambda_3$ degenerate to the single $\lambda$ when the chain has one step. The mass block degenerates from a $2\times2$ matrix to a scalar. The polar decomposition degenerates from two singular values to one modulus. The pattern is the $m=1$ case of the general $M_{2m}$:

$$
\underbrace{2m-1}_{\text{gauge}}\ \text{complex parameters},\qquad
\underbrace{m}_{\text{singular values}}\ \text{real invariants},\qquad
\underbrace{1}_{\text{phase}}\ \text{compact phase}.
$$

For $m=1$: one gauge parameter, one singular value, one phase. For $m=2$: three gauge parameters, two singular values, one phase.

## Summary

The frame carries the three-parameter complex torus $(\mathbb{C}^\times)^3$, one parameter $\lambda_k$ per simple nilpotent $E_{k,k+1}$. The mass block $\mathcal{B}$ is spanned by $E_{12},E_{14},E_{32},E_{34}$ with gauge weights $\lambda_1,\lambda_1\lambda_2\lambda_3,\lambda_2^{-1},\lambda_3$; the determinant has weight $\lambda_1\lambda_3$. The blockwise polar decomposition of a block-diagonal element is the direct sum of the two chiral polar decompositions; the antidiagonal case reduces to the chiral phases and moduli of the two off-diagonal blocks; the general element has a $U(4)$ polar factor that mixes the chiralities. The mass block has the chiral polar decomposition $M=U\Sigma V^*=WP$, with two singular values and a chiral phase. The three complex gauge parameters are not the two real singular values and the phase: the gauge quotient of the mass block has complex dimension one, while the polar data have three real parameters. At $n=2$ the gauge has a single $\lambda$, the mass block is a line, and the polar decomposition is the polar form of a scalar; the coincidence of counts is the degeneration of the three-parameter case.

$$
\boxed{\ T=(\mathbb{C}^\times)^3,\quad \det M\mapsto\lambda_1\lambda_3\det M,\quad M=U\Sigma V^*,\quad \sigma_1\ge\sigma_2\ge0,\quad \dim_\mathbb{C}\mathcal{B}=4. }
$$

| Object | Complex dimension | Real dimension |
|---|---|---|
| Gauge torus $T$ | $3$ | $6$ |
| Mass block $\mathcal{B}$ | $4$ | $8$ |
| Gauge orbit (generic) | $3$ | $6$ |
| Gauge quotient (generic) | $1$ | $2$ |
| Chiral polar data | — | $2$ singular values $+1$ phase |
| Biquaternion gauge | $1$ | $2$ |
| Biquaternion mass block | $1$ | $2$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lambda_1,\lambda_2,\lambda_3$ | the gauge parameters of the simple nilpotents |
| $T=(\mathbb{C}^\times)^3$ | the gauge torus |
| $D_+=\operatorname{diag}(\lambda_1,\lambda_2^{-1})$ | the left gauge matrix on the mass block |
| $D_-=\operatorname{diag}(1,(\lambda_2\lambda_3)^{-1})$ | the right gauge matrix, entering as $D_-^{-1}$ |
| $M=U\Sigma V^*$ | the chiral singular value decomposition |
| $W=UV^*$ | the chiral phase |
| $P=V\Sigma V^*$ | the mass modulus |
| $\lambda$ | the single gauge parameter of $\mathbb{B}$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the polar decomposition, the singular value decomposition and the unitary group.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for $U(4)$, $U(2)\times U(2)$ and the exponential.
- [The Frame, the Simple Nilpotents and the Gauge](the-frame-the-simple-nilpotents-and-the-gauge-of-m4c.html), for the torus and the cocycle.
- [The Mass Block and the Chiral Polar Decomposition](the-mass-block-and-the-chiral-polar-decomposition-of-m4c.html), for the mass block and its polar decomposition.
- [The Polar Decomposition](the-polar-decomposition-of-m4c.html), for the full $U(4)$ decomposition.
- [The Exponential Polar Decomposition](the-exponential-polar-decomposition-of-m4c.html), for the exponential form.
- [The Frame, the Simple Nilpotents and the Gauge](the-frame-the-simple-nilpotents-and-the-gauge.html), for the biquaternion case.
