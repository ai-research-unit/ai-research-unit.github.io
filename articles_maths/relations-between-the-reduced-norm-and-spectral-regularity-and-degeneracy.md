# __Relations between the Reduced Norm and Spectral Regularity and Degeneracy__

## Introduction

The reduced biquaternion algebra
$$
\mathbb{B}_{\mathrm r}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}
$$
carries two quadratic conditions on an element $\breve Q=Q_\blacktriangle+jQ_\blacktriangledown$:
$$
\nu(\breve Q)=Q_+Q_-=Q_\blacktriangle^{2}-Q_\blacktriangledown^{2},
\qquad
\delta(\breve Q)^{2}=(Q_+-Q_-)^{2}=4Q_\blacktriangledown^{2}.
$$
The first is the reduced norm; it is multiplicative, vanishes on the two hyperplanes $Q_+=0$ and $Q_-=0$, whose nonzero points are the zero divisors, and decides invertibility. The second is the square of the eigenvalue difference, the discriminant of the characteristic polynomial; it vanishes on the scalar line $Q_+=Q_-$ and decides whether the two eigenvalues can be told apart. This article compares the two, proves that the conditions are independent, shows that the zero divisors are spectrally regular and that the punctured scalar line is norm-regular and spectrally degenerate, identifies the origin as doubly degenerate, and records the chain of invariants. The spectral criterion is *Spectral Regularity and Degeneracy in the Reduced Biquaternion Algebra*; the four combinations are *The Four Sectors of the Reduced Biquaternion Algebra*.

**Notation.** The element is $\breve Q=Q_\blacktriangle+jQ_\blacktriangledown$ with $j^{2}=+1$, $ij=ji$ and $i^{2}=-1$; $\Pi_\pm=\tfrac12(1\pm j)$; $Q_\pm=Q_\blacktriangle\pm Q_\blacktriangledown$; and $\breve Q=Q_+\Pi_+ +Q_-\Pi_-$. The reduced norm and the unit criterion are *Norm and Invertibility in the Algebra of the Reduced Biquaternions*; the zero divisors are *Zero Divisors of the Algebra of the Reduced Biquaternions*; the spectrum and the spectral decomposition are *Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion*.

## The Two Quadratic Invariants

**Definition (reduced norm).** The **reduced norm** is
$$
\nu(\breve Q)=Q_+Q_-=(Q_\blacktriangle+Q_\blacktriangledown)(Q_\blacktriangle-Q_\blacktriangledown)=Q_\blacktriangle^{2}-Q_\blacktriangledown^{2}.
$$

**Definition (eigenvalue difference and discriminant).** The **eigenvalue difference** is
$$
\delta(\breve Q)=Q_+-Q_-=2Q_\blacktriangledown,
$$
and the **discriminant** is
$$
\Delta(\breve Q)=\delta(\breve Q)^{2}=4Q_\blacktriangledown^{2}.
$$

**Theorem (the algebraic relation).** The two invariants satisfy
$$
\Delta=(Q_++Q_-)^{2}-4Q_+Q_-=4Q_\blacktriangle^{2}-4(Q_\blacktriangle^{2}-Q_\blacktriangledown^{2})=4Q_\blacktriangledown^{2}.
$$

*Proof.* Expand $(Q_++Q_-)^{2}-4Q_+Q_-=(Q_+-Q_-)^{2}=\delta^{2}$ and substitute $Q_\pm=Q_\blacktriangle\pm Q_\blacktriangledown$. The last equality is $4Q_\blacktriangle^{2}-4Q_\blacktriangle^{2}+4Q_\blacktriangledown^{2}$.

**Proposition (the roles in the characteristic polynomial).** The characteristic polynomial is
$$
p_{\breve Q}(X)=X^{2}-(Q_++Q_-)X+Q_+Q_-=X^{2}-2Q_\blacktriangle X+\nu(\breve Q).
$$
Its constant term is the reduced norm, its discriminant is $\Delta(\breve Q)$, and its trace is $Q_++Q_-=2Q_\blacktriangle$. The reduced norm is multiplicative,
$$
\nu(\breve Q_1\breve Q_2)=\nu(\breve Q_1)\nu(\breve Q_2),
$$
while the eigenvalue difference is additive, $\delta(\breve Q_1+\breve Q_2)=\delta(\breve Q_1)+\delta(\breve Q_2)$; its square $\Delta$ is neither multiplicative nor additive in general.

