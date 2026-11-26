# __Coda: $n=2$ and the Biquaternion Algebra__

## Introduction

**At $n=2$ the whole spine of the category is read in one algebra: the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is isomorphic to $M_2(\mathbb{C})$, its Peirce frame $\tilde\Pi_{\mathrm{id},\pm}$ is the frame of the two smallest idempotents, and every construction of the fifty-one preceding articles becomes a count in the eight real dimensions.**

The article reads the spine at $n=2$: the element, the two halves of the involution, the product on the halves, the four forms with their inertias, the Peirce frame with its corners and companion nilpotents, the spectrum and the exponential, and the algebraic norm $N$ with its inertia $(2,2)$. It assumes *The Trace Form and Its Inertia on the Two Halves*, *The Killing Form, Its Radical and the Triangular Case* and *The Peirce Decomposition of the Biquaternion Algebra*. It defers the frame and the coordinates to *The Peirce Basis of the Biquaternion Algebra* and *The Companion Nilpotents of the Biquaternion Algebra*.

## The Algebra and Its Element at Two

**The biquaternion algebra is the matrix algebra of the smallest size.** The algebra has the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t$ the unit and $\vec e_k^{2}=-e_t$, the coefficients complex, so

$$
\dim_{\mathbb{C}}\mathbb{B}=4,\qquad \dim_{\mathbb{R}}\mathbb{B}=8,\qquad \mathbb{B}\cong M_2(\mathbb{C}),
$$

the second equality following from the first and the last from the simplicity of the algebra. The computation confirms the two dimensions on the coefficient basis, and it is the reason the coda belongs to the category of $M_n(\mathbb{C})$.

**The element has a trace and a determinant read from the left multiplication.** For $q\in\mathbb{B}$ the left multiplication $L_q$ is a complex four-by-four matrix, and

$$
\operatorname{tr}L_q=4\,\mathrm{Sc}\,q,\qquad \det q=\det L_q,\qquad \chi_q(t)=\det(t\mathrm{I}-L_q),
$$

so the characteristic polynomial has degree four with the two eigenvalues of the matrix doubled. The computation confirms the identity $\operatorname{tr}L_q=4\,\mathrm{Sc}\,q$ at a random element, and it is the reason the element of the coda is the element of the category.

**The rank takes the three values of the two-by-two case.** Since $\mathbb{B}\cong M_2(\mathbb{C})$,

$$
\operatorname{rank}q\in\{0,1,2\},
$$

the zero divisors being the elements of rank one and the invertible elements those of rank two. The computation confirms the three values on random elements of the three kinds, and it is the smallest case of the element article.

## The Involutions and the Two Halves at Two

**The quaternion conjugation cuts the algebra in two parts of dimensions two and six.** The map ${}^{\natural}$ fixes $e_t$ and negates the three $\vec e_k$, so its fixed space is the centre and its anti-fixed space the vector part,

$$
\mathbb{B}=\mathbb{B}_{C}\oplus\mathbb{B}_{V},\qquad \dim_{\mathbb{R}}=2+6,
$$

and the split is the split of the involution of the category in the smallest case. The computation confirms the two dimensions and the two eigenspaces, and it is the first of the two involutions of the algebra.

**The conjugate transpose cuts it into four and four.** The Hermitian conjugation ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ is the analogue of the conjugate transpose, so

$$
\mathbb{B}=\mathbb{B}_{H}\oplus\mathbb{B}_{\Phi},\qquad \dim_{\mathbb{R}}=4+4,
$$

the Hermitian sector and the anti-Hermitian one. The computation confirms the dimensions and the identity $\mathbb{B}_{H}=\{q:q^{*}=q\}$, and it is *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian* at $n=2$.

**The Hermitian sector carries the Lorentzian form.** On $\mathbb{B}_{H}$ the norm restricts to

$$
\langle\tilde Q\rangle_{*}=\lvert Q_t\rvert^{2}-\lvert\vec Q\rvert^{2},
$$

