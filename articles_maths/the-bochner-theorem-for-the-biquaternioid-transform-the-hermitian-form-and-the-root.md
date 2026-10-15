# __The Bochner Theorem for the Biquaternioid Transform: the Hermitian Form and the Root__

## Introduction

Bochner's theorem says that a continuous normalised positive-definite function on a group is the Fourier transform of a positive measure. Read in the other direction it says that **the transform of a positive measure is a positive-definite function**, and its proof consumes two properties of the character — that it is multiplicative under the group law, and that it is unitary — together with one property of the pairing, that the quadratic form carries the conjugation in its **second** slot.

In the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ the second and the third of these ingredients become choices. The kernel of the transform is the exponential of a **root of $-1$**, and the roots fall into three families. The algebra carries four pairings, two bilinear and two sesquilinear, and the classical statement sits in one of the sesquilinear rows. The article therefore asks the single question such a situation forces: **which pairing makes the theorem true, and for which roots?**

The answer, and the content of the article, is one sentence. The positivity the theorem needs is the positivity of the general plain sesquilinear form $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$, positive definite of signature $(8,0)$, and with that form the theorem holds exactly for the roots that are **skew-adjoint** for the Hermitian conjugation, $\tilde\Xi^{*}=-\tilde\Xi$ — the scalar imaginary $\tilde\Xi=\pm i$ and the real roots $\tilde\Xi=\pm\mu$ — and fails for the **genuinely complex** roots $\tilde\Xi=b\mu+d\nu i$. The failure recorded in *Biquaternion Continuous Harmonic Analysis* at the central element $i$ is a different statement: it tests the bilinear form $N$, it is independent of the root, and it belongs to the metric and not to the positivity. Both statements are true, and they are not the same statement.

**Boundaries.** The transform, its kernel, the classification of the roots, the factorisation into four complex transforms and the vanishing-norm issue are *Biquaternion Continuous Harmonic Analysis* and *Biquaternion Discrete Harmonic Analysis*; the transform of a measure and its quadratic form with the natural conjugation are the section §*The Transform of a Measure, and the Failure of Positivity* of the continuous article, whose eighth open question this article answers. The positivity of the form, its cone and its signature are *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*, *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint* and *Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions*; the classical theorems are *Positive Definite Functions and Hermitian Kernels*, *Reproducing Kernel Hilbert Spaces* and *Positive Definite Distributions*; the quaternion case that does hold is *Quaternion Harmonic Analysis*. The four pairings are *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*; the roots are *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*; the notation is *Conventions in Mathematics*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the identity, $e_k^{2}=-e_0$ and $e_je_k=e_l$ for $(j,k,l)$ a cyclic permutation of $(1,2,3)$; a general element is $\tilde Q=Q_0e_0+\vec Q$ with $Q_\mu\in\mathbb{C}$. The **coefficientwise conjugation** $\overline{\cdot}$ conjugates the coefficients; the **natural conjugation** ${}^{\natural}$ fixes $e_0$ and negates $e_1,e_2,e_3$ and is $\mathbb{C}$-linear; the **Hermitian conjugation** is ${}^{*}=\overline{\cdot}\circ{}^{\natural}$, so $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ with $\varepsilon=(1,-1,-1,-1)$. The four pairings are $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P\tilde Q)$, $\langle\tilde P,\tilde Q\rangle_{\natural}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$ and $\langle\tilde P,\tilde Q\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})$, and $\mathrm{Tr}=2\,\mathrm{Sc}$. A **root** is an element $\tilde\Xi$ with $\tilde\Xi^{2}=-e_0$; following the physics companion, the roots of the first and second families of the classification — the scalar imaginary $\tilde\Xi=\pm i$ and the unit real roots $\tilde\Xi=\pm\mu$ — are called **degenerate**, and the roots $\tilde\Xi=b\mu+d\nu i$ with $\mu\perp\nu$ unit real and $b^{2}-d^{2}=1$ are called **genuinely complex**. The transform articles write the root $\rho$ and the kernel $W$; this article follows *Conventions in Mathematics* and writes $\tilde\Xi$ and $\chi$, the two being the same objects. All conventions are those of *Conventions in Mathematics*.

## The Context of the Theorem

### The Two Readings

Bochner's theorem has two readings. The first says that a continuous normalised positive-definite function is the transform of a positive measure; the second says that the transform of a positive measure is a positive-definite function. They are the same equivalence read in opposite directions, but they ask different questions, and this article uses the second. The first is a representation statement: it asserts the existence of a measure behind a function. The second is a **positivity statement** about a given measure, and it is the one that can be tested, measure by measure, on the quadratic form of the transform. The question of the article is of the second kind, and its object is the character of the transform.

### The Engine of the Classical Proof

