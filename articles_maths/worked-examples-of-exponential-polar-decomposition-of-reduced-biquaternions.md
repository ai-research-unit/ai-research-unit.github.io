# __Worked Examples of Exponential Polar Decomposition of Reduced Biquaternions__

## Introduction

This article computes the exponential polar decomposition of eight reduced biquaternions, one after another. It is the computational companion of *Exponential Polar Decomposition of Reduced Biquaternions*. The decomposition, its existence and uniqueness in the principal diamond, and the two factors are established there and in *Reduced Biquaternion Elementary Functions*; the proofs are not repeated.

Each case is read from the two complex coordinates $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$. The modulus, the boost and the two phases are computed from them by the formulas of §*The Method*, and the word is checked against the reconstruction

$$
\breve Q=\rho\bigl(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}}\bigr)\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}}).
$$

The eight cases cover the generic element, the complex scalar, the two pure phases, the boundary of the principal diamond, the hyperbolic line, the central discrete element and the zero divisor.

| Group | Case | What it shows |
|---|---|---|
| Generic | $3+4i+j(1-i)$ | a nonzero boost and two nonzero phases |
| Complex scalar | $1+i$ | one phase, no boost |
| Central phase | $i$ | the phase $\theta_{\mathrm{pha}}=\pi/2$ |
| Split phase | $ij$ | the phase $\theta_{\mathrm{phb}}=\pi/2$ |
| Boundary of the diamond | $j$ | $\theta_{\mathrm{pha}}=\pi/2$, $\theta_{\mathrm{phb}}=-\pi/2$, $\lvert\theta_{\mathrm{pha}}\rvert+\lvert\theta_{\mathrm{phb}}\rvert=\pi$ |
| Hyperbolic line | $\exp(j\ln2)$ | the boost $\theta_{\mathrm{rpd}}=\ln2$, both phases zero |
| Central discrete | $-1$ | the corner $\theta_{\mathrm{pha}}=\pi$, $\theta_{\mathrm{phb}}=0$ |
| Zero divisor | $1+j$ | $C_+C_-=0$, but no polar word |

$$
C_+=Q_{\blacktriangle}+Q_{\blacktriangledown},
\qquad
C_-=Q_{\blacktriangle}-Q_{\blacktriangledown}.
$$

Their product $C_+C_-=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$ is written in full throughout. The modulus is $\rho>0$, the boost is $\theta_{\mathrm{rpd}}\in\mathbb{R}$, and the phases $(\theta_{\mathrm{pha}},\theta_{\mathrm{phb}})$ are taken in the half-open principal diamond $\lvert\theta_{\mathrm{pha}}\rvert+\lvert\theta_{\mathrm{phb}}\rvert\le\pi$, with the boundary half-open. Errors are Euclidean in the four real coefficients and are computed in double precision; a displayed zero is exact in that precision, and displayed decimals are rounded.

**The plan.** The method is stated once (§*The Method*). The eight cases follow (§*The Eight Cases*), each with its components, its polar data, its two factors and its check. The summary collects the results in two tables and reads the patterns across the cases (§*Summary*). The eigenbasis, the idempotents and the spinors of the same eight cases are collected in *Worked Examples of Exponential Polar Decomposition with Eigenbasis of Reduced Biquaternions*.

## The Method

### The Two Complex Components

For $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ the two coordinates are the complex numbers $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$. The polar data are read from their sum and difference,

$$
C_+=Q_{\blacktriangle}+Q_{\blacktriangledown},
\qquad
C_-=Q_{\blacktriangle}-Q_{\blacktriangledown}.
$$

The modulus and the boost are

$$
\rho=\sqrt{\lvert C_+C_-\rvert}
=\sqrt{\lvert Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2\rvert},
\qquad
\theta_{\mathrm{rpd}}=\tfrac12\ln\left\lvert\frac{C_+}{C_-}\right\rvert,
$$

and the two phases are

$$
\theta_{\mathrm{pha}}=\tfrac12\bigl(\operatorname{Arg}C_++\operatorname{Arg}C_-\bigr),
\qquad
\theta_{\mathrm{phb}}=\tfrac12\bigl(\operatorname{Arg}C_+-\operatorname{Arg}C_-\bigr),
$$

with $\operatorname{Arg}$ the principal argument in $(-\pi,\pi]$. The last two formulas give the representative in the principal diamond. The two scales are

