# __One-Sided Operators on the N-Regular Sector__

## Introduction

**The two projectors of the algebra.** Two endomorphisms of $\mathbb{B}$ are not of the polar family and are worth naming at the start, because they act on every sector: $P_{0}=\tfrac12(\mathrm{id}+\natural)$ and $P_{1}=\tfrac12(\mathrm{id}-\natural)$, with $P_{0}^{2}=P_{0}$, $P_{1}^{2}=P_{1}$, $P_{0}P_{1}=0$ and $P_{0}+P_{1}=\mathrm{id}$. Their images are the centre $\mathbb{C}e_t$ and the complexified vector part $\mathbb{C}\mathfrak{k}$, the two summands of the Clebsch–Gordan series $V_{1/2}\otimes V_{1/2}=V_{1}\oplus V_{0}$ of the algebra. They are canonical, they carry no parameter, and nothing in this article depends on them; they are named here because they are the only two idempotent endomorphisms that come with the algebra itself. The decomposition is *The Clebsch–Gordan Decomposition of the Biquaternion Algebra*.

The quaternion norm $N=\langle\tilde Q\rangle_{\natural}=Q_t^{2}+B^{2}$ splits the biquaternion algebra in two, and the split is the primary one for the operators: $N\neq0$ is the group of invertibles $\mathbb{B}^{\times}\cong GL(2,\mathbb{C})$, open and dense of real dimension eight, and $N=0$ is the null cone, closed of real dimension six. This article treats the first half.

Throughout, $\tilde Q$ lies in the **N-regular sector**, so $N\neq0$ and $\tilde Q$ is invertible. The biquaternion algebra acts on itself by left and right multiplication. For a parameter $\tilde Q$ the two **one-sided operators** are

$$
L_{\tilde Q}(\tilde X)=\tilde Q\tilde X,\qquad R_{\tilde Q}(\tilde X)=\tilde X\tilde Q .
$$

The two-sided operator of the polar decomposition is the product of the left action of $\tilde Q$ and the right action of $\tilde Q^{*}$, $\mathrm{Sd}_{\tilde Q}=R_{\tilde Q^{*}}\circ L_{\tilde Q}$, and its theory is *Two-Sided Operators on the N-Regular Sector*.

**What the norm decides, and what the vector form decides.** Inside the N-regular sector the second condition $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ cuts one wall, and the two sides of the wall behave differently in exactly one way. Everything global is fixed by $N$ alone: both operators are invertible, both have rank four, both have the whole algebra as image and zero as kernel, and the parameter map is faithful. The wall $B^{2}=0$ changes only the **eigenvalue count and the Jordan type**: off the wall there are two distinct eigenvalues and a semisimple operator, on the wall one repeated eigenvalue, and on the Jordan part of the wall two Jordan blocks of size two. That is the whole difference, and it is the reason the wall is a part of this article and not an article of its own.

**The complete polar decomposition.** The article reads the operators through it

$$
\tilde Q=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
=\varrho\exp(i\theta_{\mathrm{pha}})\exp\Bigl(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr)\exp\Bigl(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
\qquad \varrho\exp(i\theta_{\mathrm{pha}}),
$$

with $\varrho>0$, $\theta_{\mathrm{pha}}\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$, $\theta_{\mathrm{rpd}}\ge0$, $\theta_{\mathrm{axr}}\in[0,2\pi]$ and real unit axes $\vec u_{\mathrm b},\vec u_{\mathrm r}$, acting by a single multiplication, on the left or on the right, and the transformation it produces on a biquaternion.

The one-sided operator is the spinor action. Left multiplication by the rotor $\tilde u_{\mathrm r}$ has the eigenvalues $e^{\pm i\theta_{\mathrm{axr}}/2}$ on each Peirce column, and left multiplication by the boost $\tilde U_{\mathrm b}$ has $e^{\mp\theta_{\mathrm{rpd}}/2}$. Each Peirce column is one Weyl spinor, and the whole of $L$ is two copies of it. The two-sided operator pairs two such slots. The exponent reading of these eigenvalues — the half-angle, the half-rapidity and their doubling — is §*The Exponential of the One-Sided Operator* below and §*The Doubling Rule* of *Two-Sided Operators on the N-Regular Sector*.

The one-sided operator is $\mathbb{C}$-linear, and the map from the parameter to the operator is faithful. It multiplies the complex norm by $\varrho^{2}e^{2i\theta_{\mathrm{pha}}}$. It does not, in general, preserve the two real forms $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$. Its block form in the splitting $\mathbb{B}=\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$ is

$$
L_{\tilde Q}=
\begin{pmatrix}
D_{\tilde Q} & O_{\tilde Q}\\
O_{\tilde Q} & D_{\tilde Q}
\end{pmatrix},
$$

with the symmetrized and the antisymmetrized parts

$$
D_{\tilde Q}(\tilde X)=\tfrac12\bigl(\tilde Q\tilde X+\tilde X\tilde Q^{*}\bigr),\qquad
O_{\tilde Q}(\tilde X)=\tfrac12\bigl(\tilde Q\tilde X-\tilde X\tilde Q^{*}\bigr).
$$

The diagonal block $D_{\tilde Q}$ preserves each sector and the off-diagonal block $O_{\tilde Q}$ carries each sector into the other. For a central factor $c$ the two blocks are the scalars $\operatorname{Re}(c)$ and $i\operatorname{Im}(c)$.

The clearest case is the pure central phase of $\pi/2$. The factor is $i$, or $-i$, and the operator is

$$
L_i(\tilde X)=i\tilde X,\qquad i\mathbb{B}_{\Phi}=\mathbb{B}_{\Psi},\qquad i\mathbb{B}_{\Psi}=\mathbb{B}_{\Phi} .
$$

It is multiplication by the central imaginary, the complex structure $J$ of the algebra read over $\mathbb{R}$. It satisfies $J^{2}=-\mathrm{id}$ and $J^{-1}=J^{3}=L_{-i}$. The sign $i$ or $-i$ is the direction of the exchange. This is the operator that the two-sided operator cancels: $\mathrm{Sd}_i(\tilde X)=i\tilde X(-i)=\tilde X$. The one-sided operator sees the phase; the two-sided operator does not.

The plan is the following. §*Conventions* fixes the notation. §*The One-Sided Operators* gives the elementary properties and the factorisation through the polar word. §*The Eigenbasis and the Two Spinor Spaces* reads the eigenbasis, the two Peirce spinor spaces, and proves that the half-angle action on a spinor is the one-sided operator. §*The Two Real Forms* proves the block decomposition and the sector criterion. §*The Pure Central Phase of $\pi/2$* treats the exchange in detail, in coordinates and for a general phase. §*The Four Factors, One-Sided* reads the scale, the boost and the rotor. §*The Exponential of the One-Sided Operator* proves the element identity, the half-spin theorem and the exponent table. §*The Image and the Kernel* compares the one-sided and the two-sided images. §*The Wall $B^{2}=0$* treats the unipotent case, its Jordan structure and the shear that its exponential produces. §*The Boundary: the Null Cone* records the comparison with the N-degenerate article. The article closes with the summary, the notation and the readings.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, the product $\vec e_x\vec e_y=\vec e_z$ and the squares $\vec e_x^{2}=\vec e_y^{2}=\vec e_z^{2}=-e_t$. The scalar imaginary is $i$, central, $i^{2}=-1$. An element is $\tilde Q=Q_te_t+\vec Q$ with the four coefficients $Q_\mu$ complex.

The three conjugations are the quaternion conjugation $\natural$, the coefficient conjugation $\bar\cdot$ and their composite, the **Hermitian conjugation**

$$
\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\bar Q_te_t-\bar Q_x\vec e_x-\bar Q_y\vec e_y-\bar Q_z\vec e_z .
$$

The Hermitian and anti-Hermitian subspaces are

$$
\mathbb{B}_{\Psi}\cup\mathbb{B}_{\Phi}=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}.
$$

On $\mathbb{B}_{\Phi}$ an element is $\tilde Q_-=ia\,e_t+\vec b$ with $a\in\mathbb{R}$ and $\vec b$ a real vector; on $\mathbb{B}_{\Psi}$ an element is $\tilde Q_+=a\,e_t+i\vec b$ with the same real data. The two sectors are exchanged by multiplication by $i$, which is central. The **real quaternion subspace** is $\mathbb{B}_{H}=\{\tilde Q:Q_\mu\in\mathbb{R}\ \text{for all}\ \mu\}$; its imaginary multiple $\mathbb{B}_{iH}$ has all coefficients purely imaginary.

The **norm** is the complex number

$$
\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2},\qquad \tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}\,e_t ,
$$

and it is multiplicative, $\langle\tilde Q\tilde Q'\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}\langle\tilde Q'\rangle_{\natural}$. The polar word is

$$
\tilde Q=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},\qquad
\varrho\exp(i\theta_{\mathrm{pha}}),\qquad
\tilde U_{\mathrm b}=\exp\Bigl(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
$$

with $\varrho>0$, $\theta_{\mathrm{pha}}\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$, $\theta_{\mathrm{rpd}}\ge0$, $\theta_{\mathrm{axr}}\in[0,2\pi]$, and $\vec u_{\mathrm b},\vec u_{\mathrm r}$ real unit vectors. The modulus is $\varrho\,e^{i\theta_{\mathrm{pha}}}=\sqrt{\langle\tilde Q\rangle_{\natural}}$ on the principal branch, so $\varrho=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{1/2}$ and $\theta_{\mathrm{pha}}=\tfrac12\arg \langle\tilde Q\rangle_{\natural}$. The factors satisfy

$$
\varrho^{*}=\varrho,\qquad \tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b},\qquad \tilde u_{\mathrm r}^{*}=\tilde u_{\mathrm r}^{\natural}=\tilde u_{\mathrm r}^{-1},\qquad \langle\tilde U_{\mathrm b}\rangle_{\natural}=\langle\tilde u_{\mathrm r}\rangle_{\natural}=1 .
$$

The matrix model is $\mathsf M_2:\mathbb{B}\to M_2(\mathbb{C})$, with $\mathsf M_2(e_t)=I_2$ and $\mathsf M_2(\vec e_k)=-i\sigma_k$, the $\sigma_k$ being the Pauli matrices. It is $\mathbb{C}$-linear and satisfies $\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger}$, and its determinant is the norm, $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$.

The one-sided operators are $L_{\tilde Q}$ and $R_{\tilde Q}$ above. The **Hermitian pair** is

$$
\mathrm{Sd}_{\tilde Q}=R_{\tilde Q^{*}}\circ L_{\tilde Q},\qquad \mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}.
$$

The general algebra of the one-sided operators, without the polar word, is *One-Sided Operators on the General Plain Sesqualgebra*; the two-sided theory is *Two-Sided Operators on the General Plain Sesqualgebra*. Here only the polar specialisation is treated.

## The One-Sided Operators

### Definition and Elementary Properties

**Proposition.** Let $\tilde Q,\tilde Q'\in\mathbb{B}$. Then:

**(a)** $L_{\tilde Q}$ and $R_{\tilde Q}$ are $\mathbb{C}$-linear;

**(b)** $L_{\tilde Q}\circ L_{\tilde Q'}=L_{\tilde Q\tilde Q'}$ and $R_{\tilde Q}\circ R_{\tilde Q'}=R_{\tilde Q'\tilde Q}$;

**(c)** $L_{\tilde Q}\circ R_{\tilde Q'}=R_{\tilde Q'}\circ L_{\tilde Q}$;

**(d)** the parameter maps $\tilde Q\mapsto L_{\tilde Q}$ and $\tilde Q\mapsto R_{\tilde Q}$ are injective;

**(e)** $L_{\tilde Q}$ and $R_{\tilde Q}$ are invertible exactly when $\tilde Q$ is invertible, with $L_{\tilde Q}^{-1}=L_{\tilde Q^{-1}}$ and $R_{\tilde Q}^{-1}=R_{\tilde Q^{-1}}$.

