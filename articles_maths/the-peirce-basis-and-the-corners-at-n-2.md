# __The Peirce Basis and the Corners at $n=2$__

## Introduction

**A rank-one idempotent $e$, one nonzero element $\upsilon_{+}$ of the corner $A_{12}$, and the partner $\upsilon_{-}$ fixed by $\upsilon_{+}\upsilon_{-}=e$ form a Peirce basis $(e,\upsilon_{+},\upsilon_{-},1-e)$ in which the multiplication is the multiplication of the matrix units.**

The article builds the basis, states the eight nonzero products that define it, proves that the gauge freedom is exactly one reciprocal rescaling $\upsilon_{+}\mapsto\lambda\upsilon_{+}$, $\upsilon_{-}\mapsto\lambda^{-1}\upsilon_{-}$ with $\lambda\in\mathbb{C}^{\times}$, reads the corners in the basis, and identifies the basis with the system of matrix units $E_{11}$, $E_{12}$, $E_{21}$, $E_{22}$. It assumes *The Peirce Decomposition in Two Dimensions* and *Lagrange Idempotents of a $2\times2$ Matrix with Simple Spectrum*, and it takes the nilpotent background from *The Minimal Polynomial and the Two Jordan Regimes of $M_2(\mathbb{C})$*.

It defers the frame in general dimension to *The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$* and the recursion to *The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$*.

## The Frame

**Definition.** A **frame** at order two is a pair of orthogonal idempotents $e$ and $f=1-e$, each of rank one.

**Proposition.** The pair is determined by its first member, and any two frames are conjugate.

**Proof.** The second member is the complement of the first, and any two rank-one idempotents are conjugate because they have the same rank, so a conjugating matrix carries one frame to the other.

**Corollary.** Every rank-one idempotent is conjugate to $E_{11}$, so the study of the frame reduces to the standard one.

**Proof.** The rank of an idempotent is the dimension of its image, and a matrix of full rank is invertible and conjugates the images.

**The frame is the matrix form of the corpus's root of one.** The corpus builds the frame from a root $\tilde{Ζ}$ of the identity and the pair $\tilde\Pi_{\mathrm{id},\pm}=\tfrac12(e_t\pm\tilde{Ζ})$; on the matrix side the root is the involution $\zeta$ of *Lagrange Idempotents of a $2\times2$ Matrix with Simple Spectrum* and the pair is $\rho_{\pm}$.

**Proof.** The identities $\tilde{Ζ}^{2}=e_t$ and $\tilde\Pi_{\mathrm{id},\pm}^{2}=\tilde\Pi_{\mathrm{id},\pm}$ are the identities $\zeta^{2}=I$ and $\rho_{\pm}^{2}=\rho_{\pm}$ proved there.

## The Nilpotent Pair

**Definition.** The **companion pair** of the frame is a pair $(\upsilon_{+},\upsilon_{-})$ with $\upsilon_{+}\in A_{12}$, $\upsilon_{-}\in A_{21}$ and $\upsilon_{+}\upsilon_{-}=e$.

**Proposition.** The companion pair exists, and for every frame and every choice of $\upsilon_{+}\ne0$ in $A_{12}$ there is exactly one partner.

**Proof.** At the standard frame the pair $E_{12},E_{21}$ works. In general the corner $A_{12}$ is one-dimensional, spanned by some $\upsilon_{+}$; the product $\upsilon_{+}A_{21}\subseteq A_{11}$ is the whole line of $e$ when $\upsilon_{+}\ne0$, so there is a unique $\upsilon_{-}$ in $A_{21}$ with $\upsilon_{+}\upsilon_{-}=e$.

**Corollary.** The pair is automatically nilpotent and satisfies $\upsilon_{+}^{2}=0$, $\upsilon_{-}^{2}=0$ and $\upsilon_{-}\upsilon_{+}=f$.

**Proof.** The mixed spaces are square-zero by *The Peirce Decomposition in Two Dimensions*, and $\upsilon_{-}\upsilon_{+}$ lies in $A_{00}$, which is the line of $f$; its trace is $\operatorname{tr}(\upsilon_{-}\upsilon_{+})=\operatorname{tr}(\upsilon_{+}\upsilon_{-})=\operatorname{tr}e=1$, so it is $f$.

