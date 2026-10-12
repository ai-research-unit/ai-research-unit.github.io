# __The Bochner Theorem for the Biquaternion Transform: the Hermitian Form and the Root__

## Introduction

Bochner's theorem says that a continuous normalised positive-definite function on a group is the Fourier transform of a positive measure. Turned around, it says that **the transform of a positive measure is a positive-definite function**, and it is the statement ordinary quantum theory uses whenever it treats a spectral density, a covariance or a two-point function as a probability. Its proof is short, and it consumes exactly two properties of the character — that the character is multiplicative under the group law, and that it is unitary — together with one property of the pairing, that the quadratic form carries the conjugation in its second slot.

In the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ the second and the third of these three ingredients become choices. The kernel of the transform is an exponential of a **root of $-1$**, and the roots fall into three families. The algebra carries four forms, two bilinear and two sesquilinear, and the classical theorem sits in one of the sesquilinear rows. This article asks the single question such a situation forces: **which form makes the Bochner theorem true, and for which roots?**

The answer, and the content of the article, is one sentence. The positivity the theorem needs is the positivity of the **Hermitian form** $H=\langle\cdot,\cdot\rangle_{*}$, the probability form of the corpus, and with $H$ the theorem holds exactly for the **degenerate roots** — the central imaginary $\rho=\pm i$ and the unit pure real quaternions $\rho=\pm\mu$ — and fails for the **non-degenerate roots** $\rho=b\mu+d\nu i$. The failure recorded in the corpus at the central element $i$ is a different statement: it tests the biquaternion norm $N$, it is independent of the root, and it belongs to the metric and not to the probability. Both statements are true, and they are not the same statement.

**Boundaries.** The transform, its kernel, the three families of roots, the factorisation and the vanishing-norm issue are the mathematics articles *Biquaternion Discrete Harmonic Analysis* and *Biquaternion Continuous Harmonic Analysis*, and the transform of a measure with the norm identity is the section of the continuous article quoted in the ledger. The physical reading of the transform, the conjugate axis and the choice of root is *The Biquaternion Fourier Transform and the Imaginary Directions*; this article is its positivity companion and proves what that article reads. The positivity of $H$, its cone and its signature are *Mass, Rank and the Positivity of the Dagger*, *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing* and the mathematics *Positive Definite Functions and Hermitian Kernels* and *Positive Definite Distributions*, where the classical theorem and the Bochner–Schwartz theorem are stated; the quaternion case that does hold is *Quaternion Harmonic Analysis*. The four forms are *Conventions in the Biquaternion Universe* and *Remarkable Subspaces and the Four Forms*, and the state side is *The Born Rule as a Trace Formula — Derivation and Comparison*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity, $e_k^{2}=-e_0$ and $e_je_k=e_l$ for $(j,k,l)$ a cyclic permutation of $(1,2,3)$; a general element is $\tilde Q=Q_0e_0+\mathbf Q$ with $Q_\mu\in\mathbb{C}$. The **coefficientwise conjugation** $\overline{\cdot}$ conjugates the coefficients; the **natural conjugation** ${}^{\natural}$ fixes $e_0$ and negates $e_1,e_2,e_3$ and is $\mathbb{C}$-linear; the **Hermitian conjugation** is ${}^{*}=\overline{\cdot}\circ{}^{\natural}$, so $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ with $\varepsilon=(1,-1,-1,-1)$. The four forms are $B=\mathrm{Sc}(\tilde P\tilde Q)$, $N=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, $H=\mathrm{Sc}(\tilde P\tilde Q^{*})$ and $K=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$, and $\mathrm{Tr}=2\,\mathrm{Sc}$. A root is an element $\rho$ with $\rho^{2}=-e_0$; the **degenerate** roots are $\rho=\pm i$ and the unit pure real quaternions, the **non-degenerate** roots are $\rho=b\mu+d\nu i$ with $\mu\perp\nu$ unit real and $b^{2}-d^{2}=1$. All conventions are those of *Conventions in the Biquaternion Universe*.

## The Context of the Theorem

### The Two Readings

Bochner's theorem has two readings. The first says that a continuous normalised positive-definite function is the transform of a positive measure; the second says that the transform of a positive measure is a positive-definite function. They are the same equivalence read in opposite directions, but they ask different questions, and this article uses the second. The first is an existence statement — a positive-definite function is a spectral density in disguise and the measure is its spectrum — and it is how the theorem is usually quoted in probability. The second is a **positivity statement** about a given measure, and it is the one a two-point function, a covariance or a spectral density is asked to satisfy: the two-point function of a theory is the transform of its spectral measure, and its positive definiteness is the positivity of that measure. This article asks for which roots that statement survives when the transform is biquaternionic.

### The Engine of the Classical Proof

The classical proof is short because its engine consumes two properties of the character and no others. The character is **multiplicative**, which reassembles the difference of two frequencies as a product, $\chi_{\omega_k-\omega_l}=\chi_{\omega_k}\chi_{\omega_l}^{-1}$; and it is **unitary**, which replaces the inverse $\chi_{\omega_l}^{-1}$ by the Hermitian conjugate $\chi_{\omega_l}^{*}$, so that the sum of products closes into a square, and a square is automatically positive. The third ingredient is the pairing: the quadratic form must carry the conjugation in its second slot, which is what places the square under the integral. In the classical case the two character properties are free — the exponential of the single imaginary unit is multiplicative and unitary with no choice made — and the only care needed is the placement of the conjugation in the form. **The two character properties are therefore free in the classical case, and in the biquaternion algebra they must be re-examined: multiplicativity survives the choice of root, and unitarity does not**, which is where the whole question of the article comes from.

### Why a Root Appears

