# __One-Sided Operator Under the Polar Representation__

## Introduction

The biquaternion algebra acts on itself by left multiplication and by right multiplication. For a parameter $\tilde Q$ the two **one-sided operators** are

$$
L_{\tilde Q}(X)=\tilde QX,\qquad R_{\tilde Q}(X)=X\tilde Q.
$$

The two-sided operator of the polar representation is the product of the left action of $\tilde Q$ and the right action of $\tilde Q^{*}$,

$$
\Theta_{\tilde Q}=R_{\tilde Q^{*}}\circ L_{\tilde Q},
\qquad
\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*},
$$

and its theory is *Two-Sided Operator Under the Polar Representation*. This article reads the one-sided factors: the physics polar word

$$
\tilde Q=r\exp(i\alpha)B\tilde q,\qquad
B=\exp(-i\psi\vec u_{\mathrm b}),\qquad
\tilde q=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$, $\psi\ge0$, $\theta\in[0,2\pi]$ and real unit axes $\vec u_{\mathrm b},\vec u_{\mathrm r}$, acting by a single multiplication, on the left or on the right, and the transformation it produces on a biquaternion.

The one-sided operator is $\mathbb{C}$-linear, and the map from the parameter to the operator is faithful. It multiplies the complex norm by $\rho^{2}$, where $\rho=r\exp(i\alpha)$ is the modulus. It does not, in general, preserve the two real forms $\mathbb{M}_+$ and $\mathbb{M}_-$. Its block form in the splitting $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ is

$$
L_{\tilde Q}=
\begin{pmatrix}
D_{\tilde Q} & O_{\tilde Q}\\
O_{\tilde Q} & D_{\tilde Q}
\end{pmatrix},
$$

with the symmetrized and the skew-symmetrized parts

$$
D_{\tilde Q}(X)=\tfrac12\bigl(\tilde QX+X\tilde Q^{*}\bigr),\qquad
O_{\tilde Q}(X)=\tfrac12\bigl(\tilde QX-X\tilde Q^{*}\bigr).
$$

The diagonal block $D_{\tilde Q}$ preserves each sector and the off-diagonal block $O_{\tilde Q}$ carries each sector into the other. For a central factor $c$ the two blocks are the scalars $\operatorname{Re}(c)$ and $i\operatorname{Im}(c)$.

The clearest case is the pure central phase of $\pi/2$. The factor is $i$, or $-i$, and the operator is

$$
L_i(X)=iX,\qquad i\mathbb{M}_-=\mathbb{M}_+,\qquad i\mathbb{M}_+=\mathbb{M}_-.
$$

It is multiplication by the central imaginary, the complex structure $J$ of the algebra read over $\mathbb{R}$. It satisfies $J^{2}=-\mathrm{id}$ and $J^{-1}=J^{3}=L_{-i}$. The sign $i$ or $-i$ is the direction of the exchange. This is the operator that the two-sided sandwich cancels: $\Theta_i(X)=iX(-i)=X$. The one-sided operator sees the phase; the two-sided operator does not.

The plan is the following. §*The One-Sided Operators* gives the elementary properties and the factorisation through the polar word. §*The Two Real Forms* proves the block decomposition and the sector criterion. §*The Pure Central Phase of $\pi/2$* treats the exchange in detail, in coordinates and for a general phase. §*The Four Factors, One-Sided* reads the scale, the boost factor and the rotor. §*The Image and the Kernel* compares the one-sided and the two-sided images. §*The Null Cone* records the degenerate case. §*Worked Numbers* fixes one element and checks the formulas. The article closes with the summary, the notation and the readings.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, the product $\vec e_x\vec e_y=\vec e_z$ and the squares $\vec e_x^{2}=\vec e_y^{2}=\vec e_z^{2}=-e_t$. The scalar imaginary is $i$, central, $i^{2}=-1$. An element is $\tilde Q=Q_te_t+\vec Q$ with the four coefficients $Q_\mu$ complex.

The three conjugations are the quaternion conjugation $\natural$, the coefficient conjugation $\bar\cdot$ and their composite, the **Hermitian conjugation**

$$
\tilde Q^{*}=\overline{\tilde Q^{\natural}}
=\bar Q_te_t-\bar Q_x\vec e_x-\bar Q_y\vec e_y-\bar Q_z\vec e_z.
$$

The Hermitian and anti-Hermitian subspaces are

$$
\mathbb{M}_\pm=\{X\in\mathbb{B}:X^{*}=\pm X\}.
$$

On $\mathbb{M}_-$ an element is $X=ia\,e_t+\vec b$ with $a\in\mathbb{R}$ and $\vec b$ a real vector; on $\mathbb{M}_+$ an element is $X=a\,e_t+i\vec b$ with the same real data. The two sectors are exchanged by multiplication by $i$, which is central. The **real quaternion subspace** is $\mathbb{H}_{\mathbb{B}}=\{\tilde Q:Q_\mu\in\mathbb{R}\ \text{for all}\ \mu\}$; its imaginary multiple $i\mathbb{H}_{\mathbb{B}}$ has all coefficients purely imaginary. In the physical reading $\mathbb{M}_-$ is the material sector and $\mathbb{M}_+$ the informational sector.

The **norm** is the complex number

$$
N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}
=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2},
$$

and it is multiplicative, $N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)N(\tilde Q_2)$. The polar word is

$$
\tilde Q=r\exp(i\alpha)B\tilde q,\qquad
B=\exp(-i\psi\vec u_{\mathrm b}),\qquad
\tilde q=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$, $\psi\ge0$, $\theta\in[0,2\pi]$, and real unit vectors $\vec u_{\mathrm b},\vec u_{\mathrm r}$. The modulus is $\rho=r\exp(i\alpha)=\sqrt{N(\tilde Q)}$ on the principal branch, so $r=\lvert\rho\rvert$ and $\alpha=\tfrac12\arg N(\tilde Q)$. The factors satisfy

$$
B^{*}=B,\qquad N(B)=1,\qquad B=\tilde U_{\mathrm L}^{-2},\qquad
\tilde U_{\mathrm L}=B^{-1/2}=\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde U_{\mathrm L}^{*}=\tilde U_{\mathrm L},\qquad N(\tilde U_{\mathrm L})=1,
$$