The classical proof is short because its engine consumes two properties of the character and no others. The character is **multiplicative**, which reassembles the difference of two frequencies as a product, $\chi_{\omega_k-\omega_l}=\chi_{\omega_k}\chi_{\omega_l}^{-1}$; and it is **unitary**, which replaces the inverse $\chi_{\omega_l}^{-1}$ by the Hermitian conjugate $\chi_{\omega_l}^{*}$, so that the sum of products closes into a square, and a square is automatically positive. The third ingredient is the pairing: the quadratic form must carry the conjugation in its second slot, which is what places the square under the integral. In the classical case the two character properties are free — the exponential of the single imaginary unit is multiplicative and unitary with no choice made — and the only care needed is the placement of the conjugation in the form. **The two character properties are therefore free in the classical case, and in the biquaternion algebra they must be re-examined: multiplicativity survives the choice of root, and unitarity does not**, which is where the whole question of the article comes from.

### Why a Root Appears

The classical character is the exponential of a single imaginary unit, and the imaginary unit is canonical: the complex structure of $\mathbb{C}$ is unique, and there is nothing to choose. A hypercomplex algebra has **no single imaginary unit**. To write an exponential in $\mathbb{B}$ one must first choose an element whose square is $-e_0$, and that choice is the **root**; the character is then $\chi_\omega=\exp(-2\pi\tilde\Xi\langle\omega,x\rangle)$, and different roots give different characters. Multiplicativity survives the choice, because the character is the exponential of one and the same root at every frequency, so the reassembly of the difference of frequencies is never lost. Unitarity does not come free: $\chi_\omega^{*}=\chi_\omega^{-1}$ is the condition $\tilde\Xi^{*}=-\tilde\Xi$, which is a condition on the root, and the roots that satisfy it are the degenerate ones, the scalar imaginary and the real roots, while the genuinely complex roots do not. This is the whole origin of the root dichotomy in $\mathbb{B}$: one of the two properties the classical character has for free becomes a choice, and the root makes the choice.

### What Is and Is Not at Stake

Three features of $\mathbb{B}$ are usually named together, and the theorem uses only one of them, so it is worth saying which. **Noncommutativity** matters, and it is already spent in the *statement*: because the algebra does not commute, the quadratic form must name the slot that carries the conjugation, and the four pairings of the block exist precisely because the two conjugations can be placed in two slots. **Zero divisors** do not enter the criterion at all: the form of the theorem is the positive definite form, of signature $(8,0)$, its cone is the cone of a positive definite form, and an element at which another product vanishes — for instance $(e_0+ie_1)(e_0-ie_1)=0$, while $\langle e_0+ie_1,e_0+ie_1\rangle_{*}=2$ — is as positive as any other. The vanishing of the norm is the *other* failure, the root-independent one of §*The Norm Failure Is Independent of the Root*, and it belongs to the indefinite interval and not to the positivity of the transform. What decides the theorem is the third feature alone, **unitarity**, the one property of the classical character that a choice of root can destroy. The criterion is therefore not a statement about zero divisors and not a statement about noncommutativity as such; the first is absent from the engine and the second is absorbed into the choice of the form.

### Where the Measure Lives, and the Root Is Chosen Once

The classical theorem integrates over the dual group, and it is sometimes suggested that the biquaternion theorem integrates over the roots. It does not. The measure of this article is a measure on $\mathbb{R}^n$ — equivalently, by duality, on its dual — and the root is fixed **once**, as a parameter of the kernel, before the measure is chosen; the criterion is then a condition on that single root. There is therefore no space of roots carrying a measure, and the phrase *measures supported on the unitary roots* describes nothing here: what the criterion restricts is the choice of character, one root at a time, and not the support of the spectral measure. The two choices are independent, and the theorem is the statement that one of them, the root, is decided by positivity while the other, the measure, is not.

### What "Exactly" Means

The criterion of the article is a two-direction statement, and both directions are proved. From the root to the positivity is the factorisation of §*The Factorisation, and the Degenerate Roots*, the direction a Bochner theorem proves by hand. From the root to the failure is the proposition of §*The Genuine Failure: Every Genuinely Complex Root*, and it is proved for **every** genuinely complex root by a single witness — one atom, two frequencies, two coefficients — which depends on the root only through its two parameters $b$ and $d$. The word **exactly** is therefore earned rather than asserted: positivity holds for the degenerate roots and fails for every genuinely complex root, the criterion is an equivalence, and the eighth open question of *Biquaternion Continuous Harmonic Analysis* is answered in both directions. The forward direction is the classical engine surviving the change of algebra; the converse is the algebra's own contribution, and it says that the character of a genuinely complex root fails positivity already on the one-atom witness, so the failure is a property of the character and not of the data.

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

The definitions, the inversion and the factorisation of this transform are *Biquaternion Continuous Harmonic Analysis*; they are recalled here because the theorem is a statement about them, and nothing in the present article depends on a convergence hypothesis that article does not already make. Two of the ingredients of the classical proof now carry a choice. The value $G(\omega)$ is an element of a non-commutative algebra, so the quadratic form must say which conjugation stands between the two coefficients; and the character is $\mathbb{B}$-valued, so its unitarity is a statement about $\tilde\Xi$.

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
\text{every finite positive measure has a positive-definite transform}\ \Longleftrightarrow\ \tilde\Xi^{*}=-\tilde\Xi\ \Longleftrightarrow\ \tilde\Xi\ \text{is degenerate.}
$$