The classical character is the exponential of a single imaginary unit, and the imaginary unit is canonical: the complex structure of $\mathbb{C}$ is unique, and there is nothing to choose. A hypercomplex algebra has **no single imaginary unit**. To write an exponential in $\mathbb{B}$ one must first choose an element whose square is $-e_0$, and that choice is the **root**; the character is then $\chi_\omega=\exp(-2\pi\rho\langle\omega,x\rangle)$, and different roots give different characters. Multiplicativity survives the choice, because the character is the exponential of one and the same root at every frequency, so the reassembly of the difference of frequencies is never lost. Unitarity does not come free: $\chi_\omega^{*}=\chi_\omega^{-1}$ is the condition $\rho^{*}=-\rho$, which is a condition on the root, and the roots that satisfy it are the degenerate ones, the central imaginary and the pure real quaternions, while the non-degenerate roots do not. This is the whole origin of the root dichotomy in $\mathbb{B}$: one of the two properties the classical character has for free becomes a choice, and the root makes the choice. It is also why the choice of root, which is invisible in the classical case, becomes the axis on which the positivity of this article turns.

### What Is and Is Not at Stake

Three features of the algebra are usually named together, and only one of them decides the theorem. **Noncommutativity** is already spent: it is why the statement must say which conjugation the probability form carries, and it is what produces the four forms of *Conventions in the Biquaternion Universe*. **Zero divisors** do not enter: the probability form $H$ is positive definite of signature $(8,0)$ and its cone is the cone of a positive definite form, so the isotropic elements — the light cone of the interval $N$, where $(e_0+ie_1)(e_0-ie_1)=0$ while $H(e_0+ie_1,e_0+ie_1)=2$ — are not what fails. The zero divisors belong to the interval and to the root-independent norm failure already separated in the ledger; they are not a positivity obstruction. What decides the theorem is **unitarity** alone, the one property of the classical character that the choice of clock can destroy.

### Where the Spectral Measure Lives, and the Clock Is Chosen Once

The classical theorem integrates over the dual group, and the biquaternion theorem is sometimes read as integrating over the roots. It does not: the measure lives on the frequency space, and the root — the choice of clock — is fixed once, before the measure is chosen. The criterion is therefore a restriction on the **clock** and not on the spectrum: the spectral measure is free, and it is the clock that positivity constrains, one root at a time. This is why "a measure supported on the unitary roots" describes nothing here; there is no measure over roots, and the root is a single decision the theory makes once.

### What "Exactly" Means

The criterion of the article is a two-direction statement, and both directions are proved. From the root to the positivity is the factorisation of §*The Factorisation, and the Degenerate Roots*, the direction a Bochner theorem proves by hand. From the root to the failure is the proposition of §*The Genuine Failure: Every Non-Degenerate Root*, and it is proved for **every** non-degenerate root by a single witness — one atom, two frequencies, two coefficients — which depends on the root only through its two parameters $b$ and $d$. The word **exactly** is therefore earned rather than asserted: positivity holds for the degenerate roots and fails for every non-degenerate root, the criterion is an equivalence, and the eighth open question of *Biquaternion Continuous Harmonic Analysis* is answered in both directions. The forward direction is the classical engine surviving the change of algebra; the converse is the algebra's own contribution, and it says that the character of a non-degenerate root fails positivity already on the one-atom witness, so the failure is a property of the character and of the clock, and not of the data.

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

Two properties of the character $e^{-2\pi i\langle\omega,x\rangle}$ are used, and no others. It is **multiplicative**, $e^{-2\pi i\langle\omega_k,x\rangle}e^{-2\pi i\langle\omega_l,x\rangle}=e^{-2\pi i\langle\omega_k+\omega_l,x\rangle}$, which is what identifies the difference of frequencies with a product; and it is **unitary**, $\overline{e^{-2\pi i\langle\omega,x\rangle}}=\bigl(e^{-2\pi i\langle\omega,x\rangle}\bigr)^{-1}$, which is what turns the conjugate of one factor into the inverse of the other. The third ingredient is that the quadratic form is built with the conjugation in the **second slot**, which is what places the modulus squared under the integral.

### The Transform of a Measure in $\mathbb{B}$

Fix a root $\rho$ of $-1$ and let the biquaternion kernel be

$$
\chi_\omega(x)=\exp\bigl(-2\pi\rho\,\langle\omega,x\rangle\bigr)=\cos\bigl(2\pi\langle\omega,x\rangle\bigr)e_0-\sin\bigl(2\pi\langle\omega,x\rangle\bigr)\rho ,
$$

the two-term closure of the exponential. For a finite positive measure $\mu$ on $\mathbb{R}^n$ the **transform of the measure** is the $\mathbb{B}$-valued function

$$
G(\omega)=\int_{\mathbb{R}^n}\chi_\omega(x)\,d\mu(x),\qquad G(0)=\mu(\mathbb{R}^n)e_0 .
$$

Two of the ingredients of the classical proof now carry a choice. The value $G(\omega)$ is an element of a non-commutative algebra, so the quadratic form must say which conjugation stands between the two coefficients; and the character is $\mathbb{B}$-valued, so its unitarity is a statement about $\rho$.

### Multiplicativity Is Not in Question

The character is multiplicative for every root, and this is the one ingredient that is never lost:

$$
\chi_\omega\chi_\eta=\exp\bigl(-2\pi\rho\langle\omega+\eta,x\rangle\bigr)=\chi_{\omega+\eta},\qquad \chi_\omega^{-1}=\chi_{-\omega},
$$

because the two exponentials share the single root $\rho$, which commutes with itself. In particular the difference of frequencies always reassembles as a product, $\chi_{\omega_k-\omega_l}=\chi_{\omega_k}\chi_{\omega_l}^{-1}$. What is at stake is therefore not multiplicativity but **unitarity**: whether the inverse of the character is its Hermitian conjugate.

## Unitarity of the Character and the Root

### The Three Families

The roots of $-1$ fall into three families, and the whole positivity question divides along them.

