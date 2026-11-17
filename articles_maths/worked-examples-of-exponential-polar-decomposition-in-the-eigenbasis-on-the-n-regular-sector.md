# __Worked Examples of Exponential Polar Decomposition in the Eigenbasis on the N-Regular Sector__

## Introduction

This article reads the sixteen numerical cases of *Worked Examples of Exponential Polar Decomposition on the N-Regular Sector* through their spectral data. Off the wall the spectral data are an eigenbasis with two distinct eigenvalues. On the wall they are a single eigenvalue and a Jordan chain. The word, its coordinates and its checks are in that article; here the same elements are read the other way, and the two readings are compared case by case.

The numbering is the one of that article: cases $1$ to $8$ off the wall, cases $9$ to $16$ on it. Each case is given by its eigenvalues and its spectral basis, and the spectral values are compared with the polar ones.

**The plan.** §*The Spectral Setup* fixes the eigenvalues, the eigenprojectors and the unit-factor eigenvalues off the wall. §*The Cases off the Wall* gives the table of the eight cases, with the non-normal eigenvectors and two cases in full. §*On the Wall* replaces the eigenbasis by a Jordan chain, gives the chain and the factor matrices of the eight cases, and works two of them in full. §*What the Examples Show* and §*Summary* collect the results.

## The Spectral Setup

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
\tilde\Pi_\pm=\frac12\bigl(e_t\pm\vec{Ζ}\bigr),
\qquad
\vec{Ζ}=-i\frac{\vec Q}{B},
\qquad
\vec{Ζ}^2=-e_t.
$$

The two projectors are idempotent and orthogonal, $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\tilde\Pi_+\tilde\Pi_-=0$, and $\tilde\Pi_++\tilde\Pi_-=e_t$. The eigenvalues of the unit factor $\tilde U=\tilde Q/\Rho$ are

$$
\mu_\pm=\frac{\lambda_\pm}{\Rho}.
$$

In the normal case $\mu_\pm=e^{\mp\theta_{\mathrm{rpd}}/2}e^{\pm i\theta_{\mathrm{axr}}/2}$; in the non-normal case the moduli of $\mu_\pm$ need not be $e^{\mp\theta_{\mathrm{rpd}}/2}$, and that failure is the spectral gap of the sector.

## The Cases off the Wall

| Case | $\tilde Q$ | $\lambda_+$ | $\lambda_-$ | $\mu_+$ | $\mu_-$ | $\vec{Ζ}$ |
|---|---|---|---|---|---|---|
| 1 | $\vec e_x$ | $i$ | $-i$ | $i$ | $-i$ | $-i\vec e_x$ |
| 2 | $\sqrt2 e_t+i\vec e_x$ | $\sqrt2-1$ | $\sqrt2+1$ | $\sqrt2-1$ | $\sqrt2+1$ | $-i\vec e_x$ |
| 3 | $(1-\frac{i}{\sqrt2})e_t+(1+\frac{i}{\sqrt2})\vec e_x$ | $0.292893+0.292893i$ | $1.707107-1.707107i$ | $0.292893+0.292893i$ | $1.707107-1.707107i$ | $-i\vec e_x$ |
| 4 | $\frac{e_t+\vec e_x}{\sqrt2}$ | $\frac{1+i}{\sqrt2}$ | $\frac{1-i}{\sqrt2}$ | $\frac{1+i}{\sqrt2}$ | $\frac{1-i}{\sqrt2}$ | $-i\vec e_x$ |
| 5 | $(1-\frac{i}{2})e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z$ | $0.375189+0.300243i$ | $1.624811-1.300243i$ | $0.375189+0.300243i$ | $1.624811-1.300243i$ | see below |
| 6 | $(1+i)e_t+(1+i)\vec e_x+\vec e_y+\frac12\vec e_z$ | $0.255522+2.343223i$ | $1.744478-0.343223i$ | $0.778575+0.848287i$ | $0.587263-0.639845i$ | see below |
| 7 | $(1+i)(e_t+\vec e_x)$ | $2i$ | $2$ | $\frac{1+i}{\sqrt2}$ | $\frac{1-i}{\sqrt2}$ | $-i\vec e_x$ |
| 8 | $\vec e_x+\vec e_y$ | $i\sqrt2$ | $-i\sqrt2$ | $i$ | $-i$ | $-i\frac{\vec e_x+\vec e_y}{\sqrt2}$ |

