# __Biquaternion Representation Theory__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ was defined in the basic algebra article, with its conjugations, its norm form and its group of units. This article treats its **representation theory** in the technical sense: a representation of an algebra $A$ over a field $k$ is a $k$-vector space $V$ with a unital algebra homomorphism $A \to \operatorname{End}_k(V)$, and a representation of a group $G$ is a vector space with a homomorphism $G \to GL(V)$. The chapter also uses the word in a non-technical sense, for a *concrete realization* of the algebra: the companion articles on biquaternion algebraic representations and on biquaternion polar representations, together with the three articles on the four-vector, matrix and regular realizations of the algebra, written in parallel, use it so. Only the matrix and the regular realizations are representations in the technical sense as well, since only they carry an action; the four-vector realization is the coefficient space alone. The two senses meet at the simple module, which every realization carries, and the theory below is stated for the module, so that it holds independently of the realization chosen.

Every claim below states its ground field ($\mathbb{R}$ or $\mathbb{C}$) and its side (algebra or group). Part I treats the algebra: over $\mathbb{C}$, $\mathbb{B}$ is four-dimensional and isomorphic to $M_2(\mathbb{C})$, hence semisimple and central simple, with a unique simple module of complex dimension $2$; over $\mathbb{R}$ it is eight-dimensional, simple with centre $\mathbb{C}$, again with a unique simple module of complex dimension $2$. Part II treats the group of units $\mathbb{B}^{\times} \cong GL(2,\mathbb{C})$ and its unit-norm subgroup $SL(2,\mathbb{C})$, the double cover of the proper orthochronous Lorentz group: its finite-dimensional polynomial representations, the defining representation and the Weyl spinors, the Clebsch–Gordan rule and tensor powers, and the unitary representations, including the principal series.

# Part I: The Algebra

## 1. The Algebra and Its Two Ground Fields

As a $\mathbb{C}$-algebra, $\mathbb{B}$ has $\mathbb{C}$-basis $\{e_0,e_1,e_2,e_3\}$ and is four-dimensional; as an $\mathbb{R}$-algebra it has $\mathbb{R}$-basis $\{e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3\}$ and is eight-dimensional. The central fact is the isomorphism of $\mathbb{C}$-algebras

$$
\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H} \cong M_2(\mathbb{C}),
$$

which is the structure theorem of a central simple algebra of degree $2$ over its centre: the theorem writes such an algebra as $M_2(D)$ for a division algebra $D$ over the centre, and over the algebraically closed field $\mathbb{C}$ the only such $D$ is $\mathbb{C}$ itself, so the algebra is $M_2(\mathbb{C})$. The isomorphism is not unique, two choices differing by conjugation by an invertible matrix, and nothing below depends on the choice; it is therefore stated here as an isomorphism and not as a matrix. Each concrete realization of the algebra is one way of writing it down, and each has its own companion article: the complex four-vector realization, the $2 \times 2$ matrix realization and the $4 \times 4$ regular realization, all three written in parallel. In the four-vector realization the norm form is read directly from the coefficients; in the other two it is recovered from the operator instead, whose determinant is $N(\tilde{Q})$ on the simple module and $N(\tilde{Q})^2$ on the regular one, and whose trace is the scalar part $Q_0$ multiplied by the dimension of the space it acts on, that is, $2$ on the simple module and $4$ on the regular one. Three consequences are used throughout. The **centre** of $M_2(\mathbb{C})$ is the scalar matrices, so the centre of $\mathbb{B}$ is $\mathbb{C}_{\mathbb{B}} = \mathbb{C}e_0$: one-dimensional over $\mathbb{C}$, and the two-dimensional real space spanned by $e_0$ and $ie_0$ over $\mathbb{R}$. The algebra is **simple**, having no nontrivial two-sided ideals: a nonzero ideal of $M_2(\mathbb{C})$ contains a rank-one matrix, and products of a rank-one matrix with arbitrary matrices generate the whole algebra. Finally it is **central** over $\mathbb{C}$, since its centre is the ground field $\mathbb{C}$, but **not** central over $\mathbb{R}$, where its centre is the quadratic field $\mathbb{C} \neq \mathbb{R}$; it is central simple over its centre $\mathbb{C}$.

