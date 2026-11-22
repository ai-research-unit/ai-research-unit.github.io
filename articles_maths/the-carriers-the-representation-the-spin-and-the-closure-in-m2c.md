# __From the Spin to the Carriers and the Closures in $M_2(\mathbb{C})$__

## Introduction

**The question.** The algebra $M_2(\mathbb{C})$ is four complex dimensional. Which subspaces of it carry which spins, under which action, and how does each carrier close into a subspace of the algebra?

**Why it is the same statement.** This is the in-depth matrix reading of [From the Spin to the Carriers and the Closures](the-carriers-the-representation-the-spin-and-the-closure.html). The source's three carriers are the fixed line $\mathbb{R}e_t$, the spinor plane $\Sigma=\mathbb{C}\tilde\Pi_+$ and the vector part $\mathfrak{k}$; under $A=\mathsf M_2(\tilde Q)$ they become
$$
\mathbb{R}\mathrm I_2,\qquad \mathbb{C}P\ (P\ \text{a rank-one projection}),\qquad \mathfrak{su}(2)=\operatorname{span}_\mathbb{R}\{-i\sigma_k\},
$$
with closures $\mathbb{C}\mathrm I_2$, the minimal left ideal $M_2(\mathbb{C})P$, and the traceless part. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The three actions in matrices, and the spins they see. The slot and its Casimir $\tfrac34$. The two integer summands and their Casimir values $0$ and $2$. The three carriers with their weights and dimensions, and the table. The reason the three are not a direct sum. Completeness at $n=2$. The quadratic element $C=\tfrac34\mathrm I_2$ and its three values. The four closures.

**What the article does not do.** It does not prove the addition rule; it does not treat the minimal left ideals as spinor spaces, which is [Introduction to the Spin-Half Bispinors Spaces in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-in-m2c.html); and it does not treat the regularity of the elements, which is [The Spin-Zero Centre Subspace and the Sectors of N and Spectral Regularity in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-and-the-sectors-of-n-and-spectral-regularity-in-m2c.html).

**Conventions.** $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$; the coefficient basis is $(\mathrm I_2,E_x,E_y,E_z)=(\mathrm I_2,-i\sigma_1,-i\sigma_2,-i\sigma_3)$; the real vector part is $\mathfrak{su}(2)=\operatorname{span}_\mathbb{R}\{E_x,E_y,E_z\}$. A rank-one projection is written $P=uu^{\dagger}$. The generator of the axis $n$ is $\tfrac12 n\cdot E=-\tfrac i2 n\cdot\sigma$. The inner product on matrices is $\langle X,Y\rangle=\tfrac12\operatorname{tr}(X^{\dagger}Y)$.

