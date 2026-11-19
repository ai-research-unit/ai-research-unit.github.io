# __The Spin-One Anti-Hermitian Subspace and Spectral Regularity__

## Introduction

The spin-one carrier is the vector part $\mathfrak{k}$ and its closure is the anti-Hermitian subspace $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathfrak{k}$. This article computes the second predicate on the closure and on the carrier.

The answer is the mild one, and it is worth stating plainly because the two other carriers are extreme. On the carrier the two eigenvalues are $\pm i\lvert\vec v\rvert$, distinct for every nonzero $\vec v$, so the carrier is spectrally regular at every point except the origin. On the closure the degenerate locus is exactly the extra line $\mathbb{R}(ie_t)$, of real dimension one: an element is degenerate when its vector part vanishes and at no other time. So the closure is degenerate on a line and regular on the complement of it, and the carrier avoids the line altogether.

The spectrum has a shape of its own here. Both eigenvalues are purely imaginary, and they are symmetric about the point $i\lambda$ on the imaginary axis. That is not a coincidence of the coordinates: the anti-Hermitian condition forces it, and the reason is given below. The carrier, which is anti-Hermitian with a vanishing central part, has the symmetric pair $\pm i\lvert\vec v\rvert$ about the origin.

The article ends by comparing the degenerate loci of the three carriers. On the centre the spectrum is degenerate everywhere and the norm is regular; on the plane the norm is degenerate everywhere and the spectrum is regular; on the vector part both are regular away from the origin. On the closure the two degenerate loci are disjoint except at the origin, which is a sharper statement than the carrier comparison and is proved below.

The companion article is *The Spin-One Anti-Hermitian Subspace and N Norm Regularity*, where the first predicate is computed: the norm there is indefinite of inertia $(3,1)$ with a cone of real dimension $3$. The subspace itself is *Introduction to the Spin-One Anti-Hermitian Subspace*. The predicates and the four sectors are defined in *Relations between the N Norm and Spectral Regularity and Degeneracy*.

Nothing below is a statement of physics. The algebra $\mathbb{B}$ is real, of dimension $8$, with units $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t$ the identity and $\vec e_k^{2}=-e_t$, and with $i$ an element commuting with the units and $i^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu=q_\mu+iq'_\mu$ complex. The pure part is $\mathfrak{k}=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$, an element of it is written $\vec v$ with $\lvert\vec v\rvert^{2}=v_x^{2}+v_y^{2}+v_z^{2}$, and the star is the Hermitian conjugation.

## The Two Eigenvalues

**The quadratic relation.** Every element satisfies $X^{2}-2Q_tX+N(X)e_t=0$, so its two eigenvalues are

$$
\lambda_{\pm}=Q_t\pm iB,\qquad B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2},
$$

with $B$ a fixed square root of $B^{2}$. The sum of the two eigenvalues is $2Q_t$ and the product is $N(X)$. An element is **spectrally regular** when $B^{2}\neq0$ and **spectrally degenerate** when $B^{2}=0$, and the zero locus is the **spectral-degenerate cone** $\mathcal S=\{B^{2}=0\}$.

## The Predicate on the Closure

**Theorem (the predicate reads the vector part).** For real $\lambda$ and real $\vec v$,

$$
B^{2}(i\lambda+\vec v)=\lvert\vec v\rvert^{2},
$$

a real number which is non-negative.

*Proof.* The coordinates are $Q_k=v_k$ real, so the sum of their squares is the positive definite form on the triple.

**Corollary (the degenerate locus of the closure is the line).** On the closure,

$$
\mathbb{B}_{\Phi}\cap\mathcal S=\mathbb{R}(ie_t),
$$

of real dimension $1$.

*Proof.* The value $\lvert\vec v\rvert^{2}$ vanishes exactly when $\vec v=0$, which is the condition for the element to be a real multiple of $ie_t$.

**Theorem (the spectrum on the closure).** For every element of the closure,

$$
\operatorname{spec}(i\lambda+\vec v)=\bigl\{i(\lambda+\lvert\vec v\rvert),\ i(\lambda-\lvert\vec v\rvert)\bigr\}.
$$

