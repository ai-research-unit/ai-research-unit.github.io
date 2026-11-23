# __Worked Examples of the Complete Polar Decomposition of an N-Regular Biquaternion__

## Introduction

This article works sixteen numerical cases of the exponential form of the complete polar decomposition in the N-regular sector. Eight are off the wall, with $B^2\neq0$; eight are on it, with $B^2=0$. Every case is an element

$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,
\qquad
N=Q_t^2+Q_x^2+Q_y^2+Q_z^2\neq0,
$$

written as the four-factor word

$$
\tilde Q=\varrho\,e^{i\theta_{\mathrm{pha}}}\,
\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr)
\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
$$

and, on the wall, also in the normal form $\tilde Q=Q_t(e_t+\vec\Pi_{\mathrm{nil}})$ with $\vec\Pi_{\mathrm{nil}}^2=0$.

The two groups display the two shapes of the same word. Off the wall the cases split into the normal elements, where the two axes are parallel and the word is one exponential, and the non-normal elements, where the axes are not the eigenlines and the spectrum does not determine the rapidity and the rotor angle. On the wall the cases split into the scalar line, where the unit factor is $\pm e_t$, and the Jordan part, where it is $\pm(e_t+\vec\Pi_{\mathrm{nil}})$ with $\vec\Pi_{\mathrm{nil}}\neq0$, the two axes are orthogonal, and the rapidity is a function of the rotor angle.

The numbering runs from $1$ to $8$ off the wall and from $9$ to $16$ on it; every table and every defect refers to that numbering. The numbers are rounded to eight or nine significant digits, and the computations were carried to double precision.

**The plan.** §*Conventions and Recipes* fixes the notation, the recipe and the checks for both groups. §§*Case 1* to *Case 8* treat the elements off the wall, grouped by their normal or non-normal character. §*On the Wall* treats the eight elements of the wall, the three of the scalar line first and the five of the Jordan part after. §*The Comparison* collects the words, the constraints, the logarithms and the defects of both groups. The summary gives the tables.

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

The notation is the one of *Algebra and Element Conventions*.

### The Recipe

Given $\tilde Q$:

1. Compute $N$ and $B^2=Q_x^2+Q_y^2+Q_z^2$. Every case has $N\neq0$; the cases off the wall have $B^2\neq0$ and the cases on the wall have $B^2=0$.
2. Compute the modulus $\varrho\,e^{i\theta_{\mathrm{pha}}}$, the principal square root of $N$, and write $\varrho\,e^{i\theta_{\mathrm{pha}}}=\varrho e^{i\theta_{\mathrm{pha}}}$ with $\varrho>0$ and $\theta_{\mathrm{pha}}\in(-\frac{\pi}{2},\frac{\pi}{2}]$.
3. Off the wall, compute the unit factor $\tilde U=\tilde Q/(\varrho\,e^{i\theta_{\mathrm{pha}}})$. On the wall, compute the scalar part $Q_t$, the nilpotent direction $\vec\Pi_{\mathrm{nil}}=\vec Q/Q_t$, the sign $\varepsilon=Q_t/(\varrho\,e^{i\theta_{\mathrm{pha}}})=\pm1$ and the unit factor $\tilde U=\varepsilon(e_t+\vec\Pi_{\mathrm{nil}})$, and check $\vec\Pi_{\mathrm{nil}}^2=0$.
4. Compute the Hermitian factor $\tilde U_{\mathrm b}=(\tilde U\tilde U^*)^{1/2}$, positive of norm one, and the rotor $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$.
5. Read the boost angle and axis from $\tilde U_{\mathrm b}=c_{\mathrm b}e_t+i s_{\mathrm b}\vec u_{\mathrm b}$, and the rotor angle and axis from $\tilde u_{\mathrm r}=c_{\mathrm r}e_t+s_{\mathrm r}\vec u_{\mathrm r}$.
6. Check $\tilde Q=\varrho e^{i\theta_{\mathrm{pha}}}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ and $\langle\tilde U\rangle_{\natural}=1$.
7. Off the wall, compute the eigen-data: $\lambda_\pm=Q_t\pm iB$, $\vec{Ζ}=-i\vec Q/B$, $\tilde\Pi_{\mathrm{id},\pm}=\frac12(e_t\pm\vec{Ζ})$, and $\mu_\pm=\lambda_\pm/(\varrho\,e^{i\theta_{\mathrm{pha}}})$.
8. On the wall, check the constraints $c_{\mathrm b}c_{\mathrm r}=\varepsilon$ and $s_{\mathrm b}s_{\mathrm r}c=0$, with $c=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$, and compute the exact logarithm $\log Q_t+\vec\Pi_{\mathrm{nil}}$.
9. Compute the true logarithm by the matrix logarithm, and compare its exponential with $\tilde Q$. On the wall the exact logarithm plays that role.
10. Compute the formal exponent and its defect, in both groups.

The **defect** of a case is

$$
\delta=\bigl\lVert\exp(\tilde Q_{\log})-\tilde Q\bigr\rVert,
\qquad
\tilde Q_{\log}=\ln \varrho+i\theta_{\mathrm{pha}}+i\frac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}+\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r},
$$

where the norm is the maximum modulus of the four coordinates. Off the wall it is zero exactly in the normal cases and positive in the non-normal ones. On the wall it is zero on the scalar line and positive on the Jordan part.

### The Checks

The following identities hold in every case and are used below without comment.

| Identity | Meaning |
|---|---|
| $\langle\tilde U\rangle_{\natural}=1$ | the unit factor has norm one |
| $\tilde U_{\mathrm b}^*=\tilde U_{\mathrm b}$, $\langle\tilde U_{\mathrm b}\rangle_{\natural}=1$ | the Hermitian factor is positive of norm one |
| $\tilde u_{\mathrm r}^*=\tilde u_{\mathrm r}^{-1}$, $\langle\tilde u_{\mathrm r}\rangle_{\natural}=1$ | the rotor is $*$-unitary of norm one |
| $\tilde Q=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U$ | the modulus–unit split |
| $[\tilde Q,\tilde Q^*]=-2\vec Q\times\overline{\vec Q}$ | normality, off the wall |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues, off the wall |
| $\mu_\pm=\lambda_\pm/(\varrho\,e^{i\theta_{\mathrm{pha}}})$ | the eigenvalues of the unit factor, off the wall |
| $\tilde Q=Q_t(e_t+\vec\Pi_{\mathrm{nil}})$, $\vec\Pi_{\mathrm{nil}}^2=0$ | the normal form, on the wall |
| $\tilde U=\varepsilon(e_t+\vec\Pi_{\mathrm{nil}})$, $(\tilde U-\varepsilon e_t)^2=0$ | the unit factor on the wall is $\pm$unipotent |
| $\cosh\frac{\theta_{\mathrm{rpd}}}{2}\cos\frac{\theta_{\mathrm{axr}}}{2}=\varepsilon$ | the scalar constraint, on the wall |
| $\sinh\frac{\theta_{\mathrm{rpd}}}{2}\sin\frac{\theta_{\mathrm{axr}}}{2}\,c=0$ | the axis constraint, on the wall |
| $\operatorname{Log}\tilde Q=\log Q_t+\vec\Pi_{\mathrm{nil}}$ | the exact logarithm, on the wall |

