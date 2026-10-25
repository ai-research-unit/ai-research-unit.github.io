# __Exponential Polar Decomposition of Biquaternions__

## Introduction

This article treats the **exponential polar decomposition** of an invertible biquaternion: the writing

$$
\tilde Q=r\,\exp(i\alpha)\,\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)\,\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$ the scale, $\alpha$ the phase, $\psi\ge0$ the rapidity, $\theta\in[0,2\pi]$ the rotor angle, and $\vec u_{\mathrm b},\vec u_{\mathrm r}$ real unit axes. The four factors are the **scale**, the **phase**, the **boost** and the **rotor**, in this order. The scale and the phase are central and may be moved; the boost and the rotor do not commute. The decomposition is the exponential form of the modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Biquaternions*, which writes every invertible biquaternion as $\tilde Q=\Rho\tilde U$ with $\Rho=r\exp(i\alpha)$ in the branch $\operatorname{Re}\Rho\ge0$ and $\tilde U$ of norm one.

The exponential and the logarithm are those of *Biquaternion Elementary Functions*: the exponential is the matrix exponential through the algebra isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, and the logarithm is its inverse, multivalued. The modulus–unit theorem and the topology of the unit group are those of *Modulus–Unit Polar Decomposition of Biquaternions*; the Cartan decomposition $SL(2,\mathbb{C})=P\cdot K$ is that of *Biquaternion Lie Group and Exponential Structure*. These facts are quoted, not re-proved. What the article owns is the polar word itself, its existence and uniqueness, the relation between the Cartan logarithm and the single logarithm, the group law, the matrix picture, the exponential coordinates and the boundary behaviour.

The decomposition is noncommutative in an essential way. The boost and the rotor exponents do not commute, so the four exponents do not add: their sum, the **formal exponent**, is not a logarithm of the element. The Baker–Campbell–Hausdorff correction is another boost. The polar word is therefore a canonical product of four exponentials, not one exponential; it is a section of the **word map**, not of the exponential. This is the structural difference from the complex, split-complex and reduced biquaternion cases, where the algebra is commutative and the word is a single exponential.

**The result.** The decomposition reads as follows.

| Item | Value |
|---|---|
| Algebra | $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, basis $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| Domain | the units $\mathbb{B}^{\times}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}\neq0\}$ |
| Decomposition | $\tilde Q=r e^{i\alpha}\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\exp(\frac{\theta}{2}\vec u_{\mathrm r})$ |
| Parameters | $r>0$, $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$, $\psi\ge0$, $\theta\in[0,2\pi]$, two unit axes |
| Modulus | $\Rho=r e^{i\alpha}$ in the branch $\operatorname{Re}\Rho\ge0$ |
| Unit factor | $\tilde U=\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\exp(\frac{\theta}{2}\vec u_{\mathrm r})$ |
| Existence | every unit has a decomposition |
| Uniqueness | the factors are unique; the axes degenerate at $\psi=0$ and $\theta\in\{0,2\pi\}$ |
| Cartan logarithm | the pair $(\tilde H,\tilde K)=(i\frac{\psi}{2}\vec u_{\mathrm b},\frac{\theta}{2}\vec u_{\mathrm r})$ |
| Single logarithm | exists, multivalued; not the sum of the four exponents |
| Group | $\mathbb{B}^{\times}\cong\mathbb{C}^{\times}\times SL(2,\mathbb{C})\cong\mathrm{GL}_2(\mathbb{C})$ |
| Companion | *Relations between Exponential Polar Decomposition and Eigenbasis of a Biquaternion*, for the relation with the eigenbasis |
| Worked examples | *Worked Examples of Exponential Polar Decomposition of Biquaternions*, for the eight cases, the reconstruction and logarithm tables and the null cone |

The plan is as follows. The definition, the exponent and its components, the factors, their component form in the frame of the two axes, and the single exponential are given (§*The Decomposition*); existence and uniqueness are proved (§*Existence and Uniqueness*); the Cartan logarithm, the single logarithm, the kernel and the fibre are described (§*The Logarithm*); the group law is read as the bracket of the two kinds of exponent (§*The Group Law*); the matrix picture is given (§*The Matrix Picture*); the three polar forms are compared (§*The Three Polar Decompositions*); and the parameters are read as coordinates on the group of units (§*The Exponential Coordinates*). The boundary is treated in one block (§*The Boundary of the Word*), and the numerical cases are collected in *Worked Examples of Exponential Polar Decomposition of Biquaternions*.

## The Decomposition

### The Definition

**Definition.** An **exponential polar decomposition** of an invertible biquaternion $\tilde Q$ is a writing

$$
\boxed{\tilde Q=r\,\exp(i\alpha)\,\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)\,\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr)}
$$

with

$$
r>0,\quad
\alpha\in\Bigl(-\frac{\pi}{2},\frac{\pi}{2}\Bigr],\quad
\psi\ge0,\quad
\theta\in[0,2\pi],\quad
\lvert\vec u_{\mathrm b}\rvert=\lvert\vec u_{\mathrm r}\rvert=1.
$$

The four factors are the **scale**, the **phase**, the **boost** and the **rotor**, in this order; their product is the **polar word**. The sum of the four exponents is the **formal exponent**

$$
\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}.
$$

It is not in general a logarithm of $\tilde Q$; the defect is computed in §*The Single Logarithm*. The ranges select one representative: the phase is half-open because the sign it leaves out is the rotor of angle $2\pi$; the rapidity is non-negative because the axis absorbs the sign; the rotor angle is closed because $\theta=0$ and $\theta=2\pi$ are the two signs of the identity.

### The Exponent and Its Components

| Component | Exponent | Range | Factor | Character |
|---|---|---|---|---|
| Scale | $\ln r$ | $\mathbb{R}$ | $r=e^{\ln r}$ | central, non-compact, aperiodic |
| Phase | $i\alpha$ | $(-\frac{\pi}{2},\frac{\pi}{2}]$ | $\zeta=e^{i\alpha}$ | central, compact, period $2\pi$ |
| Boost | $i\frac{\psi}{2}\vec u_{\mathrm b}$ | $\psi\ge0$, $\lvert\vec u_{\mathrm b}\rvert=1$ | $\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ | Hermitian positive, non-compact |
| Rotor | $\frac{\theta}{2}\vec u_{\mathrm r}$ | $\theta\in[0,2\pi]$, $\lvert\vec u_{\mathrm r}\rvert=1$ | $\cos\frac{\theta}{2}+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ | unitary, compact |

The two central blocks lie in the centre $\mathbb{C}e_t$; the boost block lies in $\mathfrak p$ and the rotor block in $\mathfrak k$. The four blocks do not commute in general, and the formal exponent is not a logarithm of $\tilde Q$; that is the subject of §*The Single Logarithm*.

