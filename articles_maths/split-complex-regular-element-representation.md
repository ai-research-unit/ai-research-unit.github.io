
# __Split-Complex Regular Element Representation__

## Introduction

The split-complex algebra $\mathbb{D}$ acting on itself by left multiplication is the **left regular representation**, and writing that action in the basis $\{1, j\}$ gives the **regular matrix** of a split-complex number. This article develops that matrix in full: the Cayley matrix of multiplication by $A = a+j a'$, its identification with the algebra of $2\times 2$ real matrices of hyperbolic type, its multiplicativity, its determinant as the norm, its diagonalisation by the idempotent basis, its relation to the regular representation of the biquaternion algebra, and its relation to the hyperbolic rotations of the geometry slot. It is the two-dimensional counterpart of *Biquaternion $4\times4$ Regular Matrix Representation*, and it is the second of the three Representation articles, after *Split-Complex Element Representations* and before *Split-Complex Two-Component Element Representation*.

The general representation theory is owned by *Split-Complex Element Representations*; here the regular representation alone is studied, in its matrix form, with the multiplication operator as the object. The word *representation* is used in both senses at once, the concrete realization and the technical action of an algebra on a vector space, because the action is the object of study. The article owns the $2\times2$ regular matrix, the left and right multiplication operators and the fact that they coincide, the identification $\mathbb{D}\cong\{aI+a'J\}$, the determinant identity $\det \rho_L(A) = N(A)$, the diagonalisation in the idempotent basis, the centralizer statement, and the identification of the unit-norm subgroup with the hyperbolic rotations. It does not treat the classification of all representations, which belongs to *Split-Complex Element Representations*; it does not treat the polar parametrisation of the unit-norm group in its own right, which belongs to *Split-Complex Polar Element Representation*; and it uses, but does not reprove, the idempotent decomposition of *Split-Complex Idempotents and Projections*.

**Conventions.** The algebra is $\mathbb{D} = \mathbb{R}[x]/(x^2-1)$, basis $1$, $j$, $j^2 = +1$; general element $A = a+j a'$; conjugate $\bar A = a-j a'$; idempotents $\Pi_\pm = \tfrac12(1\pm j)$; idempotent coordinates $A_\pm = a\pm a'$, with $A = A_+\Pi_1 + A_-\Pi_2$; norm $N(A) = a^2-a'^2$. The coefficient space is the two-dimensional real vector space $\mathbb{D}$ itself, and the matrix of an operator is taken in the basis $\{1, j\}$ unless stated.

## The Left Regular Representation

**Definition.** The **left regular representation** of $\mathbb{D}$ is the map

$$
\rho_L : \mathbb{D} \longrightarrow \operatorname{End}_{\mathbb{R}}(\mathbb{D}), \qquad \rho_L(A)(B) = AB.
$$

For each $A$, the map $B \mapsto AB$ is $\mathbb{R}$-linear because multiplication is bilinear, so $\rho_L(A)$ is a real-linear endomorphism of the two-dimensional space $\mathbb{D}$. Writing each endomorphism as a matrix in the basis $1, j$, the same symbol $\rho_L(A)$ denotes the matrix acting on the column of coordinates $(B_0, B_1)^{\mathsf{T}}$ of $B = B_0 + B_1 j$:

$$
\rho_L(A)\, \begin{pmatrix} B_0 \\ B_1 \end{pmatrix} = \begin{pmatrix} (AB)_0 \\ (AB)_1 \end{pmatrix}.
$$

**Proposition (the regular matrix is the Cayley matrix).** In the basis $1, j$,

$$
\rho_L(A) = \begin{pmatrix} a & a' \\ a' & a \end{pmatrix}, \qquad A = a+j a'.
$$

Each entry is a single coefficient of $A$, carrying no sign other than those of the coefficients themselves, because in this basis each product of basis elements is one basis element.

**Proof.** The columns are the images of the basis, $\rho_L(A)(1) = A$ and $\rho_L(A)(j) = Aj$, expressed in the basis. The first is $A = a + j a'$, giving the column $(a, a')^{\mathsf{T}}$. The second is

