# __Worked Examples of Exponential Polar Decomposition of Biquaternions__

## Introduction

This article computes the exponential polar decomposition of eight biquaternions, one after another. It is the computational companion of *Exponential Polar Decomposition of Biquaternions*. The decomposition, its existence and uniqueness, the Cartan logarithm and the four-factor word are established there and in *Biquaternion Elementary Functions*; the proofs are not repeated.

Each case is read from the four complex coordinates $Q_t,Q_x,Q_y,Q_z$. The modulus, the phase, the rapidity, the rotor angle and the two axes are computed from them by the formulas of §*The Method*, and the word is checked against the reconstruction

$$
\tilde Q=r e^{i\alpha}\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)
\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr).
$$

The eight cases cover the identity, the two pure rotors, the pure boost, the parallel axes, the orthogonal axes, the non-parallel axes and the generic null-vector element.

| Group | Case | What it shows |
|---|---|---|
| Identity | $e_t$ | the trivial word, both axes undefined |
| Pure rotor | $\vec e_x$ | $\theta=\pi$ |
| Pure rotor | $\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_x$ | $\theta=\pi/2$ |
| Pure boost | $\sqrt2\,e_t+i\vec e_x$ | $\psi=2\ln(1+\sqrt2)$ |
| Parallel axes | $\bigl(1-\frac{i}{\sqrt2}\bigr)e_t+\bigl(1+\frac{i}{\sqrt2}\bigr)\vec e_x$ | one exponential for the two factors |
| Orthogonal axes | $e_t+\vec e_y+\frac{i}{\sqrt2}\vec e_x+\frac{i}{\sqrt2}\vec e_z$ | unipotent, the defect is the cross term |
| Non-parallel axes | $\bigl(1-\frac{i}{2}\bigr)e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z$ | the defect is exactly $\tfrac12$ |
| Null vector part | $(1+i)e_t+\vec e_x+i\vec e_y$ | $r\neq1$, $\alpha\neq0$, unipotent unit factor |

$$
\tilde Q\tilde Q^{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2,
$$

written in full throughout. The modulus is the principal square root $\bigl(Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2}$, taken in the branch with non-negative real part and written $r e^{i\alpha}$ with $r>0$ and $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$. The rapidity is $\psi\ge0$, the rotor angle is $\theta\in[0,2\pi]$, and the axes $\vec u_{\mathrm b},\vec u_{\mathrm r}$ are real unit vectors, undefined when the corresponding angle vanishes. Errors are the largest modulus of a coefficient difference and are computed in double precision; a displayed zero is exact in that precision, and displayed decimals are rounded.

**The plan.** The method is stated once (§*The Method*). The eight cases follow (§*The Eight Cases*), each with its coordinates, its polar data, its factors and its check. The boundary is treated separately (§*The Null Cone Family*). The summary collects the results in three tables and reads the patterns across the cases (§*Summary*).

## The Method

### The Coordinates

For $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ the four complex coordinates are $Q_t,Q_x,Q_y,Q_z$. The modulus is the principal square root

$$
r e^{i\alpha}=\bigl(Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2},
\qquad
r=\bigl\lvert Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr\rvert^{1/2},
\qquad
\alpha=\tfrac12\operatorname{Arg}\bigl(Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr),
$$

and the unit factor is

$$
\tilde U=\tilde Q\bigl(Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr)^{-1/2}.
$$

The element is a unit exactly when $Q_t^2+Q_x^2+Q_y^2+Q_z^2\neq0$. The unit factor is a unit; its Hermitian square $\tilde U\tilde U^*$ is not $e_t$ in general, and it is split by the Cartan decomposition below.

### The Unit Factor

The unit factor is split into a Hermitian positive factor and a unitary factor,

$$
\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r},
\qquad
\tilde U\tilde U^{*}=\tilde U_{\mathrm b}^2.
$$

The Hermitian factor is

$$
\tilde U_{\mathrm b}=\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)
=\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b},
\qquad
\psi=2\operatorname{arcosh}\bigl(\operatorname{Sc}\tilde U_{\mathrm b}\bigr),
$$

and the unitary factor is

$$
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr)
=\cos\frac{\theta}{2}\,e_t+\sin\frac{\theta}{2}\,\vec u_{\mathrm r},
\qquad
\theta=2\arccos\bigl(\operatorname{Sc}\tilde u_{\mathrm r}\bigr).
$$

