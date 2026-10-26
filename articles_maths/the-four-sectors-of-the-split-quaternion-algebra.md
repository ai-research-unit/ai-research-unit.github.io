# __The Four Sectors of the Split-Quaternion Algebra__

## Introduction

Two quadratic conditions act on a split quaternion $q=t+\vec v$. The norm $q\bar q=t^2-S$ vanishes exactly on the zero-divisor cone $\mathcal Z$, and the square of the vector part $S=\vec v^2=-q_x^2+q_y^2+q_z^2$ vanishes exactly on the spectral cone $\mathcal C$. Each condition has two values, zero and non-zero, so the pair of signs divides the algebra into four sectors. This article defines the sectors, proves that all four are non-empty, describes each one, and computes their closures and dimensions. The spectral theory is *Spectral Regularity and Degeneracy in the Split-Quaternion Algebra*; the comparison of the two conditions is *Relations between the Split-Quaternion Norm and Spectral Regularity and Degeneracy*; the norm and the zero divisors are *Split-Quaternion Norm and Invertibility* and *Split-Quaternion Zero Divisors*.

**Notation.** A general element is $q=t+\vec v$, with $t\in\mathbb R$ and $\vec v=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$. The basis is $e_t=1,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x^2=-e_t$, $\vec e_y^2=\vec e_z^2=+e_t$ and $\vec e_x\vec e_y=\vec e_z$. Conjugation is $\bar q=t-\vec v$, and

$$
q\bar q=t^2-S=t^2+q_x^2-q_y^2-q_z^2,\qquad
S:=\vec v^2=-q_x^2+q_y^2+q_z^2.
$$

The algebra and its multiplication table are *Split-Quaternion Algebra*.

## The Four Sectors

**Definition (the sectors).** Put $i=1$ when $t^2\neq S$ and $i=0$ when $t^2=S$; put $j=1$ when $S\neq0$ and $j=0$ when $S=0$. The **sector** $\Sigma_{ij}$ is the set of elements with these values. Explicitly,

$$
\Sigma_{11}=\{q:t^2\neq S,\ S\neq0\},\qquad
\Sigma_{10}=\{q:t^2\neq S,\ S=0\},
$$
$$
\Sigma_{01}=\{q:t^2=S,\ S\neq0\},\qquad
\Sigma_{00}=\{q:t^2=S,\ S=0\}.
$$

The index $i$ records the norm: $i=1$ on the complement of $\mathcal Z$, $i=0$ on $\mathcal Z$. The index $j$ records the spectrum: $j=1$ on the complement of $\mathcal C$, $j=0$ on $\mathcal C$.

**Proposition (the sectors form a partition).** Every element lies in exactly one sector.

*Proof.* The two numbers $t^2-S$ and $S$ are each either zero or non-zero, giving four disjoint cases, and every element falls into one of them.

**Corollary (the meaning of the indices).** The following are equivalent: $i=1$; $q$ is a unit; $q\notin\mathcal Z$. The following are equivalent: $i=0$; $q$ is a non-unit; $q\in\mathcal Z$. The following are equivalent: $j=1$; $q$ has two distinct eigenvalues; $q\notin\mathcal C$. The following are equivalent: $j=0$; $q$ has a repeated eigenvalue; $q\in\mathcal C$.

*Proof.* By *Split-Quaternion Norm and Invertibility*, $q$ is a unit exactly when $t^2-S\neq0$, and the non-zero elements of $\mathcal Z$ are the zero divisors. By *Spectral Regularity and Degeneracy in the Split-Quaternion Algebra*, the eigenvalues are distinct exactly when $S\neq0$.

The sectors therefore refine both dichotomies at once: the row $i=1$ consists of units, the row $i=0$ of non-units; the column $j=1$ consists of spectrally regular elements, the column $j=0$ of spectrally degenerate elements.

**Proposition (the sectors are cones).** If $q\in\Sigma_{ij}$ and $\lambda>0$, then $\lambda q\in\Sigma_{ij}$.

*Proof.* The two conditions are homogeneous of degree two: $(\lambda t)^2-\lambda^2S=\lambda^2(t^2-S)$ and $\lambda^2S$. Multiplication by $\lambda>0$ preserves zero and non-zero values, so it preserves both indices.

## Non-Emptiness

**Theorem (all four sectors are non-empty).** Each sector contains one of the following elements.

