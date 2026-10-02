# __Self-Adjoint Operators and the Spectral Theorem__

## Introduction

A bounded self-adjoint operator is one equal to its own adjoint. The equality is a symmetry that forces the whole spectral theory: the spectrum is real, the operator has a spectral measure, and every bounded Borel function of the operator is defined and is again an operator of the same algebra. The **spectral theorem** is the precise form of this statement, $T=\int\lambda\,dE(\lambda)$, and the **functional calculus** $f\mapsto f(T)$ is its most useful corollary, since it converts a statement about a single operator into a statement about a commutative algebra of operators. This article develops the self-adjoint operator, the spectral measure, the theorem and the calculus, and it presents the two structural consequences that classify the operator: the Cayley transform, which converts self-adjointness into unitarity, and the multiplication model, in which the operator acts as a multiplication by the independent variable.

The bounded operator theory is *Bounded Operators on a Hilbert Space*; the spectral theorem in its measure-theoretic form and the compact case are stated and proved in *Banach and Hilbert Spaces*, and the multiplication model of the theorem is developed in *The Spectral Operator*. The algebraic and order-theoretic study of the self-adjoint family is *Self-Adjoint Operators*; the unitary case with its own measure on the circle is *Unitary Operators and the Spectral Measure*; the positivity and the square root are *Positive Operators and the Square Root*; the unbounded case is *Unbounded Operators and Spectral Measures*. The measure and integration used are *Measure Theory and Integration*, and the $L^2$ theory is *Banach and Hilbert Spaces*.

Throughout, $H$ is a complex (or real) Hilbert space with inner product $\langle\cdot,\cdot\rangle$ linear in the first argument, $T\in B(H)$ is bounded, $T^*$ is its adjoint, $\sigma(T)$ is its spectrum and $E$ is a spectral measure on the Borel subsets of $\sigma(T)$.

## Self-Adjoint Operators

**Definition.** $T$ is **self-adjoint** if $T^*=T$; it is **positive** if $T=T^*$ and $\langle Tx,x\rangle\ge0$ for all $x$; the self-adjoint operators form a real vector space and are ordered by $S\le T$ iff $T-S$ is positive.

**Theorem (reality of the spectrum and the norm formula).** For a self-adjoint $T$ the spectrum is real, $\sigma(T)\subseteq\mathbb{R}$, and

$$
\|T\|=\sup_{\|x\|=1}|\langle Tx,x\rangle|=\max_{\lambda\in\sigma(T)}|\lambda| .
$$

*Proof.* The numerical range of a self-adjoint operator lies in $\mathbb{R}$ and its closure contains the spectrum, so the spectrum is real. For the norm formula, the bound $\|T\|\ge\sup|\langle Tx,x\rangle|$ is Cauchy–Schwarz; the reverse inequality follows by polarising $|\langle T(x+y),x+y\rangle|$ and using that the diagonal is real, which gives $\|Tx\|\le\sup_{\|x\|=1}|\langle Tx,x\rangle|\|x\|$; the identification with $\max|\lambda|$ is the spectral theorem below.

**Proposition (real and imaginary parts; the Cayley transform).** Every bounded operator is $T=A+iB$ with $A,B$ self-adjoint and this decomposition is unique; the **Cayley transform**

$$
C(T)=(T-iI)(T+iI)^{-1}
$$

is a unitary of $H$ whose spectrum does not contain $1$, and the assignment $T\mapsto C(T)$ is a bijection from the bounded self-adjoint operators onto the unitaries $U$ with $1\notin\sigma(U)$, with inverse $U\mapsto i(I+U)(I-U)^{-1}$.

*Proof.* Since $T\pm iI$ is invertible for self-adjoint $T$ by the reality of the spectrum, the transform is defined; $C(T)^*C(T)=(T+iI)^{-1}(T-iI)(T+iI)(T-iI)^{-1}=I$ by the commutativity of the resolvent factors, so $C(T)$ is unitary, and the inverse formula inverts the Möbius transformation; the bijection is the two-sided verification of the compositions.

**Proposition (the order).** The positive operators are exactly the self-adjoint operators with $\sigma(T)\subseteq[0,\infty)$; the order is compatible with addition and with the unit and is an order on the self-adjoint family: every bounded set has a least upper bound, $0\le T\le I$ exactly when $T$ is a contraction that is positive, and $T^*T\ge0$ with $\|T^*T\|=\|T\|^2$ for every $T$.

*Proof.* The spectral criterion for positivity is the spectral theorem; the lattice statement is the spectral theorem applied to the spectral families of two commuting self-adjoint operators; the remaining identities are the $C^*$-identity and the reality of the diagonal.

