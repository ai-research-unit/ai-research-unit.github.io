
# __The Hecke Operator__

## Introduction

The Hecke operators are the operators on spaces of modular forms that are built from the arithmetic of the level: for each positive integer $n$ and each congruence subgroup, $T_n$ averages a form over the sublattices of index $n$, and the average is again a modular form. They act on the Fourier expansion by a formula that is elementary and self-contained, they commute with one another, and their simultaneous eigenforms are exactly the forms whose coefficient functions are multiplicative. The Hecke operators are therefore the bridge between the analytic spaces of *Modular Forms* and the arithmetic of the algebra of arithmetic functions: the eigenvalue system $n\mapsto a_n$ of a normalised eigenform is a multiplicative arithmetic function, the algebra the operators generate is the Hecke algebra, and the characters of that algebra are the eigenforms.

This article defines the Hecke operators and the diamond operators, derives the action on the $q$-expansion, proves the multiplicativity and the recursion at the prime powers, and states the structure of the Hecke algebra with the eigenform correspondence and the theory of newforms. It assumes *Modular Forms* for the upper half-plane, the congruence subgroups, the weight-$k$ action, the spaces $M_k(\Gamma_1(N))$ and $S_k(\Gamma_1(N))$, their $q$-expansions and the level-one structure theorem; it assumes *Analytic Number Theory* for the arithmetic functions under Dirichlet convolution, and *L-Functions* for the Dirichlet series attached to a modular form. The Petersson inner product and the adjoint of a Hecke operator are *The Adjoint of the Hecke Operator*, later in this category; the conjugate symmetry of the eigenvalues and the Ramanujan bound are *The Conjugate Symmetry of the Hecke Operator*, also later; the adelic reading of all of this is *Automorphic Forms*, written in parallel. Nothing here reads a distance as an object; the operator is defined by its action on expansions and its algebra is finite-dimensional over $\mathbb{C}$.

Throughout, $k$ and $N$ are positive integers with $k\ge2$, $\Gamma_1(N)\subseteq\Gamma_0(N)\subseteq SL_2(\mathbb{Z})$ are the congruence subgroups of *Modular Forms*, and $f$ is a form of weight $k$, holomorphic at the cusps, with $q$-expansion $f(z)=\sum_{m\ge0}a_mq^m$, $q=e^{2\pi iz}$. The level-one case is abbreviated $\Gamma(1)=SL_2(\mathbb{Z})$. A form is **normalised** when $a_1=1$, and a **Hecke eigenform** when it is an eigenvector of every $T_n$.

## The Operators on a Modular Form

### The Hecke operator

**Definition.** For $n\ge1$ the **Hecke operator** $T_n$ acts on a function $f$ on the upper half-plane by
$$
(T_nf)(z) = n^{k-1}\sum_{\substack{a,d\ge1\\ ad=n}}\frac{1}{d^{\,k}}\sum_{b=0}^{d-1}f\!\left(\frac{az+b}{d}\right).
$$

The sum is finite, it is a sum of transforms of $f$ by the weight-$k$ action, and it commutes with $\mid_k\gamma$ for every $\gamma$ in the commensurator of $\Gamma_1(N)$, which is why it preserves the spaces of modular forms.

**Theorem.** For every $n$ the operator $T_n$ preserves $M_k(\Gamma_1(N))$ and $S_k(\Gamma_1(N))$, and if $f=\sum_{m\ge0}a_mq^m$ then
$$
T_nf = \sum_{m\ge0}b_mq^m, \qquad b_m=\sum_{d\mid\gcd(m,n)}d^{\,k-1}\,a_{mn/d^2}.
$$
The coefficient $b_m$ is a finite sum, and it depends only on $a_{mn/d^2}$ for $d\mid\gcd(m,n)$.

**Proof.** The invariance of the spaces is the double-coset computation of *Modular Forms*: the matrices $\begin{pmatrix}a&b\\0&d\end{pmatrix}$ with $ad=n$ are a set of double-coset representatives, and the average over each right coset of $\Gamma_1(N)$ is $\Gamma_1(N)$-invariant. For the coefficient formula, insert $q=e^{2\pi iz}$ and expand each term $f((az+b)/d)=\sum_ja_j e^{2\pi i j(az+b)/d}$; the sum over $b$ is a geometric sum, equal to $d$ when $d\mid j$ and to $0$ otherwise, so only the indices $j=dm'$ survive, and the substitution $m=ad\,m'$ collects the terms as displayed. The holomorphy at the cusps is preserved because each summand is and the sum is finite.

