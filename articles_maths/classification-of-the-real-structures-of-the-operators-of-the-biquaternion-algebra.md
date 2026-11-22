# __Classification of the Real Structures of the Operators of the Biquaternion Algebra, including Lie Algebras and Lie Groups__

## Introduction and Scope

The companion article [Classification of the Structures of the Operators of the Biquaternion Algebra](classification-of-the-structures-of-the-operators-of-the-biquaternion-algebra.html) proved that the complex operator algebra $\mathcal{E}_{\mathbb{C}}=\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$ has exactly two real forms, the split algebra $M_4(\mathbb{R})$ and the quaternionic algebra $M_2(\mathbb{H})$, that the two are separated by the trace-form inertias $(10,6)$ and $(6,10)$, and that the biquaternion base $L(\mathbb{B})$, $R(\mathbb{B})$ sits inside $\mathcal{E}_{\mathbb{C}}$ with a nine-dimensional complement $\mathfrak{m}$. It stopped at the classification of the forms. This article takes the two forms and develops each of them in the three layers that a real algebra carries at once: the associative product, the commutator bracket and the symmetrized product. It adds the fourth layer, the Lie groups attached to the Lie subalgebras.

The element-level sibling [Classification of the Real Structures of the Biquaternion Algebra, including Lie Algebras and Lie Groups](classification-of-the-real-structures-of-the-biquaternion-algebra.html) did the same for the two real forms $M_2(\mathbb{R})$ and $\mathbb{H}$ of $\mathbb{B}$. The present article is its operator-level analogue, and it differs from it in one structural respect that governs every section: the ambient algebra is four times larger, and its subalgebra lattice is not classified in exhaustive form. A complete classification of the unital subalgebras of $M_4(\mathbb{R})$ does not exist in any usable form, and an attempt in the style of the element-level article would produce a list of hundreds of entries, with continuous parameters and with no organising idea.

**The three-tier strategy.** The article therefore classifies by principle, not by case list, and it says which tier it is using in each layer. The three tiers are these.

1. **A structural theorem per layer.** The associative layer is governed by the module structure of the carrier: a unital subalgebra of $\operatorname{End}(V)$ is a faithful module structure on $V$, and the classification of the semisimple types reduces to a dimension count over the Frobenius division algebras. The Lie layer is governed by the classification of the maximal subalgebras of a simple Lie algebra, which is Dynkin's theorem, in the form refined by Borel–de Siebenthal and by Satake. The Jordan layer is governed by the same module principle applied to the symmetrized product.
2. **Master tables of the distinguished subalgebras.** Each layer is presented with a table that lists the subalgebras that matter: those arising from the biquaternion base, those that are maximal in their class, and those that are parabolic or Levi. Each entry carries its isomorphism type, its real dimension, a witness, and the cross-reference to the layer above or below.
3. **Honest incompleteness.** The article states where a lattice is not classified, and it names what is missing. The claim is never that a table is complete when the table is a list of distinguished members.

**Scope.** This article owns the three operator layers for the two real forms, and the group layer for the distinguished Lie subalgebras. It recaps the two real forms and the biquaternion base from the umbrella article and does not re-prove them. It cites [Classification of the Real Structures of the Biquaternion Algebra](classification-of-the-real-structures-of-the-biquaternion-algebra.html) for the element-level computations, [Real Forms and the Descent of an Algebra](real-forms-and-the-descent-of-an-algebra.html) for the general theory of descent, and [The Lie Correspondence and the Adjoint Representation](the-lie-correspondence-and-the-adjoint-representation.html) for covers and central quotients. It does not treat the complexification of the operator algebra, which is the subject of [Classification of the Complex Structures of the Operators of the Biquaternion Algebra](classification-of-the-complex-structures-of-the-operators-of-the-biquaternion-algebra.html). Operator calculus, spectral theory and representation theory belong to a separate series, and the applications belong to the application articles.

**The order of the argument.** The second section recaps the two real forms with their invariants. The third section fixes the biquaternion base inside the operator algebra and states which parts of it survive in each real form. The fourth and fifth sections treat the associative subalgebras of the split and of the quaternionic form. The sixth and seventh treat the Lie subalgebras of the two. The eighth treats the Jordan layer. The ninth states the exact relation between the element level and the operator level, which is the conceptual centre of the article. The tenth gives the Lie groups. The eleventh compares the two levels, the twelfth states what the operator form does and does not determine, and the thirteenth hands off.

## The Two Real Forms

**The algebra and its forms.** The complex operator algebra is

$$
\mathcal{E}_{\mathbb{C}}=\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C}),
$$

of complex dimension sixteen and real dimension thirty-two. It has exactly two real forms up to isomorphism, and the article writes them

$$
M_4(\mathbb{R})\quad\text{(split)},\qquad M_2(\mathbb{H})\quad\text{(quaternionic)}.
$$

Both have real dimension sixteen. Both are central simple over $\mathbb{R}$, with centre $\mathbb{R}\mathrm{I}$ and no two-sided ideal other than $0$ and the whole algebra. The proof of the classification, the two real structures

$$
\tau_{\mathbb{R}}(X)=\bar X,\qquad
\tau_{\mathbb{H}}(X)=J_0\bar XJ_0^{-1},
$$

with $J_0$ the block skew matrix of size four, and the computation of the two fixed sets are in [Classification of the Structures of the Operators of the Biquaternion Algebra](classification-of-the-structures-of-the-operators-of-the-biquaternion-algebra.html). They are used here and not repeated.

| form | $\dim_{\mathbb{R}}$ | centre | trace-form inertia | simple part | Lie algebra |
|---|---|---|---|---|---|
| $M_4(\mathbb{R})$ | $16$ | $\mathbb{R}\mathrm{I}_4$ | $(10,6)$ | $\mathfrak{sl}(4,\mathbb{R})$ | $\mathfrak{gl}(4,\mathbb{R})$ |
| $M_2(\mathbb{H})$ | $16$ | $\mathbb{R}\mathrm{I}_2$ | $(6,10)$ | $\mathfrak{sl}(2,\mathbb{H})=\mathfrak{su}^{*}(4)$ | $\mathfrak{gl}(2,\mathbb{H})$ |

**The word quaternionic, and why not compact.** The element-level pair of forms is called compact and split, because the compact member $\mathbb{H}$ is a division algebra and the group $SU(2)$ attached to its scalar-free part is compact. At the operator level the pair of words does not transfer. The compact real form of the Lie algebra $\mathfrak{gl}(4,\mathbb{C})$ is $\mathfrak{u}(4)$, and $\mathfrak{u}(4)$ is the Lie algebra of no real form of the associative algebra $M_4(\mathbb{C})$: a real form of an algebra is closed under products, and the product of two skew-Hermitian matrices is skew-Hermitian only when the two commute. The two real forms of the algebra therefore carry the split and the *quaternionic* simple part, $\mathfrak{sl}(4,\mathbb{R})$ and $\mathfrak{sl}(2,\mathbb{H})$, and the second of these is non-compact: its maximal compact subalgebra has dimension ten out of fifteen. The article writes **split** and **quaternionic** throughout, and never writes compact for $M_2(\mathbb{H})$.

The two forms are distinguished by an invariant of the algebra and not of a frame: a symmetric bilinear form built from the trace. On $M_4(\mathbb{R})$ it is $(X,Y)\mapsto\operatorname{tr}(XY)$, of inertia $(10,6)$, from ten symmetric and six skew directions. On $M_2(\mathbb{H})$ the trace is quaternion-valued, so the real form is $(X,Y)\mapsto\operatorname{Re}\operatorname{tr}(XY)$, equivalently $(X,Y)\mapsto\operatorname{tr}(X^{*}Y)$; the two differ by a positive factor, so they have the same inertia, and it is $(6,10)$, from the six-dimensional Hermitian and the ten-dimensional skew-Hermitian parts under the quaternionic conjugation. The inertia is basis-free because the trace is.

**What is not repeated.** The theorem that these are all the real forms, the theorem that the two real structures are not conjugate, the double centralizer theorem, the identification of the two-sided span and the trace-form computation are in the umbrella article. This article cites them where it uses them, and adds nothing to their proofs.

## The Biquaternion Base Inside the Operator Algebra

**The two regular families.** For an element $\tilde Q\in\mathbb{B}$ the article writes $L_{\tilde Q}$ and $R_{\tilde Q}$ for the operators

$$
L_{\tilde Q}(\tilde X)=\tilde Q\tilde X,\qquad R_{\tilde Q}(\tilde X)=\tilde X\tilde Q,
$$

and $T_{\tilde Q,\tilde P}(\tilde X)=\tilde Q\tilde X\tilde P$ for the two-sided operator. The two families are injections of $\mathbb{B}$ into $\mathcal{E}_{\mathbb{C}}$, each with image a copy of $\mathbb{B}$, and the double centralizer theorem states that each image is the centralizer of the other. Their common centralizer is the line $\mathbb{C}\mathrm{I}_4$. The sum $L(\mathbb{B})+R(\mathbb{B})$ is not direct: the two images meet in that line, so the sum has complex dimension $4+4-1=7$, not eight. The complement decomposes as

$$
\mathcal{E}_{\mathbb{C}}=(L(\mathbb{B})+R(\mathbb{B}))\oplus\mathfrak{m},\qquad \dim_{\mathbb{C}}\mathfrak{m}=9,
$$

the space $\mathfrak{m}$ being the two-sided operators whose two parameters are both traceless. It is neither an associative nor a Lie subalgebra. The witness for the first failure is $(T_{\vec e_x,\vec e_x})^{2}=T_{\vec e_x^{2},\vec e_x^{2}}=\mathrm{I}_4$, which uses $\vec e_x^{2}=-e_t$; the witness for the second is that the bracket of two elements of $\mathfrak{m}$ lands in $L(\mathbb{B})+R(\mathbb{B})$. What does hold is that $\mathfrak{m}$ is stable under the scalar-free parts of the two regular families: $[L_{\tilde Q},\mathfrak{m}]\subset\mathfrak{m}$ and $[R_{\tilde P},\mathfrak{m}]\subset\mathfrak{m}$ for traceless $\tilde Q,\tilde P$, so that $\mathfrak{m}$ is a module over $L(\mathfrak{sl}_2)\oplus R(\mathfrak{sl}_2)$.

**The six subspaces and their images.** The element algebra carries six distinguished real subspaces: the centre $\mathbb{B}_C$, the pure part $\mathbb{B}_V$, and the fixed and anti-fixed spaces $\mathbb{B}_H$, $\mathbb{B}_{iH}$, $\mathbb{B}_{\Psi}$, $\mathbb{B}_{\Phi}$ of the three involutions. Their definitions are in [Classification of the Structures of the Biquaternion Algebra](classification-of-the-structures-of-the-biquaternion-algebra.html), and the article recalls only the two that name a layer: $\mathbb{B}_{\Phi}$ is the compact Lie algebra $\mathfrak{u}(2)$, and $\mathbb{B}_{\Psi}$ is the Hermitian space, closed under the symmetrized product.

The images under $L$ are complex subspaces of $\mathcal{E}_{\mathbb{C}}$ of the same real dimensions as the subspaces, and their statuses are the following.

| subspace | $\dim_{\mathbb{R}}$ | $L(B_j)$ | $R(B_j)$ |
|---|---|---|---|
| $\mathbb{B}_C$ | $2$ | subalgebra, $\mathbb{C}\mathrm{I}_4$ | subalgebra, $\mathbb{C}\mathrm{I}_4$ |
| $\mathbb{B}_V$ | $6$ | Lie subalgebra | Lie subalgebra |
| $\mathbb{B}_H$ | $4$ | subalgebra | subalgebra, opposite |
| $\mathbb{B}_{iH}$ | $4$ | neither | neither |
| $\mathbb{B}_{\Psi}$ | $4$ | neither | neither |
| $\mathbb{B}_{\Phi}$ | $4$ | Lie subalgebra | Lie subalgebra |

Two rows are subalgebras and two are Lie subalgebras only, and the four negative entries have explicit witnesses, computed in the umbrella article. $L(\mathbb{B}_V)$ is not closed under the product because $L_{\vec e_x}^{2}=-\mathrm{I}_4$ leaves the image. $L(\mathbb{B}_{\Phi})$ is not closed under the product for the same reason. $L(\mathbb{B}_{iH})$ and $L(\mathbb{B}_{\Psi})$ are not closed under the bracket: $[i\vec e_x,i\vec e_y]=-2\vec e_z$, and $\vec e_z$ lies in neither space.

**The base is complex, and what lives in a real form is $L(B_j\cap A_0)$.** This point governs every table below. The images $L(B_j)$ are *complex* subspaces of $\mathcal{E}_{\mathbb{C}}$. They are therefore subspaces of neither real form, since $M_4(\mathbb{R})$ contains no complex subspace of positive dimension: an element $X$ and its multiple $iX$ cannot both be real. What lives in a real form is the space of real points $L(B_j\cap A_0)$, and not $L(B_j)$ itself, for $A_0$ one of the two real forms of $\mathbb{B}$. For the split form $A_0=M_2(\mathbb{R})$ the intersections are known from the element-level article, and they give the following table, whose last column records the operator-level algebra.

