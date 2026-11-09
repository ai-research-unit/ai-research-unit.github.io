# __Biquaternion Discrete Harmonic Analysis__

## Introduction

This article treats the Fourier transform of a biquaternion-valued sequence, that is, of a function on the finite group $\mathbb{Z}/N$ with values in $\mathbb{B}$. It is read after *Biquaternion Continuous Harmonic Analysis*: the kernel, the classification of the roots of $1$, the count of the complex transforms and the vanishing-norm phenomenon are that article's and are cited here, not restated.

**The root of the kernel is a root of $1$.** The kernel is built from an element whose square is the unit, and from the complex scalar $i$ beside it,

$$
W_N(n,\ell)=\exp\left(-2\pi i\,\tilde{Ζ}\,\frac{n\ell}{N}\right),\qquad \tilde{Ζ}^2=e_t .
$$

The element that the exponent needs is $i\tilde{Ζ}$, whose square is $-e_t$; the sign of a Fourier kernel is therefore carried by the scalar $i$, and no element whose square is $-1$ is ever named. This is more than a change of letter, for three reasons.

**The classification becomes a dichotomy.** The roots of $1$ of the plain product are the central pair $\pm e_t$ and the pure elements $\vec{Ζ}$ with $(\vec{Ζ},\vec{Ζ})=-1$. That is one theorem, quoted below, and its statement contains no condition of the form $b^2-d^2=1$: a root is central or it is pure, and the pure condition is a single complex equation on the vector part.

**The root is a pair of idempotents.** The halving map sends a root to an idempotent and back, and the two members of the pair are $\tilde\Pi_\pm=\tfrac12(e_t\pm\tilde{Ζ})$. A root of $1$ is therefore a complete pair of orthogonal idempotents, which is an object the corpus uses throughout, and the transform is indexed by that pair rather than by a root picked from a conic.

**The transform splits into two transforms over the two ideals of the pair.** Because $\tilde{Ζ}=\tilde\Pi_+-\tilde\Pi_-$, the kernel is a pair of conjugate unit complex numbers, one attached to each idempotent,

$$
W_N(n,\ell)=e^{-2\pi i n\ell/N}\,\tilde\Pi_+ + e^{+2\pi i n\ell/N}\,\tilde\Pi_- .
$$

The two Peirce ideals $\tilde\Pi_+\mathbb{B}$ and $\tilde\Pi_-\mathbb{B}$ are each a complex plane, so the transform is a pair of ordinary complex transforms on those planes, and its factorization into scalar complex transforms is the transform read in the coordinates that the root itself supplies. No change of basis has to be chosen: the root supplies it.

The transform pair, the inversion, the factorization and the one-sided convolution theorem are proved here; the Z transform follows, with its rules, table and recurrences.

**Inversion is unconditional.** The inverse needs no hypothesis on the samples. What a zero divisor blocks is the division of a spectrum by itself, and the condition under which a spectrum avoids the zero divisors is not settled here.

**Boundaries.** The continuous transform, the classification of the roots of $1$ and the Peirce form of the kernel are *Biquaternion Continuous Harmonic Analysis*. The exponential and the de Moivre formula are *Biquaternion Elementary Functions*. The root glyph and the Peirce vocabulary are *Special Element and Peirce Conventions*. The commutative case, in which the phenomena of this article disappear, is *Reduced Biquaternion Discrete Harmonic Analysis*, compared with this one in §*The Commutative Alternative*.

Throughout, a biquaternion is written

$$
\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z, \qquad Q_\mu \in \mathbb{C},
$$

or, more compactly, as

$$
\tilde{Q} = Q_t e_t + \vec Q, \qquad \vec Q = Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z.
$$

The scalar imaginary is $i$, which commutes with the quaternion units. The quaternion conjugate is $\tilde{Q}^{\natural} = Q_t e_t - \vec Q$, the coefficient conjugate is $\bar{\cdot}$, and the biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = \tilde{Q} \tilde{Q}^{\natural}$, a complex scalar.

**Notation.** The root of $1$ is written $\tilde{Ζ}$, and a pure root $\vec{Ζ}$, the arrow taking priority over the tilde. Every root other than $\pm e_t$ is pure, so the arrow is written wherever purity is used; the letters $e_t$ and $i$ are the unit and the scalar imaginary.

## The Fourier Kernel

### The Root of One and Its Pair

**Definition (the root of one).** An element $\tilde{Ζ}\in\mathbb{B}$ is a **root of $1$** when $\tilde{Ζ}^2=e_t$, the square being taken in the algebra product.

**Theorem (the halving map; quoted).** Let $\tilde\Pi\in\mathbb{B}$ and put $\tilde{Ζ}=2\tilde\Pi-e_t$. Then $\tilde\Pi^{2}=\tilde\Pi$ exactly when $\tilde{Ζ}^{2}=e_t$, and the two maps $\tilde{Ζ}\mapsto\tfrac12(e_t+\tilde{Ζ})$ and $\tilde\Pi\mapsto2\tilde\Pi-e_t$ are inverse to each other. The source is *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Idempotents*.

The theorem is the reason the root of $1$ is the right object for a kernel: it is an idempotent read in another coordinate. The pair attached to a root is

$$
\tilde\Pi_\pm=\tfrac12(e_t\pm\tilde{Ζ}),\qquad \tilde\Pi_\pm^{2}=\tilde\Pi_\pm,\qquad \tilde\Pi_+\tilde\Pi_-=0,\qquad \tilde\Pi_++\tilde\Pi_-=e_t ,
$$

a complete family of orthogonal idempotents in the sense of *Special Element and Peirce Conventions*, §*The General Peirce Convention*, and the root is recovered from the pair as $\tilde{Ζ}=\tilde\Pi_+-\tilde\Pi_-$. The two members are exchanged by the sign of the root and by nothing else: the root is the pair, read with a sign.

**Remark (the $i$ is a scalar and not an element).** The generator of the kernel is $-2\pi i\tilde{Ζ}/N$; its algebra part is $\tilde{Ζ}$, a root of $1$, and the factor $i$ is the complex scalar that supplies the minus sign. An element whose square is $-e_t$ serves the same purpose and is the same object as $i\tilde{Ζ}$; the convention of this article is to keep the $i$ outside and to name only the root of $1$, so that the classification of the algebra elements used is the classification of the roots of $1$, the dichotomy of §*The Classification*.

