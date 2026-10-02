# __The Spectral Operator__

## Introduction

The spectral theorem for a bounded self-adjoint operator says that the operator is a multiplication by the independent variable, read in a measure space attached to its spectrum. The multiplication operator that appears is the **spectral operator**: on $L^2(\Sigma,\mu)$ it sends $f$ to $\lambda f$, its spectrum is the support of $\mu$ inside the compact set $\Sigma$, its spectral measure is the multiplication by indicators, and its functional calculus is the multiplication by bounded Borel functions. The theorem is therefore best stated as an equivalence: a bounded self-adjoint operator is unitarily equivalent to a spectral operator, and the measure class and the multiplicity are its complete invariants.

This article makes the multiplication model explicit and reads the spectral theorem through it. The spectral theorem in its spectral-measure form is *Self-Adjoint Operators and the Spectral Theorem* below, and the compact case is *Banach and Hilbert Spaces*; what is done here is the passage from an abstract operator to the concrete operator of multiplication by the variable, together with the multiplicity theory that classifies it. The unbounded case, where the multiplication operator acts on a domain of functions for which $\lambda f$ is square-integrable, is *Unbounded Operators and Spectral Measures*; the unitary case carried by the circle is *Unitary Operators and the Spectral Measure*; the spectral operator of an unbounded symmetric form is *The Friedrichs Extension of a Hermitian Form*. The measure and integration theory is *Measure Theory and Integration*, and the $L^2$ theory is *Banach and Hilbert Spaces*.

Throughout, $\mathbb{K}=\mathbb{C}$ when a normal operator is at issue and $\mathbb{K}=\mathbb{R}$ for a self-adjoint one; $H$ is a separable Hilbert space, $T$ a bounded operator on it, $\sigma(T)\subseteq\mathbb{C}$ its spectrum, and $E$ a spectral measure. The spectral operator is written $M_\lambda$ in the self-adjoint case and $M_z$ in the normal case, and for a Borel function $f$ the multiplication is written $M_f$.

## The Multiplication Operator

**Definition.** Let $(\Sigma,\mathcal{B},\mu)$ be a finite measure space with $\Sigma\subseteq\mathbb{C}$ compact contained in the Borel sets $\mathcal{B}$. The **spectral operator** is

$$
M_\lambda:L^2(\Sigma,\mu)\longrightarrow L^2(\Sigma,\mu),\qquad (M_\lambda f)(\lambda)=\lambda f(\lambda).
$$

When $\Sigma\subseteq\mathbb{R}$ it is bounded and self-adjoint with $\|M_\lambda\|=\sup_{\lambda\in\operatorname{supp}\mu}|\lambda|$; when $\Sigma\subseteq\mathbb{T}$ it is unitary; in general it is normal.

**Proposition (the spectral data of the spectral operator).** The spectrum of $M_\lambda$ is the support of $\mu$:

$$
\sigma(M_\lambda)=\operatorname{supp}\mu=\{\lambda:\mu(\lambda-\varepsilon,\lambda+\varepsilon)>0\ \text{for every}\ \varepsilon>0\},
$$

the spectral measure is $E(S)=M_{\mathbf{1}_S}$, the functional calculus is $f(M_\lambda)=M_f$ for bounded Borel $f$, and the eigenvectors of $M_\lambda$ are the nonzero functions supported on the atoms of $\mu$, with the atom at $\lambda$ of multiplicity equal to the mass of the atom.

*Proof.* $M_\lambda-\lambda_0$ is invertible with bounded inverse exactly when $1/(\lambda-\lambda_0)$ is essentially bounded on $\operatorname{supp}\mu$, which is the complement of the support; the spectral measure and the functional calculus are immediate from the multiplication structure, since $\mathbf{1}_S(M_\lambda)=M_{\mathbf{1}_S}$; the eigenfunction statement is the fact that the only functions annihilated by $M_\lambda-\lambda_0$ are supported on the level set $\lambda=\lambda_0$, together with the multiplicities of the measure.

**Proposition (an atom is a jump of the spectral measure).** For a Borel set $S$ the projection $E(S)=M_{\mathbf{1}_S}$ is the multiplication by the indicator; it is nonzero exactly when $\mu(S)>0$, and its range is the subspace of functions supported on $S$, on which $M_\lambda$ acts as an operator with spectrum contained in $\overline{S}$.