The cases 1 to 4 and 7 are normal; their axes are the eigenlines, and $\mu_\pm=e^{\mp\theta_{\mathrm{rpd}}/2}e^{\pm i\theta_{\mathrm{axr}}/2}$ with the parameters of the polar word. The cases 5 and 6 are non-normal; their eigenlines are not the polar axes, and the eigenvalues of the unit factor do not determine the two angles.

### The Non-Normal Eigenvectors

Case 5 has

$$
\vec{Ζ}
=(0.120345-0.977578i)\vec e_x
+(-0.428617-0.548962i)\vec e_y
+(0.388175-0.303078i)\vec e_z.
$$

Case 6 has

$$
\vec{Ζ}
=(0.253867-0.885183i)\vec e_x
+(-0.315658-0.569525i)\vec e_y
+(-0.157829-0.284763i)\vec e_z.
$$

In both cases $\vec{Ζ}^2=-e_t$, and the reconstruction

$$
\tilde Q=\lambda_+\frac{e_t+\vec{Ζ}}{2}+\lambda_-\frac{e_t-\vec{Ζ}}{2}
$$

returns the element. The vectors are complex and not parallel to the polar axes.

### Case 5 in Full

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

with product $N=1$ and sum $2Q_t=2-i$. The eigenprojectors are $\tilde\Pi_\pm=\frac12(e_t\pm\vec{Ζ})$ with the vector above. The unit factor is $\tilde U=\tilde Q$ because $N=1$, so $\mu_\pm=\lambda_\pm$.

The polar word has $r=1$, $\theta_{\mathrm{pha}}=0$, $\theta_{\mathrm{rpd}}=1.762747174$, $\theta_{\mathrm{axr}}=\frac{\pi}{2}$, $\vec u_{\mathrm b}=\vec e_x$ and $\vec u_{\mathrm r}=(\vec e_x+\vec e_y)/\sqrt2$. The eigenlines are not the axes: $\vec{Ζ}$ is not parallel to $\vec e_x$ or to $(\vec e_x+\vec e_y)/\sqrt2$. The eigenvalues of $\tilde U$ have moduli $0.480534$ and $2.081019$, whose ratio is $4.331$ and whose logarithm is $1.4657$, not the rapidity $1.7627$. This is the spectral gap: the spectrum gives two complex numbers, and the word needs two angles and two axes.

### Case 3 in Full

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

and the eigenprojectors are $\tilde\Pi_\pm=\frac12(e_t\mp i\vec e_x)$. The unit factor is $\tilde U=\tilde Q$ because $N=1$, and its eigenvalues are the same. The polar word has $r=1$, $\theta_{\mathrm{pha}}=0$, $\theta_{\mathrm{rpd}}=1.762747174$, $\theta_{\mathrm{axr}}=\frac{\pi}{2}$, and the axes coincide, $\vec u_{\mathrm b}=\vec u_{\mathrm r}=\vec e_x$. In this normal case

$$
\mu_\pm=e^{\mp\theta_{\mathrm{rpd}}/2}e^{\pm i\theta_{\mathrm{axr}}/2}
=e^{\mp0.881374}e^{\pm i\pi/4},
$$

which reproduces the values above. The eigenbasis and the polar frame agree, and the spectral gap is zero.

## On the Wall