$$
\lvert C_+\rvert=\rho e^{\theta_{\mathrm{rpd}}},
\qquad
\lvert C_-\rvert=\rho e^{-\theta_{\mathrm{rpd}}},
$$

and the product and ratio read

$$
C_+C_-=\rho^2e^{2i\theta_{\mathrm{pha}}}
=\bigl(\rho e^{\theta_{\mathrm{rpd}}}\bigr)\bigl(\rho e^{-\theta_{\mathrm{rpd}}}\bigr)e^{2i\theta_{\mathrm{pha}}},
\qquad
\frac{C_+}{C_-}=e^{2\theta_{\mathrm{rpd}}}e^{2i\theta_{\mathrm{phb}}}.
$$

An element is a unit exactly when $C_+C_-\neq0$.

### The Reconstruction

The polar word separates the element into a real-hyperbolic factor and a torus factor,

$$
\breve Q=\breve r\,u,
\qquad
\breve r=\rho\bigl(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}}\bigr),
\qquad
u=\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}}).
$$

The four real numbers $\rho,\theta_{\mathrm{rpd}},\theta_{\mathrm{pha}},\theta_{\mathrm{phb}}$ are the exponent

$$
\operatorname{Log}\breve Q=\ln\rho+j\theta_{\mathrm{rpd}}+i\theta_{\mathrm{pha}}+ij\theta_{\mathrm{phb}}
=\bigl(\ln\rho+i\theta_{\mathrm{pha}}\bigr)+j\bigl(\theta_{\mathrm{rpd}}+i\theta_{\mathrm{phb}}\bigr).
$$

The factor $\breve r$ carries the two real scales $\rho e^{\pm\theta_{\mathrm{rpd}}}$ in the two complex components, and $u$ carries the two phases $\theta_{\mathrm{pha}}\pm\theta_{\mathrm{phb}}$.

### The Matrix Picture

The matrix of the regular representation,

$$
\mathsf M(\breve Q)=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix},
$$

has determinant $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=C_+C_-$. The two scales $\lvert C_+\rvert=\rho e^{\theta_{\mathrm{rpd}}}$ and $\lvert C_-\rvert=\rho e^{-\theta_{\mathrm{rpd}}}$ govern its action, each repeated.

### The Null Cone

A zero divisor is an element with $C_+C_-=0$, that is $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=0$. One of the two complex components vanishes, the element has the form $\breve Q=Q_{\blacktriangle}(1\pm j)$ with $Q_{\blacktriangle}\neq0$, and no logarithm exists: the modulus vanishes and the boost diverges. The matrix has rank one and determinant zero. Case 8 treats the boundary explicitly.

## The Eight Cases

### Case 1: A Generic Element

**Components.** For $\breve Q=3+4i+j(1-i)$,

$$
Q_{\blacktriangle}=3+4i,
\qquad
Q_{\blacktriangledown}=1-i,
\qquad
C_+=4+3i,
\qquad
C_-=2+5i,
\qquad
C_+C_-=-7+26i.
$$

Both components are nonzero, with $\lvert C_+\rvert=5$ and $\lvert C_-\rvert=\sqrt{29}$.

**Polar data.** The modulus, the boost and the two phases are

$$
\rho=\sqrt{5\sqrt{29}}=5.189009928268833,
\qquad
\ln\rho=1.6465429137136687,
$$

$$
\theta_{\mathrm{rpd}}=\tfrac12\ln\frac{5}{\sqrt{29}}=-0.03710500127956826,
$$

$$
\theta_{\mathrm{pha}}=\tfrac12\bigl(\operatorname{Arg}(4+3i)+\operatorname{Arg}(2+5i)\bigr)=0.916895529237908,
$$

$$
\theta_{\mathrm{phb}}=\tfrac12\bigl(\operatorname{Arg}(4+3i)-\operatorname{Arg}(2+5i)\bigr)=-0.27339442044462364.
$$

The two phases satisfy $\lvert\theta_{\mathrm{pha}}\rvert+\lvert\theta_{\mathrm{phb}}\rvert=1.1902899497<\pi$, so the point is interior to the diamond.

**The two factors.** The real-hyperbolic factor is

