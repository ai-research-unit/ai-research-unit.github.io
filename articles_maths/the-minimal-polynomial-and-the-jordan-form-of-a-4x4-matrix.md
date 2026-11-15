# __The Minimal Polynomial and the Jordan Form of a $4\times4$ Matrix__

## Introduction

**The minimal polynomial divides the characteristic polynomial, has the same roots, and equals it exactly when the matrix has a cyclic vector; at order four there are five Jordan shapes, and only two of them occur among the one-sided matrices of the biquaternion algebra.**

The article proves $\mu_A\mid\chi_A$ and the equality with the cyclic condition, lists the five partitions of $4$ with the shapes $4$, $3+1$, $2+2$, $2+1+1$ and $1+1+1+1$, builds the companion matrix whose minimal polynomial has degree four, splits any matrix as $S+N$ with commuting semisimple and nilpotent parts, and computes the axis-free spectrum: the two eigenvalues $Q_t\pm iB$, each twice, so the minimal polynomial has degree at most two.

It assumes *The Matrix Algebra $M_4(\mathbb{C})$* and *The Elementary Symmetric Functions and $\det(\mathrm{I}+tA)$ at $n=4$* for the characteristic polynomial. The case $n=2$ is *The Minimal Polynomial and the Two Jordan Regimes of $M_2(\mathbb{C})$*. The spectral consequences are *Normal Matrices and the Common Spectral Theorem at $n=4$*.

## The Minimal Polynomial

**Definition.** The **minimal polynomial** $\mu_A$ is the monic polynomial of least degree with $\mu_A(A)=0$.

**Proposition.** $\mu_A$ exists, is unique, divides every polynomial that annihilates $A$, and its roots are exactly the eigenvalues of $A$.

**Proof.** The powers $\mathrm I,A,\dots,A^{4}$ span a space of dimension at most $16$, so some nontrivial combination vanishes and a monic polynomial of least degree exists; division with remainder makes it divide every annihilator. If $\mu_A(\lambda)\neq0$ at an eigenvalue $\lambda$ with eigenvector $v$, then $0=\mu_A(A)v=\mu_A(\lambda)v$, a contradiction; conversely each eigenvalue is a root of $\chi_A$ and $\mu_A\mid\chi_A$, so the roots agree.

**Corollary.** $\deg\mu_A\le4$ and $\mu_A$ is the product $\prod_\lambda(X-\lambda)^{m(\lambda)}$, where $m(\lambda)$ is the size of the largest Jordan block with eigenvalue $\lambda$.

**Proof.** On a Jordan block of size $m$ the polynomial $(X-\lambda)^{m}$ kills the nilpotent part $(J-\lambda\mathrm I)^{m}=0$, and no smaller power does; the least common multiple over the blocks is the display.

**Proposition (the degrees and the shapes).** The degree of $\mu_A$ is the largest total size of the blocks sharing one eigenvalue, so $\deg\mu_A=4$ exactly when the sum of the block sizes for some one eigenvalue is $4$.

**Proof.** Read the previous corollary: the exponent for $\lambda$ is the largest block size at $\lambda$, and the degree is the sum of the exponents over the distinct eigenvalues.

## The Five Shapes at Order Four

**Definition.** The **Jordan type** of $A$ is the partition of $4$ given by the sizes of its Jordan blocks, with the eigenvalues attached.

**The five partitions.** For a matrix with a single eigenvalue there are exactly five types:

| Type | Blocks | $\deg\mu_A$ | $\dim$ centraliser |
|---|---|---|---|
| $4$ | one block of size $4$ | $4$ | $4$ |
| $3+1$ | blocks $3$ and $1$ | $3$ | $6$ |
| $2+2$ | two blocks of size $2$ | $2$ | $8$ |
| $2+1+1$ | blocks $2,1,1$ | $2$ | $7$ |
| $1+1+1+1$ | scalars | $1$ | $16$ |

**Proposition.** These five exhaust the partitions of $4$, and the centraliser of a nilpotent with blocks $b_1\ge\cdots\ge b_k$ has dimension $\sum_{i,j}\min(b_i,b_j)$.

