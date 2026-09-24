
# __Superalgebras and Graded Structures__

## Introduction

A graded algebra is an algebra with a decomposition labelled by a monoid, and the sign rule $(-1)^{|a||b|}$ of the exterior algebra of the companion article *The Exterior Algebra* is the characteristic feature of the degree-labelled case. When the labels are taken modulo $2$, so that the only information retained is **parity**, the sign rule becomes the defining relation of a **superalgebra**, and the identities of the theory acquire a sign in every place where two odd objects are exchanged. The subject of this article is that theory: graded-commutative associative superalgebras, Lie superalgebras, the Grassmann envelope that reduces the theory of Lie superalgebras to ordinary Lie algebras, and the Berezinian, which is the determinant of an even invertible supermatrix.

The exterior algebra is the universal example: if $M$ is placed in odd parity, then $\Lambda(M)$ is a graded-commutative superalgebra, and its Koszul sign rule is exactly the super sign rule. This is why graded structures and anti-symmetric algebras belong to one category: the exterior algebra is the free graded-commutative superalgebra on an odd space, and the theory of Lie superalgebras is the theory of algebras whose Grassmann envelope is a Lie algebra.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$ in which $2$ is invertible, and $K$ is a field of characteristic different from $2$; the sign rule reduces to commutativity when $2 = 0$, so the theory is vacuous in characteristic $2$ and that case is excluded. Modules are $R$-modules, and the exterior algebra is written $\Lambda(M)$ with the notation of *Exterior Powers* and *The Exterior Algebra*. Superalgebras are written lowercase fraktur when they are Lie superalgebras, so $\mathfrak{g} = \mathfrak{g}_0 \oplus \mathfrak{g}_1$. No physics is invoked.

## Graded Vector Spaces and Superalgebras

### $\mathbb{Z}$- and $\mathbb{Z}/2$-Gradings

**Definition.** A **graded $R$-module** is a module $A$ with a direct sum decomposition $A = \bigoplus_{n \in \mathbb{Z}} A_n$; a **graded algebra** is a graded module with a multiplication satisfying $A_p A_q \subseteq A_{p+q}$. A **superalgebra** is an algebra with a decomposition into two parts,

$$
A = A_0 \oplus A_1,
$$

such that $A_p A_q \subseteq A_{p+q}$ for $p, q \in \mathbb{Z}/2\mathbb{Z}$; the elements of $A_0$ are **even** and those of $A_1$ are **odd**. A **super vector space** is an $R$-module with such a decomposition, and a **supermodule** over a superalgebra is a super vector space with a parity-respecting action.

Every $\mathbb{Z}$-grading induces a $\mathbb{Z}/2$-grading by reduction modulo $2$: the even part is the sum of the even-degree pieces and the odd part the sum of the odd-degree pieces. Thus $\Lambda(M) = \bigoplus_n \Lambda^n M$ is a superalgebra with

$$
\Lambda(M)_0 = \Lambda^{\mathrm{ev}}(M) = \bigoplus_{n \text{ even}} \Lambda^n M, \qquad \Lambda(M)_1 = \Lambda^{\mathrm{odd}}(M) = \bigoplus_{n \text{ odd}} \Lambda^n M.
$$

**Definition.** For a homogeneous element $a$ of a superalgebra, its **parity** is $|a| = 0$ if $a$ is even and $|a| = 1$ if $a$ is odd. Every element is a sum of a unique even and a unique odd part, and a statement about homogeneous elements extends by linearity; in particular $(-1)^{|a|}$ means $+1$ on the even part and $-1$ on the odd part.

### The Super Sign Rule

**Definition.** An associative superalgebra $A$ is **supercommutative**, or **graded-commutative**, if

$$
ab = (-1)^{|a||b|}\, ba
$$

for all homogeneous $a, b \in A$. It is **superanticommutative** if $ab = -(-1)^{|a||b|}ba$.

