
# __Dual-Numbers Matrix Representation__

## Introduction

This article constructs the faithful two-dimensional matrix representation of the dual-number algebra $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ and identifies the dual numbers with a commutative subalgebra of the $2\times2$ matrices. It follows *Dual-Numbers Algebra* for the conventions, *Dual-Numbers Norm and Invertibility* for the norm form, and *Dual-Number Subspaces* for the two distinguished submodules. Its structural model is *Biquaternion 2×2 Matrix Representation*, in which the biquaternion algebra is identified with the full matrix algebra $M_2(\mathbb{C})$; the dual algebra is identified only with a commutative subalgebra, and the comparison at the end records the difference.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Throughout, $R$ is a commutative ring with identity in which $2$ is invertible; the geometric specialisation is $R = \mathbb{R}$, and then the algebra is written $\mathbb{D}'$. A general dual number is

$$
Z = a + \varepsilon b, \qquad a, b \in R,
$$

with $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$, dual conjugation $\bar{Z} = a - \varepsilon b$, norm form $N(Z) = Z\bar{Z} = a^2$, maximal ideal $\mathfrak{m} = (\varepsilon)$, real submodule $R_{\mathbb{D}'}$ and infinitesimal submodule $\varepsilon R_{\mathbb{D}'}$.

## The Representation

### Definition

**Definition.** The **matrix representation** of $\mathbb{D}'_R$ is the map

$$
\Phi : \mathbb{D}'_R \longrightarrow M_2(R), \qquad \Phi(a + \varepsilon b) = \begin{pmatrix} a & b \\ 0 & a \end{pmatrix}.
$$

The matrix $\Phi(Z)$ is the **matrix of** $Z$; its diagonal entry is the real part and its strictly upper-triangular entry is the infinitesimal part.

### Linearity and the Identity

$\Phi$ is $R$-linear by construction, and it preserves the identity:

$$
\Phi(Z + W) = \Phi(Z) + \Phi(W), \qquad \Phi(\lambda Z) = \lambda\,\Phi(Z), \qquad \Phi(1) = I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.
$$

## The Representation Is an Algebra Homomorphism

### Multiplicativity

**Theorem.** $\Phi$ is a unital algebra homomorphism:

$$
\Phi(zw) = \Phi(Z)\,\Phi(W) \qquad \text{for all } Z, W \in \mathbb{D}'_R.
$$

**Proof.** With $Z = a + \varepsilon b$ and $W = c + \varepsilon d$,

$$
\Phi(Z)\Phi(W) = \begin{pmatrix} a & b \\ 0 & a \end{pmatrix}\begin{pmatrix} c & d \\ 0 & c \end{pmatrix} = \begin{pmatrix} a c & a d + b c \\ 0 & a c \end{pmatrix} = \Phi(zw),
$$

using $zw = a c + (a d + b c)\varepsilon$. $\square$

### Injectivity

**Theorem.** $\Phi$ is injective, and hence a ring isomorphism onto its image.

**Proof.** If $\Phi(Z) = 0$ then $a = 0$ and $b = 0$, so $Z = 0$. $\square$

So $\mathbb{D}'_R$ is isomorphic to the subalgebra $\Phi(\mathbb{D}'_R) \subseteq M_2(R)$, and the representation is faithful. The algebra is thus a **concrete** algebra of matrices, and everything proved about $\mathbb{D}'_R$ can be read in $M_2(R)$.

### The Image: The Toeplitz Subalgebra

**Definition.** A matrix $\begin{pmatrix} a & b \\ 0 & c \end{pmatrix}$ is **upper triangular Toeplitz** if its diagonal entries are equal, $a = c$.

