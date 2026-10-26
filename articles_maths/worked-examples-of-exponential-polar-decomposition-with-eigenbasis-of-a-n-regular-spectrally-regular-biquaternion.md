# __Worked Examples of Exponential Polar Decomposition with Eigenbasis of a N-Regular, Spectrally Regular Biquaternion__

## Introduction

This article reads the eight elements of *Worked Examples of Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion* in their eigenbasis. The polar word, its coordinates and its checks are in that article; here the same elements are read through the eigenvalue decomposition.

On the N-regular, spectrally regular sector $N\neq0$ and $B^2\neq0$. The eigenvalues are distinct and nonzero,

$$
\lambda_\pm=Q_t\pm iB,
\qquad
B^2=Q_x^2+Q_y^2+Q_z^2,
\qquad
N=Q_t^2+B^2=\lambda_+\lambda_-,
$$

and the eigenprojectors are

$$
\tilde\Pi_\pm=\frac12\bigl(e_t\pm\vec\Xi\bigr),
\qquad
\vec\Xi=-i\frac{\vec Q}{B},
\qquad
\vec\Xi^2=-e_t.
$$

The two projectors are idempotent and orthogonal, $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\tilde\Pi_+\tilde\Pi_-=0$, and $\tilde\Pi_++\tilde\Pi_-=e_t$. The eigenvalues of the unit factor $\tilde U=\tilde Q/\Rho$ are

$$
\mu_\pm=\frac{\lambda_\pm}{\Rho}.
$$

In the normal case $\mu_\pm=e^{\mp\psi/2}e^{\pm i\theta/2}$; in the non-normal case the moduli of $\mu_\pm$ need not be $e^{\mp\psi/2}$, and that failure is the spectral gap of the sector.

## The Eight Cases

| Case | $\tilde Q$ | $\lambda_+$ | $\lambda_-$ | $\mu_+$ | $\mu_-$ | $\vec\Xi$ |
|---|---|---|---|---|---|---|
| 1 | $\vec e_x$ | $i$ | $-i$ | $i$ | $-i$ | $-i\vec e_x$ |
| 2 | $\sqrt2 e_t+i\vec e_x$ | $\sqrt2-1$ | $\sqrt2+1$ | $\sqrt2-1$ | $\sqrt2+1$ | $-i\vec e_x$ |
| 3 | $(1-\frac{i}{\sqrt2})e_t+(1+\frac{i}{\sqrt2})\vec e_x$ | $0.292893+0.292893i$ | $1.707107-1.707107i$ | $0.292893+0.292893i$ | $1.707107-1.707107i$ | $-i\vec e_x$ |
| 4 | $\frac{e_t+\vec e_x}{\sqrt2}$ | $\frac{1+i}{\sqrt2}$ | $\frac{1-i}{\sqrt2}$ | $\frac{1+i}{\sqrt2}$ | $\frac{1-i}{\sqrt2}$ | $-i\vec e_x$ |
| 5 | $(1-\frac{i}{2})e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z$ | $0.375189+0.300243i$ | $1.624811-1.300243i$ | $0.375189+0.300243i$ | $1.624811-1.300243i$ | see below |
| 6 | $(1+i)e_t+(1+i)\vec e_x+\vec e_y+\frac12\vec e_z$ | $0.255522+2.343223i$ | $1.744478-0.343223i$ | $0.778575+0.848287i$ | $0.587263-0.639845i$ | see below |
| 7 | $(1+i)(e_t+\vec e_x)$ | $2i$ | $2$ | $\frac{1+i}{\sqrt2}$ | $\frac{1-i}{\sqrt2}$ | $-i\vec e_x$ |
| 8 | $\vec e_x+\vec e_y$ | $i\sqrt2$ | $-i\sqrt2$ | $i$ | $-i$ | $-i\frac{\vec e_x+\vec e_y}{\sqrt2}$ |

The cases 1 to 4 and 7 are normal; their axes are the eigenlines, and $\mu_\pm=e^{\mp\psi/2}e^{\pm i\theta/2}$ with the parameters of the polar word. The cases 5 and 6 are non-normal; their eigenlines are not the polar axes, and the eigenvalues of the unit factor do not determine the two angles.

### The Non-Normal Eigenvectors

Case 5 has

$$
\vec\Xi
=(0.120345-0.977578i)\vec e_x
+(-0.428617-0.548962i)\vec e_y
+(0.388175-0.303078i)\vec e_z.
$$

Case 6 has

$$
\vec\Xi
=(0.253867-0.885183i)\vec e_x
+(-0.315658-0.569525i)\vec e_y
+(-0.157829-0.284763i)\vec e_z.
$$

In both cases $\vec\Xi^2=-e_t$, and the reconstruction

$$
\tilde Q=\lambda_+\frac{e_t+\vec\Xi}{2}+\lambda_-\frac{e_t-\vec\Xi}{2}
$$