of inertia $(1,3)$, and on the anti-Hermitian sector to the inertia $(3,1)$. The computation confirms the two inertias on a real basis of each sector, and it is the reason the coda meets the Lorentz group, the spin group being the double cover of its orthogonal group.

## The Product on the Two Halves at Two

**The product of two Hermitian elements is Hermitian exactly when they commute.** For $A,B\in\mathbb{B}_{H}$,

$$
AB\in\mathbb{B}_{H}\iff AB=BA,
$$

so the Hermitian half is closed under the product only on the commuting pairs, and the symmetrised product $\tfrac12(AB+BA)$ is the Jordan product of the half. The computation confirms the equivalence at random pairs of the sector, and it is the two-by-two case of the four multiplication tables.

**The commutator of two Hermitian elements is anti-Hermitian.** For $A,B\in\mathbb{B}_{H}$,

$$
[A,B]\in\mathbb{B}_{\Phi},
$$

so the bracket maps the Hermitian half into the antisymmetric half, and the two halves form a symmetric pair. The computation confirms the inclusion on random pairs, and it is the bracket relation $[\mathfrak{p},\mathfrak{p}]\subset\mathfrak{k}$ of *Symmetric Pairs and Cartan Pairs: the Reductivity Criterion* at $n=2$.

**The bracket of the anti-Hermitian half is the Lie algebra of the unitary group.** The anti-Hermitian sector is closed under the bracket and is

$$
\mathbb{B}_{\Phi}\cong\mathfrak{u}(2),\qquad \dim_{\mathbb{R}}=4,
$$

the Lie algebra of the unitary group of the two-by-two case. The computation confirms the closure and the dimension, and it is the smallest case of *The Lie Algebra $\operatorname{Skew}_n\cong\mathfrak{so}(n)$* read over $\mathbb{C}$.

## The Forms at Two

**The trace form of the algebra has inertia $(4,4)$.** The plain form $P(q_1,q_2)=\operatorname{Re}\mathrm{Sc}(q_1q_2)$ is a real symmetric form on the eight real dimensions, of the inertia $(4,4)$, four positive and four negative directions. The computation confirms the inertia by the eigenvalues $\pm1$ of the Gram matrix, and it is the trace form of the category at $n=2$.

**On the Hermitian half the trace form is positive definite.** For $A\in\mathbb{B}_{H}$ nonzero,

$$
P(A,A)>0,
$$

and on the anti-Hermitian half it is negative definite, so the two halves carry the two signs. The computation confirms the definiteness on random elements of each sector, and it is the reason the Hermitian half is the positive half of the coda.

**The Killing form has rank six and a radical of dimension two.** The Killing form $\kappa(X,Y)=\operatorname{tr}(\operatorname{ad}_X\operatorname{ad}_Y)$ has the eigenvalues $\pm8$ each of multiplicity three and the eigenvalue zero of multiplicity two, so the inertia on the six-dimensional quotient is $(3,3)$ and the radical is the centre $\mathbb{C}e_t$. The computation confirms the eigenvalues, the rank six and the two-dimensional radical, and it is the two-by-two case of *The Killing Form, Its Radical and the Triangular Case*.

## The Peirce Frame at Two

**A pure root of one gives the idempotent pair.** Let $\vec{Ζ}$ be a pure root of one,

$$
\vec{Ζ}^{2}=e_t,\qquad \vec{Ζ}^{\natural}=-\vec{Ζ},
$$

for example $\vec{Ζ}=i\vec e_x$. Then

$$
\tilde\Pi_{\mathrm{id},\pm}=\tfrac12(e_t\pm\tilde{Ζ})
$$

are idempotent, orthogonal and complete, with $\tilde\Pi_{\mathrm{id},+}\tilde\Pi_{\mathrm{id},-}=\tilde\Pi_{\mathrm{id},-}\tilde\Pi_{\mathrm{id},+}=0$ and $\tilde\Pi_{\mathrm{id},++}\tilde\Pi_{\mathrm{id},-}=e_t$. The computation confirms the three identities on the coefficients, and it is the frame of the coda.

