# __Determinants in Jordan Matrix Algebras__

## Introduction

A determinant is a function of a square matrix of scalars, computed by the Laplace expansion. The expansion needs the entries to commute; for matrices of biquaternions they do not, and for matrices of octonions they do not even associate. This article records a determinant that exists in that setting all the same. It is defined on the **Hermitian matrices of biquaternions**, the space

$$
H_n(\mathbb{B}) = \{x \in M_n(\mathbb{B}) : x^{\natural} = x\},
$$

and it extends to the **Cartan factor of type 6**, the exceptional algebra $H_3(\mathbb{O}_{\mathbb{C}})$ of Hermitian $3\times 3$ matrices of complex octonions. The definition is inductive, modelled on the Laplace expansion with the inverse of the pivot placed on the left; its values are complex numbers; and its square is the ordinary determinant of the $2n\times 2n$ complex matrix obtained by doubling every biquaternion entry. The result is a determinant for the matrices that carry the Jordan product of the exceptional algebras, where the classical definition is not available at all.

The source is J. Hamhalter, O. F. K. Kalenda and A. M. Peralta, *Determinants in Jordan matrix algebras*, arXiv:2110.10458v2 [math.OA] (2021). The authors' original motivation is the structure of the unitary elements of the Cartan factor of type 6, which the determinant is built to serve; the determinant turns out to be of interest on its own. The auxiliary results on finite tripotents and finite $\mathrm{JBW}^*$-triples are taken from the same authors' earlier article.

The article is placed at the operator-algebraic end of the Jordan group. It assumes the Jordan algebra and the idempotent Peirce decomposition of *Jordan Algebras* and *Hermitian Idempotents and the Peirce Decomposition*; the Jordan triple system of *Jordan Triples with an Involution*; the exceptional algebras and the Albert algebra of *Special and Exceptional Jordan Algebras*; the biquaternion algebra with its two involutions, its product table and its matrix chart of *Biquaternions as a Vector Space over $\mathbb{C}$*, *The Four General Products of the Biquaternion $\mathbb{C}$ Space* and *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*; and the octonions of *Octonion Algebra*. The JB\*-triple apparatus — tripotents, their Peirce decomposition relative to a tripotent rather than to an idempotent, minimal and unitary tripotents, frames and rank, and the Cartan factors — is not available elsewhere in the corpus and is therefore developed here, in the second section, before it is used. The determinant defined here is not the classical determinant of *Linear Maps and Matrices* and does not generalise it by restriction; it is a new function on a new domain, and the two agree only through the squaring identity recorded below. The entire presentation is over $\mathbb{C}$ and $\mathbb{R}$; no physical vocabulary is used.

**Conventions.** The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$, $e_1e_2 = e_3$, a general element $\tilde{Q} = \sum_{\mu=0}^{3}Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$, and the complex norm $\tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$; the maps $^{\natural}$ and $^*$ are the two involutions introduced below. The octonion algebra $\mathbb{O}$ is the real one of *Octonion Algebra*, with basis $e_0 = 1, e_1,\dots,e_7$, and $\mathbb{O}_{\mathbb{C}} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{O}$ is its complexification. The **linear** involution of an algebra is written $^{\natural}$ and the **conjugate-linear** involution $^{*}$; on matrices they act entrywise and transpose, $x^{\natural}_{ij} = x^{\natural}_{ji}$ and $x^{*}_{ij} = x^{*}_{ji}$. The determinant of the source is written $\Delta$, and its variants $\Delta_n$ and $\Delta_{n,e}$ are distinguished by their subscripts.

## Jordan Matrix Algebras

### JB-algebras and JB\*-algebras

A **Jordan algebra** is a commutative algebra whose product satisfies the Jordan identity; the axioms, the symmetrisation $x\bullet y = \tfrac12(xy+yx)$ of an associative product, the multiplication operator $L_x$ and the Peirce decomposition are those of *Jordan Algebras*. A **Jordan Banach algebra** is a Jordan algebra that is a Banach space with $\lVert x\bullet y\rVert \leq \lVert x\rVert\lVert y\rVert$. Two classes of these are needed here.

A **JB-algebra** is a real Jordan Banach algebra satisfying $\lVert x\rVert^2 \leq \lVert x^2+y^2\rVert$ for all $x,y$. A **JB\*-algebra** is a complex Jordan Banach algebra with a conjugate-linear involution $^*$ satisfying the axiom of the normed theory,

$$
\lVert x\rVert^3 = \lVert U_x(x^*)\rVert , \qquad U_x(y) = 2\,x\bullet(x\bullet y) - (x\bullet x)\bullet y ,
$$

so that every C\*-algebra is a JB\*-algebra under the symmetrised product of *Jordan Algebras of Sesqualgebras*.

The self-adjoint part of a JB\*-algebra is a JB-algebra, and every JB-algebra is the self-adjoint part of a JB\*-algebra, which is the sense in which the JB\*-algebras of *JB\*-Algebras and the Gelfand–Naimark Theorem* and the algebras here are one class. Every C\*-algebra is a JB\*-algebra under its natural Jordan product, and every norm-closed subspace of a C\*-algebra stable under the involution and the Jordan product is a JB\*-algebra, called a **JC\*-algebra**. The algebras $H_n(\mathbb{B})$ below are JC\*-algebras.

The real JB-algebras, their order-unit norm and the cone of squares belong to *Jordan Algebras and the Positive Cone* and are not developed here; the complex side is stated above only because the determinant below lives on a JB\*-algebra and its self-adjoint part.

