# __One-Sided Operator Under the Polar Decomposition__

## Introduction

The biquaternion algebra acts on itself by left multiplication and by right multiplication. For a parameter $\tilde Q$ the two **one-sided operators** are

$$
L_{\tilde Q}(\tilde X)=\tilde Q\tilde X,\qquad R_{\tilde Q}(\tilde X)=\tilde X\tilde Q .
$$

The two-sided operator of the polar decomposition is the product of the left action of $\tilde Q$ and the right action of $\tilde Q^{*}$, $\Theta_{\tilde Q}=R_{\tilde Q^{*}}\circ L_{\tilde Q}$, and its theory is *Two-Sided Operator Under the Polar Decomposition*. This article reads the one-sided factors: the polar word

$$
\tilde Q=\Rho\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
=r\exp(i\alpha)\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr)\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr),
\qquad \Rho=r\exp(i\alpha),
$$

with $r>0$, $\alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$, $\psi\ge0$, $\theta\in[0,2\pi]$ and real unit axes $\vec u_{\mathrm b},\vec u_{\mathrm r}$, acting by a single multiplication, on the left or on the right, and the transformation it produces on a biquaternion.

The one-sided operator is $\mathbb{C}$-linear, and the map from the parameter to the operator is faithful. It multiplies the complex norm by $\Rho^{2}$. It does not, in general, preserve the two real forms $\mathbb{M}_+$ and $\mathbb{M}_-$. Its block form in the splitting $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ is

$$
L_{\tilde Q}=
\begin{pmatrix}
D_{\tilde Q} & O_{\tilde Q}\\
O_{\tilde Q} & D_{\tilde Q}
\end{pmatrix},
$$

with the symmetrized and the skew-symmetrized parts

$$
D_{\tilde Q}(\tilde X)=\tfrac12\bigl(\tilde Q\tilde X+\tilde X\tilde Q^{*}\bigr),\qquad
O_{\tilde Q}(\tilde X)=\tfrac12\bigl(\tilde Q\tilde X-\tilde X\tilde Q^{*}\bigr).
$$

The diagonal block $D_{\tilde Q}$ preserves each sector and the off-diagonal block $O_{\tilde Q}$ carries each sector into the other. For a central factor $c$ the two blocks are the scalars $\operatorname{Re}(c)$ and $i\operatorname{Im}(c)$.

The clearest case is the pure central phase of $\pi/2$. The factor is $i$, or $-i$, and the operator is

$$
L_i(\tilde X)=i\tilde X,\qquad i\mathbb{M}_-=\mathbb{M}_+,\qquad i\mathbb{M}_+=\mathbb{M}_- .
$$

It is multiplication by the central imaginary, the complex structure $J$ of the algebra read over $\mathbb{R}$. It satisfies $J^{2}=-\mathrm{id}$ and $J^{-1}=J^{3}=L_{-i}$. The sign $i$ or $-i$ is the direction of the exchange. This is the operator that the two-sided sandwich cancels: $\Theta_i(\tilde X)=i\tilde X(-i)=\tilde X$. The one-sided operator sees the phase; the two-sided operator does not.

The plan is the following. §*Conventions* fixes the notation. §*The One-Sided Operators* gives the elementary properties and the factorisation through the polar word. §*The Two Real Forms* proves the block decomposition and the sector criterion. §*The Pure Central Phase of $\pi/2$* treats the exchange in detail, in coordinates and for a general phase. §*The Four Factors, One-Sided* reads the scale, the boost and the rotor. §*The Image and the Kernel* compares the one-sided and the two-sided images. §*The Null Cone* records the degenerate case. The article closes with the summary, the notation and the readings.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, the product $\vec e_x\vec e_y=\vec e_z$ and the squares $\vec e_x^{2}=\vec e_y^{2}=\vec e_z^{2}=-e_t$. The scalar imaginary is $i$, central, $i^{2}=-1$. An element is $\tilde Q=Q_te_t+\vec Q$ with the four coefficients $Q_\mu$ complex.

The three conjugations are the quaternion conjugation $\natural$, the coefficient conjugation $\bar\cdot$ and their composite, the **Hermitian conjugation**

$$
\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\bar Q_te_t-\bar Q_x\vec e_x-\bar Q_y\vec e_y-\bar Q_z\vec e_z .
$$

The Hermitian and anti-Hermitian subspaces are

$$
\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}.
$$

On $\mathbb{M}_-$ an element is $\tilde Q_-=ia\,e_t+\vec b$ with $a\in\mathbb{R}$ and $\vec b$ a real vector; on $\mathbb{M}_+$ an element is $\tilde Q_+=a\,e_t+i\vec b$ with the same real data. The two sectors are exchanged by multiplication by $i$, which is central. The **real quaternion subspace** is $\mathbb{H}_{\mathbb{B}}=\{\tilde Q:Q_\mu\in\mathbb{R}\ \text{for all}\ \mu\}$; its imaginary multiple $i\mathbb{H}_{\mathbb{B}}$ has all coefficients purely imaginary.

The **norm** is the complex number

$$
\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2},\qquad \tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}\,e_t ,
$$

and it is multiplicative, $\langle\tilde Q\tilde Q'\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}\langle\tilde Q'\rangle_{\natural}$. The polar word is

$$
\tilde Q=\Rho\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},\qquad
\Rho=r\exp(i\alpha),\qquad
\tilde U_{\mathrm b}=\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr),\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$, $\psi\ge0$, $\theta\in[0,2\pi]$, and $\vec u_{\mathrm b},\vec u_{\mathrm r}$ real unit vectors. The modulus is $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}$ on the principal branch, so $r=\lvert\Rho\rvert$ and $\alpha=\tfrac12\arg \langle\tilde Q\rangle_{\natural}$. The factors satisfy

$$
\Rho^{*}=\bar\Rho,\qquad \tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b},\qquad \tilde u_{\mathrm r}^{*}=\tilde u_{\mathrm r}^{\natural}=\tilde u_{\mathrm r}^{-1},\qquad \langle\tilde U_{\mathrm b}\rangle_{\natural}=\langle\tilde u_{\mathrm r}\rangle_{\natural}=1 .
$$

The matrix model is $\mathsf M_2:\mathbb{B}\to M_2(\mathbb{C})$, with $\mathsf M_2(e_t)=I_2$ and $\mathsf M_2(\vec e_k)=-i\sigma_k$, the $\sigma_k$ being the Pauli matrices. It is $\mathbb{C}$-linear and satisfies $\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger}$, and its determinant is the norm, $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$.