The wall has one eigenvalue and no eigenbasis. The spectral object is the Jordan chain of §*The Chain, the Block and the Factors*, and the spectral values are the scalar part $Q_t$ and the sign $\varepsilon$ alone. Cases $9$ to $11$ are the scalar line, where every basis is an eigenbasis; cases $12$ to $16$ are the Jordan part, where the chain is a genuine Jordan chain.

### The Chain, the Block and the Factors

On the Jordan part the matrix model is $\mathsf M(\tilde Q)=Q_t(I+N)$ with $N=\mathsf M(\vec\Upsilon)$, $N^2=0$ and $N\neq0$. Choose a vector $w$ with $v=Nw\neq0$. Then $v\in\ker N$, and $(v,w)$ is a Jordan chain. In that basis,

$$
\mathsf M_{(v,w)}(\tilde Q)=Q_t
\begin{pmatrix}
1 & 1\\
0 & 1
\end{pmatrix},
\qquad
\mathsf M_{(v,w)}(\tilde U)=\varepsilon
\begin{pmatrix}
1 & 1\\
0 & 1
\end{pmatrix}.
$$

The chain is not unique: $w$ may be replaced by $w+cv$, and $v$ may be rescaled.

The polar factors are read in the same basis. The positive factor and the rotor are not triangular in general; their matrices are full, and only their product is the unipotent block. The diagonal entries of their matrices are not the eigenvalues, because the basis is not orthonormal. What the chain does show is the eigenline and the size of the nilpotent part.

### The Scalar Line

On the scalar line $\vec\Upsilon=0$ and $\tilde Q=Q_te_t$. Every basis is an eigenbasis, and the chain is any basis.

| Case | $\tilde Q$ | $Q_t$ | $\varepsilon$ | $\mathsf M(\tilde Q)$ | $\tilde U_{\mathrm b}$ | $\tilde u_{\mathrm r}$ |
|---|---|---|---|---|---|---|
| 9 | $e_t$ | $1$ | $+1$ | $I$ | $e_t$ | $e_t$ |
| 10 | $-2e_t$ | $-2$ | $-1$ | $-2I$ | $e_t$ | $-e_t$ |
| 11 | $2i e_t$ | $2i$ | $+1$ | $2iI$ | $e_t$ | $e_t$ |

The three cases have no Jordan defect. The unit factor is $\pm e_t$, the rapidity and the rotor angle vanish or are pure periods, and the polar factors are central.

### The Jordan Part

The five cases have the same block, with different scalars and chains.

| Case | $Q_t$ | $N=\mathsf M(\vec\Upsilon)$ | chain $v=Nw$, $w$ | $\mathsf M_{(v,w)}(\tilde Q)$ |
|---|---|---|---|---|
| 12 | $1$ | $\begin{pmatrix}0&-2i\\0&0\end{pmatrix}$ | $v=(-2i,0)$, $w=(0,1)$ | $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ |
| 13 | $1$ | $\begin{pmatrix}\tfrac{1}{\sqrt2}&\tfrac{1}{\sqrt2}-1\\ \tfrac{1}{\sqrt2}+1&-\tfrac{1}{\sqrt2}\end{pmatrix}$ | $v=(\tfrac{1}{\sqrt2},1+\tfrac{1}{\sqrt2})$, $w=(1,0)$ | $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ |
| 14 | $1+i$ | $\begin{pmatrix}0&-2i\\0&0\end{pmatrix}$ | $v=(-2i,0)$, $w=(0,1)$ | $\begin{pmatrix}1+i&1\\0&1+i\end{pmatrix}$ |
| 15 | $-1$ | $\begin{pmatrix}0&2i\\0&0\end{pmatrix}$ | $v=(2i,0)$, $w=(0,1)$ | $\begin{pmatrix}-1&1\\0&-1\end{pmatrix}$ |
| 16 | $2$ | $\begin{pmatrix}0&-4i\\0&0\end{pmatrix}$ | $v=(-4i,0)$, $w=(0,1)$ | $\begin{pmatrix}2&1\\0&2\end{pmatrix}$ |