*Proof.* The polynomial is $(X-Q_+)(X-Q_-)$, so the coefficients are as displayed. Multiplicativity is the componentwise product in the idempotent coordinates,
$$
(Q_{1+}Q_{2+})(Q_{1-}Q_{2-})=(Q_{1+}Q_{1-})(Q_{2+}Q_{2-}).
$$
The difference is linear in the coordinates, hence additive. For the failure of multiplicativity of $\Delta$, take $\breve Q_1=\Pi_+$ and $\breve Q_2=\Pi_-$: their product is $0$, so $\Delta(\breve Q_1\breve Q_2)=0$, while $\Delta(\Pi_+)=1$ and $\Delta(\Pi_-)=1$, so $\Delta(\breve Q_1)\Delta(\breve Q_2)=1\neq0$. For the failure of additivity, $\Delta(\Pi_++\Pi_-)=\Delta(1)=0$, while $\Delta(\Pi_+)+\Delta(\Pi_-)=2$.

**Remark (the two forms).** In the coordinates $(Q_\blacktriangle,Q_\blacktriangledown)$, the reduced norm is the non-degenerate hyperbolic form $Q_\blacktriangle^{2}-Q_\blacktriangledown^{2}$, of real signature $(2,2)$. The discriminant is the square $4Q_\blacktriangledown^{2}$ of a linear form, hence degenerate; its zero set is the single line $Q_\blacktriangledown=0$, while the zero set of $\nu$ is the union of the two lines $Q_+=0$ and $Q_-=0$.

## Independence of the Two Conditions

**Definition (the predicates).** An element is **norm-regular** if $\nu(\breve Q)\neq0$ and **norm-degenerate** if $\nu(\breve Q)=0$. It is **spectrally regular** if $\delta(\breve Q)\neq0$, that is $Q_+\neq Q_-$, and **spectrally degenerate** if $\delta(\breve Q)=0$, that is $Q_+=Q_-$.

**Theorem (all four combinations occur).** The two predicates are independent: each of the four combinations is realized.

| sector | $(Q_+,Q_-)$ | element | $\nu$ | $\delta$ |
|---|---|---|---|---|
| $\Sigma_{11}$ | $(1,2)$ | $\tfrac32-\tfrac12 j$ | $2$ | $-1$ |
| $\Sigma_{01}$ | $(0,1)$ | $\Pi_-$ | $0$ | $-1$ |
| $\Sigma_{10}$ | $(1,1)$ | $1$ | $1$ | $0$ |
| $\Sigma_{00}$ | $(0,0)$ | $0$ | $0$ | $0$ |

*Proof.* The element is recovered from $(Q_+,Q_-)$ by $Q_\blacktriangle=\tfrac12(Q_++Q_-)$ and $Q_\blacktriangledown=\tfrac12(Q_+-Q_-)$, so each pair gives the displayed element. The values of $\nu$ and $\delta$ are read from the definitions. Hence neither predicate implies the other, and neither of the two zero sets contains the other.

**Corollary (the zero sets meet only at the origin).** The norm-zero set and the spectral-degenerate set satisfy
$$
\{Q_+Q_-=0\}\cap\{Q_+=Q_-\}=\{0\}.
$$

*Proof.* If $Q_+=Q_-$, then $Q_+Q_-=Q_+^{2}$; it vanishes only when $Q_+=0$, hence also $Q_-=0$. The origin lies in both sets.

**Remark (the geometric form of independence).** In idempotent coordinates the norm-zero set is the union of the two coordinate axes and the spectral-degenerate set is the diagonal; the diagonal meets each axis only at the origin. The four sectors are the four regions cut by these three lines, and the two conditions are transverse at their only common point.

## The Zero Divisors Are Spectrally Regular

**Theorem (the zero divisors have distinct eigenvalues).** Let $\breve Q$ be a nonzero zero divisor, so that $Q_+Q_-=0$ and $\breve Q\neq0$. Then exactly one of $Q_+,Q_-$ is zero and the other is nonzero; the spectrum is $\{0,\lambda\}$ with $\lambda\neq0$; the element is spectrally regular; and it has a two-term spectral decomposition with one zero eigenvalue.

*Proof.* The product $Q_+Q_-$ vanishes in the field $\mathbb{C}$ only when one factor vanishes. Since $\breve Q\neq0$, not both factors vanish. Hence exactly one is zero and the other is nonzero. The spectrum is $\{Q_+,Q_-\}=\{0,\lambda\}$ with $\lambda\neq0$, so the eigenvalues are distinct. If $Q_+=0$, then $\breve Q=Q_-\Pi_-$ with $Q_-\neq0$, and the spectral decomposition is
$$
\breve Q=0\cdot\Pi_+ +Q_-\Pi_-.
$$
If $Q_-=0$, the roles of $\Pi_+$ and $\Pi_-$ are exchanged.

**Example.** The element $\breve Q=1+j=2\Pi_+$ has $(Q_+,Q_-)=(2,0)$, reduced norm $0$ and spectrum $\{2,0\}$; its spectral decomposition is $2\Pi_+ +0\Pi_-$, so it is a zero divisor and spectrally regular at once.