The one-sided operators are $L_{\tilde Q}$ and $R_{\tilde Q}$ above. The **Hermitian sandwich** is

$$
\Theta_{\tilde Q}=R_{\tilde Q^{*}}\circ L_{\tilde Q},\qquad \Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}.
$$

The general algebra of the one-sided operators, without the polar word, is *One-Sided Operators on the General Quaternionic Algebra*; the two-sided theory is *Two-Sided Operators on the General Quaternionic Algebra*. Here only the polar specialisation is treated.

## The One-Sided Operators

### Definition and Elementary Properties

**Proposition.** Let $\tilde Q,\tilde Q'\in\mathbb{B}$. Then:

**(a)** $L_{\tilde Q}$ and $R_{\tilde Q}$ are $\mathbb{C}$-linear;

**(b)** $L_{\tilde Q}\circ L_{\tilde Q'}=L_{\tilde Q\tilde Q'}$ and $R_{\tilde Q}\circ R_{\tilde Q'}=R_{\tilde Q'\tilde Q}$;

**(c)** $L_{\tilde Q}\circ R_{\tilde Q'}=R_{\tilde Q'}\circ L_{\tilde Q}$;

**(d)** the parameter maps $\tilde Q\mapsto L_{\tilde Q}$ and $\tilde Q\mapsto R_{\tilde Q}$ are injective;

**(e)** $L_{\tilde Q}$ and $R_{\tilde Q}$ are invertible exactly when $\tilde Q$ is a unit, with $L_{\tilde Q}^{-1}=L_{\tilde Q^{-1}}$ and $R_{\tilde Q}^{-1}=R_{\tilde Q^{-1}}$.

*Proof.* (a) The product is $\mathbb{C}$-bilinear. (b) and (c) are associativity. (d) $L_{\tilde Q}=0$ forces $\tilde Q=L_{\tilde Q}(e_t)=0$, and $R_{\tilde Q}=0$ forces $\tilde Q=R_{\tilde Q}(e_t)=0$. (e) $L_{\tilde Q}L_{\tilde Q^{-1}}=L_{e_t}=\mathrm{id}$ and $R_{\tilde Q}R_{\tilde Q^{-1}}=R_{e_t}=\mathrm{id}$; a non-unit is a zero divisor, so it cannot be invertible.

**Remark (multiplicativity).** The map $\tilde Q\mapsto L_{\tilde Q}$ is multiplicative into $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, but a single $L_{\tilde Q}$ is rarely an algebra endomorphism: $L_{\tilde Q}(\tilde X\tilde Y)=\tilde Q\tilde X\tilde Y$ while $L_{\tilde Q}(\tilde X)L_{\tilde Q}(\tilde Y)=\tilde Q\tilde X\tilde Q\tilde Y$, so multiplicativity forces $\tilde Q$ to be a central idempotent. In $\mathbb{B}$ the central idempotents are $0$ and $e_t$, so the only nonzero multiplicative left multiplication is the identity. The representation property is the composition law (b), not the multiplicativity of each $L_{\tilde Q}$.

**Remark (linear versus quadratic).** The map $\tilde Q\mapsto L_{\tilde Q}$ is linear and faithful. The map $\tilde Q\mapsto\Theta_{\tilde Q}$ is quadratic, and on the unit group its kernel is $U(1)$, as the companion article proves. The one-sided operator carries the whole parameter; the two-sided operator carries the parameter up to a central phase. This is the first reason the phase is visible one-sided and invisible two-sided.

**Remark (left translation, not conjugation).** $L_{\tilde Q}$ is a left translation of the algebra. It is an automorphism only for a central parameter. The sandwich is an inner conjugation only when $\tilde Q\tilde Q^{*}=e_t$, where the right factor is the inverse; for a general invertible element it is a congruence by $\tilde U_{\mathrm b}$ and a conjugation by $\tilde u_{\mathrm r}$. The two-sided article treats that distinction in full.

### The Factorisation Through the Polar Word

**Proposition.** With $\tilde Q=\Rho\tilde U_{\mathrm b}\tilde u_{\mathrm r}$,

$$
L_{\tilde Q}=L_{\Rho}\circ L_{\tilde U_{\mathrm b}}\circ L_{\tilde u_{\mathrm r}},\qquad
R_{\tilde Q}=R_{\tilde u_{\mathrm r}}\circ R_{\tilde U_{\mathrm b}}\circ R_{\Rho},
$$

and the modulus acts on either side by the same scalar,

$$
L_{\Rho}=R_{\Rho}=\Rho\,\mathrm{id}.
$$

*Proof.* The identities are the composition laws (b), read on the word. The modulus is central, so $L_{\Rho}(\tilde X)=\Rho\tilde X=\tilde X\Rho=R_{\Rho}(\tilde X)$.

**Remark (the order).** In the left reading the rightmost factor of the word acts first: the rotor, then the boost, then the modulus. In the right reading the order is reversed: the modulus, then the boost, then the rotor, because the parameter sits on the right. The two-sided sandwich uses both readings: the left action of the word and the right action of its conjugate.

**Remark (the complex exponent).** The modulus is a single complex scalar, $\Rho=r\exp(i\alpha)$. Its left multiplication is the operator $\exp(\ln r+i\alpha)\,\mathrm{id}$. The exponent is the complex number $\ln\Rho=\ln r+i\alpha$; the real part is the scale and the imaginary part is the phase. The one-sided operator keeps both. The two-sided sandwich keeps only $2\ln r$ and cancels the imaginary part.

The four factors are collected in the following table. A factor **preserves** a sector when it maps the sector into itself, **exchanges** the two sectors when it maps one onto the other, and **mixes** them when some element of a sector has a nonzero component in both sectors after the multiplication.

| factor | one-sided operator | sector action | factor on $\langle\tilde Q\rangle_{\natural}$ |
|---|---|---|---|
| scale $r$ | $r\,\mathrm{id}$ | preserves both | $r^{2}$ |
| phase $\exp(i\alpha)$ | $\exp(i\alpha)\,\mathrm{id}$ | preserves at $\alpha\equiv0\pmod{\pi}$, exchanges at $\alpha\equiv\tfrac{\pi}{2}\pmod{\pi}$, mixed otherwise | $\exp(2i\alpha)$ |
| boost $\tilde U_{\mathrm b}$ | $L_{\tilde U_{\mathrm b}}$ | mixes for $\psi>0$ | $1$ |
| rotor $\tilde u_{\mathrm r}$ | $L_{\tilde u_{\mathrm r}}$ | mixes for $\theta\not\equiv0\pmod{2\pi}$ | $1$ |

