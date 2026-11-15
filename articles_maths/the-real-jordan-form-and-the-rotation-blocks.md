# __The Real Jordan Form and the Rotation Blocks__

## Introduction

**A nonreal eigenvalue cannot be isolated over $\mathbb{R}$, so the real Jordan form carries the conjugate pair as one block, and that block is a rotation composed with a dilation.** The block is built from the matrix $C$ of the multiplication by $a+bi$ on $\mathbb{C}=\mathbb{R}^{2}$, with the identity in the superdiagonal position exactly where the complex form has $1$.

The article constructs the block $R_d(a,b)$, states the real Jordan theorem and its uniqueness, identifies the block with a pair of conjugate complex Jordan blocks, reads the angle and the dilation off $a$ and $b$, computes the minimal polynomial of $R_1$, proves that $R_2$ is not conjugate to two copies of $R_1$, computes the determinant and the trace, treats the degenerate cases $b=0$ and $a=0$, lists the canonical forms at $n=2$ and $n=4$, and relates the real form to the complex form by complexification. It assumes *The Minimal Polynomial over $\mathbb{R}$ and the Real Jordan Form*, where the existence and the uniqueness of the real form are proved, and *The Real Spectrum: Real Roots and Conjugate Pairs* for the count of the blocks.

## The Rotation Block

**Definition.** For $a,b\in\mathbb{R}$ and $d\ge1$ put

$$
C=C(a,b)=\begin{pmatrix}a&-b\\ b&a\end{pmatrix},
$$

and let $R_d(a,b)$ be the $2d\times2d$ matrix with $d$ copies of $C$ on the diagonal and $\mathrm{I}_2$ in the superdiagonal block positions:

$$
R_d(a,b)=\begin{pmatrix}C&\mathrm{I}_2&&\\&\ddots&\ddots&\\&&\ddots&\mathrm{I}_2\\&&&C\end{pmatrix}.
$$

The matrix $R_d(a,b)$ is the **rotation block** of size $2d$ for the pair $a\pm bi$. Every entry is real, and the size is twice the size $d$ of the corresponding complex block, because the real form carries both members of the pair.

## The Real Jordan Theorem

**Theorem.** Every $A\in M_n(\mathbb{R})$ is similar over $\mathbb{R}$ to a direct sum of blocks $J_d(\lambda)$ with $\lambda\in\mathbb{R}$ and $R_d(a,b)$ with $b\ne0$, and the list of blocks is unique up to the order of the summands.

**The proof is in the sibling article.** The existence and the uniqueness are proved in *The Minimal Polynomial over $\mathbb{R}$ and the Real Jordan Form* by complexifying, taking the complex Jordan form, and grouping the blocks for $\mu$ and $\bar\mu$. This article takes the theorem and reads the block itself.

**Uniqueness fixes the data of a block.** For a real block the eigenvalue is fixed, and for a rotation block the pair is fixed, with $b$ replaced by $|b|$ because $R_d(a,-b)$ is similar to $R_d(a,b)$. The conjugating matrix is

$$
D=\operatorname{diag}(1,-1,1,-1,\dots),
$$

and $D\,C(a,-b)\,D^{-1}=C(a,b)$ while $D\,\mathrm{I}_2\,D^{-1}=\mathrm{I}_2$. So the normal form may be taken with $b>0$, and the pair is unordered: $\{a+bi,a-bi\}$ is the data.

## The Block as a Pair of Complex Blocks

**The complexification of $R_d(a,b)$ is a pair of Jordan blocks.** Regard $R_d(a,b)$ as a complex matrix. Then

$$
R_d(a,b)\ \sim_{\mathbb{C}}\ J_d(\mu)\oplus J_d(\bar\mu),\qquad \mu=a+bi .
$$

*Proof.* In the real basis $e_1,\dots,e_{2d}$ of the block, the pairs $(e_{2k-1},e_{2k})$ span copies of $\mathbb{C}$, and $R_d$ acts on each copy by $\mu$ and moves from the $k$-th copy to the $(k+1)$-th by the identity. The vectors $v_k=e_{2k-1}+ie_{2k}$ are then a Jordan chain of length $d$ for $\mu$, since $R_dv_k=\mu v_k+v_{k+1}$ with $v_{d+1}=0$; the conjugates $\bar v_k$ are a chain for $\bar\mu$. Together they span $\mathbb{C}^{2d}$.

