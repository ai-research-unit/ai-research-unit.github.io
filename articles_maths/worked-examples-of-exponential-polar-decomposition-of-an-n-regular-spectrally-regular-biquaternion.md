# __Worked Examples of Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion__

## Introduction

This article works eight numerical cases of the exponential polar decomposition in the N-regular, spectrally regular sector. Each case is an element

$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,
\qquad
N=Q_t^2+Q_x^2+Q_y^2+Q_z^2\neq0,
\qquad
B^2=Q_x^2+Q_y^2+Q_z^2\neq0,
$$

and each is written as

$$
\tilde Q=r\,e^{i\alpha}\,
\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)
\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr).
$$

The cases are chosen to display the spectral reading of the word: the normal elements, where the two axes are parallel and the word is one exponential, and the non-normal elements, where the axes are not the eigenlines and the spectrum does not determine the rapidity and the rotor angle. The article is independent of the main article of the same title; it repeats the recipe and the checks.

The numbers are the ones of the computational verification described in §*Conventions and Recipes*. They are rounded to eight or nine significant digits; the computations were carried to double precision.

**The plan.** §*Conventions and Recipes* fixes the notation and the algorithm. §§*Case 1* to *Case 8* treat the eight elements, grouped by their normal or non-normal character. §*The Comparison* collects the spectral data and the defects. The summary gives the tables.

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

1. Compute $N$ and $B^2=Q_x^2+Q_y^2+Q_z^2$. The sector requires $N\neq0$ and $B^2\neq0$.
2. Compute the modulus $\Rho$, the principal square root of $N$, and write $\Rho=r e^{i\alpha}$ with $r>0$ and $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$.
3. Compute the unit factor $\tilde U=\tilde Q/\Rho$.
4. Compute the Hermitian factor $\tilde U_{\mathrm b}=(\tilde U\tilde U^*)^{1/2}$, positive of norm one, and the rotor $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$.
5. Read the boost angle and axis from $\tilde U_{\mathrm b}=c_{\mathrm b}e_t+i s_{\mathrm b}\vec u_{\mathrm b}$, and the rotor angle and axis from $\tilde u_{\mathrm r}=c_{\mathrm r}e_t+s_{\mathrm r}\vec u_{\mathrm r}$.
6. Check $\tilde Q=r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ and $\langle\tilde U\rangle_{\natural}=1$.
7. Compute the eigen-data: $\lambda_\pm=Q_t\pm iB$, $\vec\Xi=-i\vec Q/B$, $\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi)$, and $\mu_\pm=\lambda_\pm/\Rho$.
8. Compute the true logarithm by the matrix logarithm, and compare its exponential with $\tilde Q$.

The **defect** of a case is

$$
\delta=\bigl\lVert\exp(\tilde Q_{\log})-\tilde Q\bigr\rVert,
\qquad
\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r},
$$

where the norm is the maximum modulus of the four coordinates. It is zero exactly in the normal cases and positive in the non-normal ones.

### The Checks

The following identities hold in every case and are used below without comment.

| Identity | Meaning |
|---|---|
| $\langle\tilde U\rangle_{\natural}=1$ | the unit factor has norm one |
| $\tilde U_{\mathrm b}^*=\tilde U_{\mathrm b}$, $\langle\tilde U_{\mathrm b}\rangle_{\natural}=1$ | the Hermitian factor is positive of norm one |
| $\tilde u_{\mathrm r}^*=\tilde u_{\mathrm r}^{-1}$, $\langle\tilde u_{\mathrm r}\rangle_{\natural}=1$ | the rotor is unitary of norm one |
| $\tilde Q=\Rho\tilde U$ | the modulus–unit split |
| $[\tilde Q,\tilde Q^*]=-2\vec Q\times\overline{\vec Q}$ | normality |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |
| $\mu_\pm=\lambda_\pm/\Rho$ | the eigenvalues of the unit factor |

## Case 1: A Rotor

### The Element

$$
\tilde Q=\vec e_x=(0,1,0,0).
$$

$$
N=1,
\qquad
B^2=1,
\qquad
\Rho=1,
\qquad
r=1,
\qquad
\alpha=0.
$$

### The Polar Factors

$$
\tilde U=\vec e_x,
\qquad
\tilde U_{\mathrm b}=e_t,
\qquad
\tilde u_{\mathrm r}=\vec e_x.
$$