## The Spectral Measure and the Spectral Theorem

**Definition.** A **spectral measure** on $H$ is a map $E$ from the Borel subsets of a compact set $\Sigma\subseteq\mathbb{C}$ to projections with

$$
E(\varnothing)=0,\quad E(\Sigma)=I,\quad E(S\cap S')=E(S)E(S'),\quad E\Bigl(\bigcup_nS_n\Bigr)=\sum_nE(S_n)
$$

for the disjoint countable unions, the sum converging in the strong operator topology.

**Theorem (the spectral theorem, self-adjoint case).** Let $T$ be a bounded self-adjoint operator. Then there is a spectral measure $E$ on the Borel subsets of the compact set $\sigma(T)\subseteq\mathbb{R}$ with

$$
T=\int_{\sigma(T)}\lambda\,dE(\lambda),
$$

and for every bounded Borel function $f$ on $\sigma(T)$ the operator

$$
f(T)=\int_{\sigma(T)}f(\lambda)\,dE(\lambda)
$$

is bounded with $\|f(T)\|=\sup_{\lambda\in\sigma(T)}|f(\lambda)|$; the map $f\mapsto f(T)$ is a $\mathbb{K}$-algebra homomorphism sending $1$ to $I$, the identity function to $T$, and $\bar f$ to $f(T)^*$.

*Proof.* The spectral measure is constructed from the continuous functional calculus: polynomials in $T$ are computed on the spectrum, the Stone–Weierstrass theorem extends the calculus to the continuous functions, and the Riesz representation theorem converts the positive linear functionals $f\mapsto\langle f(T)x,x\rangle$ into measures; the strong-operator additivity and the multiplicativity are then the countable additivity and the multiplicativity of the integral. The norm identity is the isometry of the $*$-homomorphism of the bounded Borel functions.

**Theorem (the spectral theorem, normal case).** A bounded operator $T$ on a complex Hilbert space is normal, $T^*T=TT^*$, if and only if there is a spectral measure $E$ on the Borel subsets of $\sigma(T)\subseteq\mathbb{C}$ with $T=\int\lambda\,dE(\lambda)$; equivalently, $T$ is unitarily equivalent to a multiplication by the independent variable on a direct sum of spaces $L^2(\sigma(T),\mu_j)$.

*Proof.* The self-adjoint case applied to the commuting operators $\operatorname{Re}T$ and $\operatorname{Im}T$ produces their joint spectral measure, which is a measure in the plane supported on the joint spectrum; normality is the commutativity needed for the two real parts to be simultaneously diagonalised, and the multiplication model is the spectral theorem of *The Spectral Operator*.

## The Functional Calculus

**Proposition (the calculus).** The map $f\mapsto f(T)$ from the bounded Borel functions on $\sigma(T)$ is a $*$-homomorphism onto the von Neumann algebra generated by $T$, it is isometric for the uniform norm, it is weak-operator continuous on bounded sets, and its kernel is the ideal of functions vanishing on the support of $E$.

*Proof.* Each statement is the corresponding statement for the integral against a spectral measure: multiplicativity is the multiplicativity of the integral, the $*$-property is the reality of $E$, the isometry is the norm formula, and the kernel is the vanishing of the measure on the support.

**Corollary (the calculus acts by spectral projection).** For a Borel set $S$ the operator $E(S)$ is the characteristic function of $T$, $E(S)=\mathbf{1}_S(T)$; conversely the spectral measure is recovered from the calculus, and the projections in the von Neumann algebra generated by $T$ are exactly the $E(S)$.

*Proof.* The characteristic function of $S$ integrated against $E$ is $E(S)$ by the definition of the integral, and the converse is the inversion formula for the measure.

**Corollary (the spectral mapping theorem).** For a continuous function $f$ one has $\sigma(f(T))=f(\sigma(T))$, and the eigenvalues of $T$ are the atoms of $E$, with the eigenspace at $\lambda$ the range of the projection $E(\{\lambda\})$.

*Proof.* $f(T)-\mu I=(f-\mu)(T)$ is invertible exactly when $f-\mu$ does not vanish on the spectrum; the eigenvalue statement is the atomic part of the spectral measure.

## The Multiplication Model and Multiplicity

**Theorem (the model).** A bounded self-adjoint operator $T$ on a separable Hilbert space is unitarily equivalent to the multiplication by the independent variable on $L^2(\sigma(T),\mu)$ when it has a cyclic vector; in general it is unitarily equivalent to $M_\lambda$ on a direct sum $\bigoplus_nL^2(\sigma(T),\mu_n)$, and the measure class together with the multiplicity function is a complete unitary invariant.