### Definition and the Closed Form

**Definition (the discrete kernel).** Fix a root of $1$ once and for all. The **biquaternion Fourier kernel** of length $N$ is

$$
W_N(n, \ell) = \exp\left(-2\pi i\,\tilde{Ζ}\,\frac{n\ell}{N}\right), \qquad n, \ell \in \{0, 1, \ldots, N-1\}.
$$

**Proposition (the closed form).** With $\theta=2\pi n\ell/N$,

$$
W_N(n, \ell) = \cos\theta\, e_t - i\sin\theta\,\tilde{Ζ} .
$$

*Proof.* The powers of $\tilde{Ζ}$ alternate in pairs, $\tilde{Ζ}^{2k}=e_t$ and $\tilde{Ζ}^{2k+1}=\tilde{Ζ}$, so the exponential series splits into the even part $\cos\theta\,e_t$ and the odd part $-i\sin\theta\,\tilde{Ζ}$, the cosine and the sine being the ordinary functions of the real argument.

**The kernel is a unit, at every root and every pair of indices.** Both factors of the closed form lie in $\mathbb{C}[\tilde{Ζ}]$, which is commutative, and their product is $(\cos^2\theta+\sin^2\theta)e_t$; the inverse is the closed form with the sign of the sine reversed,

$$
W_N(n, \ell)^{-1} = \cos\theta\, e_t + i\sin\theta\,\tilde{Ζ} = W_N(n, -\ell).
$$

**The inverse is the kernel at the negated frequency index.** That statement carries no case distinction: it holds for the central roots, for the Hermitian roots and for the non-Hermitian pure roots alike, because it is an identity in the commutative algebra $\mathbb{C}[\tilde{Ζ}]$ and uses nothing else.

**Whether the inverse is a conjugation depends on the root.** For a pure root the quaternion conjugation reverses the vector part, $\vec{Ζ}^{\natural}=-\vec{Ζ}$, and therefore

$$
W_N(n, \ell)^{\natural} = \cos\theta\, e_t + i\sin\theta\,\vec{Ζ} = W_N(n, \ell)^{-1}, \qquad \langle W_N(n, \ell)\rangle_{\natural} = e_t .
$$

The kernel is then on the natural unit sphere, and its norm is the unit. **At the central roots $\tilde{Ζ}=\pm e_t$ this fails**: the kernel is the complex scalar $e^{\mp 2\pi i n\ell/N}e_t$, which the natural conjugation fixes rather than inverts, $W_N^{\natural}=W_N$, while the inverse is the coefficient conjugate $\overline{W_N}$. The natural norm there is

$$
\langle W_N(n, \ell)\rangle_{\natural} = W_N^{2} = e^{\mp 4\pi i n\ell/N} e_t ,
$$

a unit and not $e_t$. So the kernel is a unit at every root, and what fails at the central root is the identification of the inverse with a conjugation, not the invertibility.

### The Peirce Form of the Kernel

Substituting $\tilde{Ζ}=\tilde\Pi_+-\tilde\Pi_-$ in the closed form, or applying the exponential to each idempotent, gives the form the rest of the article uses.

**Proposition (the Peirce form).** For every $n$ and $\ell$,

$$
W_N(n, \ell) = e^{-2\pi i n\ell/N}\,\tilde\Pi_+ + e^{+2\pi i n\ell/N}\,\tilde\Pi_- .
$$

*Proof.* The two idempotents are orthogonal and their sum is the unit, so the exponential acts on each by the scalar attached to it, $\exp(-2\pi i\theta\tilde{Ζ})\tilde\Pi_\pm=\exp(\mp 2\pi i\theta)\tilde\Pi_\pm$, because $\tilde{Ζ}\tilde\Pi_\pm=\pm\tilde\Pi_\pm$; the two terms add.

Three consequences are read off at once. **The kernel is a pair of conjugate unit complex numbers**, $e^{-2\pi i n\ell/N}$ on the component of $\tilde\Pi_+$ and its conjugate on the component of $\tilde\Pi_-$, which is the form in which the transform factorizes. **The kernel is never a zero divisor**, since each of its two Peirce coordinates is a nonzero complex number: it stays a unit and never approaches the null cone, at any root and any index.

## The Roots of One

### The Classification

The classification is quoted, because it belongs to the root theory and not to harmonic analysis.

**Theorem (the roots of one; quoted).** In the plain product the roots of $+1$ are the central pair $\pm e_t$ and the pure elements $\vec{Ζ}$ with $(\vec{Ζ},\vec{Ζ})=-1$, a family of real dimension four. Writing $\vec{Ζ}=\vec p+i\vec p'$ over two real vectors, the pure roots are the pairs with $\vec p^{2}-\vec p'^{2}=-1$ and $\vec p\cdot\vec p'=0$, and they contain the purely imaginary unit vectors $i\vec u$ over the real unit vectors $\vec u$. The source is *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Value One in the Four General Products* and §*The Two Families of the Plain Reduction*.

**Corollary (a root is central or pure).** A root of $1$ has either a vanishing vector part, and is then $\pm e_t$, or a vanishing scalar part; no root has both parts non-zero.

*Proof.* The square is $\tilde{Ζ}^{2}=\bigl(Q_t^{2}-(\vec{Ζ},\vec{Ζ})\bigr)e_t+2Q_t\vec{Ζ}$. A square that is central has a vanishing vector part, so $2Q_t\vec{Ζ}=0$, and either $Q_t=0$ or $\vec{Ζ}=0$.

The two families are disjoint and exhaustive, so a statement that holds for every root has two cases and no third.

### The Hermitian Root

**Definition.** A root is **Hermitian** when $\tilde{Ζ}^{*}=\tilde{Ζ}$, the star being the Hermitian conjugation $\bar{\cdot}\circ{}^{\natural}$ of *Conventions in Mathematics*, §*The Conjugations*.

**Proposition (the Hermitian roots).** The Hermitian roots of $1$ are the central pair $\pm e_t$ and the purely imaginary unit vectors $\pm i\vec u$ over the real unit vectors $\vec u$.