The boost is the identity, with $\psi=0$ and an undefined axis. The rotor is

$$
\tilde u_{\mathrm r}=\vec e_x=\exp\Bigl(\frac{\pi}{2}\vec e_x\Bigr),
$$

so $\theta=\pi$ and $\vec u_{\mathrm r}=\vec e_x$.

### The Word

$$
\tilde Q=\exp\Bigl(\frac{\pi}{2}\vec e_x\Bigr).
$$

The word has $r=1$, $\alpha=0$, $\psi=0$, $\theta=\pi$, $\vec u_{\mathrm r}=\vec e_x$.

### The Spectral Data

$$
\lambda_+=i,
\qquad
\lambda_-=-i,
\qquad
\vec\Xi=-i\vec e_x,
\qquad
\tilde\Pi_\pm=\frac{e_t\mp i\vec e_x}{2},
\qquad
\mu_\pm=\pm i.
$$

The element is normal: $\vec Q\times\overline{\vec Q}=0$. The eigenbasis is the polar frame, and the common axis is $i\vec\Xi=\vec e_x$.

### The Checks

The norm is one; the Hermitian factor is the identity; the rotor is unitary. The true logarithm is

$$
\operatorname{Log}\tilde Q=\frac{\pi}{2}\vec e_x,
$$

and the formal exponent is the same, with defect $0$. The element is the exponential of a single pure vector, as the normal theorem predicts.

## Case 2: A Boost

### The Element

$$
\tilde Q=\sqrt2\,e_t+i\vec e_x=(1.41421356,i,0,0).
$$

$$
N=1,
\qquad
B^2=-1,
\qquad
\Rho=1,
\qquad
r=1,
\qquad
\alpha=0.
$$

### The Polar Factors

$$
\tilde U=\sqrt2\,e_t+i\vec e_x,
\qquad
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\vec e_x,
\qquad
\tilde u_{\mathrm r}=e_t.
$$

The rotor is the identity, with $\theta=0$ and an undefined axis. The boost is

$$
\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec e_x,
\qquad
\cosh\frac{\psi}{2}=\sqrt2,
\qquad
\sinh\frac{\psi}{2}=1,
$$

so $\psi=2\ln(1+\sqrt2)=1.762747174$ and $\vec u_{\mathrm b}=\vec e_x$.

### The Word

$$
\tilde Q=\exp\Bigl(i\frac{\psi}{2}\vec e_x\Bigr),
\qquad
\psi=2\ln(1+\sqrt2).
$$

### The Spectral Data

$$
\lambda_+=\sqrt2-1=0.414213562,
\qquad
\lambda_-=\sqrt2+1=2.41421356,
\qquad
\vec\Xi=-i\vec e_x,
\qquad
\mu_\pm=\lambda_\pm.
$$

The element is normal, and the eigenvalues of the unit factor are real and reciprocal. The common axis is $i\vec\Xi=\vec e_x$.

### The Checks

The true logarithm is

$$
\operatorname{Log}\tilde Q=i\frac{\psi}{2}\vec e_x=i\ln(1+\sqrt2)\vec e_x=i\,0.88137359\vec e_x,
$$

and the formal exponent is the same, with defect $0$.

## Case 3: A Boost Followed by a Rotor on the Same Axis

### The Element

$$
\tilde Q=\Bigl(1-\frac{i}{\sqrt2}\Bigr)e_t+\Bigl(1+\frac{i}{\sqrt2}\Bigr)\vec e_x
=(1-0.70710678i,\ 1+0.70710678i,\ 0,\ 0).
$$

$$
N=1,
\qquad
B^2=\frac12+i=0.5+1i,
\qquad
\Rho=1,
\qquad
r=1,
\qquad
\alpha=0.
$$

### The Polar Factors

$$
\tilde U=\tilde Q,
\qquad
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\vec e_x,
\qquad
\tilde u_{\mathrm r}=\frac{e_t+\vec e_x}{\sqrt2}.
$$

The Hermitian factor is the one of case 2, with $\psi=2\ln(1+\sqrt2)$ and $\vec u_{\mathrm b}=\vec e_x$. The rotor is the quarter-turn about $\vec e_x$, with $\theta=\frac{\pi}{2}$ and $\vec u_{\mathrm r}=\vec e_x$.

### The Word

