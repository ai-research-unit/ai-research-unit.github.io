# __Worked Examples of Exponential Polar Decomposition of Quaternions__

## Introduction

This article computes the exponential polar decomposition of eight quaternions, one after another. It is the computational companion of *Exponential Polar Decomposition of Quaternions*. The decomposition, its existence and uniqueness, the logarithm and the matrix picture are established there and in *Quaternion Special Functions*; the proofs are not repeated. The layout follows *Worked Examples of Exponential Polar Decomposition of Biquaternions*: a method section, eight cases, a boundary family, and summary tables. The differences are forced by the algebra.

Each case is read from the four real coordinates $q_t,q_x,q_y,q_z$. The modulus, the angle and the axis are computed from them by the formulas of §*The Method*, and the word is checked against the reconstruction

$$
\tilde q=\exp(\ln r+\theta\vec n)=r\exp(\theta\vec n).
$$

The eight cases cover the identity, the two pure rotors, the pure scale, the scale and rotor on one axis, two products that exhibit the cross term, and a generic element.

| Group | Case | What it shows |
|---|---|---|
| Identity | $e_t$ | the trivial word, the axis undefined |
| Pure rotor | $\vec e_x$ | rotation angle $\pi$, exponent angle $\pi/2$ |
| Pure rotor | $\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_x$ | rotation angle $\pi/2$, exponent angle $\pi/4$ |
| Pure scale | $2e_t$ | the scale alone, no rotor |
| Scale and rotor | $3e_t+4\vec e_x$ | one axis, one exponential |
| Orthogonal axes | $\vec e_z=\vec e_x\vec e_y$ | a product word, defect $1$ |
| Non-parallel axes | $\frac{-\vec e_t+\vec e_z}{\sqrt2}$ | a product at $45^\circ$, defect $1/\sqrt2$ |
| Generic | $e_t+2\vec e_x+3\vec e_y+4\vec e_z$ | a non-unit with all four coordinates nonzero |

The norm is written in full throughout,

$$
\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}
=q_t^2+q_x^2+q_y^2+q_z^2 .
$$

The modulus is $r=\sqrt{\langle\tilde q\rangle_{\natural}}>0$, the angle is $\theta=\arccos(q_t/r)\in[0,\pi]$, and the axis $\vec n$ is a unit pure quaternion. The angle $\theta$ is the **exponent angle**, the half-angle stored in the rotor; the rotation produced by the sandwich is $2\theta$. This is the convention of *Exponential Polar Decomposition of Quaternions*. The biquaternion article writes its rotor as $\exp(\frac{\theta_{\mathrm b}}{2}\vec u_{\mathrm r})$, where $\theta_{\mathrm b}$ is its rotation angle; here $\theta_{\mathrm b}=2\theta$, so its exponent angle is $\theta$. The entries of the two case tables can be set side by side, but the biquaternion table's $\theta$ is the rotation angle, while the $\theta$ here is the exponent angle, half of it.

The quaternion case has no phase $\alpha$, no rapidity $\psi$ and no Hermitian factor: the modulus is a positive real and the unit factor is a single rotor. Errors are the largest modulus of a coefficient difference and are computed in double precision; a displayed zero is exact in that precision, and displayed decimals are rounded.

**The plan.** The method is stated once (§*The Method*). The eight cases follow (§*The Eight Cases*), each with its coordinates, its polar data and its check. The boundary is treated separately (§*The Real Axis Family*). The summary collects the results in four tables, reads the patterns across the cases, and compares the quaternion and biquaternion architectures (§*Summary*).

## The Method

### The Coordinates

For $\tilde q=q_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ the four coordinates are the real numbers $q_t,q_x,q_y,q_z$. The modulus is the positive square root

$$
r=\sqrt{q_t^2+q_x^2+q_y^2+q_z^2},
$$

and the unit factor is

$$
\tilde u_{\mathrm r}=\frac{\tilde q}{r}.
$$

The radicand is positive for every nonzero quaternion, so there is no branch choice and no null cone. The element lies on the unit sphere exactly when $r=1$. The four real dimensions split as $1+3$: one for the scale and three for the sphere $S^3$ of unit factors.

The biquaternion modulus is the principal square root of the complex number $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ and carries a phase $\alpha$; here the radicand is a positive real, so the modulus is a positive real and the phase is absent. This is the first structural difference between the two articles.

### The Unit Factor

The unit factor is written

$$
\tilde u_{\mathrm r}=\cos\theta+\vec n\sin\theta,
\qquad
\theta=\arccos\frac{q_t}{r}\in[0,\pi],
$$

with the axis

$$
\vec n=\frac{\vec q}{\sqrt{\langle\vec q\rangle_{\natural}}}
$$

when $\vec q\neq0$. The unit factor is a rotor: it lies on $S^3$, and its sandwich rotates by $2\theta$ about $\vec n$.

There is no Hermitian factor to split off. In the biquaternion case the unit factor factors as $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, a Hermitian positive factor and a unitary factor, with two angles and two axes. Here the Hermitian factor is the identity and the unitary factor is the whole unit factor. The two objects of the decomposition are the scale $r$ and the rotor $\tilde u_{\mathrm r}$; the axis is a coordinate of the rotor, not a third factor.