*Proof.* A pure root has $\vec{Ζ}=\vec p+i\vec p'$ and $\tilde{Ζ}^{*}=\bar{\tilde{Ζ}}^{\natural}=-\bar{\tilde{Ζ}}=-\vec p+i\vec p'$, so the Hermitian condition is $\vec p=0$; the root condition $\vec p^{2}-\vec p'^{2}=-1$ then gives $\lvert\vec p'\rvert=1$. The central roots are fixed by the star.

For these roots the pair is a pair of Hermitian idempotents, $\tilde\Pi_\pm^{*}=\tilde\Pi_\pm$, that is, a pair of pure states, and the kernel is unitary for the Hermitian form, by §*Definition and the Closed Form* read with the star.

### The Sign of the Root

Replacing $\tilde{Ζ}$ by $-\tilde{Ζ}$ exchanges the two members of the Peirce pair, $\tilde\Pi_+\leftrightarrow\tilde\Pi_-$, and conjugates the two coordinates of the kernel:

$$
W_N(n, \ell; -\tilde{Ζ}) = \cos\theta\, e_t + i\sin\theta\,\tilde{Ζ} .
$$

For a pure root this is the natural conjugate of $W_N(n,\ell;\tilde{Ζ})$, and for the central root it is the coefficient conjugate. **The two transforms carry the same information.**

## The Discrete Transform Pair

### Definition

Let $f : \{0, 1, \ldots, N-1\} \to \mathbb{B}$ be a biquaternion-valued sequence. The **discrete biquaternion Fourier transform** of $f$ is the sequence $F : \{0, 1, \ldots, N-1\} \to \mathbb{B}$ defined by

$$
F[\ell] = \sum_{n=0}^{N-1} W_N(n, \ell) f[n], \qquad \ell \in \{0, 1, \ldots, N-1\},
$$

and the **inverse transform** is

$$
f[n] = \frac{1}{N} \sum_{\ell=0}^{N-1} W_N(n, -\ell) F[\ell], \qquad n \in \{0, 1, \ldots, N-1\}.
$$

The inverse kernel is the kernel at the negated frequency index, which is its inverse by §*Definition and the Closed Form*; written as a conjugation it is $W_N^{\natural}$ for a pure root and $\overline{W_N}$ at the central root.

The placement of the kernel on the **left** of $f[n]$ is a choice; with the kernel on the right,

$$
F[\ell] = \sum_{n=0}^{N-1} f[n] \, W_N(n, \ell).
$$

The two are related by conjugation: the natural conjugate of the left-kernel transform of $f$ is the right-kernel transform of $f^{\natural}$, the order reversing under $\natural$.

### Invertibility

**Theorem (inversion).** For every sequence $f$ and every root of $1$, the inverse formula reproduces $f[n]$. No hypothesis on the samples is needed.

*Proof.* Split the sequence into its left Peirce components, $f[n]=\tilde\Pi_+f[n]+\tilde\Pi_-f[n]$, which is the identity $e_t=\tilde\Pi_++\tilde\Pi_-$ applied on the left. The kernel commutes with the two idempotents and acts on them by the two characters, so the transform is

$$
F[\ell] = \sum_{n=0}^{N-1} e^{-2\pi i n\ell/N}\,\tilde\Pi_+ f[n] + \sum_{n=0}^{N-1} e^{+2\pi i n\ell/N}\,\tilde\Pi_- f[n],
$$

a pair of ordinary complex discrete transforms, the second taken at the frequency $-\ell$. Applying the inverse formula, the two sums separate in the same way and each is inverted by the standard orthogonality of the $N$-th roots of unity, giving $\tilde\Pi_+f[n]+\tilde\Pi_-f[n]=f[n]$.

The orthogonality relation the proof uses is

$$
\sum_{\ell=0}^{N-1} W_N(n, -\ell) W_N(m, \ell) = N\,\delta_{n,m}\, e_t,
$$

an identity in $\mathbb{C}[\tilde{Ζ}]$: the product is $W_N(m-n,\ell)$, which reads $\exp(2\pi i(m-n)\ell/N)$ in each Peirce coordinate, and the sum of the $N$-th roots of unity is $N$ at $n=m$ and $0$ otherwise.

**The inversion is unconditional.** Nothing in the proof uses the invertibility of a sample, so a sample of vanishing norm is recovered exactly. What a zero divisor obstructs is division, the subject of §*The Vanishing-Norm Issue*.

### Symmetry of the Spectrum

For a real scalar-valued sequence the spectrum satisfies a **conjugate symmetry**, as in the ordinary theory, and which conjugation appears is decided by the root.

**Theorem (conjugate symmetry).** Let $f : \{0, 1, \ldots, N-1\} \to \mathbb{R}e_t$ be a real scalar-valued sequence, and let $F$ be its transform with respect to the root $\tilde{Ζ}$. Then

$$
F[N-\ell] = F[\ell]^{\natural}, \qquad \ell = 1, \ldots, N-1,
$$

for a pure root, and

$$
F[N-\ell] = \overline{F[\ell]}, \qquad \ell = 1, \ldots, N-1,
$$

at the central root.

*Proof.* The kernel satisfies $W_N(n, N-\ell)=W_N(n, -\ell)$ for every root, because the argument changes by the integer multiple $2\pi n$ of the period. Hence

$$
F[N-\ell] = \sum_{n=0}^{N-1} W_N(n, -\ell) f[n] = \sum_{n=0}^{N-1} W_N(n, \ell)^{-1} f[n].
$$

For a pure root the inverse is the natural conjugate, and $\natural$ is an anti-automorphism fixing the real scalars, so the last sum is $\bigl(\sum_n W_N(n,\ell)f[n]\bigr)^{\natural}=F[\ell]^{\natural}$. At the central root the kernel is a complex scalar and the coefficient conjugate is the inverse, so the last sum is $\overline{F[\ell]}$.

The symmetry is the biquaternion analogue of the Hermitian symmetry $F[-\ell]=F[\ell]^{*}$ of the ordinary transform of a real sequence. For a quaternion-valued sequence the first identity fails, because $\natural$ neither fixes the values nor preserves the order.

## Factorization into Complex Fourier Transforms

### The Peirce Coordinates

Let $\tilde{Ζ}$ be the root and $\tilde\Pi_\pm=\tfrac12(e_t\pm\tilde{Ζ})$ its pair. The two left ideals