$$
\tilde Q=\exp\Bigl(i\frac{\psi}{2}\vec e_x\Bigr)\exp\Bigl(\frac{\pi}{4}\vec e_x\Bigr)
=\exp\Bigl(\Bigl(\frac{\pi}{4}+i\frac{\psi}{2}\Bigr)\vec e_x\Bigr),
\qquad
\psi=2\ln(1+\sqrt2).
$$

The two axes are equal, so the word is a single exponential of the complex angle $\frac{\pi}{4}+i\ln(1+\sqrt2)$.

### The Spectral Data

$$
\lambda_+=\Bigl(1-\frac{1}{\sqrt2}\Bigr)(1+i)=0.292893219(1+i),
\qquad
\lambda_-=\Bigl(1+\frac{1}{\sqrt2}\Bigr)(1-i)=1.70710678(1-i),
\qquad
\vec\Xi=-i\vec e_x,
$$

$$
\mu_+=\lambda_+=0.414213562\,e^{i\pi/4},
\qquad
\mu_-=\lambda_-=2.41421356\,e^{-i\pi/4}.
$$

The element is normal. The eigenbasis is the polar frame, and the eigenvalues of the unit factor are

$$
\mu_\pm=e^{\mp\psi/2}e^{\pm i\theta/2},
\qquad
\psi=1.762747174,
\qquad
\theta=\frac{\pi}{2}.
$$

### The Checks

The true logarithm is

$$
\operatorname{Log}\tilde Q=\Bigl(\frac{\pi}{4}+i\ln(1+\sqrt2)\Bigr)\vec e_x
=(0.78539816+0.88137359i)\vec e_x,
$$

and the formal exponent is the same, with defect $0$. This is the clean normal case with both angles nonzero.

## Case 4: A Quarter-Turn Rotor

### The Element

$$
\tilde Q=\frac{e_t+\vec e_x}{\sqrt2}=(0.70710678,0.70710678,0,0).
$$

$$
N=1,
\qquad
B^2=\frac12,
\qquad
\Rho=1,
\qquad
r=1,
\qquad
\alpha=0.
$$

### The Polar Factors

$$
\tilde U=\tilde Q,
\qquad
\tilde U_{\mathrm b}=e_t,
\qquad
\tilde u_{\mathrm r}=\frac{e_t+\vec e_x}{\sqrt2}.
$$

The boost is the identity, with $\psi=0$. The rotor has $\theta=\frac{\pi}{2}$ and $\vec u_{\mathrm r}=\vec e_x$.

### The Spectral Data

$$
\lambda_\pm=\frac{1\pm i}{\sqrt2},
\qquad
\vec\Xi=-i\vec e_x,
\qquad
\mu_\pm=e^{\pm i\pi/4}.
$$

The element is normal, the axes are the same, and the eigenvalues of the unit factor have modulus one. The formula $\mu_\pm=e^{\mp\psi/2}e^{\pm i\theta/2}$ gives $e^{\pm i\pi/4}$.

### The Checks

The true logarithm is $\frac{\pi}{4}\vec e_x$, the formal exponent is the same, and the defect is $0$.

## Case 5: A Non-Normal Element with Orthogonal Axes

### The Element

$$
\tilde Q=\Bigl(1-\frac{i}{2}\Bigr)e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z
=(1-0.5i,\ 0.70710678+0.70710678i,\ 0.70710678,\ 0.5i).
$$

$$
N=1,
\qquad
B^2=\frac14+i=0.25+1i,
\qquad
\Rho=1,
\qquad
r=1,
\qquad
\alpha=0.
$$

### The Polar Factors

$$
\tilde U=\tilde Q,
\qquad
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\vec e_x,
\qquad
\tilde u_{\mathrm r}=0.70710678\,e_t+0.5\,\vec e_x+0.5\,\vec e_y
=\frac{e_t}{\sqrt2}+\frac{\vec e_x+\vec e_y}{2}.
$$

Its scalar part is $1/\sqrt2=\cos\frac{\pi}{4}$, so $\theta=\frac{\pi}{2}$, and its vector part is $\frac12(\vec e_x+\vec e_y)=\frac{1}{\sqrt2}\frac{\vec e_x+\vec e_y}{\sqrt2}$, so $\vec u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt2}$. The boost is the one of case 2, with $\psi=1.762747174$ and $\vec u_{\mathrm b}=\vec e_x$. The angle between the axes is

