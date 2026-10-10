
# __Quaternion 4x4 Matrix Element Representation $M_4(\mathbb{R})_L$__

## Introduction

Every associative algebra acts on itself by left multiplication, and the resulting matrices form the **left regular representation**. For the quaternion algebra this gives an injective algebra homomorphism $\mathbb{H}\to M_4(\mathbb{R})$, the four-dimensional real matrix representation; the matrix of left multiplication by $\tilde q$ is the **Cayley matrix** of $\tilde q$. This article develops that representation: the explicit matrix, its multiplicativity, its determinant and trace, its behaviour under transposition and under the three involutions, the parallel right regular representation, and the double centraliser theorem which identifies the two representations as each other's commutants. It is the quaternion member of the family's regular-representation pair; the counterpart is the $8\times8$ real regular representation of the biquaternion algebra, into which the present one embeds after complexification.

The article depends on *Quaternion Algebra* for the multiplication table and on *Quaternion Norm and Invertibility* for the quaternion norm; the $2\times2$ complex representation, which is obtained by complexification and carries the same information in half the size, is treated in *Quaternion 2x2 Matrix Element Representation*, and the coordinate form of the multiplication is in *Quaternion Four-Vector Element Representation*.

The corpus's default base is a commutative ring with identity, and the regular representation is defined over such a base whenever the algebra is faithful over itself; the determinant and norm statements are stated over a field $F$, and the positivity of the quaternion norm is the statement over $\mathbb{R}$.

Throughout, $\mathbb{H}$ is the quaternion algebra with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, $e_1e_2 = e_3$; a quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$, written $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with conjugate $\tilde{q}^{\natural} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ and norm $N(\tilde q) = \tilde q\tilde{q}^{\natural}$; the matrix of left multiplication is $\mathsf{M}_4(\tilde q)$ and the matrix of right multiplication is $\mathsf{M}_4^{R}(\tilde q)$.

## The Left Regular Representation

**Definition.** The **left regular representation** is the map $L : \mathbb{H}\to\operatorname{End}_F(\mathbb{H})$ sending $\tilde q$ to the endomorphism $L_{\tilde q}(\tilde r) = \tilde q \tilde r$. The **Cayley matrix** of $\tilde q$ is the matrix of $L_{\tilde q}$ in the basis $(e_0,e_1,e_2,e_3)$.

**Theorem.** The map $\mathsf{M}_4$ is an injective algebra homomorphism: $\mathsf{M}_4(p+\tilde q) = \mathsf{M}_4(p)+\mathsf{M}_4(\tilde q)$, $\mathsf{M}_4(p\tilde q) = \mathsf{M}_4(p)\mathsf{M}_4(\tilde q)$, $\mathsf{M}_4(1) = \mathrm{id}$, and $\mathsf{M}_4$ is injective. Its image is a four-dimensional subalgebra of $M_4(F)$ isomorphic to $\mathbb{H}$.

*Proof.* Left multiplication is $F$-linear, and associativity gives $\mathsf{M}_4(p)L_{\tilde q}(\tilde r) = p(\tilde q \tilde r) = (p\tilde q)\tilde r = L_{p\tilde q}(\tilde r)$. If $\mathsf{M}_4(\tilde q) = 0$ then $\tilde q = L_{\tilde q}(1) = 0$, so $\mathsf{M}_4$ is injective; the image is a subalgebra of dimension $\dim\mathbb{H} = 4$.

**Theorem (Cayley matrix).** For $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$, the Cayley matrix of left multiplication is

$$
\mathsf{M}_4(\tilde q) = \begin{pmatrix}
q_0 & -q_1 & -q_2 & -q_3 \\
q_1 & q_0 & -q_3 & q_2 \\
q_2 & q_3 & q_0 & -q_1 \\
q_3 & -q_2 & q_1 & q_0
\end{pmatrix}.
$$

*Proof.* The columns are $L_{\tilde q}(e_k) = \tilde q e_k$. Direct multiplication gives

$$
\tilde q e_0 = \tilde q, \quad \tilde q e_1 = -q_1+q_0e_1+q_3e_2-q_2e_3, \quad \tilde q e_2 = -q_2-q_3e_1+q_0e_2+q_1e_3, \quad \tilde q e_3 = -q_3+q_2e_1-q_1e_2+q_0e_3,
$$

which are the four columns of the displayed matrix.