*Proof.* The two eigenvalues are $Q_t\pm iB$ with $Q_t=i\lambda$ and $B=\lvert\vec v\rvert$, and $iB=\pm i\lvert\vec v\rvert$.

**Corollary (the spectrum is purely imaginary).** Both eigenvalues lie on the imaginary axis and are symmetric about $i\lambda$.

**Corollary (the closure is spectrally regular off the line).** Every element of the closure with a nonzero vector part is spectrally regular, and every element of the line is spectrally degenerate.

**Remark (why the spectrum is imaginary).** The condition defining the closure is $X^{*}=-X$, and the star reverses the real part of the scalar coordinate while preserving the reality of the vector part. The two eigenvalues of $X=i\lambda+\vec v$ are then $i\lambda$ plus a correction $iB$ which is also purely imaginary, because $B^{2}=\lvert\vec v\rvert^{2}$ is a non-negative real number and its square root is real. The reality of $\vec v$ is what makes $B$ real; on the complex elements of the algebra $B$ need not be real and the spectrum need not be imaginary.

## The Predicate on the Carrier

**Theorem (the carrier is regular away from the origin).** For real $\vec v\neq0$,

$$
\operatorname{spec}(\vec v)=\{i\lvert\vec v\rvert,\ -i\lvert\vec v\rvert\},
$$

and the two eigenvalues are distinct.

*Proof.* The theorem above with $\lambda=0$.

**Corollary (the carrier avoids the degenerate cone).** $\mathfrak{k}\cap\mathcal S=\{0\}$, and every nonzero element of the carrier is spectrally regular.

**Remark (the degenerate elements of the whole algebra are not far away).** The cone $\mathcal S$ is cut out by one complex equation and is large; the closure meets it on a line and the carrier only at the origin. The carrier is the part of the algebra on which the predicate is cheapest to decide, since the criterion is the vanishing of a positive definite form.

## The Two Degenerate Loci Are Disjoint

**Theorem (spectral and norm degeneracy do not meet on the closure).** On the closure,

$$
\bigl(\mathcal N\cap\mathbb{B}_{\Phi}\bigr)\cap\bigl(\mathcal S\cap\mathbb{B}_{\Phi}\bigr)=\{0\}.
$$

*Proof.* An element of the closure is norm-degenerate when $\lvert\vec v\rvert^{2}=\lambda^{2}$ and spectrally degenerate when $\lvert\vec v\rvert^{2}=0$. Both hold only when $\lambda=0$ and $\vec v=0$.

**Remark (the contrast with the plane).** On the spinor plane the opposite happens: every element is norm-degenerate and the spectral-degenerate locus is the origin alone, so the two loci coincide in one point of a plane that is entirely in the first of them. On the closure of the vector part the two loci are a cone and a line, and they meet in one point without one containing the other. On the centre they are the whole centre and the origin, and the second is contained in the first.

**Remark (the four combinations inside the closure).** The closure contains elements of three of the four sectors. The elements with a nonzero vector part off the null cone are in $\Sigma_{11}$; the elements of the line away from the origin are in $\Sigma_{10}$; the elements of the null cone with a nonzero vector part are in $\Sigma_{01}$; and the origin is the only element of $\Sigma_{00}$. So the closure is a space in which all four sectors are represented, which is not true of any of the three carriers.

## The Partner Half

**The Hermitian half.** The other half with the same shape is $\mathbb{B}_{\Psi}=\mathbb{R}e_t\oplus i\mathfrak{k}$, with elements $\lambda+i\vec v$ for real $\lambda$ and $\vec v$. Its square of the vector part is

$$
B^{2}(\lambda+i\vec v)=-\lvert\vec v\rvert^{2},
$$

and its two eigenvalues are $\lambda\pm\lvert\vec v\rvert$, real and symmetric about $\lambda$.

**Remark (the predicate is the same and the spectrum is not).** The degenerate locus is the same line, $\mathbb{R}e_t$ in that half, since the criterion is again the vanishing of the vector part. What changes is the location of the spectrum: imaginary on the anti-Hermitian half and real on the Hermitian half. The predicate is decided by $B^{2}$ and not by where the eigenvalues lie, and the two halves are the cleanest illustration of that difference.

## The Three Carriers Compared

