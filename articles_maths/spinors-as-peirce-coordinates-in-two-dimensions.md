# __Spinors as Peirce Coordinates in Two Dimensions__

## Introduction

**Choose an orthonormal pair of spinors $\psi$ and $\eta$; then the Peirce coordinates of a matrix $x$ are the four matrix elements $x_{0}=\psi^{*}x\psi$, $x_{+}=\psi^{*}x\eta$, $x_{-}=\eta^{*}x\psi$, $x_{1}=\eta^{*}x\eta$, and the Peirce formula is the change of basis $x=U\begin{pmatrix}x_{0}&x_{+}\\ x_{-}&x_{1}\end{pmatrix}U^{*}$ with $U=(\psi,\eta)$ unitary.**

The article builds the rank-one Hermitian idempotent of a spinor, obtains the Peirce frame from an orthonormal pair, proves that the Peirce coordinates are the matrix elements in that frame, reads the gauge freedom as the phase of the spinor, and interprets the sphere of Hermitian idempotents as a Hopf fibration over the projective line. It assumes *The Peirce Basis and the Corners at $n=2$*, *The Peirce Decomposition and the Two Halves at $n=2$* and *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$*.

It defers the spectral theorem to *The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents*.

## The Idempotent of a Spinor

**Definition.** A **spinor** is a column $\psi\in\mathbb{C}^{2}$ with $\psi\ne0$, and its **idempotent** is $e_{\psi}=\psi\psi^{*}/\|\psi\|^{2}$.

**Proposition.** The matrix $e_{\psi}$ is a Hermitian idempotent of rank one, and its image is the line of $\psi$.

**Proof.** $e_{\psi}^{2}=\psi(\psi^{*}\psi)\psi^{*}/\|\psi\|^{4}=\psi\psi^{*}/\|\psi\|^{2}=e_{\psi}$, and $e_{\psi}^{*}=e_{\psi}$; its image consists of the multiples of $\psi$, so its rank is one.

**Corollary.** Every rank-one Hermitian idempotent is $e_{\psi}$ for some spinor $\psi$, and $\psi$ is determined up to a phase.

**Proof.** A rank-one Hermitian idempotent is the orthogonal projection onto its image, which is a line, and a unit vector of the line gives $\psi$; two unit vectors of the same line differ by a phase.

**Corollary.** The trace of $e_{\psi}$ is one and its determinant is zero.

**Proof.** The trace is the sum of the squared moduli of the entries of the unit spinor, which is one, and the rank is one.

## The Frame from Two Spinors

**Definition.** An **orthonormal spinor frame** is a pair $(\psi,\eta)$ with $\psi^{*}\psi=\eta^{*}\eta=1$ and $\psi^{*}\eta=0$.

**Proposition.** The pair gives the Peirce frame $e=e_{\psi}$, $f=e_{\eta}$, $\upsilon_{+}=\psi\eta^{*}$, $\upsilon_{-}=\eta\psi^{*}$, and the four elements satisfy the structure constants of *The Peirce Basis and the Corners at $n=2$*.

**Proof.** $\upsilon_{+}\upsilon_{-}=\psi(\eta^{*}\eta)\psi^{*}=\psi\psi^{*}=e$ and $\upsilon_{-}\upsilon_{+}=\eta\eta^{*}=f$; the products with $e$ and $f$ follow because $\psi$ and $\eta$ are orthogonal and of norm one.

**Corollary.** The four elements are the four entries of the unitary matrix $U=(\psi,\eta)$ multiplied by the conjugate entries: $e=\psi\psi^{*}$ is the corner $(1,1)$, $\upsilon_{+}=\psi\eta^{*}$ the corner $(1,2)$, $\upsilon_{-}$ the corner $(2,1)$ and $f$ the corner $(2,2)$.

**Proof.** Each element is the outer product of one spinor of the frame with the conjugate of one spinor of the frame, and the two spins are the two entries of $U$.

**Corollary.** The two idempotents are complementary and orthogonal, and the two nilpotents are nilpotent of index two.

**Proof.** $ef=0$ because $\psi^{*}\eta=0$; and $\upsilon_{+}^{2}=\psi(\eta^{*}\psi)\eta^{*}=0$, with the same computation for $\upsilon_{-}$.

## The Peirce Coordinates as Matrix Elements

**Theorem.** For a matrix $x$ and an orthonormal spinor frame,

$$
x=x_{0}e+x_{+}\upsilon_{+}+x_{-}\upsilon_{-}+x_{1}f,\qquad
x_{0}=\psi^{*}x\psi,\quad x_{+}=\psi^{*}x\eta,\quad x_{-}=\eta^{*}x\psi,\quad x_{1}=\eta^{*}x\eta,
$$

and the four numbers are the entries of $U^{*}xU$.

**Proof.** Evaluate the Peirce expansion at the two spins: $x\psi=x_{0}\psi+x_{-}\eta$ and $x\eta=x_{+}\psi+x_{1}\eta$, because $e\psi=\psi$, $f\psi=0$, $\upsilon_{+}\psi=0$ and $\upsilon_{-}\psi=\eta$, and symmetrically for $\eta$. Taking the scalar products with $\psi$ and $\eta$ gives the four displays.

**Corollary.** The Peirce coordinates are the entries of the matrix of $x$ in the spinor basis, so the Peirce decomposition is the change of basis from the standard basis to the spinor frame.

