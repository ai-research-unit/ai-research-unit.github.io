# __The Spectral Theorem: the Skew-Hermitian Case and the Two Imaginary Eigenvalues__

## Introduction

**A skew-Hermitian $2\times2$ matrix is $X=ia\,I+ir\,\vec n\cdot\vec\sigma$ with $a$ real, $r\ge0$ and $\vec n$ a unit vector, and its two eigenvalues are the purely imaginary numbers $i(a+r)$ and $i(a-r)$, symmetric about $ia$.**

The article describes the skew-Hermitian space, proves the skew-Hermitian form of the spectral theorem, reads the two imaginary eigenvalues and their sum and product from the trace and the determinant, computes the traceless part and its Lie algebra $\mathfrak{su}(2)$, states the negative definiteness of the trace form on it, and compares the complex skew-Hermitian picture with the real antisymmetric one. It assumes *The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents*, *Normal $2\times2$ Matrices and the Common Spectral Theorem* and *The Two Halves over $\mathbb{C}$: Hermitian and Skew-Hermitian at $n=2$*.

It keeps to the spectral statement; the exponential of the skew-Hermitian half belongs to the analysis of the two halves.

## The Skew-Hermitian Space

**The skew-Hermitian matrices are the imaginary multiples of the Hermitian ones, and they form a real space of dimension four.**

**Definition.** A matrix is **skew-Hermitian** when $X^{*}=-X$.

**Proposition.** The skew-Hermitian matrices form a real vector space of dimension four, and multiplication by $i$ carries it onto the Hermitian space.

**Proof.** If $X^{*}=-X$ then $(iX)^{*}=-iX^{*}=iX$, so $iX$ is Hermitian; the inverse map is the same multiplication by $-i$, and the two spaces have the same real dimension four.

**Corollary.** Every skew-Hermitian matrix is $iaI+ir\,\vec n\cdot\vec\sigma$ with $a\in\mathbb{R}$, $r\ge0$ and $\vec n\in S^{2}$.

**Proof.** It is $i$ times a Hermitian matrix, and the Hermitian matrices are $aI+r\,\vec n\cdot\vec\sigma$.

**Corollary.** The trace of a skew-Hermitian matrix is purely imaginary, and its diagonal entries are purely imaginary.

**Proof.** The diagonal of an anti-Hermitian matrix satisfies $\bar x=-x$, so each diagonal entry is imaginary and their sum is imaginary.

## The Spectral Theorem

**Theorem.** A skew-Hermitian matrix has purely imaginary eigenvalues, an orthonormal basis of eigenvectors, and the reconstruction

$$
X=i\mu_{+}\rho_{+}+i\mu_{-}\rho_{-},\qquad \mu_{\pm}=a\pm r\in\mathbb{R},
$$

with $\rho_{\pm}$ the Hermitian spectral projections of the direction $\vec n$.

**Proof.** The matrix $iX$ is Hermitian and is $iX=aI+r\,\vec n\cdot\vec\sigma$; its spectral projections and eigenvalues are those of *The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents*, and multiplying by $i$ multiplies the eigenvalues by $i$.

**Corollary.** The two eigenvalues are conjugates exactly when the trace vanishes.

**Proof.** The eigenvalues are $i(a+r)$ and $i(a-r)$; their sum is $2ia$, which vanishes exactly when $a=0$, and then the two eigenvalues are $\pm ir$.

**Corollary.** The squared modulus of each eigenvalue is $\mu_{\pm}^{2}$, and the sum of the squares of the eigenvalues is $2(a^{2}+r^{2})$.

**Proof.** The modulus of $i\mu$ is $|\mu|$, and the two squares add to $(a+r)^{2}+(a-r)^{2}=2(a^{2}+r^{2})$.

## The Trace and the Determinant

**Proposition.** The trace is $2ia$ and the determinant is $a^{2}+r^{2}$, so the determinant is real and nonnegative, and it vanishes exactly when $X=0$.

**Proof.** The determinant is the product $i(a+r)\cdot i(a-r)=-(a^{2}-r^{2})=r^{2}+a^{2}$ by the relation $i^{2}=-1$; and the trace is the sum $2ia$.

**Corollary.** A skew-Hermitian matrix is invertible exactly when it is nonzero, so the nonzero elements of the space are all invertible.

**Proof.** The determinant is $a^{2}+r^{2}$, which vanishes only at $a=r=0$, and that is the zero matrix.

**Corollary.** The trace of the square is $-\bigl((a+r)^{2}+(a-r)^{2}\bigr)\le0$, with equality exactly at the zero matrix.

**Proof.** The square has the eigenvalues $\mu_{\pm}^{2}i^{2}=-\mu_{\pm}^{2}$, and the trace is their sum.

## The Traceless Part and $\mathfrak{su}(2)$

**Theorem.** The traceless skew-Hermitian matrices form a real Lie algebra $\mathfrak{su}(2)$ of dimension three, with the basis $\tfrac{i}{2}\sigma_{1}$, $\tfrac{i}{2}\sigma_{2}$, $\tfrac{i}{2}\sigma_{3}$ and the brackets

$$
\Bigl[\tfrac{i}{2}\sigma_{j},\tfrac{i}{2}\sigma_{k}\Bigr]=-\epsilon_{jkl}\,\tfrac{i}{2}\sigma_{l}.
$$