**Remark (the two normalisations in the literature).** Some sources place the factor $n^{k-1}$ on the whole sum and some absorb $d^{-k}$ differently; the two conventions differ by the substitution $a\leftrightarrow d$, and the coefficient formula $b_m=\sum_{d\mid\gcd(m,n)}d^{k-1}a_{mn/d^2}$ is the coordinate-free content common to both. This article fixes the display above and uses it consistently.

### The diamond operators

**Definition.** Let $N\ge1$ and let $d$ be an integer with $(d,N)=1$. Choose $\gamma_d\in\Gamma_0(N)$ with lower-right entry $d$; the **diamond operator** is
$$
\langle d\rangle f = f\mid_k\gamma_d .
$$
It depends only on $d\bmod N$, so $\langle\cdot\rangle$ is a homomorphism $(\mathbb{Z}/N\mathbb{Z})^{\times}\to\operatorname{Aut}M_k(\Gamma_1(N))$.

**Proposition.** The diamond operators preserve $M_k(\Gamma_1(N))$ and $S_k(\Gamma_1(N))$, commute with every $T_n$, and act on the $q$-expansion of a form of nebentypus $\varepsilon$ by
$$
\langle d\rangle f = \sum_{m\ge0}\varepsilon(d)\,a_mq^m .
$$
The action of $\langle d\rangle$ is diagonal on the coefficient sequence, and it is the case $n=1$ of the more general operation of the next section.

**Proof.** The first two statements are the covariance of $\mid_k$ and the computation $\gamma_d\begin{pmatrix}a&b\\0&d'\end{pmatrix}$ in the double coset; the diagonal display is the definition of the nebentypus $\varepsilon:\Gamma_0(N)\to\mathbb{C}^\times$ with $f\mid_k\gamma=\varepsilon(\gamma)f$ for $\gamma\in\Gamma_0(N)$, evaluated at $\gamma_d$.

## The Algebra of the Operators

### Multiplicativity

**Theorem.** For all $m,n\ge1$,
$$
T_mT_n = T_{mn} \quad\text{when } (m,n)=1, \qquad T_1=\mathrm{id},
$$
and for every prime $p$ and every $r\ge1$,
$$
T_{p^{\,r+1}} = T_pT_{p^{\,r}} - p^{\,k-1}\langle p\rangle T_{p^{\,r-1}} .
$$
Consequently the operators $T_n$ and the diamonds $\langle d\rangle$ generate a commutative algebra.

**Proof.** The coprimality statement is a multiplicativity of double cosets: when $(m,n)=1$ the double coset of index $mn$ factors as the product of the cosets of index $m$ and $n$, by the Chinese remainder theorem on the diagonal entries. The recursion is the coprimality case applied to the three-term relation among the representatives of index $p^{r+1}$, $p^r\cdot p$ and $p^{r-1}p^2$, in which the overlap contributes the middle term $p^{k-1}\langle p\rangle$. Commutativity follows because both relations express every generator in terms of the $T_p$ and the diamonds, and the diamonds commute with the $T_n$ by the previous section.

### Eigenforms and the recursion on coefficients

**Proposition.** Let $f=\sum a_mq^m$ be a normalised eigenform for all $T_n$, with $T_nf=a_nf$. Then
$$
a_1=1, \qquad a_{mn}=a_ma_n \ \text{ for } (m,n)=1, \qquad a_{p^{\,r+1}}=a_pa_{p^{\,r}}-\varepsilon(p)p^{\,k-1}a_{p^{\,r-1}},
$$
so the coefficient function $n\mapsto a_n$ is multiplicative and determined by its values at the primes, and its Dirichlet series has the Euler product
$$
L(f,s)=\sum_{m\ge1}a_mm^{-s}=\prod_p\Bigl(1-a_pp^{-s}+\varepsilon(p)p^{\,k-1-2s}\Bigr)^{-1}
$$
in the region of absolute convergence.

**Proof.** Apply $T_nf=a_nf$ to the coefficient of $q^1$ in the coefficient formula: the only term of $b_1$ is $d=1$, $b_1=a_n$, so $(T_nf)$ has constant $q$-coefficient $a_n$, and $T_nf=a_nf$ forces $a_1=1$ after the normalisation. The multiplicativity and the recursion are the action of the operator identities of the previous theorem on $f$, read coefficientwise; the Euler product is the multiplicativity plus the local recursion, in the form of *Analytic Number Theory*. One uses that $\langle p\rangle f=\varepsilon(p)f$.