$$
\tilde\Pi_+\mathbb{B}=\{\tilde\Pi_+X : X\in\mathbb{B}\}, \qquad \tilde\Pi_-\mathbb{B}=\{\tilde\Pi_-X : X\in\mathbb{B}\}
$$

are complementary, $\mathbb{B}=\tilde\Pi_+\mathbb{B}\oplus\tilde\Pi_-\mathbb{B}$, and each is a complex plane: an idempotent has rank one in the matrix model $\mathbb{B}=M_2(\mathbb{C})$, so each ideal has complex dimension two. Every sequence splits accordingly,

$$
f[n] = f_+[n] + f_-[n], \qquad f_\pm[n] = \tilde\Pi_\pm f[n] \in \tilde\Pi_\pm\mathbb{B},
$$

and the split is canonical: it is fixed by the root and by nothing else.

### The Factorization

Substituting the Peirce form of the kernel and the split of the sequence,

$$
F[\ell] = \sum_{n=0}^{N-1} \left(e^{-2\pi i n\ell/N}\,\tilde\Pi_+ + e^{+2\pi i n\ell/N}\,\tilde\Pi_-\right)\left(f_+[n]+f_-[n]\right).
$$

Each of the four products lands in a Peirce plane and the two planes do not mix, so the sum separates into two independent transforms:

$$
F_+[\ell] = \sum_{n=0}^{N-1} e^{-2\pi i n\ell/N} f_+[n], \qquad F_-[\ell] = \sum_{n=0}^{N-1} e^{+2\pi i n\ell/N} f_-[n].
$$

**Proposition (the factorization).** For every root of $1$ and every sequence,

$$
F[\ell] = F_+[\ell] + F_-[\ell],
$$

where $F_+$ is the ordinary complex discrete transform of $f_+$ and $F_-$ is the ordinary complex transform of $f_-$ at the negated frequency; the two displays above are the proof, since $f_\pm$ already lies in the image of $\tilde\Pi_\pm$.

### The Count

Each of the two Peirce planes is $\mathbb{C}^{2}$, so writing $f_\pm$ in a complex basis of its plane turns each of the two transforms into two scalar complex transforms. **The full transform is therefore four scalar complex discrete transforms of length $N$**, a count that does not depend on the root and needs no case distinction: at the central root one idempotent vanishes, one plane carries the whole algebra, and the same two complex coordinates are transformed, which is again four scalar transforms.

The result is a fast algorithm: four complex FFTs of size $N$, so $O(N\log N)$ against $O(N^2)$ for the naive evaluation. Everything non-trivial is in the root, which supplies the pair of planes.

## The Convolution Theorem

### Definition of Convolution

Let $f, g : \mathbb{Z} \to \mathbb{B}$ be two biquaternion-valued sequences, extended to $\mathbb{Z}$ by $f[n] = g[n] = 0$ outside the support $\{0, 1, \ldots, N-1\}$. The **convolution** of $f$ and $g$ is

$$
(f * g)[n] = \sum_{m \in \mathbb{Z}} f[m] g[n - m].
$$

The convolution is **not commutative** in general, because the biquaternion product is not commutative; the order of the factors matters.

### The Convolution Theorem

**Theorem (convolution theorem).** Let $f, g$ be biquaternion-valued sequences with finite support, and let $\mathcal{F}$ denote the discrete biquaternion Fourier transform with the kernel on the left. Assume the kernel is **central on the values**, $W_N(n,\ell)a = aW_N(n,\ell)$ for every sample $a$ of $f$ and $g$ and all $n,\ell$; this holds in particular for the central root $\tilde{Ζ}=\pm e_t$, whose kernel is a complex scalar, and for every sequence whose values lie in $\mathbb{C}[\tilde{Ζ}]$. Then

$$
\boxed{\; \mathcal{F}[f * g][\ell] = \mathcal{F}[f][\ell] \cdot \mathcal{F}[g][\ell] \;},
$$

where the product on the right is the biquaternion product.

*Proof.* Compute

$$
\mathcal{F}[f * g][\ell] = \sum_{n=0}^{N-1} W_N(n, \ell) \sum_{m=0}^{N-1} f[m] g[n-m] = \sum_{m=0}^{N-1} \sum_{n=0}^{N-1} W_N(n, \ell) f[m] g[n-m].
$$

Change variables $n = m + k$, so that $W_N(n, \ell) = W_N(m, \ell) W_N(k, \ell)$, the kernel being multiplicative in the index because the exponential is. Then

$$
\mathcal{F}[f * g][\ell] = \sum_{m=0}^{N-1} \sum_{k=0}^{N-1} W_N(m, \ell) f[m]\, W_N(k, \ell) g[k],
$$

where the passage from the previous display moves $W_N(k,\ell)$ past $f[m]$, which the hypothesis permits. The double sum then factors as $\mathcal{F}[f][\ell]\cdot\mathcal{F}[g][\ell]$.

**Remark (a genuine root).** For a root other than $\pm e_t$ the kernel is not central and the hypothesis fails for arbitrary values, so the theorem is false as stated. At $n=m+k$ a term of the sum is $W_N(m,\ell)W_N(k,\ell)f[m]g[k]$, which equals $W_N(n,\ell)\,W_N(k,\ell)^{-1} f[m] W_N(k,\ell) g[k]$; the factor $W_N(k,\ell)^{-1}f[m]W_N(k,\ell)$ depends on $k$ and $\ell$ and cannot be absorbed into a coefficient $h[n]$. The sequence

$$
h_\ell[n] = \sum_{m+k=n} W_N(k,\ell)^{-1} f[m] W_N(k,\ell) g[k]
$$

does satisfy $\mathcal{F}[h_\ell] = \mathcal{F}[f]\mathcal{F}[g]$, but it depends on $\ell$, so it is not a convolution of $f$ and $g$ alone.

**Corollary (right-kernel case).** For the transform with the kernel on the right and the same hypothesis,

$$
\mathcal{F}_{\text{right}}[f * g][\ell] = \mathcal{F}_{\text{right}}[f][\ell] \cdot \mathcal{F}_{\text{right}}[g][\ell].
$$

The order is not reversed: the same computation moves the kernel past $g$ and leaves $f$ in front. Without the hypothesis neither the left-kernel nor the right-kernel statement holds in general.

### Consequences