and

$$
\tilde q^{*}=\tilde q^{\natural}=\tilde q^{-1},\qquad N(\tilde q)=1.
$$

The matrix model is $\mathsf M_2:\mathbb{B}\to M_2(\mathbb{C})$, with $\mathsf M_2(e_t)=I_2$ and $\mathsf M_2(\vec e_k)=-i\sigma_k$, the $\sigma_k$ being the Pauli matrices. It is $\mathbb{C}$-linear and satisfies $\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger}$, and its determinant is the norm, $\det\mathsf M_2(\tilde Q)=N(\tilde Q)$.

The one-sided operators are $L_{\tilde Q}$ and $R_{\tilde Q}$ above. The **Hermitian sandwich** is

$$
\Theta_{\tilde Q}=R_{\tilde Q^{*}}\circ L_{\tilde Q},
\qquad
\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*}.
$$

The general algebra of the one-sided operators, without the polar word, is in the mathematics corpus; the two-sided theory is the companion article. Here only the polar specialisation is treated.

## The One-Sided Operators

### Definition and Elementary Properties

**Proposition.** Let $\tilde Q_1,\tilde Q_2\in\mathbb{B}$. Then:

**(a)** $L_{\tilde Q_1}$ and $R_{\tilde Q_1}$ are $\mathbb{C}$-linear;

**(b)** $L_{\tilde Q_1}\circ L_{\tilde Q_2}=L_{\tilde Q_1\tilde Q_2}$ and $R_{\tilde Q_1}\circ R_{\tilde Q_2}=R_{\tilde Q_2\tilde Q_1}$;

**(c)** $L_{\tilde Q_1}\circ R_{\tilde Q_2}=R_{\tilde Q_2}\circ L_{\tilde Q_1}$;

**(d)** the parameter maps $\tilde Q\mapsto L_{\tilde Q}$ and $\tilde Q\mapsto R_{\tilde Q}$ are injective;

**(e)** $L_{\tilde Q}$ and $R_{\tilde Q}$ are invertible exactly when $\tilde Q$ is a unit, with $L_{\tilde Q}^{-1}=L_{\tilde Q^{-1}}$ and $R_{\tilde Q}^{-1}=R_{\tilde Q^{-1}}$.

*Proof.* (a) The product is $\mathbb{C}$-bilinear. (b) and (c) are associativity. (d) $L_{\tilde Q}=0$ forces $\tilde Q=L_{\tilde Q}(e_t)=0$, and $R_{\tilde Q}=0$ forces $\tilde Q=R_{\tilde Q}(e_t)=0$. (e) $L_{\tilde Q}L_{\tilde Q^{-1}}=L_{e_t}=\mathrm{id}$ and $R_{\tilde Q}R_{\tilde Q^{-1}}=R_{e_t}=\mathrm{id}$; a non-unit is a zero divisor, so it cannot be invertible.

**Remark (multiplicativity).** The map $\tilde Q\mapsto L_{\tilde Q}$ is multiplicative into $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, but a single $L_{\tilde Q}$ is rarely an algebra endomorphism: $L_{\tilde Q}(XY)=\tilde QXY$ while $L_{\tilde Q}(X)L_{\tilde Q}(Y)=\tilde QX\tilde QY$, so multiplicativity forces $\tilde Q$ to be a central idempotent. In $\mathbb{B}$ the central idempotents are $0$ and $e_t$, so the only nonzero multiplicative left multiplication is the identity. The representation property is the composition law (b), not the multiplicativity of each $L_{\tilde Q}$.

**Remark (linear versus quadratic).** The map $\tilde Q\mapsto L_{\tilde Q}$ is linear and faithful. The map $\tilde Q\mapsto\Theta_{\tilde Q}$ is quadratic, and on the unit group its kernel is $U(1)$, as the companion article proves. The one-sided operator carries the whole parameter; the two-sided operator carries the parameter up to a central phase. This is the first reason the phase is visible one-sided and invisible two-sided.

**Remark (left translation, not conjugation).** $L_{\tilde Q}$ is a left translation of the algebra. It is an automorphism only for a central parameter. The sandwich is an inner conjugation only when $\tilde Q\tilde Q^{*}=e_t$, where the right factor is the inverse; for a general polar element it is a congruence by $B$ and a conjugation by $\tilde q$. The two-sided article treats that distinction in full.

### The Factorisation Through the Polar Word

**Proposition.** With $\tilde Q=r\exp(i\alpha)B\tilde q$,

$$
L_{\tilde Q}=L_{r\exp(i\alpha)}\circ L_B\circ L_{\tilde q},
\qquad
R_{\tilde Q}=R_{\tilde q}\circ R_B\circ R_{r\exp(i\alpha)},
$$

and the modulus acts on either side by the same scalar,

$$
L_{r\exp(i\alpha)}=R_{r\exp(i\alpha)}=r\exp(i\alpha)\,\mathrm{id}.
$$

*Proof.* The identities are the composition laws (b), read on the word. The modulus is central, so $L_{\rho}(X)=\rho X=X\rho=R_{\rho}(X)$.

**Remark (the order).** In the left reading the rightmost factor of the word acts first: the rotor, then the boost factor, then the modulus. In the right reading the order is reversed: the modulus, then the boost factor, then the rotor, because the parameter sits on the right. The two-sided sandwich uses both readings: the left action of the word and the right action of its conjugate.

**Remark (the complex exponent).** The modulus is a single complex scalar, $\rho=r\exp(i\alpha)$. Its left multiplication is the operator $\exp(\ln r+i\alpha)\,\mathrm{id}$. The exponent is the complex number $\ln\rho=\ln r+i\alpha$; the real part is the scale and the imaginary part is the phase. The one-sided operator keeps both. The two-sided sandwich keeps only $2\ln r$ and cancels the imaginary part.

The four factors are collected in the following table. A factor **preserves** a sector when it maps the sector into itself, **exchanges** the two sectors when it maps one onto the other, and **mixes** them when some element of a sector has a nonzero component in both sectors after the multiplication.