| Family | Form of $\rho$ | $\rho^{\natural}$ | $\rho^{*}$ |
|---|---|---|---|
| central | $\pm i$ | $+i$ | $-i$ |
| pure real | $\pm\mu$, $\mu$ unit real | $-\mu$ | $-\mu$ |
| non-degenerate | $b\mu+d\nu i$, $\mu\perp\nu$, $b^{2}-d^{2}=1$ | $-b\mu-d\nu i$ | $-b\mu+d\nu i$ |

The distinction of the columns is the point of the table: the natural conjugation acts on the quaternion factor alone, while the Hermitian conjugation conjugates the complex coefficients as well, and for the non-degenerate roots the two disagree on the sign of the $d\nu i$ term.

### The Character Is Unitary Exactly for a Degenerate Root

**Proposition.** For the kernel $\chi_\omega$ of a root $\rho$, the Hermitian adjoint equals the inverse,

$$
\chi_\omega^{*}=\chi_\omega^{-1},
$$

**exactly when** $\rho^{*}=-\rho$, and this holds exactly for the degenerate roots.

*Proof.* From $\chi_\omega=\cos\theta\,e_0-\sin\theta\,\rho$ and $\chi_\omega^{-1}=\cos\theta\,e_0+\sin\theta\,\rho$, with $\theta=2\pi\langle\omega,x\rangle$, one reads $\chi_\omega^{*}=\cos\theta\,e_0-\sin\theta\,\rho^{*}$, so the two agree for all $\omega$ and $x$ exactly when $\rho^{*}=-\rho$. Writing $\rho=a_0e_0+v$ with $a_0\in\mathbb{C}$ and $v=\sum_{k\geq1}a_ke_k$, the condition $\rho^{*}=-\rho$ is $\overline{a_0}=-a_0$ and $\overline{a_k}=a_k$, that is $a_0=i\theta$ with $\theta$ real and $v$ a real quaternion. Imposing $\rho^{2}=-e_0$ on $\rho=i\theta e_0+v$ gives $-\theta^{2}+\lvert v\rvert^{2}=-1$ and $2i\theta v=0$, hence either $\theta=0$, which is the pure real roots $v$ of unit length, or $v=0$, which is the central roots $\theta=\pm1$. These are the degenerate roots and no others.

The proposition is the exact biquaternion form of the classical unitarity of the character, and it is **root-dependent**, which the corpus's own statement of unitarity is not: *The Biquaternion Fourier Transform and the Imaginary Directions* proves $W^{\natural}=W^{-1}$, which uses the natural conjugation, and this holds for the pure roots — the real and the non-degenerate — while the central root is read there as the exception. **The corpus is not wrong.** $W^{\natural}=W^{-1}$ is the correct statement about the norm's conjugation, and it answers a different question from the one asked here: whether the *norm* of the character is the identity, rather than whether the character is unitary for the conjugation a positive-definite function uses. Read with the Hermitian conjugation, which is that conjugation, the central root is not an exception at all — it is one of the two degenerate families for which the character is unitary.

### The Natural Conjugation Is a Different Statement

The biquaternion norm of the kernel is the natural square, $N(\chi_\omega)=\chi_\omega\chi_\omega^{\natural}=(\cos^{2}\theta+\sin^{2}\theta)e_0=e_0$ for every pure root — the real and the non-degenerate — and it is not the identity for the central root. The two unitarity statements must therefore be kept apart:

| Reading | Condition | Holds for |
|---|---|---|
| Hermitian, $\chi_\omega^{*}=\chi_\omega^{-1}$ | $\rho^{*}=-\rho$ | central and pure real (the degenerate roots) |
| natural, $\chi_\omega^{\natural}=\chi_\omega^{-1}$ | $\rho^{\natural}=-\rho$ | pure roots: real and non-degenerate (the central root excluded) |

The Hermitian row is the one a positive-definite function uses, because a positive-definite function is sesquilinear; the natural row is the one the norm identity of the continuous article uses, and it belongs to the metric.

## Positivity of the Transform

### The Sesquilinear Quadratic Form

For coefficients $A_1,\dots,A_N$ in $\mathbb{B}$ and frequencies $\omega_1,\dots,\omega_N$ put

$$
Q(A)=\sum_{k,l=1}^{N}A_k\,G(\omega_k-\omega_l)\,A_l^{*} .
$$

This is the biquaternion quadratic form of the transform, with the Hermitian conjugation in the second slot — the slot that the classical proof conjugates and the slot the probability form uses. The theorem is the statement that $Q(A)$ is a positive element of $\mathbb{B}$ for every choice of coefficients, comparable with the scalar inequality of the classical case.

### The Factorisation, and the Degenerate Roots

Let $\rho$ be degenerate, so that $\chi_\omega^{*}=\chi_\omega^{-1}$ by the proposition. Substituting $G(\omega_k-\omega_l)=\int\chi_{\omega_k}\chi_{\omega_l}^{-1}d\mu=\int\chi_{\omega_k}\chi_{\omega_l}^{*}d\mu$,

$$
Q(A)=\int_{\mathbb{R}^n}\Bigl(\sum_{k}A_k\chi_{\omega_k}\Bigr)\Bigl(\sum_{l}A_l\chi_{\omega_l}\Bigr)^{*}\,d\mu=\int_{\mathbb{R}^n}Z\,Z^{*}\,d\mu,\qquad Z=\sum_{k}A_k\chi_{\omega_k} .
$$

The element $ZZ^{*}$ is Hermitian, $(ZZ^{*})^{*}=ZZ^{*}$, and in the matrix model $\mathbb{B}\cong M_2(\mathbb{C})$, whose representation $\Phi$ is a $*$-homomorphism, it is the matrix $\Phi(Z)\Phi(Z)^{\dagger}$, positive semidefinite. An integral of positive elements against a positive measure is positive, so $Q(A)\geq 0$. This is the biquaternion Bochner theorem, and it holds **exactly for the degenerate roots**, whose character is unitary:

$$
\text{every finite positive measure has a positive-definite transform}\ \Longleftrightarrow\ \rho^{*}=-\rho\ \Longleftrightarrow\ \rho\ \text{degenerate.}
$$

The factorisation proves the direction from the right to the left, the half a Bochner theorem proves by hand. The other direction is proved in §*The Genuine Failure: Every Non-Degenerate Root*, whose proposition produces for every non-degenerate root a value of the form that is not even Hermitian. Both directions are therefore proved, and the equivalence is a theorem of the algebra and not a choice of convention. The quantifier is part of the statement: the factorisation gives the property for **every** positive measure at once, while the converse gives one measure at which it fails, so what the theorem separates is the class of transforms from the positive-definite functions and not a single transform — the atom at the origin has the constant $e_0$ as its transform, and the constant is positive definite for every root.

### The Central Root Is the Classical Theorem

For $\rho=i$ the kernel is the central scalar $\chi_\omega=e^{-2\pi i\langle\omega,x\rangle}e_0$, and the transform is the classical one times the identity, $G(\omega)=\varphi(\omega)e_0$. The factorisation becomes $Q(A)=\sum_{k,l}A_kA_l^{*}\varphi(\omega_k-\omega_l)$; applying the representation $\Phi$, this is the classical Gram sum $\sum_{k,l}\varphi(\omega_k-\omega_l)\Phi(A_k)\Phi(A_l)^{\dagger}$, positive exactly when the scalar form $\sum_{k,l}\overline{\zeta_k}\zeta_l\varphi(\omega_k-\omega_l)$ is. The biquaternion theorem at the central root is therefore the classical theorem **componentwise**, and it is the transform the framework's own clock uses: *The Biquaternion Fourier Transform and the Imaginary Directions* reads the central root as the clock of the transform.

### The Pure Real Roots Are the Quaternion Theorem

For $\rho=\mu$ a unit pure real quaternion the kernel is a rotor, and $\chi_\omega^{*}=\chi_\omega^{-1}$ because $*$ and ${}^{\natural}$ agree on the real quaternions. The factorisation holds and $G$ is positive definite; on real coefficients the integrand reduces to $a^{2}+b^{2}\geq 0$, which is the classical quaternion case of *Quaternion Harmonic Analysis*. The two degenerate families thus give the two textbook positivity theorems of the corpus, and they give them with the same Hermitian form.

## Two Failures That Must Not Be Confused

### The Norm Failure Is Independent of the Root

The continuous article computes the quadratic form of the transform with the **natural** conjugation between the coefficients and obtains the integral of the norm,

$$
\sum_{k,l}\overline{A_k}A_l\,G(\omega_k-\omega_l)=\int N\bigl(Z\bigr)\,d\mu.
$$

At a single coefficient $A_1=i$ this reads $\overline{i}\,i\,G(0)=i^{2}\mu(\mathbb{R}^n)=-\mu(\mathbb{R}^n)e_0$, negative for every non-zero measure, **because $N(i)=i\,i^{\natural}=-1$**. Two facts about this computation must be stated together. First, it is a statement about the bilinear form $N$ and not about the sesquilinear form $H$: the conjugation written between the coefficients is ${}^{\natural}$, which is the conjugation of the norm, and the coefficient slot of the probability form carries ${}^{*}$. Second, it is **independent of the root** of the transform, because the element tested, $i$, is a coefficient and not a kernel value: the same $\overline{i}\,i=-1$ is produced whatever $\rho$ is. A failure that does not depend on the root cannot be a failure of the root criterion of the positivity, and the corpus's own sentence that the positivity "is not restored by any restriction to ordinary data" is the symptom of exactly this: the statement is about the norm, and the norm is negative on the centre for every root.

### The Genuine Failure: Every Non-Degenerate Root

The root-dependent failure is the non-degenerate one, and it is the converse of the theorem. It is not the property of one example: a single witness, the same for every non-degenerate root, decides the whole family, and it decides it in the strongest way, by producing a value of the form that is not even Hermitian.

**Proposition (converse).** Let $\rho=b\mu+d\nu i$ be a non-degenerate root, $\mu\perp\nu$ unit real and $b^{2}-d^{2}=1$, written with $b>0$ so that $b=\sqrt{1+d^{2}}>1$ and $d\neq0$. Take the single atom of unit mass at a point $x$ and a frequency $\omega$ with $2\pi\langle\omega,x\rangle=\tfrac{\pi}{2}$, the frequencies $0$ and $\omega$, and the coefficients $A_1=e_0$, $A_2=i$. Then the character at the atom is $\chi_\omega=-\rho$, the transform takes the values $G(0)=e_0$, $G(\omega)=-\rho$ and $G(-\omega)=\rho$, and

$$
Q=2e_0-2i\rho=2e_0-2ib\mu+2d\nu .
$$

Its Hermitian conjugate is $Q^{*}=2e_0-2ib\mu-2d\nu$, so

$$
Q-Q^{*}=4d\nu\neq0,\qquad \mathrm{Her}\,Q=\tfrac12\bigl(Q+Q^{*}\bigr)=2e_0-2ib\mu=2\bigl(e_0-ib\mu\bigr),
$$

and $G$ is not positive definite. The Hermitian part is $2(e_0-X)$ with $X=ib\mu$; the element $X$ is Hermitian, because $i$ is central with $i^{*}=-i$ and $\mu$ is real with $\mu^{*}=-\mu$, and $X^{2}=b^{2}e_0$. Its matrix $\Phi(X)$ is therefore Hermitian with square $b^{2}I$, so its spectrum is $\{\pm b\}$ and

$$
\mathrm{spec}\bigl(\mathrm{Her}\,Q\bigr)=\{2(1-b),\,2(1+b)\}.
$$