$$
\boxed{\;
\breve r=\rho(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}})
=\frac{5+\sqrt{29}}{2}+j\,\frac{5-\sqrt{29}}{2}
=5.1925824036-0.1925824036\,j
\;},
$$

and the torus factor is

$$
u=e^{0.9168955292\,i}e^{-0.2733944204\,ij}
=0.5856953382+0.7642383454\,i
+j\bigl(0.2143046618-0.1642383454\,i\bigr).
$$

**The word and the check.** The exponent is

$$
\operatorname{Log}\breve Q=1.6465429137+0.9168955292\,i
-0.0371050013\,j-0.2733944204\,ij.
$$

The product of the two factors is

$$
\breve r\,u=3+4i+j(1-i),
$$

with error $1.3\times10^{-15}$, and $\exp(\operatorname{Log}\breve Q)$ reproduces the element with the same error. The matrix has determinant $-7+26i$ and the two scales $5$ and $\sqrt{29}$.

### Case 2: A Complex Scalar

**Components.** For $\breve Q=1+i$,

$$
Q_{\blacktriangle}=1+i,
\qquad
Q_{\blacktriangledown}=0,
\qquad
C_+=C_-=1+i,
\qquad
C_+C_-=2i.
$$

The two components coincide, with $\lvert C_\pm\rvert=\sqrt2$.

**Polar data.** The moduli are equal, so

$$
\rho=\sqrt{\lvert 2i\rvert}=\sqrt2,
\qquad
\theta_{\mathrm{rpd}}=0,
\qquad
\theta_{\mathrm{pha}}=\tfrac12\bigl(2\cdot\tfrac{\pi}{4}\bigr)=\tfrac{\pi}{4},
\qquad
\theta_{\mathrm{phb}}=0.
$$

**The two factors.** The real-hyperbolic factor is $\breve r=\sqrt2$, and the torus factor is

$$
u=e^{i\pi/4}=\frac{1+i}{\sqrt2}.
$$

**The word and the check.** The exponent is

$$
\operatorname{Log}\breve Q=\tfrac12\ln2+\tfrac{\pi}{4}i,
$$

and

$$
\breve r\,u=\sqrt2\cdot\frac{1+i}{\sqrt2}=1+i,
$$

with error $2.2\times10^{-16}$. The matrix has determinant $2i$ and the two scales $\sqrt2$ and $\sqrt2$.

### Case 3: The Central Phase

**Components.** For $\breve Q=i$,

$$
Q_{\blacktriangle}=i,
\qquad
Q_{\blacktriangledown}=0,
\qquad
C_+=C_-=i,
\qquad
C_+C_-=-1.
$$

The element is central, with $\lvert C_\pm\rvert=1$.

**Polar data.** The modulus is one, the boost vanishes and

$$
\theta_{\mathrm{pha}}=\operatorname{Arg}i=\tfrac{\pi}{2},
\qquad
\theta_{\mathrm{phb}}=0.
$$

**The two factors.** The real-hyperbolic factor is $\breve r=1$, and the torus factor is $u=i$.

**The word and the check.** The exponent is

$$
\operatorname{Log}\breve Q=\tfrac{\pi}{2}i,
$$

and $\breve r\,u=i$, with error $6.1\times10^{-17}$. The matrix has determinant $-1$ and the two scales $1$ and $1$.

### Case 4: The Split Phase

**Components.** For $\breve Q=ij$,

$$
Q_{\blacktriangle}=0,
\qquad
Q_{\blacktriangledown}=i,
\qquad
C_+=i,
\qquad
C_-=-i,
\qquad
C_+C_-=1.
$$

The two components are opposite, with $\lvert C_\pm\rvert=1$.

**Polar data.** The two moduli are one, so

$$
\rho=1,
\qquad
\theta_{\mathrm{rpd}}=0,
\qquad
\theta_{\mathrm{pha}}=0,
\qquad
\theta_{\mathrm{phb}}=\tfrac{\pi}{2}.
$$

**The two factors.** The real-hyperbolic factor is $\breve r=1$, and the torus factor is $u=ij$.

**The word and the check.** The exponent is

$$
\operatorname{Log}\breve Q=\tfrac{\pi}{2}ij,
$$

and $\breve r\,u=ij$, with error $6.1\times10^{-17}$. The matrix has determinant $1$ and the two scales $1$ and $1$.