A **JBW\*-algebra** is a JB\*-algebra that is a dual Banach space; it has a unique isometric predual, and its product and involution are separately weak\*-continuous. Every finite-dimensional JB\*-algebra is a JBW\*-algebra, which is the only case needed here.

### JB\*-triples, tripotents and Cartan factors

The ternary structure is the one of *Jordan Triples with an Involution*, with the analytic axioms of the normed theory added. A **JB\*-triple** is a complex Banach space $E$ with a triple product $\{x,y,z\}$, symmetric and bilinear in the outer variables and conjugate-linear in the middle one, satisfying the Jordan triple identity, the condition that $L(x,x)$ be a hermitian operator with non-negative spectrum, and $\lVert\{x,x,x\}\rVert = \lVert x\rVert^3$, where $L(x,y)z = \{x,y,z\}$. A C\*-algebra is a JB\*-triple under

$$
\{x,y,z\} = \tfrac12\bigl(xy^*z + zy^*x\bigr),
$$

and a norm-closed subspace stable under this product is a JC\*-triple. Every JB\*-algebra is a JB\*-triple under

$$
\{x,y,z\} = (x\bullet y^*)\bullet z + (z\bullet y^*)\bullet x - (x\bullet z)\bullet y^*,
$$

the ternary product generated by the binary one. The quadratic operator of a JB\*-algebra is $U_a(x) = 2\,a\bullet(a\bullet x) - (a\bullet a)\bullet x$, which in the C\*-case is $U_a(x) = axa$; it satisfies $U_a(1) = a^2$. In a unital JB\*-algebra the unital triple automorphisms are exactly the Jordan \*-automorphisms, since $\{a,1,b\} = a\bullet b$ and $a^* = \{1,a,1\}$.

The **Peirce decomposition** of $E$ relative to a tripotent $e$ is the eigenspace decomposition of $L(e,e)$, the operator $x\mapsto\{e,x,e\}$ that the source writes $Q(e)$, with the eigenvalues $1, \tfrac12, 0$,

$$
E = E_2(e)\oplus E_1(e)\oplus E_0(e),
$$

and $E_2(e)$ is a unital JB\*-algebra with unit $e$, product $a\bullet_e b = \{a,e,b\}$ and involution $a^{*_e} = \{e,a,e\}$; on $E_2(e)$ the operator $L(e,e)$ is that involution. For a partial isometry $e$ of a C\*-algebra the Peirce spaces are $E_2(e) = ee^*Ae^*e$, $E_0(e) = (1-ee^*)A(1-e^*e)$ and $E_1(e)$, the sum of the two off-diagonal corners. A tripotent is **complete** if $E_0(e) = 0$, **minimal** if $E_2(e) = \mathbb{C}e$, and **unitary** if $E_2(e) = E$; two tripotents are **orthogonal**, $e\perp v$, if $\{e,e,v\} = 0$, and $e\leq u$ means that $u-e$ is a tripotent orthogonal to $e$ — equivalently that $e$ is a projection of the JB\*-algebra $E_2(u)$. A **frame** is an orthogonal family of minimal tripotents whose sum is complete, equivalently a maximal family of mutually orthogonal minimal tripotents; every finite orthogonal family of minimal tripotents extends to a frame, all the frames of one Cartan factor have the same cardinality, and any two frames are interchanged by a triple automorphism. The **rank** of $E$ is the least cardinal that bounds the cardinality of an orthogonal subset, and the rank of a tripotent is the rank of $E_2(e)$; for a Cartan factor this rank is the common cardinality of its frames.

The **Cartan factors** are the finite-rank JBW\*-triples from which every JBW\*-triple of type I is assembled. Two of the six types occur here. A Cartan factor of **type 4**, or **spin factor**, is a complex Hilbert space with a conjugation and the product $\{x,y,z\} = \langle x,y\rangle z + \langle z,y\rangle x - \langle x,\overline z\rangle\overline y$; the spin factors are the subject of *Spin Factors and the Clifford Envelope with Inner Conjugation*. A Cartan factor of **type 6** is the algebra $H_3(\mathbb{O}_{\mathbb{C}})$ constructed below, which is the exceptional case: it is not a JC\*-algebra, and it is a quotient of an ideal in every exceptional JB\*-algebra.

## The Biquaternions and the Doubling

### The Cayley–Dickson ladder

Both matrix algebras of this article are read through one doubling process. Starting from $\mathbb{C}$ and writing $\mathbb{A}_0 = \mathbb{C}$, the algebras $\mathbb{A}_{n+1} = \mathbb{A}_n\oplus\mathbb{A}_n$ are defined, and every $\mathbb{A}_n$ carries a product, a conjugation $\overline{\,\cdot\,}$, a linear involution $^{\natural}$ and a conjugate-linear involution $^{*}$, related by

$$
\overline{(x_1,x_2)} = (\overline{x_1},\overline{x_2}), \qquad
(x_1,x_2)^{\natural} = (x_1^{\natural},-x_2), \qquad
(x_1,x_2)^{*} = (x_1^{*},-\overline{x_2}),
$$

$$
(x_1,x_2)(y_1,y_2) = \bigl(x_1y_1 - y_2x_2^{\natural},\; x_1^{\natural}y_2 + y_1x_2\bigr).
$$

The three maps satisfy $x^{*} = \bar x^{\natural} = \overline{x^{\natural}}$, $x^{\natural} = \bar x^{*} = \overline{x^{*}}$ and $\bar x = (x^{\natural})^{*} = (x^{*})^{\natural}$. At the first steps,