**Proof.** The partitions of $4$ are $4$, $3+1$, $2+2$, $2+1+1$, $1+1+1+1$. A block matrix commuting with the nilpotent has, in the block from $j$ to $i$, a matrix that is constant on the diagonals and vanishes above the shorter block, so it contributes $\min(b_i,b_j)$ parameters; summing over the pairs gives the formula. The five values are $4$, $3+1+1+1=6$, $2+2+2+2=8$, $2+1+1+1+1+1=7$, and $16$.

**The count of types with distinct eigenvalues.** When the four eigenvalues are distinct only the type $1+1+1+1$ occurs. When there are two eigenvalues of multiplicities $2$ and $2$, the shapes are $2+2$, $2+1+1$ and $1+1+1+1$ within each group, and similarly for the other splits.

## The Companion Matrix and the Cyclic Vector

**Definition.** A vector $v$ is **cyclic** for $A$ when $v,Av,A^{2}v,A^{3}v$ are a basis.

**Theorem.** The following are equivalent: $A$ has a cyclic vector; $\deg\mu_A=4$; $\mu_A=\chi_A$; the centraliser of $A$ is the algebra $\mathbb{C}[A]$, of dimension $4$.

**Proof.** If $v$ is cyclic, the four vectors $v,\dots,A^{3}v$ are independent, so no polynomial of degree at most $3$ kills $A$, hence $\deg\mu_A=4$ and $\mu_A=\chi_A$ by the bound on the degree. Conversely if $\deg\mu_A=4$, the vector $v$ with $\mu_A(A)v=0$ of least degree has an annihilator of degree $4$, so it is cyclic. A matrix commuting with $A$ is determined by its value on a cyclic vector, which lies in $\mathbb{C}[A]$.

**Definition.** The **companion matrix** of $p(X)=X^{4}-c_1X^{3}-c_2X^{2}-c_3X-c_4$ is

$$
C_p=\begin{pmatrix}0&0&0&c_4\\ 1&0&0&c_3\\ 0&1&0&c_2\\ 0&0&1&c_1\end{pmatrix}.
$$

**Proposition.** $\chi_{C_p}=p=\mu_{C_p}$, and the first standard basis vector is cyclic.

**Proof.** Expand $\det(X\mathrm I-C_p)$ along the last column, or note that $C_pe_1=e_2$, $C_pe_2=e_3$, $C_pe_3=e_4$, so that the four vectors $e_1,\dots,e_4$ are the Krylov chain of $e_1$; the relation $C_p^{4}=c_1C_p^{3}+c_2C_p^{2}+c_3C_p+c_4\mathrm I$ is read off the last column, and no shorter relation holds because the chain is a basis.

**Corollary.** Every matrix of order four is similar to a companion matrix or to a direct sum of companion matrices of smaller degree, the rational canonical form.

**Proof.** Decompose the space into the cyclic subspaces generated by a vector of maximal annihilator and iterate on a complement; each summand is companion.

## The Decomposition $S+N$

**Theorem (Jordan–Chevalley).** Every $A$ is uniquely $S+N$ with $S$ semisimple, $N$ nilpotent, $SN=NS$, and both $S$ and $N$ polynomials in $A$ with zero constant term.

**Proof.** Put $A$ in Jordan form, take $S$ the diagonal part and $N$ the strictly upper part; they commute and $N^{4}=0$. Uniqueness follows because a polynomial relation between two commuting semisimple and nilpotent parts forces each to vanish, and existence as polynomials in $A$ follows by the Chinese remainder theorem applied to the coprime factors $(X-\lambda)^{m(\lambda)}$ of $\mu_A$.

**Corollary.** $A$ is diagonalisable exactly when $N=0$, that is when $\mu_A$ has only simple roots.

**Proof.** A diagonalisable matrix is its own semisimple part; conversely $S$ is diagonalisable and $N=0$ leaves $A=S$.

**Corollary.** For every $A$ of order four, $N^{4}=0$, and the exponent of $N$ is the largest block size minus one.

**Proof.** The nilpotent part has blocks of size at most $4$, so its fourth power vanishes, and a block of size $m$ needs the exponent $m-1$.

## The Axis-Free Spectrum

