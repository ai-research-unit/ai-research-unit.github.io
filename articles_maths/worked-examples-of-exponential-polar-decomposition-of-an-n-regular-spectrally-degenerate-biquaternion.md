# __Worked Examples of Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion__

## Introduction

This article works eight numerical cases of the exponential polar decomposition in the N-regular, spectrally degenerate sector. Each case is an element

$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,
\qquad
N=Q_t^2+Q_x^2+Q_y^2+Q_z^2\neq0,
\qquad
B^2=Q_x^2+Q_y^2+Q_z^2=0,
$$

and each is written as

$$
\tilde Q=Q_t\bigl(e_t+\vec\Upsilon\bigr),
\qquad
\vec\Upsilon^2=0,
$$

and as

$$
\tilde Q=r\,e^{i\alpha}\,
\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)
\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr).
$$

The cases are chosen to display the rigidity of the word: the scalar line, where the unit factor is $\pm e_t$, and the Jordan part, where the unit factor is $\pm(e_t+\vec\Upsilon)$ with $\vec\Upsilon\neq0$, the two axes are orthogonal, and the rapidity is a function of the rotor angle. The article is independent of the main article of the same title; it repeats the recipe and the checks.

The numbers are rounded to eight or nine significant digits; the computations were carried to double precision.

**The plan.** §*Conventions and Recipes* fixes the notation and the algorithm. §*The Scalar Line* treats the three scalar cases. §*The Jordan Part* treats the five defective cases. §*The Comparison* collects the constraints, the exact logarithms and the defects. The summary gives the tables.

## Conventions and Recipes

### The Coordinates

A biquaternion is a four-tuple

$$
\tilde Q=(Q_t,Q_x,Q_y,Q_z)=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,
$$

with complex coordinates. The quaternion product is

$$
(ab)_t=a_tb_t-a_xb_x-a_yb_y-a_zb_z,
\qquad
(ab)_x=a_tb_x+a_xb_t+a_yb_z-a_zb_y,
$$

and cyclically for $y,z$. The conjugate is $\tilde Q^{\natural}=(Q_t,-Q_x,-Q_y,-Q_z)$, the star is $\tilde Q^*=(\bar Q_t,-\bar Q_x,-\bar Q_y,-\bar Q_z)$, and

$$
N=\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2.
$$

The notation is the one of *Conventions in Mathematics*.

### The Recipe

Given $\tilde Q$:

1. Compute $N$ and $B^2=Q_x^2+Q_y^2+Q_z^2$. The sector requires $N\neq0$ and $B^2=0$.
2. Compute the scalar part $Q_t$ and the nilpotent direction $\vec\Upsilon=\vec Q/Q_t$. Check $\vec\Upsilon^2=0$.
3. Compute the modulus $\Rho$, the principal square root of $N=Q_t^2$, and write $\Rho=r e^{i\alpha}$ with $r>0$ and $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$.
4. Compute the sign $\varepsilon=Q_t/\Rho=\pm1$ and the unit factor $\tilde U=\varepsilon(e_t+\vec\Upsilon)$.
5. Compute the Hermitian factor $\tilde U_{\mathrm b}=(\tilde U\tilde U^*)^{1/2}$, positive of norm one, and the rotor $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$.
6. Read the boost angle and axis from $\tilde U_{\mathrm b}=c_{\mathrm b}e_t+i s_{\mathrm b}\vec u_{\mathrm b}$, and the rotor angle and axis from $\tilde u_{\mathrm r}=c_{\mathrm r}e_t+s_{\mathrm r}\vec u_{\mathrm r}$.
7. Check the constraints $c_{\mathrm b}c_{\mathrm r}=\varepsilon$ and $s_{\mathrm b}s_{\mathrm r}c=0$, with $c=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$.
8. Compute the exact logarithm $\log Q_t+\vec\Upsilon$ and check its exponential against $\tilde Q$.
9. Compute the formal exponent $\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}$ and its defect.

The **defect** of a case is

$$
\delta=\bigl\lVert\exp(\tilde Q_{\log})-\tilde Q\bigr\rVert,
$$

where the norm is the maximum modulus of the four coordinates.

### The Checks

The following identities hold in every case and are used below without comment.

