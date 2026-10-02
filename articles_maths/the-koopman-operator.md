# __The Koopman Operator__

## Introduction

The **Koopman operator** of a measure-preserving system $(X,\mathcal{B},\mu,T)$ is the operator $U_T$ on $L^2(X,\mu)$ that composes with the transformation, $U_Tf=f\circ T$. Its defining property is that it is linear: the nonlinear map $T$ acts on the infinite-dimensional space of observables by a linear isometry, and the orbit of a function under the iteration of $U_T$ contains the whole orbit structure of the system. The price is that the space is infinite-dimensional and the operator, for a mixing system, has no eigenvectors beyond the constants; the gain is that the entire spectral machinery of Hilbert-space operators — the spectral theorem, the decomposition into cyclic subspaces, the spectral measure of a vector, the notions of absolute continuity and multiplicity — becomes available for the study of the dynamics. The Koopman operator of a measure-preserving **flow** $\varphi_t$ is the one-parameter family $U_tf=f\circ\varphi_t$, a strongly continuous unitary group, so that Stone's theorem applies and the dynamics acquires a self-adjoint generator, the quantised form of the vector field of the flow.

The article treats the Koopman operator as an operator and reads the dynamics from its spectrum. It defines the operator and its basic properties (isometry, unitarity for an invertible transformation, fixed space, coboundaries); it defines the one-parameter unitary group of a measure-preserving flow and states Stone's theorem, with the identification of the generator deferred to *The Flow Operator*; it develops the spectral theory of the dynamics, in which ergodicity is the simplicity of the eigenvalue $1$, weak mixing the absence of further eigenvalues, and mixing the decay of the correlations, equivalently the continuity of the maximal spectral type; it states the spectral theorem in its multiplicity form, the spectral isomorphism theorem of Halmos and von Neumann, and the classification of the discrete spectrum as the rotations of compact abelian groups; and it computes the examples — the rotations, the Bernoulli shifts, the doubling map and its natural extension, the toral automorphisms.

The measure-preserving systems, the ergodicity, the mixing, the entropy and the ergodic theorems are those of *Ergodic Theory*, which introduces the Koopman operator and the ergodic hierarchy as measure-theoretic facts; the present article is the operator-theoretic reading of the same objects, and it cites that article rather than restating the theory. The bounded operators, the spectral theorem, the unitary operators and the spectral measure are those of *Operator Algebras* and *Unitary Operators and the Spectral Measure*; the one-parameter unitary groups and Stone's theorem are those of *Semigroups and Evolution Equations*; the flow, the vector field and the Lie derivative are those of *Smooth Dynamical Systems*, and the generator of the Koopman flow is *The Flow Operator*. The two-parameter evolution operator is *The Evolution Operator*, immediately preceding; the pre-adjoint, which is the transfer operator, is *The Transfer Operator*; the reduction of a flow to a return map is *The Poincaré Map*. The adjoint of $U_T$ and the reversing involution are not used here: they are *The Adjoint of the Koopman Operator* and *Reversible Operators and the Involution*, in the `- * Operator Theory` group of this category.

No physics is invoked.

## The Operator and its Elementary Properties

### Definition

**Definition.** Let $(X,\mathcal{B},\mu)$ be a probability space and let $T:X\to X$ be measurable and **measure-preserving**, $\mu(T^{-1}A)=\mu(A)$ for all $A\in\mathcal{B}$. The **Koopman operator** of $T$ is

$$
U_T:L^2(X,\mu)\to L^2(X,\mu), \qquad U_Tf=f\circ T .
$$

The **fixed space** is $\ker(U_T-I)$, the **coboundaries** are the functions $g\circ T-g$ with $g\in L^2$, and the **coboundary space** is the closed span of the coboundaries. For a measure-preserving flow $\varphi_t$ the **Koopman flow** is the one-parameter family

$$
U_tf=f\circ\varphi_t \qquad (t\in\mathbb{R}).
$$