**The two blocks have the same size.** A real matrix cannot have a block for $\mu$ without the block of the same size for $\bar\mu$, which is why the real form is a single object of size $2d$.

**The spectrum of the block is the pair with multiplicity $d$.** For $a=1.3$ and $b=0.7$ the eigenvalues of $R_2(1.3,0.7)$ are $1.3+0.7i$ twice and $1.3-0.7i$ twice, computed numerically.

**Complexification is the bridge in both directions.** The real Jordan form complexifies to the complex Jordan form, block by block: $J_d(\lambda)$ stays itself and $R_d(a,b)$ becomes $J_d(\mu)\oplus J_d(\bar\mu)$. Conversely, a complex Jordan form stable under conjugation, in the sense that the blocks for $\mu$ and $\bar\mu$ have the same size, is the complexification of a real form. So the real classes are exactly the conjugation-stable complex classes.

## The Angle and the Dilation

**The block $C$ is a dilation composed with a rotation.** Put

$$
r=\sqrt{a^{2}+b^{2}},\qquad \cos\theta=\frac{a}{r},\qquad \sin\theta=\frac{b}{r},
$$

so that $r>0$ and $\theta$ is determined modulo $2\pi$ when $b\ne0$. Then

$$
C=r\begin{pmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{pmatrix}=r\,\mathrm{Rot}(\theta).
$$

**The two factors both are visible in the entries.** The dilation is the scalar $r$ and the rotation is the orthogonal matrix $\mathrm{Rot}(\theta)\in\mathrm{SO}(2)$.

**The block satisfies its characteristic polynomial in the strong form.** Since $C=r\,\mathrm{Rot}(\theta)$ and $\mathrm{Rot}(\theta)^{2}-2\cos\theta\,\mathrm{Rot}(\theta)+\mathrm{I}=0$,

$$
C^{2}-2aC+r^{2}\mathrm{I}_2=0.
$$

The identity is the reason the rotation block is the right real replacement for a complex eigenvalue: it encodes $\mu$ and $\bar\mu$ at once. The powers read $C^{k}=r^{k}\mathrm{Rot}(k\theta)$, so the block spirals with ratio $r$ per step and angle $\theta$.

## The Minimal Polynomial of $R_1$

**The minimal polynomial of $R_1(a,b)$ is $(t-a)^{2}+b^{2}$ when $b\ne0$.** The matrix $R_1(a,b)=C$ is $2\times2$, its characteristic polynomial is $(t-a)^{2}+b^{2}$, and the polynomial is irreducible over $\mathbb{R}$ for $b\ne0$, so it has no factor of degree one to annihilate $C$. Hence $m_C=\chi_C$ and $\deg m_C=2$; numerically the matrix $(C-a\mathrm{I})^{2}+b^{2}\mathrm{I}$ is zero.

**The block is nonderogatory.** Since $m_C=\chi_C$, the algebra $\mathbb{R}[C]$ has dimension $2$ and is the commutant of $C$ in $M_2(\mathbb{R})$. As a real algebra it is $\mathbb{C}$, generated by $C$ with $C^{2}=2aC-r^{2}\mathrm{I}$.

**The minimal polynomial of $R_d$ is the $d$-th power.** For $d\ge1$,

$$
m_{R_d}(t)=\bigl((t-a)^{2}+b^{2}\bigr)^{d},
$$

because the largest block for $\mu$ has size $d$ and its conjugate has size $d$. For $d=1$ this is the quadratic, for $d=2$ the square of the quadratic of degree $4$, and so on; numerically the degree of the minimal polynomial of $R_2(1.3,0.7)$ is $4$ and that of $R_3$ is $6$.

## The Repeated Pair: $R_2$ against Two Copies

**The block $R_2(a,b)$ is not conjugate to two copies of $R_1(a,b)$.** The two matrices are

$$
R_2(a,b)=\begin{pmatrix}C&\mathrm{I}\\ 0&C\end{pmatrix},\qquad C\oplus C=\begin{pmatrix}C&0\\ 0&C\end{pmatrix},
$$

of the same size $4$, with the same characteristic polynomial $\bigl((t-a)^{2}+b^{2}\bigr)^{2}$ and the same spectrum. They are nevertheless in different conjugacy classes.

*Proof.* The minimal polynomial is a similarity invariant. For $C\oplus C$ the polynomial $(t-a)^{2}+b^{2}$ annihilates each summand, so $m_{C\oplus C}=(t-a)^{2}+b^{2}$ of degree $2$. For $R_2$ the polynomial $P=(t-a)^{2}+b^{2}$ does not annihilate the block: at $t$ replaced by $R_2$,

$$
(R_2-a\mathrm{I})^{2}+b^{2}\mathrm{I}=\begin{pmatrix}0&2bJ\\ 0&0\end{pmatrix},
$$

with $J=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$. That matrix has rank $2$, not $0$, so $P$ is not annihilating and the minimal polynomial of $R_2$ is $P^{2}$ of degree $4$. Two matrices with minimal polynomials of different degrees are not similar.

**The rank of the polynomial is the numerical test.** With $a=1.3$ and $b=0.7$ the rank of $P(R_2)$ is $2$ and the rank of $P(C\oplus C)$ is $0$; the nullities are $2$ and $4$. Over $\mathbb{C}$ the same difference appears as a difference of geometric multiplicities: the rank of $R_2-\mu\mathrm{I}$ is $3$, so $\mu$ has geometric multiplicity $1$, while the rank of $(C\oplus C)-\mu\mathrm{I}$ is $2$, so $\mu$ has geometric multiplicity $2$.

**The difference is the size of the largest block.** Two copies of $R_1$ give two blocks of size one for $\mu$; the block $R_2$ gives one block of size two. The characteristic polynomial does not see the difference and the minimal polynomial does. In the real form, the superdiagonal identity is exactly what merges the two chains.

## The Determinant and the Trace of $R_d$

**Proposition.**

$$
\det R_d(a,b)=\bigl(a^{2}+b^{2}\bigr)^{d},\qquad \operatorname{tr}R_d(a,b)=2da .
$$

*Proof.* The matrix is block triangular with $d$ diagonal blocks $C$, so its determinant is $(\det C)^{d}=(a^{2}+b^{2})^{d}$ and its trace is $d\operatorname{tr}C=2da$. The superdiagonal identities do not contribute to either.

**The determinant is positive and the trace is the sum of the real parts.** The determinant is the product of $|\mu|^{2}$ over the $d$ copies, hence positive; the trace is $2d\operatorname{Re}\mu$. At $a=1.3$ and $b=0.7$ the determinants for $d=1,2,3,4$ are $2.18$, $4.7524$, $10.360232$ and $22.58530576$, equal to $(a^{2}+b^{2})^{d}$ each time, and the traces are $2.6$, $5.2$, $7.8$ and $10.4$, equal to $2da$. So no rotation block can make a matrix singular: the only source of a zero determinant is a real eigenvalue equal to zero.

## The Two Degenerate Cases

**At $b=0$ the block collapses to two Jordan blocks.** With $b=0$ the block is

$$
R_d(a,0)=\begin{pmatrix}a\mathrm{I}_2&\mathrm{I}_2&&\\&\ddots&\ddots&\\&&\ddots&\mathrm{I}_2\\&&&a\mathrm{I}_2\end{pmatrix},
$$

and its nilpotent part $N=R_d(a,0)-a\mathrm{I}_{2d}$ has rank $2(d-1)$ and nilpotency index $d$. Hence

$$
R_d(a,0)\ \sim\ J_d(a)\oplus J_d(a).
$$

Numerically the ranks of $N$ for $d=1,2,3,4$ are $0,2,4,6$, and $N^{2}\ne0$ as soon as $d\ge3$. So the limit $b\to0$ is not the single Jordan block $J_{2d}(a)$: it is the pair of equal blocks of size $d$. The real Jordan form needs $b\ne0$ precisely because the rotation block is the only way to keep a single block of size $2d$ attached to a conjugate pair.

**At $d=1$ the degeneration is the scalar.** $R_1(a,0)=a\mathrm{I}_2$ has the eigenvalue $a$ with multiplicity $2$ and two blocks of size one.

**At $a=0$ the block is a rotation composed with a stretch.** Then

$$
C(0,b)=b\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}=bJ,
$$