**Corollary.** The four elements $e$, $\upsilon_{+}$, $\upsilon_{-}$, $f$ are linearly independent, hence a basis.

**Proof.** They lie in four different Peirce spaces, whose direct sum is the whole space.

## The Structure Constants

**Theorem.** In the basis $(e,\upsilon_{+},\upsilon_{-},f)$ the eight nonzero products are

$$
e^{2}=e,\quad e\upsilon_{+}=\upsilon_{+},\quad \upsilon_{+}f=\upsilon_{+},\quad \upsilon_{+}\upsilon_{-}=e,\quad
\upsilon_{-}e=\upsilon_{-},\quad f\upsilon_{-}=\upsilon_{-},\quad \upsilon_{-}\upsilon_{+}=f,\quad f^{2}=f,
$$

and every other product of two basis elements vanishes.

**Proof.** Each product is read from the index rule of *The Peirce Decomposition in Two Dimensions* together with the normalisation $\upsilon_{+}\upsilon_{-}=e$ and the identity $\upsilon_{-}\upsilon_{+}=f$; the products with a wrong middle index vanish by the second Peirce rule.

**Corollary.** The table is the table of the matrix units, with $e$ playing $E_{11}$, $\upsilon_{+}$ playing $E_{12}$, $\upsilon_{-}$ playing $E_{21}$ and $f$ playing $E_{22}$.

**Proof.** The eight products listed are exactly the eight nonzero products of the four matrix units.

**Corollary.** The algebra has no room for a second relation: the table determines the product of any two elements from their coordinates in the basis.

**Proof.** The product is bilinear, so it is determined on the basis, and the table gives it there.

## The Gauge

**Theorem.** The pair $(\upsilon_{+},\upsilon_{-})$ is determined by $\upsilon_{+}$ up to the reciprocal rescaling

$$
\upsilon_{+}\mapsto\lambda\upsilon_{+},\qquad \upsilon_{-}\mapsto\lambda^{-1}\upsilon_{-},\qquad \lambda\in\mathbb{C}^{\times}.
$$

**Proof.** The product of the rescaled pair is $\lambda\lambda^{-1}\upsilon_{+}\upsilon_{-}=e$, so every such rescaling gives a companion pair; conversely, if $(\upsilon_{+}',\upsilon_{-}')$ is another pair then $\upsilon_{+}'=\lambda\upsilon_{+}$ for some $\lambda\ne0$ because the corner is a line, and the normalisation forces $\upsilon_{-}'=\lambda^{-1}\upsilon_{-}$.

**Corollary.** The gauge is one complex parameter, and the frame itself has no gauge freedom once $e$ is fixed.

**Proof.** The idempotent $e$ is fixed and the complement is determined by it; only the choice of the generator of the mixed line and its reciprocal partner is free.

**Corollary.** The element $\upsilon_{+}\upsilon_{-}$ and the element $\upsilon_{-}\upsilon_{+}$ are gauge invariant, and the two products $\upsilon_{+}^{2}$ and $\upsilon_{-}^{2}$ vanish in every gauge.

**Proof.** The first two products are $e$ and $f$ independently of $\lambda$, and the squares vanish because the mixed spaces are square-zero.

**The gauge is what remains of the diagonal matrix of the diagonalisation.** A matrix that diagonalises an element is determined up to the diagonal rescalings, and at order two those rescalings act on the two mixed lines reciprocally.

**Proof.** Conjugating by a diagonal matrix $\operatorname{diag}(\lambda,\mu)$ multiplies $E_{12}$ by $\lambda\mu^{-1}$ and $E_{21}$ by $\mu\lambda^{-1}$; the normalisation $\upsilon_{+}\upsilon_{-}=e$ then forces $\mu=1$, leaving the single parameter $\lambda$.

## The System of Matrix Units