| Identity | Meaning |
|---|---|
| $\tilde Q=Q_t(e_t+\vec\Upsilon)$, $\vec\Upsilon^2=0$ | the normal form |
| $\tilde U=\varepsilon(e_t+\vec\Upsilon)$ | the unit factor is $\pm$unipotent |
| $(\tilde U-\varepsilon e_t)^2=0$ | the minimal polynomial is a square |
| $\tilde U_{\mathrm b}^*=\tilde U_{\mathrm b}$, $\langle\tilde U_{\mathrm b}\rangle_{\natural}=1$ | the Hermitian factor is positive of norm one |
| $\tilde u_{\mathrm r}^*=\tilde u_{\mathrm r}^{-1}$, $\langle\tilde u_{\mathrm r}\rangle_{\natural}=1$ | the rotor is $*$-unitary of norm one |
| $\cosh\frac{\psi}{2}\cos\frac{\theta}{2}=\varepsilon$ | the scalar constraint |
| $\sinh\frac{\psi}{2}\sin\frac{\theta}{2}\,c=0$ | the axis constraint |
| $\operatorname{Log}\tilde Q=\log Q_t+\vec\Upsilon$ | the exact logarithm |

## The Scalar Line

### Case 1: The Identity

#### The Element

$$
\tilde Q=e_t=(1,0,0,0).
$$

$$
N=1,
\qquad
B^2=0,
\qquad
\Rho=1,
\qquad
r=1,
\qquad
\alpha=0,
\qquad
\varepsilon=1.
$$

#### The Polar Factors

$$
\tilde U=e_t,
\qquad
\tilde U_{\mathrm b}=e_t,
\qquad
\tilde u_{\mathrm r}=e_t.
$$

The boost and the rotor are both the identity, with $\psi=0$ and $\theta=0$; the two axes are undefined.

#### The Logarithm

$$
\operatorname{Log}\tilde Q=0,
\qquad
\tilde Q_{\log}=0,
\qquad
\delta=0.
$$

The element is the identity; it is normal.

### Case 2: A Negative Scalar

#### The Element

$$
\tilde Q=-2e_t=(-2,0,0,0).
$$

$$
N=4,
\qquad
B^2=0,
\qquad
\Rho=2,
\qquad
r=2,
\qquad
\alpha=0,
\qquad
\varepsilon=-1.
$$

#### The Polar Factors

$$
\tilde U=-e_t,
\qquad
\tilde U_{\mathrm b}=e_t,
\qquad
\tilde u_{\mathrm r}=-e_t.
$$

The boost is the identity, with $\psi=0$. The rotor is the central element $-e_t$, which is $\exp(\pi\vec u_{\mathrm r})$ for every unit axis; in the range $\theta\in[0,2\pi]$ the angle is $\theta=2\pi$ and the axis is undefined.

#### The Logarithm

$$
\operatorname{Log}\tilde Q=\ln2+i\pi,
\qquad
\tilde Q_{\log}=\ln2+\pi\vec u_{\mathrm r},
\qquad
\delta=0.
$$

The formal exponent depends on the free axis, but its exponential is $-2$ for every axis, because $\exp(\pi\vec u_{\mathrm r})=-e_t$. The element is normal.

### Case 3: An Imaginary Scalar

#### The Element

$$
\tilde Q=2i\,e_t=(2i,0,0,0).
$$

$$
N=-4,
\qquad
B^2=0,
\qquad
\Rho=2i,
\qquad
r=2,
\qquad
\alpha=\frac{\pi}{2},
\qquad
\varepsilon=1.
$$

#### The Polar Factors

$$
\tilde U=e_t,
\qquad
\tilde U_{\mathrm b}=e_t,
\qquad
\tilde u_{\mathrm r}=e_t.
$$

The word is pure scale and phase, with $\psi=0$ and $\theta=0$.

#### The Logarithm

$$
\operatorname{Log}\tilde Q=\ln2+i\frac{\pi}{2},
\qquad
\tilde Q_{\log}=\ln2+i\frac{\pi}{2},
\qquad
\delta=0.
$$

The element is normal.

## The Jordan Part

### Case 4: The Standard Jordan Element

#### The Element