**Proof.** The trace is real-linear and vanishes on the three displayed matrices, which are independent and traceless skew-Hermitian; the brackets follow from $\sigma_{j}\sigma_{k}=\delta_{jk}I+i\epsilon_{jkl}\sigma_{l}$ and the factor $i^{2}=-1$.

**Corollary.** The skew-Hermitian space is the direct sum $\mathfrak{u}(2)=\mathfrak{su}(2)\oplus\mathbb{R}\,iI$, and the second summand is the centre.

**Proof.** Every skew-Hermitian matrix is traceless plus a purely imaginary scalar, which is $i$ times a real multiple of the identity; the scalars commute with everything.

**Corollary.** The trace form is negative definite on the whole skew-Hermitian space, and $-\operatorname{tr}(X^{2})=2(a^{2}+r^{2})$.

**Proof.** Write $X=i(aI+r\,\vec n\cdot\vec\sigma)$, so that $iX$ is Hermitian with $(\vec n\cdot\vec\sigma)^{2}=I$ and $\operatorname{tr}(\vec n\cdot\vec\sigma)=0$. Then $X^{2}=-\bigl((a^{2}+r^{2})I+2ar\,\vec n\cdot\vec\sigma\bigr)$ and the trace is $-2(a^{2}+r^{2})$, which is negative unless $a=r=0$.

## The Real Antisymmetric Picture

**Proposition.** A real skew-symmetric $2\times2$ matrix is $c\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, it is skew-Hermitian, and its spectrum is $\{ic,-ic\}$.

**Proof.** A real skew-symmetric two-by-two matrix has the form $\begin{pmatrix}0&c\\-c&0\end{pmatrix}$; its square is $-c^{2}I$, so its eigenvalues are $\pm ic$, and it is skew-Hermitian because the transpose and the conjugate transpose agree on real matrices.

**Corollary.** The real antisymmetric line sits inside the skew-Hermitian space as the traceless part with a real direction, and the two imaginary eigenvalues are conjugate.

**Proof.** The real antisymmetric matrix has the trace zero, so $a=0$, and the eigenvalues $\pm ic$ are conjugates.

**Corollary.** The real antisymmetric line is one of the three directions of the traceless part, and the skew-Hermitian space has real dimension four against the one of that line.

**Proof.** The antisymmetric line is spanned by $\sigma_{2}$ multiplied by $i$, which is one of the three Pauli directions of the traceless part; the imaginary scalars add a fourth real dimension.

## The Imaginary Eigenvalues as Angles

**Proposition.** The two numbers $i\mu_{\pm}$ are exponents of the eigenvalues of the unitary matrix $\exp(X)$.

**Proof.** The spectral mapping of *The Spectrum of a $2\times2$ Matrix* gives $\exp(X)=e^{i\mu_{+}}\rho_{+}+e^{i\mu_{-}}\rho_{-}$, and the two exponentials are the eigenvalues of the unitary matrix.

**Corollary.** The two phases $e^{i\mu_{\pm}}$ are the two eigenvalues of a unitary matrix, and they differ by the angle $\mu_{+}-\mu_{-}=2r$.

**Proof.** The difference of the exponents is $2r$, and the two phases differ by the angle $2r$ on the unit circle.

**Corollary.** The skew-Hermitian matrix with $a=0$ has the eigenvalues $\pm ir$, and its exponential has the eigenvalues $e^{\pm ir}$, which are conjugate phases.

**Proof.** With $a=0$ the eigenvalues are $\pm ir$ and the exponentials are $e^{ir}$ and $e^{-ir}$.

## Summary

A skew-Hermitian $2\times2$ matrix is $iaI+ir\,\vec n\cdot\vec\sigma$, and its eigenvalues are $i(a+r)$ and $i(a-r)$: purely imaginary, symmetric about $ia$, conjugate exactly when the trace vanishes. The determinant is $a^{2}+r^{2}$, so every nonzero skew-Hermitian matrix is invertible, and the trace of the square is nonpositive.

The traceless part is $\mathfrak{su}(2)$, of real dimension three, with the brackets of the Pauli basis, and the whole space is $\mathfrak{su}(2)\oplus\mathbb{R}iI$ with the imaginary scalars in the centre. The trace form is negative definite on the traceless part and degenerate on the centre, and the real antisymmetric line is the real slice of this complex picture.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a$ | half the imaginary trace, $a=\operatorname{Im}\operatorname{tr}X/2$ |
| $r$ | the length of the traceless part |
| $\mu_{\pm}=a\pm r$ | the two imaginary eigenvalues divided by $i$ |
| $\mathfrak{su}(2)$ | the traceless skew-Hermitian matrices |
| $\rho_{\pm}$ | the Hermitian spectral projections |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for skew-Hermitian matrices and their spectra.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for $\mathfrak{su}(2)$, its brackets and its Killing form.
- [The Spectral Theorem: the Hermitian Case and the Sphere of Idempotents](the-spectral-theorem-the-hermitian-case-and-the-sphere-of-idempotents.html), for the Hermitian case that this article multiplies by $i$.
- [The Two Halves over $\mathbb{C}$: Hermitian and Skew-Hermitian at $n=2$](the-two-halves-over-c-hermitian-and-skew-hermitian-at-n-2.html), for the skew-Hermitian half as a real space.
- [The Killing Form of $\mathfrak{sl}_2$ and Its Three Signatures](the-killing-form-of-sl-2-and-its-three-signatures.html), for the negative definite form on $\mathfrak{su}(2)$.