| object | formula | range |
|---|---|---|
| scale | $r=\sqrt{\langle\tilde q\rangle_{\natural}}$ | $(0,\infty)$ |
| rotor $\tilde u_{\mathrm r}$ | $\cos\theta+\vec n\sin\theta$ | $S^3$ |
| axis $\vec n$ | $\vec q/\sqrt{\langle\vec q\rangle_{\natural}}$ | $S^2$, undefined at $\vec q=0$ |

The angle is defined modulo $2\pi$ by the exponential, but the principal chart uses $\theta\in[0,\pi)$. On that chart the rotation angle $2\theta$ runs over $[0,2\pi)$.

### The Component Form

With

$$
c=\cos\theta,
\qquad
s=\sin\theta,
$$

the element is

$$
\tilde q=r\bigl(c\,e_t+s\,\vec n\bigr).
$$

This is the two-term form: the scalar term and the axis term. The biquaternion component form has four terms, the scalar term, the boost axis, the rotor axis and the cross term, because it carries two axes. A single quaternion has one axis, so the cross term has no room to appear.

The cross term appears when two elements are multiplied. For two rotors $\tilde u_j=c_j+s_j\vec n_j$, with $c_j=\cos\theta_j$ and $s_j=\sin\theta_j$, $j=1,2$, the product is

$$
\tilde u_1\tilde u_2
=\bigl(c_1c_2-s_1s_2\,\vec n_1\cdot\vec n_2\bigr)e_t
+c_1s_2\,\vec n_2+s_1c_2\,\vec n_1
+s_1s_2\,\vec n_1\times\vec n_2 .
$$

The four terms are the scalar term corrected by the angle between the axes, the two axis terms, and the cross term. The cross term is present exactly when both sines $s_1,s_2$ are nonzero, that is when both exponent angles lie strictly between $0$ and $\pi$, and the axes are neither parallel nor antiparallel. It is the term that the sum of the exponents cannot produce in general, because the sum contains only the two axes and their linear combinations. It is the quaternion analogue of the biquaternion cross term, with the sines of two rotors instead of a boost and a rotor.

### The Logarithms and the Defect

The exponent read from the polar data is

$$
\tilde q_{\log}=\ln r+\theta\vec n,
\qquad
\tilde q=\exp(\tilde q_{\log}).
$$

The **principal logarithm** is this exponent on the principal cylinder $\sqrt{\langle\vec v\rangle_{\natural}}<\pi$:

$$ \boxed{\; \log\tilde q=\ln\sqrt{\langle\tilde q\rangle_{\natural}}
+\arccos\frac{q_t}{\sqrt{\langle\tilde q\rangle_{\natural}}}\,
\frac{\vec q}{\sqrt{\langle\vec q\rangle_{\natural}}},
\qquad
\tilde q\notin(-\infty,0] \;} ,$$

with the second term read as $0$ when $\vec q=0$.

Off the real axis the general logarithms are $\log\tilde q+2\pi k\vec n$, $k\in\mathbb{Z}$. On the positive real axis they are $\ln r+2\pi k\vec n$ with $k\ge0$ and $\vec n\in S^2$, the value $k=0$ giving the principal exponent $\ln r$. On the negative real axis they are $\ln r+(2k+1)\pi\vec n$ with $k\ge0$ and $\vec n\in S^2$; none has vector length below $\pi$, so there is no principal exponent.

The **formal exponent** of a factorized word is the sum of the exponents of its factors; for a single element it is the polar exponent $\tilde q_{\log}$.

For an element $\tilde q$ and a candidate exponent $\tilde h$, the **defect** is the largest modulus of a coefficient difference,

$$
D(\tilde h)=\max_{\mu\in\{t,x,y,z\}}
\bigl\lvert(\exp\tilde h)_\mu-\tilde q_\mu\bigr\rvert .
$$

For a single element the defect of its formal exponent is zero in exact arithmetic: the scalar logarithm is central and there is only one axis. The biquaternion case differs because even a single element can carry two noncommuting logarithms. A nonzero defect appears when two elements are multiplied, and cases 6 and 7 compute two examples.

The defect of a **product** need not be zero. The exponential is not a homomorphism, and the first obstruction is the commutator. For two exponents $\tilde h_1,\tilde h_2$,

$$
\log\bigl(\exp(\tilde h_1)\exp(\tilde h_2)\bigr)
=\tilde h_1+\tilde h_2+\tfrac12[\tilde h_1,\tilde h_2]+\cdots .
$$

The scale part is central and always adds; the failure is in the rotor. If the axes are parallel or antiparallel, or one of the angles vanishes, the exponents commute and the sum is a logarithm, up to the branch. This is the quaternion analogue of the biquaternion parallel-axis case. The orthogonal-axis and non-parallel-axis products are cases 6 and 7; their defects are $1$ and $1/\sqrt2$.

### The Matrix Picture

The matrix of $\tilde q$ is

$$
\mathsf M(\tilde q)
=q_tI-iq_x\sigma_x-iq_y\sigma_y-iq_z\sigma_z
=\begin{pmatrix}
q_t-iq_z & -iq_x-q_y\\
-iq_x+q_y & q_t+iq_z
\end{pmatrix}.
$$