**Proposition.** The Cayley matrix is the sum of a scalar and a skew-symmetric part,

$$
\mathsf{M}_4(\tilde q) = q_0 I + \Omega_q, \qquad \Omega_q = \begin{pmatrix} 0 & -q_1 & -q_2 & -q_3 \\ q_1 & 0 & -q_3 & q_2 \\ q_2 & q_3 & 0 & -q_1 \\ q_3 & -q_2 & q_1 & 0 \end{pmatrix}, \qquad \Omega_q^{T} = -\Omega_q .
$$

*Proof.* Subtract the scalar matrix $q_0I$ from $\mathsf{M}_4(\tilde q)$; the remainder is the displayed matrix, whose transpose is its negative.

The decomposition separates the two subspaces: for a scalar $s$ the Cayley matrix is the scalar matrix $\mathsf{M}_4(s) = sI$, and for a pure quaternion $\mathbf{q}$ it is $\mathsf{M}_4(\mathbf{q}) = \Omega_{\mathbf{q}}$, traceless and skew-symmetric. The scalar subspace therefore maps to the scalar matrices and the vector subspace to the traceless skew-symmetric ones.

### A Worked Cayley Matrix

**Example.** For the element

$$
\tilde q = 1+2e_1-e_2+3e_3
$$

the four general products $\tilde qe_k$ are

$$
\tilde q e_0 = \tilde q, \quad \tilde q e_1 = -2+e_1+3e_2+e_3, \quad \tilde q e_2 = 1-3e_1+e_2+2e_3, \quad \tilde q e_3 = -3-e_1-2e_2+e_3,
$$

so its Cayley matrix is

$$
\mathsf{M}_4(\tilde q) = \begin{pmatrix}
1 & -2 & 1 & -3 \\
2 & 1 & -3 & -1 \\
-1 & 3 & 1 & -2 \\
3 & 1 & 2 & 1
\end{pmatrix},
$$

with $\mathsf{M}_4(\tilde q)^{T}\mathsf{M}_4(\tilde q) = 15\,I = N(\tilde q)I$, $\det \mathsf{M}_4(\tilde q) = N(\tilde q)^2 = 225$ and $\operatorname{tr}\mathsf{M}_4(\tilde q) = 4q_0 = 4$.

## Multiplicativity

**Theorem.** The Cayley matrices multiply as the quaternions do:

$$
\mathsf{M}_4(p)\mathsf{M}_4(\tilde q) = \mathsf{M}_4(p\tilde q), \qquad \mathsf{M}_4(p)+\mathsf{M}_4(\tilde q) = \mathsf{M}_4(p+\tilde q), \qquad \mathsf{M}_4(\tilde q^{-1}) = \mathsf{M}_4(\tilde q)^{-1}.
$$

*Proof.* The first two are the homomorphism property; the third follows from $\mathsf{M}_4(\tilde q)\mathsf{M}_4(\tilde q^{-1}) = \mathsf{M}_4(\tilde q \tilde q^{-1}) = \mathsf{M}_4(1) = I$ for an invertible $\tilde q$.

**Corollary.** The Cayley matrix of a unit quaternion is invertible, and $\mathsf{M}_4(\tilde q)^{-1} = \mathsf{M}_4(\tilde{q}^{\natural})/N(\tilde q)$; in particular the left regular representation restricts to an injective homomorphism of groups $Sp(1)\to O(4)$.

*Proof.* $\mathsf{M}_4(\tilde{q}^{\natural}/N(\tilde q)) = \mathsf{M}_4(\tilde{q}^{\natural})/N(\tilde q)$ and $\mathsf{M}_4(\tilde{q}^{\natural})\mathsf{M}_4(\tilde q) = \mathsf{M}_4(\tilde{q}^{\natural} \tilde q) = \mathsf{M}_4(N(\tilde q)) = N(\tilde q)I$, so $\mathsf{M}_4(\tilde q)^{-1} = \mathsf{M}_4(\tilde{q}^{\natural})/N(\tilde q)$. For a unit $N(\tilde q) = 1$ and $\mathsf{M}_4(\tilde q)^{-1} = \mathsf{M}_4(\tilde{q}^{\natural}) = \mathsf{M}_4(\tilde q)^{T}$ by the next theorem, so $\mathsf{M}_4(\tilde q)\in O(4)$.

## Determinant and Trace

**Theorem.** For every quaternion,