### Case 5: The Boundary of the Diamond

**Components.** For $\breve Q=j$,

$$
Q_{\blacktriangle}=0,
\qquad
Q_{\blacktriangledown}=1,
\qquad
C_+=1,
\qquad
C_-=-1,
\qquad
C_+C_-=-1.
$$

The two components are opposite, with $\lvert C_\pm\rvert=1$.

**Polar data.** The moduli are one and the boost vanishes. The phases are

$$
\theta_{\mathrm{pha}}=\tfrac{\pi}{2},
\qquad
\theta_{\mathrm{phb}}=-\tfrac{\pi}{2},
\qquad
\lvert\theta_{\mathrm{pha}}\rvert+\lvert\theta_{\mathrm{phb}}\rvert=\pi.
$$

The point lies on the boundary of the principal diamond, where the two phases saturate it.

**The two factors.** The real-hyperbolic factor is $\breve r=1$, and the torus factor is $u=j$.

**The word and the check.** The exponent is

$$
\operatorname{Log}\breve Q=\tfrac{\pi}{2}i-\tfrac{\pi}{2}ij,
$$

and $\breve r\,u=j$, with error $1.2\times10^{-16}$. The matrix has determinant $-1$ and the two scales $1$ and $1$.

### Case 6: The Hyperbolic Line

**Components.** For

$$
\breve Q=\exp(j\ln2)=\cosh(\ln2)+j\sinh(\ln2)=\tfrac54+\tfrac34j,
$$

the coordinates are

$$
Q_{\blacktriangle}=\tfrac54,
\qquad
Q_{\blacktriangledown}=\tfrac34,
\qquad
C_+=2,
\qquad
C_-=\tfrac12,
\qquad
C_+C_-=1.
$$

**Polar data.** The two components are positive and real, so

$$
\rho=\sqrt{2\cdot\tfrac12}=1,
\qquad
\theta_{\mathrm{rpd}}=\tfrac12\ln4=\ln2,
\qquad
\theta_{\mathrm{pha}}=\theta_{\mathrm{phb}}=0.
$$

**The two factors.** The real-hyperbolic factor is

$$
\boxed{\;
\breve r=1\cdot(\cosh(\ln2)+j\sinh(\ln2))=\tfrac54+\tfrac34j
\;},
$$

and the torus factor is $u=1$.

**The word and the check.** The exponent is

$$
\operatorname{Log}\breve Q=j\ln2,
$$

and $\breve r\,u=\tfrac54+\tfrac34j$, with error $0$. The matrix has determinant $1$ and the two scales $2$ and $\tfrac12$. The element is a pure boost: the two phases vanish and the two scales are positive.

### Case 7: The Central Discrete Element

**Components.** For $\breve Q=-1$,

$$
Q_{\blacktriangle}=-1,
\qquad
Q_{\blacktriangledown}=0,
\qquad
C_+=C_-=-1,
\qquad
C_+C_-=1.
$$

The element is central, with $\lvert C_\pm\rvert=1$.

**Polar data.** The modulus is one and the boost vanishes. The phases are

$$
\theta_{\mathrm{pha}}=\pi,
\qquad
\theta_{\mathrm{phb}}=0,
\qquad
\lvert\theta_{\mathrm{pha}}\rvert+\lvert\theta_{\mathrm{phb}}\rvert=\pi.
$$

The point is the corner $(\pi,0)$ of the diamond.

**The two factors.** The real-hyperbolic factor is $\breve r=1$, and the torus factor is $u=-1$.

**The word and the check.** The exponent is

$$
\operatorname{Log}\breve Q=\pi i,
$$

and $\breve r\,u=-1$, with error $1.2\times10^{-16}$. The matrix has determinant $1$ and the two scales $1$ and $1$. The four logarithms of $-1$ and their kernel differences belong to the polar article and to the relation article; the principal one is the one above.

### Case 8: The Zero Divisor

**Components.** For $\breve Q=1+j$,

$$
Q_{\blacktriangle}=1,
\qquad
Q_{\blacktriangledown}=1,
\qquad
C_+=2,
\qquad
C_-=0,
\qquad
C_+C_-=0.
$$

One component vanishes, so the element is a zero divisor and no logarithm exists.

**No polar word.** The modulus vanishes and the boost diverges. The matrix

