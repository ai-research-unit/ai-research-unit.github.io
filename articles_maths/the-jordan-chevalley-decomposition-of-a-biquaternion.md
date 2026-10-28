# __The Semisimple–Nilpotent Split__

## Introduction

Every element of the biquaternion algebra is the sum of a semisimple element and a nilpotent element that commute, and the sum is unique. The split is the finest decomposition that the product alone determines: it uses no norm, no form, no pairing and no matrix. This article proves the split for $\mathbb{B}$, states it in the frame supplied by *The Centraliser* and *The Peirce Decomposition of the Biquaternion Algebra*, and shows that the eigenvalue decomposition and the Jordan basis are its two frames.

The algebra has degree two, so the theorem is short. An element $\tilde Q=Q_te_t+\vec Q$ has characteristic polynomial $(X-Q_t)^2+B^2$, with $B^2=Q_x^2+Q_y^2+Q_z^2$. The cases are read in two steps, first by the discriminant and then by centrality. First $B^2\neq0$: the two roots are distinct and the element is already semisimple. Then $B^2=0$, where the roots coalesce. This second case has two halves: the central half $\vec Q=0$, where the element is scalar; and the non-central half $\vec Q\neq0$, where the element is a scalar part plus a non-zero square-zero vector. The non-central half splits once more by the scalar part, into the Jordan type when $Q_t\neq0$ and the nilpotent type when $Q_t=0$. There are therefore four minimal-polynomial types, and the semisimple outcome of the split has three Peirce sub-cases: scalar, unit and zero divisor.

The article is the biquaternion case of *Nilpotent Elements and the Jordan–Chevalley Decomposition*, where the general theorem, its uniqueness and its multiplicative form are proved. What is added here is the explicit frame, the corner pattern and the exact list of types. The two frame articles are *The Eigenbasis of a Spectrally Regular Biquaternion* and *The Jordan Basis of a Spectrally Degenerate Biquaternion*; the Peirce decomposition is *The Peirce Decomposition of the Biquaternion Algebra*, and the centraliser is *The Centraliser*.

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

The split is read in the Peirce frame of *The Peirce Decomposition of the Biquaternion Algebra*, and its uniqueness is read in the centraliser of *The Centraliser*. The two facts are these.

