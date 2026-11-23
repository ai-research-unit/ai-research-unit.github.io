# __Introduction to the Operators on the Four Sectors in $M_2(\mathbb{C})$__

## Introduction

**The question.** Three operators carry the polar word on the algebra: the left multiplication $L_A$, the right multiplication $R_A$, and the two-sided operator $\mathrm{Sd}_A=L_AR_{A^{\dagger}}$. This article states what the three have in common — their arrays, their multiplicativity, the doubling rule and the table of the four sectors — and proves nothing about a single sector.

**Why it is the same statement.** This is the in-depth matrix reading of [Introduction to the Operators on the Four Sectors](introduction-to-the-operators-on-the-four-sectors.html). The source works frame-free on $\mathbb{B}$; the display $A=\mathsf M_2(\tilde Q)$ turns every operator into an explicit $4\times4$ array and every sector condition into a condition on $\operatorname{tr}A$ and $\det A$. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The three operators as arrays: $L_A=\mathrm I_2\otimes A$ and $R_A=A^{\mathsf T}\otimes\mathrm I_2$ in the matrix-unit frame, and the coefficient-frame arrays $\sum_\mu Q_\mu M_\mu$ built from three signed-permutation multiplication tables. The three multiplicativity laws with their orders. The two projectors of the trace. The doubling rule: the two-sided operator squares every modulus and kills the central phase. The two sector indices $\det A$ and $B^2=\det A-\tfrac14(\operatorname{tr}A)^2$. The four-sector tables for $L_A$ and for $\mathrm{Sd}_A$.

