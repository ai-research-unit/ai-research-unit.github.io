# __The Bochner Theorem for the Biquaternion Transform: the Hermitian Form and the Root__

## Introduction

Bochner's theorem says that a continuous normalised positive-definite function on a group is the Fourier transform of a positive measure. Read in the other direction it says that **the transform of a positive measure is a positive-definite function**, and its proof consumes two properties of the character — that it is multiplicative under the group law, and that it is unitary — together with one property of the pairing, that the quadratic form carries the conjugation in its **second** slot.

In the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ each of these ingredients becomes a choice. The kernel of the transform is the exponential of a **root of $-1$**, and the roots fall into three families. The algebra carries four pairings, two bilinear and two sesquilinear, and the classical statement sits in one of the sesquilinear rows. The article therefore asks the single question such a situation forces: **which pairing makes the theorem true, and for which roots?**

The answer, and the content of the article, is one sentence. The positivity the theorem needs is the positivity of the general plain sesquilinear form $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$, positive definite of signature $(8,0)$, and with that form the theorem holds exactly for the roots that are **skew-adjoint** for the Hermitian conjugation, $\tilde\Xi^{*}=-\tilde\Xi$ — the scalar imaginary $\tilde\Xi=\pm i$ and the real roots $\tilde\Xi=\pm\mu$ — and fails for the **genuinely complex** roots $\tilde\Xi=b\mu+d\nu i$. The failure recorded in *Biquaternion Continuous Harmonic Analysis* at the central element $i$ is a different statement: it tests the bilinear form $N$, it is independent of the root, and it belongs to the metric and not to the positivity. Both statements are true, and they are not the same statement.

**Boundaries.** The transform, its kernel, the classification of the roots, the factorisation into four complex transforms and the vanishing-norm issue are *Biquaternion Continuous Harmonic Analysis* and *Biquaternion Discrete Harmonic Analysis*; the transform of a measure and its quadratic form with the natural conjugation are the section §*The Transform of a Measure, and the Failure of Positivity* of the continuous article, whose eighth open question this article answers. The positivity of the form, its cone and its signature are *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint* and *Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions*; the classical theorems are *Positive Definite Functions and Hermitian Kernels*, *Reproducing Kernel Hilbert Spaces* and *Positive Definite Distributions*; the quaternion case that does hold is *Quaternion Harmonic Analysis*. The four pairings are *The Four Pairings of the Biquaternion Algebra*; the roots are *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*; the notation is *Conventions in Mathematics*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity, $e_k^{2}=-e_0$ and $e_je_k=e_l$ for $(j,k,l)$ a cyclic permutation of $(1,2,3)$; a general element is $\tilde Q=Q_0e_0+\mathbf Q$ with $Q_\mu\in\mathbb{C}$. The **coefficientwise conjugation** $\overline{\cdot}$ conjugates the coefficients; the **natural conjugation** ${}^{\natural}$ fixes $e_0$ and negates $e_1,e_2,e_3$ and is $\mathbb{C}$-linear; the **Hermitian conjugation** is ${}^{*}=\overline{\cdot}\circ{}^{\natural}$, so $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ with $\varepsilon=(1,-1,-1,-1)$. The four pairings are $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$, $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$ and $\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$, and $\mathrm{Tr}=2\,\mathrm{Sc}$. A **root** is an element $\tilde\Xi$ with $\tilde\Xi^{2}=-e_0$; following the physics companion, the roots of the first and second families of the classification — the scalar imaginary $\tilde\Xi=\pm i$ and the unit real roots $\tilde\Xi=\pm\mu$ — are called **degenerate**, and the roots $\tilde\Xi=b\mu+d\nu i$ with $\mu\perp\nu$ unit real and $b^{2}-d^{2}=1$ are called **genuinely complex**. The transform articles write the root $\rho$ and the kernel $W$; this article follows *Conventions in Mathematics* and writes $\tilde\Xi$ and $\chi$, the two being the same objects. All conventions are those of *Conventions in Mathematics*.

## The Statement and What Its Proof Consumes

### Bochner's Theorem in the Classical Case

Let $\mu$ be a finite positive measure on $\mathbb{R}^n$ and let