- A non-central element has $C(\tilde Q)=\mathbb{C}[\tilde Q]$, of complex dimension two: $\mathbb{C}\times\mathbb{C}$ when $B^2\neq0$, the dual numbers when $B^2=0$ and $\vec Q\neq0$. At the centre, $B^2=0$ with $\vec Q=0$, the centraliser is all of $\mathbb{B}$.
- A complete orthogonal pair $\{\tilde\Pi,\tilde\Pi'\}$ cuts the algebra into four corners $\mathbb{B}_{\sigma\tau}$, each a complex line, with the corner rule $\mathbb{B}_{\sigma\tau}\mathbb{B}_{\mu\nu}\subseteq\delta_{\tau\mu}\mathbb{B}_{\sigma\nu}$.

In a frame adapted to the element, $\tilde Q_s$ is diagonal and $\vec\Upsilon$ lies in a single mixed corner. The mixed corner is square-zero, so $\vec\Upsilon^2=0$ and the nilpotent index is at most two. The spectral frame, which exists when $B^2\neq0$, and the defective frame, which exists when $B^2=0$ with $\vec Q\neq0$, are the two non-trivial realisations of the same adapted frame; when $B^2=0$ and $\vec Q=0$ the adapted frame is the trivial frame $\{e_t\}$, and the discriminant chooses among the three.

## The Decomposition

**Theorem (Jordan–Chevalley).** Every $\tilde Q\in\mathbb{B}$ has a unique decomposition

$$
\tilde Q=\tilde Q_s+\vec\Upsilon,\qquad \tilde Q_s\vec\Upsilon=\vec\Upsilon\tilde Q_s,
$$

with $\tilde Q_s$ semisimple and $\vec\Upsilon$ nilpotent. Moreover $\tilde Q_s,\vec\Upsilon\in\mathbb{C}[\tilde Q]$.

**Proof (existence).** Three cases.

If $B^2\neq0$, the roots $Q_t\pm iB$ are distinct, so $p_{\tilde Q}$ is squarefree. The minimal polynomial divides $p_{\tilde Q}$ and has the same roots, so $m_{\tilde Q}=p_{\tilde Q}$ is squarefree and $\tilde Q$ is semisimple. Take $\tilde Q_s=\tilde Q$ and $\vec\Upsilon=0$.

If $B^2=0$ and $\vec Q=0$, the element is scalar, $\tilde Q=Q_te_t$. Take $\tilde Q_s=\tilde Q$ and $\vec\Upsilon=0$.

If $B^2=0$ and $\vec Q\neq0$, then $\vec Q^2=-B^2e_t=0$, and $\tilde Q=Q_te_t+\vec Q$. Take

$$
\tilde Q_s=Q_te_t,\qquad \vec\Upsilon=\vec Q .
$$

Then $\vec\Upsilon^2=0$, so $\vec\Upsilon$ is nilpotent; $\tilde Q_s$ is scalar, hence semisimple and central; and $\tilde Q_s\vec\Upsilon=\vec\Upsilon\tilde Q_s$.

**Proof (uniqueness).** The two parts commute with $\tilde Q$, so they lie in the centraliser $C(\tilde Q)$ computed in *The Centraliser*.

If $B^2\neq0$, the element has two distinct eigenvalues, and its centraliser is $\mathbb{C}[\tilde Q]\cong\mathbb{C}\times\mathbb{C}$. Every element of a product of fields is semisimple, so the only nilpotent element of the centraliser is $0$. Hence $\vec\Upsilon=0$ and $\tilde Q_s=\tilde Q$.

If $\tilde Q=Q_te_t$ is scalar, write $\tilde Q_s=\tilde Q-\vec\Upsilon$. If $\vec\Upsilon\neq0$ with $\vec\Upsilon^k=0$ and $\vec\Upsilon^{k-1}\neq0$, then $(\tilde Q_s-Q_te_t)^k=0$ and $(\tilde Q_s-Q_te_t)^{k-1}\neq0$, so $m_{\tilde Q_s}=(X-Q_t)^k$ is not squarefree and $\tilde Q_s$ is not semisimple. Hence $\vec\Upsilon=0$ and $\tilde Q_s=\tilde Q$.

If $B^2=0$ and $\vec Q\neq0$, then $m_{\tilde Q}=X^2$ after the translation by $Q_t$, and the centraliser is $\mathbb{C}[\tilde Q]=\mathbb{C}[\vec Q]=\{ae_t+b\vec Q\}$, the dual numbers. In the dual numbers the semisimple elements are exactly the scalars: for $b\neq0$,

$$
(ae_t+b\vec Q-ae_t)^2=b^2\vec Q^2=0,
$$

so the minimal polynomial of $ae_t+b\vec Q$ is $(X-a)^2$, not squarefree. Hence $\tilde Q_s=ae_t$; comparing with $\tilde Q=Q_te_t+\vec Q$ gives $a=Q_t$ and $\vec\Upsilon=\vec Q$.

**Corollary (polynomial form).** $\tilde Q_s$ and $\vec\Upsilon$ are polynomials in $\tilde Q$. In the semisimple case $\tilde Q_s=\tilde Q$ and $\vec\Upsilon=0$; in the defective case $\tilde Q_s=Q_te_t$ and $\vec\Upsilon=\tilde Q-Q_te_t$.

**Remark (why the scalar part is never nilpotent).** The scalar part is central. A central element $ce_t$ is semisimple when $c\neq0$ and is zero when $c=0$. So the scalar part belongs to $\tilde Q_s$ in every case, and the nilpotent part always lies in the vector subspace. This is why the defective split is the scalar part plus the vector part, with no further correction.

## The Four Types

**The minimal polynomial, not the characteristic polynomial, separates the types: two of them share $(X-Q_t)^2$.**

| type | condition | $\tilde Q_s$ | $\vec\Upsilon$ | frame | $m_{\tilde Q}$ |
|---|---|---|---|---|---|
| semisimple, non-scalar | $B^2\neq0$ | $\tilde Q$ | $0$ | spectral $\{\tilde\Pi_+,\tilde\Pi_-\}$ | $(X-Q_t)^2+B^2$ |
| scalar | $B^2=0$, $\vec Q=0$ | $\tilde Q$ | $0$ | $\{e_t\}$ | $X-Q_t$ |
| Jordan | $B^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | $Q_te_t$ | $\vec Q$ | defective $\{e,e'\}$ | $(X-Q_t)^2$ |
| nilpotent | $B^2=0$, $\vec Q\neq0$, $Q_t=0$ | $0$ | $\tilde Q$ | defective $\{e,e'\}$ | $X^2$ |

The first row is the spectrally regular case, $B^2\neq0$. The second row is the central part of the spectral-degenerate cone, $\vec Q=0$: it is semisimple too, but its semisimplicity comes from the degree-one minimal polynomial, not from distinct roots. The last two rows form the non-central part of the cone, $B^2=0$ with $\vec Q\neq0$, split by the scalar part.

The table separates the scalar row from the Jordan row by the minimal polynomial alone: both have $p_{\tilde Q}=(X-Q_t)^2$, and only the scalar row has $m_{\tilde Q}=X-Q_t$. It separates the Jordan row from the nilpotent row by the scalar part alone: both have $m_{\tilde Q}=X^2$ after translation, and only the Jordan row has $Q_t\neq0$. No single invariant of the table does both jobs.

The non-scalar semisimple type has two Peirce sub-cases, which the decomposition does not distinguish.

| sub-case | condition | decomposition | Peirce occupancy |
|---|---|---|---|
| semisimple, unit | $B^2\neq0$, $Q_t^2+B^2\neq0$ | $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$, both $\lambda_\pm\neq0$ | two diagonal corners |
| semisimple, zero divisor | $B^2\neq0$, $Q_t^2+B^2=0$ | $\tilde Q=\lambda\tilde\Pi$, one $\lambda\neq0$ | one diagonal corner |

The condition of the second row is the vanishing of the constant term of $p_{\tilde Q}$, that is $\tilde Q\tilde Q^{\natural}=0$. One eigenvalue is then zero, the element is a non-zero complex multiple of a non-trivial idempotent, and it is a zero divisor. The first row is a unit: its inverse is $\lambda_+^{-1}\tilde\Pi_++\lambda_-^{-1}\tilde\Pi_-$. Both rows have $\tilde Q_s=\tilde Q$ and $\vec\Upsilon=0$, so the Jordan–Chevalley decomposition does not see the difference; the Peirce decomposition does.

**Remark (the two words).** *Semisimple* is a property of the minimal polynomial, and it includes the scalar line; *regular* in the spectral articles means $B^2\neq0$, which is the same condition as semisimple for a non-scalar element, while the scalar line is semisimple and spectrally degenerate at once. *Unit* and *zero divisor* are properties of the product, and the second table is their restriction to the non-scalar semisimple type.

## The Peirce Form

**In a frame adapted to the element, the semisimple part is diagonal and the nilpotent part lies in a single mixed corner.**

**Definition (adapted frame).** A **frame** is a complete idempotent pair $\{e,e'\}$ or the trivial frame $\{e_t\}$. A frame is **adapted** to $\tilde Q$ if it is the spectral frame when $B^2\neq0$, the trivial frame $\{e_t\}$ when $\vec Q=0$, and any defective frame when $B^2=0$ with $\vec Q\neq0$.

**Proposition (the corner pattern).** Let the frame be adapted to $\tilde Q$. In the scalar case it is $\{e_t\}$, and the statement reads $\tilde Q_s=\tilde Q$ and $\vec\Upsilon=0$. Otherwise it is a pair $\{e,e'\}$, and

$$
\tilde Q_s=e\tilde Q_se+e'\tilde Q_se',\qquad \vec\Upsilon=e\vec\Upsilon e',
$$

with the second identity reading $\vec\Upsilon=0$ in the semisimple case. In the Peirce basis and the corner order $(++,+-,-+,--)$, the coordinates of $\tilde Q$ are non-zero only in the two diagonal corners and in the corner $+-$. The diagonal coordinates are those of $\tilde Q_s$, and the coordinate of $+-$ is that of $\vec\Upsilon$.

*Proof.* In the semisimple case $\vec\Upsilon=0$ and $\tilde Q_s=\lambda_+e+\lambda_-e'$, which is diagonal. In the defective case $\tilde Q_s=Q_te_t=Q_te+Q_te'$, which is diagonal, and $\vec\Upsilon=\vec Q$ lies in $e\mathbb{B}e'$ by the choice of the defective frame. In the scalar case $\tilde Q_s=Q_te_t$ and $\vec\Upsilon=0$.

**Corollary (index at most two).** In the defective case $\vec\Upsilon^2=0$, because the mixed corner is square-zero:

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
\tilde Q=\tilde Q_s\tilde U,\qquad \tilde U=e_t+\tilde Q_s^{-1}\vec\Upsilon,\qquad \tilde U^{-1}=e_t-\tilde Q_s^{-1}\vec\Upsilon,
$$

with $\tilde Q_s$ semisimple, $\tilde U$ unipotent, and $\tilde Q_s\tilde U=\tilde U\tilde Q_s$.

*Proof.* The element $\tilde Q_s$ is a unit in both cases: in the semisimple case $\tilde Q_s=\tilde Q$; in the defective case $\tilde Q_s=Q_te_t$ with $Q_t\neq0$, because $\tilde Q$ is a unit, $\tilde Q^{\natural}$ is a unit, and $\tilde Q\tilde Q^{\natural}=Q_t^2e_t$ is therefore non-zero. Then $\tilde Q_s^{-1}\vec\Upsilon$ is defined, it commutes with $\tilde Q_s$, and $(\tilde Q_s^{-1}\vec\Upsilon)^2=\tilde Q_s^{-2}\vec\Upsilon^2=0$. Hence $\tilde U=e_t+\tilde Q_s^{-1}\vec\Upsilon$ is unipotent, $\tilde U^{-1}=e_t-\tilde Q_s^{-1}\vec\Upsilon$, and $\tilde Q_s\tilde U=\tilde Q_s+\vec\Upsilon=\tilde Q$.

**Remark (the obstruction).** The hypothesis is not removable. A semisimple zero divisor has $\tilde Q_s=\tilde Q$ not a unit, so $\tilde Q_s^{-1}$ does not exist. Both factors of a product commute with $\tilde Q$, hence lie in the centraliser $\mathbb{C}\times\mathbb{C}$, which has no non-zero nilpotent; so $\tilde U=e_t$ and the only product is the trivial $\tilde Q=\tilde Q\,e_t$. A nilpotent element has no product at all: a semisimple element of its centraliser is a scalar $ae_t$, and $ae_t(e_t+b\tilde Q)=ae_t+ab\tilde Q$ has scalar part $a$, which must vanish, leaving $0$. The multiplicative form is therefore a theorem about the unit group, not about the algebra: it is the biquaternion case of the multiplicative Jordan decomposition, and its natural domain is $\mathbb{B}^{\times}$.

**Remark (no form is used).** The proof uses only the inverse of $\tilde Q_s$, not a norm. The criterion that $\tilde Q$ is a unit is the existence of a two-sided inverse; the identity $\tilde Q\tilde Q^{\natural}=Q_t^2e_t$ in the defective case is the product computation

$$
(Q_te_t+\vec Q)(Q_te_t-\vec Q)=Q_t^2e_t-\vec Q^2=Q_t^2e_t,
$$

which uses $\vec Q^2=0$. No pairing of two different elements occurs.

## The Two Bases

**The eigenvalue decomposition and the Jordan basis are the two frames of the same theorem, and the discriminant chooses between them.**

| condition | eigenbasis | Jordan basis | Jordan–Chevalley frame |
|---|---|---|---|
| $B^2\neq0$ | exists | not needed | spectral |
| $B^2=0$, $\vec Q=0$ | every basis | every basis | trivial |
| $B^2=0$, $\vec Q\neq0$ | does not exist | exists | defective |

For $B^2\neq0$ the spectral frame gives

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,\qquad
\lambda_\pm=Q_t\pm iB,\qquad
\tilde\Pi_\pm=\frac{e_t\pm\vec\Xi}{2},\qquad
\vec\Xi=-\frac{i\vec Q}{B},
$$

and the eigenbasis is $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ with the two mixed generators of the corners. The element is diagonal in that basis, and its diagonal values are $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$ for the left action.

For $B^2=0$ with $\vec Q=0$, the central case, every basis is at once an eigenbasis and a Jordan basis, the frame is $\{e_t\}$, and the split is the trivial $\tilde Q=\tilde Q+0$.

For $B^2=0$ and $\vec Q\neq0$ the defective frame gives

$$
\tilde Q=Q_te_t+\vec Q,\qquad \vec Q\in e\mathbb{B}e',\qquad \vec Q^2=0,
$$

and the Jordan basis is the four vectors of the corners, in which the left action is a pair of Jordan blocks of size two. The element has no eigenbasis: its eigenspace is the two-dimensional $\ker L_{\tilde Q}=\vec Q\mathbb{B}$, which is not the whole algebra, and the minimal polynomial has a double root.

The comparison is exact. In the semisimple case the Peirce decomposition at the spectral idempotents is the eigenvalue decomposition; in the defective case the Peirce decomposition at the support idempotents is the Jordan basis; and in both cases the diagonal corners carry $\tilde Q_s$ and the mixed corner carries $\vec\Upsilon$. The Jordan–Chevalley theorem is the statement that these are the only two possibilities, and the discriminant is the switch.

**Remark (which article owns what).** The construction of the spectral frame, the branch and the expansion of every biquaternion are in *The Eigenbasis of a Spectrally Regular Biquaternion*. The construction of the canonical defective frame, the Jordan pair and the Jordan basis are in *The Jordan Basis of a Spectrally Degenerate Biquaternion*. This article owns the split, the types and the corner pattern, and cites the two constructions rather than repeating them.

## Worked Examples

**Five elements, one per type, in the order of the three cases, with the decomposition computed from the formulas.**

### A Semisimple Unit

Take $\tilde Q=2e_t+\vec e_x$. Then $B^2=1$, $B=1$, and

$$
\lambda_\pm=2\pm i,\qquad
\tilde\Pi_\pm=\frac{e_t\mp i\vec e_x}{2},\qquad
\tilde Q=(2+i)\tilde\Pi_++(2-i)\tilde\Pi_- .
$$

The element is semisimple, $\tilde Q_s=\tilde Q$ and $\vec\Upsilon=0$. It is a unit, with inverse $(2+i)^{-1}\tilde\Pi_++(2-i)^{-1}\tilde\Pi_-$, and its multiplicative form is $\tilde Q=\tilde Q\,e_t$.

### A Semisimple Zero Divisor

Take $\tilde Q=e_t+i\vec e_x$. Then $B^2=-1$, $B=i$, and

$$
\lambda_+=0,\qquad \lambda_-=2,\qquad
\tilde\Pi_+=\frac{e_t-i\vec e_x}{2},\qquad
\tilde\Pi_-=\frac{e_t+i\vec e_x}{2},\qquad
\tilde Q=2\tilde\Pi_- .
$$

The element is semisimple, $\tilde Q_s=\tilde Q$ and $\vec\Upsilon=0$. It is a zero divisor: $\tilde Q\tilde\Pi_+=0$ and $\tilde\Pi_+\tilde Q=0$. The spectral frame exists and has two idempotents, but only one diagonal corner is occupied, because the eigenvalue of $\tilde\Pi_+$ is zero. The only product with a semisimple factor and a unipotent factor is the trivial $\tilde Q=\tilde Q\,e_t$.

### A Scalar Element

Take $\tilde Q=3e_t$. Then $\vec Q=0$, $p_{\tilde Q}=(X-3)^2$, $m_{\tilde Q}=X-3$, and $\tilde Q_s=3e_t$, $\vec\Upsilon=0$. The frame is $\{e_t\}$, every basis is an eigenbasis, and every idempotent commutes with the element. The scalar case is the only one in which the characteristic polynomial is not squarefree while the element is semisimple.

### A Jordan Element

Take $\tilde Q=2e_t+\vec e_x+i\vec e_y$. Then

$$
B^2=1+i^2=0,\qquad
Q_t=2,\qquad
\vec Q=\vec e_x+i\vec e_y,\qquad
\vec Q^2=\vec e_x^2+i(\vec e_x\vec e_y+\vec e_y\vec e_x)+i^2\vec e_y^2=-e_t+e_t=0 .
$$

Hence $\tilde Q_s=2e_t$, $\vec\Upsilon=\vec Q$, and $\vec\Upsilon^2=0$. The element is a unit, and the multiplicative form is

$$
\tilde Q=2\left(e_t+\frac{\vec e_x+i\vec e_y}{2}\right)=\tilde Q_s\tilde U,\qquad
\tilde U=e_t+\frac{\vec e_x+i\vec e_y}{2},\qquad
\tilde U^{-1}=e_t-\frac{\vec e_x+i\vec e_y}{2}.
$$

In the standard frame $\tilde\Pi_\pm=(e_t\pm i\vec e_z)/2$, with generators $\vec\Upsilon_x=(i\vec e_x-\vec e_y)/2$ and $\vec\Upsilon_y=(i\vec e_x+\vec e_y)/2$, the element reads

$$
\tilde Q=2(\tilde\Pi_++\tilde\Pi_-)-2i\vec\Upsilon_x,
$$

so the semisimple part occupies the two diagonal corners and the nilpotent part the corner $+-$.

### A Nilpotent Element

Take $\tilde Q=\vec e_x+i\vec e_y$. This is the nilpotent part of the preceding example. Then $B^2=0$, $Q_t=0$, $\tilde Q_s=0$ and $\vec\Upsilon=\tilde Q$. In the same frame $\tilde Q=-2i\vec\Upsilon_x$, a single mixed corner, and $\tilde Q^2=0$. There is no product with a semisimple factor and a unipotent factor: the semisimple factor would have to be a scalar, and the scalar part of the product would be non-zero while $\tilde Q$ has none.

**Remark (the two coincidences).** The characteristic polynomial is $(X-Q_t)^2$ both for a scalar element and for a Jordan element, and it is $X^2$ both for the nilpotent element and for the origin. In each pair the minimal polynomial separates the two, and the scalar part separates the Jordan element from the nilpotent one. The examples show that neither invariant alone classifies the element.

## Summary

Every biquaternion splits uniquely as $\tilde Q=\tilde Q_s+\vec\Upsilon$ with $\tilde Q_s$ semisimple, $\vec\Upsilon$ nilpotent and $\tilde Q_s\vec\Upsilon=\vec\Upsilon\tilde Q_s$. The proof separates on the discriminant of the characteristic polynomial $(X-Q_t)^2+B^2$: distinct roots give a semisimple element; a double root gives either the central case, already scalar, or the non-central case, a scalar part plus a non-zero square-zero vector. Uniqueness follows from the centraliser, which is $\mathbb{C}\times\mathbb{C}$ in the non-scalar semisimple case $B^2\neq0$, all of $\mathbb{B}$ at the scalar, the central half of the spectral-degenerate cone, and the dual numbers in the non-central half of the cone; in each, the only semisimple elements are the ones named by the theorem.

There are four minimal-polynomial types, read first by the discriminant and then by centrality. The non-scalar semisimple type has $B^2\neq0$ and $m_{\tilde Q}=p_{\tilde Q}$. The scalar type is the central half of the spectral-degenerate cone: $\vec Q=0$ and $m_{\tilde Q}=X-Q_t$. The non-central half, $B^2=0$ with $\vec Q\neq0$, splits by the scalar part into the Jordan type, $Q_t\neq0$ and $m_{\tilde Q}=(X-Q_t)^2$, and the nilpotent type, $Q_t=0$ and $m_{\tilde Q}=X^2$. The semisimple outcome of the split has three Peirce sub-cases: the scalar, where the frame is trivial; the unit; and the zero divisor. The last two have the same Jordan–Chevalley data and differ in the occupancy of the diagonal corners.

In a frame adapted to the element, $\tilde Q_s$ is diagonal and $\vec\Upsilon$ lies in a single mixed corner. The mixed corner is square-zero, so $\vec\Upsilon^2=0$ and the nilpotent index is at most two. This is the corner form of the theorem: the diagonal carries the semisimple part, the mixed corner carries the nilpotent part, and the Peirce idempotents are the idempotents of the element. The spectral frame gives the eigenvalue decomposition; the defective frame gives the Jordan basis; the discriminant chooses between them.

For a unit, the additive split gives the multiplicative form $\tilde Q=\tilde Q_s\tilde U$ with $\tilde U=e_t+\tilde Q_s^{-1}\vec\Upsilon$ unipotent and $\tilde U^{-1}=e_t-\tilde Q_s^{-1}\vec\Upsilon$. For a semisimple zero divisor the multiplicative form collapses to the trivial product, because $\tilde Q_s$ is not a unit and the centraliser has no non-zero nilpotent; a nilpotent element has no product at all. The whole article uses the product, the scalar part and the characteristic polynomial. No form, no norm, no pairing and no matrix is used. The canonical defective frame of the Jordan basis article is built from the element and the corner condition; this article replaces it by an arbitrary adapted frame, so that the theorem and its corner reading stay algebraic.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | a general element |
| $\tilde Q^{\natural}=Q_te_t-\vec Q$ | the natural conjugation |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part, the discriminant up to $-4$ |
| $p_{\tilde Q}(X)=(X-Q_t)^2+B^2$ | the characteristic polynomial |
| $m_{\tilde Q}$ | the minimal polynomial |
| $\tilde Q_s,\vec\Upsilon$ | the semisimple and nilpotent parts of $\tilde Q$ |
| $\tilde\Pi_\pm=(e_t\pm\vec\Xi)/2$, $\vec\Xi=-i\vec Q/B$ | the spectral idempotents, for $B^2\neq0$ |
| $e,e'$ | a defective frame, with $\vec Q\in e\mathbb{B}e'$ |
| $\mathbb{B}_{\sigma\tau}=\tilde\Pi_\sigma\mathbb{B}\tilde\Pi_\tau$ | a Peirce corner |
| $\vec\Upsilon_x,\vec\Upsilon_y$ | the mixed generators of the standard frame |
| $\tilde U=e_t+\tilde Q_s^{-1}\vec\Upsilon$ | the unipotent factor of a unit |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues, for $B^2\neq0$ |

## Further Reading

- [The Spectrum](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the characteristic polynomial, the spectral criterion and the two cases.
- [The Eigenbasis of a Spectrally Regular Biquaternion](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), for the spectral frame, the root and the eigenbasis.
- [The Jordan Basis of a Spectrally Degenerate Biquaternion](the-spectrally-degenerate-sector-and-construction-of-the-jordan-basis-of-a-biquaternion.html), for the defective sector, the support idempotents and the Jordan basis.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-in-the-biquaternion-algebra.html), for the Peirce decomposition, the corners and the mixed generators.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the units, the zero divisors and their two strata.
- [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), for the general theorem, its uniqueness and the multiplicative form.
- [The Eigenvalue Decomposition in a Jordan Algebra](the-eigenvalue-decomposition-in-a-jordan-algebra.html), for the spectral idempotents read as Peirce idempotents.
- [Modules over $k[x]$ and the Jordan Form](modules-over-kx-and-the-jordan-form.html), for the Jordan block behind the defective case.
- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), for the Clifford reading of the spectral case.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (2nd edition, Cambridge University Press, 2013), for the general Jordan–Chevalley theorem and the Jordan form.