*Proof.* (a) The product is $\mathbb{C}$-bilinear. (b) and (c) are associativity. (d) $L_{\tilde Q}=0$ forces $\tilde Q=L_{\tilde Q}(e_t)=0$, and $R_{\tilde Q}=0$ forces $\tilde Q=R_{\tilde Q}(e_t)=0$. (e) $L_{\tilde Q}L_{\tilde Q^{-1}}=L_{e_t}=\mathrm{id}$ and $R_{\tilde Q}R_{\tilde Q^{-1}}=R_{e_t}=\mathrm{id}$; a non-invertible is a zero divisor, so it cannot be invertible.

**Remark (multiplicativity).** The map $\tilde Q\mapsto L_{\tilde Q}$ is multiplicative into $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, but a single $L_{\tilde Q}$ is rarely an algebra endomorphism: $L_{\tilde Q}(\tilde X\tilde Y)=\tilde Q\tilde X\tilde Y$ while $L_{\tilde Q}(\tilde X)L_{\tilde Q}(\tilde Y)=\tilde Q\tilde X\tilde Q\tilde Y$, so multiplicativity forces $\tilde Q$ to be a central idempotent. In $\mathbb{B}$ the central idempotents are $0$ and $e_t$, so the only nonzero multiplicative left multiplication is the identity. The representation property is the composition law (b), not the multiplicativity of each $L_{\tilde Q}$.

**Remark (linear versus quadratic).** The map $\tilde Q\mapsto L_{\tilde Q}$ is linear and faithful. The map $\tilde Q\mapsto\mathrm{Sd}_{\tilde Q}$ is quadratic, and on the group of invertibles its kernel is $U(1)$, as the companion article proves. The one-sided operator carries the whole parameter; the two-sided operator carries the parameter up to a central phase. This is the first reason the phase is visible one-sided and invisible two-sided.

**Remark (left translation, not conjugation).** $L_{\tilde Q}$ is a left translation of the algebra. It is an automorphism only for a central parameter. The two-sided operator is an inner conjugation only when $\tilde Q\tilde Q^{*}=e_t$, where the right factor is the inverse; for a general invertible element it is a congruence by $\tilde U_{\mathrm b}$ and a conjugation by $\tilde u_{\mathrm r}$. The two-sided article treats that distinction in full.

### The Factorisation Through the Polar Word

**Proposition.** With $\tilde Q=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$,

$$
\boxed{\;L_{\tilde Q}=L_{\varrho\,e^{i\theta_{\mathrm{pha}}}}\circ L_{\tilde U_{\mathrm b}}\circ L_{\tilde u_{\mathrm r}},\qquad
R_{\tilde Q}=R_{\tilde u_{\mathrm r}}\circ R_{\tilde U_{\mathrm b}}\circ R_{\varrho\,e^{i\theta_{\mathrm{pha}}}}\;},
$$

and the modulus acts on either side by the same scalar,

$$
L_{\varrho\,e^{i\theta_{\mathrm{pha}}}}=R_{\varrho\,e^{i\theta_{\mathrm{pha}}}}=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\mathrm{id}.
$$

*Proof.* The identities are the composition laws (b), read on the word. The modulus is central, so $L_{\varrho\,e^{i\theta_{\mathrm{pha}}}}(\tilde X)=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde X=\tilde X\varrho\,e^{i\theta_{\mathrm{pha}}}=R_{\varrho\,e^{i\theta_{\mathrm{pha}}}}(\tilde X)$.

**Remark (the order).** In the left reading the rightmost factor of the word acts first: the rotor, then the boost, then the modulus. In the right reading the order is reversed: the modulus, then the boost, then the rotor, because the parameter sits on the right. The two-sided operator uses both readings: the left action of the word and the right action of its conjugate.

**Remark (the complex exponent).** The modulus is a single complex scalar, $\varrho\exp(i\theta_{\mathrm{pha}})$. Its left multiplication is the operator $\exp(\ln \varrho+i\theta_{\mathrm{pha}})\,\mathrm{id}$. The exponent is the complex number $\ln\varrho\,e^{i\theta_{\mathrm{pha}}}=\ln \varrho+i\theta_{\mathrm{pha}}$; the real part is the scale and the imaginary part is the phase. The one-sided operator keeps both. The two-sided operator keeps only $2\ln \varrho$ and cancels the imaginary part.

The four factors are collected in the following table. A factor **preserves** a sector when it maps the sector into itself, **exchanges** the two sectors when it maps one onto the other, and **mixes** them when some element of a sector has a nonzero component in both sectors after the multiplication.

| factor | one-sided operator | sector action | factor on $\langle\tilde Q\rangle_{\natural}$ |
|---|---|---|---|
| scale $\varrho$ | $\varrho\,\mathrm{id}$ | preserves both | $\varrho^{2}$ |
| phase $\exp(i\theta_{\mathrm{pha}})$ | $\exp(i\theta_{\mathrm{pha}})\,\mathrm{id}$ | preserves at $\theta_{\mathrm{pha}}\equiv0\pmod{\pi}$, exchanges at $\theta_{\mathrm{pha}}\equiv\tfrac{\pi}{2}\pmod{\pi}$, mixed otherwise | $\exp(2i\theta_{\mathrm{pha}})$ |
| boost $\tilde U_{\mathrm b}$ | $L_{\tilde U_{\mathrm b}}$ | mixes for $\theta_{\mathrm{rpd}}>0$ | $1$ |
| rotor $\tilde u_{\mathrm r}$ | $L_{\tilde u_{\mathrm r}}$ | mixes for $\theta_{\mathrm{axr}}\not\equiv0\pmod{2\pi}$ | $1$ |

The table is justified factor by factor below; the phase row is the subject of §*The Pure Central Phase of $\pi/2$*, and the two mixing rows are the subject of §*The Four Factors, One-Sided*.

### The Norm and the Determinant

**Proposition.** For all $\tilde Q,\tilde X$,

$$ \langle L_{\tilde Q}\tilde X\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}\,\langle \tilde X\rangle_{\natural}=\varrho^{2}e^{2i\theta_{\mathrm{pha}}}\langle \tilde X\rangle_{\natural},
\qquad
\langle R_{\tilde Q}\tilde X\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}\,\langle \tilde X\rangle_{\natural}, $$

and the complex determinant and the trace of the left multiplication are

$$
\boxed{\;\det_{\mathbb{C}}L_{\tilde Q}=\langle\tilde Q\rangle_{\natural}^{2}=\varrho^{4}e^{4i\theta_{\mathrm{pha}}},\qquad
\operatorname{tr}L_{\tilde Q}=4Q_t\;}.
$$

*Proof.* The norm is multiplicative. In the matrix model $L_{\tilde Q}$ is $\tilde X\mapsto\mathsf M_2(\tilde Q)\tilde X$, the left multiplication by $\mathsf M_2(\tilde Q)$ on $M_2(\mathbb{C})$, which is $\mathsf M_2(\tilde Q)\otimes I_2$; its determinant is $\det\mathsf M_2(\tilde Q)^{2}=\langle\tilde Q\rangle_{\natural}^{2}$ and its trace is $2\operatorname{tr}\mathsf M_2(\tilde Q)=4Q_t$. The right multiplication is the mirror, with the same determinant and trace.

**Corollary (the complex similarity).** The one-sided operator multiplies the complex quadratic form $\langle\cdot\rangle_{\natural}$ by $\varrho^{2}e^{2i\theta_{\mathrm{pha}}}$. On the norm-one slice $\langle\tilde X\rangle_{\natural}=1$ it is $\mathbb{C}$-orthogonal: it preserves $N$ and has complex determinant $1$. It is not, in general, an isometry of either real form, $\mathbb{B}_{\Psi}$ or $\mathbb{B}_{\Phi}$.

The last clause is the subject of the next section: a complex isometry can exchange the two real forms, and the phase does exactly that.

## The Eigenbasis and the Two Spinor Spaces

### The Eigenbasis

The eigenbasis of the left multiplication is that of *The N-Regular, Spectrally Regular Sector*, §*The Eigenbasis, the Nilpotents, and the Peirce Corners*. For $\tilde Q$ with $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}\neq0$, put
$$
\vec U=\frac{\vec Q}{B},\qquad \vec{Ζ}=-i\vec U,\qquad
\tilde\Pi_{\mathrm{id},\pm}=\frac{e_t\pm\vec{Ζ}}{2},\qquad
\lambda_\pm=Q_t\pm iB .
$$
Choose the nilpotents
$$
\vec\Pi_{\mathrm{nil},+}\in\mathbb{B}_{-+}=\tilde\Pi_{\mathrm{id},-}\mathbb{B}\tilde\Pi_{\mathrm{id},+},\qquad
\vec\Pi_{\mathrm{nil},-}\in\mathbb{B}_{+-}=\tilde\Pi_{\mathrm{id},+}\mathbb{B}\tilde\Pi_{\mathrm{id},-},
$$
normalised by
$$
\vec\Pi_{\mathrm{nil},+}\vec\Pi_{\mathrm{nil},-}=\tilde\Pi_{\mathrm{id},-},\qquad
\vec\Pi_{\mathrm{nil},-}\vec\Pi_{\mathrm{nil},+}=\tilde\Pi_{\mathrm{id},+},\qquad
\vec\Pi_{\mathrm{nil},\pm}^{2}=0 .
$$
Then the four basis elements $\tilde\Pi_{\mathrm{id},+},\vec\Pi_{\mathrm{nil},-},\vec\Pi_{\mathrm{nil},+},\tilde\Pi_{\mathrm{id},-}$ are eigenvectors of $L_{\tilde Q}$:
$$
\tilde Q\tilde\Pi_{\mathrm{id},+}=\lambda_+\tilde\Pi_{\mathrm{id},+},\qquad
\tilde Q\vec\Pi_{\mathrm{nil},-}=\lambda_+\vec\Pi_{\mathrm{nil},-},\qquad
\tilde Q\vec\Pi_{\mathrm{nil},+}=\lambda_-\vec\Pi_{\mathrm{nil},+},\qquad
\tilde Q\tilde\Pi_{\mathrm{id},-}=\lambda_-\tilde\Pi_{\mathrm{id},-} .
$$
In this ordered basis,
$$
[L_{\tilde Q}]=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-).
$$

The two values are distinct exactly when $B\neq0$. In that case the $\lambda_+$-eigenspace is the two-dimensional right ideal $\tilde\Pi_{\mathrm{id},+}\mathbb{B}$, with basis $(\tilde\Pi_{\mathrm{id},+},\vec\Pi_{\mathrm{nil},-})$, and the $\lambda_-$-eigenspace is $\tilde\Pi_{\mathrm{id},-}\mathbb{B}$, with basis $(\vec\Pi_{\mathrm{nil},+},\tilde\Pi_{\mathrm{id},-})$.

When $B=0$ the construction is unavailable: there is no eigenbasis singled out by $\tilde Q$, the two nilpotents are not defined from $\tilde Q$, and $L_{\tilde Q}$ is not diagonal in any Peirce basis. This is the degenerate case of *The Spectrum of a Biquaternion*, §*The Degenerate Case: The Spectral-Degenerate Cone*.

### The Two Chiral Spinor Spaces

