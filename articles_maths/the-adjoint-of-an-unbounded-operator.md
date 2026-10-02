# __The Adjoint of an Unbounded Operator__

## Introduction

An unbounded operator on a Hilbert space is a linear map defined on a dense subspace, and the first question about it is not its action but its **domain**. The adjoint is where the domain enters: for a densely defined operator $T$ the adjoint $T^*$ is defined on the vectors $y$ for which the map $x\mapsto\langle Tx,y\rangle$ is bounded on the domain of $T$, and on those vectors it is given by the Riesz representation theorem. The adjoint is always closed, the adjoint of the adjoint is the closure of the operator when the closure exists, and the relation between the two is exactly the orthogonal complement relation between their graphs. Out of this relation come the three notions that organise the theory: **symmetry**, $T\subseteq T^*$; **self-adjointness**, $T=T^*$ with equality of domains; and **essential self-adjointness**, the statement that the closure is self-adjoint. The difference between the first and the second is measured by the deficiency indices, and it is the reason a differential operator needs boundary conditions before it is a self-adjoint operator.

This article fixes the densely defined operator, the adjoint and its closedness, the graph relation $\Gamma(T^*)=\Gamma(-T)^{\perp}$, the notions of symmetry, self-adjointness and essential self-adjointness, the Cayley transform, and the deficiency indices. The general theory of closed and closable operators, the spectral theorem for unbounded operators and Stone's theorem are *Unbounded Operators and Spectral Measures*, where the spectral theory and the polar decomposition are developed; the bounded adjoint is *Bounded Operators on a Hilbert Space*; the self-adjoint spectral theorem is *Self-Adjoint Operators and the Spectral Theorem*; the positive case and the square root are *Positive Operators and the Square Root* and *The Friedrichs Extension of a Hermitian Form*.

Throughout, $H$ is a complex Hilbert space with inner product linear in the first argument, and a **linear operator** on $H$ is a linear map $T:D(T)\to H$ with domain a linear subspace $D(T)\subseteq H$; the operator is **densely defined** if $D(T)$ is dense. The **graph** is $\Gamma(T)=\{(x,Tx):x\in D(T)\}\subseteq H\oplus H$, the **adjoint** is $T^*$, and $T$ is **closed** if $\Gamma(T)$ is closed.

## Unbounded Operators and Their Domains

**Definition.** A linear operator $T$ is **closed** if its graph is closed in $H\oplus H$, equivalently if $x_n\in D(T)$, $x_n\to x$ and $Tx_n\to y$ imply $x\in D(T)$ and $Tx=y$; it is **closable** if the closure of $\Gamma(T)$ is the graph of an operator, written $\overline T$ and called the **closure**.

**Proposition (the closed graph theorem).** A closed densely defined operator whose domain is all of $H$ is bounded. Consequently an unbounded operator is never everywhere defined, and the domain is part of the data of the operator, not a technicality.

*Proof.* This is the closed graph theorem of *Normed and Banach Spaces*, applied to the Banach space $H$; the corollary is the contrapositive.

**Definition.** $T$ is **symmetric** if $\langle Tx,y\rangle=\langle x,Ty\rangle$ for all $x,y\in D(T)$; it is **self-adjoint** if $T=T^*$, that is $D(T)=D(T^*)$ and the operators agree; it is **essentially self-adjoint** if its closure is self-adjoint.

**Proposition (symmetry is domain inclusion).** $T$ is symmetric if and only if $T\subseteq T^*$, that is $D(T)\subseteq D(T^*)$ and $T^*|_{D(T)}=T$. A self-adjoint operator is symmetric and closed, and a symmetric operator is closable with $\overline T\subseteq T^*$.

*Proof.* The symmetric condition says precisely that for $y\in D(T)$ the functional $x\mapsto\langle Tx,y\rangle$ is bounded on $D(T)$, with representing vector $Ty$; this is the definition of $y\in D(T^*)$ and $T^*y=Ty$. Self-adjointness is symmetry together with the reverse inclusion, and the adjoint is closed, so a self-adjoint operator is closed and a symmetric operator has closure contained in the adjoint.

## The Adjoint

**Definition.** For a densely defined $T$ the **adjoint** $T^*$ has domain

$$
D(T^*)=\{y\in H:x\mapsto\langle Tx,y\rangle\ \text{is bounded on}\ D(T)\},
$$

and for such a $y$ the vector $T^*y$ is the unique $z$ with $\langle Tx,y\rangle=\langle x,z\rangle$ for all $x\in D(T)$, which exists by the Riesz representation theorem and the density of $D(T)$.

**Proposition (the adjoint is closed and involutive on the closure).** The adjoint $T^*$ is closed, and