| subspace | $B_j\cap M_2(\mathbb{R})$ | $\dim_{\mathbb{R}}$ | in matrices | $L(B_j\cap M_2(\mathbb{R}))$ |
|---|---|---|---|---|
| $\mathbb{B}_C$ | $\mathbb{R}e_t$ | $1$ | $\mathbb{R}\mathrm{I}$ | $\mathbb{R}\mathrm{I}_4$ |
| $\mathbb{B}_V$ | $\operatorname{span}\{\vec e_y,i\vec e_x,i\vec e_z\}$ | $3$ | scalar-free | $L(\mathfrak{sl}(2,\mathbb{R}))$ |
| $\mathbb{B}_H$ | $\operatorname{span}\{e_t,\vec e_y\}$ | $2$ | $\mathbb{R}\mathrm{I}\oplus\mathbb{R}J$ | $L(\mathbb{C})$ |
| $\mathbb{B}_{iH}$ | $\operatorname{span}\{i\vec e_x,i\vec e_z\}$ | $2$ | $\operatorname{span}\{\sigma_1,\sigma_3\}$ | $L(\mathbb{R}^2)$ |
| $\mathbb{B}_{\Psi}$ | $\operatorname{span}\{e_t,i\vec e_x,i\vec e_z\}$ | $3$ | symmetric | $L(\text{symmetric})$ |
| $\mathbb{B}_{\Phi}$ | $\operatorname{span}\{\vec e_y\}$ | $1$ | antisymmetric | $L(\mathbb{R}\vec e_y)$ |

The same computation for the quaternionic form $A_0=\mathbb{H}$ gives the intersections $\mathbb{R}e_t$, $\mathbb{B}_V$, $\mathbb{H}$, $0$, $\mathbb{R}e_t$ and $\mathbb{B}_V$ in the six rows, of real dimensions $1,3,4,0,1,3$.

The two tables carry one consequence that is used twice below. The scalar-free part of the base has real dimension three in either real form, and it is the compact algebra $\mathfrak{su}(2)$ in the quaternionic form and the split algebra $\mathfrak{sl}(2,\mathbb{R})$ in the split form. The complex space $\mathbb{B}_V$, of real dimension six, read as a real Lie algebra, is a third real form of the same complex algebra $\mathfrak{so}(3,\mathbb{C})$, namely $\mathfrak{so}(3,1)$. So the biquaternion base produces all three real forms of $\mathfrak{so}(3,\mathbb{C})$: two as fixed sets and one as the complex object itself.

**The two-sided span.** For a real form $A_0$ of $\mathbb{B}$ the two-sided span is

$$
\mathcal{E}(A_0)=\operatorname{span}_{\mathbb{R}}\{T_{\tilde Q,\tilde P}:\tilde Q,\tilde P\in A_0\},
$$

and the umbrella article proved that it is a real subalgebra of $\mathcal{E}_{\mathbb{C}}$ of real dimension sixteen. Since the only real subalgebras of that dimension are the two real forms, and since $\mathcal{E}(A_0)$ contains $L_{\tilde Q}=T_{\tilde Q,e_t}$, it is one of the two forms. The theorem of the ninth section identifies it: for both $A_0=M_2(\mathbb{R})$ and $A_0=\mathbb{H}$ the two-sided span is the split form $M_4(\mathbb{R})$, by the algebra isomorphism $A_0\otimes_{\mathbb{R}}A_0^{\mathrm{op}}\cong M_4(\mathbb{R})$.

**The right-$\mathbb{H}$-linear maps.** The other real form is reached by a different construction. Put

$$
\mathcal{E}_{\mathbb{H}}=\{F\in\mathcal{E}_{\mathbb{R}}:F(\tilde X\tilde Q)=F(\tilde X)\tilde Q\ \text{for all }\tilde Q\in\mathbb{H}\},
$$

the operators commuting with the right action of the quaternions. This is a real subalgebra of $\mathcal{E}_{\mathbb{R}}$ of real dimension sixteen, isomorphic to $M_2(\mathbb{H})$, and its intersection with $\mathcal{E}_{\mathbb{C}}$ is $L(\mathbb{B})$. The identification is not a convenience. $\mathbb{B}$ is a right $\mathbb{H}$-module of rank two, and $\mathcal{E}_{\mathbb{H}}$ is its endomorphism ring as a module. The quaternionic form is the endomorphism ring of a module; the split form is a tensor square.

**Warning (the element level does not determine the operator level).** Both element-level real forms, $M_2(\mathbb{R})$ and $\mathbb{H}$, generate the *same* operator-level real form $M_4(\mathbb{R})$ by the two-sided action. The passage from the element form to the operator form is therefore not injective, and the two element forms cannot be recovered from their common image. The other operator form, $M_2(\mathbb{H})$, is not the two-sided span of any element form at all. It is selected by the module structure, that is by right-$\mathbb{H}$-linearity, and that datum is not a subalgebra of $\mathbb{B}$ but a module structure on $\mathbb{B}$.

**Warning (the biquaternion base lives in one form only).** The base $L(\mathbb{B})$, $R(\mathbb{B})$ and the complex images $L(B_j)$ are complex subspaces of $\mathcal{E}_{\mathbb{C}}$, and their real points lie in the split form $M_4(\mathbb{R})$ for either choice of element form. Nothing comparable happens in the quaternionic form. Inside $M_2(\mathbb{H})$ there is a copy of $\mathbb{H}$, the scalars, and a copy of $\mathbb{C}$, its centre; there is no copy of $M_4(\mathbb{R})$, because the two algebras have the same real dimension and are not isomorphic, an embedding of algebras of equal finite dimension being an isomorphism. The asymmetry of the two forms is the asymmetry of their constructions, and it is not a defect of the exposition.

## Associative Subalgebras of the Split Form

**The principle.** The associative layer of $M_4(\mathbb{R})$ is governed by one dictionary, and the dictionary is the reason the layer can be described at all. A unital subalgebra $A\subset\operatorname{End}(\mathbb{R}^4)$ is the same thing as a faithful $A$-module structure on $\mathbb{R}^4$: the subalgebra acts on the carrier, the action is faithful because the subalgebra is a set of operators, and every faithful module structure gives back the subalgebra as its image. The classification of the subalgebras is therefore the classification of the ways in which a finite-dimensional real algebra can act faithfully on a four-dimensional real space.

**The two structure theorems.** Two classical theorems turn that into a finite list. Wedderburn's theorem says that a finite-dimensional semisimple real algebra is a product $\prod_i M_{n_i}(D_i)$ of matrix algebras over division algebras. Frobenius' theorem says that the only finite-dimensional real division algebras are $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, of real dimensions $d=1,2,4$. The simple module of the factor $M_{n_i}(D_i)$ is $D_i^{n_i}$, of real dimension $n_id_i$, and every module over the factor is a direct sum of $m_i$ copies of it.

**Theorem (module dictionary for the split form).** Let $A$ be a semisimple real algebra, $A\cong\prod_{i=1}^{r}M_{n_i}(D_i)$ with $D_i\in\{\mathbb{R},\mathbb{C},\mathbb{H}\}$ and $d_i=\dim_{\mathbb{R}}D_i$. Then $A$ admits a unital embedding into $M_4(\mathbb{R})$ if and only if there are integers $m_i\ge1$ with

$$
\sum_{i=1}^{r}m_in_id_i=4 .
$$

*Proof.* An embedding is a faithful module structure on $\mathbb{R}^4$, and a module over the product is a direct sum $\bigoplus_i m_iD_i^{n_i}$ with each $m_i\ge1$ because the action is faithful on each factor. Its real dimension is the sum displayed. Conversely such a module structure exists and gives the embedding. ∎

**Corollary.** In particular $\sum_in_id_i\le4$. The corollary is what makes the list finite: each $n_i\ge1$ and each $d_i\ge1$, so at most four factors occur, and the number of isomorphism types is bounded by the number of multisets of at most four symbols drawn from a fixed alphabet.

**The semisimple types.** Running the count gives exactly seventeen isomorphism types, and they are collected in one table.

**What the count counts.** The seventeen is the number of *isomorphism types* of semisimple $A$, and the rule matters because one type can have several inequivalent embeddings. A type is a multiset of simple factors $M_{n_i}(D_i)$ for which some choice of multiplicities $m_i\ge1$ solves $\sum m_in_id_i=4$; distinct factor multisets give non-isomorphic $A$, and a multiset is counted once whatever multiplicities it admits. The weights $n_id_i$ available are $1$ for $\mathbb{R}$, $2$ for $M_2(\mathbb{R})$ and for $\mathbb{C}$, $3$ for $M_3(\mathbb{R})$, and $4$ for $M_4(\mathbb{R})$, $M_2(\mathbb{C})$ and $\mathbb{H}$. Note that $M_3(\mathbb{R})$ alone does not occur: $\mathbb{R}^4$ is not a multiple of $\mathbb{R}^3$, so $M_3(\mathbb{R})$ has no faithful four-dimensional module and does not embed in $M_4(\mathbb{R})$ at all; it appears only with a scalar factor, as $M_3(\mathbb{R})\oplus\mathbb{R}$. If the multiplicities are counted as part of the data the number is eighteen, the extra item being $\mathbb{R}\oplus\mathbb{R}$ with module $\mathbb{R}^3\oplus\mathbb{R}$ rather than $\mathbb{R}^2\oplus\mathbb{R}^2$. The two are the same algebra and different conjugacy classes of embeddings, $\operatorname{diag}(\lambda,\lambda,\lambda,\mu)$ against $\operatorname{diag}(\lambda,\lambda,\mu,\mu)$, and the table counts types and not classes. The column of witnesses gives a concrete embedding, written in the split form with $\mathbb{C}\subset M_2(\mathbb{R})$ the rotation block $\begin{pmatrix}a&-b\\ b&a\end{pmatrix}$.

| type | $\dim_{\mathbb{R}}$ | module | witness in $M_4(\mathbb{R})$ |
|---|---|---|---|
| $\mathbb{R}$ | $1$ | $\mathbb{R}^4$ | scalars |
| $\mathbb{C}$ | $2$ | $\mathbb{C}^2$ | $\{z\mathrm{I}_4\}$ |
| $\mathbb{R}^2$ | $2$ | $\mathbb{R}^2\oplus\mathbb{R}^2$ | $\operatorname{diag}(\lambda,\mu,\mu,\mu)$ |
| $\mathbb{C}\oplus\mathbb{R}$ | $3$ | $\mathbb{C}\oplus\mathbb{R}^2$ | $\operatorname{diag}(z,\lambda,\lambda)$ |
| $\mathbb{R}^3$ | $3$ | $\mathbb{R}\oplus\mathbb{R}\oplus\mathbb{R}^2$ | $\operatorname{diag}(\lambda,\mu,\nu,\nu)$ |
| $\mathbb{C}\oplus\mathbb{R}^2$ | $4$ | $\mathbb{C}\oplus\mathbb{R}\oplus\mathbb{R}$ | $\operatorname{diag}(z,\lambda,\mu)$ |
| $\mathbb{C}^2$ | $4$ | $\mathbb{C}\oplus\mathbb{C}$ | two complex blocks |
| $\mathbb{H}$ | $4$ | $\mathbb{H}$ | left multiplication $L(\mathbb{B}_H)$ |
| $M_2(\mathbb{R})$ | $4$ | $(\mathbb{R}^2)^2$ | $L(M_2(\mathbb{R}))$ |
| $\mathbb{R}^4$ | $4$ | four lines | diagonal |
| $M_2(\mathbb{R})\oplus\mathbb{R}$ | $5$ | $\mathbb{R}^2\oplus\mathbb{R}^2$ | $\operatorname{diag}(A,\lambda,\lambda)$ |
| $\mathbb{C}\oplus M_2(\mathbb{R})$ | $6$ | $\mathbb{C}\oplus\mathbb{R}^2$ | $\operatorname{diag}(z,A)$ |
| $M_2(\mathbb{R})\oplus\mathbb{R}^2$ | $6$ | $\mathbb{R}^2\oplus\mathbb{R}\oplus\mathbb{R}$ | $\operatorname{diag}(A,\lambda,\mu)$ |
| $M_2(\mathbb{C})$ | $8$ | $\mathbb{C}^2$ | complex-linear maps |
| $M_2(\mathbb{R})\oplus M_2(\mathbb{R})$ | $8$ | $(\mathbb{R}^2)^2$ | two real $2\times2$ blocks |
| $M_3(\mathbb{R})\oplus\mathbb{R}$ | $10$ | $\mathbb{R}^3\oplus\mathbb{R}$ | $\operatorname{diag}(A,\lambda)$ |
| $M_4(\mathbb{R})$ | $16$ | $\mathbb{R}^4$ | the algebra |

Four entries deserve a word, because they are the ones the tables of the later sections use.

- $\mathbb{H}$ is a unital subalgebra of $M_4(\mathbb{R})$ and it is not a real form of anything in the ambient: it is the image $L(\mathbb{B}_H)$ of the quaternion space, and it is four-dimensional. Its traceless part is $\mathfrak{su}(2)$, and its commutator algebra is $\mathfrak{u}(2)$.
- $M_2(\mathbb{R})$ occurs twice in the table, once as $M_2(\mathbb{R})$ and once as the block-diagonal image $L(M_2(\mathbb{R}))$; the two witnesses are conjugate in $M_4(\mathbb{R})$, since both are the endomorphism algebra of a decomposition into two $2$-planes. The entry $\mathbb{C}$ occurs with two different multiplicities, $m=2$ (as $\{z\mathrm{I}_4\}$) and $m=1$ (inside $\operatorname{diag}(z,\lambda,\lambda)$), and those two embeddings are *not* conjugate: in the first the elements of $\mathbb{C}$ are invertible, in the second they are not. Multiplicity is part of the conjugacy class, not part of the isomorphism type.
- $M_2(\mathbb{C})$ of dimension $8$ is the endomorphism algebra of a complex structure on $\mathbb{R}^4$; the set of its images is the symmetric space $GL(4,\mathbb{R})/GL(2,\mathbb{C})$ of real dimension $16-8=8$.
- $M_3(\mathbb{R})\oplus\mathbb{R}$ of dimension $10$ is the largest proper semisimple type. It is a block-diagonal algebra with a one-dimensional block, and it sits inside the stabilizer of a line.

**The maximal ones.** A subalgebra is maximal if it is proper and contained in no proper subalgebra. Among the semisimple types only two are maximal: $M_2(\mathbb{C})$ and $M_2(\mathbb{R})\oplus M_2(\mathbb{R})$, both of dimension $8$.

