
# __Matrix Algebras__

## Introduction

The algebra $M_n(R)$ of $n\times n$ matrices over a commutative ring $R$ is the model by which the general theory of associative algebras is tested. It is simple when $R$ is a field, its centre is the scalar matrices, its units are the matrices of invertible determinant, and it carries a basis — the matrix units — whose multiplication table is the clearest possible display of a non-commutative structure. This article develops those facts, together with the identification of $M_n(R)$ with the endomorphism algebra of the free module $R^n$ and the tensor product formula $M_m(k)\otimes_k M_n(k) \cong M_{mn}(k)$.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$, $k$ is a field, and $n \geq 1$. The matrix algebra $M_n(R)$ is associative and unital with unit $I_n$, the identity matrix. For $n \geq 2$ it is non-commutative; for $n = 1$ it is the ring $R$ itself. The general theory of ideals and quotients used below is that of *Ideals and Quotients of Algebras*, and the centre is as in *Centre, Units, Zero Divisors and Division Algebras*.

## Matrix Units

**Definition.** For $1 \leq i, j \leq n$ let $E_{ij}$ be the matrix whose only nonzero entry is a $1$ in position $(i,j)$. The **matrix units** $E_{ij}$ form an $R$-basis of $M_n(R)$, so that

$$
\dim_R M_n(R) = n^2, \qquad A = \sum_{i,j=1}^{n} A_{ij}E_{ij} .
$$

**Proposition (multiplication of matrix units).** For all $i,j,k,l$,

$$
E_{ij}E_{kl} = \delta_{jk}E_{il},
$$

where $\delta_{jk}$ is $1$ if $j = k$ and $0$ otherwise.

*Proof.* The matrix $E_{ij}E_{kl}$ has entry in position $(p,q)$ equal to $\sum_r (E_{ij})_{pr}(E_{kl})_{rq} = \sum_r \delta_{ip}\delta_{jr}\delta_{kr}\delta_{lq} = \delta_{jr}\delta_{kr}\delta_{ip}\delta_{lq}$. The sum over $r$ collapses to $\delta_{jk}$, so the entry is $\delta_{jk}\delta_{ip}\delta_{lq}$, which is the $(p,q)$-entry of $\delta_{jk}E_{il}$. $\square$

Two consequences are used constantly. First, $E_{ij}E_{jl} = E_{il}$, so any matrix unit is the product of two others; second, $E_{ij}E_{kl} = 0$ whenever $j \neq k$, so there are many zero-divisor pairs as soon as $n \geq 2$, and $M_n(R)$ is not a domain. The matrix units satisfy $E_{ij} = E_{ik}E_{kj}$ for every $k$, which is the identity that makes the ideal theory of $M_n(R)$ trivial.

## The Algebra as an Endomorphism Algebra

Let $R^n$ be the free $R$-module of column vectors of length $n$. Every matrix $A \in M_n(R)$ acts on $R^n$ by left multiplication, and the map

$$
M_n(R) \longrightarrow \operatorname{End}_R(R^n), \qquad A \longmapsto (x \mapsto Ax),
$$

is an isomorphism of $R$-algebras. It is injective because $Ae_j$ is the $j$-th column of $A$, so a matrix acting as zero is zero, and it is surjective because an $R$-linear endomorphism is determined by the images of the standard basis, which are the columns of a matrix. Consequently

$$
M_n(R) \cong \operatorname{End}_R(R^n) .
$$

For $n \geq 2$ the algebra is non-commutative, since $E_{12}E_{21} = E_{11}$ while $E_{21}E_{12} = E_{22}$, and these differ.

## Trace and Determinant

**Definition.** The **trace** of $A \in M_n(R)$ is $\operatorname{Tr} A = \sum_{i=1}^n A_{ii} \in R$, and the **determinant** is

$$
\det A = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \prod_{i=1}^n A_{i,\sigma(i)} \in R .
$$

Both are polynomial functions of the entries, so they are defined over any commutative ring.

**Proposition (properties).** For $A, B \in M_n(R)$:

1. $\operatorname{Tr}(A+B) = \operatorname{Tr}A + \operatorname{Tr}B$ and $\operatorname{Tr}(\lambda A) = \lambda\operatorname{Tr}A$;
2. $\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$, and more generally the trace is invariant under cyclic permutation of a product;
3. $\det(AB) = \det A \cdot \det B$ and $\det I_n = 1$;
4. the characteristic polynomial $\chi_A(t) = \det(tI_n - A)$ has constant term $(-1)^n\det A$ and coefficient of $t^{n-1}$ equal to $-\operatorname{Tr}A$.

*Proof.* The trace identities follow from the definitions, since $\operatorname{Tr}(AB) = \sum_{i,j}A_{ij}B_{ji} = \sum_{i,j}B_{ji}A_{ij} = \operatorname{Tr}(BA)$. The multiplicativity of the determinant is the classical theorem, proved by expanding both sides as sums over $S_n$ and reindexing; over a general commutative ring it follows from the universal polynomial identity over $\mathbb{Z}$, which is then evaluated in $R$. The two coefficients of $\chi_A$ are read off from the Leibniz formula. $\square$

**Theorem (unit criterion).** A matrix $A \in M_n(R)$ is a unit if and only if $\det A \in R^\times$.

*Proof.* If $AB = I_n$ then $\det A \cdot \det B = \det I_n = 1$, so $\det A$ is a unit. Conversely, if $\det A$ is a unit, let $\operatorname{adj}(A)$ be the adjugate matrix, whose entries are the cofactors; the Laplace expansion gives $A\operatorname{adj}(A) = \operatorname{adj}(A)A = (\det A)I_n$. Hence $A^{-1} = (\det A)^{-1}\operatorname{adj}(A)$ is a two-sided inverse. $\square$

Over a field the criterion reads: $A$ is a unit if and only if $\det A \neq 0$, which is the usual statement that the units are $\mathrm{GL}_n(k)$. Over a general commutative ring the determinant can be a nonzero non-unit: the matrix $\operatorname{diag}(2,1) \in M_2(\mathbb{Z})$ has determinant $2$, so it is not invertible, and it is not a zero divisor either, since $2$ is not a zero divisor in $\mathbb{Z}$.

## Ideals and Simplicity

**Theorem (simplicity).** Let $k$ be a field. Then $M_n(k)$ has exactly two two-sided ideals, $0$ and $M_n(k)$; that is, $M_n(k)$ is simple.

*Proof.* Let $I \neq 0$ be a two-sided ideal and let $0 \neq A \in I$ with $A_{ij} \neq 0$. For any $p, q$,

$$
E_{pq} = \frac{1}{A_{ij}}\, E_{pi}\, A\, E_{jq} \in I,
$$

since $E_{pi}A E_{jq}$ has $(p,q)$-entry $A_{ij}$ and all other entries zero. As the matrix units span, $I = M_n(k)$. $\square$

**Theorem (left ideals).** Let $k$ be a field. The left ideals of $M_n(k)$ are exactly the sets

$$
I_V = \{ A \in M_n(k) : \operatorname{col}(A) \subseteq V \},
$$

where $V \subseteq k^n$ is a subspace and $\operatorname{col}(A)$ is the span of the columns of $A$.

*Proof.* Each $I_V$ is a left ideal, because left multiplication replaces the columns by linear combinations of them. Conversely, if $I$ is a left ideal, let $V$ be the span of the columns of all matrices in $I$; then $I \subseteq I_V$. For the reverse inclusion, choose $A \in I$ whose columns span $V$. Every vector of $V$ is $Ay$ for some $y$, so every matrix $B$ with columns in $V$ has the form $B = AC$ for a suitable $C$; since $I$ is a left ideal, $AC \in I$ and hence $B \in I$. $\square$

