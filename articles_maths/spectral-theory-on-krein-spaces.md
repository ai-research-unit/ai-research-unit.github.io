# __Spectral Theory on Krein Spaces__

## Introduction

A $J$-self-adjoint operator on a Krein space need not have real spectrum, and the failure is not a pathology but the general situation: the fundamental symmetry $J$ has spectrum $\{\pm1\}$, so it is itself $J$-self-adjoint with a negative spectral point, and the negativity propagates to every indefinite space of positive rank. The spectral theory of a $J$-self-adjoint operator is therefore not the spectral theorem of Hilbert space with a change of notation; it is a theory in which the real axis carries the ordinary spectral data, the upper half-plane carries at most a finite amount of extra data, and the two are related by conjugation.

What survives from the Hilbert theory is the **symmetry**: the spectrum of a $J$-self-adjoint operator is invariant under conjugation, because $\bar T = JTJ^{-1}$ makes $T$ similar to its complex conjugate. What changes is the **semi-boundedness** of the real spectrum, which is lost, and the **definiteness** of the eigenvectors, which is replaced by a trichotomy of positive, negative and neutral eigenvectors. What is bounded is the exceptional set: in a Pontryagin space $\Pi_{\kappa}$ the non-real spectrum consists of at most $\kappa$ conjugate pairs counting algebraic multiplicities, and in a general Krein space the non-real spectrum consists of isolated eigenvalues with finite-dimensional root subspaces that can accumulate only on the real axis. For a bounded operator the theory is self-contained; the unbounded theory, with its own difficulties, is *Spectral Theory* (Part III).

This article fixes the conjugate symmetry of the spectrum, the trichotomy of real eigenvalues, the Pontryagin bound on the non-real spectrum, the accumulation statement, and the pointer to definitizability.

The indefinite adjoint, $J$-self-adjointness and the $J$-positive cone are *J-Self-Adjoint and J-Unitary Operators*; the space, the fundamental symmetry and the ranks are *Indefinite Inner Product Spaces*, *Krein Spaces* and *The Fundamental Symmetry*; the ordered structure is *The J-Positive Cone and the J-Order* and *Krein Algebras*; the definitizable case is *Definitizable Operators and the Krein–Naĭmark Theorem*; the unbounded case is Part III. Those are cited. The operator is bounded and $J$-self-adjoint on the Krein space $K$ with $\kappa = \kappa(K)$.

## The Spectrum of a J-Self-Adjoint Operator

**Definition.** The **spectrum** $\sigma(T)$ is the complement of the set of $\lambda$ with $\lambda - T$ boundedly invertible; the **point spectrum** $\sigma_{p}(T)$ is the set of eigenvalues, and the **root subspace** at $\lambda$ is $\bigcup_{n}\ker(\lambda - T)^{n}$.

**Proposition (resolvent identity).** If $T$ is $J$-self-adjoint then $\lambda - T$ is $J$-self-adjoint exactly for real $\lambda$, and $(\lambda - T)^{-1}$ is $J$-self-adjoint at every point of the resolvent that is real; at non-real $\lambda$ the resolvent is $J$-self-adjoint with parameter $\bar\lambda$.

**Proof.** $(\lambda - T)^{\dagger} = \bar\lambda - T^{\dagger} = \bar\lambda - T$, which equals $\lambda - T$ exactly for real $\lambda$; the resolvent of a $J$-self-adjoint operator at a real point is $J$-self-adjoint, and the general statement is the adjoint of $(\lambda - T)^{-1}$ computed at $\bar\lambda$.

**Theorem (conjugate symmetry).** The spectrum and the point spectrum of a $J$-self-adjoint operator are symmetric with respect to the real axis:

$$
\lambda\in\sigma(T) \iff \bar\lambda\in\sigma(T) , \qquad \lambda\in\sigma_{p}(T) \iff \bar\lambda\in\sigma_{p}(T) ,
$$

with equality of algebraic multiplicities, and the root subspace at $\bar\lambda$ is the $J$-orthogonal complement of the root subspace at $\lambda$ for the appropriate invariant pairing.

**Proof.** $T$ is similar to its complex conjugate, $\bar T = JTJ^{-1}$, so the spectrum is conjugation-invariant; multiplicities agree because the similarity is explicit; the pairing statement is the $J$-orthogonality of root subspaces at distinct conjugate eigenvalues.