*Proof.* This is the spectral operator of *The Spectral Operator*; the cyclic vector produces the transform that sends $T^nx_0$ to $\lambda^n$, and the general case decomposes the space into cyclic subspaces.

**Proposition (support and point spectrum).** The spectral measure of $T$ is supported on $\sigma(T)$, and its atoms are exactly the eigenvalues: $E(\{\lambda\})\neq0$ iff $\lambda$ is an eigenvalue, in which case the range of $E(\{\lambda\})$ is the eigenspace. The continuous part of $E$ corresponds to the continuous spectrum, and $T$ has no eigenvectors exactly when $E$ is non-atomic.

*Proof.* The complement of the support is the set on which $E$ vanishes, and there $T-\lambda I$ is invertible; an atom at $\lambda$ gives a nonzero projection whose range consists of eigenvectors, and conversely an eigenvector lies in the range of the corresponding atom.

**Example (compact and finite-rank).** For a compact self-adjoint operator the spectral measure is purely atomic, supported on $\{0\}\cup\{\lambda_n\}$ with $\lambda_n\to0$, and the spectral theorem is the orthonormal eigenbasis expansion of *Compact Operators*. For a finite-rank self-adjoint operator the measure is a finite atomic measure and the theorem is the orthogonal diagonalisation of a Hermitian matrix.

**Example (multiplication operators).** For $H=L^2(X,\mu)$ and a real $g\in L^\infty(X,\mu)$ the operator $M_g f=gf$ is self-adjoint, its spectral measure is $E(S)=M_{\mathbf{1}_{g^{-1}(S)}}$, and the spectral theorem is the identity $M_g=\int\lambda\,dE(\lambda)$; the model theorem in the other direction is exactly this computation.

## Summary

A bounded self-adjoint operator has real spectrum, satisfies $\|T\|=\sup_{\|x\|=1}|\langle Tx,x\rangle|=\max|\sigma(T)|$, is positive exactly when its spectrum lies in $[0,\infty)$, and is related to the unitaries by the Cayley transform $C(T)=(T-iI)(T+iI)^{-1}$. The spectral theorem represents it as $T=\int\lambda\,dE(\lambda)$ against a spectral measure on its real spectrum, and the functional calculus $f(T)=\int f\,dE$ is an isometric $*$-homomorphism from the bounded Borel functions onto the von Neumann algebra generated by $T$, sending $\mathbf{1}_S$ to $E(S)$, satisfying the spectral mapping theorem, and having as its kernel the functions vanishing on the support of $E$. A bounded operator on a complex Hilbert space is normal exactly when it has such a representation with a measure in the plane, equivalently when it is a multiplication by the independent variable on a direct sum of $L^2$ spaces; the measure class and the multiplicity form a complete unitary invariant, and the atoms of the measure are precisely the eigenvalues. The compact and finite-rank cases are the purely atomic specialisations, and the order structure and the algebraic properties of the self-adjoint family are *Self-Adjoint Operators*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T=T^*$ | self-adjointness, spectrum real |
| $\|T\|=\sup_{\|x\|=1}|\langle Tx,x\rangle|$ | the norm formula |
| $C(T)=(T-iI)(T+iI)^{-1}$ | the Cayley transform, a unitary avoiding $1$ |
| $E(S)$ | spectral measure, projection-valued |
| $T=\int\lambda\,dE(\lambda)$ | the spectral theorem |
| $f(T)=\int f\,dE$ | the functional calculus |
| $\|f(T)\|=\sup|f|$ | isometry of the calculus |
| $\sigma(f(T))=f(\sigma(T))$ | spectral mapping |
| $E(\{\lambda\})$ | eigenspace projection at an eigenvalue |
| $\bigoplus_nL^2(\sigma(T),\mu_n)$ | multiplication model with multiplicity |

## Further Reading

- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd ed. 1990), for the spectral theorem and the functional calculus.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II* (Interscience, 1963), for the spectral measure, the Cayley transform and the multiplicity theory.
- Walter Rudin, *Functional Analysis* (McGraw-Hill, 2nd ed. 1991), for the spectral theorem in its operator form and the Riesz representation theorem.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for the spectral theorem as multiplication and the spectral mapping theorem.
- Paul R. Halmos, *Introduction to Hilbert Space* (Chelsea, 2nd ed. 1957), for the self-adjoint operator and its spectral measure.