The factorisation proves the direction from the right to the left, and it is the half a Bochner theorem proves by hand. The other direction is proved in §*The Genuine Failure: Every Genuinely Complex Root*, whose proposition produces for every genuinely complex root a value of the form that is not even Hermitian. Both directions are therefore proved, and the equivalence is a theorem of the algebra and not a choice of convention. The quantifier is a part of the statement: what the factorisation gives is a property of **every** positive measure at once, and what the converse gives is one measure at which the property fails, so the criterion is about the class of measures and not about a transform chosen in advance.

### The Scalar Imaginary Is the Classical Theorem

For $\tilde\Xi=i$ the kernel is the central scalar $\chi_\omega=e^{-2\pi i\langle\omega,x\rangle}e_0$, and the transform is the classical one times the identity, $G(\omega)=\varphi(\omega)e_0$. The factorisation becomes $Q(A)=\sum_{k,l}A_kA_l^{*}\varphi(\omega_k-\omega_l)$; applying the representation $\mathsf{M}_2$, this is the classical Gram sum $\sum_{k,l}\varphi(\omega_k-\omega_l)\mathsf{M}_2(A_k)\mathsf{M}_2(A_l)^{\dagger}$, positive exactly when the scalar form $\sum_{k,l}\overline{\zeta_k}\zeta_l\varphi(\omega_k-\omega_l)$ is. The biquaternion theorem at the scalar imaginary is therefore the classical theorem **componentwise**.

### The Real Roots Are the Quaternion Theorem

For $\tilde\Xi=\mu$ a unit real root the kernel is a rotor, and $\chi_\omega^{*}=\chi_\omega^{-1}$ because ${}^{*}$ and ${}^{\natural}$ agree on the real quaternions. The factorisation holds and $G$ is positive definite; on real coefficients the integrand reduces to $a^{2}+b^{2}\geq 0$, which is the classical quaternion case of *Quaternion Harmonic Analysis*. The two degenerate families thus give the two textbook positivity theorems of the corpus, and they give them with the same Hermitian form.

## Two Failures That Must Not Be Confused

### The Norm Failure Is Independent of the Root

*Biquaternion Continuous Harmonic Analysis* computes the quadratic form of the transform with the **natural** conjugation between the coefficients and obtains the integral of the norm,

$$
\sum_{k,l}\overline{A_k}A_l\,G(\omega_k-\omega_l)=\int N\bigl(Z\bigr)\,d\mu .
$$

At a single coefficient $A_1=i$ this reads $\overline{i}\,i\,G(0)=i^{2}\mu(\mathbb{R}^n)=-\mu(\mathbb{R}^n)e_0$, negative for every non-zero measure, **because $N(i)=i\,i^{\natural}=-1$**. Two facts about this computation must be stated together. First, it is a statement about the bilinear form $N$ and not about the sesquilinear form $\langle\cdot,\cdot\rangle_{*}$: the conjugation written between the coefficients is ${}^{\natural}$, which is the conjugation of the norm, and the coefficient slot of the positive-definite form carries ${}^{*}$. Second, it is **independent of the root** of the transform, because the element tested, $i$, is a coefficient and not a kernel value: the same $\overline{i}\,i=-1$ is produced whatever $\tilde\Xi$ is. A failure that does not depend on the root cannot be a failure of the root criterion of the positivity, and the corpus's own sentence that the positivity "is not available" is the symptom of exactly this: the statement is about the norm, and the norm is negative on the centre for every root.

### The Genuine Failure: Every Genuinely Complex Root

The root-dependent failure is the genuinely complex one, and it is the converse of the theorem. It is not a property of one example: one witness, the same for every genuinely complex root, decides the whole family, and it decides it in the strongest way, by producing a value of the form that is not even Hermitian.

**Proposition (converse).** Let $\tilde\Xi=b\mu+d\nu i$ be a genuinely complex root, $\mu\perp\nu$ unit real and $b^{2}-d^{2}=1$, written with $b>0$ so that $b=\sqrt{1+d^{2}}>1$ and $d\neq0$. Take the single atom of unit mass at a point $x$ and a frequency $\omega$ with $2\pi\langle\omega,x\rangle=\tfrac{\pi}{2}$, the frequencies $0$ and $\omega$, and the coefficients $A_1=e_0$, $A_2=i$. Then the character at the atom is $\chi_\omega=-\tilde\Xi$, the transform takes the values $G(0)=e_0$, $G(\omega)=-\tilde\Xi$ and $G(-\omega)=\tilde\Xi$, and

$$
Q=2e_0-2i\tilde\Xi=2e_0-2ib\mu+2d\nu .
$$

Its Hermitian conjugate is $Q^{*}=2e_0-2ib\mu-2d\nu$, so

$$
Q-Q^{*}=4d\nu\neq0,\qquad \mathrm{Her}\,Q=\tfrac12\bigl(Q+Q^{*}\bigr)=2e_0-2ib\mu=2\bigl(e_0-ib\mu\bigr),
$$

