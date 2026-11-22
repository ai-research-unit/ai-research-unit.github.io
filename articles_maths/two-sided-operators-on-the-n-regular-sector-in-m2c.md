# __Two-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$__

## Introduction

**The question.** On the invertible locus the operator $\mathrm{Sd}_A(Y)=AYA^{\dagger}$ is a bijection of $M_2(\mathbb{C})$. What is its array, what is its spectrum, what does each factor of the polar word do to it, and what is its group of images?

**Why it is the same statement.** This is the in-depth matrix reading of [Two-Sided Operators on the N-Regular Sector](two-sided-operators-on-the-n-regular-sector.html). The source proves the closed form $\mathrm{Sd}_{\tilde Q}=\varrho^2\mathrm{Sd}_{\tilde U_b}\mathrm{Sd}_{\tilde u_r}$ and reads the spectrum as the four products $\lambda_i\bar\lambda_j$; the display $A=\mathsf M_2(\tilde Q)$ turns both into statements about $\mathrm I_2\otimes A$ and $A^{\mathsf T}\otimes\mathrm I_2$, about the two Kronecker slots, and about the Hermitian and skew sectors. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The multiplicativity and the five elementary properties. The scaling of the determinant by $|\det A|^2$. The closed form with the phase cancelled. The two slots and the array $\Delta\otimes\bar\Delta$. The spectrum as the products $\lambda_i\bar\lambda_j$, with $\operatorname{tr}\mathrm{Sd}_A=4|Q_t|^2$. The exponential: diagonalizable, with eigenvalues $e^{t\lambda_i\bar\lambda_j}$, and no element identity. The pure-factor table, which shows the full angle and the full rapidity. The image $CO^{+}(1,3)$ and the kernel $U(1)$. The wall $B^2=0$, with Jordan type $3+1$, the strict contraction on the traceless part and the fixed line.