*Proof.* Let $A$ be semisimple and maximal. If $A$ preserves a proper subspace of $\mathbb{R}^4$ then $A$ is contained in the stabilizer of that subspace, which is a proper subalgebra of dimension at most $13$, so $A$ is that stabilizer or is not maximal, and a stabilizer is not semisimple. So a maximal semisimple $A$ acts irreducibly. An irreducible semisimple $A$ has a single isotypic component, so there is one factor and $m=1$, and $nd=4$: the possibilities are $M_4(\mathbb{R})$, $M_2(\mathbb{C})$ and $\mathbb{H}$. Of these $\mathbb{H}$ is contained in $M_2(\mathbb{C})$, by complex-linearity of left quaternion multiplication on $\mathbb{H}=\mathbb{C}^2$, and it is therefore not maximal; the other two are not contained in anything but the whole algebra. ∎

The maximal subalgebras of $M_4(\mathbb{R})$ that are not semisimple are the stabilizers of subspaces. The stabilizer of a line is $\{X:X(\ell)\subset\ell\}$, of dimension $1+3+9=13$; the stabilizer of a hyperplane is its transpose and has the same dimension; the stabilizer of a $2$-plane has dimension $4+4+4=12$. These three, together with the two irreducible algebras of dimension $8$, are the maximal proper subalgebras up to conjugacy. Completeness of that list is classical, and the two ingredients are the two already used: an irreducible algebra is one factor with $m=1$ and is bounded by the table, and a reducible one is contained in a stabilizer, which for $n=4$ is one of the three listed.

**The parabolic and the Borel.** The stabilizer of a complete flag $0\subset\ell_1\subset\ell_2\subset\ell_3\subset\mathbb{R}^4$ is the algebra of upper triangular matrices in the adapted basis, of dimension $4+3+2+1=10$; it is the **Borel** subalgebra, and it is not maximal, being the intersection of the three parabolic stabilizers. The three subspace stabilizers are the **parabolic** subalgebras, of dimensions $13$, $12$ and $13$. The names are inherited from the Lie layer, where the same sets are the parabolics of $\mathfrak{sl}(4,\mathbb{R})$; the associative sets contain the Lie ones and are larger, and the two families must not be identified.

**The distinguished members.** The biquaternion base contributes the entries

$$
L(\mathbb{B})\cong M_2(\mathbb{C}),\qquad L(\mathbb{B}_H)\cong\mathbb{H},\qquad L(\mathbb{B}_V\cap M_2(\mathbb{R}))\cong M_2(\mathbb{R})\ \text{as a space},
$$

of dimensions $8$, $4$ and $4$. The first is the largest biquaternion object in the split form and it is one of the two maximal semisimple algebras; the second is the copy of the quaternions; the third is the scalar-free part of the image of the split element form, and it is not itself an associative subalgebra, since the product of two traceless matrices is not traceless. The full list of base objects with their statuses is the table of the third section.

**Warning (what is not classified).** The seventeen rows are the isomorphism types of the *semisimple* subalgebras, and the classification of all unital subalgebras is not known in closed form, even for $M_4(\mathbb{R})$. The gap is the nilpotent radical. A subalgebra with a nontrivial nilpotent radical contains elements whose action on $\mathbb{R}^4$ is nilpotent, and the isomorphism types of such algebras are not a finite list: the truncated polynomial algebras $\mathbb{R}[x]/(x^{k})$ for $k\le4$, the dual numbers $\mathbb{R}[\epsilon]$, the algebra $\mathbb{R}[\epsilon,\eta]/(\epsilon,\eta)^{2}$, the complex dual numbers $\mathbb{C}[\epsilon]$, and the upper triangular algebras all occur, together with continuous families obtained by deforming the radical inside a fixed semisimple part. The honest statement is that the semisimple layer is classified, that the parabolic and Borel algebras are classified as a family, and that the rest is a zoo with no organising theorem of the same strength.

**Remark (why the semisimple layer is the useful one).** The zoo is not a defect for the purpose of this article. Every subalgebra that arises from the biquaternion algebra is semisimple: $M_2(\mathbb{C})$, $\mathbb{H}$, $M_2(\mathbb{R})$, and their Lie and Jordan shadows. The nilpotent part of the lattice matters for the study of *degenerations* of the algebra, and that is a different subject.

## Associative Subalgebras of the Quaternionic Form

**The principle, and the extra structure.** The quaternionic form is $\mathcal{E}_{\mathbb{H}}=\operatorname{End}_{\mathbb{H}}(\mathbb{H}^2)$, the endomorphisms of a right $\mathbb{H}$-module of rank two. A unital subalgebra $A\subset\mathcal{E}_{\mathbb{H}}$ is again a faithful module structure, but on a space that already carries a right quaternionic structure, and the action of $A$ must commute with it. That commuting condition is what replaces the dimension count of the split case, and it is best expressed as a tensor.

**The criterion.** Let $A$ be a real algebra. A unital embedding $A\hookrightarrow\operatorname{End}_{\mathbb{H}}(\mathbb{H}^2)$ is the same thing as a faithful left module structure of $A$ on the real space $\mathbb{H}^2$ commuting with the right action of $\mathbb{H}$, and that is the same thing as a faithful module structure over $A\otimes_{\mathbb{R}}\mathbb{H}^{\mathrm{op}}$ on a real space of dimension $8$.

**Theorem (module dictionary for the quaternionic form).** Let $A\cong\prod_{i=1}^{r}M_{n_i}(D_i)$ be semisimple, with $D_i\in\{\mathbb{R},\mathbb{C},\mathbb{H}\}$. Then $A$ admits a unital embedding into $M_2(\mathbb{H})$ if and only if

$$
\sum_{i=1}^{r}n_i\le2 .
$$

*Proof.* Three isomorphisms fix the tensor factors: $M_n(\mathbb{R})\otimes\mathbb{H}\cong M_n(\mathbb{H})$, $M_n(\mathbb{C})\otimes\mathbb{H}\cong M_{2n}(\mathbb{C})$, and $M_n(\mathbb{H})\otimes\mathbb{H}\cong M_{4n}(\mathbb{R})$, the last from $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{H}\cong M_4(\mathbb{R})$. The minimal faithful module of $M_k(D)$ over $\mathbb{R}$ has dimension $k\,d$: it is $D^k$. So the minimal faithful module of $A\otimes\mathbb{H}^{\mathrm{op}}$ has dimension $\sum_i(2n_i)(2)=4\sum_in_i$ in the complex case and $4n_i$ in the other two, and in every case the answer is $4n_i$ for the factor $M_{n_i}(D_i)$. The product needs the sum, $4\sum_in_i$, and a module of dimension $8$ exists if and only if that sum is at most $8$. ∎

**Corollary (the two dictionary theorems compared).** The split form requires $\sum m_in_id_i=4$ with all $m_i\ge1$, and the quaternionic form requires $\sum n_i\le2$. The second condition is stronger in the complex and quaternionic directions and weaker in the real direction, and the two lists are consequently not nested in either direction.

**The semisimple types.** The count gives twelve types.

| type | $\dim_{\mathbb{R}}$ | $\sum n_i$ | witness |
|---|---|---|---|
| $\mathbb{R}$ | $1$ | $1$ | scalars |
| $\mathbb{C}$ | $2$ | $1$ | $\{z\mathrm{I}_2\}$ |
| $\mathbb{H}$ | $4$ | $1$ | scalars |
| $\mathbb{R}^2$ | $2$ | $2$ | $\operatorname{diag}(\lambda,\mu)$ |
| $\mathbb{C}\oplus\mathbb{R}$ | $3$ | $2$ | $\operatorname{diag}(z,\lambda)$ |
| $\mathbb{C}^2$ | $4$ | $2$ | two complex blocks |
| $M_2(\mathbb{R})$ | $4$ | $2$ | real entries |
| $\mathbb{H}\oplus\mathbb{R}$ | $5$ | $2$ | $\operatorname{diag}(q,\lambda)$ |
| $\mathbb{C}\oplus\mathbb{H}$ | $6$ | $2$ | $\operatorname{diag}(z,q)$ |
| $M_2(\mathbb{C})$ | $8$ | $2$ | complex entries |
| $\mathbb{H}\oplus\mathbb{H}$ | $8$ | $2$ | two quaternionic blocks |
| $M_2(\mathbb{H})$ | $16$ | $2$ | the algebra |

**The chain of matrix algebras.** Four rows of the table form a chain that does not exist in the split form:

$$
M_2(\mathbb{R})\subset M_2(\mathbb{C})\subset M_2(\mathbb{H}),
$$

of real dimensions $4\subset8\subset16$, and the chain is the entrywise one: real entries, then complex entries, then quaternionic entries. The first inclusion is the witness for $M_2(\mathbb{R})$, the second for $M_2(\mathbb{C})$, and the middle algebra is maximal in the ambient. The chain is the cleanest statement of the difference between the two forms: the quaternionic form contains the split element algebra and the complex amplification of it, and it contains them at two different levels.

**What does not occur, and why.** The criterion excludes four candidates that a naive count would admit.

- $M_4(\mathbb{R})$ does not embed in $M_2(\mathbb{H})$, because $n=4$ and $4>2$. The dimension argument is the same one stated differently: both algebras have real dimension $16$, so an embedding would be an isomorphism, and the two are not isomorphic, as their trace-form inertias $(10,6)$ and $(6,10)$ show.
- $M_3(\mathbb{R})$ does not embed, because $n=3$. Its minimal faithful module is $\mathbb{R}^3$, and $M_3(\mathbb{R})\otimes\mathbb{H}\cong M_3(\mathbb{H})$ needs $\mathbb{H}^3$ of real dimension $12$.
- $\mathbb{H}\oplus\mathbb{H}\oplus\mathbb{R}$ and the other three-factor products do not embed, because $\sum n_i=3$.
- $\mathbb{C}\oplus\mathbb{C}\oplus\mathbb{C}$ does not embed, for the same reason.

**The copies of the complex numbers.** The row $\mathbb{C}$ hides a family. A unital embedding $\mathbb{C}\hookrightarrow M_2(\mathbb{H})$ is a complex structure $J$ on $\mathbb{H}^2$ commuting with the right action of $\mathbb{H}$, that is an almost complex structure on the quaternionic plane that is $\mathbb{H}$-linear. The set of such $J$ is acted on transitively by $Sp(2)$ with stabilizer $U(2)$, so the family is the symmetric space

$$
Sp(2)/U(2),
$$

of real dimension $10-4=6$, the quaternionic hyperbolic plane. Two of its points are distinguished: the complex structure coming from the left action of $i\in\mathbb{H}$, whose copy of $\mathbb{C}$ lies in the scalars, and the ones coming from the right action, which do not. The family is not a technicality. It is the operator-level shadow of the element-level fact that $\mathbb{C}$ sits inside $\mathbb{H}$ in several ways, and it is the reason the article says "a copy of $\mathbb{C}$" and not "the copy".

**The distinguished members.** The quaternionic form carries one object that the split form does not: the scalar copy of $\mathbb{H}$ of dimension $4$, which is $\mathbb{C}$-linear and quaternionic at once. It carries also the maximal pair $M_2(\mathbb{C})$ and $\mathbb{H}\oplus\mathbb{H}$, both of dimension $8$, and the parabolic stabilizer of a quaternionic line, of dimension $4+4+4=12$. The biquaternion base contributes nothing further, by the warning of the third section: $L(\mathbb{B})$ is $8$-dimensional, it is not contained in $M_2(\mathbb{H})$ as a real subalgebra, and its only intersection with the quaternionic form is the copy of $\mathbb{C}$ that is the scalars of $\mathbb{C}\subset\mathbb{H}$.

**Remark (the intuition of the division algebra fails, and how).** The element-level pair behaves as one expects: the division algebra $\mathbb{H}$ carries a small and rigid lattice, the matrix algebra $M_2(\mathbb{R})$ a large one. At the operator level the count runs the other way. The quaternionic form has *twelve* semisimple types against the *seventeen* of the split form, and it does not have the property that matters, an exhaustive classification of the non-semisimple part. The reason is that $\mathbb{H}^2$ is only eight-dimensional over $\mathbb{R}$ while carrying a four-dimensional division algebra, so the quaternionic constraint is a strong constraint on multiplicities. A strong constraint does two things at once: it removes types, and it pins the surviving ones down, since the module is forced to be one of the few decompositions that fit in eight dimensions. Fewer types and more rigidity are one phenomenon seen twice, not a reversal of the element-level pattern. The correct measure of the difference is the pair of criteria $\sum n_i\le2$ and $\sum n_id_i\le4$, and not the words division and matrix.

## Lie Subalgebras of the Split Form

**The algebra.** The commutator turns $M_4(\mathbb{R})$ into the real Lie algebra $\mathfrak{gl}(4,\mathbb{R})$, of real dimension sixteen. Its centre is $\mathbb{R}\mathrm{I}_4$ and its derived algebra is the traceless part,

$$
\mathfrak{sl}(4,\mathbb{R})=\{X:\operatorname{tr}X=0\},
$$

of dimension fifteen, which is simple. The decomposition

$$
\mathfrak{gl}(4,\mathbb{R})=\mathfrak{sl}(4,\mathbb{R})\oplus\mathbb{R}\mathrm{I}_4
$$

is a direct sum of Lie algebras, so every subalgebra of $\mathfrak{gl}(4,\mathbb{R})$ is described by a subalgebra of $\mathfrak{sl}(4,\mathbb{R})$ together with a linear functional on it that vanishes on its derived algebra. The article uses that reduction once and then works inside $\mathfrak{sl}(4,\mathbb{R})$.

**The Killing form.** For $\mathfrak{gl}(n,\mathbb{R})$ the Killing form is