## Off the Wall

The eight cases of this group have $B^2\neq0$. Cases $1$ to $4$ and $7$ to $8$ are normal: the element commutes with its star conjugate, the two axes coincide when both are defined, and the formal exponent is a logarithm. Cases $5$ and $6$ are non-normal, and they are the ones that show the gap between the spectrum and the word.

### Case 1: A Rotor

#### The Element

$$
\tilde Q=\vec e_x=(0,1,0,0).
$$

$$
N=1,
\qquad
B^2=1,
\qquad
\varrho\,e^{i\theta_{\mathrm{pha}}}=1,
\qquad
\varrho=1,
\qquad
\theta_{\mathrm{pha}}=0.
$$

#### The Polar Factors

$$
\tilde U=\vec e_x,
\qquad
\tilde U_{\mathrm b}=e_t,
\qquad
\tilde u_{\mathrm r}=\vec e_x.
$$

The boost is the identity, with $\theta_{\mathrm{rpd}}=0$ and an undefined axis. The rotor is

$$
\tilde u_{\mathrm r}=\vec e_x=\exp\Bigl(\frac{\pi}{2}\vec e_x\Bigr),
$$

so $\theta_{\mathrm{axr}}=\pi$ and $\vec u_{\mathrm r}=\vec e_x$.

#### The Word

$$
\tilde Q=\exp\Bigl(\frac{\pi}{2}\vec e_x\Bigr).
$$

The word has $\varrho=1$, $\theta_{\mathrm{pha}}=0$, $\theta_{\mathrm{rpd}}=0$, $\theta_{\mathrm{axr}}=\pi$, $\vec u_{\mathrm r}=\vec e_x$.

#### The Spectral Data

$$
\lambda_+=i,
\qquad
\lambda_-=-i,
\qquad
\vec{Ζ}=-i\vec e_x,
\qquad
\tilde\Pi_{\mathrm{id},\pm}=\frac{e_t\mp i\vec e_x}{2},
\qquad
\mu_\pm=\pm i.
$$

The element is normal: $\vec Q\times\overline{\vec Q}=0$. The eigenbasis is the polar frame, and the common axis is $i\vec{Ζ}=\vec e_x$.

#### The Checks

The norm is one; the Hermitian factor is the identity; the rotor is $*$-unitary. The true logarithm is

$$
\operatorname{Log}\tilde Q=\frac{\pi}{2}\vec e_x,
$$

and the formal exponent is the same, with defect $0$. The element is the exponential of a single pure vector, as the normal theorem predicts.
### Case 2: A Boost

#### The Element

$$
\tilde Q=\sqrt2\,e_t+i\vec e_x=(1.41421356,i,0,0).
$$

$$
N=1,
\qquad
B^2=-1,
\qquad
\varrho\,e^{i\theta_{\mathrm{pha}}}=1,
\qquad
\varrho=1,
\qquad
\theta_{\mathrm{pha}}=0.
$$

#### The Polar Factors

$$
\tilde U=\sqrt2\,e_t+i\vec e_x,
\qquad
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\vec e_x,
\qquad
\tilde u_{\mathrm r}=e_t.
$$

The rotor is the identity, with $\theta_{\mathrm{axr}}=0$ and an undefined axis. The boost is

$$
\tilde U_{\mathrm b}=\cosh\frac{\theta_{\mathrm{rpd}}}{2}e_t+i\sinh\frac{\theta_{\mathrm{rpd}}}{2}\vec e_x,
\qquad
\cosh\frac{\theta_{\mathrm{rpd}}}{2}=\sqrt2,
\qquad
\sinh\frac{\theta_{\mathrm{rpd}}}{2}=1,
$$

so $\theta_{\mathrm{rpd}}=2\ln(1+\sqrt2)=1.762747174$ and $\vec u_{\mathrm b}=\vec e_x$.

#### The Word

$$
\tilde Q=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec e_x\Bigr),
\qquad
\theta_{\mathrm{rpd}}=2\ln(1+\sqrt2).
$$

#### The Spectral Data

$$
\lambda_+=\sqrt2-1=0.414213562,
\qquad
\lambda_-=\sqrt2+1=2.41421356,
\qquad
\vec{Ζ}=-i\vec e_x,
\qquad
\mu_\pm=\lambda_\pm.
$$

The element is normal, and the eigenvalues of the unit factor are real and reciprocal. The common axis is $i\vec{Ζ}=\vec e_x$.

#### The Checks

The true logarithm is

$$
\operatorname{Log}\tilde Q=i\frac{\theta_{\mathrm{rpd}}}{2}\vec e_x=i\ln(1+\sqrt2)\vec e_x=i\,0.88137359\vec e_x,
$$

and the formal exponent is the same, with defect $0$.
### Case 3: A Boost Followed by a Rotor on the Same Axis

#### The Element

$$
\tilde Q=\Bigl(1-\frac{i}{\sqrt2}\Bigr)e_t+\Bigl(1+\frac{i}{\sqrt2}\Bigr)\vec e_x
=(1-0.70710678i,\ 1+0.70710678i,\ 0,\ 0).
$$

$$
N=1,
\qquad
B^2=\frac12+i=0.5+1i,
\qquad
\varrho\,e^{i\theta_{\mathrm{pha}}}=1,
\qquad
\varrho=1,
\qquad
\theta_{\mathrm{pha}}=0.
$$

#### The Polar Factors

$$
\tilde U=\tilde Q,
\qquad
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\vec e_x,
\qquad
\tilde u_{\mathrm r}=\frac{e_t+\vec e_x}{\sqrt2}.
$$