| sector | witness | $t$ | $S$ | $t^2-S$ |
|---|---|---|---|---|
| $\Sigma_{11}$ | $2+\vec e_x$ | $2$ | $-1$ | $5$ |
| $\Sigma_{10}$ | $1+\vec e_x+\vec e_y$ | $1$ | $0$ | $1$ |
| $\Sigma_{01}$ | $1+\vec e_y$ | $1$ | $1$ | $0$ |
| $\Sigma_{00}$ | $\vec e_x+\vec e_y$ | $0$ | $0$ | $0$ |

*Proof.* The values in the table are computed from $S=-q_x^2+q_y^2+q_z^2$ and $t^2-S$. In each row the signs of $S$ and of $t^2-S$ match the sector. For the last row, $(\vec e_x+\vec e_y)^2=\vec e_x^2+\vec e_x\vec e_y+\vec e_y\vec e_x+\vec e_y^2=-1+\vec e_z-\vec e_z+1=0$, so $S=0$. The witnesses show that $\Sigma_{10}$ contains the scalar $1$ and the non-scalar $1+\vec e_x+\vec e_y$, and that $\Sigma_{00}$ contains the origin and the non-zero nilpotent $\vec e_x+\vec e_y$.

## Description of Each Sector

### $\Sigma_{11}$: Units off Both Cones

On $\Sigma_{11}$ the norm is non-zero and $S\neq0$. The element is a unit, the two eigenvalues $t\pm\sqrt S$ are distinct, and $L_q$ is semisimple. The minimal polynomial is $(\lambda-t)^2-S$, the characteristic polynomial is its square, over $\mathbb C$ each eigenspace has dimension $2$ and an eigenbasis exists. The eigenvalues are real when $S>0$ and a complex conjugate pair when $S<0$. The sector is open in $\mathbb H_{\mathrm s}$ and has dimension $4$.

### $\Sigma_{10}$: Units on the Spectral Cone

On $\Sigma_{10}$ the norm is $t^2-S=t^2$, so the element is a unit exactly when $t\neq0$; the condition $t^2\neq S=0$ already gives $t\neq0$. Thus every element of $\Sigma_{10}$ is a unit on the spectral cone. The sector splits into two parts:

$$
\Sigma_{10}^{\mathrm s}=\{q:t\neq0,\ \vec v=0\},\qquad
\Sigma_{10}^{\mathrm{def}}=\{q:t\neq0,\ \vec v\neq0,\ S=0\}.
$$

The first is the punctured scalar line. On it $q=t$ and $L_q=t\,\mathrm{id}$; the minimal polynomial is $\lambda-t$, the Jordan type is $(1,1,1,1)$, and the element is semisimple. It has dimension $1$.

The second is the defective part. On it $\vec v^2=0$, $\vec v\neq0$, and $L_q$ has minimal polynomial $(\lambda-t)^2$, characteristic polynomial $(\lambda-t)^4$, eigenspace $\ker L_{\vec v}$ of dimension $2$, and Jordan type $(2,2)$. No eigenbasis exists. It has dimension $3$.

A unit on the spectral cone is therefore defective exactly when its vector part is non-zero. The scalar units are semisimple. The element $1+\vec e_x+\vec e_y$ is a defective unit, with inverse $1-\vec e_x-\vec e_y$.

### $\Sigma_{01}$: Zero Divisors off the Spectral Cone

On $\Sigma_{01}$ the norm is zero and $S=t^2\neq0$. The element is a zero divisor and is spectrally regular. Its eigenvalues are $0$ and $2t$, its minimal polynomial is $\lambda(\lambda-2t)$, and its characteristic polynomial is $\lambda^2(\lambda-2t)^2$. It is semisimple, with an eigenbasis, and each eigenspace has dimension $2$. Moreover

$$
q^2=2tq,
$$

so $e=q/(2t)$ is a non-zero idempotent, $f=1-e$ is a non-zero idempotent, $ef=0$, and $q=2t\,e$ is the spectral decomposition. The sector has dimension $3$; it is open in the zero-divisor cone, which is smooth off the origin. The element $1+\vec e_y$ is an example, with $e=(1+\vec e_y)/2$ and $f=(1-\vec e_y)/2$.

### $\Sigma_{00}$: The Nilpotent Cone and the Origin

