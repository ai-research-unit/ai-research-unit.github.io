# __Worked Examples of Exponential Polar Decomposition of Split-Complex Numbers__

## Introduction

This article computes the exponential polar decomposition of eight split-complex numbers, one after another. It is the computational companion of *Exponential Polar Decomposition of Split-Complex Numbers*. The decomposition, its existence and uniqueness, the component sign and the exponential and logarithm are established in that article and in *Split-Complex Elementary Functions*; no definition or proof is repeated.

Each case is read from the two coordinates $q$ and $q'$ of $Q=q+jq'$. The modulus, the angle and the component sign are computed from them by the formulas of §*The Method*, and the word is checked against the reconstruction

$$
Q=r\,\epsilon\,e^{\phi j}.
$$

The eight cases cover the four open components, the pure discrete unit, the two scalar directions and the boundary.

| Group | Case | What it shows |
|---|---|---|
| Future cone | $5+3j$ | the generic case, $\epsilon=1$ |
| Right wedge | $3+5j$ | the same modulus and angle as $5+3j$, $\epsilon=j$ |
| Past cone | $-5-3j$ | the same modulus and angle, $\epsilon=-1$ |
| Left wedge | $1-2j$ | a negative angle, $\epsilon=-j$ |
| Discrete unit | $j$ | a pure component sign, $\phi=0$ |
| Positive scalar | $2$ | a pure scale, $\epsilon=1$ |
| Negative scalar | $-2$ | the same exponent as $2$, $\epsilon=-1$ |
| Null cone | $1+j$ | $(q+q')(q-q')=0$, but no polar word |

**The plan.** The method is stated once (§*The Method*). The eight cases follow (§*The Eight Cases*), each with its coordinates, its polar data, its word and its check. The summary collects the results in two tables and reads the patterns across the cases (§*Summary*). The eigenbasis, the idempotents and the spinors of the same eight cases are collected in *Worked Examples of Exponential Polar Decomposition with Eigenbasis of Split-Complex Numbers*.

## The Method

### The Coordinates

For $Q=q+jq'$ the two real coordinates are $q$ and $q'$. The modulus and the angle are

