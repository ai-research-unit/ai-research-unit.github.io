# __Introduction to the Spin-Zero Centre Subspace in $M_2(\mathbb{C})$__

## Introduction

**The question.** Which subspace of $M_2(\mathbb{C})$ carries spin zero, why is it fixed by every unitary conjugation, and why is it the only invariant complex line?

**Why it is the same statement.** This is the in-depth matrix reading of [Introduction to the Spin-Zero Centre Subspace](the-spin-zero-centre-subspace.html). The source's carrier is the real line $\mathbb{R}e_t$ with closure the centre $\mathbb{C}e_t$; under $A=\mathsf M_2(\tilde Q)$ these become
$$
\mathbb{R}\mathrm I_2\subset\mathbb{C}\mathrm I_2=\{\,z\mathrm I_2\,\},
$$
the real line of the identity and the complex line of the scalar matrices. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. That the fixed space of $Y\mapsto UYU^{\dagger}$, $U$ unitary, is exactly $\mathbb{C}\mathrm I_2$. That $\mathbb{C}\mathrm I_2$ is the only invariant complex line, by the bracket argument on $\mathfrak{u}(2)$ and $\mathfrak{su}(2)$. The trivial action, the zero generator, the spectrum $\{0\}$ and the label $s=0$. The doubling of the carrier in its closure, and the overlap $i\mathbb{R}\mathrm I_2$ with the skew-Hermitian space. The reason the centre is not a Peirce corner.

**What the article does not do.** It does not treat the norm on the centre, which is [The Spin-Zero Centre Subspace and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-n-norm-regularity-in-m2c.html); it does not treat the spectrum of a central element, which is [The Spin-Zero Centre Subspace and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-spectral-regularity-in-m2c.html).

**Conventions.** $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, so $Q_t=\tfrac12\operatorname{tr}A$ and the centre of the image is $\mathbb{C}\mathrm I_2$. The group is $G=\mathrm U(2)=\{U:U^{\dagger}U=\mathrm I_2\}$. The generator of the axis $n$ is $\tfrac12n\cdot E$ with $E_k=-i\sigma_k$. Inner products are $\langle X,Y\rangle=\tfrac12\operatorname{tr}(X^{\dagger}Y)$.

