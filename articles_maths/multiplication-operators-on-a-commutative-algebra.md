# __Multiplication Operators on a Commutative Algebra__

## Introduction

Every element $a$ of an algebra $A$ carries the operator of multiplication by it, $x \mapsto ax$. When $A$ is commutative this single family of operators is closed under composition and under addition, and the assignment $a \mapsto L_a$ is an algebra homomorphism

$$
L : A \longrightarrow \operatorname{End}_R(A), \qquad L_a(x) = ax ,
$$

whose image is a copy of $A$ inside the ambient operator algebra. This image is the **regular representation** of $A$, and in the commutative case it is the whole story: the left multiplication and the right multiplication by $a$ coincide, the image is its own centralizer, and every derivation of $A$ is read on it as an operator.

The first purpose of the article is to assemble the multiplication operators and to record their algebra. The second is to read the **Gelfand transform** as an operator. A character of $A$ — a unital algebra homomorphism into the ground ring — is a common eigenvector of the whole family $L(A)$: on it, $L_a$ acts by the scalar the character assigns to $a$. Collecting the scalars over all characters gives the Gelfand transform $a \mapsto (\chi \mapsto \chi(a))$, and the statement that $L_a$ is multiplication by that function is the algebraic content of the transform. The topological reading of the character set — its topology, its compactness, the fact that the transform is an isometry for a norm — belongs to *Topological Algebras and the Gelfand Transform* in Part II and *Banach Algebras* in Part III, and is named here only as a forward reference: no distance, no norm and no open set occurs in this article.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$ and $A$ is a commutative, associative and unital $R$-algebra. The unital hypothesis is used where an operator is recovered from its value at $1$; it is stated at each such point. The non-commutative case, where $L_a$ and $R_a$ differ, is *Left and Right Multiplication in a Ring*; the general ambient space of all operators is *The Operators on an Algebra*; the derivations are *Derivations of a Ring*, and their commutative-algebra form is the article *The Derivations of a Commutative Algebra* of this category.

## The Multiplication Operators

### Definition

**Definition.** For $a \in A$ the **multiplication operator** by $a$ is the $R$-linear map

$$
L_a : A \longrightarrow A, \qquad L_a(x) = ax .
$$

Because $A$ is commutative, $L_a$ is also the right multiplication $x \mapsto xa$, so there is one family and not two. The assignment is $R$-linear in the subscript, and the following identities are immediate from associativity and from the commutativity of $A$.

**Proposition.** For all $a, b \in A$ and $r \in R$,

$$
L_{a+b} = L_a + L_b, \qquad L_{ab} = L_a \circ L_b = L_b \circ L_a, \qquad L_{ra} = rL_a, \qquad L_1 = \mathrm{id}_A .
$$

*Proof.* Each identity is checked on an element $x$: $L_{a+b}(x) = (a+b)x = ax + bx$, $L_{ab}(x) = (ab)x = a(bx) = L_a(L_b x)$, $L_{ra}(x) = (ra)x = r(ax) = (rL_a)(x)$, and $L_1(x) = x$. Commutativity gives $L_aL_b = L_{ab} = L_{ba} = L_bL_a$. $\square$

**Corollary.** The image $L(A) = \{L_a : a \in A\}$ is a commutative subalgebra of $\operatorname{End}_R(A)$ with identity $L_1$, and $L : A \to L(A)$ is a surjective $R$-algebra homomorphism. If $A$ is unital then $L$ is injective, because $L_a = 0$ forces $a = L_a(1) = 0$; hence

$$
A \cong L(A)
$$

as $R$-algebras, and the **regular representation** $L$ is a faithful representation of $A$ by multiplication operators.

The injectivity is exactly the point at which the unit is used, and it is what makes the regular representation a copy of the algebra rather than a quotient of it. Without a unit the kernel is the annihilator $\{a : aA = 0\}$, which may be nonzero.

**Example.** For $A = R$ the single operator $L_a$ is multiplication by the scalar $a$ in the one-dimensional space $R$, so $L(R) = \operatorname{End}_R(R) \cong R$.