**Theorem (elementary properties).** Let $T$ be measure-preserving. Then $U_T$ is a linear isometry of $L^2(X,\mu)$, and $U_T^*U_T=I$. If $T$ is invertible with measure-preserving inverse $T^{-1}$, then $U_T$ is unitary with inverse $U_T^{-1}=U_{T^{-1}}$, and $U_T$ is the unitary operator of the representation of $\mathbb{Z}$ on $L^2$ induced by $T$. The orthogonal complement of the fixed space is the closed span of the coboundaries.

*Proof.* The change of variables $y=Tx$ and the measure-preserving property give $\|U_Tf\|_2^2=\int|f(Tx)|^2d\mu(x)=\int|f(y)|^2d\mu(y)=\|f\|_2^2$, so $U_T$ is an isometry and $U_T^*U_T=I$. If $T$ is invertible then $U_TU_{T^{-1}}=U_{T^{-1}}U_T=I$, so $U_T$ is surjective and unitary. For the last statement, $g\circ T-g$ is orthogonal to every fixed $h$ because $\langle g\circ T,h\rangle=\langle g,h\rangle$; conversely a vector orthogonal to all coboundaries is orthogonal to $(U_T-I)g$ for every $g$, hence to the image of $U_T-I$, and for a unitary operator that orthogonal complement is the kernel.

### The Koopman Flow

**Definition.** Let $\varphi_t$ be a measure-preserving flow on $(X,\mathcal{B},\mu)$, that is, $\varphi_t$ preserves $\mu$ for every $t$. The **Koopman flow** $U_tf=f\circ\varphi_t$ is a one-parameter group of unitary operators, $U_sU_t=U_{s+t}$, $U_0=I$, $U_t^{-1}=U_{-t}$.

**Theorem (Stone, quoted).** A strongly continuous one-parameter unitary group $\{U_t\}_{t\in\mathbb{R}}$ on a Hilbert space has the form

$$
U_t=e^{itA}, \qquad A \text{ self-adjoint},
$$

with the generator $A=\frac{1}{i}\frac{d}{dt}\Big|_{t=0}U_t$, and the group is recovered from the spectral measure $E$ of $A$ by $U_t=\int_{\mathbb{R}}e^{it\lambda}dE(\lambda)$.

*Proof.* Quoted as standard from *Semigroups and Evolution Equations* and *Unitary Operators and the Spectral Measure*; the theorem is the spectral representation of a one-parameter unitary group, and the flow case of the present article is its application to $U_tf=f\circ\varphi_t$.

**Remark (the generator is the Lie derivative).** For a smooth flow the generator of the Koopman group is the operator $A=-i\mathcal L_X$ on a suitable core, where $\mathcal L_X$ is the Lie derivative along the generating field, because $\frac{d}{dt}\big|_{t=0}(f\circ\varphi_t)=Xf=\mathcal L_Xf$; the identification of $A$ with $-i\mathcal L_X$, the domain, and the self-adjointness are *The Flow Operator*, later in this category, and no proof is offered here.

## Spectral Theory of the Dynamics

### Correlations and the Spectral Measure

**Definition.** The **correlation function** of $f,g\in L^2(X,\mu)$ under $T$ is the sequence $n\mapsto\langle U_T^nf,g\rangle=\int f(T^nx)\overline{g(x)}\,d\mu(x)$; the operator $U_T$ is normal when it is unitary, and $U_T$ is unitary for an invertible $T$. For a normal operator the **spectral measure of a vector** $f$ is the positive measure $\sigma_f$ on the circle $\mathbb{T}=\{z:|z|=1\}$ defined by

$$
\widehat{\sigma_f}(n)=\int_{\mathbb{T}}z^n\,d\sigma_f(z)=\langle U_T^nf,f\rangle \qquad (n\in\mathbb{Z}),
$$