The table is justified factor by factor below; the phase row is the subject of §*The Pure Central Phase of $\pi/2$*, and the two mixing rows are the subject of §*The Four Factors, One-Sided*.

### The Norm and the Determinant

**Proposition.** For all $\tilde Q,\tilde X$,

$$
\langle L_{\tilde Q}\tilde X\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}\,\langle \tilde X\rangle_{\natural}=\Rho^{2}\langle \tilde X\rangle_{\natural},
\qquad
\langle R_{\tilde Q}\tilde X\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}\,\langle \tilde X\rangle_{\natural},
$$

and the complex determinant and the trace of the left multiplication are

$$
\det_{\mathbb{C}}L_{\tilde Q}=\langle\tilde Q\rangle_{\natural}^{2}=\Rho^{4},\qquad
\operatorname{tr}L_{\tilde Q}=4Q_t .
$$

*Proof.* The norm is multiplicative. In the matrix model $L_{\tilde Q}$ is $\tilde X\mapsto\mathsf M_2(\tilde Q)\tilde X$, the left multiplication by $\mathsf M_2(\tilde Q)$ on $M_2(\mathbb{C})$, which is $\mathsf M_2(\tilde Q)\otimes I_2$; its determinant is $\det\mathsf M_2(\tilde Q)^{2}=\langle\tilde Q\rangle_{\natural}^{2}$ and its trace is $2\operatorname{tr}\mathsf M_2(\tilde Q)=4Q_t$. The right multiplication is the mirror, with the same determinant and trace.

**Corollary (the complex similarity).** The one-sided operator multiplies the complex quadratic form $\langle\cdot\rangle_{\natural}$ by $\Rho^{2}$. On the norm-one slice $\langle\tilde X\rangle_{\natural}=1$ it is $\mathbb{C}$-orthogonal: it preserves $N$ and has complex determinant $1$. It is not, in general, an isometry of either real form $\mathbb{M}_\pm$.

The last clause is the subject of the next section: a complex isometry can exchange the two real forms, and the phase does exactly that.

## The Two Real Forms

### The Block Decomposition

**Definition.** For a parameter $\tilde Q$ the **symmetrized** and the **skew-symmetrized** multiplication operators are

$$
D_{\tilde Q}(\tilde X)=\tfrac12\bigl(\tilde Q\tilde X+\tilde X\tilde Q^{*}\bigr),\qquad
O_{\tilde Q}(\tilde X)=\tfrac12\bigl(\tilde Q\tilde X-\tilde X\tilde Q^{*}\bigr).
$$

**Proposition (the block form).** In the real splitting $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$, the left multiplication has the block form

$$
L_{\tilde Q}=
\begin{pmatrix}
D_{\tilde Q} & O_{\tilde Q}\\
O_{\tilde Q} & D_{\tilde Q}
\end{pmatrix}.
$$

The diagonal block $D_{\tilde Q}$ maps each sector into itself and the off-diagonal block $O_{\tilde Q}$ maps each sector into the other.

*Proof.* Let $\tilde X=\tilde X_++\tilde X_-$ with $\tilde X_\pm\in\mathbb{M}_\pm$. Then $\tilde X^{*}=\tilde X_+-\tilde X_-$, so

$$
(\tilde Q\tilde X)^{*}=\tilde X^{*}\tilde Q^{*}=(\tilde X_+-\tilde X_-)\tilde Q^{*}.
$$

The projections on the two sectors are $\tilde Y_\pm=\tfrac12(\tilde Y\pm\tilde Y^{*})$. Hence

$$
(\tilde Q\tilde X)_+=\tfrac12\bigl[\tilde Q(\tilde X_++\tilde X_-)+(\tilde X_+-\tilde X_-)\tilde Q^{*}\bigr]
=D_{\tilde Q}(\tilde X_+)+O_{\tilde Q}(\tilde X_-),
$$

and

$$
(\tilde Q\tilde X)_-=\tfrac12\bigl[\tilde Q(\tilde X_++\tilde X_-)-(\tilde X_+-\tilde X_-)\tilde Q^{*}\bigr]
=O_{\tilde Q}(\tilde X_+)+D_{\tilde Q}(\tilde X_-).
$$

The two identities are the four blocks.

**Corollary (the central blocks).** For a central parameter $c$,

$$
D_c=\operatorname{Re}(c)\,\mathrm{id},\qquad O_c=i\operatorname{Im}(c)\,\mathrm{id},
$$

so that in the splitting

$$
L_c=
\begin{pmatrix}
\operatorname{Re}(c) & i\operatorname{Im}(c)\\
i\operatorname{Im}(c) & \operatorname{Re}(c)
\end{pmatrix},
$$

the entry $i\operatorname{Im}(c)$ being the multiplication by $i$ on a sector times the real number $\operatorname{Im}(c)$.

*Proof.* $D_c(\tilde X)=\tfrac12(c\tilde X+\tilde X\bar c)=\operatorname{Re}(c)\tilde X$ and $O_c(\tilde X)=\tfrac12(c\tilde X-\tilde X\bar c)=i\operatorname{Im}(c)\tilde X$.

**Remark (the off-diagonal block).** The block $O_{\tilde Q}$ is the skew-symmetrized part of the multiplication. It vanishes for a real scalar, and for a central imaginary scalar it is the complex structure times the imaginary part. It is the part of the multiplication that changes the sector, and it is the part that the two-sided sandwich removes: the product $L_{\tilde Q}R_{\tilde Q^{*}}$ is block diagonal, because the right factor restores the sector that the left factor changes.

### The Sector Criterion

**Proposition (which parameters preserve a sector).** The left multiplication $L_{\tilde Q}$ preserves each of $\mathbb{M}_+$ and $\mathbb{M}_-$ exactly when $\tilde Q$ is a real scalar. It exchanges the two sectors exactly when $\tilde Q$ is a nonzero purely imaginary scalar. For every other parameter it mixes them.

*Proof.* Suppose first that $L_{\tilde Q}(\mathbb{M}_-)\subseteq\mathbb{M}_-$. For every anti-Hermitian $\tilde X$,

$$
(\tilde Q\tilde X)^{*}=-\tilde Q\tilde X .
$$

But $(\tilde Q\tilde X)^{*}=\tilde X^{*}\tilde Q^{*}=-\tilde X\tilde Q^{*}$, so the condition is

