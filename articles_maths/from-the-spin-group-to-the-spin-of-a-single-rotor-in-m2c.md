# __From the Spin Group to the Spin of a Single Rotor in $M_2(\mathbb{C})$__

## Introduction

**The question.** Why must an element of the spin group act on the algebra by a two-sided product, what are the generators of that action in matrices, and how does the quadratic Casimir of those generators return the number $\tfrac12$?

**Why it is the same statement.** This is the in-depth matrix reading of [From the Spin Group to the Spin of a Single Rotor](from-the-spin-group-to-the-spin-of-a-single-rotor.html). The source's operators $A_k=\rho_L(\vec e_k)$, its Casimir $\sum_kA_k^2=-3\,\mathrm{id}$ and its split $S\otimes S=\wedge^2S\oplus\mathrm{Sym}^2S$ become, under $A=\mathsf M_2(\tilde q)$, the coefficient-frame matrices $L_k$ and a $4\times4$ Casimir computation. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. That conjugation $Y\mapsto AYA^{\dagger}$ is the only multiplicative two-sided form, and that the two candidates $\Theta_{\natural}$ and $\Theta_{*}$ differ off the rotor sphere. That the coefficient-frame generators $L_k$ are real antisymmetric with no real eigenvalue. That the Casimir $\sum_kL_k^2=-3\mathrm I_4$ and the Hermitian normalization $H_k=\tfrac i2L_k$ give $\sum_kH_k^2=\tfrac34\mathrm I_4$ and weights $\pm\tfrac12$. That the tensor square splits as $1\oplus3$ with Casimir $0$ and $2$.

**What the article does not do.** It does not develop the group displays, which are [The Spin Group via $4\times4$ Real Matrices](the-spin-group-unit-elements-rotors-and-the-two-to-one-cover.html) and its matrix reading; it does not treat the carriers, which are [From the Spin to the Carriers and the Closures in $M_2(\mathbb{C})$](the-carriers-the-representation-the-spin-and-the-closure-in-m2c.html).

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$; the coefficient basis is $(E_t,E_x,E_y,E_z)=(\mathrm I_2,-i\sigma_1,-i\sigma_2,-i\sigma_3)$; $L_k$ is the coefficient-frame array of $Y\mapsto E_kY$. Inner products of matrices are $\langle X,Y\rangle=\tfrac12\operatorname{tr}(X^{\dagger}Y)$.

**Boundaries.** The tensor square and its two summands are [The Clebsch–Gordan Decomposition of the Biquaternion Algebra in $M_2(\mathbb{C})$](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra-in-m2c.html). The two-sided operator that this action is a case of is [The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $A$ is the matrix of a rotor, $L_k$ the coefficient-frame generators, $H_k=\tfrac i2L_k$, $\mathbf H^2$ the Casimir, $s$ the spin, $S$ the two-dimensional spinor carrier.

## Why the Two-Sided Action Is Forced

**One side is not enough.** Let $\Lambda(Y)=AY$. Then $\Lambda(YZ)=\Lambda(Y)\Lambda(Z)$ for all $Y,Z$ holds only for $A=\mathrm I_2$: the left side has one factor $A$ and the right side has two.

**Two sides are multiplicative.** For invertible $A$, $\Theta_A(Y)=AYA^{-1}$ satisfies $\Theta_A(Y)\Theta_A(Z)=AYA^{-1}AZA^{-1}=AYZA^{-1}=\Theta_A(YZ)$, and $\Theta_A\Theta_B=\Theta_{AB}$, so $\Theta$ is a homomorphism with kernel the centre.

**The two marks.** The algebra carries the quaternion conjugation $\natural$ and the Hermitian adjoint $*$; for a real quaternion they coincide. In matrices,
$$
A^{\natural}=\overline{A},\qquad A^{*}=A^{\dagger}.
$$
So the two two-sided operators are
$$
\Theta_{\natural}(A):Y\mapsto AYA^{\natural},\qquad \Theta_{*}(A):Y\mapsto AYA^{\dagger}.
$$

**The scale.** Since $AA^{\natural}=\det A\cdot\mathrm I_2=N\mathrm I_2$, one gets $A^{\natural}=N A^{-1}$ and
$$
AYA^{\natural}=N\,AYA^{-1}.
$$
So $\Theta_{\natural}$ is an automorphism exactly when $\det A=1$, and $\Theta_{*}$ exactly when $A^{\dagger}=A^{-1}$. On a rotor, $A\in SU(2)$, both conditions hold at once and the two operators coincide:
$$
\Theta_{\natural}(A)=\Theta_{*}(A)=\left[Y\mapsto AYA^{-1}\right].
$$
That is the inner automorphism of the dictionary row "rotor action $\leftrightarrow$ $A\mapsto UAU^{\dagger}$".

**The involution property.** $\Theta_{*}$ always preserves the adjoint:
$$
\left(AYA^{\dagger}\right)^{\dagger}=AYA^{\dagger},
$$
so Hermitian $Y$ stays Hermitian and skew $Y$ stays skew. $\Theta_{\natural}$ does not, unless $A$ is real.

## The Generators

**The arrays.** The three coefficient-frame generators are
$$
L_x=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},\quad
L_y=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix},\quad
L_z=\begin{pmatrix}0&0&0&-1\\0&0&-1&0\\0&1&0&0\\1&0&0&0\end{pmatrix},
$$
with rows and columns $(t,x,y,z)$. They are real, antisymmetric and integer, and $L_k^2=-\mathrm I_4$; verified exactly.