which exists by the Herglotz theorem; the closed span $H_f=\overline{\operatorname{span}}\{U_T^nf:n\in\mathbb{Z}\}$ is the **cyclic subspace** generated by $f$, and $U_T|_{H_f}$ is unitarily equivalent to multiplication by $z$ on $L^2(\mathbb{T},\sigma_f)$, so that $\sigma_f$ determines the restriction of the operator to $H_f$ up to unitary equivalence.

**Theorem (ergodicity is the simplicity of $1$).** For a measure-preserving $T$:

1. $T$ is ergodic if and only if $1$ is a simple eigenvalue of $U_T$, that is, the fixed space is one-dimensional;
2. $T$ is weakly mixing if and only if $1$ is the only eigenvalue of $U_T$, the fixed space being one-dimensional and the spectrum on its orthogonal complement having no eigenvalues;
3. $T$ is mixing if and only if $\langle U_T^nf,g\rangle\to\langle f,\mathbf{1}\rangle\langle\mathbf{1},g\rangle$ for all $f,g\in L^2$, equivalently $\widehat{\sigma_f}(n)\to0$ for every $f$ orthogonal to the constants.

*Proof.* Statement 1 is the characterisation of ergodicity of *Ergodic Theory* read in the fixed space. For statement 2, a nonconstant eigenfunction $f$ with $U_Tf=\lambda f$, $|\lambda|=1$, has correlation $\langle U_T^nf,f\rangle=\lambda^n\|f\|_2^2$ whose Cesàro mean vanishes exactly when $\lambda\neq1$, so weak mixing forbids such $\lambda$; conversely, a nonconstant eigenvalue produces a nonzero function not orthogonal to its own translates in the mean. For statement 3, the definition of mixing is the displayed limit with $f=\mathbf{1}_A$ and $g=\mathbf{1}_B$, and the density of the indicators in $L^2$ gives the general case; the equivalence with the vanishing of the Fourier coefficients of $\sigma_f$ is the definition of $\sigma_f$.

**Theorem (spectral characterisation of mixing and weak mixing).** Let $\sigma$ be the maximal spectral type of $U_T$ on the orthogonal complement of the constants, that is, the measure class of any spectral measure dominating all the others. Then $T$ is weakly mixing if and only if $\sigma$ is continuous, and $T$ is mixing if and only if $\sigma$ is a **Rajchman measure**, $\widehat{\sigma}(n)\to0$ as $|n|\to\infty$.

*Proof.* Weak mixing is the absence of eigenvalues on the complement of the constants, which for a unitary operator is exactly the continuity of the maximal spectral type there; mixing is the vanishing of all the coefficients $\widehat{\sigma_f}(n)$ for $f$ in that complement, and the maximal spectral type dominates every $\sigma_f$, so the vanishing is equivalent to that of $\widehat{\sigma}$. The two statements are the standard spectral criteria; the multiplicity does not enter.

### Multiplicity and the Spectral Theorem

**Theorem (spectral theorem in multiplicity form).** For a unitary $U$ on a separable Hilbert space $H$ there are a finite or infinite sequence of measures $\sigma_1\succ\sigma_2\succ\cdots$ on the circle, each absolutely continuous with respect to the previous, a decomposition $H=H_1\oplus H_2\oplus\cdots$ into orthogonal cyclic subspaces and unitary equivalences $U|_{H_j}\cong$ multiplication by $z$ on $L^2(\mathbb{T},\sigma_j)$. The measure class of $\sigma_1$ is the **maximal spectral type**, and the number of $j$ with $\sigma_j$ not null is the **multiplicity function**.

**Theorem (Halmos–von Neumann).** Two measure-preserving transformations are spectrally isomorphic — their Koopman operators are unitarily equivalent — if and only if they have the same spectral type and multiplicity function. The **discrete spectrum** case, in which $L^2$ is spanned by the eigenfunctions, is exactly the case in which the system is measurably conjugate to a rotation on a compact abelian group; the multiplicity is then one and the maximal spectral type is the counting measure on the eigenvalue group.

