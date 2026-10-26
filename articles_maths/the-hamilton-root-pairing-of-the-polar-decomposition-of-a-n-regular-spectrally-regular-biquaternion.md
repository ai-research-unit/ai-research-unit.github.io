# __The Hamilton Root Pairing of the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion__

## Introduction

Throughout this article $\tilde Q$ lies in the N-regular, spectrally regular sector $\Sigma_{11}$, so $N\neq0$ and $B^2\neq0$. The sector condition is the domain on which the eigenbasis and the companion constructions are those of the regular case; the wall $B^2=0$ is treated in the companion article of the same title with *Spectrally Degenerate*.

Every element of $\Sigma_{11}$ is the ordered product of a positive real scale, a central phase and two unit factors,

$$
\tilde{Q} = r\,\exp(i\alpha)\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
= r\,\exp(i\alpha)\,\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr)\,\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr) .
$$

The four factors are those of *The Polar Decomposition of a N-Regular Biquaternion*, §*The Four Factors*, and their exponential forms those of *Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion*, §*The Decomposition*: the scale $r>0$, the central phase $\exp(i\alpha)$ with $\alpha\in(-\pi/2,\pi/2]$, the Hermitian positive boost $\tilde U_{\mathrm b}$ of rapidity $\psi\ge0$ and the unit real rotor $\tilde u_{\mathrm r}$ of angle $\theta\in[0,2\pi]$. They are unique, so they can be grouped in pairs in exactly three ways. This article reads the grouping that puts the scale with the phase.

**The Hamilton root pairing** is the grouping that multiplies the scale into the phase and the boost into the rotor. The two central factors multiply into the complex modulus $\Rho = r\exp(i\alpha)$; the two unit factors multiply into the non-central factor $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, the Lorentz transformation of the word. On the domain of the pairing that product is a single exponential $\exp(\vec U\Theta)$ of a **root** of $-e_t$. Write $\tilde Q = Q_te_t+\vec Q$ in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec Q = Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The axis $\vec U$ is the root proportional to $\vec Q$, normalised by $\vec U^2 = -e_t$, and $\Theta$ is the complex angle of the exponential, fixed by $\cos\Theta = Q_t/\Rho$ and $\sin\Theta = B/\Rho$, where $B^2 = \langle\vec Q,\vec Q\rangle_{\natural} = Q_x^2+Q_y^2+Q_z^2$.

$$
\tilde{Q} = \Rho\,\exp(\vec U\Theta), \qquad \Rho = r\,\exp(i\alpha), \qquad \exp(\vec U\Theta) = \tilde U_{\mathrm b}\,\tilde u_{\mathrm r}.
$$

This is the **Hamilton representation** of the biquaternion literature. The name records the axis: $\vec U$ is a root of $-e_t$, and $\vec\Xi=-i\vec U$ is the pure root of $+1$ that *The Biquaternion Eigenvalue Decomposition*, §*The Eigenprojectors*, attaches to it. The two halves of the article read the same word at these two roots. The basis in which that root diagonalises left multiplication — the eigenbasis, with its two nilpotents — carries the four basis elements and the two spinor spaces; §*The Eigenbasis and the Spinor Spaces* fixes the vocabulary used throughout.

The pairing is **partial**: its second factor is a single exponential only where the axis $\vec U=\vec Q/B$ is defined, which requires the vector part to be non-null. It is partial in both the factorisation and the construction, unlike the quaternion pairing, which is partial in the construction only. There are two partial pairings: this one, and the quaternion pairing, in which the scale is grouped with the rotor; the third grouping, in which the scale is grouped with the boost and the phase with the rotor, is not partial and is *The Cartan Hermitian Pairing of the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion*.

**The approach.** The article follows the skeleton shared by the three pairing articles: the results imported, the pairing and its two factors, existence and domain, the comparison of the three bracketings, and the three conjugations. It inserts, between the two factors and the existence theorem, the eigenbasis and the two spinor spaces, where the Hamilton data are the diagonal values. It adds a second half, the **root reading**, which reads the same word at the roots of one and collects the four-factor form, the two-exponent form, the single exponential and the idempotent exponential in one table. The first half is the Hamilton representation itself; the second is the same representation at the elements where the non-central factors close. The two halves are related by $\vec\Xi=-i\vec U$: multiplying the axis by $-i$ gives the pure root of $+1$ attached to the element. The four factors are taken from *The Polar Decomposition of a N-Regular Biquaternion*, and the exponential and the logarithm from *Biquaternion Elementary Functions*; the imported proofs are cited rather than repeated. No physics is invoked.

**The result.** On the complement of the null cone and of the quadric cone $\langle\vec Q,\vec Q\rangle_{\natural}=0$, the element factors as $\Rho\exp(\vec U\Theta)$, with $\Rho$ the complex modulus, $\vec U=\vec Q/B$ the root of $-1$ parallel to the vector part and $\Theta$ the complex angle. The pairing is collected in the table.

| item | the Hamilton pairing |
|---|---|
| grouping | the scale with the phase, the boost with the rotor |
| first factor | $\Rho=r\exp(i\alpha)=\sqrt{\langle\tilde Q\rangle_{\natural}}$, a complex scalar |
| second factor | $\exp(\vec U\Theta)=\tilde U_{\mathrm b}\tilde u_{\mathrm r}=\tilde Q/\Rho$, a unit element |
| equation | $\tilde Q=\Rho\exp(\vec U\Theta)$ |
| axis | $\vec U=\vec Q/B$, $B^{2}=\langle\vec Q,\vec Q\rangle_{\natural}$, $\vec U^{2}=-e_t$ |
| angle | $\cos\Theta=Q_t/\Rho$, $\sin\Theta=B/\Rho$ |
| domain | $\langle\tilde Q\rangle_{\natural}\neq0$ and $\langle\vec Q,\vec Q\rangle_{\natural}\neq0$ |
| classical limit | the quaternion polar form for a real quaternion |
| position among the three | the only central first factor and the only unit second factor |

The second half reads the same word at the roots of one, where it closes; the roots of one carry a second exponential form, a single exponential of the halving idempotent, and the two forms are tied by the product of the last two factors. The two exponents of the non-central factors, $i\frac{\psi}{2}\vec u_{\mathrm b}$ and $\frac{\theta}{2}\vec u_{\mathrm r}$, are one Hermitian and one real pure element; they do not commute in general, and the exponent of the single exponential is their sum exactly when the axes are parallel or one factor is central.

## The Results Used

The article takes the following results as established and does not prove them again.

| result | established in | used here for |
|---|---|---|
| the four factors, their ranges and their order | *The Polar Decomposition of a N-Regular Biquaternion*, §*The Four Factors* | the word that is bracketed |
| existence and uniqueness of the word on $\langle\tilde Q\rangle_{\natural}\neq0$ | *Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion*, §*Existence and Uniqueness* | the factorisation $\tilde Q=\Rho\exp(\vec U\Theta)$ and the uniqueness of the regrouping |
| the eigenvalues, the axis, the pure root and the eigenprojections | *The Spectrum*, §*The Spectral Criterion*, and *The Biquaternion Eigenvalue Decomposition*, §*The Eigenprojectors* | the modulus $\Rho$, the axis $\vec U=\vec Q/B$, the root $\vec\Xi$ and $\lambda_\pm=\Rho\exp(\pm i\Theta)$ |
| the closed forms of the exponential and the logarithm | *Biquaternion Elementary Functions*, §*The Closed Form* and §*The Eigenvalue Formula* | the exponential $\exp(\tilde Q)$ and the logarithm of the second factor |
| the roots of one and their idempotents | *Idempotents*, §*The Roots of One* and §*The Two Idempotents of a Root* | the second half |
| the eigenbasis, its nilpotents and the spinor spaces | *The Peirce Decomposition*, §*The Peirce Decompositions*, and *The N-Regular, Spectrally Regular Sector*, §*The Eigenbasis, the Nilpotents, and the Peirce Corners* and §*The Spinor Spaces and their Coordinates* | the eigenbasis, the diagonal action and the spinor spaces of §*The Eigenbasis and the Spinor Spaces* |
| the hyperbolic form of a non-trivial root | *Idempotents*, §*The Non-Hermitian Roots*, and §*The Root From Its Coordinates* of this article | the two directions and the rapidity of §*The Two Pure Elements* |
| the idempotent exponential form and the extraction $-i\tilde\Xi$ | §*The Idempotent Exponential Form* and §*The Bridge Between the Two Forms* of this article, on the halving map of *Idempotents*, §*The Correspondence with the Roots of One* | §*The Idempotent Exponential Form* and §*The Bridge Between the Two Forms* |
| the Peirce decomposition | *The Peirce Decomposition*, §*The Peirce Decompositions* | the idempotents and the four corners |
| the polar decomposition of the ordinary quaternions | *Modulus–Unit Polar Decomposition of Quaternions*, §*The Two Factors* | the classical limit |

The classification, the hyperbolic form, the idempotent exponential and the bridge are cited, not re-proved. The article adds three things: the placement of the Hamilton data in the eigenbasis and the two spinor spaces, in §*The Eigenbasis and the Spinor Spaces*; the reading of a root on the two exponents of the word and the bracket that forbids their sum, in §*The Two Exponents*; and the single exponential of the whole domain with its Baker–Campbell–Hausdorff gap, in §*The Single Exponential*.

## The Pairing

### The Definition

The Hamilton representation is the pairing of the scale with the phase against the boost with the rotor:

$$
\tilde{Q} = \Rho\,\exp(\vec U\Theta), \qquad \Rho = r\,\exp(i\alpha) = \sqrt{\langle\tilde Q\rangle_{\natural}}, \qquad \exp(\vec U\Theta) = \tilde U_{\mathrm b}\,\tilde u_{\mathrm r} .
$$

The modulus is the complex scalar $\Rho$ of the polar decomposition, and the exponential is the whole rotor part, boost and rotation together. The identification of $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with a single exponential is the content of the construction of *The Polar Decomposition of a N-Regular Biquaternion*, and it is why the Hamilton representation generalises the quaternion polar decomposition: when all four coefficients are real, $\tilde U_{\mathrm b} = e_t$, $\tilde u_{\mathrm r}$ is the unit quaternion, and the representation reduces to $\tilde Q = r\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ term by term.

Both non-central factors of the polar word are themselves exponentials of a single element, so the Hamilton factor is the single exponential of a **product of two exponentials**: the boost is $\tilde U_{\mathrm b}=\exp(i\frac{\psi}{2}\vec u_{\mathrm b})$ and the rotor is $\tilde u_{\mathrm r}=\exp(\frac{\theta}{2}\vec u_{\mathrm r})$, with the closed forms of §*The Decomposition* of *Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion*. Each exponent is a parameter times a root of $\pm e_t$: $i\vec u_{\mathrm b}$ is a Hermitian root of $+e_t$ and $\vec u_{\mathrm r}$ a real pure root of $-e_t$. Their product is again a single exponential because it has unit norm, and on the domain of the representation its angle and axis are read from the element as the complex $\Theta$ and the root $\vec U$; on aligned words $\Theta=\frac{\theta}{2}+\epsilon i\frac{\psi}{2}$, while in general the two parameters do not separate. The exponent of that single exponential is a complex multiple $\Theta\vec U$ of a root of $-e_t$, and it is the sum $i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}$ of the two exponents of the factors exactly when the two axes are parallel or one of the two factors is central, as the second half shows.

### The Statement

**Theorem (the representation).** Let $\tilde Q=Q_te_t+\vec Q$ with $\langle\tilde Q\rangle_{\natural}\neq0$ and $\langle\vec Q,\vec Q\rangle_{\natural}\neq0$, and put

$$
\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}},\qquad B=\sqrt{\langle\vec Q,\vec Q\rangle_{\natural}},\qquad \vec U=\frac{\vec Q}{B},\qquad \cos\Theta=\frac{Q_t}{\Rho},\qquad \sin\Theta=\frac{B}{\Rho}.
$$

Then $\tilde Q=\Rho(\cos\Theta+\vec U\sin\Theta)$.

The axis and the eigenvalues are those of *The Spectrum*, §*The Spectral Criterion*: $\vec U^2=-e_t$, $\lambda_\pm=Q_t\pm iB$, and the definitions above are the polar form $\lambda_\pm=\Rho\exp(\pm i\Theta)$ of the spectrum. The branch of $\Rho$ is fixed by the polar word and the branch of $B$ by the choice of $\vec U$; the replacement $B\mapsto-B$ exchanges the two eigenvalues and the two eigenprojections, which is the label ambiguity of §*The Spectral Decomposition* of that article.

**The axis.** The normalisation $\vec U^2=-e_t$ is what $B=\sqrt{\langle\vec Q,\vec Q\rangle_{\natural}}$ provides. The axis is not an arbitrary root of $-1$ but the one parallel to the vector part, and that parallelism is what makes the representation canonical. When the vector part is null, $B=0$ and the axis does not exist; that is the domain restriction below.

### The Exponential of the Element

The representation is a statement about $\tilde Q$ itself, not about its exponential. The exponential is the closed form of *Biquaternion Elementary Functions*, §*The Closed Form*: for $\tilde Q=Q_te_t+B\vec U$ with $\vec U^2=-e_t$,

$$
\exp(\tilde Q)=\exp(Q_t)\bigl(\cos B\,e_t+\sin B\,\vec U\bigr),
$$

and it is not re-derived here. Its data $(\exp(Q_t),B)$ coincide with the Hamilton data $(\Rho,\Theta)$ only when $\langle\tilde Q\rangle_{\natural}=\exp(2Q_t)$ and $\Theta=B$; in general it is the logarithm, not the exponential, that recovers $(\Rho,\Theta)$ from the element (*Biquaternion Elementary Functions*, §*The Logarithm*). The distinction matters whenever an element and its exponential are both in play, as for the exponential map of $\mathbb{B}^{\times}$ in *Biquaternion Lie Group and Exponential Structure*.

## The First Factor: The Complex Modulus

The first factor is the complex modulus of the polar decomposition,

$$
\Rho = r\exp(i\alpha) = \sqrt{\langle\tilde Q\rangle_{\natural}},
\qquad r>0,\quad \alpha\in(-\pi/2,\pi/2] .
$$

It is central, so it commutes with the second factor, and it carries the whole norm, $\langle\Rho\rangle_{\natural}=\Rho^{2}$. The principal branch of the square root is the one of the polar word, so the modulus is unique; its two constituents are the scale $r$ and the phase $\exp(i\alpha)$.

The modulus is the eigenvalue data of *The Spectrum*, §*The Spectral Criterion*: it is the common modulus of $\lambda_\pm=\Rho\exp(\pm i\Theta)$ read in §*The Statement*, so that $\lambda_+\lambda_-=\Rho^{2}$. The article uses that identification and does not re-derive the eigenvalue decomposition.

| aspect | value |
|---|---|
| formula | $\Rho=r\exp(i\alpha)=\sqrt{\langle\tilde Q\rangle_{\natural}}$ |
| kind | complex scalar, central |
| modulus | $\lvert\Rho\rvert=r$, $\Rho^{2}=r^{2}\exp(2i\alpha)$ |
| eigenvalue reading | $\lambda_\pm=\Rho\exp(\pm i\Theta)$ |
| conjugation | $\Rho^{\natural}=\Rho$, $\overline{\Rho}=\Rho^{*}$ |
| role | the first factor, the only central first factor of the three |

## The Second Factor: The Lorentz Transformation

The second factor is the whole non-central part of the polar word, the boost and the rotor multiplied,

$$
\tilde U_{\mathrm L} = \tilde U_{\mathrm b}\,\tilde u_{\mathrm r} = \exp(\vec U\Theta) = \frac{\tilde{Q}}{\Rho} ,
\qquad \tilde U_{\mathrm L}\,\tilde U_{\mathrm L}^{\natural} = e_t .
$$

It is a boost of rapidity $\psi$ about $\vec u_{\mathrm b}$ times a rotation of angle $\theta$ about $\vec u_{\mathrm r}$; the boost alone is the Hermitian case $\tilde u_{\mathrm r}=e_t$. In the physical interpretation $\tilde U_{\mathrm L}$ is the **Lorentz transformation**: the modulus $\Rho$ carries the scale and the phase, so every element of the domain is a complex scalar times a Lorentz transformation. The rotor of the dagger sandwich of the physics articles is this factor, written $\tilde U$ there.

| aspect | value |
|---|---|
| formula | $\tilde U_{\mathrm L}=\tilde U_{\mathrm b}\tilde u_{\mathrm r}=\exp(\vec U\Theta)=\tilde Q/\Rho$ |
| kind | unit-norm element, the Lorentz transformation |
| norm | $\tilde U_{\mathrm L}\tilde U_{\mathrm L}^{\natural}=e_t$ |
| constituents | the boost of rapidity $\psi$ about $\vec u_{\mathrm b}$ and the rotor of angle $\theta$ about $\vec u_{\mathrm r}$ |
| exponent | $\Theta\vec U$, a complex multiple of a root of $-e_t$ |
| role | the second factor, the whole non-central part of the word |

The factor is a single exponential on the whole domain, but its exponent is not the sum of the two exponents of the factors. That is the subject of the second half.

## The Eigenbasis and the Spinor Spaces

**The basis.** The Hamilton data are the eigenvalue data of *The Biquaternion Eigenvalue Decomposition*, §*The Eigenprojectors*, read in the eigenbasis of *The N-Regular, Spectrally Regular Sector*, §*The Eigenbasis, the Nilpotents, and the Peirce Corners*. The pure root of $+1$ attached to the axis is $\vec\Xi=-i\vec U$, the eigenprojections are $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$, and the two mixed Peirce corners are the complex lines spanned by the nilpotents $\vec\Upsilon_+\in\mathbb{B}_{-+}$ and $\vec\Upsilon_-\in\mathbb{B}_{+-}$, normalised by

$$
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad \vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad \vec\Upsilon_\pm^2=0 .
$$

The four elements $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ form a $\mathbb{C}$-basis of $\mathbb{B}$, the **eigenbasis**.

**The diagonal action.** In that basis left multiplication by $\tilde Q$ is diagonal,

$$
\tilde Q\tilde\Pi_+=\lambda_+\tilde\Pi_+ ,\qquad
\tilde Q\vec\Upsilon_-=\lambda_+\vec\Upsilon_- ,\qquad
\tilde Q\vec\Upsilon_+=\lambda_-\vec\Upsilon_+ ,\qquad
\tilde Q\tilde\Pi_-=\lambda_-\tilde\Pi_- ,
$$