$$
K(X,Y)=2n\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y),
$$

which for $n=4$ reads $K(X,Y)=8\operatorname{tr}(XY)-2\operatorname{tr}(X)\operatorname{tr}(Y)$. It is degenerate, with radical the centre: $\operatorname{ad}_{\mathrm{I}_4}=0$, so $K(\mathrm{I}_4,X)=0$ for every $X$, and on the traceless part it is $8\operatorname{tr}(XY)$, which is nondegenerate by the simplicity of $\mathfrak{sl}(4,\mathbb{R})$. The inertias below are computed intrinsically, in the algebra itself, and not in the ambient $\mathbb{B}_{\mathbb{R}}$; the two conventions agree on the semisimple subalgebras and differ on the abelian ones, as the element-level article explains. The first entry counts positive eigenvalues and the second negative ones, so a compact semisimple algebra, whose Killing form is negative definite, has inertia $(0,\dim)$: that is why $\mathfrak{so}(4)$ reads $(0,6)$ and not $(6,0)$.

| subalgebra | $\dim_{\mathbb{R}}$ | type | $K$ inertia | radical |
|---|---|---|---|---|
| $\mathfrak{gl}(4,\mathbb{R})$ | $16$ | reductive, $A_3\oplus T_1$ | $(9,6)$ plus one null | $\mathbb{R}\mathrm{I}_4$ |
| $\mathfrak{sl}(4,\mathbb{R})$ | $15$ | $A_3$ split | $(9,6)$ | $0$ |
| $\mathfrak{sp}(2,\mathbb{R})$ | $10$ | $C_2$ split | $(6,4)$ | $0$ |
| $\mathfrak{sl}(3,\mathbb{R})\oplus\mathbb{R}$ | $9$ | Levi | $(5,3)$ plus one null | $\mathbb{R}$ |
| $\mathfrak{sl}(2,\mathbb{R})\oplus\mathfrak{sl}(2,\mathbb{R})\oplus\mathbb{R}$ | $7$ | Levi | $(4,2)$ plus one null | $\mathbb{R}$ |
| $\mathfrak{so}(4)$ | $6$ | $D_2$ compact | $(0,6)$ | $0$ |
| $\mathfrak{so}(3,1)$ | $6$ | $D_2$ Lorentzian | $(3,3)$ | $0$ |
| $\mathfrak{so}(2,2)$ | $6$ | $D_2$ split | $(4,2)$ | $0$ |
| $\mathfrak{gl}(2,\mathbb{R})$ | $4$ | $A_1\oplus T_1$ | $(2,1)$ plus one null | $\mathbb{R}\mathrm{I}_2$ |
| $\mathfrak{u}(2)$ | $4$ | compact reductive | $(0,3)$ plus one null | $\mathbb{R}i\mathrm{I}_2$ |
| $\mathfrak{sl}(2,\mathbb{R})$ | $3$ | $A_1$ split | $(2,1)$ | $0$ |
| $\mathfrak{su}(2)$ | $3$ | $A_1$ compact | $(0,3)$ | $0$ |
| $\mathbb{R}\mathrm{I}_4$ | $1$ | abelian | $0$ | the line |

The inertias are the deciding invariant of the layer. Two real Lie algebras that are isomorphic have Killing forms related by the isomorphism, so the inertia of $K$ is an isomorphism invariant up to a positive scalar; and the table separates by inertia what the dimensions cannot separate. Three algebras of dimension six appear with inertias $(0,6)$, $(3,3)$ and $(4,2)$, and they are consequently pairwise non-isomorphic, although $\mathfrak{so}(4)$, $\mathfrak{so}(3,1)$ and $\mathfrak{so}(2,2)$ are all real forms of the one complex algebra $\mathfrak{so}(4,\mathbb{C})\cong\mathfrak{sl}(2,\mathbb{C})\oplus\mathfrak{sl}(2,\mathbb{C})$.

**The maximal subalgebras.** A subalgebra of $\mathfrak{sl}(4,\mathbb{R})$ is maximal if it is proper and contained in no proper subalgebra. Up to conjugacy they are the following.

| maximal subalgebra | $\dim_{\mathbb{R}}$ | type | why maximal |
|---|---|---|---|
| $\mathfrak{p}_1$, stabilizer of a line | $12$ | parabolic | contains the image of $\mathfrak{p}_1$ in the flag variety |
| $\mathfrak{p}_2$, stabilizer of a plane | $11$ | parabolic | same, middle Grassmannian |
| $\mathfrak{sp}(2,\mathbb{R})$ | $10$ | $C_2$ | complement is the irreducible module $\operatorname{Sym}^2_0$ |
| $\mathfrak{sl}(3,\mathbb{R})\oplus\mathbb{R}$ | $9$ | Levi of $\mathfrak{p}_1$ | reductive, maximal by Dynkin |
| $\mathfrak{sl}(2,\mathbb{R})^2\oplus\mathbb{R}$ | $7$ | Levi of $\mathfrak{p}_2$ | reductive, maximal by Dynkin |
| $\mathfrak{so}(4)$ | $6$ | $D_2$ compact | irreducible symmetric pair |
| $\mathfrak{so}(3,1)$ | $6$ | $D_2$ Lorentzian | irreducible symmetric pair |
| $\mathfrak{so}(2,2)$ | $6$ | $D_2$ split | irreducible symmetric pair |
| $\mathfrak{sl}(2,\mathbb{R})$ in $\operatorname{Sym}^3$ | $3$ | $A_1$ irreducible | Dynkin index one |

The two parabolics and the two Levis are read off from the flag structure of $\mathbb{R}^4$: the stabilizer of a line has dimension $15-3=12$, the stabilizer of a plane has dimension $15-4=11$, and the two Levis are their reductive parts, of dimensions $8+1=9$ and $3+3+1=7$. The last row is of a third kind. It is neither parabolic nor reductive-with-a-torus, and it acts irreducibly: through the adjoint action of $\mathfrak{sl}(2,\mathbb{R})$ one has $\mathbb{R}^4\cong\operatorname{Sym}^3(\mathbb{R}^2)$, and the image is the irreducible $A_1$ of dimension three. Dynkin's list separates exactly these three families, and $\mathfrak{sl}(2,\mathbb{R})$ in $\operatorname{Sym}^3$ is the only irreducible maximal subalgebra of $A_3$.

Two further questions about maximality have short answers, and the article records them because they are the questions a reader asks first. The traceless part $\mathfrak{sl}(4,\mathbb{R})$ **is** maximal in $\mathfrak{gl}(4,\mathbb{R})$: it has codimension one, so a subalgebra containing it is either $\mathfrak{sl}(4,\mathbb{R})$ or the whole algebra. And $\mathfrak{gl}(4,\mathbb{R})$ contains **no** copy of $\mathfrak{gl}(2,\mathbb{H})$, because the two algebras have the same dimension and are not isomorphic, by the Killing inertias $(9,6)$ and $(5,10)$.

**The three orthogonal forms are maximal, and the reason is the invariant form.** Each of $\mathfrak{so}(4)$, $\mathfrak{so}(3,1)$, $\mathfrak{so}(2,2)$ acts irreducibly on $\mathbb{R}^4$, so none of them is contained in a parabolic. None of them is contained in a Levi, which would preserve a decomposition into $2$-planes. None of them is contained in $\mathfrak{sp}(2,\mathbb{R})$: an algebra contained in the stabilizer of a symplectic form $\omega$ preserves $\omega$, and an irreducible algebra whose representation is self-dual preserves a unique bilinear form up to scale, by Schur's lemma applied to $\operatorname{End}_{\mathfrak{g}}(\mathbb{R}^4)$; that unique form for $\mathfrak{so}(p,q)$ is the symmetric form of inertia $(p,q)$, and the symplectic form is skew, so no invariant symplectic form exists. The same argument in reverse shows that $\mathfrak{sp}(2,\mathbb{R})$ is maximal: its complement $\operatorname{Sym}^2_0(\mathbb{R}^4)$ of dimension $5$ is irreducible for $\mathfrak{sp}(2,\mathbb{R})$, so no intermediate algebra exists.

**Remark (the small-rank coincidence that is not one).** The complex algebra $\mathfrak{sl}(4,\mathbb{C})$ is isomorphic to $\mathfrak{so}(6,\mathbb{C})$, and the isomorphism identifies the split form $\mathfrak{sl}(4,\mathbb{R})$ with $\mathfrak{so}(3,3)$. Under it the subalgebra $\mathfrak{so}(4,\mathbb{C})$ of $\mathfrak{sl}(4,\mathbb{C})$ becomes a subalgebra of $\mathfrak{so}(6,\mathbb{C})$ of type $D_2$, and the three real forms $(0,6)$, $(3,3)$, $(4,2)$ become the three real forms $\mathfrak{so}(6)$, $\mathfrak{so}(3,3)$ and $\mathfrak{so}(4,2)$-type of that $D_2$. Nothing in the table depends on the identification; it is quoted because the same chain of isomorphisms appears in the group section, where $SL(4,\mathbb{R})\cong Spin(3,3)$ and $\mathfrak{sl}(2,\mathbb{H})\cong\mathfrak{so}(5,1)$.

**The biquaternion base, and the three real forms of $\mathfrak{so}(3,\mathbb{C})$.** The base enters the Lie layer through the pure part, and the entry is worth stating carefully because it is easy to over-state.

- $\mathbb{B}_V$ is a complex Lie algebra of complex dimension three, isomorphic to $\mathfrak{so}(3,\mathbb{C})$, with bracket the commutator of the bivectors. Its image $L(\mathbb{B}_V)$ is a complex Lie subalgebra of $\mathfrak{gl}(4,\mathbb{C})$.
- Read as a *real* Lie algebra, $\mathbb{B}_V$ is $\mathfrak{so}(3,1)$. The realification of a complex Lie algebra doubles the dimension and doubles the Killing form into a real form of inertia $(n,n)$ on a compact-type complex algebra, and the computation gives $(3,3)$ here, which is the inertia of $\mathfrak{so}(3,1)$ in the table.
- The real points of $\mathbb{B}_V$ in the two real forms are the other two real forms of the same complex algebra. In the split form, $\mathbb{B}_V\cap M_2(\mathbb{R})=\mathfrak{sl}(2,\mathbb{R})=\mathfrak{so}(2,1)$, of inertia $(2,1)$; in the quaternionic form, $\mathbb{B}_V\cap\mathbb{H}=\mathbb{B}_V$ itself, the compact $\mathfrak{su}(2)=\mathfrak{so}(3)$, of inertia $(0,3)$.

So the single complex space $\mathbb{B}_V$ produces all three real forms of $\mathfrak{so}(3,\mathbb{C})$: the compact one and the split one as the real points in the two real forms of $\mathbb{B}$, and the Lorentzian one as the realification of the complex object. That is the cleanest illustration in the corpus of the general fact that a complex algebra with several real forms produces several real Lie algebras from one complex subspace.

**Warning (a complex subalgebra is not a real subalgebra).** $L(\mathbb{B}_V)$ has real dimension six, and a reader may expect to find it in the table above. It is not there, and it cannot be: $L(\mathbb{B}_V)$ contains $L_{\vec e_x}$, whose matrix has entries in $i\mathbb{R}$, and $M_4(\mathbb{R})$ contains no such element. The table is a table of *real* subalgebras of $\mathfrak{gl}(4,\mathbb{R})$, and the correct reading of the base is the one just given: the real points are in the table, the complex object is in $\mathfrak{gl}(4,\mathbb{C})$, and the realification of the complex object is $\mathfrak{so}(3,1)$, which is in the table for a different reason.

**The remaining base objects.** The other two distinguished subalgebras from the base are the following.

- $L(\mathbb{B}_H)\cong\mathbb{H}$ is a four-dimensional associative subalgebra of $M_4(\mathbb{R})$, and its commutator algebra is $\mathfrak{u}(2)$: the centre is $\mathbb{R}\mathrm{I}_4$ and the traceless part is the compact $\mathfrak{su}(2)$, so the Lie algebra of the quaternions is the compact reductive algebra $\mathfrak{u}(2)$, of dimension four and inertia $(0,3)$ plus a null direction.
- $L(\mathbb{B}_{\Phi})$ is a complex Lie subalgebra of real dimension four, and it is the same algebra $\mathfrak{u}(2)$, reached from the other side: $\mathbb{B}_{\Phi}$ *is* the compact Lie algebra $\mathfrak{u}(2)$ at the element level, and its image is a complex Lie algebra whose real points in the split form are the antisymmetric line.

The two routes to $\mathfrak{u}(2)$ agree and they illuminate the two roles of the algebra: $\mathfrak{u}(2)$ is the Lie algebra of the group of invertibles of the quaternions and it is also the compact real form of $\mathfrak{gl}(2,\mathbb{C})$. At the operator level the first role is the traceless part of $L(\mathbb{B}_H)$ and the second is the realification of $L(\mathbb{B}_{\Phi})$.

**The ideals.** The two-sided ideals of the Lie algebra $\mathfrak{gl}(4,\mathbb{R})$ are $0$, $\mathbb{R}\mathrm{I}_4$, $\mathfrak{sl}(4,\mathbb{R})$ and the whole algebra. For $\mathfrak{sl}(4,\mathbb{R})$ is simple, so an ideal not contained in the centre projects onto it and contains $[\mathfrak{sl},\mathfrak{sl}]=\mathfrak{sl}$; and an ideal inside the centre is $0$ or the centre. The list is much shorter than the list of ideals of the associative algebra, which is $0$, $M_4(\mathbb{R})$, and nothing else: the associative algebra is simple, the Lie algebra is not, and the Lie ideal $\mathfrak{sl}(4,\mathbb{R})$ is not an associative ideal.