**Proof.** The columns of $U^{*}xU$ are the coordinates of the images of the two basis spinors, which is the definition of the matrix of $x$ in that basis.

**Corollary.** The trace is $x_{0}+x_{1}$ and the determinant is $x_{0}x_{1}-x_{+}x_{-}$.

**Proof.** The trace and the determinant are invariant under the unitary change of basis $U^{*}xU$.

## The Gauge and the Phase

**Proposition.** Replacing $\psi$ by $e^{i\theta}\psi$ and $\eta$ by $e^{i\varphi}\eta$ leaves $e$ and $f$ unchanged and multiplies $\upsilon_{+}$ by $e^{i(\theta-\varphi)}$ and $\upsilon_{-}$ by $e^{-i(\theta-\varphi)}$.

**Proof.** The idempotent $e_{\psi}$ is unchanged because the phase cancels between the spinor and its conjugate; the nilpotent $\psi\eta^{*}$ collects the phase of $\psi$ and the inverse phase of $\eta$.

**Corollary.** The gauge of *The Peirce Basis and the Corners at $n=2$* is realised here by the relative phase, and the modulus of the rescaling is fixed by the normalisation of the spinors.

**Proof.** The relative phase $e^{i(\theta-\varphi)}$ is exactly the reciprocal rescaling with $\lambda$ of modulus one; the modulus is not free because both spinors are unit vectors.

**Corollary.** The frames over a fixed pair of orthogonal lines form a circle, the circle of relative phases.

**Proof.** Each of the two spinors carries a phase and only the difference acts on the mixed lines, so the effective freedom is one circle.

## The Hopf Fibration

**Theorem.** The map $\psi\mapsto e_{\psi}$ from the unit sphere $S^{3}$ to the set of Hermitian idempotents of rank one is a fibration with the fibre a circle, and its base is the projective line $\mathbb{P}^{1}$.

**Proof.** Two unit spinors give the same idempotent exactly when they differ by a phase, so the fibres are circles; the idempotent determines the line, and the lines form $\mathbb{P}^{1}$; the local triviality is the local choice of a phase.

**Corollary.** The set of Hermitian idempotents of rank one is a two-sphere, and the fibration is the Hopf fibration $S^{1}\to S^{3}\to S^{2}$.

**Proof.** Every rank-one Hermitian idempotent is $\tfrac12(I+\vec n\cdot\vec\sigma)$ with $\vec n$ a unit vector, so the set is parametrised by the unit sphere in three dimensions, and the projective line is the two-sphere of directions.

**Corollary.** The fibre direction is the phase, which acts trivially on the idempotent but not on the frame.

**Proof.** The phase multiplies the spinor and leaves the projection onto its line unchanged, while it changes the companion spinor and hence the nilpotents.

## The Action on Spinors

**Proposition.** A matrix $x$ acts on spinors by multiplication, and in the spinor frame this action is the multiplication of the Peirce matrix by the column of coordinates.

**Proof.** The coordinates of $x\psi$ in the frame are the scalar products $\psi^{*}x\psi$ and $\eta^{*}x\psi$, which are the first column of $U^{*}xU$.

**Corollary.** The rank of $x$ is the number of linearly independent columns in the spinor frame, so it is read from the Peirce coordinates directly.

**Proof.** The change of basis is invertible, so it preserves the rank, and the rank of a two-by-two matrix is the number of independent columns.

**Corollary.** The element $x$ is a rank-one matrix exactly when its two columns in the spinor frame are proportional, which is the condition $x_{0}x_{1}=x_{+}x_{-}$.

**Proof.** The proportionality of the two columns is the vanishing of the determinant, which is $x_{0}x_{1}-x_{+}x_{-}$.

## Summary

A nonzero spinor $\psi$ gives the rank-one Hermitian idempotent $e_{\psi}=\psi\psi^{*}/\|\psi\|^{2}$, and an orthonormal pair of spinors gives the Peirce frame $e$, $\upsilon_{+}=\psi\eta^{*}$, $\upsilon_{-}=\eta\psi^{*}$, $f$.

The Peirce coordinates of a matrix are its four matrix elements in the spinor basis, $x_{0}=\psi^{*}x\psi$, $x_{+}=\psi^{*}x\eta$, $x_{-}=\eta^{*}x\psi$, $x_{1}=\eta^{*}x\eta$, and the Peirce formula is the unitary change of basis. The gauge is the relative phase of the two spinors, with the modulus fixed by normalisation, and the sphere of Hermitian idempotents is the base of the Hopf fibration.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\psi,\eta$ | the orthonormal spinor frame |
| $e_{\psi}$ | the Hermitian idempotent of $\psi$ |
| $U$ | the unitary matrix $(\psi,\eta)$ |
| $x_{0},x_{+},x_{-},x_{1}$ | the Peirce coordinates, equal to the matrix elements |
| $\theta,\varphi$ | the phases of the two spinors |

## Further Reading

- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, volume 1 (Cambridge University Press, 1984), for the two-component spinor and its phase.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the unitary change of basis and the rank-one projection of a vector.
- [The Peirce Basis and the Corners at $n=2$](the-peirce-basis-and-the-corners-at-n-2.html), for the frame that the spinors build.
- [The Peirce Decomposition and the Two Halves at $n=2$](the-peirce-decomposition-and-the-two-halves-at-n-2.html), for the corners and the star.
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the rank-one idempotents as the carriers of the minimal ideals.
