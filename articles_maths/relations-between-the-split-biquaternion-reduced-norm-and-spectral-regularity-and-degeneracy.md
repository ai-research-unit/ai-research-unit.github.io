# __The Reduced Norm and Spectral Degeneracy in the Split-Biquaternion Algebra__

## Introduction

The split-biquaternion algebra $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ carries two quadratic conditions on one element. The **reduced norm** $\Delta(\tilde Q)=|Q_+|^2|Q_-|^2$ is real, non-negative, multiplicative, and vanishes exactly when a half vanishes. The **component invariants** $|\vec q_\pm|^2$ are the squared lengths of the two vector parts; each vanishes exactly when its half is scalar. The first decides invertibility, the second detects scalar halves. The **spectrum** is regular when the reduced characteristic polynomial has no repeated root.

This article compares these invariants. Spectral regularity forces $\Delta\neq0$, but $\Delta\neq0$ does not force spectral regularity. Hence the cell "reduced-norm-degenerate, spectrally regular" is empty, while its opposite is not: a vanishing reduced norm forces a whole half to vanish, and a vanishing half is scalar, hence spectrally degenerate. The biquaternion algebra differs: its norm is a sum, not a product, and its Hermitian idempotents are norm-degenerate with simple spectra.

**Conventions.** The split complex unit is $j$, with $j^2=1$, and the idempotents are $\tilde\Pi_{1,2}=\tfrac12(1\pm j)$. An element is $\tilde Q=Q_+\tilde\Pi_1+Q_-\tilde\Pi_2$ with $Q_\pm=t_\pm+\vec q_\pm$, $t_\pm\in\mathbb{R}$, $\vec q_\pm=\sum_k q_{\pm k}\vec e_k$, and $|\vec q_\pm|^2=\sum_k q_{\pm k}^2$. The quaternion norm is $|Q_\pm|^2=t_\pm^2+|\vec q_\pm|^2$. The split-biquaternion norm is $\langle\tilde Q\rangle_{\natural}=|Q_+|^2\tilde\Pi_1+|Q_-|^2\tilde\Pi_2=\sum_\mu Q_\mu^2$, where $Q_\mu$ are the coefficients in the basis $e_\mu$. The reduced norm is $\Delta=|Q_+|^2|Q_-|^2=\langle\tilde Q\rangle_{\natural}\langle\tilde Q\rangle_{\natural}^{*}$. The spectral classification is *[Spectral Regularity and Degeneracy in the Split-Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-split-biquaternion-algebra.html)*; the cells are *[The Three Sectors of the Split-Biquaternion Algebra](the-three-sectors-of-the-split-biquaternion-algebra.html)*; the algebra and norm are *[Split-Biquaternion Algebra](split-biquaternion-algebra.html)* and *[Split-Biquaternion Norm and Invertibility](split-biquaternion-norm-and-invertibility.html)*.

## The Reduced Norm and the Component Invariants

### Definitions and Identities

**Lemma (the norm in the idempotent basis).** For $\tilde Q=Q_+\tilde\Pi_1+Q_-\tilde\Pi_2$,

$$
\langle\tilde Q\rangle_{\natural}=|Q_+|^2\tilde\Pi_1+|Q_-|^2\tilde\Pi_2
=\sum_{\mu=t,x,y,z}Q_\mu^2.
$$

*Proof.* Write $Q_\mu=a_\mu+jb_\mu$ with $a_\mu,b_\mu\in\mathbb{R}$. Since $a_\mu+jb_\mu=(a_\mu+b_\mu)\tilde\Pi_1+(a_\mu-b_\mu)\tilde\Pi_2$, the coefficient of $\tilde\Pi_1$ in $\sum_\mu Q_\mu^2$ is $\sum_\mu(a_\mu+b_\mu)^2$ and the coefficient of $\tilde\Pi_2$ is $\sum_\mu(a_\mu-b_\mu)^2$. Now $a_\mu=(q_{+\mu}+q_{-\mu})/2$ and $b_\mu=(q_{+\mu}-q_{-\mu})/2$, so

