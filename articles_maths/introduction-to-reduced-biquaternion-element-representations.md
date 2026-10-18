# __Introduction to Reduced Biquaternion Element Representations__

## Introduction

An **element representation** writes the reduced biquaternion $\breve Q=Q_++jQ_-$ as an object of another kind — a quadruple of real numbers, a pair of complex numbers, a pair of idempotent coordinates, a $2\times2$ matrix, a pair of polar data. This article names the representations of the block and fixes the two structural facts that make the block short. The first is that the algebra is **commutative**, **associative** and **unital**, so its multiplication is the general plain product. The second is that it is **semisimple** and a direct product of two copies of $\mathbb{C}$, so **every representation is a direct sum of copies of the two one-dimensional characters** and no irreducible representation has dimension greater than one. That is the exact opposite of the biquaternion case, where the algebra is simple and carries a single irreducible representation, of complex dimension two.

**Conventions.** $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ has basis $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$; a general element is $\breve Q=Q_++jQ_-$ with the two complex coordinates $Q_+=q_++iq'_+$ and $Q_-=q_-+iq'_-$. The idempotents are $\Pi_{\pm}=\tfrac12(1\pm j)$, the **idempotent coordinates** are $Q_{++}=Q_++Q_-$ and $Q_{--}=Q_+-Q_-$, and $\breve Q=Q_{++}\Pi_++Q_{--}\Pi_-$. The multiplication is commutative, it **has zero divisors** — the two idempotent lines — and it is **not a division algebra**. The four general products and the forms $B,N,H,K$ are *The Four Products, Their Forms and Their Algebraic Norms*. The element glyph is $\breve Q$, upper case, with the breve and without a tilde, the reduced algebra having no quaternionic factor.

**Boundaries.** The algebra is *Reduced Biquaternion Space* and *Introduction to the Algebra of the Reduced Biquaternions*; the bases and the linear or antilinear characters are *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$*; the involutions are *The Two Involutions and the Group of Involutions*; the idempotent coordinates and the splitting $\mathbb{C}\oplus\mathbb{C}$ are *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*, and the matrices already written for the algebra are *The Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*. The representations of an element are written in the four articles below: *The Four-Vector Element Representation of the Reduced Biquaternions*, *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions*, *Reduced Biquaternion Other Algebraic Element Representations* and *Reduced Biquaternions Polar Element Representation*; the operators of the four products are *Operators on the Reduced Biquaternions*. The biquaternion counterpart is *Introduction to Biquaternion Element Representations*.

## Representations and Modules

**A representation of the algebra is a homomorphism of $\mathbb{C}$-algebras into an endomorphism algebra, and a module is the same data read as an action.**

**Definition.** A **representation** of $\mathbb{B}_{\mathrm{r}}$ on a complex vector space $V$ is a $\mathbb{C}$-linear map $\rho:\mathbb{B}_{\mathrm{r}}\to\operatorname{End}_{\mathbb{C}}(V)$ with
$$
\rho(\breve Q_{1}\breve Q_{2})=\rho(\breve Q_{1})\rho(\breve Q_{2}),\qquad \rho(1)=\operatorname{id}_{V}.
$$
A **(left) module** is a complex vector space $V$ with a multiplication $\mathbb{B}_{\mathrm{r}}\times V\to V$ that is bilinear and satisfies $1\cdot q=q$ and $(\breve Q_{1}\breve Q_{2})\cdot q=\breve Q_{1}\cdot(\breve Q_{2}\cdot q)$; a representation and a module are the same object, the map $\breve Q\cdot q=\rho(\breve Q)q$ passing from one to the other. A subspace $U\subset V$ is a **submodule** when $\breve Q\cdot U\subset U$ for every $\breve Q$. A module is **simple** when it has exactly two submodules, $0$ and $V$; **semisimple** when it is a direct sum of simple ones. The words **irreducible** and **completely reducible** say the same of a representation.

**Definition (the regular representation).** The **regular representation** is $\rho_{\mathrm{reg}}(\breve Q)=L_{\breve Q}$, where $L_{\breve Q}(\breve Q_{2})=\breve Q \breve Q_{2}$, acting on $\mathbb{B}_{\mathrm{r}}$ itself; the space is complex of dimension two on the basis $1,j$ and real of dimension four on the basis $1,i,j,ij$. The operator $L_{\breve Q}$ is read in coordinates in *Operators on the Reduced Biquaternions*.