**Theorem.** The assignment $E_{11}\mapsto e$, $E_{12}\mapsto\upsilon_{+}$, $E_{21}\mapsto\upsilon_{-}$, $E_{22}\mapsto f$ extends to an algebra isomorphism $M_2(\mathbb{C})\to M_2(\mathbb{C})$, namely the conjugation by the matrix whose columns are the images of the standard basis.

**Proof.** The assignment preserves the eight nonzero products, so it preserves every product by bilinearity, and an algebra map of a simple algebra to itself with nonzero image is injective and hence bijective.

**Corollary.** Every frame is the image of the standard frame under an automorphism, and the automorphisms of the algebra are the inner ones.

**Proof.** The map constructed is an automorphism, and every automorphism of a full matrix algebra is inner.

**Corollary.** The corners are the four lines of the basis, and their products are the products of the corners of the standard frame.

**Proof.** The isomorphism carries corners to corners, and at the standard frame the corners are the four lines.

## The Coordinates

**Proposition.** In the Peirce coordinates $x=x_{0}e+x_{+}\upsilon_{+}+x_{-}\upsilon_{-}+x_{1}f$ the product is

$$
(xy)_{0}=x_{0}y_{0}+x_{+}y_{-},\quad (xy)_{+}=x_{0}y_{+}+x_{+}y_{1},\quad (xy)_{-}=x_{-}y_{0}+x_{1}y_{-},\quad (xy)_{1}=x_{-}y_{+}+x_{1}y_{1}.
$$

**Proof.** Multiply the two coordinate expressions and collect the four basis elements using the structure constants.

**Corollary.** The trace is $x_{0}+x_{1}$ and the determinant is $x_{0}x_{1}-x_{+}x_{-}$.

**Proof.** The trace is the sum of the two idempotent coordinates because $\operatorname{tr}\upsilon_{\pm}=0$, and the determinant is the product of the diagonal coordinates minus the product of the two mixed ones, as at the standard frame.

**Corollary.** The element is invertible exactly when $x_{0}x_{1}\ne x_{+}x_{-}$, and the inverse has the coordinates $\dfrac{1}{x_{0}x_{1}-x_{+}x_{-}}(x_{1},-x_{+},-x_{-},x_{0})$.

**Proof.** The inverse of a two-by-two matrix in the matrix-unit coordinates is the adjugate divided by the determinant, and the Peirce coordinates are the matrix-unit coordinates.

## Summary

A frame at order two is a pair of orthogonal rank-one idempotents $e$ and $f=1-e$. Adjoining a nonzero $\upsilon_{+}$ in the corner $A_{12}$ and the unique partner $\upsilon_{-}$ with $\upsilon_{+}\upsilon_{-}=e$ gives the Peirce basis $(e,\upsilon_{+},\upsilon_{-},f)$, in which the eight nonzero products are those of the matrix units.

The pair $(\upsilon_{+},\upsilon_{-})$ is determined up to the reciprocal rescaling by $\lambda\in\mathbb{C}^{\times}$, and that is the only freedom of the frame. The coordinates in the basis carry the trace $x_{0}+x_{1}$ and the determinant $x_{0}x_{1}-x_{+}x_{-}$, and the assignment of the basis to the matrix units is an inner automorphism.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e,f$ | the two idempotents of the frame, $f=1-e$ |
| $\upsilon_{+},\upsilon_{-}$ | the companion pair, $\upsilon_{+}\upsilon_{-}=e$ |
| $A_{12},A_{21}$ | the mixed corners |
| $\lambda$ | the gauge parameter in $\mathbb{C}^{\times}$ |
| $x_{0},x_{+},x_{-},x_{1}$ | the Peirce coordinates |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Peirce basis and the system of matrix units.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the frame and the gauge in the Peirce language.
- [The Peirce Decomposition in Two Dimensions](the-peirce-decomposition-in-two-dimensions.html), for the four spaces that the basis linearises.
- [The Peirce Basis of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html), for the same basis in the biquaternion language.
- [The Frame, the Simple Nilpotents and the Gauge of $M_n(\mathbb{C})$](the-frame-the-simple-nilpotents-and-the-gauge-of-mnc.html), for the frame carried to the general order.
