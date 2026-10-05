# __The Regular Module and the Regular Bimodule over the Biquaternion Algebra__

## Introduction

The biquaternion algebra acts on its own additive group by its multiplication. Read on the left the action makes $\mathbb{B}$ a module over itself, the **left regular module** ${}_{\mathbb{B}}\mathbb{B}$; read on the right it makes the **right regular module** $\mathbb{B}_{\mathbb{B}}$; read on both sides at once it makes the **regular bimodule** ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$, whose two actions commute. The regular object is at once the smallest module the algebra has and the universal one: its submodules are the ideals, it is cyclic on the unit, faithful, free of rank one, a generator, and the identity of the tensor product, and its endomorphism ring recovers the algebra, its opposite or its centre according to which of the two actions is kept.

Over the biquaternion algebra these facts take a sharp form, because $\mathbb{B}\cong M_2(\mathbb{C})$ is a simple, semisimple, Artinian ring with centre $\mathbb{C}$. The bimodule ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ is **simple**, its only sub-bimodules being $0$ and $\mathbb{B}$; the left regular module is the direct sum of two copies of the simple module $S\cong\mathbb{C}^2$, hence completely reducible; the three endomorphism rings are $\mathbb{B}$, $\mathbb{B}^{\mathrm{op}}$ and $\mathbb{C}$; and the algebra is von Neumann regular and self-injective, both inherited from the matrix algebra.

The article assumes the general theory in Linear Spaces: *The Regular Module and the Regular Bimodule* for the three regular objects, the correspondence with the ideals, the four properties and the endomorphism ring, *The Balanced Product* for the tensor product and its universal property, and *Modules* and *Direct Sums, Free Modules and Rank* for submodules, free modules and rank. For the algebra it assumes *Biquaternions as a Vector Space over $\mathbb{C}$* for $\mathbb{B}$ and its centre, *Modules over the Biquaternion Algebra* for the simple module $S$, the standard bimodule ${}_{\mathbb{B}}S_{\mathbb{C}}$ and the Morita equivalence with $\mathbb{C}$, and *Biquaternion Ideals and Peirce Decomposition* together with *Biquaternion Idempotents and Projections* for the ideals, the primitive idempotents, the minimal left ideals and the Peirce decomposition; the classification of the ideals is cited and not repeated. The left and the right regular representations as $4\times4$ matrices are *Biquaternion 4×4 Regular Matrix Element Representation*, and the involution that the regular module carries, its twist and its canonical form are *The Canonical Hermitian Form on the Regular Module of the Biquaternion Algebra*. No form, no norm and no topology is used.

Throughout, $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra with complex basis $e_0,e_1,e_2,e_3$ and centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, a generic element is $\tilde Q$, an idempotent is $\tilde\Pi$, and the two one-sided multiplications are

$$
L_{\tilde Q}(\tilde R)=\tilde Q\tilde R,\qquad R_{\tilde Q}(\tilde R)=\tilde R\tilde Q .
$$

## The Three Regular Modules

### The left regular module

**Definition.** The **left regular module** ${}_{\mathbb{B}}\mathbb{B}$ is the additive group $(\mathbb{B},+)$ with the scalar multiplication

$$
\mathbb{B}\times\mathbb{B}\longrightarrow\mathbb{B},\qquad (\tilde Q,\tilde R)\mapsto \tilde Q\tilde R ,
$$

the multiplication of the algebra itself.

**Proposition (the module axioms are the ring axioms).** ${}_{\mathbb{B}}\mathbb{B}$ is a left $\mathbb{B}$-module. The four module axioms are the two distributive laws, the associativity and the unit law of $\mathbb{B}$, each read as a module axiom, and the derived identities $0\tilde R=0$ and $(-\tilde Q)\tilde R=-(\tilde Q\tilde R)$ hold because they already hold in $\mathbb{B}$. In particular $\mathbb{B}$ is a left $\mathbb{B}$-module of complex dimension four, and the same carrier with the same multiplication is a left module over $\mathbb{B}$, not a new object built from it.

