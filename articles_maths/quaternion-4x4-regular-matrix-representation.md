
# __Quaternion 4x4 Regular Matrix Representation__

## Introduction

Every associative algebra acts on itself by left multiplication, and the resulting matrices form the **left regular representation**. For the quaternion algebra this gives an injective algebra homomorphism $\mathbb{H}\to M_4(\mathbb{R})$, the four-dimensional real matrix representation; the matrix of left multiplication by $\tilde q$ is the **Cayley matrix** of $\tilde q$. This article develops that representation: the explicit matrix, its multiplicativity, its determinant and trace, its behaviour under transposition and under the three involutions, the parallel right regular representation, and the double centraliser theorem which identifies the two representations as each other's commutants. It is the quaternion member of the family's regular-representation pair; the counterpart is the $8\times8$ real regular representation of the biquaternion algebra, into which the present one embeds after complexification.

The article depends on *Quaternion Algebra* for the multiplication table and on *Quaternion Norm and Invertibility* for the norm form; the $2\times2$ complex representation, which is obtained by complexification and carries the same information in half the size, is treated in *Quaternion 2x2 Matrix Representation*, and the coordinate form of the multiplication is in *Quaternion Four-Vector Representation*.

The corpus's default base is a commutative ring with identity, and the regular representation is defined over such a base whenever the algebra is faithful over itself; the determinant and norm statements are stated over a field $F$, and the positivity of the norm form is the statement over $\mathbb{R}$.

Throughout, $\mathbb{H}$ is the quaternion algebra with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, $e_1e_2 = e_3$; a quaternion is $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$, written $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ with conjugate $\bar{\tilde q} = q_0 e_0 - q_1 e_1 - q_2 e_2 - q_3 e_3$ and norm form $N(\tilde q) = \tilde q\bar{\tilde q}$; the matrix of left multiplication is $L_q$ and the matrix of right multiplication is $R_q$.

## The Left Regular Representation

**Definition.** The **left regular representation** is the map $L : \mathbb{H}\to\operatorname{End}_F(\mathbb{H})$ sending $\tilde q$ to the endomorphism $L_q(x) = qx$. The **Cayley matrix** of $\tilde q$ is the matrix of $L_q$ in the basis $(e_0,e_1,e_2,e_3)$.

**Theorem.** The map $L$ is an injective algebra homomorphism: $L_{p+\tilde q} = L_p+L_q$, $L_{pq} = L_pL_q$, $L_1 = \mathrm{id}$, and $L$ is injective. Its image is a four-dimensional subalgebra of $M_4(F)$ isomorphic to $\mathbb{H}$.

*Proof.* Left multiplication is $F$-linear, and associativity gives $L_pL_q(x) = p(qx) = (pq)x = L_{pq}(x)$. If $L_q = 0$ then $\tilde q = L_q(1) = 0$, so $L$ is injective; the image is a subalgebra of dimension $\dim\mathbb{H} = 4$. $\square$

**Theorem (Cayley matrix).** For $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$, the Cayley matrix of left multiplication is

$$
L_q = \begin{pmatrix}
q_0 & -q_1 & -q_2 & -q_3 \\
q_1 & q_0 & -q_3 & q_2 \\
q_2 & q_3 & q_0 & -q_1 \\
q_3 & -q_2 & q_1 & q_0
\end{pmatrix}.
$$

*Proof.* The columns are $L_q(e_k) = qe_k$. Direct multiplication gives

$$
qe_0 = \tilde q, \quad qe_1 = -q_1+q_0e_1+q_3e_2-q_2e_3, \quad qe_2 = -q_2-q_3e_1+q_0e_2+q_1e_3, \quad qe_3 = -q_3+q_2e_1-q_1e_2+q_0e_3,
$$

which are the four columns of the displayed matrix. $\square$

**Proposition.** The Cayley matrix is the sum of a scalar and a skew-symmetric part,