- $\mathbb{A}_0 = \mathbb{C}$;
- $\mathbb{A}_1 \cong \mathbb{C}\oplus\mathbb{C}$ as a commutative C\*-algebra;
- $\mathbb{A}_2 = \mathbb{B}$, the biquaternions, a non-commutative C\*-algebra isomorphic to $M_2(\mathbb{C})$;
- $\mathbb{A}_3 = \mathbb{O}_{\mathbb{C}}$, the complex octonions, alternative but neither commutative nor associative.

The real form $(\mathbb{A}_n)_{\mathbb{R}} = \{x\in\mathbb{A}_n : \overline x = x\}$ gives the ladder $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{O}$, with $(\mathbb{A}_1)_{\mathbb{R}}\cong\mathbb{C}$, $(\mathbb{A}_2)_{\mathbb{R}} = \mathbb{H}$ and $(\mathbb{A}_3)_{\mathbb{R}} = \mathbb{O}$. Useful identifications are $\mathbb{A}_0 = \{(x,x)\}$, $(\mathbb{A}_0)_{\mathbb{R}} = \{(x,x) : x\in\mathbb{R}\}$ and $(\mathbb{A}_1)_{\mathbb{R}} = \{(x,\overline x)\}$ inside $\mathbb{C}\oplus\mathbb{C}$.

The algebra $\mathbb{A}_n$ is a JB\*-triple under the spin-factor product, and its unit $1$ is a unitary element for that structure, so $\mathbb{A}_n$ is also a unital JB\*-algebra with the symmetrised product $x\bullet y = \tfrac12(xy+yx) = \{x,1,y\}$. The two structures are tied by

$$
\langle x,y\rangle = \tfrac12\bigl(xy^{*} + \overline y\,x^{\natural}\bigr) = \tfrac12\bigl(x\bullet y^{*} + \overline y\bullet x\bigr).
$$

### The biquaternions as a matrix algebra

The isomorphism $\mathbb{B}\to M_2(\mathbb{C})$ used below is the chart

$$
(x_1,x_2,x_3,x_4) \longmapsto
\begin{pmatrix}
x_1+ix_2 & x_3+ix_4\\
-x_3+ix_4 & x_1-ix_2
\end{pmatrix},
\qquad x_1,\dots,x_4 \in \mathbb{C},
$$

in which $(x_1,x_2,x_3,x_4)$ are the complex coordinates of $\tilde Q$ in the basis $1,e_1,e_2,e_3$, so that $e_1,e_2,e_3$ go to $i\sigma_3,i\sigma_2,i\sigma_1$, the quaternion units are the pure imaginary Pauli matrices and the scalar $i$ is the central imaginary unit. Three properties of this chart are used repeatedly.

1. It is multiplicative: the image of a product is the product of the images.
2. The determinant of the $2\times 2$ image of $\tilde Q$ is the complex norm, $\det\iota(\tilde Q) = \tilde Q\tilde Q^{\natural} = \sum_\mu Q_\mu^2$. This is the biquaternion norm of *Biquaternion Norm and Invertibility* read as a determinant.
3. The two involutions correspond to the two matrix operations that respect the chart: the image of $^{\natural}$ is the **adjugate**, $\iota(\tilde Q^{\natural}) = \operatorname{adj}\iota(\tilde Q)$, and the image of $^{*}$ is the **conjugate transpose**, $\iota(\tilde Q^{*}) = \iota(\tilde Q)^{\dagger}$.

### Hermitian matrices of biquaternions

For $x = (x_{ij})\in M_n(\mathbb{B})$ the involution $^{\natural}$ acts entrywise and transposes, $x^{\natural}_{ij} = x^{\natural}_{ji}$. The fixed space

$$
H_n(\mathbb{B}) = \{x\in M_n(\mathbb{B}) : x^{\natural} = x\}
$$

is the space of **Hermitian matrices of biquaternions**; in the $n=1$ case it is the set of complex scalars, since $q^{\natural} = q$ forces $q\in\mathbb{C}$. The space $H_n(\mathbb{B})$ is closed under the symmetrised product, because $(xy+yx)^{\natural} = y^{\natural}x^{\natural} + x^{\natural}y^{\natural} = yx + xy$ when $x$ and $y$ are Hermitian, and it is stable under $^{*}$; it is therefore a JC\*-algebra, a Jordan \*-subalgebra of $M_n(\mathbb{B})$.

The doubling used for the determinant is the isomorphism $M_n(\mathbb{B})\cong M_{2n}(\mathbb{C})$ obtained by applying the chart to every entry. Under it a Hermitian matrix of biquaternions becomes a matrix $\widehat{x}\in M_{2n}(\mathbb{C})$, and the entrywise and transposing involution becomes a correspondence between the blocks. The space $H_n(\mathbb{B})$ is a complex vector space, because $^{\natural}$ is complex-linear; a Hermitian matrix is determined by its diagonal and its upper triangle, so

$$
\dim_{\mathbb{C}} H_n(\mathbb{B}) = n + 4\cdot\tfrac{n(n-1)}2 = 2n^2-n ,
$$

the $n$ counting the complex diagonal entries and the rest the independent biquaternion entries above the diagonal, each of complex dimension four.

### The determinant on $H_n(\mathbb{B})$

The classical Laplace expansion is not available, because the entries of a biquaternion matrix do not commute and because the pivot has to be inverted on one side. The determinant is therefore defined inductively, with the pivot on the left.

**Theorem.** There is a unique sequence of maps $\Delta_n : H_n(\mathbb{B})\to\mathbb{B}$, $n\geq 1$, such that