## Real Eigenvalues and Their Types

**Definition.** A real eigenvalue $\lambda$ of $T$ is of **positive type** when $[x,x] > 0$ for every eigenvector $x$ at $\lambda$, of **negative type** when $[x,x] < 0$, and of **neutral type** when the eigenvectors at $\lambda$ form an isotropic set; the type is a property of the eigenvalue and the operator.

**Proposition (the type is a spectral invariant).** The set of eigenvalues of positive type and of negative type are invariant under $J$-unitary equivalence, and the algebraic multiplicity of an eigenvalue of definite type is bounded by the rank of the space in the corresponding sign.

**Proof.** $J$-unitary operators preserve the form and hence the signs of vectors; the multiplicity bound is the dimensionality of a positive or negative definite subspace of $K$.

**Remark (the real spectrum need not be semi-bounded).** For a Hilbert-self-adjoint operator the spectrum lies in an interval $[m,M]$ of the line. For a $J$-self-adjoint operator the real spectrum may be bounded below but not above, or exhibit both signs, because the operator $J$ itself has real spectrum $\{-1,+1\}$ with the two points of opposite type. The real spectrum is a union of sets of positive, negative and neutral type, and only its restriction to the definite parts behaves as in the Hilbert theory.

## The Pontryagin Case

**Theorem (finiteness of the non-real spectrum).** Let $K = \Pi_{\kappa}$ be a Pontryagin space and $T$ bounded and $J$-self-adjoint. Then the non-real spectrum of $T$ consists of finitely many conjugate pairs, and the total algebraic multiplicity of the non-real eigenvalues is at most $2\kappa$; every non-real eigenvalue has a root subspace that is a nondegenerate invariant subspace.

**Proof.** The invariant subspaces of a $J$-self-adjoint operator at non-real eigenvalues are of uniform type, and the geometry of $\Pi_{\kappa}$ bounds their total dimension by $2\kappa$; the conjugate pairing follows from the symmetry theorem.

**Corollary (the non-real part is spectrally isolated).** In $\Pi_{\kappa}$ the non-real spectrum is finite, its points are poles of the resolvent, and the restriction of $T$ to the direct sum of the root subspaces at the non-real eigenvalues is similar to a normal operator on a finite-dimensional Hilbert space.

**Proof.** The direct sum of the finitely many root subspaces is finite dimensional, invariant and nondegenerate, and on it the operator is $J$-self-adjoint with no real spectrum; a finite-dimensional $J$-self-adjoint operator with no real spectrum is similar to a normal operator.

**Proposition (the Pontryagin bound is sharp).** For every $\kappa$ there is a $J$-self-adjoint operator on $\Pi_{\kappa}$ with $\kappa$ conjugate pairs of non-real eigenvalues, namely the direct sum of $\kappa$ copies of the two-dimensional example $\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$ on a neutral pair of vectors.

**Proof.** The two-dimensional example is $J$-self-adjoint and non-real on $\mathbb{C}^{1,1}$; taking the direct sum of $\kappa$ copies saturates the bound of the theorem.

## Accumulation of the Non-Real Spectrum

**Theorem (the general Krein case).** For a bounded $J$-self-adjoint operator on an arbitrary Krein space, the non-real spectrum consists of eigenvalues whose root subspaces are finite dimensional, and every point of the non-real spectrum is isolated in the non-real part of the spectrum: the non-real spectrum can accumulate only on the real axis.

**Proof (sketch).** The root subspace at a non-real eigenvalue $\lambda$ is nondegenerate, finite dimensional and invariant, and the root subspaces at distinct non-real eigenvalues are $J$-orthogonal; the indefinite form therefore controls the total dimension of the non-real part, and a non-real eigenvalue has a neighbourhood meeting the non-real spectrum only finitely. The full statement is the theorem of Kreĭn and Langer on the spectral function of a $J$-self-adjoint operator.

**Corollary (the real axis carries the continuous spectrum).** The continuous spectrum, if any, lies on the real axis, and the non-real part of the spectrum is a purely point spectrum with finite-dimensional root subspaces.

**Proof.** The complement statement from the theorem, and the Hilbert-space fact that an isolated point of the spectrum of a bounded operator is an eigenvalue.