**Warning (a Lie subalgebra is not an associative subalgebra).** The traceless part $\mathfrak{sl}(4,\mathbb{R})$ is a Lie subalgebra and not an associative one, since the product of two traceless matrices has trace $\operatorname{tr}(XY)$, which is generally nonzero. In the other direction the diagonal algebra $\mathbb{R}^4$ is associative and abelian. The two lattices of the fourth and sixth sections share elements and are not the same lattice, and every row of every table names its layer.

## Lie Subalgebras of the Quaternionic Form

**The algebra.** The commutator turns $M_2(\mathbb{H})$ into the real Lie algebra $\mathfrak{gl}(2,\mathbb{H})$, of real dimension sixteen, with centre $\mathbb{R}\mathrm{I}_2$ and derived algebra the quaternionically traceless part

$$
\mathfrak{su}^{*}(4)=\mathfrak{sl}(2,\mathbb{H})=\{X\in M_2(\mathbb{H}):\operatorname{Re}\operatorname{tr}X=0\},
$$

of dimension fifteen. The notation $\mathfrak{su}^{*}(4)$ is the classical one: $SU^{*}(2n)$ is the group of quaternionic matrices of quaternionic determinant one, and its Lie algebra consists of the matrices whose quaternionic trace is purely imaginary. In this article the algebra is written $\mathfrak{sl}(2,\mathbb{H})$ and the symbol $\mathfrak{su}^{*}(4)$ is quoted once, for the reader who looks it up.

**The Killing form and the inertias.** The Killing form of $\mathfrak{gl}(2,\mathbb{H})$ is degenerate with radical the centre, and on $\mathfrak{sl}(2,\mathbb{H})$ it is nondegenerate, by simplicity. The inertias are these.

| subalgebra | $\dim_{\mathbb{R}}$ | type | $K$ inertia | radical |
|---|---|---|---|---|
| $\mathfrak{gl}(2,\mathbb{H})$ | $16$ | reductive | $(5,10)$ plus one null | $\mathbb{R}\mathrm{I}_2$ |
| $\mathfrak{sl}(2,\mathbb{H})=\mathfrak{su}^{*}(4)$ | $15$ | $A_3$ quaternionic | $(5,10)$ | $0$ |
| $\mathfrak{sp}(2)$ | $10$ | $C_2$ compact | $(0,10)$ | $0$ |
| $\mathfrak{sp}(1,1)$ | $10$ | $B_2\cong C_2$ Lorentzian | $(4,6)$ | $0$ |
| $\mathfrak{gl}(1,\mathbb{H})\oplus\mathfrak{gl}(1,\mathbb{H})$ | $8$ | reductive | $(0,6)$ plus two null | $\mathbb{R}^2$ |
| $\mathfrak{sl}(1,\mathbb{H})\oplus\mathfrak{sl}(1,\mathbb{H})\oplus\mathbb{R}$ | $7$ | Levi | $(0,6)$ plus one null | $\mathbb{R}$ |
| $\mathbb{R}\mathrm{I}_2$ | $1$ | abelian | $0$ | the line |

**The comparison with the split form is the content of the section.** The two algebras $\mathfrak{gl}(4,\mathbb{R})$ and $\mathfrak{gl}(2,\mathbb{H})$ have the same dimension, both are reductive, both have a one-dimensional centre and a simple derived algebra of dimension fifteen. They are not isomorphic, and the invariant that decides it is the inertia of the Killing form: $(9,6)$ against $(5,10)$. This number is the operator-level analogue of the element-level statement that $\mathfrak{sl}(2,\mathbb{R})$ and $\mathfrak{su}(2)$ have inertias $(2,1)$ and $(0,3)$, and it is the only invariant of the layer that separates the two forms without a frame.

| invariant | $M_4(\mathbb{R})$ | $M_2(\mathbb{H})$ |
|---|---|---|
| $\dim_{\mathbb{R}}$ of the algebra | $16$ | $16$ |
| centre | $\mathbb{R}\mathrm{I}_4$ | $\mathbb{R}\mathrm{I}_2$ |
| derived algebra | $\mathfrak{sl}(4,\mathbb{R})$ | $\mathfrak{sl}(2,\mathbb{H})$ |
| $K$ inertia of the derived algebra | $(9,6)$ | $(5,10)$ |
| maximal compact of the derived algebra | $\mathfrak{so}(4)$, $\dim 6$ | $\mathfrak{sp}(2)$, $\dim 10$ |
| real rank of the derived algebra | $3$ | $1$ |
| restricted root system | $A_3$ | $BC_1$ |

The last two rows are the structural explanation of the difference of inertias. The split form has real rank three and the full root system $A_3$; the quaternionic form has real rank one and restricted root system $BC_1$, with a two-dimensional root space of each sign. A rank-one algebra has a small non-compact part, hence a small positive-definite part of $K$, and $(5,10)$ is what a non-compact part of dimension five produces.

**The isomorphism with $\mathfrak{so}(5,1)$.** The quaternionic simple algebra of rank one is the Lorentz algebra of dimension six, and the identification is classical:

$$
\mathfrak{sl}(2,\mathbb{H})\cong\mathfrak{so}(5,1).
$$

Three invariants agree and they determine the algebra among the real forms of $A_3$: the dimension is fifteen, the maximal compact subalgebra is $\mathfrak{sp}(2)\cong\mathfrak{so}(5)$ of dimension ten, and the real rank is one. The compact part of $\mathfrak{so}(5,1)$ is $\mathfrak{so}(5)$, and its non-compact part has dimension $5=15-10$, which matches the five positive directions of the Killing form in the row above.

**The maximal subalgebras.** Up to conjugacy, the maximal subalgebras of $\mathfrak{sl}(2,\mathbb{H})$ are three.

| maximal subalgebra | $\dim_{\mathbb{R}}$ | type | reading under $\mathfrak{so}(5,1)$ |
|---|---|---|---|
| $\mathfrak{sp}(2)$ | $10$ | $C_2$ compact | $\mathfrak{so}(5)$, the maximal compact |
| $\mathfrak{sp}(1,1)$ | $10$ | $B_2\cong C_2$ Lorentzian | $\mathfrak{so}(4,1)$, the stabilizer of a spacelike vector |
| parabolic $\mathfrak{p}$ | $11$ | stabilizer of a quaternionic line | stabilizer of a null line |

The parabolic has Levi $\mathfrak{sl}(1,\mathbb{H})\oplus\mathfrak{sl}(1,\mathbb{H})\oplus\mathbb{R}$, of dimension $3+3+1=7$, and it is the full stabilizer of a one-dimensional quaternionic subspace of $\mathbb{H}^2$. The two algebras of dimension ten are $\mathfrak{so}(5)$ and $\mathfrak{so}(4,1)$; the first is compact and the second is the Lorentz algebra of five-dimensional Minkowski space, and the pair is the exact quaternionic analogue of the pair $\mathfrak{so}(4)$, $\mathfrak{so}(3,1)$ in the split form.

**Remark (no biquaternion base).** The quaternionic form carries no copy of the biquaternion base, by the warning of the third section, and the Lie layer reflects that. What the form carries from the element level is the scalar copy of $\mathbb{H}$, whose commutator algebra is $\mathfrak{su}(2)\oplus\mathbb{R}=\mathfrak{u}(2)$, and the scalar copy of $\mathbb{C}$, whose commutator algebra is $\mathbb{R}$ with zero bracket. Both are small and neither is maximal. The interesting Lie subalgebras of $\mathfrak{gl}(2,\mathbb{H})$ are the two $C_2$'s and the parabolic, and they have no element-level ancestor: they are genuinely quaternionic-linear objects.

**Warning (the compact $\mathfrak{sp}(2)$ is not all of the quaternionic unitary algebra).** The notation invites the error of identifying $\mathfrak{su}^{*}(4)$ with a unitary algebra. It is not one. $\mathfrak{su}^{*}(4)$ consists of the quaternionic matrices with vanishing real trace, and it is non-compact of real rank one; its maximal compact part is $\mathfrak{sp}(2)$, of dimension ten, and the remaining five dimensions are non-compact. The unitary algebra of the same dimension is $\mathfrak{su}(3,1)$, of real rank one as well, and the two are distinguished by their compact parts: $\mathfrak{u}(3)$ of dimension $9$ against $\mathfrak{sp}(2)$ of dimension $10$. The six real forms of $A_3$ are $\mathfrak{sl}(4,\mathbb{R})$, $\mathfrak{su}(4)$, $\mathfrak{su}(3,1)$, $\mathfrak{su}(2,2)$, $\mathfrak{su}^{*}(4)$ and $\mathfrak{sl}(4,\mathbb{C})_{\mathbb{R}}$; two of them have real rank one, and the operator-level pair $M_4(\mathbb{R})$, $M_2(\mathbb{H})$ corresponds to the first and the fifth.

## The Jordan Layer

**The third product.** On an associative algebra the symmetrized product

$$
X\circ Y=\tfrac12(XY+YX)
$$

is commutative and satisfies $X^{2}\circ(X\circ Y)=X^{2}\circ Y$; a real vector space with such a product is a **Jordan algebra**. The passage from the associative to the Jordan layer is not invertible, and the layer is therefore a genuinely different lattice. The article uses only the three standard facts: the product $\circ$ is commutative but not associative; an element is invertible in the Jordan sense exactly when it is invertible in the associative sense; and a subspace closed under $\circ$ need not be closed under the product or under the bracket.

**The three Jordan real forms.** The Jordan algebra $M_4(\mathbb{C})^{+}$ has exactly three real forms, and they are not the two of the associative layer.

| Jordan form | realisation | $\dim_{\mathbb{R}}$ | trace-form inertia | formally real |
|---|---|---|---|---|
| $M_4(\mathbb{R})^{+}$ | all of $M_4(\mathbb{R})$ | $16$ | $(10,6)$ | no |
| $M_2(\mathbb{H})^{+}$ | all of $M_2(\mathbb{H})$ | $16$ | $(6,10)$ | no |
| $H_4(\mathbb{C})$ | Hermitian matrices | $16$ | $(16,0)$ | yes |

The third form is the one the associative layer does not have. $H_4(\mathbb{C})$ is the space of complex Hermitian $4\times4$ matrices, of real dimension $4+2\cdot6=16$, and it is closed under $\circ$ because the symmetrized product of two Hermitian matrices is Hermitian. It is not the Hermitian part of a real form of the associative algebra: its real points in $M_4(\mathbb{R})$ are the real symmetric matrices $H_4(\mathbb{R})$, of dimension $10$, and those are only ten-dimensional. $H_4(\mathbb{C})$ has no associative real form above it in $M_4(\mathbb{C})$, and that is the precise sense in which the Jordan layer is larger than the associative one.

The inertias in the third column are computed on the trace form $(X,Y)\mapsto\operatorname{tr}(XY)$, which is a symmetric bilinear form on the Jordan algebra and not a Hermitian form. On $H_4(\mathbb{C})$ the form is positive definite, because $\operatorname{tr}(X^{2})=\sum_k\lambda_k^{2}$ for a Hermitian $X$ with eigenvalues $\lambda_k$. A Jordan algebra with a positive definite trace form is **formally real**: a sum of squares vanishes only when every term vanishes. That property is what the two associative forms lose, and it is the operator-level statement of the element-level fact that $\mathbb{B}_{\Psi}$ is the observable space.

**The Hermitian layer of the base.** The base enters here through $\mathbb{B}_{\Psi}$, and the entry is the one place in the article where the operator level is *smaller* than the element level.

- $\mathbb{B}_{\Psi}$ is the Hermitian space at the element level, of real dimension four, and it is closed under $\circ$.
- $L(\mathbb{B}_{\Psi})$ is a real subspace of $\mathcal{E}_{\mathbb{C}}$ of real dimension four. It is not closed under $\circ$: the product of two Hermitian operators is Hermitian only when they commute, and the witness is $L_{i\vec e_x}L_{i\vec e_y}=L_{(i\vec e_x)(i\vec e_y)}=L_{-\vec e_z}$, which is anti-Hermitian: $i\vec e_x$ and $i\vec e_y$ are Hermitian, and their product is not.
- What does hold is containment in the Jordan form: $L(\mathbb{B}_{\Psi})\subset H_4(\mathbb{C})$, since each $L_{\tilde Q}$ with $\tilde Q$ Hermitian is a Hermitian matrix. The image is a four-dimensional subspace of the sixteen-dimensional formally real Jordan algebra, and it is not a Jordan subalgebra of it.

So the Hermitian layer of the element algebra embeds as a subspace and not as a subalgebra, exactly as the pure part embeds as a Lie subalgebra but not as an associative one. The three base subspaces that survive as subalgebras of some layer are $\mathbb{B}_C$, $\mathbb{B}_H$ and $\mathbb{B}_{\Phi}$, and $\mathbb{B}_{\Phi}$ survives in two layers at once, the Lie layer and the associative layer of the opposite form.

**The distinguished Jordan subalgebras.** The Jordan lattice contains the associative lattice, because a subspace closed under products is closed under $\circ$. It contains more, and the extra elements are the Hermitian spaces. The following table lists the distinguished members.