The axes are recovered from the vector parts when the corresponding angle is nonzero. The two angles and the two axes are the six real data of the unit factor; every case below displays the four objects $\tilde U_{\mathrm b}$, $\tilde u_{\mathrm r}$, $\vec u_{\mathrm b}$ and $\vec u_{\mathrm r}$.

### The Component Form

The product of the two exponentials is the four-term expression of the source. With

$$
c_{\mathrm b}=\cosh\frac{\psi}{2},
\qquad
s_{\mathrm b}=\sinh\frac{\psi}{2},
\qquad
c_{\mathrm r}=\cos\frac{\theta}{2},
\qquad
s_{\mathrm r}=\sin\frac{\theta}{2},
$$

the unit factor is

$$
\tilde U=\bigl(c_{\mathrm b}c_{\mathrm r}-i s_{\mathrm b}s_{\mathrm r}c\bigr)e_t
+i s_{\mathrm b}c_{\mathrm r}\vec u_{\mathrm b}
+c_{\mathrm b}s_{\mathrm r}\vec u_{\mathrm r}
+i s_{\mathrm b}s_{\mathrm r}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r},
\qquad
c=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}.
$$

The four terms are the scalar term, corrected by the angle between the axes, the boost axis, the rotor axis and the cross term. The cross term is present exactly when both angles are nonzero and the axes are neither parallel nor antiparallel. It is the term that the sum of the exponents cannot produce in general, because the sum contains only the two axes and their linear combinations.

### The Logarithms and the Defect

The Cartan logarithm is the pair

$$
\tilde H=i\frac{\psi}{2}\vec u_{\mathrm b},
\qquad
\tilde K=\frac{\theta}{2}\vec u_{\mathrm r},
$$

and its sum is

$$
\tilde H+\tilde K=i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}.
$$

The exponential of this sum is the unit factor only when the two terms commute, that is when the axes are parallel or antiparallel, or one of the angles vanishes. In general it is not a logarithm of $\tilde U$. The **formal exponent** of the element is

$$
\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r},
$$

and its defect is the largest modulus of a coefficient difference in $\exp(\tilde Q_{\log})-\tilde Q$.

The true logarithm is the principal logarithm of the unit factor, shifted by the scalar term,

$$
\operatorname{Log}\tilde Q=(\ln r+i\alpha)e_t+\operatorname{Log}\tilde U,
$$

where $\operatorname{Log}\tilde U$ is the principal logarithm of *Biquaternion Elementary Functions*, evaluated on the unit factor. When the unit factor is unipotent, $(\tilde U-e_t)^2=0$ and the series truncates:

$$
\operatorname{Log}\tilde U=\tilde U-e_t.
$$

### The Matrix Picture

The matrix of $\tilde Q$ is

$$
\mathsf M(\tilde Q)=Q_tI-iQ_x\sigma_x-iQ_y\sigma_y-iQ_z\sigma_z.
$$

Its determinant is $Q_t^2+Q_x^2+Q_y^2+Q_z^2$, and its two scales are

$$
r e^{\psi/2}
\qquad\text{and}\qquad
r e^{-\psi/2},
$$

each counted with its multiplicity. The matrix picture confirms the scale and the rapidity, and it shows the phase as the phase of the scalar factor.

### The Null Cone

For $Q_t^2+Q_x^2+Q_y^2+Q_z^2=0$ the modulus vanishes, no unit factor exists, and no polar word exists. The element is a nonzero zero divisor of rank one. The boundary is approached by families whose modulus tends to zero and whose rapidity diverges; §*The Null Cone Family* below gives the standard family.

## The Eight Cases

### Case 1: The Identity

**Coordinates.** For $\tilde Q=e_t$,

$$
Q_t=1,
\qquad
Q_x=Q_y=Q_z=0,
\qquad
Q_t^2+Q_x^2+Q_y^2+Q_z^2=1.
$$

**Polar data.** The modulus is one and the unit factor is the identity:

$$
r=1,
\qquad
\alpha=0,
\qquad
\tilde U=e_t.
$$

Both angles vanish, $\psi=0$ and $\theta=0$, so both axes are undefined. The four objects are

$$
\tilde U_{\mathrm b}=e_t,
\qquad
\tilde u_{\mathrm r}=e_t,
\qquad
\vec u_{\mathrm b}\ \text{undefined},
\qquad
\vec u_{\mathrm r}\ \text{undefined}.
$$