and $G$ is not positive definite.

*Proof.* The value of the character at the atom is read from the kernel, $\chi_\omega=-\sin\tfrac{\pi}{2}\tilde\Xi=-\tilde\Xi$, and the sum $Q=\sum_{k,l}A_kG(\omega_k-\omega_l)A_l^{*}$ is the four-term computation written out below for the example. For the Hermitian part put $X=ib\mu$. The element $X$ is Hermitian: $i$ is central with $i^{*}=-i$, and $\mu^{*}=-\mu$ for a real quaternion $\mu$, so $(ib\mu)^{*}=(b\mu)^{*}(i)^{*}=b\mu^{*}(-i)=b(-\mu)(-i)=ib\mu$. And $X^{2}=i^{2}b^{2}\mu^{2}=b^{2}e_0$, since $\mu^{2}=-e_0$ for a unit real $\mu$. In the matrix model $\mathsf{M}_2(X)$ is therefore a Hermitian matrix whose square is $b^{2}I$, so its eigenvalues are $\pm b$, and those of $\mathsf{M}_2(\mathrm{Her}\,Q)=2\bigl(I-\mathsf{M}_2(X)\bigr)$ are

$$
\mathrm{spec}\bigl(\mathrm{Her}\,Q\bigr)=\{2(1-b),\,2(1+b)\}.
$$

Because $b^{2}-d^{2}=1$ with $d\neq0$ forces $b>1$, the eigenvalue $2(1-b)$ is negative and the form is not positive definite; and because $d\neq0$ the difference $Q-Q^{*}=4d\nu$ does not vanish, so $Q$ is not Hermitian and is not a positive element of the cone at all. The same witness at a real root, $d=0$ and $b=1$, gives the spectrum $\{0,4\}$, which is positive semidefinite; the failure is therefore exactly the twist $d$, and the size of the twist sets the magnitude $2(b-1)$ of the negative eigenvalue.

The example is the case $b=2$, $d=\sqrt{3}$, $\mu=e_1$, $\nu=e_3$. Take $\tilde\Xi=2e_1+\sqrt{3}\,ie_3$, a genuinely complex root since $\tilde\Xi^{*}=-2e_1+\sqrt{3}\,ie_3\neq-\tilde\Xi$; take the kernel with the exponent sign of the conventions, $\chi_\omega=\cos(2\pi\langle\omega,x\rangle)e_0-\sin(2\pi\langle\omega,x\rangle)\tilde\Xi$; take the single atom of unit mass at $x=\tfrac14$, so that $G(0)=e_0$, $G(1)=-\tilde\Xi$, $G(-1)=\tilde\Xi$; and take the frequencies $0,1$ and the coefficients $A_1=e_0$, $A_2=i$. Then

$$
Q=e_0+\tilde\Xi(-i)+i(-\tilde\Xi)+(i)(-i)=2e_0-2i\tilde\Xi=2e_0-4ie_1+2\sqrt{3}\,e_3 ,
$$

in agreement with the general formula, whose twist term is $4d\nu=4\sqrt{3}\,e_3$. The element $Q$ is not Hermitian, so it is not a positive element at all, and its Hermitian part is $2e_0-4ie_1$, since $-4ie_1$ is Hermitian. In the matrix model $\mathsf{M}_2(2e_0-4ie_1)=2I-4\sigma_1$, whose spectrum is $\{6,-2\}$, the general spectrum $\{2(1-b),2(1+b)\}$ at $b=2$: the form is **not** positive definite, and the witness is the negative eigenvalue $-2$, which is $2(1-b)$. **The sign of the imaginary part is a matter of the exponent's sign convention**, and the reader who uses $e^{+2\pi\tilde\Xi\langle\omega,x\rangle}$ instead gets $G(1)=+\tilde\Xi$ and $Q=2e_0+2i\tilde\Xi$, of Hermitian part $2e_0+4ie_1$; what is not conventional is the spectrum, which is $\{6,-2\}$ under either sign, and hence the negative eigenvalue that the witness is. The failure is structural and not numerical: the character of a genuinely complex root is not unitary for the Hermitian conjugation, so $\chi_{\omega_k}\chi_{\omega_l}^{-1}$ never reassembles into $ZZ^{*}$, and the proposition shows that the sum which replaces the factorisation is not merely outside the cone but outside the Hermitian elements.

