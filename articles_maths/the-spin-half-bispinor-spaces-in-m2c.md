# __Introduction to the Spin-Half Bispinors Spaces in $M_2(\mathbb{C})$__

## Introduction

**The question.** Which subspaces of $M_2(\mathbb{C})$ of real dimensions $2$, $4$ and $8$ carry the action with weights $\pm\tfrac12$, and why is the family infinite?

**Why it is the same statement.** This is the in-depth matrix reading of [Introduction to the Spin-Half Bispinors Spaces](the-spin-half-bispinor-spaces.html). The source's plane $\mathbb{C}\tilde\Pi_{\mathrm{id},+}$, its spinor spaces $\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}$ and its bispinor space become
$$
\mathbb{C}P\subset M_2(\mathbb{C})P\subset M_2(\mathbb{C})=M_2P\oplus M_2P_{\perp},
$$
with $P=\tfrac12(\mathrm I_2+n\cdot\sigma)$ a rank-one projection. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The idempotence of $P$ and the plane. The phase $e^{-i\theta/2}$ and the weights $\pm\tfrac12$. That the plane is invariant under the rotations about $n$ alone. The first closure, the minimal left ideal of complex dimension two, and the second, the Peirce splitting. The index of the family, which in the display is the sphere of axes. The dimensions against the Peirce corners.

**What the article does not do.** It does not treat the determinant or the spectrum on these spaces, which are [The Spin-Half Bispinors and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinors-and-n-norm-regularity-in-m2c.html) and [The Spin-Half Bispinors and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinors-and-spectral-regularity-in-m2c.html); it does not treat the spinors themselves, which is [Spinors and Dirac Spinors in the Biquaternion Algebra in $M_2(\mathbb{C})$](spinors-and-dirac-spinors-in-the-biquaternion-algebra-in-m2c.html).

**Conventions.** $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$; $E_k=-i\sigma_k$; the unit real axis $n$ gives the projection $P=\tfrac12(\mathrm I_2+n\cdot\sigma)$; the rotor is $A=\cos\tfrac\theta2\mathrm I_2-i\sin\tfrac\theta2\,(n\cdot\sigma)=\cos\tfrac\theta2\mathrm I_2+\sin\tfrac\theta2\,(n\cdot E)$. Left multiplication is $L_A(Y)=AY$.

**Boundaries.** The carrier's place among the three is [From the Spin to the Carriers and the Closures in $M_2(\mathbb{C})$](from-the-spin-to-the-carriers-and-the-closures-in-m2c.html). The label is [From the Spin Group to the Spin of a Single Rotor in $M_2(\mathbb{C})$](from-the-spin-group-to-the-spin-of-a-single-rotor-in-m2c.html). The sectors are [The Spin-Half Bispinors and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinors-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $P$ a rank-one projection, $n$ its axis, $P_{\perp}=\mathrm I_2-P$, $\Sigma$ the plane, $S_\pm$ the two left ideals.

## The Plane

**The projection.** For a unit real $n$,
$$
P=\frac{\mathrm I_2+n\cdot\sigma}{2},\qquad P^2=P,\qquad \operatorname{rank}P=1,\qquad \operatorname{tr}P=1,
$$
verified exactly. The idempotence is one line: $(n\cdot\sigma)^2=|n|^2\mathrm I_2=\mathrm I_2$.

**The plane.**
$$
\Sigma(n)=\mathbb{C}P=\mathbb{R}\{P,iP\},
$$
of real dimension two and complex dimension one.

**The complementary projection.** $P_{\perp}=\mathrm I_2-P=\tfrac12(\mathrm I_2-n\cdot\sigma)$ satisfies $PP_{\perp}=0$, and the two projections sum to the identity; verified exactly.

**The action.** Left multiplication, $Y\mapsto AY$: one-sided, and this is what separates the plane from the other two carriers.

**The half angle.** Since $n\cdot\sigma\,P=P$ and $E_kP=-iP$ on the axis,
$$
A\,P=\left(\cos\tfrac\theta2-i\sin\tfrac\theta2\right)P=e^{-i\theta/2}P,
$$
verified exactly for a generic angle. The half angle is a consequence of $E_k=-i\sigma_k$, not an insertion.