| factor | one-sided operator | sector action | factor on $N$ |
|---|---|---|---|
| scale $r$ | $r\,\mathrm{id}$ | preserves both | $r^{2}$ |
| phase $\exp(i\alpha)$ | $\exp(i\alpha)\,\mathrm{id}$ | preserves at $\alpha\equiv0\pmod{\pi}$, exchanges at $\alpha\equiv\tfrac{\pi}{2}\pmod{\pi}$, mixed otherwise | $\exp(2i\alpha)$ |
| boost $B$ | $L_B$ | mixes for $\psi>0$ | $1$ |
| rotor $\tilde q$ | $L_{\tilde q}$ | mixes for $\theta\not\equiv0\pmod{2\pi}$ | $1$ |

The table is justified factor by factor below; the phase row is the subject of §*The Pure Central Phase of $\pi/2$*, and the two mixing rows are the subject of §*The Four Factors, One-Sided*.

### The Norm and the Determinant

**Proposition.** For all $\tilde Q,X\in\mathbb{B}$,

$$
N\bigl(L_{\tilde Q}X\bigr)=N(\tilde Q)\,N(X)=\rho^{2}N(X),
\qquad
N\bigl(R_{\tilde Q}X\bigr)=N(\tilde Q)\,N(X),
$$

and the complex determinant and the trace of the left multiplication are

$$
\det_{\mathbb{C}}L_{\tilde Q}=N(\tilde Q)^{2}=\rho^{4},\qquad
\operatorname{tr}L_{\tilde Q}=4Q_t.
$$

*Proof.* The norm is multiplicative. In the matrix model $L_{\tilde Q}$ is $X\mapsto\mathsf M_2(\tilde Q)X$, the left multiplication by $\mathsf M_2(\tilde Q)$ on $M_2(\mathbb{C})$, which is $\mathsf M_2(\tilde Q)\otimes I_2$; its determinant is $\det\mathsf M_2(\tilde Q)^{2}=N(\tilde Q)^{2}$ and its trace is $2\operatorname{tr}\mathsf M_2(\tilde Q)=4Q_t$. The right multiplication is the mirror, with the same determinant and trace.

**Corollary (the complex similarity).** The one-sided operator multiplies the complex quadratic form $N$ by $\rho^{2}$. On the norm-one slice $N=1$ it is $\mathbb{C}$-orthogonal: it preserves $N$ and has complex determinant $1$. It is not, in general, an isometry of either real form $\mathbb{M}_\pm$.

The last clause is the subject of the next section: a complex isometry can exchange the two real forms, and the phase does exactly that.

## The Two Real Forms

### The Block Decomposition

**Definition.** For a parameter $\tilde Q$ the **symmetrized** and the **skew-symmetrized** multiplication operators are

$$
D_{\tilde Q}(X)=\tfrac12\bigl(\tilde QX+X\tilde Q^{*}\bigr),\qquad
O_{\tilde Q}(X)=\tfrac12\bigl(\tilde QX-X\tilde Q^{*}\bigr).
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

*Proof.* Let $X=X_++X_-$ with $X_\pm\in\mathbb{M}_\pm$. Then $X^{*}=X_+-X_-$, so

$$
(\tilde QX)^{*}=X^{*}\tilde Q^{*}=(X_+-X_-)\tilde Q^{*}.
$$

The projections on the two sectors are $Y_\pm=\tfrac12(Y\pm Y^{*})$. Hence

$$
(\tilde QX)_+
=\tfrac12\bigl[\tilde Q(X_++X_-)+(X_+-X_-)\tilde Q^{*}\bigr]
=D_{\tilde Q}(X_+)+O_{\tilde Q}(X_-),
$$

and

$$
(\tilde QX)_-
=\tfrac12\bigl[\tilde Q(X_++X_-)-(X_+-X_-)\tilde Q^{*}\bigr]
=O_{\tilde Q}(X_+)+D_{\tilde Q}(X_-).
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

*Proof.* $D_c(X)=\tfrac12(cX+X\bar c)=\operatorname{Re}(c)X$ and $O_c(X)=\tfrac12(cX-X\bar c)=i\operatorname{Im}(c)X$.

**Remark (the off-diagonal block).** The block $O_{\tilde Q}$ is the skew-symmetrized part of the multiplication. It vanishes for a real scalar, and for a central imaginary scalar it is the complex structure times the imaginary part. It is the part of the multiplication that changes the sector, and it is the part that the two-sided sandwich removes: the product $L_{\tilde Q}R_{\tilde Q^{*}}$ is block diagonal, because the right factor restores the sector that the left factor changes.

### The Sector Criterion

**Proposition (which parameters preserve a sector).** The left multiplication $L_{\tilde Q}$ preserves each of $\mathbb{M}_+$ and $\mathbb{M}_-$ exactly when $\tilde Q$ is a real scalar. It exchanges the two sectors exactly when $\tilde Q$ is a nonzero purely imaginary scalar. For every other parameter it mixes them.

*Proof.* Suppose first that $L_{\tilde Q}(\mathbb{M}_-)\subseteq\mathbb{M}_-$. For every anti-Hermitian $X$,

$$
(\tilde QX)^{*}=-\tilde QX.
$$

But $(\tilde QX)^{*}=X^{*}\tilde Q^{*}=-X\tilde Q^{*}$, so the condition is

$$
X\tilde Q^{*}=\tilde QX
$$

for every anti-Hermitian $X$. Taking $X=ie_t$ gives $i\tilde Q^{*}=i\tilde Q$, hence $\tilde Q^{*}=\tilde Q$. Taking $X=\vec e_x$ gives $\vec e_x\tilde Q=\tilde Q\vec e_x$, so $\tilde Q$ commutes with $\vec e_x$; the same holds with $\vec e_y$ and $\vec e_z$. A Hermitian element commuting with the three vector units is a real scalar: commuting with $\vec e_x$ forces the $\vec e_y$ and $\vec e_z$ coefficients to vanish, and then commuting with $\vec e_y$ forces the $\vec e_x$ coefficient to vanish. The converse is immediate.