with $\lambda_\pm=\Rho\exp(\pm i\Theta)$. The basis is therefore an eigenbasis of the operator $L_{\tilde Q}$, with the eigenvalues $(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$. The second factor of the pairing is the same operator stripped of the modulus: since $\Rho$ is central, $L_{\tilde U_{\mathrm L}}=\Rho^{-1}L_{\tilde Q}$ is diagonal in the same basis, with the values $(\exp(i\Theta),\exp(i\Theta),\exp(-i\Theta),\exp(-i\Theta))$. The Hamilton modulus is thus the common factor of the two eigenvalues, $\lambda_\pm=\Rho\exp(\pm i\Theta)$, of $L_{\tilde Q}$, and the Hamilton angle is half the difference of their logarithms: the pairing is the polar form of the spectrum.

**The two spinor spaces.** The two minimal left ideals

$$
S_+=\mathbb{B}\tilde\Pi_+=\mathbb{C}\tilde\Pi_+\oplus\mathbb{C}\vec\Upsilon_+ ,\qquad
S_-=\mathbb{B}\tilde\Pi_-=\mathbb{C}\vec\Upsilon_-\oplus\mathbb{C}\tilde\Pi_-
$$

are the two **spinor spaces**, and $\mathbb{B}=S_+\oplus S_-$ (*The N-Regular, Spectrally Regular Sector*, §*The Spinor Spaces and their Coordinates*). Each carries both eigenvalues, with eigenbasis $(\tilde\Pi_+,\vec\Upsilon_+)$ on $S_+$ and $(\vec\Upsilon_-,\tilde\Pi_-)$ on $S_-$; the two eigenvalues are distinct there, so the eigenbasis of each space is unique up to a rescaling of each vector. A general element is not a spinor: it has one component in $S_+$ and one in $S_-$.

**The matrix model.** With the assignment

$$
\mathsf M_2^Q(\tilde\Pi_+)=E_{11},\quad
\mathsf M_2^Q(\vec\Upsilon_-)=E_{12},\quad
\mathsf M_2^Q(\vec\Upsilon_+)=E_{21},\quad
\mathsf M_2^Q(\tilde\Pi_-)=E_{22},
$$

the two spinor spaces are the two columns, and

$$
\mathsf M_2^Q(\tilde Q)=\operatorname{diag}(\lambda_+,\lambda_-),\qquad
\mathsf M_2^Q(\tilde U_{\mathrm L})=\operatorname{diag}\bigl(\exp(i\Theta),\exp(-i\Theta)\bigr).
$$

Both columns are acted on by the same diagonal matrix, which is the matrix form of the statement that $L_{\tilde Q}$ preserves each left ideal and has the same spectrum on each. The pairing of this article is the scalar reading of that diagonal.

## Existence, Uniqueness and the Domain

### The Theorem

**Theorem (the Hamilton pairing).** Let $\tilde Q\in\mathbb{B}$ with $\langle\tilde Q\rangle_{\natural}\neq0$ and $\langle\vec Q,\vec Q\rangle_{\natural}\neq0$. Then $\tilde Q=\Rho(\cos\Theta+\vec U\sin\Theta)$ with $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}$, $B=\sqrt{\langle\vec Q,\vec Q\rangle_{\natural}}$, $\vec U=\vec Q/B$, $\cos\Theta=Q_t/\Rho$ and $\sin\Theta=B/\Rho$. The factors are unique once the branches of $\Rho$ and $B$ are fixed.

The factorisation exists whenever the four-factor word exists and the vector part is non-null, because the axis $\vec U=\vec Q/B$ must be defined. The existence of the four factors needs no separate argument; the single exponential is the construction of *The Polar Decomposition of a N-Regular Biquaternion*, §*The Hamilton root pairing*. What the pairing adds is the reading of the two factors as a complex modulus and a single exponential.

### Uniqueness and the Branch Choices

The representation is unique once two branch choices are fixed. The parameters $(\Rho,B,\vec U,\Theta)$ are not independent: $B$ is a square root of $\langle\vec Q,\vec Q\rangle_{\natural}$, $\Rho$ a square root of the norm, $\vec U=\vec Q/B$, and the angle solves $\cos\Theta=Q_t/\Rho$ and $\sin\Theta=B/\Rho$. The two square-root branches act as follows.

| branch | replacement | compensating change | effect on $\tilde Q$ |
|---|---|---|---|
| $\Rho$ | $\Rho\mapsto-\Rho$ | $\Theta\mapsto\Theta+\pi$ | none: $\cos\Theta$ and $\sin\Theta$ both change sign |
| $B$ | $B\mapsto-B$ | $\vec U\mapsto-\vec U$, $\Theta\mapsto-\Theta$ | none: $B\vec U$ and $\vec U\sin\Theta$ are unchanged |
| $\Theta$ | $\Theta\mapsto\Theta+2\pi k$ | none | none |

The first two rows are the branch ambiguities of the two square roots; the third is the period of the angle. The sign of the axis is the sign of $B$, and the sign of $\Theta$ follows once $\cos\Theta$ is fixed, so there is no independent sign choice for the axis or for the angle. Fixing the branches of $\Rho$ and $B$ leaves the angle modulo $2\pi$, which is precisely the multivaluedness of the logarithm: the branches of $\log\tilde Q$ differ by the kernel of the exponential, and the powers inherit the ambiguity. This is why the logarithm and the powers are many-valued on $\mathbb{B}^\times$ while the exponential is single-valued.

### The Domain

The Hamilton representation is therefore available on

$$
\left\{\tilde{Q} : \langle\tilde Q\rangle_{\natural}\neq0 \ \text{ and } \ \langle\vec Q,\vec Q\rangle_{\natural}\neq0\right\},
$$

which is the complement of the union of the null cone and the quadric cone $\langle\vec Q,\vec Q\rangle_{\natural} = 0$. The second condition is independent of the first: the element $1+\vec e_x+i\vec e_y$ has $\langle\tilde Q\rangle_{\natural} = 1$ and $\langle\vec Q,\vec Q\rangle_{\natural} = 1+i^2 = 0$, so it is invertible and has no Hamilton representation. It is the degenerate case $B=0$, $\vec Q\neq0$ of *The Spectrum*, §*The Behaviour on the Cone*: a single Jordan block, written $Q_te_t+N$ with $N^2=0$, which has no eigenvalue decomposition. The eigenbasis of §*The Eigenbasis and the Spinor Spaces* does not exist there, since the root $\vec\Xi=-i\vec U$ is undefined. The element $e_t+i\vec e_x$, on the other hand, has $\langle\vec Q,\vec Q\rangle_{\natural} = -1\neq0$ and $\langle\tilde Q\rangle_{\natural}=0$: it has a Hamilton axis but lies on the null cone. Within its domain the representation is unique up to the period of $\Theta$ once the branches of $\Rho$ and $B$ are fixed.

## The Three Pairings

### The Three Bracketings

The four factors can be bracketed in exactly three ways, and each bracketing is a pairing. The table records the two factors and the norm each carries; the domains are the subject of the next subsection.

| pairing | first factor | second factor | norm of the first factor | norm of the second factor |
|---|---|---|---|---|
| Hamilton | $\Rho=r\exp(i\alpha)$, complex scalar | $\exp(\vec U\Theta)=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\Rho^{2}$ | $e_t$ |
| quaternion | $\tilde q=r\tilde u_{\mathrm r}$, real quaternion | $\exp(i\tilde\Psi)=\exp(i\alpha)\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $r^{2}$ | $\exp(2i\alpha)$ |
| Cartan | $\tilde H=r\tilde U_{\mathrm b}$, Hermitian positive | $\tilde U=\exp(i\alpha)\tilde u_{\mathrm r}$, unitary | $r^{2}$ | $\exp(2i\alpha)$ |

The three rows split the same norm $\Rho^{2}=r^{2}\exp(2i\alpha)$ in three ways. The Hamilton row is the only one that puts the whole norm in its first factor and leaves a unit second factor. The quaternion and Cartan rows put the scale in the first factor and the phase in the second; what distinguishes them is the kind of the first factor, a real quaternion in one and a Hermitian positive element in the other. The three moduli are therefore a complex scalar, a real quaternion and a Hermitian positive element, and the four-factor word is the reference in which the scale stands alone.

### The Domains and the Witnesses

Five elements separate the cases. The Hamilton axis needs $B^{2}=\langle\vec Q,\vec Q\rangle_{\natural}\neq0$, the quaternion construction needs $\langle\tilde Q\rangle_{\natural}\neq0$ and $\tilde q_r\neq0$, and the Cartan pairing needs only $\langle\tilde Q\rangle_{\natural}\neq0$.

| element | $\langle\tilde Q\rangle_{\natural}$ | $\langle\vec Q,\vec Q\rangle_{\natural}$ | $\tilde q_r$ | Hamilton | quaternion construction | Cartan |
|---|---|---|---|---|---|---|
| $(1+i)e_t+\vec e_x+2\vec e_y$ | $5+2i$ | $5$ | $e_t+\vec e_x+2\vec e_y$ | yes | yes | yes |
| $1+\vec e_x+i\vec e_y$ | $1$ | $0$ | $1+\vec e_x$ | no | yes | yes |
| $i\vec e_x+i\vec e_y$ | $-2$ | $-2$ | $0$ | yes | no | yes |
| $i$ | $-1$ | $0$ | $0$ | no | no | yes |
| $e_t+i\vec e_x$ | $0$ | $-1$ | $e_t$ | no word | no word | no word |