In every case the unit factor is $\varepsilon$ times the same unipotent block, with $\varepsilon=+1$ in cases $12$, $13$, $14$ and $16$, and $\varepsilon=-1$ in case $15$. The rapidity and the rotor angle are the ones of *Worked Examples of Exponential Polar Decomposition on the N-Regular Sector*; the scalar cases $9$ to $11$ are the only ones with no nilpotent part.



### Case 12 in Full

For $\tilde Q=e_t+\vec e_x+i\vec e_y$ the chain is $v=(-2i,0)$, $w=(0,1)$, and the two polar factors are

$$
\mathsf M_{(v,w)}(\tilde U_{\mathrm b})
=
\frac{1}{\sqrt2}
\begin{pmatrix}
3 & \tfrac12\\
2 & 1
\end{pmatrix},
\qquad
\mathsf M_{(v,w)}(\tilde u_{\mathrm r})
=
\frac{1}{\sqrt2}
\begin{pmatrix}
1 & \tfrac12\\
-2 & 1
\end{pmatrix}.
$$

Neither matrix is triangular: the lower-left entries are nonzero. Their product is the unipotent block. The eigenline is spanned by $v=(-2i,0)$, and the image of $v$ under either factor is not proportional to $v$. The polar factors therefore move the eigenline, while their product preserves it.

### Case 13 in Full

For $\tilde Q=e_t+\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z$ the chain is $v=(\tfrac{1}{\sqrt2},1+\tfrac{1}{\sqrt2})$, $w=(1,0)$. The factors are

$$
\mathsf M_{(v,w)}(\tilde U_{\mathrm b})
=
\begin{pmatrix}
2\sqrt2-1 & 2-\sqrt2\\
\sqrt2 & 1
\end{pmatrix},
\qquad
\mathsf M_{(v,w)}(\tilde u_{\mathrm r})
=
\begin{pmatrix}
1 & \sqrt2-1\\
-\sqrt2 & \sqrt2-1
\end{pmatrix}.
$$

The entries are the exact forms of the decimals $1.82843,0.585786,1.41421,1$ and $1,0.414214,-1.41421,0.414214$. Again the factors are full and the product is the unipotent block.

## What the Examples Show

- Off the wall the eigenvalues are distinct and nonzero in every case, and the eigenbasis exists in every case.
- The eigenprojectors are explicit through $\vec{Ζ}=-i\vec Q/B$; the vector is complex and has square $-e_t$.
- In the normal cases the eigenlines are the polar axes, and the unit eigenvalues factor into a modulus and a phase. In the non-normal cases the eigenlines are not the axes, and the unit eigenvalues do not determine the rapidity and the rotor angle. The reconstruction $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ is exact in all eight cases, including the non-normal ones.
- On the wall the spectral object is a Jordan chain. It is explicit in every case, its vectors are not normalized, and the chain is not unique.
- On the wall the element and the unit factor are triangular in the chain, and the polar factors are not.
- The polar factors have distinct eigenvalues $e^{\pm\theta_{\mathrm{rpd}}/2}$ and $e^{\pm i\theta_{\mathrm{axr}}/2}$; the element has the double eigenvalue $Q_t$ and the unit factor has the double eigenvalue $\varepsilon$. The scalar line is the only locus on which the chain and the polar frame can be chosen to agree.

## Summary

### Main Results, Off the Wall

