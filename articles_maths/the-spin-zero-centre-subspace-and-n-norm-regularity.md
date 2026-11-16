# __The Spin-Zero Centre Subspace and N Norm Regularity__

## Introduction

The spin-zero carrier is the real line $\mathbb{R}e_t$, and its closure is the centre $\mathbb{C}e_t$. This article computes the $N$ norm on the closure and reads the first of the two predicates off it.

The answer is the extreme one, and it is the opposite of the answer for the spin-half carrier. On the centre the norm is the square of the complex coordinate, so it vanishes at the origin alone. Every nonzero element of the centre is norm-regular. The centre is a copy of the complex field inside the algebra, no nonzero element of it is a zero divisor, and the null cone meets it in one point.

The article then separates two statements that the single formula hides. The complex norm is nondegenerate on the centre, in the sense that only the origin is null. Its real part is not: read as a real quadratic form on the real plane, the real part is indefinite, of signature $(1,1)$, and it has two isotropic lines. The lines are $\mathbb{R}(e_t+ie_t)$ and $\mathbb{R}(e_t-ie_t)$, and on each of them the complex norm is $\pm2i$ and not zero. A reader who reports from the real part alone that the centre is isotropic has reported a fact about one of the two real forms and not about the norm.

The companion article is *The Spin-Zero Centre Subspace and Spectral Regularity*, where the second predicate is computed and the answer is the extreme one in the other direction. The subspace itself is *Introduction to the Spin-Zero Centre Subspace*. The norm and the predicate are defined in *Relations between the N Norm and Spectral Regularity and Degeneracy*.

Nothing below is a statement of physics. The algebra $\mathbb{B}$ is real, of dimension $8$, with units $e_t,\vec e_x,\vec e_y,\vec e_z$, $e_t$ the identity and $\vec e_k^{2}=-e_t$, and with $i$ an element commuting with the units and $i^2=-e_t$. An element is $\tilde Q=Q_te_t+\vec Q$ with $Q_\mu=q_\mu+iq'_\mu$ complex and $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ a complex combination of the pure units.

## The Norm and the Predicate

**Definition (the $N$ norm).** For $\tilde Q=Q_te_t+\vec Q$ put

$$
N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}.
$$

It is a complex-valued quadratic form. It is multiplicative, $N(XY)=N(X)N(Y)$, and it vanishes exactly on the elements without an inverse. Both properties are proved in *N-Regularity and N-Degeneracy in the Biquaternion Algebra* and are used here without proof.

**Definition (the predicate).** An element is **norm-regular** when $N(\tilde Q)\neq0$ and **norm-degenerate** when $N(\tilde Q)=0$. The zero locus is the **null cone** $\mathcal N=\{N=0\}$.

## The Norm on the Centre

**Theorem (the formula).** For $\lambda\in\mathbb{C}$,

$$
N(\lambda e_t)=\lambda^{2}.
$$

*Proof.* The coordinates of $\lambda e_t$ are $Q_t=\lambda$ and $\vec Q=0$, so all three of $Q_x,Q_y,Q_z$ vanish and $N=Q_t^{2}=\lambda^{2}$.

**Corollary (the null cone meets the centre at the origin).** On the centre,

$$
\{X\in\mathbb{C}e_t:N(X)=0\}=\{0\}.
$$

*Proof.* The square $\lambda^{2}$ vanishes if and only if $\lambda$ vanishes, and the complex field has no other zero.

**Corollary (every nonzero element of the centre is norm-regular and invertible).** The inverse is $\lambda^{-1}e_t$, and

$$
N\bigl(\lambda^{-1}e_t\bigr)=\lambda^{-2},\qquad N(\lambda e_t)\,N\bigl(\lambda^{-1}e_t\bigr)=1 .
$$

So the centre is closed under inversion, it contains no zero divisor, and it is a copy of the complex field sitting inside $\mathbb{B}$.

## The Two Real Forms

**The real and the imaginary part.** Write $\lambda=a+ib$ with real $a$ and $b$. Then

$$
N(\lambda e_t)=(a^{2}-b^{2})+2iab .
$$

The display is two real quadratic forms on the real plane of the centre, and they behave differently.

**The real part is indefinite.** The form $a^{2}-b^{2}$ has signature $(1,1)$: it is positive on the line $b=0$, negative on the line $a=0$, and it has two isotropic lines, $a=b$ and $a=-b$. In the algebra the two lines are

$$
\mathcal I_{\pm}=\mathbb{R}\bigl(e_t\pm ie_t\bigr),
$$

each of real dimension $1$.

**The norm is not zero on the isotropic lines.** On those lines

$$
N\bigl(e_t+ie_t\bigr)=2i,\qquad N\bigl(e_t-ie_t\bigr)=-2i .
$$

So the isotropic lines of the real part are not null for the norm. The two statements are about different objects: the first is about one real form, the second about the complex form.

**The imaginary part.** The form $2ab$ vanishes on the two coordinate lines $\mathbb{R}e_t$ and $\mathbb{R}(ie_t)$ and is indefinite on the same plane, of signature $(1,1)$. It too has two isotropic lines, the same pair, since $2ab$ and $a^{2}-b^{2}$ vanish together on $a=\pm b$ and nowhere else together.

**Remark (the two forms are one object).** The complex norm is the pair of the two real forms, and its null cone is the intersection of the two zero loci. That intersection is the origin, which is the statement of the corollary above. Neither real form alone carries it: each has a line of zeros, and the two lines coincide.

**Remark (why the lines are not idempotents).** A negligible remark, included because the elements $e_t\pm ie_t$ invite the comparison. The idempotents of the algebra are $\tfrac12(e_t\pm i\vec u_{\mathrm r})$ at a unit real axis $\vec u_{\mathrm r}$, and the axis is pure. The element $e_t$ is central and not pure, so $e_t\pm ie_t$ is not of that shape and is not idempotent. Its square is