### The Factors

The scale and the phase form the complex modulus

$$
\Rho=r e^{i\alpha},
\qquad
r=\lvert\Rho\rvert,
\qquad
\alpha=\arg\Rho\in\Bigl(-\frac{\pi}{2},\frac{\pi}{2}\Bigr],
$$

the principal argument of the principal square root, in the closed right half-plane.

The boost is

$$
\tilde U_{\mathrm b}=\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)
=\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b},
$$

because $(i\frac{\psi}{2}\vec u_{\mathrm b})^2=\frac{\psi^2}{4}e_t$. It is Hermitian, positive, of norm one, and unbounded as $\psi\to\infty$. The rapidity and the axis are recovered by

$$
\cosh\frac{\psi}{2}=\operatorname{Sc}\tilde U_{\mathrm b},
\qquad
\sinh\frac{\psi}{2}=\bigl\lvert\operatorname{Vect}\tilde U_{\mathrm b}\bigr\rvert,
\qquad
\psi=2\operatorname{arcosh}\bigl(\operatorname{Sc}\tilde U_{\mathrm b}\bigr),
$$

with the axis the normalized vector part divided by $i$.

The rotor is

$$
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr)
=\cos\frac{\theta}{2}\,e_t+\sin\frac{\theta}{2}\,\vec u_{\mathrm r},
$$

because $(\frac{\theta}{2}\vec u_{\mathrm r})^2=-\frac{\theta^2}{4}e_t$. It is a unit real quaternion, unitary, and periodic: the rotation has period $2\pi$ in $\theta$, while the rotor itself is $4\pi$-periodic. The angle and the axis are recovered by

$$
\cos\frac{\theta}{2}=\operatorname{Sc}\tilde u_{\mathrm r},
\qquad
\sin\frac{\theta}{2}=\bigl\lvert\operatorname{Vect}\tilde u_{\mathrm r}\bigr\rvert,
\qquad
\theta=2\arccos\bigl(\operatorname{Sc}\tilde u_{\mathrm r}\bigr).
$$

The four factors group into the modulus and the unit factor.

| Factor | Formula | Range | Exponent | Parameter |
|---|---|---|---|---|
| Modulus | $\Rho=r e^{i\alpha}$ | $\arg\Rho\in(-\frac{\pi}{2},\frac{\pi}{2}]$ | $\ln r+i\alpha$ | $r>0$, $\alpha$ in the branch |
| Unit factor | $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $SL(2,\mathbb{C})$ | $i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}$ | $\psi\ge0$, $\theta\in[0,2\pi]$, unit axes |

### The Unit Factor and the Two Axes

The boost and the rotor are exponentials of pure vector exponents, so their product is read with the quaternion product of the two axes. For real unit vectors,

$$
\vec u_{\mathrm b}\vec u_{\mathrm r}
=-\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}+\vec u_{\mathrm b}\times\vec u_{\mathrm r}.
$$

Write $c_{\mathrm b}=\cosh\frac{\psi}{2}$, $s_{\mathrm b}=\sinh\frac{\psi}{2}$, $c_{\mathrm r}=\cos\frac{\theta}{2}$, $s_{\mathrm r}=\sin\frac{\theta}{2}$. Expanding the product of the two closed forms of §*The Factors* gives

$$
\begin{aligned}
\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}={}&
\Bigl(c_{\mathrm b}c_{\mathrm r}-i s_{\mathrm b}s_{\mathrm r}\,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}\Bigr)e_t
+i s_{\mathrm b}c_{\mathrm r}\,\vec u_{\mathrm b}\\
&+c_{\mathrm b}s_{\mathrm r}\,\vec u_{\mathrm r}
+i s_{\mathrm b}s_{\mathrm r}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r}.
\end{aligned}
$$

Its scalar and vector parts are

$$
\operatorname{Sc}\tilde U=c_{\mathrm b}c_{\mathrm r}-i s_{\mathrm b}s_{\mathrm r}\,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r},
\qquad
\operatorname{Vect}\tilde U=i s_{\mathrm b}c_{\mathrm r}\,\vec u_{\mathrm b}+c_{\mathrm b}s_{\mathrm r}\,\vec u_{\mathrm r}+i s_{\mathrm b}s_{\mathrm r}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r}.
$$

| Term | Direction | Coefficient | Coefficient type | Vanishes when |
|---|---|---|---|---|
| scalar | $e_t$ | $c_{\mathrm b}c_{\mathrm r}-i s_{\mathrm b}s_{\mathrm r}\,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ | complex | never |
| boost axis | $\vec u_{\mathrm b}$ | $i s_{\mathrm b}c_{\mathrm r}$ | imaginary | $\psi=0$ or $\theta=\pi$ |
| rotor axis | $\vec u_{\mathrm r}$ | $c_{\mathrm b}s_{\mathrm r}$ | real | $\theta\in\{0,2\pi\}$ |
| cross term | $\vec u_{\mathrm b}\times\vec u_{\mathrm r}$ | $i s_{\mathrm b}s_{\mathrm r}$ | imaginary, orthogonal to both axes | $\psi=0$, $\theta\in\{0,2\pi\}$, or axes parallel or antiparallel |

The vector part is a combination of the two axes and their cross product. If the axes are not parallel, it is parallel to $\vec u_{\mathrm b}$ exactly when $\theta\in\{0,2\pi\}$, and parallel to $\vec u_{\mathrm r}$ exactly when $\psi=0$; otherwise it is along neither. The cross term is present whenever the axes are neither parallel nor antiparallel and both parameters are nonzero. The two axes need not be orthogonal, so in general the three directions form a frame, not an orthogonal one; the cross product is orthogonal to both.

The table collects the configurations in which the frame collapses.

| Configuration | Condition | $\tilde U$ | $\operatorname{Vect}\tilde U$ |
|---|---|---|---|
| boost only | $\theta=0$ | $\tilde U_{\mathrm b}$ | $i s_{\mathrm b}\vec u_{\mathrm b}$ |
| boost with a full turn | $\theta=2\pi$ | $-\tilde U_{\mathrm b}$ | $-i s_{\mathrm b}\vec u_{\mathrm b}$ |
| rotor only | $\psi=0$ | $\tilde u_{\mathrm r}$ | $s_{\mathrm r}\vec u_{\mathrm r}$ |
| parallel axes | $\vec u_{\mathrm r}=\vec u_{\mathrm b}=\vec u$ | $\exp\bigl(\frac{\theta+i\psi}{2}\vec u\bigr)$ | $\sin\bigl(\frac{\theta+i\psi}{2}\bigr)\vec u$ |
| antiparallel axes | $\vec u_{\mathrm r}=-\vec u_{\mathrm b}$ | $\exp\bigl(\frac{-\theta+i\psi}{2}\vec u_{\mathrm b}\bigr)$ | $\sin\bigl(\frac{-\theta+i\psi}{2}\bigr)\vec u_{\mathrm b}$ |