**Skew-adjointness.** For the inner product $\langle X,Y\rangle=\tfrac12\operatorname{tr}(X^{\dagger}Y)$ the coefficient basis is orthonormal, so $L_k^{\mathsf T}=-L_k$ says $L_k^{*}=-L_k$: each generator is skew-adjoint, the matrix form of the source's anti-Hermitian $A_k$.

**No real eigenvalue.** $\operatorname{spec}L_k=\{\pm i\}$, each twice; verified on $L_z$. So no generator fixes a real line: no basis can give a real skew-adjoint square root of $-\mathrm I_4$ a real eigenvector.

**The bracket.** $[L_x,L_y]=2L_z$ and cyclically, verified exactly. Halving gives $J_k=\tfrac12L_k$ with $[J_i,J_j]=\varepsilon_{ijk}J_k$.

## The Casimir

**Step one.** $\sum_kL_k^2=-3\,\mathrm I_4$; verified exactly, because each square is $-\mathrm I_4$. Hence
$$
\mathbf J^2=\tfrac14\sum_kL_k^2=-\tfrac34\,\mathrm I_4 .
$$

**Step two.** With $H_k=\tfrac i2L_k$ the generators are Hermitian, $H_k^{\dagger}=H_k$, verified exactly, and
$$
[H_i,H_j]=i\varepsilon_{ijk}H_k,\qquad \mathbf H^2=\sum_kH_k^2=\tfrac34\,\mathrm I_4,
$$
verified exactly.

**Step three.** On an irreducible carrier $\mathbf H^2=s(s+1)\mathrm I$, so $s(s+1)=\tfrac34$ and $s=\tfrac12$, the other root being $-\tfrac32$.

**Step four, the weights.** The eigenvalues of $H_z=\tfrac i2L_z$ are $+\tfrac12$ twice and $-\tfrac12$ twice; verified. The weight set is $\{\pm\tfrac12\}$ and the complex dimension is $2s+1=2$. The carrier is four real dimensions because the left regular action is quaternionic: multiplication by the central $i$ commutes with it and is not a real scalar.

**The axis is not chosen.** The generator of any axis $\vec u$ is $L(\vec u)=u\cdot L$, conjugate to $L_z$ inside $\mathfrak{g}_L$, and conjugation preserves the spectrum. The number $\tfrac12$ is a property of the carrier.

## The Tensor Square and the Split

**The total generator.** On $S\otimes S$ with $S=\mathbb{C}^2$,
$$
H_{\mathrm{tot},k}=H_k\otimes\mathrm I_2+\mathrm I_2\otimes H_k .
$$

**The swap.** $\sigma(x\otimes y)=y\otimes x$ has eigenvalues $+1$ (three times) and $-1$ (once), and the action commutes with it, so the square splits:
$$
S\otimes S=\mathrm{Sym}^2S\oplus\wedge^2S,\qquad 4=3+1 .
$$

**The Casimir on each summand.** Since $H_k=\tfrac12\sigma_k$,
$$
\sum_kH_k\otimes H_k=+\tfrac34\ \text{on}\ \mathrm{Sym}^2S,\qquad -\tfrac34\ \text{on}\ \wedge^2S,
$$
and the total Casimir is
$$
\mathbf H^2_{\mathrm{tot}}=2\mathbf H^2\otimes\mathrm I_2+2\sum_kH_k\otimes H_k=2\ \text{on}\ \mathrm{Sym}^2S,\qquad 0\ \text{on}\ \wedge^2S .
$$
Verified: the eigenvalues of the total Casimir on $\mathbb{C}^4$ are $2,2,2,0$.

**The spins.** $0=0\cdot1$ and $2=1\cdot2$, so the antisymmetric part has spin $0$ and the symmetric part spin $1$, that is $\tfrac12\otimes\tfrac12=0\oplus1$.