1. $\Delta_n$ is continuous for every $n$;
2. $\Delta_1(x) = x_{11}$ for $x\in H_1(\mathbb{B}) = \mathbb{C}$;
3. if $x\in H_{n+1}(\mathbb{B})$ and $x_{11}\neq 0$, then

$$
\Delta_{n+1}(x) = x_{11}\cdot\Delta_n\bigl(x_{ij} - x_{11}^{-1}x_{i1}x_{1j}\bigr)_{2\leq i,j\leq n+1}.
$$

Moreover:

4. the values of $\Delta_n$ are complex numbers;
5. $\Delta_n(\alpha x) = \alpha^n\Delta_n(x)$ for $\alpha\in\mathbb{C}$;
6. $\Delta_n(x) = \sum_{\sigma,\pi\in S_n}\alpha_{\sigma,\pi}\,x_{\sigma(1)\pi(1)}\cdots x_{\sigma(n)\pi(n)}$ for a family of complex coefficients $\alpha_{\sigma,\pi}$;
7. $\det\widehat{x} = \bigl(\Delta_n(x)\bigr)^2$ for $x\in H_n(\mathbb{B})$;
8. $\lambda\mapsto\Delta_n(\lambda y + x)$ is a complex polynomial of degree at most $n$, with the coefficient of $\lambda^n$ equal to $\Delta_n(y)$ and the constant term equal to $\Delta_n(x)$;
9. every eigenvalue of $\widehat{x}$ has even multiplicity, and $\Delta_n(x)$ is the product of all the eigenvalues of $\widehat{x}$, each counted with **half** its multiplicity.

The recursion in the third item is well posed: a Hermitian matrix has $x_{11}\in\mathbb{C}$, which is therefore invertible whenever it is nonzero, and the matrix shown on the right is again Hermitian. The maps are defined with values in the biquaternion algebra because the recursion is a computation inside it; the fourth item says that the values in fact land in the complex scalars, and the ninth explains why. The recursion determines $\Delta_n$ on the dense set $x_{11}\neq 0$ and the continuity of the first item extends it, which is where the uniqueness comes from.

Three of the assertions carry the content. The seventh says that Hermitian matrices of biquaternions have ordinary determinants that are perfect squares, and that $\Delta_n$ is a distinguished square root of them; it is what makes $\Delta_n$ a determinant rather than an arbitrary polynomial. The ninth is its eigenvalue form: the eigenvalues of the doubled matrix pair up, and $\Delta_n$ takes one from each pair. The sixth says that $\Delta_n$ is a polynomial in the entries, but one with a coefficient for every **pair** of permutations $\sigma,\pi$ rather than a single sign $(-1)^\sigma$; the commutative formula is the collapse of these coefficients, and its non-commutative replacement is not an alternating sum.

The first two cases read explicitly. For $n = 1$, $\Delta_1(x) = x_{11}$ and the square root is the identity. For $n = 2$, with $x = \begin{pmatrix}p & u\\ u^{\natural} & q\end{pmatrix}$, $p,q\in\mathbb{C}$ and $u\in\mathbb{B}$,

$$
\Delta_2(x) = p\,q - u^{\natural}u ,
$$

the classical $2\times 2$ determinant with the product of the two off-diagonal entries replaced by the complex norm of the off-diagonal entry. The quantity $u^{\natural}u = \sum_\mu u_\mu^2$ is a complex scalar and not a real number, so $\Delta_2(x)$ is complex, as it must be. For $n = 3$ on $H_3(\mathbb{B})$, and for $x_{11}\neq 0$ with the general case by continuity, Sarrus' rule survives:

$$
\Delta_3(x) = x_{11}x_{22}x_{33} + x_{32}x_{21}x_{13} + x_{31}x_{12}x_{23} - x_{11}x_{32}x_{23} - x_{22}x_{31}x_{13} - x_{21}x_{12}x_{33},
$$

with the order of the factors in each product decisive, since the biquaternion algebra is associative but not commutative; the deletion identity that makes the expanded products collapse to this form uses the complex diagonal entries.

### The determinant relative to a unitary

The determinant is not attached to the standard unit alone. If $e\in H_n(\mathbb{B})$ is unitary, the algebra $H_n(\mathbb{B})$ carries a second JB\*-algebra structure in which $e$ is the unit, with the operations

$$
x\bullet_e y = \{x,e,y\}, \qquad x^{*_e} = \{e,x,e\},
$$

and this structure is isomorphic to the standard one. There is a \*-isomorphism $T : M_n(\mathbb{B})\to M_n(\mathbb{B})$ carrying the $e$-structure to the standard one and preserving $H_n(\mathbb{B})$, given by $T(x) = v^{*}xv^{*}$ for a square root $v\in H_n(\mathbb{B})$ of $e$, which is unitary; and setting

$$
\Delta_{n,e}(x) = \Delta_n(Tx)
$$

gives a determinant relative to $e$ which does not depend on the choice of $T$, and for which

$$
\Delta_n(x) = \Delta_{n,e}(x)\cdot\Delta_n(e), \qquad x\in H_n(\mathbb{B}).
$$

This is the change-of-unit rule for the determinant, and it is the identity that the Cartan-factor version repeats in the form $\Delta(u) = \Delta_e(u)\,\Delta(e)$.

## The Cartan Factor of Type 6

### The algebra

The Cartan factor of type 6 is