In the parallel and antiparallel rows the cross term vanishes and the three directions collapse to one axis; the formula becomes the single exponential of §*One Exponential*, with the complex angle $\frac{\theta+i\psi}{2}$ and, for opposite axes, $\frac{-\theta+i\psi}{2}$. This is the component form of the commutativity criterion of that section. When the axes are orthogonal, the scalar part is real, $c_{\mathrm b}c_{\mathrm r}$, and the vector part is the sum of three mutually orthogonal terms.

The cross term is also the finite counterpart of the Baker–Campbell–Hausdorff defect of §*The Single Logarithm*: the defect lies along the same direction $\vec u_{\mathrm b}\times\vec u_{\mathrm r}$, with first-order coefficient $\frac{i\psi\theta}{4}$ in place of $i s_{\mathrm b}s_{\mathrm r}$.

**The complete result.** The modulus is central, so multiplying the two parts of $\tilde U$ by $\Rho=r e^{i\alpha}$ gives the element in full:

$$
\boxed{
\begin{aligned}
\tilde Q={}&
r e^{i\alpha}\Bigl(\cosh\frac{\psi}{2}\cos\frac{\theta}{2}
-i\sinh\frac{\psi}{2}\sin\frac{\theta}{2}\,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}\Bigr)e_t\\[2pt]
&+i\,r e^{i\alpha}\sinh\frac{\psi}{2}\cos\frac{\theta}{2}\,\vec u_{\mathrm b}
+r e^{i\alpha}\cosh\frac{\psi}{2}\sin\frac{\theta}{2}\,\vec u_{\mathrm r}
+i\,r e^{i\alpha}\sinh\frac{\psi}{2}\sin\frac{\theta}{2}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r}.
\end{aligned}}
$$

The four terms are the scalar part and the three components of the vector part: along the boost axis, along the rotor axis, and along their cross product. The scalar part is complex; the rotor-axis component is real, and the other two are imaginary. The vector part is generally parallel to neither axis, and the modulus multiplies both parts by the same complex number without mixing them.

### One Exponential

The two central factors commute with the two non-central ones and with each other. The boost and the rotor commute exactly when their axes are parallel or antiparallel:

$$
\Bigl[i\frac{\psi}{2}\vec u_{\mathrm b},\frac{\theta}{2}\vec u_{\mathrm r}\Bigr]
=\frac{i\psi\theta}{4}[\vec u_{\mathrm b},\vec u_{\mathrm r}]
=\frac{i\psi\theta}{2}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r},
$$

which vanishes exactly when $\vec u_{\mathrm b}\times\vec u_{\mathrm r}=0$, that is, when the axes are parallel or antiparallel, or one of the two parameters is zero. In that case the four exponents add, and the word is the single exponential of the sum:

$$
\tilde Q=\exp\Bigl(\ln r+i\alpha+\frac{\theta+i\psi}{2}\vec u\Bigr),
\qquad
\vec u_{\mathrm b}=\vec u_{\mathrm r}=\vec u,
$$

with the complex angle $\frac{\theta+i\psi}{2}$; for opposite axes, replace $\theta$ by $-\theta$. The right-hand side is the exponential of a single element, read through the complex cosine and sine. When the axes are not parallel, the four exponents do not add: the word is not the exponential of their sum, and it stays a product of four exponentials, although it still has other single logarithms.

## Existence and Uniqueness

**Theorem (the exponential polar decomposition).** Every invertible biquaternion $\tilde Q$ has a unique writing

$$
\fbox{\tilde Q=r\,\exp(i\alpha)\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}},
$$

with $r>0$, $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$, $\tilde U_{\mathrm b}$ Hermitian positive of norm one, and $\tilde u_{\mathrm r}$ a unit real quaternion. Consequently it has the exponential writing above, with $\psi\ge0$, $\theta\in[0,2\pi]$, and the two axes; the axes are unique when $\psi>0$ and $\theta\notin\{0,2\pi\}$.

**Proof.** The algebraic statement is the modulus–unit theorem of *Modulus–Unit Polar Decomposition of Biquaternions*: the modulus $\Rho$ is the principal square root of $\tilde Q\tilde Q^{\natural}$, in the branch $\operatorname{Re}\Rho\ge0$, and $\tilde U=\tilde Q/\Rho$ has norm one. The matrix image of $\tilde U$ lies in $SL(2,\mathbb{C})$, and the global Cartan decomposition $SL(2,\mathbb{C})=P\cdot K$ gives the unique factorization $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\tilde U_{\mathrm b}$ positive Hermitian of determinant one and $\tilde u_{\mathrm r}$ unitary of determinant one. A positive Hermitian determinant-one matrix is the exponential of a unique Hermitian traceless matrix, which is $i\frac{\psi}{2}\vec u_{\mathrm b}$ with $\psi\ge0$ and a unit axis; a unitary determinant-one matrix is the exponential of an anti-Hermitian traceless matrix, which is $\frac{\theta}{2}\vec u_{\mathrm r}$ with $\theta\in[0,2\pi]$. The endpoint $\theta=2\pi$ is the central rotor $-e_t$, where the axis is undefined. The scale and the phase are the polar coordinates of $\Rho$, unique in the branch.

The count of parameters is

$$
\underbrace{1}_{\ln r}+\underbrace{1}_{\alpha}+\underbrace{1+2}_{\psi,\vec u_{\mathrm b}}+\underbrace{1+2}_{\theta,\vec u_{\mathrm r}}=8,
$$

the real dimension of $\mathbb{B}^{\times}$.

**Degeneracies.** The boost axis is undefined at $\psi=0$, where the boost is the identity; the rotor axis is undefined at $\theta=0$, where the rotor is the identity, and at $\theta=2\pi$, where the rotor is $-e_t$ for every axis. These are the usual coordinate singularities of polar coordinates. The element is smooth there, and the word is unique.

| Parameter | Range | Unique? |
|---|---|---|
| $r$ | $(0,\infty)$ | yes |
| $\alpha$ | $(-\frac{\pi}{2},\frac{\pi}{2}]$ | yes: the branch |
| $\psi$ | $[0,\infty)$ | yes |
| $\vec u_{\mathrm b}$ | $S^2$ | no: undefined at $\psi=0$ |
| $\theta$ | $[0,2\pi]$ | yes |
| $\vec u_{\mathrm r}$ | $S^2$ | no: undefined at $\theta\in\{0,2\pi\}$ |