$$
\sum_\mu(a_\mu+b_\mu)^2=\sum_\mu q_{+\mu}^2=|Q_+|^2,
\qquad
\sum_\mu(a_\mu-b_\mu)^2=\sum_\mu q_{-\mu}^2=|Q_-|^2.
$$

**Definition (reduced norm).** The **reduced norm** of $\tilde Q$ is

$$
\Delta(\tilde Q)=|Q_+|^2|Q_-|^2=\langle\tilde Q\rangle_{\natural}\langle\tilde Q\rangle_{\natural}^{*}\in\mathbb{R}.
$$

It is a homogeneous real quartic in the eight real coordinates.

**Theorem (positivity and the zero criterion).** For every $\tilde Q$,

$$
\Delta(\tilde Q)\ge0,\qquad
\Delta(\tilde Q)=0\iff Q_+=0\text{ or }Q_-=0.
$$

Consequently $\tilde Q$ is a unit exactly when $\Delta(\tilde Q)\neq0$.

*Proof.* Each $|Q_\pm|^2$ is a sum of four squares, hence non-negative and zero only at $Q_\pm=0$. A product of non-negative reals vanishes exactly when a factor vanishes. In $\mathbb{H}\oplus\mathbb{H}$, an element is invertible exactly when both components are non-zero, by *[Split-Biquaternion Norm and Invertibility](split-biquaternion-norm-and-invertibility.html)*.

**Proposition (multiplicativity).** The reduced norm is multiplicative:

$$
\Delta(\tilde P\tilde Q)=\Delta(\tilde P)\Delta(\tilde Q).
$$

*Proof.* The halves multiply componentwise, $(\tilde P\tilde Q)_\pm=P_\pm Q_\pm$. The quaternion norm is multiplicative, since $|PQ|^2=(PQ)(PQ)^{*}=PQQ^{*}P^{*}=|P|^2|Q|^2$. Hence

$$
\Delta(\tilde P\tilde Q)=|P_+Q_+|^2|P_-Q_-|^2=|P_+|^2|P_-|^2|Q_+|^2|Q_-|^2.
$$

**Definition (component invariants).** The **component invariants** are $|\vec q_+|^2$ and $|\vec q_-|^2$. Each is a sum of three squares and is not multiplicative: $\vec e_x^2=-1$ has zero vector part while $|\vec e_x|^2|\vec e_x|^2=1$.

$\Delta$ is the product of the squared quaternion norms; the component invariants are the squared vector parts inside those norms. The identity $|Q_\pm|^2=t_\pm^2+|\vec q_\pm|^2$ splits each factor of $\Delta$ into a scalar square and a vector square.

### The Two Kinds of Invariant Side by Side

| Invariant | Formula | Vanishes exactly when | Multiplicative |
|---|---|---|---|
| $\Delta$ | $\lvert Q_+\rvert^2\lvert Q_-\rvert^2$ | $Q_+=0$ or $Q_-=0$ | yes |
| $\lvert Q_+\rvert^2$ | $t_+^2+\lvert\vec q_+\rvert^2$ | $Q_+=0$ | yes |
| $\lvert Q_-\rvert^2$ | $t_-^2+\lvert\vec q_-\rvert^2$ | $Q_-=0$ | yes |
| $\lvert\vec q_+\rvert^2$ | $q_{+x}^2+q_{+y}^2+q_{+z}^2$ | $\vec q_+=0$ | no |
| $\lvert\vec q_-\rvert^2$ | $q_{-x}^2+q_{-y}^2+q_{-z}^2$ | $\vec q_-=0$ | no |

A vanishing component invariant means only that one half is scalar; the half may still be a non-zero scalar, and then $\Delta$ is non-zero. A vanishing reduced norm is stronger: it requires a whole half to vanish.

**Proposition (the only implications).** The following hold.