The word is the identity for every choice of the axes; the parameters are fixed.

**The word and the check.** The exponent is $\operatorname{Log}\tilde Q=0$, and

$$
\tilde Q=\exp(0)=e_t,
$$

with error $0$. The matrix is $I$, with determinant $1$ and the two scales $1$ and $1$.

### Case 2: A Pure Rotor of Angle Pi

**Coordinates.** For $\tilde Q=\vec e_x$,

$$
Q_t=0,
\qquad
Q_x=1,
\qquad
Q_y=Q_z=0,
\qquad
Q_t^2+Q_x^2+Q_y^2+Q_z^2=1.
$$

**Polar data.** The modulus is one, the boost vanishes and the rotor is half a turn:

$$
r=1,
\qquad
\alpha=0,
\qquad
\tilde U=\vec e_x,
\qquad
\psi=0,
\qquad
\theta=\pi.
$$

The four objects are

$$
\tilde U_{\mathrm b}=e_t,
\qquad
\tilde u_{\mathrm r}=\vec e_x,
\qquad
\vec u_{\mathrm b}\ \text{undefined},
\qquad
\vec u_{\mathrm r}=\vec e_x.
$$

**The word and the check.** The word is

$$
\tilde Q=\exp\Bigl(\frac{\pi}{2}\vec e_x\Bigr)=\cos\frac{\pi}{2}\,e_t+\sin\frac{\pi}{2}\vec e_x=\vec e_x,
$$

and the logarithm is the same exponent, $\operatorname{Log}\tilde Q=\frac{\pi}{2}\vec e_x$. The error is $2.2\times10^{-16}$. The matrix is $-i\sigma_x$, with determinant $1$ and the two scales $1$ and $1$.

### Case 3: A Pure Rotor of Angle Pi Over Two

**Coordinates.** For $\tilde Q=\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_x$,

$$
Q_t=\frac{1}{\sqrt2},
\qquad
Q_x=\frac{1}{\sqrt2},
\qquad
Q_y=Q_z=0,
\qquad
Q_t^2+Q_x^2+Q_y^2+Q_z^2=1.
$$

**Polar data.** The modulus is one, the boost vanishes and

$$
r=1,
\qquad
\alpha=0,
\qquad
\tilde U=\tilde Q,
\qquad
\psi=0,
\qquad
\theta=\frac{\pi}{2}.
$$

The four objects are

$$
\tilde U_{\mathrm b}=e_t,
\qquad
\tilde u_{\mathrm r}=\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_x,
\qquad
\vec u_{\mathrm b}\ \text{undefined},
\qquad
\vec u_{\mathrm r}=\vec e_x.
$$

**The word and the check.** The word is

$$
\tilde Q=\exp\Bigl(\frac{\pi}{4}\vec e_x\Bigr)
=\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_x,
$$

and the logarithm is $\operatorname{Log}\tilde Q=\frac{\pi}{4}\vec e_x$. The error is $3.3\times10^{-16}$. The matrix

$$
\mathsf M(\tilde Q)=\frac{1}{\sqrt2}\begin{pmatrix}1&-i\\-i&1\end{pmatrix}
$$

has determinant $1$ and the two scales $1$ and $1$.

### Case 4: A Pure Boost

**Coordinates.** For $\tilde Q=\sqrt2\,e_t+i\vec e_x$,

$$
Q_t=\sqrt2,
\qquad
Q_x=i,
\qquad
Q_y=Q_z=0,
\qquad
Q_t^2+Q_x^2+Q_y^2+Q_z^2=2-1=1.
$$

**Polar data.** The modulus is one and the element is Hermitian:

$$
r=1,
\qquad
\alpha=0,
\qquad
\tilde U=\tilde Q,
\qquad
\tilde U\tilde U^*=3e_t+2\sqrt2\,i\vec e_x.
$$

The scalar part of $\tilde U\tilde U^*$ is $3$, so

$$
\psi=2\operatorname{arcosh}\sqrt2=\operatorname{arcosh}3=2\ln(1+\sqrt2)=1.7627471740.
$$

The four objects are

$$
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\vec e_x,
\qquad
\tilde u_{\mathrm r}=e_t,
\qquad
\vec u_{\mathrm b}=\vec e_x,
\qquad
\vec u_{\mathrm r}\ \text{undefined}.
$$

The rotor angle is $\theta=0$.

**The word and the check.** The boost factor is