$$
\varphi(\omega)=\int_{\mathbb{R}^n}e^{-2\pi i\langle\omega,x\rangle}\,d\mu(x)
$$

be its transform, normalised so that $\varphi(0)=\mu(\mathbb{R}^n)$ is the total mass. Bochner's theorem says that a continuous $\varphi$ with $\varphi(0)\geq 0$ is of this form **exactly when** it is positive definite in the sense that

$$
\sum_{k,l=1}^{N}\overline{\zeta_k}\zeta_l\,\varphi(\omega_k-\omega_l)\geq 0
$$

for every finite set of frequencies and every set of complex coefficients. The forward direction is one line: because $e^{-2\pi i\langle\omega_k-\omega_l,x\rangle}=e^{-2\pi i\langle\omega_k,x\rangle}\overline{e^{-2\pi i\langle\omega_l,x\rangle}}$, the sum is $\int\lvert\sum_k\zeta_ke^{-2\pi i\langle\omega_k,x\rangle}\rvert^{2}d\mu$, a modulus squared integrated against a positive measure.

Two properties of the character $e^{-2\pi i\langle\omega,x\rangle}$ are used, and no others. It is **multiplicative**, which is what identifies the difference of frequencies with a product; and it is **unitary**, $\overline{e^{-2\pi i\langle\omega,x\rangle}}=\bigl(e^{-2\pi i\langle\omega,x\rangle}\bigr)^{-1}$, which is what turns the conjugate of one factor into the inverse of the other. The third ingredient is that the quadratic form is built with the conjugation in the **second slot**, which is what places the modulus squared under the integral.

### The Transform of a Measure in $\mathbb{B}$

Fix a root $\tilde\Xi$ of $-1$ and let the biquaternion kernel be

$$
\chi_\omega(x)=\exp\bigl(-2\pi\tilde\Xi\,\langle\omega,x\rangle\bigr)=\cos\bigl(2\pi\langle\omega,x\rangle\bigr)e_0-\sin\bigl(2\pi\langle\omega,x\rangle\bigr)\tilde\Xi ,
$$

the two-term closure of the exponential. For a finite positive measure $\mu$ on $\mathbb{R}^n$ the **transform of the measure** is the $\mathbb{B}$-valued function

$$
G(\omega)=\int_{\mathbb{R}^n}\chi_\omega(x)\,d\mu(x),\qquad G(0)=\mu(\mathbb{R}^n)e_0 .
$$

The definitions, the inversion and the factorisation of this transform are *Biquaternion Continuous Harmonic Analysis*; they are recalled here because the theorem is a statement about them, and nothing in the present article depends on a convergence hypothesis that article does not already make. Every ingredient of the classical proof now has a choice. The value $G(\omega)$ is an element of a non-commutative algebra, so the quadratic form must say which conjugation stands between the two coefficients; and the character is $\mathbb{B}$-valued, so its unitarity is a statement about $\tilde\Xi$.

### Multiplicativity Is Not in Question

The character is multiplicative for every root, and this is the one ingredient that is never lost:

$$
\chi_\omega\chi_\eta=\exp\bigl(-2\pi\tilde\Xi\langle\omega+\eta,x\rangle\bigr)=\chi_{\omega+\eta},\qquad \chi_\omega^{-1}=\chi_{-\omega},
$$

because the two exponentials share the single root $\tilde\Xi$, which commutes with itself. In particular the difference of frequencies always reassembles as a product, $\chi_{\omega_k-\omega_l}=\chi_{\omega_k}\chi_{\omega_l}^{-1}$. What is at stake is therefore not multiplicativity but **unitarity**: whether the inverse of the character is its Hermitian conjugate.

## Unitarity of the Character and the Root

### The Three Families

The roots of $-1$ fall into three families (*Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*), and the whole positivity question divides along them.

| Family | Form of $\tilde\Xi$ | $\tilde\Xi^{\natural}$ | $\tilde\Xi^{*}$ |
|---|---|---|---|
| scalar imaginary | $\pm i$ | $+i$ | $-i$ |
| real | $\pm\mu$, $\mu$ unit real | $-\mu$ | $-\mu$ |
| genuinely complex | $b\mu+d\nu i$, $\mu\perp\nu$, $b^{2}-d^{2}=1$ | $-b\mu-d\nu i$ | $-b\mu+d\nu i$ |