Its determinant is $r^2$, its eigenvalues are $q_t\pm i\lvert\vec q\rvert$, and both have modulus $r$. The matrix is normal and satisfies $\mathsf M(\tilde q)\mathsf M(\tilde q)^{\dagger}=r^2I$, so its polar decomposition is

$$
\mathsf M(\tilde q)=r\,U,
\qquad
U=\frac{\mathsf M(\tilde q)}{r}\in SU(2).
$$

The positive factor is the scalar matrix $rI$, and the unitary factor is the matrix of the rotor. In the exponential form, with $N=-i\vec n\cdot\vec\sigma$,

$$
N^2=-I,
\qquad
N^{\dagger}=-N,
\qquad
\mathsf M(\tilde q)=\exp\bigl(\ln r\,I+\theta N\bigr)
=r\bigl(\cos\theta\,I+\sin\theta\,N\bigr).
$$

| factor | matrix | determinant | eigenvalues |
|---|---|---|---|
| element | $\mathsf M(\tilde q)$ | $r^2$ | $q_t\pm i\lvert\vec q\rvert$ |
| scale | $rI$ | $r^2$ | $r,r$ |
| rotor | $\mathsf M(\tilde u_{\mathrm r})$ | $1$ | $e^{\pm i\theta}$ |

The two singular values of $\mathsf M(\tilde q)$ are both $r$. In the biquaternion case they are $r e^{\pm\psi/2}$ and the determinant carries the phase; here the rapidity and the phase are absent, and the two scales coincide.

### The Boundary

The quaternion norm is definite, so there is no null cone. Every nonzero quaternion has a modulus and a polar word. The only boundary is the branch cut of the principal logarithm, the open negative real axis $(-\infty,0)$. Away from the origin every point of the cut has a polar word but no principal exponent.

| element | unit factor | logarithms | principal |
|---|---|---|---|
| $r>0$ | $e_t$ | $\ln r+2\pi k\vec n$, $k\ge0$, $\vec n\in S^2$ | $\ln r$ |
| $-r<0$ | $-e_t$ | $\ln r+(2k+1)\pi\vec n$, $k\ge0$, $\vec n\in S^2$ | none |

At $k=0$ the first row is the single value $\ln r$ for every $\vec n$. The exponential has critical spheres $\sqrt{\langle\vec v\rangle_{\natural}}=\pi k$, whose image is the nonzero real axis; the principal cylinder $\sqrt{\langle\vec v\rangle_{\natural}}<\pi$ is the domain of uniqueness. The kernel is the union of the spheres $\sqrt{\langle\vec v\rangle_{\natural}}=2\pi k$, together with the origin; it is not a subgroup. The boundary family is computed in §*The Real Axis Family*.

## The Eight Cases

The first five cases mirror the first five of the biquaternion article: the identity, the two rotors, the pure boost replaced by the pure scale, and the parallel-axis case replaced by a scale and a rotor on one axis. Cases 6 and 7 mirror the biquaternion orthogonal-axis and non-parallel-axis cases: the two axes sit in two factors of a product, and the formal exponent is the sum of their exponents. Case 8 is the generic element, a non-unit with all four coordinates nonzero. The two-axis defect that the biquaternion cases carry inside one element is carried here by the product in cases 6 and 7, because a single quaternion has only one axis.

### Case 1: The Identity

**Coordinates.** For $\tilde q=e_t$,

$$
q_t=1,
\qquad
q_x=q_y=q_z=0,
\qquad
\langle\tilde q\rangle_{\natural}=1.
$$

**Polar data.** The modulus is one and the unit factor is the identity:

$$
r=1,
\qquad
\theta=0,
\qquad
\tilde u_{\mathrm r}=e_t.
$$

The axis is undefined and the rotation angle is zero.

**The word and the check.** The word is

$$
\tilde q=\exp(0)=e_t,
$$

and the principal logarithm is $\log\tilde q=0$, with error $0$. The word is the identity for every choice of the axis. The matrix is $I$, with determinant $1$ and eigenvalues $1$ and $1$.

### Case 2: A Pure Rotor of Rotation Angle Pi

**Coordinates.** For $\tilde q=\vec e_x$,

$$
q_t=0,
\qquad
q_x=1,
\qquad
q_y=q_z=0,
\qquad
\langle\tilde q\rangle_{\natural}=1.
$$

**Polar data.** The modulus is one and the unit factor is half a turn:

$$
r=1,
\qquad
\theta=\frac{\pi}{2},
\qquad
\tilde u_{\mathrm r}=\vec e_x,
\qquad
\vec n=\vec e_x.
$$

The exponent angle is $\pi/2$; the rotation angle is $2\theta=\pi$.

**The word and the check.** The word is

$$
\tilde q=\exp\Bigl(\frac{\pi}{2}\vec e_x\Bigr)
=\cos\frac{\pi}{2}\,e_t+\sin\frac{\pi}{2}\,\vec e_x
=\vec e_x,
$$

and the logarithm is $\log\tilde q=\frac{\pi}{2}\vec e_x$. The error is $6.1\times10^{-17}$. The matrix is $-i\sigma_x$, with determinant $1$ and eigenvalues $\pm i$.