**The weights.** The composite weights are the sums, $\{1,0,0,-1\}$: $\{0\}$ for the singlet and $\{\pm1,0\}$ for the triplet. The dimensions add, $1+3=4$.

**The full turn.** The rotor of a full turn is $-\mathrm I_2$. On $S$ it acts as $-1$; on $S\otimes S$ as $(-1)\otimes(-1)=+1$. The sign a single rotor carries cancels in pairs, and the composite is an action of the rotation group and not of its cover.

## The Two Carriers in Matrices

**The singlet.** $1=\mathbb{C}\cdot$ the antisymmetric form $\epsilon=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, up to scale; the group acts on it trivially, and the Casimir is zero.

**The triplet.** $3=\mathrm{Sym}^2\mathbb{C}^2$, spanned by $e_1e_1$, $e_1e_2+e_2e_1$, $e_2e_2$; its weights are $1,0,-1$ and its Casimir is $2$.

**The identification with the algebra.** The line $\mathbb{C}\mathrm I_2$ and the traceless part $\mathfrak{sl}_2$ are the two integer carriers; $\mathrm{Sym}^2\mathbb{C}^2\cong\mathfrak{sl}_2$ and $\wedge^2\mathbb{C}^2\cong\mathbb{C}$ as modules. At $n=2$ the identification is exact and needs no correction.

## Where $n=2$ Differs

**The dimension.** At $n=2$ the left regular carrier is four real dimensional and the spinor carrier two complex dimensional, and the tensor square has dimension four with the split $1+3$. At order $n$ the carrier is $n^2$ complex dimensional and the tensor square is $n^4$ dimensional, with a longer Clebsch–Gordan series.

**The Casimir.** At $n=2$ the Casimir is a single number, $-\tfrac34$ or $+\tfrac34$, because the carrier is irreducible. At order $n$ the adjoint carrier has a Casimir proportional to the identity with the constant $n$, and the traceless part has dimension $n^2-1$.

**What does not differ.** The forcing of the two-sided form, the collapse $\exp(\theta U)=\cos\theta\,\mathrm I+\sin\theta\,U$ on a unit generator, and the parity argument for the full turn are the same at every order.

## Summary

The two-sided form is forced: $Y\mapsto AYA^{-1}$ is the only multiplicative action of an invertible matrix, and on a rotor $A\in SU(2)$ the two candidates $AYA^{\natural}$ and $AYA^{\dagger}$ coincide, since $A^{\natural}=A^{-1}=A^{\dagger}$.

The coefficient-frame generators $L_x,L_y,L_z$ are real antisymmetric signed permutations with $L_k^2=-\mathrm I_4$ and $[L_x,L_y]=2L_z$, and $\sum_kL_k^2=-3\,\mathrm I_4$. Halving and multiplying by $i$ gives Hermitian generators $H_k$ with $\mathbf H^2=\tfrac34\,\mathrm I_4$ and weights $\pm\tfrac12$, each twice; hence $s=\tfrac12$.

The tensor square splits as $\mathrm{Sym}^2\mathbb{C}^2\oplus\wedge^2\mathbb{C}^2$, of dimensions $3$ and $1$, with total Casimir $2$ and $0$: the spins $1$ and $0$, that is $\tfrac12\otimes\tfrac12=0\oplus1$. The full turn acts as $+1$ on the square, which is why an integer-spin object is a representation of the rotation group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | the matrix of a rotor, $A\in SU(2)$ |
| $\Theta_{\natural},\Theta_{*}$ | $Y\mapsto AYA^{\natural}$ and $Y\mapsto AYA^{\dagger}$ |
| $L_k$ | coefficient-frame generator of left multiplication |
| $H_k=\tfrac i2L_k$ | Hermitian generator |
| $\mathbf H^2$ | the Casimir, $\tfrac34\mathrm I_4$ on the carrier |
| $S$ | the spinor carrier $\mathbb{C}^2$ |
| $s$ | the spin, $\tfrac12$ |

## Further Reading

- [From the Spin Group to the Spin of a Single Rotor](from-the-spin-group-to-the-spin-of-a-single-rotor.html), for the source's basis-free proof of the forcing and the Casimir.
- [The Clebsch–Gordan Decomposition of the Biquaternion Algebra in $M_2(\mathbb{C})$](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra-in-m2c.html), for the split of the algebra that the tensor square reproduces.
- [The Spin Group via $4\times4$ Real Matrices](the-spin-group-via-4x4-real-matrices-in-m2c.html), for the group whose generators these are.
- [The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-m2c.html), for the two-sided operators as a family.
- [From the Spin to the Carriers and the Closures in $M_2(\mathbb{C})$](the-carriers-the-representation-the-spin-and-the-closure-in-m2c.html), for the two integer carriers in full.
