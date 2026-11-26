# __Spinors as Peirce Coordinates in Two Dimensions__

## Introduction

**Choose an orthonormal pair of spinors $Ξ_{\mathrm{wfn}}$ and $\eta$; then the Peirce coordinates of a matrix $x$ are the four matrix elements $x_{0}=Ξ_{\mathrm{wfn}}^{*}xΞ_{\mathrm{wfn}}$, $x_{+}=Ξ_{\mathrm{wfn}}^{*}x\eta$, $x_{-}=\eta^{*}xΞ_{\mathrm{wfn}}$, $x_{1}=\eta^{*}x\eta$, and the Peirce formula is the change of basis $x=U\begin{pmatrix}x_{0}&x_{+}\\ x_{-}&x_{1}\end{pmatrix}U^{*}$ with $U=(Ξ_{\mathrm{wfn}},\eta)$ unitary.**

The article builds the rank-one Hermitian idempotent of a spinor, obtains the Peirce frame from an orthonormal pair, proves that the Peirce coordinates are the matrix elements in that frame, reads the frame freedom as the phase of the spinor, and interprets the sphere of Hermitian idempotents as a Hopf fibration over the projective line. It assumes *The Peirce Basis and the Corners at $n=2$*, *The Peirce Decomposition and the Two Halves at $n=2$* and *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$*.

It defers the spectral theorem to *The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents*.

## The Idempotent of a Spinor

**Definition.** A **spinor** is a column $Ξ_{\mathrm{wfn}}\in\mathbb{C}^{2}$ with $Ξ_{\mathrm{wfn}}\ne0$, and its **idempotent** is $e_{Ξ_{\mathrm{wfn}}}=Ξ_{\mathrm{wfn}}Ξ_{\mathrm{wfn}}^{*}/\|Ξ_{\mathrm{wfn}}\|^{2}$.

**Proposition.** The matrix $e_{Ξ_{\mathrm{wfn}}}$ is a Hermitian idempotent of rank one, and its image is the line of $Ξ_{\mathrm{wfn}}$.

**Proof.** $e_{Ξ_{\mathrm{wfn}}}^{2}=Ξ_{\mathrm{wfn}}(Ξ_{\mathrm{wfn}}^{*}Ξ_{\mathrm{wfn}})Ξ_{\mathrm{wfn}}^{*}/\|Ξ_{\mathrm{wfn}}\|^{4}=Ξ_{\mathrm{wfn}}Ξ_{\mathrm{wfn}}^{*}/\|Ξ_{\mathrm{wfn}}\|^{2}=e_{Ξ_{\mathrm{wfn}}}$, and $e_{Ξ_{\mathrm{wfn}}}^{*}=e_{Ξ_{\mathrm{wfn}}}$; its image consists of the multiples of $Ξ_{\mathrm{wfn}}$, so its rank is one.

**Corollary.** Every rank-one Hermitian idempotent is $e_{Ξ_{\mathrm{wfn}}}$ for some spinor $Ξ_{\mathrm{wfn}}$, and $Ξ_{\mathrm{wfn}}$ is determined up to a phase.

**Proof.** A rank-one Hermitian idempotent is the orthogonal projection onto its image, which is a line, and a unit vector of the line gives $Ξ_{\mathrm{wfn}}$; two unit vectors of the same line differ by a phase.

**Corollary.** The trace of $e_{Ξ_{\mathrm{wfn}}}$ is one and its determinant is zero.

**Proof.** The trace is the sum of the squared moduli of the entries of the unit spinor, which is one, and the rank is one.

## The Frame from Two Spinors

**Definition.** An **orthonormal spinor frame** is a pair $(Ξ_{\mathrm{wfn}},\eta)$ with $Ξ_{\mathrm{wfn}}^{*}Ξ_{\mathrm{wfn}}=\eta^{*}\eta=1$ and $Ξ_{\mathrm{wfn}}^{*}\eta=0$.

**Proposition.** The pair gives the Peirce frame $e=e_{Ξ_{\mathrm{wfn}}}$, $f=e_{\eta}$, $\upsilon_{+}=Ξ_{\mathrm{wfn}}\eta^{*}$, $\upsilon_{-}=\etaΞ_{\mathrm{wfn}}^{*}$, and the four elements satisfy the structure constants of *The Peirce Basis and the Corners at $n=2$*.

**Proof.** $\upsilon_{+}\upsilon_{-}=Ξ_{\mathrm{wfn}}(\eta^{*}\eta)Ξ_{\mathrm{wfn}}^{*}=Ξ_{\mathrm{wfn}}Ξ_{\mathrm{wfn}}^{*}=e$ and $\upsilon_{-}\upsilon_{+}=\eta\eta^{*}=f$; the products with $e$ and $f$ follow because $Ξ_{\mathrm{wfn}}$ and $\eta$ are orthogonal and of norm one.