## 2. Complex Representations of the Algebra

Over $\mathbb{C}$, a representation is a complex vector space with a unital homomorphism $\mathbb{B} \to \operatorname{End}_{\mathbb{C}}(V)$, that is, a left $\mathbb{B}$-module. Since $\mathbb{B} \cong M_2(\mathbb{C})$, this is the theory of left modules over a full matrix algebra. Let $V$ be a simple left $\mathbb{B}$-module, of complex dimension $2$; in the matrix realization $V$ is the space of column vectors with the natural action, and in the regular realization it appears as a minimal left ideal. The theory below is stated for $V$ and not for any particular realization of it.

**Theorem.** Up to isomorphism, $V$ is the only simple $\mathbb{B}$-module, and $\dim_{\mathbb{C}} V = 2$.

**Proof.** The minimal left ideals of $M_n(\mathbb{C})$ are the spaces of matrices supported in one column, all isomorphic to $\mathbb{C}^n$; for $n = 2$ this is $V$. $\square$

**Theorem.** Every finite-dimensional $\mathbb{B}$-module is a direct sum of copies of $V$,

$$
W \cong V^{\oplus n}, \qquad n = \tfrac{1}{2}\dim_{\mathbb{C}} W.
$$

**Proof.** The algebra $M_2(\mathbb{C})$ is simple Artinian, hence semisimple; a finite-dimensional module over a semisimple algebra is a direct sum of simple modules, each isomorphic to $V$. $\square$

Hence a finite-dimensional complex representation is determined up to isomorphism by its (even) dimension, and no irreducible representation other than $V$ exists. Every such representation is completely reducible, and the category of finite-dimensional $\mathbb{B}$-modules is semisimple with a single simple object. The dual $V^{*}$ is again simple of dimension $2$, so $V^{*} \cong V$, and the Grothendieck group of finite-dimensional modules is $\mathbb{Z}$, generated by $[V]$.

The case $n = 2$ is the **regular representation**: the algebra regarded as a left module over itself by left multiplication is $\mathbb{B} = I_1 \oplus I_2 \cong V \oplus V$, the direct sum of two minimal left ideals. Over $\mathbb{C}$ this is a representation on a four-dimensional space, and the matrix of left multiplication by $\tilde{Q}$ in the basis $e_0, e_1, e_2, e_3$ is $\rho_L(\tilde{Q})$; its entries are the coefficients of $\tilde{Q}$, with signs, and its explicit form is the subject of the companion article on the regular representation, written in parallel. Right multiplication is not a second representation of the algebra but the regular representation of the **opposite** algebra, with matrix $\rho_R(\tilde{Q})$, and the two matrices agree exactly on the centre: this is where left and right first differ, the algebra being non-commutative. The classification above is therefore not confined to the two-dimensional module: the algebra itself is the first reducible case.

A caution: for a non-commutative algebra the tensor product of two left modules is not naturally a left module, so the tensor-product ring structure belongs to the group side (Part II); the classification above uses direct sums only.

## 3. Schur's Lemma, Intertwiners, Automorphisms and Derivations

Let $V$ be the simple module. A $\mathbb{B}$-module homomorphism, or intertwining operator, is a $\mathbb{C}$-linear map $T$ with $T(\tilde{Q}u) = \tilde{Q}T(u)$.