**Remark (the annihilated idempotent).** If $Q_+=0$, the element is $Q_-\Pi_-$ and annihilates $\Pi_+$: $\breve Q\Pi_+=0$. The zero eigenvalue is attached to $\Pi_+$ and the nonzero eigenvalue $Q_-$ to $\Pi_-$: one spectral idempotent is annihilated, but the eigenvalues remain distinct.

## The Central Line and the Origin

**Theorem (the punctured scalar line is norm-regular and spectrally degenerate).** On the set
$$
\mathbb{C}^{\times}\cdot1=\{Q_+=Q_-\neq0\}=\{Q_\blacktriangledown=0,\ Q_\blacktriangle\neq0\},
$$
the reduced norm is $\nu=Q_+^{2}\neq0$, so the element is a unit; the spectrum is the singleton $\{Q_+\}$; the characteristic polynomial is $(X-Q_+)^{2}$; the minimal polynomial is $X-Q_+$; the spectral decomposition is the one-term writing $Q_+1$; and the element is semisimple, not defective.

*Proof.* The identities $Q_+=Q_-$ and $Q_+\neq0$ give $Q_\blacktriangle=Q_+\neq0$ and $Q_\blacktriangledown=0$, hence $\nu=Q_+^{2}\neq0$. The spectrum, the characteristic polynomial and the minimal polynomial are those of the scalar line in *Spectral Regularity and Degeneracy in the Reduced Biquaternion Algebra*, §*The Scalar Stratum*. The minimal polynomial is linear, hence squarefree, so the element is semisimple.

**Theorem (the origin is doubly degenerate).** At $\breve Q=0$, both conditions degenerate: $\nu(0)=0$ and $\delta(0)=0$. The spectrum is $\{0\}$, the characteristic polynomial is $X^{2}$, the minimal polynomial is $X$, the eigenspace is all of $\mathbb{B}_{\mathrm r}$, and the spectral decomposition is the one-term writing $0=0\cdot1$.

*Proof.* The values follow from $Q_+=Q_-=0$. The spectrum is the singleton $\{0\}$, and $X$ is the monic polynomial of least degree annihilating $0$, so the minimal polynomial is $X$. Every vector $v$ satisfies $0v=0$, so the eigenspace is the whole algebra.

## The Chain of Invariants

**Definition (the binary invariants).** Define
$$
\nu_0(\breve Q)=
\begin{cases}1,&\nu(\breve Q)\neq0,\\0,&\nu(\breve Q)=0,\end{cases}
\qquad
\sigma_0(\breve Q)=
\begin{cases}1,&\delta(\breve Q)\neq0,\\0,&\delta(\breve Q)=0.\end{cases}
$$
Then the four sectors are
$$
\Sigma_{ij}=\{\breve Q:\nu_0(\breve Q)=i,\ \sigma_0(\breve Q)=j\},
\qquad i,j\in\{0,1\}.
$$

**Theorem (the chain).** The invariants form the chain
$$
\breve Q\ \longmapsto\ (\nu(\breve Q),\delta(\breve Q))\ \longmapsto\ (\nu_0(\breve Q),\sigma_0(\breve Q)),
$$
and the types are counted in the table.

| invariant | data | number of types |
|---|---|---|
| reduced norm | $\nu=Q_+Q_-$ | $2$: $\nu\neq0$ (units) and $\nu=0$ (zero divisors and origin) |
| eigenvalue difference | $\delta=Q_+-Q_-$ | $2$: $\delta\neq0$ (regular) and $\delta=0$ (degenerate) |
| pair | $(\nu,\delta)$ | $4$: the four sectors |
| element | $(Q_+,Q_-)$ | continuum: all values |

*Proof.* The element determines $\nu$ and $\delta$ by their definitions, and the pair determines the two binary invariants. The four combinations of the binary invariants are the four sectors, and all four occur by the witness table of §*Independence of the Two Conditions*. The element has two complex degrees of freedom, so it is not determined by the two invariants; the pair $(\nu,\delta)$ determines the trace only up to sign, since $(Q_++Q_-)^{2}=\delta^{2}+4\nu$.

**Corollary (the characteristic polynomial reads the chain).** The characteristic polynomial is
$$
p_{\breve Q}(X)=X^{2}-(Q_++Q_-)X+\nu(\breve Q),
$$
of discriminant $\Delta(\breve Q)=\delta(\breve Q)^{2}$. The constant term is the reduced norm, the discriminant is the square of the eigenvalue difference, and the trace is the coefficient that the pair $(\nu,\delta)$ retains only up to sign.