$$
\exp\Bigl(i\frac{\psi}{2}\vec e_x\Bigr)=\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\vec e_x
=\sqrt2+i\vec e_x,
$$

and the word is the single exponential

$$
\tilde Q=\exp\bigl(i\ln(1+\sqrt2)\vec e_x\bigr).
$$

The logarithm is $\operatorname{Log}\tilde Q=i\ln(1+\sqrt2)\vec e_x$, with error $2.2\times10^{-16}$. The matrix is Hermitian, with determinant $1$ and the two scales $\sqrt2+1$ and $\sqrt2-1$.

### Case 5: Parallel Axes

**Coordinates.** For $\tilde Q=\bigl(1-\frac{i}{\sqrt2}\bigr)e_t+\bigl(1+\frac{i}{\sqrt2}\bigr)\vec e_x$,

$$
Q_t=1-\frac{i}{\sqrt2},
\qquad
Q_x=1+\frac{i}{\sqrt2},
\qquad
Q_y=Q_z=0,
$$

and

$$
Q_t^2+Q_x^2+Q_y^2+Q_z^2=1.
$$

**Polar data.** The modulus is one, and the Hermitian square is the same as in case 4:

$$
r=1,
\qquad
\alpha=0,
\qquad
\psi=2\ln(1+\sqrt2).
$$

The four objects are

$$
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\vec e_x,
\qquad
\tilde u_{\mathrm r}=\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_x,
\qquad
\vec u_{\mathrm b}=\vec e_x,
\qquad
\vec u_{\mathrm r}=\vec e_x.
$$

The rotor is a quarter turn about the same axis, $\theta=\frac{\pi}{2}$.

**The word and the check.** The axes are parallel, so the two exponents add:

$$
\tilde Q=\exp\Bigl(\frac{\theta+i\psi}{2}\vec e_x\Bigr)
=\exp\Bigl(\Bigl(\frac{\pi}{4}+i\ln(1+\sqrt2)\Bigr)\vec e_x\Bigr).
$$

The logarithm is

$$
\operatorname{Log}\tilde Q=\Bigl(\frac{\pi}{4}+i\ln(1+\sqrt2)\Bigr)\vec e_x,
$$

with error $3.1\times10^{-16}$. The matrix has determinant $1$ and the two scales $\sqrt2+1$ and $\sqrt2-1$. The formal exponent is the true logarithm: the axes commute.

### Case 6: Orthogonal Axes and a Unipotent Element

**Coordinates.** For $\tilde Q=e_t+\vec e_y+\frac{i}{\sqrt2}\vec e_x+\frac{i}{\sqrt2}\vec e_z$,

$$
Q_t=1,
\qquad
Q_x=\frac{i}{\sqrt2},
\qquad
Q_y=1,
\qquad
Q_z=\frac{i}{\sqrt2},
$$

and

$$
Q_t^2+Q_x^2+Q_y^2+Q_z^2=1-\tfrac12+1-\tfrac12=1.
$$

The vector part is null, $Q_x^2+Q_y^2+Q_z^2=0$, and nonzero.

**Polar data.** The modulus is one, the Hermitian square is again

$$
r=1,
\qquad
\alpha=0,
\qquad
\tilde U\tilde U^*=3e_t+2\sqrt2\,i\vec e_x,
\qquad
\psi=2\ln(1+\sqrt2).
$$

The four objects are

$$
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\vec e_x,
\qquad
\tilde u_{\mathrm r}=\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_y,
\qquad
\vec u_{\mathrm b}=\vec e_x,
\qquad
\vec u_{\mathrm r}=\vec e_y.
$$

The rotor is a quarter turn about the orthogonal axis, $\theta=\frac{\pi}{2}$.

**The word and the check.** The word is

$$
\tilde Q=\exp\bigl(i\ln(1+\sqrt2)\vec e_x\bigr)
\exp\Bigl(\frac{\pi}{4}\vec e_y\Bigr).
$$

The unit factor is unipotent, and the true logarithm truncates at the first term:

$$
\operatorname{Log}\tilde Q=\tilde Q-e_t
=\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z,
$$

with error $1.1\times10^{-16}$. The formal exponent is

$$
\tilde Q_{\log}=i\ln(1+\sqrt2)\vec e_x+\frac{\pi}{4}\vec e_y,
$$