The left ideals are therefore in bijection with the subspaces of $k^n$, the two trivial ideals corresponding to $V = 0$ and $V = k^n$ and the others to the proper subspaces; over $\mathbb{R}$ and $n = 2$ the minimal ones form the projective line. The minimal left ideals are the $I_V$ with $\dim V = 1$, each isomorphic to $k^n$ as a left module. The right ideals are described by the rows in the same way, and the two-sided ideals are the two trivial ones, in agreement with simplicity.

**Corollary (the centre).** For a commutative ring $R$, $Z(M_n(R)) = R I_n$, and $M_n(R)$ is a central $R$-algebra.

*Proof.* If $A$ commutes with every matrix unit, then $AE_{ij} = E_{ij}A$ for all $i,j$. Comparing the $(k,l)$-entries gives $A_{ki}\delta_{jl} = \delta_{ik}A_{jl}$. Taking $j = l$ yields $A_{ki} = \delta_{ik}A_{jj}$ for all $i,k,j$: with $i = k$ this gives $A_{ii} = A_{jj}$, so all diagonal entries are equal, and with $i \neq k$ it gives $A_{ki} = 0$, so all off-diagonal entries vanish. Hence $A = \lambda I_n$ with $\lambda \in R$. $\square$

## Tensor Products of Matrix Algebras

**Theorem (tensor product formula).** For a field $k$ and positive integers $m, n$,

$$
M_m(k) \otimes_k M_n(k) \cong M_{mn}(k).
$$

*Proof.* Define

$$
\Phi\left(E_{ij} \otimes E_{kl}\right) = E_{(i,k),(j,l)},
$$

where the right-hand index $(i,k)$ is read as the integer $(i-1)n + k$ and correspondingly for $(j,l)$; extend $k$-bilinearly. The matrix units $E_{ij}\otimes E_{kl}$ form a basis of the tensor product, and the target matrix units $E_{(i,k),(j,l)}$ form a basis of $M_{mn}(k)$, so $\Phi$ is a linear isomorphism. It is multiplicative because

$$
\Phi\bigl((E_{ij}\otimes E_{kl})(E_{i'j'}\otimes E_{k'l'})\bigr)
= \delta_{ji'}\delta_{lk'}\, \Phi\bigl(E_{ij'}\otimes E_{kl'}\bigr)
= \delta_{ji'}\delta_{lk'}\, E_{(i,k),(j',l')},
$$

which is exactly the product $E_{(i,k),(j,l)}E_{(i',k'),(j',l')}$; and it sends $I_m\otimes I_n$ to $I_{mn}$. $\square$

The formula is the algebraic statement that the tensor product of two matrix algebras is again a matrix algebra, of size the product of the sizes; the two factors embed as the subalgebras of matrices acting on the two tensor legs, and the two images commute. Iterating, $M_{n_1}(k)\otimes\dots\otimes M_{n_r}(k) \cong M_{n_1\cdots n_r}(k)$. The construction is the matrix case of the tensor product of algebras in *Tensor Products of Algebras*.

## The Regular Module

$M_n(k)$ is a left module over itself in the evident way, the **regular module**. The standard basis of $k^n$ as a column vector gives

$$
M_n(k) = I_{V_1} \oplus \dots \oplus I_{V_n},
$$

where $V_j = ke_j$ is the $j$-th coordinate line and $I_{V_j}$ is the minimal left ideal of matrices supported in the $j$-th column. Each $I_{V_j}$ is isomorphic to the simple module $k^n$ (column vectors), so the regular module is a direct sum of $n$ copies of the unique simple left module; this is the concrete form of the Wedderburn structure theory: $M_n(k)$ is the matrix algebra over the division ring $k$, and its regular module is $n$ copies of the unique simple module $k^n$. The same decomposition with $k$ replaced by a division ring $D$ describes $M_n(D)$, the general simple finite-dimensional algebra, whose simple module is $D^n$.

## The Case $n = 2$

For $n = 2$ the algebra is four-dimensional, with basis $E_{11}, E_{12}, E_{21}, E_{22}$ and multiplication

$$
E_{11}^2 = E_{11}, \quad E_{22}^2 = E_{22}, \quad E_{12}^2 = E_{21}^2 = 0, \quad E_{11}E_{22} = E_{22}E_{11} = 0,
$$