The Hermitian factor is the one of case 2, with $\theta_{\mathrm{rpd}}=2\ln(1+\sqrt2)$ and $\vec u_{\mathrm b}=\vec e_x$. The rotor is the quarter-turn about $\vec e_x$, with $\theta_{\mathrm{axr}}=\frac{\pi}{2}$ and $\vec u_{\mathrm r}=\vec e_x$.

#### The Word

$$
\tilde Q=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec e_x\Bigr)\exp\Bigl(\frac{\pi}{4}\vec e_x\Bigr)
=\exp\Bigl(\Bigl(\frac{\pi}{4}+i\frac{\theta_{\mathrm{rpd}}}{2}\Bigr)\vec e_x\Bigr),
\qquad
\theta_{\mathrm{rpd}}=2\ln(1+\sqrt2).
$$

The two axes are equal, so the word is a single exponential of the complex angle $\frac{\pi}{4}+i\ln(1+\sqrt2)$.

#### The Spectral Data

$$
\lambda_+=\Bigl(1-\frac{1}{\sqrt2}\Bigr)(1+i)=0.292893219(1+i),
\qquad
\lambda_-=\Bigl(1+\frac{1}{\sqrt2}\Bigr)(1-i)=1.70710678(1-i),
\qquad
\vec{Ζ}=-i\vec e_x,
$$

$$
\mu_+=\lambda_+=0.414213562\,e^{i\pi/4},
\qquad
\mu_-=\lambda_-=2.41421356\,e^{-i\pi/4}.
$$

The element is normal. The eigenbasis is the polar frame, and the eigenvalues of the unit factor are

$$
\mu_\pm=e^{\mp\theta_{\mathrm{rpd}}/2}e^{\pm i\theta_{\mathrm{axr}}/2},
\qquad
\theta_{\mathrm{rpd}}=1.762747174,
\qquad
\theta_{\mathrm{axr}}=\frac{\pi}{2}.
$$

#### The Checks

The true logarithm is

$$
\operatorname{Log}\tilde Q=\Bigl(\frac{\pi}{4}+i\ln(1+\sqrt2)\Bigr)\vec e_x
=(0.78539816+0.88137359i)\vec e_x,
$$

and the formal exponent is the same, with defect $0$. This is the clean normal case with both angles nonzero.
### Case 4: A Quarter-Turn Rotor

#### The Element

$$
\tilde Q=\frac{e_t+\vec e_x}{\sqrt2}=(0.70710678,0.70710678,0,0).
$$

$$
N=1,
\qquad
B^2=\frac12,
\qquad
\varrho\,e^{i\theta_{\mathrm{pha}}}=1,
\qquad
\varrho=1,
\qquad
\theta_{\mathrm{pha}}=0.
$$

#### The Polar Factors

$$
\tilde U=\tilde Q,
\qquad
\tilde U_{\mathrm b}=e_t,
\qquad
\tilde u_{\mathrm r}=\frac{e_t+\vec e_x}{\sqrt2}.
$$

The boost is the identity, with $\theta_{\mathrm{rpd}}=0$. The rotor has $\theta_{\mathrm{axr}}=\frac{\pi}{2}$ and $\vec u_{\mathrm r}=\vec e_x$.

#### The Spectral Data

$$
\lambda_\pm=\frac{1\pm i}{\sqrt2},
\qquad
\vec{Ζ}=-i\vec e_x,
\qquad
\mu_\pm=e^{\pm i\pi/4}.
$$

The element is normal, the axes are the same, and the eigenvalues of the unit factor have modulus one. The formula $\mu_\pm=e^{\mp\theta_{\mathrm{rpd}}/2}e^{\pm i\theta_{\mathrm{axr}}/2}$ gives $e^{\pm i\pi/4}$.

#### The Checks

The true logarithm is $\frac{\pi}{4}\vec e_x$, the formal exponent is the same, and the defect is $0$.
### Case 5: A Non-Normal Element with Orthogonal Axes

#### The Element

$$
\tilde Q=\Bigl(1-\frac{i}{2}\Bigr)e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z
=(1-0.5i,\ 0.70710678+0.70710678i,\ 0.70710678,\ 0.5i).
$$

$$
N=1,
\qquad
B^2=\frac14+i=0.25+1i,
\qquad
\varrho\,e^{i\theta_{\mathrm{pha}}}=1,
\qquad
\varrho=1,
\qquad
\theta_{\mathrm{pha}}=0.
$$

#### The Polar Factors

$$
\tilde U=\tilde Q,
\qquad
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\vec e_x,
\qquad
\tilde u_{\mathrm r}=0.70710678\,e_t+0.5\,\vec e_x+0.5\,\vec e_y
=\frac{e_t}{\sqrt2}+\frac{\vec e_x+\vec e_y}{2}.
$$

Its scalar part is $1/\sqrt2=\cos\frac{\pi}{4}$, so $\theta_{\mathrm{axr}}=\frac{\pi}{2}$, and its vector part is $\frac12(\vec e_x+\vec e_y)=\frac{1}{\sqrt2}\frac{\vec e_x+\vec e_y}{\sqrt2}$, so $\vec u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt2}$. The boost is the one of case 2, with $\theta_{\mathrm{rpd}}=1.762747174$ and $\vec u_{\mathrm b}=\vec e_x$. The angle between the axes is

$$
c=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=\frac{1}{\sqrt2}.
$$

#### The Word

$$
\tilde Q=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec e_x\Bigr)
\exp\Bigl(\frac{\pi}{4}\frac{\vec e_x+\vec e_y}{\sqrt2}\Bigr),
\qquad
\theta_{\mathrm{rpd}}=2\ln(1+\sqrt2).
$$

The two axes are neither parallel nor antiparallel, and both angles are nonzero. The element is non-normal:

$$
\vec Q\times\overline{\vec Q}
=\Bigl(-\frac{i}{\sqrt2},\frac{i}{\sqrt2},i\Bigr)\neq0.
$$

#### The Spectral Data

$$
\vec{Ζ}=-i\frac{\vec Q}{B},
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

The eigenbasis is not the polar frame. The common-axis formula fails: the moduli of $\mu_\pm$ are not $e^{\mp\theta_{\mathrm{rpd}}/2}$, and the arguments are not $\pm\theta_{\mathrm{axr}}/2$.

#### The Spectral Gap

The normal-case reading would give

$$
\theta_{\mathrm{rpd},\mathrm{spec}}=\ln\frac{2.081019}{0.480533816}=1.4657,
\qquad
\theta_{\mathrm{spec}}=2(0.674888846)=1.3498,
$$

while the true word has