The distinction of the columns is the point of the table: the natural conjugation acts on the quaternion factor alone, while the Hermitian conjugation conjugates the complex coefficients as well, and for the genuinely complex roots the two disagree on the sign of the $d\nu i$ term. The first two families are the **degenerate** roots of the physics companion, and the criterion below singles them out.

### The Character Is Unitary Exactly for a Skew-Adjoint Root

**Proposition.** For the kernel $\chi_\omega$ of a root $\tilde\Xi$, the Hermitian adjoint equals the inverse,

$$
\chi_\omega^{*}=\chi_\omega^{-1},
$$

**exactly when** $\tilde\Xi^{*}=-\tilde\Xi$, and this holds exactly for the degenerate roots.

*Proof.* From $\chi_\omega=\cos\theta\,e_0-\sin\theta\,\tilde\Xi$ and $\chi_\omega^{-1}=\cos\theta\,e_0+\sin\theta\,\tilde\Xi$, with $\theta=2\pi\langle\omega,x\rangle$, one reads $\chi_\omega^{*}=\cos\theta\,e_0-\sin\theta\,\tilde\Xi^{*}$, so the two agree for all $\omega$ and $x$ exactly when $\tilde\Xi^{*}=-\tilde\Xi$. Write $\tilde\Xi=a_0e_0+v$ with $a_0\in\mathbb{C}$ and $v=\sum_{k\geq1}a_ke_k$; the condition $\tilde\Xi^{*}=-\tilde\Xi$ is $\overline{a_0}=-a_0$ and $\overline{a_k}=a_k$, that is $a_0=i\theta$ with $\theta$ real and $v$ a real quaternion. Imposing $\tilde\Xi^{2}=-e_0$ on $\tilde\Xi=i\theta e_0+v$ gives $-\theta^{2}+\lvert v\rvert^{2}=-1$ and $2i\theta v=0$, hence either $\theta=0$, which is the real roots $v$ of unit length, or $v=0$, which is the scalar imaginary $\theta=\pm1$. These are the degenerate roots and no others.

The proposition is the exact biquaternion form of the classical unitarity of the character, and it is **root-dependent**, which the corpus's own statement of unitarity is not: *Biquaternion Continuous Harmonic Analysis*, §*The Fourier Kernel*, records $\chi_\omega^{\natural}=\chi_\omega^{-1}$ for a pure root, which uses the **natural** conjugation, and this holds for the pure roots — the real and the genuinely complex — while the scalar imaginary is read there as the exception. **The corpus is not wrong.** $\chi_\omega^{\natural}=\chi_\omega^{-1}$ is the correct statement about the norm's conjugation, and it answers a different question from the one asked here: whether the *norm* of the character is the identity, rather than whether the character is unitary for the conjugation a positive-definite function uses. Read with the Hermitian conjugation, which is that conjugation, the scalar imaginary is not an exception at all — it is one of the two degenerate families for which the character is unitary.

### The Natural Conjugation Is a Different Statement

The biquaternion norm of the kernel is the natural square, $N(\chi_\omega)=\chi_\omega\chi_\omega^{\natural}=(\cos^{2}\theta+\sin^{2}\theta)e_0=e_0$ for every pure root — the real and the genuinely complex — and it is not the identity only for the scalar imaginary. The two unitarity statements must therefore be kept apart:

| Reading | Condition | Holds for |
|---|---|---|
| Hermitian, $\chi_\omega^{*}=\chi_\omega^{-1}$ | $\tilde\Xi^{*}=-\tilde\Xi$ | scalar imaginary and real (the degenerate roots) |
| natural, $\chi_\omega^{\natural}=\chi_\omega^{-1}$ | $\tilde\Xi^{\natural}=-\tilde\Xi$ | pure roots: real and genuinely complex (the scalar imaginary excluded) |

The Hermitian row is the one a positive-definite function uses, because a positive-definite function is sesquilinear; the natural row is the one the norm identity of the continuous article uses, and it belongs to the metric.

## Positivity of the Transform

### The Sesquilinear Quadratic Form

For coefficients $A_1,\dots,A_N$ in $\mathbb{B}$ and frequencies $\omega_1,\dots,\omega_N$ put