Suppose next that $L_{\tilde Q}(\mathbb{M}_-)\subseteq\mathbb{M}_+$. Then $(\tilde QX)^{*}=+\tilde QX$ for every anti-Hermitian $X$, so $-X\tilde Q^{*}=\tilde QX$, that is

$$
X\tilde Q^{*}=-\tilde QX.
$$

Taking $X=ie_t$ gives $i\tilde Q^{*}=-i\tilde Q$, hence $\tilde Q^{*}=-\tilde Q$. Taking $X=\vec e_x$ gives $\vec e_x(-\tilde Q)=-\tilde Q\vec e_x$, that is $\vec e_x\tilde Q=\tilde Q\vec e_x$; the same holds with $\vec e_y$ and $\vec e_z$. An anti-Hermitian element commuting with the three vector units is a purely imaginary scalar, by the same coefficient argument. The converse is immediate.

If $\tilde Q$ is neither a real scalar nor a purely imaginary scalar, then $L_{\tilde Q}(\mathbb{M}_-)$ is contained neither in $\mathbb{M}_-$ nor in $\mathbb{M}_+$. The sets of $X\in\mathbb{M}_-$ whose image has zero $\mathbb{M}_+$ component and zero $\mathbb{M}_-$ component are real linear subspaces; if neither is all of $\mathbb{M}_-$, their union cannot cover $\mathbb{M}_-$. Hence some $X$ has both components nonzero, and the multiplication mixes the sectors.

**Corollary (the only one-sided Lorentz transformations).** Among the units, the real scalars are the only left multiplications that preserve $\mathbb{M}_-$, and among them the only isometries of $g$ are $\pm\mathrm{id}$. The one-sided action therefore gives no nontrivial real Lorentz transformation of $\mathbb{M}_-$; the real Lorentz group is the image of the two-sided sandwich, not of the one-sided operator.

**Physical reading.** A spinor is multiplied on one side; a four-vector is a bilinear object and is acted on by two sides. The one-sided multiplication can therefore move an element between the material and the informational sectors; it is not the four-vector action. The four-vector action is the sandwich of the companion article, and it preserves the sectors.

## The Pure Central Phase of $\pi/2$

### The Operator

**Definition.** The **pure central phase of $\pi/2$** is the factor $P=\exp(i\pi/2)=i$, and its operator is

$$
J=L_i=R_i,\qquad J(X)=iX.
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

*Proof.* For $X\in\mathbb{M}_-$,

$$
(iX)^{*}=-iX^{*}=-i(-X)=iX,
$$

so $iX\in\mathbb{M}_+$. The map $X\mapsto iX$ is injective and $\mathbb{M}_-$ and $\mathbb{M}_+$ are both real four-dimensional, so $i\mathbb{M}_-=\mathbb{M}_+$. The same computation with $X\in\mathbb{M}_+$ gives $i\mathbb{M}_+=\mathbb{M}_-$. The powers follow from $i^{2}=-1$ and the centrality of $i$.

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

Let $X\in\mathbb{M}_-$ be written as $X=ia\,e_t+\vec b$ with $a\in\mathbb{R}$ and $\vec b\in\mathbb{R}^{3}$. Then

$$
iX=i(ia\,e_t+\vec b)=-a\,e_t+i\vec b.
$$

The result is the element of $\mathbb{M}_+$ with scalar coordinate $-a$ and vector coordinate $\vec b$. In the pair $(a,\vec b)$ the exchange is therefore the **time reflection**

$$
(a,\vec b)\longmapsto(-a,\vec b).
$$

The following table records the two coordinate descriptions; the first column is the element of $\mathbb{M}_-$ and the second its image in $\mathbb{M}_+$.

| $X\in\mathbb{M}_-$ | $iX\in\mathbb{M}_+$ |
|---|---|
| $ia\,e_t+\vec b$ | $-a\,e_t+i\vec b$ |

The Minkowski form on the two sectors is

$$
g(X)=a^{2}-\lvert\vec b\rvert^{2}\quad(X\in\mathbb{M}_-),\qquad
g(Y)=a^{2}-\lvert\vec b\rvert^{2}\quad(Y=a\,e_t+i\vec b\in\mathbb{M}_+).
$$

With this convention

$$
g(iX)=g(X),
$$

so $J$ is an isometry between $(\mathbb{M}_-,g)$ and $(\mathbb{M}_+,g)$. In the coordinates above its determinant is $-1$: it is the improper isometry that reverses the time direction and fixes the three space directions. It is the discrete symmetry that exchanges the two real forms, not a proper Lorentz transformation of either one.

**Remark (the norm sign).** The complex norm changes sign,

$$
N(iX)=i^{2}N(X)=-N(X).
$$

On $\mathbb{M}_-$ one has $N=-g$, and on $\mathbb{M}_+$ one has $N=+g$. The minus sign in $N(iX)=-N(X)$ is therefore the change of the sector convention, not a failure of the isometry: the form $g$ is preserved.

**Physical reading.** In the physical interpretation of the corpus, $\mathbb{M}_-$ is the material sector and $\mathbb{M}_+$ the informational sector. The phase of $\pi/2$ exchanges the two: it turns an anti-Hermitian element into a Hermitian one and back. The exchange is the discrete operation of the algebra that the two-sided sandwich cannot see, because the sandwich multiplies by $i$ on the left and by $-i$ on the right. The full Wick rotation of the physics articles is a different operation: it acts on the time coefficient alone and maps $\mathbb{M}_-$ to the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, not to $\mathbb{M}_+$. The operator $J$ is the sector exchange, not the whole Wick rotation.

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

For $X\in\mathbb{M}_-$ the image $Y=\exp(i\alpha)X$ satisfies

$$
Y^{*}=-\exp(-2i\alpha)\,Y.
$$

Hence $Y\in\mathbb{M}_+$ exactly when $\alpha\equiv\tfrac{\pi}{2}\pmod{\pi}$, and $Y\in\mathbb{M}_-$ exactly when $\alpha\equiv0\pmod{\pi}$. For every other $\alpha$ the image lies in the real four-dimensional subspace $\exp(i\alpha)\mathbb{M}_-$, on which $*$ acts by the scalar $-\exp(-2i\alpha)$; that subspace is neither $\mathbb{M}_+$ nor $\mathbb{M}_-$.