$$
Aj = (a+j a')j = j a + a'\,j^2 = a' + j a,
$$

using $j^2 = +1$, giving the column $(a', a)^{\mathsf{T}}$. Hence the matrix displayed.

The matrix is the **Cayley matrix** of multiplication by $A$; it is symmetric, and its two columns are obtained from one another by exchanging the two coordinates, which is the reflection $j$ of the algebra.

**Example.** For $A = 2+3j$,

$$
\rho_L(2+3j) = \begin{pmatrix} 2 & 3 \\ 3 & 2 \end{pmatrix},
\qquad
\rho_L(2+3j)\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 2 \\ 3 \end{pmatrix},
\qquad
\rho_L(2+3j)\begin{pmatrix} 0 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}.
$$

The first column is the coordinate column of $A$, the second that of $Aj = 3+2j$; the product $A \cdot 1 = A$ and $A\cdot j = Aj$ are read off directly.

## The Left Representation Is a Homomorphism

**Theorem (multiplicativity).** For all $A, B \in \mathbb{D}$,

$$
\rho_L(A)\,\rho_L(B) = \rho_L(AB).
$$

Hence $\rho_L$ is an algebra homomorphism, and $\mathbb{D}$ is a left $\mathbb{D}$-module under it.

**Proof.** Both sides are $\mathbb{R}$-linear in the second factor and are computed on the basis. For every basis element $e_m$, associativity of the algebra gives

$$
\rho_L(A)\bigl(\rho_L(B)(e_m)\bigr) = A(We_m) = (AB)e_m = \rho_L(AB)(e_m),
$$

so the two matrices agree on a basis. In matrices this is the identity

$$
\begin{pmatrix} a & a' \\ a' & a \end{pmatrix}\begin{pmatrix} b & b' \\ b' & b \end{pmatrix} = \begin{pmatrix} a b+a' b' & a b'+a' b \\ a b'+a' b & a b+a' b' \end{pmatrix} = \rho_L(AB),
\qquad B = b+j b',
$$

whose right side is the Cayley matrix of $AB$.

**Corollary ($\rho_L$ is faithful).** The map $\rho_L$ is injective, whence $\mathbb{D}$ embeds as an algebra of $2\times2$ real matrices. Indeed $\rho_L(A) = 0$ forces the first column $(a,a')^{\mathsf{T}}$ to vanish, so $A = 0$.

**Example (a concrete check).** For $A = 1+j$ and $B = 1+2j$, the product is $AB = (1+2) + (2+1)j = 3+3j$, and

$$
\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} 3 & 3 \\ 3 & 3 \end{pmatrix} = \rho_L(3+3j). \checkmark
$$

## The Right Regular Representation and Commutativity

**Definition.** The **right regular representation** is

$$
\rho_R : \mathbb{D} \longrightarrow \operatorname{End}_{\mathbb{R}}(\mathbb{D}), \qquad \rho_R(A)(B) = BA.
$$

In the basis $1, j$ its matrix has columns $\rho_R(A)(1) = A$ and $\rho_R(A)(j) = jA = Aj$; since the algebra is commutative, $jA = Aj$, so the two columns are again $(a,a')^{\mathsf{T}}$ and $(a',a)^{\mathsf{T}}$:

$$
\rho_R(A) = \begin{pmatrix} a & a' \\ a' & a \end{pmatrix} = \rho_L(A).
$$

**Proposition.** The left and right regular representations of $\mathbb{D}$ coincide: $\rho_L = \rho_R$.

**Proof.** This is the commutativity of $\mathbb{D}$: $AB = BA$ for all $B$, so the two endomorphisms agree.

This is a systematic difference from the biquaternion case, where the left and right regular matrices are distinct and are obtained from one another by transposition and the reversal of the coefficients; here there is no distinction to make, and the transposition identity of the four-dimensional article degenerates to the statement that the single regular matrix is symmetric. The vanishing of the commutator of the two actions is exactly the commutativity of the algebra.

## The Image: $2\times2$ Real Matrices of Hyperbolic Type

The image of $\rho_L$ is the set

$$
\rho_L(\mathbb{D}) = \left\{ \begin{pmatrix} a & a' \\ a' & a \end{pmatrix} : a, a' \in \mathbb{R} \right\} = \left\{ a I + a' J : a, a' \in \mathbb{R} \right\},
\qquad
I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad J = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.
$$

The matrix $J$ satisfies

$$
J^2 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}^2 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I,
$$

so the algebra $\rho_L(\mathbb{D})$ is the **hyperbolic** (or split-complex, or double-number) algebra of matrices, with the generator $J$ of square $+I$. It is the matrix image of $\mathbb{D}$ and is isomorphic to it:

$$
\mathbb{D} \;\cong\; \rho_L(\mathbb{D}) = \mathbb{R}[J], \qquad j \longmapsto J.
$$

By contrast the complex field embeds as $\mathbb{C}\cong\{aI + a'K\}$ with $K = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ of square $-I$; the two matrix algebras differ only in the sign of the square of their generator, which is precisely the difference between $j^2 = +1$ and $i^2 = -1$.

The matrix picture also exhibits the multiplication table of $\mathbb{D}$ on the generators $I, J$:

| product | $I$ | $J$ |
|---|---|---|
| $I$ | $I$ | $J$ |
| $J$ | $J$ | $I$ |

which is the table of $\mathbb{Z}/2$ under addition, that is, the group ring $\mathbb{R}[\mathbb{Z}/2]$.

## The Determinant, the Trace and the Norm

**Theorem.** For $A = a+j a'$,

$$
\det \rho_L(A) = a^2 - a'^2 = N(A), \qquad \operatorname{Tr}\rho_L(A) = 2a = A_+ + A_-.
$$

**Proof.** The determinant of a $2\times2$ matrix with diagonal $a$ and off-diagonal $a'$ is $a^2-a'^2$, which is $N(A)$; the trace is $2a$, which is $A_+ + A_-$.

**Corollary (multiplicativity of the norm).** Since $\rho_L$ is a homomorphism and the determinant is multiplicative,

$$
N(AB) = \det \rho_L(AB) = \det\bigl(\rho_L(A)\rho_L(B)\bigr) = \det \rho_L(A)\det \rho_L(B) = N(A)N(B),
$$

which is the multiplicativity of the norm, proved here as a special case of the multiplicativity of the determinant.

**Corollary (invertibility).** The matrix $\rho_L(A)$ is invertible iff $\det \rho_L(A) = N(A) \neq 0$, so $\mathbb{D}^\times$ corresponds to the invertible matrices in $\rho_L(\mathbb{D})$, and

$$
\rho_L(A)^{-1} = \rho_L(A^{-1}) = \frac{1}{N(A)}\begin{pmatrix} a & -a' \\ -a' & a \end{pmatrix}.
$$

**The characteristic polynomial.** A $2\times2$ matrix has characteristic polynomial

$$
\lambda^2 - \operatorname{Tr}\rho_L(A)\,\lambda + \det \rho_L(A) = \lambda^2 - 2a\lambda + (a^2-a'^2) = (\lambda - A_+)(\lambda - A_-),
$$

whose roots are the two idempotent coordinates $A_+ = a+a'$ and $A_- = a-a'$, both real. The eigenvalues of the regular matrix of $A$ are therefore the two numbers from which $A$ is reconstructed, and the Cayley–Hamilton identity reads

$$
\rho_L(A)^2 - 2a\,\rho_L(A) + (a^2-a'^2) I = 0.
$$

So the norm and the idempotent coordinates are the two elementary symmetric functions of the eigenvalues, and $\mathbb{D}$ is the algebra of real $2\times2$ matrices whose spectrum is real and whose eigenvectors are fixed, the two idempotent lines.

## Diagonalisation in the Idempotent Basis

Change basis from the eigenbasis $\{1, j\}$ of the involution to the idempotent basis $\{\Pi_1, \Pi_2\}$. In the idempotent basis multiplication is componentwise, so the left regular operator acts by

$$
A \Pi_1 = A_+ \Pi_1, \qquad A \Pi_2 = A_- \Pi_2,
$$

whence its matrix is diagonal:

$$
\rho_L(A)\big|_{\{\Pi_1, \Pi_2\}} = \begin{pmatrix} A_+ & 0 \\ 0 & A_- \end{pmatrix} = \begin{pmatrix} a+a' & 0 \\ 0 & a-a' \end{pmatrix}.
$$

The change-of-basis matrix from $\{1, j\}$ to $\{\Pi_1, \Pi_2\}$ is $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ acting on coordinate columns, and the diagonalisation is the similarity

$$
P\,\rho_L(A)\,P^{-1} = \begin{pmatrix} a+a' & 0 \\ 0 & a-a' \end{pmatrix}, \qquad P \begin{pmatrix} a & a' \\ a' & a \end{pmatrix} P^{-1} = \begin{pmatrix} a+a' & 0 \\ 0 & a-a' \end{pmatrix},
$$

which holds for every $A$. So the whole algebra $\rho_L(\mathbb{D})$ is simultaneously diagonalised by the single matrix $P$: the two idempotent coordinates are a complete set of eigenvalues, and the regular matrix is the diagonal matrix $\operatorname{diag}(A_+, A_-)$ in the idempotent basis.

**Corollary (simultaneous diagonalisation and commutativity).** The algebra $\rho_L(\mathbb{D})$ consists of the matrices simultaneously diagonalised by $P$, namely $\operatorname{diag}(\lambda, \mu)$ with $\lambda, \mu \in \mathbb{R}$; this is the matrix form of the isomorphism $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$.

**Example.** For $A = 2+3j$ the idempotent coordinates are $A_+ = 5$ and $A_- = -1$, and

$$
\rho_L(2+3j) = \begin{pmatrix} 2 & 3 \\ 3 & 2 \end{pmatrix}, \qquad
P \begin{pmatrix} 2 & 3 \\ 3 & 2 \end{pmatrix} P^{-1} = \begin{pmatrix} 5 & 0 \\ 0 & -1 \end{pmatrix}. \checkmark
$$

### The Idempotents as Diagonal Matrix Units

In the idempotent basis the two idempotents are the diagonal matrix units of the model:

$$
\rho_L(\Pi_1) = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} = E_{11}, \qquad \rho_L(\Pi_2) = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} = E_{22}.
$$

The corresponding abstract statement — that $\Pi_\pm$ are the diagonal matrix units of $\mathbb{D}$, with the multiplication rule $\Pi_1^2=\Pi_1$, $\Pi_2^2=\Pi_2$, $\Pi_1\Pi_2=0$, $\Pi_1+\Pi_2=1$, and that no off-diagonal matrix units exist because the algebra is commutative — is the content of *Split-Complex Ideals and Peirce Decomposition*. In the matrix model it reads as the diagonalisation just recorded: the image is a direct sum of two diagonal blocks, and in the biquaternion algebra the same decomposition splits $\mathbb{B}$ into four blocks of complex dimensions $1+1+1+1$ with all matrix units present, whereas here only two blocks survive, of real dimension $1$ each.

## The Unit-Norm Subgroup and the Hyperbolic Rotations

The unit-norm elements are those with $N(A) = 1$; in the matrix picture they are the matrices of determinant $1$ in $\rho_L(\mathbb{D})$,

$$
SO(1,1) \;\cong\; \rho_L(\{A : N(A) = 1\}) = \left\{ \begin{pmatrix} a & a' \\ a' & a \end{pmatrix} : a^2 - a'^2 = 1 \right\},
$$

Writing the spacelike branch $a > 0$ in the hyperbolic parametrisation $a = \cosh t$, $a' = \sinh t$ gives

$$
R_j(t) = \rho_L(e^{jt}) = \begin{pmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t \end{pmatrix},
\qquad t \in \mathbb{R},
$$

the **hyperbolic rotation** matrix of angle $t$. It is the matrix of the one-parameter group $\{e^{jt}\}$, and the group law

$$
R_j(t)R_j(s) = R_j(t+s)
$$

is the multiplicativity of $\rho_L$ combined with $e^{jt}e^{js} = e^{j(t+s)}$.

**Proposition.** For every $t$, $R_j(t)$ preserves the norm: if $B = b+j b'$, then $N(R_j(t)B) = N(B)$.

**Proof.** $\det R_j(t) = \cosh^2 t - \sinh^2 t = 1$, and $N$ is the determinant of the coordinate matrix, so $N(R_j(t)B) = \det(R_j(t)\rho_L(B)) = \det R_j(t)\det\rho_L(B) = N(B)$.

So the hyperbolic rotations are exactly the identity component $SO^+(1,1)$ of the determinant-one subgroup of the regular matrix algebra, and their action is the linear action on $\mathbb{R}^2$ preserving $a^2-a'^2$. The unit-norm group has a second branch, $a < 0$, related to the first by the central reflection $-1$, and the whole group $\{N=1\}$ has two components; the matrix picture and the group structure are developed in *Split-Complex Exponential and Lie Group Structure* and in *Hyperbolic Rotations*, where $R_j(t)$ is the generator of the hyperbolic one-parameter group.

## The Centralizer

**Theorem.** The centralizer of $\rho_L(\mathbb{D})$ in $M_2(\mathbb{R})$ is $\rho_L(\mathbb{D})$ itself.

**Proof.** A matrix $C = \begin{pmatrix} p & q \\ r & s \end{pmatrix}$ commutes with $J = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ iff

$$
\begin{pmatrix} p & q \\ r & s \end{pmatrix}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} q & p \\ s & r \end{pmatrix}, \qquad
\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\begin{pmatrix} p & q \\ r & s \end{pmatrix} = \begin{pmatrix} r & s \\ p & q \end{pmatrix},
$$

and equality gives $q = r$ and $p = s$. So $C = \begin{pmatrix} p & q \\ q & p \end{pmatrix} \in \rho_L(\mathbb{D})$. Conversely every matrix in $\rho_L(\mathbb{D})$ commutes with $J$, because $\rho_L(\mathbb{D})$ is commutative.

So $\rho_L(\mathbb{D})$ is its own centralizer and its own bicommutant, a **maximal commutative subalgebra** of $M_2(\mathbb{R})$ of dimension two. This is the degeneration of the biquaternion double centralizer statement, where the centralizer of $\rho_L(\mathbb{B})$ is the image of the right regular representation $\rho_R(\mathbb{B})$, a distinct copy of complex dimension four that commutes with $\rho_L(\mathbb{B})$; here the two copies coincide, $\rho_R(\mathbb{D}) = \rho_L(\mathbb{D})$, and the algebra is its own centralizer because it is already commutative.

## The Real Form and the Relation to the Biquaternion Case

The image $\rho_L(\mathbb{D})$ is defined over $\mathbb{R}$ and consists of the real symmetric matrices of the special form $aI+a'J$. Under the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$ the regular representation of $\mathbb{B}$ is the left action of $M_2(\mathbb{C})$ on the four-real-dimensional space $\mathbb{B}$, and its matrix is $4\times4$ over $\mathbb{C}$. The split-complex case is the two-dimensional real shadow of that construction:

| feature | $\mathbb{B}$ | $\mathbb{D}$ |
|---|---|---|
| dimension over the base field | $4$ over $\mathbb{C}$ | $2$ over $\mathbb{R}$ |
| regular matrix | $4\times4$, complex, one sign per entry | $2\times2$, real, symmetric |
| left vs right | $\rho_R(\tilde{Q})$ distinct from $\rho_L(\tilde{Q})$, the two copies commuting | $\rho_L = \rho_R$ (commutativity) |
| determinant of the regular matrix | $N(\tilde{Q})^2$ | $N(A) = a^2-a'^2$ |
| eigenvalues | the roots of a complex quartic | the two real numbers $A_\pm$ |
| diagonalisation | block diagonalisation into two minimal ideals | diagonalisation by $P$ into $\mathbb{R}\oplus\mathbb{R}$ |
| centralizer | $\rho_R(\mathbb{B})$, a distinct copy | the algebra itself |

The regular representation of $\mathbb{B}$ is reducible, splitting into the two minimal left ideals; the regular representation of $\mathbb{D}$ is likewise reducible, splitting into the two idempotent lines $I_1 = \mathbb{R}\Pi_1$ and $I_2 = \mathbb{R}\Pi_2$:

$$
\mathbb{D} = I_1 \oplus I_2, \qquad I_1 = \mathbb{R}\Pi_1, \quad I_2 = \mathbb{R}\Pi_2,
$$

on each of which $\rho_L(A)$ acts by the scalar $A_+$ or $A_-$. So the two-dimensional regular representation is the direct sum of the two one-dimensional representations $A \mapsto A_+$ and $A \mapsto A_-$, and it is completely reducible, as a representation of a semisimple algebra must be.

## Summary

The left regular representation $\rho_L$ of $\mathbb{D}$ sends $A$ to the endomorphism $B \mapsto AB$ of the coefficient space $\mathbb{D}$, with matrix $\begin{pmatrix} a & a' \\ a' & a \end{pmatrix}$ in the basis $\{1, j\}$. The map is an algebra homomorphism and a faithful embedding, so $\mathbb{D}$ is isomorphic to the algebra $\{aI+a'J\}$ of real $2\times2$ matrices with $J^2 = I$, the hyperbolic analogue of the matrix model of $\mathbb{C}$. Because $\mathbb{D}$ is commutative the right regular representation coincides with the left, and the regular matrix is symmetric.

The determinant of the regular matrix is the norm, $\det\rho_L(A) = a^2-a'^2 = N(A)$, and the trace is $2a$; multiplicativity of the determinant gives multiplicativity of the norm, and invertibility of the matrix is the unit criterion. The characteristic polynomial is $(\lambda - A_+)(\lambda - A_-)$, so the eigenvalues are the idempotent coordinates; the idempotent basis diagonalises the whole algebra simultaneously, $\rho_L(A) = \operatorname{diag}(a+a', a-a')$ up to the change of basis $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, and the regular representation splits as the direct sum of the two one-dimensional representations $A \mapsto A_\pm$; the idempotents become the diagonal matrix units $\operatorname{diag}(1,0)$ and $\operatorname{diag}(0,1)$, and no off-diagonal matrix unit exists. The unit-norm elements form the determinant-one subgroup, the hyperbolic rotations $R_j(t) = \begin{pmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t \end{pmatrix}$, and the centralizer of the image is the image itself. The regular matrix is the two-dimensional real shadow of the $4\times4$ complex regular matrix of the biquaternion algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $A = a + j a'$ | General split complex number |
| $\rho_L(A)$ | Left regular representation, matrix $\begin{pmatrix} a & a' \\ a' & a \end{pmatrix}$ |
| $\rho_R(A)$ | Right regular representation; $\rho_R = \rho_L$ |
| $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, $J = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ | Matrix units of the image, $J^2 = I$ |
| $E_{11} = \rho_L(\Pi_1)$, $E_{22} = \rho_L(\Pi_2)$ | Diagonal matrix units of the image |
| $\det\rho_L(A) = a^2-a'^2$ | Determinant of the regular matrix, the norm |
| $\operatorname{Tr}\rho_L(A) = 2a$ | Trace of the regular matrix |
| $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ | Change of basis to the idempotents, $P\rho_L(A)P^{-1} = \operatorname{diag}(A_+,A_-)$ |
| $A_\pm = a\pm a'$ | Idempotent coordinates, the eigenvalues |
| $\Pi_\pm = \tfrac12(1\pm j)$ | Idempotents |
| $I_1 = \mathbb{R}\Pi_1$, $I_2 = \mathbb{R}\Pi_2$ | The two minimal left ideals |
| $R_j(t) = \begin{pmatrix} \cosh t & \sinh t \\ \sinh t & \cosh t \end{pmatrix}$ | Hyperbolic rotation matrix, $\rho_L(e^{jt})$ |
| $N(A) = a^2-a'^2$ | Norm |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the regular representation, the Cayley matrix and the structure of finite-dimensional algebras.
- John Stillwell, *Naive Lie Theory* (Springer, Undergraduate Texts in Mathematics, 2008), for $2\times2$ matrix groups, the hyperbolic rotation matrices and $SO(1,1)$.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the realization of split-complex numbers as matrices and its geometric meaning.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for regular representations of low-dimensional Clifford algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, Graduate Texts in Mathematics 131, 2nd ed. 2001), for the double centralizer theorem and its commutative degeneration.