$$
Q(A)=\sum_{k,l=1}^{N}A_k\,G(\omega_k-\omega_l)\,A_l^{*} .
$$

This is the biquaternion quadratic form of the transform, with the Hermitian conjugation in the second slot — the slot the classical proof conjugates and the slot the general plain sesquilinear form uses. The theorem is the statement that $Q(A)$ lies in the Hermitian cone $P=\{\tilde Q\tilde Q^{*}\}$ of *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* for every choice of coefficients, which is the algebraic form of the scalar inequality of the classical case.

### The Factorisation, and the Degenerate Roots

Let $\tilde\Xi$ be degenerate, so that $\chi_\omega^{*}=\chi_\omega^{-1}$ by the proposition. Substituting $G(\omega_k-\omega_l)=\int\chi_{\omega_k}\chi_{\omega_l}^{-1}d\mu=\int\chi_{\omega_k}\chi_{\omega_l}^{*}d\mu$,

$$
Q(A)=\int_{\mathbb{R}^n}\Bigl(\sum_{k}A_k\chi_{\omega_k}\Bigr)\Bigl(\sum_{l}A_l\chi_{\omega_l}\Bigr)^{*}\,d\mu=\int_{\mathbb{R}^n}Z\,Z^{*}\,d\mu,\qquad Z=\sum_{k}A_k\chi_{\omega_k} .
$$

The element $ZZ^{*}$ is Hermitian, $(ZZ^{*})^{*}=ZZ^{*}$, and in the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$, whose representation $\mathsf{M}_2$ is a $*$-homomorphism, it is the matrix $\mathsf{M}_2(Z)\mathsf{M}_2(Z)^{\dagger}$, positive semidefinite. An integral of positive elements against a positive measure is positive, so $Q(A)\geq 0$. This is the biquaternion Bochner theorem, and it holds **exactly for the degenerate roots**, whose character is unitary:

$$
G\ \text{is positive definite}\ \Longleftrightarrow\ \tilde\Xi^{*}=-\tilde\Xi\ \Longleftrightarrow\ \tilde\Xi\ \text{is degenerate.}
$$

### The Scalar Imaginary Is the Classical Theorem

For $\tilde\Xi=i$ the kernel is the central scalar $\chi_\omega=e^{-2\pi i\langle\omega,x\rangle}e_0$, and the transform is the classical one times the identity, $G(\omega)=\varphi(\omega)e_0$. The factorisation becomes $Q(A)=\sum_{k,l}A_kA_l^{*}\varphi(\omega_k-\omega_l)$; applying the representation $\mathsf{M}_2$, this is the classical Gram sum $\sum_{k,l}\varphi(\omega_k-\omega_l)\mathsf{M}_2(A_k)\mathsf{M}_2(A_l)^{\dagger}$, positive exactly when the scalar form $\sum_{k,l}\overline{\zeta_k}\zeta_l\varphi(\omega_k-\omega_l)$ is. The biquaternion theorem at the scalar imaginary is therefore the classical theorem **componentwise**, and it is the transform the framework's clock uses.

### The Real Roots Are the Quaternion Theorem

For $\tilde\Xi=\mu$ a unit real root the kernel is a rotor, and $\chi_\omega^{*}=\chi_\omega^{-1}$ because ${}^{*}$ and ${}^{\natural}$ agree on the real quaternions. The factorisation holds and $G$ is positive definite; on real coefficients the integrand reduces to $a^{2}+b^{2}\geq 0$, which is the classical quaternion case of *Quaternion Harmonic Analysis*. The two degenerate families thus give the two textbook positivity theorems of the corpus, and they give them with the same Hermitian form.

## Two Failures That Must Not Be Confused

### The Norm Failure Is Independent of the Root

*Biquaternion Continuous Harmonic Analysis* computes the quadratic form of the transform with the **natural** conjugation between the coefficients and obtains the integral of the norm,

$$
\sum_{k,l}\overline{A_k}A_l\,G(\omega_k-\omega_l)=\int N\bigl(Z\bigr)\,d\mu .
$$