*Proof.* The scalar is central, so $L_{P_\alpha}=R_{P_\alpha}=\exp(i\alpha)\mathrm{id}$. The block matrix is the corollary of the block decomposition with $c=\exp(i\alpha)$. For the eigenvalue, $Y^{*}=\exp(-i\alpha)X^{*}=-\exp(-i\alpha)X=-\exp(-2i\alpha)Y$. The two sector values are the two solutions of $-\exp(-2i\alpha)=\pm1$.

**Corollary (the special angles).** The phase preserves each sector at $\alpha=0$ and $\alpha=\pi$, where it is $+\mathrm{id}$ and $-\mathrm{id}$. It exchanges the two sectors at $\alpha=\pi/2$ and $\alpha=3\pi/2$, where it is $i$ and $-i$. At $\alpha=\pi/4$ it is a square root of the exchange,

$$
L_{\exp(i\pi/4)}^{2}=L_i,
$$

and the image of $\mathbb{M}_-$ is the mixed real four-dimensional subspace on which $*$ acts by $i$.

*Proof.* The values at the four angles are immediate from the block matrix. The square is $L_{\exp(i\pi/2)}=L_i$ by the composition law.

**Remark (the period).** The operator $L_{P_\alpha}$ has period $2\pi$ in $\alpha$. The sector behaviour has period $\pi$, because $\exp(i(\alpha+\pi))=-\exp(i\alpha)$ multiplies the operator by $-1$ and leaves the eigenvalue $-\exp(-2i\alpha)$ unchanged. The exchange therefore occurs on the two classes $\alpha\equiv\pi/2\pmod{\pi}$, and the preservation on the two classes $\alpha\equiv0\pmod{\pi}$.

**Remark (not a half-angle).** The polar word stores the phase as $\exp(i\alpha)$, with $\alpha=\tfrac12\arg N(\tilde Q)$. The pure phase of $\pi/2$ is therefore $i=\exp(i\pi/2)$, not $\exp(i\pi/4)$. The half-angle $\exp(i\pi/4)$ is the square root of the exchange, not the exchange itself. A half-angle convention would rename the angle of the exchange to $\pi$; it would not change the operator, only the name of its parameter.

### The Cancellation in the Two-Sided Operator

**Proposition.** The two-sided sandwich of the pure phase is the identity:

$$
\Theta_i(X)=iX(-i)=X,\qquad
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

*Proof.* The scalar $i$ is central, so the two factors commute with $X$ and with each other, and $i(-i)=1$. The block product is the same computation with the two off-diagonal exchanges.

**Remark (the two readings of the same word).** The one-sided operator of the phase is $\exp(i\alpha)\mathrm{id}$; the two-sided operator is the identity. The one-sided operator sees the whole complex modulus $\rho=r\exp(i\alpha)$; the two-sided operator sees only its modulus $r$ and the two non-central factors. The cancellation is the product of the left factor $\exp(i\alpha)$ and the right factor $\exp(-i\alpha)$; it is exact because the two scalars are central and inverse. The phase is not halved in either reading; it is either kept whole, one-sided, or cancelled whole, two-sided.

## The Four Factors, One-Sided

### The Scale

The scale is $r=\exp(\ln r)$, positive, real and central. Its one-sided operators are

$$
L_r=R_r=r\,\mathrm{id}.
$$

In the block decomposition $D_r=r\,\mathrm{id}$ and $O_r=0$: the scale preserves both sectors and multiplies every coordinate by $r$. The norm is multiplied by $r^{2}$, and the exponent is

$$
\ln r\longmapsto\ln r.
$$

The one-sided operator does not double the exponent. The doubling $2\ln r$ belongs to the two-sided sandwich, where the scale appears twice, once on each side. The determinant of $L_r$ is $r^{4}$ on the complex four-space and $r^{8}$ on the real eight-space.

### The Boost

The boost factor is

$$
B=\exp(-i\psi\vec u_{\mathrm b})
=\cosh\psi\,e_t-i\sinh\psi\,\vec u_{\mathrm b},
\qquad \psi\ge0,\qquad \lvert\vec u_{\mathrm b}\rvert=1.
$$

It is Hermitian and of norm one. Write $c=\cosh\psi$, $s=\sinh\psi$, $\vec u=\vec u_{\mathrm b}$, and let $X=ia\,e_t+\vec b$ be an element of $\mathbb{M}_-$. Then

$$
BX=i\bigl(ac+s\,\vec u\cdot\vec b\bigr)e_t
-i s\,\vec u\times\vec b
+c\,\vec b+s a\,\vec u.
$$

The term $-i s\,\vec u\times\vec b$ is the whole $\mathbb{M}_+$ part, an imaginary vector. The remaining terms $i(ac+s\,\vec u\cdot\vec b)e_t+c\vec b+s a\,\vec u$ are the $\mathbb{M}_-$ part, an imaginary scalar plus the real vector $c\vec b+s a\,\vec u$. The boost therefore mixes the two sectors in general. For $a=0$ the $\mathbb{M}_-$ part is $c\vec b+i s(\vec u\cdot\vec b)e_t$ and the $\mathbb{M}_+$ part is $-i s\,\vec u\times\vec b$, which vanishes only when $\vec b$ is parallel to $\vec u$. For $\vec b=0$ the image is $i a(c\,e_t+i s\,\vec u)=i a c\,e_t-s a\,\vec u$, entirely in $\mathbb{M}_-$: the central imaginary line is mapped into the two-plane spanned by $i e_t$ and $\vec u$.

The boost factor is of norm one, so $L_B$ preserves the complex norm, $N(L_BX)=N(X)$, and is $\mathbb{C}$-orthogonal. It is not a real Lorentz transformation of $\mathbb{M}_-$: it does not preserve the sector, and the only one-sided real Lorentz transformations are $\pm\mathrm{id}$, by the sector criterion.

**Physical reading.** The word's factor $B$ is the inverse square of the frame rotor $\tilde U_{\mathrm L}$. The one-sided operator $L_B$ is not the physical four-vector boost; that is the two-sided congruence by $\tilde U_{\mathrm L}$. It is the spinor multiplication by the positive Hermitian factor, and it mixes the two real forms because a spinor has no separate material and informational components.