$$
\tilde Q=e_t+\vec e_x+i\vec e_y=(1,1,i,0).
$$

$$
N=1,
\qquad
B^2=0,
\qquad
\Rho=1,
\qquad
r=1,
\qquad
\alpha=0,
\qquad
\varepsilon=1,
\qquad
Q_t=1,
\qquad
\vec\Upsilon=\vec e_x+i\vec e_y.
$$

#### The Polar Factors

$$
\tilde U=\tilde Q,
\qquad
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\frac{\vec e_y+\vec e_z}{\sqrt2},
\qquad
\tilde u_{\mathrm r}=\frac{e_t+\vec e_x}{\sqrt2}.
$$

The boost has

$$
\psi=2\ln(1+\sqrt2)=1.762747174,
\qquad
\vec u_{\mathrm b}=\frac{\vec e_y+\vec e_z}{\sqrt2},
$$

and the rotor has

$$
\theta=\frac{\pi}{2},
\qquad
\vec u_{\mathrm r}=\vec e_x.
$$

The axes are orthogonal: $c=0$. The scalar constraint is $\cosh\frac{\psi}{2}\cos\frac{\theta}{2}=\sqrt2\cdot\frac{1}{\sqrt2}=1=\varepsilon$.

#### The Word

$$
\tilde Q=\exp\Bigl(i\frac{\psi}{2}\frac{\vec e_y+\vec e_z}{\sqrt2}\Bigr)
\exp\Bigl(\frac{\pi}{4}\vec e_x\Bigr).
$$

#### The Exact Logarithm

$$
\operatorname{Log}\tilde Q=\vec e_x+i\vec e_y,
\qquad
\exp(\operatorname{Log}\tilde Q)=\tilde Q,
\qquad
\text{error}<10^{-15}.
$$

#### The Formal Exponent

$$
\tilde Q_{\log}=\frac{\pi}{4}\vec e_x+i\ln(1+\sqrt2)\frac{\vec e_y+\vec e_z}{\sqrt2}
=0.78539816\,\vec e_x+i0.62322524(\vec e_y+\vec e_z).
$$

$$
\delta=0.63997478.
$$

The formal exponent is not the logarithm: the cross term $i\tanh\frac{\psi}{2}\tan\frac{\theta}{2}\vec u_{\mathrm b}\times\vec u_{\mathrm r}$ is present.

### Case 5: The Second Jordan Element

#### The Element

$$
\tilde Q=e_t+\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z
=(1,\ 0.70710678i,\ 1,\ 0.70710678i).
$$

$$
N=1,
\qquad
B^2=0,
\qquad
\Rho=1,
\qquad
r=1,
\qquad
\alpha=0,
\qquad
\varepsilon=1,
\qquad
Q_t=1,
\qquad
\vec\Upsilon=\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z.
$$

#### The Polar Factors

$$
\tilde U=\tilde Q,
\qquad
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\vec e_x,
\qquad
\tilde u_{\mathrm r}=\frac{e_t+\vec e_y}{\sqrt2}.
$$

The boost has

$$
\psi=2\ln(1+\sqrt2)=1.762747174,
\qquad
\vec u_{\mathrm b}=\vec e_x,
$$

and the rotor has

$$
\theta=\frac{\pi}{2},
\qquad
\vec u_{\mathrm r}=\vec e_y.
$$

The axes are orthogonal: $c=0$. The scalar constraint is again $\sqrt2\cdot\frac{1}{\sqrt2}=1$.

#### The Word

$$
\tilde Q=\exp\Bigl(i\frac{\psi}{2}\vec e_x\Bigr)
\exp\Bigl(\frac{\pi}{4}\vec e_y\Bigr).
$$

#### The Exact Logarithm

$$
\operatorname{Log}\tilde Q=\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z,
\qquad
\exp(\operatorname{Log}\tilde Q)=\tilde Q,
\qquad
\text{error}<10^{-15}.
$$

#### The Formal Exponent

$$
\tilde Q_{\log}=i\ln(1+\sqrt2)\vec e_x+\frac{\pi}{4}\vec e_y
=i0.88137359\,\vec e_x+0.78539816\,\vec e_y.
$$

$$
\delta=0.70710678.
$$