$$
T\subseteq T^{**},\qquad \overline T=T^{**} ,
$$

the second identity holding exactly when $T$ is closable; in that case $T^{**}$ is the smallest closed extension of $T$, and $(T^*)^*=T$ for a closed $T$.

*Proof.* The graph of $T^*$ is the set of $(y,z)$ with $\langle Tx,y\rangle=\langle x,z\rangle$ for all $x\in D(T)$, which is the orthogonal complement of $\{(Tx,-x)\}$; an orthogonal complement is closed, so $T^*$ is closed. Iterating the definition gives $T\subseteq T^{**}$, and $T^{**}$ is the closed operator whose graph is the closure of $\Gamma(T)$, so it is the closure of $T$ when that closure is an operator; for a closed $T$ one has $\overline T=T$ and the identity gives $(T^*)^*=T$.

## The Graph and the Adjoint

**Theorem (graph relation).** For a densely defined $T$,

$$
\Gamma(T^*)=\Gamma(-T)^{\perp}\subseteq H\oplus H ,
$$

where the orthogonal complement is taken in the inner product $\langle(x,y),(x',y')\rangle=\langle x,x'\rangle+\langle y,y'\rangle$.

*Proof.* A pair $(y,z)$ lies in $\Gamma(T^*)$ exactly when $\langle Tx,y\rangle=\langle x,z\rangle$ for all $x\in D(T)$, which is $\langle Tx,y\rangle-\langle x,z\rangle=0$, that is $\langle(Tx,-x),(y,z)\rangle=0$; the set of vectors $(Tx,-x)$ is precisely $\Gamma(-T)$, so the condition is $(y,z)\perp\Gamma(-T)$.

**Corollary (the graph of a closed or self-adjoint operator).** With the unitary $U(x,y)=(y,-x)$ the graph relation reads $\Gamma(T^*)=U\Gamma(T)^{\perp}$, and:

(i) $T$ is closed if and only if $\Gamma(T)=U\Gamma(T^*)^{\perp}$;

(ii) $T$ is self-adjoint if and only if

$$
H\oplus H=\Gamma(T)\oplus U\Gamma(T).
$$

*Proof.* Since $U\Gamma(T)=\Gamma(-T)$ and $U$ is unitary, the theorem is $\Gamma(T^*)=U\Gamma(T)^{\perp}$; taking orthogonal complements and applying $U$ gives $U\Gamma(T^*)^{\perp}=\overline{\Gamma(T)}$, which is (i). For (ii), $\Gamma(T)$ and $U\Gamma(T)$ are orthogonal exactly when $\langle Tx,y\rangle=\langle x,Ty\rangle$ for all $x,y\in D(T)$, that is when $T$ is symmetric; the sum is all of $H\oplus H$ exactly when the orthogonal complement of $U\Gamma(T)$ is $\Gamma(T)$, which by the graph relation is the statement $\Gamma(T^*)=\Gamma(T)$, that is self-adjointness.

**Proposition (the spectrum of the adjoint).** For a closed densely defined $T$ the resolvent of $T$ and of $T^*$ are related by

$$
(T^*-zI)^{-1}=\bigl((T-\bar zI)^{-1}\bigr)^* ,
$$

so $\sigma(T^*)=\overline{\sigma(T)}$, and the adjoint of a self-adjoint operator is itself.

*Proof.* Taking adjoints in $(\lambda I-T)^{-1}=R$ gives $(\lambda I-T)^*=(\bar\lambda I-T^*)$ and $R^*=(\bar\lambda I-T^*)^{-1}$; the spectrum identity is the conjugating of the resolvent set, and the self-adjoint case is $T=T^*$.

## Symmetric, Self-Adjoint and Essentially Self-Adjoint Operators

**Theorem (the Cayley transform of a symmetric operator).** A densely defined symmetric operator $T$ has $T+iI$ and $T-iI$ injective with closed range, and the **Cayley transform**

$$
C(T)=(T-iI)(T+iI)^{-1}
$$

is an isometry from $\operatorname{ran}(T+iI)$ onto $\operatorname{ran}(T-iI)$ with $\|C(T)v\|=\|v\|$; $T$ is self-adjoint exactly when $C(T)$ is unitary.

*Proof.* The symmetry gives $\|(T\pm iI)x\|^2=\|Tx\|^2+\|x\|^2$, so both maps are injective with closed range and $(T+iI)^{-1}$ is an isometry onto its range; the transform is the product of that inverse with $T-iI$, hence an isometry, and the deficiencies are the orthogonal complements of the two ranges; the isometry is unitary exactly when both deficiencies vanish, which is self-adjointness.

**Definition.** The **deficiency indices** of a densely defined symmetric operator are