### Case 3: A Pure Rotor of Rotation Angle Pi Over Two

**Coordinates.** For $\tilde q=\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_x$,

$$
q_t=\frac{1}{\sqrt2},
\qquad
q_x=\frac{1}{\sqrt2},
\qquad
q_y=q_z=0,
\qquad
\langle\tilde q\rangle_{\natural}=1.
$$

**Polar data.** The modulus is one and

$$
r=1,
\qquad
\theta=\frac{\pi}{4},
\qquad
\tilde u_{\mathrm r}=\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_x,
\qquad
\vec n=\vec e_x.
$$

The exponent angle is $\pi/4$; the rotation angle is $2\theta=\pi/2$.

**The word and the check.** The word is

$$
\tilde q=\exp\Bigl(\frac{\pi}{4}\vec e_x\Bigr)
=\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_x,
$$

and the logarithm is $\log\tilde q=\frac{\pi}{4}\vec e_x$. The error is $1.1\times10^{-16}$. The matrix is

$$
\mathsf M(\tilde q)=\frac{1}{\sqrt2}
\begin{pmatrix}1&-i\\-i&1\end{pmatrix},
$$

with determinant $1$ and eigenvalues $e^{\pm i\pi/4}$.

### Case 4: A Pure Scale

**Coordinates.** For $\tilde q=2e_t$,

$$
q_t=2,
\qquad
q_x=q_y=q_z=0,
\qquad
\langle\tilde q\rangle_{\natural}=4.
$$

**Polar data.** The modulus is two and the unit factor is the identity:

$$
r=2,
\qquad
\theta=0,
\qquad
\tilde u_{\mathrm r}=e_t.
$$

The axis is undefined and the rotation angle is zero.

**The word and the check.** The word is

$$
\tilde q=\exp(\ln2)=2e_t,
$$

and the logarithm is $\log\tilde q=\ln2$, with error $0$. The matrix is $2I$, with determinant $4$ and eigenvalues $2$ and $2$. This is the degenerate replacement for the biquaternion pure boost: there is no noncompact unit direction, the rotor is the identity, and the axis is undefined.

### Case 5: A Scale and a Rotor on One Axis

**Coordinates.** For $\tilde q=3e_t+4\vec e_x$,

$$
q_t=3,
\qquad
q_x=4,
\qquad
q_y=q_z=0,
\qquad
\langle\tilde q\rangle_{\natural}=9+16=25.
$$

**Polar data.** The modulus is five and

$$
r=5,
\qquad
\theta=\arccos\frac35=0.9272952180,
\qquad
\tilde u_{\mathrm r}=\frac{3e_t+4\vec e_x}{5},
\qquad
\vec n=\vec e_x.
$$

The rotation angle is $2\theta=1.8545904360$.

**The word and the check.** The word is

$$ \boxed{\; \tilde q=\exp\Bigl(\ln5+\arccos\frac35\,\vec e_x\Bigr)
=3e_t+4\vec e_x \;} ,$$

and the logarithm is

$$
\log\tilde q=1.6094379124+0.9272952180\,\vec e_x,
$$

with error $8.9\times10^{-16}$. The matrix is

$$
\mathsf M(\tilde q)=\begin{pmatrix}3&-4i\\-4i&3\end{pmatrix},
$$

with determinant $25$ and eigenvalues $3\pm4i$. The scale is central, so the two factors amalgamate without a defect; the exponent is the true logarithm.

### Case 6: Orthogonal Axes

**Coordinates.** For $\tilde q=\vec e_z=\vec e_x\vec e_y$,

$$
q_t=0,
\qquad
q_x=q_y=0,
\qquad
q_z=1,
\qquad
\langle\tilde q\rangle_{\natural}=1.
$$

**Polar data.** The modulus is one and

$$
r=1,
\qquad
\theta=\frac{\pi}{2},
\qquad
\tilde u_{\mathrm r}=\vec e_z,
\qquad
\vec n=\vec e_z.
$$

The rotation angle is $2\theta=\pi$.

**The word and the check.** The word is the product of two rotors of exponent angle $\pi/2$ about orthogonal axes,

$$
\tilde q=\exp\Bigl(\frac{\pi}{2}\vec e_x\Bigr)\exp\Bigl(\frac{\pi}{2}\vec e_y\Bigr)
=\vec e_x\vec e_y
=\vec e_z .
$$

The formal exponent is the sum $\frac{\pi}{2}(\vec e_x+\vec e_y)$, and

$$
\exp\Bigl(\frac{\pi}{2}(\vec e_x+\vec e_y)\Bigr)
=\cos\frac{\pi}{\sqrt2}
+\frac{\vec e_x+\vec e_y}{\sqrt2}\sin\frac{\pi}{\sqrt2}
=-0.6056998671+0.5626400586\,(\vec e_x+\vec e_y),
$$

which misses $\vec e_z$ by $1$ in the largest coefficient. The defect is $D\bigl(\frac{\pi}{2}(\vec e_x+\vec e_y)\bigr)=1$. The true polar word is the single exponential

$$
\tilde q=\exp\Bigl(\frac{\pi}{2}\vec e_z\Bigr)=\vec e_z,
$$