$$
\theta_{\mathrm{rpd}}=1.7627,
\qquad
\theta_{\mathrm{axr}}=1.5708.
$$

The spectrum is the same; the rapidity and the rotor angle are not. The gap is a measurement of the non-normality, not a rounding error.

#### The Checks

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
### Case 6: A Generic Non-Normal Element

#### The Element

$$
\tilde Q=(1+i)e_t+(1+i)\vec e_x+\vec e_y+\frac12\vec e_z
=(1+i,\ 1+i,\ 1,\ 0.5).
$$

$$
N=1.25+4i,
\qquad
B^2=1.25+2i,
\qquad
\varrho\,e^{i\theta_{\mathrm{pha}}}=1.649358004+1.212593018i,
\qquad
\varrho=2.047135475,
\qquad
\theta_{\mathrm{pha}}=0.6339557292.
$$

#### The Polar Factors

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
\theta_{\mathrm{rpd}}=0.696809291,
\qquad
\vec u_{\mathrm b}=(0,-0.316227766,-0.948683298),
\qquad
\theta_{\mathrm{axr}}=1.743551853,
\qquad
\vec u_{\mathrm r}=(0.840615184,0.484451122,0.242225561),
$$

and

$$
c=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=-0.382992240.
$$

#### The Spectral Data

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

#### The Spectral Gap

The normal-case reading would give

$$
\theta_{\mathrm{rpd},\mathrm{spec}}=\bigl\lvert\ln\frac{0.868492475}{1.15142045}\bigr\rvert=0.2820,
\qquad
\theta_{\mathrm{spec}}=2(0.828222573)=1.6564,
$$

while the true word has $\theta_{\mathrm{rpd}}=0.6968$ and $\theta_{\mathrm{axr}}=1.7436$. The gap is larger than in case 5, because the axes are farther from parallel.

#### The Checks

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
### Case 7: A Normal Element with a Complex Phase

#### The Element

$$
\tilde Q=(1+i)(e_t+\vec e_x)=(1+i,\ 1+i,\ 0,\ 0).
$$

$$
N=4i,
\qquad
B^2=2i,
\qquad
\varrho\,e^{i\theta_{\mathrm{pha}}}=\sqrt2(1+i),
\qquad
\varrho=2,
\qquad
\theta_{\mathrm{pha}}=\frac{\pi}{4}.
$$

#### The Polar Factors

$$
\tilde U=\frac{e_t+\vec e_x}{\sqrt2},
\qquad
\tilde U_{\mathrm b}=e_t,
\qquad
\tilde u_{\mathrm r}=\frac{e_t+\vec e_x}{\sqrt2}.
$$

The element is the phase $2e^{i\pi/4}$ times the quarter-turn rotor. The boost is the identity, with $\theta_{\mathrm{rpd}}=0$; the rotor has $\theta_{\mathrm{axr}}=\frac{\pi}{2}$ and $\vec u_{\mathrm r}=\vec e_x$.

#### The Spectral Data

$$
\lambda_+=2i,
\qquad
\lambda_-=2,
\qquad
\vec{Ζ}=-i\vec e_x,
\qquad
\mu_\pm=e^{\pm i\pi/4}.
$$

The element is normal. The eigenvalues of $\tilde Q$ have modulus $2$, and the eigenvalues of the unit factor have modulus one.

#### The Checks

The true logarithm is

$$
\operatorname{Log}\tilde Q=\ln2+i\frac{\pi}{4}+i\frac{\pi}{4}\vec e_x
=(0.69314718+0.78539816i)e_t+0.78539816\vec e_x,
$$

and the formal exponent is the same, with defect $0$. This case shows that the phase and the rotor angle add in the scalar and the vector parts independently.
### Case 8: A Pure Vector

#### The Element

$$
\tilde Q=\vec e_x+\vec e_y=(0,1,1,0).
$$

$$
N=2,
\qquad
B^2=2,
\qquad
\varrho\,e^{i\theta_{\mathrm{pha}}}=\sqrt2,
\qquad
\varrho=\sqrt2,
\qquad
\theta_{\mathrm{pha}}=0.
$$

#### The Polar Factors

$$
\tilde U=\frac{\vec e_x+\vec e_y}{\sqrt2},
\qquad
\tilde U_{\mathrm b}=e_t,
\qquad
\tilde u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt2}.
$$

The boost is the identity, with $\theta_{\mathrm{rpd}}=0$. The rotor is a half-turn about the diagonal, with $\theta_{\mathrm{axr}}=\pi$ and $\vec u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt2}$.

#### The Spectral Data

$$
\lambda_+=i\sqrt2,
\qquad
\lambda_-=-i\sqrt2,
\qquad
\vec{Ζ}=-\frac{i}{\sqrt2}(\vec e_x+\vec e_y),
\qquad
\mu_\pm=\pm i.
$$

The element is normal. The eigenbasis is the polar frame, and the common axis is $i\vec{Ζ}=\frac{\vec e_x+\vec e_y}{\sqrt2}$.

#### The Checks

The true logarithm is

$$
\operatorname{Log}\tilde Q=\ln\sqrt2+\frac{\pi}{2}\frac{\vec e_x+\vec e_y}{\sqrt2}
=0.34657359\,e_t+1.11072073(\vec e_x+\vec e_y),
$$

and the formal exponent is the same, with defect $0$.
## On the Wall

The eight cases of this group have $B^2=0$, so every element is $Q_t(e_t+\vec\Pi_{\mathrm{nil}})$ with $\vec\Pi_{\mathrm{nil}}^2=0$. Cases $9$ to $11$ are the scalar line: the unit factor is $\pm e_t$, the boost is the identity and the word is central. Cases $12$ to $16$ are the Jordan part: the unit factor is $\pm(e_t+\vec\Pi_{\mathrm{nil}})$ with $\vec\Pi_{\mathrm{nil}}\neq0$, the two axes are orthogonal, and the rapidity is a function of the rotor angle.

### Case 9: The Identity

#### The Element

$$
\tilde Q=e_t=(1,0,0,0).
$$

$$
N=1,
\qquad
B^2=0,
\qquad
\varrho\,e^{i\theta_{\mathrm{pha}}}=1,
\qquad
\varrho=1,
\qquad
\theta_{\mathrm{pha}}=0,
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

The boost and the rotor are both the identity, with $\theta_{\mathrm{rpd}}=0$ and $\theta_{\mathrm{axr}}=0$; the two axes are undefined.

#### The Logarithm