At a single coefficient $A_1=i$ this reads $\overline{i}\,i\,G(0)=i^{2}\mu(\mathbb{R}^n)=-\mu(\mathbb{R}^n)e_0$, negative for every non-zero measure, **because $N(i)=i\,i^{\natural}=-1$**. Two facts about this computation must be stated together. First, it is a statement about the bilinear form $N$ and not about the sesquilinear form $\langle\cdot,\cdot\rangle_{*}$: the conjugation written between the coefficients is ${}^{\natural}$, which is the conjugation of the norm, and the coefficient slot of the positive-definite form carries ${}^{*}$. Second, it is **independent of the root** of the transform, because the element tested, $i$, is a coefficient and not a kernel value: the same $\overline{i}\,i=-1$ is produced whatever $\tilde\Xi$ is. A failure that does not depend on the root cannot be a failure of the root criterion of the positivity, and the corpus's own sentence that the positivity "is not available" is the symptom of exactly this: the statement is about the norm, and the norm is negative on the centre for every root.

### The Genuine Failure: the Genuinely Complex Roots

The root-dependent failure is the genuinely complex one, and it is the failure of the proposition. Take $\tilde\Xi=2e_1+\sqrt{3}\,ie_3$, a genuinely complex root since $\tilde\Xi^{*}=-2e_1+\sqrt{3}\,ie_3\neq-\tilde\Xi$; take the kernel with the exponent sign of the conventions, $\chi_\omega=\cos(2\pi\langle\omega,x\rangle)e_0-\sin(2\pi\langle\omega,x\rangle)\tilde\Xi$; take the single atom of unit mass at $x=\tfrac14$, so that $G(0)=e_0$, $G(1)=-\tilde\Xi$, $G(-1)=\tilde\Xi$; and take the frequencies $0,1$ and the coefficients $A_1=e_0$, $A_2=i$. Then

$$
Q=e_0+\tilde\Xi(-i)+i(-\tilde\Xi)+(i)(-i)=2e_0-2i\tilde\Xi=2e_0-4ie_1+2\sqrt{3}\,e_3 .
$$

The element $Q$ is not Hermitian, so it is not a positive element at all, and its Hermitian part is $2e_0-4ie_1$, since $-4ie_1$ is Hermitian. In the matrix model $\mathsf{M}_2(2e_0-4ie_1)=2I-4\sigma_1$, whose spectrum is $\{6,-2\}$: the form is **not** positive definite, and the witness is the negative eigenvalue $-2$. **The sign of the imaginary part is a matter of the exponent's sign convention**, and the reader who uses $e^{+2\pi\tilde\Xi\langle\omega,x\rangle}$ instead gets $G(1)=+\tilde\Xi$ and $Q=2e_0+2i\tilde\Xi$, of Hermitian part $2e_0+4ie_1$; what is not conventional is the spectrum, which is $\{6,-2\}$ under either sign, and hence the negative eigenvalue that the witness is. The failure is structural and not numerical: the character of a genuinely complex root is not unitary for the Hermitian conjugation, so $\chi_{\omega_k}\chi_{\omega_l}^{-1}$ never reassembles into $ZZ^{*}$, and no choice of coefficients can repair a factorisation that does not exist.

**Remark (verified).** Over $100$ random positive measures of total mass one with two atoms and three frequencies each, the minimum eigenvalue of the Hermitian part of $Q$ stayed positive for every degenerate root tested — smallest $+2.1\times10^{-3}$, the scalar imaginary $+6.3\times10^{-2}$, the real root $e_1$ $+1.6\times10^{-2}$ — and was negative for every genuinely complex root, $-3.1\times10^{1}$ for $\tilde\Xi=2e_1+\sqrt{3}\,ie_3$ and $-5.1$ for $\tilde\Xi=1.25e_1+0.75\,ie_3$. At the same data the factorisation $Q=\int ZZ^{*}d\mu$ held to machine precision for the degenerate roots and failed by $4\sqrt{3}$ for the witness, whose matrix difference is exactly the term the non-unitarity of its character produces.

## The Scalar Shadow, and the Ordinary Case

The scalar part of the transform is positive definite for **every** root, because $\mathrm{Sc}(\chi_\omega)=\cos(2\pi\langle\omega,x\rangle)$, so

$$
\mathrm{Sc}\,G(\omega)=\int\cos\bigl(2\pi\langle\omega,x\rangle\bigr)\,d\mu
$$