**Corollary.** The four elements are the four entries of the unitary matrix $U=(Ξ_{\mathrm{wfn}},\eta)$ multiplied by the conjugate entries: $e=Ξ_{\mathrm{wfn}}Ξ_{\mathrm{wfn}}^{*}$ is the corner $(1,1)$, $\upsilon_{+}=Ξ_{\mathrm{wfn}}\eta^{*}$ the corner $(1,2)$, $\upsilon_{-}$ the corner $(2,1)$ and $f$ the corner $(2,2)$.

**Proof.** Each element is the outer product of one spinor of the frame with the conjugate of one spinor of the frame, and the two spins are the two entries of $U$.

**Corollary.** The two idempotents are complementary and orthogonal, and the two nilpotents are nilpotent of index two.

**Proof.** $ef=0$ because $Ξ_{\mathrm{wfn}}^{*}\eta=0$; and $\upsilon_{+}^{2}=Ξ_{\mathrm{wfn}}(\eta^{*}Ξ_{\mathrm{wfn}})\eta^{*}=0$, with the same computation for $\upsilon_{-}$.

## The Peirce Coordinates as Matrix Elements

**Theorem.** For a matrix $x$ and an orthonormal spinor frame,

$$
x=x_{0}e+x_{+}\upsilon_{+}+x_{-}\upsilon_{-}+x_{1}f,\qquad
x_{0}=Ξ_{\mathrm{wfn}}^{*}xΞ_{\mathrm{wfn}},\quad x_{+}=Ξ_{\mathrm{wfn}}^{*}x\eta,\quad x_{-}=\eta^{*}xΞ_{\mathrm{wfn}},\quad x_{1}=\eta^{*}x\eta,
$$

and the four numbers are the entries of $U^{*}xU$.

**Proof.** Evaluate the Peirce expansion at the two spins: $xΞ_{\mathrm{wfn}}=x_{0}Ξ_{\mathrm{wfn}}+x_{-}\eta$ and $x\eta=x_{+}Ξ_{\mathrm{wfn}}+x_{1}\eta$, because $eΞ_{\mathrm{wfn}}=Ξ_{\mathrm{wfn}}$, $fΞ_{\mathrm{wfn}}=0$, $\upsilon_{+}Ξ_{\mathrm{wfn}}=0$ and $\upsilon_{-}Ξ_{\mathrm{wfn}}=\eta$, and symmetrically for $\eta$. Taking the scalar products with $Ξ_{\mathrm{wfn}}$ and $\eta$ gives the four displays.

**Corollary.** The Peirce coordinates are the entries of the matrix of $x$ in the spinor basis, so the Peirce decomposition is the change of basis from the standard basis to the spinor frame.

**Proof.** The columns of $U^{*}xU$ are the coordinates of the images of the two basis spinors, which is the definition of the matrix of $x$ in that basis.

**Corollary.** The trace is $x_{0}+x_{1}$ and the determinant is $x_{0}x_{1}-x_{+}x_{-}$.

**Proof.** The trace and the determinant are invariant under the unitary change of basis $U^{*}xU$.

## The Frame Group and the Phase

**Proposition.** Replacing $Ξ_{\mathrm{wfn}}$ by $e^{i\theta}Ξ_{\mathrm{wfn}}$ and $\eta$ by $e^{i\digamma_{\mathrm{map}}}\eta$ leaves $e$ and $f$ unchanged and multiplies $\upsilon_{+}$ by $e^{i(\theta-\digamma_{\mathrm{map}})}$ and $\upsilon_{-}$ by $e^{-i(\theta-\digamma_{\mathrm{map}})}$.

**Proof.** The idempotent $e_{Ξ_{\mathrm{wfn}}}$ is unchanged because the phase cancels between the spinor and its conjugate; the nilpotent $Ξ_{\mathrm{wfn}}\eta^{*}$ collects the phase of $Ξ_{\mathrm{wfn}}$ and the inverse phase of $\eta$.

**Corollary.** The frame group of *The Peirce Basis and the Corners at $n=2$* is realised here by the relative phase, and the modulus of the rescaling is fixed by the normalisation of the spinors.

**Proof.** The relative phase $e^{i(\theta-\digamma_{\mathrm{map}})}$ is exactly the reciprocal rescaling with $\lambda$ of modulus one; the modulus is not free because both spinors are unit vectors.

**Corollary.** The frames over a fixed pair of orthogonal lines form a circle, the circle of relative phases.