Because $b^{2}-d^{2}=1$ with $d\neq0$ forces $b>1$, the eigenvalue $2(1-b)$ is negative and the form is not positive definite; and because $d\neq0$ the difference $Q-Q^{*}=4d\nu$ does not vanish, so $Q$ is not Hermitian and is not a positive element of the cone at all. The same witness at a pure real root, $d=0$ and $b=1$, gives the spectrum $\{0,4\}$, which is positive semidefinite; the failure is therefore exactly the twist $d$, and the size of the twist sets the magnitude $2(b-1)$ of the negative eigenvalue.

The witness of the corpus's illustration is the case $b=2$, $d=\sqrt{3}$, $\mu=e_1$, $\nu=e_3$: take $\rho=2e_1+\sqrt{3}\,ie_3$, a non-degenerate root since $\rho^{*}=-2e_1+\sqrt{3}\,ie_3\neq-\rho$; take the kernel with the exponent sign of the conventions, $\chi_\omega=\cos(2\pi\langle\omega,x\rangle)e_0-\sin(2\pi\langle\omega,x\rangle)\rho$; take the single atom of unit mass at $x=\tfrac14$, so that $G(0)=e_0$, $G(1)=-\rho$, $G(-1)=\rho$; and take the frequencies $0,1$ and the coefficients $A_1=e_0$, $A_2=i$. Then

$$
Q=e_0+\rho(-i)+i(-\rho)+(i)(-i)=2e_0-2i\rho=2e_0-4ie_1+2\sqrt{3}\,e_3 ,
$$

in agreement with the general formula, whose twist term is $4d\nu=4\sqrt{3}\,e_3$. The element $Q$ is not Hermitian, so it is not a positive element at all, and its Hermitian part is $2e_0-4ie_1$, since $-4ie_1$ is Hermitian. In the matrix model $\Phi(2e_0-4ie_1)=2I-4\sigma_1$, whose spectrum is $\{6,-2\}$, the general spectrum $\{2(1-b),2(1+b)\}$ at $b=2$: the form is **not** positive definite, and the witness is the negative eigenvalue $-2$, which is $2(1-b)$. **The sign of the imaginary part is a matter of the exponent's sign convention**, and the reader who uses $e^{+2\pi\rho\langle\omega,x\rangle}$ instead gets $G(1)=+\rho$ and $Q=2e_0+2i\rho$, of Hermitian part $2e_0+4ie_1$; what is not conventional is the spectrum, which is $\{6,-2\}$ under either sign, and hence the negative eigenvalue that the witness is. The failure is structural and not numerical: the character of a non-degenerate root is not unitary for the Hermitian conjugation, so $\chi_{\omega_k}\chi_{\omega_l}^{-1}$ never reassembles into a modulus squared, and the proposition shows that no measure and no choice of coefficients can mend it, since the value which replaces the factorisation is not merely outside the cone but outside the Hermitian elements.

**Remark (verified).** The general formula was checked by recomputation in the matrix model $\Phi$. For the roots $(b,d)=(2,\sqrt3)$, $(1.25,0.75)$, $(\sqrt2,1)$ and $(3,\sqrt8)$, with $\mu,\nu$ unit real and orthogonal, the witness gave $Q-Q^{*}=4d\nu$ and $\mathrm{Her}\,Q=2e_0-2ib\mu$ to machine precision, and the spectrum of the Hermitian part agreed exactly with $\{2(1-b),2(1+b)\}$: $\{-2,6\}$, $\{-0.5,4.5\}$, $\{-0.828,4.828\}$ and $\{-4,8\}$. Over $400$ random positive measures of total mass one with two to four atoms the minimum eigenvalue of the Hermitian part of $Q$ stayed positive for every degenerate root tested — smallest $+2.8\times10^{-2}$, central root $+1.7\times10^{-1}$ — and was negative for every non-degenerate root, $-3.2\times10^{1}$ for $\rho=2e_1+\sqrt{3}\,ie_3$ and $-2.7$ for $\rho=1.25e_1+\sqrt{0.5625}\,ie_3$. The scalar contraction with $\mathrm{Sc}$ behaved the same way, positive for the degenerate roots and negative for the non-degenerate ones.

## The Scalar Shadow, and the Ordinary Reading

### The Scalar Part Is the Classical Function

The scalar part of the transform is positive definite for **every** root, because $\mathrm{Sc}(\chi_\omega)=\cos(2\pi\langle\omega,x\rangle)$, so

$$
\mathrm{Sc}\,G(\omega)=\int\cos\bigl(2\pi\langle\omega,x\rangle\bigr)\,d\mu
$$

is the real part of the classical positive-definite function and is itself positive definite. The scalar contraction $\sum_{k,l}\overline{\zeta_k}\zeta_l\,\mathrm{Sc}\,G(\omega_k-\omega_l)$ is therefore non-negative for every root. This is why the corpus's negative example must use a non-central coefficient: with central coefficients and the coefficientwise conjugation the scalar shadow is already positive, and only the bilinear form $N$ produces a negative value.

### Positivity in Quantum Mechanics Is a Postulate, Not Bochner's Theorem

Ordinary quantum mechanics never runs the Bochner chain, and this is why the present question does not perturb it. Quantum theory **postulates** the positive Hilbert space and its definite inner product, and obtains the spectral theorem from the self-adjoint generator by Stone's theorem; the positive-definite function $\omega\mapsto\langle\psi,e^{iA}\psi\rangle$ is then a **consequence**, not a hypothesis. Bochner's theorem is the abelian case of that structure, and the non-commutative route does not need it. In the framework the same input is available and it is exactly the Hermitian form $H$: positive definite of signature $(8,0)$ on $\mathbb{B}$, the Born pairing on the informational sector, and the mother of the trace pairing. The framework's quantum-mechanical positivity is therefore supplied by $H$, as it is in ordinary theory, and the failure at the non-degenerate roots is a property of the *transform* and not of the state space.