and its exponential misses the cross term $i\frac{1}{\sqrt2}\vec e_z$: the defect is $1/\sqrt2=0.7071067812$. The matrix has determinant $1$ and the two scales $\sqrt2+1$ and $\sqrt2-1$.

### Case 7: Non-Parallel Axes

**Coordinates.** For $\tilde Q=\bigl(1-\frac{i}{2}\bigr)e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z$,

$$
Q_t=1-\frac{i}{2},
\qquad
Q_x=\frac{1+i}{\sqrt2},
\qquad
Q_y=\frac{1}{\sqrt2},
\qquad
Q_z=\frac{i}{2},
$$

and

$$
Q_t^2+Q_x^2+Q_y^2+Q_z^2=\tfrac34-i+i+\tfrac12-\tfrac14=1.
$$

The vector part is not null.

**Polar data.** The modulus is one, the Hermitian square is the same as in cases 4 to 6,

$$
r=1,
\qquad
\alpha=0,
\qquad
\tilde U\tilde U^*=3e_t+2\sqrt2\,i\vec e_x,
\qquad
\psi=2\ln(1+\sqrt2).
$$

The four objects are

$$
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\vec e_x,
\qquad
\tilde u_{\mathrm r}=\frac{1}{\sqrt2}e_t+\frac12\vec e_x+\frac12\vec e_y,
\qquad
\vec u_{\mathrm b}=\vec e_x,
\qquad
\vec u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt2}.
$$

The rotor angle is $\theta=\frac{\pi}{2}$, and the scalar product of the axes is $c=1/\sqrt2$.

**The word and the check.** The word is

$$
\tilde Q=\exp\bigl(i\ln(1+\sqrt2)\vec e_x\bigr)
\exp\Bigl(\frac{\pi}{4}\frac{\vec e_x+\vec e_y}{\sqrt2}\Bigr).
$$

The component form is the direct check: with $c_{\mathrm b}=\sqrt2$, $s_{\mathrm b}=1$, $c_{\mathrm r}=s_{\mathrm r}=1/\sqrt2$,

$$
\tilde Q=\Bigl(1-\frac{i}{2}\Bigr)e_t+\frac{1+i}{\sqrt2}\vec e_x
+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z,
$$

which is the element. The true logarithm is

$$
\operatorname{Log}\tilde Q
=\bigl(0.5715606945+0.7976455849\,i\bigr)\vec e_x
+\bigl(0.6846031397+0.1130424452\,i\bigr)\vec e_y
+\bigl(-0.0799330796+0.4840875225\,i\bigr)\vec e_z,
$$

with error $5.0\times10^{-16}$. The formal exponent is

$$
\tilde Q_{\log}=i\ln(1+\sqrt2)\vec e_x+\frac{\pi}{4}\frac{\vec e_x+\vec e_y}{\sqrt2},
$$

and its exponential misses the cross term $i\frac12\vec e_z$: the defect is exactly $\tfrac12$. The matrix has determinant $1$ and the two scales $\sqrt2+1$ and $\sqrt2-1$.

### Case 8: A Generic Null-Vector Element

**Coordinates.** For $\tilde Q=(1+i)e_t+\vec e_x+i\vec e_y$,

$$
Q_t=1+i,
\qquad
Q_x=1,
\qquad
Q_y=i,
\qquad
Q_z=0,
$$

and

$$
Q_t^2+Q_x^2+Q_y^2+Q_z^2=(1+i)^2+1+i^2=2i.
$$

The vector part is null, $Q_x^2+Q_y^2+Q_z^2=1+i^2=0$.

**Polar data.** The modulus is $\bigl(2i\bigr)^{1/2}=1+i$, so

$$
r=\sqrt2,
\qquad
\alpha=\frac{\pi}{4},
\qquad
\tilde U=e_t+\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y.
$$

The Hermitian and unitary factors are

$$
\tilde U_{\mathrm b}=\frac{3e_t-i\vec e_x+i\vec e_y+i\vec e_z}{\sqrt6},
\qquad
\tilde u_{\mathrm r}=\sqrt{\frac23}\,e_t+\frac{1}{\sqrt6}\vec e_x+\frac{1}{\sqrt6}\vec e_y,
$$

with

$$
\psi=2\operatorname{arcosh}\frac{3}{\sqrt6}=\operatorname{arcosh}2=1.3169578969,
\qquad
\vec u_{\mathrm b}=\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt3},
$$

and

$$
\theta=2\arccos\sqrt{\frac23}=\arccos\frac13=1.2309594173,
\qquad
\vec u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt2}.
$$