$$
c=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=\frac{1}{\sqrt2}.
$$

### The Word

$$
\tilde Q=\exp\Bigl(i\frac{\psi}{2}\vec e_x\Bigr)
\exp\Bigl(\frac{\pi}{4}\frac{\vec e_x+\vec e_y}{\sqrt2}\Bigr),
\qquad
\psi=2\ln(1+\sqrt2).
$$

The two axes are neither parallel nor antiparallel, and both angles are nonzero. The element is non-normal:

$$
\vec Q\times\overline{\vec Q}
=\Bigl(-\frac{i}{\sqrt2},\frac{i}{\sqrt2},i\Bigr)\neq0.
$$

### The Spectral Data

$$
\vec\Xi=-i\frac{\vec Q}{B},
\qquad
\lambda_+=0.375189466+0.30024259i,
\qquad
\lambda_-=1.62481053-1.30024259i,
$$

$$
\mu_+=0.480533816\,e^{+0.674888846i},
\qquad
\mu_-=2.081019\,e^{-0.674888846i}.
$$

The eigenbasis is not the polar frame. The common-axis formula fails: the moduli of $\mu_\pm$ are not $e^{\mp\psi/2}$, and the arguments are not $\pm\theta/2$.

### The Spectral Gap

The normal-case reading would give

$$
\psi_{\mathrm{spec}}=\ln\frac{2.081019}{0.480533816}=1.4657,
\qquad
\theta_{\mathrm{spec}}=2(0.674888846)=1.3498,
$$

while the true word has

$$
\psi=1.7627,
\qquad
\theta=1.5708.
$$

The spectrum is the same; the rapidity and the rotor angle are not. The gap is a measurement of the non-normality, not a rounding error.

### The Checks

The true logarithm is

$$
\operatorname{Log}\tilde Q
=(0.57156069+0.79764558i)\vec e_x
+(0.68460314+0.11304245i)\vec e_y
+(-0.07993308+0.48408752i)\vec e_z,
$$

and the formal exponent is

$$
\tilde Q_{\log}
=(0.55536037+0.88137359i)\vec e_x+0.55536037\vec e_y.
$$

The exponential of the formal exponent misses the element by $0.5$. The commutator $[\tilde U_{\mathrm b},\tilde Q]$ has norm $1.41$, so the polar factors are not diagonal in the eigenbasis.

## Case 6: A Generic Non-Normal Element

### The Element

$$
\tilde Q=(1+i)e_t+(1+i)\vec e_x+\vec e_y+\frac12\vec e_z
=(1+i,\ 1+i,\ 1,\ 0.5).
$$

$$
N=1.25+4i,
\qquad
B^2=1.25+2i,
\qquad
\Rho=1.649358004+1.212593018i,
\qquad
r=2.047135475,
\qquad
\alpha=0.6339557292.
$$

### The Polar Factors

$$
\tilde U=0.68291874+0.10422086i
+(0.68291874+0.10422086i)\vec e_x
+(0.39356980-0.28934894i)\vec e_y
+(0.19678490-0.14467447i)\vec e_z,
$$

$$
\tilde U_{\mathrm b}=1.06130933\,e_t-i0.11241774\,\vec e_y-i0.33725322\,\vec e_z,
$$

$$
\tilde u_{\mathrm r}=0.64346814\,e_t+0.64346814\,\vec e_x+0.37083420\,\vec e_y+0.18541710\,\vec e_z.
$$

The word has

$$
\psi=0.696809291,
\qquad
\vec u_{\mathrm b}=(0,-0.316227766,-0.948683298),
\qquad
\theta=1.743551853,
\qquad
\vec u_{\mathrm r}=(0.840615184,0.484451122,0.242225561),
$$

and

$$
c=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=-0.382992240.
$$

### The Spectral Data

$$
\lambda_+=0.2555219+2.34322286i,
\qquad
\lambda_-=1.7444781-0.343222856i,
$$

$$
\mu_+=1.15142045\,e^{+0.828222573i},
\qquad
\mu_-=0.868492475\,e^{-0.828222573i}.
$$

The element is non-normal:

$$
\vec Q\times\overline{\vec Q}=(0,-i,2i)\neq0.
$$

### The Spectral Gap

The normal-case reading would give