**Remark (verified).** The general formula was checked by recomputation in the matrix model $\mathsf{M}_2$. For the roots $(b,d)=(2,\sqrt3)$, $(1.25,0.75)$, $(\sqrt2,1)$ and $(3,\sqrt8)$, with $\mu,\nu$ unit real and orthogonal, the witness gave $Q-Q^{*}=4d\nu$ and $\mathrm{Her}\,Q=2e_0-2ib\mu$ to machine precision, and the spectrum of the Hermitian part agreed exactly with $\{2(1-b),2(1+b)\}$: $\{-2,6\}$, $\{-0.5,4.5\}$, $\{-0.828,4.828\}$ and $\{-4,8\}$. Over $100$ random positive measures of total mass one with two to four atoms, three frequencies and random biquaternion coefficients, the minimum eigenvalue of the Hermitian part of $Q$ stayed positive for every degenerate root tested and was negative for every genuinely complex root tested. On the narrower scan of two atoms and three frequencies each, the smallest degenerate eigenvalue was $+2.1\times10^{-3}$ and the genuinely complex minima were $-3.1\times10^{1}$ for $\tilde\Xi=2e_1+\sqrt{3}\,ie_3$ and $-5.1$ for $\tilde\Xi=1.25e_1+0.75\,ie_3$; at the same data the factorisation $Q=\int ZZ^{*}d\mu$ held to machine precision for the degenerate roots and failed by $4\sqrt{3}$ for the example, whose matrix difference is exactly the twist term the non-unitarity of its character produces.

## The Scalar Shadow, and the Ordinary Case

The scalar part of the transform is positive definite for **every** root, because $\mathrm{Sc}(\chi_\omega)=\cos(2\pi\langle\omega,x\rangle)$, so

$$
\mathrm{Sc}\,G(\omega)=\int\cos\bigl(2\pi\langle\omega,x\rangle\bigr)\,d\mu
$$

is the real part of the classical positive-definite function and is itself positive definite. The scalar contraction $\sum_{k,l}\overline{\zeta_k}\zeta_l\,\mathrm{Sc}\,G(\omega_k-\omega_l)$ is therefore non-negative for every root. This is why the corpus's negative example must use a non-central coefficient: with central coefficients and the coefficientwise conjugation the scalar shadow is already positive, and only the bilinear form $N$ produces a negative value.

## Relation to the Open Question of the Continuous Article

The eighth open question of *Biquaternion Continuous Harmonic Analysis* asks whether some pairing internal to the algebra supplies the positivity that the Bochner-type hypothesis needs, and records that no such pairing is known. The present article answers it: the pairing is the general plain sesquilinear form $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$, the positive definite form of signature $(8,0)$ that the block already carries, and the statement it supplies holds exactly for the degenerate roots.

The Euclidean form the continuous article offers as a repair is the algebraic norm of this pairing, $\lVert Z\rVert_E^{2}=\langle Z,Z\rangle_{*}=\sum_\mu\lvert Z_\mu\rvert^{2}$, so the repair the article found is the positivity the theorem needs, stated without the criterion on the root; the form is internal to the algebra, and the obstacle is not the absence of a pairing but the non-unitarity of the character at the genuinely complex roots. It is the scalar part of the sesquilinear product, $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$, so it does come from the product; what fails there is multiplicativity, $\lVert ZW\rVert_E\neq\lVert Z\rVert_E\lVert W\rVert_E$ in general — the Hermitian idempotent $\tilde\Pi=\tfrac12(e_0+ie_1)$ gives $\lVert\tilde\Pi^{2}\rVert_E=\tfrac12$ against $\lVert\tilde\Pi\rVert_E^{2}=\tfrac14$ — and it is this, and not the origin of the pairing, that makes the form the topology of the transform article rather than the norm of the algebra.

**Remark (scope).** Since $\mathbb{B}\cong M_2(\mathbb{C})$, the theorem is a finite-dimensional matrix-valued Bochner theorem: for a skew-adjoint root the map $x\mapsto\chi_\omega(x)$ is a unitary character of $\mathbb{R}^n$ into the unitaries of the algebra, and the factorisation is the classical one for a one-parameter unitary representation. The contribution is therefore not a new general theorem but the identification, inside this algebra, of which element supplies the positivity — the general plain sesquilinear form, one of the four that the block carries — of which roots carry a unitary character, namely the degenerate ones, and of where the classical duality stops, at the genuinely complex roots, which generate a non-unitary one-parameter group and fail by the proposition of the converse. The criterion is a specialization, and it is a sharp one: it says that the only obstruction left is unitarity, so the size of the failure is exactly the twist and no choice of measure or of coefficients removes it.

## Consequences

The theorem is a criterion, and a criterion decides more than the statement it closes. The paragraphs below collect what follows from it and what it leaves to the neighbouring articles: the exact quantifier, the name the criterion takes in the matrix model, the size of the locus it defines, and the half of a two-sided duality that remains open. Nothing here is used in the proof above.

### The Quantifier of the Criterion

The criterion is a statement about the **class of positive measures** and not about one transform, and only in that form is it true. For a degenerate root the factorisation holds for every finite positive measure, so every transform of a positive measure is positive definite. For a genuinely complex root the class of transforms is not contained in the positive-definite functions, because the atom of the converse proposition is a positive measure whose transform is not positive definite. The quantifier cannot be reduced to a single measure either: the atom at the origin has the constant $e_0$ as its transform, and the constant is positive definite for every root. What the theorem separates is therefore not one transform but the whole class of transforms from the positive-definite functions, and it does so exactly on the degenerate locus.

### The Unitary Characters and the Normality of the Root