$$
\operatorname{Log}\tilde Q=0,
\qquad
\tilde Q_{\log}=0,
\qquad
\delta=0.
$$

The element is the identity; it is normal.

### Case 10: A Negative Scalar

#### The Element

$$
\tilde Q=-2e_t=(-2,0,0,0).
$$

$$
N=4,
\qquad
B^2=0,
\qquad
\varrho\,e^{i\theta_{\mathrm{pha}}}=2,
\qquad
\varrho=2,
\qquad
\theta_{\mathrm{pha}}=0,
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

The boost is the identity, with $\theta_{\mathrm{rpd}}=0$. The rotor is the central element $-e_t$, which is $\exp(\pi\vec u_{\mathrm r})$ for every invertible element axis; in the range $\theta_{\mathrm{axr}}\in[0,2\pi]$ the angle is $\theta_{\mathrm{axr}}=2\pi$ and the axis is undefined.

#### The Logarithm

$$
\operatorname{Log}\tilde Q=\ln2+i\pi,
\qquad
\tilde Q_{\log}=\ln2+\pi\vec u_{\mathrm r},
\qquad
\delta=0.
$$

The formal exponent depends on the free axis, but its exponential is $-2$ for every axis, because $\exp(\pi\vec u_{\mathrm r})=-e_t$. The element is normal.

### Case 11: An Imaginary Scalar

#### The Element

$$
\tilde Q=2i\,e_t=(2i,0,0,0).
$$

$$
N=-4,
\qquad
B^2=0,
\qquad
\varrho\,e^{i\theta_{\mathrm{pha}}}=2i,
\qquad
\varrho=2,
\qquad
\theta_{\mathrm{pha}}=\frac{\pi}{2},
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

The word is pure scale and phase, with $\theta_{\mathrm{rpd}}=0$ and $\theta_{\mathrm{axr}}=0$.

#### The Logarithm

$$
\operatorname{Log}\tilde Q=\ln2+i\frac{\pi}{2},
\qquad
\tilde Q_{\log}=\ln2+i\frac{\pi}{2},
\qquad
\delta=0.
$$

The element is normal.

### Case 12: The Standard Jordan Element

#### The Element

$$
\tilde Q=e_t+\vec e_x+i\vec e_y=(1,1,i,0).
$$

$$
N=1,
\qquad
B^2=0,
\qquad
\varrho\,e^{i\theta_{\mathrm{pha}}}=1,
\qquad
\varrho=1,
\qquad
\theta_{\mathrm{pha}}=0,
\qquad
\varepsilon=1,
\qquad
Q_t=1,
\qquad
\vec\Pi_{\mathrm{nil}}=\vec e_x+i\vec e_y.
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
\theta_{\mathrm{rpd}}=2\ln(1+\sqrt2)=1.762747174,
\qquad
\vec u_{\mathrm b}=\frac{\vec e_y+\vec e_z}{\sqrt2},
$$

and the rotor has

$$
\theta_{\mathrm{axr}}=\frac{\pi}{2},
\qquad
\vec u_{\mathrm r}=\vec e_x.
$$

The axes are orthogonal: $c=0$. The scalar constraint is $\cosh\frac{\theta_{\mathrm{rpd}}}{2}\cos\frac{\theta_{\mathrm{axr}}}{2}=\sqrt2\cdot\frac{1}{\sqrt2}=1=\varepsilon$.

#### The Word

$$
\tilde Q=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\frac{\vec e_y+\vec e_z}{\sqrt2}\Bigr)
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

The formal exponent is not the logarithm: the cross term $i\tanh\frac{\theta_{\mathrm{rpd}}}{2}\tan\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm b}\times\vec u_{\mathrm r}$ is present.

### Case 13: The Second Jordan Element

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
\varrho\,e^{i\theta_{\mathrm{pha}}}=1,
\qquad
\varrho=1,
\qquad
\theta_{\mathrm{pha}}=0,
\qquad
\varepsilon=1,
\qquad
Q_t=1,
\qquad
\vec\Pi_{\mathrm{nil}}=\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z.
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
\theta_{\mathrm{rpd}}=2\ln(1+\sqrt2)=1.762747174,
\qquad
\vec u_{\mathrm b}=\vec e_x,
$$

and the rotor has

$$
\theta_{\mathrm{axr}}=\frac{\pi}{2},
\qquad
\vec u_{\mathrm r}=\vec e_y.
$$

The axes are orthogonal: $c=0$. The scalar constraint is again $\sqrt2\cdot\frac{1}{\sqrt2}=1$.

#### The Word

$$
\tilde Q=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\vec e_x\Bigr)
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

The defect is larger than in case 12, because the two axes are orthogonal but the coefficients of the two exponents are different.

### Case 14: A Jordan Element with a Complex Scalar

#### The Element

$$
\tilde Q=(1+i)e_t+\vec e_x+i\vec e_y=(1+i,\ 1,\ i,\ 0).
$$

$$
N=2i,
\qquad
B^2=0,
\qquad
\varrho\,e^{i\theta_{\mathrm{pha}}}=1+i,
\qquad
\varrho=\sqrt2,
\qquad
\theta_{\mathrm{pha}}=\frac{\pi}{4},
\qquad
\varepsilon=1,
\qquad
Q_t=1+i,
\qquad
\vec\Pi_{\mathrm{nil}}=\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y.
$$

#### The Polar Factors

$$
\tilde U=\tilde Q/(\varrho\,e^{i\theta_{\mathrm{pha}}})=e_t+\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y,
$$

$$
\tilde U_{\mathrm b}=1.22474487\,e_t-i0.40824829\,\vec e_x+i0.40824829\,\vec e_y+i0.40824829\,\vec e_z,
$$

$$
\tilde u_{\mathrm r}=0.81649658\,e_t+0.40824829\,\vec e_x+0.40824829\,\vec e_y.
$$

The boost has

$$
\theta_{\mathrm{rpd}}=\operatorname{arcosh}2=1.316957897,
\qquad
\vec u_{\mathrm b}=\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt3},
$$

and the rotor has

$$
\theta_{\mathrm{axr}}=\arccos\frac13=1.230959417,
\qquad
\vec u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt2}.
$$

The axes are orthogonal: $c=0$. The scalar constraint is $\cosh\frac{\theta_{\mathrm{rpd}}}{2}\cos\frac{\theta_{\mathrm{axr}}}{2}=\sqrt{1.5}\cdot\sqrt{2/3}=1$.

#### The Word