The axes are perpendicular, $c=0$. The Hermitian square is

$$
\tilde U\tilde U^*=2e_t-i\vec e_x+i\vec e_y+i\vec e_z.
$$

**The word and the check.** The word is

$$
\tilde Q=\sqrt2\,e^{i\pi/4}
\exp\Bigl(i\frac{1.3169578969}{2}\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt3}\Bigr)
\exp\Bigl(\frac{1.2309594173}{2}\frac{\vec e_x+\vec e_y}{\sqrt2}\Bigr).
$$

The unit factor is unipotent, and the scalar factor splits off. The true logarithm is

$$
\operatorname{Log}\tilde Q
=\Bigl(\frac12\ln2+\frac{\pi}{4}i\Bigr)e_t
+\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y,
$$

with error $5.0\times10^{-16}$. The formal exponent is

$$
\tilde Q_{\log}=\frac12\ln2+\frac{\pi}{4}i
+\bigl(0.4352098757-0.3801729982\,i\bigr)\vec e_x
+\bigl(0.4352098757+0.3801729982\,i\bigr)\vec e_y
+0.3801729982\,i\vec e_z,
$$

and its exponential misses the element by $0.5425679115$ in the largest coefficient modulus. The matrix has determinant $2i$ and the two scales $\sqrt3+1$ and $\sqrt3-1$.

## The Null Cone Family

The null cone $Q_t^2+Q_x^2+Q_y^2+Q_z^2=0$ is the complement of the polar domain. The standard family is

$$
\tilde Q(\psi)=e^{-\psi/2}\exp\Bigl(i\frac{\psi}{2}\vec e_z\Bigr)
=\frac{1+e^{-\psi}}{2}e_t+\frac{1-e^{-\psi}}{2}i\vec e_z,
\qquad
\psi\ge0.
$$

Every member is a unit, with product $e^{-\psi}$, and the polar word is a pure boost with $r=e^{-\psi/2}$, $\alpha=0$, rapidity $\psi$ and axis $\vec e_z$. The four objects are

$$
\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\,\vec e_z,
\qquad
\tilde u_{\mathrm r}=e_t,
\qquad
\vec u_{\mathrm b}=\vec e_z,
\qquad
\vec u_{\mathrm r}\ \text{undefined}.
$$

The limit

$$
\tilde Q(\infty)=\frac12\bigl(e_t+i\vec e_z\bigr)
$$

is a null element of rank one. The table gives the approach.

| $\psi$ | scalar part | vector coefficient | $\tilde Q\tilde Q^{\natural}$ |
|---|---|---|---|
| $1$ | $0.6839397206$ | $0.3160602794\,i\vec e_z$ | $0.3678794412$ |
| $2$ | $0.5676676416$ | $0.4323323584\,i\vec e_z$ | $0.1353352832$ |
| $4$ | $0.5091578194$ | $0.4908421806\,i\vec e_z$ | $0.0183156389$ |
| $8$ | $0.5001677313$ | $0.4998322687\,i\vec e_z$ | $0.0003354626$ |
| $\infty$ | $0.5$ | $0.5\,i\vec e_z$ | $0$ |

The scale vanishes and the coefficient of $i\vec e_z$ tends to $\tfrac12$. The convergence is exponential in the rapidity. The limit is a rank-one zero divisor, with no modulus and no word.

## Summary

### Main Results

| Case | $\tilde Q$ | $Q_t$ | $Q_x^2+Q_y^2+Q_z^2$ | $r$ | $\alpha$ | $\psi$ | $\theta$ |
|---|---|---|---|---|---|---|---|
| $1$ | $e_t$ | $1$ | $0$ | $1$ | $0$ | $0$ | $0$ |
| $2$ | $\vec e_x$ | $0$ | $1$ | $1$ | $0$ | $0$ | $\pi$ |
| $3$ | $\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_x$ | $\frac{1}{\sqrt2}$ | $\frac12$ | $1$ | $0$ | $0$ | $\pi/2$ |
| $4$ | $\sqrt2\,e_t+i\vec e_x$ | $\sqrt2$ | $-1$ | $1$ | $0$ | $2\ln(1+\sqrt2)$ | $0$ |
| $5$ | $\bigl(1-\frac{i}{\sqrt2}\bigr)e_t+\bigl(1+\frac{i}{\sqrt2}\bigr)\vec e_x$ | $1-\frac{i}{\sqrt2}$ | $\tfrac12+i\sqrt2$ | $1$ | $0$ | $2\ln(1+\sqrt2)$ | $\pi/2$ |
| $6$ | $e_t+\vec e_y+\frac{i}{\sqrt2}\vec e_x+\frac{i}{\sqrt2}\vec e_z$ | $1$ | $0$ | $1$ | $0$ | $2\ln(1+\sqrt2)$ | $\pi/2$ |
| $7$ | $\bigl(1-\frac{i}{2}\bigr)e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z$ | $1-\frac{i}{2}$ | $\tfrac14+i$ | $1$ | $0$ | $2\ln(1+\sqrt2)$ | $\pi/2$ |
| $8$ | $(1+i)e_t+\vec e_x+i\vec e_y$ | $1+i$ | $0$ | $\sqrt2$ | $\pi/4$ | $\operatorname{arcosh}2$ | $\arccos\frac13$ |