$$
L_q = q_0 I + \Omega_q, \qquad \Omega_q = \begin{pmatrix} 0 & -q_1 & -q_2 & -q_3 \\ q_1 & 0 & -q_3 & q_2 \\ q_2 & q_3 & 0 & -q_1 \\ q_3 & -q_2 & q_1 & 0 \end{pmatrix}, \qquad \Omega_q^{T} = -\Omega_q .
$$

*Proof.* Subtract the scalar matrix $q_0I$ from $L_q$; the remainder is the displayed matrix, whose transpose is its negative. $\square$

The decomposition separates the two subspaces: for a scalar $s$ the Cayley matrix is the scalar matrix $L_s = sI$, and for a pure quaternion $\mathbf{q}$ it is $L_{\mathbf{q}} = \Omega_{\mathbf{q}}$, traceless and skew-symmetric. The scalar subspace therefore maps to the scalar matrices and the vector subspace to the traceless skew-symmetric ones.

### A Worked Cayley Matrix

**Example.** For the element

$$
\tilde q = 1+2e_1-e_2+3e_3
$$

the four products $\tilde qe_k$ are

$$
\tilde q e_0 = \tilde q, \quad \tilde q e_1 = -2+e_1+3e_2+e_3, \quad \tilde q e_2 = 1-3e_1+e_2+2e_3, \quad \tilde q e_3 = -3-e_1-2e_2+e_3,
$$

so its Cayley matrix is

$$
L_q = \begin{pmatrix}
1 & -2 & 1 & -3 \\
2 & 1 & -3 & -1 \\
-1 & 3 & 1 & -2 \\
3 & 1 & 2 & 1
\end{pmatrix},
$$

with $L_q^{T}L_q = 15\,I = N(\tilde q)I$, $\det L_q = N(\tilde q)^2 = 225$ and $\operatorname{tr}L_q = 4q_0 = 4$.

## Multiplicativity

**Theorem.** The Cayley matrices multiply as the quaternions do:

$$
L_pL_q = L_{pq}, \qquad L_p+L_q = L_{p+\tilde q}, \qquad L_{\tilde q^{-1}} = L_q^{-1}.
$$

*Proof.* The first two are the homomorphism property; the third follows from $L_qL_{\tilde q^{-1}} = L_{\tilde q \tilde q^{-1}} = L_1 = I$ for an invertible $\tilde q$. $\square$

**Corollary.** The Cayley matrix of a unit quaternion is invertible, and $L_q^{-1} = L_{\bar{\tilde q}}/N(\tilde q)$; in particular the left regular representation restricts to an injective homomorphism of groups $Sp(1)\to O(4)$.

*Proof.* $L_{\bar{\tilde q}/N(\tilde q)} = L_{\bar{\tilde q}}/N(\tilde q)$ and $L_{\bar{\tilde q}}L_q = L_{\bar{\tilde q} \tilde q} = L_{N(\tilde q)} = N(\tilde q)I$, so $L_q^{-1} = L_{\bar{\tilde q}}/N(\tilde q)$. For a unit $N(\tilde q) = 1$ and $L_q^{-1} = L_{\bar{\tilde q}} = L_q^{T}$ by the next theorem, so $L_q\in O(4)$. $\square$

## Determinant and Trace

**Theorem.** For every quaternion,

$$
\det L_q = N(\tilde q)^2 = (q_0^2+q_1^2+q_2^2+q_3^2)^2, \qquad \operatorname{tr}L_q = 4q_0 .
$$

*Proof.* The trace is the sum of the diagonal entries $q_0+q_0+q_0+q_0 = 4q_0$. For the determinant, compute $L_q^{T}L_q$. By the next theorem $L_q^{T} = L_{\bar{\tilde q}}$, so

$$
L_q^{T}L_q = L_{\bar{\tilde q}}L_q = L_{\bar{\tilde q} \tilde q} = L_{N(\tilde q)} = N(\tilde q)\,I,
$$

whence $(\det L_q)^2 = \det(N(\tilde q)I) = N(\tilde q)^4$, and $\det L_q = N(\tilde q)^2$ by the sign check at $\tilde q = 1$, where $L_1 = I$ and $\det = 1 = N(1)^2$. $\square$