On $\Sigma_{00}$ both conditions hold: $t=0$ and $S=0$. The element is $q=\vec v$ with $\vec v^2=0$, so $q^2=0$. Conversely, if $q^2=0$ then $q\in\Sigma_{00}$: from $q^2=(t^2+S)+2t\vec v$, either $\vec v\neq0$ gives $t=0$ and then $S=0$, or $\vec v=0$ gives $t=0$ and $S=0$. Hence $\Sigma_{00}$ is exactly the nilpotent cone

$$
N_V=\{q=\vec v:\vec v^2=0\}=\{q_x^2=q_y^2+q_z^2\}.
$$

It splits into the origin and the non-zero nilpotents. At the origin $L_0=0$, the minimal polynomial is $\lambda$, the characteristic polynomial is $\lambda^4$, the Jordan type is $(1,1,1,1)$, and the element is semisimple; its dimension is $0$. At a non-zero nilpotent $q=\vec v$, the minimal polynomial is $\lambda^2$, the characteristic polynomial is $\lambda^4$, the eigenspace is $\ker L_{\vec v}$ of dimension $2$, and the Jordan type is $(2,2)$; the element is defective. This part has dimension $2$. The nilpotent cone is a double cone over a circle: for $\vec v\neq0$ write $q_x=\pm r$ and $(q_y,q_z)=r(\cos\theta,\sin\theta)$ with $r>0$.

## Closure and Dimensions

**Theorem (closures).** The closures of the sectors are

$$
\overline{\Sigma_{11}}=\mathbb H_{\mathrm s},\qquad
\overline{\Sigma_{10}}=\mathcal C,\qquad
\overline{\Sigma_{01}}=\mathcal Z,\qquad
\overline{\Sigma_{00}}=\Sigma_{00}.
$$

*Proof.* The set $\Sigma_{11}$ is the complement of $\mathcal Z\cup\mathcal C$, a finite union of zero sets of non-zero polynomials, so it is open and dense; its closure is $\mathbb H_{\mathrm s}$. The sector $\Sigma_{10}$ is $\mathcal C$ with the slice $t=0$ removed; every point of that slice is a limit of points with $t\neq0$ and the same vector part, so its closure is $\mathcal C$. The sector $\Sigma_{01}$ is $\mathcal Z$ with the slice $S=0$ removed; every point of that slice is a limit of points of $\mathcal Z$ with $S>0$ and $t=\sqrt S$ (add a small multiple of $\vec e_y$ if necessary), so its closure is $\mathcal Z$. The sector $\Sigma_{00}$ is the zero set of the two polynomials $t$ and $S$, hence closed.

**Corollary (the common boundary).** The origin lies in the closure of every sector, and

$$
\overline{\Sigma_{10}}\cap\overline{\Sigma_{01}}=\mathcal C\cap\mathcal Z=\Sigma_{00}.
$$

*Proof.* The origin lies in $\mathbb H_{\mathrm s}$, in $\mathcal C$ and in $\mathcal Z$, and $\Sigma_{00}$ contains it. The intersection of the two cone closures is the intersection of the two cones, which is $\Sigma_{00}$ by definition.

**Theorem (dimensions and openness).** The dimensions of the sectors are $4,3,3,2$ in the order $\Sigma_{11},\Sigma_{10},\Sigma_{01},\Sigma_{00}$. The sector $\Sigma_{11}$ is the only one open in $\mathbb H_{\mathrm s}$. The sectors $\Sigma_{10}$ and $\Sigma_{01}$ are open in $\mathcal C$ and $\mathcal Z$ respectively, and $\Sigma_{00}$ is closed.

*Proof.* The sector $\Sigma_{11}$ is open in $\mathbb R^4$, so it has dimension $4$. The cone $\mathcal C=\mathbb R\times N_V$ has dimension $3$, and $\Sigma_{10}$ is open in it, so $\Sigma_{10}$ has dimension $3$; the scalar part has dimension $1$ and the defective part has dimension $3$. The cone $\mathcal Z$ has dimension $3$ and is smooth off the origin, and $\Sigma_{01}=\mathcal Z\setminus N_V$ is open in it, so $\Sigma_{01}$ has dimension $3$. The nilpotent cone $N_V$ has dimension $2$, and the origin has dimension $0$. A sector on a proper cone is not open in $\mathbb R^4$, and $\Sigma_{00}$ is closed by the closure theorem.