**Proof.** The distributivity of the action in the scalar and in the vector is the two distributive laws of $\mathbb{B}$, the compatibility $(\tilde P\tilde Q)\tilde R=\tilde P(\tilde Q\tilde R)$ is the associativity, and $e_0\tilde R=\tilde R$ is the unit law. The derived identities are the elementary properties of *Modules*.

### The right regular module

**Definition.** The **right regular module** $\mathbb{B}_{\mathbb{B}}$ is $(\mathbb{B},+)$ with the right scalar multiplication $(\tilde R,\tilde Q)\mapsto \tilde R\tilde Q$, which is the same multiplication read on the right.

### The regular bimodule

**Definition.** The left action and the right action of $\mathbb{B}$ on $(\mathbb{B},+)$, taken together, make it a **bimodule** ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$. The two actions commute,

$$
\tilde A(\tilde R\tilde B)=(\tilde A\tilde R)\tilde B \qquad (\tilde A,\tilde B,\tilde R\in\mathbb{B}),
$$

which is the associativity of $\mathbb{B}$ once more: the two scalar multiplications of the bimodule are the two readings of one product.

**Remark (why the regular module is the reference object).** Every left ideal of $\mathbb{B}$ is a submodule of ${}_{\mathbb{B}}\mathbb{B}$ and every element of $\mathbb{B}$ is a scalar of the module, so the algebra and its module are cut from the same multiplication. This is why the module theory of $\mathbb{B}$ can be read off from the single object ${}_{\mathbb{B}}\mathbb{B}$ and its two one-sided twins, and why the left ideal theory of *Biquaternion Ideals and Peirce Decomposition* is simultaneously the submodule theory of the regular module.

## The Submodules Are the Ideals

**Theorem.** Let $L\subseteq\mathbb{B}$ be an additive subgroup. Then $L$ is a submodule of ${}_{\mathbb{B}}\mathbb{B}$ if and only if $L$ is a left ideal of $\mathbb{B}$; $L$ is a submodule of $\mathbb{B}_{\mathbb{B}}$ if and only if $L$ is a right ideal; and $L$ is a sub-bimodule of ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ if and only if $L$ is a two-sided ideal.

**Proof.** A submodule of ${}_{\mathbb{B}}\mathbb{B}$ is an additive subgroup closed under $\tilde Q\tilde R$ for all $\tilde Q\in\mathbb{B}$ and $\tilde R\in L$, and that is the definition of a left ideal. The scalar action of ${}_{\mathbb{B}}\mathbb{B}$ is by construction the multiplication of $\mathbb{B}$, so the two conditions are the same formula and not two equivalent ones. The right-handed statement is the same argument with the multiplication read on the right, and the two-sided statement applies both readings at once.

**Corollary (the lattice of ideals is the lattice of submodules).** The identity map on subsets of $\mathbb{B}$ is an isomorphism of the lattice of submodules of ${}_{\mathbb{B}}\mathbb{B}$ onto the lattice of left ideals of $\mathbb{B}$, preserving inclusion, intersection and sum; likewise for the right ideals and for the two-sided ideals of the bimodule.

**Remark (the biquaternion content).** Because $\mathbb{B}$ is simple, the two-sided ideals are only $0$ and $\mathbb{B}$, so the regular bimodule has no nontrivial sub-bimodule; this is the bimodule reading of the simplicity proved in *Biquaternion Ideals and Peirce Decomposition*. The left ideals are the left ideals of the algebra, classified there as the Peirce subspaces and the minimal left ideals $\mathbb{B}\tilde\Pi$ generated by the primitive idempotents of *Biquaternion Idempotents and Projections*; the theorem above says that the same list is the complete list of submodules of the left regular module.

## The Four Properties of the Regular Object

### Cyclic and faithful

**Proposition.** ${}_{\mathbb{B}}\mathbb{B}$ is **cyclic**, generated by the unit: ${}_{\mathbb{B}}\mathbb{B}=\mathbb{B}e_0$, since $\tilde R=\tilde R e_0$. It is **faithful**: its annihilator

$$
\operatorname{Ann}({}_{\mathbb{B}}\mathbb{B})=\{\tilde Q:\tilde Q\tilde R=0 \text{ for all } \tilde R\in\mathbb{B}\}
$$