**The frame cuts the algebra into four corners of two real dimensions.** Put

$$
\mathbb{B}_{st}=\tilde\Pi_{\mathrm{id},s}\mathbb{B}\tilde\Pi_{\mathrm{id},t},
$$

so that each corner is a complex line, of two real dimensions, the four summing to eight. The computation confirms the dimensions and the decomposition $8=2+2+2+2$, and it is the Peirce decomposition of the two-by-two case.

**The companion nilpotents normalise the frame.** Choose a nonzero $u\in\mathbb{B}_{+-}$ and the partner $v\in\mathbb{B}_{-+}$ fixed by

$$
uv=\tilde\Pi_{\mathrm{id},+},\qquad vu=\tilde\Pi_{\mathrm{id},-},
$$

so that $u^{2}=0=v^{2}$ and $u$ is one of the companion nilpotents $\vec\Pi_{\mathrm{nil},+-}$, $\vec\Pi_{\mathrm{nil},-+}$. The computation confirms the two squares and the two products on the coefficients, and it is the construction of *The Companion Nilpotents of the Biquaternion Algebra*.

**The freedom of the frame is one reciprocal rescaling.** The pair $(u,v)$ is defined up to $u\mapsto\lambda u$ and $v\mapsto\lambda^{-1}v$ with $\lambda\in\mathbb{C}^{\times}$, which keeps $uv=\tilde\Pi_{\mathrm{id},+}$ and $vu=\tilde\Pi_{\mathrm{id},-}$ unchanged, so the frame group has one complex parameter. The computation confirms the invariance on three values of $\lambda$, and it is the whole freedom of the frame, the idempotents being fixed once $\vec{Ζ}$ is chosen.

## The Spectrum, the Exponential and the Polar Decomposition at Two

**The Hermitian elements have a real spectrum.** For $A\in\mathbb{B}_{H}$ the eigenvalues are real and a unitary congruence diagonalises the element, so

$$
A=U\operatorname{diag}(\lambda_+,\lambda_-)U^{*},\qquad \lambda_\pm\in\mathbb{R},
$$

which was confirmed at $n=2$ on random Hermitian elements. So the spectral theorem of the two halves is the spectral theory of the biquaternion algebra on its Hermitian sector.

**The exponential splits into the rotation and the stretch.** For $X$ anti-Hermitian and $S$ Hermitian,

$$
e^{X}\in\mathrm{U}(2),\qquad e^{S}\text{ positive definite},
$$

so the exponential of the anti-Hermitian half gives the rotations and the exponential of the Hermitian half the stretches, each rotation having the two rotor signs $\pm e^{X/2}$. The computation confirms the unitarity of the first exponential, the positivity of the second and the two roots of a random unitary, and it is the polar decomposition of *The Polar Decomposition from the Two Halves* at $n=2$.

## The Norm and the Inertia $(2,2)$

**The norm is the product of the two corner coordinates.** On the diagonal subalgebra $\mathbb{C}\tilde\Pi_{\mathrm{id},+}\oplus\mathbb{C}\tilde\Pi_{\mathrm{id},-}$ the quaternionic algebraic norm is

$$
N(\alpha_+\tilde\Pi_{\mathrm{id},++}\alpha_-\tilde\Pi_{\mathrm{id},-})=\alpha_+\alpha_-,
$$

the product of the two Peirce coordinates, since $\tilde\Pi_{\mathrm{id},\pm}^{\natural}=\tilde\Pi_{\mathrm{id},\mp}$ and the two idempotents are orthogonal. The computation confirms the identity on random pairs of coefficients, and it is the reason the norm of the coda is written in the Peirce coordinates.