$$
E_{12}E_{21} = E_{11}, \quad E_{21}E_{12} = E_{22}, \quad E_{11}E_{12} = E_{12}, \quad E_{12}E_{22} = E_{12}, \quad E_{22}E_{21} = E_{21}, \quad E_{21}E_{11} = E_{21}.
$$

The matrix units $E_{12}$ and $E_{21}$ are nilpotent and are zero divisors; the identity $E_{11}E_{22} = 0$ exhibits another zero-divisor pair. The centre is $kI_2$, of dimension $1$, so the algebra is central and simple of dimension $4$. Its units are the matrices with nonzero determinant, and

$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix} .
$$

As a left module over itself $M_2(k)$ decomposes as the sum of the two minimal left ideals $I_{ke_1} = kE_{11} \oplus kE_{21}$ and $I_{ke_2} = kE_{12} \oplus kE_{22}$, each a copy of the simple module $k^2$.

The idempotents $E_{11}$ and $E_{22}$ are orthogonal and complete, and the Peirce decomposition of $M_2(k)$ with respect to $E_{11}$ is the matrix-unit decomposition

$$
M_2(k) = kE_{11} \oplus kE_{12} \oplus kE_{21} \oplus kE_{22},
$$

the four one-dimensional Peirce spaces being the matrix units themselves. The off-diagonal spaces are $E_{11}M_2E_{22} = kE_{12}$ and $E_{22}M_2E_{11} = kE_{21}$. The idempotent $E_{11}$ is not central, since $E_{11}E_{12} = E_{12}$ while $E_{12}E_{11} = 0$, so the two off-diagonal spaces do not vanish and the decomposition is not a product of algebras; consistently with the simplicity of $M_2(k)$, none of the four spaces is a two-sided ideal. The general theorem, with the product decomposition that a central idempotent gives instead, is *Unital Algebras*, §*Idempotents and the Peirce Decomposition*. The column decomposition above groups $E_{11}$ with $E_{21}$ and the Peirce decomposition groups $E_{11}$ with $E_{12}$: the two groupings are the left-ideal and the corner decompositions of the same four matrix units.

## The Trace Form and Skolem–Noether

**Proposition (the trace form).** The bilinear form on $M_n(k)$ defined by

$$
\langle A, B\rangle = \operatorname{Tr}(AB)
$$

is symmetric, associative in the sense that $\langle AB, C\rangle = \langle A, BC\rangle$, and non-degenerate.

*Proof.* Symmetry is $\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$. Associativity is $\operatorname{Tr}((AB)C) = \operatorname{Tr}(A(BC))$. For non-degeneracy, suppose $\langle A, B\rangle = 0$ for all $B$; taking $B = E_{ji}$ gives $\operatorname{Tr}(AE_{ji}) = A_{ij} = 0$ for all $i,j$, hence $A = 0$. $\square$

The trace form is the concrete case of the non-degenerate associative form that makes $M_n(k)$ a **symmetric Frobenius algebra**, and it can be used in place of the matrix units in many arguments, for instance to identify the dual of $M_n(k)$ with itself.

**Theorem (Skolem–Noether, standard).** Every $k$-algebra automorphism $\varphi$ of $M_n(k)$ is inner: there is $P \in \mathrm{GL}_n(k)$ with

$$
\varphi(A) = PAP^{-1}, \qquad A \in M_n(k),
$$

and the assignment $P \mapsto (A \mapsto PAP^{-1})$ induces an isomorphism

$$
\operatorname{Aut}_k(M_n(k)) \cong \mathrm{PGL}_n(k) = \mathrm{GL}_n(k)/k^\times.
$$

*Proof (sketch).* The algebra $M_n(k)$ has a unique simple left module $k^n$ up to isomorphism, and $\varphi$ transports the module structure to an isomorphic one; an isomorphism of the transported module with $k^n$ is a matrix $P$, and comparing the actions gives $\varphi(A) = PAP^{-1}$. The kernel of $P \mapsto (A\mapsto PAP^{-1})$ is $k^\times I_n$. $\square$