The defect is larger than in case 4, because the two axes are orthogonal but the coefficients of the two exponents are different.

### Case 6: A Jordan Element with a Complex Scalar

#### The Element

$$
\tilde Q=(1+i)e_t+\vec e_x+i\vec e_y=(1+i,\ 1,\ i,\ 0).
$$

$$
N=2i,
\qquad
B^2=0,
\qquad
\Rho=1+i,
\qquad
r=\sqrt2,
\qquad
\alpha=\frac{\pi}{4},
\qquad
\varepsilon=1,
\qquad
Q_t=1+i,
\qquad
\vec\Upsilon=\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y.
$$

#### The Polar Factors

$$
\tilde U=\tilde Q/\Rho=e_t+\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y,
$$

$$
\tilde U_{\mathrm b}=1.22474487\,e_t-i0.40824829\,\vec e_x+i0.40824829\,\vec e_y+i0.40824829\,\vec e_z,
$$

$$
\tilde u_{\mathrm r}=0.81649658\,e_t+0.40824829\,\vec e_x+0.40824829\,\vec e_y.
$$

The boost has

$$
\psi=\operatorname{arcosh}2=1.316957897,
\qquad
\vec u_{\mathrm b}=\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt3},
$$

and the rotor has

$$
\theta=\arccos\frac13=1.230959417,
\qquad
\vec u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt2}.
$$

The axes are orthogonal: $c=0$. The scalar constraint is $\cosh\frac{\psi}{2}\cos\frac{\theta}{2}=\sqrt{1.5}\cdot\sqrt{2/3}=1$.

#### The Word

$$
\tilde Q=(1+i)\exp\Bigl(i\frac{\psi}{2}\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt3}\Bigr)
\exp\Bigl(\frac{\theta}{2}\frac{\vec e_x+\vec e_y}{\sqrt2}\Bigr).
$$

#### The Exact Logarithm

$$
\operatorname{Log}\tilde Q=\Bigl(\ln\sqrt2+i\frac{\pi}{4}\Bigr)e_t
+\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y
=(0.34657359+0.78539816i)e_t+(0.5-0.5i)\vec e_x+(0.5+0.5i)\vec e_y,
$$

with exponential $\tilde Q$ to $10^{-15}$.

#### The Formal Exponent

$$
\tilde Q_{\log}=(0.34657359+0.78539816i)e_t
+(0.43520988-0.38017300i)\vec e_x
+(0.43520988+0.38017300i)\vec e_y
+0.38017300i\,\vec e_z.
$$

$$
\delta=0.54256791.
$$

### Case 7: A Negative Jordan Element

#### The Element

$$
\tilde Q=-e_t-\vec e_x-i\vec e_y=(-1,-1,-i,0).
$$

$$
N=1,
\qquad
B^2=0,
\qquad
\Rho=1,
\qquad
r=1,
\qquad
\alpha=0,
\qquad
\varepsilon=-1,
\qquad
Q_t=-1,
\qquad
\vec\Upsilon=\vec e_x+i\vec e_y.
$$

#### The Polar Factors

$$
\tilde U=-\bigl(e_t+\vec e_x+i\vec e_y\bigr),
\qquad
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\frac{\vec e_y+\vec e_z}{\sqrt2},
\qquad
\tilde u_{\mathrm r}=-\frac{e_t+\vec e_x}{\sqrt2}.
$$

The boost is the one of case 4, with $\psi=1.762747174$ and the same axis. The rotor has

$$
\theta=\frac{3\pi}{2},
\qquad
\vec u_{\mathrm r}=-\vec e_x.
$$

The axes are orthogonal: $c=0$. The scalar constraint is $\sqrt2\cdot(-\frac{1}{\sqrt2})=-1=\varepsilon$; the sign of the rotor angle is the sign of $\varepsilon$.

#### The Word

$$
\tilde Q=\exp\Bigl(i\frac{\psi}{2}\frac{\vec e_y+\vec e_z}{\sqrt2}\Bigr)
\exp\Bigl(\frac{3\pi}{4}(-\vec e_x)\Bigr).
$$

#### The Exact Logarithm

