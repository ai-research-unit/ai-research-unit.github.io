# __Worked Examples of Exponential Polar Decomposition with Eigenbasis of a N-Regular, Spectrally Degenerate Biquaternion__

## Introduction

This article reads the eight elements of *Worked Examples of Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion* in their spectral basis. The sector has one eigenvalue, so the spectral basis is a Jordan chain, not an eigenbasis. The polar word itself, its coordinates and its checks are in that article; here the same elements are read through the chain.

The eight cases are the three scalar elements $e_t$, $-2e_t$ and $2i e_t$, and the five Jordan elements

$$
e_t+\vec e_x+i\vec e_y,
\qquad
e_t+\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z,
\qquad
(1+i)e_t+\vec e_x+i\vec e_y,
\qquad
-e_t-\vec e_x-i\vec e_y,
\qquad
2e_t+2\vec e_x+2i\vec e_y.
$$

Each element is written as $\tilde Q=Q_t(e_t+\vec\Upsilon)$ with $\vec\Upsilon^2=0$, and as $\tilde Q=r e^{i\alpha}\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\exp(\frac{\theta}{2}\vec u_{\mathrm r})$.

## The Chain, the Block and the Factors

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

## The Scalar Line

On the scalar line $\vec\Upsilon=0$ and $\tilde Q=Q_te_t$. Every basis is an eigenbasis, and the chain is any basis.

| Case | $\tilde Q$ | $Q_t$ | $\varepsilon$ | $\mathsf M(\tilde Q)$ | $\tilde U_{\mathrm b}$ | $\tilde u_{\mathrm r}$ |
|---|---|---|---|---|---|---|
| 1 | $e_t$ | $1$ | $+1$ | $I$ | $e_t$ | $e_t$ |
| 2 | $-2e_t$ | $-2$ | $-1$ | $-2I$ | $e_t$ | $-e_t$ |
| 3 | $2i e_t$ | $2i$ | $+1$ | $2iI$ | $e_t$ | $e_t$ |

The three cases have no Jordan defect. The unit factor is $\pm e_t$, the rapidity and the rotor angle vanish or are pure periods, and the polar factors are central.

## The Jordan Part

The five cases have the same block, with different scalars and chains.

| Case | $Q_t$ | $N=\mathsf M(\vec\Upsilon)$ | chain $v=Nw$, $w$ | $\mathsf M_{(v,w)}(\tilde Q)$ |
|---|---|---|---|---|
| 4 | $1$ | $\begin{pmatrix}0&-2i\\0&0\end{pmatrix}$ | $v=(-2i,0)$, $w=(0,1)$ | $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ |
| 5 | $1$ | $\begin{pmatrix}\tfrac{1}{\sqrt2}&\tfrac{1}{\sqrt2}-1\\ \tfrac{1}{\sqrt2}+1&-\tfrac{1}{\sqrt2}\end{pmatrix}$ | $v=(\tfrac{1}{\sqrt2},1+\tfrac{1}{\sqrt2})$, $w=(1,0)$ | $\begin{pmatrix}1&1\\0&1\end{pmatrix}$ |
| 6 | $1+i$ | $\begin{pmatrix}0&-2i\\0&0\end{pmatrix}$ | $v=(-2i,0)$, $w=(0,1)$ | $\begin{pmatrix}1+i&1\\0&1+i\end{pmatrix}$ |
| 7 | $-1$ | $\begin{pmatrix}0&2i\\0&0\end{pmatrix}$ | $v=(2i,0)$, $w=(0,1)$ | $\begin{pmatrix}-1&1\\0&-1\end{pmatrix}$ |
| 8 | $2$ | $\begin{pmatrix}0&-4i\\0&0\end{pmatrix}$ | $v=(-4i,0)$, $w=(0,1)$ | $\begin{pmatrix}2&1\\0&2\end{pmatrix}$ |

In every case the unit factor is $\varepsilon$ times the same unipotent block, with $\varepsilon=+1$ in cases 4, 5, 6 and 8, and $\varepsilon=-1$ in case 7. The rapidity and the rotor angle are those of the companion article; the scalar cases 1 to 3 are the only ones with no nilpotent part.

### Case 4 in Full

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

### Case 5 in Full

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

- The Jordan chain is explicit in every case; its vectors are not normalized, and the chain is not unique.
- The element and the unit factor are triangular in the chain, but the polar factors are not.
- The polar factors have distinct eigenvalues $e^{\pm\psi/2}$ and $e^{\pm i\theta/2}$; the element has the double eigenvalue $Q_t$ and the unit factor has the double eigenvalue $\varepsilon$.
- The scalar line is the only locus on which the chain and the polar frame can be chosen to agree.

## Summary

### Main Results

| Case | $\tilde Q$ | $Q_t$ | $\varepsilon$ | chain |
|---|---|---|---|---|
| 1 | $e_t$ | $1$ | $+1$ | any basis |
| 2 | $-2e_t$ | $-2$ | $-1$ | any basis |
| 3 | $2i e_t$ | $2i$ | $+1$ | any basis |
| 4 | $e_t+\vec e_x+i\vec e_y$ | $1$ | $+1$ | $v=(-2i,0)$, $w=(0,1)$ |
| 5 | $e_t+\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z$ | $1$ | $+1$ | $v=(\tfrac{1}{\sqrt2},1+\tfrac{1}{\sqrt2})$, $w=(1,0)$ |
| 6 | $(1+i)e_t+\vec e_x+i\vec e_y$ | $1+i$ | $+1$ | $v=(-2i,0)$, $w=(0,1)$ |
| 7 | $-e_t-\vec e_x-i\vec e_y$ | $-1$ | $-1$ | $v=(2i,0)$, $w=(0,1)$ |
| 8 | $2e_t+2\vec e_x+2i\vec e_y$ | $2$ | $+1$ | $v=(-4i,0)$, $w=(0,1)$ |

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
| $N=\langle\tilde Q\rangle_{\natural}$ | the reduced product |
| $B^2=\langle\vec Q,\vec Q\rangle_{\natural}$ | the vector form |
| $\vec\Upsilon=\vec Q/Q_t$ | the null vector of the normal form |
| $\varepsilon=Q_t/\Rho=\pm1$ | the sign of the unit factor |
| $\Rho$ | the modulus, principal square root of $N$ |
| $v,w$ | a Jordan chain, $Nw=v$ and $Nv=0$ |
| $\mathsf M_{(v,w)}$ | the matrix in the basis $(v,w)$ |
| $\tilde U_{\mathrm b},\tilde u_{\mathrm r}$ | the positive factor and the rotor |
| $\psi,\theta$ | the rapidity and the rotor angle |

## Further Reading

- [Relations between Exponential Polar Decomposition and Eigenbasis of a N-Regular, Spectrally Degenerate Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the Jordan reading in general.
- [Worked Examples of Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](worked-examples-of-exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html), for the coordinates, the word and the checks.
- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of a N-Regular, Spectrally Regular Biquaternion](worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-a-n-regular-spectrally-regular-biquaternion.html), for the regular side.