with logarithm $\log\tilde q=\frac{\pi}{2}\vec e_z$ and error $6.1\times10^{-17}$. The matrix is

$$
\mathsf M(\tilde q)=-i\sigma_z=\begin{pmatrix}-i&0\\0&i\end{pmatrix},
$$

with determinant $1$ and eigenvalues $\pm i$. This is the quaternion analogue of the biquaternion orthogonal-axis case: the two axes are orthogonal, the formal exponent misses the cross term, and the defect is exactly $1$. The biquaternion counterpart is unipotent; here the definite norm excludes a nonzero null vector, so the product is a pure rotor. The defect is still the cross term of the two axes.

### Case 7: Non-Parallel Axes

**Coordinates.** For $\tilde q=\frac{-\vec e_t+\vec e_z}{\sqrt2}$,

$$
q_t=-\frac{1}{\sqrt2},
\qquad
q_x=q_y=0,
\qquad
q_z=\frac{1}{\sqrt2},
\qquad
\langle\tilde q\rangle_{\natural}=\frac12+\frac12=1.
$$

**Polar data.** The modulus is one and

$$
r=1,
\qquad
\theta=\arccos\Bigl(-\frac{1}{\sqrt2}\Bigr)=\frac{3\pi}{4}=2.3561944902,
\qquad
\tilde u_{\mathrm r}=\frac{-\vec e_t+\vec e_z}{\sqrt2},
\qquad
\vec n=\vec e_z.
$$

The rotation angle is $2\theta=3\pi/2$.

**The word and the check.** The word is the product of two rotors of exponent angle $\pi/2$ about axes at $45^\circ$,

$$ \boxed{\; \tilde q=\exp\Bigl(\frac{\pi}{2}\vec e_x\Bigr)
\exp\Bigl(\frac{\pi}{2}\frac{\vec e_x+\vec e_y}{\sqrt2}\Bigr)
=\vec e_x\frac{\vec e_x+\vec e_y}{\sqrt2}
=\frac{-\vec e_t+\vec e_z}{\sqrt2} \;} .$$

The formal exponent is the sum

$$
\tilde h=\frac{\pi}{2}\vec e_x+\frac{\pi}{2}\frac{\vec e_x+\vec e_y}{\sqrt2},
$$

and

$$
\exp\tilde h
=-0.9715421580+0.2188362994\,\vec e_x+0.0906449631\,\vec e_y,
$$

which misses the product by $1/\sqrt2=0.7071067812$ in the largest coefficient. The defect is $D(\tilde h)=1/\sqrt2$. The true polar word is the single exponential

$$
\tilde q=\exp\Bigl(\frac{3\pi}{4}\vec e_z\Bigr)=\frac{-\vec e_t+\vec e_z}{\sqrt2},
$$

with logarithm $\log\tilde q=\frac{3\pi}{4}\vec e_z$ and error $1.1\times10^{-16}$. The matrix is

$$
\mathsf M(\tilde q)=\begin{pmatrix}
\frac{-1-i}{\sqrt2}&0\\
0&\frac{-1+i}{\sqrt2}
\end{pmatrix},
$$

with determinant $1$ and eigenvalues $e^{\pm i3\pi/4}$. The scalar is negative, the angle is $3\pi/4<\pi$, and the principal logarithm exists. This is the quaternion analogue of the biquaternion non-parallel-axis case: the cross term is the defect, and the negative scalar is the scalar part of the product, not a point on the branch cut.

### Case 8: A Generic Element

**Coordinates.** For $\tilde q=e_t+2\vec e_x+3\vec e_y+4\vec e_z$,

$$
q_t=1,
\qquad
q_x=2,
\qquad
q_y=3,
\qquad
q_z=4,
\qquad
\langle\tilde q\rangle_{\natural}=1+4+9+16=30.
$$

**Polar data.** The modulus and angle are

$$
r=\sqrt{30}=5.4772255751,
\qquad
\theta=\arccos\frac{1}{\sqrt{30}}=1.3871923165,
$$

and the axis is

$$
\vec n=\frac{2\vec e_x+3\vec e_y+4\vec e_z}{\sqrt{29}}
=0.3713906764\,\vec e_x+0.5570860145\,\vec e_y+0.7427813527\,\vec e_z .
$$

The unit factor is

$$
\tilde u_{\mathrm r}=\frac{e_t+2\vec e_x+3\vec e_y+4\vec e_z}{\sqrt{30}},
$$

and the rotation angle is $2\theta=2.7743846330$.

**The word and the check.** The exponent is

$$
\log\tilde q=1.7005986908+0.5151902927\,\vec e_x
+0.7727854390\,\vec e_y+1.0303805853\,\vec e_z,
$$

and its exponential is the element, with error $1.1\times10^{-15}$. The formal exponent is the true logarithm, so the defect is zero. The matrix has determinant $30$ and eigenvalues $1\pm i\sqrt{29}$; both have modulus $\sqrt{30}$. This is the generic case: all four coordinates are nonzero and the axis has all three components.

## The Real Axis Family

The biquaternion article follows its cases with the null cone, where the modulus vanishes and no polar word exists. The quaternion norm is definite, so there is no null cone. The corresponding boundary is the branch cut of the principal logarithm, the open negative real axis. On it the polar word exists but the principal exponent does not.

