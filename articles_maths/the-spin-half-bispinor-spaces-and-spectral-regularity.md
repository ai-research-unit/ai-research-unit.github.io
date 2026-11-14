# __The Spin-Half Bispinors and Spectral Regularity__

## Introduction

The spin-half carrier is the plane $\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_+(\vec u_{\mathrm r})$, and its closures are the two spinor spaces and their sum. This article computes the second predicate on all of them, and the answer is the opposite of the answer for the norm.

On the plane the norm vanishes everywhere and the two eigenvalues are separated everywhere except at the origin. The plane is a null plane and a spectrally regular plane at the same time. This is the sharpest single statement in the group of articles: it shows that the two predicates are independent, that neither implies the other, and that a carrier can sit at one extreme for one of them and at the other extreme for the other.

The two eigenvalues of an element of the plane are $0$ and $\lambda$, so the spectrum is the pair of the coordinate and zero, and the separation is exactly the nonvanishing of the coordinate. The idempotent itself has spectrum $\{0,1\}$, which is the idempotent relation read as a statement about eigenvalues, and that is where the two values come from.

Inside the spinor space the statement is finer. Every element has a vanishing eigenvalue, because the norm vanishes and the product of the two eigenvalues is the norm. The other eigenvalue is twice the scalar coordinate, and the degenerate elements are those whose scalar coordinate vanishes. They form a real plane inside the spinor space, and they are exactly the elements of the ideal whose square vanishes. So the degenerate locus inside a spinor space is neither empty nor the whole space: it is a plane of square-zero elements.

The companion article is *The Spin-Half Bispinors and N Norm Regularity*, where the first predicate is computed and the answer is degenerate everywhere. The spaces themselves are *Introduction to the Spin-Half Bispinors*. The predicates and the four sectors are defined in *Relations between the N Norm and Spectral Regularity and Degeneracy*.

Nothing below is a statement of physics. The algebra $\mathbb{B}$ is real, of dimension $8$, with units $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t$ the identity and $\vec e_k^{2}=-e_t$, and with $i$ an element commuting with the units and $i^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu=q_\mu+iq'_\mu$ complex. A unit real axis is written $\vec u_{\mathrm r}$, and $\vec u_2,\vec u_3$ is an oriented orthonormal pair completing it.

## The Two Eigenvalues

**The quadratic relation.** Every element satisfies $X^{2}-2Q_tX+N(X)e_t=0$, so its two eigenvalues are

$$
\lambda_{\pm}=Q_t\pm iB,\qquad B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2},
$$

with $B$ a fixed square root of $B^{2}$. The element is **spectrally regular** when $B^{2}\neq0$ and **spectrally degenerate** when $B^{2}=0$. The degenerate locus is the **spectral-degenerate cone** $\mathcal S=\{B^{2}=0\}$.

**Remark (the sum and the product).** The two eigenvalues are determined by their sum $2Q_t$ and their product $N(X)$, and the predicate asks whether the product equals the square of half the sum. Two complex numbers with a given sum and product coincide exactly when the product equals the square of half the sum, and that is the condition $B^{2}=0$.

## The Plane

**Theorem (the square of the vector part).** For every complex $\lambda$,

$$
B^{2}\bigl(\lambda\tilde\Pi_+(\vec u_{\mathrm r})\bigr)=-\tfrac14\lambda^{2}.
$$

*Proof.* The coordinates are $Q_t=\tfrac12\lambda$ and $Q_k=\tfrac i2\lambda u_k$, so

$$
B^{2}=\sum_k\Bigl(\tfrac i2\lambda u_k\Bigr)^{2}=-\tfrac14\lambda^{2}\sum_k u_k^{2}=-\tfrac14\lambda^{2}.
$$

**Corollary (the plane is spectrally regular away from the origin).** The factor $-\tfrac14$ is invertible, so $B^{2}$ vanishes on the plane exactly at $\lambda=0$:

$$
\Sigma(\vec u_{\mathrm r})\cap\mathcal S=\{0\}.
$$

**Theorem (the spectrum of an element of the plane).** For $\lambda\neq0$,

$$
\operatorname{spec}\bigl(\lambda\tilde\Pi_+(\vec u_{\mathrm r})\bigr)=\{0,\lambda\},
$$

and the two eigenvalues are distinct.

*Proof.* The two eigenvalues are $Q_t\pm iB$ with $Q_t=\tfrac12\lambda$ and $iB=\pm\tfrac12\lambda$, so the pair is $\{\lambda,0\}$.

**Corollary (the plane is null and spectrally regular).** Every nonzero element of the carrier is norm-degenerate and spectrally regular, so the plane away from the origin lies in the sector $\Sigma_{01}$.