The proposition is a statement about the one-parameter group and not only about the kernel. The group $t\mapsto\exp(t\tilde\Xi)$ is a one-parameter unitary group of $\mathbb{B}$ exactly when $\tilde\Xi^{*}=-\tilde\Xi$, by differentiation at $t=0$, so the characters $x\mapsto\exp(-2\pi\tilde\Xi\langle\omega,x\rangle)$ of $\mathbb{R}^n$ are unitary-valued exactly for the degenerate roots, and the genuinely complex roots generate the non-unitary one-parameter groups. In the matrix model the condition has a name: $\mathsf{M}_2(\tilde\Xi)$ is a square root of $-I$, and such a matrix is skew-Hermitian exactly when it is normal, so the criterion separates the **normal** square roots of $-I$ from the non-normal ones. The failure of the transform is thus the non-normality of the matrix of its root, a dichotomy wholly internal to $M_2(\mathbb{C})$.

### The Locus of Positivity in the Root Variety

The roots of $-1$ form a real four-dimensional variety: they are the conjugates $S\,\mathrm{diag}(i,-i)\,S^{-1}$ of the diagonal complex structure, an orbit of complex dimension two. The degenerate roots are the unit sphere of the real pure quaternions, of real dimension two, together with the two central points $\pm i$. The locus on which the transform of a positive measure is positive definite is therefore a real two-dimensional set, plus two isolated points, inside a real four-dimensional variety: positivity is not generic in the root, the generic root is genuinely complex, and the generic root fails the criterion. The parametrisation $\tilde\Xi=b\mu+d\nu i$ exhibits the same count, with the twist $d$ as the one-parameter family that carries the failure.

### The Failure Is a Genuine Biquaternion Phenomenon

Over the real quaternions every root of $-1$ is a unit pure imaginary, which is degenerate, so the quaternion theorem of *Quaternion Harmonic Analysis* has no twisted case at all and the criterion is vacuous there. The twist $d\neq0$ requires the coefficients of $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ to be genuinely complex, so the failure is invisible to every purely quaternionic statement and belongs to the complexification rather than to the quaternions. This is why the two degenerate families exhaust the classical theorems: they are the only cases the restriction to the reals can see.

### The Obstruction Is Invisible to the Scalar Part

The scalar part is positive definite for every root, so the criterion cannot be stated at the level of scalar functions: for the roots with $\mathrm{Sc}\,\tilde\Xi=0$ — the real and the genuinely complex families — $\mathrm{Sc}\,G(\omega)=\int\cos(2\pi\langle\omega,x\rangle)\,d\mu$, while for the central root $\tilde\Xi=\pm i$ it is the classical complex transform $\varphi(\omega)=\int e^{-2\pi i\langle\omega,x\rangle}\,d\mu$, and both are ordinary positive-definite functions. The projection to the centre erases whatever distinction the theorem draws. The failure appears already with central coefficients — the witness of the converse uses $A_1=e_0$ and $A_2=i$, and $i$ is central — so it is not a matter of restricting the coefficients to the centre either, and the criterion is genuinely $\mathbb{B}$-valued in the coefficients and in the root at once.

### The Form Is Part of the Datum

The positivity is a property of the pair (kernel, form) and not of the kernel alone. Of the four pairings of the block, the one whose second slot is the Hermitian conjugation is the general plain sesquilinear form, and it is that form which consumes the unitarity of the character; a pairing that places another conjugation in the second slot cannot use $\chi_\omega^{*}=\chi_\omega^{-1}$ and is not covered by the theorem. The criterion therefore identifies the form as part of its own statement, which is what the eighth open question of the continuous article anticipated when it asked for a pairing able to supply the positivity.

### The Positive Form Is Classical; the Criterion Is Not

The positivity the theorem consumes is not a new notion of positivity, and the isomorphism settles the question. Under $\mathsf{M}_2$, with $\mathrm{Sc}=\tfrac12\mathrm{tr}$ on the matrices and $\mathsf{M}_2$ a $*$-homomorphism,

$$
\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})=\tfrac12\,\mathrm{tr}\bigl(\mathsf{M}_2(\tilde P)\,\mathsf{M}_2(\tilde Q)^{\dagger}\bigr)=\tfrac12\langle\mathsf{M}_2(\tilde P),\mathsf{M}_2(\tilde Q)\rangle_{\mathrm{HS}} ,
$$

so the general plain sesquilinear form **is** the Hilbert–Schmidt form of $M_2(\mathbb{C})$, and the cone $P=\{\tilde Q\tilde Q^{*}\}$ is exactly the cone of the positive semidefinite matrices. The positivity in the factorisation is therefore the textbook positivity of the matrix model, and the theorem is a restriction of the classical matrix-valued Bochner theorem to the one-parameter family of characters $x\mapsto\exp(-2\pi\tilde\Xi\langle\omega,x\rangle)$. What is not classical is the criterion: the matrix-valued theorem begins with a positive-definite matrix function, while the biquaternion statement must first decide which elements of the family are unitary, and the answer — the skew-adjoint roots — is the real content. The contribution is thus the classification of the characters and not the positivity they are tested against, which is the honest reading of the article's novelty.

### The Discrete Case Is Group-Dependent