The two **spinor spaces** are the Peirce carriers, which here are the minimal left ideals,
$$
S_+=\mathbb{B}\tilde\Pi_{\mathrm{id},+}=\mathbb{C}\tilde\Pi_{\mathrm{id},+}\oplus\mathbb{C}\vec\Pi_{\mathrm{nil},+},
\qquad
S_-=\mathbb{B}\tilde\Pi_{\mathrm{id},-}=\mathbb{C}\vec\Pi_{\mathrm{nil},-}\oplus\mathbb{C}\tilde\Pi_{\mathrm{id},-},
\qquad
\mathbb{B}=S_+\oplus S_- .
$$
A spinor of the first Peirce copy is an element of $S_+$; a spinor of the second Peirce copy is an element of $S_-$. In the eigenbasis $(\tilde\Pi_{\mathrm{id},+},\vec\Pi_{\mathrm{nil},+})$ of $S_+$,
$$
\zeta_+=\alpha\,\tilde\Pi_{\mathrm{id},++}\beta\,\vec\Pi_{\mathrm{nil},+},
\qquad
\tilde Q\zeta_+=\lambda_+\alpha\,\tilde\Pi_{\mathrm{id},++}\lambda_-\beta\,\vec\Pi_{\mathrm{nil},+},
$$
so
$$
[\zeta_+]\longmapsto
\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}
\begin{pmatrix}\alpha\\ \beta\end{pmatrix}.
$$
In the eigenbasis $(\vec\Pi_{\mathrm{nil},-},\tilde\Pi_{\mathrm{id},-})$ of $S_-$,
$$
\zeta_-=\gamma\,\vec\Pi_{\mathrm{nil},-+}\delta\,\tilde\Pi_{\mathrm{id},-},
\qquad
\tilde Q\zeta_-=\lambda_+\gamma\,\vec\Pi_{\mathrm{nil},-+}\lambda_-\delta\,\tilde\Pi_{\mathrm{id},-},
$$
and the same matrix appears:
$$
[\zeta_-]\longmapsto
\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}
\begin{pmatrix}\gamma\\ \delta\end{pmatrix}.
$$
Thus, in the ordered splitting $(S_+,S_-)$,
$$
\boxed{\;[L_{\tilde Q}]=\begin{pmatrix}\Delta&0\\0&\Delta\end{pmatrix},
\qquad \Delta=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}\; }.
$$
The one-sided operator therefore acts by the **same** diagonal matrix on the two spinor spaces and never mixes the two Peirce copies. The two copies are not an accident of notation: $S_+$ and $S_-$ are distinct minimal left ideals, and left multiplication preserves each of them separately. Neither $S_+$ nor $S_-$ is an eigenspace of $L_{\tilde Q}$: each carries both eigenvalues, and the eigenspaces of $L_{\tilde Q}$ are the right ideals $\tilde\Pi_{\mathrm{id},\pm}\mathbb{B}$ of §*The Eigenbasis*.

**The label is the Peirce index.** The words first and second copy name the two Peirce components $S_+$ and $S_-$; they are a copy label, not a Lorentz chirality. Both components carry the same spinor representation, and the two Lorentz chiralities are the two tensor slots of §*The Weight Relation and the Two Copies*.

In the eigenbasis matrix model $\mathsf M^{\tilde Q}$ — not the Pauli model $\mathsf M_2$ of §*Conventions* — with
$$
\tilde\Pi_{\mathrm{id},+}\mapsto E_{11},\quad
\vec\Pi_{\mathrm{nil},-}\mapsto E_{12},\quad
\vec\Pi_{\mathrm{nil},+}\mapsto E_{21},\quad
\tilde\Pi_{\mathrm{id},-}\mapsto E_{22},
$$
the first column is $S_+$ and the second column is $S_-$:
$$
S_+\longleftrightarrow\operatorname{span}\{E_{11},E_{21}\},
\qquad
S_-\longleftrightarrow\operatorname{span}\{E_{12},E_{22}\}.
$$
Multiplication by $\tilde Q$ is left multiplication by $\Delta$ on the matrix, hence the same $\Delta$ acts on each column. The two columns are the two Peirce copies; the one-sided operator sees one copy of $\Delta$ per column.

## The Two Real Forms

### The Block Decomposition

**Definition.** For a parameter $\tilde Q$ the **symmetrized** and the **antisymmetrized** multiplication operators are

$$
D_{\tilde Q}(\tilde X)=\tfrac12\bigl(\tilde Q\tilde X+\tilde X\tilde Q^{*}\bigr),\qquad
O_{\tilde Q}(\tilde X)=\tfrac12\bigl(\tilde Q\tilde X-\tilde X\tilde Q^{*}\bigr).
$$

**Proposition (the block form).** In the real splitting $\mathbb{B}=\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$, the left multiplication has the block form

$$
L_{\tilde Q}=
\begin{pmatrix}
D_{\tilde Q} & O_{\tilde Q}\\
O_{\tilde Q} & D_{\tilde Q}
\end{pmatrix}.
$$

The diagonal block $D_{\tilde Q}$ maps each sector into itself and the off-diagonal block $O_{\tilde Q}$ maps each sector into the other.

*Proof.* Let $\tilde X=\tilde X_++\tilde X_-$ with $\tilde X_\pm\in\mathbb{B}_{\Psi}\cup\mathbb{B}_{\Phi}$. Then $\tilde X^{*}=\tilde X_+-\tilde X_-$, so

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

**Remark (the off-diagonal block).** The block $O_{\tilde Q}$ is the antisymmetrized part of the multiplication. It vanishes for a real scalar, and for a central imaginary scalar it is the complex structure times the imaginary part. It is the part of the multiplication that changes the sector, and it is the part that the two-sided operator removes: the product $L_{\tilde Q}R_{\tilde Q^{*}}$ is block diagonal, because the right factor restores the sector that the left factor changes.

### The Sector Criterion

**Proposition (which parameters preserve a sector).** The left multiplication $L_{\tilde Q}$ preserves each of $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ exactly when $\tilde Q$ is a real scalar. It exchanges the two sectors exactly when $\tilde Q$ is a nonzero purely imaginary scalar. For every other parameter it mixes them.

*Proof.* Suppose first that $L_{\tilde Q}(\mathbb{B}_{\Phi})\subseteq\mathbb{B}_{\Phi}$. For every anti-Hermitian $\tilde X$,

$$
(\tilde Q\tilde X)^{*}=-\tilde Q\tilde X .
$$

But $(\tilde Q\tilde X)^{*}=\tilde X^{*}\tilde Q^{*}=-\tilde X\tilde Q^{*}$, so the condition is

$$
\tilde X\tilde Q^{*}=\tilde Q\tilde X
$$

for every anti-Hermitian $\tilde X$. Taking $\tilde X=ie_t$ gives $i\tilde Q^{*}=i\tilde Q$, hence $\tilde Q^{*}=\tilde Q$. Taking $\tilde X=\vec e_x$ gives $\vec e_x\tilde Q=\tilde Q\vec e_x$, so $\tilde Q$ commutes with $\vec e_x$; the same holds with $\vec e_y$ and $\vec e_z$. A Hermitian element commuting with the three vector units is a real scalar: commuting with $\vec e_x$ forces the $\vec e_y$ and $\vec e_z$ coefficients to vanish, and then commuting with $\vec e_y$ forces the $\vec e_x$ coefficient to vanish. The converse is immediate.

Suppose next that $L_{\tilde Q}(\mathbb{B}_{\Phi})\subseteq\mathbb{B}_{\Psi}$. Then $(\tilde Q\tilde X)^{*}=+\tilde Q\tilde X$ for every anti-Hermitian $\tilde X$, so $-\tilde X\tilde Q^{*}=\tilde Q\tilde X$, that is

$$
\tilde X\tilde Q^{*}=-\tilde Q\tilde X .
$$

Taking $\tilde X=ie_t$ gives $i\tilde Q^{*}=-i\tilde Q$, hence $\tilde Q^{*}=-\tilde Q$. Taking $\tilde X=\vec e_x$ gives $\vec e_x(-\tilde Q)=-\tilde Q\vec e_x$, that is $\vec e_x\tilde Q=\tilde Q\vec e_x$; the same holds with $\vec e_y$ and $\vec e_z$. An anti-Hermitian element commuting with the three vector units is a purely imaginary scalar, by the same coefficient argument. The converse is immediate.

**Corollary (the only one-sided Lorentz transformations).** Among the invertibles, the real scalars are the only left multiplications that preserve $\mathbb{B}_{\Phi}$, and among them the only isometries of $g$ are $\pm\mathrm{id}$. The one-sided action therefore gives no nontrivial real Lorentz transformation of $\mathbb{B}_{\Phi}$; the real Lorentz group is the image of the two-sided operator, not of the one-sided operator.

## The Pure Central Phase of $\pi/2$

### The Operator

**Definition.** The **pure central phase of $\pi/2$** is the factor $P=\exp(i\pi/2)=i$, and its operator is

$$
J=L_i=R_i,\qquad J(\tilde X)=i\tilde X .
$$

The phase of $-\pi/2$ is $-i$ and its operator is $J^{-1}=L_{-i}$. On the principal branch of the polar word only $\theta_{\mathrm{pha}}=\pi/2$ occurs; the sign $-i$ is the other square root and the inverse operator.

**Proposition.** The operator $J$ is $\mathbb{C}$-linear, exchanges the two real forms,

$$ J(\mathbb{B}_{\Phi})=\mathbb{B}_{\Psi},\qquad J(\mathbb{B}_{\Psi})=\mathbb{B}_{\Phi}, $$

and satisfies

$$
J^{2}=-\mathrm{id},\qquad J^{4}=\mathrm{id},\qquad J^{-1}=J^{3}=L_{-i}.
$$

*Proof.* For $\tilde X\in\mathbb{B}_{\Phi}$,

$$
(i\tilde X)^{*}=-i\tilde X^{*}=-i(-\tilde X)=i\tilde X,
$$

so $i\tilde X\in\mathbb{B}_{\Psi}$. The map $\tilde X\mapsto i\tilde X$ is injective and $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ are both real four-dimensional, so $i\mathbb{B}_{\Phi}=\mathbb{B}_{\Psi}$. The same computation with $\tilde X\in\mathbb{B}_{\Psi}$ gives $i\mathbb{B}_{\Psi}=\mathbb{B}_{\Phi}$. The powers follow from $i^{2}=-1$ and the centrality of $i$.

**Remark (the sign).** Both $i$ and $-i$ exchange the sectors, and they are inverse to each other. The sign selects which of the two inverse swaps is used; both exchange the same pair of sectors. The square of either is $-\mathrm{id}$, and the fourth power is the identity.

**Remark (the block matrix).** In the ordered splitting $(\mathbb{B}_{\Psi},\mathbb{B}_{\Phi})$ the operator is

$$
J=
\begin{pmatrix}
0 & i\\
i & 0
\end{pmatrix},
$$

the off-diagonal blocks being the multiplication by $i$ on each real four-dimensional sector. It is the block matrix of a swap times the complex structure. Its square is $-I_8$ and its fourth power is $I_8$.

**Remark (the complex structure).** Since $i$ is central, $J$ is the multiplication by the complex scalar $i$. As a complex-linear map it is the scalar $i$; as a real-linear map it is a complex structure on the eight-dimensional real space. The exchange of $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ is invisible to the complex-linear structure and visible only over $\mathbb{R}$. This is the precise sense in which the phase is a real operation and not a complex one.

### The Coordinate Form

Let $\tilde X\in\mathbb{B}_{\Phi}$ be written as $\tilde X=ia\,e_t+\vec b$ with $a\in\mathbb{R}$ and $\vec b\in\mathbb{R}^{3}$. Then

$$
i\tilde X=i(ia\,e_t+\vec b)=-a\,e_t+i\vec b .
$$

The result is the element of $\mathbb{B}_{\Psi}$ with scalar coordinate $-a$ and vector coordinate $\vec b$. In the pair $(a,\vec b)$ the exchange is therefore the **time reflection**

$$
(a,\vec b)\longmapsto(-a,\vec b).
$$

The following table records the two coordinate descriptions; the first column is the element of $\mathbb{B}_{\Phi}$ and the second its image in $\mathbb{B}_{\Psi}$.

| $\tilde X\in\mathbb{B}_{\Phi}$ | $i\tilde X\in\mathbb{B}_{\Psi}$ |
|---|---|
| $ia\,e_t+\vec b$ | $-a\,e_t+i\vec b$ |

The Minkowski form on the two sectors is

$$
g(\tilde X)=a^{2}-\lvert\vec b\rvert^{2}\quad(\tilde X\in\mathbb{B}_{\Phi}),\qquad
g(\tilde Y)=a^{2}-\lvert\vec b\rvert^{2}\quad(\tilde Y=a\,e_t+i\vec b\in\mathbb{B}_{\Psi}).
$$

With this convention

$$
g(i\tilde X)=g(\tilde X),
$$

