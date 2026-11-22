# __The Clebsch–Gordan Decomposition of the Biquaternion Algebra in $M_2(\mathbb{C})$__

## Introduction

**The question.** The algebra carries four complex dimensions. Under conjugation by unitary matrices, how does it split, and why is the split $1\oplus3$ and nothing else?

**Why it is the same statement.** This is the in-depth matrix reading of [The Clebsch–Gordan Decomposition of the Biquaternion Algebra](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra.html). The source's projectors $P_0=\tfrac12(\mathrm{id}+\natural)$ and $P_1=\tfrac12(\mathrm{id}-\natural)$ become, under $A=\mathsf M_2(\tilde Q)$, the projectors onto the scalar line and onto the traceless part,
$$
P_0(Y)=\frac{\operatorname{tr}Y}{2}\,\mathrm I_2,\qquad P_1(Y)=Y-\frac{\operatorname{tr}Y}{2}\,\mathrm I_2,
$$
and the two-sided action becomes $Y\mapsto UYU^{\dagger}$. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The involution $\natural$ as the map $Y\mapsto(\operatorname{tr}Y)\mathrm I_2-Y$, and the two projectors. Their images: $\mathbb{C}\mathrm I_2$ and $\mathfrak{sl}_2$. The equivariance under unitary conjugation. The weights $\{-1,0,+1,0\}$ of the diagonal generator. The Casimir operator $\mathbf H^2_{\mathrm{tot}}=2P_1=\mathrm{id}-\natural$ as the map $Y\mapsto2Y-(\operatorname{tr}Y)\mathrm I_2$. The single-slot value $\tfrac34$. The reason no half-integer summand occurs, and why the slot is a factor and not a summand.

**What the article does not do.** It does not prove the addition rule; it does not resolve the summand into weight vectors, which is the axis-dependent step; and it does not treat the minimal left ideals that realise the slot, which are [Introduction to the Spin-Half Bispinors Spaces in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-in-m2c.html).

**Conventions.** $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, so $\operatorname{tr}A=2Q_t$. The coefficient basis is $(\mathrm I_2,-i\sigma_1,-i\sigma_2,-i\sigma_3)$; the coefficient-frame array of an operator is written in that basis. The involution $\natural$ acts on matrices by $A\mapsto\overline{A}$ and on operators by $T\mapsto\natural\circ T\circ\natural$. The inner product is $\langle X,Y\rangle=\tfrac12\operatorname{tr}(X^{\dagger}Y)$.

**Boundaries.** The dictionary is [The Pauli Representation : Operators](m2c-pauli-representation-operators.html). The two sides separately are [Operators Acting on One Side in $M_2(\mathbb{C})$](operators-acting-on-one-side-in-m2c.html) and [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html). The carriers built on the split are [From the Spin to the Carriers and the Closures in $M_2(\mathbb{C})$](the-carriers-the-representation-the-spin-and-the-closure-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html).

**Letters.** $Y$ is a general matrix, $\natural$ the matrix conjugation, $P_0,P_1$ the two projectors, $H_k$ the Hermitian generators, $\mathbf H^2_{\mathrm{tot}}$ the Casimir operator.

## The Involution in Matrices

**The map.** On the coefficient basis $\natural$ fixes $E_t=\mathrm I_2$ and negates $E_x,E_y,E_z=-i\sigma_k$. So its array is
$$
[\natural]=\operatorname{diag}(1,-1,-1,-1),
$$
and on a general matrix
$$
A^{\natural}=Q_t\mathrm I_2+(\text{vector part reversed})=\overline{A}.
$$
Equivalently, since $\overline{A}=(\operatorname{tr}A)\mathrm I_2-A$ for a $2\times2$ matrix,
$$
\natural(Y)=\left(\operatorname{tr}Y\right)\mathrm I_2-Y .
$$
Verified on random matrices with residual $6\cdot10^{-17}$.

**Linearity.** $\natural$ is complex-linear, $\natural(iY)=i\natural(Y)$, and involutive, $\natural^2=\mathrm{id}$. The Hermitian adjoint is the other composite, $Y^{\dagger}=\natural(Y)^{\mathsf T}$, and it is conjugate-linear. A conjugate-linear involution has no $\pm1$ eigenspaces inside a complex space, so the split must be built from $\natural$; this is the source's reason, read on the array.

**The trace form.** The map $Y\mapsto\operatorname{tr}(Y)\mathrm I_2$ is the projection onto the scalar line, and its kernel is the traceless part. Composing, one gets the three-term identity
$$
\natural = 2P_0-\mathrm{id},\qquad P_0(Y)=\frac{\operatorname{tr}Y}{2}\mathrm I_2 .
$$

## The Two Projectors

**The definition.** $P_0=\tfrac12(\mathrm{id}+\natural)$ and $P_1=\tfrac12(\mathrm{id}-\natural)$. On matrices,
$$
P_0(Y)=\frac{\operatorname{tr}Y}{2}\mathrm I_2,\qquad P_1(Y)=Y-\frac{\operatorname{tr}Y}{2}\mathrm I_2 .
$$