$$
\det \mathsf{M}_4(\tilde q) = N(\tilde q)^2 = (q_0^2+q_1^2+q_2^2+q_3^2)^2, \qquad \operatorname{tr}\mathsf{M}_4(\tilde q) = 4q_0 .
$$

*Proof.* The trace is the sum of the diagonal entries $q_0+q_0+q_0+q_0 = 4q_0$. For the determinant, compute $\mathsf{M}_4(\tilde q)^{T}\mathsf{M}_4(\tilde q)$. By the next theorem $\mathsf{M}_4(\tilde q)^{T} = \mathsf{M}_4(\tilde{q}^{\natural})$, so

$$
\mathsf{M}_4(\tilde q)^{T}\mathsf{M}_4(\tilde q) = \mathsf{M}_4(\tilde{q}^{\natural})\mathsf{M}_4(\tilde q) = \mathsf{M}_4(\tilde{q}^{\natural} \tilde q) = \mathsf{M}_4(N(\tilde q)) = N(\tilde q)\,I,
$$

whence $(\det \mathsf{M}_4(\tilde q))^2 = \det(N(\tilde q)I) = N(\tilde q)^4$, and $\det \mathsf{M}_4(\tilde q) = N(\tilde q)^2$ by the sign check at $\tilde q = 1$, where $\mathsf{M}_4(1) = I$ and $\det = 1 = N(1)^2$.

**Corollary.** The Cayley matrix of a non-zero quaternion is invertible, and $\det \mathsf{M}_4(\tilde q) > 0$ for $\tilde q\neq0$; the representation $\mathsf{M}_4$ sends $\mathbb{H}^{\times}$ into $GL_4(F)$, and over $\mathbb{R}$ the determinant is a perfect square.

*Proof.* $\det \mathsf{M}_4(\tilde q) = N(\tilde q)^2\neq0$ for $\tilde q\neq0$ by the unit criterion, and the square of a non-zero real number is positive.

**Remark.** The identity $\mathsf{M}_4(\tilde q)^{T}\mathsf{M}_4(\tilde q) = N(\tilde q)I$ says that $\mathsf{M}_4(\tilde q)$ is $\sqrt{N(\tilde q)}$ times an orthogonal matrix; on the unit sphere the map $\tilde q\mapsto \mathsf{M}_4(\tilde q)$ is then a homomorphism $Sp(1)\to SO(4)$, the left-translation factor of the two-sided covering $Sp(1)\times Sp(1)\to SO(4)$, whose matrix form is recorded in *Quaternion Rotations and Reflections*, §*The Two-Sided Action and SO(4)*, and whose other factor is the right regular representation.

## Transposition and the Conjugations

**Theorem.** Transposition of the Cayley matrix is quaternion conjugation:

$$
\mathsf{M}_4(\tilde q)^{T} = \mathsf{M}_4(\tilde{q}^{\natural}).
$$

*Proof.* The transpose of the displayed matrix is obtained by interchanging rows and columns; comparing entrywise with $\mathsf{M}_4(\tilde{q}^{\natural})$, the diagonal is unchanged and each off-diagonal entry changes sign in the pattern $-q_1,-q_2,-q_3$ exactly as conjugation negates the vector part.

**Theorem.** The three involutions of the algebra act on the Cayley matrix by

$$
\mathsf{M}_4(\tilde{q}^{\natural}) = \mathsf{M}_4(\tilde q)^{T}, \qquad \mathsf{M}_4(-\tilde{q}^{\natural}) = -\mathsf{M}_4(\tilde q)^{T}, \qquad \mathsf{M}_4(-\tilde q) = -\mathsf{M}_4(\tilde q),
$$

and the identity involution gives $\mathsf{M}_4(\tilde q)$ itself.

*Proof.* The first is the transposition theorem; the second follows from linearity, $\mathsf{M}_4(-\tilde{q}^{\natural}) = -\mathsf{M}_4(\tilde{q}^{\natural}) = -\mathsf{M}_4(\tilde q)^T$; the third likewise, $\mathsf{M}_4(-\tilde q) = -\mathsf{M}_4(\tilde q)$.