**What the article does not do.** It does not develop any sector; that is [One-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$](one-sided-operators-on-the-n-regular-sector-in-m2c.html) and its three companions. It does not treat the two-sided operator as a family, which is [The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-m2c.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, so that
$$
A=\begin{pmatrix}Q_t-iQ_z & -iQ_x-Q_y\\ -iQ_x+Q_y & Q_t+iQ_z\end{pmatrix},\qquad
\operatorname{tr}A=2Q_t,\qquad \det A=Q_t^2+Q_x^2+Q_y^2+Q_z^2=N(\tilde Q).
$$
The vector form is $B^2=Q_x^2+Q_y^2+Q_z^2=\det A-\tfrac14(\operatorname{tr}A)^2$, and the discriminant is $\Delta=(\operatorname{tr}A)^2-4\det A=-4B^2$. The matrix adjoint is $A^{\dagger}=\overline{A^{\mathsf T}}$; it is the composite of the natural involution $\natural$ with the conjugation of the coefficients, verified below. Arrays are printed in the coefficient frame $(E_t,E_x,E_y,E_z)=(\mathrm I_2,-i\sigma_1,-i\sigma_2,-i\sigma_3)$ unless the matrix-unit frame is named.

**Boundaries.** The frame-free operator theory is [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html) and [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html). The polar decomposition of a matrix is [The Adjoints and the Polar Decomposition of an Operator at $n=2$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-2.html). The array privilege is [The Axis-Free $4\times4$ Representation : Operators](m4c-axis-free-representation-operators.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $A=\mathsf M_2(\tilde Q)$ is the matrix of the element. $M_\mu$ are the four multiplication tables. $\mathrm{Sd}_A$ is the two-sided operator $Y\mapsto AYA^{\dagger}$. $\Sigma_{\varepsilon\eta}$ are the four sectors. $\lambda_\pm$ are the eigenvalues of $A$.

## The Three Operators as Arrays

**The definitions.** For $Y\in M_2(\mathbb{C})$,
$$
L_A(Y)=AY,\qquad R_A(Y)=YA,\qquad \mathrm{Sd}_A(Y)=AYA^{\dagger}.
$$
All three are $\mathbb{C}$-linear endomorphisms of a space of complex dimension four, hence $4\times4$ arrays.

**The matrix-unit frame.** With the basis ordered $(E_{11},E_{12},E_{21},E_{22})$ and $Y$ read as a column, the two one-sided operators are the Kronecker products
$$
L_A=\mathrm I_2\otimes A,\qquad R_A=A^{\mathsf T}\otimes\mathrm I_2 .
$$
For the displayed $A$ this gives
$$
L_A=\begin{pmatrix}
Q_t-iQ_z & -iQ_x-Q_y & 0 & 0\\
-iQ_x+Q_y & Q_t+iQ_z & 0 & 0\\
0 & 0 & Q_t-iQ_z & -iQ_x-Q_y\\
0 & 0 & -iQ_x+Q_y & Q_t+iQ_z
\end{pmatrix},
$$
verified against the action $Y\mapsto AY$ to $4\cdot10^{-16}$, and $R_A$ is the same array with the two diagonal $2\times2$ blocks exchanged. The two commute, since they act on different tensor slots.

**The coefficient frame.** In the basis $(E_t,E_x,E_y,E_z)$ the same operator is
$$
L_A=Q_tM_t+Q_xM_x+Q_yM_y+Q_zM_z,\qquad M_t=\mathrm I_4,
$$
with rows and columns indexed $t,x,y,z$,
$$
M_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\quad
M_y=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\quad
M_z=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix}.
$$
Every row has one nonzero entry of modulus one, so the three are signed permutation matrices: they are the multiplication table read aloud. The identities $M_x^2=M_y^2=M_z^2=-\mathrm I_4$ and $M_xM_y=M_z$ hold exactly, with residual $0$, and reproduce $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$.

**Why the coefficient array is not the Kronecker array.** The two frames differ by the change of basis from the matrix units to the $E_\mu$, and that change is not a permutation: $E_x=-i\sigma_1$ is not a matrix unit. The Kronecker form is the one that shows the tensor slots; the coefficient form is the one in which $\sum_\mu Q_\mu M_\mu$ is linear in the coefficients with integer structure constants.

**Rank and invertibility.** $L_A$ is invertible exactly when $\det A\neq0$. When $A\neq0$ has $\det A=0$ the rank is $2$; when $A=0$ it is $0$. The trichotomy $4,2,0$ holds for $R_A$ as well, and $\mathrm{Sd}_A$ is invertible exactly when $A$ is.

## Multiplicativity

**The three laws.** For all $A,A'\in M_2(\mathbb{C})$,
$$
L_{AA'}=L_A L_{A'},\qquad R_{AA'}=R_{A'}R_A,\qquad \mathrm{Sd}_{AA'}=\mathrm{Sd}_A\,\mathrm{Sd}_{A'}.
$$
Each is associativity read at one position, and the third uses $(AA')^{\dagger}=A'{}^{\dagger}A^{\dagger}$. Verified on a hundred random pairs, with residuals $1.5\cdot10^{-14}$, $1.6\cdot10^{-14}$ and $2\cdot10^{-13}$.

**The orders.** The left multiplication is a representation, the right multiplication an anti-representation, and the two-sided operator a representation again because the two reversals cancel. In arrays, $L$ acts on the first Kronecker slot and $R$ on the second.

**The image on the invertibles.** $A\mapsto L_A$ is faithful with image $GL(2,\mathbb{C})$, of real dimension eight. $A\mapsto\mathrm{Sd}_A$ kills the central circle: $\mathrm{Sd}_{\omega A}=\mathrm{Sd}_A$ for every $\omega\in\mathbb{C}$ with $|\omega|=1$, because $\omega$ is central and $\omega\omega^{\dagger}=1$. Its image is the conformal group $CO^{+}(1,3)$, of real dimension seven.

**The involution, verified.** The natural involution $\natural$ of the source is the $\mathbb{C}$-linear quaternion conjugation $q\mapsto(Q_t,-Q_x,-Q_y,-Q_z)$, which on the display is $A\mapsto(\operatorname{tr}A)\mathrm I_2-A$. Composed with the conjugation of the coefficients it is the matrix adjoint. On the coefficient vector $q=(Q_t,Q_x,Q_y,Q_z)$ the composite acts by
$$
q\mapsto\left(\bar Q_t,-\bar Q_x,-\bar Q_y,-\bar Q_z\right),
$$
and the display of the resulting vector is the matrix adjoint:
$$
A^{\dagger}=\overline{A^{\mathsf T}}.
$$
Verified on a hundred random elements with residual exactly $0$.

**The trap in the array form.** Entrywise conjugation of the array is not the conjugation of the coefficients, because $\sigma_2$ is imaginary: entrywise conjugation agrees with $A^{\dagger}$ only when $A$ is symmetric, and a random $A$ fails by $O(1)$. The safest reading is on the coefficient vector, where the composite is a signed conjugation.

**The two projectors.** The $\mathbb{C}$-linear quaternion conjugation, without the conjugation of the coefficients, is
$$
A\longmapsto \operatorname{tr}(A)\mathrm I_2-A,
$$
verified to $6\cdot10^{-17}$; equivalently $q\mapsto(Q_t,-Q_x,-Q_y,-Q_z)$. Its two projectors are
$$
P_0(A)=\frac{\operatorname{tr}A}{2}\mathrm I_2,\qquad P_1(A)=A-\frac{\operatorname{tr}A}{2}\mathrm I_2,
$$
with $P_0^2=P_0$, $P_1^2=P_1$, $P_0P_1=0$, $P_0+P_1=\mathrm{id}$. Their images are the centre $\mathbb{C}\mathrm I_2$ and the traceless part $\mathfrak{sl}_2$, of complex dimensions $1$ and $3$. They are canonical, built from the trace alone.

## The Doubling Rule

**The polar word.** Write $A=A_HA_0$ with $A_H$ positive semidefinite Hermitian and $A_0$ a partial isometry. Multiplicativity gives
$$
\mathrm{Sd}_A=\mathrm{Sd}_{A_H}\circ\mathrm{Sd}_{A_0}.
$$
The modulus of the operator is $\lvert\mathrm{Sd}_A\rvert=\mathrm{Sd}_{A_H}$, and the singular values of $\mathrm{Sd}_A$ are the squares of those of $A$.

**The table.**

| element | two-sided operator |
|---|---|
| scale $r$ | $r^2$ |
| singular value $2a$ | $4a^2$ |
| phase $e^{i\theta}$ | $1$ |

**Why the phase cancels.** $A$ and $\omega A$ with $|\omega|=1$ give the same $\mathrm{Sd}$, since $\mathrm{Sd}_{\omega A}(Y)=\omega AY\bar\omega A^{\dagger}=AYA^{\dagger}$.

**The collapse on the singular locus.** When $A$ has rank one, $A=2aA_0$ with $A_0$ a rank-one partial isometry, and
$$
\mathrm{Sd}_A=4a^2\,\mathrm{Sd}_{A_0}.
$$
Two-sided operator, scalar, times a partial isometry of rank one.

## The Four Sectors

**The two indices.** The sectors are indexed by
$$
N=\det A,\qquad B^2=\det A-\tfrac14(\operatorname{tr}A)^2,
$$
so that
$$
\Sigma_{11}=\{\det A\neq0,\ B^2\neq0\},\quad
\Sigma_{10}=\{\det A\neq0,\ B^2=0\},\quad
\Sigma_{01}=\{\det A=0,\ A\neq0,\ B^2\neq0\},\quad
\Sigma_{00}=\{\det A=0,\ A\neq0,\ B^2=0\}.
$$

**The matrix forms.** On $\Sigma_{11}$ the matrix has two distinct eigenvalues $\lambda_\pm=Q_t\pm iB$ and is diagonalizable. On $\Sigma_{10}$ it has the single eigenvalue $Q_t$; it is the scalar $Q_t\mathrm I_2$ exactly on the scalar line, and otherwise similar to $\begin{pmatrix}Q_t&1\\0&Q_t\end{pmatrix}$. On $\Sigma_{01}$ it is a rank-one matrix with eigenvalues $2Q_t$ and $0$. On $\Sigma_{00}$ it is a non-zero nilpotent, $A^2=0$, similar to $\begin{pmatrix}0&1\\0&0\end{pmatrix}$.

**The eigenvalues of the operators.** Because $A$ acts on the left and on the right on two tensor slots,
$$
\operatorname{spec}L_A=\operatorname{spec}R_A=\{\lambda_+,\lambda_+,\lambda_-,\lambda_-\},\qquad
\operatorname{spec}\mathrm{Sd}_A=\{\lambda_i\bar\lambda_j\}.
$$
The four products were computed on random elements of $\Sigma_{11}$ and agree with the spectrum of the array to $10^{-15}$.

**The one-sided table.**

| sector | rank $L_A$ | spectrum | Jordan type | image |
|---|---|---|---|---|
| $\Sigma_{11}$ | $4$ | $\lambda_+,\lambda_-$, each twice | $\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$ | $M_2(\mathbb{C})$ |
| $\Sigma_{10}$, scalar line | $4$ | $Q_t$ four times, geometric $4$ | $Q_t\mathrm I_4$ | $M_2(\mathbb{C})$ |
| $\Sigma_{10}$, Jordan part | $4$ | $Q_t$ four times, geometric $2$ | $J_2(Q_t)\oplus J_2(Q_t)$ | $M_2(\mathbb{C})$ |
| $\Sigma_{01}$ | $2$ | $c,0$ with $c=2Q_t$, multiplicities $2,2$ | $\operatorname{diag}(c,c,0,0)$ | the rank-one ideal $AM_2(\mathbb{C})$ |
| $\Sigma_{00}$ | $2$ | $0$ four times, geometric $2$ | $J_2(0)\oplus J_2(0)$ | $\mathbb{C}A\oplus\mathbb{C}P_+=\ker L_A$ |

**The two image columns.** On $\Sigma_{01}$ the images of $L_A$ and $R_A$ are the distinct rank-one ideals $AM_2(\mathbb{C})$ and $M_2(\mathbb{C})A$, meeting in $\mathbb{C}A$. On $\Sigma_{00}$ they are $\mathbb{C}A\oplus\mathbb{C}P_+$ and $\mathbb{C}A\oplus\mathbb{C}P_-$, where $P_\pm$ are the canonical rank-one projections with $A=P_+AP_-$. On $\Sigma_{11}$ and $\Sigma_{10}$ both images are the whole algebra.

**The two-sided table.**

| sector | rank | spectrum | Jordan type | image |
|---|---|---|---|---|
| $\Sigma_{11}$ | $4$ | $\lambda_i\bar\lambda_j$ | semisimple | $M_2(\mathbb{C})$ |
| $\Sigma_{10}$, scalar line | $4$ | $\lvert Q_t\rvert^2$ four times, geometric $4$ | $\lvert Q_t\rvert^2\mathrm I_4$ | $M_2(\mathbb{C})$ |
| $\Sigma_{10}$, Jordan part | $4$ | $\lvert Q_t\rvert^2$ four times, geometric $2$ | $J_3(\lvert Q_t\rvert^2)\oplus J_1(\lvert Q_t\rvert^2)$ | $M_2(\mathbb{C})$ |
| $\Sigma_{01}$ | $1$ | $\lvert c\rvert^2,0$, multiplicities $1,3$ | $\operatorname{diag}(\lvert c\rvert^2,0,0,0)$ | the line $\mathbb{C}P$, $P=AA^{\dagger}/\operatorname{tr}(AA^{\dagger})$ |
| $\Sigma_{00}$ | $1$ | $0$ four times, geometric $3$ | $J_2(0)\oplus0\oplus0$ | the line $\mathbb{C}P_+$ |

**Reading the two tables.** Along a row the rank drops when $\det A=0$, and the Jordan type leaves the semisimple case when $B^2=0$. Along a column the two-sided operator replaces $\lambda_i$ by $\lambda_i\bar\lambda_j$, so it loses one factor of the spectrum and gains one degree of defect: the block $2+2$ becomes $3+1$, and $J_2(0)\oplus J_2(0)$ becomes $J_2(0)\oplus0\oplus0$.

**The Jordan check.** For $A=\begin{pmatrix}1&2\\0&1\end{pmatrix}$ the ranks of $(\mathrm{Sd}_A-\mathrm I_4)^k$ are $4,2,1,0$, that is nullities $0,2,3,4$, which is $J_3(1)\oplus J_1(1)$. For $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ the ranks of $\mathrm{Sd}_A^k$ are $4,1,0$, which is $J_2(0)\oplus0\oplus0$. For $A=\operatorname{diag}(1,0)$ they are $4,1,1$, a rank-one projection.

## Where $n=2$ Differs

**The size of the operator.** At $n=2$ the arrays are $4\times4$ and the operator algebra is $M_4(\mathbb{C})$, of complex dimension sixteen; there is no larger space, since $\dim_{\mathbb{C}}\mathbb{B}=4$.

**The sector count.** At $n=2$ the two indices $\det A$ and $B^2$ are single complex numbers, so the discriminant $\Delta=-4B^2$ is a single number and there are exactly four sectors. At order $n$ the second index is a form on a space of dimension $n^2-1$ and the sector count is not four.

**The eigenvalue count.** A $2\times2$ matrix has two eigenvalues, so $L_A$ has at most two distinct eigenvalues each of multiplicity two, and $\mathrm{Sd}_A$ at most four distinct ones.

**What does not differ.** The multiplicativity laws, the killing of the central phase and the doubling of the modulus are identities at every order.

## Summary

The three operators are $L_A(Y)=AY$, $R_A(Y)=YA$ and $\mathrm{Sd}_A(Y)=AYA^{\dagger}$, with $\mathrm{Sd}_A=L_AR_{A^{\dagger}}$. In the matrix-unit frame $L_A=\mathrm I_2\otimes A$ and $R_A=A^{\mathsf T}\otimes\mathrm I_2$; in the coefficient frame they are $\sum_\mu Q_\mu M_\mu$ with the signed-permutation tables $M_x,M_y,M_z$ satisfying $M_k^2=-\mathrm I_4$ exactly.

The three are multiplicative, with the order reversed on the right and restored on the two-sided operator, verified to $2\cdot10^{-13}$. The composite of the natural involution with the conjugation of the coefficients is the matrix adjoint $A^{\dagger}$, the display of $q\mapsto(\bar Q_t,-\bar Q_x,-\bar Q_y,-\bar Q_z)$ with residual $0$; entrywise conjugation of the array is a different operation, because $\sigma_2$ is imaginary. The $\mathbb{C}$-linear quaternion conjugation is $A\mapsto\operatorname{tr}(A)\mathrm I_2-A$, whose projectors are the scalar and traceless parts.

The two-sided operator squares the scale and the singular value and kills the central phase. The four sectors are indexed by $\det A$ and $B^2$, with the forms $\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$, $J_2\oplus J_2$, $\operatorname{diag}(c,c,0,0)$ and $J_2(0)\oplus J_2(0)$ for $L_A$, and spectra $\lambda_i\bar\lambda_j$ with the Jordan types $J_3\oplus J_1$ and $J_2\oplus0\oplus0$ for $\mathrm{Sd}_A$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=\mathsf M_2(\tilde Q)$ | the $2\times2$ matrix of the element |
| $L_A,R_A$ | $Y\mapsto AY$ and $Y\mapsto YA$ |
| $\mathrm{Sd}_A$ | $Y\mapsto AYA^{\dagger}$ |
| $M_\mu$ | the four multiplication tables in the coefficient frame |
| $N=\det A$ | the norm |
| $B^2=\det A-\tfrac14(\operatorname{tr}A)^2$ | the vector form |
| $\Delta=-4B^2$ | the discriminant |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues of $A$ |
| $\Sigma_{\varepsilon\eta}$ | the four sectors |
| $P_\pm$ | the canonical rank-one projections of a nilpotent |

## Further Reading

- [Introduction to the Operators on the Four Sectors](introduction-to-the-operators-on-the-four-sectors.html), for the source's frame-free statement of the three operators and the sector index.
- [One-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$](one-sided-operators-on-the-n-regular-sector-in-m2c.html), for the sector $\Sigma_{11}$ and the wall in full.
- [Two-Sided Operators on the N-Degenerate Sector in $M_2(\mathbb{C})$](two-sided-operators-on-the-n-degenerate-sector-in-m2c.html), for the two null sectors and the single Jordan chain.
- [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html), for $L_A$ and $R_A$ with their commutant and their rank trichotomy.
- [The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-m2c.html), for the two-sided operator as a family and its parameter modulo the central phase.