$$
\psi_{\mathrm{spec}}=\bigl\lvert\ln\frac{0.868492475}{1.15142045}\bigr\rvert=0.2820,
\qquad
\theta_{\mathrm{spec}}=2(0.828222573)=1.6564,
$$

while the true word has $\psi=0.6968$ and $\theta=1.7436$. The gap is larger than in case 5, because the axes are farther from parallel.

### The Checks

The true logarithm is

$$
\operatorname{Log}\tilde Q
=(0.71644149+0.63395573i)e_t
+(0.76892326+0.08545096i)\vec e_x
+(0.42718711-0.34173615i)\vec e_y
+(0.21359356-0.17086807i)\vec e_z,
$$

and the formal exponent is

$$
\tilde Q_{\log}
=(0.71644149+0.63395573i)e_t
+0.73282808\vec e_x
+(0.42233283-0.11017522i)\vec e_y
+(0.21116641-0.33052567i)\vec e_z.
$$

The exponential of the formal exponent misses the element by $0.4222$. The commutator $[\tilde U_{\mathrm b},\tilde Q]$ has norm $0.954$.

## Case 7: A Normal Element with a Complex Phase

### The Element

$$
\tilde Q=(1+i)(e_t+\vec e_x)=(1+i,\ 1+i,\ 0,\ 0).
$$

$$
N=4i,
\qquad
B^2=2i,
\qquad
\Rho=\sqrt2(1+i),
\qquad
r=2,
\qquad
\alpha=\frac{\pi}{4}.
$$

### The Polar Factors

$$
\tilde U=\frac{e_t+\vec e_x}{\sqrt2},
\qquad
\tilde U_{\mathrm b}=e_t,
\qquad
\tilde u_{\mathrm r}=\frac{e_t+\vec e_x}{\sqrt2}.
$$

The element is the phase $2e^{i\pi/4}$ times the quarter-turn rotor. The boost is the identity, with $\psi=0$; the rotor has $\theta=\frac{\pi}{2}$ and $\vec u_{\mathrm r}=\vec e_x$.

### The Spectral Data

$$
\lambda_+=2i,
\qquad
\lambda_-=2,
\qquad
\vec\Xi=-i\vec e_x,
\qquad
\mu_\pm=e^{\pm i\pi/4}.
$$

The element is normal. The eigenvalues of $\tilde Q$ have modulus $2$, and the eigenvalues of the unit factor have modulus one.

### The Checks

The true logarithm is

$$
\operatorname{Log}\tilde Q=\ln2+i\frac{\pi}{4}+i\frac{\pi}{4}\vec e_x
=(0.69314718+0.78539816i)e_t+0.78539816\vec e_x,
$$

and the formal exponent is the same, with defect $0$. This case shows that the phase and the rotor angle add in the scalar and the vector parts independently.

## Case 8: A Pure Vector

### The Element

$$
\tilde Q=\vec e_x+\vec e_y=(0,1,1,0).
$$

$$
N=2,
\qquad
B^2=2,
\qquad
\Rho=\sqrt2,
\qquad
r=\sqrt2,
\qquad
\alpha=0.
$$

### The Polar Factors

$$
\tilde U=\frac{\vec e_x+\vec e_y}{\sqrt2},
\qquad
\tilde U_{\mathrm b}=e_t,
\qquad
\tilde u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt2}.
$$

The boost is the identity, with $\psi=0$. The rotor is a half-turn about the diagonal, with $\theta=\pi$ and $\vec u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt2}$.

### The Spectral Data

$$
\lambda_+=i\sqrt2,
\qquad
\lambda_-=-i\sqrt2,
\qquad
\vec\Xi=-\frac{i}{\sqrt2}(\vec e_x+\vec e_y),
\qquad
\mu_\pm=\pm i.
$$

The element is normal. The eigenbasis is the polar frame, and the common axis is $i\vec\Xi=\frac{\vec e_x+\vec e_y}{\sqrt2}$.

### The Checks

The true logarithm is

$$
\operatorname{Log}\tilde Q=\ln\sqrt2+\frac{\pi}{2}\frac{\vec e_x+\vec e_y}{\sqrt2}
=0.34657359\,e_t+1.11072073(\vec e_x+\vec e_y),
$$

and the formal exponent is the same, with defect $0$.

## The Comparison

### The Normal Cases