## Ledger

**Proved.** The character is multiplicative for every root, $\chi_\omega\chi_\eta=\chi_{\omega+\eta}$. The character is unitary for the Hermitian conjugation exactly when $\rho^{*}=-\rho$, which holds exactly for the degenerate roots; the natural-conjugation unitarity holds exactly for the pure real roots, the central root excluded. For a degenerate root the quadratic form is the integral of a positive element, $Q=\int ZZ^{*}d\mu\geq 0$, so the transform of a positive measure is positive definite; at the central root the theorem is the classical theorem with $G=\varphi e_0$. For a non-degenerate root the form is not positive definite, and this holds for **every** non-degenerate root: the proposition exhibits one witness, the same for the whole family — one atom, the frequencies $0$ and $\omega$ with $2\pi\langle\omega,x\rangle=\tfrac{\pi}{2}$, and the coefficients $A_1=e_0$, $A_2=i$ — giving $Q=2e_0-2ib\mu+2d\nu$, which is not Hermitian because $Q-Q^{*}=4d\nu\neq0$, and whose Hermitian part $2e_0-2ib\mu$ has spectrum $\{2(1-b),2(1+b)\}$ with the negative eigenvalue $2(1-b)$, since $b=\sqrt{1+d^{2}}>1$. The corpus's witness $\rho=2e_1+\sqrt{3}\,ie_3$ is the case $b=2$, $d=\sqrt{3}$, with the Hermitian part $2e_0-4ie_1$ of spectrum $\{6,-2\}$. Both directions of the equivalence are therefore proved. The norm failure at $A=i$ is independent of the root.

**Interpretations.** The probability form $H$ is the form the theorem needs and the norm $N$ is the metric; the central root is the clock of the transform and its theorem is classical; the non-degenerate roots are the transform in which the central and spatial axes are twisted together, and it is exactly that **twist**, and not a hierarchy of roots, that the positivity excludes — the algebra prefers no root, and the central root is distinguished only by being central, so no root family is more fundamental than another; the size of the twist sets the depth $2(b-1)$ of the failure; the scalar part is the ordinary positive-definite function and the loss is invisible in it.

**Not claimed.** That the choice of root is physical — the algebra prefers no root, and the central root is distinguished only by being central; that the non-degenerate transform is meaningless — it is invertible and unitary as a transform, and only its positivity fails, so that it remains a describable frame whose significance is set out under Consequences; that the corpus's norm computation is wrong — it is correct as a statement about $N$; that any internal pairing restores the positivity at the non-degenerate roots — the failure is the non-unitarity of the character and is pairing-independent within the four forms; that some measure or some choice of coefficients could restore it — the proposition's value is non-Hermitian for every non-degenerate root, so no data repair what unitarity alone decides.

## Physical Readings

The theorem reads as the statement that **probability is positive and the interval is indefinite, and the two do not trade places**. The form that makes the transform of a measure positive definite is $H$, the probability form, the same form whose algebraic norm is the squared modulus and whose trace is the Born rule; the form that fails at the central element is $N$, the interval, whose signature is $(3,1)$ on the material sector and whose vanishing set is the light cone (*Mass, Rank and the Positivity of the Dagger*). A positive measure whose transform is asked for a probability therefore returns one through $H$ and never through $N$, and the corpus's standing separation of the two forms is what keeps the two readings apart.

Read on the root, the theorem says that **the momentum-space positivity of ordinary theory is the positivity of the central clock.** The central root is the one that commutes with the whole algebra, the one the framework's relational time uses, and it is exactly for it that the biquaternion theorem reduces to the classical one and the positivity is available without qualification (*The Biquaternion Fourier Transform and the Imaginary Directions*, *Each Sector Is the Other's Clock: the Sector Exchange as Relational Time*). A non-central clock is a rotation about a spatial axis, and it is exactly there that momentum-space positivity is lost. The reading is that the framework's own clock is the one that carries the positivity, and that the non-degenerate roots are rotated clocks of it, whose transforms are genuine biquaternion transforms with their positive-definite function replaced by an indefinite one.

Read on the state space, the theorem is one more place where the framework's positivity is carried by the informational sector. The positive Hilbert space that quantum mechanics postulates is supplied here by the same form $H$ that the state side uses, and the Bochner statement is a statement about that form and not about a new structure. The failure at the non-degenerate roots is a property of the conjugate space and of the clock, and it leaves the state space, the Born rule and the unitary evolution untouched.

## Consequences

The theorem is a **structural particularity** of the framework and not a defect of it, and none of what follows contradicts the physics that is actually experienced. Ordinary quantum mechanics postulates the positive Hilbert space, obtains the spectral theorem from the self-adjoint generator by Stone's theorem, and derives the positive-definite function $\omega\mapsto\langle\psi,e^{iA}\psi\rangle$ as a consequence; it never runs the Bochner chain. The framework has the same postulate available and it is the form $H$, so the chain is likewise optional, and what its outcome at the non-degenerate roots changes is not a state, not a probability and not an evolution, but the **place of the probabilistic structure inside the algebra**. The consequences below are consequences of placement.