**Corollary.** The left regular representation identifies the four linear involutions $\tilde q\mapsto \tilde q,\ \tilde{q}^{\natural},\ -\tilde{q}^{\natural},\ -\tilde q$ with the four matrices $\pm \mathsf{M}_4(\tilde q),\ \pm \mathsf{M}_4(\tilde q)^{T}$, and the fixed spaces of the involutions are the $\pm1$ eigenspaces of these matrices, in agreement with *The Scalar and Vector Subspaces of $\mathbb{H}$*.

## The Right Regular Representation

**Definition.** The **right regular representation** is $\mathsf{M}_4^{R} : \mathbb{H}\to M_4(F)$ with $R_{\tilde q}(\tilde r) = \tilde r\tilde q$.

**Theorem.** The map $\mathsf{M}_4^{R}$ is an injective algebra anti-homomorphism, $\mathsf{M}_4^{R}(p\tilde q) = \mathsf{M}_4^{R}(\tilde q)\mathsf{M}_4^{R}(p)$, and the matrix of right multiplication is

$$
\mathsf{M}_4^{R}(\tilde q) = \begin{pmatrix}
q_0 & -q_1 & -q_2 & -q_3 \\
q_1 & q_0 & q_3 & -q_2 \\
q_2 & -q_3 & q_0 & q_1 \\
q_3 & q_2 & -q_1 & q_0
\end{pmatrix}.
$$

*Proof.* $(\mathsf{M}_4^{R}(p)\mathsf{M}_4^{R}(\tilde q))(\tilde r) = R_{p}(\tilde r\tilde q) = \tilde r\tilde q p = R_{\tilde q p}(\tilde r)$, so $\mathsf{M}_4^{R}(p\tilde q) = \mathsf{M}_4^{R}(\tilde q)\mathsf{M}_4^{R}(p)$. The columns are $R_{\tilde q}(e_k) = e_k\tilde q$, computed directly as

$$
e_0\tilde q = \tilde q, \quad e_1\tilde q = -q_1+q_0e_1-q_3e_2+q_2e_3, \quad e_2\tilde q = -q_2+q_3e_1+q_0e_2-q_1e_3, \quad e_3\tilde q = -q_3-q_2e_1+q_1e_2+q_0e_3 .
$$

**Theorem.** The right representation has the same determinant and trace,

$$
\det \mathsf{M}_4^{R}(\tilde q) = N(\tilde q)^2, \qquad \operatorname{tr}\mathsf{M}_4^{R}(\tilde q) = 4q_0,
$$

and it satisfies $\mathsf{M}_4^{R}(\tilde q)^{T} = \mathsf{M}_4^{R}(\tilde{q}^{\natural})$ together with the relation

$$
\mathsf{M}_4^{R}(\tilde q) = D\,\mathsf{M}_4(\tilde q)^{T}\,D, \qquad D = \operatorname{diag}(1,-1,-1,-1),
$$

where $D$ is the matrix of quaternion conjugation.

*Proof.* The trace is $4q_0$ from the diagonal. The relation $\mathsf{M}_4^{R}(\tilde q)^{T} = \mathsf{M}_4^{R}(\tilde{q}^{\natural})$ is the same entrywise comparison as for $\mathsf{M}_4$. For the last identity, $D$ is the matrix of the linear map $\tilde r\mapsto \tilde r^{\natural}$, so for every $\tilde r$,

$$
D \mathsf{M}_4(\tilde q)^{T} D \tilde r = D \mathsf{M}_4(\tilde{q}^{\natural}) D \tilde r = D\bigl(\tilde{q}^{\natural}\,\tilde r^{\natural}\bigr) = (\tilde{q}^{\natural}\,\tilde r^{\natural})^{\natural} = \tilde r\tilde q = \mathsf{M}_4^{R}(\tilde q)\,\tilde r,
$$

using $\mathsf{M}_4(\tilde q)^{T} = \mathsf{M}_4(\tilde{q}^{\natural})$ and the reversal $(\tilde q_1\tilde q_2)^{\natural} = \tilde{q}^{\natural}_2\,\tilde{q}^{\natural}_1$ of conjugation. Hence $\mathsf{M}_4^{R}(\tilde q) = D \mathsf{M}_4(\tilde q)^{T} D$, and the determinant is that of $\mathsf{M}_4(\tilde q)$ because $D^2 = I$.

**Proposition.** The left and right representations commute: $\mathsf{M}_4(p)\mathsf{M}_4^{R}(\tilde q) = \mathsf{M}_4^{R}(\tilde q)\mathsf{M}_4(p)$ for all $p,\tilde q$.