is zero, since $\tilde Q e_0=\tilde Q$.

**Proof.** The two statements are the computations $\tilde R=\tilde R e_0$ and $\tilde Q e_0=0\Rightarrow \tilde Q=0$. The same two computations with the multiplication read on the right give the cyclicity and the faithfulness of $\mathbb{B}_{\mathbb{B}}$ and of the bimodule.

### Free of rank one

**Proposition.** ${}_{\mathbb{B}}\mathbb{B}$ is **free of rank one**, with basis $\{e_0\}$: the expansion $\tilde R=\tilde R e_0$ is unique, because a linear combination of the single basis element $e_0$ with coefficient $\tilde R$ is $\tilde R e_0$ and determines $\tilde R$. Hence ${}_{\mathbb{B}}\mathbb{B}$ is finitely generated, projective and free of rank one, and the same holds for $\mathbb{B}_{\mathbb{B}}$ and for ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$.

**Proof.** Generation is $\tilde R=\tilde R e_0$; linear independence of $\{e_0\}$ is $\tilde R e_0=0\Rightarrow\tilde R=0$. A module with a basis is free and therefore projective, by *Projective and Injective Modules*.

### A generator

**Definition.** A left $\mathbb{B}$-module $G$ is a **generator** if every left $\mathbb{B}$-module is a quotient of a direct sum $G^{(I)}$ of copies of $G$.

**Proposition.** ${}_{\mathbb{B}}\mathbb{B}$ is a generator. Every left $\mathbb{B}$-module is a quotient of a direct sum of copies of the regular module, so the regular module is the single test object of the module category.

**Proof.** By *Modules* every module $M$ is a quotient of a free module, $M\cong F/\ker\varphi$ with $F$ free; by the universal property of a basis $F$ is a direct sum of copies of ${}_{\mathbb{B}}\mathbb{B}$. The quotient map is $\varphi$. In the biquaternion case the statement is also read through the Morita equivalence of *Modules over the Biquaternion Algebra*: a $\mathbb{B}$-module is $S\otimes_{\mathbb{C}}W$ for a complex vector space $W$, and it is a quotient of copies of $S\otimes_{\mathbb{C}}\mathbb{C}^n$, that is of copies of ${}_{\mathbb{B}}\mathbb{B}$.

### The identity of the tensor product

**Proposition.** For a right $\mathbb{B}$-module $M$ and a left $\mathbb{B}$-module $N$ there are natural isomorphisms

$$
M\otimes_{\mathbb{B}}{}_{\mathbb{B}}\mathbb{B}\cong M,\qquad {}_{\mathbb{B}}\mathbb{B}\otimes_{\mathbb{B}}N\cong N ,
$$

given by $\tilde m\otimes\tilde Q\mapsto \tilde m\tilde Q$ and $\tilde Q\otimes\tilde n\mapsto \tilde Q\tilde n$. For bimodules the same elements are the two-sided identity, ${}_{S}M_{\mathbb{B}}\otimes_{\mathbb{B}}{}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}\cong{}_{S}M_{\mathbb{B}}$ and ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}\otimes_{\mathbb{B}}{}_{\mathbb{B}}N_{T}\cong{}_{\mathbb{B}}N_{T}$, naturally in the outer module.

**Proof.** The map $\tilde m\otimes\tilde Q\mapsto\tilde m\tilde Q$ is well defined because the assignment is $\mathbb{B}$-balanced: it is additive in each variable, and $(\tilde m\tilde A)\otimes\tilde B$ and $\tilde m\otimes(\tilde A\tilde B)$ both go to $\tilde m(\tilde A\tilde B)=(\tilde m\tilde A)\tilde B$. Its inverse is $\tilde m\mapsto\tilde m\otimes e_0$, and uniqueness is the universal property of *The Balanced Product*. The left-handed statement is the mirror, and the bimodule statements follow by carrying the outer actions through both maps.

**Remark (the categorical reading).** The isomorphisms above say that ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ is the unit of the tensor product of bimodules: tensoring a bimodule with the regular bimodule on either side returns it. This is the module-level form of the fact that the tensor product is a monoidal structure whose unit is the base object, and its categorical statement belongs to the general theory of module categories.