The standard family is

$$
\tilde q(\delta)=2\cos(\pi-\delta)\,e_t+2\sin(\pi-\delta)\,\vec e_x,
\qquad
0\le\delta<\pi .
$$

Every member has modulus $2$ and norm $4$. For $\delta>0$ the element is not on the negative real axis, the axis is $\vec e_x$, and the principal exponent is

$$
\log\tilde q(\delta)=\ln2+(\pi-\delta)\vec e_x .
$$

At $\delta=0$ the element is $-2e_t$, the angle is $\pi$, the axis is free, and there is no principal exponent. The table gives the approach.

| $\delta$ | $q_t$ | $q_x$ | $r$ | $\theta$ |
|---|---|---|---|---|
| $0.5$ | $-1.7551651238$ | $0.9588510772$ | $2$ | $2.6415926536$ |
| $0.1$ | $-1.9900083306$ | $0.1996668333$ | $2$ | $3.0415926536$ |
| $0.01$ | $-1.9999000008$ | $0.0199996667$ | $2$ | $3.1315926536$ |
| $0.001$ | $-1.9999990000$ | $0.0019999997$ | $2$ | $3.1405926536$ |
| $0$ | $-2$ | $0$ | $2$ | $\pi$ |

The modulus stays fixed and the vector part tends to zero. This is the sharpest contrast with the biquaternion null-cone family, where the modulus tends to zero and the rapidity diverges; here the modulus stays fixed and only the axis and the principal exponent degenerate.

Every unit pure quaternion gives a logarithm of $-2e_t$:

$$
\log(-2e_t)=\ln2+(2k+1)\pi\vec n,
\qquad
k\ge0,\quad \vec n\in S^2 .
$$

The table records three choices with $k=0$; each reconstructs the element.

| axis $\vec n$ | logarithm | error |
|---|---|---|
| $\vec e_x$ | $\ln2+\pi\vec e_x$ | $2.4\times10^{-16}$ |
| $\vec e_y$ | $\ln2+\pi\vec e_y$ | $2.4\times10^{-16}$ |
| $\frac{\vec e_x+\vec e_y}{\sqrt2}$ | $\ln2+\frac{\pi}{\sqrt2}(\vec e_x+\vec e_y)$ | $1.7\times10^{-16}$ |

The kernel is the union of the spheres $\sqrt{\langle\vec v\rangle_{\natural}}=2\pi k$, together with the origin. The elements $2\pi\vec e_x$, $2\pi\vec e_y$ and $2\pi(\vec e_x+\vec e_y)/\sqrt2$ lie in the kernel and exponentiate to $e_t$ to $2.4\times10^{-16}$, $2.4\times10^{-16}$ and $1.7\times10^{-16}$. The sum $2\pi(\vec e_x+\vec e_y)$ does not lie in the kernel; its exponential is

$$
\exp\bigl(2\pi(\vec e_x+\vec e_y)\bigr)
=-0.8582161857+0.3629497063\,(\vec e_x+\vec e_y),
$$

which is not $e_t$. The kernel is not a subgroup. The fibre over a non-real element is a line, the fibre over the positive real axis is the translate $\ln r+\ker\exp$, and the fibre over the open negative real axis is a union of spheres.

## Summary

### Main Results

| Case | $\tilde q$ | $q_t$ | $q_x^2+q_y^2+q_z^2$ | $r$ | $\theta$ | $\vec n$ | rotation $2\theta$ |
|---|---|---|---|---|---|---|---|
| $1$ | $e_t$ | $1$ | $0$ | $1$ | $0$ | — | $0$ |
| $2$ | $\vec e_x$ | $0$ | $1$ | $1$ | $\pi/2$ | $\vec e_x$ | $\pi$ |
| $3$ | $\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_x$ | $\frac{1}{\sqrt2}$ | $\frac12$ | $1$ | $\pi/4$ | $\vec e_x$ | $\pi/2$ |
| $4$ | $2e_t$ | $2$ | $0$ | $2$ | $0$ | — | $0$ |
| $5$ | $3e_t+4\vec e_x$ | $3$ | $16$ | $5$ | $\arccos\frac35$ | $\vec e_x$ | $2\arccos\frac35$ |
| $6$ | $\vec e_z$ | $0$ | $1$ | $1$ | $\pi/2$ | $\vec e_z$ | $\pi$ |
| $7$ | $\frac{-\vec e_t+\vec e_z}{\sqrt2}$ | $-\frac{1}{\sqrt2}$ | $\frac12$ | $1$ | $3\pi/4$ | $\vec e_z$ | $3\pi/2$ |
| $8$ | $e_t+2\vec e_x+3\vec e_y+4\vec e_z$ | $1$ | $29$ | $\sqrt{30}$ | $\arccos\frac{1}{\sqrt{30}}$ | $\frac{2\vec e_x+3\vec e_y+4\vec e_z}{\sqrt{29}}$ | $2\arccos\frac{1}{\sqrt{30}}$ |

### The Factors