The first line is the generic case, in which all three pairings exist and regroup the same four factors in three ways. The second line separates this pairing: the vector part is null, so no axis exists. The third line separates the quaternion construction, and the fourth line is missed by both partial pairings. The fifth line separates the conditions of the factorisation: $e_t+i\vec e_x$ has a Hamilton axis and a quaternion part to divide by, and lies on the null cone, where no word exists.

The two senses of partial are separated in the table.

| pairing | factorisation exists when | construction exists when |
|---|---|---|
| Hamilton | $\langle\tilde Q\rangle_{\natural}\neq0$ and $\langle\vec Q,\vec Q\rangle_{\natural}\neq0$ | the same |
| quaternion | $\langle\tilde Q\rangle_{\natural}\neq0$ | $\langle\tilde Q\rangle_{\natural}\neq0$ and $\tilde q_r\neq0$ |
| Cartan | $\langle\tilde Q\rangle_{\natural}\neq0$ | the same |

The Hamilton row is partial in both senses: its single exponential needs the axis $\vec U=\vec Q/B$, so it fails where the vector part is null, and the factorisation fails with it. The quaternion row is partial in its construction only; the Cartan row in neither.

The two partial domains are not nested, and the Cartan domain contains both; *The Cartan Hermitian Pairing of the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion*, §*The Domains and the Witnesses* records the exact cover of the complement of the null cone.

### What This Pairing Carries

The Hamilton row is the only one whose modulus is central. Its modulus and angle are the eigenvalue data of *The Biquaternion Eigenvalue Decomposition*, §*The Eigenprojectors*, $\lambda_\pm=\Rho\exp(\pm i\Theta)$, read in the eigenbasis of §*The Eigenbasis and the Spinor Spaces*, and its second factor is the unit element $\tilde Q/\Rho$ itself. The pairing generalises the quaternion polar decomposition: when all four coefficients are real the boost is trivial and the word reduces to $\tilde Q=r\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ term by term.

## Behaviour Under the Three Conjugations

The algebra has three nontrivial conjugations: quaternion conjugation ${}^{\natural}$, the anti-automorphism fixing the centre $\mathbb{C}_{\mathbb{B}}$; complex conjugation $\bar{\cdot}$, the automorphism conjugating every coefficient; and Hermitian conjugation ${}^{*} = {}^{\natural}\circ\bar{\cdot}$, the two operations commuting because one acts on the coefficients and the other on the units. The three act on the Hamilton data as follows.

### The Hamilton Data

In $\tilde{Q} = \Rho\exp(\vec U\Theta)$ the modulus $\Rho$ and the angle $\Theta$ are complex scalars and therefore central, while the axis $\vec U$ is pure, so that $\vec U^{\natural} = -\vec U$. Quaternion conjugation fixes the centre and reverses a pure element, complex conjugation is an automorphism and conjugates the coefficients of the axis as it conjugates the rest, and Hermitian conjugation does both. The axis of a conjugated element is again a root of $-1$, and it is read off the conjugate: complex conjugation carries $\vec U$ to $\bar{\vec U}$, quaternion conjugation to $-\vec U$, and Hermitian conjugation to $-\bar{\vec U}$:

$$
(\tilde{Q})^{\natural} = \Rho\exp(-\vec U\Theta), \qquad \bar{\tilde{Q}} = \bar{\Rho}\exp(\bar{\vec U}\,\bar{\Theta}), \qquad \tilde{Q}^{*} = \bar{\Rho}\exp(-\bar{\vec U}\,\bar{\Theta}) .
$$

| conjugation | $\Rho$ | $\vec U$ | $\Theta$ | result |
|---|---|---|---|---|
| quaternion ${}^{\natural}$ | $\Rho$ | $-\vec U$ | $\Theta$ | $\Rho\exp(-\vec U\Theta)$ |
| complex $\bar{\cdot}$ | $\bar{\Rho}$ | $\bar{\vec U}$ | $\bar{\Theta}$ | $\bar{\Rho}\exp(\bar{\vec U}\bar{\Theta})$ |
| Hermitian ${}^{*}$ | $\bar{\Rho}$ | $-\bar{\vec U}$ | $\bar{\Theta}$ | $\bar{\Rho}\exp(-\bar{\vec U}\bar{\Theta})$ |

The consistency of the second row is a consequence of $\langle\bar{\tilde Q}\rangle_{\natural} = \overline{\langle\tilde Q\rangle_{\natural}}$, hence $\Rho(\bar{\tilde{Q}}) = \overline{\Rho(\tilde{Q})}$: the modulus conjugates, the angle conjugates, and the axis conjugates coefficientwise. Quaternion conjugation is the operation that reverses the axis, complex conjugation the one that reverses nothing, and Hermitian conjugation the one that does both.

## The Root Reading

The second half reads the same four-factor word at the elements where it closes, $\tilde\Xi^2=e_t$. The classification of the roots is that of *Idempotents*, and the exponential forms are read here on the polar word. The readings are collected in the table.

