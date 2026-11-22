# __One-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$__

## Introduction

**The question.** On the invertible locus $\det A\neq0$ the two one-sided operators $L_A(Y)=AY$ and $R_A(Y)=YA$ are bijections of $M_2(\mathbb{C})$. What are their arrays, their spectra, their behaviour on the two Hermitian sectors, and their one-parameter groups?

**Why it is the same statement.** This is the in-depth matrix reading of [One-Sided Operators on the N-Regular Sector](one-sided-operators-on-the-n-regular-sector.html). The source works frame-free; the display $A=\mathsf M_2(\tilde Q)$ turns the factorisation $L_{\tilde Q}=L_\varrho L_{\tilde U_b}L_{\tilde u_r}$ into a product of three explicit $4\times4$ arrays, the Peirce spinors into the two eigenspaces of $A$, and the sector criterion into a statement about Hermitian and skew matrices. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The arrays of $L_A$ and $R_A$ in the two frames, and their block form on the splitting of $M_2(\mathbb{C})$ into Hermitian and skew matrices. The elementary properties and the multiplicativity laws. The norm and the determinant: $\det_{\mathbb{C}}L_A=(\det A)^2$ and $\operatorname{tr}L_A=2\operatorname{tr}A$. The eigenbasis and the two minimal right ideals, which are the two spinor spaces. The sector criterion: the only one-sided real Lorentz transformations are $\pm\mathrm{id}$. The pure central phase $A=i\mathrm I_2$ as the exchange of the two sectors. The four factors as explicit matrices. The exponential theorem $\exp(tL_A)=L_{\exp(tA)}$ with the half-angle spectrum. The image and the kernel. The wall $B^2=0$ with its Jordan type $2+2$ and the shear of its exponential.