**Remark (why this is the sharp case).** On the centre the norm separated and the spectrum did not. On the plane the spectrum separates and the norm does not, and the two failures are at the same elements. Neither predicate controls the other, and the plane is the cleanest demonstration of it.

## The Idempotent

**Theorem.** $\operatorname{spec}\bigl(\tilde\Pi_+(\vec u_{\mathrm r})\bigr)=\{0,1\}$.

*Proof.* The coordinate is $Q_t=\tfrac12$, so the eigenvalues are $\tfrac12\pm\tfrac12$.

**Remark (the idempotent relation read spectrally).** The two eigenvalues of an idempotent sum to $2Q_t(P)=1$ and multiply to $N(P)=0$. A pair of complex numbers with sum $1$ and product $0$ is $\{0,1\}$, so the spectral content of $P^{2}=P$ is that the two values are $0$ and $1$. The spectral version of "the algebra splits as a sum of two ideals" is "the idempotent has one eigenvalue zero and one eigenvalue one", and the two statements carry the same content.

**Remark (the same element is null).** The element of the previous display is also of norm zero. So the two eigenvalues are $0$ and $1$, distinct, and the norm vanishes. There is no contradiction: the norm is the product of the two eigenvalues, and a product vanishes when one factor does.

## Inside the Spinor Space

**Theorem (one eigenvalue always vanishes).** For every $Y\in S_+(\vec u_{\mathrm r})$,

$$
N(Y)=0,\qquad \operatorname{spec}(Y)=\{0,\,2Q_t(Y)\}.
$$

*Proof.* The norm vanishes on the spinor space, and the two eigenvalues have product $N(Y)=0$ and sum $2Q_t(Y)$. A pair of complex numbers with vanishing product contains a zero, so the pair is $\{0,2Q_t(Y)\}$.

**Corollary (the degenerate elements of the spinor space).** An element $Y$ of the spinor space is spectrally degenerate exactly when

$$
Q_t(Y)=0 .
$$

**Theorem (the degenerate locus is a real plane).** In the complex basis $\tilde\Pi_+$ and $\vec u_2\tilde\Pi_+$ of the spinor space, the scalar coordinate is the coefficient of the first basis element, since

$$
\vec u_2\tilde\Pi_+(\vec u_{\mathrm r})=\tfrac12\bigl(\vec u_2-i\vec u_3\bigr),\qquad Q_t\bigl(\tfrac12(\vec u_2-i\vec u_3)\bigr)=0 .
$$

So the degenerate elements are the complex multiples of $\vec u_2-i\vec u_3$, a real plane:

$$
S_+(\vec u_{\mathrm r})\cap\mathcal S=\mathbb{C}\bigl(\vec u_2-i\vec u_3\bigr),\qquad \dim_\mathbb{R}=2 .
$$

*Proof.* The first display uses $\vec u_2\vec u_{\mathrm r}=-\vec u_3$, which follows from the multiplication of the pure units. The coefficient of $\tilde\Pi_+$ in $\alpha\tilde\Pi_++\beta\vec u_2\tilde\Pi_+$ is $\alpha$, and $Q_t$ reads half of it, so $Q_t=0$ is $\alpha=0$.

**Theorem (the degenerate elements are the square-zero elements).** For $Y$ in the spinor space,

$$
Y^{2}=0\iff Y\ \text{is spectrally degenerate}.
$$

*Proof.* On the spinor space the quadratic relation reduces to $Y^{2}=2Q_t(Y)Y$, since the norm vanishes. If $Q_t(Y)=0$ then $Y^{2}=0$. Conversely if $Y^{2}=0$ and $Y\neq0$ then $2Q_t(Y)Y=0$, so $Q_t(Y)=0$.

**Remark (the plane is not the degenerate locus).** The degenerate locus of the spinor space is a real plane, and it is not the carrier. The carrier is $\mathbb{C}\tilde\Pi_+$, spanned by the idempotent; the degenerate locus is $\mathbb{C}(\vec u_2-i\vec u_3)$, spanned by a square-zero element. The two planes meet only at the origin, since the two spanning elements are not proportional: one has $Q_t=\tfrac12$ and the other $Q_t=0$.

**Remark (one plane per axis, one degenerate plane per axis).** The two planes move with the axis, and the degenerate plane of one axis is the carrier plane of no axis, since its generator is not an idempotent. The family of carriers and the family of degenerate planes are two different families, both indexed by the axis.

## The Bispinor Space

**The predicate on a bispinor space.** An element $X=X_++X_-$ is spectrally degenerate exactly when $B^{2}(X)=0$. The quantity $B^{2}$ is a quadratic form in the eight real coordinates of $X$, and the equation is complex, so it is two real equations; the degenerate elements form a set of real dimension $6$ and the regular ones are its complement, of real dimension $8$ minus that set.