$$
C_6 = H_3(\mathbb{O}_{\mathbb{C}}) = \{x\in M_3(\mathbb{O}_{\mathbb{C}}) : x^{\natural} = x\}
$$

with the Jordan product $x\bullet y = \tfrac12(xy+yx)$, the involution $^{*}$ and its JB\*-norm. A general element is

$$
x = \begin{pmatrix}
\alpha & a & b\\
a^{\natural} & \beta & c\\
b^{\natural} & c^{\natural} & \gamma
\end{pmatrix},
\qquad \alpha,\beta,\gamma\in\mathbb{C},\; a,b,c\in\mathbb{O}_{\mathbb{C}},
$$

so that $\dim_{\mathbb{C}}C_6 = 3 + 3\cdot 8 = 27$. The element $x$ is self-adjoint, $x^{*} = x$, exactly when $\alpha,\beta,\gamma$ are real and $a,b,c$ are in $\mathbb{O}$; the self-adjoint part is the real Albert algebra $H_3(\mathbb{O})$ of *Special and Exceptional Jordan Algebras*, of real dimension $27$. The algebra $C_6$ is unital, its unit is the unit matrix, and it is of rank three, the unit being the sum of three mutually orthogonal minimal projections. Frames behave as the rank suggests: if $u_1,u_2,u_3$ and $v_1,v_2,v_3$ are two triples of mutually orthogonal minimal tripotents, then the sums $u_1+u_2+u_3$ and $v_1+v_2+v_3$ are unitary and there is a triple automorphism $T$ of $C_6$ with $T(u_j) = v_j$, a Jordan \*-automorphism when all six are projections. Any triple of mutually orthogonal minimal tripotents is therefore a frame, and any two frames are exchanged by an automorphism.

### Unitaries and their spectral decomposition

**Theorem.** Let $u\in C_6$ be unitary.

1. There are complex units $\alpha_1,\alpha_2,\alpha_3$ and mutually orthogonal minimal projections $p_1,p_2,p_3$ with $u = \alpha_1p_1 + \alpha_2p_2 + \alpha_3p_3$.
2. The triple $(\alpha_1,\alpha_2,\alpha_3)$ is unique up to reordering, and for a complex unit $\alpha$ the sum $\sum_{\alpha_j = \alpha}p_j$ is determined.
3. There is a Jordan \*-automorphism $T$ of $C_6$ with $T(u)$ diagonal.

The same statement holds with real numbers in place of the complex units when $u$ is self-adjoint, and in that form it is used to extend the determinant from the unitaries to all self-adjoint elements. The decomposition is elementary and the source states it for every finite-dimensional JB\*-algebra: for a normal element — in particular for a unitary or a self-adjoint one — the Jordan \*-subalgebra generated by the element and its adjoint is a finite-dimensional commutative C\*-algebra, hence $*$-isomorphic to $\mathbb{C}^n$, in which the element is an $n$-tuple of complex units when it is unitary and of real numbers when it is self-adjoint, and the coordinate idempotents are the mutually orthogonal projections of the decomposition. An element is called **normal** if it is a linear combination of mutually orthogonal minimal projections, equivalently if the Jordan \*-subalgebra it generates with its adjoint is associative. Both the unitaries and the self-adjoint elements are normal, and the definition is the common roof under which the two spectral decompositions are one.

The theorem permits the definition of the **determinant of a unitary** by

$$
\Delta(u) = \alpha_1\alpha_2\alpha_3 ,
$$

and this is invariant under the Jordan \*-automorphisms of $C_6$, because such an automorphism permutes the triple of coefficients. The same definition with the unit $e$ in place of the matrix unit gives $\Delta_e(u)$ for a pair of unitaries $u,e$, and the two are linked by the product theorem.

**Product theorem.** For unitary $u,e\in C_6$,

$$
\Delta(u) = \Delta_e(u)\cdot\Delta(e).
$$

The proof turns on the reduction theorem below and on the corresponding rule for $H_n(\mathbb{B})$. Two corollaries are used later. If $u$ is self-adjoint in the JB\*-algebra with unit $e$, then $u = u_1-u_2$ with $u_1,u_2$ orthogonal projections below $e$ and $u_1+u_2 = e$, so its coefficients relative to $e$ are $\pm1$ and

$$
\Delta(u) = \Delta(e) \quad\text{or}\quad \Delta(u) = -\Delta(e).
$$

And for a triple automorphism $T$ of $C_6$,

$$
\Delta\bigl(T(u)\bigr) = \Delta(u)\cdot\Delta\bigl(T(1)\bigr),
$$

which measures the failure of $\Delta$ to be invariant under an arbitrary triple automorphism; it is invariant under the Jordan \*-automorphisms, which fix the unit.

### Reduction of two unitaries to biquaternions

**Theorem.** For unitary $u,e\in C_6$ there is a Jordan \*-automorphism $T$ of $C_6$ with $T(e)$ diagonal and all entries of $T(u)$ in $\mathbb{B}$.

Up to a Jordan \*-automorphism the two unitaries therefore lie in $H_3(\mathbb{B})$, a Jordan \*-subalgebra of the C\*-algebra $M_3(\mathbb{B})\cong M_6(\mathbb{C})$. The Jordan \*-subalgebra generated by two unitaries is thus not merely some JC\*-algebra, as the functional calculus already shows; the surrounding C\*-algebra can be taken to be $M_3(\mathbb{B})$, and the inclusions can be induced by a Jordan \*-automorphism of $C_6$, so that the whole structure, determinants included, is preserved. The same statement with **normal** in place of unitary holds for a pair of normal elements, and applying it to the real and imaginary parts of an arbitrary element $x = a+ib$ gives the next corollary.