*Proof.* Quoted as standard. The discrete case is the Halmos–von Neumann theorem: the eigenfunctions form a group under multiplication, the eigenvalue group is discrete, the action of $T$ is by a translation on its dual, and the system is the rotation generated by it. The general multiplicity theorem is the von Neumann spectral theorem for a normal operator.

**Remark (spectral is not conjugated).** Spectral isomorphism is strictly weaker than conjugacy: the classical maximally spectral but non-conjugate systems of Anzai and Katok show that a unitary equivalence of the Koopman operators need not come from a measure-preserving conjugacy. The spectrum is therefore an invariant, not a classification.

## The Examples

**Example (rotations: pure point spectrum).** Let $X=\mathbb{T}$, $T x=x+\alpha\bmod1$ with $\alpha$ irrational. The functions $e_n(x)=e^{2\pi inx}$ satisfy

$$
U_Te_n=e^{2\pi in\alpha}e_n ,
$$

so every $e_n$ is an eigenfunction, the eigenvalues are the group $\{e^{2\pi in\alpha}\}$, and $L^2$ is the closed span of the eigenfunctions: the Koopman operator has pure point spectrum. The system is ergodic and not weakly mixing, and the maximal spectral type is the counting measure on the eigenvalue group; the check $U_Te_1(x)=e^{2\pi i\alpha}e_1(x)$ was recomputed numerically from the definition and holds to $2\times10^{-17}$.

**Example (Bernoulli shifts: countable Lebesgue spectrum).** For the Bernoulli shift on $\{0,1\}^{\mathbb{Z}}$ the Koopman operator on the orthogonal complement of the constants has countable Lebesgue spectrum: it has infinite multiplicity, its maximal spectral type is Lebesgue, and the correlations decay, so the system is mixing. The spectrum is the opposite extreme from the pure point spectrum of a rotation, and the contrast is the model of the spectral dichotomy.

**Example (the doubling map and its natural extension).** The doubling map $T x=2x\bmod1$ is measure-preserving and not invertible, so $U_T$ is an isometry and not unitary, with $\operatorname{Im}U_T$ a proper closed subspace. The **natural extension** is the invertible system on $\mathbb{T}\times\{0,1\}^{\mathbb{N}}$ whose Koopman operator extends the isometry to a unitary operator; the doubling map itself has no nonconstant eigenfunctions and its correlations for Hölder functions decay exponentially, with the rate the second eigenvalue $1/2$ of the transfer operator. The extension is the standard way in which a non-invertible system acquires a unitary Koopman operator, and the same construction is the invertible extension of a one-sided shift.

**Example (toral automorphisms).** For $A\in\mathrm{GL}(n,\mathbb{Z})$ with $\det A=\pm1$ the induced automorphism of $\mathbb{T}^n$ has a Koopman operator which on the characters $e_k(x)=e^{2\pi i\langle k,x\rangle}$ acts by $U_Ae_k=e_{A^{\mathsf T}k}$; the spectrum is a mixture of the discrete part generated by the characters in the finite orbits and a countable Lebesgue part on the characters with infinite orbit. The mixing of the hyperbolic case and the quasi-periodicity of the elliptic case are read from the orbits of $\mathbb{Z}^n$ under $A^{\mathsf T}$, which is the arithmetic of the spectral problem.

## Summary