| Jordan subalgebra | ambient | $\dim_{\mathbb{R}}$ | maximal | witness |
|---|---|---|---|---|
| $H_4(\mathbb{R})$ | $M_4(\mathbb{R})^{+}$ | $10$ | yes | symmetric matrices |
| $\mathbb{R}^4$ | $M_4(\mathbb{R})^{+}$ | $4$ | no | diagonal |
| $H_3(\mathbb{R})\oplus\mathbb{R}$ | $M_4(\mathbb{R})^{+}$ | $7$ | no | $\operatorname{diag}(A,\lambda)$ with $A$ symmetric |
| $M_2(\mathbb{R})^{+}\oplus M_2(\mathbb{R})^{+}$ | $M_4(\mathbb{R})^{+}$ | $8$ | no | two real blocks |
| Borel of $M_4(\mathbb{R})$ | $M_4(\mathbb{R})^{+}$ | $10$ | no | upper triangular |
| parabolic of $M_4(\mathbb{R})$ | $M_4(\mathbb{R})^{+}$ | $12$ | yes | $\{X:X(\pi)\subset\pi\}$ |
| $H_2(\mathbb{H})$ | $M_2(\mathbb{H})^{+}$ | $6$ | yes | quaternionic Hermitian |
| $\mathbb{H}\oplus\mathbb{R}$ | $M_2(\mathbb{H})^{+}$ | $5$ | no | $\operatorname{diag}(q,\lambda)$ |
| $H_4(\mathbb{R})$ | $H_4(\mathbb{C})$ | $10$ | no | real symmetric inside Hermitian |
| $H_2(\mathbb{C})\oplus H_2(\mathbb{C})$ | $H_4(\mathbb{C})$ | $8$ | no | two complex Hermitian blocks |

**The two maximal ones, and their warrant.** $H_4(\mathbb{R})$ is maximal in $M_4(\mathbb{R})^{+}$, and $H_2(\mathbb{H})$ is maximal in $M_2(\mathbb{H})^{+}$. The warrant for both is the same generation test: the Jordan subalgebra generated by the Hermitian space together with one element outside it is the whole algebra. For $H_4(\mathbb{R})$ the dimension jumps from $10$ to $16$ at the first generic element, and for $H_2(\mathbb{H})$ from $6$ to $16$; the computation is a Jordan closure, the span of all iterated symmetrized products of the generators, and it is the analogue of the argument that made $\mathfrak{so}(p,q)$ maximal in the Lie layer. A reader who wants the structural reason: an element outside $H_n(\mathbb{D})$ has a nonzero skew part, and the Jordan products of that skew part with the off-diagonal Hermitian elements sweep out all the missing directions.

**The parabolic Jordan subalgebras.** Every subspace stabilizer is closed under $\circ$, and this is worth a proof because it is the reason the two lattices overlap so much.

**Proposition.** Let $\pi\subset\mathbb{R}^4$ be a subspace and $A_\pi=\{X:X(\pi)\subset\pi\}$. Then $A_\pi$ is closed under $\circ$.

*Proof.* If $X(\pi)\subset\pi$ and $Y(\pi)\subset\pi$ then $XY(\pi)\subset\pi$ and $YX(\pi)\subset\pi$, so their sum does. ∎

The proposition gives the Jordan parabolic of dimension $12$ for a plane and of dimension $13$ for a line, and the Borel of dimension $10$ for a complete flag. None of these is a Hermitian space, and all of them are Jordan subalgebras: the Jordan lattice is the union of two families, the stabilizers of subspaces and the Hermitian spaces with their products, together with their intersections.

**Scope of the Jordan layer.** The article does not attempt a classification of the Jordan subalgebras of the three forms. The reason is the same as in the associative layer, one step worse: the Jordan algebras with a faithful representation in dimension sixteen include the matrix algebras $H_m(\mathbb{D})$ for $m\le4$, their direct sums, the spin factors $J(2,\mathbb{D})$, the parabolics above, and a family of nilpotent-containing algebras that no theorem organises. What the article does claim is the table: the distinguished members, their dimensions, their maximality where the generation test settles it, and the containment $L(\mathbb{B}_{\Psi})\subset H_4(\mathbb{C})$.

## The Relation Between the Element Level and the Operator Level

**The theorem.** The two-sided span of a real form is the split operator algebra, for either real form.

**Theorem (two-sided span).** Let $A_0$ be a real form of $\mathbb{B}$, that is $M_2(\mathbb{R})$ or $\mathbb{H}$. Then

$$
\mathcal{E}(A_0)=\operatorname{span}_{\mathbb{R}}\{T_{\tilde Q,\tilde P}:\tilde Q,\tilde P\in A_0\}\cong A_0\otimes_{\mathbb{R}}A_0^{\mathrm{op}}\cong M_4(\mathbb{R}).
$$

*Proof.* The map $\tilde Q\otimes\tilde P\mapsto T_{\tilde Q,\tilde P}$ is a surjection of $A_0\otimes A_0^{\mathrm{op}}$ onto $\mathcal{E}(A_0)$ by the definition of the span, and it is injective because $\mathbb{B}$ is a faithful $A_0$-bimodule: if $\sum_k\tilde Q_k\tilde X\tilde P_k=0$ for all $\tilde X$ then the corresponding tensor acts as zero on a faithful module, and a tensor acting as zero on a faithful module is zero. So $\mathcal{E}(A_0)\cong A_0\otimes A_0^{\mathrm{op}}$. For $A_0=M_2(\mathbb{R})$ this is $M_2(\mathbb{R})\otimes M_2(\mathbb{R})^{\mathrm{op}}\cong M_4(\mathbb{R})$, by the identification $\mathbb{R}^2\otimes\mathbb{R}^2\cong\mathbb{R}^4$ of carriers. For $A_0=\mathbb{H}$ it is $\mathbb{H}\otimes\mathbb{H}^{\mathrm{op}}\cong\operatorname{End}_{\mathbb{R}}(\mathbb{H})\cong M_4(\mathbb{R})$, by the identification of $\mathbb{H}$ with $\mathbb{R}^4$. ∎

**The non-injectivity.** Both element forms give the *same* operator form, and this is the central structural fact of the article. The passage

$$
\{\text{real forms of }\mathbb{B}\}\longrightarrow\{\text{real forms of }\mathcal{E}_{\mathbb{C}}\},\qquad A_0\longmapsto\mathcal{E}(A_0)
$$

is constant, with value $M_4(\mathbb{R})$. The operator-level classification is therefore strictly coarser than the element-level classification along the two-sided axis, and no information about *which* element form was used survives in the two-sided span. What survives is the pair of subalgebras $L(A_0)$ and $R(A_0)$, of dimension four each, which are different for the two forms:

| element form $A_0$ | $L(A_0)$ | $R(A_0)$ | two-sided span |
|---|---|---|---|
| $M_2(\mathbb{R})$ | $L(M_2(\mathbb{R}))\cong M_2(\mathbb{R})$ | $R(M_2(\mathbb{R}))\cong M_2(\mathbb{R})^{\mathrm{op}}$ | $M_4(\mathbb{R})$ |
| $\mathbb{H}$ | $L(\mathbb{H})\cong\mathbb{H}$ | $R(\mathbb{H})\cong\mathbb{H}^{\mathrm{op}}$ | $M_4(\mathbb{R})$ |

The two images are non-isomorphic subalgebras of $M_4(\mathbb{R})$, of dimensions four each, and they are conjugate to neither each other nor to the entries of the fourth section in a single orbit. The element form is recoverable from the pair $(L(A_0),R(A_0))$ and not from their span.

**The other operator form.** The quaternionic form is not a two-sided span, and the article has already said why. It is the endomorphism ring $\mathcal{E}_{\mathbb{H}}$ of $\mathbb{B}$ as a right $\mathbb{H}$-module, of rank two. In the language of the ninth section it is selected by a module structure on $\mathbb{B}$ and not by a subalgebra of $\mathbb{B}$, and no choice of element form produces it by the two-sided construction. The two constructions are the two halves of the operator-level classification, and they are of different kinds: one is a tensor square, the other is an endomorphism ring.

**What transfers, and what does not.** The map $L$ is an injective algebra homomorphism, so every associative statement about an element subalgebra transfers verbatim to $L$ of it. The bracket satisfies $[L_{\tilde Q},L_{\tilde P}]=L_{[\tilde Q,\tilde P]}$ and the symmetrized product satisfies $L_{\tilde Q}\circ L_{\tilde P}=L_{\tilde Q\circ\tilde P}$, so the Lie and Jordan statements transfer as well. Three things do not transfer.

- **Anything about $R$ alone.** $R$ is an anti-isomorphism, $R_{\tilde Q}R_{\tilde P}=R_{\tilde P\tilde Q}$, so it reverses products and preserves brackets. A subalgebra of $\mathbb{B}$ maps to a subalgebra under $L$ and to the opposite subalgebra under $R$, and the two images agree only when the subalgebra is commutative.
- **Anything about sums.** $L(\mathfrak{a})+R(\mathfrak{b})$ is not isomorphic to $\mathfrak{a}\oplus\mathfrak{b}$: the two images meet in the scalars, so a direct sum loses one dimension. The double centralizer theorem is the theorem about the sum, and it has no element-level statement.
- **Anything about the carrier.** The element level acts on itself; the operator level acts on $\mathcal{E}_{\mathbb{C}}$, a space of dimension sixteen over $\mathbb{R}$. Spectral statements at the element level concern a four-dimensional space and at the operator level a sixteen-dimensional one, and the spectra are different objects. That is the subject of the operator series and not of this article.

**The induced real structures.** The complex algebra $\mathcal{E}_{\mathbb{C}}$ carries the two real structures $\tau_{\mathbb{R}}$ and $\tau_{\mathbb{H}}$ of the second section. Transported along $L$ they become two real structures on $\mathbb{B}$,

$$
\sigma_j=L^{-1}\circ\tau_j\circ L,
$$

and they are the two element-level real structures $\sigma_{\mathrm{split}}$ and $\sigma_{\mathrm{comp}}$ of the element-level article. The fixed sets are $L(M_2(\mathbb{R}))$ and $L(\mathbb{H})$, both four-dimensional, both inside the *same* real form $M_4(\mathbb{R})$ of the operator algebra. That is the precise content of the warning of the third section: the two real structures of the operator algebra restrict to the two real structures of the element algebra, and the two element forms they produce are two subalgebras of one operator form, not two operator forms.

**Warning (the two-sided span is not a fixed set).** It is tempting to think that $\mathcal{E}(A_0)$ is the fixed set of $\tau_{A_0}$. It is not, and the two coincidences and the two failures are worth stating together. The fixed set of $\tau_{\mathbb{R}}$ is $M_4(\mathbb{R})$, and it equals $\mathcal{E}(\mathbb{H})$ and $\mathcal{E}(M_2(\mathbb{R}))$; here the fixed set and the two-sided span agree. The fixed set of $\tau_{\mathbb{H}}$ is $M_2(\mathbb{H})$, and it is neither $\mathcal{E}(\mathbb{H})$ nor $\mathcal{E}(M_2(\mathbb{R}))$; here they differ, and the reason is that a two-sided span is built from products on both sides, while a fixed set is built from a conjugate-linear involution. A two-sided span is a tensor square; a fixed set is an invariant subspace. They coincide only when the real structure is the entrywise conjugation.

## The Lie Groups Attached to the Lie Subalgebras

**The general correspondence, cited.** By the Lie correspondence, stated and proved in [The Lie Correspondence and the Adjoint Representation](the-lie-correspondence-and-the-adjoint-representation.html), every finite-dimensional real Lie algebra has a simply connected Lie group, unique up to isomorphism; every connected Lie group with that algebra is a quotient of that cover by a discrete central subgroup; and the fundamental group of the quotient is that subgroup. This section applies the correspondence to the distinguished subalgebras of the sixth and seventh sections, and the application is the contribution of the article. The general theory is not reproduced.

**The split form.** The table gives, for each distinguished subalgebra, the simply connected group, its centre, the connected quotients, and the fundamental group of each quotient.

| algebra | $\dim$ | simply connected group | centre | connected quotients and $\pi_1$ |
|---|---|---|---|---|
| $\mathfrak{gl}(4,\mathbb{R})$ | $16$ | $\widetilde{SL(4,\mathbb{R})}\times\mathbb{R}$ | $\mathbb{Z}_2^2\times\mathbb{R}$ | $GL^{+}(4,\mathbb{R})\cong SL(4,\mathbb{R})\times\mathbb{R}_{>0}$, $\pi_1=\mathbb{Z}_2$; $GL(4,\mathbb{R})$, $\pi_1=\mathbb{Z}_2$ per component; $SL(4,\mathbb{R})\times S^1$, $\pi_1=\mathbb{Z}_2\oplus\mathbb{Z}$ |
| $\mathfrak{sl}(4,\mathbb{R})$ | $15$ | $\widetilde{SL(4,\mathbb{R})}$ | $\mathbb{Z}_2^2$ | $SL(4,\mathbb{R})$, $\pi_1=\mathbb{Z}_2$; $PSL(4,\mathbb{R})$, $\pi_1=\mathbb{Z}_2^2$; two further double covers of $PSL(4,\mathbb{R})$ |
| $\mathfrak{sp}(2,\mathbb{R})$ | $10$ | $\widetilde{Sp(2,\mathbb{R})}$ | $\mathbb{Z}$ | $Sp(2,\mathbb{R})$, $\pi_1=\mathbb{Z}$; $PSp(2,\mathbb{R})$, $\pi_1=\mathbb{Z}$ |
| $\mathfrak{sl}(3,\mathbb{R})\oplus\mathbb{R}$ | $9$ | $\widetilde{SL(3,\mathbb{R})}\times\mathbb{R}$ | $\mathbb{Z}_2\times\mathbb{R}$ | $SL(3,\mathbb{R})\times\mathbb{R}$, $\pi_1=\mathbb{Z}_2$; $SL(3,\mathbb{R})\times S^1$, $\pi_1=\mathbb{Z}_2\oplus\mathbb{Z}$ |
| $\mathfrak{sl}(2,\mathbb{R})^2\oplus\mathbb{R}$ | $7$ | $\widetilde{SL(2,\mathbb{R})}^2\times\mathbb{R}$ | $\mathbb{Z}^2\times\mathbb{R}$ | $SL(2,\mathbb{R})^2\times\mathbb{R}$, $\pi_1=\mathbb{Z}^2$; $PSL(2,\mathbb{R})^2$, $\pi_1=\mathbb{Z}^2$ |
| $\mathfrak{so}(4)$ | $6$ | $Spin(4)=SU(2)\times SU(2)$ | $\mathbb{Z}_2^2$ | $SO(4)$, $\pi_1=\mathbb{Z}_2$; $SO(3)\times SU(2)$; $SO(3)\times SO(3)$, $\pi_1=\mathbb{Z}_2^2$ |
| $\mathfrak{so}(3,1)$ | $6$ | $SL(2,\mathbb{C})$ | $\mathbb{Z}_2$ | $SL(2,\mathbb{C})$, $\pi_1=0$; $SO^{+}(3,1)$, $\pi_1=\mathbb{Z}_2$ |
| $\mathfrak{so}(2,2)$ | $6$ | $\widetilde{SL(2,\mathbb{R})}^2$ | $\mathbb{Z}^2$ | $SL(2,\mathbb{R})^2$, $\pi_1=\mathbb{Z}^2$; $SO^{+}(2,2)\cong(SL(2,\mathbb{R})\times SL(2,\mathbb{R}))/\{\pm(\mathrm{I},\mathrm{I})\}$, $\pi_1=\mathbb{Z}^2$; $PSL(2,\mathbb{R})^2$, the adjoint group, $\pi_1=\mathbb{Z}^2$ |
| $\mathfrak{u}(2)$ | $4$ | $SU(2)\times\mathbb{R}$ | $\mathbb{Z}_2\times\mathbb{R}$ | $U(2)$, $\pi_1=\mathbb{Z}$; $SU(2)\times S^1$, $\pi_1=\mathbb{Z}$ |
| $\mathfrak{sl}(2,\mathbb{R})$ | $3$ | $\widetilde{SL(2,\mathbb{R})}$ | $\mathbb{Z}$ | $SL(2,\mathbb{R})$, $\pi_1=\mathbb{Z}$; $PSL(2,\mathbb{R})$, $\pi_1=\mathbb{Z}$ |
| $\mathfrak{su}(2)$ | $3$ | $SU(2)$ | $\mathbb{Z}_2$ | $SU(2)$, $\pi_1=0$; $SO(3)$, $\pi_1=\mathbb{Z}_2$ |