**Remark (the shape of the spectral theory).** The spectral theory of a $J$-self-adjoint operator is therefore layered: on the real axis the spectral data may be as complicated as in the Hilbert theory and in general is not semi-bounded; off the real axis the data is a finite (in $\Pi_{\kappa}$) or thin (in general) set of invariant subspaces with a conjugate pairing; and the two layers are coupled by the form. The tool that controls the coupling is definitizability, taken up in *Definitizable Operators and the Krein–Naĭmark Theorem*, where the spectral function of the operator is built.

## Worked Cases

### The Fundamental Symmetry

For $T = J$ the spectrum is $\{-1,+1\}$; the eigenvalue $+1$ is of positive type with multiplicity $\kappa_{+}$ and the eigenvalue $-1$ is of negative type with multiplicity $\kappa_{-}$; the non-real spectrum is empty and the structure is purely real.

### The Two-Dimensional Example

For $T = \left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$ on $\mathbb{C}^{1,1}$ the spectrum is $\{i,-i\}$, a conjugate pair, and the root subspaces are one dimensional; this saturates the Pontryagin bound for $\kappa = 1$ and shows that a $J$-self-adjoint operator with real rank one can have all of its spectrum non-real.

### A Hilbert-Self-Adjoint Operator

If $T$ commutes with $J$ and is Hilbert-self-adjoint, then $T$ is $J$-self-adjoint with real spectrum, all eigenvalues of definite type, and the spectral theory reduces to the Hilbert one; the indefinite theory is nontrivial exactly when $T$ fails to commute with $J$.

## Summary

The spectrum of a bounded **$J$-self-adjoint** operator on a Krein space is **symmetric with respect to the real axis**, $\lambda\in\sigma(T)\iff\bar\lambda\in\sigma(T)$ with equal multiplicities, because $T$ is similar to its complex conjugate, $\bar T = JTJ^{-1}$. Real eigenvalues carry a **type** — positive, negative or neutral according to the sign of $[x,x]$ on the eigenvectors — and the real spectrum need not be semi-bounded, since $J$ itself has the two real points of opposite type. The non-real spectrum is bounded by the indefiniteness: in a **Pontryagin space** $\Pi_{\kappa}$ the non-real spectrum consists of at most $\kappa$ conjugate pairs counting algebraic multiplicities, and the bound is sharp; in a general Krein space the non-real spectrum consists of **isolated eigenvalues with finite-dimensional root subspaces**, accumulating only on the real axis, so the continuous spectrum lies on the real line. The controlling tool for the coupling of the two layers is definitizability, which is *Definitizable Operators and the Krein–Naĭmark Theorem*; the indefinite adjoint and the $J$-self-adjoint operators are *J-Self-Adjoint and J-Unitary Operators*, the space and its ranks are *Krein Spaces* and *Indefinite Inner Product Spaces*, and the unbounded theory is Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma(T)$, $\sigma_{p}(T)$ | Spectrum and point spectrum |
| $\bar T = JTJ^{-1}$ | Similarity to the complex conjugate |
| $\lambda\in\sigma(T)\iff\bar\lambda\in\sigma(T)$ | Conjugate symmetry |
| Positive, negative, neutral type | Sign of $[x,x]$ on eigenvectors |
| $\Pi_{\kappa}$ | Pontryagin space of rank $\kappa$ |
| $\leq\kappa$ conjugate pairs | Bound on the non-real spectrum |
| Isolated root subspaces | Accumulation only on the real axis |
| $\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$ | Sharp example on $\mathbb{C}^{1,1}$ |

## Further Reading

- Mark G. Kreĭn and Heinz Langer, "On the spectral function of a self-adjoint operator in a space with indefinite metric", *Doklady Akademii Nauk SSSR* **211** (1973), 1027–1030, for the spectral function of a $J$-self-adjoint operator.
- Heinz Langer, "Spectral functions of definitizable operators in Krein spaces", in *Functional Analysis*, Lecture Notes in Mathematics 948 (Springer, 1982), for the structure of the spectrum.
- Tomas Ya. Azizov and I. S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for the Pontryagin case and the accumulation theorem.
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for the spectral theory of $J$-self-adjoint operators.
- Peter Jonas, "On the spectral theory of operators on Krein spaces", in *Operator Theory: Advances and Applications* (Birkhäuser), for the modern account.
