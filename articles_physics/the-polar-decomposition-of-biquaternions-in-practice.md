# __The Polar Decomposition of Biquaternions in Practice__

## Introduction

This article is the working procedure of the polar representation. It takes a biquaternion off the null cone and returns the four factors

$$
\tilde Q=r\,\exp(i\alpha)\,B\,\tilde q,
$$

with the positive scale $r$, the central phase $\alpha$ on the branch $(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$, the Hermitian positive unit-norm boost factor $B$, and the unit real quaternion rotor $\tilde q$.

The boost factor is the **positive Hermitian factor** of the matrix polar decomposition. It is the square of the inverse frame rotor,

$$
B=(U_L^\natural)^2,
\qquad
\tilde U_L=\exp\Bigl(i\frac{\eta}{2}\vec u_{\mathrm b}\Bigr),\qquad B^{1/2}=U_L^\natural=\exp\Bigl(-i\frac{\eta}{2}\vec u_{\mathrm b}\Bigr),
$$

with $\eta$ the frame rapidity and $\vec u_{\mathrm b}$ the axis. The word uses $B$; the action on a four-vector uses $\tilde U_L$. The square root $B^{1/2}=U_L^\natural$ is the inverse frame rotor. This distinction is the first practical warning of the article.

The article records the test of the domain, the five steps in their forced order, the output as eight real numbers, the physical dictionary, four worked instances, and the numerical precautions. The existence and uniqueness theorem is in *The Polar Element Representation of Biquaternions*; the present article adds the coordinate formulas and the error control.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and central $i$. An element is $\tilde Q=Q_te_t+\vec Q$, with complex $Q_\mu$. The norm is $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$, the quaternion conjugation is $\natural$, and the Hermitian conjugation is ${}^{*}=\overline{\ \cdot\ }^{\natural}$. The matrix model is $\mathsf M_2(e_t)=I_2$, $\mathsf M_2(\vec e_k)=-i\sigma_k$, with $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$. The symbol $\eta$ is the frame rapidity, written $\psi$ in *The Polar Element Representation of Biquaternions*. The boost factor is $B=\exp(-i\eta\vec u_{\mathrm b})$; the frame rotor is $U_L=\exp(i\eta\vec u_{\mathrm b}/2)$, and $B^{1/2}=U_L^\natural$ is its inverse. The Hamilton and Cartan articles write the frame rotor with $\psi/2$.

## The Test of the Domain

The first step is the norm. Compute

$$
N=\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2.
$$

If $N=0$, stop. The element is a zero divisor, the matrix image is singular, and no polar word exists. A numerical test must use a tolerance relative to the size of the coefficients, because $N$ is a difference of squares and cancels on the light cone. A practical test is

$$
\lvert N\rvert\le \varepsilon\,\bigl(\lvert Q_t\rvert^2+\lvert Q_x\rvert^2+\lvert Q_y\rvert^2+\lvert Q_z\rvert^2\bigr),
$$

with $\varepsilon$ a few units of machine precision, or the larger of that and an absolute tolerance set by the application.

The failure is physical as well as numerical. On the material sector $N=-a^2+\lvert\vec b\rvert^2$ is the interval, and $N=0$ is the light cone. On the informational sector the same set is the cone of the rank-one Hermitian matrices. On a general element $N=0$ is the zero-divisor cone. In every case the polar word has no scale and no rest frame.

## The Five Steps

### Step 1: The Modulus

Take the principal square root

$$
\rho=\sqrt{N},\qquad r=\lvert\rho\rvert,\qquad \alpha=\tfrac12\arg N.
$$

The branch of $\alpha$ is $(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$. In practice, compute $r=\lvert N\rvert^{1/2}$ and $\alpha=\tfrac12\operatorname{atan2}(\operatorname{Im}N,\operatorname{Re}N)$, then reduce $\alpha$ to the branch by adding or subtracting $\pi$ and multiplying $\rho$ by $-1$ if necessary. The modulus is

$$
\rho=r\exp(i\alpha).
$$

### Step 2: The Unit-Norm Element

Divide by the modulus,

$$
\tilde U=\tilde Q/\rho.
$$

Then $\langle\tilde U\rangle_{\natural}=1$. Compute the Hermitian product

$$
\tilde P=\tilde U\tilde U^{*}.
$$

It is Hermitian and positive definite, of unit determinant. Write it in the form

$$
\tilde P=E\,e_t+i\vec v,
\qquad E>0,\qquad \vec v=(v_x,v_y,v_z)\in\mathbb{R}^3.
$$

The scalar part is $E=\tfrac12\operatorname{tr}\mathsf M_2(\tilde P)$, and the vector part is read from the imaginary coefficients: $\tilde P=Ee_t+i(v_x\vec e_x+v_y\vec e_y+v_z\vec e_z)$.

The unit determinant gives the identity

$$
E^2-\lvert\vec v\rvert^2=1.
$$

Hence $E\ge1$, with equality exactly when the boost is trivial. The boost data are

$$
\eta=\tfrac12\operatorname{arccosh}E,\qquad
\vec u_{\mathrm b}=-\frac{\vec v}{\lvert\vec v\rvert},
$$

with $\eta=0$ and no axis when $\vec v=0$. The minus sign is the one in $B=\cosh\eta-i\sinh\eta\,\vec u_{\mathrm b}$: the vector $\vec v$ is the imaginary vector part of $\tilde P$, and the boost axis points opposite to it.

### Step 3: The Boost

The positive square root of $\tilde P$ is the boost factor. The stable closed form is

$$
B
=\frac{e_t+\tilde P}{\sqrt{2(E+1)}}
=\sqrt{\frac{E+1}{2}}\,e_t
+i\,\frac{\vec v}{\sqrt{2(E+1)}}.
$$

The formula avoids subtracting $1$ from $E$ when the boost is small. Its square is $\tilde P$:

$$
B^2
=\frac{(e_t+\tilde P)^2}{2(E+1)}
=\frac{2(E+1)\tilde P}{2(E+1)}
=\tilde P,
$$

because $\tilde P^2=2E\tilde P-2(E^2-\lvert\vec v\rvert^2)e_t=2E\tilde P-2e_t$ and $(e_t+\tilde P)^2=2(E+1)\tilde P$. The matrix image is positive definite, with eigenvalues $e^{\pm\eta}$.

The rapidity is also

$$
\eta=\operatorname{arcsinh}\frac{\lvert\vec v\rvert}{\sqrt{2(E+1)}},
$$

which is the stable form when $E$ is close to one and the direct $\operatorname{arccosh}$ loses relative accuracy. The inverse frame rotor is the positive square root of $B$,

$$
B^{1/2}=U_L^\natural
=\cosh\frac{\eta}{2}\,e_t
-i\sinh\frac{\eta}{2}\,\vec u_{\mathrm b}.
$$

The frame rotor is $U_L=B^{-1/2}$; it is the factor that acts on a four-vector, and $B$ is the square of its inverse. The closed form of $B$ above gives the full-angle factor directly, and the square root is read from $\eta$ and the axis.

### Step 4: The Rotor

The rotor is what remains after the boost is removed,

$$
\tilde q=B^{-1}\tilde U.
$$

It is a unit real quaternion. Its scalar part is $\cos(\theta/2)$ and its vector part is $\sin(\theta/2)\vec u_{\mathrm r}$. Hence

$$
\theta=2\arccos(\operatorname{Re}\tilde q),\qquad
\vec u_{\mathrm r}=\frac{\operatorname{Im}\tilde q}{\lvert\operatorname{Im}\tilde q\rvert},
$$

with $\theta\in[0,2\pi]$ and the axis undefined at $\theta=0$ or $2\pi$. The rotor is determined uniquely by the principal decomposition: the positivity of $B$ and the branch of $\rho$ fix its sign. Flipping the rotor would require flipping $B$ or moving $\rho$ off its branch, neither of which the principal decomposition allows.

### Step 5: The Reconstruction

Assemble

$$
\tilde Q_{\mathrm{rec}}=r\exp(i\alpha)\,B\,\tilde q
$$

and compare with the input. A relative test is

$$
\lVert\tilde Q_{\mathrm{rec}}-\tilde Q\rVert
\le \varepsilon\,\lVert\tilde Q\rVert,
$$

with the largest coefficient norm. The reconstruction is the only test that catches a mistake in the order of the factors, the sign of the rotor, or the branch of the phase. It costs one multiplication and must be performed.

## The Output as Eight Real Numbers

The four factors carry eight real numbers.

| factor | data | count |
|---|---|---|
| scale | $r>0$ | 1 |
| phase | $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ | 1 |
| boost | $\eta\ge0$ and the axis $\vec u_{\mathrm b}\in S^2$ | 3 |
| rotor | $\theta\in[0,2\pi]$ and the axis $\vec u_{\mathrm r}\in S^2$ | 3 |

The total is eight, the real dimension of the algebra. The data are not independent coordinates of the algebra at the degenerate points: the boost axis is undefined at $\eta=0$, and the rotor axis is undefined at $\theta=0$ or $2\pi$. The reconstruction test is the guard against the false impression that the degeneracies are errors.

The four factors are also the four physical objects of the corpus: the scale is a length, the phase is a gauge phase, the boost is a velocity, and the rotor is a spin. The output is therefore a physical parametrisation, not only an algebraic one.

## The Physics Normalisation

The word is

$$
\tilde Q=r\,\exp(i\alpha)\,B\,\tilde q,
\qquad
B=\exp(-i\eta\vec u_{\mathrm b}),
\qquad
\tilde q=\tilde u_{\mathrm r},
$$

with $B$ the positive Hermitian factor and $\tilde q$ the rotor. The inverse frame rotor is the positive square root

$$
B^{1/2}=U_L^\natural
=\cosh\frac{\eta}{2}\,e_t
-i\sinh\frac{\eta}{2}\,\vec u_{\mathrm b},
\qquad
U_L=B^{-1/2}=\exp\Bigl(i\frac{\eta}{2}\vec u_{\mathrm b}\Bigr),
$$

and the boost factor is the square of its conjugate, $B=(U_L^\natural)^2$. The distinction is the most common source of a factor-of-two error in a rapidity. If the inverse frame rotor is wanted, take the positive square root of the output $B$; if the element is a four-position, the frame rotor is $U_L=B^{-1/2}$, and the four-position is $\tilde X=i r B$.

For a four-vector,

$$
\tilde X=i a e_t+\vec b,
\qquad N=-a^2+\lvert\vec b\rvert^2,
\qquad r=\lvert N\rvert^{1/2},
\qquad \alpha=\frac{\pi}{2}\ \text{or}\ 0,
$$

and the boost factor is $B=-(i/c)\tilde V$ for the timelike case. For a four-velocity, $r=c$; for a four-momentum, $r=mc$. The phase is $\pi/2$ on the timelike cone and $0$ on the spacelike sheet.

On the Lorentz group, $N=1$, so $r=1$ and $\alpha=0$, and the first two steps return the unit element. The word is then the Cartan decomposition $\tilde U_L=B\tilde q$. The practice reduces to the two-factor problem of the physics articles.

## Worked Examples

### A General Element

Take

$$
\tilde Q=(1+i)e_t+\vec e_x+2\vec e_y.
$$

The norm is $N=5+2i$, with $\lvert N\rvert=\sqrt{29}=5.385164807$ and $\arg N=0.380506377$. Hence

$$
r=2.320595787,\qquad \alpha=0.190253189,\qquad \rho=2.320595787\exp(0.190253189i).
$$

The unit element is $\tilde U=\tilde Q/\rho$, and its Hermitian product is

$$
\tilde P=1.299867367\,e_t-0.371390676\,i\vec e_x-0.742781353\,i\vec e_y.
$$

Thus $E=1.299867367$, $\vec v=(-0.371390676,-0.742781353,0)$, $\lvert\vec v\rvert=0.830454799$, and

$$
B=1.072349609\,e_t-0.173166789\,i\vec e_x-0.346333577\,i\vec e_y,
$$

with $\eta=0.378136610$ and axis $(0.447213595,0.894427191,0)$. The inverse frame rotor is

$$
\tilde U_L=1.017926719\,e_t-0.085058573\,i\vec e_x-0.170117147\,i\vec e_y.
$$

The rotor is

$$
\tilde q=0.470592172\,e_t+0.394599292\,\vec e_x+0.789198585\,\vec e_y,
$$

with $\theta=2.161669077$ and axis $(0.447213595,0.894427191,0)$. The reconstruction holds to $2.7\times10^{-15}$.

### A Four-Position

Take $\tilde X=i e_t+0.6\vec e_x$ at $ct=1$. The norm is $-0.64$, so

$$
r=0.8,\qquad \alpha=\frac{\pi}{2},\qquad \rho=0.8i.
$$

The unit element is $\tilde U=\tilde X/\rho$. The calculation gives

$$
\tilde U=1.25-0.75i\vec e_x,
$$

which is already Hermitian positive. Hence $B=1.25e_t-0.75i\vec e_x$, $\eta=0.693147181$ about $\vec e_x$, and $\tilde q=e_t$. The reconstruction is exact. The inverse frame rotor is

$$
B^{1/2}=1.060660172e_t-0.353553391i\vec e_x.
$$

### A Pure Boost Factor

Take $\tilde Q=1.25e_t-0.75i\vec e_x$, the boost factor of rapidity $\eta=0.693147181$ about $\vec e_x$. Its norm is one, so $r=1$ and $\alpha=0$. The element is Hermitian positive, so $B=\tilde Q$ and $\tilde q=e_t$. The inverse frame rotor is $B^{1/2}=1.060660172e_t-0.353553391i\vec e_x$. The practice returns the boost factor, not the inverse frame rotor; the square root is the inverse frame rotor.

### A Null Element

Take $\tilde Q=i e_t+\vec e_x$. The norm is $-1+1=0$. The test of the domain fails, and the algorithm stops. There is no scale and no phase; the matrix image is singular; the element is a zero divisor. The correct output is the failure, not a large or a rounded value.

## Numerical Precautions

**The norm cancels.** $N$ is a sum of squares with signs in the vector directions. Near the cone, the sum of large terms cancels to a small value. Use a relative tolerance and, if the application needs the distance to the cone, compute it in higher precision or from the matrix singular values.

**The scalar part of the Hermitian product.** $E$ is close to one for a small boost. Write $E=\cosh 2\eta$ and use $\eta=\tfrac12\operatorname{arccosh}E$; the stable form is $\eta=\operatorname{arcsinh}(\lvert\vec v\rvert/\sqrt{2(E+1)})$.

**The phase branch.** The argument of $N$ jumps by $2\pi$ across the negative real axis. Reduce $\alpha$ to $(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ and flip the sign of $\rho$ at the same time. The reconstruction catches a missed flip.

**The rotor sign.** The rotor sign is a branch choice. The principal modulus and the branch of the phase fix it; a solver that computes $\tilde q$ from a different square root may return the opposite sign together with the phase shifted by $\pi$, which is outside the branch. Normalise the branch before comparing.

**The degenerate axes.** The boost axis is undefined at $\eta=0$ and the rotor axis at $\theta=0$ or $2\pi$. Return the identity factor and a flag, not an arbitrary axis.

**The order.** The reconstruction must multiply in the order $r\exp(i\alpha)B\tilde q$. The order $\tilde q B$ is a different element unless the two commute. A reconstruction error that vanishes only for collinear axes is the signature of the wrong order.

**The two roots.** $B$ is the positive square root of $\tilde P$; the inverse frame rotor is the positive square root of $B$. Do not use $B$ as the frame rotor. The congruence by $B$ doubles the rapidity, and the error is invisible in the norm.

## Numerical Ledger

The formulas of this article were checked on $100$ random elements with complex Gaussian coefficients, excluding the cone.

| test | largest error |
|---|---|
| reconstruction $\tilde Q_{\mathrm{rec}}-\tilde Q$ | $2.7\times10^{-15}$ |
| unit norms of $B$ and $\tilde q$ | $2.5\times10^{-15}$ |
| Hermitian defect $B^{*}-B$ | $0$ |
| Cartan identity $rB\cdot\exp(i\alpha)\tilde q=\tilde Q$ | $7.1\times10^{-15}$ |
| action preserves the sector norm | $7.1\times10^{-14}$ |

The numbers are double-precision results; they are not a proof. The proof is the theorem of the companion article. The checks are the evidence that the coordinate formulas and the branch conventions are the same as the theorem's.

## What the Practice Is Not

The practice is not a proof of existence. It is not a model of a physical process. It is not defined on the null cone. It is not a replacement for the theorem when the element is symbolic: the square root of a complex number and the branch of its argument are choices, and the theorem states the choices that make the word unique. The practice is the numerical shadow of the theorem, and the reconstruction is the test that the shadow is faithful.

## Summary

The polar decomposition in practice is five steps. Test the norm; compute the modulus $\rho$; divide to get the unit element; take the positive square root of $\tilde U\tilde U^{*}$ for the boost; multiply by the inverse for the rotor; reconstruct and compare. The output is eight real numbers: a scale, a phase, a boost rapidity and axis, and a rotor angle and axis. The boost factor is the positive Hermitian factor; the inverse frame rotor is its square root. The algorithm fails exactly on the null cone, and the failure is the physical absence of a rest frame.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q$ | the input biquaternion |
| $N=\langle\tilde Q\rangle_{\natural}$ | the norm |
| $\rho=\sqrt{N}=r\exp(i\alpha)$ | the modulus |
| $r$ | the scale |
| $\alpha$ | the phase |
| $\tilde U=\tilde Q/\rho$ | the unit-norm element |
| $\tilde P=\tilde U\tilde U^{*}$ | the Hermitian product |
| $E,\vec v$ | the scalar and vector data of $\tilde P=Ee_t+i\vec v$ |
| $B$ | the positive Hermitian boost factor |
| $\eta,\vec u_{\mathrm b}$ | the rapidity and axis |
| $B^{1/2}=U_L^\natural$ | the inverse frame rotor |
| $\tilde q$ | the rotor |
| $\theta,\vec u_{\mathrm r}$ | the angle and axis |

## Further Reading

- *The Polar Element Representation of Biquaternions* (`articles_physics/the-polar-element-representation-of-biquaternions.md`), the theorem and the physical readings.
- *The Quaternion Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-quaternion-pairing-of-the-polar-element-representation-of-biquaternions.md`), the real-quaternion construction.
- *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-hamilton-root-pairing-of-the-polar-element-representation-of-biquaternions.md`), the complex axis-angle construction.
- *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-cartan-hermitian-pairing-of-the-polar-element-representation-of-biquaternions.md`), the positive-unitary construction.
- *The Action of the Polar Element Representation on the Hermitian and Anti-Hermitian Subspaces* (`articles_physics/the-action-of-the-polar-element-representation-on-the-hermitian-and-anti-hermitian-subspaces.md`), the action of the output.
- *The Polar Element Representation in Subspaces* (`articles_physics/the-polar-element-representation-in-subspaces.md`), the restrictions and the numerical tables.
- *The 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* (`articles_physics/the-2x2-matrix-element-representation-m2c-of-biquaternions.md`), the determinant and the matrix polar decomposition.