$$
r=\sqrt{\lvert q^2-q'^2\rvert}
=\sqrt{\lvert(q+q')(q-q')\rvert},
\qquad
\phi=\tfrac12\ln\left\lvert\frac{q+q'}{q-q'}\right\rvert.
$$

The component sign is read from the quadrant of the pair $(q,q')$:

| Condition | $\epsilon$ | Component |
|---|---|---|
| $q>\lvert q'\rvert$ | $1$ | future cone $F$ |
| $q<-\lvert q'\rvert$ | $-1$ | past cone |
| $q'>\lvert q\rvert$ | $j$ | right wedge $R$ |
| $q'<-\lvert q\rvert$ | $-j$ | left wedge $L$ |

The four conditions are exclusive and cover every unit. In every row the product $\epsilon Q$ lies in $F$.

The two combinations are recovered from the polar data by

$$
\boxed{\; r\,e^{\phi}=\lvert q+q'\rvert,
\qquad
r\,e^{-\phi}=\lvert q-q'\rvert \;}
$$

These two identities are the check used in every case.

### The Reconstruction

The polar word is

$$
\boxed{\; Q=\epsilon\,r\,e^{\phi j}=r\,\epsilon\bigl(\cosh\phi+j\sinh\phi\bigr),
\qquad
Q_{\log}=\ln r+j\phi \;}
$$

The exponent of $\epsilon Q$ and the unit factor $\epsilon e^{\phi j}$ are read separately, and the reconstruction is the scale $r$ times the unit factor. The check is the multiplication.

### The Matrix Picture

The matrix of multiplication by $Q$ in the basis $(1,j)$ is

$$
M_Q=\begin{pmatrix}q&q'\\q'&q\end{pmatrix}.
$$

Its trace is $2q$ and its determinant is $q^2-q'^2=(q+q')(q-q')$. It is invertible exactly when $Q$ is a unit. The product $\epsilon Q$ acts on $F$ by a positive scale and a hyperbolic rotation.

### The Null Cone

For $q^2-q'^2=0$ the element is a nonzero zero divisor, of the form $Q=q(1\pm j)$ with $q\neq0$, and no polar word exists: the modulus vanishes, the angle diverges and the unit factor is undefined. The matrix has rank one, its determinant is zero, and $Q^2=2q\,Q$. Case 8 treats the boundary explicitly.

## The Eight Cases

### Case 1: A Generic Element of the Future Cone

**Coordinates.** For $Q=5+3j$,

$$
q=5,
\qquad
q'=3,
\qquad
q^2-q'^2=25-9=16,
\qquad
q+q'=8,
\qquad
q-q'=2.
$$

Since $q>\lvert q'\rvert$, the component sign is $\epsilon=1$.

**Polar data.** The modulus and the angle are

$$
r=\sqrt{16}=4,
\qquad
\phi=\tfrac12\ln\frac{8}{2}=\ln2,
\qquad
\epsilon=1.
$$

The two combinations check: $r e^{\phi}=4\cdot2=8=q+q'$ and $r e^{-\phi}=4\cdot\tfrac12=2=q-q'$.

**The word.** The exponent and the unit factor are

$$
Q_{\log}=\ln4+j\ln2,
\qquad
\epsilon e^{\phi j}=\cosh(\ln2)+j\sinh(\ln2)=\tfrac54+\tfrac34j.
$$

Therefore

$$
Q=4\left(\tfrac54+\tfrac34j\right)=5+3j.
$$

**Check.** The exponential of the exponent is

$$
\exp(Q_{\log})=4\bigl(\cosh(\ln2)+j\sinh(\ln2)\bigr)=4\left(\tfrac54+\tfrac34j\right)=5+3j,
$$

and the error is $0$. The matrix

$$
M_Q=\begin{pmatrix}5&3\\3&5\end{pmatrix}
$$

has trace $10$ and determinant $16$.

### Case 2: A Generic Element of the Right Wedge

**Coordinates.** For $Q=3+5j$,

$$
q=3,
\qquad
q'=5,
\qquad
q^2-q'^2=9-25=-16,
\qquad
q+q'=8,
\qquad
q-q'=-2.
$$

Since $q'>\lvert q\rvert$, the component sign is $\epsilon=j$.

**Polar data.** The modulus and the angle are

$$
r=\sqrt{\lvert-16\rvert}=4,
\qquad
\phi=\tfrac12\ln\left\lvert\frac{8}{-2}\right\rvert=\ln2,
\qquad
\epsilon=j.
$$

The two combinations check: $r e^{\phi}=8=\lvert q+q'\rvert$ and $r e^{-\phi}=2=\lvert q-q'\rvert$.

**The word.** The exponent is the same string as in case 1,

$$
Q_{\log}=\ln4+j\ln2,
$$

but the unit factor is different:

$$
\epsilon e^{\phi j}=j\left(\tfrac54+\tfrac34j\right)=\tfrac34+\tfrac54j.
$$

Therefore

$$
Q=4\left(\tfrac34+\tfrac54j\right)=3+5j.
$$

**Check.** The product $\epsilon Q=jQ=5+3j$ lies in $F$, and

$$
\exp(Q_{\log})=5+3j=\epsilon Q.
$$

The exponent is a logarithm of $\epsilon Q$, not of $Q$. The error in $Q$ is $0$. The matrix

$$
M_Q=\begin{pmatrix}3&5\\5&3\end{pmatrix}
$$

has trace $6$ and determinant $-16$.

### Case 3: A Generic Element of the Past Cone

**Coordinates.** For $Q=-5-3j$,

$$
q=-5,
\qquad
q'=-3,
\qquad
q^2-q'^2=25-9=16,
\qquad
q+q'=-8,
\qquad
q-q'=-2.
$$

Since $q<-\lvert q'\rvert$, the component sign is $\epsilon=-1$.

**Polar data.** The modulus and the angle are again

$$
r=4,
\qquad
\phi=\ln2,
\qquad
\epsilon=-1.
$$

The two combinations check: $r e^{\phi}=8=\lvert q+q'\rvert$ and $r e^{-\phi}=2=\lvert q-q'\rvert$.

**The word.** The exponent is again $\ln4+j\ln2$, and the unit factor is

$$
\epsilon e^{\phi j}=-\left(\tfrac54+\tfrac34j\right).
$$

Therefore

$$
Q=4\left(-\tfrac54-\tfrac34j\right)=-5-3j.
$$

**Check.** The product $\epsilon Q=-Q=5+3j$ lies in $F$, and $\exp(Q_{\log})=5+3j=\epsilon Q$ with error $0$. The matrix

$$
M_Q=\begin{pmatrix}-5&-3\\-3&-5\end{pmatrix}
$$

has trace $-10$ and determinant $16$.

### Case 4: A Generic Element of the Left Wedge

**Coordinates.** For $Q=1-2j$,

$$
q=1,
\qquad
q'=-2,
\qquad
q^2-q'^2=1-4=-3,
\qquad
q+q'=-1,
\qquad
q-q'=3.
$$

Since $q'<-\lvert q\rvert$, the component sign is $\epsilon=-j$.

**Polar data.** The modulus is $\sqrt3$ and the angle is negative:

$$
r=\sqrt{\lvert-3\rvert}=\sqrt3,
\qquad
\phi=\tfrac12\ln\left\lvert\frac{-1}{3}\right\rvert=-\tfrac12\ln3,
\qquad
\epsilon=-j.
$$

The two combinations check: $r e^{\phi}=\sqrt3\cdot\tfrac{1}{\sqrt3}=1=\lvert q+q'\rvert$ and $r e^{-\phi}=\sqrt3\cdot\sqrt3=3=\lvert q-q'\rvert$.

**The word.** The exponent is

$$
Q_{\log}=\ln\sqrt3-\tfrac12\ln3\,j=\tfrac12\ln3-\tfrac12\ln3\,j,
$$

and the unit factor is

$$
\epsilon e^{\phi j}=-j\left(\frac{2}{\sqrt3}-\frac{1}{\sqrt3}j\right)
=\frac{1}{\sqrt3}-\frac{2}{\sqrt3}j.
$$

Therefore

$$
Q=\sqrt3\left(\frac{1}{\sqrt3}-\frac{2}{\sqrt3}j\right)=1-2j.
$$

**Check.** The product $\epsilon Q=-j(1-2j)=2-j$ lies in $F$, and

$$
\exp(Q_{\log})=\sqrt3\left(\frac{2}{\sqrt3}-\frac{1}{\sqrt3}j\right)=2-j=\epsilon Q.
$$

The error is $2.2\times10^{-16}$. The matrix

$$
M_Q=\begin{pmatrix}1&-2\\-2&1\end{pmatrix}
$$

has trace $2$ and determinant $-3$.

### Case 5: The Discrete Unit

**Coordinates.** For $Q=j$,

$$
q=0,
\qquad
q'=1,
\qquad
q^2-q'^2=-1,
\qquad
q+q'=1,
\qquad
q-q'=-1.
$$

Since $q'>\lvert q\rvert$, the component sign is $\epsilon=j$.

**Polar data.** The modulus is one and the angle vanishes:

$$
r=1,
\qquad
\phi=0,
\qquad
\epsilon=j.
$$

The two combinations check: $r e^{\phi}=1=\lvert q+q'\rvert$ and $r e^{-\phi}=1=\lvert q-q'\rvert$.

**The word.** The exponent is $Q_{\log}=0$, and the unit factor is $\epsilon e^{\phi j}=j$. Therefore

$$
Q=1\cdot j=j.
$$

**Check.** $\exp(0)=1$, so $\exp(Q_{\log})=1=\epsilon Q$, and the error is $0$. The matrix

$$
M_Q=\begin{pmatrix}0&1\\1&0\end{pmatrix}
$$

has trace $0$ and determinant $-1$. The element is the pure component sign: no scale and no angle.

### Case 6: The Positive Scalar

**Coordinates.** For $Q=2$,

$$
q=2,
\qquad
q'=0,
\qquad
q^2-q'^2=4,
\qquad
q+q'=2,
\qquad
q-q'=2.
$$

Since $q>\lvert q'\rvert$, the component sign is $\epsilon=1$.

**Polar data.** The modulus is two and the angle vanishes:

$$
r=2,
\qquad
\phi=0,
\qquad
\epsilon=1.
$$

The two combinations check: $r e^{\phi}=2=q+q'$ and $r e^{-\phi}=2=q-q'$.

**The word.** The exponent is

$$
Q_{\log}=\ln2,
$$

and the unit factor is $1$. Therefore

$$
Q=2\cdot1=2.
$$

**Check.** $\exp(\ln2)=2$, with error $0$. The matrix $M_Q=2I$ has trace $4$ and determinant $4$.

### Case 7: The Negative Scalar

**Coordinates.** For $Q=-2$,

$$
q=-2,
\qquad
q'=0,
\qquad
q^2-q'^2=4,
\qquad
q+q'=-2,
\qquad
q-q'=-2.
$$

Since $q<-\lvert q'\rvert$, the component sign is $\epsilon=-1$.

**Polar data.** The modulus is two and the angle vanishes:

$$
r=2,
\qquad
\phi=0,
\qquad
\epsilon=-1.
$$

The two combinations check: $r e^{\phi}=2=\lvert q+q'\rvert$ and $r e^{-\phi}=2=\lvert q-q'\rvert$.

**The word.** The exponent is the same as in case 6,

$$
Q_{\log}=\ln2,
$$

and the unit factor is $-1$. Therefore

$$
Q=2\cdot(-1)=-2.
$$

**Check.** $\exp(\ln2)=2=\epsilon Q$, with error $0$. The matrix $M_Q=-2I$ has trace $-4$ and determinant $4$. Cases 6 and 7 show that the exponent does not determine the element: the component sign does.

### Case 8: The Null Cone

**Coordinates.** For $Q=1+j$,

$$
q=1,
\qquad
q'=1,
\qquad
q^2-q'^2=1-1=0,
\qquad
q+q'=2,
\qquad
q-q'=0.
$$

The product $Q\bar Q$ vanishes, so there is no modulus, no angle and no component sign: the element is a zero divisor.

**No polar word.** The exponential has image $F$ and is injective, so $Q\notin F$ has no logarithm. The matrix

$$
M_Q=\begin{pmatrix}1&1\\1&1\end{pmatrix}
$$

has rank one and determinant $0$. Its square is

$$
Q^2=2Q.
$$

**The boundary.** The element is the limit of the future-cone family

$$
Q_\delta=(1+\delta)+j,
\qquad
\delta>0.
$$

Its coordinates give

$$
r=\sqrt{\delta(2+\delta)},
\qquad
\phi=\tfrac12\ln\frac{2+\delta}{\delta},
\qquad
\epsilon=1,
$$

and the two combinations are $r e^{\phi}=2+\delta$ and $r e^{-\phi}=\delta$. The table gives the approach.

| $\delta$ | $r$ | $\phi$ | $r e^{\phi}$ | $r e^{-\phi}$ |
|---|---|---|---|---|
| $0.1$ | $0.4582575695$ | $1.522261219$ | $2.1$ | $0.1$ |
| $0.01$ | $0.1417744688$ | $2.651652454$ | $2.01$ | $0.01$ |
| $0.001$ | $0.0447325385$ | $3.800701167$ | $2.001$ | $0.001$ |

As $\delta\to0$, the modulus tends to $0$, the angle diverges, and the larger combination tends to $2$; the word tends to the boundary value $1+j$. The polar decomposition exists on the open components and stops exactly at $q^2-q'^2=0$.

## Summary

### Main Results

| Case | $Q$ | $q$ | $q'$ | $q^2-q'^2$ | $\epsilon$ | $r$ | $\phi$ | $Q_{\log}$ |
|---|---|---|---|---|---|---|---|---|
| $1$ | $5+3j$ | $5$ | $3$ | $16$ | $1$ | $4$ | $\ln2$ | $\ln4+j\ln2$ |
| $2$ | $3+5j$ | $3$ | $5$ | $-16$ | $j$ | $4$ | $\ln2$ | $\ln4+j\ln2$ |
| $3$ | $-5-3j$ | $-5$ | $-3$ | $16$ | $-1$ | $4$ | $\ln2$ | $\ln4+j\ln2$ |
| $4$ | $1-2j$ | $1$ | $-2$ | $-3$ | $-j$ | $\sqrt3$ | $-\tfrac12\ln3$ | $\tfrac12\ln3-\tfrac12\ln3\,j$ |
| $5$ | $j$ | $0$ | $1$ | $-1$ | $j$ | $1$ | $0$ | $0$ |
| $6$ | $2$ | $2$ | $0$ | $4$ | $1$ | $2$ | $0$ | $\ln2$ |
| $7$ | $-2$ | $-2$ | $0$ | $4$ | $-1$ | $2$ | $0$ | $\ln2$ |
| $8$ | $1+j$ | $1$ | $1$ | $0$ | — | — | — | none |

### The Reconstruction Table

| Case | $Q$ | Unit factor $\epsilon e^{\phi j}$ | $r$ times the unit factor | Error |
|---|---|---|---|---|
| $1$ | $5+3j$ | $\tfrac54+\tfrac34j$ | $5+3j$ | $0$ |
| $2$ | $3+5j$ | $\tfrac34+\tfrac54j$ | $3+5j$ | $0$ |
| $3$ | $-5-3j$ | $-\tfrac54-\tfrac34j$ | $-5-3j$ | $0$ |
| $4$ | $1-2j$ | $\tfrac{1}{\sqrt3}-\tfrac{2}{\sqrt3}j$ | $1-2j$ | $2.2\times10^{-16}$ |
| $5$ | $j$ | $j$ | $j$ | $0$ |
| $6$ | $2$ | $1$ | $2$ | $0$ |
| $7$ | $-2$ | $-1$ | $-2$ | $0$ |
| $8$ | $1+j$ | — | — | no word |

### What the Cases Show

- Cases 1 to 3 share the modulus $r=4$ and the angle $\phi=\ln2$. The two combinations $(q+q',q-q')$ are $(8,2)$, $(8,-2)$ and $(-8,-2)$, and the exponent is the same string in all three; only $\epsilon$ changes. Case 4 completes the four quadrants, with a different modulus and a negative angle.
- Cases 2 and 3 have $\exp(Q_{\log})=\epsilon Q$, not $Q$. The exponent is the logarithm of the element pushed into the future cone.
- Case 4 has $q>0$ but $q+q'<0$, so the component is the left wedge, not the future cone. The sign of $q$ does not determine the component.
- Cases 6 and 7 have the same exponent $\ln2$ and differ only by $\epsilon$. The discrete factor is not a period: the kernel of the exponential is $\{0\}$.
- Case 5 is the pure discrete factor, with $r=1$ and $\phi=0$.
- Case 8 is the boundary. The matrix has rank one, while the polar word does not exist. The family shows the rate $r\to0$, $\phi\to\infty$ with $r e^{\phi}\to2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | the split-complex algebra, $j^2=+1$ |
| $Q=q+jq'$ | a split-complex number |
| $q,q'$ | the two real coordinates |
| $q^2-q'^2=(q+q')(q-q')$ | the product $Q\bar Q$ |
| $\epsilon\in\{1,-1,j,-j\}$ | the component sign |
| $r=\sqrt{\lvert q^2-q'^2\rvert}$ | the modulus |
| $\phi$ | the hyperbolic angle |
| $Q_{\log}=\ln r+j\phi$ | the exponent, a logarithm of $\epsilon Q$ |
| $F,R,L$ | the future cone and the two spacelike wedges |
| $M_Q$ | the real symmetric matrix of multiplication by $Q$ |
| $\delta$ | the parameter of the boundary family of case 8 |

## Further Reading

- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of Split-Complex Numbers](worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-split-complex-numbers.md), for the eigenbasis, the idempotents and the spinors of the same eight cases.
- [Exponential Polar Decomposition of Split-Complex Numbers](exponential-polar-decomposition-of-split-complex-numbers.html), for the decomposition, existence, uniqueness and the component sign.
- [Split-Complex Elementary Functions](split-complex-elementary-functions.html), for the exponential, the logarithm and the future cone.
- [Modulus–Unit Polar Decomposition of Split-Complex Numbers](modulus-unit-polar-decomposition-of-split-complex-numbers.html), for the algebraic modulus–unit form.
- [Worked Examples of Exponential Polar Decomposition of Reduced Biquaternions](worked-examples-of-exponential-polar-decomposition-of-reduced-biquaternions.html), for the commutative four-dimensional companion.
- *Worked Examples of Exponential Polar Decomposition of Biquaternions*, for the noncommutative companion.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the hyperbolic functions and the split-complex exponential.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the exponential map and the four components of the unit group.