**Boundaries.** The split is [The Clebsch–Gordan Decomposition of the Biquaternion Algebra in $M_2(\mathbb{C})$](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra-in-m2c.html). The single-slot Casimir is [From the Spin Group to the Spin of a Single Rotor in $M_2(\mathbb{C})$](from-the-spin-group-to-the-spin-of-a-single-rotor-in-m2c.html). The zero-spin sector is [Introduction to the Spin-Zero Centre Subspace in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $P$ is a rank-one projection at the axis $n$, $A$ a rotor matrix, $\varrho$ an action, $\lambda$ a weight, $s$ a spin, $C$ the quadratic element.

## Preliminaries: Three Actions

**The trivial action.** On the real line $\mathbb{R}\mathrm I_2$ the operator is the identity for every rotor, and the generator acts as $0$.

**The adjoint action.** $Y\mapsto AYA^{\dagger}$ preserves the traceless part and the Hermitian and skew sectors, and it fixes $\mathbb{C}\mathrm I_2$.

**The one-sided action.** $Y\mapsto AY$ is defined for every matrix, is multiplicative, and is not an algebra map of the target: it carries the algebra into itself but not onto a subalgebra. It is the action that produces the half-integer.

**The weights.** A weight is a real $\lambda$ such that $i\lambda$ is an eigenvalue of the generator $\tfrac12n\cdot E=-\tfrac i2n\cdot\sigma$ on the carrier, counted with multiplicity.

## The Slot and the Label $\tfrac12$

**The Casimir.** With $L_k$ the coefficient-frame array of $Y\mapsto E_kY$, one has $\sum_kL_k^2=-3\mathrm I_4$ and $\sum_k(\tfrac i2L_k)^2=\tfrac34\mathrm I_4$; verified exactly.

**The label.** $s(s+1)=\tfrac34$ gives $s=\tfrac12$, the other root being $-\tfrac32$.

**The operator on a line of the algebra.** Let $P=\tfrac12(\mathrm I_2+n\cdot\sigma)$ be the rank-one projection at the unit real $n$, and let $A=\cos\tfrac\theta2\,\mathrm I_2+\sin\tfrac\theta2\,(n\cdot E)=\cos\tfrac\theta2\,\mathrm I_2-i\sin\tfrac\theta2\,(n\cdot\sigma)$ be the rotor. Since $E_kP=-iP$ on the axis,
$$
AP=\left(\cos\tfrac\theta2-i\sin\tfrac\theta2\right)P=e^{-i\theta/2}P,
$$
verified exactly. Left multiplication by a rotor is a phase on the line $\mathbb{C}P$, and the phase is the half angle.

**The generator on the line.** $E_kP=-iP$ says that the generator acts as the scalar $-\tfrac i2$, hence the weights $\pm\tfrac12$ and $2s+1=2$.

**The type, not the copy.** The plane is one complex line; the left regular carrier of four real dimensions holds two copies of it, which is why the coefficient-frame spectrum of $L_z$ is $\pm i$ each twice.

## The Two Integer Summands

**The scalar summand.** On $\mathbb{C}\mathrm I_2$ the adjoint action is trivial: $A\mathrm I_2A^{\dagger}=\mathrm I_2$. The generator acts as $0$, the weight set is $\{0\}$ and $s=0$.

**The traceless summand.** On $\mathfrak{sl}_2$ the generator acts as the commutator,
$$
Y\mapsto\left[\tfrac12n\cdot E,\,Y\right]=-\tfrac i2\left[n\cdot\sigma,Y\right],
$$
and for $Y=y\cdot\sigma$ one has $[n\cdot\sigma,Y]=2i(n\times y)\cdot\sigma$, so
$$
\left[\tfrac12n\cdot E,\,y\cdot\sigma\right]=(n\times y)\cdot\sigma .
$$
The operator is the cross product on the coefficients, real and antisymmetric, with eigenvalues $0,\pm i$; verified on a generic axis, where the $3\times3$ array is $|\!|n|\!|$ times the cross-product matrix and its eigenvalues are $0,\pm i$. Hence the weights are $0,\pm1$, the dimension is three and $s=1$.

**The two values.** The quadratic Casimir of the diagonal action is $2$ on the traceless part and $0$ on the scalars, as the previous article in this category states and the next section re-derives from one element.

## The Three Carriers

### The Fixed Line

**The subspace.** $\mathbb{R}\mathrm I_2$, of real dimension one.

**The action.** The adjoint action, which fixes it pointwise.

**The spectrum.** $\{0\}$, and $s=0$, $2s+1=1$, full turn $+1$.

### The Spinor Plane

**The subspace.** Fix a unit real $n$ and $P=\tfrac12(\mathrm I_2+n\cdot\sigma)$, a rank-one projection. The plane is
$$
\Sigma(n)=\mathbb{C}P=\mathbb{R}\{P,iP\},
$$
of real dimension two, spanned by $P$ and $iP$; verified: $P^2=P$, $\operatorname{rank}P=1$.

**The action.** Left multiplication. The rotor multiplies the plane by $e^{-i\theta/2}$; the generator acts as $-\tfrac i2$.

**The spectrum.** $\{\pm\tfrac12\}$; $s=\tfrac12$, $2s+1=2$, full turn $-1$, since $-\mathrm I_2$ times $P$ is $-P$; verified exactly.

**The axis is a parameter.** A different unit $n'$ gives a different plane, and the planes are rotated into one another by the adjoint action. The carrier is a family, not a subspace of the algebra: the choice of $n$ is exactly the choice that a basis would make silently.

### The Vector Part

**The subspace.** $\mathfrak{su}(2)=\operatorname{span}_\mathbb{R}\{E_x,E_y,E_z\}$, of real dimension three, the traceless skew-Hermitian matrices.

**The action.** The adjoint action, $Y\mapsto AYA^{\dagger}$, which preserves the trace and the skew property.

**The operator.** The commutator with $\tfrac12n\cdot E$, that is $(n\times\cdot)$ on the coefficients, with eigenvalues $0,\pm i$ on the three real directions after complexification.

**The spectrum.** $\{\pm1,0\}$; $s=1$, $2s+1=3$, full turn $+1$.

### The Spin Table

| carrier | $\dim_\mathbb{R}$ | action | generator | weights | $s$ | $2s+1$ | full turn |
|---|---|---|---|---|---|---|---|
| $\mathbb{R}\mathrm I_2$ | $1$ | trivial | $0$ | $\{0\}$ | $0$ | $1$ | $+1$ |
| $\mathbb{C}P$ | $2$ | left mult. | $-\tfrac i2$ | $\{\pm\tfrac12\}$ | $\tfrac12$ | $2$ | $-1$ |
| $\mathfrak{su}(2)$ | $3$ | adjoint | $n\times$ | $\{\pm1,0\}$ | $1$ | $3$ | $+1$ |

**The generators as arrays.**
$$
E_1=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\qquad
E_2=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
E_3=\begin{pmatrix}-i&0\\0&i\end{pmatrix},
$$
with $E_kE_l=-\delta_{kl}\mathrm I_2+\epsilon_{klm}E_m$ and $[E_k,E_l]=2\epsilon_{klm}E_m$, verified. The first two rows of the table act on the span of $\mathrm I_2$ and each $E_k$ singly; the third acts on the span of the three $E_k$, and that is the reason its generator is the commutator.

**The factor of two between the last two rows.** The commutator consumes the axis twice and the multiplication consumes it once. On the plane the generator is one multiplication by half the axis; on the vector part it is the difference of two multiplications, which is the cross product with the whole axis.

## Summands and Factor

**The arithmetic.** $1+3=4$ for the two summands, which is the complex dimension of the algebra; $1+2+3=6$ real dimensions for the three carriers, against the real dimension $8$. The half-integer contributes to neither sum, because it is a factor and not a summand.

**The canonical and the chosen.** $\mathbb{C}\mathrm I_2$ and $\mathfrak{sl}_2$ are canonical: their projectors are $\tfrac12\operatorname{tr}$ and $\mathrm{id}-\tfrac12\operatorname{tr}$, and neither mentions an axis. The plane $\mathbb{C}P$ mentions $n$, and every $n$ gives another plane.

**Two other splits, neither of them this one.** $M_2(\mathbb{C})=\mathfrak{u}(2)\oplus i\mathfrak{u}(2)$, the skew and the Hermitian halves, of real dimensions $4+4$; and $M_2(\mathbb{C})=M_2P\oplus M_2P_{\perp}$ as left modules, of complex dimensions $2+2$. The plane is a line inside the first summand of the second split, and it is not a module over the whole algebra.

## Three and No More

**The statement.** At $n=2$ the three carriers above are the only irreducible real subspaces of the algebra, under the three actions, that are invariant and of dimension $2s+1$.

**The reason.** An invariant subspace of the adjoint action is a sum of isotypic pieces, and $\mathfrak{gl}_2=\mathbb{C}\mathrm I_2\oplus\mathfrak{sl}_2$ is a sum of two irreducibles, of dimensions one and three. An invariant subspace of left multiplication is a left ideal, and every non-zero left ideal contains a minimal one, $M_2P$, of complex dimension two; the line $\mathbb{C}P$ inside it is the smallest invariant piece under the circle of rotations about $n$.

**The check.** The dimensions $1,3$ for the adjoint action and $2$ for the one-sided action exhaust the irreducible sizes, and the corresponding Casimir values $0,2,\tfrac34$ are distinct.

## The Quadratic Element

**The element.** With $S_k=\tfrac12 iE_k=\tfrac12\sigma_k$,
$$
C=S_x^2+S_y^2+S_z^2=\tfrac14\left(\sigma_1^2+\sigma_2^2+\sigma_3^2\right)=\tfrac34\mathrm I_2,
$$
verified exactly.

**The three values.** Acting in the module of each carrier,
$$
C\big|_{\mathbb{C}\mathrm I_2}=0,\qquad C\big|_{M_2P}=\tfrac34,\qquad C\big|_{\mathfrak{sl}_2}=2 .
$$
The middle value is left multiplication by the central $\tfrac34\mathrm I_2$ on the ideal; the last is the composed operator $\sum_k\operatorname{ad}^2_{\sigma_k/2}$, whose array is $\operatorname{diag}(0,2,2,2)$ in the coefficient basis, verified exactly.

**The distinction.** The central element $C$ itself acts as $0$ under the adjoint action, because the adjoint of a central element is zero. The value $2$ belongs to the composed operator and not to the element. The two agree on the ideal, where the module is the defining one.

**The three values as spins.** $0=0\cdot1$, $\tfrac34=\tfrac12\cdot\tfrac32$, $2=1\cdot2$: the values are $s(s+1)$ at the three spins.

## The Closures

**The rule.** A closure attaches to a carrier a subspace of the algebra that contains it, on which the action is defined. The property required is different in each case, and it is the property that makes the closure minimal.

### The Centre

**The carrier.** The line $\mathbb{R}\mathrm I_2$, spin $0$. The property is being a complex subspace, and the algebra has an $i$ to spend. The closure is $\mathbb{C}\mathrm I_2$, of real dimension two: the scalar matrices $z\mathrm I_2$, which are exactly the matrices fixed by the adjoint action.

### The Spinor Space, and Then the Bispinor Space

**The first step.** The plane $\mathbb{C}P$ is carried by the rotations about $n$ and by no others: a transverse rotation sends $P$ out of $\mathbb{C}P$. The smallest left ideal containing it is
$$
M_2(\mathbb{C})P=\{YP\},\qquad \dim_\mathbb{C}=2,
$$
verified: $YP$ is fixed by right multiplication by $P$ to $2\cdot10^{-16}$, and the set $\{Y:YP=Y\}$ has complex dimension two.

**The second step.** The two minimal ideals $M_2P$ and $M_2P_{\perp}$ together span the algebra; their sum is the bispinor space, of complex dimension four, and the Peirce decomposition
$$
M_2(\mathbb{C})=PM_2P\oplus PM_2P_{\perp}\oplus P_{\perp}M_2P\oplus P_{\perp}M_2P_{\perp}
$$
is the matrix form of the source's Peirce corners.

**The dimensions.** $2+2=4$ complex, and the four corners of the Peirce decomposition have complex dimensions $1,1,1,1$.

### The Anti-Hermitian Space

**The carrier.** $\mathfrak{su}(2)$, spin $1$. The property is being the whole eigenspace of the involution, and the involution is $Y\mapsto-Y^{\dagger}$. The closure is
$$
\mathfrak{u}(2)=\{Y:Y^{\dagger}=-Y\},
$$
of real dimension four, the skew-Hermitian matrices: $\mathfrak{su}(2)$ plus the line $i\mathbb{R}\mathrm I_2$.

**The check.** $\mathfrak{u}(2)$ is closed under the commutator, and its dimension is $3+1=4$.

### The Spaces Together

**The four closures.** $\mathbb{C}\mathrm I_2$ of real dimension two; $M_2P$ of real dimension four; the bispinor space of real dimension eight; $\mathfrak{u}(2)$ of real dimension four. They overlap, and their dimensions sum to more than eight, which is why the closures are not a decomposition.

## Where $n=2$ Differs

**The carriers.** At $n=2$ there are three carriers and the largest spin is one. At order $n$ the algebra $M_n(\mathbb{C})$ carries the adjoint carrier of dimension $n^2-1$ and spin $n-1$, and its square has a longer chain of labels.

**The planes.** At $n=2$ the spinor plane is a complex line, real dimension two, and it closes to a minimal left ideal of complex dimension two. At order $n$ the minimal left ideal has complex dimension $n$, and the plane is a line inside it.

**The quadratic element.** At $n=2$ the element is $\tfrac34\mathrm I_2$ and the value on the adjoint carrier is $2$. At order $n$ the adjoint value is $n$, and the defining value is $\tfrac{n^2-1}{2n}$, which is $\tfrac34$ at $n=2$.

**What does not differ.** The three actions, the identity $2s+1=\dim_\mathbb{R}$ on each carrier, and the full-turn sign $(-1)^{2s}$ are the same at every order.

## Summary

Three actions act on the algebra: the trivial one on $\mathbb{R}\mathrm I_2$, the adjoint one $Y\mapsto AYA^{\dagger}$, and left multiplication $Y\mapsto AY$. They see three carriers, of real dimensions $1,2,3$ and spins $0,\tfrac12,1$: the fixed line, the plane $\mathbb{C}P$ at a rank-one projection, and $\mathfrak{su}(2)$.

The slot carries $\tfrac12$ because the Casimir of the left-regular generators is $\tfrac34$ and because left multiplication by a rotor is the phase $e^{-i\theta/2}$ on $\mathbb{C}P$. The two integer summands carry $0$ and $2$, from the trivial action and from the cross product on the traceless part with weights $\{\pm1,0\}$. The table is $1,2,3$ against $0,\tfrac12,1$, with full turns $+1,-1,+1$.

The three are not a direct sum: two are canonical summands and the third is a factor, realised only as a line inside a minimal left ideal. The closures are $\mathbb{C}\mathrm I_2$, $M_2P$ and then the bispinor space, and $\mathfrak{u}(2)$. The quadratic element is $C=\tfrac34\mathrm I_2$, with values $0,\tfrac34,2$ on the three modules.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $P=\tfrac12(\mathrm I_2+n\cdot\sigma)$ | rank-one projection at the axis $n$ |
| $\Sigma(n)=\mathbb{C}P$ | the spinor plane |
| $\mathfrak{su}(2)$ | the real span of $E_k=-i\sigma_k$ |
| $\varrho$ | an action: trivial, adjoint, one-sided |
| $\lambda$ | a weight |
| $s$ | the spin, the largest weight |
| $C$ | the quadratic element $\tfrac34\mathrm I_2$ |

## Further Reading

- [From the Spin to the Carriers and the Closures](the-carriers-the-representation-the-spin-and-the-closure.html), for the source's trichotomy, its no-array rule and its four closure rules.
- [The Clebsch–Gordan Decomposition of the Biquaternion Algebra in $M_2(\mathbb{C})$](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra-in-m2c.html), for the two canonical summands that this article reads as carriers.
- [Introduction to the Spin-Half Bispinors Spaces in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-in-m2c.html), for the minimal left ideals in full.
- [The Spin-One Anti-Hermitian Subspace in $M_2(\mathbb{C})$](the-spin-one-anti-hermitian-subspace-in-m2c.html), for the third carrier and its sectors.
- [Introduction to the Spin-Zero Centre Subspace in $M_2(\mathbb{C})$](the-spin-zero-centre-subspace-in-m2c.html), for the first carrier and its regularity.