**Proof.** Each of the two spinors carries a phase and only the difference acts on the mixed lines, so the effective freedom is one circle.

## The Hopf Fibration

**Theorem.** The map $Ξ_{\mathrm{wfn}}\mapsto e_{Ξ_{\mathrm{wfn}}}$ from the unit sphere $S^{3}$ to the set of Hermitian idempotents of rank one is a fibration with the fibre a circle, and its base is the projective line $\mathbb{P}^{1}$.

**Proof.** Two unit spinors give the same idempotent exactly when they differ by a phase, so the fibres are circles; the idempotent determines the line, and the lines form $\mathbb{P}^{1}$; the local triviality is the local choice of a phase.

**Corollary.** The set of Hermitian idempotents of rank one is a two-sphere, and the fibration is the Hopf fibration $S^{1}\to S^{3}\to S^{2}$.

**Proof.** Every rank-one Hermitian idempotent is $\tfrac12(I+\vec n\cdot\vec\sigma)$ with $\vec n$ a unit vector, so the set is parametrised by the unit sphere in three dimensions, and the projective line is the two-sphere of directions.

**Corollary.** The fibre direction is the phase, which acts trivially on the idempotent but not on the frame.

**Proof.** The phase multiplies the spinor and leaves the projection onto its line unchanged, while it changes the companion spinor and hence the nilpotents.

## The Action on Spinors

**Proposition.** A matrix $x$ acts on spinors by multiplication, and in the spinor frame this action is the multiplication of the Peirce matrix by the column of coordinates.

**Proof.** The coordinates of $xΞ_{\mathrm{wfn}}$ in the frame are the scalar products $Ξ_{\mathrm{wfn}}^{*}xΞ_{\mathrm{wfn}}$ and $\eta^{*}xΞ_{\mathrm{wfn}}$, which are the first column of $U^{*}xU$.

**Corollary.** The rank of $x$ is the number of linearly independent columns in the spinor frame, so it is read from the Peirce coordinates directly.

**Proof.** The change of basis is invertible, so it preserves the rank, and the rank of a two-by-two matrix is the number of independent columns.

**Corollary.** The element $x$ is a rank-one matrix exactly when its two columns in the spinor frame are proportional, which is the condition $x_{0}x_{1}=x_{+}x_{-}$.

**Proof.** The proportionality of the two columns is the vanishing of the determinant, which is $x_{0}x_{1}-x_{+}x_{-}$.

## Summary

A nonzero spinor $Ξ_{\mathrm{wfn}}$ gives the rank-one Hermitian idempotent $e_{Ξ_{\mathrm{wfn}}}=Ξ_{\mathrm{wfn}}Ξ_{\mathrm{wfn}}^{*}/\|Ξ_{\mathrm{wfn}}\|^{2}$, and an orthonormal pair of spinors gives the Peirce frame $e$, $\upsilon_{+}=Ξ_{\mathrm{wfn}}\eta^{*}$, $\upsilon_{-}=\etaΞ_{\mathrm{wfn}}^{*}$, $f$.

The Peirce coordinates of a matrix are its four matrix elements in the spinor basis, $x_{0}=Ξ_{\mathrm{wfn}}^{*}xΞ_{\mathrm{wfn}}$, $x_{+}=Ξ_{\mathrm{wfn}}^{*}x\eta$, $x_{-}=\eta^{*}xΞ_{\mathrm{wfn}}$, $x_{1}=\eta^{*}x\eta$, and the Peirce formula is the unitary change of basis. The frame group is the relative phase of the two spinors, with the modulus fixed by normalisation, and the sphere of Hermitian idempotents is the base of the Hopf fibration.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Ξ_{\mathrm{wfn}},\eta$ | the orthonormal spinor frame |
| $e_{Ξ_{\mathrm{wfn}}}$ | the Hermitian idempotent of $Ξ_{\mathrm{wfn}}$ |
| $U$ | the unitary matrix $(Ξ_{\mathrm{wfn}},\eta)$ |
| $x_{0},x_{+},x_{-},x_{1}$ | the Peirce coordinates, equal to the matrix elements |
| $\theta,\digamma_{\mathrm{map}}$ | the phases of the two spinors |

## Further Reading

- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, volume 1 (Cambridge University Press, 1984), for the two-component spinor and its phase.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the unitary change of basis and the rank-one projection of a vector.
- [The Peirce Basis and the Corners at $n=2$](the-peirce-basis-and-the-corners-at-n-2.html), for the frame that the spinors build.
- [The Peirce Decomposition and the Two Halves at $n=2$](the-peirce-decomposition-and-the-two-halves-at-n-2.html), for the corners and the star.
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the rank-one idempotents as the carriers of the minimal ideals.