so $J$ is an isometry between $(\mathbb{B}_{\Phi},g)$ and $(\mathbb{B}_{\Psi},g)$. In the coordinates above its determinant is $-1$: it is the improper isometry that reverses the time direction and fixes the three space directions. It is the discrete symmetry that exchanges the two real forms, not a proper Lorentz transformation of either one.

**Remark (the norm sign).** The complex norm changes sign,

$$
\langle i\tilde X\rangle_{\natural}=i^{2}\langle\tilde X\rangle_{\natural}=-\langle\tilde X\rangle_{\natural}.
$$

On $\mathbb{B}_{\Phi}$ one has $\langle\tilde X\rangle_{\natural}=-g$, and on $\mathbb{B}_{\Psi}$ one has $\langle\tilde X\rangle_{\natural}=+g$. The minus sign in $\langle i\tilde X\rangle_{\natural}=-\langle\tilde X\rangle_{\natural}$ is therefore the change of the sector convention, not a failure of the isometry: the form $g$ is preserved.

**Remark (physical interpretation).** In the physical interpretation of the corpus, $\mathbb{B}_{\Phi}$ is the material sector and $\mathbb{B}_{\Psi}$ the informational sector. The phase of $\pi/2$ exchanges the two: it turns an anti-Hermitian element into a Hermitian one and back. The exchange is the discrete operation of the algebra that the two-sided operator cannot see, because the two-sided operator multiplies by $i$ on the left and by $-i$ on the right. The full Wick rotation of the physics articles is a different operation: it acts on the time coefficient alone and maps $\mathbb{B}_{\Phi}$ to the quaternion subspace $\mathbb{B}_{H}$, not to $\mathbb{B}_{\Psi}$. The operator $J$ is the sector exchange, not the whole Wick rotation.

### The General Phase

**Proposition.** For the phase $P_{\mathrm{pha}}=\exp(i\theta_{\mathrm{pha}})$ the one-sided operator is

$$
L_{P_{\mathrm{pha}}}=R_{P_{\mathrm{pha}}}=\exp(i\theta_{\mathrm{pha}})\,\mathrm{id},
$$

and in the splitting $(\mathbb{B}_{\Psi},\mathbb{B}_{\Phi})$ its block matrix is

$$
L_{P_{\mathrm{pha}}}=
\begin{pmatrix}
\cos\theta_{\mathrm{pha}} & i\sin\theta_{\mathrm{pha}}\\
i\sin\theta_{\mathrm{pha}} & \cos\theta_{\mathrm{pha}}
\end{pmatrix}.
$$

For $\tilde X\in\mathbb{B}_{\Phi}$ the image $\tilde Y=\exp(i\theta_{\mathrm{pha}})\tilde X$ satisfies

$$
\tilde Y^{*}=-\exp(-2i\theta_{\mathrm{pha}})\,\tilde Y .
$$

Hence $\tilde Y\in\mathbb{B}_{\Psi}$ exactly when $\theta_{\mathrm{pha}}\equiv\tfrac{\pi}{2}\pmod{\pi}$, and $\tilde Y\in\mathbb{B}_{\Phi}$ exactly when $\theta_{\mathrm{pha}}\equiv0\pmod{\pi}$. For every other $\theta_{\mathrm{pha}}$ the image lies in the real four-dimensional subspace $\exp(i\theta_{\mathrm{pha}})\mathbb{B}_{\Phi}$, on which $*$ acts by the scalar $-\exp(-2i\theta_{\mathrm{pha}})$; that subspace is neither $\mathbb{B}_{\Psi}$ nor $\mathbb{B}_{\Phi}$.

*Proof.* The scalar is central, so $L_{P_{\mathrm{pha}}}=R_{P_{\mathrm{pha}}}=\exp(i\theta_{\mathrm{pha}})\mathrm{id}$. The block matrix is the corollary of the block decomposition with $c=\exp(i\theta_{\mathrm{pha}})$. For the eigenvalue, $\tilde Y^{*}=\exp(-i\theta_{\mathrm{pha}})\tilde X^{*}=-\exp(-i\theta_{\mathrm{pha}})\tilde X=-\exp(-2i\theta_{\mathrm{pha}})\tilde Y$. The two sector values are the two solutions of $-\exp(-2i\theta_{\mathrm{pha}})=\pm1$.

**Corollary (the special angles).** The phase preserves each sector at $\theta_{\mathrm{pha}}=0$ and $\theta_{\mathrm{pha}}=\pi$, where it is $+\mathrm{id}$ and $-\mathrm{id}$. It exchanges the two sectors at $\theta_{\mathrm{pha}}=\pi/2$ and $\theta_{\mathrm{pha}}=3\pi/2$, where it is $i$ and $-i$. At $\theta_{\mathrm{pha}}=\pi/4$ it is a square root of the exchange,

$$
L_{\exp(i\pi/4)}^{2}=L_i,
$$

and the image of $\mathbb{B}_{\Phi}$ is the mixed real four-dimensional subspace on which $*$ acts by $i$.

*Proof.* The values at the four angles are immediate from the block matrix. The square is $L_{\exp(i\pi/2)}=L_i$ by the composition law.

**Remark (the period).** The operator $L_{P_{\mathrm{pha}}}$ has period $2\pi$ in $\theta_{\mathrm{pha}}$. The sector behaviour has period $\pi$, because $\exp(i(\theta_{\mathrm{pha}}+\pi))=-\exp(i\theta_{\mathrm{pha}})$ multiplies the operator by $-1$ and leaves the eigenvalue $-\exp(-2i\theta_{\mathrm{pha}})$ unchanged. The exchange therefore occurs on the two classes $\theta_{\mathrm{pha}}\equiv\pi/2\pmod{\pi}$, and the preservation on the two classes $\theta_{\mathrm{pha}}\equiv0\pmod{\pi}$.

**Remark (not a half-angle).** The polar word stores the phase as $\exp(i\theta_{\mathrm{pha}})$, with $\theta_{\mathrm{pha}}=\tfrac12\arg \langle\tilde Q\rangle_{\natural}$. The pure phase of $\pi/2$ is therefore $i=\exp(i\pi/2)$, not $\exp(i\pi/4)$. The half-angle $\exp(i\pi/4)$ is the square root of the exchange, not the exchange itself. A half-angle convention would rename the angle of the exchange to $\pi$; it would not change the operator, only the name of its parameter.

### The Cancellation in the Two-Sided Operator

**Proposition.** The two-sided operator of the pure phase is the identity:

$$
\mathrm{Sd}_i(\tilde X)=i\tilde X(-i)=\tilde X,\qquad
\mathrm{Sd}_{\exp(i\theta_{\mathrm{pha}})}=\mathrm{id}.
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

**Remark (the two readings of the same word).** The one-sided operator of the phase is $\exp(i\theta_{\mathrm{pha}})\mathrm{id}$; the two-sided operator is the identity. The one-sided operator sees the whole complex modulus $\varrho\exp(i\theta_{\mathrm{pha}})$; the two-sided operator sees only its modulus $\varrho$ and the two non-central factors. The cancellation is the product of the left factor $\exp(i\theta_{\mathrm{pha}})$ and the right factor $\exp(-i\theta_{\mathrm{pha}})$; it is exact because the two scalars are central and inverse. The phase is not halved in either reading; it is either kept whole, one-sided, or cancelled whole, two-sided.

## The Four Factors, One-Sided

### The Scale

The scale is $\varrho=\exp(\ln \varrho)$, positive, real and central. Its one-sided operators are

$$
L_r=R_r=\varrho\,\mathrm{id}.
$$

In the block decomposition $D_r=\varrho\,\mathrm{id}$ and $O_r=0$: the scale preserves both sectors and multiplies every coordinate by $\varrho$. The norm is multiplied by $\varrho^{2}$, because it is quadratic in the element. The two-sided operator acts by $\varrho^{2}$, once on each side. The determinant of $L_r$ is $\varrho^{4}$ on the complex four-space and $\varrho^{8}$ on the real eight-space. The exponent form of the comparison is §*The Exponents of the Four Factors*.

### The Boost

The boost is

$$
\tilde U_{\mathrm b}=\exp\Bigl(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr)
=\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}\,e_t+i\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}\,\vec u_{\mathrm b},
\qquad \theta_{\mathrm{rpd}}\ge0,\qquad \lvert\vec u_{\mathrm b}\rvert=1 .
$$

It is Hermitian and of norm one. Write $c=\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}$, $s=\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}$, $\vec u=\vec u_{\mathrm b}$, and let $\tilde X=ia\,e_t+\vec b$ be an element of $\mathbb{B}_{\Phi}$. Then

$$
\tilde U_{\mathrm b}\tilde X
=i\bigl(ac-s\,\vec u\cdot\vec b\bigr)e_t+i s\,\vec u\times\vec b
+c\,\vec b-s a\,\vec u .
$$

The term $i s\,\vec u\times\vec b$ is the whole $\mathbb{B}_{\Psi}$ part, an imaginary vector. The remaining terms $i(ac-s\,\vec u\cdot\vec b)e_t+c\vec b-s a\,\vec u$ are the $\mathbb{B}_{\Phi}$ part, an imaginary scalar plus the real vector $c\vec b-s a\,\vec u$. The boost therefore mixes the two sectors in general. For $a=0$ the $\mathbb{B}_{\Phi}$ part is $c\vec b-i s(\vec u\cdot\vec b)e_t$ and the $\mathbb{B}_{\Psi}$ part is $i s\,\vec u\times\vec b$, which vanishes only when $\vec b$ is parallel to $\vec u$. For $\vec b=0$ the image is $i a(c\,e_t+i s\,\vec u)=i a c\,e_t-s a\,\vec u$, entirely in $\mathbb{B}_{\Phi}$: the central imaginary line is mapped into the two-plane spanned by $i e_t$ and $\vec u$.

The boost is of norm one, so $L_{\tilde U_{\mathrm b}}$ preserves the complex norm, $\langle L_{\tilde U_{\mathrm b}}\tilde X\rangle_{\natural}=\langle \tilde X\rangle_{\natural}$, and is $\mathbb{C}$-orthogonal. It is not a real Lorentz transformation of $\mathbb{B}_{\Phi}$: it does not preserve the sector, and the only one-sided real Lorentz transformations are $\pm\mathrm{id}$, by the sector criterion.

### The Rotor

The rotor is

$$
\tilde u_{\mathrm r}=\exp\Bigl(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr)
=\cos\tfrac{\theta_{\mathrm{axr}}}{2}\,e_t+\sin\tfrac{\theta_{\mathrm{axr}}}{2}\,\vec u_{\mathrm r},
\qquad \theta_{\mathrm{axr}}\in[0,2\pi],\qquad \lvert\vec u_{\mathrm r}\rvert=1 .
$$

It is a real quaternion, of norm one, and $*$-unitary. Write $c=\cos\tfrac{\theta_{\mathrm{axr}}}{2}$, $s=\sin\tfrac{\theta_{\mathrm{axr}}}{2}$, $\vec u=\vec u_{\mathrm r}$, and let $\tilde X=ia\,e_t+\vec b$ be an element of $\mathbb{B}_{\Phi}$. Then

$$
\tilde u_{\mathrm r}\tilde X
=-s\,\vec u\cdot\vec b\,e_t+i a s\,\vec u
+i a c\,e_t+c\,\vec b+s\,\vec u\times\vec b .
$$

The first two terms are in $\mathbb{B}_{\Psi}$: a real scalar and an imaginary vector. The last two terms are in $\mathbb{B}_{\Phi}$: an imaginary scalar and the real vector $c\vec b+s\vec u\times\vec b$. The rotor mixes the two sectors in general. For $a=0$ the $\mathbb{B}_{\Psi}$ part is the real scalar $-s\,\vec u\cdot\vec b$, which vanishes only when $\vec b$ is perpendicular to $\vec u$; the $\mathbb{B}_{\Phi}$ part is the real vector $c\vec b+s\vec u\times\vec b$.