$$
\tilde Q=(1+i)\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt3}\Bigr)
\exp\Bigl(\frac{\theta_{\mathrm{axr}}}{2}\frac{\vec e_x+\vec e_y}{\sqrt2}\Bigr).
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

### Case 15: A Negative Jordan Element

#### The Element

$$
\tilde Q=-e_t-\vec e_x-i\vec e_y=(-1,-1,-i,0).
$$

$$
N=1,
\qquad
B^2=0,
\qquad
\varrho\,e^{i\theta_{\mathrm{pha}}}=1,
\qquad
\varrho=1,
\qquad
\theta_{\mathrm{pha}}=0,
\qquad
\varepsilon=-1,
\qquad
Q_t=-1,
\qquad
\vec\Pi_{\mathrm{nil}}=\vec e_x+i\vec e_y.
$$

#### The Polar Factors

$$
\tilde U=-\bigl(e_t+\vec e_x+i\vec e_y\bigr),
\qquad
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\frac{\vec e_y+\vec e_z}{\sqrt2},
\qquad
\tilde u_{\mathrm r}=-\frac{e_t+\vec e_x}{\sqrt2}.
$$

The boost is the one of case 12, with $\theta_{\mathrm{rpd}}=1.762747174$ and the same axis. The rotor has

$$
\theta_{\mathrm{axr}}=\frac{3\pi}{2},
\qquad
\vec u_{\mathrm r}=-\vec e_x.
$$

The axes are orthogonal: $c=0$. The scalar constraint is $\sqrt2\cdot(-\frac{1}{\sqrt2})=-1=\varepsilon$; the sign of the rotor angle is the sign of $\varepsilon$.

#### The Word

$$
\tilde Q=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\frac{\vec e_y+\vec e_z}{\sqrt2}\Bigr)
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

The formal exponent has no scalar part, because $\ln \varrho+i\theta_{\mathrm{pha}}=0$; the true logarithm has $i\pi$, the period that the word does not see.

### Case 16: A Scaled Jordan Element

#### The Element

$$
\tilde Q=2e_t+2\vec e_x+2i\vec e_y=(2,2,2i,0).
$$

$$
N=4,
\qquad
B^2=0,
\qquad
\varrho\,e^{i\theta_{\mathrm{pha}}}=2,
\qquad
\varrho=2,
\qquad
\theta_{\mathrm{pha}}=0,
\qquad
\varepsilon=1,
\qquad
Q_t=2,
\qquad
\vec\Pi_{\mathrm{nil}}=\vec e_x+i\vec e_y.
$$

#### The Polar Factors

$$
\tilde U=e_t+\vec e_x+i\vec e_y,
\qquad
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\frac{\vec e_y+\vec e_z}{\sqrt2},
\qquad
\tilde u_{\mathrm r}=\frac{e_t+\vec e_x}{\sqrt2}.
$$

The word is the one of case 12 with the scale $\varrho=2$:

$$
\theta_{\mathrm{rpd}}=1.762747174,
\qquad
\vec u_{\mathrm b}=\frac{\vec e_y+\vec e_z}{\sqrt2},
\qquad
\theta_{\mathrm{axr}}=\frac{\pi}{2},
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

The defect is twice the defect of case 12, because the exponential of the central $\ln2$ multiplies the miss by $2$.
## The Comparison

### The Normal Cases

| Case | Element | $\theta_{\mathrm{rpd}}$ | $\theta_{\mathrm{axr}}$ | Axes | Defect |
|---|---|---|---|---|---|
| 1 | $\vec e_x$ | $0$ | $\pi$ | undefined, $\vec e_x$ | $0$ |
| 2 | $\sqrt2e_t+i\vec e_x$ | $2\ln(1+\sqrt2)$ | $0$ | $\vec e_x$, undefined | $0$ |
| 3 | $(1-\frac{i}{\sqrt2})e_t+(1+\frac{i}{\sqrt2})\vec e_x$ | $2\ln(1+\sqrt2)$ | $\frac{\pi}{2}$ | $\vec e_x$, $\vec e_x$ | $0$ |
| 4 | $\frac{e_t+\vec e_x}{\sqrt2}$ | $0$ | $\frac{\pi}{2}$ | undefined, $\vec e_x$ | $0$ |
| 7 | $(1+i)(e_t+\vec e_x)$ | $0$ | $\frac{\pi}{2}$ | undefined, $\vec e_x$ | $0$ |
| 8 | $\vec e_x+\vec e_y$ | $0$ | $\pi$ | undefined, $\frac{\vec e_x+\vec e_y}{\sqrt2}$ | $0$ |

In every normal case the formal exponent is a logarithm, the axes coincide when both are defined, and the eigenvalues of the unit factor are $e^{\mp\theta_{\mathrm{rpd}}/2}e^{\pm i\theta_{\mathrm{axr}}/2}$.

### The Non-Normal Cases

| Case | Element | $\theta_{\mathrm{rpd}}$ | $\theta_{\mathrm{axr}}$ | $c$ | $\theta_{\mathrm{rpd},\mathrm{spec}}$ | $\theta_{\mathrm{spec}}$ | Defect |
|---|---|---|---|---|---|---|---|
| 5 | $1-\frac{i}{2}+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z$ | $1.7627$ | $1.5708$ | $0.7071$ | $1.4657$ | $1.3498$ | $0.5000$ |
| 6 | $(1+i)(e_t+\vec e_x)+\vec e_y+\frac12\vec e_z$ | $0.6968$ | $1.7436$ | $-0.3830$ | $0.2820$ | $1.6564$ | $0.4222$ |

The two columns $\theta_{\mathrm{rpd},\mathrm{spec}},\theta_{\mathrm{spec}}$ are the values extracted from the eigenvalues of the unit factor by the normal-case formulas. They disagree with the true word in both cases. The defect is nonzero in both.

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

The table is the numerical form of the spectral reading. In cases 1 to 4, 7 and 8 the moduli and arguments are $e^{\mp\theta_{\mathrm{rpd}}/2}$ and $\pm\theta_{\mathrm{axr}}/2$. In cases 5 and 6 they are not.

### The Scalar Line

| Case | $\tilde Q$ | $Q_t$ | $\varrho\,e^{i\theta_{\mathrm{pha}}}$ | $\varepsilon$ | $\theta_{\mathrm{axr}}$ | $\operatorname{Log}\tilde Q$ | $\delta$ |
|---|---|---|---|---|---|---|---|
| 9| $e_t$ | $1$ | $1$ | $+1$ | $0$ | $0$ | $0$ |
| 10| $-2e_t$ | $-2$ | $2$ | $-1$ | $2\pi$ | $\ln2+i\pi$ | $0$ |
| 11| $2ie_t$ | $2i$ | $2i$ | $+1$ | $0$ | $\ln2+i\frac{\pi}{2}$ | $0$ |