$$
\tilde X\tilde Q^{*}=\tilde Q\tilde X
$$

for every anti-Hermitian $\tilde X$. Taking $\tilde X=ie_t$ gives $i\tilde Q^{*}=i\tilde Q$, hence $\tilde Q^{*}=\tilde Q$. Taking $\tilde X=\vec e_x$ gives $\vec e_x\tilde Q=\tilde Q\vec e_x$, so $\tilde Q$ commutes with $\vec e_x$; the same holds with $\vec e_y$ and $\vec e_z$. A Hermitian element commuting with the three vector units is a real scalar: commuting with $\vec e_x$ forces the $\vec e_y$ and $\vec e_z$ coefficients to vanish, and then commuting with $\vec e_y$ forces the $\vec e_x$ coefficient to vanish. The converse is immediate.

Suppose next that $L_{\tilde Q}(\mathbb{M}_-)\subseteq\mathbb{M}_+$. Then $(\tilde Q\tilde X)^{*}=+\tilde Q\tilde X$ for every anti-Hermitian $\tilde X$, so $-\tilde X\tilde Q^{*}=\tilde Q\tilde X$, that is

$$
\tilde X\tilde Q^{*}=-\tilde Q\tilde X .
$$

Taking $\tilde X=ie_t$ gives $i\tilde Q^{*}=-i\tilde Q$, hence $\tilde Q^{*}=-\tilde Q$. Taking $\tilde X=\vec e_x$ gives $\vec e_x(-\tilde Q)=-\tilde Q\vec e_x$, that is $\vec e_x\tilde Q=\tilde Q\vec e_x$; the same holds with $\vec e_y$ and $\vec e_z$. An anti-Hermitian element commuting with the three vector units is a purely imaginary scalar, by the same coefficient argument. The converse is immediate.

**Corollary (the only one-sided Lorentz transformations).** Among the units, the real scalars are the only left multiplications that preserve $\mathbb{M}_-$, and among them the only isometries of $g$ are $\pm\mathrm{id}$. The one-sided action therefore gives no nontrivial real Lorentz transformation of $\mathbb{M}_-$; the real Lorentz group is the image of the two-sided sandwich, not of the one-sided operator.

## The Pure Central Phase of $\pi/2$

### The Operator

**Definition.** The **pure central phase of $\pi/2$** is the factor $P=\exp(i\pi/2)=i$, and its operator is

$$
J=L_i=R_i,\qquad J(\tilde X)=i\tilde X .
$$

The phase of $-\pi/2$ is $-i$ and its operator is $J^{-1}=L_{-i}$. On the principal branch of the polar word only $\alpha=\pi/2$ occurs; the sign $-i$ is the other square root and the inverse operator.

**Proposition.** The operator $J$ is $\mathbb{C}$-linear, exchanges the two real forms,

$$
J(\mathbb{M}_-)=\mathbb{M}_+,\qquad J(\mathbb{M}_+)=\mathbb{M}_-,
$$

and satisfies

$$
J^{2}=-\mathrm{id},\qquad J^{4}=\mathrm{id},\qquad J^{-1}=J^{3}=L_{-i}.
$$

*Proof.* For $\tilde X\in\mathbb{M}_-$,

$$
(i\tilde X)^{*}=-i\tilde X^{*}=-i(-\tilde X)=i\tilde X,
$$

so $i\tilde X\in\mathbb{M}_+$. The map $\tilde X\mapsto i\tilde X$ is injective and $\mathbb{M}_-$ and $\mathbb{M}_+$ are both real four-dimensional, so $i\mathbb{M}_-=\mathbb{M}_+$. The same computation with $\tilde X\in\mathbb{M}_+$ gives $i\mathbb{M}_+=\mathbb{M}_-$. The powers follow from $i^{2}=-1$ and the centrality of $i$.

**Remark (the sign).** Both $i$ and $-i$ exchange the sectors, and they are inverse to each other. The sign selects which of the two inverse swaps is used; both exchange the same pair of sectors. The square of either is $-\mathrm{id}$, and the fourth power is the identity.

**Remark (the block matrix).** In the ordered splitting $(\mathbb{M}_+,\mathbb{M}_-)$ the operator is

$$
J=
\begin{pmatrix}
0 & i\\
i & 0
\end{pmatrix},
$$

the off-diagonal blocks being the multiplication by $i$ on each real four-dimensional sector. It is the block matrix of a swap times the complex structure. Its square is $-I_8$ and its fourth power is $I_8$.

**Remark (the complex structure).** Since $i$ is central, $J$ is the multiplication by the complex scalar $i$. As a complex-linear map it is the scalar $i$; as a real-linear map it is a complex structure on the eight-dimensional real space. The exchange of $\mathbb{M}_+$ and $\mathbb{M}_-$ is invisible to the complex-linear structure and visible only over $\mathbb{R}$. This is the precise sense in which the phase is a real operation and not a complex one.

### The Coordinate Form

Let $\tilde X\in\mathbb{M}_-$ be written as $\tilde X=ia\,e_t+\vec b$ with $a\in\mathbb{R}$ and $\vec b\in\mathbb{R}^{3}$. Then

$$
i\tilde X=i(ia\,e_t+\vec b)=-a\,e_t+i\vec b .
$$

The result is the element of $\mathbb{M}_+$ with scalar coordinate $-a$ and vector coordinate $\vec b$. In the pair $(a,\vec b)$ the exchange is therefore the **time reflection**

$$
(a,\vec b)\longmapsto(-a,\vec b).
$$

The following table records the two coordinate descriptions; the first column is the element of $\mathbb{M}_-$ and the second its image in $\mathbb{M}_+$.

| $\tilde X\in\mathbb{M}_-$ | $i\tilde X\in\mathbb{M}_+$ |
|---|---|
| $ia\,e_t+\vec b$ | $-a\,e_t+i\vec b$ |

The Minkowski form on the two sectors is

$$
g(\tilde X)=a^{2}-\lvert\vec b\rvert^{2}\quad(\tilde X\in\mathbb{M}_-),\qquad
g(\tilde Y)=a^{2}-\lvert\vec b\rvert^{2}\quad(\tilde Y=a\,e_t+i\vec b\in\mathbb{M}_+).
$$

With this convention

$$
g(i\tilde X)=g(\tilde X),
$$

so $J$ is an isometry between $(\mathbb{M}_-,g)$ and $(\mathbb{M}_+,g)$. In the coordinates above its determinant is $-1$: it is the improper isometry that reverses the time direction and fixes the three space directions. It is the discrete symmetry that exchanges the two real forms, not a proper Lorentz transformation of either one.