**Corollary.** The Cayley matrix of a non-zero quaternion is invertible, and $\det L_q > 0$ for $\tilde q\neq0$; the representation $L$ sends $\mathbb{H}^{\times}$ into $GL_4(F)$, and over $\mathbb{R}$ the determinant is a perfect square.

*Proof.* $\det L_q = N(\tilde q)^2\neq0$ for $\tilde q\neq0$ by the unit criterion, and the square of a non-zero real number is positive. $\square$

**Remark.** The identity $L_q^{T}L_q = N(\tilde q)I$ says that $L_q$ is $\sqrt{N(\tilde q)}$ times an orthogonal matrix; on the unit sphere the map $\tilde q\mapsto L_q$ is then a homomorphism $Sp(1)\to SO(4)$, the left-translation factor of the two-sided covering $Sp(1)\times Sp(1)\to SO(4)$ of *Quaternion Operator Representation* in matrix form, whose other factor is the right regular representation.

## Transposition and the Conjugations

**Theorem.** Transposition of the Cayley matrix is quaternion conjugation:

$$
L_q^{T} = L_{\bar{\tilde q}}.
$$

*Proof.* The transpose of the displayed matrix is obtained by interchanging rows and columns; comparing entrywise with $L_{\bar{\tilde q}}$, the diagonal is unchanged and each off-diagonal entry changes sign in the pattern $-q_1,-q_2,-q_3$ exactly as conjugation negates the vector part. $\square$

**Theorem.** The three involutions of the algebra act on the Cayley matrix by

$$
L_{\bar{\tilde q}} = L_q^{T}, \qquad L_{-\bar{\tilde q}} = -L_q^{T}, \qquad L_{-\tilde q} = -L_q,
$$

and the identity involution gives $L_q$ itself.

*Proof.* The first is the transposition theorem; the second follows from linearity, $L_{-\bar{\tilde q}} = -L_{\bar{\tilde q}} = -L_q^T$; the third likewise, $L_{-\tilde q} = -L_q$. $\square$

**Corollary.** The left regular representation identifies the four linear involutions $\tilde q\mapsto \tilde q,\ \bar{\tilde q},\ -\bar{\tilde q},\ -\tilde q$ with the four matrices $\pm L_q,\ \pm L_q^{T}$, and the fixed spaces of the involutions are the $\pm1$ eigenspaces of these matrices, in agreement with *The Scalar and Vector Subspaces of $\mathbb{H}$*.

## The Right Regular Representation

**Definition.** The **right regular representation** is $R : \mathbb{H}\to M_4(F)$ with $R_q(x) = xq$.

**Theorem.** The map $R$ is an injective algebra anti-homomorphism, $R_{pq} = R_qR_p$, and the matrix of right multiplication is

$$
R_q = \begin{pmatrix}
q_0 & -q_1 & -q_2 & -q_3 \\
q_1 & q_0 & q_3 & -q_2 \\
q_2 & -q_3 & q_0 & q_1 \\
q_3 & q_2 & -q_1 & q_0
\end{pmatrix}.
$$

*Proof.* $(R_pR_q)(x) = R_p(xq) = xqp = R_{qp}(x)$, so $R_{pq} = R_qR_p$. The columns are $R_q(e_k) = e_kq$, computed directly as

$$
e_0\tilde q = \tilde q, \quad e_1\tilde q = -q_1+q_0e_1-q_3e_2+q_2e_3, \quad e_2\tilde q = -q_2+q_3e_1+q_0e_2-q_1e_3, \quad e_3\tilde q = -q_3-q_2e_1+q_1e_2+q_0e_3 . \square
$$

**Theorem.** The right representation has the same determinant and trace,

$$
\det R_q = N(\tilde q)^2, \qquad \operatorname{tr}R_q = 4q_0,
$$

and it satisfies $R_q^{T} = R_{\bar{\tilde q}}$ together with the relation