**Example.** For $A = R[x]$, the operator $L_x$ is the shift $x^k \mapsto x^{k+1}$ on the monomial basis and $L_f = f(L_x)$ for a polynomial $f$; the map $L$ is the evaluation $f \mapsto f(L_x)$. Every $L_f$ raises the degree by $\deg f$, so each $L_f$ has no nonzero eigenvalue on the polynomial algebra and has infinite order of growth on the monomials. The operator $L_x$ is the **shift**, and the regular representation is the classical realisation of a polynomial algebra by a shift.

### The Centralizer and the Double Centralizer

The multiplication operators are exactly the operators that commute with all of them.

**Theorem.** In $\operatorname{End}_R(A)$, the centralizer of $L(A)$ is $L(A)$ itself:

$$
\{T \in \operatorname{End}_R(A) : T L_a = L_a T \ \text{for all } a \in A\} = L(A) .
$$

Equivalently, every $A$-linear endomorphism of the regular module $A$ is a multiplication operator, and $A \cong \operatorname{End}_A(A)$.

*Proof.* An operator $T$ commutes with every $L_a$ precisely when $T(ax) = a\,T(x)$ for all $a, x$, which is $A$-linearity of the regular module; putting $a = x$ gives $T(a) = a\,T(1) = L_{T(1)}(a)$, so $T = L_b$ with $b = T(1)$. Conversely every $L_b$ is $A$-linear by associativity. Here the unit is again used, in the evaluation at $1$. $\square$

**Corollary.** When $A$ is free of finite rank over the field $k$, the subalgebra $L(A)$ is a maximal commutative subalgebra of $\operatorname{End}_k(A)$: it equals its own centralizer and is commutative. The double centralizer theorem for the regular module therefore terminates at the first step.

**Remark.** For a non-commutative algebra the two families $L(A)$ and $R(A)$ are different, they commute with one another, and each is the other's centralizer in the appropriate sense; the coincidence above is peculiar to the commutative case, and it is why one representation suffices here.

## The Interaction with Derivations

A derivation of $A$ is intertwined with the multiplication operators in a single identity, and the identity says that a derivation is determined by how it moves the parameters.

**Proposition.** Let $\delta \in \operatorname{Der}_R(A)$ be a derivation, $\delta(ab) = \delta(a)b + a\delta(b)$. Then for every $a \in A$,

$$
\delta \circ L_a = L_{\delta(a)} + L_a \circ \delta, \qquad \text{equivalently} \qquad [\delta, L_a] = L_{\delta(a)} .
$$

*Proof.* Apply both sides to $x$: $\delta(ax) = \delta(a)x + a\delta(x) = L_{\delta(a)}(x) + L_a(\delta x)$. $\square$

**Corollary.** The $R$-linear map $\operatorname{Der}_R(A) \to L(A)$, $\delta \mapsto L_{\delta(a)}$ for a fixed $a$, is the restriction of the adjoint action of $\operatorname{Der}_R(A)$ on the operator algebra; on the whole of $L(A)$ the derivation acts by $L_b \mapsto L_{\delta(b)}$, and this is the derivation of the commutative algebra $L(A) \cong A$ carried across the isomorphism. In particular the derivation space depends only on the algebra structure of $A$, as it must.