**Remark (the norm sign).** The complex norm changes sign,

$$
\langle i\tilde X\rangle_{\natural}=i^{2}\langle\tilde X\rangle_{\natural}=-\langle\tilde X\rangle_{\natural}.
$$

On $\mathbb{M}_-$ one has $\langle\tilde X\rangle_{\natural}=-g$, and on $\mathbb{M}_+$ one has $\langle\tilde X\rangle_{\natural}=+g$. The minus sign in $\langle i\tilde X\rangle_{\natural}=-\langle\tilde X\rangle_{\natural}$ is therefore the change of the sector convention, not a failure of the isometry: the form $g$ is preserved.

**Remark (physical interpretation).** In the physical interpretation of the corpus, $\mathbb{M}_-$ is the material sector and $\mathbb{M}_+$ the informational sector. The phase of $\pi/2$ exchanges the two: it turns an anti-Hermitian element into a Hermitian one and back. The exchange is the discrete operation of the algebra that the two-sided sandwich cannot see, because the sandwich multiplies by $i$ on the left and by $-i$ on the right. The full Wick rotation of the physics articles is a different operation: it acts on the time coefficient alone and maps $\mathbb{M}_-$ to the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, not to $\mathbb{M}_+$. The operator $J$ is the sector exchange, not the whole Wick rotation.

### The General Phase

**Proposition.** For the phase $P_\alpha=\exp(i\alpha)$ the one-sided operator is

$$
L_{P_\alpha}=R_{P_\alpha}=\exp(i\alpha)\,\mathrm{id},
$$

and in the splitting $(\mathbb{M}_+,\mathbb{M}_-)$ its block matrix is

$$
L_{P_\alpha}=
\begin{pmatrix}
\cos\alpha & i\sin\alpha\\
i\sin\alpha & \cos\alpha
\end{pmatrix}.
$$

For $\tilde X\in\mathbb{M}_-$ the image $\tilde Y=\exp(i\alpha)\tilde X$ satisfies

$$
\tilde Y^{*}=-\exp(-2i\alpha)\,\tilde Y .
$$

Hence $\tilde Y\in\mathbb{M}_+$ exactly when $\alpha\equiv\tfrac{\pi}{2}\pmod{\pi}$, and $\tilde Y\in\mathbb{M}_-$ exactly when $\alpha\equiv0\pmod{\pi}$. For every other $\alpha$ the image lies in the real four-dimensional subspace $\exp(i\alpha)\mathbb{M}_-$, on which $*$ acts by the scalar $-\exp(-2i\alpha)$; that subspace is neither $\mathbb{M}_+$ nor $\mathbb{M}_-$.

*Proof.* The scalar is central, so $L_{P_\alpha}=R_{P_\alpha}=\exp(i\alpha)\mathrm{id}$. The block matrix is the corollary of the block decomposition with $c=\exp(i\alpha)$. For the eigenvalue, $\tilde Y^{*}=\exp(-i\alpha)\tilde X^{*}=-\exp(-i\alpha)\tilde X=-\exp(-2i\alpha)\tilde Y$. The two sector values are the two solutions of $-\exp(-2i\alpha)=\pm1$.

**Corollary (the special angles).** The phase preserves each sector at $\alpha=0$ and $\alpha=\pi$, where it is $+\mathrm{id}$ and $-\mathrm{id}$. It exchanges the two sectors at $\alpha=\pi/2$ and $\alpha=3\pi/2$, where it is $i$ and $-i$. At $\alpha=\pi/4$ it is a square root of the exchange,

$$
L_{\exp(i\pi/4)}^{2}=L_i,
$$

and the image of $\mathbb{M}_-$ is the mixed real four-dimensional subspace on which $*$ acts by $i$.

*Proof.* The values at the four angles are immediate from the block matrix. The square is $L_{\exp(i\pi/2)}=L_i$ by the composition law.

**Remark (the period).** The operator $L_{P_\alpha}$ has period $2\pi$ in $\alpha$. The sector behaviour has period $\pi$, because $\exp(i(\alpha+\pi))=-\exp(i\alpha)$ multiplies the operator by $-1$ and leaves the eigenvalue $-\exp(-2i\alpha)$ unchanged. The exchange therefore occurs on the two classes $\alpha\equiv\pi/2\pmod{\pi}$, and the preservation on the two classes $\alpha\equiv0\pmod{\pi}$.

**Remark (not a half-angle).** The polar word stores the phase as $\exp(i\alpha)$, with $\alpha=\tfrac12\arg \langle\tilde Q\rangle_{\natural}$. The pure phase of $\pi/2$ is therefore $i=\exp(i\pi/2)$, not $\exp(i\pi/4)$. The half-angle $\exp(i\pi/4)$ is the square root of the exchange, not the exchange itself. A half-angle convention would rename the angle of the exchange to $\pi$; it would not change the operator, only the name of its parameter.

### The Cancellation in the Two-Sided Operator

**Proposition.** The two-sided sandwich of the pure phase is the identity:

$$
\Theta_i(\tilde X)=i\tilde X(-i)=\tilde X,\qquad
\Theta_{\exp(i\alpha)}=\mathrm{id}.
$$

In the block matrices,

$$
\begin{pmatrix}
0 & i\\
i & 0
\end{pmatrix}
\begin{pmatrix}
0 & -i\\
-i & 0
\end{pmatrix}
=
\begin{pmatrix}
1 & 0\\
0 & 1
\end{pmatrix}.
$$

*Proof.* The scalar $i$ is central, so the two factors commute with $\tilde X$ and with each other, and $i(-i)=1$. The block product is the same computation with the two off-diagonal exchanges.

**Remark (the two readings of the same word).** The one-sided operator of the phase is $\exp(i\alpha)\mathrm{id}$; the two-sided operator is the identity. The one-sided operator sees the whole complex modulus $\Rho=r\exp(i\alpha)$; the two-sided operator sees only its modulus $r$ and the two non-central factors. The cancellation is the product of the left factor $\exp(i\alpha)$ and the right factor $\exp(-i\alpha)$; it is exact because the two scalars are central and inverse. The phase is not halved in either reading; it is either kept whole, one-sided, or cancelled whole, two-sided.

## The Four Factors, One-Sided

### The Scale

The scale is $r=\exp(\ln r)$, positive, real and central. Its one-sided operators are

$$
L_r=R_r=r\,\mathrm{id}.
$$