**Corollary (derivations).** Every $k$-derivation of $M_n(k)$ is inner, $\delta(A) = [H, A]$ for some $H \in M_n(k)$.

This is the finite-dimensional case of the innerness theorem for von Neumann algebr, and it is the worked case promised in *Automorphisms and Derivations of Algebras*: for a matrix algebra the automorphism group is $\mathrm{PGL}_n(k)$, so the outer automorphism group $\operatorname{Out}_k(M_n(k)) = \operatorname{Aut}_k(M_n(k))/\operatorname{Inn}_k(M_n(k))$ is trivial, and the space of outer derivations is zero.

## Summary

The matrix algebra $M_n(R)$ over a commutative ring $R$ has $R$-basis the matrix units $E_{ij}$, $1 \leq i,j \leq n$, with multiplication $E_{ij}E_{kl} = \delta_{jk}E_{il}$ and dimension $n^2$. It is isomorphic to the endomorphism algebra $\operatorname{End}_R(R^n)$, it is associative with unit $I_n$, and it is non-commutative for $n \geq 2$. **Trace** is $R$-linear and satisfies $\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$, and **determinant** is multiplicative; a matrix is a unit if and only if its determinant lies in $R^\times$, with $A^{-1} = (\det A)^{-1}\operatorname{adj}(A)$. Over a field, $M_n(k)$ is **simple**: its only two-sided ideals are $0$ and itself, proved by writing each matrix unit as $E_{pi}AE_{jq}$ scaled; its left ideals correspond to subspaces of $k^n$, and its centre is $kI_n$. The tensor product formula $M_m(k)\otimes_k M_n(k)\cong M_{mn}(k)$ holds, and the regular module is a direct sum of $n$ copies of the simple module $k^n$. The **trace form** $\langle A,B\rangle = \operatorname{Tr}(AB)$ is symmetric, associative and non-degenerate, and by the Skolem–Noether theorem every automorphism of $M_n(k)$ is inner, $\varphi(A) = PAP^{-1}$, so that $\operatorname{Aut}_k(M_n(k)) \cong \mathrm{PGL}_n(k)$ and every derivation is inner.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $k$ | Field |
| $M_n(R)$ | Algebra of $n\times n$ matrices over $R$ |
| $I_n$ | Identity matrix |
| $E_{ij}$ | Matrix unit, $E_{ij}E_{kl} = \delta_{jk}E_{il}$ |
| $A_{ij}$ | Entries of $A$ |
| $\operatorname{Tr}A$ | Trace |
| $\det A$ | Determinant |
| $\operatorname{adj}(A)$ | Adjugate, $A\operatorname{adj}(A) = (\det A)I_n$ |
| $\mathrm{GL}_n(k)$ | Units of $M_n(k)$, $= \{A : \det A \neq 0\}$ |
| $\operatorname{End}_R(R^n)$ | Endomorphism algebra, $\cong M_n(R)$ |
| $I_V$ | Left ideal of matrices with columns in $V$ |
| $M_n(D)$ | Matrix algebra over a division ring $D$ |
| $\langle A,B\rangle = \operatorname{Tr}(AB)$ | Trace form |
| $\operatorname{Aut}_k(M_n(k)) \cong \mathrm{PGL}_n(k)$ | Automorphisms, all of them inner; $\operatorname{Out}_k(M_n(k)) = 1$ |
| $\otimes_k$ | Tensor product of algebras |



## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for simplicity, the regular module and the Wedderburn decomposition.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for matrix units, the endomorphism algebra and the tensor product formula.
- Nathan Jacobson, *Basic Algebra I* (Dover, 2nd ed. 2009), for the trace, the determinant and the adjugate over a commutative ring.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the ideal theory of $M_n(D)$ and the structure of simple rings.
- Jean-Pierre Serre, *Linear Representations of Finite Groups* (Springer, 1977), for the tensor product of matrix representations and the identification $M_m\otimes M_n\cong M_{mn}$.