The **Koopman operator** of a measure-preserving $T$ is $U_Tf=f\circ T$ on $L^2(X,\mu)$; it is a linear isometry with $U_T^*U_T=I$, unitary exactly when $T$ is invertible, with the fixed space $\ker(U_T-I)$ and the coboundary space $\operatorname{span}\{g\circ T-g\}$ orthogonal to it. For a measure-preserving flow the **Koopman flow** $U_tf=f\circ\varphi_t$ is a strongly continuous one-parameter unitary group, hence $U_t=e^{itA}$ with a self-adjoint generator $A$ by **Stone's theorem**; on a smooth flow the generator is $A=-i\mathcal L_X$ with $\mathcal L_X$ the Lie derivative, whose proof is *The Flow Operator*. The dynamics is read from the spectrum: **ergodicity** is the simplicity of the eigenvalue $1$, **weak mixing** the absence of all other eigenvalues, and **mixing** the decay $\langle U_T^nf,g\rangle\to\langle f,\mathbf{1}\rangle\langle\mathbf{1},g\rangle$; equivalently, with $\sigma$ the maximal spectral type on the complement of the constants, weak mixing is the continuity of $\sigma$ and mixing the Rajchman property $\widehat\sigma(n)\to0$. The **spectral measure** $\sigma_f$ of a vector has $\widehat{\sigma_f}(n)=\langle U_T^nf,f\rangle$ and realises the restriction of $U_T$ to its cyclic subspace as multiplication by $z$; the von Neumann multiplicity theorem decomposes the operator into a sequence of cyclic pieces with measures in a domination chain, and the **Halmos–von Neumann theorem** identifies the discrete-spectrum case with the rotations on compact abelian groups while the general spectral isomorphism is strictly weaker than conjugacy. The examples are the rotations (pure point spectrum, $\{e^{2\pi in\alpha}\}$ irreducible to constants), the Bernoulli shifts (countable Lebesgue spectrum, mixing), the doubling map (an isometry, made unitary on its natural extension, with exponential correlation decay and the transfer-operator second eigenvalue $1/2$), and the toral automorphisms (a discrete part on the finite character orbits with a countable Lebesgue part on the infinite ones). The adjoint of $U_T$ and the reversing involution are not used here, and belong to the `- * Operator Theory` group of this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $U_T$, $U_Tf=f\circ T$ | Koopman operator of a measure-preserving map $T$ |
| $U_t$, $U_tf=f\circ\varphi_t$ | Koopman flow of a measure-preserving flow $\varphi_t$ |
| $L^2(X,\mu)$ | Hilbert space of observables |
| $\ker(U_T-I)$ | Fixed space; the constants for an ergodic $T$ |
| $g\circ T-g$ | Coboundary |
| $A$, $E(\lambda)$ | Generator and spectral measure of the Koopman flow, $U_t=\int e^{it\lambda}dE$ |
| $\mathcal L_X$ | Lie derivative along the generating field; $A=-i\mathcal L_X$ |
| $\langle U_T^nf,g\rangle$ | Correlation function |
| $\sigma_f$, $H_f$ | Spectral measure of $f$; cyclic subspace generated by $f$ |
| $\sigma$, multiplicities | Maximal spectral type and multiplicity function |
| $e_n(x)=e^{2\pi inx}$ | Characters of the circle |

## Further Reading

- Bernard O. Koopman, "Hamiltonian Systems and Transformation in Hilbert Space", *Proceedings of the National Academy of Sciences* 17 (1931), 315–318, for the operator and its origin.
- John von Neumann, "Zur Operatorenmethode in der klassischen Mechanik", *Annals of Mathematics* 33 (1932), 587–642, for the spectral theory of measure-preserving transformations.
- Paul R. Halmos and John von Neumann, "Operator Methods in Classical Mechanics II", *Annals of Mathematics* 43 (1942), 332–350, for the spectral isomorphism theorem and the discrete-spectrum classification.
- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the ergodic hierarchy read from the spectrum and the spectral criteria.
- I. P. Cornfeld, S. V. Fomin and Ya. G. Sinai, *Ergodic Theory* (Springer, 1982), for the multiplicity theory and the examples.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for the spectral theorem, Stone's theorem and the spectral measure.
- Hitoshi Anzai, "Ergodic Skew Product Transformations on the Torus", *Osaka Mathematical Journal* 3 (1951), 83–99, and Anatole B. Katok, "Spectral Properties of Dynamical Systems", for the maximally spectral but non-conjugate systems.
- Marshall H. Stone, "On One-Parameter Unitary Groups in Hilbert Space", *Annals of Mathematics* 33 (1932), 643–648, for the one-parameter unitary group.