$$
\boxed{\;
\mathsf M(\breve Q)=\begin{pmatrix}1&1\\1&1\end{pmatrix}
\;}
$$

has rank one and determinant $0$. Its square is $\breve Q^2=2\breve Q$.

**The boundary.** The element is the limit of the hyperbolic family

$$
\breve Q_\delta=(1+\delta)+j,
\qquad
\delta>0.
$$

Its components give

$$
\rho=\sqrt{\delta(2+\delta)},
\qquad
\theta_{\mathrm{rpd}}=\tfrac12\ln\frac{2+\delta}{\delta},
\qquad
\theta_{\mathrm{pha}}=\theta_{\mathrm{phb}}=0,
$$

and the factor is

$$
\breve r_\delta=\rho(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}})=(1+\delta)+j=\breve Q_\delta.
$$

The two scales are $\rho e^{\theta_{\mathrm{rpd}}}=2+\delta$ and $\rho e^{-\theta_{\mathrm{rpd}}}=\delta$. The table gives the approach.

| $\delta$ | $\rho$ | $\theta_{\mathrm{rpd}}$ | $\rho e^{\theta_{\mathrm{rpd}}}$ | $\rho e^{-\theta_{\mathrm{rpd}}}$ |
|---|---|---|---|---|
| $0.1$ | $0.4582575695$ | $1.522261219$ | $2.1$ | $0.1$ |
| $0.01$ | $0.1417744688$ | $2.651652454$ | $2.01$ | $0.01$ |
| $0.001$ | $0.0447325385$ | $3.800701167$ | $2.001$ | $0.001$ |

As $\delta\to0$, the modulus tends to $0$, the boost diverges, and the larger scale tends to $2$; the factor tends to $1+j$. The polar decomposition exists on the unit group and stops exactly at $C_+C_-=0$.

## Summary

### Main Results

| Case | $\breve Q$ | $Q_{\blacktriangle}$ | $Q_{\blacktriangledown}$ | $C_+C_-$ | $\rho$ | $\theta_{\mathrm{rpd}}$ | $\theta_{\mathrm{pha}}$ | $\theta_{\mathrm{phb}}$ |
|---|---|---|---|---|---|---|---|---|
| $1$ | $3+4i+j(1-i)$ | $3+4i$ | $1-i$ | $-7+26i$ | $5.1890099283$ | $-0.0371050013$ | $0.9168955292$ | $-0.2733944204$ |
| $2$ | $1+i$ | $1+i$ | $0$ | $2i$ | $\sqrt2$ | $0$ | $\pi/4$ | $0$ |
| $3$ | $i$ | $i$ | $0$ | $-1$ | $1$ | $0$ | $\pi/2$ | $0$ |
| $4$ | $ij$ | $0$ | $i$ | $1$ | $1$ | $0$ | $0$ | $\pi/2$ |
| $5$ | $j$ | $0$ | $1$ | $-1$ | $1$ | $0$ | $\pi/2$ | $-\pi/2$ |
| $6$ | $\exp(j\ln2)$ | $\tfrac54$ | $\tfrac34$ | $1$ | $1$ | $\ln2$ | $0$ | $0$ |
| $7$ | $-1$ | $-1$ | $0$ | $1$ | $1$ | $0$ | $\pi$ | $0$ |
| $8$ | $1+j$ | $1$ | $1$ | $0$ | $0$ | — | — | — |

### The Reconstruction Table

| Case | $\breve Q$ | $\breve r$ | $u$ | $\breve r\,u$ | Error |
|---|---|---|---|---|---|
| $1$ | $3+4i+j(1-i)$ | $5.1925824036-0.1925824036j$ | $0.5856953382+0.7642383454i+j(0.2143046618-0.1642383454i)$ | $3+4i+j(1-i)$ | $1.3\times10^{-15}$ |
| $2$ | $1+i$ | $\sqrt2$ | $(1+i)/\sqrt2$ | $1+i$ | $2.2\times10^{-16}$ |
| $3$ | $i$ | $1$ | $i$ | $i$ | $6.1\times10^{-17}$ |
| $4$ | $ij$ | $1$ | $ij$ | $ij$ | $6.1\times10^{-17}$ |
| $5$ | $j$ | $1$ | $j$ | $j$ | $1.2\times10^{-16}$ |
| $6$ | $\exp(j\ln2)$ | $\tfrac54+\tfrac34j$ | $1$ | $\tfrac54+\tfrac34j$ | $0$ |
| $7$ | $-1$ | $1$ | $-1$ | $-1$ | $1.2\times10^{-16}$ |
| $8$ | $1+j$ | — | — | — | no word |