**The algebra.** $P_0^2=P_0$, $P_1^2=P_1$, $P_0P_1=P_1P_0=0$, $P_0+P_1=\mathrm{id}$; verified exactly on random matrices.

**The images.** $P_0M_2(\mathbb{C})=\mathbb{C}\mathrm I_2$, of complex dimension one; $P_1M_2(\mathbb{C})=\mathfrak{sl}_2(\mathbb{C})$, the traceless matrices, of complex dimension three. As arrays,
$$
[P_0]=\operatorname{diag}(1,0,0,0),\qquad [P_1]=\operatorname{diag}(0,1,1,1),
$$
and $1+3=4$.

**The equivariance.** For unitary $U$,
$$
P_0(UYU^{\dagger})=U P_0(Y)U^{\dagger},\qquad P_1(UYU^{\dagger})=U P_1(Y)U^{\dagger},
$$
because $\operatorname{tr}(UYU^{\dagger})=\operatorname{tr}Y$. So the split is invariant under the two-sided action, and it is the decomposition of the algebra as a module for that action.

**The one-sided failure.** The split does not commute with $Y\mapsto AY$: left multiplication moves the scalar line into the traceless part, $\operatorname{tr}(AY)=2Q_t\operatorname{tr}Y/2+\dots$. The split belongs to the diagonal action and not to either factor.

## The Casimir Is the Projector

**The adjoint arrays.** $H_k=\tfrac i2(L_k-R_k)$ is the Hermitian generator of the diagonal action, and $L_k-R_k$ is the coefficient-frame array of $Y\mapsto[E_k,Y]$. Each $L_k-R_k$ is real antisymmetric, verified exactly.

**The identity.** In arrays,
$$
\sum_k(L_k-R_k)^2=-8\,[P_1],\qquad \mathbf H^2_{\mathrm{tot}}=\sum_kH_k^2=2\,[P_1]=\mathrm{id}-\natural,
$$
verified exactly. On matrices the Casimir is the operator
$$
Y\mapsto 2Y-\left(\operatorname{tr}Y\right)\mathrm I_2,
$$
with eigenvalues $2$ on $\mathfrak{sl}_2$ and $0$ on $\mathbb{C}\mathrm I_2$.

**The weights.** The eigenvalues of $H_{\mathrm{tot},z}=\tfrac i2[E_z,\cdot]$ are $+1,0,0,-1$; verified. The weight set is $\{-1,0,+1,0\}$, the union of $\{-1,0,+1\}$ on the traceless part and $\{0\}$ on the scalar line.

**The two values.** $2=1\cdot(1+1)$ and $0=0\cdot(0+1)$, so the traceless part is spin one and the scalar line is spin zero. The label is not bookkeeping: the Casimir is the projector, and the split is the difference of two eigenvalues of one operator.

**The cross term.** Writing the total Casimir as $\tfrac32\mathrm{id}-2\sum_kH_kH'_k$ and comparing with $2P_1$ gives
$$
\sum_kH_kH'_k=\tfrac34\mathrm{id}-P_1,
$$
with values $\tfrac34$ on the traceless part and $-\tfrac14$ on the scalar line. The difference of the two values is the split, and the average is the single-slot value $\tfrac34$.

## The Single Slot

**The value.** For one side alone, $\sum_kH_k^2=\tfrac34\mathrm I_4$ (the previous article in this category), and $\tfrac34=\tfrac12\cdot\tfrac32=s(s+1)$ at $s=\tfrac12$.

**The two numbers.** $\tfrac34$ on a factor, $2$ on the summand of top label; the difference is the difference between a factor and a summand, and the algebra has both.

## What the Split Contains and What It Does Not

**The integer labels.** The summands are $0$ and $1$, both integers. No half-integer occurs, and the full turn is the identity: $\exp(2\pi i\,H_{\mathrm{tot},z})$ acts as $e^{\pm2\pi i}=1$ on the weight $\pm1$ directions and as $1$ on the weight $0$ directions. Verified numerically to $7.5\cdot10^{-15}$.

**The half turn.** $\exp(\pi i\,H_{\mathrm{tot},z})$ acts as $-1$ on the two weight-$\pm1$ directions and $+1$ on the two weight-$0$ directions; verified, with array $\operatorname{diag}(1,-1,-1,1)$. It is not the identity. This is the difference between the rotation group and its cover, read on the algebra.

**The slot is not a summand.** The spin-$\tfrac12$ carrier is $\mathbb{C}^2$, the defining carrier, and it is not a subspace of $M_2(\mathbb{C})$: it is one of the two factors of $M_2(\mathbb{C})=\mathbb{C}^2\otimes(\mathbb{C}^2)^{*}$. To see it inside the algebra one chooses a rank-one projection $\Pi=uu^{\dagger}$, and then
$$
M_2(\mathbb{C})\,\Pi=\{Y\Pi\}
$$
is a minimal left ideal, of complex dimension two, carrying the defining action of $SU(2)$ by left multiplication. The choice of $u$ is a choice of axis, and different choices give different ideals.

