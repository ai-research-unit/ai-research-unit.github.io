# __The Frame, the Simple Nilpotent and the Gauge of $M_2(\mathbb{C})$__

## Introduction

**At order two a frame is an idempotent of rank one together with a nonzero element of one mixed corner, a simple nilpotent is a rank-one matrix with square zero, and the gauge that remains after the idempotent is fixed is the single group $\mathbb{C}^{\times}$ of reciprocal rescalings.**

The article separates the three data of a frame, namely the idempotent, the simple nilpotent and the normalisation, computes the stabilisers and the orbit dimensions, proves that all frames are conjugate, and identifies the gauge with the stabiliser of the ordered frame. It assumes *The Peirce Basis and the Corners at $n=2$*, *The Peirce Decomposition and the Corner Recursion of $M_2(\mathbb{C})$* and *Lagrange Idempotents of a $2\times2$ Matrix with Simple Spectrum*.

It defers the general-order frame to *The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$*. The orbit count here is self-contained.

## The Three Data of a Frame

**A frame carries an idempotent, a nilpotent and a normalisation, and each is determined by the others only up to a choice.**

**Definition.** A **frame** at order two is a quadruple $(e,\upsilon_{+},\upsilon_{-},f)$ with $e$ and $f$ orthogonal idempotents of rank one summing to $I$ and with $\upsilon_{+}\upsilon_{-}=e$.

**Proposition.** The frame is determined by the pair $(e,\upsilon_{+})$ with $\upsilon_{+}$ a nonzero element of the corner $eM(1-e)$, and $\upsilon_{-}$ is then unique.

**Proof.** The idempotent $f$ is the complement of $e$; the corner $eM(1-e)$ is one-dimensional; and the normalisation $\upsilon_{+}\upsilon_{-}=e$ fixes the partner in the other mixed corner uniquely, as proved in *The Peirce Basis and the Corners at $n=2$*.

**Corollary.** The frame is determined by the idempotent together with a point of a punctured line, so the set of frames is a bundle over the set of idempotents with fibre $\mathbb{C}^{\times}$.

**Proof.** The corner is a complex line and the admissible $\upsilon_{+}$ are its nonzero points, which form a copy of $\mathbb{C}^{\times}$.

## The Simple Nilpotent

**Definition.** A **simple nilpotent** at order two is a matrix $N\ne0$ with $N^{2}=0$.

**Proposition.** Every simple nilpotent has rank one, its image equals its kernel, and it is the mixed generator of exactly those frames whose idempotent has the line of the image as its kernel.

**Proof.** The square zero gives $\operatorname{im}N\subseteq\ker N$; both are nonzero or zero together, and $N\ne0$ forces both to be the same line by the dimension count $1+1=2$. A frame with $\upsilon_{+}=N$ has $eN=N$ and $Ne=0$, so the image of $N$ lies in the image of $e$ and the kernel of $N$ contains the kernel of $e$; the two lines agree, so the image of $N$ is the image of $e$.

**Corollary.** The simple nilpotent fixes the line but not the idempotent: the idempotents whose mixed generator is $N$ are exactly those with image the line of $N$.

**Proof.** The image of $e$ must contain the image of $N$, which is a line, so the image of $e$ is that line; and every idempotent with that image satisfies $eN=N$ and $Ne=0$.

**Corollary.** All nonzero simple nilpotents are conjugate.

**Proof.** Each is the mixed generator of some frame, and all frames are conjugate by the theorem of the next section.

## All Frames Are Conjugate

**Theorem.** The group $\mathrm{GL}_2(\mathbb{C})$ acts transitively on the frames by conjugation.

**Proof.** Every idempotent of rank one is conjugate to $E_{11}$, so a frame may be carried to a frame with the idempotent $E_{11}$; then $\upsilon_{+}$ is a nonzero multiple of $E_{12}$, and the diagonal matrix $\operatorname{diag}(\lambda,\lambda^{-1})$ with $\lambda^{2}$ equal to that multiple carries it to $E_{12}$, with the partner carried to $E_{21}$.

**Corollary.** The conjugacy class of a frame is the class of the standard frame, and the orbit is the whole variety of frames.

**Proof.** The theorem gives the transitivity, so there is one orbit.

**Corollary.** Two frames are conjugate exactly when their idempotents have the same rank, which at order two is the only invariant.

**Proof.** Idempotents of the same rank are conjugate, and the frame is determined by the idempotent together with a point of the corner, which a conjugating matrix can always adjust.

## The Stabilisers and the Orbit Dimensions

**Theorem.** The stabilisers in $\mathrm{GL}_2(\mathbb{C})$ of the four data have the complex dimensions

$$
\dim\operatorname{Stab}(e)=2,\qquad \dim\operatorname{Stab}(e,f)=2,\qquad \dim\operatorname{Stab}(N)=2,\qquad \dim\operatorname{Stab}(\text{frame})=1 .
$$

**Proof.** The matrices commuting with $E_{11}$ are the diagonal ones, of dimension two; the same diagonal matrices fix $E_{22}$; the matrices commuting with $E_{12}$ are the matrices $\begin{pmatrix}a&b\\0&a\end{pmatrix}$, of dimension two; and the matrices fixing all four elements of the frame must commute with $E_{11}$ and with $E_{12}$, which forces the scalars.