## The Endomorphisms of the Regular Object

### The one-sided endomorphisms

**Proposition.** There are ring isomorphisms

$$
\operatorname{End}_{\mathbb{B}}(\mathbb{B}_{\mathbb{B}})\cong\mathbb{B},\qquad \operatorname{End}_{\mathbb{B}}({}_{\mathbb{B}}\mathbb{B})\cong\mathbb{B}^{\mathrm{op}},
$$

the first given by the left multiplications $\tilde Q\mapsto L_{\tilde Q}$ and the second by the right multiplications $\tilde Q\mapsto R_{\tilde Q}$.

**Proof.** Let $T:\mathbb{B}_{\mathbb{B}}\to\mathbb{B}_{\mathbb{B}}$ be right $\mathbb{B}$-linear, $T(\tilde R\tilde Q)=T(\tilde R)\tilde Q$. With $\tilde R=e_0$ one has $T(\tilde Q)=T(e_0)\tilde Q=L_{T(e_0)}(\tilde Q)$, so $T=L_{\tilde B}$ with $\tilde B=T(e_0)$; conversely $L_{\tilde B}(\tilde R\tilde Q)=\tilde B(\tilde R\tilde Q)=(\tilde B\tilde R)\tilde Q=L_{\tilde B}(\tilde R)\tilde Q$, so $L_{\tilde B}$ is right $\mathbb{B}$-linear. The assignment $\tilde B\mapsto L_{\tilde B}$ is additive and satisfies $L_{\tilde B\tilde C}=L_{\tilde B}L_{\tilde C}$, hence is a ring isomorphism onto $\operatorname{End}_{\mathbb{B}}(\mathbb{B}_{\mathbb{B}})$, injective because $L_{\tilde B}(e_0)=\tilde B$. The left-module case is the mirror: a left $\mathbb{B}$-linear $T$ has $T(\tilde R)=T(\tilde R e_0)=\tilde R T(e_0)=R_{T(e_0)}(\tilde R)$, and $\tilde B\mapsto R_{\tilde B}$ is additive with $R_{\tilde B\tilde C}=R_{\tilde C}R_{\tilde B}$, hence a ring isomorphism $\mathbb{B}^{\mathrm{op}}\to\operatorname{End}_{\mathbb{B}}({}_{\mathbb{B}}\mathbb{B})$.

**Corollary (the operator reading).** The endomorphism ring of the regular module is the algebra itself, read on the same side for the representation and on the opposite side for the anti-representation: the left multiplications reproduce $\mathbb{B}$ as the endomorphisms of the right regular module, the right multiplications reproduce $\mathbb{B}^{\mathrm{op}}$ as the endomorphisms of the left regular module. In the matrix model this is the double centraliser of *Biquaternion 4×4 Regular Matrix Element Representation*, where the reproducing copy is written $\rho_R(\mathbb{B})=\operatorname{End}_{\mathbb{B}}(\mathbb{B})$ and the two copies are shown to generate $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$.

### The bimodule endomorphisms are the centre

**Proposition.** $\operatorname{End}_{\mathbb{B}\text{-}\mathbb{B}}(\mathbb{B})\cong Z(\mathbb{B})$, the centre of $\mathbb{B}$, the isomorphism sending a central $\tilde S$ to $L_{\tilde S}=R_{\tilde S}$. In particular

$$
\operatorname{End}_{\mathbb{B}\text{-}\mathbb{B}}(\mathbb{B})\cong\mathbb{C}e_0\cong\mathbb{C},
$$

of complex dimension one.

**Proof.** A $\mathbb{B}$-$\mathbb{B}$-linear $T$ is in particular right $\mathbb{B}$-linear, so $T=L_{\tilde B}$, and in particular left $\mathbb{B}$-linear, so $T=R_{\tilde C}$; then $L_{\tilde B}=R_{\tilde C}$ gives $\tilde B\tilde R=\tilde R\tilde C$ for all $\tilde R$, and with $\tilde R=e_0$ one gets $\tilde B=\tilde C$ and then $\tilde B\tilde R=\tilde R\tilde B$ for all $\tilde R$, so $\tilde B$ is central. Conversely a central $\tilde B$ has $L_{\tilde B}=R_{\tilde B}$ and this map is a bimodule endomorphism. The centre is $\mathbb{C}e_0$ by *Biquaternions as a Vector Space over $\mathbb{C}$*.