| reading | object | form | what it shows |
|---|---|---|---|
| four factors | $\tilde Q$ | $r\exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the word that is bracketed |
| non-central root | $\tilde\Xi$ | $i\,\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the word at a root of $+1$ of norm $-e_t$ |
| two exponents | $\mathcal H,\mathcal R$ | $i\frac{\psi}{2}\vec u_{\mathrm b}$, $\frac{\theta}{2}\vec u_{\mathrm r}$ | the factors are exponentials; their bracket measures the failure of additivity |
| single exponential | $-i\tilde\Xi$ | $\exp(\vec U'\frac{\pi}{2})=\vec U'$ | the product is one exponential, with a real angle on the root set |
| idempotent | $\tilde\Xi$ | $\exp(i\pi\tilde\Pi_-)$ | one exponential of an idempotent |
| bridge | $\tilde\Xi$, $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $-i\tilde\Xi=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the two forms determine each other |

The first row is the word of the first half; the other five are the readings of this half, and the table is the order of the subsections. The classification, the hyperbolic form, the idempotent form and the bridge are cited; the bracket of the two exponents and the single exponential on the whole domain are what this half adds.

### The Word at a Root of One

The roots of $+1$ are classified in *Idempotents*, §*The Roots of One*: they are $\pm e_t$ and the pure roots $\vec\Xi$ with $\vec\Xi^2=e_t$. Taking norms in $\tilde\Xi^2=e_t$ gives $\langle\tilde\Xi\rangle_{\natural}=\pm e_t$, because the norm is multiplicative, so the polar word of a root has one of two shapes.

| norm | word | condition on the factors |
|---|---|---|
| $e_t$ | $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\psi=0$ and $\theta\in\{0,2\pi\}$ |
| $-e_t$ | $i\,\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\vec u_{\mathrm b}\perp\vec u_{\mathrm r}$ and $\theta=\pi$ |

The first row is the central pair. A root of unit norm has $r=1$ and $\alpha=0$, so its word is the unit product itself, and the only roots of unit norm are $\pm e_t$. The second row is the non-central family: the norm $-e_t$ forces $\exp(2i\alpha)=-1$, hence $\exp(i\alpha)=i$, and the unit product must itself square to $-e_t$, which on the two axes is the orthogonality of the axes together with the half-turn of the rotor, $\tilde u_{\mathrm r}=\vec u_{\mathrm r}$. The family has four real parameters, the rapidity $\psi$, the rotor axis (two) and the boost axis in the plane orthogonal to it (one), which is the dimension of the classification.

### The Root From Its Coordinates

The coordinates give the two factors directly. Write $\Xi_\mu=\xi_\mu+i\xi'_\mu$ and collect the real triples $\vec\xi=(\xi_x,\xi_y,\xi_z)$ and $\vec\xi'=(\xi'_x,\xi'_y,\xi'_z)$. The single complex equation $\Xi_x^2+\Xi_y^2+\Xi_z^2=-1$ is the pair

$$
\vec\xi\cdot\vec\xi'=0,\qquad \lvert\vec\xi'\rvert^2-\lvert\vec\xi\rvert^2=1,
$$

so the two triples are orthogonal and the imaginary one is the longer. In the hyperbolic form $\tilde\Xi=\exp(t\,i\vec u_{\mathrm b})\,i\vec u_{\mathrm n}$ read from these coordinates, the two halves are $\vec\xi=-\sinh t\,\vec u_{\mathrm b}\vec u_{\mathrm n}$ and $\vec\xi'=\cosh t\,\vec u_{\mathrm n}$, so the reading is

$$
\cosh t=\lvert\vec\xi'\rvert,\qquad \sinh t=\lvert\vec\xi\rvert,\qquad \vec u_{\mathrm n}=\frac{\vec\xi'}{\lvert\vec\xi'\rvert},\qquad \vec u_{\mathrm b}=\Bigl(\frac{\vec\xi}{\lvert\vec\xi\rvert}\Bigr)\vec u_{\mathrm n}.
$$

The imaginary triple therefore carries the rotor axis, $\vec u_{\mathrm r}=\vec u_{\mathrm n}$, and the real triple the boost axis; the rapidity of the polar word is $\psi=2t$. The reconstruction of the root from the two triples is the hyperbolic form itself, which the cited article proves. The polar word names the same two factors and adds nothing on the root set.

### The Two Exponents

The two non-central factors are exponentials, and the elements whose exponentials they are, rather than the factors themselves, are the primitive data of the word. The two exponents are

$$
\mathcal H=i\frac{\psi}{2}\vec u_{\mathrm b},\qquad \mathcal R=\frac{\theta}{2}\vec u_{\mathrm r},\qquad \tilde U_{\mathrm b}=\exp(\mathcal H),\qquad \tilde u_{\mathrm r}=\exp(\mathcal R).
$$

| exponent | formula | kind | square | exponential |
|---|---|---|---|---|
| $\mathcal H$ | $i\frac{\psi}{2}\vec u_{\mathrm b}$ | Hermitian, in $\mathbb{M}_+$ | $\frac{\psi^2}{4}e_t$ | the boost $\tilde U_{\mathrm b}$ |
| $\mathcal R$ | $\frac{\theta}{2}\vec u_{\mathrm r}$ | real pure, in $\mathbb{M}_-\cap\mathrm{Vect}(\mathbb{B})$ | $-\frac{\theta^2}{4}e_t$ | the rotor $\tilde u_{\mathrm r}$ |

The Hermitian exponent is the real $\frac{\psi}{2}$ times the Hermitian root $i\vec u_{\mathrm b}$ of $+e_t$, and the real pure exponent the real $\frac{\theta}{2}$ times the root $\vec u_{\mathrm r}$ of $-e_t$. On the exponents, the two non-central factors are the two halves of the Hermitian split of the exponent, which *The Cartan Hermitian Pairing of the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion* reads at the level of the element.

**The root on the exponents.** On the root set the rotor is pure, so $\theta=\pi$ and the rotor exponent is the same quarter turn $\mathcal R=\frac{\pi}{2}\vec u_{\mathrm r}$ for every root; the roots are separated by the rapidity inside $\mathcal H$ and by the two directions, and the closing condition $\tilde\Xi^2=e_t$ is exactly their orthogonality,

$$
\tilde\Xi=i\exp(\mathcal H)\exp(\mathcal R),\qquad \tilde\Pi_\pm=\frac12\bigl(e_t\pm i\exp(\mathcal H)\exp(\mathcal R)\bigr).
$$

**The bracket.** The two exponents do not commute in general, and their bracket is

$$
[\mathcal H,\mathcal R]=i\frac{\psi\theta}{2}\bigl(\vec u_{\mathrm b}\times\vec u_{\mathrm r}\bigr),
$$

nonzero as soon as $\psi\theta\neq0$ and the two axes are not parallel. On the root set, where the axes are orthogonal and $\theta=\pi$, it is the Hermitian root $i\vec u_{\mathrm b}\vec u_{\mathrm r}$ of $+e_t$ multiplied by the real $\frac{\pi\psi}{2}$,

$$
[\mathcal H,\mathcal R]=i\frac{\pi\psi}{2}\vec u_{\mathrm b}\vec u_{\mathrm r},\qquad \bigl(i\vec u_{\mathrm b}\vec u_{\mathrm r}\bigr)^2=e_t .
$$

A non-zero bracket is exactly what forbids adding the exponents, and the roots of norm $-e_t$ are the elements on which it does not vanish, except at the Hermitian root $\psi=0$.

### The Single Exponential

Whether the word adds is decided by the bracket of the two factors, and the non-Hermitian roots of one are its extreme case. The bracket of the two factors is

$$
[\tilde U_{\mathrm b},\tilde u_{\mathrm r}] = 2i\sinh\frac{\psi}{2}\sin\frac{\theta}{2}\bigl(\vec u_{\mathrm b}\times\vec u_{\mathrm r}\bigr) ,
$$

so the two factors commute exactly when the two axes are parallel or one of the two factors is central,

$$
[\tilde U_{\mathrm b},\tilde u_{\mathrm r}] = 0 \iff \vec u_{\mathrm b}\parallel\vec u_{\mathrm r} \ \text{ or } \ \psi = 0 \ \text{ or } \ \theta\in\{0,2\pi\} .
$$

Call such a word **aligned**. The parallelism is a condition of codimension two on the element, the two axes being two independent directions of the axis sphere, while the central cases are lower-dimensional; a generic element is therefore not aligned. The worked example below is aligned because its two axes were chosen collinear, which is a special choice.

**The roots of norm $-e_t$ are aligned only at the Hermitian root.** The axes of a root of norm $-e_t$ are orthogonal, so the bracket of a root is $2i\sinh\frac{\psi}{2}(\vec u_{\mathrm b}\times\vec u_{\mathrm r})$, which vanishes only at $\psi = 0$, the Hermitian root $i\vec u_{\mathrm r}$ whose boost is trivial. Apart from that root, the roots of norm $-e_t$ sit at one extreme of the bracket and the aligned elements at the other.

**An aligned word is a single exponential with a complex number inside.** With $\vec u_{\mathrm b} = \epsilon\vec u_{\mathrm r} = \epsilon\vec u$ and $\epsilon = \pm1$, the two exponents add, their sum is one complex number times the common direction, and the product of the two factors is the single exponential

$$
\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \exp(\mathcal H+\mathcal R) = \exp\Bigl(\Bigl(\frac{\theta}{2}+\epsilon i\frac{\psi}{2}\Bigr)\vec u\Bigr) = \cos\Bigl(\frac{\theta}{2}+\epsilon i\frac{\psi}{2}\Bigr)e_t+\sin\Bigl(\frac{\theta}{2}+\epsilon i\frac{\psi}{2}\Bigr)\vec u .
$$

The number inside is the rotation half-angle plus $i$ times the rapidity half-angle, and it is exactly the complex angle of the Hamilton representation of that element: on the aligned words $\Theta = \frac{\theta}{2}+\epsilon i\frac{\psi}{2}$ and $\vec U = \vec u$ up to sign. The aligned line is where the two halves of the article meet term by term, the complex angle of the element degenerating into the sum of its two exponents.

**Away from the aligned line the exponents do not add.** The product is then not the exponential of the sum, and the gap is the Baker–Campbell–Hausdorff series of the two exponents,

$$
\Theta\vec U = \mathcal H+\mathcal R+\frac{1}{2}[\mathcal H,\mathcal R]+\frac{1}{12}\bigl[\mathcal H,[\mathcal H,\mathcal R]\bigr]-\frac{1}{12}\bigl[\mathcal R,[\mathcal H,\mathcal R]\bigr]+\cdots ,
$$

whose leading term is half the bracket. On 100 random pairs with the rapidity and the rotation angle both between $0.02$ and $0.12$, the relative deviation $\lvert\Theta\vec U-(\mathcal H+\mathcal R)\rvert/\lvert\Theta\vec U\rvert$, in the Euclidean norm of the coefficients, is bounded as in the table.

| truncation of $\Theta\vec U$ | relative deviation |
|---|---|
| $\mathcal H+\mathcal R$ | $\le 3.9\times10^{-2}$ |
| $+\frac{1}{2}[\mathcal H,\mathcal R]$ | $\le 1.0\times10^{-3}$ |
| $+$ the two cubic terms | $\le 2.1\times10^{-5}$ |

**The single exponential does not need the alignment.** The product $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ has norm one and is the element $\tilde Q$ stripped of its central modulus $\Rho$, and dividing by the central $\Rho$ leaves the Hamilton axis and the complex angle unchanged, both being read from the ratio of the parts of the element. The product is therefore a single exponential with a complex number inside on the whole domain,

$$
\boxed{\;\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \exp(\vec U\Theta)\;},
$$

with the same root $\vec U$ of $-e_t$ and the same complex $\Theta$ as the element, its exponent $\Theta\vec U$ being a complex multiple of a root. The single exponential is thus the reward of the norm being one, which is general, and not of the commutativity, which is exceptional; what commutativity buys is only the identity of the exponent $\Theta\vec U$ with the sum $\mathcal H+\mathcal R$ of the two given exponents.

**On the root set the complex number collapses to a real one.** The extracted element $-i\tilde\Xi = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ is pure, so $\cos\Theta = 0$, the complex angle is the real quarter turn $\Theta = \frac{\pi}{2}$, and the extracted element, a unit-norm root of $-e_t$, is its own quarter-turn exponential,

$$
-i\tilde\Xi = \tilde U_{\mathrm b}\tilde u_{\mathrm r} = \exp\Bigl(\vec U'\frac{\pi}{2}\Bigr) = \vec U' , \qquad \vec U' = -i\tilde\Xi .
$$

The non-Hermitian roots of one are therefore the elements furthest from the aligned case and, at the same time, the elements whose single exponential carries a real number in place of the complex one. The complex angle is not lost with them: it is the aligned words that carry the genuinely complex number $\frac{\theta}{2}+\epsilon i\frac{\psi}{2}$ of the subsection above.

### The Idempotent Exponential Form

Every root of one is the exponential of its halving idempotent. Since $\tilde\Pi_-$ is idempotent the exponential series truncates,

$$
\exp(i\pi\tilde\Pi_-)=e_t+\bigl(\exp(i\pi)-1\bigr)\tilde\Pi_-=e_t-2\tilde\Pi_-=\tilde\Xi,
$$

so

$$
\tilde\Xi=\exp(i\pi\tilde\Pi_-),\qquad \tilde\Pi_-=\tfrac12(e_t-\tilde\Xi)
$$

The identity is the idempotency of $\tilde\Pi_-$, and the halving is that of *Idempotents*, §*The Correspondence with the Roots of One*. The form is a single exponential of one element where the polar word is an ordered product of four. The two ends of the halving are the trivial roots: $\tilde\Xi=e_t$ gives $\tilde\Pi_-=0$, and $\tilde\Xi=-e_t$ gives $\tilde\Pi_-=e_t$.

### The Bridge Between the Two Forms

The two forms are tied by the product of the last two factors. On a root of norm $-e_t$ the word is $\tilde\Xi=i\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, so left multiplication by $-i$ extracts that product, and the halving idempotent and the exponent split as

$$
-i\tilde\Xi=\tilde U_{\mathrm b}\tilde u_{\mathrm r},\qquad
\tilde\Pi_-=\tfrac12\bigl(e_t-i\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr),\qquad
i\pi\tilde\Pi_-=\tfrac{i\pi}{2}e_t+\tfrac{\pi}{2}\tilde U_{\mathrm b}\tilde u_{\mathrm r}.
$$

The central part of the exponent is fixed at $\tfrac{i\pi}{2}e_t$, and the two-factor part is the last two factors of the word multiplied by the real half-turn. These are the statements of the cited article, §*The Idempotent Exponential Form of a Root*; they are recorded here because the extracted product is the second factor of the Hamilton pairing of the root: with $\Rho=i$ on the norm $-e_t$ family,

$$
\tilde U_{\mathrm L}=\frac{\tilde\Xi}{\Rho}=-i\tilde\Xi=\tilde U_{\mathrm b}\tilde u_{\mathrm r}.
$$

### The Hermitian Roots

The roots of one that are Hermitian, $\tilde\Xi^{*}=\tilde\Xi$, are the zero-rapidity case. On a root of norm $-e_t$ the word is $\tilde\Xi=i\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\tilde u_{\mathrm r}$ pure and the axes orthogonal, and

$$
\tilde\Xi^{*}-\tilde\Xi=2\sinh\tfrac{\psi}{2}\,\vec u_{\mathrm b}\vec u_{\mathrm r},
$$

which vanishes exactly when the boost is trivial. The Hermitian roots are therefore the central pair and the purely imaginary family,

$$
\tilde\Xi=\pm e_t,\qquad \tilde\Xi=i\vec u_{\mathrm n}\quad(\vec u_{\mathrm n}\in\mathcal{A}),
$$

as in *Idempotents*, §*The Roots of One*. In the idempotent form the halving element of a Hermitian root is Hermitian.

### The Two Pure Elements

**The two directions.** The root set is generated by two orthogonal unit pure real quaternions and one rapidity: the rotor axis $\vec u_{\mathrm r}$, the boost axis $\vec u_{\mathrm b}$ and $\psi\ge0$. Their product $\vec u_{\mathrm b}\vec u_{\mathrm r}$ is the third unit pure direction, perpendicular to both, and

$$
\tilde\Xi=i\cosh\tfrac{\psi}{2}\,\vec u_{\mathrm r}-\sinh\tfrac{\psi}{2}\,\vec u_{\mathrm b}\vec u_{\mathrm r},\qquad \tilde\Xi^2=e_t,\qquad \langle\tilde\Xi\rangle_{\natural}=-e_t
$$

(§*The Root From Its Coordinates* above, and *Idempotents*, §*The Non-Hermitian Roots*). The root is pure and lies in the plane of the two directions; at zero rapidity it is the Hermitian root $i\vec u_{\mathrm r}$, a single direction, and the boost switches the second direction on.

**The element.** The same two non-central factors, dialled by the central scale and the central phase, are the general element of the domain,

$$
\tilde Q=r\exp(i\alpha)\,\tilde U_{\mathrm b}\tilde u_{\mathrm r}.
$$

An element whose non-central factors are those of the root is the central multiple $\tilde Q=-i\,r\exp(i\alpha)\,\tilde\Xi$ of it; in general the element carries its own two factors, of the same kind.

**The idempotents and the spinor spaces.** The halving map carries the root to the pair $\tilde\Pi_\pm=\tfrac12(e_t\pm\tilde\Xi)$, and the Peirce decomposition of *The Peirce Decomposition*, §*The Peirce Decompositions*, splits the algebra into the four corners. The eigenbasis of §*The Eigenbasis and the Spinor Spaces* completes the two idempotents by the nilpotents of the two mixed corners and reads the same split as $\mathbb{B}=S_+\oplus S_-$, the two spinor spaces. The chain is thus

$$
\text{two pure directions}\;\longrightarrow\;\text{the root}\;\longrightarrow\;\text{the idempotents}\;\longrightarrow\;\text{the Peirce corners and the spinor spaces},
$$

and the same two directions, with their angles and the central dial, give the general element.

## Worked Examples

The examples are collected in the table, with the status of the pairing and the Hamilton data. The subsections give the computations.

| element | Hamilton | $\Rho$ | $\Theta$ | $\vec U$ |
|---|---|---|---|---|
| $(1+i)e_t+\vec e_x+2\vec e_y$ | yes | $2.278724+0.438842i$ | $1.080835-0.378137i$ | $0.447214\,\vec e_x+0.894427\,\vec e_y$ |
| $1+\vec e_x+i\vec e_y$ | no | — | — | $B=0$ |
| $i\vec e_x+i\vec e_y$ | yes | $i\sqrt2$ | $\tfrac{\pi}{2}e_t$ | $0.707107(\vec e_x+\vec e_y)$ |
| $i$ | no | $i$ | — | $\vec Q=0$ |
| root of norm $-e_t$, $\psi=1.386294$ | yes | $i$ | $\tfrac{\pi}{2}e_t$ | $1.25\,\vec u_{\mathrm r}+0.75\,i\,\vec e_z$ |
| skew axes, $\theta=1.2$, $\psi=0.8$ | yes | $e_t$ | $0.551851+0.307926i$ | $0.636163-0.308495i$ in $\vec e_x$, $0.878459+0.191155i$ in $\vec e_y$, $-0.117212-0.241710i$ in $\vec e_z$ |

### The Generic Element

Take $\tilde{Q} = (1+i)e_t+\vec e_x+2\vec e_y$, the worked example of the companion article. Its polar decomposition is

$$
r = 2.320595787, \quad \alpha = 0.190253189, \quad \tilde U_{\mathrm b} = 1.072349609\,e_t - 0.173166789\,i\,\vec e_x - 0.346333577\,i\,\vec e_y, \quad \tilde u_{\mathrm r} = 0.470592172\,e_t+0.394599292\,\vec e_x+0.789198585\,\vec e_y .
$$

*The Hamilton regrouping.* The vector part is $\vec Q = \vec e_x+2\vec e_y$, so $\langle\vec Q,\vec Q\rangle_{\natural} = 5$ and $B = \sqrt{5} = 2.236067978$; the axis is $\vec U = (\vec e_x+2\vec e_y)/\sqrt{5} = 0.447213595\,\vec e_x+0.894427191\,\vec e_y$, which satisfies $\vec U^2 = -e_t$. The modulus is $\Rho = 2.278723854+0.438842117i$, and the complex angle is fixed by

$$
\cos\Theta = \frac{Q_t}{\Rho} = 0.504639332+0.341657461i, \qquad \sin\Theta = \frac{\sqrt{5}}{\Rho} = 0.946188580-0.182219271i ,
$$

so that $\tilde{Q} = \Rho(\cos\Theta+\vec U\sin\Theta)$; the identity $\exp(\vec U\Theta) = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ then holds term by term, both sides being $\tilde{Q}/\Rho$, and with it the equality of the Hamilton representation with the first pairing of the four factors.

*The two exponents.* The polar data also give the two exponents of the word,

$$
\mathcal H = i\frac{\psi}{2}\vec u_{\mathrm b} = -0.169107833\,i\,\vec e_x-0.338215666\,i\,\vec e_y , \qquad \mathcal R = \frac{\theta}{2}\vec u_{\mathrm r} = 0.483363900\,\vec e_x+0.966727800\,\vec e_y ,
$$

and here $\vec u_{\mathrm b} = -\vec u_{\mathrm r}$, so the word is aligned and the exponents add. Their sum is

$$
\mathcal H+\mathcal R = \bigl(0.483363900-0.169107833i\bigr)\vec e_x+\bigl(0.966727800-0.338215666i\bigr)\vec e_y ,
$$

the complex number $\frac{\theta}{2}-i\frac{\psi}{2} = 1.080834538-0.378136610i$ times the rotor axis, and it is exactly the Hamilton exponent: $\Theta\vec U = \mathcal H+\mathcal R$ to machine precision, with $\Theta = 1.080834538-0.378136610i$ and $\vec U = \vec u_{\mathrm r}$. The alignment here is an accident of the example, whose two axes were chosen collinear; the last example has the skew case.

### The Element with a Null Vector Part

Take $\tilde{Q} = 1+\vec e_x+i\vec e_y$. Then $\langle\tilde Q\rangle_{\natural} = 1$ but $\langle\vec Q,\vec Q\rangle_{\natural} = 1+i^2 = 0$, so $B=0$ and the Hamilton axis does not exist. The element lies in the degenerate case of *The Spectrum*, §*The Behaviour on the Cone*, where the vector part $N=\vec Q$ satisfies $N^2=0$: a single Jordan block, with no eigenvalue decomposition. The four-factor word exists, and with it the quaternion and Cartan pairings of the companion articles; only the Hamilton pairing is unavailable.

### The Element with a Vanishing Real Part

Take $\tilde{Q} = i\vec e_x+i\vec e_y$. Then $\langle\tilde Q\rangle_{\natural} = -2$ and $\langle\vec Q,\vec Q\rangle_{\natural} = -2$, so $B = i\sqrt2$ and the Hamilton axis exists, $\vec U = (\vec e_x+\vec e_y)/\sqrt2$, with $\Rho = i\sqrt2$, $\cos\Theta = 0$ and $\sin\Theta = 1$:

$$
\tilde Q = i\sqrt2\,\exp\Bigl(\vec U\frac{\pi}{2}\Bigr).
$$

The real quaternion part vanishes, $\tilde q_r = 0$, so the quaternion construction fails on the same element, while the Cartan pairing reads $\tilde H = \sqrt2\,e_t$ with second factor $i\vec U$. The example exhibits the Hamilton domain against the quaternion one.

### The Scalar Imaginary

Take $\tilde{Q} = i$. Then $\langle\tilde Q\rangle_{\natural} = -1$ and $\vec Q=0$, so $B=0$: the modulus $\Rho=i$ exists but the axis and the angle do not, and the Hamilton representation is unavailable. The polar word is $i = 1\cdot\exp(i\pi/2)\cdot e_t\cdot e_t$. The element is the scalar vertex of *The Spectrum*, §*The Behaviour on the Cone*, in which the eigenprojections are not unique. The Cartan pairing reads $i=e_t\cdot i$; the quaternion construction also fails, since $\tilde q_r=0$.

### An Element at a Root of One

Take the rotor axis $\vec u_{\mathrm r} = (\vec e_x+\vec e_y)/\sqrt2$ and a boost axis orthogonal to it, $\vec u_{\mathrm b} = (\vec e_x-\vec e_y)/\sqrt2$, with the rapidity fixed by $\cosh\tfrac{\psi}{2} = \tfrac{5}{4}$ and $\sinh\tfrac{\psi}{2} = \tfrac{3}{4}$. The two axes multiply to the third pure direction, $\vec u_{\mathrm b}\vec u_{\mathrm r} = \vec e_z$, and the root is

$$
\tilde\Xi = i\cosh\tfrac{\psi}{2}\,\vec u_{\mathrm r}-\sinh\tfrac{\psi}{2}\,\vec u_{\mathrm b}\vec u_{\mathrm r} = 0.883883476\,i\,\vec e_x+0.883883476\,i\,\vec e_y-0.75\,\vec e_z , \qquad \tilde\Xi^2 = e_t , \qquad \langle\tilde\Xi\rangle_{\natural} = -e_t .
$$

Its halving idempotent and the product of the last two factors of the word are

$$
\tilde\Pi_- = \tfrac12(e_t-\tilde\Xi) = 0.5\,e_t-0.441941738\,i\,\vec e_x-0.441941738\,i\,\vec e_y+0.375\,\vec e_z , \qquad -i\tilde\Xi = \tilde U_{\mathrm b}\tilde u_{\mathrm r} = \tfrac{5}{4}\vec u_{\mathrm r}+i\tfrac{3}{4}\,\vec e_z ,
$$

and the root is the single exponential of its halving idempotent, $\tilde\Xi = \exp(i\pi\tilde\Pi_-)$. The element is Hermitian only at zero rapidity, where it reduces to $i\vec u_{\mathrm r}$.

*The two exponents and the bracket.* The exponents of the word are

$$
\mathcal H = i\frac{\psi}{2}\vec u_{\mathrm b} = 0.490129072\,i\,\vec e_x-0.490129072\,i\,\vec e_y , \qquad \mathcal R = \frac{\pi}{2}\vec u_{\mathrm r} = 1.110720735\,\vec e_x+1.110720735\,\vec e_y ,
$$

with $\psi = 1.386294361$, and their bracket is $[\mathcal H,\mathcal R] = i\frac{\pi\psi}{2}\vec u_{\mathrm b}\vec u_{\mathrm r} = 2.177586090\,i\,\vec e_z$, of length $2.177586090$. The two axes are orthogonal, so the root is not aligned and the exponents do not add. The Hamilton data of the root show the gap: its complex angle is the real quarter turn $\Theta = \frac{\pi}{2}$, and $\Theta\vec U$ differs from $\mathcal H+\mathcal R$ by $1.178097$ in the largest coefficient, against $1.088793$ for half the bracket, the leading term of the Baker–Campbell–Hausdorff series.

### An Element with Skew Axes

Take the rotor axis $\vec u_{\mathrm r} = (\vec e_x+\vec e_y)/\sqrt2$, the boost axis $\vec u_{\mathrm b} = \vec e_y$, the rotation angle $\theta = 1.2$ and the rapidity $\psi = 0.8$. The two directions meet at $45$ degrees, so the word is neither aligned nor orthogonal, and the product of the two factors is

$$
\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \bigl(0.892247531-0.163998009i\bigr)e_t+0.431631682\,\vec e_x+\bigl(0.431631682+0.339008523i\bigr)\vec e_y-0.163998009\,i\,\vec e_z .
$$

The exponents and their bracket are

$$
\mathcal H = 0.4\,i\,\vec e_y , \qquad \mathcal R = 0.424264069\,\vec e_x+0.424264069\,\vec e_y , \qquad [\mathcal H,\mathcal R] = i\frac{\psi\theta}{2}\bigl(\vec u_{\mathrm b}\times\vec u_{\mathrm r}\bigr) = -0.339411255\,i\,\vec e_z ,
$$

and the exponents do not add: the difference $\exp(\mathcal H+\mathcal R)-\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ has Euclidean norm $0.168866$ in the coefficients. The single exponential is nevertheless there, with the genuinely complex angle and the root of $-e_t$

$$
\Theta = 0.551850513+0.307926415i , \qquad \vec U = \bigl(0.636163468-0.308495063i\bigr)\vec e_x+\bigl(0.878459065+0.191155095i\bigr)\vec e_y-\bigl(0.117212379+0.241709650i\bigr)\vec e_z ,
$$

so that $\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \cos\Theta\,e_t+\sin\Theta\,\vec U$, and the exponent $\Theta\vec U$ is a complex multiple of a root of $-e_t$ whose difference from $\mathcal H+\mathcal R$ has $e_z$-component $0.169760320$ in magnitude, against $0.169705627$ for half the bracket: away from the aligned line the leading Baker–Campbell–Hausdorff term accounts for the gap along the bracket.

## Summary

### Main Results

| item | result |
|---|---|
| domain | $\langle\tilde Q\rangle_{\natural}\neq0$ and $\langle\vec Q,\vec Q\rangle_{\natural}\neq0$ |
| first factor | $\Rho=r\exp(i\alpha)=\sqrt{\langle\tilde Q\rangle_{\natural}}$, a complex scalar |
| second factor | $\exp(\vec U\Theta)=\tilde U_{\mathrm b}\tilde u_{\mathrm r}=\tilde Q/\Rho$ |
| equation | $\tilde Q=\Rho(\cos\Theta+\vec U\sin\Theta)$, with $\vec U=\vec Q/B$ |
| uniqueness | the two branch choices $\Rho\mapsto-\Rho$ with $\Theta\mapsto\Theta+\pi$, and $B\mapsto-B$ with $\vec U\mapsto-\vec U$, $\Theta\mapsto-\Theta$; fixed by the branches, leaving $\Theta$ modulo $2\pi$ |
| complex conjugation | $\Rho$, $\Theta$ and $\vec U$ all conjugate |
| quaternion conjugation | $\Rho$ and $\Theta$ fixed, $\vec U\mapsto-\vec U$ |
| Hermitian conjugation | $\Rho$ and $\Theta$ conjugate, $\vec U\mapsto-\bar{\vec U}$ |
| degenerate limits | a non-scalar real quaternion gives the quaternion polar form; a complex scalar has no Hamilton representation |
| eigenbasis and spinors | in the eigenbasis $(\tilde\Pi_+,\vec\Upsilon_-,\vec\Upsilon_+,\tilde\Pi_-)$ the operator $L_{\tilde Q}$ is $\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$; the two spinor spaces $S_\pm=\mathbb{B}\tilde\Pi_\pm$ are the two columns of $\mathsf M_2^Q$ |
| classical case | the polar decomposition of the ordinary quaternions |

The Hamilton pairing groups the scale with the phase into the complex modulus $\Rho=r\exp(i\alpha)$ and the boost with the rotor into the unit factor $\exp(\vec U\Theta)=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$. Its modulus is the eigenvalue data of *The Biquaternion Eigenvalue Decomposition*, §*The Eigenprojectors*, and its second factor is the Lorentz transformation of the word. It is the only pairing whose modulus is central, and it is partial in both senses: the axis $\vec U=\vec Q/B$ needs the vector part non-null, although the four-factor grouping exists on the whole complement of the null cone.

The second half reads the same word at a root of one, $\tilde\Xi^2=e_t$. Apart from the central pair $\pm e_t$, the non-Hermitian roots are generated by two orthogonal unit pure quaternions and one rapidity, and the Hermitian roots $i\vec u_{\mathrm n}$ are the zero-rapidity case; every root has both a two-factor form and the single exponential $\tilde\Xi=\exp(i\pi\tilde\Pi_-)$ of its halving idempotent.

### The Roots of One

| root | norm | form in the word | axes | $\mathcal H$ | $\mathcal R$ | commute? |
|---|---|---|---|---|---|---|
| $e_t$ | $e_t$ | central | none | $0$ | $0$ | yes |
| $-e_t$ | $e_t$ | central | arbitrary | $0$ | $\pi\vec u$ (any $\vec u$) | yes |
| $i\vec u_{\mathrm n}$ | $-e_t$ | $i\vec u_{\mathrm n}$ | boost trivial | $0$ | $\tfrac{\pi}{2}\vec u_{\mathrm n}$ | yes |
| non-Hermitian | $-e_t$ | $i\tilde U_{\mathrm b}\,\vec u_{\mathrm r}$ | $\vec u_{\mathrm b}\perp\vec u_{\mathrm r}$ | $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | $\tfrac{\pi}{2}\vec u_{\mathrm r}$ | no |

The two exponents of the word, the Hermitian $\mathcal H=i\frac{\psi}{2}\vec u_{\mathrm b}$ and the real pure $\mathcal R=\frac{\theta}{2}\vec u_{\mathrm r}$, add exactly on the aligned words, where the two axes are parallel or one factor is central. Elsewhere the sum is corrected by the Baker–Campbell–Hausdorff series, whose leading term is half the bracket $[\mathcal H,\mathcal R]=i\frac{\psi\theta}{2}(\vec u_{\mathrm b}\times\vec u_{\mathrm r})$. The product is nevertheless a single exponential on the whole domain, with the complex multiple $\Theta\vec U$ of a root of $-e_t$ as its exponent.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde{Q} = r \exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the polar decomposition, four factors |
| $r$, $\exp(i\alpha)$, $\tilde U_{\mathrm b}$, $\tilde u_{\mathrm r}$ | scale, central phase, Hermitian positive boost, unit real rotor |
| $\tilde{Q} = \Rho\exp(\vec U\Theta)$ | the Hamilton representation, the root pairing |
| $\tilde U_{\mathrm L} = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the second factor, the Lorentz transformation |
| $\Rho = r\exp(i\alpha) = \sqrt{\langle\tilde Q\rangle_{\natural}}$ | the Hamilton modulus, the complex modulus of the polar decomposition |
| $\vec U = \vec Q/B$ | the Hamilton axis, the root of $-1$ parallel to the vector part |
| $L_{\tilde Q}$, $R_{\tilde Q}$ | left and right multiplication by $\tilde Q$ on $\mathbb{B}$; $L_{\tilde Q}$ is diagonal in the eigenbasis, $R_{\tilde Q}$ has the left ideals $S_\pm$ as eigenspaces |
| $\vec\Xi = -i\vec U$ | the pure root of $+1$ attached to the axis |
| $\lambda_\pm = Q_t\pm iB = \Rho\exp(\pm i\Theta)$ | the eigenvalues, the coefficients of the eigenvalue decomposition |
| $\tilde\Pi_\pm = \frac12(e_t\pm\vec\Xi)$ | the eigenprojections, primitive orthogonal idempotents |
| $\vec\Upsilon_+\in\mathbb{B}_{-+}$, $\vec\Upsilon_-\in\mathbb{B}_{+-}$ | the nilpotents of the eigenbasis, normalised by $\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-$ and $\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+$ |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the two spinor spaces, the minimal left ideals, the two columns of $\mathsf M_2^Q$ |
| $\mathsf M_2^Q$ | the matrix model in the eigenbasis, with $\mathsf M_2^Q(\tilde Q)=\operatorname{diag}(\lambda_+,\lambda_-)$ |
| $\Theta$ | the complex angle of the single exponential; it is $\frac{\theta}{2}+\epsilon i\frac{\psi}{2}$ on aligned words and does not separate in general |
| $\vec Q = Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | the vector part of $\tilde{Q}$ |
| $\langle\vec Q,\vec Q\rangle_{\natural} = Q_x^2+Q_y^2+Q_z^2$ | the quaternionic bilinear square of the vector part |
| $B = \sqrt{\langle\vec Q,\vec Q\rangle_{\natural}}$ | the length of the vector part, in the branch that fixes the axis |
| $\tilde q_r$, $\tilde q_i$ | the real and imaginary quaternion parts of $\tilde{Q}$ |
| $\tilde q=r\tilde u_{\mathrm r}$, $\tilde\Psi$ | the quaternion modulus and the quaternion angle of the companion pairing |
| $Q_\mu = q_\mu+iq'_\mu$ | the four complex coefficients of $\tilde{Q}$, split into their real and imaginary parts |
| $\Xi_\mu = \xi_\mu+i\xi'_\mu$ | the four complex coefficients of a root of one $\tilde\Xi$ |
| $\exp(\tilde{Q})$ | the exponential; its Hamilton data $\exp(Q_t)$ and $B$ are generally not those of $\tilde{Q}$ |
| $\tilde\Xi$ | a root of one, $\tilde\Xi^2 = e_t$; the pure root attached to the Hamilton axis is $\vec\Xi=-i\vec U$ |
| $\tilde\Pi_- = \tfrac12(e_t-\tilde\Xi)$ | the halving idempotent of a root of one, whose exponential is the root |
| $-i\tilde\Xi = \tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the product of the last two factors of the polar word, read from a root of norm $-e_t$ |
| $\mathcal H = i\frac{\psi}{2}\vec u_{\mathrm b}$ | the exponent of the boost, Hermitian, in $\mathbb{M}_+$, the real $\frac{\psi}{2}$ times the Hermitian root $i\vec u_{\mathrm b}$ of $+e_t$ |
| $\mathcal R = \frac{\theta}{2}\vec u_{\mathrm r}$ | the exponent of the rotor, real pure, in $\mathbb{M}_-\cap\mathrm{Vect}(\mathbb{B})$, the real $\frac{\theta}{2}$ times the root $\vec u_{\mathrm r}$ of $-e_t$ |
| $[\mathcal H,\mathcal R] = i\frac{\psi\theta}{2}(\vec u_{\mathrm b}\times\vec u_{\mathrm r})$ | the bracket of the two exponents, vanishing exactly on the aligned words |
| $\Theta\vec U$ | the exponent of the single exponential, a complex multiple of a root of $-e_t$; it equals $\mathcal H+\mathcal R$ exactly on the aligned words, and otherwise differs from the sum by the Baker–Campbell–Hausdorff series |
| $\vec u_{\mathrm b} = \epsilon\vec u_{\mathrm r} = \epsilon\vec u$ | the aligned case, in which $\tilde U_{\mathrm b}\tilde u_{\mathrm r} = \exp\bigl((\frac{\theta}{2}+\epsilon i\frac{\psi}{2})\vec u\bigr)$ |
| $\vec u_{\mathrm b}$, $\vec u_{\mathrm r}$ | the boost and rotor axes, unit pure real quaternions |
| $\psi$, $\theta$, $\vec u_{\mathrm n}$ | rapidity, rotation angle, and axis of a Hermitian root of one |
| $\mathbb{M}_\pm$ | the Hermitian and the anti-Hermitian subspaces of $\mathbb{B}$ |
| $\mathrm{Sp}(1)$, $\mathbb{H}_{\mathbb{B}}$, $\mathcal{A}$ | the unit real quaternions, the real quaternion subspace, the unit pure real quaternions |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ | quaternion, coefficientwise and Hermitian conjugation |

## Further Reading

- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), §*The Eigenvalues* and §*The Eigenprojectors*, for the eigenvalues $\lambda_\pm=Q_t\pm iB$, the pure unit element $\vec U=\vec Q/B$ and the eigenprojections $\tilde\Pi_\pm$.
- [The N-Regular, Spectrally Regular Sector](the-n-regular-spectrally-regular-sector.html), §*The Eigenbasis, the Nilpotents, and the Peirce Corners*, for the eigenbasis with its nilpotents, and the two spinor spaces, on which the Hamilton parameters and the diagonal action are read.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a N-Regular, Spectrally Regular Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-n-regular-spectrally-regular-biquaternion.html), for the unit factor $\tilde U=\tilde Q/(r\exp(i\alpha))$, its eigenvalues $\exp(\pm i\Theta)$ and the eigenprojections it shares with $\tilde Q$.
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential, the logarithm and the powers, which fix the Hamilton parameters and carry their multivaluedness.
- [Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html), for the four exponentials, the existence and uniqueness of the word, and the logarithms that fix the branches.
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the four factors, the modulus $\Rho = \sqrt{\langle\tilde Q\rangle_{\natural}}$, the domain, and the degenerate cases against which the roots of the second half are read; §*The Algorithm* of that article, for the procedure in the coordinates of the element, the five steps, the factors and the exponents with their positions; and §*The Order of the Factors* of that article, for the exponents $i\frac{\psi}{2}\vec u_{\mathrm b}$ and $\frac{\theta}{2}\vec u_{\mathrm r}$ of the two non-central factors and for the failing sum rule; §*The Single Exponential* above is the sharpened form, where the product is nevertheless a single exponential with a complex angle.
- [The Quaternion Pairing of the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](the-quaternion-pairing-of-the-polar-decomposition-of-a-n-regular-spectrally-regular-biquaternion.html), for the quaternion grouping, the other partial pairing, and the comparison of the two domains.
- [The Cartan Hermitian Pairing of the Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](the-cartan-hermitian-pairing-of-the-polar-decomposition-of-a-n-regular-spectrally-regular-biquaternion.html), for the third grouping, $\tilde{Q} = HU$, which is not partial and has the full domain.
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the classification of the roots of one and the halving map to the idempotents.
- [The Peirce Decomposition](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html) and [Hermitian Idempotents and the Peirce Decomposition](hermitian-idempotents-and-the-peirce-decomposition.html), for the Peirce pieces into which a root of one splits the algebra through its halving idempotents.
- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the coordinate systems $Q_\mu = q_\mu+iq'_\mu$ used to read the coordinates of a root.
- [Modulus–Unit Polar Decomposition of Quaternions](modulus-unit-polar-decomposition-of-quaternions.html), for the quaternion polar form that the Hamilton representation generalises on the real quaternions.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the null cone on which the pairing fails.