| Case | scale $r$ | rotor $\tilde u_{\mathrm r}$ | axis $\vec n$ | rotation $2\theta$ |
|---|---|---|---|---|
| $1$ | $1$ | $e_t$ | — | $0$ |
| $2$ | $1$ | $\vec e_x$ | $\vec e_x$ | $\pi$ |
| $3$ | $1$ | $\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_x$ | $\vec e_x$ | $\pi/2$ |
| $4$ | $2$ | $e_t$ | — | $0$ |
| $5$ | $5$ | $\frac{3e_t+4\vec e_x}{5}$ | $\vec e_x$ | $1.8545904360$ |
| $6$ | $1$ | $\vec e_z$ | $\vec e_z$ | $\pi$ |
| $7$ | $1$ | $\frac{-\vec e_t+\vec e_z}{\sqrt2}$ | $\vec e_z$ | $3\pi/2$ |
| $8$ | $\sqrt{30}$ | $\frac{e_t+2\vec e_x+3\vec e_y+4\vec e_z}{\sqrt{30}}$ | $\frac{2\vec e_x+3\vec e_y+4\vec e_z}{\sqrt{29}}$ | $2.7743846330$ |

### The Reconstruction Table

The **word** is the factorized exponential constructed in the case: one exponential in cases 1 to 5 and 8, and the product of the two factor exponentials in cases 6 and 7. The **formal exponent** is the sum of the factor exponents. The **defect** is the largest coefficient difference between the exponential of the formal exponent and the element in exact arithmetic. The word reconstructs the element; the reconstruction error of each case is displayed in the case. The defect is zero exactly when the formal exponent is a true logarithm.

| Case | Word | Defect |
|---|---|---|
| $1$ | $e_t$ | $0$ |
| $2$ | $\exp\bigl(\frac{\pi}{2}\vec e_x\bigr)$ | $0$ |
| $3$ | $\exp\bigl(\frac{\pi}{4}\vec e_x\bigr)$ | $0$ |
| $4$ | $\exp(\ln2)$ | $0$ |
| $5$ | $\exp\bigl(\ln5+\arccos\frac35\,\vec e_x\bigr)$ | $0$ |
| $6$ | $\exp\bigl(\frac{\pi}{2}\vec e_x\bigr)\exp\bigl(\frac{\pi}{2}\vec e_y\bigr)$ | $1$ |
| $7$ | $\exp\bigl(\frac{\pi}{2}\vec e_x\bigr)\exp\bigl(\frac{\pi}{2}\frac{\vec e_x+\vec e_y}{\sqrt2}\bigr)$ | $1/\sqrt2$ |
| $8$ | $\exp\bigl(\ln\sqrt{30}+\arccos\frac{1}{\sqrt{30}}\,\vec n\bigr)$ | $0$ |

### The Logarithms

| Case | $\log\tilde q$ | Error |
|---|---|---|
| $1$ | $0$ | $0$ |
| $2$ | $\frac{\pi}{2}\vec e_x$ | $6.1\times10^{-17}$ |
| $3$ | $\frac{\pi}{4}\vec e_x$ | $1.1\times10^{-16}$ |
| $4$ | $\ln2$ | $0$ |
| $5$ | $\ln5+\arccos\frac35\,\vec e_x$ | $8.9\times10^{-16}$ |
| $6$ | $\frac{\pi}{2}\vec e_z$ | $6.1\times10^{-17}$ |
| $7$ | $\frac{3\pi}{4}\vec e_z$ | $1.1\times10^{-16}$ |
| $8$ | $\ln\sqrt{30}+\arccos\frac{1}{\sqrt{30}}\,\vec n$ | $1.1\times10^{-15}$ |

Off the real axis the other logarithms are obtained by adding $2\pi k\vec n$. On the positive real axis they are $\ln r+2\pi k\vec n$ with $k\ge0$ and $\vec n\in S^2$; on the negative real axis they are $\ln r+(2k+1)\pi\vec n$ with $k\ge0$ and $\vec n\in S^2$, and none is principal.

### What the Cases Show

- The identity and the pure scale show the angle-zero end: the rotor is the identity and the axis is undefined. The two rotors show pure rotation: the modulus is one and the scale is absent. At the angle-$\pi$ end the axis is free; the boundary family approaches it. The quaternion case has no phase and no rapidity; the pure scale is the whole non-rotating part.
- Cases 2, 3 and 5 share the axis $\vec e_x$ and differ in scale and angle. Cases 6 and 7 share the axis $\vec e_z$. Case 8 has the generic axis. The exponent angle is half the rotation angle, so the rotation columns of the table are twice the angle columns.
- Case 5 is the one-axis case. The scale is central, the two factors commute, the word is one exponential, and the formal exponent is the true logarithm. The defect is zero.
- Case 6 is the orthogonal-axis product. The word is $\vec e_x\vec e_y=\vec e_z$; the polar data give the axis $\vec e_z$ and the exponent $\frac{\pi}{2}\vec e_z$. The formal exponent $\frac{\pi}{2}(\vec e_x+\vec e_y)$ misses the element by $1$, so the defect is $1$. The true polar word is one exponential.
- Case 7 is the non-parallel product. The word is a product of rotors at $45^\circ$, and the element has the negative scalar $-1/\sqrt2$. The polar data give the axis $\vec e_z$ and the exponent $\frac{3\pi}{4}\vec e_z$; the formal exponent misses the element by $1/\sqrt2$. The angle is $3\pi/4<\pi$, so the principal logarithm exists. The negative scalar is the scalar part of the product, not a point on the branch cut.
- Case 8 is the generic non-unit. The modulus is $\sqrt{30}$, all four coordinates are nonzero, and the axis has all three components. The formal exponent is the true logarithm, so the defect is zero.
- The defect is zero when the word is a single factor, in cases 1 to 5 and 8; it is nonzero when two rotors about different axes are multiplied, in cases 6 and 7. The cross term is the defect. This is how the quaternion article mirrors the biquaternion defect without a second axis inside one element.
- The open negative real axis is the branch cut. The polar word exists there, but the principal exponent does not, and the axis is free. The general logarithms form the spheres of radii $(2k+1)\pi$ at scalar height $\ln r$; the first is the sphere of radius $\pi$. The kernel is a union of spheres and is not a subgroup.