(i) If $|\vec q_+|^2\neq0$ and $|\vec q_-|^2\neq0$, then $\Delta\neq0$.
(ii) If $\Delta=0$, then $|\vec q_+|^2=0$ or $|\vec q_-|^2=0$.
(iii) Neither converse holds.

*Proof.* (i) A non-zero vector part makes its half non-zero, so both factors of $\Delta$ are non-zero. (ii) By the zero criterion, one half is zero, so its vector part is zero. (iii) $Q_+=1$, $Q_-=\vec e_z$ has $|\vec q_+|^2=0$ but $\Delta=1$, so neither converse holds.

## Independence in the Only Direction Available

**Definition (the two predicates).** An element is **norm-regular** when $\Delta\neq0$ and **norm-degenerate** when $\Delta=0$. It is **spectrally regular** when $p_{\tilde Q}$ has no repeated root and **spectrally degenerate** when it has one.

**Theorem (the one-way implication).** Spectral regularity implies norm regularity. Norm regularity does not imply spectral regularity.

*Proof.* If $\Delta=0$, then $Q_+=0$ or $Q_-=0$ by the zero criterion. If $Q_+=0$ then $\vec q_+=0$, so case 1 of the repeated-root theorem of *[Spectral Regularity and Degeneracy in the Split-Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-split-biquaternion-algebra.html)* applies; the other case is the same. Hence spectral regularity forces $\Delta\neq0$.

For the converse, take $Q_+=1$ and $Q_-=\vec e_z$. Then $\Delta=1$ but $p_+=(\lambda-1)^2$ has a repeated root, so the element is spectrally degenerate.

**Corollary (the mixed cells).** The cell $\{\Delta\neq0,\ \text{spectrally degenerate}\}$ is non-empty, and the cell $\{\Delta=0,\ \text{spectrally regular}\}$ is empty.

The only independence available is the failure of the converse: a unit can have a repeated root, but a zero divisor cannot have a simple spectrum. In logical form,

$$
\text{spectrally regular}\Longrightarrow\text{norm-regular},
\qquad
\text{norm-regular}\not\Longrightarrow\text{spectrally regular}.
$$

There is no element that is norm-degenerate and spectrally regular.

## The Empty Mixed Cell and Its Cause

**Definition (the mixed cell).** Let

$$
\Sigma_{01}=\{\tilde Q:\Delta(\tilde Q)=0\text{ and }p_{\tilde Q}\text{ has no repeated root}\}.
$$

**Theorem ($\Sigma_{01}$ is empty).** No split biquaternion is both norm-degenerate and spectrally regular.

*Proof.* Let $\Delta(\tilde Q)=0$. By the zero criterion, $Q_+=0$ or $Q_-=0$. Suppose $Q_+=0$. Then $Q_+=0$ is the zero scalar, so $\vec q_+=0$; by the repeated-root theorem, $p_{\tilde Q}$ has a repeated root. The case $Q_-=0$ is identical. Hence spectral regularity fails.

The zero-divisor half is the **zero** scalar, so its reduced polynomial is $\lambda^2$, a double root at $0$. The other half may have a simple spectrum, but the double root already makes the element degenerate. A product of non-negative factors vanishes only through a zero factor.

**Corollary (no norm-degenerate regular element).** The empty cell is the failure of the converse. The non-empty cells are $\Sigma_{11}=\{\Delta\neq0,\ \text{spectrally regular}\}$, $\Sigma_{10}=\{\Delta\neq0,\ \text{spectrally degenerate}\}$ and $\Sigma_{00}=\{\Delta=0\}$; their geometry is *[The Three Sectors of the Split-Biquaternion Algebra](the-three-sectors-of-the-split-biquaternion-algebra.html)*.

## The Chain of Invariants

The zero criterion, the definition of a zero half, and the repeated-root criterion form a chain:

$$
\Delta=0
\iff Q_+=0\text{ or }Q_-=0
\implies \vec q_+=0\text{ or }\vec q_-=0
\implies p_{\tilde Q}\text{ has a repeated root}.
$$