$$
\bigl(e_t+ie_t\bigr)^{2}=2ie_t ,
$$

which is neither the element nor zero.

## The Polar Form

**Definition (the polar form).** For two elements put

$$
B(X,Y)=\tfrac12\bigl(N(X+Y)-N(X)-N(Y)\bigr)=\sum_\mu Q_\mu(X)Q_\mu(Y),
$$

a symmetric complex-bilinear form, the polar form of $N$.

**Proposition (the polar form on the centre).** For complex $\lambda$ and $\mu$,

$$
B(\lambda e_t,\mu e_t)=\lambda\mu ,
$$

and the form is nondegenerate there: if $B(\lambda e_t,\mu e_t)=0$ for every $\mu$ then $\lambda=0$.

*Proof.* The first display is the definition with $\vec Q=0$ at both arguments. For the second, take $\mu=1$.

**Remark (the form is complex-bilinear and not Hermitian).** The polar form is linear in each argument over $\mathbb{C}$, so $B(iX,iY)=-B(X,Y)$. A reader who expects the sesquilinear habit will read the display $B(\lambda e_t,\lambda e_t)=\lambda^{2}$ as a squared modulus, and it is not one.

## The Centre Against the Other Carriers

| carrier | norm on it | null locus in it |
| --- | --- | --- |
| centre $\mathbb{C}e_t$ | $\lambda^{2}$ | $\{0\}$ |
| spinor plane $\Sigma$ | $0$ | the whole plane |
| vector part $\mathfrak{k}$ | $\lvert\vec v\rvert^{2}$ | $\{0\}$ |

**The two extremes.** The centre and the plane are the two extremes of the group, and the vector part sits at neither. On the centre the norm separates points; on the plane it separates nothing; on the vector part it separates points and is moreover positive, so the whole of the vector part away from the origin is norm-regular.

**The reason for the contrast.** The norm of an element is the sum of the squares of its four coordinates. On the centre three of the four vanish, so one square remains and it is the square of the coordinate. On the plane the four squares cancel against one another exactly, because the plane is built from an idempotent of norm zero. The cancellation is the subject of *The Spin-Half Bispinors and N Norm Regularity*.

## Summary

The norm on the centre is $N(\lambda e_t)=\lambda^{2}$. Its null locus in the centre is the origin alone, so every nonzero element of the centre is norm-regular and invertible, and the centre is a copy of the complex field inside the algebra. The real part of the norm is an indefinite form of signature $(1,1)$ with the two isotropic lines $\mathbb{R}(e_t\pm ie_t)$, and on those lines the norm itself is $\pm2i$ and not zero. The polar form is $\lambda\mu$, complex-bilinear and nondegenerate. Against the other two carriers the centre is the case in which the norm separates, and the plane is the case in which it does not.

## The Boxed Summary

| the point | in plain words |
| --- | --- |
| the carrier | The carrier of spin zero is the real line along the identity, and its closure is the centre, a copy of the complex numbers inside the algebra. |
| the norm on it | The norm of a central element is the square of its complex coordinate. |
| what vanishes | Only the zero element. No other central element has a vanishing norm. |
| the answer | Every central element except zero is norm-regular, and its inverse is central again. |
| the consequence | The centre contains no zero divisor, and the null cone meets it in a single point. |
| the trap | The real part of the norm is not the norm. Read on the real plane it is indefinite, of signature (1,1), with two isotropic lines. |
| why that is no contradiction | On the two lines the norm itself is not zero, so the centre is not isotropic. |
| the polar form | It is the product of the two coordinates, and it is nondegenerate. |
| against the other carriers | The norm separates points on the centre and on the vector part, and it separates nothing on the spin-half plane. |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, real, of dimension $8$ |
| $e_t$ | the identity of the algebra |
| $i$ | the complex unit, an element of $\mathbb{B}$ |
| $\tilde Q=Q_te_t+\vec Q$ | an element, with $Q_\mu$ complex |
| $N(\tilde Q)=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the $N$ norm, complex-valued and multiplicative |
| $\mathcal N=\{N=0\}$ | the null cone |
| norm-regular | $N\neq0$ |
| $\mathbb{C}e_t$ | the centre, the closure of the carrier, $\dim_\mathbb{R}=2$ |
| $\mathbb{R}$-line $\mathbb{R}(e_t\pm ie_t)$ | the isotropic lines of the real part |
| $B(X,Y)=\tfrac12\bigl(N(X+Y)-N(X)-N(Y)\bigr)$ | the polar form of the norm |
| $\mathfrak{k}$ | the vector part, the spin-one carrier |
| $\Sigma$ | the spinor plane, the spin-half carrier |

## Further Reading

- [Introduction to the Spin-Zero Centre Subspace](the-spin-zero-centre-subspace.html), for the line, the closure and the action on it
- [The Spin-Zero Centre Subspace and Spectral Regularity](the-spin-zero-centre-subspace-and-spectral-regularity.html), for the other predicate on the same space
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm, its multiplicativity and its zero locus
- [Relations between the N Norm and Spectral Regularity and Degeneracy](relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the definitions of the two predicates and the four sectors
- [The N-Regular Sector](the-n-regular-sector.html), for the open set on which the norm does not vanish
- [Centre, Units, Zero Divisors and Division Algebras](centre-units-zero-divisors-and-division-algebras.html), for the centre as a division algebra inside the algebra
- [From the Spin to the Carriers and the Closures](the-carriers-the-representation-the-spin-and-the-closure.html), for the three carriers taken together