**The boundary.** The word is defined on the complement of the null cone. As an element approaches the cone, the scale vanishes and the rapidity diverges: the word has boundary values, reached with $r\to0$ and $\psi\to\infty$ at the rate $r e^{\psi/2}\to R$ with $0<R<\infty$. The boundary is treated in §*The Boundary of the Word*.

## The Logarithm

### The Cartan Logarithm

Write the unit factor as $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ and put

$$
\tilde H=\operatorname{Log}\tilde U_{\mathrm b}=i\frac{\psi}{2}\vec u_{\mathrm b},
\qquad
\tilde K=\operatorname{Log}\tilde u_{\mathrm r}=\frac{\theta}{2}\vec u_{\mathrm r}.
$$

The pair $(\tilde H,\tilde K)$ is the **Cartan logarithm** of $\tilde U$. It is unique with the ranges of the theorem, except at the central rotor $-e_t$, where the axis is undefined. It consists of a Hermitian traceless element and an anti-Hermitian traceless element, and it satisfies

$$
\tilde U=\exp(\tilde H)\exp(\tilde K).
$$

The name is the one of the Cartan decomposition: the rotor exponent lies in $\mathfrak k$, the boost exponent in $\mathfrak p$, and $SL(2,\mathbb{C})=\exp(\mathfrak p)\exp(\mathfrak k)$ is global and unique. The full algebra splits as

$$
\mathbb{B}=\mathbb{R}e_t\ \oplus\ i\mathbb{R}e_t\ \oplus\ \mathfrak p\ \oplus\ \mathfrak k,
$$

with the scale exponent in the first summand, the phase exponent in the second, the boost exponent in the third and the rotor exponent in the fourth. This is the exponential reading of the four coordinate blocks of *The Polar Decomposition and Remarkable Subspaces*.

### The Single Logarithm

A **single logarithm** of $\tilde Q$ is an element $\operatorname{Log}\tilde Q$ with $\exp(\operatorname{Log}\tilde Q)=\tilde Q$. Since $\mathbb{B}\cong M_2(\mathbb{C})$ and every invertible complex matrix has a logarithm, the exponential $\exp:\mathbb{B}\to\mathbb{B}^{\times}$ is surjective. A single logarithm is related to the Cartan logarithm, for a compatible choice of branches, by

$$
\boxed{\operatorname{Log}\tilde Q=\ln r+i\alpha+\operatorname{Log}\bigl(\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr)}.
$$

The last term is a logarithm of the unit factor inside $\mathfrak{gl}(2,\mathbb{C})$, not inside $\mathfrak{sl}(2,\mathbb{C})$: its trace may be a nonzero multiple of $2\pi i$. This trace obstruction is what makes $SL(2,\mathbb{C})$ not globally exponential, even though it is connected.

The single logarithm is not the sum of the four exponents. The sum is the **formal exponent**

$$
\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r},
$$

and

$$
\exp\bigl(\tilde Q_{\log}\bigr)\neq\tilde Q
\qquad\text{unless}\qquad
[\vec u_{\mathrm b},\vec u_{\mathrm r}]=0\quad\text{or}\quad\psi\theta=0.
$$

The defect is the Baker–Campbell–Hausdorff correction. To first order,

$$
\operatorname{Log}\bigl(\exp\tilde H\exp\tilde K\bigr)
=\tilde H+\tilde K+\tfrac12[\tilde H,\tilde K]+\cdots,
$$

and the first correction is again a boost, because

$$
\boxed{\tfrac12[\tilde H,\tilde K]
=\frac{i\psi\theta}{4}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r}
\in\mathfrak p}.
$$

So the sum of a boost and a rotor exponent is corrected by another boost, and the true logarithm is not the sum of the four exponents. The correction vanishes exactly when the axes are parallel or antiparallel, or one of the two parameters vanishes, which is the amalgamation of §*One Exponential*. The higher terms are the iterated commutators; the series is the one of *Biquaternion Lie Group and Exponential Structure*, §*The Correspondence with the Lie Algebra*.

The defect is not a rounding effect. In the worked example of *Worked Examples of Exponential Polar Decomposition of Biquaternions*, §*Case 8*, the four exponents sum to an element whose exponential misses the element by $0.5425679115$ in the largest coefficient modulus, while the true logarithm reproduces it to $5.0\times10^{-16}$.

### The Kernel and the Fibre

The exponential is not injective. The elementary article computes its kernel: it contains the central periods $2\pi i k\,e_t$, the pure periods $2\pi\vec U$ for every real unit vector $\vec U$, and the mixed elements $\pi i\,e_t+\pi\vec U$. The kernel is **not a subgroup**: it is not closed under addition, because the exponential is not a homomorphism; the sum of two kernel elements need not lie in the kernel.

The fibre over an element is not a coset of the kernel either. The logarithms of a unit form a discrete or continuous family according to the type of the matrix; the description is in *Biquaternion Elementary Functions*, §*The Domain and the Fibre*. The polar parameters do not cut the fibre of the exponential to one point: the four exponents sum to the formal exponent, which is not a logarithm. What they cut to one point, up to the degeneracies of the axes, is the fibre of the **word map**

$$
(r,\alpha,\psi,\vec u_{\mathrm b},\theta,\vec u_{\mathrm r})
\longmapsto
r\exp(i\alpha)\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr).
$$

The scale is fixed by positivity, the phase by the branch, the rapidity by $\psi\ge0$, and the rotor angle by $[0,2\pi]$. The exponential polar decomposition is therefore a **section** of the word map, a global parametrization of $\mathbb{B}^{\times}$; it is neither a section of the exponential nor a quotient.

## The Group Law

The product of two words is

$$
\bigl(r_1e^{i\alpha_1}e^{\tilde H_1}e^{\tilde K_1}\bigr)
\bigl(r_2e^{i\alpha_2}e^{\tilde H_2}e^{\tilde K_2}\bigr)
=r_1r_2\,e^{i(\alpha_1+\alpha_2)}\,e^{\tilde H_1}e^{\tilde K_1}e^{\tilde H_2}e^{\tilde K_2}.
$$

The central factors add. The non-central ones do not: the middle product $e^{\tilde K_1}e^{\tilde H_2}$ has to be re-split as a boost times a rotor, and the re-splitting is the Cartan decomposition of a product of two exponentials. The first correction is the commutator,

$$
e^{\tilde K_1}e^{\tilde H_2}
=e^{\tilde H_2+\tfrac12[\tilde K_1,\tilde H_2]+\cdots}e^{\tilde K_1+\cdots},
$$