**Corollary.** The orbit of the idempotent has dimension two, the orbit of the nilpotent has dimension two, and the orbit of the frame has dimension three.

**Proof.** The orbit dimension is the dimension of the group minus the dimension of the stabiliser, $4-2=2$ and $4-1=3$.

**Corollary.** The gauge is the quotient of the stabiliser of the idempotent by the stabiliser of the frame, and that quotient is the group $\mathbb{C}^{\times}$ of reciprocal rescalings.

**Proof.** Both stabilisers consist of diagonal matrices, of dimension two and one respectively; the quotient is one-dimensional and acts on the mixed line by rescaling, with the partner rescaled reciprocally to keep the normalisation.

## The Normalisation

**The normalisation $\upsilon_{+}\upsilon_{-}=e$ is what pins the gauge, and it is the only place where a choice is made.**

**Proposition.** The rescaling $\upsilon_{+}\mapsto\lambda\upsilon_{+}$ forces $\upsilon_{-}\mapsto\lambda^{-1}\upsilon_{-}$, and the two products $\upsilon_{+}\upsilon_{-}$ and $\upsilon_{-}\upsilon_{+}$ are invariant.

**Proof.** The product of the rescaled pair is $\lambda\lambda^{-1}\upsilon_{+}\upsilon_{-}=e$, and the second product is $\lambda^{-1}\lambda\upsilon_{-}\upsilon_{+}=f$; both are unchanged.

**Corollary.** The gauge is a torsor over $\mathbb{C}^{\times}$, with no preferred point, so a frame is a point of the bundle and not a canonical object.

**Proof.** Any two normalisations differ by a unique rescaling, and no rescaling is distinguished by the algebra alone.

**Corollary.** The modulus of the rescaling can be fixed by requiring $\operatorname{tr}(\upsilon_{-}\upsilon_{+})=\operatorname{tr}e$ together with a Hermitian condition, which selects a circle inside the gauge.

**Proof.** The trace condition is automatic, and the Hermitian condition $\upsilon_{-}=\upsilon_{+}^{*}$ is preserved exactly by the rescalings of modulus one.

## The Biquaternion Case

**Proposition.** In the biquaternion language the idempotent is the root of one $\tilde{Ζ}$ read through the pair $\tilde\Pi_{\mathrm{id},\pm}$, and the simple nilpotent is the companion nilpotent $\vec\Pi_{\mathrm{nil},+-}$ with its partner $\vec\Pi_{\mathrm{nil},-+}$.

**Proof.** The corpus builds the pair $\tilde\Pi_{\mathrm{id},\pm}=\tfrac12(e_t\pm\tilde{Ζ})$ from the root, which is the idempotent of the frame; and the companion nilpotents are the generators of the mixed corners normalised so that their product is $\tilde\Pi_{\mathrm{id},+}$.

**Corollary.** The gauge of the corpus is the same one complex parameter, and the normalisation is the same product condition.

**Proof.** The corpus states the freedom as one reciprocal rescaling $\lambda\in\mathbb{C}^{\times}$, which is the structure proved here.

**Corollary.** The correction recorded in the corpus applies here: the frame is built from the root and the idempotent pair, and no second anticommuting root is assumed.

**Proof.** The construction of the frame uses one idempotent, one nilpotent and one normalisation, and the involution that models the root is one point of the gauge, not a primitive datum.

## Summary

A frame at order two is an idempotent of rank one, a nonzero element of one mixed corner and the unique normalised partner, and it is determined by the idempotent together with a point of a punctured line. A simple nilpotent is a rank-one matrix with square zero; it fixes a line but not an idempotent, and all simple nilpotents are conjugate.

The stabilisers have complex dimensions two, two, two and one for the idempotent, the pair, the nilpotent and the ordered frame, so the orbits have dimensions two, two and three. The gauge after fixing the idempotent is $\mathbb{C}^{\times}$ of reciprocal rescalings, and the normalisation $\upsilon_{+}\upsilon_{-}=e$ is the only choice made.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e,f$ | the idempotent and its complement |
| $\upsilon_{+},\upsilon_{-}$ | the mixed generators of the frame |
| $N$ | a simple nilpotent, $N^{2}=0$, $N\ne0$ |
| $\lambda$ | the gauge parameter in $\mathbb{C}^{\times}$ |
| $\operatorname{Stab}$ | the stabiliser in $\mathrm{GL}_2(\mathbb{C})$ under conjugation |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for frames, the gauge and the conjugacy of idempotents.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the Jordan form of a nilpotent matrix at order two.
- [The Peirce Basis and the Corners at $n=2$](the-peirce-basis-and-the-corners-at-n-2.html), for the basis and the structure constants.
- [The Peirce Decomposition and the Corner Recursion of $M_2(\mathbb{C})$](the-peirce-decomposition-and-the-corner-recursion-of-m2c.html), for the corner language used here.
- [The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-mnc.html), for the frame at general order.