**Corollary.** For every $x\in C_6$ there is a Jordan \*-automorphism $T$ of $C_6$ with all entries of $T(x)$ in $\mathbb{B}$.

This is the reduction that makes the biquaternion theory sufficient for the whole Cartan factor.

### Minimal projections

The minimal projections of $C_6$ have an explicit description, a result of independent interest which the source also uses as a tool: through the rank-two lemma below it is what identifies the determinant of an element of $H_3(\mathbb{B})$ with the product of its spectral values.

**Theorem.** The minimal projections of $C_6$ are exactly the matrices

$$
\begin{pmatrix}
0&0&0\\0&0&0\\0&0&1
\end{pmatrix},
$$

$$
\begin{pmatrix}
0&0&0\\ 0&\alpha&a\\ 0&a^{\natural}&\tfrac1\alpha\lVert a\rVert^2
\end{pmatrix},
\qquad \alpha\in\mathbb{R}\setminus\{0\},\; a\in\mathbb{O},\; \alpha = \alpha^2 + \lVert a\rVert^2 ,
$$

$$
\begin{pmatrix}
\alpha&a&b\\
a^{\natural}&\tfrac1\alpha\lVert a\rVert^2&\tfrac1\alpha(a^{\natural}b)\\
b^{\natural}&\tfrac1\alpha(b^{\natural}a)&\tfrac1\alpha\lVert b\rVert^2
\end{pmatrix},
\qquad \alpha\in\mathbb{R}\setminus\{0\},\; a,b\in\mathbb{O},\; \alpha = \alpha^2 + \lVert a\rVert^2 + \lVert b\rVert^2 .
$$

The constraint is a quadratic condition on $\alpha$. In the second family $\alpha = \tfrac12\bigl(1\pm\sqrt{1-4\lVert a\rVert^2}\bigr)$, so a real $\alpha$ exists exactly when $\lVert a\rVert\leq\tfrac12$ and then there are two of them, possibly coincident; in the third family the same formula holds with $\lVert a\rVert^2+\lVert b\rVert^2$ in place of $\lVert a\rVert^2$. The set of minimal projections is therefore the single matrix of the first form together with two families parameterised by one and by two real octonions; in the second case the third row is the second multiplied on the left by $\tfrac1\alpha a^{\natural}$, and in the third case the second and third rows are the first multiplied on the left by $\tfrac1\alpha a^{\natural}$ and $\tfrac1\alpha b^{\natural}$. The structural content of the description is the **rank-two lemma**: a minimal projection $q\in H_3(\mathbb{B})$ — the entries here are quaternions, the octonion case being the theorem above — has $\widehat{q}\in M_6(\mathbb{C})$ of rank two. Its proof is a case check on the three forms. In the second case the third row of $q$ is a left multiple of the second, so rows five and six of the doubled matrix are combinations of rows three and four, which are independent; in the third case every row of the doubled matrix is a combination of the first two.

### Automorphisms

The automorphisms used in the proofs are of two kinds. Exchanging two rows of a matrix of $C_6$ and then the corresponding two columns defines a Jordan \*-automorphism $U_{k,l}$ of $C_6$. It is the shift $x\mapsto\{u,x^{*},u\}$ by the symmetry $u$ that is the corresponding permutation matrix; a shift by a unitary element is a triple automorphism, and this one fixes the unit and is therefore a Jordan \*-automorphism. Since $u\bullet u = 1$ the shift reads $\{u,x^{*},u\} = 2\,u\bullet(x\bullet u) - x = uxu$, which is exactly the exchange of the two rows and columns.

The second kind is induced from the octonions. A linear bijection $T$ of $\mathbb{O}_{\mathbb{C}}$ is an **asymmetric triple isomorphism** if it preserves the asymmetric triple product,

$$
T\bigl((xy^{*})z\bigr) = \bigl(T(x)T(y)^{*}\bigr)T(z),
$$

and it is **hermitian** if in addition $T(\overline x) = \overline{T(x)}$; it then preserves $\mathbb{O}$. A hermitian asymmetric triple isomorphism $T$ of $\mathbb{O}_{\mathbb{C}}$ induces a Jordan \*-automorphism $\widetilde T$ of $C_6$ acting on the three off-diagonal octonion entries, and conjugating $\widetilde T$ by the row and column exchanges $U_{k,l}$ produces three further automorphisms $\widetilde T_1,\widetilde T_2,\widetilde T_3$. These automorphisms normalise an octonion: for any nonzero $u\in\mathbb{O}$ there is an asymmetric triple isomorphism carrying $u$ into the real line $\operatorname{span}\{e_0\}$, an automorphism carrying $u$ into $\operatorname{span}\{e_0,e_1\}$, and an automorphism fixing $e_1$ and carrying $u$ into $\operatorname{span}\{e_0,e_1,e_2\}$. These are the normalisations used to bring a minimal projection of $C_6$ into one of the three canonical forms above.

## The Determinant on the Cartan Factor

### From the unitaries to all the elements

The determinant has so far been defined on the unitaries of $C_6$ and, separately, on the Hermitian matrices of biquaternions of every order. The two agree where both are defined, and together they extend to all of $C_6$.

**Theorem.** Let $x\in C_6$.