**Theorem (the regular representation is faithful).** $L_{\breve Q}=0$ if and only if $\breve Q=0$, so $\rho_{\mathrm{reg}}$ is injective and its image is an algebra isomorphic to $\mathbb{B}_{\mathrm{r}}$,
$$
\rho_{\mathrm{reg}}(\mathbb{B}_{\mathrm{r}})=\{L_{\breve Q}:\breve Q\in\mathbb{B}_{\mathrm{r}}\}\cong\mathbb{B}_{\mathrm{r}},
$$
a commutative two-dimensional subalgebra of $\operatorname{End}_{\mathbb{C}}(\mathbb{B}_{\mathrm{r}})\cong M_{2}(\mathbb{C})$.

*Proof.* $L_{\breve Q}(1)=\breve Q$, so $L_{\breve Q}=0$ forces $\breve Q=0$; and $\rho_{\mathrm{reg}}(\breve Q_{1}\breve Q_{2})=L_{\breve Q_{1}\breve Q_{2}}=L_{\breve Q_{1}}L_{\breve Q_{2}}=\rho_{\mathrm{reg}}(\breve Q_{1})\rho_{\mathrm{reg}}(\breve Q_{2})$ is multiplicativity, because the multiplication is associative. The image is commutative because the multiplication is commutative, $L_{\breve Q_{1}}L_{\breve Q_{2}}=L_{\breve Q_{1}\breve Q_{2}}=L_{\breve Q_{2}\breve Q_{1}}=L_{\breve Q_{2}}L_{\breve Q_{1}}$.

## The Algebra as a Module over Itself, over $\mathbb{C}$ and over $\mathbb{R}$

**The algebra is a free module over itself and over the two base fields, of ranks two over $\mathbb{C}$ and four over $\mathbb{R}$, and the three readings carry the same module.**

**Theorem (the ground fields).** The left regular module is $\mathbb{B}_{\mathrm{r}}$ acting on itself by left multiplication; over $\mathbb{C}$ it is free of rank two on the basis $1,j$, over $\mathbb{R}$ it is free of rank four on the basis $1,i,j,ij$, and as a module over the algebra itself it is free of rank one. Its composition length is two in every reading, with the same two composition factors, the two simple modules $\lambda_+$ and $\lambda_-$.

*Proof.* The ranks are the dimensions of the two bases of *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$*. The chain
$$
0\subset\mathbb{C}\Pi_+\subset\mathbb{B}_{\mathrm{r}}
$$
is a composition series: the submodule $\mathbb{C}\Pi_+$ carries the character $\lambda_+$, and the quotient is isomorphic to $\mathbb{C}\Pi_-$ carrying $\lambda_-$, both simple by §*The Simple Modules and Complete Reducibility*.

**Corollary (the module category).** Every module is a direct sum of copies of the two simple modules; the category of modules is the product of two copies of the category of complex vector spaces, and a module is described by the pair of multiplicities $(m,n)$ of $\lambda_+$ and $\lambda_-$. The regular module is $(1,1)$.

*Proof.* Complete reducibility gives the decomposition; the multiplicity pair is the dimension of the $\lambda_+$-part and of the $\lambda_-$-part, and the module is determined by them because the two simples are non-isomorphic.

## The Simple Modules and Complete Reducibility

**The algebra has exactly two simple modules, both of complex dimension one; every module is a direct sum of copies of them, and the regular representation is their sum with multiplicity one.**

**Definition (the two characters).** For $\breve Q=Q_{++}\Pi_++Q_{--}\Pi_-$ set
$$
\lambda_+(\breve Q)=Q_{++},\qquad \lambda_-(\breve Q)=Q_{--}.
$$
Each is a $\mathbb{C}$-algebra homomorphism into the one-dimensional algebra $\mathbb{C}$, $\lambda_{i}(\breve Q_{1}\breve Q_{2})=\lambda_{i}(\breve Q_{1})\lambda_{i}(\breve Q_{2})$ and $\lambda_{i}(1)=1$, because the idempotent coordinates multiply componentwise.

**Theorem (the simple modules).** Up to isomorphism the algebra has exactly two simple modules, the one-dimensional complex lines read through $\lambda_+$ and through $\lambda_-$; no simple module has dimension greater than one.