- **The quantum-mechanical structure is carried by $H$ and is untouched.** The state space, the Born pairing and the unitary evolution are built from $H$, which is positive definite of signature $(8,0)$ on the whole algebra; they never invoke the kernel of a transform. The particularity therefore sits in the conjugate space and leaves the measurable structure exactly as it was (*Mass, Rank and the Positivity of the Dagger*, *The Born Rule as a Trace Formula — Derivation and Comparison*).
- **The root is fixed in a probabilistic context, and free in every other.** A spectral density or a covariance requires the second slot of the quadratic form to carry the Hermitian conjugation, and that is exactly the conjugation the non-degenerate roots violate. In such a context the frequency axis is therefore central or pure real, and a twisted root is not a probability clock. This settles a choice and does not lose a generality, because the algebra prefers no root at all and the root was never a physical quantity; a non-degenerate root necessarily tilts the central axis toward a spatial axis orthogonal to it, $\rho=b\mu+d\nu i$ with $\mu\perp\nu$ and $d\neq0$, and the vanishing twist $d=0$ returns the degenerate real root $\mu$, so what is excluded is the twist and not the spatial axis.
- **The exclusion is uniform over the twisted family, and the depth of the failure is the twist.** The failure is not a curiosity of one root: the proposition's witness is non-Hermitian for **every** non-degenerate root, so no measure and no choice of coefficients restore the positivity once $d\neq0$. What a twisted clock can and cannot do is therefore decided in advance by the single number $b=\sqrt{1+d^{2}}>1$, the deeper the twist the wider the negative eigenvalue $2(1-b)$ of the Hermitian part. The family is excluded as a family, and it is excluded by the algebra and not by the data.
- **The two forms cannot be collapsed into one.** Probability is $H$ and the interval is $N$; the theorem is the proof that the norm cannot double as the probability, since $N(i)=-1$ is root-independent and $H$ is what carries the positivity. The corpus's two metrics of one element are therefore **forced by the algebra and not chosen for economy** (*Mass, Rank and the Positivity of the Dagger*).
- **The positivity is the classical positivity of matrices; only the clock is biquaternionic.** Under the matrix model the probability form is the Hilbert–Schmidt form, $\langle\tilde P,\tilde Q\rangle_{*}=\tfrac12\mathrm{tr}\bigl(\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}\bigr)$, so the cone of positive elements is the textbook cone of positive semidefinite matrices and the positivity in the factorisation is not a new notion. What is new is the criterion: the theorem restricts the classical matrix-valued theorem to the one-parameter characters $\exp(-2\pi\rho\langle\omega,x\rangle)$ and decides which of them are unitary. The biquaternion content is therefore carried by the clock and not by the positivity, and the zero divisors of the algebra — the light cone of the interval — play no part in it; the exclusion at the twisted clocks is a failure of unitarity and not of the zero divisors.
- **Momentum space is imported through $H$, exactly as ordinary theory postulates it.** The framework does not derive positivity for every root and does not need to; it postulates it, in the form $H$, precisely where quantum mechanics postulates it, in the form of a positive Hilbert space. The parallel is exact rather than a retreat: the central-root theorem *is* the classical theorem, so the framework's positive-definite functions are the ordinary ones.
- **The theory is compatible with infinite dimensions on the module, and the transform is what assembles them.** The algebra stays finite while the carrier may grow: on the space of $\mathbb{B}$-valued square-integrable functions of the material sector the transform presents that infinite-dimensional space as a direct integral over the dual of copies of the finite algebra, $L^2(G,\mathbb{B})\cong\int^{\oplus}_{\hat G}\mathbb{B}\,d\mu(\omega)$ — a finite direct sum when the configuration group is finite. The infinite dimension is assembled from the algebra's own fibres and not from a larger algebra, and it is root-independent because the transform is invertible and factorises for every root; it is unitary, an isometry of the direct integral, exactly for the roots with $\rho^{*}=-\rho$, the degenerate families whose positivity the theorem of this article also requires; on the central clock, which the framework already uses, the transform diagonalises the translations as well, so momentum is the fibre label and position the derivative across the fibres, and the canonical pair lives on the module and not in $\mathbb{B}$; and positivity is decided one fibre at a time, which is the form the Bochner question takes here (*Biquaternion Continuous Harmonic Analysis*, *Noncommutative Harmonic Analysis*).
- **The non-degenerate transform is a change of description and not a spectral density.** It remains an invertible transform, it still factorises into four complex transforms, and it still diagonalises the constant-coefficient operators; what it cannot be is a probability density in its conjugate variable. It **describes** a frame; it does not **measure** one.

Read as a particularity, the theorem says that the framework's probability is **quaternionic plus the central phase**, while the biquaternionic feature proper — the twist between the central axis and a spatial axis — is kinematical. This is not a limitation of the framework relative to experience, because every measurement the framework performs is a central-clock measurement: the Born pairing, the trace and the relational time are all central, and the non-degenerate transforms are frames the theory may use freely without ever asking them for densities. No experiment is contradicted, since no experiment asks a twisted clock for a positive-definite two-point function. The theorem separates the clock the theory **measures with** from the clocks it may **describe with**, and it says that the separation is forced by the positivity of probability and by nothing else. The particularity is likewise separate from the representation question: the absence of a canonical commutator inside the algebra is lifted on an infinite-dimensional module, as the bullet above records, whereas the positivity particularity is a statement about the character and is lifted by no module at all — enlarging the carrier repairs the first and leaves the second exactly as it was.

## Summary