**Remark (the minimal polynomial does not refine the chain).** The minimal polynomial is $X-Q_+$ on the scalar line $\Sigma_{10}\cup\Sigma_{00}$ and $(X-Q_+)(X-Q_-)$ on its complement $\Sigma_{11}\cup\Sigma_{01}$. It therefore separates two types, not four, and it does not split any sector. This is the effect of semisimplicity: the biquaternion algebra refines the four sectors into six strata by the minimal polynomial, because its scalar line splits into a scalar and a Jordan part and its origin splits into the origin and the nonzero nilpotents (*Relations between the N Norm and Spectral Regularity and Degeneracy*, §*The Chain of Invariants*). In the reduced algebra those defective parts are empty.

**Remark (the chain is not multiplicative).** The reduced norm is multiplicative, but the sector is not. The unit group $\Sigma_{11}\cup\Sigma_{10}$ is closed under multiplication. In $\Sigma_{01}$, $\Pi_+^{2}=\Pi_+$ stays in the sector while $\Pi_+\Pi_-=0$ falls in $\Sigma_{00}$. Two elements of $\Sigma_{11}$ can multiply into $\Sigma_{10}$:
$$
\left(\tfrac32-\tfrac12 j\right)\left(\tfrac32+\tfrac12 j\right)=2,
$$
with factors $(1,2)$ and $(2,1)$. An element of $\Sigma_{01}$ times an element of $\Sigma_{10}$ stays in $\Sigma_{01}$, because one coordinate remains zero and the other is multiplied by a nonzero scalar.

## Summary

The reduced norm and the eigenvalue difference are the two quadratic invariants:
$$
\nu=Q_+Q_-=Q_\blacktriangle^{2}-Q_\blacktriangledown^{2},
\qquad
\delta^{2}=(Q_+-Q_-)^{2}=4Q_\blacktriangledown^{2}.
$$
The first is multiplicative, vanishes on the two hyperplanes $Q_+=0$ and $Q_-=0$, and decides invertibility. The second is the discriminant of the characteristic polynomial, vanishes on the scalar line $Q_+=Q_-$, and decides spectral degeneracy. They are related by $\delta^{2}=(Q_++Q_-)^{2}-4\nu$, so the characteristic polynomial is determined by the trace and the reduced norm.

The conditions are independent: all four combinations occur, and the two zero sets meet only at the origin. The zero divisors $\Sigma_{01}$ are spectrally regular, with spectrum $\{0,\lambda\}$, $\lambda\neq0$, and a two-term decomposition with one zero eigenvalue. The punctured scalar line $\Sigma_{10}$ is norm-regular and spectrally degenerate, with reduced norm $Q_+^{2}\neq0$, spectrum $\{Q_+\}$ and linear minimal polynomial. The origin $\Sigma_{00}$ is doubly degenerate and is the only element in both zero sets.

The chain runs from the element to $(\nu,\delta)$, then to the binary pair $(\nu_0,\sigma_0)$, which is the sector. The pair forgets the sign of the trace, and the minimal polynomial separates only two types, not four: every element is semisimple, so the defective strata of the biquaternion algebra are absent. The chain is not multiplicative; the four sectors are studied in *The Four Sectors of the Reduced Biquaternion Algebra*.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\nu(\breve Q)=Q_+Q_-=Q_\blacktriangle^{2}-Q_\blacktriangledown^{2}$ | the reduced norm |
| $\delta(\breve Q)=Q_+-Q_-=2Q_\blacktriangledown$ | the eigenvalue difference |
| $\Delta(\breve Q)=\delta^{2}=4Q_\blacktriangledown^{2}$ | the discriminant |
| $Q_++Q_-=2Q_\blacktriangle$ | the trace |
| $\nu_0,\sigma_0$ | the binary norm and spectral predicates |
| $\Sigma_{ij}$ | the sector with $\nu_0=i$ and $\sigma_0=j$ |
| $\{Q_+Q_-=0\}$ | the norm-zero set, the two coordinate hyperplanes |
| $\{Q_+=Q_-\}$ | the spectral-degenerate set, the scalar line |
| $\mathbb{C}^{\times}\cdot1$ | the punctured scalar line |
| $\Pi_\pm=\tfrac12(1\pm j)$ | the two idempotents |

## Further Reading

- [Spectral Regularity and Degeneracy in the Reduced Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-reduced-biquaternion-algebra.html), for the spectral criterion, the eigenspaces and the scalar stratum.
- [The Four Sectors of the Reduced Biquaternion Algebra](the-four-sectors-of-the-reduced-biquaternion-algebra.html), for the four cells, their dimensions and their closures.
- [Norm and Invertibility in the Algebra of the Reduced Biquaternions](norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the reduced norm and the unit criterion.
- [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the two punctured idempotent lines.
- [Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion](eigenvalue-decomposition-and-eigenbasis-of-a-reduced-biquaternion.html), for the spectrum and the spectral decomposition.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-quaternionic-norm-and-spectral-regularity-and-degeneracy.html), for the non-commutative comparison and its finer chain of invariants.