*Proof.* Let $V$ be a module and $\Pi_+,\Pi_-$ the two idempotents, $\Pi_++\Pi_-=1$ and $\Pi_+\Pi_-=0$. For $V$ simple, each of $\Pi_+$ and $\Pi_-$ acts as an idempotent operator, and each image $\Pi_+V$, $\Pi_-V$ is a submodule, so each is $0$ or $V$. Both zero is impossible, since $\operatorname{id}_{V}=(\Pi_++\Pi_-)$ would act as $0$. So exactly one acts as the identity and the other as $0$, and $V$ is a module of the one-dimensional algebra $\mathbb{C}$ through the surviving character; over the algebraically closed field $\mathbb{C}$ such a module is one-dimensional. The two choices of surviving character give $\lambda_+$ and $\lambda_-$, and the two are non-isomorphic because $\lambda_+(\Pi_+)=1\neq0=\lambda_-(\Pi_+)$.

**Theorem (complete reducibility).** Every module is a direct sum of copies of $\lambda_+$ and $\lambda_-$; the regular representation is
$$
\rho_{\mathrm{reg}}\cong\lambda_+\oplus\lambda_-,
$$
each character with multiplicity one.

*Proof.* The algebra is the product of the two fields $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$, hence semisimple, and a module over a product of fields splits as the direct sum of its two components, each a complex vector space, that is a direct sum of copies of the corresponding character. On $\mathbb{B}_{\mathrm{r}}$ itself the two lines $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$ are submodules carrying $\lambda_+$ and $\lambda_-$, and they span the two-dimensional space, so each multiplicity is one.

**Corollary (the zero divisors carry the submodules).** The non-zero submodules of the regular module are the two idempotent lines $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$ and the whole space, and the two lines are exactly the minimal ideals of *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*; every element of one line annihilates every element of the other, which is the module statement that the two simple components are mutually annihilating.

*Proof.* The submodules of a direct sum of two non-isomorphic simples are generated by subsets of the summands; here that gives only the four subspaces listed, and the annihilation is $\Pi_+\Pi_-=0$.

## Schur's Lemma and the Intertwiners

**Definition.** For two modules $V$ and $W$ an **intertwiner** is a $\mathbb{C}$-linear map $f:V\to W$ with $f(\breve Q\cdot q)=\breve Q\cdot f(q)$ for every $\breve Q$ and $q$; the space of intertwiners is $\operatorname{Hom}_{\mathbb{B}_{\mathrm{r}}}(V,W)$.

**Theorem (Schur).** If $V$ and $W$ are simple then every non-zero intertwiner is an isomorphism; consequently $\operatorname{End}_{\mathbb{B}_{\mathrm{r}}}(V)=\mathbb{C}\operatorname{id}_{V}$ and $\operatorname{Hom}_{\mathbb{B}_{\mathrm{r}}}(\lambda_+,\lambda_-)=0$.

*Proof.* The kernel and the image of an intertwiner are submodules, so a non-zero one has zero kernel and full image, hence is an isomorphism. An endomorphism of the one-dimensional space $V$ is a scalar; and $\lambda_+\not\cong\lambda_-$, so there is no non-zero map between them.

**Corollary (all endomorphisms are scalars).** Over the algebraically closed field $\mathbb{C}$ the two simple modules are absolutely simple, $\operatorname{End}(\lambda_+)=\operatorname{End}(\lambda_-)=\mathbb{C}$, and the algebra is commutative but **not central**, its centre being the whole of $\mathbb{C}\times\mathbb{C}$. This is the whole of the intertwiner calculus, against the richer calculus of *Introduction to Biquaternion Element Representations*, where the one simple module is two-dimensional and its endomorphism ring is the whole of $M_{2}(\mathbb{C})$.

*Proof.* The centre of $\mathbb{C}\times\mathbb{C}$ is $\mathbb{C}\times\mathbb{C}$, which is larger than $\mathbb{C}$ — so the algebra is commutative but **not central**. The absolute simplicity of the two one-dimensional modules is immediate: an endomorphism of a one-dimensional space is a scalar, and scalar multiplication commutes with the action.

## The List of Representations

**The same element is written in six representations, and the table locates each in the block.**

| representation | the element read as | article |
|---|---|---|
| idempotent coordinates | the pair $(Q_{++},Q_{--})$ of complex numbers, $\breve Q=Q_{++}\Pi_++Q_{--}\Pi_-$ | *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions* |
| four-vector | the real quadruple $(q_+,q'_+,q_-,q'_-)$ and the complex pair $(Q_+,Q_-)$ | *The Four-Vector Element Representation of the Reduced Biquaternions* |
| matrix | the $2\times2$ matrix of $L_{\breve Q}$, complex or real | *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions* |
| other algebraic | the Clifford and quotient presentations, the block array | *Reduced Biquaternion Other Algebraic Element Representations* |
| polar | the two polar complex forms of $Q_{++}$ and of $Q_{--}$ | *Reduced Biquaternions Polar Element Representation* |
| operator | the multiplication operator $L_{\breve Q}$ and its companions | *Operators on the Reduced Biquaternions* |