1. There is a unitary $u\in C_6$ with $x = \{u,x,u\}$.
2. For such a $u$ there are real numbers $\alpha_1,\alpha_2,\alpha_3$ and mutually orthogonal minimal tripotents $u_1,u_2,u_3$ with $u_j\leq u$ and $x = \alpha_1u_1+\alpha_2u_2+\alpha_3u_3$; the triple $(\alpha_1,\alpha_2,\alpha_3)$ is unique up to reordering, and for a real number $\alpha$ the sum $\sum_{\alpha_j = \alpha}u_j$ is determined.
3. Setting $\Delta_u(x) = \alpha_1\alpha_2\alpha_3$ gives a quantity which, when $x$ is unitary, equals the determinant of the unitary case, and which, when $x$ and $u$ lie in $H_3(\mathbb{B})$, equals the relative determinant $\Delta_{3,u}(x)$.
4. The product
    $$
    \Delta(x) = \Delta_u(x)\cdot\Delta(u)
    $$
    does not depend on the choice of $u$ among the unitaries of the first item; it coincides with the determinant of the unitary case when $x$ is unitary, and with $\Delta_3(x)$ when $x\in H_3(\mathbb{B})$.
5. Every Jordan \*-automorphism of $C_6$ preserves $\Delta$.

The first item is the range tripotent: an element $x$ of a finite-rank JB\*-triple has a range tripotent $r(x)$, which satisfies $x = \{r(x),x,r(x)\}$ and is positive in the algebra $(C_6)_2(r(x))$; extending $r(x)$ to a unitary $u$ gives $x = \{u,x,u\}$. The decomposition of the second item is the spectral decomposition of $x$ in the JB\*-algebra that $C_6$ becomes when the unit is moved to $u$, that is the Peirce space $E_2(u)=C_6$ read with $u$ as unit; this algebra is Jordan \*-isomorphic to $C_6$ and of rank three, so the spectrum has at most three points and the tripotents $u_j$ are the projections of the unit $u$. The fourth item, which is what makes $\Delta$ a function of $x$ alone, is proved by the reduction to biquaternions and the change-of-unit rule for $\Delta_n$.

Finally, for a triple automorphism $T$ of $C_6$ the analogue of the unitary case holds,

$$
\Delta\bigl(T(x)\bigr) = \Delta(x)\cdot\Delta\bigl(T(1)\bigr), \qquad x\in C_6 .
$$

## Summary

A determinant is defined on the Hermitian matrices of biquaternions $H_n(\mathbb{B})$ and on the exceptional Cartan factor of type 6, $C_6 = H_3(\mathbb{O}_{\mathbb{C}})$, in the two cases where the classical Laplace expansion is unavailable.

- The definition is inductive, with the inverse of the pivot on the left, and it is unique; it takes values in $\mathbb{C}$.
- Its square is the ordinary determinant of the doubled matrix: $\det\widehat{x} = \Delta_n(x)^2$; every eigenvalue of $\widehat{x}$ has even multiplicity, and $\Delta_n(x)$ is their product with each multiplicity halved.
- It is homogeneous of degree $n$, polynomial in the entries with a coefficient for each pair of permutations, and the polynomial $\lambda\mapsto\Delta_n(\lambda y+x)$ has degree at most $n$.
- For $n = 2$ it is $\Delta_2(x) = x_{11}x_{22} - x_{12}^{\natural}x_{12}$, in which the off-diagonal product is replaced by the complex norm of the biquaternion.
- A determinant relative to a unitary $e$ is defined on the algebra with unit $e$, and $\Delta_n(x) = \Delta_{n,e}(x)\Delta_n(e)$; on $C_6$ the same rule reads $\Delta(u) = \Delta_e(u)\Delta(e)$ for unitaries.
- A unitary of $C_6$ is $\alpha_1p_1+\alpha_2p_2+\alpha_3p_3$ with $\alpha_j$ complex units and $p_j$ orthogonal minimal projections, uniquely up to reordering, and $\Delta(u) = \alpha_1\alpha_2\alpha_3$.
- Any two unitaries, any two normal elements, and any single element of $C_6$ are carried by a Jordan \*-automorphism into $H_3(\mathbb{B})$, so the biquaternion determinant governs the whole Cartan factor.
- The minimal projections of $C_6$ have an explicit description in three cases: one matrix, and two families parameterised by one and by two real octonions whose real parameter is constrained to at most two values. A minimal projection of $H_3(\mathbb{B})$ doubles to a matrix of rank two.
- The determinant of $C_6$ extends from the unitaries to every element, is independent of the unitary used in the spectral decomposition, and is preserved by the Jordan \*-automorphisms; for a triple automorphism it transforms by $\Delta(T(x)) = \Delta(x)\Delta(T(1))$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{A}_n$ | Cayley–Dickson level over $\mathbb{C}$; $\mathbb{A}_2 = \mathbb{B}$, $\mathbb{A}_3 = \mathbb{O}_{\mathbb{C}}$ |
| $\mathbb{O}_{\mathbb{C}}$, $\mathbb{O}$ | Complex octonions, real octonions $(\mathbb{O}_{\mathbb{C}})_{\mathbb{R}}$ |
| $x^{\natural}$ | Linear involution; on $\mathbb{B}$ the quaternion conjugation, $qq^{\natural} = \sum_\mu Q_\mu^2$ |
| $x^{*}$ | Conjugate-linear involution; its image under the doubling is the conjugate transpose |
| $\overline{\,\cdot\,}$ | Conjugation of the Cayley–Dickson ladder, $\bar x = (x^{\natural})^{*}$ |
| $M_n(\mathbb{B})\cong M_{2n}(\mathbb{C})$, $\widehat{x}$ | Doubling of a biquaternion matrix |
| $H_n(\mathbb{B})$ | Hermitian (that is, $^{\natural}$-fixed) $n\times n$ matrices of biquaternions |
| $C_6 = H_3(\mathbb{O}_{\mathbb{C}})$ | Cartan factor of type 6, $\dim_{\mathbb{C}} = 27$ |
| $H_3(\mathbb{O})$ | Self-adjoint part of $C_6$; the real Albert algebra |
| $x\bullet y$, $x\bullet_e y$ | Jordan product, and the Jordan product relative to the unit $e$ |
| $\{x,y,z\}$ | Triple product of a JB\*-triple |
| $E_2(e),E_1(e),E_0(e)$ | Peirce spaces of a tripotent $e$ |
| $\Delta_n$, $\Delta_{n,e}$ | Determinant on $H_n(\mathbb{B})$, and relative to a unitary $e$ |
| $\Delta$, $\Delta_e$ | Determinant on $C_6$, and relative to a unitary $e$ |
| $U_{k,l}$ | Jordan \*-automorphism of $C_6$ exchanging rows and columns $k,l$ |
| $\widetilde T$ | Jordan \*-automorphism of $C_6$ induced by a hermitian asymmetric triple isomorphism $T$ of $\mathbb{O}_{\mathbb{C}}$ |