**The two eigenvalues.** Write $\tilde Q=Q_te_t+\vec v$ with $\vec v=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ and put $B^{2}=-\vec v^{\,2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$. The spectrum of the left matrix is

$$
\operatorname{spec}L_{\mathrm{axf}}(\tilde Q)=\{Q_t+iB,\;Q_t+iB,\;Q_t-iB,\;Q_t-iB\}.
$$

**Proposition.** The minimal polynomial of $L_{\mathrm{axf}}(\tilde Q)$ has degree at most two, namely $\mu=(X-Q_t)^{2}-(iB)^{2}=(X-Q_t)^{2}+B^{2}$ when $B\neq0$ and $\mu=X-Q_t$ when $\tilde Q=Q_te_t$.

**Proof.** The algebra $\mathbb{B}$ is $M_2(\mathbb{C})$, so every element satisfies its characteristic polynomial of degree two, and the left regular representation is a homomorphism; the two eigenvalues are then the roots of that quadratic. When $B\neq0$ the roots are distinct and $\mu$ has degree two; when $\vec v=0$ the element is scalar.

**Corollary (only two shapes occur).** A one-sided matrix is diagonalisable when $B\neq0$, with the type $1+1+1+1$; it has the type $2+2$ with the single eigenvalue $Q_t$ when $B=0$ and $\tilde Q\neq Q_te_t$; and it is a scalar when $\tilde Q=Q_te_t$.

**Proof.** Distinct roots give simple blocks. In the isotropic case $B=0$ with $\vec v\neq0$ one has $\vec v^{\,2}=0$, so $L_{\mathrm{axf}}(\tilde Q)=Q_t\mathrm I+L_{\mathrm{axf}}(\vec v)$ with $L_{\mathrm{axf}}(\vec v)^{2}=0$ and rank $2$; a nilpotent of rank two and square zero on a space of dimension four has two blocks of size two.

**The comparison.** A general matrix of $M_4(\mathbb{C})$ can realise all five types, and the type $3+1$ and the type $4$ are the ones a one-sided matrix never has. This is the structural reason the length of an operator, not the rank of a matrix, is the invariant that separates the two-sided world from the one-sided one; the count is *The Length and the Two Ranks at $n=4$*.

## Summary

The minimal polynomial divides the characteristic polynomial and shares its roots; it equals it exactly when the matrix is nonderogatory, equivalently when a cyclic vector exists, equivalently when the centraliser is $\mathbb{C}[A]$ of dimension four. At order four the five partitions give the five shapes, with degrees $4,3,2,2,1$ and centraliser dimensions $4,6,8,7,16$.

Every matrix splits as $S+N$ with commuting semisimple and nilpotent parts, both polynomial in $A$, with $N^{4}=0$; the matrix is diagonalisable exactly when $N=0$. The companion matrix of a quartic is nonderogatory, and the rational canonical form reassembles any matrix from companion blocks.

In the axis-free frame the spectrum is $Q_t\pm iB$ each twice, so the minimal polynomial has degree at most two and the one-sided matrices realise only the shapes $1+1+1+1$ and $2+2$: the types $3+1$ and $4$ are two-sided phenomena.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\chi_A$ | the characteristic polynomial, of degree $4$ |
| $\mu_A$ | the minimal polynomial, dividing $\chi_A$ |
| $m(\lambda)$ | the largest Jordan block size at $\lambda$ |
| $S$, $N$ | the semisimple and nilpotent parts of $A$ |
| $C_p$ | the companion matrix of the quartic $p$ |
| $Q_t$, $B$ | the scalar coordinate and $\sqrt{Q_x^{2}+Q_y^{2}+Q_z^{2}}$ |
| $L_{\mathrm{axf}}$ | the left regular representation of $\mathbb{B}$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the Jordan and rational canonical forms and the centraliser count.
- [The Matrix Algebra $M_4(\mathbb{C})$](the-matrix-algebra-m4c.html), for the algebra in which the Jordan form is computed.
- [The Elementary Symmetric Functions and $\det(\mathrm{I}+tA)$ at $n=4$](the-elementary-symmetric-functions-and-det-i-plus-ta-at-n-4.html), for the coefficients of the characteristic polynomial.
- [The Quartic, the Discriminant and the Spectral Strata of $M_4(\mathbb{C})$](the-quartic-the-discriminant-and-the-spectral-strata-of-m4c.html), for the discriminant that separates the shapes.
- [The Minimal Polynomial and the Two Jordan Regimes of $M_2(\mathbb{C})$](the-minimal-polynomial-and-the-two-jordan-regimes-of-m2c.html), for the same dichotomy at order two.