### The Rotor

The rotor is

$$
\tilde q=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr)
=\cos\frac{\theta}{2}\,e_t+\sin\frac{\theta}{2}\,\vec u_{\mathrm r},
\qquad \theta\in[0,2\pi],\qquad \lvert\vec u_{\mathrm r}\rvert=1.
$$

It is a real quaternion, of norm one, and unitary. Write $c=\cos\tfrac{\theta}{2}$, $s=\sin\tfrac{\theta}{2}$, $\vec u=\vec u_{\mathrm r}$, and let $X=ia\,e_t+\vec b$ be an element of $\mathbb{M}_-$. Then

$$
\tilde qX
=-s\,\vec u\cdot\vec b\,e_t
+i a s\,\vec u
+i a c\,e_t
+c\,\vec b
+s\,\vec u\times\vec b.
$$

The first two terms are in $\mathbb{M}_+$: a real scalar and an imaginary vector. The last two terms are in $\mathbb{M}_-$: an imaginary scalar and the real vector $c\vec b+s\,\vec u\times\vec b$. The rotor mixes the two sectors in general. For $a=0$ the $\mathbb{M}_+$ part is the real scalar $-s\,\vec u\cdot\vec b$, which vanishes only when $\vec b$ is perpendicular to $\vec u$; the $\mathbb{M}_-$ part is the real vector $c\vec b+s\,\vec u\times\vec b$.

The rotor is of norm one, so $L_{\tilde q}$ preserves the complex norm and is $\mathbb{C}$-orthogonal. It also preserves the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ and its imaginary multiple $i\mathbb{H}_{\mathbb{B}}$, because it is a real quaternion and left multiplication by a real quaternion preserves the subalgebra $\mathbb{H}_{\mathbb{B}}$ and the module $i\mathbb{H}_{\mathbb{B}}$. On $\mathbb{H}_{\mathbb{B}}$ it is an isometry of the Euclidean norm. It does not preserve $\mathbb{M}_\pm$.

**Physical reading.** The rotor is the spin rotation. It is real, so it preserves the real quaternion subspace; the complex structure $i$ is central, so it preserves the imaginary multiple as well. It does not preserve the material and informational sectors, because those are defined by the Hermitian conjugation and the rotor multiplies only one side.

### The Bookkeeping

The following table collects the exponents. The **exponent** is the element $A$ such that the factor is $\exp(A)$; the **scalar parameter** is the real coefficient inside that exponential; the **one-sided output** is the exponent of the one-sided operator; and the **two-sided output** is the parameter of the corresponding transformation in the sandwich.

| factor | exponent $A$ | scalar parameter | one-sided output | two-sided output |
|---|---|---|---|---|
| scale $r$ | $\ln r$ | $\ln r$ | $\ln r$ | $2\ln r$ |
| phase $\exp(i\alpha)$ | $i\alpha$ | $\alpha$ | $i\alpha$ | $0$ |
| boost $B$ | $-i\psi\vec u_{\mathrm b}$ | $\psi$ | $-i\psi\vec u_{\mathrm b}$ | $-2\psi$ |
| frame rotor $\tilde U_{\mathrm L}$ | $+i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | $\tfrac{\psi}{2}$ | $+i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | $+\psi$ |
| rotor $\tilde q$ | $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | $\tfrac{\theta}{2}$ | $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | $\theta$ |

The rule is the number of slots. A one-sided operator is one factor of the word, so its exponent is the exponent of that factor: the scale keeps $\ln r$, the phase keeps $i\alpha$, the boost factor keeps the rapidity $\psi$ in $-i\psi\vec u_{\mathrm b}$, the frame rotor keeps the half-rapidity in $+i\tfrac{\psi}{2}\vec u_{\mathrm b}$, and the rotor keeps the half-angle in $\tfrac{\theta}{2}\vec u_{\mathrm r}$. A two-sided operator uses two slots, the parameter and its Hermitian conjugate. For the Hermitian factors the two exponents are equal and add, giving $2\ln r$ for the scale, $-2\psi$ for the boost factor and $+\psi$ for the frame rotor; for the unitary rotor they are opposite and the conjugation gives the angle $\theta$; for the central imaginary phase they cancel to $0$. The doubling of the companion article is therefore a two-slot phenomenon for the scale, the boost and the rotor, and the phase is its exceptional case.

## The Image and the Kernel

**Proposition.** Let $\tilde Q\in\mathbb{B}$.

**(a)** The parameter map $\tilde Q\mapsto L_{\tilde Q}$ is injective. The operator $L_{\tilde Q}$ is injective exactly when $\tilde Q$ is a unit.

**(b)** For a unit $\tilde Q$, $L_{\tilde Q}$ is a bijection of $\mathbb{B}$.

**(c)** For a nonzero null $\tilde Q$, the operator $L_{\tilde Q}$ has complex rank two, its kernel is the right annihilator $\{X:\tilde QX=0\}$ of complex dimension two, and its image is the right ideal $\tilde Q\mathbb{B}$ of complex dimension two.

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
| norm of the image | $\rho^{2}N(X)$ | $r^{4}N(X)$ |
| complex determinant | $\rho^{4}$ | $r^{8}$ |
| image on the units | $\cong GL(2,\mathbb{C})$, real dimension $8$ | $\cong CO^{+}(1,3)$, real dimension $7$ |
| kernel on the units | trivial | $U(1)$ |
| nonzero null parameter | rank $2$, right ideal | rank $1$, complex line |

**Corollary (the real forms are two-sided).** The only one-sided multiplications that preserve $\mathbb{M}_-$ are the real scalars, and among them the only isometries of $g$ are $\pm\mathrm{id}$. The one-sided action therefore does not give the Lorentz group on $\mathbb{M}_-$. The norm-one one-sided operators are $\mathbb{C}$-orthogonal. The proper orthochronous Lorentz group is not among them: it is the image of the two-sided sandwich on the norm-one slice, the identity component of the subgroup of the $\mathbb{C}$-orthogonal group that also preserves the two real forms.