**Example.** For $A = R[x]$ the derivations form the free module $R[x]\partial_x$ of rank one, and $[\partial_x, L_f] = L_{f'}$ where $f' = \partial_x f$ is the formal derivative. The operator identity $[\partial_x, L_f] = L_{f'}$ is the operator form of the product rule.

## Characters and the Gelfand Transform

### Characters

**Definition.** A **character** of $A$ over $R$ is a unital $R$-algebra homomorphism $\chi : A \to R$, so that $\chi(1) = 1$, $\chi(a+b) = \chi(a)+\chi(b)$ and $\chi(ab) = \chi(a)\chi(b)$. The **character set** is

$$
\mathfrak X(A) = \operatorname{Hom}_{\mathsf{CAlg}_R}(A, R) .
$$

It is a set, and it is written here as a set: the topology it carries in the analytic theory is not used.

**Proposition.** Every character is a common eigenvector of the family $L(A)$: for every $a \in A$,

$$
\chi \circ L_a = \chi(a)\,\chi ,
$$

that is, $\chi$ is a linear functional on $A$ that is an eigenvector of the transposed operator $L_a^{\mathsf T}$ with eigenvalue $\chi(a)$. Equivalently, the ideal $\ker\chi$ is a maximal ideal of $A$ and $A/\ker\chi \cong R$.

*Proof.* $\chi(L_a x) = \chi(ax) = \chi(a)\chi(x) = \chi(a)\,\chi(x)$; the quotient statement is the first isomorphism theorem for algebras, and $\ker\chi$ is maximal because $A/\ker\chi$ is a subalgebra of the field $R$ (or of $R$ itself) containing $1$. $\square$

The eigenvalue assigned to $a$ by the character is forced: a character is a multiplicative functional, and the eigenvalues of the family are exactly the values of the characters.

**Proposition (simultaneous triangularisation).** Suppose $A$ is a finitely generated free $R$-module and that the characters separate the elements of $A$, in the sense that $\chi(a) = 0$ for all $\chi$ forces $a = 0$. Then the family $L(A)$ is **simultaneously diagonalisable** in a suitable extension of scalars: there is a basis of $A \otimes_R S$ over a ring $S$ in which every $L_a$ is diagonal, with the diagonal entries the values $\chi(a)$.

*Proof.* The hypothesis exhibits $A$ as a subalgebra of the algebra of functions $\mathfrak X(A) \to R$ and hence of a product of copies of $R$, one for each character; in the corresponding idempotent decomposition $A \otimes_R S \cong \prod_\chi S$, the operator $L_a$ is multiplication by the scalar $\chi(a)$ in the $\chi$-th coordinate. $\square$

For a finite-dimensional reduced commutative algebra over an algebraically closed field $k$, the characters are exactly the $k$-algebra homomorphisms into $k$, they separate points, and the proposition reduces to the classical diagonalisation of a commuting family of diagonalisable operators.

### The Gelfand Transform

**Definition.** The **Gelfand transform** of $A$ is the map

$$
\Gamma : A \longrightarrow \operatorname{Fun}(\mathfrak X(A), R), \qquad \Gamma(a)(\chi) = \chi(a),
$$

into the $R$-algebra of functions on the character set with pointwise operations.

**Theorem.** $\Gamma$ is a unital $R$-algebra homomorphism, and under it the multiplication operator $L_a$ becomes multiplication of functions by $\Gamma(a)$:

$$
\Gamma(L_a x) = \Gamma(a)\,\Gamma(x), \qquad \text{that is} \qquad \widehat{ax} = \hat a\,\hat x ,
$$

where $\hat a = \Gamma(a)$.

*Proof.* For $a, b \in A$ and a character $\chi$, $\Gamma(a+b)(\chi) = \chi(a+b) = \chi(a)+\chi(b)$ and $\Gamma(ab)(\chi) = \chi(ab) = \chi(a)\chi(b) = \Gamma(a)(\chi)\Gamma(b)(\chi)$, so $\Gamma$ is additive and multiplicative; $\Gamma(1)(\chi) = 1$. The second display is the defining property $\chi(ax) = \chi(a)\chi(x)$. $\square$

The kernel of $\Gamma$ is the **Jacobson radical** — the intersection of the maximal ideals, that is, the elements annihilated by every character — and $\Gamma$ is injective exactly when the characters separate points, which is the hypothesis of the triangularisation proposition. For a reduced algebra of finite type over a field the radical vanishes and the transform is injective.

**Remark (what is deferred).** The transform is treated here as an algebraic homomorphism into a ring of functions. Its analytic theory — that when $R = \mathbb{C}$ and $A$ carries a norm the character set becomes a compact space, the transform is an isometry, and it is an isomorphism onto the algebra of continuous functions for a suitable class of algebras — needs the distance of Part II and the limit of Part III. The reader will find it in *Topological Algebras and the Gelfand Transform* and *Banach Algebras*; nothing of it is used here.

## Worked Examples

### The Split-Complex Numbers

Let $A = \mathbb D = R[x]/(x^2-1)$ over $R = \mathbb R$, with basis $1, j$ and $j^2 = 1$. In this basis

$$
L_1 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad
L_j = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad
L_{a+bj} = \begin{pmatrix} a & b \\ b & a \end{pmatrix} ,
$$

so $L(A)$ is the algebra of matrices of the form $\binom{a\ b}{b\ a}$, a two-dimensional commutative subalgebra of $M_2(\mathbb R)$. The characters are the two homomorphisms $\chi_\pm$ with $\chi_\pm(j) = \pm 1$, and the eigenvalues of $L_j$ are $1$ and $-1$, so $L_j$ is a reflection, of order two. The Gelfand transform sends $a+bj$ to the pair $(\chi_+,\chi_-) = (a+b, a-b)$, which is the isomorphism $\mathbb D \cong \mathbb R \times \mathbb R$ of the idempotent decomposition.

### A Split Polynomial Algebra

Let $A = k[x]/(f)$ with $f$ monic of degree $n$ splitting into $n$ distinct linear factors over $k$: $f = (x-r_1)\cdots(x-r_n)$. Then $A \cong k^n$ by the Chinese remainder theorem and the characters are the evaluations $\chi_i(x) = r_i$. The multiplication operator $L_x$ is the companion-type matrix acting on the basis $1, x, \dots, x^{n-1}$,

$$
L_x = \begin{pmatrix}
0 & 0 & \cdots & 0 & -c_0 \\
1 & 0 & \cdots & 0 & -c_1 \\
0 & 1 & \cdots & 0 & -c_2 \\
\vdots & & \ddots & & \vdots \\
0 & 0 & \cdots & 1 & -c_{n-1}
\end{pmatrix}, \qquad f(x) = x^n + c_{n-1}x^{n-1} + \cdots + c_0 ,
$$

and the Cayley–Hamilton theorem is the statement that its characteristic polynomial is $f$. Its eigenvalues are $r_1, \dots, r_n$, the values of the characters, and the Gelfand transform is the diagonalisation by the Vandermonde matrix, which is invertible exactly because the roots are distinct.

### The Trace Pairing

**Definition.** Let $A$ be free of rank $n$ over $R$. The **trace pairing** is

$$
T : A \times A \longrightarrow R, \qquad T(a,b) = \operatorname{tr}(L_{ab}) = \operatorname{tr}(L_a L_b) .
$$

It is $R$-bilinear and symmetric, because $L_{ab} = L_aL_b = L_bL_a$ and the trace is symmetric. It satisfies $T(a, 1) = \operatorname{tr}(L_a)$, the **regular trace** of $a$, and it is **associative**,

$$
T(ab, c) = T(a, bc),
$$

because both sides are $\operatorname{tr}(L_{abc})$. The pairing is the coefficient of $a \mapsto \operatorname{tr}(L_a)$ read as a bilinear form.

**Proposition.** Every multiplication operator is **self-adjoint** for the trace pairing:

$$
T(L_a x, y) = T(x, L_a y) \qquad \text{for all } a, x, y \in A .
$$

*Proof.* $T(L_a x, y) = \operatorname{tr}(L_{(ax)y}) = \operatorname{tr}(L_{a(xy)}) = T(x, ay) = T(x, L_a y)$, using associativity of $A$ in the middle. $\square$

**Corollary.** The family $L(A)$ is a commutative subalgebra of the space of operators self-adjoint for $T$. When $T$ is non-degenerate the adjoint operation makes $\operatorname{End}_R(A)$ an algebra with an involution, and $L(A)$ lies in its self-adjoint part; the involution is developed in the `* Operator Theory` group of this category, where the pairing and the adjoint are read with the involution of the elements.

**Example.** For $A = k^n$ the multiplication operator $L_a$ with $a = (a_1, \dots, a_n)$ is the diagonal matrix $\operatorname{diag}(a_1, \dots, a_n)$, and $T(a,b) = \sum_i a_i b_i$; the trace pairing is the standard bilinear form on $k^n$. For $A = \mathbb D$ above, $T(a+bj, c+dj) = 2(ac+bd)$ by the matrix form of $L$, the factor $2$ being the rank.

## Summary

For a commutative unital $R$-algebra $A$, the **multiplication operators** $L_a(x) = ax$ satisfy $L_{ab} = L_aL_b = L_bL_a$ and $L_{a+b} = L_a + L_b$, so $L : A \to \operatorname{End}_R(A)$ is a faithful $R$-algebra homomorphism; its image is the **regular representation** $L(A)$, a commutative subalgebra isomorphic to $A$. The family is its own centralizer in the operator algebra: every operator commuting with all $L_a$ is a multiplication operator, which is the statement $\operatorname{End}_A(A) \cong A$ for the regular module. A derivation interacts with the family by $[\delta, L_a] = L_{\delta(a)}$.

The **characters** of $A$ are the unital homomorphisms $\chi : A \to R$, and each is a common eigenvector of the family, with $\chi \circ L_a = \chi(a)\chi$. Collecting the eigenvalues gives the **Gelfand transform** $\Gamma(a)(\chi) = \chi(a)$, a unital algebra homomorphism into the algebra of functions on the character set, under which $L_a$ is multiplication of functions by $\hat a$. The transform is injective exactly when the characters separate points, and its kernel is the Jacobson radical. The topological and analytic theory of the transform — the compact character space, the norm, the isometry — needs the distance of Part II and the limit of Part III and is deferred to *Topological Algebras and the Gelfand Transform* and *Banach Algebras*. The trace pairing $T(a,b) = \operatorname{tr}(L_a L_b)$ is symmetric and associative, and every multiplication operator is self-adjoint for it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $A$ | Commutative unital associative $R$-algebra |
| $L_a$, $L_a(x) = ax$ | Multiplication operator by $a$ |
| $L : A \to \operatorname{End}_R(A)$ | The regular representation |
| $L(A)$ | Image of $L$, a commutative subalgebra of $\operatorname{End}_R(A)$ |
| $[\delta, L_a] = L_{\delta(a)}$ | A derivation acts on the parameters |
| $\mathfrak X(A) = \operatorname{Hom}_{\mathsf{CAlg}_R}(A,R)$ | Character set of $A$ |
| $\chi$ | A character, $\chi(ab) = \chi(a)\chi(b)$, $\chi(1) = 1$ |
| $\Gamma$, $\hat a = \Gamma(a)$ | Gelfand transform; the function $\chi \mapsto \chi(a)$ |
| $\ker\Gamma$ | Jacobson radical, the intersection of the maximal ideals |
| $T(a,b) = \operatorname{tr}(L_aL_b)$ | Trace pairing; symmetric, associative |
| $\operatorname{tr}(L_a)$ | Regular trace of $a$ |

## Further Reading

- Israel M. Gelfand and Mark A. Naimark, "On the imbedding of normed rings into the ring of operators in Hilbert space", *Matematicheskii Sbornik* 12 (1943), 197–213, for the origin of the Gelfand transform and its spectral reading.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953), for the character space and the algebra of functions.
- Walter Rudin, *Functional Analysis*, 2nd ed. (McGraw–Hill, 1991), for the commutative Banach-algebra form of the transform, in Part II and Part III.
- Nathan Jacobson, *Lectures in Abstract Algebra*, Vol. II: *Linear Algebra* (Van Nostrand, 1953), for the regular representation and the trace form of a finite-dimensional algebra.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules*, 2nd ed. (Springer, 1992), for the regular module, its endomorphism ring and the double centralizer theorem.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for multiplication operators, derivations and the trace form.