**Theorem.** The image $\Phi(\mathbb{D}'_R)$ is exactly the subalgebra of upper-triangular Toeplitz matrices,

$$
\Phi(\mathbb{D}'_R) = \left\{\begin{pmatrix} a & b \\ 0 & a \end{pmatrix} : a, b \in R\right\}.
$$

It is a commutative unital subalgebra of $M_2(R)$, of $R$-rank two, spanned by $I$ and the nilpotent $E = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.

**Proof.** The displayed set is the image by definition; it is closed under addition and multiplication, since

$$
\begin{pmatrix} a & b \\ 0 & a \end{pmatrix}\begin{pmatrix} c & d \\ 0 & c \end{pmatrix} = \begin{pmatrix} a c & a d+b c \\ 0 & a c \end{pmatrix},
$$

which is again upper-triangular Toeplitz; the unit is $I$; and $E^2 = 0$. $\square$

### The Nilpotent

**Proposition.** $\Phi(\varepsilon) = E$ and every element of the image is $aI + bE$; the algebra is the algebra of truncated polynomials in $E$ at $E^2 = 0$.

**Proof.** $\Phi(\varepsilon) = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = E$, and $\Phi(a + \varepsilon b) = aI + bE$ by linearity. $\square$

## The Trace and the Determinant

**Theorem.** For $Z = a + \varepsilon b$,

$$
\operatorname{tr}\Phi(Z) = 2a, \qquad \det\Phi(Z) = a^2 = N(Z), \qquad \chi_{\Phi(Z)}(\lambda) = (\lambda - a)^2.
$$

**Proof.** The trace is the sum of the diagonal entries $a + a = 2a$; the determinant is $a^2 - 0 = a^2$; the characteristic polynomial is the product of the diagonal entries of $\lambda I - \Phi(Z)$, namely $(\lambda - a)^2$, the matrix being triangular. $\square$

**Corollary.** The determinant is the norm form and is multiplicative, $\det\Phi(zw) = \det\Phi(Z)\det\Phi(W)$, which is the multiplicativity of $N$ read in the matrix algebra; the trace is twice the real part.

**Corollary.** The eigenvalues of $\Phi(Z)$ are both equal to $a$, the real part. The matrix is diagonalizable only when $b = 0$, in which case it is the scalar matrix $aI$; otherwise it is a nondiagonalizable Jordan block.

**Remark.** The determinant vanishes if and only if the eigenvalues vanish, that is if and only if $a = 0$; so $\Phi(Z)$ is invertible if and only if $a$ is a unit of $R$, recovering the criterion of *Dual-Numbers Norm and Invertibility* from the matrix side.

**Corollary (the polar form).** For $Z, W \in \mathbb{D}'_R$ the polar form of the norm is read from the trace and the determinant:

$$
B(Z, W) = \tfrac{1}{2}\bigl(\operatorname{tr}\Phi(Z)\operatorname{tr}\Phi(W) - \operatorname{tr}(\Phi(Z)\Phi(W))\bigr).
$$

**Proof.** The identity $\det(X + Y) - \det X - \det Y = \operatorname{tr}(X)\operatorname{tr}(Y) - \operatorname{tr}(XY)$ holds for all $2\times2$ matrices; substituting $\operatorname{tr}\Phi(Z) = 2a$, $\operatorname{tr}\Phi(W) = 2c$ and $\operatorname{tr}(\Phi(Z)\Phi(W)) = \operatorname{tr}\Phi(ZW) = 2ac$ gives $\tfrac{1}{2}(4ac - 2ac) = ac = B(Z,W)$. $\square$

## The Image of the Distinguished Submodules

**Theorem.** The two distinguished submodules map onto the scalar and the strictly upper-triangular matrices:

$$
\Phi(R_{\mathbb{D}'}) = \left\{\begin{pmatrix} a & 0 \\ 0 & a \end{pmatrix} : a \in R\right\} = R\,I, \qquad \Phi(\varepsilon R_{\mathbb{D}'}) = \left\{\begin{pmatrix} 0 & b \\ 0 & 0 \end{pmatrix} : b \in R\right\} = R\,E.
$$

**Proof.** An element of $R_{\mathbb{D}'}$ is $a$, mapping to $aI$; an element of $\varepsilon R_{\mathbb{D}'}$ is $\varepsilon b$, mapping to $bE$. $\square$

**Corollary.** The matrix model carries the direct-sum decomposition to the decomposition $M_2(R) \supseteq R\,I \oplus R\,E$, with $\Phi(R_{\mathbb{D}'}) \cap \Phi(\varepsilon R_{\mathbb{D}'}) = 0$ and sum $\Phi(\mathbb{D}'_R)$.

**Corollary.** The maximal ideal corresponds to the nilpotent line $R\,E$, and the zero divisors of *Dual-Numbers Zero Divisors* correspond to the nonzero scalar multiples of $E$.

## The Conjugations in Matrix Form

**Theorem.** Dual conjugation becomes the conjugation by the diagonal involution $J = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$:

$$
\Phi(\bar{Z}) = J\,\Phi(Z)\,J^{-1} = J\,\Phi(Z)\,J = \begin{pmatrix} a & -b \\ 0 & a \end{pmatrix}.
$$

**Proof.** $J^2 = I$ and $J\begin{pmatrix} a & b \\ 0 & a \end{pmatrix}J = \begin{pmatrix} a & -b \\ 0 & a \end{pmatrix}$. $\square$

**Corollary.** The real submodule is the fixed subalgebra of the inner involution $\operatorname{Ad}_J$, and the infinitesimal submodule is the $(-1)$-eigenspace; in matrix form these are the scalar matrices and the strictly upper-triangular matrices.

**Remark (the transpose and the regular representation).** The multiplication convention of the matrix model puts the infinitesimal part in the upper-right corner. The regular representation of *Dual-Numbers Representations* and *Shears and Parabolic Rotations*, computed in the basis $(1, \varepsilon)$ of left multiplication, instead puts it in the lower-left corner:

$$
[u] = \begin{pmatrix} a & 0 \\ b & a \end{pmatrix}, \qquad u = a + \varepsilon b.
$$

The two conventions are related by transpose, $[u] = \Phi(u)^{\mathsf{T}}$, and the transpose reverses the order of multiplication, so $[u][v] = \Phi(vu)^{\mathsf{T}} = \Phi(uv)^{\mathsf{T}}$ because the algebra is commutative. Both are faithful representations of $\mathbb{D}'_R$ by $2\times2$ matrices; the classification of representations in *Dual-Numbers Representations* shows that this is essentially the only faithful two-dimensional one, up to the choice of basis in which the nilpotent is a Jordan block.

## Structural Consequences

### Commutativity and the Center

The image is commutative, so $\Phi$ cannot be surjective onto $M_2(R)$ unless the base ring is the zero ring; the image is a proper subalgebra of dimension two inside the four-dimensional $M_2(R)$. The center of the image is the whole image, and the centralizer of a non-scalar element $aI + bE$, $b \neq 0$, is exactly the image; the centralizer of a scalar matrix is all of $M_2(R)$.

### Units

An upper-triangular Toeplitz matrix $aI + bE$ is invertible if and only if $a$ is a unit of $R$, and then

$$
(aI + bE)^{-1} = a^{-1}I - a^{-2}b\,E = \begin{pmatrix} a^{-1} & -a^{-2}b \\ 0 & a^{-1} \end{pmatrix},
$$

matching $\Phi(Z^{-1})$ for $Z = a + \varepsilon b$. The unit group of the image is the set of matrices $aI + bE$ with $a \in R^\times$, whose shear subgroup is $I + R\,E = \{I + bE\} \cong (R,+)$.

### Automorphisms in the Matrix Model

**Proposition.** The automorphism $\varphi_c(\varepsilon) = \varepsilon c$ with $c \in R^\times$ of *Dual-Numbers Automorphisms and Derivations* is realised by conjugation with the diagonal matrix $\operatorname{diag}(c, 1)$:

$$
\operatorname{diag}(c, 1)\,\Phi(Z)\,\operatorname{diag}(c, 1)^{-1} = \begin{pmatrix} a & c b \\ 0 & a \end{pmatrix} = \Phi\bigl(\varphi_c(Z)\bigr).
$$

**Proof.** $\operatorname{diag}(c,1)^{-1} = \operatorname{diag}(c^{-1},1)$, and multiplying the three matrices gives $\begin{pmatrix} a & c b \\ 0 & a \end{pmatrix}$. $\square$

So $\operatorname{Aut}_R(\mathbb{D}'_R)$ is the image of the diagonal subgroup of $GL_2(R)$ acting by conjugation: a diagonal element $\operatorname{diag}(c, d)$ rescales the $E$-coordinate by $c d^{-1}$, and the induced homomorphism $(c,d) \mapsto c d^{-1}$ onto $R^\times$ is surjective with kernel the scalar matrices $\operatorname{diag}(c, c)$.

## Comparison with the $2\times2$ Representation of $\mathbb{H}$ and the Absence for $\mathbb{H}_{\mathbb{D}}$

### The Quaternion Case

The quaternion algebra $\mathbb{H}$ has the faithful $2\times2$ representation over $\mathbb{C}$

$$
\Psi(a + \varepsilon b + ce_2 + de_3) = \begin{pmatrix} a + i b & c + i d \\ -c + i d & a - i b \end{pmatrix}, \qquad i = \sqrt{-1},
$$

with determinant $a^2 + b^2 + c^2 + d^2$, the non-degenerate norm form of $\mathbb{H}$; the image is not a subalgebra of $M_2(\mathbb{R})$ but a real form inside $M_2(\mathbb{C})$, of real dimension four, which realifies to a four-dimensional subalgebra of $M_4(\mathbb{R})$.

The dual-number model is the analogue in which the coefficient ring stays $\mathbb{R}$ and the image is the commutative Toeplitz subalgebra; the determinant is the degenerate norm $a^2$, and the missing imaginary part of the coefficients is exactly the lost second coordinate. Both models sit inside a four-real-dimensional matrix algebra, but the quaternion image is a four-real-dimensional real form of $M_2(\mathbb{C})$, while the dual image is only the two-real-dimensional commutative subalgebra $RI \oplus RE$ of $M_2(\mathbb{R})$: $\mathbb{H}$ needs complex coefficients and $\mathbb{D}'$ does not.

### The Absence of a Two-Dimensional Representation for $\mathbb{H}_{\mathbb{D}}$

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ has real dimension eight, and $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H}\oplus\mathbb{H}$. There is **no** faithful representation of $\mathbb{H}_{\mathbb{D}}$ by $2\times2$ matrices over $\mathbb{R}$, and none over $\mathbb{C}$. Over $\mathbb{R}$, a faithful representation would be an injective $\mathbb{R}$-linear map into $M_2(\mathbb{R})$, which would need $\dim_{\mathbb{R}} M_2(\mathbb{R}) = 4 \ge \dim_{\mathbb{R}}\mathbb{H}_{\mathbb{D}} = 8$, and this fails. Over $\mathbb{C}$ the dimension count alone does **not** obstruct: a homomorphism of $\mathbb{R}$-algebras $\mathbb{H}_{\mathbb{D}} \to M_2(\mathbb{C})$ is only $\mathbb{R}$-linear, and $M_2(\mathbb{C})$ has real dimension $8$, equal to $\dim_{\mathbb{R}}\mathbb{H}_{\mathbb{D}}$, so an injective such map exists as a linear map and its image would be all of $M_2(\mathbb{C})$. What obstructs is the centre: such an embedding would give an isomorphism of $\mathbb{R}$-algebras $\mathbb{H}_{\mathbb{D}} \cong M_2(\mathbb{C})$, but the centre of $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H}\oplus\mathbb{H}$ is $\mathbb{R}\oplus\mathbb{R}$, not a field, while the centre of $M_2(\mathbb{C})$ is $\mathbb{C}$, a field. So the failure over $\mathbb{C}$ is a failure of the centre, not of the dimension.

**Remark.** Over $\mathbb{R}$ the obstruction is dimension, and over $\mathbb{C}$ it is the centre; in neither case is it the presence of zero divisors, since $M_2(\mathbb{R})$ itself has zero divisors and $\mathbb{H}_{\mathbb{D}}$ has zero divisors, so the failure is not caused by the ring-theoretic degeneracy. The smallest faithful matrix representation of $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H}\oplus\mathbb{H}$ is by $4\times4$ matrices over $\mathbb{C}$ (equivalently $8\times8$ over $\mathbb{R}$), obtained by embedding each factor $\mathbb{H}$ in $M_2(\mathbb{C})$ and taking the block diagonal sum. So the dual-number algebra, although degenerate, is small enough to fit in $M_2(\mathbb{R})$, while the split biquaternion algebra, although it has the same kind of zero divisors, is too large.

## Worked Examples

**Example (the homomorphism property).** For $Z = 2 + 3\varepsilon$ and $W = 4 + 5\varepsilon$,

$$
\Phi(Z)\Phi(W) = \begin{pmatrix} 2 & 3 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 4 & 5 \\ 0 & 4 \end{pmatrix} = \begin{pmatrix} 8 & 22 \\ 0 & 8 \end{pmatrix} = \Phi(ZW),
$$

matching $ZW = 8 + 22\varepsilon$; moreover $\det\Phi(Z) = 4 = N(Z)$ and $\det\Phi(ZW) = 64 = N(Z)N(W)$.

**Example (the shear subgroup).** For $s \in R$ the image of $1 + s\varepsilon$ is the unipotent matrix

$$
\Phi(1 + s\varepsilon) = I + sE = \begin{pmatrix} 1 & s \\ 0 & 1 \end{pmatrix}, \qquad \Phi(1 + s\varepsilon)\Phi(1 + t\varepsilon) = \Phi\bigl(1 + (s+t)\varepsilon\bigr),
$$

so these matrices form the shear subgroup $I + R\,E$, with $\Phi(1 + s\varepsilon)^{-1} = \Phi(1 - s\varepsilon)$. For instance $\Phi(1 + 3\varepsilon)\Phi(1 + 5\varepsilon) = \Phi(1 + 8\varepsilon)$.

## Summary

The dual-number algebra has the faithful unital $R$-algebra representation

$$
\Phi(a + \varepsilon b) = \begin{pmatrix} a & b \\ 0 & a \end{pmatrix}, \qquad \Phi(zw) = \Phi(Z)\Phi(W), \qquad \ker\Phi = 0,
$$

identifying $\mathbb{D}'_R$ with the commutative subalgebra of upper-triangular Toeplitz matrices, spanned by $I$ and the nilpotent $E = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ with $E^2 = 0$. The trace is $2a$, twice the real part; the determinant is $a^2 = N(Z)$, the degenerate norm form; and the characteristic polynomial is $(\lambda - a)^2$, exhibiting the single repeated eigenvalue equal to the real part. The distinguished submodules map to the scalar matrices $R\,I$ and the strictly upper-triangular matrices $R\,E$; dual conjugation is the inner involution by $J = \operatorname{diag}(1,-1)$; and the maximal ideal is the nilpotent line $R\,E$. The regular representation of the companion articles is the transpose convention, with the infinitesimal part in the lower-left corner. the shear subgroup is $I + R\,E$, with $\Phi(1 + s\varepsilon)\Phi(1 + t\varepsilon) = \Phi(1 + (s+t)\varepsilon)$; the algebra automorphisms $\varphi_c$ are realised by conjugation with the diagonal matrices $\operatorname{diag}(c, 1)$; and the polar form is recovered from the trace and the determinant by $B(Z, W) = \tfrac{1}{2}(\operatorname{tr}\Phi(Z)\operatorname{tr}\Phi(W) - \operatorname{tr}(\Phi(Z)\Phi(W)))$. Comparing with the quaternion case, $\mathbb{H}$ has a faithful $2\times2$ representation over $\mathbb{C}$ with determinant the non-degenerate form $a^2 + b^2 + c^2 + d^2$, while the dual algebra has a faithful $2\times2$ representation over $R$ with determinant the degenerate form $a^2$. The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$, of real dimension eight, has **no** faithful $2\times2$ representation, over $\mathbb{R}$ or over $\mathbb{C}$ — by the dimension count over $\mathbb{R}$ and by the centre obstruction over $\mathbb{C}$ — the smallest faithful representation being $4\times4$ over $\mathbb{C}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}'_R = R[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra over $R$; $\varepsilon^2 = 0$ |
| $\mathbb{D}' = \mathbb{D}'_{\mathbb{R}}$ | Dual-number algebra over $\mathbb{R}$ |
| $Z = a + \varepsilon b$ | General dual number |
| $a = \operatorname{Re} Z$, $b = \operatorname{Inf} Z$ | Real and infinitesimal parts |
| $\bar{Z} = a - \varepsilon b$ | Dual conjugation |
| $N(Z) = a^2$ | Norm form, equal to $\det\Phi(Z)$ |
| $\Phi(a + \varepsilon b) = \begin{pmatrix} a & b \\ 0 & a \end{pmatrix}$ | Faithful matrix representation |
| $E = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \Phi(\varepsilon)$ | Nilpotent Jordan block, $E^2 = 0$ |
| $J = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ | Involution realizing dual conjugation |
| $\varphi_c$ | Automorphism $\varepsilon \mapsto c\varepsilon$, conjugation by $\operatorname{diag}(c, 1)$ |
| $B(Z,W) = ac$ | Polar form, $\tfrac{1}{2}(\operatorname{tr}\Phi(Z)\operatorname{tr}\Phi(W) - \operatorname{tr}(\Phi(Z)\Phi(W)))$ |
| $[u] = \begin{pmatrix} a & 0 \\ b & a \end{pmatrix} = \Phi(u)^{\mathsf{T}}$ | Regular representation, transpose convention |
| $I = \Phi(1)$ | Identity matrix |
| $\mathbb{H}$ | Quaternions, faithful $2\times2$ representation over $\mathbb{C}$ |
| $\mathbb{H}_{\mathbb{D}} \cong \mathbb{H}\oplus\mathbb{H}$ | Split biquaternions, no faithful $2\times2$ representation |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, Cambridge, 2013), for triangular Toeplitz matrices, their spectra, and the matrix functions of a nilpotent.
- F. R. Gantmacher, *The Theory of Matrices* (Chelsea, New York, 1959), for Jordan blocks, the centralizer of a nongeneric matrix, and the functional calculus of a nilpotent.
- Israel N. Herstein, *Noncommutative Rings* (Mathematical Association of America, Washington, 1968), for the matrix representation of division algebras and the dimension obstruction to faithfulness.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for the matrix models of the quaternions and the two-dimensional real algebras.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation* (SIAM, Philadelphia, 2008), for the triangular matrix model of the nilpotent extension in computation.
- S. J. Sangwine, T. A. Ell and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions", *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the matrix representation of the biquaternions and the size of the smallest faithful one.