Under the same hypothesis, convolution in the index domain is **biquaternion multiplication** in the frequency domain. The convolution is associative and distributive over addition, and not commutative: the complex case is commutative, the quaternion case is not, and the biquaternion case is the natural extension.

## The Vanishing-Norm Issue

### Samples of Vanishing Norm

A sample $f[n]$ with $\langle f[n]\rangle_{\natural}=0$ is a zero divisor, and by the inversion theorem of §*Invertibility* it is still recovered exactly. What the vanishing norm costs is arithmetic with the spectrum, not the transform.

**The natural norm is a seminorm.** It vanishes on the null cone, a real quadric of codimension two, so it cannot measure a spectrum and no Parseval identity can be stated in it. A zero-divisor entry also has no inverse, so such a spectrum cannot be divided by pointwise.

The kernel is never on the cone: its two Peirce coordinates are unit complex numbers, so the transform never loses rank for lack of a kernel, whatever the root.

### Consequences for the Transform

- **The transform is a bijection, at every root and for every sequence.** The inverse formula is an identity in the algebra and uses no hypothesis on the samples.
- **Pointwise division by the spectrum is defined exactly on the sequences whose spectrum avoids the null cone.** A convolution is undone by dividing the transform pointwise by the transform of the kernel, and that division exists at the frequency $\ell$ exactly when $F[\ell]$ is a unit.

### Structural Interpretation

The vanishing norm is a genuinely biquaternionic feature: it does not arise in the complex or quaternion transforms, whose algebras are division algebras, and in $\mathbb{B}$ the units are the complement of the null cone, so division is available off the cone and nowhere on it.

### The Open Question

Which sequences have a spectrum free of zero divisors is not decided by the norms of the samples. Each Peirce coordinate of $F[\ell]$ is a complex discrete transform, so $\ell\mapsto\langle F[\ell]\rangle_{\natural}$ is one trigonometric polynomial in $\omega=e^{2\pi i\ell/N}$, of degree at most $2(N-1)$; the question is a count of its real zeros, and it is not settled here.

## The Two-Dimensional Transform

### Definition

For a biquaternion-valued array $f : \{0, 1, \ldots, M-1\} \times \{0, 1, \ldots, N-1\} \to \mathbb{B}$, the **two-dimensional discrete biquaternion Fourier transform** is

$$
F[\ell, v] = \sum_{m=0}^{M-1} \sum_{n=0}^{N-1} W_M(m, \ell) \, f[m, n] \, W_N(n, v),
$$

where $W_M$ and $W_N$ are the one-dimensional kernels of lengths $M$ and $N$, taken for the same root.

### Factorization

The two-dimensional transform factorizes through the same Peirce pair: writing $f = f_+ + f_-$ with $f_\pm = \tilde\Pi_\pm f$, each component is a $\mathbb{C}^2$-valued array, transformed by the ordinary two-dimensional complex transform, the second at the negated frequency in both indices.

### Separability

The two-dimensional kernel is **separable**, in the sense that

$$
W_{M \times N}((m, n), (\ell, v)) = W_M(m, \ell) \, W_N(n, v).
$$

This follows from the multiplicativity of the exponential in the time index and the additivity of the exponent. The separability is what allows the two-dimensional transform to be computed as a sequence of one-dimensional transforms.

## Higher-Dimensional Transforms

The generalization is by $d$ kernels, one for each dimension, all for the same root. The transform of a biquaternion-valued function on $\{0, 1, \ldots, N_1 - 1\} \times \cdots \times \{0, 1, \ldots, N_d - 1\}$ factorizes into four scalar complex transforms per Peirce coordinate, and it is separable, so it is computed along the axes in turn.

## The Z Transform

### Definition

The transform above analyses a finite sequence; this one analyses an infinite sequence, and it is the discrete analogue of the Laplace transform rather than of the Fourier transform. Let $f = \{f_n\}_{n \ge 0}$ be a biquaternion-valued sequence. Its **Z transform** is

$$
\mathcal{X}[f](\tilde{Q}) = \sum_{n=0}^{\infty} f_n \tilde{Q}^{-n}, \qquad \tilde{Q} \in \mathbb{B}^{\times},
$$

the generating function of the sequence, and the variable ranges over the units of $\mathbb{B}$ because its negative powers occur in the definition. Substituting $\tilde{Q} = \exp(s)$ turns the sum into $\sum_n f_n \exp(-ns)$, the discrete Laplace transform of the sequence, and the region of convergence discussed below is the analogue of the half-plane of the continuous theory. Evaluating the transform at the $N$-th roots of unity instead, $\tilde{Q} = \exp(2\pi i \ell/N)$, returns the ordinary complex discrete Fourier transform of the periodisation of the sequence, which is the central root $\tilde{Ζ}=e_t$ of the transform pair above.

The sample $f_n$ is written on the **left** of the variable, so the variable plays the role that the kernel played above. This is the mirror image of the convention of the transform pair, and it is not neutral: the rules below move powers of $\tilde{Q}$ through the sequence, and with the variable placed on the left the $\tilde A$-scaling rule would require every sample to commute with $\tilde A$. The two conventions are interconverted by the quaternion conjugate. Writing

$$
\mathcal{Y}[f](\tilde{Q}) = \sum_{n=0}^{\infty} \tilde{Q}^{-n} f_n
$$

for the transform with the variable on the left,

$$
(\mathcal{X}[f](\tilde{Q}))^{\natural} = \mathcal{Y}[f^{\natural}](\tilde{Q}^{\natural}),
$$

because quaternion conjugation reverses products and $(\tilde{Q}^{-1})^{\natural} = (\tilde{Q}^{\natural})^{-1}$.

### The Region of Convergence

Two norms describe the size of a biquaternion, and the choice between them is the whole difficulty of the convergence question. The **Euclidean norm** $\lVert\tilde{Q}\rVert = \left(\sum_\mu \lvert Q_\mu\rvert^2\right)^{1/2}$ is the norm of the metric structure of *Biquaternion Analysis*; the **multiplicative real norm** $r(\tilde{Q}) = \sqrt{\lvert \langle\tilde{Q}\rangle_{\natural}\rvert}$ is the unique real norm that is multiplicative and normalised on the real scalars, by *N-Regularity and N-Degeneracy in the Biquaternion Algebra*. Only the second reduces the question to scalars, because only the second is multiplicative:

$$
r(f_n \tilde{Q}^{-n}) = r(f_n)\,r(\tilde{Q})^{-n}.
$$

So a sequence that grows at most geometrically, $r(f_n) \le \sigma_f^{\,n}$, has terms of seminorm tending to zero as soon as $r(\tilde{Q}) > \sigma_f$, and the Z-transform literature takes the **region of convergence** to be this set, with $\sigma_f$ the **radius of convergence**. Two corrections come from the vanishing of $r$ on the zero divisors.

**Vanishing of the seminorm is not convergence.** The standard idempotent of *Idempotents* is the one attached to the root $i\vec e_z$ of $+1$: here $(i\vec e_z)^2 = e_t$, and the two idempotents $\tilde\Pi_+ = \tfrac12(e_t+i\vec e_z)$ and $\tilde\Pi_- = \tfrac12(e_t-i\vec e_z)$ are its associated idempotents.

$$
\tilde\Pi_+ = \tfrac12(e_t + i\vec e_z), \qquad \tilde\Pi_+^2 = \tilde\Pi_+, \qquad \langle\tilde\Pi_+\rangle_{\natural} = 0, \qquad r(\tilde\Pi_+) = 0,
$$

and its powers are $\tilde\Pi_+^{\,k} = \tilde\Pi_+$ for $k \ge 1$. Multiplicativity of $r$ then gives

$$
r(\tilde\Pi_+^{\,k}) = r(\tilde\Pi_+)^k = 0 \qquad\text{for every } k,
$$

so every term of the geometric series $\sum_k \tilde\Pi_+^{\,k}$ has seminorm zero, while the partial sums

$$
S_K = \sum_{k=0}^{K-1} \tilde\Pi_+^{\,k} = e_t + (K-1)\tilde\Pi_+, \qquad r(S_K) = \sqrt{K},
$$

are unbounded in both norms. The point lies inside the claimed region $r(\tilde{Q}) < 1$, and the geometric identity

$$
\sum_{k=0}^{\infty} \tilde{Q}^{k} = (e_t - \tilde{Q})^{-1}
$$

fails there, because $e_t - \tilde\Pi_+ = \tilde\Pi_-$ is the complementary idempotent and is again a zero divisor. The series converges exactly when the powers $\tilde{Q}^k$ tend to zero, equivalently, the algebra being finite-dimensional, when every eigenvalue of $\tilde{Q}$, read in the $2\times2$ complex matrix representation of *$M_2(\mathbb{C})$ Pauli Representation*, has modulus less than one; the sum is then $(e_t - \tilde{Q})^{-1}$, as the identity $(e_t - \tilde{Q})S_K = e_t - \tilde{Q}^K$ shows. The obstruction is the summation and not the multiplication: a finite sum of products is always defined, and only the passage to the limit fails.

**The seminorm radius is the geometric mean of the eigenvalues.** By the same representation the eigenvalues $\lambda_1, \lambda_2$ of $\tilde{Q}$ satisfy $\lambda_1\lambda_2 = \langle\tilde{Q}\rangle_{\natural}$, so $r(\tilde{Q}) = \sqrt{\lvert\lambda_1\lambda_2\rvert}$ is the geometric mean of their moduli. The region in which the series in $\tilde{Q}^{-1}$ actually converges is governed by the smaller of the two: for a positive real $c$ the series $\sum_k (c\tilde{Q}^{-1})^k$ converges exactly when $c < \min(\lvert\lambda_1\rvert, \lvert\lambda_2\rvert)$. The geometric mean never falls below the minimum, so the region $r(\tilde{Q}) > \sigma_f$ always **contains** the true region and may contain divergent points. For

$$
\tilde{Q} = 3e_t + i\vec e_x, \qquad \langle\tilde{Q}\rangle_{\natural} = 8, \qquad r(\tilde{Q}) = 2\sqrt2 \approx 2.83,
$$

the eigenvalues are $4$ and $2$. With $\sigma_f = 2.5$ the point lies in the region, although $\sum_k (2.5\,\tilde{Q}^{-1})^k$ diverges, its partial sums reaching Euclidean norm $6.8 \times 10^{19}$ at $k = 200$. For an element with real quaternion coordinates the two eigenvalues are conjugate, $r$ is their common modulus, and the two regions coincide, so the correction concerns the biquaternions proper and not the quaternion subspace. In the applications the variable is a complex scalar, where $\tilde{Q}^{-n}$ has norm $\lvert \tilde{Q}\rvert^{-n}$ and the classical theory of the complex Z transform carries over to the coefficients unchanged.

### The Calculation Rules

Each row below is an identity of series, valid wherever the series concerned converge; the rows built from the central calculus carry the commutation hypothesis displayed with them. The sequences are $f$ and $g$, the constants are $c_1, c_2$, the bases are $\tilde Q_1, \tilde A \in \mathbb{B}$, and $k$ is a non-negative integer.

| Property | Sequence | Transform |
|---|---|---|
| Left linearity | $c_1f + c_2g$ | $c_1\mathcal{X}[f](\tilde{Q}) + c_2\mathcal{X}[g](\tilde{Q})$, for any constants |
| Right linearity | $fc_1 + gc_2$ | $\mathcal{X}[f](\tilde{Q})c_1 + \mathcal{X}[g](\tilde{Q})c_2$, for $c_1\tilde{Q} = \tilde{Q}c_1$ and $c_2\tilde{Q} = \tilde{Q}c_2$ |
| Two-sided linearity | $c_1f + gc_2$ | $c_1\mathcal{X}[f](\tilde{Q}) + \mathcal{X}[g](\tilde{Q})c_2$, for $c_2\tilde{Q} = \tilde{Q}c_2$ |
| $\tilde A$-scaling | $f_n\tilde A^n$ | $\mathcal{X}[f](\tilde A^{-1}\tilde{Q})$, for $\tilde A\tilde{Q} = \tilde{Q}\tilde A$ |
| $n$-scaling | $nf_n$ | $-\tilde{Q}\,\dfrac{d}{d\tilde{Q}}\mathcal{X}[f](\tilde{Q})$, for $\tilde{Q}$ central |
| Shifting | $f_{n+k}$ | $\mathcal{X}[f](\tilde{Q})\tilde{Q}^{k} - \sum_{n=0}^{k-1} f_n\tilde{Q}^{k-n}$ |
| Inverse shifting | $f_{n-k}$ ($0$ for $n<k$) | $\mathcal{X}[f](\tilde{Q})\tilde{Q}^{-k}$ |
| Convolution | $\sum_{j=0}^{n} f_{n-j}g_j$ | $\mathcal{X}[f](\tilde{Q})\mathcal{X}[g](\tilde{Q})$, for $\tilde{Q}$ central |