**Schur's lemma.** $\operatorname{End}_{\mathbb{B}}(V) \cong \mathbb{C}$; if $V$ and $V'$ are non-isomorphic simple modules then $\operatorname{Hom}_{\mathbb{B}}(V, V') = 0$.

**Proof.** The kernel and image of a module homomorphism are submodules; a nonzero endomorphism of the simple module $V$ has zero kernel and full image, hence is an isomorphism, and an operator commuting with all of $M_2(\mathbb{C})$ is a scalar matrix. $\square$

For direct sums of the simple module,

$$
\operatorname{Hom}_{\mathbb{B}}\!\left(V^{\oplus m}, V^{\oplus n}\right) \cong M_{n \times m}(\mathbb{C}), \qquad \operatorname{End}_{\mathbb{B}}(V^{\oplus n}) \cong M_n(\mathbb{C}).
$$

The centre of $M_n(\mathbb{C})$ is the scalars, so the centre of $\mathbb{B}$ acts on every representation by scalars. Since $V$ is simple and faithful, the double centraliser theorem gives $\operatorname{End}_{\operatorname{End}_{\mathbb{B}}(V)}(V) = \mathbb{B}$, that is, $\operatorname{End}_{\mathbb{C}}(V) \cong \mathbb{B}$: the algebra is exactly the algebra of all $\mathbb{C}$-linear endomorphisms of its simple module. This is the sense in which the structure of the algebra is reflected in its intertwining operators.

**Automorphisms.** By the Skolem–Noether theorem, every $\mathbb{C}$-algebra automorphism of $\mathbb{B}$ is inner, $\varphi(\tilde{Q}) = T\tilde{Q}T^{-1}$ with $T \in GL_2(\mathbb{C})$ unique up to scalars, so

$$
\operatorname{Aut}_{\mathbb{C}\text{-alg}}(\mathbb{B}) \cong PGL_2(\mathbb{C}) = GL_2(\mathbb{C})/\mathbb{C}^{\times} \cong PSL_2(\mathbb{C});
$$

the scalar ambiguity is exactly Schur's lemma. Over $\mathbb{R}$, complex conjugation of matrix entries is an $\mathbb{R}$-algebra automorphism that is not $\mathbb{C}$-linear, and

$$
\operatorname{Aut}_{\mathbb{R}\text{-alg}}(\mathbb{B}) \cong PGL_2(\mathbb{C}) \rtimes \mathbb{Z}/2.
$$

**Derivations.** Every derivation of a full matrix algebra is inner, $D = \operatorname{ad}_X$ with $\operatorname{ad}_X(Y) = XY - YX$. The map $X \mapsto \operatorname{ad}_X$ has kernel the centre $\mathbb{C}$ and image the traceless matrices, so

$$
\operatorname{Der}_{\mathbb{C}}(\mathbb{B}) \cong \mathfrak{sl}(2,\mathbb{C}), \qquad \dim_{\mathbb{C}} \operatorname{Der}_{\mathbb{C}}(\mathbb{B}) = 3.
$$

Every $\mathbb{R}$-derivation annihilates the centre, because for central $\lambda$ one has $D(\lambda)x = xD(\lambda)$ for all $x$, and $0 = D(-1) = D(i^2) = 2iD(i)$ forces $D(i) = 0$, so the derivation is $\mathbb{C}$-linear; hence $\operatorname{Der}_{\mathbb{R}}(\mathbb{B}) = \operatorname{Der}_{\mathbb{C}}(\mathbb{B}) \cong \mathfrak{sl}(2,\mathbb{C})$ as a real Lie algebra of dimension $6$. All derivations, over $\mathbb{C}$ and over $\mathbb{R}$, are inner.

## 4. Real Representations of the Algebra

Over $\mathbb{R}$, the algebra $\mathbb{B}$ is the eight-dimensional simple real algebra underlying $M_2(\mathbb{C})$, with centre $\mathbb{C}$. It is central simple over $\mathbb{C}$, but not central over $\mathbb{R}$. Let $S = \operatorname{Res}_{\mathbb{C}/\mathbb{R}} V$ be the complex simple module regarded as a real vector space by restriction of scalars; then $\dim_{\mathbb{R}} S = 4$ and $\dim_{\mathbb{C}} S = 2$.

**Theorem.** Up to isomorphism, $S$ is the only simple real $\mathbb{B}$-module, and every finite-dimensional real representation is a direct sum of copies of $S$,

$$
W \cong S^{\oplus n}, \qquad n = \tfrac{1}{4}\dim_{\mathbb{R}} W.
$$

**Proof.** The real algebra $\mathbb{B}_{\mathbb{R}} \cong M_2(\mathbb{C})$ is simple, and its minimal left ideals all have real dimension $4$. A real subspace of $S$ stable under $\mathbb{B}$ is stable in particular under the scalar matrices $zI$, $z \in \mathbb{C}$, hence is a complex subspace; therefore the $\mathbb{B}$-submodules of $S$ are exactly its complex subspaces, and $S$ is simple. Semisimplicity of $\mathbb{B}_{\mathbb{R}}$ gives the direct-sum statement. $\square$

By Schur's lemma, $\operatorname{End}_{\mathbb{B}}(S) = \mathbb{C}$: an $\mathbb{R}$-division algebra containing the algebraically closed field $\mathbb{C} = Z(\mathbb{B})$ and finite-dimensional over it, hence equal to $\mathbb{C}$. Thus $S$ is of **complex type**, neither real nor quaternionic, and this is the precise sense in which the simple module of the real algebra is "two-dimensional complex" while being four-dimensional real. Restriction and extension of scalars relate the two cases, $S$ being the restriction of the complex simple module $V$. The case $n = 2$ of the theorem is the real regular representation, $\mathbb{B} \cong S \oplus S$ of real dimension $8$: the algebra as a left module over itself. This is why the regular representation is $4 \times 4$ over $\mathbb{C}$ and $8 \times 8$ over $\mathbb{R}$, the complex and the real matrix realization of one and the same action.

# Part II: The Group

## 5. The Group of Units and $SL(2,\mathbb{C})$

The group of units is $\mathbb{B}^{\times} = \{\tilde{Q} : N(\tilde{Q}) \neq 0\}$, which under $\mathbb{B} \cong M_2(\mathbb{C})$ is the group of invertible matrices, because the norm form is the determinant:

$$
\mathbb{B}^{\times} \cong GL_2(\mathbb{C}),
$$

a connected non-compact complex Lie group of complex dimension $4$, real dimension $8$, with centre $\mathbb{C}^{\times}$. The unit-norm subgroup is

$$
SL(2,\mathbb{C}) = \{\tilde{Q} : N(\tilde{Q}) = 1\} \cong \{g \in GL_2(\mathbb{C}) : \det g = 1\},
$$

a simply connected complex Lie group of complex dimension $3$, real dimension $6$. The map

$$
SL(2,\mathbb{C}) \longrightarrow SO^{+}(1,3), \qquad \tilde{Q} \longmapsto \left(\tilde{X} \mapsto \tilde{Q}\tilde{X}\tilde{Q}^{\dagger}\right),
$$

is surjective with kernel $\{\pm e_0\}$, so $SL(2,\mathbb{C})$ is the double cover of the proper orthochronous Lorentz group. Since $-e_0$ acts as $-\mathrm{id}$ on $V$, the defining two-dimensional representation does not descend to $SO^{+}(1,3)$. The unitary biquaternions $\tilde{Q}^{\dagger}\tilde{Q} = 1$ form $U(2)$, the maximal compact subgroup of $\mathbb{B}^{\times}$, and the unit quaternions form $SU(2) = SL(2,\mathbb{C}) \cap U(2)$, the maximal compact subgroup of $SL(2,\mathbb{C})$ and the double cover of $SO(3)$.

**Representations of the unit group.** As a reductive group, $GL_2(\mathbb{C})$ has finite-dimensional algebraic (rational) representations parameterised by highest weights $(\lambda_1, \lambda_2) \in \mathbb{Z}^2$ with $\lambda_1 \geq \lambda_2$; the irreducible one is $\operatorname{Sym}^{\lambda_1 - \lambda_2}(\mathbb{C}^2) \otimes (\det)^{\lambda_2}$, of dimension $\lambda_1 - \lambda_2 + 1$, with central character $z \mapsto z^{\lambda_1 + \lambda_2}$. Restriction to $SL(2,\mathbb{C})$ forgets the determinant twist, leaving the highest weight $2j = \lambda_1 - \lambda_2 \geq 0$, that is, the irreducible $V_j$ of the next section with spin $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$.

## 6. Finite-Dimensional Representations of $SL(2,\mathbb{C})$

Let $G = SL(2,\mathbb{C})$ and let $\mathfrak{g} = \mathfrak{sl}(2,\mathbb{C})$ be its Lie algebra, regarded as a real Lie algebra. Its complexification is a sum of two copies of $\mathfrak{sl}(2,\mathbb{C})$, the complexified Lorentz algebra:

$$
\mathfrak{so}(1,3)\otimes_{\mathbb{R}}\mathbb{C} \cong \mathfrak{sl}(2,\mathbb{C}) \oplus \mathfrak{sl}(2,\mathbb{C}),
$$

the two summands corresponding to the self-dual and anti-self-dual parts.

Every finite-dimensional smooth complex representation of $G$ is completely reducible, and its irreducible summands are the outer tensor products $(m,n) = V_m \boxtimes V_n$ with $m, n \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$, where $V_j$ denotes the irreducible $\mathfrak{su}(2)$-module of dimension $2j+1$, equivalently the $\mathfrak{sl}(2,\mathbb{C})$-module $\operatorname{Sym}^{2j}(\mathbb{C}^2)$ of highest weight $2j$; thus $\dim_{\mathbb{C}}(m,n) = (2m+1)(2n+1)$. The defining representation is $(\tfrac{1}{2}, 0)$ and its complex conjugate is $(0, \tfrac{1}{2})$.

**Polynomial representations.** Relative to a Cartan subalgebra spanned by $h = \operatorname{diag}(1,-1)$, the irreducible $\mathfrak{sl}(2,\mathbb{C})$-modules are the symmetric powers $V_j \cong \operatorname{Sym}^{2j}(\mathbb{C}^2)$, with spin $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$, highest weight $2j$ and dimension $2j+1$. These are exactly the **polynomial** (equivalently holomorphic, equivalently algebraic) finite-dimensional representations of the complex group $G$: their matrix entries are polynomial functions of the entries of $g \in G$, and every finite-dimensional holomorphic representation of $G$ is a direct sum of the $V_j$, hence is parameterised by its highest weight $2j$, that is, by its spin $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$. Not every continuous finite-dimensional representation is polynomial: the complex conjugates of the $V_j$ are antiholomorphic and belong to the $(0, j)$ family.

**The unitary trick.** Restriction to the maximal compact subgroup $SU(2)$ is an equivalence of categories

$$
\left\{\text{f.d. polynomial representations of } SL(2,\mathbb{C})\right\} \simeq \left\{\text{f.d. unitary representations of } SU(2)\right\},
$$

so the finite-dimensional polynomial representations of $SL(2,\mathbb{C})$ are obtained from those of $SU(2)$ by complexifying the Lie algebra and exponentiating, and both are parameterised by the same highest weights $2j$, $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$. What complexification does not preserve is unitarity, a point taken up in Section 9.

## 7. The Defining Representation and the Weyl Spinors

The defining representation of $SL(2,\mathbb{C})$ is $V_{1/2} = \mathbb{C}^2$, the polynomial representation of highest weight $1$. It is the same space that appears in Part I as the unique simple module of the algebra $\mathbb{B}$, and the isomorphism $\mathbb{B} \cong \operatorname{End}_{\mathbb{C}}(V_{1/2})$ is the content of the matrix realization: choosing a basis of $V_{1/2}$ writes each element of the algebra as a $2 \times 2$ matrix, and the choice of basis is the only freedom in doing so. Under the Lorentz group the defining representation and its conjugate are the two **Weyl spinors**: $V_{1/2} = (\tfrac{1}{2}, 0)$ is the left-handed one and $\overline{V_{1/2}} = (0, \tfrac{1}{2})$ is the right-handed one; they are not isomorphic as complex representations, and parity exchanges them. Their direct sum is the **Dirac spinor**

$$
\Delta = V_{1/2} \oplus \overline{V_{1/2}} = (\tfrac{1}{2},0) \oplus (0,\tfrac{1}{2}), \qquad \dim_{\mathbb{C}} \Delta = 4,
$$

and their tensor product is the **vector representation** $(\tfrac{1}{2}, \tfrac{1}{2}) = V_{1/2} \otimes \overline{V_{1/2}}$, of complex dimension $4$, whose real form is the Lorentz action on the four-dimensional vector space. The adjoint representation of the Lorentz algebra is $(1,0) \oplus (0,1)$, of dimension $3 + 3$.

Two dualities must be distinguished. The defining module is **self-dual** as a representation of $SL(2,\mathbb{C})$: since $\det = 1$, the alternating form $\varepsilon(u,v) = u_1 v_2 - u_2 v_1$ is invariant and identifies $V_{1/2}^{*}$ with $V_{1/2}$, so $V_{1/2}^{*} \cong V_{1/2}$. The **conjugate** $\overline{V_{1/2}}$, by contrast, is not isomorphic to $V_{1/2}$; it is the other chirality. Finally, $-e_0$ acts as $-1$ on $V_{1/2}$, so the defining representation, and every $(m,n)$ with $m+n$ half-integral, is a genuine spin representation that does not descend to $SO^{+}(1,3)$.

## 8. Tensor Products and the Clebsch–Gordan Rule

Group representations tensor with the diagonal action $g \cdot (v \otimes w) = (gv) \otimes (gw)$. For the polynomial representations of $SL(2,\mathbb{C})$ the Clebsch–Gordan rule is

$$
V_j \otimes V_k \cong \bigoplus_{l=|j-k|}^{j+k} V_l, \qquad j, k \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}.
$$

