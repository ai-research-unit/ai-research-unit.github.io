# __Relations between the Split-Quaternion Norm and Spectral Regularity and Degeneracy__

## Introduction

The split-quaternion algebra carries two quadratic conditions on one element. The split-quaternion norm is $q\bar q=t^2-S$, and the square of the vector part is $S=\vec v^2=-q_x^2+q_y^2+q_z^2$. The first is multiplicative and detects zero divisors; the second is the spectral discriminant and detects repeated eigenvalues. The two conditions are different. Neither implies the other, and neither is a function of the other. This article compares them, proves their independence, identifies their zero sets and their intersection, and shows how the norm, the characteristic polynomial and the minimal polynomial form a chain of invariants with two, four and six types. The spectral theory itself is *Spectral Regularity and Degeneracy in the Split-Quaternion Algebra*; the four combinations are *The Four Sectors of the Split-Quaternion Algebra*.

**Notation.** A general element is $q=t+\vec v$, with $t\in\mathbb R$ and $\vec v=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$. The basis is $e_t=1,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_x^2=-e_t$, $\vec e_y^2=\vec e_z^2=+e_t$ and $\vec e_x\vec e_y=\vec e_z$. Conjugation is $\bar q=t-\vec v$, and

$$
q\bar q=t^2-S=t^2+q_x^2-q_y^2-q_z^2,\qquad
S:=\vec v^2=-q_x^2+q_y^2+q_z^2.
$$

The algebra and its multiplication table are *Split-Quaternion Algebra*. The norm and the zero divisors are *Split-Quaternion Norm and Invertibility* and *Split-Quaternion Zero Divisors*.

## The Two Quadratic Conditions

**Definition (the two conditions).** The **norm condition** is $t^2-S=0$, and the **spectral condition** is $S=0$. Their zero sets are

$$
\mathcal Z=\{q:t^2-S=0\},\qquad
\mathcal C=\{q:S=0\}.
$$

The set $\mathcal Z$ is the **zero-divisor cone**: by *Split-Quaternion Norm and Invertibility*, its non-zero elements are exactly the zero divisors. The set $\mathcal C$ is the **spectral cone**: by *Spectral Regularity and Degeneracy in the Split-Quaternion Algebra*, its elements are exactly those with a repeated eigenvalue.

Both conditions are homogeneous quadratics on $\mathbb R^4$. The form $S$ depends only on the vector part and has signature $(2,1)$ on $\mathbb R^3$. The form $t^2-S$ depends on $t$ as well and has signature $(2,2)$ on $\mathbb R^4$.

**Theorem (logical independence).** Neither condition implies the other.

*Proof.* The element $1+\vec e_y$ has $q\bar q=1-1=0$ and $S=1$, so it is norm-degenerate and spectrally regular. The element $1+\vec e_x+\vec e_y$ has $q\bar q=1-0=1$ and $S=-1+1=0$, so it is norm-regular and spectrally degenerate. Hence $\mathcal Z$ is not contained in $\mathcal C$, and $\mathcal C$ is not contained in $\mathcal Z$.

**Theorem (algebraic independence).** The two quadratic forms $t^2-S$ and $S$ are algebraically independent in $\mathbb R[t,q_x,q_y,q_z]$.

*Proof.* Their gradients are

$$
\nabla(t^2-S)=(2t,2q_x,-2q_y,-2q_z),\qquad
\nabla S=(0,-2q_x,2q_y,2q_z).
$$

At $1+\vec e_y$ these are $(2,0,-2,0)$ and $(0,0,2,0)$, which are linearly independent. If $P(t^2-S,S)=0$ for a non-zero polynomial $P$, differentiation gives

$$
P_x(t^2-S,S)\nabla(t^2-S)+P_y(t^2-S,S)\nabla S=0.
$$

On the open set where the gradients are independent, $P_x$ and $P_y$ vanish. The image of $(t^2-S,S)$ has non-empty interior (it contains the half-plane $a+b>0$), so $P_x=P_y=0$ identically; then $P$ is constant, and $P(0,0)=0$, so $P=0$, a contradiction.

The two forms are therefore independent in both the logical and the algebraic sense.

## The Two Cones and Their Intersection

**Theorem (the intersection).** The intersection of the two cones is