**Corollary (no nontrivial bimodule endomorphisms).** The regular bimodule has no nontrivial endomorphism exactly when the centre reduces to the scalars, which is the case here: a sub-bimodule of ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ is a two-sided ideal, the only ones are $0$ and $\mathbb{B}$, and the endomorphism ring that acts on it is the line of central scalars $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$. This is the precise sense in which the biquaternion algebra is a central simple algebra over $\mathbb{C}$.

## The Biquaternion Case

### Simple and semisimple

**Proposition.** The algebra $\mathbb{B}$ is simple as a ring: its only two-sided ideals are $0$ and $\mathbb{B}$. Consequently the regular bimodule ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ is simple as a bimodule, and the algebra is Artinian and semisimple.

**Proof.** The simplicity is *Biquaternion Ideals and Peirce Decomposition*, read through the theorem above as the absence of sub-bimodules between $0$ and ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$. Semisimplicity and the descending chain condition follow because $\mathbb{B}\cong M_2(\mathbb{C})$ is a matrix algebra over a field, and these are the Wedderburn–Artin properties of *Simple and Semisimple Modules*.

### The left regular module is $S\oplus S$

**Theorem.** There is a simple left $\mathbb{B}$-module $S$, of complex dimension two, with

$$
{}_{\mathbb{B}}\mathbb{B}\cong S\oplus S,\qquad \operatorname{End}_{\mathbb{B}}(S)=\mathbb{C},\qquad S\cong\mathbb{C}^2 .
$$

The decomposition is produced by the orthogonal idempotents $\tilde\Pi_1=\tfrac12(e_0+ie_3)$ and $\tilde\Pi_2=\tfrac12(e_0-ie_3)$, which satisfy $\tilde\Pi_1+\tilde\Pi_2=e_0$ and $\tilde\Pi_1\tilde\Pi_2=0$, by ${}_{\mathbb{B}}\mathbb{B}=\mathbb{B}\tilde\Pi_1\oplus\mathbb{B}\tilde\Pi_2$ with $\mathbb{B}\tilde\Pi_j\cong S$.

**Proof.** The idempotents, the Peirce decomposition and the minimality of the ideals $\mathbb{B}\tilde\Pi_j$ are *Biquaternion Ideals and Peirce Decomposition*; the two minimal left ideals are isomorphic because the algebra is simple, and $S$ is their isomorphism class, the unique simple left module of *Modules over the Biquaternion Algebra*, of complex dimension two. That $\operatorname{End}_\mathbb{B}(S)=\mathbb{C}$ is Schur's lemma, recorded there; in the matrix model $S$ is the column space $\mathbb{C}^2$ of $M_2(\mathbb{C})$.

**Corollary (complete reducibility).** Every left $\mathbb{B}$-module is semisimple: it is a direct sum of copies of $S$, and by the Morita equivalence of *Modules over the Biquaternion Algebra* it is $S\otimes_\mathbb{C}W$ for a complex vector space $W$, of complex dimension $2\dim_\mathbb{C}W$. The regular module is the particular case $W=\mathbb{C}^2$.

**Remark (the minimal left ideals and the lines of $S$).** The minimal left ideals of $\mathbb{B}$ are the two-dimensional subspaces

$$
L_\ell=\{\tilde R:\tilde R S\subseteq\ell\},\qquad \ell \text{ a line in } S,
$$

one for each line $\ell$, so the family of minimal left ideals is a projective line; the two summands of the decomposition above correspond to the two coordinate lines, and the general element of the family is $\mathbb{B}\tilde\Pi$ for a rank-one idempotent $\tilde\Pi$ with image $\ell$. The classification is that of *Biquaternion Ideals and Peirce Decomposition*, and the theorem above adds only the reading that these are the simple submodules of the regular module.

### Von Neumann regular and self-injective