**Physical reading.** The left multiplication is the action on a two-component spinor, by $\mathsf M_2(\tilde Q)$ on $\mathbb{C}^2$. The spinor is linear and sees the phase; the four-vector is the Hermitian bilinear of two spinors, and the induced action on it is the sandwich. The one-sided image is the whole $GL(2,\mathbb{C})$; the two-sided image is the conformal Lorentz group. The missing dimension is the phase. This is the operator statement of the physics distinction between a spinor and a four-vector.

## The Null Cone

On the null cone the polar word does not exist, but both one-sided operators do. Let $\tilde Q\neq0$ with $N(\tilde Q)=0$. In the matrix model $\mathsf M_2(\tilde Q)=uv^{*}$ with $u$ a nonzero column and $v^{*}$ a nonzero row. Then

$$
\mathsf M_2(L_{\tilde Q}X)=\mathsf M_2(\tilde Q)\,\mathsf M_2(X)=u\,(v^{*}\mathsf M_2(X)).
$$

The image consists of the matrices $u r^{*}$ with $r^{*}$ an arbitrary row, that is, the matrices all of whose columns lie in the complex line $\mathbb{C}u$. This is a right ideal of complex dimension two, not a line. The kernel is the set of $X$ with $v^{*}\mathsf M_2(X)=0$, of complex dimension two. The rank is two.

The sandwich of the same element is

$$
\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*}
=u\,(v^{*}\mathsf M_2(X)v)\,u^{*},
$$

a multiple of $uu^{*}=\mathsf M_2(\tilde Q\tilde Q^{*})$. Its image is the single complex line $\mathbb{C}\tilde Q\tilde Q^{*}$, and its rank is one. The one-sided operator keeps a two-dimensional right ideal; the two-sided operator collapses it to a line. The failure of invertibility is therefore different in the two readings: the one-sided operator loses half of the algebra, the two-sided operator loses all but one complex direction.

For the example $\tilde Q_0=e_t+i\vec e_x$ one has $N(\tilde Q_0)=0$, $\mathsf M_2(\tilde Q_0)=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ of rank one, and $\tilde Q_0\tilde Q_0^{*}=2\tilde Q_0$; the sandwich image is the line $\mathbb{C}\tilde Q_0$.

**Physical reading.** A lightlike four-momentum has no rest frame and no polar data. The one-sided operator still acts on the spinor, with a two-dimensional kernel; the two-sided operator collapses the algebra to the lightlike line.

## Worked Numbers

Take the same element as in the companion article:

$$
r=1.25,\qquad \alpha=0.3,\qquad \psi=0.5,\qquad \theta=0.7,
\qquad \vec u_{\mathrm b}=\vec e_x,\qquad \vec u_{\mathrm r}=\vec e_z,
$$

and

$$
\tilde Q=r\exp(i\alpha)B\tilde q,
$$

with coordinates

$$
Q_t=1.264938430+0.391291310i,\quad
Q_x=0.180822428-0.584549751i,
$$

$$
Q_y=-0.066005339+0.213377316i,\quad
Q_z=0.461738571+0.142832478i.
$$

The norm is $N(\tilde Q)=1.289586898+0.882253865i$, so $\rho=1.194170611+0.369400258i$, $r=1.25$ and $\alpha=0.3$.

Take $X=i e_t+0.6\vec e_x$. The two multiplications are

| coordinate | $L_{\tilde Q}(X)$ | $R_{\tilde Q}(X)$ |
|---|---|---|
| $e_t$ | $-0.499784767+1.615668281i$ | $-0.499784767+1.615668281i$ |
| $\vec e_x$ | $1.343512809+0.415597214i$ | $1.343512809+0.415597214i$ |
| $\vec e_y$ | $0.063665827+0.019694148i$ | $-0.490420459-0.151704825i$ |
| $\vec e_z$ | $-0.103229275+0.333712182i$ | $-0.182435681+0.589764961i$ |

The two agree in the scalar and $\vec e_x$ coordinates and differ in the transverse coordinates, as the non-commutativity of the two sides requires.

The sector split of the left multiplication is

$$
(L_{\tilde Q}X)_{\mathbb{M}_+}
=-0.499784767\,e_t
+i\bigl(0.415597214\vec e_x+0.019694148\vec e_y+0.333712182\vec e_z\bigr),
$$

$$
(L_{\tilde Q}X)_{\mathbb{M}_-}
=1.615668281\,i e_t
+1.343512809\vec e_x+0.063665827\vec e_y-0.103229275\vec e_z.
$$

The norm of the image is

$$
N\bigl(L_{\tilde Q}X\bigr)=-0.825335615-0.564642473i
=N(\tilde Q)N(X),
\qquad N(X)=-0.64.
$$

The trace and determinant of the left multiplication are

$$
\operatorname{tr}L_{\tilde Q}=5.059753720+1.565165240i=4Q_t,
\qquad
\det_{\mathbb{C}}L_{\tilde Q}=0.884662487+2.275486050i=\rho^{4}.
$$

The pure phase of $\pi/2$ is checked on $Z=2i e_t+\vec e_x+2\vec e_y+3\vec e_z$:

$$
iZ=-2\,e_t+i\bigl(\vec e_x+2\vec e_y+3\vec e_z\bigr),
$$

the time reflection of the coordinate pair, with the norm changing sign.

## Summary

The one-sided operators of the polar word are $L_{\tilde Q}(X)=\tilde QX$ and $R_{\tilde Q}(X)=X\tilde Q$. They are $\mathbb{C}$-linear, faithful in the parameter, and they multiply the complex norm by $\rho^{2}$. The left multiplication factorises as

$$
L_{\tilde Q}=L_{r\exp(i\alpha)}\circ L_B\circ L_{\tilde q},
$$

with $L_{r\exp(i\alpha)}=r\exp(i\alpha)\,\mathrm{id}$; the right multiplication is the mirror.

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

The pure central phase of $\pi/2$ is the exchange. The factor is $i$ or $-i$, the operator is $J(X)=iX$, and

$$
J(\mathbb{M}_-)=\mathbb{M}_+,\qquad J(\mathbb{M}_+)=\mathbb{M}_-,\qquad J^{2}=-\mathrm{id},\qquad J^{-1}=L_{-i}.
$$