The rotor is of norm one, so $L_{\tilde u_{\mathrm r}}$ preserves the complex norm and is $\mathbb{C}$-orthogonal. It also preserves the real quaternion subspace $\mathbb{B}_{H}$ and its imaginary multiple $\mathbb{B}_{iH}$, because it is a real quaternion and left multiplication by a real quaternion preserves the subalgebra $\mathbb{B}_{H}$ and the module $\mathbb{B}_{iH}$. On $\mathbb{B}_{H}$ it is an isometry of the Euclidean norm. It does not preserve $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$.

## The Exponential of the One-Sided Operator

### The Element Identity

**Theorem.** For every $\tilde Q\in\mathbb{B}$ and every $t\in\mathbb{C}$,
$$
\boxed{\;\exp\bigl(tL_{\tilde Q}\bigr)=L_{\exp(t\tilde Q)},\qquad
\exp\bigl(tR_{\tilde Q}\bigr)=R_{\exp(t\tilde Q)}\;}
$$

*Proof.* Left multiplication is multiplicative, $L_{\tilde Q}^{n}=L_{\tilde Q^{n}}$, so the exponential series is
$$
\exp\bigl(tL_{\tilde Q}\bigr)
=\sum_{n\ge0}\frac{t^{n}}{n!}L_{\tilde Q}^{n}
=\sum_{n\ge0}L_{t^{n}\tilde Q^{n}/n!}
=L_{\exp(t\tilde Q)} .
$$
The same computation holds on the right, because $R_{\tilde Q}^{n}=R_{\tilde Q^{n}}$: the right multiplication is an anti-representation, and a single element commutes with its own powers.

**The spectrum of the group.** On $\Sigma_{11}$ the operator is diagonalisable, with the eigenvalues $\lambda_+,\lambda_+,\lambda_-,\lambda_-$ of §*The Eigenbasis*, so its exponential has the eigenvalues $e^{t\lambda_+}$ twice and $e^{t\lambda_-}$ twice, where $\lambda_\pm=Q_t\pm iB$. Its determinant and trace are
$$
\det\exp\bigl(tL_{\tilde Q}\bigr)=\exp\bigl(4tQ_t\bigr),
\qquad
\operatorname{tr}\exp\bigl(tL_{\tilde Q}\bigr)
=2\bigl(e^{t\lambda_+}+e^{t\lambda_-}\bigr)
=4e^{tQ_t}\cos(tB).
$$

**The rate is the eigenvalue, not its square.** For a central element $\tilde Q=c\,e_t$ the operator is $c\,\mathrm{id}$ and the group is $e^{tc}\,\mathrm{id}$; the two-sided operator of the same element is $\lvert c\rvert^{2}\mathrm{id}$, and its group is $e^{t\lvert c\rvert^{2}}\mathrm{id}$. The one-sided rate is $c$, the two-sided rate is $\lvert c\rvert^{2}$.

The identity holds at every point of the sector, so the norm decides nothing new: invertibility, the rate and the group law are uniform. The wall $B^{2}=0$ decides only the **shape** of the one-parameter group, and §*The Exponential at the Wall* computes it.

### The Polar Word on a Spinor

Write the polar word as $\tilde Q=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ and put
$$
\lambda_\pm=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\mu_\pm,\qquad
\mu_+\mu_-=1 .
$$
The numbers $\mu_\pm$ are the eigenvalues of the unit factor $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$. On either spinor space the operator multiplies the first coordinate by $\lambda_+$ and the second by $\lambda_-$, so the spinor coordinates carry the pair $(\lambda_+,\lambda_-)$.

For each pure factor, read with the other factors absent, the pair is elementary. The scale $\varrho$ gives $\mu_+=\mu_-=1$. The central phase $\exp(i\theta_{\mathrm{pha}})$ gives $\mu_+=\mu_-=1$ and multiplies both coordinates by $\exp(i\theta_{\mathrm{pha}})$. The boost gives
$$
\tilde U_{\mathrm b}=\exp\Bigl(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr)
\quad\Longrightarrow\quad
\mu_+=e^{-\theta_{\mathrm{rpd}}/2},\qquad \mu_-=e^{\theta_{\mathrm{rpd}}/2},
$$
and the rotor gives
$$
\tilde u_{\mathrm r}=\exp\Bigl(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr)
\quad\Longrightarrow\quad
\mu_+=e^{i\theta_{\mathrm{axr}}/2},\qquad \mu_-=e^{-i\theta_{\mathrm{axr}}/2}.
$$

**Theorem (the half-spin theorem).** The one-sided operator produces the half-angle and the half-rapidity; the two-sided operator produces the full angle and the full rapidity. For the rotor,
$$
\boxed{\;
L_{\tilde u_{\mathrm r}}=\exp\Bigl(\tfrac{\theta_{\mathrm{axr}}}{2}\,L_{\vec u_{\mathrm r}}\Bigr)
\ \Longrightarrow\ (\alpha,\beta)\longmapsto(e^{i\theta_{\mathrm{axr}}/2}\alpha,\ e^{-i\theta_{\mathrm{axr}}/2}\beta),
\qquad
\mathrm{Sd}_{\tilde u_{\mathrm r}}=\exp\Bigl(\tfrac{\theta_{\mathrm{axr}}}{2}\,\mathrm{ad}_{\vec u_{\mathrm r}}\Bigr)
\ \Longrightarrow\ \vec v\longmapsto R_{\vec u_{\mathrm r}}(\theta_{\mathrm{axr}})\vec v
\; }.
$$
The exponent is $\tfrac{\theta_{\mathrm{axr}}}{2}$ in both readings. The exponent $\tfrac{\theta_{\mathrm{axr}}}{2}$ of $L_{\tilde u_{\mathrm r}}$ multiplies the two spinor coordinates by $e^{i\theta_{\mathrm{axr}}/2}$ and $e^{-i\theta_{\mathrm{axr}}/2}$, hence the output is the half-angle; the same $\tfrac{\theta_{\mathrm{axr}}}{2}$ in $\mathrm{ad}_{\vec u}(X)=[\vec u,X]$ gives the rotation of angle $\theta_{\mathrm{axr}}$, because $\mathrm{ad}_{\vec u}=2\,[\vec u\times]$ and the factor $2$ doubles it. The boost is the same:
$$
\boxed{\;
L_{\tilde U_{\mathrm b}}=\exp\Bigl(i\tfrac{\theta_{\mathrm{rpd}}}{2}\,L_{\vec u_{\mathrm b}}\Bigr)
\ \Longrightarrow\ (\alpha,\beta)\longmapsto(e^{-\theta_{\mathrm{rpd}}/2}\alpha,\ e^{\theta_{\mathrm{rpd}}/2}\beta),
\qquad
\mathrm{Sd}_{\tilde U_{\mathrm b}}\ \Longrightarrow\ \text{rapidity }\theta_{\mathrm{rpd}}
\; }.
$$
A spinor transforms by half of what a vector transforms by, and the operator that produces the half is the one-sided one. This is the precise sense in which the spin representation of the polar word is the one-sided operator and the vector representation is the two-sided one. The spectral form of the same statement is §*The Spectrum of the Two-Sided Operator* and §*The Pure Factors and the Full Rotor* of *Two-Sided Operators on the N-Regular Sector*.

The following table collects the pure factors. The last column is the nontrivial factor in the spectrum of the two-sided operator, that is, in the products $\lambda_i\bar\lambda_j$.

| factor | $\mu_+,\mu_-$ | exponent per coordinate | nontrivial two-sided factor |
|---|---|---|---|
| scale $\varrho$ | $1,1$ | $\ln \varrho$ | $\varrho^{2}$ |
| phase $\exp(i\theta_{\mathrm{pha}})$ | $1,1$ | $i\theta_{\mathrm{pha}}$ | $1$ |
| boost $\tilde U_{\mathrm b}$ | $e^{-\theta_{\mathrm{rpd}}/2},e^{\theta_{\mathrm{rpd}}/2}$ | $\mp\theta_{\mathrm{rpd}}/2$ | $e^{\pm\theta_{\mathrm{rpd}}}$ |
| rotor $\tilde u_{\mathrm r}$ | $e^{i\theta_{\mathrm{axr}}/2},e^{-i\theta_{\mathrm{axr}}/2}$ | $\pm i\theta_{\mathrm{axr}}/2$ | $e^{\pm i\theta_{\mathrm{axr}}}$ |

The scale and the phase are central. Their rows are read as scalar multipliers of a word with $B\neq0$; for a purely central element $B=0$, every basis is an eigenbasis, and the single eigenvalue is $Q_t$.

For a general word the two factors do not commute, and $\mu_\pm$ are not separately exponentials of half the boost and half the rotor angle. The pair is still $(\lambda_+,\lambda_-)$; the half-angle formulas are the statement for the pure factors, and for commuting axes. The general relation between the spectral data and the polar angles is *Relations between the Complete Polar Decomposition and Eigenbasis of an N-Regular Biquaternion*, §*The Spectral Data from the Polar Factors*.

### The Weight Relation and the Two Copies

The algebra is the tensor product of a spinor space and its dual,
$$
\mathbb{B}\cong S\otimes S^{*},
$$
where $S=\mathbb{C}^{2}$ is the spinor space and $S^{*}$ its dual, and $S_+\cong S_-\cong S$ as left modules. Left multiplication acts on the first factor, right multiplication on the second:
$$
L_{\tilde Q}=\Delta_{\mathrm{rep}}(\tilde Q)\otimes 1,
\qquad
R_{\tilde Q}=1\otimes\Delta_{\mathrm{rep}}(\tilde Q)^{T},
\qquad
R_{\tilde Q^{*}}=1\otimes\bar\Delta_{\mathrm{rep}}(\tilde Q),
$$
where $\Delta_{\mathrm{rep}}$ is the defining representation on $S$ and $\bar\Delta_{\mathrm{rep}}$ its conjugate. The two factors commute, so the exponents add:
$$
\exp\bigl(tL_A\bigr)\exp\bigl(sR_B\bigr)=\exp\bigl(tL_A+sR_B\bigr).
$$

For the rotor, $\Delta_{\mathrm{rep}}(\tilde u_{\mathrm r})$ has weights $e^{\pm i\theta_{\mathrm{axr}}/2}$ and $\bar\Delta_{\mathrm{rep}}(\tilde u_{\mathrm r})$ has weights $e^{\mp i\theta_{\mathrm{axr}}/2}$. The tensor weights, in additive notation, are the four sums
$$
\tfrac{\theta_{\mathrm{axr}}}{2}-\tfrac{\theta_{\mathrm{axr}}}{2}=0,\qquad
\tfrac{\theta_{\mathrm{axr}}}{2}+\tfrac{\theta_{\mathrm{axr}}}{2}=\theta_{\mathrm{axr}},\qquad
-\tfrac{\theta_{\mathrm{axr}}}{2}-\tfrac{\theta_{\mathrm{axr}}}{2}=-\theta_{\mathrm{axr}},\qquad
-\tfrac{\theta_{\mathrm{axr}}}{2}+\tfrac{\theta_{\mathrm{axr}}}{2}=0,
$$
that is $(\theta_{\mathrm{axr}},0,0,-\theta_{\mathrm{axr}})$. For the boost, both slots carry $e^{\mp\theta_{\mathrm{rpd}}/2}$ because the boost is Hermitian, and the sums are $(\theta_{\mathrm{rpd}},0,0,-\theta_{\mathrm{rpd}})$. These are the weights of the vector. The invariant statement is that the weights of $S\otimes S^{*}$ are the pairwise sums of the weights of $S$ and $S^{*}$; the factor two sits in the pairing, not in a rescaling of the angle.

**"Half" is relative.** The angle $\theta_{\mathrm{axr}}$ is defined by the vector action, as the rotation of $\mathbb{R}^{3}$. The spinor weight is $\theta_{\mathrm{axr}}/2$ because the rotor is $\exp(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r})$. A different normalisation of the angle would change the number and not the relation.