Five entries deserve a word, and each is a point where a plausible guess is wrong.

- The centre of $\widetilde{SL(4,\mathbb{R})}$ is $\mathbb{Z}_2^2$ and not $\mathbb{Z}_4$. The computation is a retraction: $SL(4,\mathbb{R})$ deformation-retracts to $SO(4)$, so $\pi_1(SL(4,\mathbb{R}))=\pi_1(SO(4))=\mathbb{Z}_2$; and the centre of the cover is the fundamental group of the adjoint group, $Z(\widetilde{SL(4,\mathbb{R})})=\pi_1(PSL(4,\mathbb{R}))=\pi_1(PSO(4))=\pi_1(SO(3)\times SO(3))=\mathbb{Z}_2^2$. The order $4$ is forced by the two-step covering, and the group is the elementary abelian one because $PSO(4)$ is a product of two circles' worth of rotations.
- $\mathfrak{sl}(4,\mathbb{R})$ therefore has *five* connected groups below its cover: the cover, the group $SL(4,\mathbb{R})$ obtained by killing the subgroup generated by the deck transformation, the adjoint group $PSL(4,\mathbb{R})$ obtained by killing the whole centre, and the two intermediate groups obtained by killing one of the two remaining subgroups of order two. The count is five because $\mathbb{Z}_2^2$ has five subgroups. The element-level article found three groups for $\mathfrak{sl}(2,\mathbb{R})$; the operator level finds five for $\mathfrak{sl}(4,\mathbb{R})$, and the difference is the rank of the centre of the cover.
- $Sp(2,\mathbb{R})$ is not simply connected, although it is the symplectic group. Its fundamental group is $\mathbb{Z}$, because it retracts onto its maximal compact $U(2)$, and the centre of its cover is $\mathbb{Z}$. The pattern is the pattern of $SL(2,\mathbb{R})$: a Hermitian symmetric space of tube type has fundamental group $\mathbb{Z}$ and centre $\mathbb{Z}$ in the cover.
- $\pi_1(GL(4,\mathbb{R}))=\mathbb{Z}_2$ on each of its two components, since $GL(4,\mathbb{R})$ retracts onto $O(4)$ and $SO(4)$ has fundamental group $\mathbb{Z}_2$. The general linear group of a real vector space of dimension at least three is never simply connected.
- $\mathfrak{so}(2,2)$ has cover the product of two covers of $SL(2,\mathbb{R})$ and centre $\mathbb{Z}^2$, so its quotients form a lattice: quotienting by $n\mathbb{Z}\times m\mathbb{Z}$ gives a family of connected groups. The matrix group of the family is the quotient by the *diagonal* $\mathbb{Z}_2$, $SO^{+}(2,2)\cong(SL(2,\mathbb{R})\times SL(2,\mathbb{R}))/\{\pm(\mathrm{I},\mathrm{I})\}$, and it is not $PSL(2,\mathbb{R})^2$: its centre is $\mathbb{Z}_2$, whereas $PSL(2,\mathbb{R})^2$ has trivial centre and is the quotient by the whole centre of the cover, that is the adjoint group. The isomorphism is the one used in [Split-Biquaternion Rotations and the Lorentz Group](split-biquaternion-rotations-and-the-lorentz-group.html).

**The quaternionic form.** The same table for the distinguished subalgebras of the seventh section.

| algebra | $\dim$ | simply connected group | centre | connected quotients and $\pi_1$ |
|---|---|---|---|---|
| $\mathfrak{gl}(2,\mathbb{H})$ | $16$ | $SL(2,\mathbb{H})\times\mathbb{R}$ | $\mathbb{Z}_2\times\mathbb{R}$ | $GL(2,\mathbb{H})\cong SL(2,\mathbb{H})\times\mathbb{R}_{>0}$, $\pi_1=0$; $SL(2,\mathbb{H})\times S^1$, $\pi_1=\mathbb{Z}$ |
| $\mathfrak{sl}(2,\mathbb{H})$ | $15$ | $SL(2,\mathbb{H})$ | $\mathbb{Z}_2$ | $SL(2,\mathbb{H})$, $\pi_1=0$; $PSL(2,\mathbb{H})\cong SO^{+}(5,1)$, $\pi_1=\mathbb{Z}_2$ |
| $\mathfrak{sp}(2)$ | $10$ | $Sp(2)$ | $\mathbb{Z}_2$ | $Sp(2)$, $\pi_1=0$; $PSp(2)\cong SO(5)$, $\pi_1=\mathbb{Z}_2$ |
| $\mathfrak{sp}(1,1)$ | $10$ | $Sp(1,1)\cong Spin(4,1)$ | $\mathbb{Z}_2$ | $Sp(1,1)$, $\pi_1=0$; $SO^{+}(4,1)$, $\pi_1=\mathbb{Z}_2$ |
| $\mathfrak{sl}(1,\mathbb{H})^2\oplus\mathbb{R}$ | $7$ | $SU(2)^2\times\mathbb{R}$ | $\mathbb{Z}_2^2\times\mathbb{R}$ | $(SU(2)^2/\mathbb{Z}_2)\times\mathbb{R}\cong SO(4)\times\mathbb{R}$, $\pi_1=\mathbb{Z}_2$ |

Three entries carry the contrasts with the split form.

- $GL(2,\mathbb{H})$ is **simply connected**, and $SL(2,\mathbb{H})$ is simply connected. Both statements fail for their real counterparts, and the contrast is the cleanest global statement of the whole article: the quaternionic general linear group is a homotopy product of a point-like factor and a circle-free factor, and the real one carries a double cover. The reason is that the maximal compact subgroup of $SL(2,\mathbb{H})$ is $Sp(2)$, which is simply connected, while the maximal compact subgroup of $SL(4,\mathbb{R})$ is $SO(4)$, which is not.
- $SL(2,\mathbb{H})$ double-covers $SO^{+}(5,1)$ and is the spin group of that Lorentzian form: $SL(2,\mathbb{H})\cong Spin(5,1)$. The isomorphism is the quaternionic twin of $SL(2,\mathbb{C})\cong Spin(3,1)$, and the two are the classical isomorphisms $A_3\cong D_3$ and $C_2\cong B_2$ at the group level.
- $Sp(1,1)\cong Spin(4,1)$ and $Sp(2)\cong Spin(5)$ are the two algebras of dimension ten, one non-compact and one compact, and their quotients by the centre are $SO^{+}(4,1)$ and $SO(5)$.

**The covers that matter in geometry.** Three twofold covers appear in the table, and they are the ones the application articles use:

$$
SL(2,\mathbb{C})\longrightarrow SO^{+}(3,1),\qquad
Spin(4)=SU(2)\times SU(2)\longrightarrow SO(4),\qquad
SL(2,\mathbb{H})\longrightarrow SO^{+}(5,1).
$$

The first is the spin cover of the Lorentz group; the second is the double cover of the four-dimensional rotation group, which splits as a product; the third is the quaternionic counterpart of the first. None of the three is visible in the Lie algebra, and each is the choice of a discrete central subgroup of the cover.

**Formulas for the elements.** The exponential map is the matrix exponential in every case, and two formulas are worth recording because they show the difference between the compact and the non-compact directions in one frame. For $X\in\mathfrak{so}(4)$ the exponential is a rotation and is periodic; for $X\in\mathfrak{so}(3,1)$ hyperbolic directions give $\exp(tX)$ with eigenvalues $e^{\pm t}$ and the map is not periodic. The same distinction is the distinction between $\mathfrak{u}(2)$ and $\mathfrak{gl}(2,\mathbb{R})$ inside the operator algebra, and it is the operator-level form of the element-level contrast between the circle and the hyperbola.

**Warning (the algebra does not determine the group).** $\mathfrak{sl}(4,\mathbb{R})$ is the algebra of five connected groups, $\mathfrak{gl}(4,\mathbb{R})$ of infinitely many, and $\mathfrak{sl}(2,\mathbb{H})$ of two. The discrete central subgroup is extra data, invisible to the algebra, and the fundamental group of the group is that subgroup. A statement about the Lie algebra of the operator algebra is therefore a statement about all of these groups at once, and any claim of the form "the group of the algebra is ..." must name the subgroup or the group.

## Comparison of the Two Levels

**The two levels in one table.** The comparison of the element level and the operator level is the conceptual summary of the article.

| invariant | element level, $\mathbb{B}=M_2(\mathbb{C})$ | operator level, $\mathcal{E}_{\mathbb{C}}=M_4(\mathbb{C})$ |
|---|---|---|
| complex dimension | $4$ | $16$ |
| real forms, associative | $2$: $M_2(\mathbb{R})$, $\mathbb{H}$ | $2$: $M_4(\mathbb{R})$, $M_2(\mathbb{H})$ |
| separating invariant | trace inertia $(2,2)$ against $(4,0)$ | trace inertia $(10,6)$ against $(6,10)$ |
| simple part of the Lie algebra | $\mathfrak{sl}(2,\mathbb{R})$, $\mathfrak{su}(2)$ | $\mathfrak{sl}(4,\mathbb{R})$, $\mathfrak{sl}(2,\mathbb{H})$ |
| Killing inertia of the simple part | $(2,1)$ against $(0,3)$ | $(9,6)$ against $(5,10)$ |
| real rank of the simple part | $1$ | $3$ against $1$ |
| Jordan real forms | $M_2(\mathbb{R})^{+}$, $\mathbb{H}^{+}$, $H_2(\mathbb{C})$ | $M_4(\mathbb{R})^{+}$, $M_2(\mathbb{H})^{+}$, $H_4(\mathbb{C})$ |
| semisimple associative types | finite, small | $17$ against $12$ |
| maximal Lie subalgebra | two lines, the compact and the split | nine up to conjugacy: two parabolics and seven reductive |
| two-sided span | — | constant, equal to $M_4(\mathbb{R})$ |

**What the operator level adds.** Three things, and each is a genuinely new phenomenon.

1. **A second construction.** At the element level every subobject is a subalgebra of $\mathbb{B}$. At the operator level one of the two real forms is not reached by subalgebras at all but by a module structure, the right-$\mathbb{H}$-linearity of $\mathcal{E}_{\mathbb{H}}$. The operator level is therefore the first level at which endomorphism rings and tensor squares appear as two different constructions of the same kind of object.
2. **A non-injective passage.** The two-sided span loses the element form, as stated in the ninth section. The element-level classification is finer, and the loss is precisely the loss of the pair $(L(A_0),R(A_0))$ when only its span is retained.
3. **A larger lattice.** The semisimple associative types go from a handful to seventeen and twelve, the Lie maximal subalgebras from two lines to the parabolic and irreducible list, and the Jordan lattice acquires the parabolic stabilizers. No classification of the non-semisimple part exists at either level, and the operator level is where that becomes visible rather than an accident of small dimension.

**The two lattices are not isomorphic.** A lattice is a poset, and an isomorphism of the Lie lattices would carry the ambient algebra to the ambient algebra and therefore the derived algebra to the derived algebra, giving $\mathfrak{sl}(4,\mathbb{R})\cong\mathfrak{sl}(2,\mathbb{H})$. Three negative answers follow, and they are worth stating because each has a different proof.