$$
n_-=\dim\ker(T^*+iI)=\dim\operatorname{ran}(T+iI)^{\perp},
\qquad
n_+=\dim\ker(T^*-iI)=\dim\operatorname{ran}(T-iI)^{\perp} .
$$

**Theorem (von Neumann's criterion).** A densely defined symmetric operator $T$ is essentially self-adjoint exactly when $n_+=n_-=0$; it has self-adjoint extensions exactly when $n_+=n_-$, and the self-adjoint extensions are in bijection with the unitary maps from $\ker(T^*-iI)$ onto $\ker(T^*+iI)$.

*Proof.* The deficiency subspaces are the two directions in which the Cayley isometry fails to be unitary; the extension of the isometry to a unitary of the whole space is the choice of a partial isometry between the two deficiencies, and the extension exists exactly when the two have the same dimension; the bijection with the unitary maps is the standard parametrisation, and no extension exists when the indices differ.

**Example (the differentiation operator).** On $L^2(\mathbb{R})$ the operator $T=-i\,d/dx$ with domain the compactly supported smooth functions $C_c^\infty(\mathbb{R})$ is densely defined and symmetric; its adjoint has domain $H^1(\mathbb{R})$, the deficiency indices are $0$, and $T$ is essentially self-adjoint with closure the self-adjoint operator $-i\,d/dx$ on $H^1(\mathbb{R})$. On $L^2(0,1)$ the same formula with $C_c^\infty(0,1)$ has deficiency indices $(1,1)$, and the self-adjoint extensions are the boundary conditions $\psi(1)=e^{i\theta}\psi(0)$.

**Example (the multiplication operator).** For the operator $Qf(x)=xf(x)$ with domain $\{f:\int x^2|f|^2<\infty\}$ the operator is self-adjoint: its graph is closed, its domain is the maximal domain of multiplication by $x$, and $Q^*=Q$. This is the model from which the unbounded spectral theorem is read, and the adjoint of a bounded operator is the bounded special case in which $D(T)=D(T^*)=H$.

## Summary

An unbounded operator on a Hilbert space is a linear map on a dense subspace, and its domain is part of its data; a closed operator with domain all of $H$ is bounded, so an unbounded operator is never everywhere defined. The adjoint $T^*$ is defined on the vectors $y$ for which $x\mapsto\langle Tx,y\rangle$ is bounded, is always closed, satisfies $T\subseteq T^{**}$ and $\overline T=T^{**}$ for a closable $T$, and is characterised by the graph relation $\Gamma(T^*)=\Gamma(-T)^{\perp}$, so the graphs of a closed operator and its adjoint form an orthogonal decomposition of $H\oplus H$ under the rotation $U(x,y)=(y,-x)$. An operator is symmetric exactly when $T\subseteq T^*$, self-adjoint exactly when $T=T^*$ with equality of domains, and essentially self-adjoint when its closure is self-adjoint; the Cayley transform converts the symmetric operator into an isometry whose unitary defect is measured by the deficiency indices $n_\pm=\dim\ker(T^*\mp iI)$, and von Neumann's criterion states that no defect is essential self-adjointness and that equal indices characterise the existence of self-adjoint extensions. The differentiation operator $-i\,d/dx$ on the line and the multiplication operator are the standard examples of essential self-adjointness and of self-adjointness, and the interval case shows how boundary conditions arise.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $D(T)$ | domain of the operator, a dense subspace |
| $\Gamma(T)=\{(x,Tx)\}$ | the graph in $H\oplus H$ |
| $T^*$ | the adjoint, defined where $x\mapsto\langle Tx,y\rangle$ is bounded |
| $T\subseteq T^*$ | symmetry |
| $T=T^*$ | self-adjointness, with equality of domains |
| $\overline T=T^{**}$ | the closure for a closable operator |
| $\Gamma(T^*)=\Gamma(-T)^{\perp}$ | the graph relation |
| $C(T)=(T-iI)(T+iI)^{-1}$ | the Cayley transform, an isometry |
| $n_\pm=\dim\ker(T^*\mp iI)$ | the deficiency indices |
| $n_+=n_-=0$ | essential self-adjointness |

## Further Reading

- John von Neumann, "Allgemeine Eigenwerttheorie Hermitescher Funktionaloperatoren", *Mathematische Annalen* **102** (1930), 49–131, for the adjoint, the deficiency indices and the extension theory.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* (Academic Press, 1980), for the domains, the graph relation and the Cayley transform.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for symmetric and self-adjoint operators and their extensions.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II* (Interscience, 1963), for the closed operators and the adjoint on a Hilbert space.
- Joachim Weidmann, *Linear Operators in Hilbert Spaces* (Springer, 1980), for the systematic treatment of the deficiency indices and the self-adjoint extensions.