returns the element. The vectors are complex and not parallel to the polar axes.

## Case 5 in Full

The element is

$$
\tilde Q=\Bigl(1-\frac{i}{2}\Bigr)e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z.
$$

The eigenvalues are

$$
\lambda_+=0.375189+0.300243i,
\qquad
\lambda_-=1.624811-1.300243i,
$$

with product $N=1$ and sum $2Q_t=2-i$. The eigenprojectors are $\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi)$ with the vector above. The unit factor is $\tilde U=\tilde Q$ because $N=1$, so $\mu_\pm=\lambda_\pm$.

The polar word has $r=1$, $\alpha=0$, $\psi=1.762747174$, $\theta=\frac{\pi}{2}$, $\vec u_{\mathrm b}=\vec e_x$ and $\vec u_{\mathrm r}=(\vec e_x+\vec e_y)/\sqrt2$. The eigenlines are not the axes: $\vec\Xi$ is not parallel to $\vec e_x$ or to $(\vec e_x+\vec e_y)/\sqrt2$. The eigenvalues of $\tilde U$ have moduli $0.480534$ and $2.081019$, whose ratio is $4.331$ and whose logarithm is $1.4657$, not the rapidity $1.7627$. This is the spectral gap: the spectrum gives two complex numbers, and the word needs two angles and two axes.

## Case 3 in Full

The element is

$$
\tilde Q=\Bigl(1-\frac{i}{\sqrt2}\Bigr)e_t+\Bigl(1+\frac{i}{\sqrt2}\Bigr)\vec e_x.
$$

The eigenvalues are

$$
\lambda_+=0.292893+0.292893i,
\qquad
\lambda_-=1.707107-1.707107i,
$$

and the eigenprojectors are $\tilde\Pi_\pm=\frac12(e_t\mp i\vec e_x)$. The unit factor is $\tilde U=\tilde Q$ because $N=1$, and its eigenvalues are the same. The polar word has $r=1$, $\alpha=0$, $\psi=1.762747174$, $\theta=\frac{\pi}{2}$, and the axes coincide, $\vec u_{\mathrm b}=\vec u_{\mathrm r}=\vec e_x$. In this normal case

$$
\mu_\pm=e^{\mp\psi/2}e^{\pm i\theta/2}
=e^{\mp0.881374}e^{\pm i\pi/4},
$$

which reproduces the values above. The eigenbasis and the polar frame agree, and the spectral gap is zero.

## What the Examples Show

- The eigenvalues are distinct and nonzero on the whole sector; the eigenbasis exists in every case.
- The eigenprojectors are explicit through $\vec\Xi=-i\vec Q/B$; the vector is complex and has square $-e_t$.
- In the normal cases the eigenlines are the polar axes and the unit eigenvalues factor into a modulus and a phase.
- In the non-normal cases the eigenlines are not the axes, and the unit eigenvalues do not determine the rapidity and the rotor angle.
- The reconstruction $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ is exact in every case, including the non-normal ones.

## Summary

### Main Results

| Item | Value |
|---|---|
| eigenvalues | $\lambda_\pm=Q_t\pm iB$ |
| eigenprojectors | $\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi)$ |
| eigenvector | $\vec\Xi=-i\vec Q/B$, $\vec\Xi^2=-e_t$ |
| unit eigenvalues | $\mu_\pm=\lambda_\pm/\Rho$ |
| normal factorisation | $\mu_\pm=e^{\mp\psi/2}e^{\pm i\theta/2}$ |
| non-normal gap | the moduli of $\mu_\pm$ need not be $e^{\mp\psi/2}$ |
| reconstruction | $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ |

### The Cases

| Case | Character | Axes and eigenlines | Gap |
|---|---|---|---|
| 1 | normal rotor | same | $0$ |
| 2 | normal boost | same | $0$ |
| 3 | normal, parallel axes | same | $0$ |
| 4 | normal rotor | same | $0$ |
| 5 | non-normal | different | $1.4657$ vs $1.7627$ |
| 6 | non-normal | different | $0.2820$ vs $0.6968$ |
| 7 | normal with phase | same | $0$ |
| 8 | normal pure vector | same | $0$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion |
| $N=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | the reduced product |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the vector form |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |
| $\vec\Xi=-i\vec Q/B$ | the eigenvector |
| $\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi)$ | the eigenprojectors |
| $\Rho$ | the modulus |
| $\mu_\pm=\lambda_\pm/\Rho$ | the eigenvalues of the unit factor |
| $\psi,\theta$ | the rapidity and the rotor angle |

## Further Reading

- [Relations between Exponential Polar Decomposition and Eigenbasis of a N-Regular, Spectrally Regular Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-n-regular-spectrally-regular-biquaternion.html), for the general spectral reading.
- [Worked Examples of Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](worked-examples-of-exponential-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html), for the coordinates, the word and the checks.
- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of a N-Regular, Spectrally Degenerate Biquaternion](worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the Jordan side.