with $J^{2}=-\mathrm{I}$. The factor $b$ is a dilation and $J$ is the rotation by $\pi/2$. At $b=1$ and $d=1$ the block is $J$ itself, which is orthogonal with determinant $1$; for $|b|\ne1$ it is a similarity of ratio $|b|$ and angle $\pi/2$, neither orthogonal nor a scalar.

## The Canonical Lists at $n=2$ and $n=4$

**At $n=2$ the list is short.** Every real $2\times2$ matrix is similar to exactly one of

$$
J_1(\lambda),\qquad J_2(\lambda),\qquad R_1(a,b)\ \text{with}\ b>0 .
$$

The first is the scalar $\lambda\mathrm{I}$, the second is the nontrivial Jordan block for a real eigenvalue, and the third is the rotation block for a pair.

**At $n=4$ the list is organised by the number of real eigenvalues.** The possibilities are:

- four real eigenvalues: $J_4(\lambda)$, $J_3(\lambda)\oplus J_1(\mu)$, $J_2(\lambda)\oplus J_2(\mu)$, $J_2(\lambda)\oplus J_1(\mu)\oplus J_1(\nu)$ and four blocks $J_1$, with equal labels for equal eigenvalues and distinct labels for distinct ones;
- two real eigenvalues and one pair: $R_2(a,b)$ alone, $R_1(a,b)\oplus J_2(\lambda)$, and $R_1(a,b)\oplus J_1(\lambda)\oplus J_1(\mu)$;
- two pairs: $R_1(a,b)\oplus R_1(c,d)$, with distinct or equal pairs.