The scalar line is the normal locus of the sector. The rotor is central, the boost is the identity, and the exact logarithm is the scalar logarithm.

### The Jordan Part

| Case | $Q_t$ | $\varepsilon$ | $\theta_{\mathrm{rpd}}$ | $\theta_{\mathrm{axr}}$ | $\vec u_{\mathrm b}$ | $\vec u_{\mathrm r}$ | $\delta$ |
|---|---|---|---|---|---|---|---|
| 12| $1$ | $+1$ | $1.762747$ | $\frac{\pi}{2}$ | $\frac{\vec e_y+\vec e_z}{\sqrt2}$ | $\vec e_x$ | $0.639975$ |
| 13| $1$ | $+1$ | $1.762747$ | $\frac{\pi}{2}$ | $\vec e_x$ | $\vec e_y$ | $0.707107$ |
| 14| $1+i$ | $+1$ | $1.316958$ | $1.230959$ | $\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt3}$ | $\frac{\vec e_x+\vec e_y}{\sqrt2}$ | $0.542568$ |
| 15| $-1$ | $-1$ | $1.762747$ | $\frac{3\pi}{2}$ | $\frac{\vec e_y+\vec e_z}{\sqrt2}$ | $-\vec e_x$ | $1.233061$ |
| 16| $2$ | $+1$ | $1.762747$ | $\frac{\pi}{2}$ | $\frac{\vec e_y+\vec e_z}{\sqrt2}$ | $\vec e_x$ | $1.279950$ |

In every Jordan case $c=0$, the axes are orthogonal, and the rapidity is a function of the angle:

$$
\lvert\cos\frac{\theta_{\mathrm{axr}}}{2}\rvert=\frac{1}{\cosh\frac{\theta_{\mathrm{rpd}}}{2}}.
$$

### The Constraints

| Case | $(\tilde U-\varepsilon e_t)^2$ | $\vec\Pi_{\mathrm{nil}}^2$ | $c$ | $\cosh\frac{\theta_{\mathrm{rpd}}}{2}\cos\frac{\theta_{\mathrm{axr}}}{2}$ |
|---|---|---|---|---|
| 9| $0$ | $0$ | -- | $1$ |
| 10| $0$ | $0$ | -- | $-1$ |
| 11| $0$ | $0$ | -- | $1$ |
| 12| $0$ | $0$ | $0$ | $1$ |
| 13| $0$ | $0$ | $0$ | $1$ |
| 14| $0$ | $0$ | $0$ | $1$ |
| 15| $0$ | $0$ | $0$ | $-1$ |
| 16| $0$ | $0$ | $0$ | $1$ |

The two columns of zeros are the numerical form of the rigidity: the unit factor is $\pm$unipotent and the nilpotent direction is null.

### The Exact Logarithm

| Case | $\operatorname{Log}\tilde Q-\log Q_t$ | $\lVert\exp(\operatorname{Log}\tilde Q)-\tilde Q\rVert$ |
|---|---|---|
| 9| $0$ | $0$ |
| 10| $0$ | $7\times10^{-16}$ |
| 11| $0$ | $7\times10^{-16}$ |
| 12| $\vec e_x+i\vec e_y$ | $0$ |
| 13| $\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z$ | $4\times10^{-16}$ |
| 14| $\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y$ | $9\times10^{-16}$ |
| 15| $\vec e_x+i\vec e_y$ | $1.5\times10^{-15}$ |
| 16| $\vec e_x+i\vec e_y$ | $4\times10^{-16}$ |

The exact logarithm is exact: the error is the rounding of the matrix exponential, not a truncation.

### The Defects

| Case | $\tilde Q_{\log}$ | $\delta$ |
|---|---|---|
| 9| $0$ | $0$ |
| 10| $\ln2+\pi\vec u_{\mathrm r}$ | $0$ |
| 11| $\ln2+i\frac{\pi}{2}$ | $0$ |
| 12| $\frac{\pi}{4}\vec e_x+i0.623225(\vec e_y+\vec e_z)$ | $0.639975$ |
| 13| $i0.881374\vec e_x+0.785398\vec e_y$ | $0.707107$ |
| 14| $(0.346574+0.785398i)e_t+(0.435210-0.380173i)\vec e_x+(0.435210+0.380173i)\vec e_y+0.380173i\vec e_z$ | $0.542568$ |
| 15| $-2.356194\vec e_x+i0.623225(\vec e_y+\vec e_z)$ | $1.233061$ |
| 16| $\ln2+\frac{\pi}{4}\vec e_x+i0.623225(\vec e_y+\vec e_z)$ | $1.279950$ |

The scalar line has zero defect, because the formal exponent is a logarithm there. The Jordan part has positive defect in every case, because the cross term is nonzero.

## Summary

### The Cases

| Case | $\tilde Q$ | $N$ | $B^2$ | $\varrho\,e^{i\theta_{\mathrm{pha}}}$ | Normal |
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

| Case | $\varrho$ | $\theta_{\mathrm{pha}}$ | $\theta_{\mathrm{rpd}}$ | $\vec u_{\mathrm b}$ | $\theta_{\mathrm{axr}}$ | $\vec u_{\mathrm r}$ |
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
- In the normal cases the axes coincide when both are defined, the word is a single exponential, the formal exponent is the logarithm, and the spectrum gives the two angles by $\theta_{\mathrm{rpd}}=\ln\lvert\mu_-/\mu_+\rvert$ and $\theta_{\mathrm{axr}}=2\arg\mu_+$.
- In the non-normal cases the axes are not the eigenlines, the formal exponent is not the logarithm, the defect is positive, and the spectrum does not give the two angles. The gap is visible in the table: $1.4657$ against $1.7627$ in case 5, and $0.2820$ against $0.6968$ in case 6.
- The two factors commute with the element exactly in the normal cases; the norm of the commutator is zero there and $1.41$ and $0.954$ in the two non-normal cases.
- The eigenvalues of the unit factor are the same function of $U_t$ in all cases; what changes is whether the word's angles can be read from them.

### The Cases on the Wall