is the real part of the classical positive-definite function and is itself positive definite. The scalar contraction $\sum_{k,l}\overline{\zeta_k}\zeta_l\,\mathrm{Sc}\,G(\omega_k-\omega_l)$ is therefore non-negative for every root. This is why the corpus's negative example must use a non-central coefficient: with central coefficients and the coefficientwise conjugation the scalar shadow is already positive, and only the bilinear form $N$ produces a negative value.

## Relation to the Open Question of the Continuous Article

The eighth open question of *Biquaternion Continuous Harmonic Analysis* asks whether some pairing internal to the algebra supplies the positivity that the Bochner-type hypothesis needs, and records that no such pairing is known. The present article answers it: the pairing is the general plain sesquilinear form $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$, the positive definite form of signature $(8,0)$ that the block already carries, and the statement it supplies holds exactly for the degenerate roots.

The Euclidean form the continuous article offers as a repair is the diagonal of this pairing, $\lVert Z\rVert_E^{2}=\langle Z,Z\rangle_{*}=\sum_\mu\lvert Z_\mu\rvert^{2}$, so the repair the article found is the positivity the theorem needs, stated without the criterion on the root; the form is internal to the algebra, and the obstacle is not the absence of a pairing but the non-unitarity of the character at the genuinely complex roots. It is the scalar part of the sesquilinear product, $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$, so it does come from the product; what fails there is multiplicativity, $\lVert ZW\rVert_E\neq\lVert Z\rVert_E\lVert W\rVert_E$ in general — the Hermitian idempotent $\tilde\Pi=\tfrac12(e_0+ie_1)$ gives $\lVert\tilde\Pi^{2}\rVert_E=\tfrac12$ against $\lVert\tilde\Pi\rVert_E^{2}=\tfrac14$ — and it is this, and not the origin of the pairing, that makes the form the topology of the transform article rather than the norm of the algebra.

## Summary

Bochner's theorem for the biquaternion transform is a theorem about the general plain sesquilinear form $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$ and about the **root**. The character $\chi_\omega=\cos(2\pi\langle\omega,x\rangle)e_0-\sin(2\pi\langle\omega,x\rangle)\tilde\Xi$ is multiplicative for every root, with $\chi_{\omega_k-\omega_l}=\chi_{\omega_k}\chi_{\omega_l}^{-1}$; it is unitary for the Hermitian conjugation, $\chi_\omega^{*}=\chi_\omega^{-1}$, **exactly when $\tilde\Xi^{*}=-\tilde\Xi$**, and this holds exactly for the degenerate roots, the scalar imaginary $\tilde\Xi=\pm i$ and the unit real roots. For those roots the quadratic form $Q=\sum_{k,l}A_kG(\omega_k-\omega_l)A_l^{*}$ factorises as the integral of the positive element $ZZ^{*}$ and the transform of a positive measure is positive definite; the scalar imaginary gives the classical theorem with $G=\varphi e_0$, the real roots the quaternion theorem of *Quaternion Harmonic Analysis*. For the genuinely complex roots the character is not unitary, the factorisation does not exist, and the form is not positive definite, with the witness $\tilde\Xi=2e_1+\sqrt{3}\,ie_3$ and the Hermitian part $2e_0-4ie_1$ of spectrum $\{6,-2\}$. The failure recorded in the corpus at the central coefficient $A=i$ is a different statement: it tests the bilinear norm $N$, for which $N(i)=-1$ for every root, and it is the indefiniteness of the metric and not the failure of the positivity. The scalar part of the transform is the classical positive-definite function and is positive definite for every root, which is why the loss appears only in the full $\mathbb{B}$-valued form. The theorem answers the eighth open question of *Biquaternion Continuous Harmonic Analysis*: the pairing the Bochner-type hypothesis needs is the one the block already carries, and it is the root, not the pairing, that decides.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde\Xi$, $\tilde\Xi^{2}=-e_0$ | a root of $-1$ of $\mathbb{B}$; written $\rho$ in the transform articles |
| $\chi_\omega=\cos\theta\,e_0-\sin\theta\,\tilde\Xi$, $\theta=2\pi\langle\omega,x\rangle$ | the biquaternion kernel of a root |
| $G(\omega)=\int\chi_\omega\,d\mu$ | the transform of the measure; $G(0)=\mu(\mathbb{R}^n)e_0$ |
| $\chi_\omega^{*}=\chi_\omega^{-1}\Leftrightarrow\tilde\Xi^{*}=-\tilde\Xi$ | Hermitian unitarity; the degenerate roots |
| $\chi_\omega^{\natural}=\chi_\omega^{-1}\Leftrightarrow\tilde\Xi^{\natural}=-\tilde\Xi$ | natural unitarity; the pure roots (real and genuinely complex) |
| $Q=\sum_{k,l}A_kG(\omega_k-\omega_l)A_l^{*}$ | the sesquilinear quadratic form, conjugation in the second slot |
| $Q=\int ZZ^{*}d\mu$, $Z=\sum_kA_k\chi_{\omega_k}$ | the factorisation; positive definite for the degenerate roots |
| $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$, signature $(8,0)$ | the pairing the theorem needs; the diagonal of the Euclidean form |
| $N(\tilde P)=\tilde P\tilde P^{\natural}$, $N(i)=-1$ | the norm/interval; the root-independent failure |
| $\tilde\Xi=\pm i$, $\tilde\Xi=\pm\mu$ | the scalar imaginary and the real roots; the degenerate family |
| $\tilde\Xi=b\mu+d\nu i$, $b^{2}-d^{2}=1$ | the genuinely complex roots; where positivity fails |
| $G=\varphi e_0$, $\mathrm{Sc}\,G$ central | the scalar imaginary read as the classical theorem |