*Proof.* Both sides applied to $\tilde r$ give $pxq$, by associativity.

## The Double Centraliser

**Theorem.** The commutant of the image of the left regular representation in $M_4(F)$ is the image of the right regular representation, and conversely:

$$
\{A\in M_4(F) : A\mathsf{M}_4(\tilde q) = \mathsf{M}_4(\tilde q)A \ \forall \tilde q\} = \{\mathsf{M}_4^{R}(p) : p\in\mathbb{H}\}, \qquad
\{A : A\mathsf{M}_4^{R}(\tilde q) = \mathsf{M}_4^{R}(\tilde q)A \ \forall \tilde q\} = \{\mathsf{M}_4(p) : p\in\mathbb{H}\}.
$$

*Proof.* Every $\mathsf{M}_4^{R}(p)$ commutes with every $\mathsf{M}_4(\tilde q)$, so the right image lies in the commutant of the left image, and the two have the same dimension four; for the reverse inclusion, an $A$ commuting with all $\mathsf{M}_4(\tilde q)$ is determined by its first column $v = Ae_0$ because the columns $Ae_k$ are obtained from $v$ by the action of the left multiplication, and such an $A$ is exactly some $\mathsf{M}_4^{R}(p)$ with $p = v$. The second statement is symmetric.

**Corollary (double centraliser).** The image $L(\mathbb{H})$ of the left regular representation is its own double commutant, it is a simple algebra of dimension four, and its centraliser in $M_4(F)$ is the opposite algebra $\mathsf{M}_4^{R}(\mathbb{H})\cong\mathbb{H}^{\mathrm{op}}$. Over $\mathbb{R}$, the algebra generated by the two images together is all of $M_4(\mathbb{R})$.

*Proof.* The double centraliser theorem for a faithful finite-dimensional simple module gives that the image equals its double commutant; the dimension count $4\cdot4 = 16 = \dim M_4(\mathbb{R})$ shows that the two images together span $M_4(\mathbb{R})$.

## Relation to the Biquaternion $8\times8$ Form

Over the complex field the quaternion algebra becomes the matrix algebra $M_2(\mathbb{C})$, and its regular representation becomes a representation in $\mathsf{M}_2(M_2(\mathbb{C}))\cong M_4(\mathbb{C})$, which is the complex form of the matrix above; regarded as a real representation, it is a four-dimensional complex representation and hence an **eight-dimensional real** one. The biquaternion algebra, which is the complex quaternion algebra, therefore has an $8\times8$ real regular representation into $M_8(\mathbb{R})$, and the $4\times4$ real representation of this article is the restriction of that to the real form $\mathbb{H}$.

| Feature | $\mathbb{H}$ | $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
|---|---|---|
| Regular representation | $L:\mathbb{H}\to M_4(\mathbb{R})$ | $L:\mathbb{B}\to M_8(\mathbb{R})$, equivalently $M_4(\mathbb{C})$ |
| Matrix size over the base | $4\times4$ real | $8\times8$ real, $4\times4$ complex |
| Determinant | $N(\tilde q)^2$, a real square | $N(\tilde Q)^2$, a complex square |
| Trace | $4q_0$ | $4\tilde Q_{\text{scal}}$, complex |
| Transpose | $\mathsf{M}_4(\tilde q)^{T} = \mathsf{M}_4(\tilde{q}^{\natural})$ | $\mathsf{M}_4(\tilde Q)^{T} = \mathsf{M}_4(\tilde{Q}^{\natural})$ |
| Commutant | $\mathsf{M}_4^{R}(\mathbb{H})\cong\mathbb{H}^{\mathrm{op}}$ | $\mathsf{M}_4^{R}(\mathbb{B})\cong\mathbb{B}^{\mathrm{op}}$ |

The pattern is the same in both columns, with the complex field replacing the real one and the matrix size doubling in the real counting; the determinant acquires the complex values of the biquaternion norm, and its vanishing locus is the null cone rather than the origin. The biquaternion account is in *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$*.

## Summary