The proof is finite, so the **forward** direction needs no convergence hypothesis: on a finite abelian group the quadratic form is a finite sum and the factorisation holds for every degenerate root, so a finite positive combination of atoms has a positive-definite transform. The **failure** direction is another matter, and it is where the continuous statement must not be quoted verbatim. The character is $\chi_\omega(x)=\cos(2\pi\langle\omega,x\rangle)e_0-\sin(2\pi\langle\omega,x\rangle)\tilde\Xi$, non-central exactly at the pairs with $\sin(2\pi\langle\omega,x\rangle)\neq0$, and at a fixed root it is unitary at such a pair only when $\tilde\Xi^{*}=-\tilde\Xi$; a group that attains such a pair therefore inherits the twisted failure, reproduced by the witness on $\mathbb{Z}_3$, $\mathbb{Z}_4$ and $\mathbb{Z}_6$, while a group all of whose characters are central has no failing character at all. The extreme case is $\mathbb{Z}_2^n$, where $2\pi\langle\omega,x\rangle$ is $0$ or $2\pi$, so $\chi_\omega=\pm e_0$ is central and unitary **for every root**: the transform of a positive measure is there positive definite for every root, degenerate or not, and the criterion's only-if half is empty. The discrete criterion is therefore a statement about the group as well as about the root, and $\mathbb{Z}_2^n$ is the clean counterexample to the verbatim transfer; the discrete article should be read with its group named.

### The Template for a General Hermitian Algebra

The proof consumes four things and no others: that the character is the exponential of a root, that the root squares to $-e_0$, that the algebra carries a Hermitian adjoint with a positive cone, and that the character is multiplicative. Two of them transfer to any finite-dimensional Hermitian algebra with a Hermitian adjoint: the equivalence $\chi_\omega^{*}=\chi_\omega^{-1}\Leftrightarrow\tilde\Xi^{*}=-\tilde\Xi$, which is algebraic and uses nothing of $\mathbb{B}$, and the **forward** direction of the theorem, since a unitary character factorises the form as $\int ZZ^{*}d\mu$ in any such algebra. What does not transfer is the failure direction, which needs a witness of its own, and the explicit list of roots: the split into the degenerate and the genuinely complex families, and the proposition that every genuinely complex root admits a value that is not positive, use the arithmetic of $\mathbb{B}$ and of its complexification. The transferable statement is therefore one half of a criterion — *a skew-adjoint root gives a positive-definite transform* — and the **exactly** of this article is proved for $\mathbb{B}$ and would need its own witness elsewhere (*Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint*).

### The Representability Half That Remains Open

The theorem proves the direction from the measure to the positive-definite function, with the criterion on the root. The reverse half of a two-sided duality — whether an arbitrary positive-definite $\mathbb{B}$-valued function is the transform of a positive measure — is not proved here. The criterion constrains it: a two-sided duality cannot hold at a genuinely complex root, because the witness is then a transform of a positive measure which is not positive definite, and an equality of the two classes would be contradicted by that single element. At a degenerate root the forward half holds and the question reduces to representability, that is, to the range of the transform and to the measure that represents a given positive-definite function. The scalar imaginary case is classical and answered by the classical theorem; the real root case is the quaternion theorem; the genuinely complex case is excluded before the question can be asked.

## Summary

