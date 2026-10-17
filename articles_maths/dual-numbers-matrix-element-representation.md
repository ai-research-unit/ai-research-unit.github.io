
# __Dual-Numbers Matrix Element Representation__

## Introduction

This article constructs the faithful two-dimensional matrix representation of the dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ and identifies the dual numbers with a commutative subalgebra of the $2\times2$ matrices. It follows *Dual-Numbers Algebra* for the conventions, *Dual-Numbers Norm and Invertibility* for the norm, and *Dual-Number Subspaces* for the two distinguished submodules. The comparison at the end records the difference from the complex algebra, whose $2\times2$ real representation is the non-degenerate analogue.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Throughout, $R$ is a commutative ring with identity in which $2$ is invertible; the geometric specialisation is $R = \mathbb{R}$, and then the algebra is written $\mathbb{D}'$. A general dual number is

$$
Q = q + \varepsilon q', \qquad q, q' \in R,
$$

with $q = \operatorname{Re} Q$, $q' = \operatorname{Inf} Q$, dual conjugation $\bar Q = q - \varepsilon q'$, norm $\langle Q\rangle = Q\bar Q = q^2$, maximal ideal $\mathrm{M} = (\varepsilon)$, real submodule $R_{\mathbb{D}'}$ and infinitesimal submodule $\varepsilon R_{\mathbb{D}'}$.

## The Representation

### Definition

**Definition.** The **matrix representation** of $\mathbb{D}'_R$ is the isomorphism written $\mathsf{M}_2$. It converts a dual number into a $2 \times 2$ matrix over $R$,

$$
\mathsf{M}_2 : \mathbb{D}'_R \longrightarrow M_2(R),
$$

and it is fixed by its values on the basis, the rest following by $R$-linearity. The unit and the infinitesimal element are assigned the matrices

$$
\mathsf{M}_2(1) = I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad \mathsf{M}_2(\varepsilon) = J = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix},
$$

so that on a general dual number $Q = q + \varepsilon q'$,

$$
\mathsf{M}_2(q + \varepsilon q') = \begin{pmatrix} q & q' \\ 0 & q \end{pmatrix}.
$$

The matrix $\mathsf{M}_2(Q)$ is the **matrix of** $Q$; its diagonal entry is the real part and its strictly upper-triangular entry is the infinitesimal part.

**The check.** The assignment is the right one because the two matrices multiply as the two units do. The square of the infinitesimal image vanishes,

$$
\mathsf{M}_2(\varepsilon)^2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}^2 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix} = \mathsf{M}_2(\varepsilon^2),
$$

reproducing $\varepsilon^2 = 0$, and $\mathsf{M}_2(1)^2 = \mathsf{M}_2(1)$ reproduces $1^2 = 1$; those relations are the whole multiplication table of $\mathbb{D}'_R$, so the correspondence of bases is an isomorphism of algebras and not a formal analogy.

### Linearity and the Identity

$\mathsf{M}_2$ is $R$-linear by construction, and it preserves the identity:

$$
\mathsf{M}_2(Q_1 + Q_2) = \mathsf{M}_2(Q_1) + \mathsf{M}_2(Q_2), \qquad \mathsf{M}_2(\lambda Q_1) = \lambda\,\mathsf{M}_2(Q_1), \qquad \mathsf{M}_2(1) = I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.
$$

## The Representation Is an Algebra Homomorphism

### Multiplicativity

**Theorem.** $\mathsf{M}_2$ is a unital algebra homomorphism:

$$
\mathsf{M}_2(Q_1 Q_2) = \mathsf{M}_2(Q_1)\,\mathsf{M}_2(Q_2) \qquad \text{for all } Q_1, Q_2 \in \mathbb{D}'_R.
$$

**Proof.** With $Q_1 = q_1 + \varepsilon q'_1$ and $Q_2 = q_2 + \varepsilon q'_2,$

$$
\mathsf{M}_2(Q_1)\mathsf{M}_2(Q_2) = \begin{pmatrix} q_1 & q'_1 \\ 0 & q_1 \end{pmatrix}\begin{pmatrix} q_2 & q'_2 \\ 0 & q_2 \end{pmatrix} = \begin{pmatrix} q_1 q_2 & q_1 q'_2 + q'_1 q_2 \\ 0 & q_1 q_2 \end{pmatrix} = \mathsf{M}_2(Q_1 Q_2),
$$

using $Q_1 Q_2 = q_1 q_2 + (q_1 q'_2 + q'_1 q_2)\varepsilon$.