so the rotor of the first word changes the boost of the second by a term in $\mathfrak p$: the boost is conjugated, not added. The rotor itself is unchanged to first order; its first correction is of second order. The parameters of the product are not the sums of the parameters.

The brackets of the two summands close as a **symmetric pair**:

| bracket | lies in | reading |
|---|---|---|
| $[\mathfrak k,\mathfrak k]$ | $\mathfrak k$ | two rotors compose to a rotor |
| $[\mathfrak p,\mathfrak p]$ | $\mathfrak k$ | two boosts compose to a boost times a rotor |
| $[\mathfrak k,\mathfrak p]$ | $\mathfrak p$ | the commutator of a rotor and a boost is a boost |

The first row is the subgroup $SU(2)$ of the rotor. The second is the Thomas–Wigner rotation: the product of two boosts is a boost times a rotor, and the residual rotor is computed in *The Polar Decomposition and Remarkable Subspaces*, §*The Boost Family and the Rotor Group*. The third is the statement that the boost set is a symmetric space and not a group: the commutator of an infinitesimal boost and an infinitesimal rotation is an infinitesimal boost, so the boost directions are stable under the adjoint action of the rotor, while the boost set itself is not closed under multiplication. The four factors obey the following laws.

| Data | Law |
|---|---|
| Scale and phase | multiply |
| Boost | conjugated by the rotor, not added |
| Rotor | multiplies |
| Exponent | does not add: the Baker–Campbell–Hausdorff correction |
| Group | $\mathbb{B}^{\times}\cong\mathrm{GL}_2(\mathbb{C})$, generated by the scalars and $SL(2,\mathbb{C})$ |

## The Matrix Picture

### The Matrix Exponential

The matrix model turns the exponential into the matrix exponential, because $\mathsf M_2$ is a $\mathbb{C}$-algebra homomorphism:

$$
\mathsf M_2\bigl(\exp\tilde X\bigr)=\exp\bigl(\mathsf M_2(\tilde X)\bigr).
$$

The polar word becomes the polar decomposition of $\mathrm{GL}_2(\mathbb{C})$,

$$
\mathsf M_2(\tilde Q)=r\,e^{i\alpha}\,\mathsf M_2(\tilde U_{\mathrm b})\,\mathsf M_2(\tilde u_{\mathrm r}),
$$

with $\mathsf M_2(\tilde U_{\mathrm b})$ positive definite of determinant one and $\mathsf M_2(\tilde u_{\mathrm r})$ unitary of determinant one. The four exponents sit in the two summands of the decomposition of the Lie algebra

$$
\mathfrak{gl}_2(\mathbb{C})=\mathfrak{u}(2)\oplus\mathfrak{H},
\qquad
\mathfrak{u}(2)=\{X:X^{\dagger}=-X\},
\qquad
\mathfrak{H}=\{X:X^{\dagger}=X\},
$$

of real dimensions $4$ and $4$. The exponents of the scale and the boost lie in $\mathfrak H$, those of the phase and the rotor in $\mathfrak u(2)$; the central real line is the scale, the central imaginary line is the phase, and the traceless parts are the boost and the rotor.

| Matrix object | Algebra object | Dimension | Factor |
|---|---|---|---|
| positive determinant-one matrix | Hermitian positive unit-norm element | $3$ | boost |
| unitary determinant-one matrix | unit real quaternion | $3$ | rotor |
| positive real scalar | scale | $1$ | $r$ |
| unit complex scalar | phase | $1$ | $\zeta$ |

### The Derivative and the Jacobian

The exponential is surjective onto $\mathrm{GL}_2(\mathbb{C})$ because every invertible matrix has a logarithm, and it is not injective because the logarithm is multivalued. The determinant gives

$$
\det\mathsf M_2\bigl(\exp\tilde X\bigr)=\exp\bigl(\operatorname{tr}\mathsf M_2(\tilde X)\bigr)\neq0,
$$

so the image lies in the units, and the trace is the logarithmic scale of the determinant.

The derivative of the exponential is not left multiplication by the exponential. By *Biquaternion Elementary Functions*, §*Properties* of §*The Exponential*,

$$
d\exp_{\tilde X}(\tilde H)=\int_0^1\exp(s\tilde X)\,\tilde H\,\exp((1-s)\tilde X)\,ds,
$$

and it reduces to $\exp(\tilde X)\tilde H$ when $[\tilde H,\tilde X]=0$. In the commutative algebras the commutator vanishes identically, so the derivative is left multiplication by the exponential; here it is not, because the algebra is noncommutative.

The derivative of the logarithm is the inverse linear map, by the inverse function theorem:

$$
d\operatorname{Log}_{\tilde Q}=\bigl(d\exp_{\operatorname{Log}\tilde Q}\bigr)^{-1}.
$$

The exponential is a local biholomorphism on the complement of its critical set; the critical set is described in *Biquaternion Elementary Functions*, §*The Logarithm*.

## The Three Polar Decompositions

The exponential form is one of three presentations of the same factorisation. The algebraic word $\tilde Q=\Rho\tilde U$ of *Modulus–Unit Polar Decomposition of Biquaternions* is the coarsest; the Cartan form splits the unit factor into a Hermitian positive factor and a unitary factor; the exponential form writes each factor as an exponential. The three agree on the element and differ in the functions they use and in the group law.

### The Three Forms

| Decomposition | Formula | Parameters | Domain | Uniqueness | Functions | Group reading |
|---|---|---|---|---|---|---|
| Modulus–unit | $\tilde Q=\Rho\tilde U$ | $\Rho=r e^{i\alpha}\in\mathbb{C}^{\times}$ in the branch, $\tilde U\in SL(2,\mathbb{C})$ | all units | unique | complex polar coordinates | $\mathbb{C}^{\times}\times SL(2,\mathbb{C})$ |
| Cartan | $\tilde Q=r\zeta\,\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $r>0$, $\alpha$, $\psi$, $\vec u_{\mathrm b}$, $\theta$, $\vec u_{\mathrm r}$ | all units | unique factors; axes degenerate | square roots | $P\cdot K$ |
| Exponential | each factor written $\exp$ | the same six data | all units | unique word; axes degenerate | exponential and logarithm | four exponents |

### The Modulus–Unit Form

The modulus–unit form writes $\tilde Q=\Rho\tilde U$ with $\Rho=r e^{i\alpha}\in\mathbb{C}^{\times}$ in the branch and $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ of norm one. The complex modulus carries the scale and the central phase; the unit factor carries the six remaining real dimensions. It is global, algebraic and unique, and it is the form from which the other two are read.

### The Cartan Form