**Proposition.** The algebra $\mathbb{B}$ is von Neumann regular: for every $\tilde Q\in\mathbb{B}$ there is a $\tilde B\in\mathbb{B}$ with $\tilde Q\tilde B\tilde Q=\tilde Q$. It is self-injective: as a left module over itself it is injective, so every $\mathbb{B}$-linear map from a submodule of ${}_{\mathbb{B}}\mathbb{B}$ to ${}_{\mathbb{B}}\mathbb{B}$ extends to ${}_{\mathbb{B}}\mathbb{B}$.

**Proof.** Both properties are properties of the algebra $\mathbb{B}\cong M_2(\mathbb{C})$: it is von Neumann regular, and it is self-injective because it is a Frobenius algebra, the trace providing the non-degenerate associative pairing. Both are preserved by isomorphism, and the injectivity statement is the Baer criterion applied to ${}_{\mathbb{B}}\mathbb{B}$.

**Corollary (the regular module is projective and injective).** The left regular module is free and therefore projective, and it is injective by the proposition; the two properties together mean that ${}_{\mathbb{B}}\mathbb{B}$ is a projective generator and an injective cogenerator of the module category, the reference object from which every module is built by direct sums, quotients and submodules.

## Worked Verification

The regular module of the biquaternion algebra is small enough that the general statements can be checked by hand. In the complex basis $e_0,e_1,e_2,e_3$ the following hold.

| Item | Value | Where |
|---|---|---|
| ${}_{\mathbb{B}}\mathbb{B}$ | free of rank one, basis $\{e_0\}$ | §*Free of rank one* |
| $\mathbb{B}\tilde\Pi_1$, $\mathbb{B}\tilde\Pi_2$ | minimal left ideals, complex dimension $2$, $\mathbb{B}\tilde\Pi_1\cap\mathbb{B}\tilde\Pi_2=0$ | §*The left regular module is $S\oplus S$* |
| ${}_{\mathbb{B}}\mathbb{B}$ | $\cong S\oplus S$, $\dim_\mathbb{C}S=2$ | §*The left regular module is $S\oplus S$* |
| $\operatorname{End}_{\mathbb{B}}(\mathbb{B}_{\mathbb{B}})$ | $\cong\mathbb{B}$, complex dimension $4$ | §*The one-sided endomorphisms* |
| $\operatorname{End}_{\mathbb{B}}({}_{\mathbb{B}}\mathbb{B})$ | $\cong\mathbb{B}^{\mathrm{op}}$, complex dimension $4$ | §*The one-sided endomorphisms* |
| $\operatorname{End}_{\mathbb{B}\text{-}\mathbb{B}}(\mathbb{B})$ | $\cong\mathbb{C}e_0$, complex dimension $1$ | §*The bimodule endomorphisms are the centre* |
| two-sided ideals | $0$ and $\mathbb{B}$ only | §*Simple and semisimple* |

The two idempotents $\tilde\Pi_1,\tilde\Pi_2$ are orthogonal and sum to the unit; the left ideals they generate are each of complex dimension two and meet only in $0$, so that ${}_{\mathbb{B}}\mathbb{B}=\mathbb{B}\tilde\Pi_1\oplus\mathbb{B}\tilde\Pi_2$ is a direct sum of two simple modules. The right multiplications give a copy of $\mathbb{B}^{\mathrm{op}}$ in $\operatorname{End}_\mathbb{C}(\mathbb{B})$ whose commutant is the image of the left multiplications, the double centraliser statement of *Biquaternion 4×4 Regular Matrix Element Representation*; the only operators that are simultaneously a left and a right multiplication are the multiplications by the central scalars, and they are the bimodule endomorphisms of complex dimension one.

## Summary