**The whole operator is two copies.** On $\mathbb{B}=S_+\oplus S_-$ the two summands are isomorphic as left modules, so
$$
\operatorname{spec}L_{\tilde u_{\mathrm r}}
=\{e^{i\theta_{\mathrm{axr}}/2},e^{i\theta_{\mathrm{axr}}/2},
e^{-i\theta_{\mathrm{axr}}/2},e^{-i\theta_{\mathrm{axr}}/2}\},
$$
each weight twice. The one-sided operator is $2\Delta_{\mathrm{rep}}$ as a left module: two copies of the Weyl module, not the Dirac module $\Delta_{\mathrm{rep}}\oplus\bar\Delta_{\mathrm{rep}}$. One Peirce column is one elementary spinor, a Weyl spinor in the language of physics; the whole of $L$ is a pair of them, which is a Dirac spinor (*Spinors and Dirac Spinors in the Biquaternion Algebra*, §*The Pair Is a Multiplicity*). The precise phrase is therefore: the one-sided operator, restricted to one Peirce component, is the half-spin.

**The two Peirce copies are not the two Lorentz chiralities.** Both $S_+$ and $S_-$ carry the same representation $\Delta_{\mathrm{rep}}$; they differ by the Peirce idempotent, not by the Lorentz chirality. The two Lorentz chiralities are the two tensor factors $S$ and $S^{*}$, that is the left and right slots.

**Factor by factor.** For a general word the factors do not commute and $\lambda_\pm$ are not $e^{\pm i\theta_{\mathrm{axr}}/2}$ or $e^{\mp\theta_{\mathrm{rpd}}/2}$. There is no single half-angle of a general polar word; the additive relation is the statement for the pure factors and for commuting axes.

**The whole of $L$ is twisted.** $L_{\tilde Q}$ also carries the scale $\varrho$ and the phase $e^{i\theta_{\mathrm{pha}}}$. The spinor statement concerns the norm-one, phase-one part $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$; the full operator is the twisted spinor representation of the module.

**The double cover.** Replacing $\tilde u_{\mathrm r}$ by $-\tilde u_{\mathrm r}$ leaves the two-sided operator unchanged and changes $L$ by $-1$. On the norm-one slice the two-sided operator determines the element only up to sign; $L$ distinguishes the sign. The half-angle is therefore defined only after the lift to the double cover is chosen, and $L$ is the operator that carries the choice.

**Corollary (the one-sided operator is the spinor action).** The operator $L_{\tilde Q}$ is the action of $\tilde Q$ on a single spinor. It preserves chirality, acts by the same module on $S_+$ and $S_-$, and its rotor and boost exponents are half those of the two-sided operator.

### The Exponents of the Four Factors

The following table collects the exponents. The **exponent** is the element $A$ such that the factor is $\exp(A)$; the **scalar parameter** is the real or imaginary coefficient inside that exponential, and the **two-sided output** is the parameter of the corresponding transformation in the two-sided operator.

| factor | exponent $A$ | scalar parameter | two-sided output |
|---|---|---|---|
| scale $\varrho$ | $\ln \varrho$ | $\ln \varrho$ | $2\ln \varrho$ |
| phase $\exp(i\theta_{\mathrm{pha}})$ | $i\theta_{\mathrm{pha}}$ | $\theta_{\mathrm{pha}}$ | $0$ |
| boost $\tilde U_{\mathrm b}$ | $i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ | $\tfrac{\theta_{\mathrm{rpd}}}{2}$ | $\theta_{\mathrm{rpd}}$ |
| rotor $\tilde u_{\mathrm r}$ | $\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}$ | $\tfrac{\theta_{\mathrm{axr}}}{2}$ | $\theta_{\mathrm{axr}}$ |

The rule is the number of slots. A one-sided operator is one factor of the word, so its exponent is the exponent of that factor: the scale keeps $\ln \varrho$, the phase keeps $i\theta_{\mathrm{pha}}$, the boost keeps the half-rapidity in $i\theta_{\mathrm{rpd}}/2\,\vec u_{\mathrm b}$, the rotor keeps the half-angle in $\theta_{\mathrm{axr}}/2\,\vec u_{\mathrm r}$. A two-sided operator uses two slots, the parameter and its Hermitian conjugate. For the Hermitian factors the two exponents are equal and add, giving $2\ln \varrho$ for the scale and $\theta_{\mathrm{rpd}}$ for the boost; for the $*$-unitary rotor they are opposite and the conjugation gives the angle $\theta_{\mathrm{axr}}$; for the central imaginary phase they cancel to $0$. The doubling is therefore a two-slot phenomenon for the scale, the boost and the rotor, and the phase is its exceptional case (§*The Doubling Rule* of *Two-Sided Operators on the N-Regular Sector*).

## The Image and the Kernel

**Proposition.** Let $\tilde Q\in\mathbb{B}$.

**(a)** The parameter map $\tilde Q\mapsto L_{\tilde Q}$ is injective. The operator $L_{\tilde Q}$ is injective exactly when $\tilde Q$ is invertible.

**(b)** For an invertible element $\tilde Q$, $L_{\tilde Q}$ is a bijection of $\mathbb{B}$.

**(c)** For a nonzero null $\tilde Q$, the operator $L_{\tilde Q}$ has complex rank two, its kernel is the right annihilator $\{\tilde X:\tilde Q\tilde X=0\}$ of complex dimension two, and its image is the right ideal $\tilde Q\mathbb{B}$ of complex dimension two.

**(d)** For $\tilde Q=0$ the operator is zero.

*Proof.* (a) Injectivity of the parameter map is (d) of the first proposition. If $\tilde Q$ is invertible, $L_{\tilde Q}^{-1}=L_{\tilde Q^{-1}}$. If $\tilde Q$ is a nonzero null element, $\mathsf M_2(\tilde Q)$ has rank one, so the kernel of $X\mapsto\mathsf M_2(\tilde Q)X$ is the two-dimensional space of matrices whose columns lie in the kernel of $\mathsf M_2(\tilde Q)$, and the image is the two-dimensional space of matrices whose columns lie in the image. (b) is (e) of the first proposition. (c) is the matrix computation just given. (d) is immediate.

**Proposition (the image on the group of invertibles).** The restriction of $\tilde Q\mapsto L_{\tilde Q}$ to $\mathbb{B}^{\times}$ is a faithful representation whose image is a subgroup of $GL_{\mathbb{C}}(\mathbb{B})$ isomorphic to $\mathbb{B}^{\times}$. As a complex Lie group,

$$
\boxed{\;\mathbb{B}^{\times}\cong GL(2,\mathbb{C})\;},
$$

of complex dimension four and real dimension eight. The kernel is trivial.

*Proof.* The map is injective by (a) and multiplicative by the composition law, so it is a faithful representation. The algebra isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ identifies the invertibles with $GL(2,\mathbb{C})$.

**Corollary (the contrast with the two-sided operator).** The two-sided image is the conformal Lorentz group $CO^{+}(1,3)$, of real dimension seven, with kernel $U(1)$. The one-sided image is $\mathbb{B}^{\times}\cong GL(2,\mathbb{C})$, of real dimension eight, with trivial kernel. The missing dimension is the phase: the one-sided action sees it, the two-sided action quotients by it.

The following table collects the comparison. The rank is the complex rank of the operator on $\mathbb{B}$.

| | one-sided $L_{\tilde Q}$ | two-sided $\mathrm{Sd}_{\tilde Q}$ |
|---|---|---|
| parameter map | linear, faithful | quadratic; kernel $U(1)$ on the invertibles |
| scale | $\varrho$ | $\varrho^{2}$ |
| phase | $\exp(i\theta_{\mathrm{pha}})$, exchange at $\pi/2$ | $1$ |
| norm of the image | $\varrho^{2}e^{2i\theta_{\mathrm{pha}}}\langle \tilde X\rangle_{\natural}$ | $\varrho^{4}\langle \tilde X\rangle_{\natural}$ |
| complex determinant | $\varrho^{4}e^{4i\theta_{\mathrm{pha}}}$ | $\varrho^{8}$ |
| image on the invertibles | $\cong GL(2,\mathbb{C})$, real dimension $8$ | $\cong CO^{+}(1,3)$, real dimension $7$ |
| kernel on the invertibles | trivial | $U(1)$ |
| nonzero null parameter | rank $2$, right ideal | rank $1$, complex line |

**Corollary (the real forms are two-sided).** The only one-sided multiplications that preserve $\mathbb{B}_{\Phi}$ are the real scalars, and among them the only isometries of $g$ are $\pm\mathrm{id}$. The one-sided action therefore does not give the Lorentz group on $\mathbb{B}_{\Phi}$. The norm-one one-sided operators are $\mathbb{C}$-orthogonal. The proper orthochronous Lorentz group is not among them: it is the image of the two-sided operator on the norm-one slice, the identity component of the subgroup of the $\mathbb{C}$-orthogonal group that also preserves the two real forms.

## The Wall $B^{2}=0$: the Unipotent Case

The second condition $B^{2}=0$ is the wall inside the N-regular sector. Off the wall the element has two distinct eigenvalues and the operators are semisimple. On the wall the element is $Q_t(e_t+\vec\Pi_{\mathrm{nil}})$ with $\vec\Pi_{\mathrm{nil}}^{2}=0$, the operators are a scalar times a unipotent operator, and the Jordan type leaves the semisimple case. Nothing else changes: the operators remain invertible, of rank four, with the whole algebra as image and zero as kernel.

The scalar line $\vec\Pi_{\mathrm{nil}}=0$ is the case $\tilde Q=Q_t e_t$. The operator is $Q_t\,\mathrm{id}$, with the single eigenvalue $Q_t$ of algebraic and geometric multiplicity four and Jordan type $1+1+1+1$; that case needs no separate treatment, and the sections below describe the Jordan part $\vec\Pi_{\mathrm{nil}}\neq0$.

### The Jordan Structure

Let

$$
\tilde Q=Q_t\bigl(e_t+\vec\Pi_{\mathrm{nil}}\bigr),
\qquad
\vec\Pi_{\mathrm{nil}}^2=0,
\qquad
\vec\Pi_{\mathrm{nil}}\neq0.
$$

Then

$$
L_{\tilde Q}=Q_t\bigl(I+L_{\vec\Pi_{\mathrm{nil}}}\bigr),
\qquad
L_{\vec\Pi_{\mathrm{nil}}}^2=0,
\qquad
L_{\vec\Pi_{\mathrm{nil}}}\neq0.
$$

**Proposition (the two blocks).** The operator $L_{\vec\Pi_{\mathrm{nil}}}$ has rank two and kernel of dimension two. The operator $L_{\tilde Q}$ has the single eigenvalue $Q_t$, minimal polynomial $(X-Q_t)^2$, geometric multiplicity two and two Jordan blocks of size two. The same statements hold for $R_{\tilde Q}$.

*Proof.* The image of $L_{\vec\Pi_{\mathrm{nil}}}$ is the left ideal $\mathbb{B}\vec\Pi_{\mathrm{nil}}$, of complex dimension two because $\vec\Pi_{\mathrm{nil}}\neq0$ and $\vec\Pi_{\mathrm{nil}}^2=0$; the kernel is the right annihilator of $\vec\Pi_{\mathrm{nil}}$, also of complex dimension two. The square is zero, so the image lies in the kernel and both have dimension two. A nilpotent of index two on a four-dimensional space with rank two has two blocks of size two. Adding the scalar $Q_t$ shifts the eigenvalue and preserves the blocks.

The determinant and the trace follow from the matrix model:

$$
\det_{\mathbb{C}}L_{\tilde Q}=Q_t^4,
\qquad
\operatorname{tr}L_{\tilde Q}=4Q_t.
$$

The determinant is the fourth power of the scalar, not the square, because the left multiplication acts on the four-dimensional algebra. The trace is four times the scalar because the diagonal of $L_{\tilde Q}$ has the four entries $Q_t$.

The polar word splits the operator into four one-sided factors. The modulus is the scalar $\varrho\,e^{i\theta_{\mathrm{pha}}}\,\mathrm{id}$. The positive factor and the rotor act by left multiplication:

$$
L_{\tilde U_{\mathrm b}}(\tilde X)=\tilde U_{\mathrm b}\tilde X,
\qquad
L_{\tilde u_{\mathrm r}}(\tilde X)=\tilde u_{\mathrm r}\tilde X.
$$

Their product is the left multiplication by the unit factor,

$$
L_{\tilde U}=L_{\tilde U_{\mathrm b}}\circ L_{\tilde u_{\mathrm r}},
\qquad
\tilde U=\varepsilon\bigl(e_t+\vec\Pi_{\mathrm{nil}}\bigr).
$$

The product is unipotent up to $\varepsilon$, while the two factors are not. This is the one-sided form of the Cartan phenomenon: the operator $L_{\tilde U}$ has a double eigenvalue and two Jordan blocks, and its two polar factors are left multiplications by a positive element and a rotor, each with distinct eigenvalues.

The one-sided operator therefore sees the defect more directly than the element. The element is defective but scalar; the operator is defective on a four-dimensional space and exhibits the two blocks explicitly.

### The Word One-Sided

The polar word splits the operator into four one-sided factors. The modulus is the scalar $\varrho\,e^{i\theta_{\mathrm{pha}}}\,\mathrm{id}$. The positive factor and the rotor act by left multiplication:

$$
L_{\tilde U_{\mathrm b}}(\tilde X)=\tilde U_{\mathrm b}\tilde X,
\qquad
L_{\tilde u_{\mathrm r}}(\tilde X)=\tilde u_{\mathrm r}\tilde X.
$$

Their product is the left multiplication by the unit factor,

$$
L_{\tilde U}=L_{\tilde U_{\mathrm b}}\circ L_{\tilde u_{\mathrm r}},
\qquad
\tilde U=\varepsilon\bigl(e_t+\vec\Pi_{\mathrm{nil}}\bigr).
$$

The product is unipotent up to $\varepsilon$, while the two factors are not. This is the one-sided form of the Cartan phenomenon: the operator $L_{\tilde U}$ has a double eigenvalue and two Jordan blocks, and its two polar factors are left multiplications by a positive element and a rotor, each with distinct eigenvalues.

The one-sided operator therefore sees the defect more directly than the element. The element is defective but scalar; the operator is defective on a four-dimensional space and exhibits the two blocks explicitly.

### The Exponential at the Wall

On the wall the element is $Q_t(e_t+\vec\Pi_{\mathrm{nil}})$ with $\vec\Pi_{\mathrm{nil}}^{2}=0$, so the operator is $Q_t(I+L_{\vec\Pi_{\mathrm{nil}}})$ with $L_{\vec\Pi_{\mathrm{nil}}}^{2}=0$, and its exponential is a shear:
$$
\boxed{\;\exp\bigl(tL_{\tilde Q}\bigr)
=e^{tQ_t}\bigl(I+tQ_t\,L_{\vec\Pi_{\mathrm{nil}}}\bigr)\;}
$$
for every complex $t$. In particular $\exp L_{\tilde Q}=e^{Q_t}(I+Q_tL_{\vec\Pi_{\mathrm{nil}}})$.

*Proof.* $L_{\tilde Q}=Q_t(I+L_{\vec\Pi_{\mathrm{nil}}})$ and $L_{\vec\Pi_{\mathrm{nil}}}^{2}=L_{\vec\Pi_{\mathrm{nil}}^{2}}=0$. The two terms commute, being polynomials in $L_{\vec\Pi_{\mathrm{nil}}}$, so the exponential is $e^{tQ_t}\exp(tQ_tL_{\vec\Pi_{\mathrm{nil}}})$, and the second factor truncates at degree one.

**The group is a line of shears.** It moves the identity along the nilpotent direction and stops at degree one; it has no period and carries no angle. The polar angles are in the factors: $L_{\tilde U_{\mathrm b}}$ has the eigenvalues $e^{\pm\theta_{\mathrm{rpd}}/2}$, each twice, and $L_{\tilde u_{\mathrm r}}$ has $e^{\pm i\theta_{\mathrm{axr}}/2}$, each twice. Their product has the single eigenvalue $Q_t$, with two Jordan blocks of size two, and its spectrum carries no angle at all. In the regular sector the eigenvalues of $L_{\tilde Q}$ are $\varrho\,e^{i\theta_{\mathrm{pha}}}\mu_\pm$ with $\mu_\pm=U_t\pm i\sqrt{1-U_t^{2}}$ and $U_t=\operatorname{Sc}\tilde U$; at the wall $U_t\to\varepsilon$ and both eigenvalues tend to $\varrho\,e^{i\theta_{\mathrm{pha}}}\varepsilon=Q_t$.

**The two angles are locked.** The wall removes neither factor; it removes two real degrees of freedom. Write $\vec\Pi_{\mathrm{nil}}=\vec A+i\vec B$ with $\vec A$ and $\vec B$ real, so that $\vec A\cdot\vec B=0$ and $\lvert\vec A\rvert=\lvert\vec B\rvert=a$. The regular word carries two independent exponents, $i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ and $\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}$, about two independent axes. At the wall the exact exponent is $\vec\Pi_{\mathrm{nil}}$ itself, and the formal sum of the two factor exponents differs from it by the log defect of *The Complete Polar Decomposition of an N-Regular Biquaternion*, §*The Formal Exponent and the Defect at the Wall*, whose cross term $i\varepsilon\tanh\frac{\theta_{\mathrm{rpd}}}{2}\tan\frac{\theta_{\mathrm{axr}}}{2}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r}$ is non-zero because the axes are orthogonal. What the wall leaves is a pair of constraints between the two factors:
$$
\boxed{\;\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0,\qquad
\varepsilon\tan\frac{\theta_{\mathrm{axr}}}{2}=\sinh\frac{\theta_{\mathrm{rpd}}}{2}=a.\;}
$$

*Proof.* From the coordinate boxes of *The Complete Polar Decomposition of an N-Regular Biquaternion*, $\cosh\frac{\theta_{\mathrm{rpd}}}{2}=\sqrt{1+a^2}$, $\sinh\frac{\theta_{\mathrm{rpd}}}{2}=a$, $\lvert\cos\frac{\theta_{\mathrm{axr}}}{2}\rvert=1/\sqrt{1+a^2}$ and $\sin\frac{\theta_{\mathrm{axr}}}{2}=a/\sqrt{1+a^2}$. Hence $\varepsilon\tan\frac{\theta_{\mathrm{axr}}}{2}=a=\sinh\frac{\theta_{\mathrm{rpd}}}{2}$. The axes are $\vec u_{\mathrm b}\propto\vec B+\vec A\times\vec B$ and $\vec u_{\mathrm r}=\varepsilon\vec A/a$. The vectors $\vec B$ and $\vec A\times\vec B$ are both orthogonal to $\vec A$, because $\vec A\cdot\vec B=0$, so $\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0$.

**One slot against two.** At the wall the spinor exponent is $\vec\Pi_{\mathrm{nil}}$, carried by the left slot, and the vector exponent of the two-sided operator is $\vec\Pi_{\mathrm{nil}}$ in the left slot plus $\vec\Pi_{\mathrm{nil}}^{*}$ in the right. That is the wall form of the doubling: the scalar part appears once per slot, which is why the modulus is $Q_t$ in the one-sided reading and $\lvert Q_t\rvert^{2}$ in the two-sided one, and not a doubled exponent.

### Worked Example

Take $\tilde Q=e_t+\vec e_x+i\vec e_y$. In the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$,

$$
\mathsf M(L_{\tilde Q})=
\begin{pmatrix}
1 & -1 & -i & 0\\
1 & 1 & 0 & i\\
i & 0 & 1 & -1\\
0 & -i & 1 & 1
\end{pmatrix},
\qquad
\mathsf M(L_{\vec\Pi_{\mathrm{nil}}})=
\begin{pmatrix}
0 & -1 & -i & 0\\
1 & 0 & 0 & i\\
i & 0 & 0 & -1\\
0 & -i & 1 & 0
\end{pmatrix}.
$$

The second matrix squares to zero and has rank two. The first is the identity plus the second, so it has the single eigenvalue $1$, two Jordan blocks of size two, determinant $1$ and trace $4$. The exponential is $e^{t}\bigl(I+t\,\mathsf M(L_{\vec\Pi_{\mathrm{nil}}})\bigr)$: the identity plus $t$ times the nilpotent part, multiplied by $e^{t}$, and at $t=1$ it is $e$ times the unipotent matrix above, as §*The Exponential at the Wall* requires.

The polar factors are left multiplications by

$$
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\frac{\vec e_y+\vec e_z}{\sqrt2},
\qquad
\tilde u_{\mathrm r}=\frac{e_t+\vec e_x}{\sqrt2}.
$$

Their left multiplication matrices are not unipotent. Their product is the unipotent matrix above. The example shows the same contrast as the element-level article: the factors are diagonalizable, the product is not.

### The Image and the Kernel of the Nilpotent Part

Because $\tilde Q$ is invertible, $L_{\tilde Q}$ is invertible: its image is the whole algebra and its kernel is zero. The interesting image and kernel are those of $L_{\vec\Pi_{\mathrm{nil}}}$, not of $L_{\tilde Q}$.

The image of $L_{\vec\Pi_{\mathrm{nil}}}$ is the left ideal generated by $\vec\Pi_{\mathrm{nil}}$,

$$
\operatorname{im}L_{\vec\Pi_{\mathrm{nil}}}=\mathbb{B}\vec\Pi_{\mathrm{nil}}
=\mathbb{C}\{\vec\Pi_{\mathrm{nil}},\vec\Pi_{\mathrm{nil}}\vec e_x,\vec\Pi_{\mathrm{nil}}\vec e_y,\vec\Pi_{\mathrm{nil}}\vec e_z\},
$$

of dimension two. The kernel is the right annihilator

$$
\ker L_{\vec\Pi_{\mathrm{nil}}}=\{\tilde X:\vec\Pi_{\mathrm{nil}}\tilde X=0\},
$$

also of dimension two. The kernel is the generalized eigenspace of $L_{\tilde Q}$ at $Q_t$; the image is the left ideal inside it. The Jordan blocks live on a complement to the kernel.

## The Boundary: the Null Cone

The null cone $N=0$ is the subject of *One-Sided Operators on the N-Degenerate Sector*. Only the comparison of the two readings is recorded here, because it measures how much the one-sided operator keeps. On the cone the polar word does not exist, but both one-sided operators do. Let $\tilde Q\neq0$ with $\langle\tilde Q\rangle_{\natural}=0$. In the matrix model $\mathsf M_2(\tilde Q)=uv^{*}$ with $u$ a nonzero column and $v^{*}$ a nonzero row. Then

$$
\mathsf M_2(L_{\tilde Q}\tilde X)=\mathsf M_2(\tilde Q)\,\mathsf M_2(\tilde X)=u\,(v^{*}\mathsf M_2(\tilde X)).
$$

The image consists of the matrices $u \varrho^{*}$ with $\varrho^{*}$ an arbitrary row, that is, the matrices all of whose columns lie in the complex line $\mathbb{C}u$. This is a right ideal of complex dimension two, not a line. The kernel is the set of $\tilde X$ with $v^{*}\mathsf M_2(\tilde X)=0$, of complex dimension two. The rank is two.

The two-sided operator of the same element is

$$
\mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}
=u\,(v^{*}\mathsf M_2(\tilde X)v)\,u^{*},
$$

a multiple of $uu^{*}=\mathsf M_2(\tilde Q\tilde Q^{*})$. Its image is the single complex line $\mathbb{C}\tilde Q\tilde Q^{*}$, and its rank is one. The one-sided operator keeps a two-dimensional right ideal; the two-sided operator collapses it to a line. The failure of invertibility is therefore different in the two readings: the one-sided operator loses half of the algebra, the two-sided operator loses all but one complex direction.

## Summary

The one-sided operators of the polar word are $L_{\tilde Q}(\tilde X)=\tilde Q\tilde X$ and $R_{\tilde Q}(\tilde X)=\tilde X\tilde Q$. They are $\mathbb{C}$-linear, faithful in the parameter, and they multiply the complex norm by $\varrho^{2}e^{2i\theta_{\mathrm{pha}}}$. The left multiplication factorises as