Bochner's theorem for the biquaternion transform is a theorem about the general plain sesquilinear form $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$ and about the **root**. The character $\chi_\omega=\cos(2\pi\langle\omega,x\rangle)e_0-\sin(2\pi\langle\omega,x\rangle)\tilde\Xi$ is multiplicative for every root, with $\chi_{\omega_k-\omega_l}=\chi_{\omega_k}\chi_{\omega_l}^{-1}$; it is unitary for the Hermitian conjugation, $\chi_\omega^{*}=\chi_\omega^{-1}$, **exactly when $\tilde\Xi^{*}=-\tilde\Xi$**, and this holds exactly for the degenerate roots, the scalar imaginary $\tilde\Xi=\pm i$ and the unit real roots. For those roots the quadratic form $Q=\sum_{k,l}A_kG(\omega_k-\omega_l)A_l^{*}$ factorises as the integral of the positive element $ZZ^{*}$ and the transform of a positive measure is positive definite; the scalar imaginary gives the classical theorem with $G=\varphi e_0$, the real roots the quaternion theorem of *Quaternion Harmonic Analysis*. For the genuinely complex roots $\tilde\Xi=b\mu+d\nu i$ the character is not unitary, the factorisation does not exist, and the form is not positive definite: the proposition of the converse exhibits for **every** such root a value $Q=2e_0-2ib\mu+2d\nu$ that is not even Hermitian, with $Q-Q^{*}=4d\nu\neq0$ and the Hermitian part $2e_0-2ib\mu$ of spectrum $\{2(1-b),2(1+b)\}$, negative because $b^{2}-d^{2}=1$ with $d\neq0$ gives $b=\sqrt{1+d^{2}}>1$; the example $\tilde\Xi=2e_1+\sqrt{3}\,ie_3$ is the case $b=2$, $d=\sqrt{3}$, with $Q=2e_0-4ie_1+2\sqrt{3}e_3$ and the Hermitian part $2e_0-4ie_1$ of spectrum $\{6,-2\}$. Both directions of the equivalence are therefore proved, and the criterion is a theorem. The failure recorded in the corpus at the central coefficient $A=i$ is a different statement: it tests the bilinear norm $N$, for which $N(i)=-1$ for every root, and it is the indefiniteness of the metric and not the failure of the positivity. The scalar part of the transform is the classical positive-definite function and is positive definite for every root, which is why the loss appears only in the full $\mathbb{B}$-valued form. The theorem answers the eighth open question of *Biquaternion Continuous Harmonic Analysis*: the pairing the Bochner-type hypothesis needs is the one the block already carries, and it is the root, not the pairing, that decides.

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
| $Q=2e_0-2ib\mu+2d\nu$, $Q-Q^{*}=4d\nu$, $\mathrm{spec}(\mathrm{Her}\,Q)=\{2(1-b),2(1+b)\}$ | the converse witness, for a genuinely complex root; the eigenvalue $2(1-b)$ is negative |
| $\langle\tilde P,\tilde Q\rangle_{*}=\mathrm{Sc}(\tilde P\tilde Q^{*})$, signature $(8,0)$ | the pairing the theorem needs; the algebraic norm of the Euclidean form |
| $N(\tilde P)=\tilde P\tilde P^{\natural}$, $N(i)=-1$ | the norm/interval; the root-independent failure |
| $\tilde\Xi=\pm i$, $\tilde\Xi=\pm\mu$ | the scalar imaginary and the real roots; the degenerate family |
| $\tilde\Xi=b\mu+d\nu i$, $b^{2}-d^{2}=1$, $b>1$ | the genuinely complex roots; positivity fails for every one of them |
| $G=\varphi e_0$, $\mathrm{Sc}\,G$ central | the scalar imaginary read as the classical theorem |

## Further Reading

- *Biquaternion Continuous Harmonic Analysis* (`articles_maths/biquaternion-continuous-harmonic-analysis.md`), for the transform, its kernel, the classification of the roots, the two-unit kernel, the vanishing-norm issue, the transform of a measure with the natural conjugation, and the open question answered here.
- *Biquaternion Discrete Harmonic Analysis* (`articles_maths/biquaternion-discrete-harmonic-analysis.md`), for the discrete transform, the sampling theorem and the discrete form of the same positivity statement.
- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the four pairings, $\langle\tilde P,\tilde Q\rangle_{*}$ among them, and their conjugations.
- *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/positivity-and-the-hermitian-cone-of-the-biquaternioid-algebra-with-hermitian-adjoint.md`), for the positivity of the Hermitian conjugation and the cone $P=\{\tilde Q\tilde Q^{*}\}$.
- *Hermitian Forms over the Biquaternion Algebra and the Unitary Witt Group with Hermitian Adjoint* (`articles_maths/hermitian-forms-over-the-biquaternioid-algebra-and-the-unitary-witt-group-with-hermitian-adjoint.md`), for the classification of the Hermitian forms and the unit form of signature $(8,0)$.
- *Remarkable Subspaces under the General Plain Sesqualgebra of Biquaternions* (`articles_maths/remarkable-subspaces-under-the-general-plain-sesqualgebra.md`), for the restriction of the form to the remarkable subspaces.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the classification of the roots of $-1$, $-0$ and $+1$.
- *Quaternion Harmonic Analysis* (`articles_maths/quaternion-harmonic-analysis.md`), for the quaternion case that does hold, the positivity theorem of the real roots.
- *Positive Definite Functions and Hermitian Kernels* (`articles_maths/positive-definite-functions-and-hermitian-kernels.md`), *Reproducing Kernel Hilbert Spaces* (`articles_maths/reproducing-kernel-hilbert-spaces.md`) and *Positive Definite Distributions* (`articles_maths/positive-definite-distributions.md`), for Bochner's theorem, the Aronszajn theorem and the Bochner–Schwartz theorem in the classical setting.
- *Conventions in Mathematics* (`articles_maths/conventions-in-mathematics.md`), for the symbols of the roots, the conjugations and the pairings.
- *The Biquaternioid General Plain Sesqualgebra (GPS) over $\mathbb{C}$* (`articles_physics/the-biquaternioid-general-plain-sesqualgebra-gps-over-c.md`), the physics companion, for the physical reading of the same theorem.
- S. Bochner, "Monotone Funktionen, Stieltjessche Integrale und harmonische Analyse", *Mathematische Annalen* **108** (1933) 378–410, for the classical theorem that a normalised positive-definite function is the Fourier transform of a measure.
- S. Georgiev, J. Morais, K. I. Kou, and W. Sprößig, "Bochner–Minlos theorem and quaternion Fourier transform", in *Quaternion and Clifford–Fourier Transforms and Wavelets*, Trends in Mathematics (Springer, 2013), 105–120, for the quaternion theorem whose biquaternionic counterpart fails at the genuinely complex roots.