In the block decomposition $D_r=r\,\mathrm{id}$ and $O_r=0$: the scale preserves both sectors and multiplies every coordinate by $r$. The norm is multiplied by $r^{2}$, and the exponent is

$$
\ln r\longmapsto\ln r .
$$

The one-sided operator does not double the exponent. The doubling $2\ln r$ belongs to the two-sided sandwich, where the scale appears twice, once on each side. The determinant of $L_r$ is $r^{4}$ on the complex four-space and $r^{8}$ on the real eight-space.

### The Boost

The boost is

$$
\tilde U_{\mathrm b}=\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr)
=\cosh\tfrac{\psi}{2}\,e_t+i\sinh\tfrac{\psi}{2}\,\vec u_{\mathrm b},
\qquad \psi\ge0,\qquad \lvert\vec u_{\mathrm b}\rvert=1 .
$$

It is Hermitian and of norm one. Write $c=\cosh\tfrac{\psi}{2}$, $s=\sinh\tfrac{\psi}{2}$, $\vec u=\vec u_{\mathrm b}$, and let $\tilde X=ia\,e_t+\vec b$ be an element of $\mathbb{M}_-$. Then

$$
\tilde U_{\mathrm b}\tilde X
=i\bigl(ac-s\,\vec u\cdot\vec b\bigr)e_t+i s\,\vec u\times\vec b
+c\,\vec b-s a\,\vec u .
$$

The term $i s\,\vec u\times\vec b$ is the whole $\mathbb{M}_+$ part, an imaginary vector. The remaining terms $i(ac-s\,\vec u\cdot\vec b)e_t+c\vec b-s a\,\vec u$ are the $\mathbb{M}_-$ part, an imaginary scalar plus the real vector $c\vec b-s a\,\vec u$. The boost therefore mixes the two sectors in general. For $a=0$ the $\mathbb{M}_-$ part is $c\vec b-i s(\vec u\cdot\vec b)e_t$ and the $\mathbb{M}_+$ part is $i s\,\vec u\times\vec b$, which vanishes only when $\vec b$ is parallel to $\vec u$. For $\vec b=0$ the image is $i a(c\,e_t+i s\,\vec u)=i a c\,e_t-s a\,\vec u$, entirely in $\mathbb{M}_-$: the central imaginary line is mapped into the two-plane spanned by $i e_t$ and $\vec u$.

The boost is of norm one, so $L_{\tilde U_{\mathrm b}}$ preserves the complex norm, $\langle L_{\tilde U_{\mathrm b}}\tilde X\rangle_{\natural}=\langle \tilde X\rangle_{\natural}$, and is $\mathbb{C}$-orthogonal. It is not a real Lorentz transformation of $\mathbb{M}_-$: it does not preserve the sector, and the only one-sided real Lorentz transformations are $\pm\mathrm{id}$, by the sector criterion.

### The Rotor

The rotor is

$$
\tilde u_{\mathrm r}=\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr)
=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,\vec u_{\mathrm r},
\qquad \theta\in[0,2\pi],\qquad \lvert\vec u_{\mathrm r}\rvert=1 .
$$

It is a real quaternion, of norm one, and unitary. Write $c=\cos\tfrac{\theta}{2}$, $s=\sin\tfrac{\theta}{2}$, $\vec u=\vec u_{\mathrm r}$, and let $\tilde X=ia\,e_t+\vec b$ be an element of $\mathbb{M}_-$. Then

$$
\tilde u_{\mathrm r}\tilde X
=-s\,\vec u\cdot\vec b\,e_t+i a s\,\vec u
+i a c\,e_t+c\,\vec b+s\,\vec u\times\vec b .
$$

The first two terms are in $\mathbb{M}_+$: a real scalar and an imaginary vector. The last two terms are in $\mathbb{M}_-$: an imaginary scalar and the real vector $c\vec b+s\vec u\times\vec b$. The rotor mixes the two sectors in general. For $a=0$ the $\mathbb{M}_+$ part is the real scalar $-s\,\vec u\cdot\vec b$, which vanishes only when $\vec b$ is perpendicular to $\vec u$; the $\mathbb{M}_-$ part is the real vector $c\vec b+s\vec u\times\vec b$.

The rotor is of norm one, so $L_{\tilde u_{\mathrm r}}$ preserves the complex norm and is $\mathbb{C}$-orthogonal. It also preserves the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and its imaginary multiple $i\mathbb{H}_{\mathbb{B}}$, because it is a real quaternion and left multiplication by a real quaternion preserves the subalgebra $\mathbb{H}_{\mathbb{B}}$ and the module $i\mathbb{H}_{\mathbb{B}}$. On $\mathbb{H}_{\mathbb{B}}$ it is an isometry of the Euclidean norm. It does not preserve $\mathbb{M}_\pm$.

### The Bookkeeping

The following table collects the exponents. The **exponent** is the element $A$ such that the factor is $\exp(A)$; the **scalar parameter** is the real or imaginary coefficient inside that exponential, and the **two-sided output** is the parameter of the corresponding transformation in the sandwich.

| factor | exponent $A$ | scalar parameter | two-sided output |
|---|---|---|---|
| scale $r$ | $\ln r$ | $\ln r$ | $2\ln r$ |
| phase $\exp(i\alpha)$ | $i\alpha$ | $\alpha$ | $0$ |
| boost $\tilde U_{\mathrm b}$ | $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | $\tfrac{\psi}{2}$ | $\psi$ |
| rotor $\tilde u_{\mathrm r}$ | $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | $\tfrac{\theta}{2}$ | $\theta$ |

The rule is the number of slots. A one-sided operator is one factor of the word, so its exponent is the exponent of that factor: the scale keeps $\ln r$, the phase keeps $i\alpha$, the boost keeps the half-rapidity in $i\psi/2\,\vec u_{\mathrm b}$, the rotor keeps the half-angle in $\theta/2\,\vec u_{\mathrm r}$. A two-sided operator uses two slots, the parameter and its Hermitian conjugate. For the Hermitian factors the two exponents are equal and add, giving $2\ln r$ for the scale and $\psi$ for the boost; for the unitary rotor they are opposite and the conjugation gives the angle $\theta$; for the central imaginary phase they cancel to $0$. The doubling of the companion article is therefore a two-slot phenomenon for the scale, the boost and the rotor, and the phase is its exceptional case.

## The Image and the Kernel

**Proposition.** Let $\tilde Q\in\mathbb{B}$.