$$
L_{\tilde Q}=L_{\varrho\,e^{i\theta_{\mathrm{pha}}}}\circ L_{\tilde U_{\mathrm b}}\circ L_{\tilde u_{\mathrm r}},
$$

with $L_{\varrho\,e^{i\theta_{\mathrm{pha}}}}=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\mathrm{id}$; the right multiplication is the mirror.

In the real splitting $\mathbb{B}=\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$ the left multiplication has the block form

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
J(\mathbb{B}_{\Phi})=\mathbb{B}_{\Psi},\qquad J(\mathbb{B}_{\Psi})=\mathbb{B}_{\Phi},\qquad J^{2}=-\mathrm{id},\qquad J^{-1}=L_{-i}.
$$

In coordinates, $\tilde X=ia\,e_t+\vec b$ is sent to $-a\,e_t+i\vec b$: the time reflection $(a,\vec b)\mapsto(-a,\vec b)$, an improper isometry of the Minkowski form $g=a^{2}-\lvert\vec b\rvert^{2}$. The complex norm changes sign, $\langle i\tilde X\rangle_{\natural}=-\langle\tilde X\rangle_{\natural}$, because the two sectors carry opposite signs in $\langle\cdot\rangle_{\natural}$. For a general phase the block matrix is

$$
\begin{pmatrix}
\cos\theta_{\mathrm{pha}} & i\sin\theta_{\mathrm{pha}}\\
i\sin\theta_{\mathrm{pha}} & \cos\theta_{\mathrm{pha}}
\end{pmatrix},
$$

the image of $\mathbb{B}_{\Phi}$ has $*$-eigenvalue $-\exp(-2i\theta_{\mathrm{pha}})$, and the sectors are reached exactly at $\theta_{\mathrm{pha}}\equiv0$ and $\theta_{\mathrm{pha}}\equiv\pi/2$ modulo $\pi$.

The scale acts as $\varrho$, not $\varrho^{2}$. The phase acts as $\exp(i\theta_{\mathrm{pha}})$, not as the identity. The boost and the rotor are $\mathbb{C}$-orthogonal and mix the sectors. The one-sided operator has one slot; the two-sided operator pairs two slots. The exponent reading of the half-angle, the half-rapidity and the doubling is §*The Exponential of the One-Sided Operator* above.

Off the wall the exponential has the eigenvalues $e^{t\lambda_\pm}$, each twice, the determinant $\exp(4tQ_t)$ and the trace $4e^{tQ_t}\cos(tB)$.

On the wall $B^{2}=0$ the element is $\tilde Q=Q_t(e_t+\vec\Pi_{\mathrm{nil}})$ and $L_{\tilde Q}=Q_t(I+L_{\vec\Pi_{\mathrm{nil}}})$ with $L_{\vec\Pi_{\mathrm{nil}}}^{2}=0$. The operator has the single eigenvalue $Q_t$, minimal polynomial $(X-Q_t)^{2}$, rank two for $L_{\vec\Pi_{\mathrm{nil}}}$, geometric multiplicity two and two Jordan blocks of size two, with $\det_{\mathbb{C}}L_{\tilde Q}=Q_t^{4}$ and $\operatorname{tr}L_{\tilde Q}=4Q_t$. The polar factors $L_{\tilde U_{\mathrm b}}$ and $L_{\tilde u_{\mathrm r}}$ are not unipotent; their product is. The image of $L_{\vec\Pi_{\mathrm{nil}}}$ is the left ideal $\mathbb{B}\vec\Pi_{\mathrm{nil}}$ and its kernel is the right annihilator, both of complex dimension two. Its exponential is the shear $\exp(tL_{\tilde Q})=e^{tQ_t}(I+tQ_tL_{\vec\Pi_{\mathrm{nil}}})$, with no period and no angle, while the polar angles survive in the factors and are locked by $\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0$ and $\varepsilon\tan\frac{\theta_{\mathrm{axr}}}{2}=\sinh\frac{\theta_{\mathrm{rpd}}}{2}=a$.

In the eigenbasis the left multiplication is diagonal,
$$
[L_{\tilde Q}]=\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-),
\qquad
\lambda_\pm=Q_t\pm iB .
$$
The two spinor spaces $S_+=\mathbb{B}\tilde\Pi_{\mathrm{id},+}$ and $S_-=\mathbb{B}\tilde\Pi_{\mathrm{id},-}$ are the two Peirce copies. On each, with the eigenbasis $(\tilde\Pi_{\mathrm{id},+},\vec\Pi_{\mathrm{nil},+})$ or $(\vec\Pi_{\mathrm{nil},-},\tilde\Pi_{\mathrm{id},-})$, the operator is the same matrix
$$
\Delta=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix},
$$
so $L_{\tilde Q}$ acts by $\Delta$ on both and never mixes them. The algebra is $S\otimes S^{*}$; $L$ acts on each copy of $S$ and is $2\Delta_{\mathrm{rep}}$, two copies of the Weyl spinor. The spectral form of the half-spin and of the doubling is §*The Exponential of the One-Sided Operator* above and §*The Doubling Rule* of *Two-Sided Operators on the N-Regular Sector*.

The image of the one-sided action on the invertibles is $\mathbb{B}^{\times}\cong GL(2,\mathbb{C})$, of real dimension eight, with trivial kernel. The image of the two-sided action is $CO^{+}(1,3)$, of real dimension seven, with kernel $U(1)$. The missing dimension is the phase. On the null cone the one-sided operator has rank two and image the right ideal $\tilde Q\mathbb{B}$; the two-sided operator has rank one and image the line $\mathbb{C}\tilde Q\tilde Q^{*}$.

The one-sided multiplication is a left translation of the algebra. The two-sided operator is the product of a left translation and a right translation, and it is that product which gives the real Lorentz transformations. The phase is the clearest witness: one-sided it is the exchange of the two real forms, two-sided it is the identity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, with $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | the central scalar imaginary, $i^{2}=-1$ |
| $\tilde Q^{*}$ | the Hermitian conjugation $\overline{\tilde Q^{\natural}}$ |
| $\natural$, $\bar\cdot$ | the quaternion and coefficient conjugations |
| $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ | the Hermitian and anti-Hermitian subspaces, $\tilde Q^{*}=\pm\tilde Q$ |
| $L_{\tilde Q},R_{\tilde Q}$ | the left and right multiplications |
| $\mathrm{Sd}_{\tilde Q}=R_{\tilde Q^{*}}\circ L_{\tilde Q}$ | the two-sided Hermitian pair |
| $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | the complex norm |
| $\varrho\exp(i\theta_{\mathrm{pha}})$ | the complex modulus, the principal square root of $\langle\tilde Q\rangle_{\natural}$ |
| $\varrho>0$, $\theta_{\mathrm{pha}}\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$ | the scale and the phase angle |
| $\tilde U_{\mathrm b}=\exp(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b})$ | the Hermitian positive unit-norm boost |
| $\tilde u_{\mathrm r}=\exp(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r})$ | the unit real quaternion rotor |
| $D_{\tilde Q},O_{\tilde Q}$ | the symmetrized and antisymmetrized multiplication blocks |
| $\lambda_\pm=Q_t\pm iB$, $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the two eigenvalues of $L_{\tilde Q}$ |
| $\tilde\Pi_{\mathrm{id},\pm},\vec\Pi_{\mathrm{nil},\pm}$ | the eigenprojections and the normalised nilpotents of the eigenbasis |
| $S_+=\mathbb{B}\tilde\Pi_{\mathrm{id},+}$, $S_-=\mathbb{B}\tilde\Pi_{\mathrm{id},-}$ | the two spinor spaces (Peirce copy), the Peirce carriers (minimal left ideals here) |
| $\Delta=\operatorname{diag}(\lambda_+,\lambda_-)$ | the common spinor matrix on $S_+$ and $S_-$ |
| $S,S^{*}$ | the spinor space $\mathbb{C}^{2}$ and its dual, with $\mathbb{B}\cong S\otimes S^{*}$ |
| $\Delta_{\mathrm{rep}},\bar\Delta_{\mathrm{rep}}$ | the defining representation on $S$ and its conjugate |
| $\mu_\pm=\lambda_\pm/(\varrho\,e^{i\theta_{\mathrm{pha}}})$ | the eigenvalues of the unit factor, the pair on one spinor slot |
| $\mathsf M^{\tilde Q}$ | the eigenbasis matrix model, not the Pauli model $\mathsf M_2$ |
| $\vec\Pi_{\mathrm{nil}}=\vec A+i\vec B$, $a$ | the null vector on the wall, $\lvert\vec A\rvert=\lvert\vec B\rvert=a$, $\vec A\cdot\vec B=0$ |
| $L_{\vec\Pi_{\mathrm{nil}}}$ | the left multiplication by the null vector, $L_{\vec\Pi_{\mathrm{nil}}}^{2}=0$ |
| $J=L_i=R_i$ | the pure central phase of $\pi/2$, the complex structure |
| $g$ | the Minkowski form, $\langle\tilde Q\rangle_{\natural}$ on $\mathbb{B}_{\Psi}$ and $-\langle\tilde Q\rangle_{\natural}$ on $\mathbb{B}_{\Phi}$ |
| $GL(2,\mathbb{C})$ | the image of the one-sided action on the invertibles |
| $CO^{+}(1,3)$ | the image of the two-sided action on the invertibles |
| $U(1)$ | the kernel of the two-sided action, the central unit circle |

## Further Reading

- [Two-Sided Operators on the N-Regular Sector](two-sided-operators-on-the-n-regular-sector.html), for the two-sided operator, the spectral form of its exponential, the doubling rule and the cancellation of the phase.
- [The N-Regular, Spectrally Regular Sector](the-n-regular-spectrally-regular-sector.html), §*The Eigenbasis, the Nilpotents, and the Peirce Corners*, for the basis, the two Peirce spinor spaces and the diagonal action used here.
- [Relations between the Complete Polar Decomposition and Eigenbasis of an N-Regular Biquaternion](relations-between-the-complete-polar-decomposition-and-eigenbasis-of-an-n-regular-biquaternion.html), for the general dictionary between the spectral data and the polar angles when the axes do not commute.
- [The Complete Polar Decomposition of an N-Regular Biquaternion](the-complete-polar-decomposition-of-an-n-regular-biquaternion.html), for the four factors, the modulus, the branch and the domain, and §*The Operator Reading: the Twist*, for the same word read on the spinor module.
- [The Complete Polar Decomposition and Remarkable Subspaces](the-complete-polar-decomposition-and-remarkable-subspaces.html), for the four exponents read against the six remarkable subspaces and the sector blocks, and §*The Action on the Two Halves*, for the detailed action on the two sectors, the boost matrices and the infinitesimal split of the rotor and the boost.
- [The Eigenbasis of a Spectrally Regular Biquaternion](the-eigenbasis-of-a-spectrally-regular-biquaternion.html), §*The $4\times4$ Diagonalising Matrix*, for the left and right regular representations and their eigenvalues.
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the Lorentz group in biquaternionic form and the double cover.
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), §*The Defining Representation and the Weyl Spinors*, for the Weyl spinors and the half-spin in the representation-theoretic language.
- [Four-Vectors and the Interval](../articles_physics/four-vectors-and-the-interval.html) and [States, Observables and the Born Weight](../articles_physics/states-observables-and-the-born-weight.html), for the physical interpretation of the two real forms exchanged by the phase.
- [$M_2(\mathbb{R})$ Hyperbolic Representation : Operators](m2r-hyperbolic-representation-operators.html), for the commutative case where $L=R$, the one-sided operator is the regular representation, and the half-angle disappears.
- [$M_2(\mathbb{C})$ Reduced Representation : Operators](m2c-reduced-representation-operators.html), for the commutative reduced biquaternion case where $L=R$, the one-sided operator carries the full parameters, and the two-sided operator is the modulus squared.