**Summary table.**

| sector | condition | description | dimension |
|---|---|---|---|
| $\Sigma_{11}$ | $t^2\neq S,\ S\neq0$ | units with two distinct eigenvalues; semisimple; open and dense | $4$ |
| $\Sigma_{10}$ | $t^2\neq S,\ S=0$ | units on the spectral cone; scalar part semisimple, defective part Jordan $(2,2)$ | $3$ |
| $\Sigma_{01}$ | $t^2=S,\ S\neq0$ | zero divisors with spectrum $\{0,2t\}$; semisimple; $q=2t e$ | $3$ |
| $\Sigma_{00}$ | $t^2=S,\ S=0$ | the origin and the non-zero nilpotents; closed | $2$ |

## Summary

The four sectors are the four sign combinations of the norm $t^2-S$ and the spectral form $S$. All four are non-empty: $2+\vec e_x$ lies in $\Sigma_{11}$, $1+\vec e_x+\vec e_y$ in $\Sigma_{10}$, $1+\vec e_y$ in $\Sigma_{01}$, and $\vec e_x+\vec e_y$ in $\Sigma_{00}$. Each sector is a cone.

The sector $\Sigma_{11}$ consists of units with simple spectrum; it is open and dense, of dimension $4$. The sector $\Sigma_{10}$ consists of units on the spectral cone. Its scalar part $t\neq0$, $\vec v=0$ is semisimple, and its defective part $t\neq0$, $\vec v\neq0$, $S=0$ has minimal polynomial $(\lambda-t)^2$ and Jordan type $(2,2)$; the sector has dimension $3$. A unit on the spectral cone is defective exactly when $\vec v\neq0$.

The sector $\Sigma_{01}$ consists of zero divisors with simple spectrum $\{0,2t\}$; it is semisimple, with $q=2t e$ and $e=q/(2t)$ idempotent, and has dimension $3$. The sector $\Sigma_{00}$ is the nilpotent cone $q_x^2=q_y^2+q_z^2$, consisting of the origin and the non-zero nilpotents; it has dimension $2$ and is closed. The closures are $\mathbb H_{\mathrm s}$, $\mathcal C$, $\mathcal Z$ and $\Sigma_{00}$; the origin lies in the closure of every sector, and $\Sigma_{00}$ is the intersection of the two cones.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb H_{\mathrm s}$ | the split-quaternion algebra |
| $q=t+\vec v$ | a general element |
| $S=\vec v^2=-q_x^2+q_y^2+q_z^2$ | the square of the vector part |
| $q\bar q=t^2-S$ | the split-quaternion norm |
| $\mathcal Z=\{t^2=S\}$ | the zero-divisor cone |
| $\mathcal C=\{S=0\}$ | the spectral cone |
| $\Sigma_{ij}$ | the sector with norm index $i$ and spectral index $j$ |
| $\Sigma_{10}^{\mathrm s}$ | the scalar part of $\Sigma_{10}$ |
| $\Sigma_{10}^{\mathrm{def}}$ | the defective part of $\Sigma_{10}$ |
| $N_V=\{q_x^2=q_y^2+q_z^2\}$ | the nilpotent cone, equal to $\Sigma_{00}$ |

## Further Reading

- [Spectral Regularity and Degeneracy in the Split-Quaternion Algebra](spectral-regularity-and-degeneracy-in-the-split-quaternion-algebra.html), for the spectral polynomials, the spectral cone and the defective stratum.
- [Relations between the Split-Quaternion Norm and Spectral Regularity and Degeneracy](relations-between-the-split-quaternion-norm-and-spectral-regularity-and-degeneracy.html), for the independence of the two conditions and the chain of invariants.
- [Split-Quaternion Norm and Invertibility](split-quaternion-norm-and-invertibility.html), for the norm, its isotropy and the unit criterion.
- [Split-Quaternion Zero Divisors](split-quaternion-zero-divisors.html), for the zero-divisor cone, the minimal ideals and the nilpotents.
- [Split-Quaternion Spectral Theory](split-quaternion-spectral-theory.html), for the spectrum and the eigenvalue problems.
- [Split-Quaternion Algebra](split-quaternion-algebra.html), for the multiplication table and the conjugations.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (2nd edition, Cambridge University Press, 2013), for the Jordan form and the spectral decomposition.