**Proposition.** In a supercommutative algebra, $a^2 = 0$ for every odd $a$, and the even part $A_0$ is a commutative algebra. If $2$ is invertible in $R$, the converse holds under one further hypothesis: if $A_0$ is commutative, if $a^2 = 0$ for every odd $a$ and if every even element commutes with every odd element, then $A$ is supercommutative.

**Proof.** For odd $a$, the sign is $(-1)^{1 \cdot 1} = -1$, so $a^2 = -a^2$ and $2a^2 = 0$; invertibility of $2$ gives $a^2 = 0$. For even $a, b$ the sign is $+1$. Conversely, polarising $0 = (a+b)^2 = a^2 + ab + ba + b^2$ for odd $a, b$ gives $ab = -ba$, so odd elements anticommute; the mixed case is the extra hypothesis, since an odd element can fail to commute with an even one while both of the other conditions hold. $\square$

**Example.** The exterior algebra $\Lambda(M)$ with $M$ declared odd is supercommutative, by the Koszul sign rule of *The Exterior Algebra*. Its degree grading refines the parity grading, and the identity $x \wedge x = 0$ for $x \in M$ is the super sign rule in parity one.

### Constructing Superalgebras

The standard constructions of algebra carry over with the sign inserted.

**Definition.** The **tensor product** of two superalgebras $A$ and $B$ is the superalgebra $A \otimes_R B$ with the multiplication