| Case | Element | $\psi$ | $\theta$ | Axes | Defect |
|---|---|---|---|---|---|
| 1 | $\vec e_x$ | $0$ | $\pi$ | undefined, $\vec e_x$ | $0$ |
| 2 | $\sqrt2e_t+i\vec e_x$ | $2\ln(1+\sqrt2)$ | $0$ | $\vec e_x$, undefined | $0$ |
| 3 | $(1-\frac{i}{\sqrt2})e_t+(1+\frac{i}{\sqrt2})\vec e_x$ | $2\ln(1+\sqrt2)$ | $\frac{\pi}{2}$ | $\vec e_x$, $\vec e_x$ | $0$ |
| 4 | $\frac{e_t+\vec e_x}{\sqrt2}$ | $0$ | $\frac{\pi}{2}$ | undefined, $\vec e_x$ | $0$ |
| 7 | $(1+i)(e_t+\vec e_x)$ | $0$ | $\frac{\pi}{2}$ | undefined, $\vec e_x$ | $0$ |
| 8 | $\vec e_x+\vec e_y$ | $0$ | $\pi$ | undefined, $\frac{\vec e_x+\vec e_y}{\sqrt2}$ | $0$ |

In every normal case the formal exponent is a logarithm, the axes coincide when both are defined, and the eigenvalues of the unit factor are $e^{\mp\psi/2}e^{\pm i\theta/2}$.

### The Non-Normal Cases

| Case | Element | $\psi$ | $\theta$ | $c$ | $\psi_{\mathrm{spec}}$ | $\theta_{\mathrm{spec}}$ | Defect |
|---|---|---|---|---|---|---|---|
| 5 | $1-\frac{i}{2}+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z$ | $1.7627$ | $1.5708$ | $0.7071$ | $1.4657$ | $1.3498$ | $0.5000$ |
| 6 | $(1+i)(e_t+\vec e_x)+\vec e_y+\frac12\vec e_z$ | $0.6968$ | $1.7436$ | $-0.3830$ | $0.2820$ | $1.6564$ | $0.4222$ |

The two columns $\psi_{\mathrm{spec}},\theta_{\mathrm{spec}}$ are the values extracted from the eigenvalues of the unit factor by the normal-case formulas. They disagree with the true word in both cases. The defect is nonzero in both.

### The Eigenvalues of the Unit Factor

| Case | $\mu_+$ | $\mu_-$ | $\lvert\mu_+\rvert$ | $\arg\mu_+$ |
|---|---|---|---|---|
| 1 | $i$ | $-i$ | $1$ | $\frac{\pi}{2}$ |
| 2 | $0.414213562$ | $2.41421356$ | $0.414213562$ | $0$ |
| 3 | $0.414213562e^{i\pi/4}$ | $2.41421356e^{-i\pi/4}$ | $0.414213562$ | $\frac{\pi}{4}$ |
| 4 | $e^{i\pi/4}$ | $e^{-i\pi/4}$ | $1$ | $\frac{\pi}{4}$ |
| 5 | $0.480533816e^{0.674888846i}$ | $2.081019e^{-0.674888846i}$ | $0.480533816$ | $0.674888846$ |
| 6 | $1.15142045e^{0.828222573i}$ | $0.868492475e^{-0.828222573i}$ | $1.15142045$ | $0.828222573$ |
| 7 | $e^{i\pi/4}$ | $e^{-i\pi/4}$ | $1$ | $\frac{\pi}{4}$ |
| 8 | $i$ | $-i$ | $1$ | $\frac{\pi}{2}$ |

The table is the numerical form of the spectral reading. In cases 1 to 4, 7 and 8 the moduli and arguments are $e^{\mp\psi/2}$ and $\pm\theta/2$. In cases 5 and 6 they are not.

## Summary

### The Cases

| Case | $\tilde Q$ | $N$ | $B^2$ | $\Rho$ | Normal |
|---|---|---|---|---|---|
| 1 | $\vec e_x$ | $1$ | $1$ | $1$ | yes |
| 2 | $\sqrt2e_t+i\vec e_x$ | $1$ | $-1$ | $1$ | yes |
| 3 | $(1-\frac{i}{\sqrt2})e_t+(1+\frac{i}{\sqrt2})\vec e_x$ | $1$ | $\frac12+i$ | $1$ | yes |
| 4 | $\frac{e_t+\vec e_x}{\sqrt2}$ | $1$ | $\frac12$ | $1$ | yes |
| 5 | $1-\frac{i}{2}+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z$ | $1$ | $\frac14+i$ | $1$ | no |
| 6 | $(1+i)(e_t+\vec e_x)+\vec e_y+\frac12\vec e_z$ | $1.25+4i$ | $1.25+2i$ | $1.649+1.213i$ | no |
| 7 | $(1+i)(e_t+\vec e_x)$ | $4i$ | $2i$ | $\sqrt2(1+i)$ | yes |
| 8 | $\vec e_x+\vec e_y$ | $2$ | $2$ | $\sqrt2$ | yes |