The Cartan form is the split $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ of the unit factor into a Hermitian positive element of norm one and a unit real quaternion. In the matrix model it is $SL(2,\mathbb{C})=P\cdot K$, unique because $P\cap K=\{e_t\}$. It is algebraic and parameter-free: the two factors are determined by $\tilde U$, and the rapidity and angle are their polar coordinates.

### The Exponential Form

The exponential form writes each of the four factors as an exponential,

$$
r=\exp(\ln r),\qquad
\zeta=\exp(i\alpha),\qquad
\tilde U_{\mathrm b}=\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr),\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

and multiplies them in the order scale, phase, boost, rotor. It is the transcendental coordinate on the Cartan form. Its four exponents do not add: the single logarithm differs from their sum by the Baker–Campbell–Hausdorff correction of §*The Single Logarithm*.

### What the Comparison Says

The modulus–unit form is the coarsest and the most algebraic. The Cartan form is the finest algebraic split, and the form that identifies the two real forms of the Lie algebra. The exponential form is the only one that uses the logarithm; the word itself is a product of exponentials, and the single logarithm is a separate, multivalued object. The parameters select a canonical word, not a canonical logarithm.

| Property | Modulus–unit | Cartan | Exponential |
|---|---|---|---|
| Algebraic or transcendental | algebraic | algebraic | transcendental |
| Global on the units | yes | yes | yes |
| Unique without a choice | yes | yes | up to the axis degeneracies |
| Non-uniqueness | none | none | the axis degeneracies |
| Group law | multiplication of the factors | re-splitting of $P$ and $K$ | Baker–Campbell–Hausdorff |
| Logarithm | none: a square root is used | the Cartan pair | the single logarithm, multivalued |

## The Exponential Coordinates

### The Coordinate Map

The parameters $r,\alpha,\psi,\theta$ and the two axes are coordinates on the group of units, and their ranges make the map a bijection up to the degeneracies of the axes. The coordinate lines are the four one-parameter families:

- the **scale line** $r\mapsto r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, a half-line, non-compact;
- the **phase circle** $\alpha\mapsto r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, a circle of length $2\pi$ before the branch cuts it to $\pi$;
- the **boost hyperbola** $\psi\mapsto r e^{i\alpha}\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\tilde u_{\mathrm r}$, a non-compact ray;
- the **rotor arc** $\theta\mapsto r e^{i\alpha}\tilde U_{\mathrm b}\exp(\frac{\theta}{2}\vec u_{\mathrm r})$, a great semicircle from $e_t$ to $-e_t$.

### The Topology

The positive cone $P$ is homeomorphic to $\mathbb{R}^{3}$ and the rotor sphere $K=SU(2)$ is $S^{3}$, so

$$
SL(2,\mathbb{C})\simeq\mathbb{R}^{3}\times S^{3}.
$$

The group of units retracts onto $U(2)$, and the determinant splits $U(2)\cong U(1)\times SU(2)$ as a space, so

$$
\mathbb{B}^{\times}\simeq U(2)\cong S^{1}\times S^{3}.
$$

The branch of the modulus makes $\tilde Q\mapsto(\Rho,\tilde U)$ a bijection onto $\mathbb{C}^{\times}\times SL(2,\mathbb{C})$, but not a homeomorphism: on the cut the phase jumps by the factor $-1$ and the rotor changes sign, so the circular direction is carried by the phase, and the branch coordinate does not see it continuously. The fundamental group of the group of units is therefore $\mathbb{Z}$, carried by the phase alone; the rotor contributes the simply connected factor $S^{3}$, and the scale and the boost are the two non-compact directions. This is the exponential reading of the homotopy statement of *Modulus–Unit Polar Decomposition of Biquaternions*, §*The Group of Units and the Unitary Group*.

### The Conformal Factor

The **conformal factor** is read in the coordinates. Under the sandwich $\tilde Q\,X\,\tilde Q^{*}$, the quaternionic norm of $X$ is multiplied by

$$
r^{4}=\exp(4\ln r)=\bigl\lvert\langle\tilde Q\rangle_{\natural}\bigr\rvert^{2},
$$

so lengths are multiplied by $r^{2}=\lvert\langle\tilde Q\rangle_{\natural}\rvert$. The scale exponent is thus a quarter of the logarithm of the conformal factor. The phase, the boost and the rotor are isometries of the form; only the scale moves it.

## The Boundary of the Word

The word is defined on the complement of the null cone,

$$
\mathcal N=\{\tilde Q\in\mathbb{B}:\langle\tilde Q\rangle_{\natural}=0\}.
$$

The cone is one complex equation, hence a cone of real dimension six. In the matrix model it is the determinant-zero set, so its nonzero elements are exactly the rank-one matrices, that is, the zero divisors of the algebra (*Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra*). On the cone the rapidity diverges, the scale collapses, and the word has boundary values rather than a value.

### The Two Strata

The scalar part cuts the cone into two strata.

| Stratum | Condition | Form | Real dimension |
|---|---|---|---|
| Non-nilpotent | $Q_t\neq0$ | $\tilde Q=Q_te_t+\vec Q$, $\vec Q^{2}=-Q_t^{2}$ | $6$ |
| Nilpotent | $Q_t=0$ | $\tilde Q=\vec Q$, $\vec Q^{2}=0$ | $4$ |

The first stratum consists of the nonzero null elements with nonzero scalar part; it is open and dense in the cone. The second is the nilpotent stratum, of real codimension two, and it lies in the closure of the first. The scalar part is the exact invariant that separates them. Only the normal forms in the table are used below.

### The Boundary Limits

**Theorem (the boundary limits).** Let $\vec u_{\mathrm b}$ and $\vec u_{\mathrm r}$ be unit vectors, $\zeta$ a unit complex number and $R>0$, and let

$$
\tilde Q(\psi)=R\exp\Bigl(-\frac{\psi}{2}\Bigr)\zeta
\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)\tilde u_{\mathrm r},
\qquad \psi>0.
$$

Then $\tilde Q(\psi)$ is invertible for every $\psi$, and

$$
\boxed{\tilde Q(\psi)\longrightarrow
\frac{R\zeta}{2}\bigl(e_t+i\vec u_{\mathrm b}\bigr)\tilde u_{\mathrm r}
\qquad(\psi\to\infty)},
$$

a nonzero null element of rank one. It is nilpotent exactly when $\tilde u_{\mathrm r}$ anticommutes with $\vec u_{\mathrm b}$, and it has nonzero scalar part otherwise.

**Proof.** The closed form of the boost gives

$$
\exp\Bigl(-\frac{\psi}{2}\Bigr)\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)
=\frac{1+e^{-\psi}}{2}e_t+\frac{1-e^{-\psi}}{2}i\vec u_{\mathrm b}
\longrightarrow\frac12\bigl(e_t+i\vec u_{\mathrm b}\bigr).
$$