The left regular representation $L_{\tilde q}(\tilde r) = \tilde q \tilde r$ is an injective algebra homomorphism $\mathbb{H}\to M_4(F)$, whose matrix in the basis $(e_0,e_1,e_2,e_3)$ is the Cayley matrix displayed above; it is the sum $q_0I+\Omega_q$ of a scalar and a skew-symmetric part, it multiplies as the quaternions do, $\mathsf{M}_4(p)\mathsf{M}_4(\tilde q) = \mathsf{M}_4(p\tilde q)$, and it carries units to invertible matrices with $\mathsf{M}_4(\tilde q)^{-1} = \mathsf{M}_4(\tilde{q}^{\natural})/N(\tilde q)$.

The determinant and trace of the Cayley matrix are $\det \mathsf{M}_4(\tilde q) = N(\tilde q)^2$ and $\operatorname{tr}\mathsf{M}_4(\tilde q) = 4q_0$, computed from the identity $\mathsf{M}_4(\tilde q)^{T}\mathsf{M}_4(\tilde q) = N(\tilde q)I$ that also shows $\mathsf{M}_4(\tilde q)$ to be a positive multiple of an orthogonal matrix. Transposition is quaternion conjugation, $\mathsf{M}_4(\tilde q)^{T} = \mathsf{M}_4(\tilde{q}^{\natural})$, and the three involutions of the algebra act by the four sign combinations $\pm \mathsf{M}_4(\tilde q),\pm \mathsf{M}_4(\tilde q)^{T}$ of the Cayley matrix.

The right regular representation $R_{\tilde q}(\tilde r) = \tilde r\tilde q$ is an injective anti-homomorphism with the same determinant and trace, related to the left one by the identity $\mathsf{M}_4^{R}(\tilde q) = D \mathsf{M}_4(\tilde q)^{T} D$ with $D$ the conjugation matrix, and the two representations are each other's commutants; the double centraliser theorem makes the left image its own double commutant and shows the two images together to span $M_4(F)$. After complexification the representation becomes the $8\times8$ real or $4\times4$ complex regular representation of the biquaternion algebra, with the same formal identities and a complex-valued determinant.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $F$ | Base field |
| $e_0 = 1, e_1, e_2, e_3$ | Basis, $e_k^2 = -e_0$ |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | Quaternion, conjugate $\tilde{q}^{\natural}$, norm $N(\tilde q)$ |
| $\mathsf{M}_4(\tilde q)$ | Cayley matrix of left multiplication $\tilde r\mapsto \tilde q \tilde r$ |
| $M_4(\mathbb{R})_L=\operatorname{image}\mathsf{M}_4$ | the regular matrices, the real subspace of dimension $4$ inside $M_4(\mathbb{R})$ |
| $\Omega_q = \mathsf{M}_4(\tilde q) - q_0I$ | Skew-symmetric part of the Cayley matrix |
| $\mathsf{M}_4^{R}(\tilde q)$ | Matrix of right multiplication $\tilde r\mapsto \tilde r\tilde q$ |
| $D = \operatorname{diag}(1,-1,-1,-1)$ | Matrix of conjugation, $\mathsf{M}_4^{R}(\tilde q) = D \mathsf{M}_4(\tilde q)^{T} D$ |
| $\mathsf{M}_4(\tilde q)^{T} = \mathsf{M}_4(\tilde{q}^{\natural})$, $\mathsf{M}_4^{R}(\tilde q)^{T} = \mathsf{M}_4^{R}(\tilde{q}^{\natural})$ | Transposition as conjugation |
| $\det \mathsf{M}_4(\tilde q) = N(\tilde q)^2$, $\operatorname{tr}\mathsf{M}_4(\tilde q) = 4q_0$ | Determinant and trace |
| $\mathsf{M}_4(\tilde q)^{T}\mathsf{M}_4(\tilde q) = N(\tilde q)I$ | Orthogonality up to the quaternion norm scale |
| $\mathbb{H}^{\mathrm{op}}$ | Opposite algebra, the commutant of the left image |
| $M_4(F)$, $M_8(\mathbb{R})$ | Matrix algebras of the real and biquaternion regular representations |
| $\mathbb{B}$ | Biquaternion algebra, the $8\times8$ real case |

## Further Reading

- Arthur Cayley, "A memoir on the theory of matrices", *Philosophical Transactions of the Royal Society of London* **148** (1858) 17–37, for the origin of the regular matrix representation.
- Bartel Leendert van der Waerden, *Algebra*, Vol. II (Springer, 1955), for the regular representation and the double centraliser theorem.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the left and right regular representations of a finite-dimensional algebra.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the double centraliser theorem.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the matrix representations of the quaternion algebra.