**The idempotent coordinates are the universal representation.** Every other reading is the pair $(Q_{++},Q_{--})$ written in another alphabet: the four-vector splits each of $Q_{++}$ and $Q_{--}$ into two reals, the matrix puts them on the diagonal, the other algebraic representations formalise the isomorphism $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\times\mathbb{C}$, the polar writes each in polar form, and the operator representation is the regular representation of the same pair. A statement is written in the representation that makes it shortest, and the **two characters $\lambda_+,\lambda_-$ are the two coordinates of the universal one**.

## The Representations of the Unit Group

**The units are $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$, an abelian group all of whose irreducible complex representations are one-dimensional.**

**Theorem.** $U=Q_{++}\Pi_++Q_{--}\Pi_-$ is a unit if and only if $\langle U\rangle_{\natural}=Q_{++}Q_{--}\neq0$, that is $Q_{++}\neq0$ and $Q_{--}\neq0$; the unit group is
$$
\mathbb{B}_{\mathrm{r}}^{\times}\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times}\cong (S^{1}\times S^{1})\times(\mathbb{R}_{>0}\times\mathbb{R}_{>0}),
$$
connected and abelian.

*Proof.* The criterion is that of *Norm and Invertibility in the Algebra of the Reduced Biquaternions*, and the decomposition $\mathbb{C}^{\times}\cong S^{1}\times\mathbb{R}_{>0}$ by modulus and argument gives the display; a product of connected sets is connected and abelian.

**Corollary (the characters).** The irreducible complex representations of the unit group are the one-dimensional characters
$$
\chi_{m,n}(U)=Q_{++}^{m}Q_{--}^{n},\qquad (m,n)\in\mathbb{Z}^{2},
$$
extending the two characters of the algebra; the full group of continuous characters is the larger family
$$
U\mapsto Q_{++}^{m}|Q_{++}|^{it}Q_{--}^{n}|Q_{--}|^{is},\qquad (m,n)\in\mathbb{Z}^{2},\ (t,s)\in\mathbb{R}^{2},
$$
with character group $\mathbb{Z}^{2}\times\mathbb{R}^{2}$. The group is **abelian**, so every irreducible representation is one-dimensional; there is no representation of dimension greater than one, against the non-abelian unit group of the biquaternion algebra and its higher-dimensional representations.

*Proof.* An abelian group has only one-dimensional irreducible complex representations, by Schur's lemma. The characters $\chi_{m,n}$ are the holomorphic ones, the two integers being the exponents on the two factors; adjoining the two real exponents of the moduli gives the continuous character group, because the continuous characters of $\mathbb{C}^{\times}$ are $z\mapsto z^{m}|z|^{it}$.

## The Relation to the Split Biquaternions and to the Biquaternions

**The reduced biquaternions are the commutative member of the semisimple family; the split biquaternions are its non-commutative member and the biquaternions the simple member.**

The three algebras are the three ways of splitting a quaternionic algebra over $\mathbb{R}$: the biquaternions $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ are simple, the split biquaternions $\mathbb{H}_{\mathbb{D}}=\mathbb{H}\oplus\mathbb{H}$ are a product of two quaternion division algebras, and the reduced biquaternions $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ are a product of two complex fields, commutative.

| algebra | structure | simple modules | division ring of a simple | unit group | regular representation |
|---|---|---|---|---|---|
| $\mathbb{B}_{\mathrm{r}}$ | $\mathbb{C}\times\mathbb{C}$, commutative | two, of complex dimension one | $\mathbb{C}$ | $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ | complex dimension two |
| $\mathbb{H}_{\mathbb{D}}$ | $\mathbb{H}\oplus\mathbb{H}$, non-commutative | two, of real dimension four | $\mathbb{H}$ | $\mathbb{H}^{\times}\times\mathbb{H}^{\times}$ | real dimension eight |
| $\mathbb{B}$ | $M_{2}(\mathbb{C})$, simple | one, of complex dimension two | $\mathbb{C}$ | essentially $GL_{2}(\mathbb{C})$ | complex dimension four |

**Theorem (the passage).** The passage from the split biquaternions to the reduced biquaternions is the replacement of the division ring $\mathbb{H}$ by the field $\mathbb{C}$ in the two factors, together with the commutativity that this forces; the passage from the biquaternions to the reduced biquaternions is the splitting of the single simple module into the two characters.