The norm of the limit is zero, and its matrix image has rank one because the first factor has rank one and $\tilde u_{\mathrm r}$ is invertible. Write $\tilde u_{\mathrm r}=a e_t+b\vec u_{\mathrm b}+\tilde u_{\perp}$ with $a,b\in\mathbb{R}$ and $\tilde u_{\perp}$ orthogonal to $\vec u_{\mathrm b}$. Then $\operatorname{tr}\mathsf M_2(\tilde u_{\mathrm r})=2a$ and $\operatorname{tr}\mathsf M_2(\vec u_{\mathrm b}\tilde u_{\mathrm r})=-2b$, so the trace of the limit is $R\zeta(a-ib)$. A rank-one matrix $L$ satisfies $L^{2}=(\operatorname{tr}L)L$. Hence, if $a-ib\neq0$, the limit has nonzero scalar part; if $a-ib=0$, the trace vanishes and $L^{2}=0$. Now $a-ib=0$ with real $a,b$ means $a=b=0$, that is, $\tilde u_{\mathrm r}=\tilde u_{\perp}$ orthogonal to $\vec u_{\mathrm b}$, that is, $\tilde u_{\mathrm r}$ anticommutes with $\vec u_{\mathrm b}$.

**The rate.** The word of the theorem has norm

$$
\langle\tilde Q(\psi)\rangle_{\natural}=R^{2}\exp(-\psi)\zeta^{2},
$$

so the distance to the cone is exponential in the rapidity, and the modulus is $R\exp(-\psi/2)$. The boundary is approached along the exponential coordinate line of the boost, with the scale line compensating: the boost is the non-compact factor that drives the word to the boundary, and the scale is the factor that keeps the element finite.

**The exponential limit.** For a real unit vector $\vec u$,

$$
\frac12\bigl(e_t+i\vec u\bigr)
=\lim_{\psi\to\infty}\frac{\exp(i\frac{\psi}{2}\vec u)}{2\cosh\frac{\psi}{2}}
=\lim_{\psi\to\infty}\exp\Bigl(-\frac{\psi}{2}\Bigr)\exp\Bigl(i\frac{\psi}{2}\vec u\Bigr).
$$

The limit is the direction of an infinite boost, with the scale removed. The nilpotent stratum has its own exponential description: for $N$ with $N^{2}=0$, $\exp(tN)=e_t+tN$ for every complex $t$, a unipotent line which is invertible for every finite $t$ and tends to infinity with $t$.

The boundary points are not in the image of the exponential, because every value of the exponential is invertible and a null element is not. They are in its closure, as the limits above.

## Summary

### Main Results

| Result | Statement |
|---|---|
| Domain | the units $\mathbb{B}^{\times}=\{\langle\tilde Q\rangle_{\natural}\neq0\}$ |
| Decomposition | $\tilde Q=r e^{i\alpha}\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\exp(\frac{\theta}{2}\vec u_{\mathrm r})$ |
| Parameters | $r>0$, $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$, $\psi\ge0$, $\theta\in[0,2\pi]$, two unit axes |
| Modulus | $\Rho=r e^{i\alpha}$, the principal square root of $\tilde Q\tilde Q^{\natural}$ |
| Unit factor | $\tilde U=\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\exp(\frac{\theta}{2}\vec u_{\mathrm r})$ |
| Existence | every unit has a decomposition |
| Uniqueness | the factors are unique; axes degenerate at $\psi=0$ and $\theta\in\{0,2\pi\}$ |
| Cartan logarithm | $(\tilde H,\tilde K)=(i\frac{\psi}{2}\vec u_{\mathrm b},\frac{\theta}{2}\vec u_{\mathrm r})$ |
| Single logarithm | exists; multivalued; not the sum of the four exponents |
| BCH defect | $\tfrac12[\tilde H,\tilde K]=\frac{i\psi\theta}{4}\vec u_{\mathrm b}\times\vec u_{\mathrm r}\in\mathfrak p$ |
| Group | $\mathbb{B}^{\times}\cong\mathbb{C}^{\times}\times SL(2,\mathbb{C})\cong\mathrm{GL}_2(\mathbb{C})$ |
| Topology | $\mathbb{B}^{\times}\simeq S^{1}\times S^{3}$ |
| Conformal factor | $r^{4}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}$ |
| Boundary | the null cone, with the two strata of non-nilpotent and nilpotent elements |

### Formulas

| Quantity | Formula |
|---|---|
| Scale and phase | $\Rho=r e^{i\alpha}$, $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$ |
| Boost | $\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ |
| Rotor | $\tilde u_{\mathrm r}=\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ |
| Unit factor, scalar part | $\operatorname{Sc}\tilde U=c_{\mathrm b}c_{\mathrm r}-i s_{\mathrm b}s_{\mathrm r}\,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ |
| Unit factor, vector part | $\operatorname{Vect}\tilde U=i s_{\mathrm b}c_{\mathrm r}\vec u_{\mathrm b}+c_{\mathrm b}s_{\mathrm r}\vec u_{\mathrm r}+i s_{\mathrm b}s_{\mathrm r}\vec u_{\mathrm b}\times\vec u_{\mathrm r}$ |
| Axis content of the element | $\operatorname{Sc}\tilde Q=\Rho\operatorname{Sc}\tilde U$, $\operatorname{Vect}\tilde Q=\Rho\operatorname{Vect}\tilde U$ |
| Decomposition | $\tilde Q=\Rho\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ |
| Formal exponent | $\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}$ |
| Cartan logarithm | $\tilde H=i\frac{\psi}{2}\vec u_{\mathrm b}$, $\tilde K=\frac{\theta}{2}\vec u_{\mathrm r}$ |
| Single logarithm | $\operatorname{Log}\tilde Q=\ln r+i\alpha+\operatorname{Log}(\tilde U_{\mathrm b}\tilde u_{\mathrm r})$ |
| BCH correction | $\tfrac12[\tilde H,\tilde K]=\frac{i\psi\theta}{4}\vec u_{\mathrm b}\times\vec u_{\mathrm r}$ |
| Boundary limit | $\frac{R\zeta}{2}(e_t+i\vec u_{\mathrm b})\tilde u_{\mathrm r}$ |
| Matrix model | $\mathsf M_2(\tilde Q)=r e^{i\alpha}\mathsf M_2(\tilde U_{\mathrm b})\mathsf M_2(\tilde u_{\mathrm r})$ |

Every invertible biquaternion has a unique exponential polar word,

$$
\tilde Q=r\,e^{i\alpha}\,
\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)\,
\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with