$$
\mathcal Z\cap\mathcal C=\{q:t=0,\ S=0\}=N_V,
\qquad
N_V=\{\vec v\in V:\vec v^2=0\}.
$$

It is the nilpotent cone: $q^2=0$ exactly on $\mathcal Z\cap\mathcal C$.

*Proof.* The equality $\mathcal Z\cap\mathcal C=\{t=0,S=0\}$ is immediate from $t^2=S$ and $S=0$. For $q=t+\vec v$,

$$
q^2=(t^2+S)+2t\vec v,
$$

so $q^2=0$ exactly when $t^2+S=0$ and $t\vec v=0$. If $\vec v\neq0$ this gives $t=0$ and $S=0$; if $\vec v=0$ it gives $t=0$. Hence $q^2=0$ exactly on $\mathcal Z\cap\mathcal C$. The intersection is not the origin: $\vec e_x+\vec e_y$ satisfies $S=0$ and is a non-zero nilpotent, since $(\vec e_x+\vec e_y)^2=0$.

**Theorem (geometry of the intersection and the two cones).** The cones $\mathcal Z$ and $\mathcal C$ both have dimension $3$. Their intersection $N_V$ has dimension $2$. The cone $\mathcal Z$ is smooth off the origin and singular at the origin. The cone $\mathcal C$ is smooth off the scalar line and singular along the whole scalar line. The two cones are tangent along $N_V\setminus\{0\}$.

*Proof.* The gradients of $t^2-S$ and $S$ are displayed above. The gradient of $t^2-S$ vanishes only at the origin, so $\mathcal Z$ is smooth off the origin; the gradient of $S$ vanishes exactly when $\vec v=0$, so $\mathcal C$ is smooth off the scalar line and singular along it. Both have dimension $3$. The intersection is one equation $q_x^2=q_y^2+q_z^2$ in $V$, with non-zero gradient off the origin, so it has dimension $2$. On $N_V\setminus\{0\}$ we have $t=0$, and the two gradients are $(0,2q_x,-2q_y,-2q_z)$ and $(0,-2q_x,2q_y,2q_z)$, which are opposite; hence the tangent planes coincide.

The intersection is not the origin, so the cones are not disjoint. They meet along the whole nilpotent cone, a two-dimensional subset of $\mathbb R^4$. The complement of their union is the open dense set $\Sigma_{11}$ of *The Four Sectors of the Split-Quaternion Algebra*; the union has empty interior, because it is a finite union of zero sets of non-zero polynomials.

## Zero Divisors with Non-Zero Trace

**Theorem (simple spectrum on the zero-divisor cone).** Let $q=t+\vec v$ with $t^2=S$ and $t\neq0$. Then $q$ is a zero divisor, $q$ is spectrally regular, and $q$ is semisimple. Its eigenvalues are $0$ and $2t$, and

$$
q^2=2tq.
$$

Moreover $e=q/(2t)$ is a non-zero idempotent, $f=1-e$ is a non-zero idempotent, $ef=0$, and $q=2t\,e$ is the spectral decomposition of $q$.

*Proof.* The norm is $q\bar q=t^2-S=0$, and $q\neq0$ because $t\neq0$; hence $q$ is a zero divisor. The reduced characteristic polynomial is

$$
p_q(\lambda)=(\lambda-t)^2-S=\lambda^2-2t\lambda=\lambda(\lambda-2t),
$$

whose roots $0$ and $2t$ are distinct because $t\neq0$. Hence $S=t^2\neq0$, so $q$ is spectrally regular. Cayley–Hamilton gives $q^2-2tq+(t^2-S)=0$, that is $q^2=2tq$. Dividing by $2t$ gives $e^2=e$. The element $e$ is non-zero because $q$ is. If $f=1-e$ were zero, then $q=2t$ would be scalar and $S=0$, contradicting $S=t^2\neq0$; so $f$ is non-zero. Finally $ef=e-e^2=0$, and $q=2t e=2t e+0\cdot f$. The decomposition is unique because the eigenvalues are distinct.

**Example.** For $q=1+\vec e_y$ we have $t=1$, $S=1$, $e=(1+\vec e_y)/2$ and $f=(1-\vec e_y)/2$. The spectrum is $\{0,2\}$, and $q$ is a zero divisor with an eigenbasis. The zero-divisor cone is therefore not contained in the spectral cone, and a zero divisor need not be defective.