**The weights.** The generator $\tfrac12n\cdot E$ acts on the plane as $-\tfrac i2$; the two real eigenvalues are the scalar and its conjugate, so the spectrum is $\{\pm\tfrac12\}$ and $2s+1=2$.

**The full turn.** $-\mathrm I_2$ times $P$ is $-P$: the operator is $-\mathrm{id}$, the sign $(-1)^{2s}=-1$, and it is a half turn of the real plane.

## The Plane Is Not Invariant for the Whole Group

**The transverse multiplication.** $\sigma_1P$ is not a multiple of $P$: the projection onto $\mathbb{C}P$ leaves a residual of size $1$ in the matrix norm, verified. So a transverse rotation sends $P$ out of the plane.

**The reading.** The plane is a carrier for the circle of rotations about $n$ alone. This is the one place among the three carriers where carrier and group do not match, and it is why the spin-half case needs two closures.

## The First Closure: The Left Ideals

**The space.**
$$
S_+(n)=M_2(\mathbb{C})P=\{YP\},\qquad \dim_\mathbb{C}S_+=2,\ \dim_\mathbb{R}S_+=4,
$$
verified: the span of $\{P,\sigma_1P,\sigma_2P,\sigma_3P\}$ has complex dimension two.

**Why it is closed.** $A(YP)=(AY)P$, so left multiplication stays inside, for every matrix $A$ and not only for the rotors.

**Why it is minimal.** A left ideal $I\subseteq S_+$ is a subspace carried into itself by every left multiplication; the smallest such spaces are the $M_2P$ for rank-one $P$, which are exactly the minimal left ideals. The dimension two over $\mathbb{C}$ is the smallest that supports the action.

**The second ideal.** $S_-(n)=M_2P_{\perp}$, of the same dimensions, with $S_+\cap S_-=\{0\}$ since $PP_{\perp}=0$ and the sum is direct:
$$
M_2(\mathbb{C})=S_+\oplus S_-,\qquad 2+2=4\ \text{over }\mathbb{C}.
$$

**What the first step adds.** Not the complex structure: the plane is already a complex line and $i$ acts inside it. It adds the transverse direction, which is two real dimensions.

## The Second Closure: The Bispinor Space

**The space.** The sum of the two ideals is the whole algebra:
$$
M_2(\mathbb{C})=M_2P\oplus M_2P_{\perp}.
$$
A bispinor space is the algebra together with a Peirce basis, which is the pair $\{P,P_{\perp}\}$.

**The two steps.** The first goes from real dimension two to four and repairs invariance; the second goes from four to eight and completes the pair. The two are different in kind.

**The Peirce corners.** The four spaces $PM_2P$, $PM_2P_{\perp}$, $P_{\perp}M_2P$, $P_{\perp}M_2P_{\perp}$ each have complex dimension one, hence real dimension two. The two ideals group them two by two: $S_+$ contains the first and the second, $S_-$ the third and the fourth.

**The count.** Four corners of real dimension two, two ideals of real dimension four, one algebra of real dimension eight.

## The Index of the Family

**The sign.** $P(-n)=\mathrm I_2-P(n)=P_{\perp}(n)$, verified exactly. So the unordered pair $\{P,P_{\perp}\}$ depends on $n$ up to sign, and the family of bispinor spaces is indexed by the real projective plane.

**The sphere.** The set of rank-one projections in the display is the sphere: writing $n$ as the unit vector of $\mathbb{R}^3$, the map $n\mapsto P(n)$ is one to one onto $\{P:P^2=P,\ P=P^{\dagger},\ \operatorname{tr}P=1\}$, and $n$ and $-n$ give the complementary pair. So one index set serves both readings, and the display names it as the sphere of axes.

**No canonical member.** Nothing in the algebra singles out an axis, so nothing singles out a plane, an ideal or a bispinor space. A statement about one of them is a statement about all, and the axis is a parameter.