**Boundaries.** The trifurcation of carriers is [From the Spin to the Carriers and the Closures in $M_2(\mathbb{C})$](from-the-spin-to-the-carriers-and-the-closures-in-m2c.html). The split is [The Clebsch–Gordan Decomposition of the Biquaternion Algebra in $M_2(\mathbb{C})$](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra-in-m2c.html). The sectors are [The Spin-Zero Centre Subspace and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $U$ is unitary, $n$ a unit real vector, $X,Y$ general matrices, $\varrho$ the adjoint action.

## The Subspace and Its Closure

**The carrier.** $\mathbb{R}\mathrm I_2=\{t\mathrm I_2:t\in\mathbb{R}\}$, of real dimension one. It is not built and not chosen: it is the set of real multiples of the identity, and the identity is the one matrix the algebra supplies without a choice.

**The closure.** $\mathbb{C}\mathrm I_2=\mathbb{R}\mathrm I_2\oplus\mathbb{R}(i\mathrm I_2)$, of real dimension two and complex dimension one, the centre.

**The projector.** In the matrix reading the Clebsch–Gordan projector onto the closure is $\tfrac12\operatorname{tr}$,
$$
P_0(Y)=\frac{\operatorname{tr}Y}{2}\,\mathrm I_2,
$$
whose image is exactly $\mathbb{C}\mathrm I_2$. The label is placed on the space by the projector, not read off it afterwards.

## The Fixed Space

**The action.** $\varrho(U)(X)=UXU^{\dagger}$. On a scalar matrix,
$$
U(z\mathrm I_2)U^{\dagger}=z\,UU^{\dagger}=z\mathrm I_2 .
$$
So the centre is fixed pointwise, at every unitary, and the operator of the generator $\tfrac12n\cdot E$ is the commutator with $-\tfrac i2 n\cdot\sigma$, which kills every scalar.

**The converse.** Suppose $UXU^{\dagger}=X$ for every unitary $U$. Then $UX=XU$, so $X$ commutes with a set spanning $M_2(\mathbb{C})$: the four matrices $\mathrm I_2,\sigma_1,\sigma_2,\sigma_3$ are unitary (the last three are Hermitian unitaries), and they span. Hence $X$ is central, and the centre of $M_2(\mathbb{C})$ is $\mathbb{C}\mathrm I_2$.

**The statement in one line.** The fixed space of the adjoint action of $\mathrm U(2)$ is the centre, and the centre is the closure of the carrier, not the carrier itself.

## The Only Invariant Complex Line

**The theorem.** Let $W$ be a complex line with $UWU^{\dagger}\subseteq W$ for every unitary $U$. Then $W=\mathbb{C}\mathrm I_2$.

**The proof.** Let $w\neq0$ span $W$ and write $UwU^{\dagger}=\chi(U)w$. Differentiating along $U=e^{tA}$ with $A\in\mathfrak{u}(2)$ gives
$$
[A,w]=\mu(A)w .
$$
The Jacobi identity gives $\mu([A,B])w=\operatorname{ad}_{[A,B]}w=[\operatorname{ad}_A,\operatorname{ad}_B]w=0$, since the two scalars commute. So $\mu$ vanishes on the derived algebra $[\mathfrak{u}(2),\mathfrak{u}(2)]=\mathfrak{su}(2)$; and $\mu(i\mathrm I_2)=0$ because $\operatorname{ad}_{i\mathrm I_2}=0$. Hence $\mu=0$ on $\mathfrak{u}(2)$, so $w$ commutes with $\mathfrak{su}(2)$, and since $\mathfrak{su}(2)$ together with $\mathrm I_2$ spans $M_2(\mathbb{C})$, the matrix $w$ is central.

**The matrix form of the last step.** $w$ commutes with $\sigma_1,\sigma_2,\sigma_3$; commuting with $\sigma_3=\operatorname{diag}(1,-1)$ forces $w$ to be diagonal, and then commuting with $\sigma_1$ forces the two diagonal entries to be equal. So $w\in\mathbb{C}\mathrm I_2$; verified on random unitary conjugations.

**Why the norm is not used.** The tempting argument multiplies by the determinant: $\chi(U)^2\det w=\det w$ gives $\chi(U)^2=1$ only when $\det w\neq0$. A singular $w$ is exactly the case where the invariance is invisible element by element, and the derivative argument needs neither the determinant nor the invertibility.

## The Action and the Two Numbers

**The generator.** $\varrho\bigl(\tfrac12n\cdot E\bigr)(t\mathrm I_2)=\tfrac12 t[n\cdot E,\mathrm I_2]=0$. So the operator is zero at every axis, and the spectrum is $\{0\}$ with multiplicity one on the line.

**The label.** $s=0$, and $2s+1=1=\dim_\mathbb{R}\mathbb{R}\mathrm I_2$.

**The full turn.** The rotor of a full turn is $-\mathrm I_2$, and $(-\mathrm I_2)X(-\mathrm I_2)^{\dagger}=X$ on the centre. The sign is $(-1)^{2s}=+1$, and the two agree.

## The Centre as a Space of Multiplicity Two

**The doubling.** The real line and the imaginary line $i\mathbb{R}\mathrm I_2$ are each fixed pointwise, and they are the real and imaginary parts of one complex line. The carrier is the real line; the space that carries it is the centre, which holds two copies.

**The module is one-dimensional.** The multiplicity belongs to the space and not to the carrier: the module is a real line and the space is a complex line.

**The overlap with the skew-Hermitian space.** The centre meets $\mathfrak{u}(2)=\{Y:Y^{\dagger}=-Y\}$ in
$$
\mathbb{C}\mathrm I_2\cap\mathfrak{u}(2)=i\mathbb{R}\mathrm I_2,
$$
of real dimension one: the imaginary scalar line. This is the only overlap the centre has with the other closures.

## Why the Centre Is Not a Peirce Corner

**The corners.** For a rank-one projection $P$ the four corners $PM_2P$, $PM_2P_{\perp}$, $P_{\perp}M_2P$, $P_{\perp}M_2P_{\perp}$ each have complex dimension one, hence real dimension two.

**The difference.** A corner is a space of products $\Pi X\Pi'$, and the centre is a space of fixed points. A corner contains elements with non-central products; every element of the centre has a central product. The dimensions agree, and the constructions do not: the algebra has eight real dimensions and the two rules cut it differently.

## Worked Example

**A central element.** $X=z\mathrm I_2$ with $z=2+3i$: invariant under every unitary conjugation, spectrum $\{z,z\}$ as a matrix, and the adjoint action on it is trivial.

**A non-central element with a scalar part.** $X=\begin{pmatrix}1&2\\0&1\end{pmatrix}$ has $\operatorname{tr}X=2$, so $P_0X=\mathrm I_2$ and $P_1X=\begin{pmatrix}0&2\\0&0\end{pmatrix}$: the scalar part is central and the traceless part is not.

**An invariant line that is not the centre.** The line $\mathbb{C}P$ of a rank-one projection is invariant under the circle of rotations about its axis and under no larger group, which is why it is not an invariant line in the sense of the theorem.

## Where $n=2$ Differs

**The centre.** At $n=2$ the centre is one complex line, of real dimension two, and the carrier is one real line. At order $n$ the centre is still one complex line, so nothing changes in the centre itself.

**The uniqueness.** At $n=2$ the derived algebra is all of $\mathfrak{sl}_2$ and the argument closes in one step. At order $n$ the same argument works, with $\mathfrak{su}(n)$ spanning the traceless part, so the uniqueness of the invariant line holds at every order.

**What does differ.** At $n=2$ the centre meets the skew-Hermitian space in a line and the complement is three-dimensional; at order $n$ the complement is $n^2-1$ dimensional. The arithmetic of the doubling is the same.

## Summary

The carrier of spin zero is $\mathbb{R}\mathrm I_2$, of real dimension one, and its closure is the centre $\mathbb{C}\mathrm I_2$, of real dimension two. The projector onto the closure is $Y\mapsto\tfrac12\operatorname{tr}(Y)\mathrm I_2$.

The fixed space of $X\mapsto UXU^{\dagger}$ is exactly the centre, and the centre is the only invariant complex line: differentiating the character gives $[A,w]=\mu(A)w$, the Jacobi identity kills $\mu$ on $\mathfrak{su}(2)$, and $\operatorname{ad}_{i\mathrm I_2}=0$ kills the last direction. The action on the carrier is trivial, the generator is zero, the spectrum is $\{0\}$, $s=0$, $2s+1=1$, and the full turn is $+1$.

The centre holds two copies of the real line, it meets the skew-Hermitian space in $i\mathbb{R}\mathrm I_2$, and it is a space of fixed points rather than a Peirce corner.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{R}\mathrm I_2$ | the carrier, spin zero |
| $\mathbb{C}\mathrm I_2$ | the centre, the closure |
| $i\mathbb{R}\mathrm I_2$ | the overlap with the skew-Hermitian space |
| $P_0(Y)=\tfrac12\operatorname{tr}(Y)\mathrm I_2$ | the projector onto the centre |
| $\varrho$ | the adjoint action |
| $n$ | the unit axis of the generator |

## Further Reading

- [Introduction to the Spin-Zero Centre Subspace](the-spin-zero-centre-subspace.html), for the source's proof that no other invariant line exists.
- [The Spin-Zero Centre Subspace and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-n-norm-regularity-in-m2c.html), for the determinant on the centre.
- [The Spin-Zero Centre Subspace and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-spectral-regularity-in-m2c.html), for the double eigenvalue of a central element.
- [From the Spin to the Carriers and the Closures in $M_2(\mathbb{C})$](from-the-spin-to-the-carriers-and-the-closures-in-m2c.html), for the three carriers and the four closures.
- [The Clebsch–Gordan Decomposition of the Biquaternion Algebra in $M_2(\mathbb{C})$](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra-in-m2c.html), for the projector $P_0$ and the label zero.