| carrier | $B^{2}$ on it | spectrally degenerate locus in it |
| --- | --- | --- |
| centre $\mathbb{C}e_t$ | $0$ | the whole centre |
| spinor plane $\Sigma$ | $-\lambda^{2}/4$ | $\{0\}$ |
| vector part $\mathfrak{k}$ | $\lvert\vec v\rvert^{2}$ | $\{0\}$ |

**The pattern of the three.** With the two predicates read together, the three carriers occupy three different sectors away from the origin: the centre is in $\Sigma_{10}$, the plane in $\Sigma_{01}$, and the vector part in $\Sigma_{11}$. No carrier away from the origin is in $\Sigma_{00}$, and each carrier is entirely inside one sector. The three subsections of the spin geometry are therefore the three sectors, and the fourth is empty of carriers.

**Why the vector part is the last one.** The sequence of the three carriers, from the line through the plane to the vector part, is the sequence in which the two predicates are repaired one at a time. The line has the norm and loses the spectrum; the plane has the spectrum and loses the norm; the vector part has both. That is the content of the three articles on regularity taken together.

## Summary

On the anti-Hermitian closure the square of the vector part is $\lvert\vec v\rvert^{2}$, a non-negative real number, so the degenerate locus of the closure is the line $\mathbb{R}(ie_t)$ and the spectrum of $i\lambda+\vec v$ is the purely imaginary pair $i(\lambda\pm\lvert\vec v\rvert)$. On the carrier the spectrum is $\pm i\lvert\vec v\rvert$, distinct for every nonzero $\vec v$, so the carrier is spectrally regular away from the origin and avoids the degenerate cone entirely. On the closure the degenerate cone and the null cone are disjoint except at the origin, and the closure meets all four sectors while no carrier meets more than one.

## The Boxed Summary

| the point | in plain words |
| --- | --- |
| the question | Spectral regularity asks whether the square of the vector part is nonzero, which is the same as asking whether the two eigenvalues differ. |
| the quantity on the closure | The square of the vector length, a real number that is never negative. |
| what vanishes there | The line along the imaginary identity, and the whole of it. |
| the spectrum of the closure | Purely imaginary: the scalar coordinate plus and minus the vector length. |
| the spectrum of the carrier | Plus and minus the imaginary vector length, distinct for every nonzero vector. |
| the answer on the carrier | Spectrally regular everywhere except at the origin, and it avoids the degenerate locus entirely. |
| the two loci | On the closure the degenerate locus and the null cone meet only at the origin. |
| the moral | The closure meets all four sectors, while no individual carrier meets more than one. |

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
| $\mathbb{B}_{\Phi}=\mathbb{R}(ie_t)\oplus\mathfrak{k}$ | the anti-Hermitian subspace, the closure |
| $\mathfrak{k}$ | the vector part, the carrier |
| $\lvert\vec v\rvert^{2}=v_x^{2}+v_y^{2}+v_z^{2}$ | the positive definite form on the triple |
| $\mathbb{B}_{\Psi}=\mathbb{R}e_t\oplus i\mathfrak{k}$ | the Hermitian partner half |
| $\Sigma_{ij}$ | the sector with $N\neq0$ for $i=1$ and $B^{2}\neq0$ for $j=1$ |

## Further Reading

- [Introduction to the Spin-One Anti-Hermitian Subspace](the-spin-one-anti-hermitian-subspace.html), for the carrier, the closure and the action on it
- [The Spin-One Anti-Hermitian Subspace and N Norm Regularity](the-spin-one-anti-hermitian-subspace-and-n-norm-regularity.html), for the other predicate on the same space
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the definitions of the two predicates and the four sectors
- [The Spectrum](the-spectrum-of-a-biquaternion.html), for the two eigenvalues of an element and the quadratic relation
- [The N-Regular, Spectrally Regular Sector](the-n-regular-spectrally-regular-sector.html), for the sector in which the carrier away from the origin lies
- [The N-Degenerate, Spectrally Regular Sector](the-n-degenerate-spectrally-regular-sector.html), for the sector containing the null cone of the closure
- [From the Spin to the Carriers and the Closures](the-carriers-the-representation-the-spin-and-the-closure.html), for the three carriers taken together
