# __The Semisimple–Nilpotent Split__

## Introduction

Every element of the biquaternion algebra is the sum of a semisimple element and a nilpotent element that commute, and the sum is unique. The split is the finest decomposition that the product alone determines: it uses no norm, no form, no pairing and no matrix. This article proves the split for $\mathbb{B}$, states it in the frame supplied by *The Centraliser* and *The Peirce Decomposition*, and shows that the eigenvalue decomposition and the Jordan basis are its two frames.

The algebra has degree two, so the theorem is short. An element $\tilde Q=Q_te_t+\vec Q$ has characteristic polynomial $(X-Q_t)^2+B^2$, with $B^2=Q_x^2+Q_y^2+Q_z^2$. Either $B^2\neq0$, the two roots are distinct, and the element is already semisimple; or $B^2=0$, the roots coalesce, and the element is a scalar plus a square-zero vector. There are therefore four minimal-polynomial types, and the semisimple outcome of the split has three Peirce sub-cases: scalar, unit and zero divisor.

The article is the biquaternion case of *Nilpotent Elements and the Jordan–Chevalley Decomposition*, where the general theorem, its uniqueness and its multiplicative form are proved. What is added here is the explicit frame, the corner pattern and the exact list of types. The two frame articles are *The Eigenbasis* and *The Jordan Normal Form*; the Peirce decomposition is *The Peirce Decomposition*, and the centraliser is *The Centraliser*.

**Notation.** An element is $\tilde Q=Q_te_t+\vec Q$, with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, and its natural conjugation is $\tilde Q^{\natural}=Q_te_t-\vec Q$. The product is the plain product, associative with unit $e_t$. The scalar part is $\operatorname{Sc}(\tilde Q)=Q_t$, and

$$
B^2=Q_x^2+Q_y^2+Q_z^2,\qquad \vec Q^2=-B^2e_t .
$$

The characteristic polynomial is

$$
p_{\tilde Q}(X)=(X-Q_t)^2+B^2,
$$

and the minimal polynomial is written $m_{\tilde Q}$. An element is **semisimple** when $m_{\tilde Q}$ is squarefree, and **nilpotent** when some power of it is zero. An element is a **zero divisor** when $\tilde Q\neq0$ and some non-zero $\tilde R$ satisfies $\tilde Q\tilde R=0$ or $\tilde R\tilde Q=0$. All three notions are properties of the product alone. The algebra and its conventions are *The Biquaternion Algebra*; the polynomial and its two cases are *The Spectrum*.

## The Frame

The split is read in the Peirce frame of *The Peirce Decomposition*, and its uniqueness is read in the centraliser of *The Centraliser*. The two facts are these.