**(a)** The parameter map $\tilde Q\mapsto L_{\tilde Q}$ is injective. The operator $L_{\tilde Q}$ is injective exactly when $\tilde Q$ is a unit.

**(b)** For a unit $\tilde Q$, $L_{\tilde Q}$ is a bijection of $\mathbb{B}$.

**(c)** For a nonzero null $\tilde Q$, the operator $L_{\tilde Q}$ has complex rank two, its kernel is the right annihilator $\{\tilde X:\tilde Q\tilde X=0\}$ of complex dimension two, and its image is the right ideal $\tilde Q\mathbb{B}$ of complex dimension two.

**(d)** For $\tilde Q=0$ the operator is zero.

*Proof.* (a) Injectivity of the parameter map is (d) of the first proposition. If $\tilde Q$ is a unit, $L_{\tilde Q}^{-1}=L_{\tilde Q^{-1}}$. If $\tilde Q$ is a nonzero null element, $\mathsf M_2(\tilde Q)$ has rank one, so the kernel of $X\mapsto\mathsf M_2(\tilde Q)X$ is the two-dimensional space of matrices whose columns lie in the kernel of $\mathsf M_2(\tilde Q)$, and the image is the two-dimensional space of matrices whose columns lie in the image. (b) is (e) of the first proposition. (c) is the matrix computation just given. (d) is immediate.

**Proposition (the image on the group of units).** The restriction of $\tilde Q\mapsto L_{\tilde Q}$ to $\mathbb{B}^{\times}$ is a faithful representation whose image is a subgroup of $GL_{\mathbb{C}}(\mathbb{B})$ isomorphic to $\mathbb{B}^{\times}$. As a complex Lie group,

$$
\mathbb{B}^{\times}\cong GL(2,\mathbb{C}),
$$

of complex dimension four and real dimension eight. The kernel is trivial.

*Proof.* The map is injective by (a) and multiplicative by the composition law, so it is a faithful representation. The algebra isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ identifies the units with $GL(2,\mathbb{C})$.

**Corollary (the contrast with the two-sided operator).** The two-sided image is the conformal Lorentz group $CO^{+}(1,3)$, of real dimension seven, with kernel $U(1)$. The one-sided image is $\mathbb{B}^{\times}\cong GL(2,\mathbb{C})$, of real dimension eight, with trivial kernel. The missing dimension is the phase: the one-sided action sees it, the two-sided action quotients by it.

The following table collects the comparison. The rank is the complex rank of the operator on $\mathbb{B}$.

| | one-sided $L_{\tilde Q}$ | two-sided $\Theta_{\tilde Q}$ |
|---|---|---|
| parameter map | linear, faithful | quadratic; kernel $U(1)$ on the units |
| scale | $r$ | $r^{2}$ |
| phase | $\exp(i\alpha)$, exchange at $\pi/2$ | $1$ |
| norm of the image | $\Rho^{2}\langle \tilde X\rangle_{\natural}$ | $r^{4}\langle \tilde X\rangle_{\natural}$ |
| complex determinant | $\Rho^{4}$ | $r^{8}$ |
| image on the units | $\cong GL(2,\mathbb{C})$, real dimension $8$ | $\cong CO^{+}(1,3)$, real dimension $7$ |
| kernel on the units | trivial | $U(1)$ |
| nonzero null parameter | rank $2$, right ideal | rank $1$, complex line |

**Corollary (the real forms are two-sided).** The only one-sided multiplications that preserve $\mathbb{M}_-$ are the real scalars, and among them the only isometries of $g$ are $\pm\mathrm{id}$. The one-sided action therefore does not give the Lorentz group on $\mathbb{M}_-$. The norm-one one-sided operators are $\mathbb{C}$-orthogonal. The proper orthochronous Lorentz group is not among them: it is the image of the two-sided sandwich on the norm-one slice, the identity component of the subgroup of the $\mathbb{C}$-orthogonal group that also preserves the two real forms.

## The Null Cone

On the null cone the polar word does not exist, but both one-sided operators do. Let $\tilde Q\neq0$ with $\langle\tilde Q\rangle_{\natural}=0$. In the matrix model $\mathsf M_2(\tilde Q)=uv^{*}$ with $u$ a nonzero column and $v^{*}$ a nonzero row. Then

$$
\mathsf M_2(L_{\tilde Q}\tilde X)=\mathsf M_2(\tilde Q)\,\mathsf M_2(\tilde X)=u\,(v^{*}\mathsf M_2(\tilde X)).
$$

The image consists of the matrices $u r^{*}$ with $r^{*}$ an arbitrary row, that is, the matrices all of whose columns lie in the complex line $\mathbb{C}u$. This is a right ideal of complex dimension two, not a line. The kernel is the set of $\tilde X$ with $v^{*}\mathsf M_2(\tilde X)=0$, of complex dimension two. The rank is two.

The sandwich of the same element is

$$
\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}
=u\,(v^{*}\mathsf M_2(\tilde X)v)\,u^{*},
$$

a multiple of $uu^{*}=\mathsf M_2(\tilde Q\tilde Q^{*})$. Its image is the single complex line $\mathbb{C}\tilde Q\tilde Q^{*}$, and its rank is one. The one-sided operator keeps a two-dimensional right ideal; the two-sided operator collapses it to a line. The failure of invertibility is therefore different in the two readings: the one-sided operator loses half of the algebra, the two-sided operator loses all but one complex direction.

## Summary

The one-sided operators of the polar word are $L_{\tilde Q}(\tilde X)=\tilde Q\tilde X$ and $R_{\tilde Q}(\tilde X)=\tilde X\tilde Q$. They are $\mathbb{C}$-linear, faithful in the parameter, and they multiply the complex norm by $\Rho^{2}$. The left multiplication factorises as

$$
L_{\tilde Q}=L_{\Rho}\circ L_{\tilde U_{\mathrm b}}\circ L_{\tilde u_{\mathrm r}},
$$

with $L_{\Rho}=\Rho\,\mathrm{id}$; the right multiplication is the mirror.

In the real splitting $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ the left multiplication has the block form

$$
L_{\tilde Q}=
\begin{pmatrix}
D_{\tilde Q} & O_{\tilde Q}\\
O_{\tilde Q} & D_{\tilde Q}
\end{pmatrix},
\qquad
D_{\tilde Q}=\tfrac12(\tilde Q\,\cdot+\cdot\,\tilde Q^{*}),\quad
O_{\tilde Q}=\tfrac12(\tilde Q\,\cdot-\cdot\,\tilde Q^{*}).
$$