- $\mathfrak{gl}(2,\mathbb{H})$ contains no copy of $\mathfrak{sl}(4,\mathbb{R})$. A subalgebra of dimension fifteen either contains the centre or supplements it. If it contains the centre it is $\mathbb{R}\mathrm{I}_2\oplus\mathfrak{h}$ with $\mathfrak{h}$ of dimension fourteen inside the simple algebra $\mathfrak{sl}(2,\mathbb{H})$, and a subalgebra of codimension one in a simple algebra is an ideal, so $\mathfrak{h}$ does not exist. If it supplements the centre it is the graph of a linear functional on $\mathfrak{sl}(2,\mathbb{H})$, and the graph is a subalgebra only when the functional vanishes on $[\mathfrak{sl},\mathfrak{sl}]=\mathfrak{sl}$, which forces it to be zero. So the only subalgebra of dimension fifteen is $\mathfrak{sl}(2,\mathbb{H})$ itself.
- $\mathfrak{gl}(4,\mathbb{R})$ contains no copy of $\mathfrak{sl}(2,\mathbb{H})$, by the same argument with the roles exchanged.
- The associative lattices are not isomorphic either, and the shortest proof is the list of types: $M_3(\mathbb{R})\oplus\mathbb{R}$ embeds in $M_4(\mathbb{R})$ and has no embedding in $M_2(\mathbb{H})$, while $\mathbb{H}\oplus\mathbb{H}$ embeds in $M_2(\mathbb{H})$ and has no embedding in $M_4(\mathbb{R})$. The two isomorphism types are witnesses on opposite sides.
- The Jordan lattices are not isomorphic, and the invariant is the number of orthogonal idempotents summing to the identity: four for $M_4(\mathbb{R})^{+}$ and two for $M_2(\mathbb{H})^{+}$. Two Jordan algebras with different degrees are not isomorphic, whatever their dimensions.

**What the element level determines for the operator level.** More than one might expect, and the article has used it throughout. The element-level real structures are the restrictions of the operator-level ones; the element-level Lie subalgebras have operator-level images with the same isomorphism type, $L(\mathbb{B}_V)\cong\mathbb{B}_V\cong\mathfrak{so}(3,\mathbb{C})$, $L(\mathbb{B}_H)\cong\mathbb{H}$, $L(\mathbb{B}_\Phi)\cong\mathfrak{u}(2)$; and the element-level groups are the groups of the scalar-free parts of the images. What the element level does not determine is the quaternionic form, the shape of the operator lattice above dimension four, and the analysis of the carrier.

## What the Operator Real Structure Determines

**Determined.** The following are determined by the operator real structure, that is by the choice of $\tau_{\mathbb{R}}$ or $\tau_{\mathbb{H}}$.

- **The associative form, up to isomorphism.** By the trace-form inertia, and independently by the presence or absence of the chain $M_2(\mathbb{R})\subset M_2(\mathbb{C})$.
- **The Lie algebra, up to isomorphism.** By the Killing inertia, $(9,6)$ against $(5,10)$.
- **The lattice of complex subalgebras that are stable under the real structure.** The base $L(\mathbb{B})$ is stable under both, and its real points in each form are the tables of the third section.
- **The Jordan form, up to isomorphism.** The three Jordan forms are distinguished by whether the trace form is definite and by whether an associative form lies above.

**Not determined.** The following are not determined, and each failure has a witness in the tables.

- **The element form.** Both element forms have the same two-sided span, by the ninth section. No operator invariant distinguishes which element form was used, and the distinction lives in the pair of images $L(A_0)$, $R(A_0)$.
- **The choice of carrier decomposition.** The six subspaces $\mathbb{B}_C,\dots,\mathbb{B}_\Phi$ depend on the choice of the quaternionic structure on $\mathbb{B}$, that is on the identification $\mathbb{B}\cong\mathbb{H}^2$. A different identification gives a different list of six, conjugated by the corresponding element automorphism. The operator invariants are the ones stable under that conjugation, and the six-row tables are therefore tables in a frame.
- **The non-semisimple part of any of the three lattices.** No theorem classifies it, and the article has said so in each layer.
- **The group.** Infinitely many connected groups carry each algebra, by the eleventh section.
- **The analysis of operators.** Spectra, ideals of compact operators, functional calculus and the trace-class structure are not determined by the real structure; they belong to the operator series.

**Warning (the operator form does not determine the element form).** The single most likely error in reading this article is to suppose that the two operator forms correspond to the two element forms. They do not. Both element forms generate the split operator form, and the quaternionic operator form has no element-level ancestor at all. The correspondence is

$$
\{M_2(\mathbb{R}),\mathbb{H}\}\longrightarrow\{M_4(\mathbb{R})\},\qquad
\text{right-}\mathbb{H}\text{-module structure}\longrightarrow M_2(\mathbb{H}),
$$

and the first arrow is constant. The two real forms of the operator algebra are separated by the trace form, which is an invariant of the operator level; the two real forms of the element algebra are separated by the same kind of invariant one level down; and the two classifications are related by the loss of information described in the ninth section.

## Hand-off

**What this article has established.** Four things. The two real forms of the operator algebra, $M_4(\mathbb{R})$ and $M_2(\mathbb{H})$, carry three lattices each — associative, Lie, Jordan — and the lattices are classified at the semisimple level by two dimension criteria, $\sum m_in_id_i=4$ and $\sum n_i\le2$, with seventeen and twelve types. The two forms are separated by the trace form and, in the Lie layer, by the Killing inertia, $(9,6)$ against $(5,10)$. The biquaternion base produces all three real forms of $\mathfrak{so}(3,\mathbb{C})$, two as real points and one as a realification, and it lives entirely in the split operator form. Every connected group with one of the distinguished algebras is a quotient of the simply connected cover by a discrete central subgroup, and the fundamental group is that subgroup.

**What comes next in the operator series.** Three directions, in order of dependence.

- **The complex structures of the operator algebra.** The complexification $\mathcal{E}_{\mathbb{C}}\otimes_{\mathbb{R}}\mathbb{C}\cong M_8(\mathbb{C})$ and the two complex structures $\mathcal{E}_{\mathbb{C}}\otimes1$ and $1\otimes\mathcal{E}_{\mathbb{C}}$ inside it, together with the real forms of $M_8(\mathbb{C})$ that do not come from real forms of $\mathcal{E}_{\mathbb{C}}$. That is the subject of [Classification of the Complex Structures of the Operators of the Biquaternion Algebra](classification-of-the-complex-structures-of-the-operators-of-the-biquaternion-algebra.html).
- **The operator series proper.** The spectrum, the trace, the determinant and the functional calculus of operators in $\mathcal{E}_{\mathbb{C}}$ and $\mathcal{E}_{\mathbb{R}}$, which require the analysis that this article deliberately does not use.
- **The applications.** The action of $SL(2,\mathbb{H})$ on $SO^{+}(5,1)$ and the action of $SL(2,\mathbb{C})$ on $SO^{+}(3,1)$ are computed at the element level in [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), and the present article supplies the group theory that makes those actions well defined.

**What remains at the element level.** The element-level article [Classification of the Real Structures of the Biquaternion Algebra, including Lie Algebras and Lie Groups](classification-of-the-real-structures-of-the-biquaternion-algebra.html) is self-contained, and this article does not replace it. A reader who wants the full lattice of $M_2(\mathbb{R})$ or $\mathbb{H}$ should read that article; a reader who wants the general theory of real forms of a Lie algebra should read [Real Forms of a Complex Lie Algebra](real-forms-of-a-complex-lie-algebra.html) and [Real Forms of a Complex Lie Group and the Cartan Involution](real-forms-of-a-complex-lie-group-and-the-cartan-involution.html).

## Summary

The operator algebra of the biquaternion algebra is $\mathcal{E}_{\mathbb{C}}\cong M_4(\mathbb{C})$, and it has two real forms. The split form $M_4(\mathbb{R})$ has trace inertia $(10,6)$; the quaternionic form $M_2(\mathbb{H})$ has $(6,10)$. The biquaternion base $L(\mathbb{B})$, $R(\mathbb{B})$ is a pair of commuting copies of $M_2(\mathbb{C})$ with a nine-dimensional non-associative, non-Lie complement, and its real points lie in the split form only.

Each form carries three lattices. The associative lattices are classified at the semisimple level: a semisimple algebra embeds in $M_4(\mathbb{R})$ exactly when $\sum m_in_id_i=4$, giving seventeen types, and in $M_2(\mathbb{H})$ exactly when $\sum n_i\le2$, giving twelve. The Lie lattices are separated by the Killing form, of inertia $(9,6)$ on $\mathfrak{sl}(4,\mathbb{R})$ and $(5,10)$ on $\mathfrak{sl}(2,\mathbb{H})\cong\mathfrak{so}(5,1)$; the maximal subalgebras are the parabolics and Levis with $\mathfrak{sp}(2,\mathbb{R})$ and the three real forms of $\mathfrak{so}(4,\mathbb{C})$ in the split case, and the two $C_2$'s with a parabolic in the quaternionic case. The Jordan lattices have three real forms each, including $H_4(\mathbb{C})$ with a positive definite trace form, and contain the associative lattices as a sublattice.

The passage from the element level to the operator level is not injective: both element forms have the same two-sided span $M_4(\mathbb{R})$, and only the pair of images remembers which form was used. The quaternionic operator form is not a two-sided span at all; it is the endomorphism ring of $\mathbb{B}$ as a right $\mathbb{H}$-module.

The Lie groups follow. $\mathfrak{sl}(4,\mathbb{R})$ has five connected groups, $\mathfrak{sl}(2,\mathbb{H})$ has two, and $SL(2,\mathbb{H})$ is simply connected while $SL(4,\mathbb{R})$ is not. The discrete central subgroup of the cover is extra data, invisible to the algebra, and its order is the fundamental group of the quotient.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $M_2(\mathbb{C})$, with base $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| $A_0$ | a real form of $\mathbb{B}$, that is $M_2(\mathbb{R})$ or $\mathbb{H}$ |
| $\mathcal{E}_{\mathbb{C}}$ | $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$ |
| $\mathcal{E}_{\mathbb{R}}$ | the real operators on $\mathbb{B}$, $\cong M_8(\mathbb{R})$ |
| $\mathcal{E}(A_0)$ | the two-sided span of $A_0$, $\cong A_0\otimes A_0^{\mathrm{op}}\cong M_4(\mathbb{R})$ |
| $\mathcal{E}_{\mathbb{H}}$ | the right-$\mathbb{H}$-linear operators, $\cong M_2(\mathbb{H})$ |
| $L_{\tilde Q}$, $R_{\tilde Q}$, $T_{\tilde Q,\tilde P}$ | left, right and two-sided multiplication |
| $\mathfrak{m}$ | the complement of $L(\mathbb{B})+R(\mathbb{B})$, of complex dimension $9$ |
| $\tau_{\mathbb{R}}$, $\tau_{\mathbb{H}}$ | the two real structures of $\mathcal{E}_{\mathbb{C}}$ |
| $\mathbb{B}_C,\mathbb{B}_V,\mathbb{B}_H,\mathbb{B}_{iH},\mathbb{B}_{\Psi},\mathbb{B}_{\Phi}$ | the six element subspaces |
| $H_n(\mathbb{D})$ | Hermitian $n\times n$ matrices over $\mathbb{D}$, as a Jordan algebra |
| $X\circ Y$ | the symmetrized product $\tfrac12(XY+YX)$ |
| $\mathfrak{gl}(n,\mathbb{D})$, $\mathfrak{sl}(n,\mathbb{D})$ | the commutator algebras of $M_n(\mathbb{D})$ and its traceless part |
| $\mathfrak{su}^{*}(4)$ | $\mathfrak{sl}(2,\mathbb{H})$, the quaternionically traceless part |
| $\mathfrak{sp}(2)$, $\mathfrak{sp}(1,1)$ | the compact and the Lorentzian quaternionic unitary algebras of dimension $10$ |
| $\widetilde{G}$ | the simply connected cover of the connected group $G$ |
| $\pi_1(G)$, $Z(G)$ | fundamental group, centre |

## Further Reading

**Real forms and descent.** The general theory of real forms of an algebra, with the Galois-descent formulation used in the second section, is in [Real Forms and the Descent of an Algebra](real-forms-and-the-descent-of-an-algebra.html), [Real Forms of a Complex Lie Algebra](real-forms-of-a-complex-lie-algebra.html) and [Real Forms and the Signature](real-forms-and-the-signature.html). The classification of real forms of a complex Lie group by Cartan involutions is in [Real Forms of a Complex Lie Group and the Cartan Involution](real-forms-of-a-complex-lie-group-and-the-cartan-involution.html).

**Division algebras and matrix algebras.** The theorem that $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ are the only finite-dimensional real division algebras is Frobenius', and the structure theorem for finite-dimensional semisimple algebras is Wedderburn's; both are in any graduate algebra text. For quaternionic linear algebra, including the determinant, the canonical forms, and the module structure used in the fifth section, the standard reference is L. Rodman, *Topics in Quaternion Linear Algebra*, Princeton University Press, 2014.

**Lie algebras and their subalgebras.** The classification of the maximal subalgebras of a simple Lie algebra is E. B. Dynkin, *Semisimple subalgebras of semisimple Lie algebras*, Mat. Sbornik 30 (1952), 349–462. The real forms and the restricted root systems are in A. L. Onishchik and E. B. Vinberg, *Lie Groups and Algebraic Groups*, Springer, 1990, and in S. Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Academic Press, 1978, which is also the reference for the correspondence between symmetric pairs and involutions.

**Jordan algebras.** The structure theory, the formally real algebras, and the exceptional algebra $H_3(\mathbb{O})$ are in N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS Colloquium Publications 39, 1968. The identification of $H_2(\mathbb{H})$ as a Jordan algebra of rank two and the role of the trace form are in the same volume.

**Groups and covers.** The Lie correspondence, the existence of the simply connected cover, and the classification of connected groups with a given algebra by discrete central subgroups are in N. Bourbaki, *Lie Groups and Lie Algebras*, Chapters 1–3 and 9, Springer, and in A. Knapp, *Lie Groups Beyond an Introduction*, 2nd edition, Birkhäuser, 2002, where the fundamental groups of the classical groups are tabulated. The computations of $\pi_1$ by retraction onto a maximal compact subgroup, used throughout the eleventh section, are in Helgason, Chapter VI.