In coordinates, $X=ia\,e_t+\vec b$ is sent to $-a\,e_t+i\vec b$: the time reflection $(a,\vec b)\mapsto(-a,\vec b)$, an improper isometry of the Minkowski form $g=a^{2}-\lvert\vec b\rvert^{2}$. The complex norm changes sign, $N(iX)=-N(X)$, because the two sectors carry opposite signs in $N$. For a general phase the block matrix is

$$
\begin{pmatrix}
\cos\alpha & i\sin\alpha\\
i\sin\alpha & \cos\alpha
\end{pmatrix},
$$

the image of $\mathbb{M}_-$ has $*$-eigenvalue $-\exp(-2i\alpha)$, and the sectors are reached exactly at $\alpha\equiv0$ and $\alpha\equiv\pi/2$ modulo $\pi$.

The scale acts as $r$, not $r^{2}$. The phase acts as $\exp(i\alpha)$, not as the identity. The boost factor and the rotor are $\mathbb{C}$-orthogonal and mix the sectors; their one-sided exponents are the rapidity $\psi$ in $-i\psi\vec u_{\mathrm b}$ and the half-angle $\tfrac{\theta}{2}\vec u_{\mathrm r}$, and the physical rapidity and angle are the two-sided outputs, with the frame rotor $\tilde U_{\mathrm L}$ carrying the physical rapidity $+\psi$. The one-sided operator has one slot and does not double; the two-sided operator has two slots and doubles the scale and the non-central exponents, while it cancels the central imaginary one.

The image of the one-sided action on the units is $\mathbb{B}^{\times}\cong GL(2,\mathbb{C})$, of real dimension eight, with trivial kernel. The image of the two-sided action is $CO^{+}(1,3)$, of real dimension seven, with kernel $U(1)$. The missing dimension is the phase. On the null cone the one-sided operator has rank two and image the right ideal $\tilde Q\mathbb{B}$; the sandwich has rank one and image the line $\mathbb{C}\tilde Q\tilde Q^{*}$.

The one-sided multiplication is a left translation of the algebra. The two-sided sandwich is the product of a left translation and a right translation, and it is that product which gives the real Lorentz transformations. The phase is the clearest witness: one-sided it is the exchange of the two real forms, two-sided it is the identity.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, with $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | the central scalar imaginary, $i^{2}=-1$ |
| $\tilde Q^{*}$ | the Hermitian conjugation $\overline{\tilde Q^{\natural}}$ |
| $\natural$, $\bar\cdot$ | the quaternion and coefficient conjugations |
| $\mathbb{M}_\pm$ | the Hermitian and anti-Hermitian subspaces, $X^{*}=\pm X$ |
| $\mathbb{H}_{\mathbb{B}}$ | the real quaternion subspace, all coefficients real |
| $L_{\tilde Q},R_{\tilde Q}$ | the left and right multiplications |
| $\Theta_{\tilde Q}=R_{\tilde Q^{*}}\circ L_{\tilde Q}$ | the two-sided Hermitian sandwich |
| $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | the complex norm |
| $\rho=r\exp(i\alpha)$ | the complex modulus, the principal square root of $N$ |
| $r>0$, $\alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$ | the scale and the phase angle |
| $B=\exp(-i\psi\vec u_{\mathrm b})$ | the positive Hermitian boost factor |
| $\tilde U_{\mathrm L}=B^{-1/2}=\exp(i\tfrac{\psi}{2}\vec u_{\mathrm b})$ | the frame rotor |
| $\tilde q=\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ | the unit real quaternion rotor |
| $D_{\tilde Q},O_{\tilde Q}$ | the symmetrized and skew-symmetrized multiplication blocks |
| $J=L_i=R_i$ | the pure central phase of $\pi/2$, the complex structure |
| $g$ | the Minkowski form, $N$ on $\mathbb{M}_+$ and $-N$ on $\mathbb{M}_-$ |
| $GL(2,\mathbb{C})$ | the image of the one-sided action on the units |
| $CO^{+}(1,3)$ | the image of the two-sided action on the units |
| $U(1)$ | the kernel of the two-sided action, the central unit circle |

## Further Reading

- *Two-Sided Operator Under the Polar Representation* (`articles_physics/two-sided-operator-under-the-polar-representation.md`), for the sandwich, the factor-by-factor doubling rule, the square-root rule for the boost and the cancellation of the phase.
- *The Action of the Polar Element Representation on the Hermitian and Anti-Hermitian Subspaces* (`articles_physics/the-action-of-the-polar-element-representation-on-the-hermitian-and-anti-hermitian-subspaces.md`), for the detailed action on the two sectors, the boost matrices and the frame rotor.
- *The Polar Decomposition of Biquaternions in Practice* (`articles_physics/the-polar-decomposition-of-biquaternions-in-practice.md`), for the algorithm that produces the four factors.
- *The Polar Element Representation and Remarkable Subspaces* (`articles_physics/the-polar-element-representation-and-remarkable-subspaces.md`), for the four exponents read against the six remarkable subspaces and the sector blocks.
- *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-cartan-hermitian-pairing-of-the-polar-element-representation-of-biquaternions.md`), for the positive-unitary decomposition.
- *The Polar Element Representation of Biquaternions* (`articles_maths/the-polar-element-representation-of-biquaternions.md`), for the four factors, the modulus, the branch and the domain.
- *One-Sided Operator Under the Polar Representation* (`articles_maths/one-sided-operator-under-the-polar-representation.md`), for the mathematics reference in the normalization $B=\tilde U_{\mathrm b}$.
- *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/the-spectra-of-the-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the left and right regular representations and the eigenvalues of the sandwich.
- *The Four-Vector Operator Representation of Biquaternions* (`articles_physics/the-four-vector-operator-representation-of-biquaternions.md`), for the sandwich written in the four complex coefficients.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the Lorentz group in biquaternionic form and the double cover.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* (`articles_physics/the-anti-hermitian-subspace-m-as-the-material-sector.md`) and *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* (`articles_physics/the-hermitian-subspace-m-plus-as-the-informational-sector.md`), for the physical interpretation of the two real forms exchanged by the phase.