**As sets, one space.** Every bispinor space is $M_2(\mathbb{C})$; what varies is the splitting. The ideals, by contrast, are proper subspaces and genuinely differ from axis to axis.

## What the Family Teaches

**The other carriers do not move.** $\mathbb{C}\mathrm I_2$ and $\mathfrak{su}(2)$ are the same at every axis; only the spin-half closure moves, because only it is built from an idempotent.

**Spaces exceed carriers.** There are three carriers and infinitely many ideals, because a carrier is a module and a module can be realised in many subspaces.

## Worked Example

**The axis $n=e_3$.** $P=\operatorname{diag}(1,0)$, $P_{\perp}=\operatorname{diag}(0,1)$. The ideal $S_+$ is the set of matrices with second column zero:
$$
S_+=\left\{\begin{pmatrix}a&0\\ c&0\end{pmatrix}\right\},\qquad \dim_\mathbb{C}=2 .
$$
The plane is the set of matrices $\begin{pmatrix}\lambda&0\\0&0\end{pmatrix}$.

**The transverse direction.** $\sigma_1P=\begin{pmatrix}0&0\\1&0\end{pmatrix}$ is in $S_+$ and not in the plane: this is the second complex line of the ideal.

**The rotor about $e_3$.** $A=\operatorname{diag}(e^{-i\theta/2},e^{i\theta/2})$, and $AP=e^{-i\theta/2}P$.

## Where $n=2$ Differs

**The dimension of the ideal.** At $n=2$ a minimal left ideal has complex dimension two and real dimension four; the plane inside it has real dimension two. At order $n$ the ideal has complex dimension $n$, and the plane is still a line.

**The index of the family.** At $n=2$ the family of projections is the sphere $S^2$, indexed by the real projective plane of axes. At order $n$ the family is the complex projective space $\mathbb{CP}^{n-1}$, of real dimension $2n-2$, which is bigger than the space of real axes.

**The bispinor space.** At $n=2$ the splitting into two ideals of equal dimension is a splitting into $2+2$. At order $n$ it is $n+n$, and the Peirce corners number $n^2$.

## Summary

The spin-half carrier is the plane $\mathbb{C}P$ at a rank-one projection, of real dimension two, with weights $\pm\tfrac12$ and a full turn acting as $-1$. It is invariant under the rotations about $n$ alone, since a transverse multiplication leaves the line.

The first closure is the minimal left ideal $M_2P$, of complex dimension two, closed under left multiplication by every matrix and minimal with that property. The second closure is the Peirce splitting $M_2=M_2P\oplus M_2P_{\perp}$, of complex dimension four: as a set the bispinor space is the algebra, and what varies with the axis is the splitting.

The family is indexed by the sphere of axes, with $n$ and $-n$ giving the complementary pair; there is no canonical member, and the only carrier whose closure moves with the axis is this one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P=\tfrac12(\mathrm I_2+n\cdot\sigma)$ | rank-one projection at the axis $n$ |
| $P_{\perp}=\mathrm I_2-P$ | the complementary projection |
| $\Sigma=\mathbb{C}P$ | the spin-half plane |
| $S_\pm=M_2P,\,M_2P_{\perp}$ | the two minimal left ideals |
| $\theta$ | the rotation angle, twice the rotor angle |
| $A$ | the rotor matrix |

## Further Reading

- [Introduction to the Spin-Half Bispinors Spaces](the-spin-half-bispinor-spaces.html), for the source's family and its two closures.
- [The Spin-Half Bispinors and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinors-and-n-norm-regularity-in-m2c.html), for the determinant on the ideal.
- [The Spin-Half Bispinors and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinors-and-spectral-regularity-in-m2c.html), for the spectrum of an element of the ideal.
- [Spinors and Dirac Spinors in the Biquaternion Algebra in $M_2(\mathbb{C})$](spinors-and-dirac-spinors-in-the-biquaternion-algebra-in-m2c.html), for the elements of these spaces read as spinors.
- [From the Spin to the Carriers and the Closures in $M_2(\mathbb{C})$](from-the-spin-to-the-carriers-and-the-closures-in-m2c.html), for the three carriers and the four closures.