## Further Reading

- *Biquaternion Continuous Harmonic Analysis* (`articles_maths/biquaternion-continuous-harmonic-analysis.md`), for the transform, its kernel, the classification of the roots, the two-unit kernel, the vanishing-norm issue, the transform of a measure with the natural conjugation, and the open question answered here.
- *Biquaternion Discrete Harmonic Analysis* (`articles_maths/biquaternion-discrete-harmonic-analysis.md`), for the discrete transform, the sampling theorem and the discrete form of the same positivity statement.
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the four pairings, $\langle\tilde P,\tilde Q\rangle_{*}$ among them, and their conjugations.
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the positivity of the Hermitian conjugation and the cone $P=\{\tilde Q\tilde Q^{*}\}$.
- *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint* (`articles_maths/hermitian-forms-over-the-biquaternion-algebra-and-the-unitary-witt-group-with-hermitian-adjoint.md`), for the classification of the Hermitian forms and the unit form of signature $(8,0)$.
- *Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-plain-sesqualgebra-of-biquaternions.md`), for the restriction of the form to the remarkable subspaces.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the classification of the roots of $-1$, $-0$ and $+1$.
- *Quaternion Harmonic Analysis* (`articles_maths/quaternion-harmonic-analysis.md`), for the quaternion case that does hold, the positivity theorem of the real roots.
- *Positive Definite Functions and Hermitian Kernels* (`articles_maths/positive-definite-functions-and-hermitian-kernels.md`), *Reproducing Kernel Hilbert Spaces* (`articles_maths/reproducing-kernel-hilbert-spaces.md`) and *Positive Definite Distributions* (`articles_maths/positive-definite-distributions.md`), for Bochner's theorem, the Aronszajn theorem and the Bochner–Schwartz theorem in the classical setting.
- *Conventions in Mathematics* (`articles_maths/conventions-in-mathematics.md`), for the symbols of the roots, the conjugations and the pairings.
- *The Bochner Theorem for the Biquaternion Transform: the Hermitian Form and the Root* (`articles_physics/the-bochner-theorem-for-the-biquaternion-transform-the-hermitian-form-and-the-root.md`), the physics companion, for the physical reading of the same theorem.
- S. Bochner, "Monotone Funktionen, Stieltjessche Integrale und harmonische Analyse", *Mathematische Annalen* **108** (1933) 378–410, for the classical theorem that a normalised positive-definite function is the Fourier transform of a measure.
- S. Georgiev, J. Morais, K. I. Kou, and W. Sprößig, "Bochner–Minlos theorem and quaternion Fourier transform", in *Quaternion and Clifford–Fourier Transforms and Wavelets*, Trends in Mathematics (Springer, 2013), 105–120, for the quaternion theorem whose biquaternionic counterpart fails at the genuinely complex roots.