| Item | Value |
|---|---|
| eigenvalues | $\lambda_\pm=Q_t\pm iB$ |
| eigenprojectors | $\tilde\Pi_\pm=\frac12(e_t\pm\vec{Ζ})$ |
| eigenvector | $\vec{Ζ}=-i\vec Q/B$, $\vec{Ζ}^2=-e_t$ |
| unit eigenvalues | $\mu_\pm=\lambda_\pm/\Rho$ |
| normal factorisation | $\mu_\pm=e^{\mp\theta_{\mathrm{rpd}}/2}e^{\pm i\theta_{\mathrm{axr}}/2}$ |
| non-normal gap | the moduli of $\mu_\pm$ need not be $e^{\mp\theta_{\mathrm{rpd}}/2}$ |
| reconstruction | $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ |

### The Cases, Off the Wall

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

### The Chains, On the Wall

| Case | $\tilde Q$ | $Q_t$ | $\varepsilon$ | chain |
|---|---|---|---|---|
| 9 | $e_t$ | $1$ | $+1$ | any basis |
| 10 | $-2e_t$ | $-2$ | $-1$ | any basis |
| 11 | $2i e_t$ | $2i$ | $+1$ | any basis |
| 12 | $e_t+\vec e_x+i\vec e_y$ | $1$ | $+1$ | $v=(-2i,0)$, $w=(0,1)$ |
| 13 | $e_t+\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z$ | $1$ | $+1$ | $v=(\tfrac{1}{\sqrt2},1+\tfrac{1}{\sqrt2})$, $w=(1,0)$ |
| 14 | $(1+i)e_t+\vec e_x+i\vec e_y$ | $1+i$ | $+1$ | $v=(-2i,0)$, $w=(0,1)$ |
| 15 | $-e_t-\vec e_x-i\vec e_y$ | $-1$ | $-1$ | $v=(2i,0)$, $w=(0,1)$ |
| 16 | $2e_t+2\vec e_x+2i\vec e_y$ | $2$ | $+1$ | $v=(-4i,0)$, $w=(0,1)$ |

### The Block

| Object | Matrix in the chain |
|---|---|
| element | $Q_t\begin{pmatrix}1&1\\0&1\end{pmatrix}$ |
| unit factor | $\varepsilon\begin{pmatrix}1&1\\0&1\end{pmatrix}$ |
| positive factor | full, not triangular |
| rotor | full, not triangular |
| product of the factors | the unipotent block |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion |
| $N=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | the reduced product |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the vector form |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |
| $\vec{Ζ}=-i\vec Q/B$ | the eigenvector |
| $\tilde\Pi_\pm=\frac12(e_t\pm\vec{Ζ})$ | the eigenprojectors |
| $\Rho$ | the modulus |
| $\mu_\pm=\lambda_\pm/\Rho$ | the eigenvalues of the unit factor |
| $\theta_{\mathrm{rpd}},\theta_{\mathrm{axr}}$ | the rapidity and the rotor angle |
| $\vec\Upsilon=\vec Q/Q_t$ | the null vector of the normal form |
| $\varepsilon=Q_t/\Rho=\pm1$ | the sign of the unit factor on the wall |
| $v,w$ | a Jordan chain, $Nw=v$ and $Nv=0$ |
| $\mathsf M_{(v,w)}$ | the matrix in the basis $(v,w)$ |

## Further Reading

- [Worked Examples of Exponential Polar Decomposition on the N-Regular Sector](worked-examples-of-exponential-polar-decomposition-on-the-n-regular-sector.html), for the coordinates, the word and the checks of the sixteen cases.
- [Relations between Exponential Polar Decomposition and Eigenbasis on the N-Regular Sector](relations-between-exponential-polar-decomposition-and-eigenbasis-on-the-n-regular-sector.html), for the general spectral reading and its collapse on the wall.
- [The Complete Polar Decomposition on the N-Regular Sector](the-complete-polar-decomposition-on-the-n-regular-sector.html), for the theorem, the proofs and the spectral reading.
- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), for the eigenvalues and the eigenprojectors.
- [The Jordan Basis of a Spectrally Degenerate Biquaternion](the-jordan-basis-of-a-spectrally-degenerate-biquaternion.html), for the chain selected by the Hermitian form.