### The Hecke algebra

**Definition.** The **Hecke algebra** is the $\mathbb{Z}$-subalgebra
$$
\mathbb{T}_k(N)=\mathbb{Z}\bigl[\,T_n\ (n\ge1),\ \langle d\rangle\ ((d,N)=1)\,\bigr]\subseteq\operatorname{End}_{\mathbb{C}}\bigl(S_k(\Gamma_1(N))\bigr),
$$
a commutative ring of finite rank, and its complexification is $\mathbb{T}_k(N)\otimes_{\mathbb{Z}}\mathbb{C}$.

**Theorem (the correspondence).** Suppose first that the nebentypus is fixed, so that the diamonds act by the character $\varepsilon$ and may be treated as scalars. Then the following three sets are in canonical bijection:

1. the algebra homomorphisms $\mathbb{T}_k(N)\otimes\mathbb{C}\to\mathbb{C}$;
2. the normalised eigenforms $f\in S_k(\Gamma_1(N))$;
3. the systems of eigenvalues $(a_p)_p$, equivalently the multiplicative functions $n\mapsto a_n$ satisfying the local recursion above and the growth condition $a_n=O(n^{k/2+\epsilon})$.

The bijection sends a homomorphism to the form whose eigenvalue system it produces, $T_n\mapsto a_n$, and it is the content of the statement that the Hecke algebra is generated by the operators and that its characters are the eigenforms.

**Proof sketch.** The operators $T_n$ are normalised by the recursion, so $\mathbb{T}_k(N)\otimes\mathbb{C}$ is generated by commuting operators each of which satisfies a monic polynomial over $\mathbb{Z}$; it is therefore finite-dimensional and semisimple, and it splits as a product of copies of $\mathbb{C}$ indexed by its characters. Each character $\lambda$ cuts out the generalised eigenspace on which $T_n$ acts by $\lambda(T_n)$, and the semisimplicity makes it an eigenspace; choosing a nonzero vector in it and clearing denominators produces a normalised eigenform with $a_n=\lambda(T_n)$. Conversely a normalised eigenform gives the character $T_n\mapsto a_n$. The growth condition on the coefficients is the estimate of *Modular Forms*, and it is what makes the eigenform holomorphic at the cusps.

**Corollary (the coefficient function is an arithmetic function).** The map $f\mapsto (n\mapsto a_n)$ embeds the eigenforms into the algebra of arithmetic functions of *Analytic Number Theory*, compatibly with the Hecke action: the operator $T_n$ corresponds to the arithmetic function $n\mapsto T_n$ under the pairing of a form with its coefficient sequence, and the Dirichlet convolution of the eigenvalue systems is the product of the corresponding operators.

## Newforms and the Old Part

### The old subspace

**Definition.** For $M\mid N$ and $d\mid N/M$ the form $f\mid_k\gamma_d$ for $f\in S_k(\Gamma_1(M))$ lies in $S_k(\Gamma_1(N))$; the **old subspace** $S_k(\Gamma_1(N))^{\mathrm{old}}$ is the span of all such forms, and the **new subspace** is the quotient
$$
S_k(\Gamma_1(N))^{\mathrm{new}} = S_k(\Gamma_1(N))^{\mathrm{old}\,\perp}
$$
taken with respect to the Petersson inner product of *The Adjoint of the Hecke Operator*.

**Theorem (Atkin–Lehner, multiplicity one).** The new subspace has a basis of normalised eigenforms whose eigenvalue systems are not of lower level, the old and new parts are stable under the Hecke operators for $(n,N)=1$, and on the new part a normalised eigenform is determined by its eigenvalue system; the space decomposes as
$$
S_k(\Gamma_1(N)) = S_k^{\mathrm{old}}\oplus S_k^{\mathrm{new}},
$$
an orthogonal direct sum once the Petersson product is available.

**Proof sketch.** The Atkin–Lehner operators $W_Q$ for the divisors $Q$ of $N$ permute the old/new decomposition and give a finite group of involutions acting on the space; the fixed spaces of the various products of the $W_Q$ cut the old part out, and the quotient is the new part. Multiplicity one for the new part is the statement that the Hecke algebra acts with multiplicity one on each Galois-conjugacy class of eigenvalue systems, which follows from the recursion and the excluded lower levels. The full proofs are in *Modular Forms*, to which this article defers.

### The correspondence on the modular curve