## Units on the Spectral Cone

**Theorem (units and defect on the spectral cone).** Let $S=0$. Then $q$ is a unit exactly when $t\neq0$. If $t\neq0$ and $\vec v\neq0$, then $q$ is defective: its minimal polynomial is $(\lambda-t)^2$, its characteristic polynomial is $(\lambda-t)^4$, its eigenspace has dimension $2$, and its Jordan type is $(2,2)$. If $t\neq0$ and $\vec v=0$, then $q=t$ is scalar and semisimple, with minimal polynomial $\lambda-t$ and Jordan type $(1,1,1,1)$.

*Proof.* On $\mathcal C$ the norm is $t^2-S=t^2$, so $q$ is a unit exactly when $t\neq0$. The claims about the minimal polynomial, the characteristic polynomial, the eigenspace and the Jordan type are the spectral polynomial theorem of *Spectral Regularity and Degeneracy in the Split-Quaternion Algebra*. The scalar case is immediate from $L_t=t\,\mathrm{id}$.

**Corollary (defective units).** A unit on the spectral cone is defective exactly when its vector part is non-zero. The scalar units are semisimple.

*Proof.* The scalar units are the elements $q=t$ with $t\neq0$, and $L_t=t\,\mathrm{id}$ is semisimple. Every other unit on the spectral cone has $\vec v\neq0$ and is defective by the theorem.

The spectral cone therefore contains both units and non-units, and its unit part contains both semisimple and defective elements. The element $1+\vec e_x+\vec e_y$ is a defective unit on $\mathcal C$; the element $\vec e_x+\vec e_y$ is a nilpotent on $\mathcal C$.

## The Chain of Invariants

**Definition (the sectors).** Put $i=1$ when $t^2\neq S$ and $i=0$ when $t^2=S$; put $j=1$ when $S\neq0$ and $j=0$ when $S=0$. The **sector** $\Sigma_{ij}$ is the set of elements with these values. Thus

$$
\Sigma_{11}=\{t^2\neq S,\ S\neq0\},\quad
\Sigma_{10}=\{t^2\neq S,\ S=0\},
$$
$$
\Sigma_{01}=\{t^2=S,\ S\neq0\},\quad
\Sigma_{00}=\{t^2=S,\ S=0\}.
$$

The index $i$ records the norm: $i=1$ on the complement of $\mathcal Z$, $i=0$ on $\mathcal Z$. The index $j$ records the spectrum: $j=1$ on the complement of $\mathcal C$, $j=0$ on $\mathcal C$. The four sectors are studied in *The Four Sectors of the Split-Quaternion Algebra*.

**Theorem (the chain).** The norm, the reduced characteristic polynomial and the minimal polynomial give, respectively, two, four and six degeneration types. The chain is strict.

*Proof.* The norm is either zero or non-zero, giving two types. The reduced characteristic polynomial is $p_q(\lambda)=(\lambda-t)^2-S$; its coefficient $-2t$ determines $t$, and its constant term $t^2-S$ then determines $S$, so it determines the signs of $S$ and of $t^2-S$, that is the sector. The four sectors are non-empty: $2+\vec e_x\in\Sigma_{11}$, $1+\vec e_x+\vec e_y\in\Sigma_{10}$, $1+\vec e_y\in\Sigma_{01}$ and $\vec e_x+\vec e_y\in\Sigma_{00}$; so there are four types. The minimal polynomial refines the sectors as follows.

| stratum | condition | minimal polynomial | characteristic polynomial | Jordan type over $\mathbb C$ |
|---|---|---|---|---|
| $\Sigma_{11}$ | $t^2\neq S,\ S\neq0$ | $(\lambda-t)^2-S$, squarefree | $\big((\lambda-t)^2-S\big)^2$ | $(1,1,1,1)$ |
| $\Sigma_{10}^{\mathrm s}$ | $t\neq0,\ S=0,\ \vec v=0$ | $\lambda-t$ | $(\lambda-t)^4$ | $(1,1,1,1)$ |
| $\Sigma_{10}^{\mathrm{def}}$ | $t\neq0,\ S=0,\ \vec v\neq0$ | $(\lambda-t)^2$ | $(\lambda-t)^4$ | $(2,2)$ |
| $\Sigma_{01}$ | $t^2=S\neq0$ | $\lambda(\lambda-2t)$ | $\lambda^2(\lambda-2t)^2$ | $(1,1,1,1)$ |
| $\Sigma_{00}^{0}$ | $t=0,\ S=0,\ \vec v=0$ | $\lambda$ | $\lambda^4$ | $(1,1,1,1)$ |
| $\Sigma_{00}^{\mathrm{nil}}$ | $t=0,\ S=0,\ \vec v\neq0$ | $\lambda^2$ | $\lambda^4$ | $(2,2)$ |