*Proof.* Multiplication by an indicator is a projection onto the functions vanishing off $S$; nonvanishing of the range is nonvanishing of the measure of $S$, and the restriction of the multiplication to that invariant subspace is again a spectral operator with measure $\mu|_S$.

## The Spectral Theorem as a Unitary Equivalence

**Theorem (self-adjoint case).** Let $T$ be a bounded self-adjoint operator on a separable Hilbert space $H$. Then there are a finite measure space $(\Sigma,\mathcal{B},\mu)$ with $\Sigma\subseteq\mathbb{R}$ compact and a unitary

$$
U:H\longrightarrow L^2(\Sigma,\mu)
$$

with

$$
U\,T\,U^{-1}=M_\lambda .
$$

Equivalently, $T=\int\lambda\,dE(\lambda)$ where $E$ is the spectral measure of $T$ and the measure class of $\mu$ may be taken as the class of $\langle E(\cdot)x,x\rangle$ for a total family of vectors $x$.

*Proof.* The spectral measure $E$ of *Self-Adjoint Operators and the Spectral Theorem* is a projection-valued measure on $\sigma(T)$; by choosing a countable total family $(x_n)$ of vectors, guaranteed by separability, and forming the finite measure $\mu=\sum_n2^{-n}\langle E(\cdot)x_n,x_n\rangle$, the multiplication model on $\bigoplus_nL^2(\sigma(T),\mu_n)$ is obtained; passing to a single measure space by the standard identifications gives the stated unitary equivalence.

**Theorem (normal case).** A bounded normal operator $T$ on a separable Hilbert space is unitarily equivalent to a multiplication operator,

$$
T\simeq M_z \quad\text{on}\quad \bigoplus_{n}L^2(\sigma(T),\mu_n),
\qquad (M_z f)(z)=z f(z),
$$

and the same statement with $M_\lambda$ holds for a self-adjoint operator; in both cases the unitary equivalence is implemented by the spectral measure through the Borel functional calculus, $x\mapsto(f\mapsto\langle f(T)x,y\rangle)$.

*Proof.* The Borel functional calculus of the spectral theorem produces the commuting algebra of $T$, and the cyclic decomposition of $H$ under this algebra gives the direct sum of multiplication spaces; the multiplicity functions $\mu_n$ are equivalent to the spectral measure classes of the cyclic vectors.

## Cyclic Vectors and Multiplicity

**Definition.** A vector $x\in H$ is **cyclic** for $T$ if the closed span of $\{T^nx:n\ge0\}$ is $H$. The **multiplicity function** of $T$ is the multiplicity of the direct sum decomposition of the theorem, defined $\mu$-almost everywhere.

**Proposition (the cyclic case).** $T$ has a cyclic vector exactly when it is unitarily equivalent to a single spectral operator $M_\lambda$ on $L^2(\sigma(T),\mu)$, with $U x_0=\mathbf{1}$ for the cyclic vector $x_0$; in that case the spectral measure is determined by the pair $(x_0,T)$ through $\mu(S)=\langle E(S)x_0,x_0\rangle$.

*Proof.* The transform $U$ sending $T^nx_0$ to $\lambda^n$ extends by continuity to a unitary onto $L^2(\sigma(T),\mu)$, and it intertwines $T$ with $M_\lambda$; conversely, in the multiplication model the constant function is cyclic.

**Theorem (classification).** Two bounded self-adjoint operators on separable Hilbert spaces are unitarily equivalent if and only if their spectral measures have the same measure classes with the same multiplicities: the pair consisting of the measure class on the spectrum and the multiplicity function is a complete unitary invariant. In particular a self-adjoint operator with a cyclic vector is determined up to unitary equivalence by the measure class of its spectral measure.

*Proof.* A unitary intertwining two multiplication operators carries the measure classes and multiplicities into one another, so the invariants agree; conversely, equal invariants allow the two multiplication models to be identified by a unitary that maps $L^2(\Sigma,\mu)$ to $L^2(\Sigma',\mu')$ through the Radon–Nikodým derivatives, and a measurable multiplicity isomorphism reduces the general case to the cyclic one.