$$
\operatorname{Log}\tilde Q=i\pi+\vec e_x+i\vec e_y,
\qquad
\exp(\operatorname{Log}\tilde Q)=\tilde Q,
\qquad
\text{error}<10^{-15}.
$$

The scalar logarithm is $i\pi$, the principal logarithm of $-1$.

#### The Formal Exponent

$$
\tilde Q_{\log}=-2.35619449\,\vec e_x+i0.62322524(\vec e_y+\vec e_z).
$$

$$
\delta=1.2330607.
$$

The formal exponent has no scalar part, because $\ln r+i\alpha=0$; the true logarithm has $i\pi$, the period that the word does not see.

### Case 8: A Scaled Jordan Element

#### The Element

$$
\tilde Q=2e_t+2\vec e_x+2i\vec e_y=(2,2,2i,0).
$$

$$
N=4,
\qquad
B^2=0,
\qquad
\Rho=2,
\qquad
r=2,
\qquad
\alpha=0,
\qquad
\varepsilon=1,
\qquad
Q_t=2,
\qquad
\vec\Upsilon=\vec e_x+i\vec e_y.
$$

#### The Polar Factors

$$
\tilde U=e_t+\vec e_x+i\vec e_y,
\qquad
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\frac{\vec e_y+\vec e_z}{\sqrt2},
\qquad
\tilde u_{\mathrm r}=\frac{e_t+\vec e_x}{\sqrt2}.
$$

The word is the one of case 4 with the scale $r=2$:

$$
\psi=1.762747174,
\qquad
\vec u_{\mathrm b}=\frac{\vec e_y+\vec e_z}{\sqrt2},
\qquad
\theta=\frac{\pi}{2},
\qquad
\vec u_{\mathrm r}=\vec e_x.
$$

#### The Exact Logarithm

$$
\operatorname{Log}\tilde Q=\ln2+\vec e_x+i\vec e_y,
\qquad
\exp(\operatorname{Log}\tilde Q)=\tilde Q,
\qquad
\text{error}<10^{-15}.
$$

#### The Formal Exponent

$$
\tilde Q_{\log}=\ln2+\frac{\pi}{4}\vec e_x+i0.62322524(\vec e_y+\vec e_z).
$$

$$
\delta=1.2799496.
$$

The defect is twice the defect of case 4, because the exponential of the central $\ln2$ multiplies the miss by $2$.

## The Comparison

### The Scalar Line

| Case | $\tilde Q$ | $Q_t$ | $\Rho$ | $\varepsilon$ | $\theta$ | $\operatorname{Log}\tilde Q$ | $\delta$ |
|---|---|---|---|---|---|---|---|
| 1 | $e_t$ | $1$ | $1$ | $+1$ | $0$ | $0$ | $0$ |
| 2 | $-2e_t$ | $-2$ | $2$ | $-1$ | $2\pi$ | $\ln2+i\pi$ | $0$ |
| 3 | $2ie_t$ | $2i$ | $2i$ | $+1$ | $0$ | $\ln2+i\frac{\pi}{2}$ | $0$ |

The scalar line is the normal locus of the sector. The rotor is central, the boost is the identity, and the exact logarithm is the scalar logarithm.

### The Jordan Part

| Case | $Q_t$ | $\varepsilon$ | $\psi$ | $\theta$ | $\vec u_{\mathrm b}$ | $\vec u_{\mathrm r}$ | $\delta$ |
|---|---|---|---|---|---|---|---|
| 4 | $1$ | $+1$ | $1.762747$ | $\frac{\pi}{2}$ | $\frac{\vec e_y+\vec e_z}{\sqrt2}$ | $\vec e_x$ | $0.639975$ |
| 5 | $1$ | $+1$ | $1.762747$ | $\frac{\pi}{2}$ | $\vec e_x$ | $\vec e_y$ | $0.707107$ |
| 6 | $1+i$ | $+1$ | $1.316958$ | $1.230959$ | $\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt3}$ | $\frac{\vec e_x+\vec e_y}{\sqrt2}$ | $0.542568$ |
| 7 | $-1$ | $-1$ | $1.762747$ | $\frac{3\pi}{2}$ | $\frac{\vec e_y+\vec e_z}{\sqrt2}$ | $-\vec e_x$ | $1.233061$ |
| 8 | $2$ | $+1$ | $1.762747$ | $\frac{\pi}{2}$ | $\frac{\vec e_y+\vec e_z}{\sqrt2}$ | $\vec e_x$ | $1.279950$ |