**Remark (the degenerate set is not small).** The cone is not a subspace and not empty. The element $\vec u_2-i\vec u_3$ is in it, and so is every element whose spinor decomposition has a vanishing component, since each spinor space is entirely degenerate. What is not in it is a generic element of the bispinor space, and that is the sense in which the bispinor read is the regular case.

## The Three Carriers Compared

| carrier | $B^{2}$ on it | spectrally degenerate locus in it |
| --- | --- | --- |
| centre $\mathbb{C}e_t$ | $0$ | the whole centre |
| spinor plane $\Sigma$ | $-\lambda^{2}/4$ | $\{0\}$ |
| vector part $\mathfrak{k}$ | $\lvert\vec v\rvert^{2}$ | $\{0\}$ |

**Where the carrier sits.** The plane away from the origin is norm-degenerate and spectrally regular, hence in $\Sigma_{01}$; the centre is in $\Sigma_{10}$; the vector part is in $\Sigma_{11}$. The fourth sector $\Sigma_{00}$ is met by no carrier except at the origin, though the closure of the plane meets it on the degenerate plane of the spinor space.

## Summary

The square of the vector part on the plane is $-\lambda^{2}/4$, so the plane is spectrally regular at every point except the origin, while its norm vanishes everywhere. The spectrum of $\lambda\tilde\Pi_+$ is $\{0,\lambda\}$, and the idempotent itself has spectrum $\{0,1\}$. Inside the spinor space every element has spectrum $\{0,2Q_t\}$, the degenerate elements are those with vanishing scalar coordinate, they form the real plane $\mathbb{C}(\vec u_2-i\vec u_3)$, and they are exactly the elements whose square vanishes. The plane away from the origin lies in the sector $\Sigma_{01}$: null and spectrally regular.

## The Boxed Summary

| the point | in plain words |
| --- | --- |
| the carrier | The spin-half carrier is a complex line generated by an element of zero norm. |
| the spectral quantity | On the plane the square of the vector part is minus a quarter of the square of the coordinate. |
| where it vanishes | At the origin alone. |
| the answer on the plane | The plane is spectrally regular everywhere except at the origin, although its norm vanishes everywhere. |
| the spectrum | An element of the plane has the spectrum made of zero and its own coordinate. The generator of the plane has spectrum zero and one. |
| inside an ideal | Every element of an ideal has the spectrum made of zero and twice its scalar coordinate. |
| the degenerate part of an ideal | The elements whose scalar coordinate vanishes form a real plane, and they are exactly the elements whose square vanishes. |
| the moral | The two halves behave oppositely. The norm sees nothing, the spectral condition sees almost everything. |
| the sector | Away from the origin the plane lies in the sector that is norm-degenerate and spectrally regular. |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, real, of dimension $8$ |
| $\tilde Q=Q_te_t+\vec Q$ | an element, with $Q_\mu$ complex |
| $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the $N$ norm |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the square of the vector part |
| $\lambda_{\pm}=Q_t\pm iB$ | the two eigenvalues of an element |
| spectral-regular | $B^{2}\neq0$ |
| $\mathcal S=\{B^{2}=0\}$ | the spectral-degenerate cone |
| $\tilde\Pi_\pm(\vec u_{\mathrm r})=\tfrac12(e_t\pm i\vec u_{\mathrm r})$ | the two idempotents of the axis |
| $\Sigma(\vec u_{\mathrm r})=\mathbb{C}\tilde\Pi_+$ | the spinor plane, the carrier |
| $S_\pm(\vec u_{\mathrm r})=\mathbb{B}\tilde\Pi_\pm$ | the spinor spaces |
| $\vec u_2-i\vec u_3$ | the square-zero element spanning the degenerate plane of $S_+$ |
| $\Sigma_{ij}$ | the sector with $N\neq0$ for $i=1$ and $B^{2}\neq0$ for $j=1$ |

## Further Reading

- [Introduction to the Spin-Half Bispinors](the-spin-half-bispinor-spaces.html), for the plane, the two spinor spaces and the family of bispinor spaces
- [The Spin-Half Bispinors and N Norm Regularity](the-spin-half-bispinor-spaces-and-n-norm-regularity.html), for the other predicate on the same spaces
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the definitions of the two predicates and the four sectors
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for the sector in which the plane away from the origin lies
- [The Spectrum](the-spectrum.html), for the two eigenvalues of an element and the quadratic relation
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the idempotents, the ideals and the splitting
- [The Carriers, the Representation, the Spin and the Closure](the-carriers-the-representation-the-spin-and-the-closure.html), for the three carriers taken together