The shifting rows need no hypothesis, because $\tilde{Q}^{-(n+k)} = \tilde{Q}^{-n}\tilde{Q}^{-k}$ for the powers of a single element. The $\tilde A$-scaling row compares $(\tilde A\tilde{Q}^{-1})^n$ with $\tilde A^n\tilde{Q}^{-n}$ and therefore needs $\tilde A\tilde{Q} = \tilde{Q}\tilde A$, and the convolution row needs each $g_j$ to commute with $\tilde{Q}$, which the centrality of $\tilde{Q}$ supplies. The linearity rows show where the non-commutativity bites: a constant written on the right of a sequence may be moved outside the transform only if it commutes with the variable.

### The Elementary Sequences

In the table below the entry $n$ abbreviates the sequence $ne_t$, and the variable is a complex scalar, the case used in the applications. The rows whose base is a biquaternion carry the commutation hypotheses displayed, and the two scalar rows use the $n$-scaling rule, which a complex scalar satisfies.

| $f_n$ | $\mathcal{X}[f](\tilde{Q})$ |
|---|---|
| $e_t$ | $(e_t - \tilde{Q}^{-1})^{-1}$ |
| $n$ | $\tilde{Q}(\tilde{Q} - e_t)^{-2}$ |
| $n^2$ | $(\tilde{Q} + \tilde{Q}^2)(\tilde{Q} - e_t)^{-3}$ |
| $\tilde Q_1^n$, for $\tilde Q_1\tilde{Q} = \tilde{Q}\tilde Q_1$ | $(e_t - \tilde Q_1\tilde{Q}^{-1})^{-1}$ |
| $n\tilde Q_1^n$, for $\tilde Q_1\tilde{Q} = \tilde{Q}\tilde Q_1$ | $\tilde Q_1\tilde{Q}^{-1}(e_t - \tilde Q_1\tilde{Q}^{-1})^{-2}$ |
| $\dfrac{\tilde A^n}{n!}$, for $\tilde A\tilde{Q} = \tilde{Q}\tilde A$ | $\exp(\tilde A\tilde{Q}^{-1})$ |

### Recurrence Relations

The purpose of the transform is the solution of linear recurrences with constant biquaternion coefficients,

$$
\sum_{m=0}^{M} f_{n+m}p_m = g_n, \qquad n \ge 0,
$$

where the coefficients $p_m$ are biquaternions and the right-hand side $g$ is a known sequence. Transforming both sides with the shifting and linearity rules converts the recurrence into an algebraic equation for $\mathcal{X}[f]$, which is solved in the algebra; the sequence is then read off the table of elementary sequences. It is the discrete analogue of the Laplace-transform solution of a linear differential equation with constant coefficients.

**Example.** Let $\vec Q = \vec e_x + \vec e_y$, so that $\vec Q^2 = -2e_t$, and let

$$
f_{n+2} = f_{n+1}(\vec Q - e_t) + f_n\vec Q, \qquad f_0 = e_t, \qquad f_1 = \vec Q .
$$

Transforming both sides and using the shifting rule, with $\tilde{Q}$ central,

$$
\tilde{Q}^2\bigl(\mathcal{X}[f] - e_t - \vec Q\tilde{Q}^{-1}\bigr) = \tilde{Q}\bigl(\mathcal{X}[f] - e_t\bigr)(\vec Q - e_t) + \mathcal{X}[f]\vec Q,
$$

which, after $e_t\vec Q = \vec Q$ and $e_t^2 = e_t$, is the linear equation

$$
\mathcal{X}[f](\tilde{Q})\,(\tilde{Q}^2 + \tilde{Q} - \tilde{Q}\vec Q - \vec Q) = \tilde{Q}^2 + \tilde{Q} .
$$

The left factor is the product $(\tilde{Q} + e_t)(\tilde{Q} - \vec Q)$ of two commuting factors, and $\tilde{Q}^2 + \tilde{Q} = \tilde{Q}(\tilde{Q} + e_t)$, so

$$
\mathcal{X}[f](\tilde{Q}) = \tilde{Q}(\tilde{Q} - \vec Q)^{-1} = (e_t - \vec Q\tilde{Q}^{-1})^{-1}.
$$

By the table this is the transform of the sequence $f_n = \vec Q^n$, which satisfies the recurrence because $\vec Q^{n+1}(\vec Q - e_t) + \vec Q^{n+1} = \vec Q^{n+2}$, and satisfies the initial values. The solution is

$$
f_n = (\vec e_x + \vec e_y)^n, \qquad n \ge 0 .
$$

An inhomogeneous recurrence is treated in the same way: the transform of the known right-hand side is inserted, the resulting equation for $\mathcal{X}[f]$ is decomposed in powers of $\tilde{Q}^{-1}$, and each term is read off the table.


## The Commutative Alternative: The Reduced Biquaternion Transform

Everything in this article is the transform of $\mathbb{B}$, whose product is non-commutative and whose convolution theorem therefore fixes the kernel to one side. A commutative four-dimensional algebra has a discrete transform of its own, due to Pei, Chang and Ding, and it is the corpus's only worked instance of a discrete hypercomplex transform over a commutative algebra; it is recorded here because it is the case in which the phenomena of the previous sections disappear.

The algebra is $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\oplus\mathbb{C}$, the reduced biquaternion algebra of *List of Algebras by Dimension*, and the transform is the **discrete reduced biquaternion Fourier transform**. Two kernel conventions are used, with two imaginary units or with one; the sequence is split by the idempotents into two complex sequences, so either type costs two complex DFTs, the same count the quaternion transform costs.

The convolution theorem is the sharpest contrast with the theorem of this article. The convolution here is commutative, the kernel needs no side convention, and the product in the frequency domain is the transform of the convolution for either type; the paper reports that for the quaternion transform the corresponding identity holds only in a restricted one-side form, which is consistent with the one-sided theorem proved above for $\mathbb{B}$ and with its loss of commutativity.