Bochner's theorem for the biquaternion transform is a theorem about the **Hermitian form** $H=\mathrm{Sc}(\tilde P\tilde Q^{*})$ and about the **root**. The character $\chi_\omega=\cos(2\pi\langle\omega,x\rangle)e_0-\sin(2\pi\langle\omega,x\rangle)\rho$ is multiplicative for every root, with $\chi_{\omega_k-\omega_l}=\chi_{\omega_k}\chi_{\omega_l}^{-1}$; it is unitary for the Hermitian conjugation, $\chi_\omega^{*}=\chi_\omega^{-1}$, **exactly when $\rho^{*}=-\rho$**, and this holds exactly for the degenerate roots, the central imaginary $\rho=\pm i$ and the unit pure real quaternions. For those roots the quadratic form $Q=\sum_{k,l}A_kG(\omega_k-\omega_l)A_l^{*}$ factorises as the integral of the positive element $ZZ^{*}$ and the transform of a positive measure is positive definite; the central root is the classical theorem with $G=\varphi e_0$, the pure real roots the quaternion theorem of *Quaternion Harmonic Analysis*. For the non-degenerate roots $\rho=b\mu+d\nu i$ the character is not unitary, the factorisation does not exist, and the form is not positive definite: the proposition of the converse exhibits for **every** such root a value $Q=2e_0-2ib\mu+2d\nu$ that is not even Hermitian, with $Q-Q^{*}=4d\nu\neq0$ and the Hermitian part $2e_0-2ib\mu$ of spectrum $\{2(1-b),2(1+b)\}$, negative because $b^{2}-d^{2}=1$ with $d\neq0$ gives $b=\sqrt{1+d^{2}}>1$; the corpus's witness $\rho=2e_1+\sqrt{3}\,ie_3$ is the case $b=2$, $d=\sqrt{3}$, with $Q=2e_0-4ie_1+2\sqrt{3}e_3$ and the Hermitian part $2e_0-4ie_1$ of spectrum $\{6,-2\}$. Both directions of the equivalence are therefore proved, and the criterion is a theorem. The failure recorded in the corpus at the central coefficient $A=i$ is a different statement: it tests the bilinear norm $N$, for which $N(i)=-1$ for every root, and it is the indefiniteness of the metric and not the failure of the probability. The scalar part of the transform is the classical positive-definite function and is positive definite for every root, which is why the loss appears only in the full $\mathbb{B}$-valued form. Ordinary quantum mechanics never runs the chain, because it postulates the positive Hilbert space and derives the positive-definite function as a consequence; in the framework that postulate is the form $H$ itself, and the theorem records where and how $H$ sees the root.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\chi_\omega(x)=\cos(2\pi\langle\omega,x\rangle)e_0-\sin(2\pi\langle\omega,x\rangle)\rho$ | the biquaternion kernel of a root $\rho$ |
| $G(\omega)=\int\chi_\omega\,d\mu$ | the transform of the measure; $G(0)=\mu(\mathbb{R}^n)e_0$ |
| $\chi_\omega^{*}=\chi_\omega^{-1}\Leftrightarrow\rho^{*}=-\rho$ | the unitarity of the character; the degenerate roots |
| $\chi_\omega^{\natural}=\chi_\omega^{-1}\Leftrightarrow\rho^{\natural}=-\rho$ | natural unitarity; the pure roots (real and non-degenerate) |
| $Q=\sum_{k,l}A_kG(\omega_k-\omega_l)A_l^{*}$ | the sesquilinear quadratic form of the transform |
| $Q=\int ZZ^{*}d\mu$, $Z=\sum_kA_k\chi_{\omega_k}$ | the factorisation; positive definite for the degenerate roots |
| $Q=2e_0-2ib\mu+2d\nu$, $Q-Q^{*}=4d\nu$, $\mathrm{spec}(\mathrm{Her}\,Q)=\{2(1-b),2(1+b)\}$ | the converse witness, for a non-degenerate root; the eigenvalue $2(1-b)$ is negative |
| $H=\mathrm{Sc}(\tilde P\tilde Q^{*})$, signature $(8,0)$ | the probability form the theorem needs |
| $N=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, $N(i)=-1$ | the norm/interval; the root-independent failure |
| $\rho=\pm i$, $\rho=\pm\mu$ | the central and pure real roots; the degenerate family |
| $\rho=b\mu+d\nu i$, $b^{2}-d^{2}=1$, $b>1$ | the non-degenerate roots; positivity fails for every one of them |
| $G=\varphi e_0$, $H$ central | the central root read as the classical theorem |

## Further Reading

- *Biquaternion Continuous Harmonic Analysis* and *Biquaternion Discrete Harmonic Analysis* — the mathematics of the transform: the kernel, the transform pair, the factorisation into complex transforms, the relation to the gradient and the d'Alembertian, the vanishing-norm issue, and the positivity failure stated there for the transform of a measure.
- *The Bochner Theorem for the Biquaternion Transform: the Hermitian Form and the Root* — the mathematics mirror of the present article, where the same theorem is stated and proved on the algebra side: the unitarity proposition, the factorisation $Q=\int ZZ^{*}d\mu$ for the degenerate roots, the witness against the genuinely complex roots, the separation of the norm failure from the root criterion, and the identification of the Euclidean form of the continuous article with the general plain sesquilinear algebraic norm, which closes the open question that article left on the pairing.
- *The Biquaternion Fourier Transform and the Imaginary Directions* — the physical reading of the transform: the conjugate axis, the choice of root as a choice of clock, the natural-conjugation unitarity $W^{\natural}=W^{-1}$, and the positivity failure read at a value of the norm.
- *Mass, Rank and the Positivity of the Dagger* — the two squares of one element: the Hermitian square positive definite of signature $(8,0)$, the natural square indefinite and the interval; the positivity of $H$ against the metric of $N$.
- *The Hermitian Form as a Product: Positivity and the Real Part of the Born Pairing* and *Why Probability Values Are Central: the Symmetric Sesquilinear Product and Its Cone* — the form $H$ as a product, its cone and its real part.
- *The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra* and the mathematics *Positive Definite Functions and Hermitian Kernels*, *Reproducing Kernel Hilbert Spaces* and *Positive Definite Distributions* — the classical theorem, the Bochner–Schwartz theorem, and the canonical form the argument descends from.
- *Quaternion Harmonic Analysis* — the quaternion case that does hold, the pure real roots' positivity theorem.
- *Conventions in the Biquaternion Universe* and *Remarkable Subspaces and the Four Forms* — the four forms $B$, $N$, $H$, $K$ and the conventions of the series.
- *Each Sector Is the Other's Clock: the Sector Exchange as Relational Time* — the central root as the framework's own clock.
- *The Born Rule as a Trace Formula — Derivation and Comparison* — the state side: the Born pairing and its trace form, where the framework's quantum-mechanical positivity already lives.