$$
R_q = D\,L_q^{T}\,D, \qquad D = \operatorname{diag}(1,-1,-1,-1),
$$

where $D$ is the matrix of quaternion conjugation.

*Proof.* The trace is $4q_0$ from the diagonal. The relation $R_q^{T} = R_{\bar{\tilde q}}$ is the same entrywise comparison as for $L$. For the last identity, $D$ is the matrix of the linear map $x\mapsto\bar x$, so for every $x$,

$$
D L_q^{T} D x = D L_{\bar{\tilde q}} D x = D\bigl(\bar{\tilde q}\,\bar x\bigr) = \overline{\bar{\tilde q}\,\bar x} = xq = R_q\,x,
$$

using $L_q^{T} = L_{\bar{\tilde q}}$ and the reversal $\overline{\tilde q_1\tilde q_2} = \bar{\tilde q}_2\,\bar{\tilde q}_1$ of conjugation. Hence $R_q = D L_q^{T} D$, and the determinant is that of $L_q$ because $D^2 = I$. $\square$

**Proposition.** The left and right representations commute: $L_pR_q = R_qL_p$ for all $p,\tilde q$.

*Proof.* Both sides applied to $x$ give $pxq$, by associativity. $\square$

## The Double Centraliser

**Theorem.** The commutant of the image of the left regular representation in $M_4(F)$ is the image of the right regular representation, and conversely:

$$
\{A\in M_4(F) : AL_q = L_qA \ \forall \tilde q\} = \{R_p : p\in\mathbb{H}\}, \qquad
\{A : AR_q = R_qA \ \forall \tilde q\} = \{L_p : p\in\mathbb{H}\}.
$$

*Proof.* Every $R_p$ commutes with every $L_q$, so the right image lies in the commutant of the left image, and the two have the same dimension four; for the reverse inclusion, an $A$ commuting with all $L_q$ is determined by its first column $v = Ae_0$ because the columns $Ae_k$ are obtained from $v$ by the action of the left multiplication, and such an $A$ is exactly some $R_p$ with $p = v$. The second statement is symmetric. $\square$

**Corollary (double centraliser).** The image $L(\mathbb{H})$ of the left regular representation is its own double commutant, it is a simple algebra of dimension four, and its centraliser in $M_4(F)$ is the opposite algebra $R(\mathbb{H})\cong\mathbb{H}^{\mathrm{op}}$. Over $\mathbb{R}$, the algebra generated by the two images together is all of $M_4(\mathbb{R})$.

*Proof.* The double centraliser theorem for a faithful finite-dimensional simple module gives that the image equals its double commutant; the dimension count $4\cdot4 = 16 = \dim M_4(\mathbb{R})$ shows that the two images together span $M_4(\mathbb{R})$. $\square$

## Relation to the Biquaternion $8\times8$ Form

Over the complex field the quaternion algebra becomes the matrix algebra $M_2(\mathbb{C})$, and its regular representation becomes a representation in $M_2(M_2(\mathbb{C}))\cong M_4(\mathbb{C})$, which is the complex form of the matrix above; regarded as a real representation, it is a four-dimensional complex representation and hence an **eight-dimensional real** one. The biquaternion algebra, which is the complex quaternion algebra, therefore has an $8\times8$ real regular representation into $M_8(\mathbb{R})$, and the $4\times4$ real representation of this article is the restriction of that to the real form $\mathbb{H}$.

| Feature | $\mathbb{H}$ | $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
|---|---|---|
| Regular representation | $L:\mathbb{H}\to M_4(\mathbb{R})$ | $L:\mathbb{B}\to M_8(\mathbb{R})$, equivalently $M_4(\mathbb{C})$ |
| Matrix size over the base | $4\times4$ real | $8\times8$ real, $4\times4$ complex |
| Determinant | $N(\tilde q)^2$, a real square | $N(\tilde Q)^2$, a complex square |
| Trace | $4q_0$ | $4\tilde Q_{\text{scal}}$, complex |
| Transpose | $L_q^{T} = L_{\bar{\tilde q}}$ | $L_{\tilde Q}^{T} = L_{\bar{\tilde Q}}$ |
| Commutant | $R(\mathbb{H})\cong\mathbb{H}^{\mathrm{op}}$ | $R(\mathbb{B})\cong\mathbb{B}^{\mathrm{op}}$ |