The tensor square of the spinor is the simplest nontrivial case:

$$
V_{1/2} \otimes V_{1/2} \cong \operatorname{Sym}^2 V_{1/2} \oplus \Lambda^2 V_{1/2} \cong V_1 \oplus V_0, \qquad \dim_{\mathbb{C}} V_1 = 3, \quad \dim_{\mathbb{C}} V_0 = 1.
$$

The summand $V_1$ is the **traceless symmetric part** and is the adjoint representation of $\mathfrak{sl}(2,\mathbb{C})$, that is, the complexification of the adjoint representation of the compact algebra $\mathfrak{su}(2) \cong \mathfrak{so}(3)$; concretely, $\operatorname{Sym}^2 V_{1/2}$ is the space of symmetric $2 \times 2$ matrices and $V_1$ the traceless subspace. The summand $V_0 = \Lambda^2 V_{1/2} \cong \mathbb{C}$ is the **scalar**, spanned by the invariant alternating form $\varepsilon$. Thus the tensor square of the spinor splits as the complexified adjoint representation plus a scalar. This is the three-dimensional rotation algebra; the adjoint representation of the six-dimensional Lorentz algebra is instead $(1,0) \oplus (0,1)$.

For the two-parameter family the rule applies to each factor:

$$
(m,n) \otimes (m',n') \cong \bigoplus_{k=0}^{\min(m,m')} \bigoplus_{k'=0}^{\min(n,n')} (m+m'-2k,\ n+n'-2k').
$$

For example, $(\tfrac{1}{2},\tfrac{1}{2}) \otimes (\tfrac{1}{2},\tfrac{1}{2}) \cong (0,0) \oplus (1,0) \oplus (0,1) \oplus (1,1)$, of dimension $1 + 3 + 3 + 9 = 16 = 4 \times 4$.

**Tensor powers of the defining representation.** Iterating the rule gives the complete decomposition of the $N$-fold tensor power of the spinor,

$$
V_{1/2}^{\otimes N} \cong \bigoplus_{k=0}^{\lfloor N/2 \rfloor} \left[ \binom{N}{k} - \binom{N}{k-1} \right] V_{N/2-k}, \qquad \binom{N}{-1} = 0,
$$

the multiplicity of $V_{N/2-k}$ being the ballot (Catalan-triangle) number $\binom{N}{k} - \binom{N}{k-1}$. For example $V_{1/2}^{\otimes 2} \cong V_1 \oplus V_0$ and $V_{1/2}^{\otimes 3} \cong V_{3/2} \oplus 2V_{1/2}$. Since every finite-dimensional polynomial representation is completely reducible, the **composition factors** of a tensor power are exactly its direct summands, with these multiplicities.

## 9. Unitary Representations

A representation $\rho$ on $W$ is **unitary** if $W$ carries an invariant positive-definite Hermitian form $\langle \cdot, \cdot \rangle$. On $V_{1/2} = \mathbb{C}^2$ the standard form $\langle u,v \rangle = u_1^{*}v_1 + u_2^{*}v_2$ is invariant under $SU(2)$, so $V_{1/2}$ is unitary for the compact form $SU(2)$. It is **not** unitary for $SL(2,\mathbb{C})$: the non-compact one-parameter subgroups of hyperbolic rotations do not preserve it. More generally a non-compact simple Lie group has no nontrivial finite-dimensional unitary representation, since the image would lie in a compact group; hence only the trivial representation is finite-dimensional and unitary for $SL(2,\mathbb{C})$, and the defining representation is not unitarisable for the complex group. Unitarity of the compact form $SU(2)$, not of $SL(2,\mathbb{C})$, is what complexification preserves.

**The principal series.** The infinite-dimensional unitary representations are built by induction. Let $P$ be the Borel subgroup of upper triangular matrices, with $P = MAN$,

$$
M = \{\operatorname{diag}(u,u^{-1}) : |u| = 1\} \cong U(1), \qquad A = \{\operatorname{diag}(e^{t/2}, e^{-t/2}) : t \in \mathbb{R}\},
$$

and $N$ the upper unitriangular matrices. For $m \in \mathbb{Z}$ and $\nu \in \mathbb{R}$ define a unitary character of $P$ by $\chi_{m,\nu}(man) = u^{m} e^{i\nu t}$; the **principal series** representation is the unitarily induced representation

$$
\pi_{m,\nu} = \operatorname{Ind}_{P}^{G}(\chi_{m,\nu}),
$$

realised on $L^2(G/P) = L^2(S^2)$, where $G/P \cong SU(2)/U(1) \cong S^2$. Each $\pi_{m,\nu}$ is unitary by construction; it is irreducible for generic parameters, and for $\nu \in \mathbb{R}$ it is tempered. The parameter $m$ is discrete and $\nu$ is continuous. The principal series is not the whole unitary dual: there are also the **complementary series**, for which the continuous parameter is purely imaginary and bounded rather than real, and the trivial representation. The finite-dimensional polynomial representations are not unitary for $SL(2,\mathbb{C})$, except for the trivial representation $V_0$; only their restrictions to $SU(2)$ are unitary.

**Complexification of the unitary dual.** The unitary dual of the maximal compact subgroup $SU(2)$ is discrete, the family $\{V_j\}_{j \in \frac{1}{2}\mathbb{Z}_{\geq 0}}$. Passing to the complexification $SL(2,\mathbb{C})$ replaces the discrete highest-weight parameter by a continuous complex parameter; the representations that remain unitary form the principal series, with parameter on the unitary axis, together with the complementary series on a bounded interval of the imaginary axis. In this sense the unitary dual of $SL(2,\mathbb{C})$ is the complexification of the unitary dual of $SU(2)$. The polynomial representations correspond to the dominant integral highest weights, the discrete points that were unitary for $SU(2)$; under complexification those points cease to be unitary except for the trivial representation.

## Summary

Every statement in this article carries its ground field and its side. On the algebra side, $\mathbb{B}$ over $\mathbb{C}$ is four-dimensional and isomorphic to $M_2(\mathbb{C})$, hence semisimple and central simple, with a unique simple module $V$ up to isomorphism, of complex dimension $2$; by Schur's lemma its intertwining algebra is $\operatorname{End}_{\mathbb{B}}(V) \cong \mathbb{C}$, and $\mathbb{B} \cong \operatorname{End}_{\mathbb{C}}(V)$: the algebra is the full endomorphism algebra of its simple module, a statement about the algebra rather than about any one realization of it. The several realizations treated in the companion articles — the complex four-vector, the $2 \times 2$ matrix and the $4 \times 4$ regular — are the several ways of writing this one algebra down, and the regular case is the reducible module $V \oplus V$. Over $\mathbb{R}$ the same set is an eight-dimensional simple algebra with centre $\mathbb{C}$, again with a unique simple module, of complex dimension $2$. Both representation theories are therefore the module theory of a full matrix algebra, and they agree on the simple module.

On the group side, the group of units is $\mathbb{B}^{\times} \cong GL(2,\mathbb{C})$, and the unit-norm subgroup is $SL(2,\mathbb{C})$, the double cover of the proper orthochronous Lorentz group $SO^{+}(1,3)$. Its finite-dimensional polynomial representations are parameterised by the highest weight $2j$, $j \in \tfrac{1}{2}\mathbb{Z}_{\geq 0}$, and coincide with the finite-dimensional unitary representations of $SU(2)$ after complexification of the Lie algebra. The defining representation $V_{1/2} = \mathbb{C}^2$ is the simple module of the algebra; it and its conjugate are the two Weyl spinors $(\tfrac{1}{2},0)$ and $(0,\tfrac{1}{2})$, whose direct sum is the Dirac spinor and whose tensor product is the four-dimensional vector representation $(\tfrac{1}{2},\tfrac{1}{2})$. Tensor products obey the Clebsch–Gordan rule, with the two-parameter rule for the Lorentz irreps $(m,n)$; the adjoint representation of the Lorentz algebra is $(1,0) \oplus (0,1)$.

Unitarity is the one property that complexification does not preserve. The defining representation is unitary for the compact form $SU(2)$ but not for $SL(2,\mathbb{C})$, and the only finite-dimensional unitary representation of $SL(2,\mathbb{C})$ is the trivial one. The infinite-dimensional unitary representations are the principal series, induced from unitary characters $\chi_{m,\nu}$ of the Borel subgroup $P = MAN$ and realised on $L^2(G/P) = L^2(S^2)$, together with the complementary series and the trivial representation; the continuous parameter of the principal series is the complexification of the discrete highest-weight parameter of $SU(2)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $V$ | Unique simple complex $\mathbb{B}$-module, $\dim_{\mathbb{C}} V = 2$, isomorphic to $\mathbb{C}^2$ |
| $S = \operatorname{Res}_{\mathbb{C}/\mathbb{R}} V$ | Unique simple real $\mathbb{B}$-module, $\dim_{\mathbb{R}} S = 4$, of complex type |
| $I_1, I_2$ | The two minimal left ideals, $\mathbb{B} = I_1 \oplus I_2 \cong V \oplus V$ |
| $\rho_L, \rho_R$ | Matrices of left and right multiplication in the basis $e_0, e_1, e_2, e_3$ |
| $\mathbb{B}^{\times} \cong GL_2(\mathbb{C})$ | Group of units |
| $SL(2,\mathbb{C})$ | Unit-norm subgroup, double cover of $SO^{+}(1,3)$ |
| $SU(2)$ | Maximal compact subgroup |
| $V_j$ | Irreducible representation of spin $j$, highest weight $2j$, dimension $2j+1$ |
| $(m,n)$ | Irreducible representation of the complexified Lorentz algebra |
| $\operatorname{End}_{\mathbb{B}}(V) \cong \mathbb{C}$ | Intertwining operators, by Schur's lemma |
| $\operatorname{Der}(\mathbb{B}) \cong \mathfrak{sl}(2,\mathbb{C})$ | Inner derivations |

## Further Reading

- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the representation theory of $\mathfrak{sl}(2,\mathbb{C})$, highest weights, Clebsch–Gordan decompositions, and the spin representations.
- Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples* (Princeton University Press, 1986), for the principal series, the complementary series, and the unitary dual of $SL(2,\mathbb{C})$.
- Hermann Weyl, *The Classical Groups: Their Invariants and Representations* (Princeton University Press, 1946), for the unitary trick relating representations of a compact group and its complexification.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the structure theory of semisimple algebras and the classification of simple modules over matrix algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for Schur's lemma, semisimple rings, and the double centraliser theorem.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Interscience, 1962), for the regular representation of an algebra, the opposite algebra, and the relation between the left and right regular matrices.