## Further Reading

- J. Hamhalter, O. F. K. Kalenda and A. M. Peralta, *Determinants in Jordan matrix algebras*, arXiv:2110.10458v2 [math.OA] (2021). The source of this article: the inductive determinant $\Delta_n$ on $H_n(\mathbb{B})$ and its properties, the determinant on the Cartan factor of type 6, the unitaries and their spectral decomposition, the product theorem, the simultaneous reduction to biquaternions, the explicit minimal projections, and the automorphisms of $C_6$.
- J. Hamhalter, O. F. K. Kalenda and A. M. Peralta, "Finite tripotents and finite $\mathrm{JBW}^*$-triples", *Journal of Mathematical Analysis and Applications* **490** (2020) 124217. The source's own companion: finite-rank tripotents, the Cayley–Dickson ladder $(A_n)$, its lemmas, and the extension of the range tripotent to a unitary that the general determinant invokes.
- H. Hanche-Olsen and E. Størmer, *Jordan Operator Algebras* (Pitman, 1984). For the axioms of JB- and JB\*-algebras, the Jordan matrix algebras $H_n(D)$ and their norms, the unitality of finite-dimensional Jordan algebras, and the place of $H_3(\mathbb{O})$ among the exceptional JB\*-algebras.
- M. Cabrera García and Á. Rodríguez Palacios, *Non-associative Normed Algebras*, Vol. 1 (2014) and Vol. 2 (2018), Cambridge University Press. For the JB\*-triple axioms and the ternary product of a JB\*-algebra, the Peirce decomposition, the equivalence of a triple isomorphism with an isometry (Kaup), and the classification of the Cartan factors.
- W. Kaup, "A Riemann mapping theorem for bounded symmetric domains in complex Banach spaces", *Mathematische Zeitschrift* **183** (1983) 503–529, and "On real Cartan factors", *Manuscripta Mathematica* **92** (1997) 191–222. For the theorem that a bijective triple homomorphism is an isometry, and for the frames of a real Cartan factor and the triple automorphisms exchanging them.
- C.-H. Chu, *Jordan Structures in Geometry and Analysis* (Cambridge Tracts in Mathematics 190, 2012). For the triple product of a JB\*-algebra, the Peirce decomposition with its Peirce-2 algebra, and the classification of the JC\*-triples.
- J. D. M. Wright, "Jordan $C^*$-algebras", *Michigan Mathematical Journal* **24** (1977) 291–302, and R. Braun, W. Kaup and H. Upmeier, "A holomorphic characterization of Jordan $C^*$-algebras", *Mathematische Zeitschrift* **161** (1978) 277–290. For the relation between JB\*-algebras and JB-algebras, and for the shift $x\mapsto\{u,x^{*},u\}$ by a unitary element as a triple automorphism.
- T. Barton and R. M. Timoney, "Weak\*-continuity of Jordan triple products and its applications", *Mathematica Scandinavica* **59** (1986) 177–191. For the unique predual of a JBW\*-triple and the separate weak\*-continuity of its triple product.
- G. Horn, "Classification of $\mathrm{JBW}^*$-triples of type I", *Mathematische Zeitschrift* **196** (1987) 271–291. For the representation of a JBW\*-triple from the Cartan factors.
- G. Horn, "Characterization of the predual and ideal structure of a $\mathrm{JBW}^*$-triple", *Mathematica Scandinavica* **61** (1987) 117–133. For the sum of an orthogonal family of tripotents in the weak\*-topology.
- W. Loos, *Bounded Symmetric Domains and Jordan Pairs* (University of California, Irvine, 1977). For the classical theory of the bounded symmetric domains whose Jordan-triple data the Cartan factors are.
- T. A. Springer and F. D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups* (Springer Monographs in Mathematics, 2000). For the complex octonions, the exceptional Jordan algebra $H_3(\mathbb{O}_{\mathbb{C}})$ and its automorphisms.
- L. A. Harris, "Bounded symmetric homogeneous domains in infinite dimensional spaces", in *Proceedings on Infinite Dimensional Holomorphy* (Lecture Notes in Mathematics 364, Springer, 1974), 13–40. For the class of JC\*-triples as the closed subspaces of C\*-algebras stable under $\{x,y,z\} = \tfrac12(xy^*z+zy^*x)$.