The pattern is the same in both columns, with the complex field replacing the real one and the matrix size doubling in the real counting; the determinant acquires the complex values of the biquaternion norm form, and its vanishing locus is the null cone rather than the origin. The biquaternion account is in *Biquaternion 4x4 Regular Matrix Representation*.

## Summary

The left regular representation $L_q(x) = qx$ is an injective algebra homomorphism $\mathbb{H}\to M_4(F)$, whose matrix in the basis $(e_0,e_1,e_2,e_3)$ is the Cayley matrix displayed above; it is the sum $q_0I+\Omega_q$ of a scalar and a skew-symmetric part, it multiplies as the quaternions do, $L_pL_q = L_{pq}$, and it carries units to invertible matrices with $L_q^{-1} = L_{\bar{\tilde q}}/N(\tilde q)$.

The determinant and trace of the Cayley matrix are $\det L_q = N(\tilde q)^2$ and $\operatorname{tr}L_q = 4q_0$, computed from the identity $L_q^{T}L_q = N(\tilde q)I$ that also shows $L_q$ to be a positive multiple of an orthogonal matrix. Transposition is quaternion conjugation, $L_q^{T} = L_{\bar{\tilde q}}$, and the three involutions of the algebra act by the four sign combinations $\pm L_q,\pm L_q^{T}$ of the Cayley matrix.

The right regular representation $R_q(x) = xq$ is an injective anti-homomorphism with the same determinant and trace, related to the left one by the identity $R_q = D L_q^{T} D$ with $D$ the conjugation matrix, and the two representations are each other's commutants; the double centraliser theorem makes the left image its own double commutant and shows the two images together to span $M_4(F)$. After complexification the representation becomes the $8\times8$ real or $4\times4$ complex regular representation of the biquaternion algebra, with the same formal identities and a complex-valued determinant.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra |
| $F$ | Base field |
| $e_0 = 1, e_1, e_2, e_3$ | Basis, $e_k^2 = -e_0$ |
| $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$ | Quaternion, conjugate $\bar{\tilde q}$, norm form $N(\tilde q)$ |
| $L_q$ | Cayley matrix of left multiplication $x\mapsto qx$ |
| $\Omega_q = L_q - q_0I$ | Skew-symmetric part of the Cayley matrix |
| $R_q$ | Matrix of right multiplication $x\mapsto xq$ |
| $D = \operatorname{diag}(1,-1,-1,-1)$ | Matrix of conjugation, $R_q = D L_q^{T} D$ |
| $L_q^{T} = L_{\bar{\tilde q}}$, $R_q^{T} = R_{\bar{\tilde q}}$ | Transposition as conjugation |
| $\det L_q = N(\tilde q)^2$, $\operatorname{tr}L_q = 4q_0$ | Determinant and trace |
| $L_q^{T}L_q = N(\tilde q)I$ | Orthogonality up to the norm scale |
| $\mathbb{H}^{\mathrm{op}}$ | Opposite algebra, the commutant of the left image |
| $M_4(F)$, $M_8(\mathbb{R})$ | Matrix algebras of the real and biquaternion regular representations |
| $\mathbb{B}$ | Biquaternion algebra, the $8\times8$ real case |

## Further Reading

- Arthur Cayley, "A memoir on the theory of matrices", *Philosophical Transactions of the Royal Society of London* **148** (1858) 17–37, for the origin of the regular matrix representation.
- Bartel Leendert van der Waerden, *Algebra*, Vol. II (Springer, 1955), for the regular representation and the double centraliser theorem.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the left and right regular representations of a finite-dimensional algebra.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the double centraliser theorem.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the matrix representations of the quaternion algebra.