The diagonal block preserves the sectors and the off-diagonal block carries each sector into the other. For a central factor $c$ the blocks are $\operatorname{Re}(c)$ and $i\operatorname{Im}(c)$. A one-sided multiplication preserves each sector exactly for a real scalar, exchanges the two exactly for a nonzero purely imaginary scalar, and mixes them otherwise.

The pure central phase of $\pi/2$ is the exchange. The factor is $i$ or $-i$, the operator is $J(\tilde X)=i\tilde X$, and

$$
J(\mathbb{M}_-)=\mathbb{M}_+,\qquad J(\mathbb{M}_+)=\mathbb{M}_-,\qquad J^{2}=-\mathrm{id},\qquad J^{-1}=L_{-i}.
$$

In coordinates, $\tilde X=ia\,e_t+\vec b$ is sent to $-a\,e_t+i\vec b$: the time reflection $(a,\vec b)\mapsto(-a,\vec b)$, an improper isometry of the Minkowski form $g=a^{2}-\lvert\vec b\rvert^{2}$. The complex norm changes sign, $\langle i\tilde X\rangle_{\natural}=-\langle\tilde X\rangle_{\natural}$, because the two sectors carry opposite signs in $\langle\cdot\rangle_{\natural}$. For a general phase the block matrix is

$$
\begin{pmatrix}
\cos\alpha & i\sin\alpha\\
i\sin\alpha & \cos\alpha
\end{pmatrix},
$$

the image of $\mathbb{M}_-$ has $*$-eigenvalue $-\exp(-2i\alpha)$, and the sectors are reached exactly at $\alpha\equiv0$ and $\alpha\equiv\pi/2$ modulo $\pi$.

The scale acts as $r$, not $r^{2}$. The phase acts as $\exp(i\alpha)$, not as the identity. The boost and the rotor are $\mathbb{C}$-orthogonal and mix the sectors; their one-sided exponents are the half-rapidity and the half-angle, and the physical rapidity and angle are the two-sided outputs. The one-sided operator has one slot and does not double; the two-sided operator has two slots and doubles the scale and the non-central exponents, while it cancels the central imaginary one.

The image of the one-sided action on the units is $\mathbb{B}^{\times}\cong GL(2,\mathbb{C})$, of real dimension eight, with trivial kernel. The image of the two-sided action is $CO^{+}(1,3)$, of real dimension seven, with kernel $U(1)$. The missing dimension is the phase. On the null cone the one-sided operator has rank two and image the right ideal $\tilde Q\mathbb{B}$; the sandwich has rank one and image the line $\mathbb{C}\tilde Q\tilde Q^{*}$.

The one-sided multiplication is a left translation of the algebra. The two-sided sandwich is the product of a left translation and a right translation, and it is that product which gives the real Lorentz transformations. The phase is the clearest witness: one-sided it is the exchange of the two real forms, two-sided it is the identity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, with $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | the central scalar imaginary, $i^{2}=-1$ |
| $\tilde Q^{*}$ | the Hermitian conjugation $\overline{\tilde Q^{\natural}}$ |
| $\natural$, $\bar\cdot$ | the quaternion and coefficient conjugations |
| $\mathbb{M}_\pm$ | the Hermitian and anti-Hermitian subspaces, $\tilde Q^{*}=\pm\tilde Q$ |
| $L_{\tilde Q},R_{\tilde Q}$ | the left and right multiplications |
| $\Theta_{\tilde Q}=R_{\tilde Q^{*}}\circ L_{\tilde Q}$ | the two-sided Hermitian sandwich |
| $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | the complex norm |
| $\Rho=r\exp(i\alpha)$ | the complex modulus, the principal square root of $\langle\tilde Q\rangle_{\natural}$ |
| $r>0$, $\alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$ | the scale and the phase angle |
| $\tilde U_{\mathrm b}=\exp(i\tfrac{\psi}{2}\vec u_{\mathrm b})$ | the Hermitian positive unit-norm boost |
| $\tilde u_{\mathrm r}=\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ | the unit real quaternion rotor |
| $D_{\tilde Q},O_{\tilde Q}$ | the symmetrized and skew-symmetrized multiplication blocks |
| $J=L_i=R_i$ | the pure central phase of $\pi/2$, the complex structure |
| $g$ | the Minkowski form, $\langle\tilde Q\rangle_{\natural}$ on $\mathbb{M}_+$ and $-\langle\tilde Q\rangle_{\natural}$ on $\mathbb{M}_-$ |
| $GL(2,\mathbb{C})$ | the image of the one-sided action on the units |
| $CO^{+}(1,3)$ | the image of the two-sided action on the units |
| $U(1)$ | the kernel of the two-sided action, the central unit circle |

## Further Reading

- [Two-Sided Operator Under the Polar Decomposition](two-sided-operator-under-the-polar-decomposition.html), for the sandwich, the factor-by-factor doubling rule and the cancellation of the phase.
- [The Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the four factors, the modulus, the branch and the domain.
- [The Polar Decomposition and Remarkable Subspaces](the-polar-decomposition-and-remarkable-subspaces.html), for the four exponents read against the six remarkable subspaces and the sector blocks.
- [The Polar Decomposition and Remarkable Subspaces](the-polar-decomposition-and-remarkable-subspaces.html), §*The Action on the Two Halves*, for the detailed action on the two sectors, the boost matrices and the infinitesimal split of the rotor and the boost.
- [One-Sided Operators on the General Quaternionic Algebra](one-sided-operators-on-the-general-quaternionic-algebra.html), for the general left and right multiplications, their adjoints and their normal forms.
- [Two-Sided Operators on the General Quaternionic Algebra](two-sided-operators-on-the-general-quaternionic-algebra.html), for the general two-sided family and the sandwich as its conjugation member.
- [The Twisted Spinor Operator Representation of Biquaternions](the-twisted-spinor-operator-representation-of-biquaternions.html), for the left multiplication read on the spinor module, where the phase is the twist.
- [The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint](the-spectra-of-the-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.html), for the left and right regular representations and the eigenvalues of the sandwich.
- [The Four-Vector Operator Representation of Biquaternions](the-four-vector-operator-representation-of-biquaternions.html), for the sandwich written in the four complex coefficients.
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the Lorentz group in biquaternionic form and the double cover.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](../articles_physics/the-material-sector-four-vectors-interval-and-lorentz-action.html) and [The Informational Sector: States, Observables and Probability](../articles_physics/the-informational-sector-states-observables-and-probability.html), for the physical interpretation of the two real forms exchanged by the phase.