**Remark (the correspondences).** Each $T_n$ is not only an operator but the trace of a **Hecke correspondence** on the modular curve: the arithmetic points of the modular curve parametrise pairs of lattices, and the locus of pairs of index $n$ defines a curve-with-multiplicity in $X_1(N)\times X_1(N)$ whose two projections pull back and push forward forms. The Eichler–Shimura isomorphism of *Modular Forms* identifies this correspondence with $T_n$ on $S_k$, and it is the geometric form of the same operator. The reading belongs to *Modular Forms*; this article uses only the operator action on expansions.

## Summary

For $n\ge1$ the Hecke operator $T_n$ is the average $n^{k-1}\sum_{ad=n}d^{-k}\sum_{b=0}^{d-1}f((az+b)/d)$; it preserves $M_k(\Gamma_1(N))$ and $S_k(\Gamma_1(N))$ and acts on the Fourier expansion by $b_m=\sum_{d\mid\gcd(m,n)}d^{k-1}a_{mn/d^2}$. The diamond operators $\langle d\rangle$ for $(d,N)=1$ commute with the $T_n$ and act on a form of nebentypus $\varepsilon$ by $\varepsilon(d)$ on each coefficient. The operators satisfy $T_mT_n=T_{mn}$ for $(m,n)=1$ and $T_{p^{r+1}}=T_pT_{p^r}-p^{k-1}\langle p\rangle T_{p^{r-1}}$, so they generate the commutative Hecke algebra $\mathbb{T}_k(N)$, of finite rank over $\mathbb{Z}$; on a normalised eigenform $f=\sum a_mq^m$ the recursion reads $a_{p^{r+1}}=a_pa_{p^r}-\varepsilon(p)p^{k-1}a_{p^{r-1}}$, the coefficient function $n\mapsto a_n$ is multiplicative, and its Dirichlet series has the degree-two Euler product $\prod_p(1-a_pp^{-s}+\varepsilon(p)p^{k-1-2s})^{-1}$. The characters of $\mathbb{T}_k(N)\otimes\mathbb{C}$ are the normalised eigenforms, by semisimplicity and the generation of the algebra; the new subspace is the orthogonal complement of the forms raised from lower level, and it carries a basis of newforms determined by their eigenvalue systems (Atkin–Lehner, multiplicity one). The adjoint of $T_n$ for the Petersson product and the Ramanujan bound on $a_p$ are the subjects of the two following articles of the category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_n$ | Hecke operator of index $n$ |
| $b_m=\sum_{d\mid\gcd(m,n)}d^{k-1}a_{mn/d^2}$ | Action on the $q$-expansion |
| $\langle d\rangle$, $\varepsilon$ | Diamond operator; nebentypus |
| $\mathbb{T}_k(N)$ | Hecke algebra generated by the $T_n$ and the $\langle d\rangle$ |
| $T_mT_n=T_{mn}$, $(m,n)=1$ | Coprime multiplicativity |
| $T_{p^{r+1}}=T_pT_{p^r}-p^{k-1}\langle p\rangle T_{p^{r-1}}$ | Prime-power recursion |
| $a_{mn}=a_ma_n$, $a_{p^{r+1}}=a_pa_{p^r}-\varepsilon(p)p^{k-1}a_{p^{r-1}}$ | Recursion for a normalised eigenform |
| $L(f,s)=\prod_p(1-a_pp^{-s}+\varepsilon(p)p^{k-1-2s})^{-1}$ | Euler product of an eigenform |
| $S_k^{\mathrm{old}}, S_k^{\mathrm{new}}$ | Old subspace; new subspace |
| $W_Q$ | Atkin–Lehner operators of the divisors $Q\mid N$ |

## Further Reading

- Goro Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions* (Princeton University Press, 1971), for the Hecke operators, the Hecke algebra and the eigenform correspondence.
- Jean-Pierre Serre, *A Course in Arithmetic* (Springer, 1973), for the level-one Hecke operators and the arithmetic of the coefficients.
- Fred Diamond and Jerry Shurman, *A First Course in Modular Forms* (Springer, 2005), for the coefficient action, the new subspace and the Atkin–Lehner theory.
- Andrew Ogg, *Modular Forms and Dirichlet Series* (Benjamin, 1969), for the Euler product of an eigenform and the correspondence with Dirichlet series.
- Erich Hecke, *Mathematische Werke* (Vandenhoeck & Ruprecht, 1970), for the original construction of the operators and their algebra.