**The dimension bookkeeping.** $1+3=4$ complex dimensions for the two summands; $2+2=4$ for the factor and its dual; and the algebra is four complex dimensional. The half-integer carrier contributes to the second count only, which is why the list of three carriers is not a direct sum.

**The refinement.** The Clebsch–Gordan coefficients appear when the traceless part is resolved into weight vectors, and that resolution needs an axis: with $\sigma_3$ chosen, the weight vectors are $\sigma_1\pm i\sigma_2$ and $\sigma_3$. The series itself is coefficient-free.

## Worked Example

**The three Pauli directions.** $\sigma_1,\sigma_2,\sigma_3$ are traceless, so $P_1\sigma_k=\sigma_k$ and $P_0\sigma_k=0$; $\mathrm I_2$ is scalar, so $P_0\mathrm I_2=\mathrm I_2$ and $P_1\mathrm I_2=0$. The array of $P_1$ is $\operatorname{diag}(0,1,1,1)$ in the coefficient basis.

**A general matrix.** $Y=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ has $\operatorname{tr}Y=5$, so $P_0Y=\tfrac52\mathrm I_2$ and $P_1Y=\begin{pmatrix}-1.5&2\\3&1.5\end{pmatrix}$, with trace zero.

**The Casimir on it.** $2Y-(\operatorname{tr}Y)\mathrm I_2=\begin{pmatrix}-3&4\\6&3\end{pmatrix}$, which is $2P_1Y$; the scalar part is killed.

## Where $n=2$ Differs

**The split.** At $n=2$ the split is $1\oplus3$: the scalar line plus the traceless part. At order $n$ the same two projectors exist, and the split is $1\oplus(n^2-1)$; the traceless part is $n^2-1$ complex dimensional, and it is irreducible only at $n=2$.

**The Casimir.** At $n=2$ the traceless part is irreducible with Casimir $2$. At order $n$ the adjoint carrier is irreducible with Casimir $n$, and the value $2$ is the value at $n=2$.

**The labels.** At $n=2$ the labels are $0$ and $1$ and the chain stops. At order $n$ the labels run from $0$ to $n-1$, and the top label is $n-1$.

**What does not differ.** The two projectors, their algebra, the equivariance and the identity "Casimir equals twice the projector" hold at every order.

## Summary

The involution $\natural$ is the matrix conjugation, and on a $2\times2$ matrix it is $Y\mapsto(\operatorname{tr}Y)\mathrm I_2-Y$; it is complex-linear and involutive. Its averaging operators are $P_0(Y)=\tfrac12\operatorname{tr}(Y)\mathrm I_2$ and $P_1(Y)=Y-\tfrac12\operatorname{tr}(Y)\mathrm I_2$, with images the scalar line and $\mathfrak{sl}_2$, of complex dimensions one and three.

Both are equivariant for $Y\mapsto UYU^{\dagger}$, and neither commutes with one-sided multiplication, so the split belongs to the diagonal action. The diagonal weights are $\{-1,0,+1,0\}$ and the Casimir operator is $\mathbf H^2_{\mathrm{tot}}=2P_1=\mathrm{id}-\natural$, that is $Y\mapsto2Y-(\operatorname{tr}Y)\mathrm I_2$, with values $2$ and $0$: spin one and spin zero. The single-slot Casimir is $\tfrac34$, and the cross term is $\tfrac34\mathrm{id}-P_1$.

No half-integer summand occurs, because the split has only integer labels and the full turn is the identity. The half-integer carrier is the defining factor $\mathbb{C}^2$, realised inside the algebra only as a minimal left ideal $M_2\Pi$ after a rank-one projection is chosen.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\natural$ | the matrix conjugation $Y\mapsto(\operatorname{tr}Y)\mathrm I_2-Y$ |
| $P_0,P_1$ | the projectors onto scalars and traceless matrices |
| $H_k$ | $\tfrac i2(L_k-R_k)$, the diagonal generators |
| $\mathbf H^2_{\mathrm{tot}}$ | the Casimir, $2P_1$ |
| $\Pi$ | a rank-one projection, for the minimal left ideal |

## Further Reading

- [The Clebsch–Gordan Decomposition of the Biquaternion Algebra](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra.html), for the source's canonical construction and its remarks on the coefficients.
- [From the Spin to the Carriers and the Closures in $M_2(\mathbb{C})$](the-carriers-the-representation-the-spin-and-the-closure-in-m2c.html), for the three carriers built on this split.
- [From the Spin Group to the Spin of a Single Rotor in $M_2(\mathbb{C})$](from-the-spin-group-to-the-spin-of-a-single-rotor-in-m2c.html), for the single-slot Casimir $\tfrac34$.
- [Operators Acting on Two Sides in $M_2(\mathbb{C})$](operators-acting-on-two-sides-in-m2c.html), for the diagonal action whose Casimir this is.
- [Introduction to the Spin-Half Bispinors Spaces in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-in-m2c.html), for the minimal left ideals that realise the factor.