- The centraliser of a non-central element is $\mathbb{C}[\tilde Q]$, of complex dimension two: it is $\mathbb{C}\times\mathbb{C}$ off the cone $B^2=0$ and the dual numbers on it. At the centre it is all of $\mathbb{B}$.
- A complete orthogonal pair $\{\tilde\Pi,\tilde\Pi'\}$ cuts the algebra into four corners $\mathbb{B}_{\sigma\tau}$, each a complex line, with the corner rule $\mathbb{B}_{\sigma\tau}\mathbb{B}_{\mu\nu}\subseteq\delta_{\tau\mu}\mathbb{B}_{\sigma\nu}$.

In a frame adapted to the element, $S$ is diagonal and $N$ lies in a single mixed corner. The mixed corner is square-zero, so $N^2=0$ and the nilpotent index is at most two. The spectral frame, which exists when $B^2\neq0$, and the defective frame, which exists when $B^2=0$, are the two realisations of the same adapted frame; the discriminant chooses between them.

## The Decomposition

**Theorem (Jordan–Chevalley).** Every $\tilde Q\in\mathbb{B}$ has a unique decomposition

$$
\tilde Q=S+N,\qquad SN=NS,
$$

with $S$ semisimple and $N$ nilpotent. Moreover $S,N\in\mathbb{C}[\tilde Q]$.

**Proof (existence).** Two cases.

If $B^2\neq0$, the roots $Q_t\pm iB$ are distinct, so $p_{\tilde Q}$ is squarefree. The minimal polynomial divides $p_{\tilde Q}$ and has the same roots, so $m_{\tilde Q}=p_{\tilde Q}$ is squarefree and $\tilde Q$ is semisimple. Take $S=\tilde Q$ and $N=0$.

If $B^2=0$, then $\vec Q^2=-B^2e_t=0$, and $\tilde Q=Q_te_t+\vec Q$. Take

$$
S=Q_te_t,\qquad N=\vec Q .
$$

Then $N^2=0$, so $N$ is nilpotent; $S$ is scalar, hence semisimple and central; and $SN=NS$.

**Proof (uniqueness).** The two parts commute with $\tilde Q$, so they lie in the centraliser $C(\tilde Q)$ computed in *The Centraliser*.

If $B^2\neq0$, the element has two distinct eigenvalues, and its centraliser is $\mathbb{C}[\tilde Q]\cong\mathbb{C}\times\mathbb{C}$. Every element of a product of fields is semisimple, so the only nilpotent element of the centraliser is $0$. Hence $N=0$ and $S=\tilde Q$.

If $B^2=0$ and $\vec Q\neq0$, then $m_{\tilde Q}=X^2$ after the translation by $Q_t$, and the centraliser is $\mathbb{C}[\tilde Q]=\mathbb{C}[\vec Q]=\{ae_t+b\vec Q\}$, the dual numbers. In the dual numbers the semisimple elements are exactly the scalars: for $b\neq0$,

$$
(ae_t+b\vec Q-ae_t)^2=b^2\vec Q^2=0,
$$

so the minimal polynomial of $ae_t+b\vec Q$ is $(X-a)^2$, not squarefree. Hence $S=ae_t$; comparing with $\tilde Q=Q_te_t+\vec Q$ gives $a=Q_t$ and $N=\vec Q$.

If $\tilde Q=Q_te_t$ is scalar, write $S=\tilde Q-N$. If $N\neq0$ with $N^k=0$ and $N^{k-1}\neq0$, then $(S-Q_te_t)^k=0$ and $(S-Q_te_t)^{k-1}\neq0$, so $m_S=(X-Q_t)^k$ is not squarefree and $S$ is not semisimple. Hence $N=0$ and $S=\tilde Q$.

**Corollary (polynomial form).** $S$ and $N$ are polynomials in $\tilde Q$. In the semisimple case $S=\tilde Q$ and $N=0$; in the defective case $S=Q_te_t$ and $N=\tilde Q-Q_te_t$.

**Remark (why the scalar part is never nilpotent).** The scalar part is central. A central element $ce_t$ is semisimple when $c\neq0$ and is zero when $c=0$. So the scalar part belongs to $S$ in every case, and the nilpotent part always lies in the vector subspace. This is why the defective split is the scalar part plus the vector part, with no further correction.

## The Four Types

**The minimal polynomial, not the characteristic polynomial, separates the types: two of them share $(X-Q_t)^2$.**

| type | condition | $S$ | $N$ | frame | $m_{\tilde Q}$ |
|---|---|---|---|---|---|
| scalar | $\vec Q=0$ | $\tilde Q$ | $0$ | $\{e_t\}$ | $X-Q_t$ |
| semisimple, non-scalar | $B^2\neq0$ | $\tilde Q$ | $0$ | spectral $\{\tilde\Pi_+,\tilde\Pi_-\}$ | $(X-Q_t)^2+B^2$ |
| Jordan | $B^2=0$, $Q_t\neq0$, $\vec Q\neq0$ | $Q_te_t$ | $\vec Q$ | defective $\{e,e'\}$ | $(X-Q_t)^2$ |
| nilpotent | $B^2=0$, $Q_t=0$, $\vec Q\neq0$ | $0$ | $\tilde Q$ | defective $\{e,e'\}$ | $X^2$ |

The scalar row is semisimple as well. It is listed separately because its minimal polynomial has degree one, while the other semisimple row has degree two; the split $S+N$ does not distinguish the two, and the frame does.

The table separates the scalar case from the Jordan case by the minimal polynomial alone: both have $p_{\tilde Q}=(X-Q_t)^2$, and only the scalar case has $m_{\tilde Q}=X-Q_t$. It separates the Jordan case from the nilpotent case by the scalar part alone: both have $m_{\tilde Q}=X^2$ after translation, and only the Jordan case has $Q_t\neq0$. No single invariant of the table does both jobs.

The non-scalar semisimple type has two Peirce sub-cases, which the decomposition does not distinguish.

| sub-case | condition | decomposition | Peirce occupancy |
|---|---|---|---|
| semisimple, unit | $B^2\neq0$, $Q_t^2+B^2\neq0$ | $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$, both $\lambda_\pm\neq0$ | two diagonal corners |
| semisimple, zero divisor | $B^2\neq0$, $Q_t^2+B^2=0$ | $\tilde Q=\lambda\tilde\Pi$, one $\lambda\neq0$ | one diagonal corner |

The condition of the second row is the vanishing of the constant term of $p_{\tilde Q}$, that is $\tilde Q\tilde Q^{\natural}=0$. One eigenvalue is then zero, the element is a non-zero complex multiple of a non-trivial idempotent, and it is a zero divisor. The first row is a unit: its inverse is $\lambda_+^{-1}\tilde\Pi_++\lambda_-^{-1}\tilde\Pi_-$. Both rows have $S=\tilde Q$ and $N=0$, so the Jordan–Chevalley decomposition does not see the difference; the Peirce decomposition does.

**Remark (the two words).** *Semisimple* is a property of the minimal polynomial, and it includes the scalar line; *regular* in the spectral articles means $B^2\neq0$, which is the same condition as semisimple for a non-scalar element, while the scalar line is semisimple and spectrally degenerate at once. *Unit* and *zero divisor* are properties of the product, and the second table is their restriction to the non-scalar semisimple type.

## The Peirce Form

**In a frame adapted to the element, the semisimple part is diagonal and the nilpotent part lies in a single mixed corner.**

**Definition (adapted frame).** A **frame** is a complete idempotent pair $\{e,e'\}$ or the trivial frame $\{e_t\}$. A frame is **adapted** to $\tilde Q$ if it is the spectral frame when $B^2\neq0$, any defective frame when $B^2=0$ and $\vec Q\neq0$, and $\{e_t\}$ when $\vec Q=0$.

**Proposition (the corner pattern).** Let the frame be adapted to $\tilde Q$. In the scalar case it is $\{e_t\}$, and the statement reads $S=\tilde Q$ and $N=0$. Otherwise it is a pair $\{e,e'\}$, and

$$
S=eSe+e'Se',\qquad N=eNe',
$$

with the second identity reading $N=0$ in the semisimple case. In the Peirce basis and the corner order $(++,+-,-+,--)$, the coordinates of $\tilde Q$ are non-zero only in the two diagonal corners and in the corner $+-$. The diagonal coordinates are those of $S$, and the coordinate of $+-$ is that of $N$.

*Proof.* In the semisimple case $N=0$ and $S=\lambda_+e+\lambda_-e'$, which is diagonal. In the defective case $S=Q_te_t=Q_te+Q_te'$, which is diagonal, and $N=\vec Q$ lies in $e\mathbb{B}e'$ by the choice of the defective frame. In the scalar case $S=Q_te_t$ and $N=0$.

**Corollary (index at most two).** In the defective case $N^2=0$, because the mixed corner is square-zero:

$$
(e\mathbb{B}e')(e\mathbb{B}e')=e\mathbb{B}(e'e)\mathbb{B}e'=0 .
$$

So the nilpotent part has index two, never higher: the element has a single Jordan block of size two, and the left and right actions on $\mathbb{B}$ have two copies of it. This is the degree of the algebra read on the corners.

**Remark (the frame is not unique).** In the defective case any frame with $\vec Q\in e\mathbb{B}e'$ gives the same corner pattern. The element's coordinates in the corner change with the frame, but its Jordan type does not: the pattern is a normal form, and the frame is the coordinate system. The canonical frame of the Jordan basis article is one choice, selected by extra data; the theorem needs none.

**Remark (the two readings).** The diagonal corners carry the semisimple part and the mixed corner carries the nilpotent part. This is the precise sense in which the Jordan–Chevalley decomposition is a Peirce decomposition at the frame of the element: the spectral idempotents are Peirce idempotents, and the nilpotent part is the component in the mixed corner. The general Peirce decomposition needs an arbitrary idempotent; the Jordan–Chevalley decomposition needs the idempotents of the element, and in $\mathbb{B}$ those are the spectral ones in the semisimple case and the support ones in the defective case.

## The Multiplicative Form

**For a unit, the additive split has a multiplicative form: a product of a semisimple element and a unipotent one. For a semisimple zero divisor the only product is trivial, and for a nilpotent element there is none.**

**Corollary (multiplicative form).** Let $\tilde Q$ be a unit. Then

$$
\tilde Q=SU,\qquad U=e_t+S^{-1}N,\qquad U^{-1}=e_t-S^{-1}N,
$$

with $S$ semisimple, $U$ unipotent, and $SU=US$.

*Proof.* The element $S$ is a unit in both cases: in the semisimple case $S=\tilde Q$; in the defective case $S=Q_te_t$ with $Q_t\neq0$, because $\tilde Q$ is a unit, $\tilde Q^{\natural}$ is a unit, and $\tilde Q\tilde Q^{\natural}=Q_t^2e_t$ is therefore non-zero. Then $S^{-1}N$ is defined, it commutes with $S$, and $(S^{-1}N)^2=S^{-2}N^2=0$. Hence $U=e_t+S^{-1}N$ is unipotent, $U^{-1}=e_t-S^{-1}N$, and $SU=S+N=\tilde Q$.

**Remark (the obstruction).** The hypothesis is not removable. A semisimple zero divisor has $S=\tilde Q$ not a unit, so $S^{-1}$ does not exist. Both factors of a product commute with $\tilde Q$, hence lie in the centraliser $\mathbb{C}\times\mathbb{C}$, which has no non-zero nilpotent; so $U=e_t$ and the only product is the trivial $\tilde Q=\tilde Q\,e_t$. A nilpotent element has no product at all: a semisimple element of its centraliser is a scalar $ae_t$, and $ae_t(e_t+b\tilde Q)=ae_t+ab\tilde Q$ has scalar part $a$, which must vanish, leaving $0$. The multiplicative form is therefore a theorem about the unit group, not about the algebra: it is the biquaternion case of the multiplicative Jordan decomposition, and its natural domain is $\mathbb{B}^{\times}$.

**Remark (no form is used).** The proof uses only the inverse of $S$, not a norm. The criterion that $\tilde Q$ is a unit is the existence of a two-sided inverse; the identity $\tilde Q\tilde Q^{\natural}=Q_t^2e_t$ in the defective case is the product computation

$$
(Q_te_t+\vec Q)(Q_te_t-\vec Q)=Q_t^2e_t-\vec Q^2=Q_t^2e_t,
$$

which uses $\vec Q^2=0$. No pairing of two different elements occurs.

## The Two Bases

**The eigenvalue decomposition and the Jordan basis are the two frames of the same theorem, and the discriminant chooses between them.**

| condition | eigenbasis | Jordan basis | Jordan–Chevalley frame |
|---|---|---|---|
| $B^2\neq0$ | exists | not needed | spectral |
| $B^2=0$, $\vec Q\neq0$ | does not exist | exists | defective |
| $\vec Q=0$ | every basis | every basis | trivial |

For $B^2\neq0$ the spectral frame gives

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,\qquad
\lambda_\pm=Q_t\pm iB,\qquad
\tilde\Pi_\pm=\frac{e_t\pm\vec\Xi}{2},\qquad
\vec\Xi=-\frac{i\vec Q}{B},
$$

and the eigenbasis is $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ with the two mixed generators of the corners. The element is diagonal in that basis, and its diagonal values are $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$ for the left action.

For $B^2=0$ and $\vec Q\neq0$ the defective frame gives

$$
\tilde Q=Q_te_t+\vec Q,\qquad \vec Q\in e\mathbb{B}e',\qquad \vec Q^2=0,
$$

and the Jordan basis is the four vectors of the corners, in which the left action is a pair of Jordan blocks of size two. The element has no eigenbasis: its eigenspace is the two-dimensional $\ker L_{\tilde Q}=\vec Q\mathbb{B}$, which is not the whole algebra, and the minimal polynomial has a double root.

The comparison is exact. In the semisimple case the Peirce decomposition at the spectral idempotents is the eigenvalue decomposition; in the defective case the Peirce decomposition at the support idempotents is the Jordan basis; and in both cases the diagonal corners carry $S$ and the mixed corner carries $N$. The Jordan–Chevalley theorem is the statement that these are the only two possibilities, and the discriminant is the switch.

**Remark (which article owns what).** The construction of the spectral frame, the branch and the expansion of every biquaternion are in *The Eigenbasis*. The construction of the canonical defective frame, the Jordan pair and the Jordan basis are in *The Jordan Normal Form*. This article owns the split, the types and the corner pattern, and cites the two constructions rather than repeating them.

## Worked Examples

**Five elements, one per type, with the decomposition computed from the formulas.**

### A Semisimple Unit

Take $\tilde Q=2e_t+\vec e_x$. Then $B^2=1$, $B=1$, and

$$
\lambda_\pm=2\pm i,\qquad
\tilde\Pi_\pm=\frac{e_t\mp i\vec e_x}{2},\qquad
\tilde Q=(2+i)\tilde\Pi_++(2-i)\tilde\Pi_- .
$$

The element is semisimple, $S=\tilde Q$ and $N=0$. It is a unit, with inverse $(2+i)^{-1}\tilde\Pi_++(2-i)^{-1}\tilde\Pi_-$, and its multiplicative form is $\tilde Q=\tilde Q\,e_t$.

### A Semisimple Zero Divisor

Take $\tilde Q=e_t+i\vec e_x$. Then $B^2=-1$, $B=i$, and

$$
\lambda_+=0,\qquad \lambda_-=2,\qquad
\tilde\Pi_+=\frac{e_t-i\vec e_x}{2},\qquad
\tilde\Pi_-=\frac{e_t+i\vec e_x}{2},\qquad
\tilde Q=2\tilde\Pi_- .
$$

The element is semisimple, $S=\tilde Q$ and $N=0$. It is a zero divisor: $\tilde Q\tilde\Pi_+=0$ and $\tilde\Pi_+\tilde Q=0$. The spectral frame exists and has two idempotents, but only one diagonal corner is occupied, because the eigenvalue of $\tilde\Pi_+$ is zero. The only product with a semisimple factor and a unipotent factor is the trivial $\tilde Q=\tilde Q\,e_t$.

### A Jordan Element

Take $\tilde Q=2e_t+\vec e_x+i\vec e_y$. Then

$$
B^2=1+i^2=0,\qquad
Q_t=2,\qquad
\vec Q=\vec e_x+i\vec e_y,\qquad
\vec Q^2=\vec e_x^2+i(\vec e_x\vec e_y+\vec e_y\vec e_x)+i^2\vec e_y^2=-e_t+e_t=0 .
$$

Hence $S=2e_t$, $N=\vec Q$, and $N^2=0$. The element is a unit, and the multiplicative form is

$$
\tilde Q=2\left(e_t+\frac{\vec e_x+i\vec e_y}{2}\right)=SU,\qquad
U=e_t+\frac{\vec e_x+i\vec e_y}{2},\qquad
U^{-1}=e_t-\frac{\vec e_x+i\vec e_y}{2}.
$$

In the standard frame $\tilde\Pi_\pm=(e_t\pm i\vec e_z)/2$, with generators $\vec\Upsilon_x=(i\vec e_x-\vec e_y)/2$ and $\vec\Upsilon_y=(i\vec e_x+\vec e_y)/2$, the element reads

$$
\tilde Q=2(\tilde\Pi_++\tilde\Pi_-)-2i\vec\Upsilon_x,
$$

so the semisimple part occupies the two diagonal corners and the nilpotent part the corner $+-$.

### A Nilpotent Element

Take $\tilde Q=\vec e_x+i\vec e_y$. This is the nilpotent part of the preceding example. Then $B^2=0$, $Q_t=0$, $S=0$ and $N=\tilde Q$. In the same frame $\tilde Q=-2i\vec\Upsilon_x$, a single mixed corner, and $\tilde Q^2=0$. There is no product with a semisimple factor and a unipotent factor: the semisimple factor would have to be a scalar, and the scalar part of the product would be non-zero while $\tilde Q$ has none.

### A Scalar Element

Take $\tilde Q=3e_t$. Then $\vec Q=0$, $p_{\tilde Q}=(X-3)^2$, $m_{\tilde Q}=X-3$, and $S=3e_t$, $N=0$. The frame is $\{e_t\}$, every basis is an eigenbasis, and every idempotent commutes with the element. The scalar case is the only one in which the characteristic polynomial is not squarefree while the element is semisimple.

**Remark (the two coincidences).** The characteristic polynomial is $(X-Q_t)^2$ both for a scalar element and for a Jordan element, and it is $X^2$ both for the nilpotent element and for the origin. In each pair the minimal polynomial separates the two, and the scalar part separates the Jordan element from the nilpotent one. The examples show that neither invariant alone classifies the element.

## Summary

Every biquaternion splits uniquely as $\tilde Q=S+N$ with $S$ semisimple, $N$ nilpotent and $SN=NS$. The proof is a two-case argument on the discriminant of the characteristic polynomial $(X-Q_t)^2+B^2$: distinct roots give a semisimple element, a double root gives a scalar plus a square-zero vector. Uniqueness follows from the centraliser, which is $\mathbb{C}\times\mathbb{C}$ in the non-scalar semisimple case, the dual numbers in the defective case, and all of $\mathbb{B}$ at the scalar; in each, the only semisimple elements are the ones named by the theorem.

There are four minimal-polynomial types. The scalar type has $m_{\tilde Q}=X-Q_t$; the non-scalar semisimple type has $B^2\neq0$ and $m_{\tilde Q}=p_{\tilde Q}$; the Jordan type has $B^2=0$, $Q_t\neq0$ and $m_{\tilde Q}=(X-Q_t)^2$; the nilpotent type has $B^2=0$, $Q_t=0$ and $m_{\tilde Q}=X^2$. The semisimple outcome of the split has three Peirce sub-cases: the scalar, where the frame is trivial; the unit; and the zero divisor. The last two have the same Jordan–Chevalley data and differ in the occupancy of the diagonal corners.

In a frame adapted to the element, $S$ is diagonal and $N$ lies in a single mixed corner. The mixed corner is square-zero, so $N^2=0$ and the nilpotent index is at most two. This is the corner form of the theorem: the diagonal carries the semisimple part, the mixed corner carries the nilpotent part, and the Peirce idempotents are the idempotents of the element. The spectral frame gives the eigenvalue decomposition; the defective frame gives the Jordan basis; the discriminant chooses between them.

For a unit, the additive split gives the multiplicative form $\tilde Q=SU$ with $U=e_t+S^{-1}N$ unipotent and $U^{-1}=e_t-S^{-1}N$. For a semisimple zero divisor the multiplicative form collapses to the trivial product, because $S$ is not a unit and the centraliser has no non-zero nilpotent; a nilpotent element has no product at all. The whole article uses the product, the scalar part and the characteristic polynomial. No form, no norm, no pairing and no matrix is used. The canonical defective frame of the Jordan basis article is built from the element and the corner condition; this article replaces it by an arbitrary adapted frame, so that the theorem and its corner reading stay algebraic.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | a general element |
| $\tilde Q^{\natural}=Q_te_t-\vec Q$ | the natural conjugation |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part, the discriminant up to $-4$ |
| $p_{\tilde Q}(X)=(X-Q_t)^2+B^2$ | the characteristic polynomial |
| $m_{\tilde Q}$ | the minimal polynomial |
| $S,N$ | the semisimple and nilpotent parts of $\tilde Q$ |
| $\tilde\Pi_\pm=(e_t\pm\vec\Xi)/2$, $\vec\Xi=-i\vec Q/B$ | the spectral idempotents, for $B^2\neq0$ |
| $e,e'$ | a defective frame, with $\vec Q\in e\mathbb{B}e'$ |
| $\mathbb{B}_{\sigma\tau}=\tilde\Pi_\sigma\mathbb{B}\tilde\Pi_\tau$ | a Peirce corner |
| $\vec\Upsilon_x,\vec\Upsilon_y$ | the mixed generators of the standard frame |
| $U=e_t+S^{-1}N$ | the unipotent factor of a unit |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues, for $B^2\neq0$ |

## Further Reading

- [The Spectrum](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the characteristic polynomial, the spectral criterion and the two cases.
- [The Eigenbasis](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), for the spectral frame, the root and the eigenbasis.
- [The Jordan Normal Form](the-spectrally-degenerate-sector-and-construction-of-the-jordan-basis-of-a-biquaternion.html), for the defective sector, the support idempotents and the Jordan basis.
- [The Peirce Decomposition](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the Peirce decomposition, the corners and the mixed generators.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the units, the zero divisors and their two strata.
- [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), for the general theorem, its uniqueness and the multiplicative form.
- [The Eigenvalue Decomposition in a Jordan Algebra](the-eigenvalue-decomposition-in-a-jordan-algebra.html), for the spectral idempotents read as Peirce idempotents.
- [Modules over $k[x]$ and the Jordan Form](modules-over-kx-and-the-jordan-form.html), for the Jordan block behind the defective case.
- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), for the Clifford reading of the spectral case.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (2nd edition, Cambridge University Press, 2013), for the general Jordan–Chevalley theorem and the Jordan form.