**What the article does not do.** It does not treat the two-sided operator, which is [Two-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$](two-sided-operators-on-the-n-regular-sector-in-m2c.html), nor the null cone, which is [One-Sided Operators on the N-Degenerate Sector in $M_2(\mathbb{C})$](one-sided-operators-on-the-n-degenerate-sector-in-m2c.html). It does not repeat the general operator theory of [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, so $\operatorname{tr}A=2Q_t$ and $\det A=N=Q_t^2+B^2$ with $B^2=Q_x^2+Q_y^2+Q_z^2$. The N-regular sector is $\det A\neq0$; the wall is $B^2=0$. The Hermitian adjoint is $A^{\dagger}=\overline{A^{\mathsf T}}$, and the two real sectors are the Hermitian matrices $\mathfrak{H}$ and the skew matrices $\mathfrak{K}=i\mathfrak{H}$, each of real dimension four. Arrays are printed in the coefficient frame $(E_t,E_x,E_y,E_z)$ unless the matrix-unit frame is named.

**Boundaries.** The four sector table is [Introduction to the Operators on the Four Sectors in $M_2(\mathbb{C})$](introduction-to-the-operators-on-the-four-sectors-in-m2c.html). The adjoints and the polar decomposition are [The Adjoints and the Polar Decomposition of an Operator at $n=2$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-2.html). The spin group is [The Spin Group via $4\times4$ Real Matrices](the-spin-group-via-4x4-real-matrices-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $A$ is the matrix of the parameter. $\mathfrak{H}$ and $\mathfrak{K}$ are the Hermitian and the skew sectors. $D_A$ and $O_A$ are the diagonal and off-diagonal blocks of $L_A$. $P_\pm$ are the spectral projections of $A$ at $\lambda_\pm$.

## The Operator and Its Arrays

**The two arrays.** With $Y$ read as a column in the matrix-unit frame,
$$
L_A=\mathrm I_2\otimes A,\qquad R_A=A^{\mathsf T}\otimes\mathrm I_2 .
$$
Both are invertible exactly when $A$ is, with $L_A^{-1}=L_{A^{-1}}$ and $R_A^{-1}=R_{A^{-1}}$.

**The coefficient frame.** In the basis $(E_t,E_x,E_y,E_z)$,
$$
L_A=Q_t\mathrm I_4+Q_xM_x+Q_yM_y+Q_zM_z,
$$
with the signed-permutation tables $M_x,M_y,M_z$ of [Introduction to the Operators on the Four Sectors in $M_2(\mathbb{C})$](introduction-to-the-operators-on-the-four-sectors-in-m2c.html). The verification of this identity on a random element gives residual $4\cdot10^{-16}$, and the entries are integral, so the array is the multiplication table read aloud.

**The block form.** The real space $M_2(\mathbb{C})$ splits as $\mathfrak{H}\oplus\mathfrak{K}$, each summand of real dimension four. In that splitting $L_A$ is a block matrix
$$
L_A=\begin{pmatrix}D_A & O_A\\ O_A & D_A\end{pmatrix},\qquad
D_A(X)=\tfrac12\left(AX+XA^{\dagger}\right),\qquad
O_A(X)=\tfrac12\left(AX-XA^{\dagger}\right).
$$
The diagonal block preserves each sector and the off-diagonal block exchanges them, both read over $\mathbb{R}$.

**The central case.** For $A=c\mathrm I_2$ the two blocks are the scalars $\operatorname{Re}(c)$ and $i\operatorname{Im}(c)$: a real scalar preserves both sectors, a purely imaginary one exchanges them.

**Rank and invertibility.** On the N-regular sector $\det A\neq0$, so $L_A$ and $R_A$ have rank $4$, kernel $0$ and image all of $M_2(\mathbb{C})$. The whole global behaviour is decided by $\det A$ alone.

## Elementary Properties and Multiplicativity

**The five properties.** For all $A,A'\in M_2(\mathbb{C})$: both operators are $\mathbb{C}$-linear; $L_AL_{A'}=L_{AA'}$ and $R_AR_{A'}=R_{A'A}$; $L_AR_{A'}=R_{A'}L_A$; the maps $A\mapsto L_A$ and $A\mapsto R_A$ are injective; and both are invertible exactly when $A$ is. Injectivity follows from $L_A(\mathrm I_2)=A$.

**Multiplicativity of a single operator.** A single $L_A$ is an algebra endomorphism only for a central idempotent, since $L_A(XY)=AXY$ while $L_A(X)L_A(Y)=AXAY$. The only central idempotents of $M_2(\mathbb{C})$ are $0$ and $\mathrm I_2$, so the only multiplicative left multiplication is the identity.

**Linear against quadratic.** $A\mapsto L_A$ is linear and faithful; $A\mapsto AYA^{\dagger}$ is quadratic and kills the central circle. The one-sided operator carries the whole parameter, the two-sided one carries it up to a phase.

**Translation, not conjugation.** $L_A$ is a left translation; it is an automorphism only for a scalar $A$. The inner automorphism $X\mapsto AXA^{-1}$ is $L_AR_{A^{-1}}$, which is a two-sided object.

## The Norm and the Determinant

**The norm is multiplicative.** Since $\det(AY)=\det A\det Y$,
$$
N(L_AY)=\det(A)\det(Y)=N(A)N(Y),
$$
and the same holds for $R_A$. On the norm-one slice the operators are $\mathbb{C}$-orthogonal: they preserve $N$ and have complex determinant $1$.

**The determinant and the trace.** In arrays,
$$
\det_{\mathbb{C}}L_A=(\det A)^2=N^2,\qquad \operatorname{tr}L_A=2\operatorname{tr}A=4Q_t .
$$
Verified on a hundred random elements, with residuals $9\cdot10^{-14}$ and $9\cdot10^{-16}$. The determinant is the square because $L_A=\mathrm I_2\otimes A$ acts on two copies of the defining space; the trace is the sum of the two eigenvalues of $A$, each taken twice.

**What the operators do not preserve.** $L_A$ multiplies the complex quadratic form by $N$, and it is not in general an isometry of either real sector. A complex isometry can exchange the two sectors, and the phase does exactly that.

## The Eigenbasis and the Two Spinor Spaces

**The spectral data.** For $B^2\neq0$ put $\lambda_\pm=Q_t\pm iB$, so $\lambda_+\lambda_-=\det A$ and $\lambda_++\lambda_-=\operatorname{tr}A$. The matrix is diagonalizable,
$$
A=S\operatorname{diag}(\lambda_+,\lambda_-)S^{-1},\qquad S\in GL(2,\mathbb{C}),
$$
and the two spectral projections
$$
P_+=\frac{A-\lambda_-\mathrm I_2}{\lambda_+-\lambda_-},\qquad P_-=\mathrm I_2-P_+
$$
are rank-one, satisfy $AP_\pm=\lambda_\pm P_\pm$, $P_+P_-=0$ and $P_++P_-=\mathrm I_2$.

**The eigenspaces of the operator.** Because $L_A(Y)=AY$,
$$
\{Y:AY=\lambda_+Y\}=P_+M_2(\mathbb{C}),\qquad \{Y:AY=\lambda_-Y\}=P_-M_2(\mathbb{C}),
$$
the two minimal right ideals, each of complex dimension two, with bases $(P_+,P_+J)$ and $(P_-,P_-J)$ for any $J$ with $P_-JP_+\neq0$. The spectrum of $L_A$ is
$$
\operatorname{spec}L_A=\{\lambda_+,\lambda_+,\lambda_-,\lambda_-\},
$$
computed on a random element of the sector and matching to $10^{-15}$; the eigenspace of $\lambda_+$ has dimension exactly two. The two ideals are the two spinor spaces of the source: $S_-=M_2P_-$ and $S_+=M_2P_+$.

**No eigenbasis on the wall.** When $B^2=0$ the two eigenvalues coincide, the projections $P_\pm$ are not defined from $A$, and $L_A$ is not diagonal in any Peirce basis. That is the next article's wall, treated here in its last section.

**The two-sided comparison.** $R_A$ has the same spectrum, with eigenspaces $P_+M_2$ and $P_-M_2$ replaced by the left ideals $M_2P_+$ and $M_2P_-$; and $\mathrm{Sd}_A$ has the four products $\lambda_i\bar\lambda_j$, so it loses one factor of the spectrum. The doubling is the subject of [Two-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$](two-sided-operators-on-the-n-regular-sector-in-m2c.html).

## The Two Real Sectors and the Sector Criterion

**The splitting.** $\mathfrak{H}=\{X:X^{\dagger}=X\}$ and $\mathfrak{K}=\{X:X^{\dagger}=-X\}$, with $\mathfrak{K}=i\mathfrak{H}$, both of real dimension four, and $M_2(\mathbb{C})=\mathfrak{H}\oplus\mathfrak{K}$ over $\mathbb{R}$.

**The block formula, verified.** With $D_A$ and $O_A$ as above, $D_A(\mathfrak{H})\subset\mathfrak{H}$ and $O_A(\mathfrak{H})\subset\mathfrak{K}$, and symmetrically. The two identities
$$
D_A(X)=\tfrac12\left(AX+(AX)^{\dagger}\right),\qquad O_A(X)=\tfrac12\left(AX-(AX)^{\dagger}\right)
$$
are the Hermitian and the skew part of the product, computed on a hundred random pairs with residual $5\cdot10^{-16}$.

**The sector criterion.** A one-sided operator $L_A$ maps $\mathfrak{H}$ into itself exactly when $A$ is a real scalar: the value at $X=\mathrm I_2$ gives $A\in\mathfrak{H}$, and then the value at $X=\sigma_1,\sigma_2,\sigma_3$ forces $A$ real. So the only one-sided real Lorentz transformations are $\pm\mathrm{id}$, and a single left multiplication never produces a non-trivial real orthogonal map of the sector.

**The central phase.** For $A=i\mathrm I_2$ the block form is $D=0$, $O=i\,\mathrm{id}$, and
$$
L_i(\mathfrak{H})=\mathfrak{K},\qquad L_i(\mathfrak{K})=\mathfrak{H},\qquad L_i^2=-\mathrm{id}.
$$
So $L_i$ is a complex structure $J$ on the real eight-space, with $J^{-1}=L_{-i}$ and $J^3=-J$. The two-sided operator cancels it: $\mathrm{Sd}_i(Y)=iY(-i)=Y$.

**The general phase.** For $A=e^{i\theta}\mathrm I_2$ the blocks are $\cos\theta\,\mathrm{id}$ and $i\sin\theta\,\mathrm{id}$: at $\theta\equiv0$ both sectors are preserved, at $\theta\equiv\tfrac{\pi}{2}$ they are exchanged, and otherwise each sector is mixed with the other.

## The Four Factors as Matrices

**The scale.** $A=\varrho\mathrm I_2$ with $\varrho>0$ gives $L_A=R_A=\varrho\,\mathrm{id}$, of determinant $\varrho^4$ on the complex four-space and $\varrho^8$ on the real eight-space.

**The phase.** $A=e^{i\theta}\mathrm I_2$ gives $e^{i\theta}\mathrm{id}$, of determinant $e^{4i\theta}$.

**The boost.** $A=\cosh\tfrac{\theta}{2}\mathrm I_2+\sinh\tfrac{\theta}{2}\,u\cdot\sigma$ for a real unit $u$, which is Hermitian, positive definite and of determinant $1$:
$$
A=A^{\dagger},\qquad \det A=\cosh^2\tfrac\theta2-\sinh^2\tfrac\theta2=1,\qquad \operatorname{tr}A=2\cosh\tfrac\theta2\ge 2 .
$$
Its eigenvalues are $e^{\pm\theta/2}$, real and reciprocal, which is the half-rapidity.

**The rotor.** $A=\cos\tfrac{\theta}{2}\mathrm I_2-i\sin\tfrac{\theta}{2}\,u\cdot\sigma$, which is unitary and of determinant $1$:
$$
AA^{\dagger}=\mathrm I_2,\qquad \det A=1,\qquad A\in SU(2).
$$
Its eigenvalues are $e^{\pm i\theta/2}$, on the unit circle, which is the half-angle.

**The factorisation.** Every invertible $A$ factors uniquely as
$$
A=\varrho\,e^{i\theta}\,U_b\,U_r,\qquad U_b \text{ positive Hermitian of determinant }1,\quad U_r\in SU(2),
$$
and the two one-sided operators factor in the corresponding orders: $L_A=L_\varrho L_{e^{i\theta}}L_{U_b}L_{U_r}$ and $R_A=R_{U_r}R_{U_b}R_{e^{i\theta}}R_\varrho$.

**The table.**

| factor | matrix | one-sided operator | sector action | effect on $\det$ |
|---|---|---|---|---|
| scale | $\varrho\mathrm I_2$ | $\varrho\,\mathrm{id}$ | preserves both | $\varrho^2$ |
| phase | $e^{i\theta}\mathrm I_2$ | $e^{i\theta}\mathrm{id}$ | preserves at $\theta\equiv0$, exchanges at $\theta\equiv\tfrac\pi2$ | $e^{2i\theta}$ |
| boost | Hermitian, $\det1$, $\operatorname{tr}\ge2$ | $L_{U_b}$ | mixes | $1$ |
| rotor | $SU(2)$ | $L_{U_r}$ | mixes | $1$ |

## The Exponential of the One-Sided Operator

**The element identity.** For every $A$ and every $t\in\mathbb{C}$,
$$
\exp\left(tL_A\right)=L_{\exp(tA)},\qquad \exp\left(tR_A\right)=R_{\exp(tA)} .
$$
The proof is the exponential series and $L_A^n=L_{A^n}$; the identity was checked numerically on a random element with residual $7\cdot10^{-16}$.

**The spectrum of the group.** With $\lambda_\pm=Q_t\pm iB$,
$$
\det\exp(tL_A)=\exp\left(2t\operatorname{tr}A\right)=\exp(4tQ_t),\qquad
\operatorname{tr}\exp(tL_A)=2\left(e^{t\lambda_+}+e^{t\lambda_-}\right)=4e^{tQ_t}\cos(tB),
$$
verified to $2\cdot10^{-15}$ on a random element.

**The rate is the eigenvalue.** For a central $A=c\mathrm I_2$ the group is $e^{tc}\mathrm{id}$; the two-sided group of the same element is $e^{t|c|^2}\mathrm{id}$. The one-sided rate is $c$, the two-sided rate is $|c|^2$.

**The half-spin theorem.** For the rotor $A=\exp(\tfrac\theta2 u\cdot\sigma)$ the operator has eigenvalues $e^{\pm i\theta/2}$, so a spinor is multiplied by half the angle. For the boost $A=\exp(\tfrac\theta2 u\cdot\sigma)$ in the Hermitian sense the eigenvalues are $e^{\pm\theta/2}$, so a spinor is boosted by half the rapidity. The two-sided operator, which acts on the tensor square, produces the full angle and the full rapidity.

**The weight relation.** $\mathbb{B}\cong S\otimes S^*$ with $S=\mathbb{C}^2$, and $L_A=\Delta(A)\otimes1$, $R_A=1\otimes\Delta(A)^{\mathsf T}$. That is the matrix form of the two Kronecker slots, and the two factors commute, so the exponents add.

## The Image and the Kernel

**On the sector.** Both images are all of $M_2(\mathbb{C})$ and both kernels vanish. So the one-sided operators distinguish nothing inside the N-regular sector: the whole of the geometry is in the spectrum and the sectors, not in the rank.

**Comparison with the two-sided operator.** $\mathrm{Sd}_A$ is also invertible on the sector, with kernel $0$, but it drops rank on the wall and on the null cone, where the one-sided operators keep rank $4$. The one-sided rank drops only when $\det A=0$.

**Why.** $\mathrm{Sd}_A$ is quadratic in $A$ and its kernel is $\{Y:AYA^{\dagger}=0\}$, which contains the annihilators of $A$; $L_A$ is linear and its kernel is only $\{Y:AY=0\}$.

## The Wall $B^2=0$

**The form of the matrix.** On the N-regular wall, $\det A=Q_t^2\neq0$ and $B^2=0$, so the single eigenvalue is $Q_t$ and
$$
A=Q_t\left(\mathrm I_2+N\right),\qquad N^2=0,\qquad N\neq0 \text{ off the scalar line}.
$$
The scalar line is $N=0$; the Jordan part is $N\neq0$.

**The operator.** $L_A=Q_t\left(\mathrm I_4+L_N\right)$ with $L_N^2=L_{N^2}=0$, so $L_A-Q_t\mathrm I_4$ is nilpotent of index two. Its ranks are $4,2,0$ for the powers $0,1,2$, that is nullities $0,2,4$, which is the Jordan type
$$
J_2(Q_t)\oplus J_2(Q_t).
$$
The computation is exact on $A=\begin{pmatrix}2+i&3\\0&2+i\end{pmatrix}$ and on a hundred random elements of the Jordan part.

**The shear.** Because $L_N^2=0$,
$$
\exp\left(tL_A\right)=e^{tQ_t}\left(\mathrm I_4+tQ_tL_N\right),
$$
a unipotent times a scalar: the one-parameter group is a shear, not a diagonal group. On the scalar line it is the pure scaling $e^{tQ_t}\mathrm I_4$.

**Comparison with the spectrum off the wall.** Off the wall the group is diagonalizable with eigenvalues $e^{t\lambda_\pm}$, each twice; on the wall the two eigenvalues have collided and the group has a linear term in $t$. That is the whole difference the wall makes.

## The Boundary: the Null Cone

**What fails.** At $\det A=0$ the operator drops to rank $2$, the kernel is the annihilator, and the parameter map is no longer an isomorphism onto an open set. The one-sided theory there is [One-Sided Operators on the N-Degenerate Sector in $M_2(\mathbb{C})$](one-sided-operators-on-the-n-degenerate-sector-in-m2c.html).

**What survives.** Multiplicativity, the identity $L_{A^n}=L_A^n$, and the exponential theorem hold at every point, since none of them uses invertibility.

## Where $n=2$ Differs

**The rotation plane.** At $n=2$ there is one rotation plane and one boost direction, given by a single unit vector $u$ in $\mathbb{R}^3$; the boosts and the rotors form a one-parameter family each. At order $n$ the traceless part has dimension $n^2-1$ and there are $\binom{n}{2}$ rotation planes.

**The spinor spaces.** At $n=2$ the two spinor spaces have complex dimension two and are the minimal right ideals $P_\pm M_2$; the eigenvalues are two and each occurs twice. At order $n$ there are $n$ eigenspaces and each has dimension $n$.

**The discriminant.** At $n=2$ the wall is the single equation $B^2=0$ in one complex number; the Jordan type on it is $2+2$, which is a partition of $4$. At order $n$ the wall is a hypersurface of higher codimension and the Jordan type is a partition of $n^2$.

**What does not differ.** $\det L_A=(\det A)^2$, $\operatorname{tr}L_A=n\operatorname{tr}A$, multiplicativity and the exponential theorem hold at every order.

## Summary

The one-sided operators on the N-regular sector are $L_A(Y)=AY$ and $R_A(Y)=YA$, with arrays $\mathrm I_2\otimes A$ and $A^{\mathsf T}\otimes\mathrm I_2$ in the matrix-unit frame, and $\sum_\mu Q_\mu M_\mu$ in the coefficient frame. Both have rank $4$, kernel $0$ and image $M_2(\mathbb{C})$, and they multiply the norm: $N(AY)=\det(A)\det(Y)$. Their determinant and trace are $\det_{\mathbb{C}}L_A=N^2$ and $\operatorname{tr}L_A=4Q_t$.

The spectrum is $\lambda_\pm=Q_t\pm iB$ each twice, with the two eigenspaces the minimal right ideals $P_\pm M_2(\mathbb{C})$, which are the two spinor spaces. On the splitting $M_2=\mathfrak{H}\oplus\mathfrak{K}$ the operator is $\begin{pmatrix}D_A&O_A\\O_A&D_A\end{pmatrix}$ with $D_A$ the Hermitian and $O_A$ the skew part of the product; a one-sided operator preserves $\mathfrak{H}$ only for a real scalar, and $A=i\mathrm I_2$ gives the complex structure that exchanges the two sectors.

The four factors are the scalar $\varrho\mathrm I_2$, the phase $e^{i\theta}\mathrm I_2$, the positive Hermitian matrix of determinant $1$ and the unitary matrix of determinant $1$, with exponents $\ln\varrho$, $i\theta$, $\pm\theta/2$ and $\pm i\theta/2$. The exponential identity is $\exp(tL_A)=L_{\exp(tA)}$, with $\operatorname{tr}\exp(tL_A)=4e^{tQ_t}\cos(tB)$. On the wall $B^2=0$ the operator is $Q_t(\mathrm I_4+L_N)$ with $L_N^2=0$, of Jordan type $J_2\oplus J_2$, and its group is the shear $e^{tQ_t}(\mathrm I_4+tQ_tL_N)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=\mathsf M_2(\tilde Q)$ | the matrix of the parameter |
| $L_A,R_A$ | $Y\mapsto AY$ and $Y\mapsto YA$ |
| $\mathfrak{H},\mathfrak{K}$ | the Hermitian and the skew sectors |
| $D_A,O_A$ | the blocks of $L_A$ on $\mathfrak{H}\oplus\mathfrak{K}$ |
| $P_\pm$ | the spectral projections of $A$ |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues of $A$ |
| $N=\det A$ | the norm |
| $B^2$ | the vector form $\det A-\tfrac14(\operatorname{tr}A)^2$ |

## Further Reading

- [One-Sided Operators on the N-Regular Sector](one-sided-operators-on-the-n-regular-sector.html), for the source's frame-free proof of the factorisation, the half-spin theorem and the wall.
- [Two-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$](two-sided-operators-on-the-n-regular-sector-in-m2c.html), for the doubling rule and the products $\lambda_i\bar\lambda_j$.
- [One-Sided Operators on the N-Degenerate Sector in $M_2(\mathbb{C})$](one-sided-operators-on-the-n-degenerate-sector-in-m2c.html), for the null cone where the rank drops.
- [Introduction to the Operators on the Four Sectors in $M_2(\mathbb{C})$](introduction-to-the-operators-on-the-four-sectors-in-m2c.html), for the sector index and the four tables in one page.
- [The Exponential of a $2\times2$ Matrix and Its Image](the-exponential-of-a-2x2-matrix-and-its-image.html), for the matrix exponential at this size.