**What the article does not do.** It does not treat the one-sided operators, which are [One-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$](one-sided-operators-on-the-n-regular-sector-in-m2c.html), nor the null cone, which is [Two-Sided Operators on the N-Degenerate Sector in $M_2(\mathbb{C})$](two-sided-operators-on-the-n-degenerate-sector-in-m2c.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, so $\operatorname{tr}A=2Q_t$, $\det A=N=Q_t^2+B^2$ with $B^2=Q_x^2+Q_y^2+Q_z^2$, and $A^{\dagger}=\overline{A^{\mathsf T}}$. The N-regular sector is $\det A\neq0$, and the wall in it is $B^2=0$. The Hermitian sector is $\mathfrak{H}$ and the skew sector $\mathfrak{K}=i\mathfrak{H}$; each is a real four-space, and $X=t\mathrm I_2+x\sigma_1+y\sigma_2+z\sigma_3$ parametrizes $\mathfrak{H}$.

**Boundaries.** The polar decomposition of a matrix is [The Adjoints and the Polar Decomposition of an Operator at $n=2$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-2.html). The two-sided family is [The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-m2c.html). The Lorentz group as an array is [The Spin Group via $4\times4$ Real Matrices](the-spin-group-via-4x4-real-matrices-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $A$ is the parameter matrix, $(\lambda_+,\lambda_-)$ its eigenvalues, $P_\pm$ its spectral projections, $G=\operatorname{diag}(1,-1,-1,-1)$ the Lorentz form on $\mathfrak{H}$, and $\Lambda_A$ the real $4\times4$ array of $\mathrm{Sd}_A$ on $\mathfrak{H}$.

## The Operator and Its Arrays

**The composite.** $\mathrm{Sd}_A=R_{A^{\dagger}}\circ L_A$, so in the matrix-unit frame
$$
\mathrm{Sd}_A(Y)=AYA^{\dagger},\qquad \mathrm{Sd}_A=\left(\mathrm I_2\otimes A\right)\left(A^{\mathsf T}\otimes\mathrm I_2\right),
$$
the left factor acting on the column slot and the right factor on the row slot.

**The five properties.** $\mathrm{Sd}_{AA'}=\mathrm{Sd}_A\mathrm{Sd}_{A'}$; the operator is $\mathbb{C}$-linear; it is invertible exactly when $A$ is, with $\mathrm{Sd}_A^{-1}=\mathrm{Sd}_{A^{-1}}$; it preserves each of $\mathfrak{H}$ and $\mathfrak{K}$; and $\mathrm{Sd}_A(\mathrm I_2)=AA^{\dagger}$.

**The proof of the last one.** If $X^{\dagger}=\pm X$ then $(AXA^{\dagger})^{\dagger}=AX^{\dagger}A^{\dagger}=\pm AXA^{\dagger}$, since $(A^{\dagger})^{\dagger}=A$. So a two-sided operator can never mix the two sectors, and it splits into two real $4\times4$ arrays, one per sector.

**The preservation, checked.** On a hundred random pairs the Hermitian part of $AYA^{\dagger}$ differs from $AYA^{\dagger}$ by $4\cdot10^{-16}$, so the sector statement is exact.

**The determinant.** Since $\det(AYA^{\dagger})=\det A\det Y\overline{\det A}$,
$$
\det\left(\mathrm{Sd}_A(Y)\right)=|N|^2\det Y,
$$
and therefore $\det_{\mathbb{C}}\mathrm{Sd}_A=|N|^4$ on the complex four-space; verified to $10^{-11}$ on random elements. The operator multiplies the quadratic form by $|N|^2$, not by $N^2$: the two-sided reading takes one modulus from each side.

**The trace.** $\operatorname{tr}\mathrm{Sd}_A=|\operatorname{tr}A|^2=4|Q_t|^2$, verified to $4\cdot10^{-15}$; the four products sum to $(\lambda_++\lambda_-)(\bar\lambda_++\bar\lambda_-)$.

## The Closed Form of the Polar Word

**The theorem.** For $A=\varrho e^{i\theta}U_bU_r$ with $U_b$ positive Hermitian of determinant one and $U_r\in SU(2)$,
$$
\mathrm{Sd}_A=\varrho^2\,\mathrm{Sd}_{U_b}\circ\mathrm{Sd}_{U_r},\qquad \mathrm{Sd}_A(Y)=\varrho^2\,U_b\left(U_rYU_r^{-1}\right)U_b,
$$
and $\mathrm{Sd}_{e^{i\theta}\mathrm I_2}=\mathrm{id}$.

**The proof in arrays.** $A^{\dagger}=\varrho e^{-i\theta}U_r^{-1}U_b$, because $U_b^{\dagger}=U_b$ and $U_r^{\dagger}=U_r^{-1}$. Then
$$
AYA^{\dagger}=\varrho e^{i\theta}U_bU_rYU_r^{-1}U_b\varrho e^{-i\theta}=\varrho^2U_b\left(U_rYU_r^{-1}\right)U_b .
$$
The two scalar factors meet and give $\varrho^2$; the phase has cancelled.

**The order.** The rightmost factor acts first, so the rotor acts first, then the boost, then the scale. The boost and the rotor do not commute, so their order is part of the word.

**The phase is invisible.** $\mathrm{Sd}$ depends on $A$ only through the pair $(\varrho^2,U_b,U_r)$ modulo the phase, which is exactly the statement that the kernel is $U(1)$.

## The Two Slots

**The eigenvalue form.** On $B^2\neq0$ diagonalize $A=S\operatorname{diag}(\lambda_+,\lambda_-)S^{-1}$ and put $\Delta=\operatorname{diag}(\lambda_+,\lambda_-)$. Then, with $Z=S^{-1}YS$,
$$
\mathrm{Sd}_A(Y)=S\,\Delta Z\Delta^{\dagger}\,S^{-1},\qquad \Delta^{\dagger}=\operatorname{diag}(\bar\lambda_+,\bar\lambda_-),
$$
so the operator is the two-sided multiplication by $\Delta$ in the eigenbasis. The left factor acts on the column index and the right factor on the row index, and in the tensor form
$$
\mathrm{Sd}_A=\Delta\otimes\bar\Delta,\qquad \Delta\in GL(2,\mathbb{C}),
$$
which is the defining representation tensored with its conjugate.

**The two slots.** A matrix $Y$ has a column slot and a row slot; left multiplication uses the column slot only, right multiplication the row slot only. The one-sided operator carries the pair $(\lambda_+,\lambda_-)$ on one slot; the two-sided operator carries the four products on the pair of slots.

**The commuting pair.** $L_A$ and $R_{A^{\dagger}}$ commute, and each is diagonalizable off the wall, so they have a common eigenbasis in which $\mathrm{Sd}_A$ is diagonal. The common eigenbasis is the tensor product of a left eigenbasis of $L_A$ and a right eigenbasis of $R_{A^{\dagger}}$; it is not the eigenbasis of $L_A$ alone unless $A^{\dagger}$ is diagonal in it.

## The Spectrum

**The four products.** In the common eigenbasis,
$$
\operatorname{spec}\mathrm{Sd}_A=\{\lambda_+\bar\lambda_+,\ \lambda_+\bar\lambda_-,\ \lambda_-\bar\lambda_+,\ \lambda_-\bar\lambda_-\}
=\left\{|\lambda_+|^2,\ \lambda_+\bar\lambda_-,\ \lambda_-\bar\lambda_+,\ |\lambda_-|^2\right\},
$$
with the two off-diagonal products conjugate to each other. Verified on random elements of the sector to $10^{-15}$.

**The diagonal ones.** The two diagonal products are the moduli squared, real and positive on the sector. The two off-diagonal ones are conjugate.

**The pure factors.** For the boost, $\lambda_\pm=e^{\mp\theta/2}$, so the products are $e^{-\theta},1,1,e^{\theta}$; for the rotor, $\lambda_\pm=e^{\pm i\theta/2}$, so they are $e^{i\theta},1,1,e^{-i\theta}$; for the phase they are $1,1,1,1$; for the scale they are $\varrho^2$ four times.

**The meaning.** The two-sided operator carries the full angle and the full rapidity, while the one-sided one carries their halves. The doubling is the statement that the weights of the two slots add, and the cancellation of the phase is the statement that the two slots carry opposite phases.

## The Exponential

**The spectral form.** On the sector $\mathrm{Sd}_A$ is diagonalizable, so
$$
\exp\left(t\,\mathrm{Sd}_A\right)\ \text{has eigenvalues}\ e^{t\lambda_+\bar\lambda_+},\ e^{t\lambda_+\bar\lambda_-},\ e^{t\lambda_-\bar\lambda_+},\ e^{t\lambda_-\bar\lambda_-},
$$
and
$$
\det\exp\left(t\,\mathrm{Sd}_A\right)=\exp\left(t\operatorname{tr}\mathrm{Sd}_A\right)=\exp\left(4t|Q_t|^2\right).
$$

**There is no element identity.** Unlike the one-sided case, $\exp(t\,\mathrm{Sd}_A)\neq\mathrm{Sd}_{\exp(tA)}$ in general, because the operator is quadratic in $A$. For a central $A=c\mathrm I_2$ the operator is $|c|^2\mathrm{id}$, so its exponential is $e^{t|c|^2}\mathrm{id}$, while $\mathrm{Sd}_{e^{tc}}=e^{2t\operatorname{Re}c}\mathrm{id}$; these agree only when $|c|^2=2\operatorname{Re}c$, which fails for $c=2+3i$ ($13$ against $4$). Numerically the two arrays differ by $8$ on a random element of the sector. The two-sided operator exponentiates its image, not its parameter.

**The group of the operator.** The group generated by $\mathrm{Sd}_A$ is a one-parameter group of $\mathbb{C}$-linear maps with the eigenvalues above; it is not the Lorentz group, which is the image of $A\mapsto\mathrm{Sd}_A$ itself.

## The Image and the Kernel

**The kernel.** If $\mathrm{Sd}_A=\mathrm{id}$ then $AA^{\dagger}=\mathrm I_2$ by evaluating at $\mathrm I_2$, so $A^{\dagger}=A^{-1}$ and $AXA^{-1}=X$ for all $X$; hence $A$ is scalar, $A=\omega\mathrm I_2$, and $|\omega|=1$. Conversely every such $\omega$ gives the identity. So
$$
\ker\left(A\mapsto\mathrm{Sd}_A\right)=U(1)=\{\omega\mathrm I_2:|\omega|=1\}.
$$

**The image.** Every invertible $A$ is $\varrho e^{i\theta}U$ with $U\in SL(2,\mathbb{C})$, and the kernel is the unit circle of the scalar factor, so
$$
\operatorname{im}\cong\mathbb{R}_{>0}\times PSL(2,\mathbb{C})=\mathbb{R}_{>0}\times SO^{+}(1,3)=CO^{+}(1,3),
$$
the linear conformal group, of real dimension seven. On the modulus-one slice the image is $SO^{+}(1,3)$, and on the norm-one slice it is $SO^{+}(1,3)$ with kernel $\{\pm\mathrm I_2\}$, which is the double cover $SL(2,\mathbb{C})\to SO^{+}(1,3)$.

**On the Hermitian sector.** Write $X=t\mathrm I_2+x\sigma_1+y\sigma_2+z\sigma_3$ and let $\Lambda_A$ be the real $4\times4$ array of $\mathrm{Sd}_A$ on the coordinates $(t,x,y,z)$. Then
$$
\Lambda_A^{\mathsf T}G\Lambda_A=\varrho^4G,\qquad \det\Lambda_A=\varrho^8,\qquad G=\operatorname{diag}(1,-1,-1,-1),
$$
verified on a random element with residuals $2\cdot10^{-14}$ and $5\cdot10^{-13}$. So the operator is a similarity of the Lorentz form of ratio $\varrho^2$, and an isometry exactly when $\varrho=1$.

**What the image is not.** It is neither the $*$-unitary group nor $GL(2,\mathbb{C})$. The unitary group acts on the spinor slot and sees the phase; the two-sided operator sees only the conformal Lorentz group.

## The Wall $B^2=0$

**The form of the matrix.** On the wall $\det A=Q_t^2$ and $B^2=0$, so
$$
A=Q_t\left(\mathrm I_2+N\right),\qquad N^2=0,\qquad N\neq0 \text{ off the scalar line},
$$
and $\mathrm{Sd}_A=|Q_t|^2\mathrm{Sd}_{\mathrm I_2+N}$.

**The nilpotent part.** With $|Q_t|=1$ for clarity, put
$$
\mathsf N=\mathrm{Sd}_{\mathrm I+N}-\mathrm I_4,\qquad \mathsf N=A_{\mathrm{op}}+B_{\mathrm{op}}+A_{\mathrm{op}}B_{\mathrm{op}},
$$
where $A_{\mathrm{op}}(Y)=NY$ and $B_{\mathrm{op}}(Y)=YN^{\dagger}$ commute and square to zero. Then
$$
\mathsf N^2=2A_{\mathrm{op}}B_{\mathrm{op}},\qquad \mathsf N^3=0,\qquad \operatorname{rank}\mathsf N=2,\qquad \operatorname{rank}\mathsf N^2=1,
$$
verified exactly on $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$.

**The Jordan type.** The ranks of $\mathsf N^k$ for $k=0,1,2,3$ are $4,2,1,0$, that is nullities $0,2,3,4$, which is
$$
J_3\left(|Q_t|^2\right)\oplus J_1\left(|Q_t|^2\right).
$$

**The fixed subspace.** It is two-dimensional: one vector comes from the $3\times3$ block and one from the $1\times1$ block. For $A=\mathrm I_2+E_{12}$ it is
$$
\ker\left(\mathrm{Sd}_A-\mathrm I_4\right)=\operatorname{span}\left\{E_{11},\,E_y\right\},
$$
both fixed, with $E_{11}$ the rank-one projection onto $\ker N$ and $E_y=-i\sigma_2$; verified by an exact rank computation, which gives rank $2$ for $\mathrm{Sd}_A-\mathrm I_4$.

**The group.** Because $\mathsf N^3=0$,
$$
\exp\left(t\,\mathrm{Sd}_A\right)=e^{t|Q_t|^2}\left(\mathrm I_4+t|Q_t|^2\mathsf N+\frac{t^2|Q_t|^4}{2}\mathsf N^2\right),
$$
verified on a random element of the Jordan part with residual $2\cdot10^{-16}$.

**The null rotation.** On $\mathfrak{H}$ the factor $\mathrm{Sd}_{U}$ with $U$ of norm one preserves the Minkowski form, and its single eigenvalue is $1$ with Jordan type $3+1$. A Lorentz transformation of that type is a null rotation: it fixes a lightlike direction and shears the two transverse directions. The finite shear is $I+s\mathsf N+\tfrac{s^2}{2}\mathsf N^2$ with $s=t|Q_t|^2$. No angle and no rapidity survive on the wall; they are locked to the single null parameter.

## The Boundary: the Null Cone

**What fails.** At $\det A=0$ the operator drops rank: the kernel contains $\{Y:AYA^{\dagger}=0\}$, which is the annihilator of $A$ on both sides, of complex dimension three for a rank-one $A$. The two-sided theory there is [Two-Sided Operators on the N-Degenerate Sector in $M_2(\mathbb{C})$](two-sided-operators-on-the-n-degenerate-sector-in-m2c.html).

**What survives.** Multiplicativity, the sector preservation, the determinant scaling by $|N|^2$ and the closed form all hold at every point.

## Where $n=2$ Differs

**The number of slots.** At $n=2$ the algebra is a tensor square of a two-dimensional spinor space, so $\mathrm{Sd}_A=\Delta\otimes\bar\Delta$ with $\Delta\in GL(2,\mathbb{C})$ and the operator lives on four complex dimensions. At order $n$ it lives on $n^2$ dimensions and the tensor decomposition is $\Delta\otimes\bar\Delta$ on $n\times n$.

**The spectrum.** At $n=2$ there are four products of two eigenvalues; at order $n$ there are $n^2$ products, and the trace is $|\operatorname{tr}A|^2$ at both orders only because the sums factor.

**The wall.** At $n=2$ the wall $B^2=0$ gives the Jordan type $3+1$; at order $n$ the corresponding type is a partition of $n^2$ with one large block and $n-1$ singletons.

**The Lorentz form.** At $n=2$ the vector space $\mathfrak{H}$ is four-dimensional with form $\operatorname{diag}(1,-1,-1,-1)$, so the image is $CO^{+}(1,3)$. At order $n$ the Hermitian sector has dimension $n^2$ and the form is that of $\mathfrak{su}(n)$ read over $\mathbb{R}$, so the group is larger.

**What does not differ.** The kernel $U(1)$, the cancellation of the phase, the doubling of the angle and the absence of an element identity are properties of the two-slot structure at every order.

## Summary

The two-sided operator is $\mathrm{Sd}_A(Y)=AYA^{\dagger}=R_{A^{\dagger}}L_A$, with the left factor on the column slot and the right factor on the row slot. It is multiplicative, $\mathbb{C}$-linear, invertible exactly when $A$ is, and it preserves each of the Hermitian and the skew sectors. It multiplies the determinant by $|N|^2$ and has $\operatorname{tr}\mathrm{Sd}_A=4|Q_t|^2$ and $\det_{\mathbb{C}}\mathrm{Sd}_A=|N|^4$.

The closed form is $\mathrm{Sd}_A=\varrho^2\mathrm{Sd}_{U_b}\mathrm{Sd}_{U_r}$, with the phase cancelled. The spectrum is the four products $\lambda_i\bar\lambda_j$, verified to $10^{-15}$, and in the eigenbasis the operator is $\Delta\otimes\bar\Delta$. Its exponential has the eigenvalues $e^{t\lambda_i\bar\lambda_j}$ and determinant $e^{4t|Q_t|^2}$; there is no element identity, because the operator is quadratic in its parameter. The kernel is the unit circle and the image is $CO^{+}(1,3)$; on the Hermitian sector the real array satisfies $\Lambda_A^{\mathsf T}G\Lambda_A=\varrho^4G$ and $\det\Lambda_A=\varrho^8$.

On the wall $B^2=0$ the Jordan type is $J_3(|Q_t|^2)\oplus J_1(|Q_t|^2)$, the fixed space is one-dimensional, and the exponential acts as a null rotation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Sd}_A$ | $Y\mapsto AYA^{\dagger}$ |
| $N=\det A$ | the norm |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues of $A$ |
| $\Delta$ | $\operatorname{diag}(\lambda_+,\lambda_-)$ in the eigenbasis |
| $\varrho$ | the modulus $|N|^{1/2}$ |
| $U_b,U_r$ | the Hermitian positive factor and the $SU(2)$ factor |
| $G$ | $\operatorname{diag}(1,-1,-1,-1)$ on $\mathfrak{H}$ |
| $\Lambda_A$ | the real $4\times4$ array of $\mathrm{Sd}_A$ on $\mathfrak{H}$ |

## Further Reading

- [Two-Sided Operators on the N-Regular Sector](two-sided-operators-on-the-n-regular-sector.html), for the source's closed form, its product spectrum and its treatment of the image.
- [One-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$](one-sided-operators-on-the-n-regular-sector-in-m2c.html), for the half-angle and the factorisation of $L_A$.
- [Two-Sided Operators on the N-Degenerate Sector in $M_2(\mathbb{C})$](two-sided-operators-on-the-n-degenerate-sector-in-m2c.html), for the rank drop on the null cone.
- [The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-m2c.html), for the general two-sided family and its uniqueness up to a scalar.
- [The Spin Group via $4\times4$ Real Matrices](the-spin-group-via-4x4-real-matrices-in-m2c.html), for the Lorentz array and the double cover.