| Case | $\tilde Q$ | $N$ | $Q_t$ | $\varepsilon$ | Stratum |
|---|---|---|---|---|---|
| 9| $e_t$ | $1$ | $1$ | $+1$ | scalar |
| 10| $-2e_t$ | $4$ | $-2$ | $-1$ | scalar |
| 11| $2ie_t$ | $-4$ | $2i$ | $+1$ | scalar |
| 12| $e_t+\vec e_x+i\vec e_y$ | $1$ | $1$ | $+1$ | Jordan |
| 13| $e_t+\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z$ | $1$ | $1$ | $+1$ | Jordan |
| 14| $(1+i)e_t+\vec e_x+i\vec e_y$ | $2i$ | $1+i$ | $+1$ | Jordan |
| 15| $-e_t-\vec e_x-i\vec e_y$ | $1$ | $-1$ | $-1$ | Jordan |
| 16| $2e_t+2\vec e_x+2i\vec e_y$ | $4$ | $2$ | $+1$ | Jordan |

### The Word Data on the Wall

| Case | $\varrho$ | $\theta_{\mathrm{pha}}$ | $\theta_{\mathrm{rpd}}$ | $\theta_{\mathrm{axr}}$ | $\vec u_{\mathrm b}$ | $\vec u_{\mathrm r}$ | $c$ |
|---|---|---|---|---|---|---|---|
| 9| $1$ | $0$ | $0$ | $0$ | -- | -- | -- |
| 10| $2$ | $0$ | $0$ | $2\pi$ | -- | -- | -- |
| 11| $2$ | $\frac{\pi}{2}$ | $0$ | $0$ | -- | -- | -- |
| 12| $1$ | $0$ | $1.762747$ | $\frac{\pi}{2}$ | $\frac{\vec e_y+\vec e_z}{\sqrt2}$ | $\vec e_x$ | $0$ |
| 13| $1$ | $0$ | $1.762747$ | $\frac{\pi}{2}$ | $\vec e_x$ | $\vec e_y$ | $0$ |
| 14| $\sqrt2$ | $\frac{\pi}{4}$ | $1.316958$ | $1.230959$ | $\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt3}$ | $\frac{\vec e_x+\vec e_y}{\sqrt2}$ | $0$ |
| 15| $1$ | $0$ | $1.762747$ | $\frac{3\pi}{2}$ | $\frac{\vec e_y+\vec e_z}{\sqrt2}$ | $-\vec e_x$ | $0$ |
| 16| $2$ | $0$ | $1.762747$ | $\frac{\pi}{2}$ | $\frac{\vec e_y+\vec e_z}{\sqrt2}$ | $\vec e_x$ | $0$ |

### What the Wall Shows

- Every case has $B^2=0$ and $N\neq0$, and every element is $Q_t(e_t+\vec\Pi_{\mathrm{nil}})$ with $\vec\Pi_{\mathrm{nil}}^2=0$.
- The unit factor is $\pm(e_t+\vec\Pi_{\mathrm{nil}})$: its scalar part is $\pm1$ and its square is the identity on the scalar line, a nontrivial unipotent on the Jordan part.
- On the Jordan part the axes are orthogonal, $c=0$, and the rapidity is tied to the rotor angle by $|\cos\frac{\theta_{\mathrm{axr}}}{2}|=1/\cosh\frac{\theta_{\mathrm{rpd}}}{2}$.
- The exact logarithm is $\log Q_t+\vec\Pi_{\mathrm{nil}}$, with no series and no correction. The scalar logarithm carries the sign and the phase; the nilpotent part is fixed.
- The formal exponent is a logarithm on the scalar line and not on the Jordan part. The defect is the cross term $i\tanh\frac{\theta_{\mathrm{rpd}}}{2}\tan\frac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm b}\times\vec u_{\mathrm r}$ plus the nonlinear terms.
- The defect scales with the element: case 16 is twice case 12, and its defect is twice as large.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q$ | the element of the case |
| $N$ | the reduced product |
| $B^2$ | the vector form |
| $\varrho\,e^{i\theta_{\mathrm{pha}}}$ | the modulus, principal square root of $N$ |
| $\varrho,\theta_{\mathrm{pha}}$ | the polar coordinates of $\varrho\,e^{i\theta_{\mathrm{pha}}}$ |
| $\tilde U$ | the unit factor |
| $\tilde U_{\mathrm b}$ | the Hermitian positive factor |
| $\tilde u_{\mathrm r}$ | the rotor |
| $\theta_{\mathrm{rpd}},\vec u_{\mathrm b}$ | the rapidity and the boost axis |
| $\theta_{\mathrm{axr}},\vec u_{\mathrm r}$ | the rotor angle and the rotor axis |
| $c$ | the cosine between the axes |
| $\lambda_\pm$ | the eigenvalues of $\tilde Q$ |
| $\vec{Ζ}$ | the root of one, $-i\vec Q/B$ |
| $\tilde\Pi_{\mathrm{id},\pm}$ | the spectral idempotents |
| $\mu_\pm$ | the eigenvalues of the unit factor |
| $\tilde Q_{\log}$ | the formal exponent |
| $\delta$ | the defect of the case |
| $\vec\Pi_{\mathrm{nil}}=\vec Q/Q_t$ | the nilpotent direction on the wall |
| $\varepsilon=Q_t/(\varrho\,e^{i\theta_{\mathrm{pha}}})$ | the sign of the unit factor on the wall, $\pm1$ |
| $\delta$ | the defect of the case |
| $\tilde Q_{\log}$ | the formal exponent |

## Further Reading

- [The Complete Polar Decomposition of an N-Regular Biquaternion](the-complete-polar-decomposition-of-an-n-regular-biquaternion.html), for the theorem, the proofs, the spectral reading and the rigidity of the word.
- [Relations between the Complete Polar Decomposition and Eigenbasis of an N-Regular Biquaternion](relations-between-the-complete-polar-decomposition-and-eigenbasis-of-an-n-regular-biquaternion.html), for the dictionary between the word and the eigenvalue data, and its collapse on the Jordan part.
- [Worked Examples of the Complete Polar Decomposition in the Eigenbasis of an N-Regular Biquaternion](worked-examples-of-the-complete-polar-decomposition-in-the-eigenbasis-of-an-n-regular-biquaternion.html), for the same sixteen cases read in the eigenbasis and in the Jordan chain.
- [The Complete Polar Decomposition of an N-Regular Biquaternion](the-complete-polar-decomposition-of-an-n-regular-biquaternion.html), for the modulus–unit theorem.
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential and the logarithm.
- [Algebra and Element Conventions](algebra-and-element-conventions.html), for the notation.