### The Factors

| Case | $\tilde U_{\mathrm b}$ | $\tilde u_{\mathrm r}$ | $\vec u_{\mathrm b}$ | $\vec u_{\mathrm r}$ |
|---|---|---|---|---|
| $1$ | $e_t$ | $e_t$ | — | — |
| $2$ | $e_t$ | $\vec e_x$ | — | $\vec e_x$ |
| $3$ | $e_t$ | $\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_x$ | — | $\vec e_x$ |
| $4$ | $\sqrt2\,e_t+i\vec e_x$ | $e_t$ | $\vec e_x$ | — |
| $5$ | $\sqrt2\,e_t+i\vec e_x$ | $\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_x$ | $\vec e_x$ | $\vec e_x$ |
| $6$ | $\sqrt2\,e_t+i\vec e_x$ | $\frac{1}{\sqrt2}e_t+\frac{1}{\sqrt2}\vec e_y$ | $\vec e_x$ | $\vec e_y$ |
| $7$ | $\sqrt2\,e_t+i\vec e_x$ | $\frac{1}{\sqrt2}e_t+\frac12\vec e_x+\frac12\vec e_y$ | $\vec e_x$ | $\frac{\vec e_x+\vec e_y}{\sqrt2}$ |
| $8$ | $\frac{3e_t-i\vec e_x+i\vec e_y+i\vec e_z}{\sqrt6}$ | $\sqrt{\frac23}\,e_t+\frac{1}{\sqrt6}\vec e_x+\frac{1}{\sqrt6}\vec e_y$ | $\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt3}$ | $\frac{\vec e_x+\vec e_y}{\sqrt2}$ |

### The Reconstruction Table

The word reconstructs the element exactly; the last column is the defect of the formal exponent, the largest coefficient difference in $\exp(\tilde Q_{\log})-\tilde Q$.

| Case | Word | Defect |
|---|---|---|
| $1$ | $e_t$ | $0$ |
| $2$ | $\exp\bigl(\frac{\pi}{2}\vec e_x\bigr)$ | $0$ |
| $3$ | $\exp\bigl(\frac{\pi}{4}\vec e_x\bigr)$ | $0$ |
| $4$ | $\exp\bigl(i\ln(1+\sqrt2)\vec e_x\bigr)$ | $0$ |
| $5$ | $\exp\bigl(\bigl(\frac{\pi}{4}+i\ln(1+\sqrt2)\bigr)\vec e_x\bigr)$ | $0$ |
| $6$ | $\exp\bigl(i\ln(1+\sqrt2)\vec e_x\bigr)\exp\bigl(\frac{\pi}{4}\vec e_y\bigr)$ | $0.7071067812$ |
| $7$ | $\exp\bigl(i\ln(1+\sqrt2)\vec e_x\bigr)\exp\bigl(\frac{\pi}{4}\frac{\vec e_x+\vec e_y}{\sqrt2}\bigr)$ | $0.5$ |
| $8$ | the four-factor word above | $0.5425679115$ |

### The Logarithms