### The Word Data

| Case | $r$ | $\alpha$ | $\psi$ | $\vec u_{\mathrm b}$ | $\theta$ | $\vec u_{\mathrm r}$ |
|---|---|---|---|---|---|---|
| 1 | $1$ | $0$ | $0$ | -- | $\pi$ | $\vec e_x$ |
| 2 | $1$ | $0$ | $1.762747174$ | $\vec e_x$ | $0$ | -- |
| 3 | $1$ | $0$ | $1.762747174$ | $\vec e_x$ | $\frac{\pi}{2}$ | $\vec e_x$ |
| 4 | $1$ | $0$ | $0$ | -- | $\frac{\pi}{2}$ | $\vec e_x$ |
| 5 | $1$ | $0$ | $1.762747174$ | $\vec e_x$ | $\frac{\pi}{2}$ | $\frac{\vec e_x+\vec e_y}{\sqrt2}$ |
| 6 | $2.047135$ | $0.633956$ | $0.696809$ | $(0,-0.3162,-0.9487)$ | $1.743552$ | $(0.8406,0.4845,0.2422)$ |
| 7 | $2$ | $\frac{\pi}{4}$ | $0$ | -- | $\frac{\pi}{2}$ | $\vec e_x$ |
| 8 | $\sqrt2$ | $0$ | $0$ | -- | $\pi$ | $\frac{\vec e_x+\vec e_y}{\sqrt2}$ |

### What the Examples Show

- The word exists in every case, with $N\neq0$ and $B^2\neq0$.
- In the normal cases the axes coincide when both are defined, the word is a single exponential, the formal exponent is the logarithm, and the spectrum gives the two angles by $\psi=\ln\lvert\mu_-/\mu_+\rvert$ and $\theta=2\arg\mu_+$.
- In the non-normal cases the axes are not the eigenlines, the formal exponent is not the logarithm, the defect is positive, and the spectrum does not give the two angles. The gap is visible in the table: $1.4657$ against $1.7627$ in case 5, and $0.2820$ against $0.6968$ in case 6.
- The two factors commute with the element exactly in the normal cases; the norm of the commutator is zero there and $1.41$ and $0.954$ in the two non-normal cases.
- The eigenvalues of the unit factor are the same function of $U_t$ in all cases; what changes is whether the word's angles can be read from them.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q$ | the element of the case |
| $N$ | the reduced product |
| $B^2$ | the vector form |
| $\Rho$ | the modulus, principal square root of $N$ |
| $r,\alpha$ | the polar coordinates of $\Rho$ |
| $\tilde U$ | the unit factor |
| $\tilde U_{\mathrm b}$ | the Hermitian positive factor |
| $\tilde u_{\mathrm r}$ | the rotor |
| $\psi,\vec u_{\mathrm b}$ | the rapidity and the boost axis |
| $\theta,\vec u_{\mathrm r}$ | the rotor angle and the rotor axis |
| $c$ | the cosine between the axes |
| $\lambda_\pm$ | the eigenvalues of $\tilde Q$ |
| $\vec\Xi$ | the root of one, $-i\vec Q/B$ |
| $\tilde\Pi_\pm$ | the spectral idempotents |
| $\mu_\pm$ | the eigenvalues of the unit factor |
| $\tilde Q_{\log}$ | the formal exponent |
| $\delta$ | the defect of the case |

## Further Reading

- [Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html), for the theorem, the proofs and the spectral reading.
- [Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html), for the companion sector and its worked examples.
- [Worked Examples of Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](worked-examples-of-exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html), for the degenerate cases.
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the modulus–unit theorem.
- [The Spectrally Regular Sector and Construction of the Eigenbasis of a Biquaternion](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), for the eigenbasis and the spectral idempotents.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation.