**The norm is indefinite, of inertia $(2,2)$ over $\mathbb{R}$.** Writing $\alpha_\pm=a_\pm+ib_\pm$,

$$
\operatorname{Re}N=a_+a_- - b_+b_-,
$$

whose Gram matrix is $\tfrac12\begin{pmatrix}0&1\\1&0\end{pmatrix}\oplus\tfrac12\begin{pmatrix}0&-1\\-1&0\end{pmatrix}$, of the eigenvalues $\pm\tfrac12$ each twice, so the inertia is $(2,2)$. The computation confirms the Gram matrix and the eigenvalues, and it is the inertia the coda has to report.

**On the whole algebra the same norm has inertia $(4,4)$.** The realification of $N$ on the eight dimensions gives $\operatorname{sign}N=(4,4)$, so the diagonal subalgebra carries half the positive and half the negative directions. The computation confirms the eigenvalues $\pm1$ each four times on the coefficient basis, and it is the reason the two readings are one form.

## Summary

At $n=2$ the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is $M_2(\mathbb{C})$, of real dimension eight, with the rank in $\{0,1,2\}$ and the characteristic polynomial of the left multiplication of degree four with the two eigenvalues doubled. The quaternion conjugation cuts it into the centre and the vector part of dimensions $2$ and $6$, the Hermitian conjugation into the Hermitian and the anti-Hermitian sectors of four real dimensions each, carrying the forms of inertia $(1,3)$ and $(3,1)$; the commutator of the Hermitian half lands in the anti-Hermitian half and the adjoint action of the anti-Hermitian half lands in the Hermitian half, and the anti-Hermitian half is $\mathfrak{u}(2)$. The trace form has inertia $(4,4)$ with the two halves definite, and the Killing form has rank six, inertia $(3,3)$ and the two-dimensional radical $\mathbb{C}e_t$. A pure root $\vec{Ζ}$ gives the idempotent pair $\tilde\Pi_{\mathrm{id},\pm}$, the four corners $\mathbb{B}_{st}$ of two real dimensions each, and the companion nilpotents $\vec\Pi_{\mathrm{nil},+-}$, $\vec\Pi_{\mathrm{nil},-+}$ normalised by $uv=\tilde\Pi_{\mathrm{id},+}$, with the single reciprocal rescaling as the whole frame group. The spectrum has the two points doubled, the Hermitian sector has a real spectrum, the exponential gives the rotations and the stretches, and the algebraic norm $N$ equals $\alpha_+\alpha_-$ on the diagonal subalgebra, with the inertia $(2,2)$ there and $(4,4)$ on the whole algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ | the biquaternion algebra, real dimension eight |
| $e_t$ | the unit |
| $\vec{Ζ}$, $\tilde{Ζ}$ | a pure root of one and a root of one |
| $\tilde\Pi_{\mathrm{id},\pm}=\tfrac12(e_t\pm\tilde{Ζ})$ | the idempotent pair |
| $\mathbb{B}_{st}=\tilde\Pi_{\mathrm{id},s}\mathbb{B}\tilde\Pi_{\mathrm{id},t}$ | the four corners |
| $\vec\Pi_{\mathrm{nil},+-}$, $\vec\Pi_{\mathrm{nil},-+}$ | the companion nilpotents, with $uv=\tilde\Pi_{\mathrm{id},+}$ |
| $N$ | the quaternionic algebraic norm, inertia $(2,2)$ on the diagonal subalgebra |
| $\mathbb{B}_{H}$, $\mathbb{B}_{\Phi}$ | the Hermitian and the anti-Hermitian sectors |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge, 1995), for the complex quaternions and the matrix model.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the biquaternions and their norms.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the two-by-two spectral theory.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the frame used here.
- [The Companion Nilpotents of the Biquaternion Algebra](the-companion-nilpotents-of-the-biquaternion-algebra.html), for the normalisation $uv=\tilde\Pi_{\mathrm{id},+}$.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four forms of the coda.