The first equivalence is the zero criterion; the second says a zero quaternion has zero scalar and vector parts; the third is case 1 or case 2. The chain is one-way: $Q_+=1$, $Q_-=\vec e_z$ has $\vec q_+=0$ and a repeated root but $\Delta=1$; $Q_+=\vec e_x$, $Q_-=\vec e_z$ has both vector parts non-zero and a repeated root.

In terms of information, the invariants form a hierarchy:

| Invariant | Data | What it determines |
|---|---|---|
| $\Delta$ | one real number | whether the element is a unit |
| $(\lvert Q_+\rvert^2,\lvert Q_-\rvert^2)$ | two non-negative reals | the two factors of $\Delta$ and which half vanishes |
| $(t_\pm,\lvert\vec q_\pm\rvert^2)$ | four reals | the two half-spectra and the repeated-root pattern |
| $p_{\tilde Q}=p_+p_-$ | a monic quartic | the spectrum with the multiplicity of the reduced polynomial |
| $p_{\tilde Q}^2$ | a monic octic | the spectrum with the multiplicity of $L_{\tilde Q}$ |

The scalar/vector data determines the rest: the factor norms are $t_\pm^2+|\vec q_\pm|^2$, $\Delta$ is their product, and $p_{\tilde Q}=p_+p_-$. The reverse maps do not exist: $\Delta$ does not determine the factor norms, the factor norms do not determine the scalar/vector data, and $p_{\tilde Q}$ does not determine the pairing of roots with halves. The operator polynomial $p_{\tilde Q}^2$ adds only multiplicity.

**Proposition (what $\Delta$ forgets).** The reduced norm does not determine either component invariant, either scalar part, spectral regularity, or which half vanishes.

*Proof.* $Q_+=1$, $Q_-=\vec e_z$ has $\Delta=1$ and $|\vec q_+|^2=0$; $Q_+=\vec e_x$, $Q_-=\vec e_z$ has $\Delta=1$ and $|\vec q_+|^2=1$. $Q_+=1$, $Q_-=2\vec e_z$ and $Q_+=2$, $Q_-=\vec e_z$ both have $\Delta=4$ and scalar parts $(1,2)$ and $(2,1)$. At the same value $\Delta=4$, $Q_+=1$, $Q_-=2\vec e_z$ is degenerate while $Q_+=\vec e_x$, $Q_-=2\vec e_z$ is regular. Finally, $Q_+=0$, $Q_-=1$ and $Q_+=1$, $Q_-=0$ both have $\Delta=0$ and different vanishing halves.

The comparison is thus of a product with its factors: $\Delta$ is the product, the component invariants are the internal vector squares, and the scalar parts are the remaining data.

## Contrast with the Biquaternion Case

In the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the norm is

$$
\eta=Q_t^2+B^2,\qquad B^2=Q_x^2+Q_y^2+Q_z^2,
$$

with $Q_\mu\in\mathbb{C}$. It is a **sum**, not a product. The norm-degenerate set is the complex cone $\{Q_t^2+B^2=0\}$, and the spectral-degenerate set is $\{B^2=0\}$. The mixed cell $\Sigma_{01}$ is non-empty; the witnesses are the Hermitian idempotents.

Let $\vec u\in\mathbb{R}^3$ with $\vec u\cdot\vec u=1$ and put

$$
E=\tfrac12(1+i\vec u).
$$

The element $E$ is Hermitian, $E^*=E$. Then

$$
E^2=\tfrac14(1+2i\vec u+i^2\vec u^2)
=\tfrac14(1+2i\vec u-\vec u^2)
=\tfrac12(1+i\vec u)=E,
$$

because $\vec u^2=-\vec u\cdot\vec u=-1$. Its scalar part is $1/2$ and its vector part is $i\vec u/2$, so

$$
\eta(E)=\tfrac14+\tfrac{i^2}{4}(\vec u\cdot\vec u)=\tfrac14-\tfrac14=0,
\qquad
B^2(E)=\tfrac{i^2}{4}(\vec u\cdot\vec u)=-\tfrac14\neq0.
$$