### Injectivity

**Theorem.** $\mathsf{M}_2$ is injective, and hence a ring isomorphism onto its image.

**Proof.** If $\mathsf{M}_2(Q) = 0$ then $q = 0$ and $q' = 0$, so $Q = 0$.

So $\mathbb{D}'_R$ is isomorphic to the subalgebra $\mathsf{M}_2(\mathbb{D}'_R) \subseteq M_2(R)$, and the representation is faithful. The algebra is thus a **concrete** algebra of matrices, and everything proved about $\mathbb{D}'_R$ can be read in $M_2(R)$.

### The Image: The Toeplitz Subalgebra

**Definition.** A matrix $\begin{pmatrix} a & b \\ 0 & c \end{pmatrix}$ is **upper triangular Toeplitz** if its diagonal entries are equal, $a = c$.

**Theorem.** The image $\mathsf{M}_2(\mathbb{D}'_R)$ is exactly the subalgebra of upper-triangular Toeplitz matrices,

$$
\mathsf{M}_2(\mathbb{D}'_R) = \left\{\begin{pmatrix} q & q' \\ 0 & q \end{pmatrix} : q, q' \in R\right\}.
$$

It is a commutative unital subalgebra of $M_2(R)$, of $R$-rank two, spanned by $I$ and the nilpotent $E = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.

**Proof.** The displayed set is the image by definition; it is closed under addition and multiplication, since

$$
\begin{pmatrix} q_1 & q'_1 \\ 0 & q_1 \end{pmatrix}\begin{pmatrix} q_2 & q'_2 \\ 0 & q_2 \end{pmatrix} = \begin{pmatrix} q_1 q_2 & q_1 q'_2+q'_1 q_2 \\ 0 & q_1 q_2 \end{pmatrix},
$$

which is again upper-triangular Toeplitz; the unit is $I$; and $E^2 = 0$.

### The Nilpotent

**Proposition.** $\mathsf{M}_2(\varepsilon) = E$ and every element of the image is $qI + q'E$; the algebra is the algebra of truncated polynomials in $E$ at $E^2 = 0$.

**Proof.** $\mathsf{M}_2(\varepsilon) = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = E$, and $\mathsf{M}_2(q + \varepsilon q') = qI + q'E$ by linearity.

## The Trace and the Determinant

**Theorem.** For $Q = q + \varepsilon q',$

$$
\operatorname{tr}\mathsf{M}_2(Q) = 2q, \qquad \det\mathsf{M}_2(Q) = q^2 = \langle Q\rangle, \qquad \chi_{\mathsf{M}_2(Q)}(\lambda) = (\lambda - q)^2.
$$

**Proof.** The trace is the sum of the diagonal entries $q + q = 2q$; the determinant is $q^2 - 0 = q^2$; the characteristic polynomial is the product of the diagonal entries of $\lambda I - \mathsf{M}_2(Q)$, namely $(\lambda - q)^2$, the matrix being triangular.

**Corollary.** The determinant is the norm and is multiplicative, $\det\mathsf{M}_2(Q_1 Q_2) = \det\mathsf{M}_2(Q_1)\det\mathsf{M}_2(Q_2)$, which is the multiplicativity of $\langle\cdot\rangle$ read in the matrix algebra; the trace is twice the real part.

**Corollary.** The eigenvalues of $\mathsf{M}_2(Q)$ are both equal to $q$, the real part. The matrix is diagonalizable only when $q' = 0$, in which case it is the scalar matrix $qI$; otherwise it is a nondiagonalizable Jordan block.

**Remark.** The determinant vanishes if and only if the eigenvalues vanish, that is if and only if $q = 0$; so $\mathsf{M}_2(Q)$ is invertible if and only if $q$ is a unit of $R$, recovering the criterion of *Dual-Numbers Norm and Invertibility* from the matrix side.

**Corollary (the polar form).** For $Q_1, Q_2 \in \mathbb{D}'_R$ the polar form of the norm is read from the trace and the determinant:

$$
B(Q_1, Q_2) = \tfrac{1}{2}\bigl(\operatorname{tr}\mathsf{M}_2(Q_1)\operatorname{tr}\mathsf{M}_2(Q_2) - \operatorname{tr}(\mathsf{M}_2(Q_1)\mathsf{M}_2(Q_2))\bigr).
$$

**Proof.** The identity $\det(X + Y) - \det X - \det Y = \operatorname{tr}(X)\operatorname{tr}(Y) - \operatorname{tr}(XY)$ holds for all $2\times2$ matrices; substituting $\operatorname{tr}\mathsf{M}_2(Q_1) = 2q_1$, $\operatorname{tr}\mathsf{M}_2(Q_2) = 2q_2$ and $\operatorname{tr}(\mathsf{M}_2(Q_1)\mathsf{M}_2(Q_2)) = \operatorname{tr}\mathsf{M}_2(Q_1Q_2) = 2q_1q_2$ gives $\tfrac{1}{2}(4q_1q_2 - 2q_1q_2) = q_1q_2 = B(Q_1,Q_2)$.

## The Image of the Distinguished Submodules

**Theorem.** The two distinguished submodules map onto the scalar and the strictly upper-triangular matrices:

$$
\mathsf{M}_2(R_{\mathbb{D}'}) = \left\{\begin{pmatrix} q & 0 \\ 0 & q \end{pmatrix} : q \in R\right\} = R\,I, \qquad \mathsf{M}_2(\varepsilon R_{\mathbb{D}'}) = \left\{\begin{pmatrix} 0 & q' \\ 0 & 0 \end{pmatrix} : q' \in R\right\} = R\,E.
$$

**Proof.** An element of $R_{\mathbb{D}'}$ is $q$, mapping to $qI$; an element of $\varepsilon R_{\mathbb{D}'}$ is $\varepsilon q'$, mapping to $q'E$.

**Corollary.** The matrix model carries the direct-sum decomposition to the decomposition $M_2(R) \supseteq R\,I \oplus R\,E$, with $\mathsf{M}_2(R_{\mathbb{D}'}) \cap \mathsf{M}_2(\varepsilon R_{\mathbb{D}'}) = 0$ and sum $\mathsf{M}_2(\mathbb{D}'_R)$.

**Corollary.** The maximal ideal corresponds to the nilpotent line $R\,E$, and the zero divisors of *Dual-Numbers Zero Divisors* correspond to the nonzero scalar multiples of $E$.

## The Conjugations in Matrix Form

**Theorem.** Dual conjugation becomes the conjugation by the diagonal involution $J = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$:

$$
\mathsf{M}_2(\bar Q) = J\,\mathsf{M}_2(Q)\,J^{-1} = J\,\mathsf{M}_2(Q)\,J = \begin{pmatrix} q & -q' \\ 0 & q \end{pmatrix}.
$$

**Proof.** $J^2 = I$ and $J\begin{pmatrix} q & q' \\ 0 & q \end{pmatrix}J = \begin{pmatrix} q & -q' \\ 0 & q \end{pmatrix}$.

**Corollary.** The real submodule is the fixed subalgebra of the inner involution $\operatorname{Ad}_J$, and the infinitesimal submodule is the $(-1)$-eigenspace; in matrix form these are the scalar matrices and the strictly upper-triangular matrices.

**Remark (the transpose and the regular representation).** The multiplication convention of the matrix model puts the infinitesimal part in the upper-right corner. The regular representation of *Dual-Numbers Element Representations* and *Shears and Parabolic Rotations*, computed in the basis $(1, \varepsilon)$ of left multiplication, instead puts it in the lower-left corner:

$$
[u] = \begin{pmatrix} q & 0 \\ q' & q \end{pmatrix}, \qquad u = q + \varepsilon q'.
$$

The two conventions are related by transpose, $[u] = \mathsf{M}_2(u)^{\mathsf{T}}$, and the transpose reverses the order of multiplication, so $[u][v] = \mathsf{M}_2(vu)^{\mathsf{T}} = \mathsf{M}_2(uv)^{\mathsf{T}}$ because the algebra is commutative. Both are faithful representations of $\mathbb{D}'_R$ by $2\times2$ matrices; the classification of representations in *Dual-Numbers Element Representations* shows that this is essentially the only faithful two-dimensional one, up to the choice of basis in which the nilpotent is a Jordan block.

## Structural Consequences

### Commutativity and the Centre

The image is commutative, so $\mathsf{M}_2$ cannot be surjective onto $M_2(R)$ unless the base ring is the zero ring; the image is a proper subalgebra of dimension two inside the four-dimensional $M_2(R)$. The centre of the image is the whole image, and the centralizer of a non-scalar element $qI + q'E$, $q' \neq 0$, is exactly the image; the centralizer of a scalar matrix is all of $M_2(R)$.

### Units

An upper-triangular Toeplitz matrix $qI + q'E$ is invertible if and only if $q$ is a unit of $R$, and then

$$
(qI + q'E)^{-1} = q^{-1}I - q^{-2}q'\,E = \begin{pmatrix} q^{-1} & -q^{-2}q' \\ 0 & q^{-1} \end{pmatrix},
$$

matching $\mathsf{M}_2(Q^{-1})$ for $Q = q + \varepsilon q'$. The unit group of the image is the set of matrices $qI + q'E$ with $q \in R^\times$, whose shear subgroup is $I + R\,E = \{I + q'E\} \cong (R,+)$.

### Automorphisms in the Matrix Model

**Proposition.** The automorphism $\varphi_c(\varepsilon) = \varepsilon c$ with $c \in R^\times$ of *Dual-Numbers Automorphisms and Derivations* is realised by conjugation with the diagonal matrix $\operatorname{diag}(c, 1)$:

$$
\operatorname{diag}(c, 1)\,\mathsf{M}_2(Q)\,\operatorname{diag}(c, 1)^{-1} = \begin{pmatrix} q & c q' \\ 0 & q \end{pmatrix} = \mathsf{M}_2\bigl(\varphi_c(Q)\bigr).
$$

**Proof.** $\operatorname{diag}(c,1)^{-1} = \operatorname{diag}(c^{-1},1)$, and multiplying the three matrices gives $\begin{pmatrix} q & c q' \\ 0 & q \end{pmatrix}$.

So $\operatorname{Aut}_R(\mathbb{D}'_R)$ is the image of the diagonal subgroup of $GL_2(R)$ acting by conjugation: a diagonal element $\operatorname{diag}(c, d)$ rescales the $E$-coordinate by $c d^{-1}$, and the induced homomorphism $(c,d) \mapsto c d^{-1}$ onto $R^\times$ is surjective with kernel the scalar matrices $\operatorname{diag}(c, c)$.

## Comparison with the $2\times2$ Representation of $\mathbb{C}$

### The Complex Case

The complex algebra $\mathbb{C}$ has the faithful $2\times2$ real representation

$$
\Psi(a + b i) = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}, \qquad i = \sqrt{-1},
$$

with determinant $a^2 + b^2$, the non-degenerate norm of $\mathbb{C}$; the image is the subalgebra of rotation-scaling matrices inside $M_2(\mathbb{R})$, of real dimension two.

### The Dual Case

The dual-number model is the analogue in which the imaginary part is replaced by the nilpotent $\varepsilon$: the image is the commutative Toeplitz subalgebra, the determinant is the degenerate norm $q^2$, and the missing imaginary part of the coefficients is exactly the lost second coordinate. Both models are two-real-dimensional commutative subalgebras of $M_2(\mathbb{R})$. The complex image is the rotation-scaling algebra $RI \oplus RJ$ with $J^2 = -I$, and the dual image is $RI \oplus RE$ with $E^2 = 0$: the complex algebra needs a matrix with negative square, and the dual algebra does not.

## Worked Examples

**Example (the homomorphism property).** For $Q_1 = 2 + 3\varepsilon$ and $Q_2 = 4 + 5\varepsilon$,

$$
\mathsf{M}_2(Q_1)\mathsf{M}_2(Q_2) = \begin{pmatrix} 2 & 3 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 4 & 5 \\ 0 & 4 \end{pmatrix} = \begin{pmatrix} 8 & 22 \\ 0 & 8 \end{pmatrix} = \mathsf{M}_2(Q_1 Q_2),
$$

matching $Q_1 Q_2 = 8 + 22\varepsilon$; moreover $\det\mathsf{M}_2(Q_1) = 4 = \langle Q_1\rangle$ and $\det\mathsf{M}_2(Q_1 Q_2) = 64 = \langle Q_1\rangle\langle Q_2\rangle$.

**Example (the shear subgroup).** For $s \in R$ the image of $1 + s\varepsilon$ is the unipotent matrix

$$
\mathsf{M}_2(1 + s\varepsilon) = I + sE = \begin{pmatrix} 1 & s \\ 0 & 1 \end{pmatrix}, \qquad \mathsf{M}_2(1 + s\varepsilon)\mathsf{M}_2(1 + t\varepsilon) = \mathsf{M}_2\bigl(1 + (s+t)\varepsilon\bigr),
$$

so these matrices form the shear subgroup $I + R\,E$, with $\mathsf{M}_2(1 + s\varepsilon)^{-1} = \mathsf{M}_2(1 - s\varepsilon)$. For instance $\mathsf{M}_2(1 + 3\varepsilon)\mathsf{M}_2(1 + 5\varepsilon) = \mathsf{M}_2(1 + 8\varepsilon)$.

## Summary

The dual-number algebra has the faithful unital $R$-algebra representation

$$
\mathsf{M}_2(q + \varepsilon q') = \begin{pmatrix} q & q' \\ 0 & q \end{pmatrix}, \qquad \mathsf{M}_2(Q_1 Q_2) = \mathsf{M}_2(Q_1)\mathsf{M}_2(Q_2), \qquad \ker\mathsf{M}_2 = 0,
$$

identifying $\mathbb{D}'_R$ with the commutative subalgebra of upper-triangular Toeplitz matrices, spanned by $I$ and the nilpotent $E = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ with $E^2 = 0$. The trace is $2q$, twice the real part; the determinant is $q^2 = \langle Q\rangle$, the degenerate norm; and the characteristic polynomial is $(\lambda - q)^2$, exhibiting the single repeated eigenvalue equal to the real part. The distinguished submodules map to the scalar matrices $R\,I$ and the strictly upper-triangular matrices $R\,E$; dual conjugation is the inner involution by $J = \operatorname{diag}(1,-1)$; and the maximal ideal is the nilpotent line $R\,E$. The regular representation of the companion articles is the transpose convention, with the infinitesimal part in the lower-left corner. the shear subgroup is $I + R\,E$, with $\mathsf{M}_2(1 + s\varepsilon)\mathsf{M}_2(1 + t\varepsilon) = \mathsf{M}_2(1 + (s+t)\varepsilon)$; the algebra automorphisms $\varphi_c$ are realised by conjugation with the diagonal matrices $\operatorname{diag}(c, 1)$; and the polar form is recovered from the trace and the determinant by $\langle Q_1, Q_2\rangle = \tfrac{1}{2}(\operatorname{tr}\mathsf{M}_2(Q_1)\operatorname{tr}\mathsf{M}_2(Q_2) - \operatorname{tr}(\mathsf{M}_2(Q_1)\mathsf{M}_2(Q_2)))$. Compared with the complex algebra, $\mathbb{C}$ has a faithful $2\times2$ real representation with determinant the non-degenerate form $a^2 + b^2$, while the dual algebra has a faithful $2\times2$ representation over $R$ with determinant the degenerate form $q^2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra over $R$; $\varepsilon^2 = 0$ |
| $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$ | Dual-number algebra over $\mathbb{R}$ |
| $Q = q + \varepsilon q'$ | General dual number |
| $q = \operatorname{Re} Q$, $q' = \operatorname{Inf} Q$ | Real and infinitesimal parts |
| $\bar{Q} = q - \varepsilon q'$ | Dual conjugation |
| $\langle Q\rangle = q^2$ | Norm, equal to $\det\mathsf{M}_2(Q)$ |
| $\mathsf{M}_2(q + \varepsilon q') = \begin{pmatrix} q & q' \\ 0 & q \end{pmatrix}$ | Faithful matrix representation |
| $E = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \mathsf{M}_2(\varepsilon)$ | Nilpotent Jordan block, $E^2 = 0$ |
| $J = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ | Involution realizing dual conjugation |
| $\varphi_c$ | Automorphism $\varepsilon \mapsto c\varepsilon$, conjugation by $\operatorname{diag}(c, 1)$ |
| $B(Q_1,Q_2) = q_1q_2$ | Polar form, $\tfrac{1}{2}(\operatorname{tr}\mathsf{M}_2(Q_1)\operatorname{tr}\mathsf{M}_2(Q_2) - \operatorname{tr}(\mathsf{M}_2(Q_1)\mathsf{M}_2(Q_2)))$ |
| $[u] = \begin{pmatrix} q & 0 \\ q' & q \end{pmatrix} = \mathsf{M}_2(u)^{\mathsf{T}}$ | Regular representation, transpose convention |
| $I = \mathsf{M}_2(1)$ | Identity matrix |
| $\mathbb{C}$ | Complex algebra, faithful $2\times2$ real representation |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, Cambridge, 2013), for triangular Toeplitz matrices, their spectra, and the matrix functions of a nilpotent.
- F. R. Gantmacher, *The Theory of Matrices* (Chelsea, New York, 1959), for Jordan blocks, the centralizer of a nongeneric matrix, and the functional calculus of a nilpotent.
- Israel N. Herstein, *Noncommutative Rings* (Mathematical Association of America, Washington, 1968), for the matrix representation of division algebras and the dimension obstruction to faithfulness.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation* (SIAM, Philadelphia, 2008), for the triangular matrix model of the nilpotent extension in computation.