In every Jordan case $c=0$, the axes are orthogonal, and the rapidity is a function of the angle:

$$
\lvert\cos\frac{\theta}{2}\rvert=\frac{1}{\cosh\frac{\psi}{2}}.
$$

### The Constraints

| Case | $(\tilde U-\varepsilon e_t)^2$ | $\vec\Upsilon^2$ | $c$ | $\cosh\frac{\psi}{2}\cos\frac{\theta}{2}$ |
|---|---|---|---|---|
| 1 | $0$ | $0$ | -- | $1$ |
| 2 | $0$ | $0$ | -- | $-1$ |
| 3 | $0$ | $0$ | -- | $1$ |
| 4 | $0$ | $0$ | $0$ | $1$ |
| 5 | $0$ | $0$ | $0$ | $1$ |
| 6 | $0$ | $0$ | $0$ | $1$ |
| 7 | $0$ | $0$ | $0$ | $-1$ |
| 8 | $0$ | $0$ | $0$ | $1$ |

The two columns of zeros are the numerical form of the rigidity: the unit factor is $\pm$unipotent and the nilpotent direction is null.

### The Exact Logarithm

| Case | $\operatorname{Log}\tilde Q-\log Q_t$ | $\lVert\exp(\operatorname{Log}\tilde Q)-\tilde Q\rVert$ |
|---|---|---|
| 1 | $0$ | $0$ |
| 2 | $0$ | $7\times10^{-16}$ |
| 3 | $0$ | $7\times10^{-16}$ |
| 4 | $\vec e_x+i\vec e_y$ | $0$ |
| 5 | $\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z$ | $4\times10^{-16}$ |
| 6 | $\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y$ | $9\times10^{-16}$ |
| 7 | $\vec e_x+i\vec e_y$ | $1.5\times10^{-15}$ |
| 8 | $\vec e_x+i\vec e_y$ | $4\times10^{-16}$ |

The exact logarithm is exact: the error is the rounding of the matrix exponential, not a truncation.

### The Defects

| Case | $\tilde Q_{\log}$ | $\delta$ |
|---|---|---|
| 1 | $0$ | $0$ |
| 2 | $\ln2+\pi\vec u_{\mathrm r}$ | $0$ |
| 3 | $\ln2+i\frac{\pi}{2}$ | $0$ |
| 4 | $\frac{\pi}{4}\vec e_x+i0.623225(\vec e_y+\vec e_z)$ | $0.639975$ |
| 5 | $i0.881374\vec e_x+0.785398\vec e_y$ | $0.707107$ |
| 6 | $(0.346574+0.785398i)e_t+(0.435210-0.380173i)\vec e_x+(0.435210+0.380173i)\vec e_y+0.380173i\vec e_z$ | $0.542568$ |
| 7 | $-2.356194\vec e_x+i0.623225(\vec e_y+\vec e_z)$ | $1.233061$ |
| 8 | $\ln2+\frac{\pi}{4}\vec e_x+i0.623225(\vec e_y+\vec e_z)$ | $1.279950$ |

The scalar line has zero defect, because the formal exponent is a logarithm there. The Jordan part has positive defect in every case, because the cross term is nonzero.

## Summary

### The Cases

| Case | $\tilde Q$ | $N$ | $Q_t$ | $\varepsilon$ | Stratum |
|---|---|---|---|---|---|
| 1 | $e_t$ | $1$ | $1$ | $+1$ | scalar |
| 2 | $-2e_t$ | $4$ | $-2$ | $-1$ | scalar |
| 3 | $2ie_t$ | $-4$ | $2i$ | $+1$ | scalar |
| 4 | $e_t+\vec e_x+i\vec e_y$ | $1$ | $1$ | $+1$ | Jordan |
| 5 | $e_t+\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z$ | $1$ | $1$ | $+1$ | Jordan |
| 6 | $(1+i)e_t+\vec e_x+i\vec e_y$ | $2i$ | $1+i$ | $+1$ | Jordan |
| 7 | $-e_t-\vec e_x-i\vec e_y$ | $1$ | $-1$ | $-1$ | Jordan |
| 8 | $2e_t+2\vec e_x+2i\vec e_y$ | $4$ | $2$ | $+1$ | Jordan |