Since $E^2=E$ and $E\neq0,1$, its minimal polynomial is $X(X-1)$, so the spectrum $\{0,1\}$ is simple. Thus $E$ is norm-degenerate and spectrally regular: it lies in the biquaternion $\Sigma_{01}$, the cell that is empty in the split algebra. These idempotents are non-central, form a two-sphere, and are rank-one projections in the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$.

A sum can cancel: $Q_t^2$ and $B^2$ can be opposite non-zero complex numbers, whereas a product of non-negative reals needs a zero factor. And $\mathbb{H}_{\mathbb{D}}$ has only the four central idempotents $0,\tilde\Pi_1,\tilde\Pi_2,1$, because each division algebra has only $0$ and $1$; a non-zero idempotent of the split algebra has a zero half. The biquaternion matrix algebra has non-central idempotents, and the Hermitian ones are the witnesses the split algebra cannot produce.

## Summary

The reduced norm is $\Delta=|Q_+|^2|Q_-|^2$, the product of the two quaternion norms; it is real, non-negative, multiplicative, and vanishes exactly when one half vanishes. The component invariants vanish exactly when a half is scalar. A zero component invariant does not force $\Delta=0$ (the scalar half may be non-zero); $\Delta=0$ forces one component invariant to zero (the zero half).

Spectral regularity implies norm regularity but not conversely. $\Sigma_{01}$ is empty; $\Sigma_{10}$ is non-empty. The scalar/vector data determines the factor norms, their product $\Delta$, and $p_{\tilde Q}$; these maps do not reverse.

The biquaternion algebra has a sum, not a product. Its Hermitian idempotents $\tfrac12(1+i\vec u)$ have norm zero and spectrum $\{1,0\}$, so its $\Sigma_{01}$ is non-empty. The split algebra has no such element, and its empty cell measures the difference.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ | Split-biquaternion algebra |
| $\tilde Q=Q_+\tilde\Pi_1+Q_-\tilde\Pi_2$ | Idempotent decomposition |
| $Q_\pm=t_\pm+\vec q_\pm$ | A half |
| $\lvert Q_\pm\rvert^2=t_\pm^2+\lvert\vec q_\pm\rvert^2$ | Quaternion norm of a half |
| $\lvert\vec q_\pm\rvert^2$ | Component invariant, the squared vector part |
| $\langle\tilde Q\rangle_{\natural}=\lvert Q_+\rvert^2\tilde\Pi_1+\lvert Q_-\rvert^2\tilde\Pi_2$ | Split-biquaternion norm |
| $\Delta=\lvert Q_+\rvert^2\lvert Q_-\rvert^2=\langle\tilde Q\rangle_{\natural}\langle\tilde Q\rangle_{\natural}^{*}$ | Reduced norm |
| $\Sigma_{01}=\{\Delta=0,\ \text{spectrally regular}\}$ | The empty mixed cell |
| $\Sigma_{10}=\{\Delta\neq0,\ \text{spectrally degenerate}\}$ | The non-empty mixed cell |
| $p_{\tilde Q}=p_+p_-$ | Reduced characteristic polynomial |

## Further Reading

- [Split-Biquaternion Algebra](split-biquaternion-algebra.html), for the algebra and its idempotents.
- [Split-Biquaternion Norm and Invertibility](split-biquaternion-norm-and-invertibility.html), for the reduced norm, the inverse formula and the unit group.
- [Split-Biquaternion Zero Divisors](split-biquaternion-zero-divisors.html), for the two ideals and the zero-divisor set.
- [Spectral Regularity and Degeneracy in the Split-Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-split-biquaternion-algebra.html), for the repeated-root criterion.
- [The Spectrum](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the complex cone and the comparison with the split case.
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for the biquaternion $\Sigma_{01}$ and the Hermitian idempotents.
- [The Three Sectors of the Split-Biquaternion Algebra](the-three-sectors-of-the-split-biquaternion-algebra.html), for the three non-empty cells and their dimensions.