The biquaternion algebra acts on its own additive group by multiplication, giving the left regular module ${}_{\mathbb{B}}\mathbb{B}$, the right regular module $\mathbb{B}_{\mathbb{B}}$, and the regular bimodule ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ whose two actions commute. The submodules of the three objects are exactly the left, the right and the two-sided ideals, so the lattice of ideals of *Biquaternion Ideals and Peirce Decomposition* is the lattice of submodules of the regular object. The regular module is cyclic on the unit, faithful, free of rank one, a generator, and the identity of the tensor product, $M\otimes_{\mathbb{B}}{}_{\mathbb{B}}\mathbb{B}\cong M$ and ${}_{\mathbb{B}}\mathbb{B}\otimes_{\mathbb{B}}N\cong N$; every module is a quotient of a direct sum of copies of it. Its endomorphism rings are $\operatorname{End}_{\mathbb{B}}(\mathbb{B}_{\mathbb{B}})\cong\mathbb{B}$, $\operatorname{End}_{\mathbb{B}}({}_{\mathbb{B}}\mathbb{B})\cong\mathbb{B}^{\mathrm{op}}$ and $\operatorname{End}_{\mathbb{B}\text{-}\mathbb{B}}(\mathbb{B})\cong Z(\mathbb{B})=\mathbb{C}e_0\cong\mathbb{C}$. Because $\mathbb{B}$ is simple, semisimple and Artinian, the bimodule is simple, the left regular module is $S\oplus S$ with $S\cong\mathbb{C}^2$ the unique simple module, every module is semisimple, and the algebra is von Neumann regular and self-injective; the regular module is therefore a projective generator and an injective cogenerator, the module from which the whole module theory is read.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| ${}_{\mathbb{B}}\mathbb{B}$ | the left regular module, $(\mathbb{B},+)$ with $\tilde Q\cdot\tilde R=\tilde Q\tilde R$ |
| $\mathbb{B}_{\mathbb{B}}$ | the right regular module, $(\mathbb{B},+)$ with $\tilde R\cdot\tilde Q=\tilde R\tilde Q$ |
| ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ | the regular bimodule, the two commuting actions |
| $L\subseteq\mathbb{B}$ submodule of ${}_{\mathbb{B}}\mathbb{B}$ | left ideal of $\mathbb{B}$ |
| $L\subseteq\mathbb{B}$ submodule of $\mathbb{B}_{\mathbb{B}}$ | right ideal of $\mathbb{B}$ |
| $L\subseteq\mathbb{B}$ sub-bimodule of ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ | two-sided ideal of $\mathbb{B}$ |
| ${}_{\mathbb{B}}\mathbb{B}=\mathbb{B}e_0$, $\operatorname{Ann}({}_{\mathbb{B}}\mathbb{B})=0$ | cyclic on the unit, faithful |
| $\{e_0\}$ | the basis, of rank one |
| $M\otimes_{\mathbb{B}}{}_{\mathbb{B}}\mathbb{B}\cong M$, ${}_{\mathbb{B}}\mathbb{B}\otimes_{\mathbb{B}}N\cong N$ | the regular bimodule is the tensor unit |
| $\operatorname{End}_{\mathbb{B}}(\mathbb{B}_{\mathbb{B}})\cong\mathbb{B}$ | the left multiplications |
| $\operatorname{End}_{\mathbb{B}}({}_{\mathbb{B}}\mathbb{B})\cong\mathbb{B}^{\mathrm{op}}$ | the right multiplications |
| $\operatorname{End}_{\mathbb{B}\text{-}\mathbb{B}}(\mathbb{B})\cong Z(\mathbb{B})=\mathbb{C}e_0$ | the bimodule endomorphisms |
| $S$ | the unique simple left module, $S\cong\mathbb{C}^2$ |
| ${}_{\mathbb{B}}\mathbb{B}\cong S\oplus S$ | complete reducibility of the regular module |
| $\tilde\Pi_1,\tilde\Pi_2$ | the orthogonal idempotents of the splitting, $\mathbb{B}\tilde\Pi_j\cong S$ |
| von Neumann regular, self-injective | $\tilde Q\tilde B\tilde Q=\tilde Q$; injectivity of ${}_{\mathbb{B}}\mathbb{B}$ |

## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for the regular module, its generator property and the endomorphism ring of a module.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the regular module and the correspondence between submodules and ideals.
- Tsit-Yuen Lam, *Lectures on Modules and Rings* (Springer, 1999), for the regular module, its projectivity and the centre as the bimodule endomorphism ring.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the matrix algebra $M_2(\mathbb{C})$, its minimal left ideals and its idempotents.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for the tensor unit and the generator property.