**Example (discrete multiplicity one).** A compact self-adjoint operator with simple spectrum is unitarily equivalent to the spectral operator of the purely atomic measure $\sum_n\delta_{\lambda_n}$ on the set $\{\lambda_n\}\cup\{0\}$, and the unitary sends the eigenvector $e_n$ to the indicator of the point $\lambda_n$. A self-adjoint operator whose spectral measure is absolutely continuous with respect to Lebesgue measure on an interval has no eigenvectors and its model is a multiplication on an interval of the line.

## The Functional Calculus as Multiplication

**Proposition.** In the multiplication model every bounded Borel function $f$ acts as

$$
f(T)=U^{-1}M_fU,\qquad M_f g=f\,g,
$$

so $\|f(T)\|=\|f\|_{L^\infty(\sigma(T),\mu)}$, the map $f\mapsto f(T)$ is a $*$-homomorphism of the bounded Borel functions onto the von Neumann algebra generated by $T$, and it is isometric exactly in the uniform norm.

*Proof.* The functional calculus of the spectral theorem is the multiplication by $f$ in the model, and the stated norm identity is the essential supremum formula; multiplicativity and the adjoint identity $f(T)^*=\bar f(T)$ are those of multiplication.

**Remark.** The spectral operator is therefore the answer to the question the spectral theorem poses: it is the model operator, the one whose domain, spectrum and functional calculus are all visible at once. The price of the model is the measure space, which is not canonical but may be chosen; the invariant content is the measure class and the multiplicity, and the rest is a choice of coordinates on the spectrum.

## Summary

A spectral operator is a multiplication by the independent variable, $M_\lambda f=\lambda f$ on $L^2(\Sigma,\mu)$ for a compact $\Sigma\subseteq\mathbb{C}$ and a finite measure $\mu$; its spectrum is the support of the measure, its spectral measure is the multiplication by indicators, its functional calculus is the multiplication by bounded Borel functions, and its eigenvectors are the functions supported on atoms, with multiplicity the mass of the atom. The spectral theorem for a bounded self-adjoint operator is the statement that it is unitarily equivalent to such an operator with $\Sigma\subseteq\mathbb{R}$, and for a bounded normal operator that it is unitarily equivalent to $M_z$ on a direct sum of spectral operators; the unitary equivalence is the coordinate change that turns the abstract operator into a concrete multiplication. The cyclic case is the case of a single summand, and the multiplicity function together with the measure class of the spectral measure is a complete unitary invariant, so two such operators are unitarily equivalent exactly when their invariants agree. The functional calculus is multiplication in the model, $f(T)=U^{-1}M_fU$, with $\|f(T)\|=\|f\|_{L^\infty}$, and it realises the von Neumann algebra generated by $T$ as the algebra of multiplications.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_\lambda$, $M_z$ | the spectral operator, multiplication by the variable |
| $L^2(\Sigma,\mu)$ | the multiplication model, $\Sigma\subseteq\mathbb{C}$ compact |
| $\sigma(T)=\operatorname{supp}\mu$ | the spectrum is the support of the measure |
| $E(S)=M_{\mathbf{1}_S}$ | the spectral measure of the spectral operator |
| $f(T)=U^{-1}M_fU$ | the functional calculus as multiplication |
| $\|f(T)\|=\|f\|_{L^\infty}$ | the isometric property of the functional calculus |
| $\bigoplus_nL^2(\sigma(T),\mu_n)$ | the normal model with multiplicity |
| cyclic vector | reduces the model to a single summand |
| measure class $+$ multiplicity | complete unitary invariant |

## Further Reading

- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd ed. 1990), for the spectral theorem as multiplication and the multiplicity theory.
- Paul R. Halmos, *Introduction to Hilbert Space* (Chelsea, 2nd ed. 1957), for the spectral operator and the cyclic decomposition.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II* (Interscience, 1963), for the classification of normal operators by multiplicity.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for the multiplication operator and its domain.
- Walter Rudin, *Real and Complex Analysis* (McGraw-Hill, 3rd ed. 1987), for the $L^2$ and Radon–Nikodým background of the model.