### What the Cases Show

- The two complex components determine the polar data. In every unit the four numbers $\rho,\theta_{\mathrm{rpd}},\theta_{\mathrm{pha}},\theta_{\mathrm{phb}}$ are read from $C_+$ and $C_-$ by the formulas of §*The Two Complex Components*, and $\lvert C_+\rvert$ and $\lvert C_-\rvert$ are the two scales.
- The central rows have $Q_{\blacktriangledown}=0$, hence $C_+=C_-$. The elements $1+i$, $i$ and $-1$ have $\theta_{\mathrm{rpd}}=0$ and lie on the torus; the two components coincide and the phases add.
- The elements $i$ and $ij$ are the two pure phases, with $\theta_{\mathrm{pha}}=\pi/2$ and $\theta_{\mathrm{phb}}=\pi/2$ respectively. Both have $\rho=1$ and $\theta_{\mathrm{rpd}}=0$; the difference is the phase, not the modulus.
- The elements $j$ and $-1$ lie on the boundary of the principal diamond. The first has $\theta_{\mathrm{pha}}=\pi/2$, $\theta_{\mathrm{phb}}=-\pi/2$; the second is the corner $(\pi,0)$. The polar data are still unique there, because the boundary is taken half-open.
- The hyperbolic line $\exp(j\ln2)$ has both phases zero and the boost $\ln2$. Its two scales are $2$ and $\tfrac12$, the two values of $\lvert C_\pm\rvert$.
- The zero divisor $1+j$ has $C_-=0$, but no polar word. The family shows the rate $\rho\to0$, $\theta_{\mathrm{rpd}}\to\infty$ with $\rho e^{\theta_{\mathrm{rpd}}}\to2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\mathrm{red}}$ | the reduced biquaternion algebra, $\mathbb{B}_{\mathrm{red}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ |
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | a reduced biquaternion |
| $Q_{\blacktriangle},Q_{\blacktriangledown}$ | the two complex coordinates |
| $C_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ | the two complex components |
| $C_+C_-=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$ | the product of the components |
| $\rho=\sqrt{\lvert C_+C_-\rvert}$ | the modulus |
| $\theta_{\mathrm{rpd}}$ | the real boost |
| $\theta_{\mathrm{pha}},\theta_{\mathrm{phb}}$ | the two phases, in the principal diamond |
| $\breve r=\rho(\cosh\theta_{\mathrm{rpd}}+j\sinh\theta_{\mathrm{rpd}})$ | the real-hyperbolic factor |
| $u=\exp(i\theta_{\mathrm{pha}})\exp(ij\theta_{\mathrm{phb}})$ | the torus factor |
| $\operatorname{Log}\breve Q=(\ln\rho+i\theta_{\mathrm{pha}})+j(\theta_{\mathrm{rpd}}+i\theta_{\mathrm{phb}})$ | the principal logarithm |
| $\mathsf M(\breve Q)$ | the block matrix $\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix}$ |
| $\delta$ | the parameter of the boundary family of case 8 |

## Further Reading

- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of Reduced Biquaternions](worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-reduced-biquaternions.md), for the eigenbasis, the idempotents and the spinors of the same eight cases.
- [Exponential Polar Decomposition of Reduced Biquaternions](exponential-polar-decomposition-of-reduced-biquaternions.html), for the decomposition, the principal diamond and uniqueness.
- [Reduced Biquaternion Elementary Functions](reduced-biquaternion-elementary-functions.html), for the exponential, the logarithm and the kernel.
- [Modulus–Unit Polar Decomposition of Reduced Biquaternions](modulus-unit-polar-decomposition-of-reduced-biquaternions.html), for the algebraic modulus–unit form.
- [Worked Examples of Exponential Polar Decomposition of Split-Complex Numbers](worked-examples-of-exponential-polar-decomposition-of-split-complex-numbers.html), for the two-dimensional companion.
- *Worked Examples of Exponential Polar Decomposition of Biquaternions*, for the noncommutative companion.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the exponential map and the torus.