*Proof.* The idempotent decomposition writes each of the two semisimple algebras as a product of two factors; the factors are $\mathbb{H}$ and $\mathbb{H}$ for the split biquaternions and $\mathbb{C}$ and $\mathbb{C}$ for the reduced ones, the latter thus commutative; and the biquaternion algebra, being simple, has a single simple module, whose splitting into two characters is the reduction. The structures of the companions are *Split-Biquaternion Element Representation Theory* and *Introduction to Biquaternion Element Representations*.

**Corollary (the smallest simples).** The reduced algebra has the smallest simple modules of the three, of complex dimension one over the commutative base; its representation theory is therefore the product of two copies of the representation theory of $\mathbb{C}$, the simplest member of the family. All three algebras are semisimple, the reduced and the split biquaternion by being products, the biquaternion by being a full matrix algebra; none of the three needs the theory of modules over a non-semisimple ring.

*Proof.* The two product cases are semisimple as products of division algebras, and the matrix algebra is semisimple by Wedderburn; the simples of the reduced algebra are one-dimensional because each factor is a field, and a module over a field is a vector space.

## Summary

The reduced biquaternion algebra is commutative, associative and unital, and it is the direct product of two copies of $\mathbb{C}$; its representation theory is therefore the simplest of the corpus. A representation is a module; the regular representation $\breve Q\mapsto L_{\breve Q}$ is faithful with image $\{L_{\breve Q}\}\cong\mathbb{B}_{\mathrm{r}}$; the simple modules are exactly the two characters $\lambda_+(Q_{++}\Pi_++Q_{--}\Pi_-)=Q_{++}$ and $\lambda_-(Q_{++}\Pi_++Q_{--}\Pi_-)=Q_{--}$, of complex dimension one, and every module is a direct sum of copies of them. The regular representation is $\lambda_+\oplus\lambda_-$, each with multiplicity one, its non-zero submodules are the two idempotent lines, and those two lines are the minimal ideals and the zero divisors. Schur's lemma gives $\operatorname{End}(\lambda_{i})=\mathbb{C}$ and no intertwiner between $\lambda_+$ and $\lambda_-$. The element is written in the six representations of the table, the idempotent coordinates being the universal one and the two characters its two coordinates. The unit group is $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$, abelian and connected, with the one-dimensional characters $\chi_{m,n}$ and no higher-dimensional irreducible representation; the multiplication has zero divisors and is not a division algebra. As a module over itself the algebra has composition length two, with the same two simple factors in the readings over $\mathbb{C}$ of rank two and over $\mathbb{R}$ of rank four, and the comparison of the three algebras places it as the commutative member of the semisimple family, against the non-commutative split biquaternions $\mathbb{H}\oplus\mathbb{H}$ and the simple biquaternions $M_{2}(\mathbb{C})$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho$, $V$ | a representation and its module |
| $L_{\breve Q}$, $\rho_{\mathrm{reg}}$ | left multiplication by $\breve Q$; the regular representation |
| $\lambda_+,\lambda_-$ | the two characters, $\lambda_+(Q_{++}\Pi_++Q_{--}\Pi_-)=Q_{++}$, $\lambda_-=Q_{--}$ |
| $\operatorname{Hom}_{\mathbb{B}_{\mathrm{r}}}(V,W)$ | the intertwiners between two modules |
| $\mathbb{B}_{\mathrm{r}}^{\times}$ | the unit group, $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ |
| $\chi_{m,n}(U)=Q_{++}^{m}Q_{--}^{n}$ | the holomorphic characters of the unit group |

## Further Reading

- *Reduced Biquaternion Space* (`articles_maths/reduced-biquaternion-space.md`), for the multiplication and the isomorphism $\mathbb{C}\oplus\mathbb{C}$.
- *Introduction to the Algebra of the Reduced Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the algebra read as an algebra.
- *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the idempotent coordinates and the minimal ideals.
- *The Group of Units of the Algebra of the Reduced Biquaternions* (`articles_maths/the-group-of-units-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the unit group and its complement.
- *Operators on the Reduced Biquaternions* (`articles_maths/operators-on-the-reduced-biquaternions.md`), for the multiplication operators of the four products.
- *Introduction to Biquaternion Element Representations* (`articles_maths/introduction-to-biquaternion-element-representations.md`), for the non-commutative companion and the one simple module of dimension two.
- *Split-Biquaternion Element Representation Theory* (`articles_maths/split-biquaternion-element-representation-theory.md`), for the non-commutative semisimple companion with its two four-dimensional simple modules.