The rows are distinct, so the minimal polynomial separates six strata. The count is of types. The chain is strict: $2<4<6$.

**Corollary (what each invariant forgets).** The norm separates units from zero divisors but not the four sectors; the characteristic polynomial separates the four sectors but not the defect; the minimal polynomial separates all six strata. The norm cuts across the chain, with zero set $\Sigma_{01}\cup\Sigma_{00}$ and non-zero set $\Sigma_{11}\cup\Sigma_{10}$.

*Proof.* This follows from the table.

## Summary

The norm $t^2-S$ and the spectral form $S$ are independent: $1+\vec e_y$ has norm $0$ and $S=1$, $1+\vec e_x+\vec e_y$ has norm $1$ and $S=0$, and their gradients are independent at $1+\vec e_y$. Their zero sets are $\mathcal Z$ and $\mathcal C$; their intersection is the nilpotent cone $\{t=0,S=0\}$, not the origin. The cones are distinct, neither contains the other, and they are tangent along the non-zero nilpotents.

On $\mathcal Z$ with $t\neq0$, the element is semisimple and spectrally regular, with eigenvalues $0$ and $2t$ and $q=2t e$, where $e=q/(2t)$ is an idempotent. On $\mathcal C$, an element is a unit exactly when $t\neq0$; a unit is defective exactly when $\vec v\neq0$, and the scalar units are semisimple.

The norm, the characteristic polynomial and the minimal polynomial form a strict chain of two, four and six types: the norm separates units from zero divisors, the characteristic polynomial separates the four sectors, and the minimal polynomial separates the six strata.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb H_{\mathrm s}$ | the split-quaternion algebra |
| $q=t+\vec v$ | a general element |
| $S=\vec v^2=-q_x^2+q_y^2+q_z^2$ | the square of the vector part |
| $q\bar q=t^2-S$ | the split-quaternion norm |
| $\mathcal Z=\{t^2=S\}$ | the zero-divisor cone |
| $\mathcal C=\{S=0\}$ | the spectral cone |
| $N_V=\{q_x^2=q_y^2+q_z^2\}$ | the vector null cone, equal to $\mathcal Z\cap\mathcal C$ |
| $p_q(\lambda)=(\lambda-t)^2-S$ | the reduced characteristic polynomial |
| $m_q$ | the minimal polynomial of $L_q$ |
| $\Sigma_{ij}$ | the sector with norm index $i$ and spectral index $j$ |
| $\Sigma_{10}^{\mathrm s}$ | the scalar part of $\Sigma_{10}$ |
| $\Sigma_{10}^{\mathrm{def}}$ | the defective part of $\Sigma_{10}$ |

## Further Reading

- [Spectral Regularity and Degeneracy in the Split-Quaternion Algebra](spectral-regularity-and-degeneracy-in-the-split-quaternion-algebra.html), for the spectral polynomials, the spectral cone and the defective stratum.
- [The Four Sectors of the Split-Quaternion Algebra](the-four-sectors-of-the-split-quaternion-algebra.html), for the definitions, the non-emptiness and the dimensions of the sectors.
- [Split-Quaternion Norm and Invertibility](split-quaternion-norm-and-invertibility.html), for the norm, its isotropy and the zero divisors.
- [Split-Quaternion Zero Divisors](split-quaternion-zero-divisors.html), for the zero-divisor cone, the minimal ideals and the nilpotents.
- [The Spectrum](the-spectrum.html), for the complex analogue, where the two cones are both complex.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (2nd edition, Cambridge University Press, 2013), for the characteristic and minimal polynomials.