$$
r>0,\qquad
\alpha\in\Bigl(-\frac{\pi}{2},\frac{\pi}{2}\Bigr],\qquad
\psi\ge0,\qquad
\theta\in[0,2\pi],\qquad
\lvert\vec u_{\mathrm b}\rvert=\lvert\vec u_{\mathrm r}\rvert=1.
$$

The modulus $\Rho=r e^{i\alpha}$ is the principal square root of $\tilde Q\tilde Q^{\natural}$, and the unit factor is $\tilde U=\tilde Q/\Rho$. The Cartan decomposition $SL(2,\mathbb{C})=P\cdot K$ splits the unit factor into the boost and the rotor, and the two angles are the polar coordinates of the two factors.

The four exponents do not add. The formal exponent

$$
\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}
$$

satisfies $\exp(\tilde Q_{\log})=\tilde Q$ exactly when the boost and the rotor commute, that is, when their axes are parallel or antiparallel, or one of the two parameters vanishes. In general the Baker–Campbell–Hausdorff correction is a boost, and the single logarithm is not the sum of the four exponents. The polar word is a section of the word map, not of the exponential.

The group law is not additive: the scale and the phase multiply, the rotor multiplies, and the boost is conjugated by the rotor. The brackets close as the symmetric pair $(\mathfrak k,\mathfrak p)$: $[\mathfrak k,\mathfrak k]\subset\mathfrak k$, $[\mathfrak p,\mathfrak p]\subset\mathfrak k$, $[\mathfrak k,\mathfrak p]\subset\mathfrak p$. The group is $\mathbb{B}^{\times}\cong\mathrm{GL}_2(\mathbb{C})$, with the topology $S^{1}\times S^{3}$.

The word is defined on the complement of the null cone. At the boundary the scale collapses and the rapidity diverges at the rate $r=e^{-\psi/2}$, and the limit is a rank-one null element. It is nilpotent exactly when the rotor anticommutes with the boost axis, and it has nonzero scalar part otherwise. The two strata and the boundary form are collected in §*The Boundary of the Word*.

### Comparison with the Neighbouring Cases

The table compares the three exponential polar decompositions; in the split-complex column, $\epsilon$ is the component sign.

| Feature | Split-complex | Reduced biquaternion | Biquaternion |
|---|---|---|---|
| Algebra | $\mathbb{R}[j]$, $j^2=1$ | $\mathbb{C}\otimes\mathbb{C}$ | $\mathbb{C}\otimes\mathbb{H}$ |
| Element | $Q=q+jq'$ | $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | $\tilde Q=Q_te_t+\vec Q$ |
| Parameters | $r>0$, $\phi$, $\epsilon$ | $\rho>0$, $\phi$, $\alpha$, $\beta$ | $r>0$, $\alpha$, $\psi$, $\theta$, two axes |
| Discrete data | $(\mathbb{Z}/2)^2$ | lattice $\Lambda$ | none |
| Kernel | trivial | $\mathbb{Z}^2$ | not a subgroup |
| Matrix model | $2\times2$ real symmetric | $2\times2$ complex in $\{1,j\}$ | $2\times2$ complex |
| Group | $(\mathbb{Z}/2)^2\times\mathbb{R}^2$ | $\mathbb{R}^2\times T^2$ | $\mathbb{C}^{\times}\times SL(2,\mathbb{C})\cong\mathrm{GL}_2(\mathbb{C})$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | the element, with scalar part $Q_t$ and vector part $\vec Q$ |
| $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | the quaternionic norm |
| $\natural$ | the quaternion conjugation |
| $*$ | the Hermitian star, $\natural$ composed with coefficientwise conjugation |
| $\mathsf M_2$ | the matrix model, $\tilde Q\mapsto Q_tI_2-i\vec Q\cdot\boldsymbol\sigma$ |
| $\Rho=r e^{i\alpha}$ | the complex modulus |
| $r>0$ | the scale |
| $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$ | the phase |
| $\psi\ge0$ | the rapidity |
| $\theta\in[0,2\pi]$ | the rotor angle |
| $\vec u_{\mathrm b},\vec u_{\mathrm r}\in S^2$ | the boost and rotor axes |
| $\tilde U_{\mathrm b}=\exp(i\frac{\psi}{2}\vec u_{\mathrm b})$ | the boost |
| $\tilde u_{\mathrm r}=\exp(\frac{\theta}{2}\vec u_{\mathrm r})$ | the rotor |
| $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}=\tilde Q/\Rho$ | the unit factor |
| $\tilde H=i\frac{\psi}{2}\vec u_{\mathrm b}$ | the boost exponent |
| $\tilde K=\frac{\theta}{2}\vec u_{\mathrm r}$ | the rotor exponent |
| $\tilde Q_{\log}=\ln r+i\alpha+\tilde H+\tilde K$ | the formal exponent |
| $\mathfrak{k},\mathfrak{p}$ | the compact and non-compact summands of $\mathfrak{sl}(2,\mathbb{C})$ |
| $\mathcal N=\{\langle\tilde Q\rangle_{\natural}=0\}$ | the null cone |
| $R$ | the boundary rate, $r e^{\psi/2}\to R$ |
| $\zeta=e^{i\alpha}$ | the phase factor |

## Further Reading

- [Worked Examples of Exponential Polar Decomposition of Biquaternions](worked-examples-of-exponential-polar-decomposition-of-biquaternions.html), for the eight cases, the reconstruction and logarithm tables, and the null cone.
- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of Biquaternions](worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-biquaternions.html), for the same eight cases read in the eigenbasis, with the nilpotents and the spinors.
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential and the logarithm, their closed forms, the kernel and the principal branch.
- [Modulus–Unit Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the modulus, the unit factor and the uniqueness of the pair.
- [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), for the Hermitian positive and unitary factors.
- [Biquaternion Lie Group and Exponential Structure](biquaternion-lie-group-and-exponential-structure.html), for the Cartan decomposition, the Baker–Campbell–Hausdorff formula and the Lie algebra.
- [The Polar Decomposition and Remarkable Subspaces](the-polar-decomposition-and-remarkable-subspaces.html), for the four coordinate blocks and the boost family.
- [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the null cone and the zero divisors.
- [Exponential Polar Decomposition of Quaternions](exponential-polar-decomposition-of-quaternions.html), for the quaternion case.
- [Exponential Polar Decomposition of Split-Complex Numbers](exponential-polar-decomposition-of-split-complex-numbers.html), for the commutative two-dimensional case.
- [Exponential Polar Decomposition of Reduced Biquaternions](exponential-polar-decomposition-of-reduced-biquaternions.html), for the commutative four-dimensional case.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-biquaternion.html), for the relation with the eigenbasis.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation.