**The list is unique up to order and up to $b\mapsto|b|$.** Each block contributes its eigenvalue or its pair and its size; the order of the summands is free, the sign of $b$ is free by the diagonal $D$, and nothing else is.

## Summary

The rotation block $R_d(a,b)$ is built from $C(a,b)$ and the identity in the superdiagonal position, and it is the real form of a pair $\mu,\bar\mu$ of Jordan blocks of size $d$. The block is a dilation of ratio $r=\sqrt{a^{2}+b^{2}}$ composed with a rotation of angle $\theta$ with $\cos\theta=a/r$ and $\sin\theta=b/r$. Its minimal polynomial is $\bigl((t-a)^{2}+b^{2}\bigr)^{d}$, which is $(t-a)^{2}+b^{2}$ at $d=1$, so $R_2$ is not conjugate to two copies of $R_1$ although the characteristic polynomials agree. Its determinant is $(a^{2}+b^{2})^{d}$ and its trace is $2da$. At $b=0$ it degenerates to $J_d(a)\oplus J_d(a)$, and at $a=0$ it is a rotation composed with a stretch. Complexification recovers the complex Jordan form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $C(a,b)$ | the $2\times2$ block $\begin{pmatrix}a&-b\\ b&a\end{pmatrix}$ |
| $R_d(a,b)$ | the rotation block of size $2d$ |
| $J_d(\lambda)$ | the Jordan block of size $d$ for the real eigenvalue $\lambda$ |
| $\mu=a+bi$ | the eigenvalue carried by the block |
| $r,\theta$ | the dilation $\sqrt{a^{2}+b^{2}}$ and the angle |
| $J$ | the rotation $\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$ |
| $m_A$ | the minimal polynomial |
| $D$ | the diagonal $\operatorname{diag}(1,-1,1,-1,\dots)$ that flips the sign of $b$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the real Jordan form and the rotation blocks.
- F. R. Gantmacher, *The Theory of Matrices* (Chelsea, 1959), for the uniqueness of the real form and its relation to the complex form.
- [The Minimal Polynomial over $\mathbb{R}$ and the Real Jordan Form](the-minimal-polynomial-over-r-and-the-real-jordan-form.html), for the existence and the uniqueness of the decomposition.
- [The Real Spectrum: Real Roots and Conjugate Pairs](the-real-spectrum-real-roots-and-conjugate-pairs.html), for the count $r+2s=n$ behind the list of blocks.
- [Normal Matrices over $\mathbb{R}$ and the Orthogonal Spectral Theorem](normal-matrices-over-r-and-the-orthogonal-spectral-theorem.html), for the case where the blocks are orthogonal.