### The Word Data

| Case | $r$ | $\alpha$ | $\psi$ | $\theta$ | $\vec u_{\mathrm b}$ | $\vec u_{\mathrm r}$ | $c$ |
|---|---|---|---|---|---|---|---|
| 1 | $1$ | $0$ | $0$ | $0$ | -- | -- | -- |
| 2 | $2$ | $0$ | $0$ | $2\pi$ | -- | -- | -- |
| 3 | $2$ | $\frac{\pi}{2}$ | $0$ | $0$ | -- | -- | -- |
| 4 | $1$ | $0$ | $1.762747$ | $\frac{\pi}{2}$ | $\frac{\vec e_y+\vec e_z}{\sqrt2}$ | $\vec e_x$ | $0$ |
| 5 | $1$ | $0$ | $1.762747$ | $\frac{\pi}{2}$ | $\vec e_x$ | $\vec e_y$ | $0$ |
| 6 | $\sqrt2$ | $\frac{\pi}{4}$ | $1.316958$ | $1.230959$ | $\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt3}$ | $\frac{\vec e_x+\vec e_y}{\sqrt2}$ | $0$ |
| 7 | $1$ | $0$ | $1.762747$ | $\frac{3\pi}{2}$ | $\frac{\vec e_y+\vec e_z}{\sqrt2}$ | $-\vec e_x$ | $0$ |
| 8 | $2$ | $0$ | $1.762747$ | $\frac{\pi}{2}$ | $\frac{\vec e_y+\vec e_z}{\sqrt2}$ | $\vec e_x$ | $0$ |

### What the Examples Show

- Every case has $B^2=0$ and $N\neq0$, and every element is $Q_t(e_t+\vec\Upsilon)$ with $\vec\Upsilon^2=0$.
- The unit factor is $\pm(e_t+\vec\Upsilon)$: its scalar part is $\pm1$ and its square is the identity on the scalar line, a nontrivial unipotent on the Jordan part.
- On the Jordan part the axes are orthogonal, $c=0$, and the rapidity is tied to the rotor angle by $|\cos\frac{\theta}{2}|=1/\cosh\frac{\psi}{2}$.
- The exact logarithm is $\log Q_t+\vec\Upsilon$, with no series and no correction. The scalar logarithm carries the sign and the phase; the nilpotent part is fixed.
- The formal exponent is a logarithm on the scalar line and not on the Jordan part. The defect is the cross term $i\tanh\frac{\psi}{2}\tan\frac{\theta}{2}\vec u_{\mathrm b}\times\vec u_{\mathrm r}$ plus the nonlinear terms.
- The defect scales with the element: case 8 is twice case 4, and its defect is twice as large.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q$ | the element of the case |
| $N$ | the reduced product |
| $B^2$ | the vector form |
| $Q_t$ | the scalar part |
| $\vec\Upsilon=\vec Q/Q_t$ | the nilpotent direction |
| $\Rho$ | the modulus, principal square root of $N$ |
| $r,\alpha$ | the polar coordinates of $\Rho$ |
| $\varepsilon=Q_t/\Rho$ | the sign of the unit factor, $\pm1$ |
| $\tilde U$ | the unit factor |
| $\tilde U_{\mathrm b}$ | the Hermitian positive factor |
| $\tilde u_{\mathrm r}$ | the rotor |
| $\psi,\vec u_{\mathrm b}$ | the rapidity and the boost axis |
| $\theta,\vec u_{\mathrm r}$ | the rotor angle and the rotor axis |
| $c$ | the cosine between the axes |
| $\tilde Q_{\log}$ | the formal exponent |
| $\delta$ | the defect of the case |

## Further Reading

- [Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html), for the theorem, the proofs and the rigidity of the word.
- [Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html), for the companion sector and its worked examples.
- [Worked Examples of Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](worked-examples-of-exponential-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html), for the regular cases.
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the modulus–unit theorem.
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the normal forms and the two strata.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation.