$$
(a \otimes b)(a' \otimes b') = (-1)^{|b||a'|}\, (a a') \otimes (b b').
$$

**Proposition.** $A \otimes_R B$ is associative if $A$ and $B$ are; it is supercommutative if $A$ and $B$ are; and the exterior algebra satisfies

$$
\Lambda(M \oplus N) \cong \Lambda(M) \otimes_R \Lambda(N)
$$

as superalgebras, which is the isomorphism of *The Exterior Algebra* with the graded tensor product reinterpreted as a super tensor product.

**Proof.** Associativity is the verification that the two bracketings of $(a \otimes b)(a' \otimes b')(a'' \otimes b'')$ have the same sign, namely $(-1)^{|b||a'|} \cdot (-1)^{|b||a''| + |b'||a''|}$; supercommutativity follows by moving the two tensor factors past one another and collecting the signs. The isomorphism is the one already constructed degree by degree. $\square$

## The Grassmann Envelope

### The Parity Extension

Superalgebra has a universal property that makes it redundant in a precise sense: it is a theory of ordinary algebra with coefficients extended by odd variables.

**Definition.** Let $G = G_0 \oplus G_1$ be a graded-commutative associative $R$-algebra with $G_0$ containing $R$, called a **Grassmann algebra** if $G_1$ generates $G$ over $G_0$ and $G_1$ is generated by odd elements that square to zero. The standard example is $G = \Lambda(V)$ for an odd module $V$.

**Definition.** Let $\mathfrak{g} = \mathfrak{g}_0 \oplus \mathfrak{g}_1$ be a Lie superalgebra and $G$ a Grassmann algebra. The **Grassmann envelope** is the $R$-module

$$
G(\mathfrak{g}) = (G_0 \otimes_R \mathfrak{g}_0) \oplus (G_1 \otimes_R \mathfrak{g}_1),
$$

with the bracket

$$
[g \otimes x, h \otimes y] = (-1)^{|h||x|}\, (gh) \otimes [x, y], \qquad g, h \in G,\ x, y \in \mathfrak{g}.
$$

Note that $G(\mathfrak{g})$ is concentrated in parity zero: it pairs even elements of $G$ with even elements of $\mathfrak{g}$ and odd with odd. It is therefore an ordinary $R$-module with an ordinary bracket.

### The Structural Theorem

**Theorem (Berezin–Kac).** Let $\mathfrak{g} = \mathfrak{g}_0 \oplus \mathfrak{g}_1$ be a superalgebra over $R$, and let $G$ be a Grassmann algebra with $G_1 \neq 0$. Then $\mathfrak{g}$ is a Lie superalgebra if and only if its Grassmann envelope $G(\mathfrak{g})$ is a Lie algebra over $R$.

**Proof sketch.** Write $g \in G$ and $x \in \mathfrak{g}$ as homogeneous and expand. The superbracket on $\mathfrak{g}$ is recovered from the bracket on the envelope by tensoring with a basis of $G$ and using the fact that products of odd generators are nonzero, so that no relation between the structure constants is lost. The ordinary Jacobi identity for $G(\mathfrak{g})$, expanded in a basis of $G$, has components that are exactly the super Jacobi identity for $\mathfrak{g}$ together with the super antisymmetry of the bracket. $\square$

**Corollary.** Every theorem about Lie algebras that is proved by multilinear identities has a version for Lie superalgebras, and the proof is the proof of the Lie algebra statement applied to the Grassmann envelope and then read off. This is the sense in which the exterior algebra is the universal passage from an anti-symmetric structure to an ordinary one.

**Remark.** The argument also explains the presence of the signs: the sign $(-1)^{|h||x|}$ in the definition of the envelope is forced, because it is the sign that makes $G(\mathfrak{g})$ land in parity zero and makes the bracket satisfy the ordinary Jacobi identity.

## Lie Superalgebras

### Definitions and the Sign Rule

**Definition.** A **Lie superalgebra** over $R$ is a super vector space $\mathfrak{g} = \mathfrak{g}_0 \oplus \mathfrak{g}_1$ with a bilinear bracket $\mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$ preserving parity, $[\mathfrak{g}_p, \mathfrak{g}_q] \subseteq \mathfrak{g}_{p+q}$, which is **super anticommutative**,

$$
[x, y] = -(-1)^{|x||y|}\,[y, x],
$$

and satisfies the **super Jacobi identity**

$$
(-1)^{|x||z|}\,[x, [y, z]] + (-1)^{|y||x|}\,[y, [z, x]] + (-1)^{|z||y|}\,[z, [x, y]] = 0.
$$

**Remark.** In parity zero the definition is that of an ordinary Lie algebra. For odd $x$ the super anticommutativity gives $[x, x] = [x,x]$, hence **no constraint**: odd elements may have nonzero bracket with themselves. This is the single structural difference between Lie algebras and Lie superalgebras, and it is a consequence of the sign rule rather than an independent axiom.

**Example.** Let $A$ be an associative superalgebra. Define the **superbracket**

$$
[a, b] = ab - (-1)^{|a||b|}\, ba.
$$

Then $A$ with this bracket is a Lie superalgebra: the superbracket is super anticommutative by construction, and the super Jacobi identity follows from associativity. This is the super analogue of the fact that an associative algebra is a Lie algebra under the commutator, and the sign in the bracket is the sign required to make the associativity identity close up.

### The General Linear Superalgebra

**Definition.** Let $V = K^{m} \oplus K^{n}$ with the first summand even and the second odd. The **general linear superalgebra** $\mathfrak{gl}(m|n)$ is the Lie superalgebra of endomorphisms of $V$, which are the block matrices

$$
X = \begin{pmatrix} A & B \\ C & D \end{pmatrix}, \qquad A \in \mathfrak{gl}(m),\ D \in \mathfrak{gl}(n),\ B, C \text{ of the appropriate parity},
$$

with bracket $[X, Y] = XY - (-1)^{|X||Y|}YX$. Its even part is $\mathfrak{gl}(m) \oplus \mathfrak{gl}(n)$ and its odd part is the space of off-diagonal blocks, of dimension $2mn$.

**Definition.** The **supertrace** of $X = \begin{pmatrix} A & B \\ C & D\end{pmatrix}$ is

$$
\operatorname{str}(X) = \operatorname{tr}(A) - \operatorname{tr}(D).
$$

**Proposition.** $\operatorname{str}$ vanishes on superbrackets: $\operatorname{str}([X, Y]) = 0$ for all $X, Y \in \mathfrak{gl}(m|n)$. Consequently

$$
\mathfrak{sl}(m|n) = \{X \in \mathfrak{gl}(m|n) : \operatorname{str}(X) = 0\}
$$

is a Lie subalgebra of $\mathfrak{gl}(m|n)$.

**Proof.** For homogeneous $X$ and $Y$ one has $\operatorname{str}(XY) = (-1)^{|X||Y|}\operatorname{str}(YX)$. If the parities are opposite then $XY$ and $YX$ are odd, so both have zero diagonal blocks and both supertraces vanish. If $X$ and $Y$ are even, the diagonal blocks of $XY$ are $A_XA_Y$ and $D_XD_Y$ and those of $YX$ are $A_YA_X$ and $D_YD_X$, and the trace identity $\operatorname{tr}(PQ) = \operatorname{tr}(QP)$ gives equality. If $X$ and $Y$ are odd, the diagonal blocks of $XY$ are $B_XC_Y$ and $C_XB_Y$ and those of $YX$ are $B_YC_X$ and $C_YB_X$, so

$$
\operatorname{str}(XY) = \operatorname{tr}(B_XC_Y) - \operatorname{tr}(C_XB_Y) = \operatorname{tr}(B_XC_Y) - \operatorname{tr}(B_YC_X) = -\operatorname{str}(YX).
$$

In each case $\operatorname{str}(XY) = (-1)^{|X||Y|}\operatorname{str}(YX)$, and substituting into the superbracket gives $\operatorname{str}([X,Y]) = \operatorname{str}(XY) - (-1)^{|X||Y|}\operatorname{str}(YX) = 0$. $\square$

**Remark.** When $m = n$ the identity matrix has $\operatorname{str}(I_{2n}) = n - n = 0$, so $\mathfrak{sl}(n|n)$ contains the central element $I_{2n}$ and is not simple; the simple algebra is the quotient $\mathfrak{psl}(n|n) = \mathfrak{sl}(n|n)/\langle I_{2n}\rangle$, which appears in the classification below.

**Definition.** Let $\beta$ be a nondegenerate even or odd supersymmetric bilinear form on $V$. The **orthosymplectic Lie superalgebra** $\mathfrak{osp}(\beta)$ is the subalgebra of $\mathfrak{gl}(m|n)$ consisting of those $X$ with $\beta(Xv, w) + (-1)^{|X||v|}\beta(v, Xw) = 0$ for all homogeneous $v, w$; with the standard choices it is written $\mathfrak{osp}(m|n)$.

**Remark (classification).** Over $\mathbb{C}$ the finite-dimensional simple Lie superalgebras are classified. They are the classical algebras $\mathfrak{sl}(m|n)$, $\mathfrak{psl}(n|n)$, $\mathfrak{osp}(m|n)$ with the natural restrictions on $m, n$, the exceptional superalgebras $D(2,1;\alpha)$, $F(4)$ and $G(3)$, and the four infinite families $W$, $S$, $\tilde S$, $H$ of superalgebras of vector fields, due to Cartan. This classification is due to Kac and is the super analogue of the Killing–Cartan classification of *Root Systems and Classification*; the simple Lie superalgebras are not all semisimple in the ordinary sense, which is the reason the classification is a separate theorem.

## Graded-Commutative Superalgebras

### Alternating and Symmetric Elements

**Definition.** Let $A$ be a supercommutative associative superalgebra. The **supercommutator** is the bracket $[a, b] = ab - (-1)^{|a||b|}ba$, which vanishes identically on $A$, so a supercommutative algebra is exactly a Lie superalgebra with zero bracket; its structure is that of a commutative algebra in the symmetric monoidal category of super vector spaces.

**Proposition.** In a supercommutative algebra, the even part is commutative, the odd part is a module over the even part, and the product of two odd elements is even and symmetric: for odd $a, b, c$,

$$
abc = -cba, \qquad (ab)c = c(ab), \qquad (ab)c = (bc)a.
$$

**Proof.** For odd $a, b$ the sign in $ab = -ba$ is $-1$, and the product $ab$ is even, so it commutes with $c$: $(ab)c = c(ab)$. Associativity and the anticommutativity of odd elements give $cba = (cb)a = -(bc)a = -a(bc) = -(ab)c$, which is $abc = -cba$; the last identity is the same computation with the letters cyclically permuted. $\square$

**Example.** In $\Lambda(M)$ with $M$ odd, the even part $\Lambda^{\mathrm{ev}}(M)$ is commutative, and the product of two odd elements is even and behaves accordingly: for $x, y, z \in M$ one has $(x \wedge y) \wedge z = z \wedge (x \wedge y)$ in the even part.

### The Super Trace and the Berezinian

The determinant has a super analogue, and it is not the naive determinant of the block matrix.

**Definition.** Let $X = \begin{pmatrix} A & B \\ C & D\end{pmatrix}$ be an even supermatrix over a supercommutative algebra, with $A$ and $D$ even and invertible and $B, C$ odd. The **Berezinian** of $X$ is

$$
\operatorname{Ber}(X) = \det(A - B D^{-1} C)\, \det(D)^{-1} = \det(A)\, \det(D - C A^{-1} B)^{-1}.
$$

The two expressions agree over a supercommutative algebra, and the Berezinian is an even invertible element.

**Theorem.** The Berezinian is multiplicative:

$$
\operatorname{Ber}(XY) = \operatorname{Ber}(X)\operatorname{Ber}(Y)
$$

for even supermatrices with invertible even diagonal blocks, and it is characterised by the two properties $\operatorname{Ber}\!\begin{pmatrix} A & 0 \\ 0 & D\end{pmatrix} = \det(A)\det(D)^{-1}$ and multiplicativity.

**Proof.** Both sides are rational functions of the entries; by the super analogue of the splitting principle one reduces to supermatrices that are products of block diagonal and block triangular factors, and for those the formula is immediate from the definition and the multiplicativity of the ordinary determinant. The odd entries are nilpotent over a finitely generated supercommutative algebra, so the rational expression is a polynomial in the odd variables and the reduction is legitimate. $\square$

**Proposition.** For an even supermatrix $X$ one has $\operatorname{Ber}(e^X) = e^{\operatorname{str}(X)}$, where $\operatorname{str}$ is the supertrace.

**Proof.** Reduce to the diagonal case by multiplicativity: the relation is multiplicative in $X$ to first order, and both sides have the same derivative at $X = 0$, namely $\operatorname{str}$. $\square$

**Remark.** Unlike the determinant, the Berezinian is defined only on the even supermatrices: the block formula uses determinants, so the diagonal blocks must be invertible, and an odd block would have no inverse. For an even supermatrix the odd blocks are corrections to the block diagonal part, and the invertibility of the supermatrix forces the invertibility of both diagonal blocks; the two displayed expressions are therefore available and agree. The group on which $\operatorname{Ber}$ is defined is the even part of the general linear supergroup, and on it $\operatorname{Ber}$ is a homomorphism with values in the even units, so the special linear supergroup is the kernel of the Berezinian in the same way that the special linear group is the kernel of the determinant.

## The Algebra of Odd Generators

### Odd Generators and the Exterior Algebra

**Definition.** Let $M$ be an $R$-module, placed in odd parity, and let $\Lambda(M)$ be its exterior algebra with the Koszul sign rule. Then $\Lambda(M)$ is the **free supercommutative algebra** on the odd module $M$: for any supercommutative algebra $A$ and any $R$-linear map $f : M \to A_1$ with $f(x)^2 = 0$, there is a unique morphism of superalgebras $\Lambda(M) \to A$ extending $f$.

**Proof.** This is the universal property of *The Exterior Algebra*, read in parity: an odd element has square zero in a supercommutative algebra, and the parity-respecting algebra maps are exactly the algebra maps sending $M$ into the odd part. $\square$

### The Commutation Factors

Let $M$ be free with a basis of odd generators $x_1, \ldots, x_m$. The exterior algebra has the basis of squarefree monomials $x_{i_1} \cdots x_{i_k}$ with $i_1 < \cdots < i_k$, and the super sign rule reads

$$
x_{i_1} \cdots x_{i_k} = (-1)^{\sigma(i_1, \ldots, i_k)}\, x_{\sigma(i_1)} \cdots x_{\sigma(i_k)}
$$

for a permutation $\sigma$, where the sign is the sign of the permutation restricted to the chosen indices. Equivalently, the monomial $x_{i_1}\cdots x_{i_k}$ corresponding to a subset $I = \{i_1 < \cdots < i_k\}$ satisfies

$$
x_I\, x_J = \varepsilon(I, J)\, x_{I \cup J}, \qquad \varepsilon(I, J) = (-1)^{\#\{(i,j) \in I \times J : i > j\}},
$$

with $x_{I\cup J} = 0$ when $I \cap J \neq \varnothing$. The factor $\varepsilon(I, J)$ is the **commutation factor**, and the identity $\varepsilon(I,J)\varepsilon(J,I) = (-1)^{|I||J|}$ is the super sign rule.

**Proposition.** The assignment $I \mapsto x_I$ is a bijection from the finite subsets of $\{1, \ldots, m\}$ to a basis of $\Lambda(M)$, and the commutation factors satisfy the cocycle identity

$$
\varepsilon(I, J)\, \varepsilon(I \cup J, L) = \varepsilon(J, L)\, \varepsilon(I, J \cup L)
$$

for pairwise disjoint subsets $I, J, L$.

**Proof.** The basis statement is the rank computation of *Exterior Powers*. The cocycle identity counts the inversions on both sides: each of the three sets contributes its inversions with each of the others, and the counting is symmetric. $\square$

**Remark.** The commutation factors are the data that a general **graded-commutative algebra** with an arbitrary abelian grading carries: for a grading by an abelian group $\Gamma$ with a bilinear pairing $\varepsilon : \Gamma \times \Gamma \to R^\times$, the algebras with $ab = \varepsilon(|a|, |b|) ba$ are the **colour algebras**, and the exterior algebra with its Koszul sign is the case $\Gamma = \mathbb{Z}/2$ and $\varepsilon(p, q) = (-1)^{pq}$. Colour algebras are the natural generalisation of the anti-symmetric algebras of this category, and they reduce to superalgebras when the colour group is $\mathbb{Z}/2$.

## Summary

A superalgebra is an algebra graded by $\mathbb{Z}/2$; an associative superalgebra is supercommutative when $ab = (-1)^{|a||b|}ba$, and in that case odd elements square to zero and the even part is commutative. The exterior algebra with its generators placed in odd parity is the universal example and the free supercommutative algebra on an odd module; a $\mathbb{Z}$-grading with the Koszul rule reduces to a supergrading by parity.

A Lie superalgebra is super anticommutative, $[x,y] = -(-1)^{|x||y|}[y,x]$, and satisfies the super Jacobi identity; in parity zero this is an ordinary Lie algebra, and the only structural novelty is that odd elements need not bracket to zero with themselves. The associative superbracket $[a,b] = ab - (-1)^{|a||b|}ba$ makes an associative superalgebra a Lie superalgebra, and the general linear superalgebra $\mathfrak{gl}(m|n)$ with its supertrace and the orthosymplectic algebras are the basic examples; the simple Lie superalgebras over $\mathbb{C}$ are classified by Kac. The Grassmann envelope reduces the theory of Lie superalgebras to ordinary Lie algebras, which is the precise sense in which the exterior algebra is universal for the sign rule. The Berezinian is the multiplicative determinant of an even supermatrix, defined on the even part of the general linear supergroup, with $\operatorname{Ber}(e^X) = e^{\operatorname{str}(X)}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity in which $2$ is invertible |
| $K$ | Field of characteristic different from $2$ |
| $A = A_0 \oplus A_1$ | Superalgebra with even and odd parts |
| $\vert a\vert \in \{0,1\}$ | Parity of a homogeneous element |
| $ab = (-1)^{\vert a\vert\vert b\vert}ba$ | Supercommutativity; Koszul sign rule in parity |
| $\Lambda(M)$ with $M$ odd | Free supercommutative algebra on an odd module |
| $A \otimes_R B$, $(a\otimes b)(a'\otimes b') = (-1)^{\vert b\vert\vert a'\vert}(aa')\otimes(bb')$ | Super tensor product |
| $G(\mathfrak{g}) = (G_0\otimes\mathfrak{g}_0)\oplus(G_1\otimes\mathfrak{g}_1)$ | Grassmann envelope; a Lie algebra iff $\mathfrak{g}$ is a Lie superalgebra |
| $\mathfrak{g} = \mathfrak{g}_0\oplus\mathfrak{g}_1$ | Lie superalgebra |
| $[x,y] = -(-1)^{\vert x\vert\vert y\vert}[y,x]$ | Super anticommutativity; $[x,x]$ unconstrained for odd $x$ |
| $[a,b] = ab - (-1)^{\vert a\vert\vert b\vert}ba$ | Superbracket of an associative superalgebra |
| $\mathfrak{gl}(m\vert n)$ | General linear superalgebra of $K^m\oplus K^n$ |
| $\operatorname{str}\begin{pmatrix}A&B\\C&D\end{pmatrix} = \operatorname{tr}A - \operatorname{tr}D$ | Supertrace; vanishes on superbrackets |
| $\mathfrak{sl}(m\vert n)$, $\mathfrak{psl}(n\vert n)$, $\mathfrak{osp}(m\vert n)$ | Supertraceless, projective and orthosymplectic subalgebras; $\mathfrak{psl}(n\vert n) = \mathfrak{sl}(n\vert n)/\langle I_{2n}\rangle$ |
| $\operatorname{Ber}(X) = \det(A-BD^{-1}C)\det(D)^{-1}$ | Berezinian of an even supermatrix |
| $\operatorname{Ber}(XY) = \operatorname{Ber}(X)\operatorname{Ber}(Y)$, $\operatorname{Ber}(e^X) = e^{\operatorname{str}X}$ | Multiplicativity and the trace relation |
| $\varepsilon(I,J) = (-1)^{\#\{(i,j)\in I\times J : i>j\}}$ | Commutation factor of squarefree monomials |
| Colour algebra | $\Gamma$-graded algebra with $ab = \varepsilon(\vert a\vert,\vert b\vert)ba$; $\Gamma = \mathbb{Z}/2$ gives superalgebras |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for graded algebras, superalgebras, and the graded tensor product.
- F. A. Berezin, *Introduction to Superanalysis* (Reidel, 1987), for the Grassmann envelope, the supertrace, and the Berezinian.
- Victor G. Kac, "Lie Superalgebras", *Advances in Mathematics* 26 (1977), for the classification of simple Lie superalgebras.
- Manfred Scheunert, *The Theory of Lie Superalgebras* (Springer, 1979), for a systematic treatment of Lie superalgebras and their representations.
- I. N. Bernstein, D. A. Leites, and V. I. Shander, "Lie Superalgebras and Supergravity" (in *Lie Groups and Lie Algebras: Their Representations, Generalisations and Applications*, Kluwer, 1998), for the superalgebraic formalism.
- Pierre Deligne and John W. Morgan, "Notes on Supersymmetry (following Joseph Bernstein)" (in *Quantum Fields and Strings: A Course for Mathematicians*, AMS, 1999), for a rigorous algebraic development of super linear algebra.
- V. S. Varadarajan, *Supersymmetry for Mathematicians: An Introduction* (AMS, 2004), for Lie superalgebras, the Berezinian, and their geometric applications.