| Case | $\operatorname{Log}\tilde Q$ | Error |
|---|---|---|
| $1$ | $0$ | $0$ |
| $2$ | $\frac{\pi}{2}\vec e_x$ | $2.2\times10^{-16}$ |
| $3$ | $\frac{\pi}{4}\vec e_x$ | $3.3\times10^{-16}$ |
| $4$ | $i\ln(1+\sqrt2)\vec e_x$ | $2.2\times10^{-16}$ |
| $5$ | $\bigl(\frac{\pi}{4}+i\ln(1+\sqrt2)\bigr)\vec e_x$ | $3.1\times10^{-16}$ |
| $6$ | $\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z$ | $1.1\times10^{-16}$ |
| $7$ | the logarithm vector of case 7 | $5.0\times10^{-16}$ |
| $8$ | $\bigl(\frac12\ln2+\frac{\pi}{4}i\bigr)e_t+\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y$ | $5.0\times10^{-16}$ |

### What the Cases Show

- The identity, the two rotors and the pure boost show the degenerate ends: when one angle vanishes, its axis disappears, and when both vanish the word is the identity for every axis.
- Case 5 is the parallel-axis case. The two exponents add, the word is a single exponential, and the formal exponent is the true logarithm.
- Case 6 is the orthogonal-axis case with a unipotent element. The vector part is null and nonzero, the unit factor is unipotent, and the polar word exists. The defect is exactly the cross term $i/\sqrt2\,\vec e_z$.
- Case 7 is the non-parallel case. The formal exponent has no $\vec e_z$ component, while the element has $i/2\,\vec e_z$; the defect is exactly $\tfrac12$, the cross term.
- Case 8 is the generic null-vector element. The scalar factor is not real, the vector part is null, and the unit factor is unipotent. The polar word exists and is unique; the true logarithm truncates because the unit factor is unipotent.
- The cases 4 to 7 share the same Hermitian square $\tilde U\tilde U^*=3e_t+2\sqrt2\,i\vec e_x$ and the same rapidity. They differ by the rotor: none, a quarter turn about the same axis, a quarter turn about an orthogonal axis, and a quarter turn about an axis at $45^\circ$. The defect is zero for the first two and equals the cross term for the last two, $1/\sqrt2$ and $\tfrac12$.
- Cases 6 and 8 have a polar word with a null vector part; the zero divisors of §*The Null Cone Family* have no polar word.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion |
| $Q_t,Q_x,Q_y,Q_z$ | the four complex coordinates |
| $\tilde Q\tilde Q^{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ | the reduced product |
| $\bigl(Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2}$ | the modulus, the principal square root |
| $r>0$, $\alpha$ | the scale and the phase |
| $\tilde U=\tilde Q\bigl(Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr)^{-1/2}$ | the unit factor |
| $\tilde U\tilde U^*=\tilde U_{\mathrm b}^2$ | the Hermitian square |
| $\tilde U_{\mathrm b}$ | the Hermitian positive factor |
| $\tilde u_{\mathrm r}$ | the unitary factor |
| $\tilde H,\tilde K$ | the Cartan logarithm, $i\frac{\psi}{2}\vec u_{\mathrm b}$ and $\frac{\theta}{2}\vec u_{\mathrm r}$ |
| $\psi\ge0$ | the rapidity |
| $\theta\in[0,2\pi]$ | the rotor angle |
| $\vec u_{\mathrm b},\vec u_{\mathrm r}$ | the boost and rotor axes |
| $c=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ | the cosine of the angle between the axes |
| $\tilde Q_{\log}$ | the formal exponent |
| $\mathsf M(\tilde Q)$ | the matrix $Q_tI-iQ_x\sigma_x-iQ_y\sigma_y-iQ_z\sigma_z$ |
| $c_{\mathrm b},s_{\mathrm b},c_{\mathrm r},s_{\mathrm r}$ | the half-angle cosines and sines |

## Further Reading

- [Exponential Polar Decomposition of Biquaternions](exponential-polar-decomposition-of-biquaternions.html), for the four-factor word, the Cartan decomposition, existence, uniqueness and the boundary.
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential, the logarithm, the kernel and the degenerate limit.
- [Modulus–Unit Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the modulus and the unit factor.
- [Worked Examples of Exponential Polar Decomposition of Quaternions](worked-examples-of-exponential-polar-decomposition-of-quaternions.html), for the definite compact companion with one axis.
- [Worked Examples of Exponential Polar Decomposition of Split-Complex Numbers](worked-examples-of-exponential-polar-decomposition-of-split-complex-numbers.html), for the two-dimensional companion.
- [Worked Examples of Exponential Polar Decomposition of Reduced Biquaternions](worked-examples-of-exponential-polar-decomposition-of-reduced-biquaternions.html), for the commutative four-dimensional companion.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation.