### The Two Algebras

The two architectures compare as follows.

| feature | biquaternion case | quaternion case |
|---|---|---|
| coordinates | $Q_t,Q_x,Q_y,Q_z\in\mathbb{C}$ | $q_t,q_x,q_y,q_z\in\mathbb{R}$ |
| modulus | $re^{i\alpha}$, principal square root | $r>0$ |
| unit factor | $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, Hermitian times unitary | $\tilde u_{\mathrm r}$, a rotor |
| angles and axes | $\psi,\theta_{\mathrm b}$; $\vec u_{\mathrm b},\vec u_{\mathrm r}$ | $\theta$; $\vec n$ |
| polar word | $re^{i\alpha}\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\exp(\frac{\theta_{\mathrm b}}{2}\vec u_{\mathrm r})$ | $\exp(\ln r+\theta\vec n)$ |
| defect of one element's polar word | the cross term when the axes are non-parallel | zero |
| boundary | the null cone, where no polar word exists | the open negative real axis, where no principal exponent exists |
| matrix scales | $re^{\pm\psi/2}$ | $r,r$ |

The quaternion case is the definite compact companion of the biquaternion case: the phase, the rapidity, the Hermitian factor and the second axis are absent, and the four-factor word of the biquaternion case collapses to one exponential for a single element. What survives is the noncommutativity, and it appears in the product of two elements rather than in the decomposition of one.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra, basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ |
| $\tilde q=q_te_t+\vec q$ | a quaternion, $q_t$ its scalar part, $\vec q$ its pure part |
| $q_t,q_x,q_y,q_z$ | the four real coordinates |
| $\tilde q^{\natural}=q_te_t-\vec q$ | the quaternion conjugate |
| $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}=q_t^2+q_x^2+q_y^2+q_z^2$ | the quaternion norm |
| $r=\sqrt{\langle\tilde q\rangle_{\natural}}$ | the modulus |
| $\theta=\arccos(q_t/r)\in[0,\pi]$ | the exponent angle, half the rotation angle |
| $\vec n=\vec q/\sqrt{\langle\vec q\rangle_{\natural}}$ | the axis, undefined when $\vec q=0$ |
| $\tilde u_{\mathrm r}=\cos\theta+\vec n\sin\theta$ | the rotor, the unit factor |
| $2\theta$ | the rotation angle of the sandwich |
| $\tilde q_{\log}=\ln r+\theta\vec n$ | the exponent |
| $\log\tilde q$ | the principal logarithm on $\mathbb{H}\setminus(-\infty,0]$ |
| $D(\tilde h)$ | the defect of a candidate exponent |
| $\ker\exp=\{0\}\cup\bigcup_{k\ge1}\{\vec v:\langle\vec v\rangle_{\natural}=(2\pi k)^2\}$ | the kernel, not a subgroup |
| $\mathsf M(\tilde q)=q_tI-iq_x\sigma_x-iq_y\sigma_y-iq_z\sigma_z$ | the matrix of the element |
| $N=-i\vec n\cdot\vec\sigma$ | the skew-Hermitian matrix of the axis |
| $c=\cos\theta$, $s=\sin\theta$ | the half-angle cosine and sine |

## Further Reading

- [Exponential Polar Decomposition of Quaternions](exponential-polar-decomposition-of-quaternions.html), for the decomposition, the logarithm, the principal branch, the kernel and the matrix picture.
- [Quaternion Special Functions](quaternion-special-functions.html), for the exponential and the logarithm.
- [Modulus–Unit Polar Decomposition of Quaternions](modulus-unit-polar-decomposition-of-quaternions.html), for the modulus and the unit factor.
- [Worked Examples of Exponential Polar Decomposition of Biquaternions](worked-examples-of-exponential-polar-decomposition-of-biquaternions.html), for the noncommutative four-dimensional companion with two axes.
- [Worked Examples of Exponential Polar Decomposition of Reduced Biquaternions](worked-examples-of-exponential-polar-decomposition-of-reduced-biquaternions.html), for the commutative four-dimensional companion.
- [Worked Examples of Exponential Polar Decomposition of Split-Complex Numbers](worked-examples-of-exponential-polar-decomposition-of-split-complex-numbers.html), for the two-dimensional indefinite companion.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation.