The price is the vanishing-norm phenomenon of the previous section, which the commutative algebra has as well: the norm is the determinant, it vanishes on two ideals, and the transform has no single magnitude to be stationary in. The applications the paper gives are to colour, where the four dimensions are matched to a three-dimensional colour space; the redundancy is removed by a **simplified polar form**, treated with the other polar forms of the family in *The Polar Decomposition of an N-Regular Biquaternion*.


## Open Questions

1. **A kernel from a genuine root.** For a root other than $\pm e_t$ no frequency-independent convolution reproduces the product of the transforms, by the remark of §*The Convolution Theorem*. Whether a twisted product, or a convolution carrying the root as data, repairs this is not known.

2. **Frequency analysis of a sequence.** Can a biquaternion distribution of a sequence over the index and the frequency be defined, what are its invariance properties, and does the choice of root enter it?

3. **Non-commutative convolution.** What are the implications of the non-commutativity of the biquaternion product for the convolution theorem? Convolution is not commutative, and the classical convolution theorem assumes commutativity.

4. **The spectrum and vanishing norms.** Whether a spectrum can meet the null cone is not settled here. The transform is a bijection regardless, so the question is whether a convolution can be undone pointwise, and it is a question about the zeros of one trigonometric polynomial, as §*The Open Question* states.

5. **The relation to the continuous transform.** How does the discrete transform relate to the continuous transform of the companion article? The sampling and periodization theorems should be stated in the Peirce coordinates, where they are statements about two complex sequences.

## Summary

The discrete biquaternion Fourier transform is defined by the kernel $W_N(n, \ell) = \exp(-2\pi i\tilde{Ζ} n\ell/N)$, where $\tilde{Ζ}$ is a root of $1$ in $\mathbb{B}$. The root of $1$ is the parameter, not a root of $-1$: the complex scalar $i$ in the exponent supplies the sign, and the algebra element carries only the square $e_t$.

The root is an idempotent pair. The halving map $\tilde{Ζ}\mapsto\tfrac12(e_t+\tilde{Ζ})$ is a bijection between the roots of $1$ and the idempotents, and the kernel is a pair of conjugate unit complex numbers, one on each Peirce ideal $\tilde\Pi_\pm\mathbb{B}$. The transform is the pair of ordinary complex transforms on those ideals, that is four scalar complex transforms of length $N$, which gives a fast algorithm.

The transform is invertible at every root and for every sequence, by the orthogonality of the inverse kernel. That inverse is the kernel at the negated frequency index, at every root without exception; it is the natural conjugate for every pure root and the coefficient conjugate at the central roots $\pm e_t$. The conjugate symmetry for real scalar sequences carries the same dichotomy. The convolution theorem holds when the kernel commutes with the samples, in particular at the central root; for a genuine root no frequency-independent convolution reproduces the product of the transforms.

The vanishing norm does not obstruct inversion; it obstructs division, and the sequences whose spectrum avoids the null cone are exactly those whose convolutions can be undone pointwise.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, $M_2(\mathbb{C})$ as a complex algebra |
| $e_t, \vec e_x, \vec e_y, \vec e_z$ | the unit and the three vector units, with $\vec e_k^{2}=-e_t$ |
| $i$ | the complex scalar imaginary, commuting with the units |
| $\tilde{Ζ}$ | a root of $1$, $\tilde{Ζ}^{2}=e_t$ |
| $\vec{Ζ}$ | a pure root of $1$, $(\vec{Ζ},\vec{Ζ})=-1$ |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\tilde{Ζ})$ | the idempotent pair of the root, $\tilde{Ζ}=\tilde\Pi_+-\tilde\Pi_-$ |
| $\mathbb{B}=\tilde\Pi_+\mathbb{B}\oplus\tilde\Pi_-\mathbb{B}$ | the Peirce decomposition into two complex planes |
| $W_N(n,\ell) = \exp(-2\pi i\tilde{Ζ} n\ell/N)$ | the discrete Fourier kernel, placed on the left of $f[n]$ |
| $\cos\theta\,e_t - i\sin\theta\,\tilde{Ζ}$ | the closed form of the kernel, $\theta=2\pi n\ell/N$ |
| $W_N(n,-\ell)=W_N(n,\ell)^{-1}$ | the inverse kernel, at every root |
| $F[\ell]$ | the transform of the sequence $f[n]$ |
| $f = f_+ + f_-$ | the split into the two Peirce components |
| $\mathcal{F}[f * g] = \mathcal{F}[f]\,\mathcal{F}[g]$ | the convolution theorem, under the centrality hypothesis |
| $\natural$ | the quaternion conjugation, $e_t\mapsto e_t$, $\vec e_k\mapsto-\vec e_k$ |
| $*$ | the Hermitian conjugation, $\bar{\cdot}\circ\natural$ |
| $\langle\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}$ | the natural norm, a complex scalar |
| $\overline{W_N}$ | the coefficient conjugate of the kernel |
| $N$ | the length of the transform |
| $\mathbb{Z}/N$ | the index group |

## Further Reading

- [Biquaternion Continuous Harmonic Analysis](biquaternion-continuous-harmonic-analysis.html), for the continuous kernel, the classification of the roots of $1$ and the Peirce form behind every statement here.
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential, the de Moivre formula and the idempotents of the biquaternion algebra.
- *Square Roots of One and the Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, for the classification of the roots of $1$ and the halving map.
- [Special Element and Peirce Conventions](special-element-and-peirce-conventions.html), for the root glyph, the idempotent family and the Peirce table.
- [Reduced Biquaternion Discrete Harmonic Analysis](reduced-biquaternion-discrete-harmonic-analysis.html), for the commutative case and its four-dimensional discrete transform.
- [Harmonic Analysis over Hypercomplex Systems](harmonic-analysis-over-hypercomplex-systems.html), for the place of the transform among the eight systems.
- [Quaternion Fourier Transform: Properties and Convolution Theorems](quaternion-fourier-transform-properties-and-convolution-theorems.html), for the quaternion case and the one-sided form of its convolution theorem.
- *Commutative Reduced Biquaternions and Their Fourier Transform*, for the reduced biquaternion transform and the two kernel conventions of the commutative case.
- [Conventions in Mathematics](algebra-and-element-conventions.html), for the units, the conjugations and the norms.
