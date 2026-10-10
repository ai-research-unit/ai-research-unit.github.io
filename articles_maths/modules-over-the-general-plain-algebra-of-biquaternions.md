# __Modules over the General Plain Algebra of Biquaternions__


## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is isomorphic to the full matrix algebra $M_2(\mathbb{C})$, and this one fact settles both its action on itself and its module theory. A module over a general ring is an intractable object; a module over $\mathbb{B}$ is a direct sum of copies of a single two-dimensional module $S=\mathbb{C}^2$, and the category of modules is the linear algebra of $\mathbb{C}$ with every dimension doubled. The algebra acting on its own additive group by its multiplication gives the **regular module**, the object cut from the same multiplication as the algebra: its submodules are the ideals, it is cyclic on the unit, faithful, free of rank one, a generator and the identity of the tensor product, and its endomorphism ring recovers the algebra, its opposite or its centre according to which of the two actions is kept. This article develops both in the concrete case of $\mathbb{B}$: the three regular objects and their four properties, the defining module, the classification of modules, the parity that decides freeness, the endomorphism algebras, the Morita equivalence with $\mathbb{C}$, the degeneration of torsion, and the descent to the real form. The regular object is at once the smallest module the algebra has and the universal one.

The general theory is used, not repeated. The definitions and the isomorphism theorems are those of *Modules over an Algebra*, the simple and semisimple theory is *Simple and Semisimple Modules*, the Morita theorem is *Morita Equivalence*, the balanced product is *The Balanced Product over an Algebra*, and base change is *Change of Rings*. The general theory of the regular object is *The Regular Module and the Regular Bimodule* for the three regular objects, the correspondence with the ideals, the four properties and the endomorphism ring, with *The Balanced Product* for the tensor product and its universal property, and *Modules* and *Direct Sums, Free Modules and Rank* for submodules, free modules and rank. The quaternionic side of the comparison is *Quaternion Ideals and Simplicity*, which owns the module theory over the division ring, and the companion ring-based reading of the same additive group is *Biquaternions as a Bimodule over $\mathbb{H}$*. What is added here is the module theory of the system $\mathbb{B}$ itself. The algebra conventions are those of *Biquaternions as a Vector Space over $\mathbb{C}$*: the basis $e_0,e_1,e_2,e_3$ with $e_0=1$, $e_k^2=-e_0$ and $e_1e_2=e_3$; the central imaginary $i$ with $i^2=-1$; the idempotents $\tilde\Pi_1=\tfrac12(e_0+ie_3)$, $\tilde\Pi_2=\tfrac12(e_0-ie_3)$ and the matrix units $\tilde R=\tfrac12(ie_1-e_2)$, $\tilde T=\tfrac12(ie_1+e_2)$, with the Peirce decomposition, as in *Biquaternion Idempotents and Projections* and *Biquaternion Ideals and Peirce Decomposition*.

A generic element is $\tilde Q$, an idempotent is $\tilde\Pi$, and the two one-sided multiplications are

$$
L_{\tilde Q}(\tilde R)=\tilde Q\tilde R,\qquad R_{\tilde Q}(\tilde R)=\tilde R\tilde Q .
$$

Two ownership notes fix the boundaries of the article. The norm $N(\tilde Q)=\tilde Q\tilde{Q}^{\natural}$, its vanishing, the invertibility criterion $N(\tilde Q)\neq0$, the group of units $\mathbb{B}^\times$ and the zero divisors are the content of *Biquaternion Norm and Invertibility* and are cited here rather than restated; they are used only in the one place where they bear on the module category, the degeneration of torsion. The group-theoretic side — Schur's lemma for group representations, the defining representation and the half-spin representations, the Clebsch–Gordan rule — is *Biquaternion Rotations and Lorentz Transformations*; this article is about the modules, and it does not carry the group theory.

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

**Proof.** By *Modules* every module $M$ is a quotient of a free module, $M\cong F/\ker\varphi$ with $F$ free; by the universal property of a basis $F$ is a direct sum of copies of ${}_{\mathbb{B}}\mathbb{B}$. The quotient map is $\varphi$. In the biquaternion case the statement is also read through the Morita equivalence of §*Morita Equivalence with the Complex Field*: a $\mathbb{B}$-module is $S\otimes_{\mathbb{C}}W$ for a complex vector space $W$, and it is a quotient of copies of $S\otimes_{\mathbb{C}}\mathbb{C}^n$, that is of copies of ${}_{\mathbb{B}}\mathbb{B}$.

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

**Corollary (the operator reading).** The endomorphism ring of the regular module is the algebra itself, read on the same side for the representation and on the opposite side for the anti-representation: the left multiplications reproduce $\mathbb{B}$ as the endomorphisms of the right regular module, the right multiplications reproduce $\mathbb{B}^{\mathrm{op}}$ as the endomorphisms of the left regular module. In the matrix model this is the double centraliser of *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$*, where the reproducing copy is written $\operatorname{mat}_4^{R}(\mathbb{B})=\operatorname{End}_{\mathbb{B}}(\mathbb{B})$ and the two copies are shown to generate $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$.

### The bimodule endomorphisms are the centre

**Proposition.** $\operatorname{End}_{\mathbb{B}\text{-}\mathbb{B}}(\mathbb{B})\cong Z(\mathbb{B})$, the centre of $\mathbb{B}$, the isomorphism sending a central $\tilde S$ to $L_{\tilde S}=R_{\tilde S}$. In particular

$$
\operatorname{End}_{\mathbb{B}\text{-}\mathbb{B}}(\mathbb{B})\cong\mathbb{C}e_0\cong\mathbb{C},
$$

of complex dimension one.

**Proof.** A $\mathbb{B}$-$\mathbb{B}$-linear $T$ is in particular right $\mathbb{B}$-linear, so $T=L_{\tilde B}$, and in particular left $\mathbb{B}$-linear, so $T=R_{\tilde C}$; then $L_{\tilde B}=R_{\tilde C}$ gives $\tilde B\tilde R=\tilde R\tilde C$ for all $\tilde R$, and with $\tilde R=e_0$ one gets $\tilde B=\tilde C$ and then $\tilde B\tilde R=\tilde R\tilde B$ for all $\tilde R$, so $\tilde B$ is central. Conversely a central $\tilde B$ has $L_{\tilde B}=R_{\tilde B}$ and this map is a bimodule endomorphism. The centre is $\mathbb{C}e_0$ by *Biquaternions as a Vector Space over $\mathbb{C}$*.

**Corollary (no nontrivial bimodule endomorphisms).** The regular bimodule has no nontrivial endomorphism exactly when the centre reduces to the scalars, which is the case here: a sub-bimodule of ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ is a two-sided ideal, the only ones are $0$ and $\mathbb{B}$, and the endomorphism ring that acts on it is the line of central scalars $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$. This is the precise sense in which the biquaternion algebra is a central simple algebra over $\mathbb{C}$.

## The Defining Module

Two orthogonal idempotents generate the two columns of the algebra. With $\tilde\Pi_2=e_0-\tilde\Pi_1$ one has

$$
\tilde\Pi_1^2=\tilde\Pi_1,\qquad \tilde\Pi_2^2=\tilde\Pi_2,\qquad \tilde\Pi_1\tilde\Pi_2=\tilde\Pi_2\tilde\Pi_1=0,\qquad \tilde\Pi_1+\tilde\Pi_2=e_0,
$$

and the four Peirce corners of $\mathbb{B}$ with respect to the pair are

$$
\tilde\Pi_1\mathbb{B}\tilde\Pi_1=\mathbb{C}\tilde\Pi_1,\qquad \tilde\Pi_1\mathbb{B}\tilde\Pi_2=\mathbb{C}\tilde R,\qquad \tilde\Pi_2\mathbb{B}\tilde\Pi_1=\mathbb{C}\tilde T,\qquad \tilde\Pi_2\mathbb{B}\tilde\Pi_2=\mathbb{C}\tilde\Pi_2,
$$

each of complex dimension one. The minimal left ideal generated by $\tilde\Pi_1$ is therefore

$$
S:=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\,\tilde T\},
$$

of complex dimension two, the **defining module** of $\mathbb{B}$. The second column $\mathbb{B}\tilde\Pi_2=\mathbb{C}\{\tilde\Pi_2,\,\tilde R\}$ is a second minimal left ideal, isomorphic to the first.

The left action of $\mathbb{B}$ on $S$ is computed on the basis $(\tilde\Pi_1,\tilde T)$. Multiplication by the idempotent fixes $\tilde\Pi_1$ and kills $\tilde T$, while multiplication by the off-diagonal elements interchanges the two: $\tilde R\tilde\Pi_1=0$, $\tilde T\tilde\Pi_1=\tilde T$, $\tilde R \tilde T=\tilde\Pi_1$ and $\tilde T^2=0$. The action makes $S$ the defining two-dimensional module of $\mathbb{B}$. Nothing in this paragraph depends on the choice of idempotent: all minimal left ideals of $\mathbb{B}$ are isomorphic, and they are indexed by the projective line $\mathbb{P}^1(\mathbb{C})$, as in *Biquaternion Ideals and Peirce Decomposition*.

**Theorem.** $S$ is a simple left $\mathbb{B}$-module, and up to isomorphism it is the only one.

*Proof.* For $s\neq0$ the left ideal $\mathbb{B}s$ is nonzero, and $\mathbb{B}$ being simple artinian it is all of $S$; so $S$ has no nonzero proper submodule. For uniqueness, $\mathbb{B}$ is a simple artinian ring with a single isotypic component, and such a ring has exactly one simple module up to isomorphism; see *Simple and Semisimple Modules* and *Representations of Algebras*.

## The Category of Left Modules

The classification of modules over $\mathbb{B}$ is complete and has no exceptional cases.

**Theorem.** Let $M$ be a left $\mathbb{B}$-module. Then $M$ is a direct sum of copies of $S$,

$$
M\cong S^{\oplus k},
$$

with $k$ an integer when $M$ is finitely generated. Every $\mathbb{B}$-module is projective. The left regular module is free of rank one over $\mathbb{B}$ and decomposes as

$$
{}_\mathbb{B}\mathbb{B}\cong S\oplus S,
$$

the two summands being the two columns $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}\tilde\Pi_2$.

*Proof.* The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is simple and artinian, hence semisimple; over a semisimple ring every module is a direct sum of simple modules, every module is projective, and there is a single simple module up to isomorphism. The decomposition of the regular module is the Peirce decomposition read column by column, and freeness of rank one is the basis $e_0$.

For a finite-dimensional $\mathbb{B}$-module the invariant $k$ is recovered from the dimension: since $\dim_\mathbb{C}S=2$,

$$
\dim_\mathbb{C}S^{\oplus k}=2k,
$$

so a finite-dimensional module is a direct sum of $k$ copies of $S$. The module category of $\mathbb{B}$ is thus the category of finite-dimensional complex vector spaces carrying that action; what the biquaternion structure adds over the bare complex field is exactly the action through $S$, and nothing else.

**A caution on tensor products.** For a non-commutative algebra the tensor product of two left $\mathbb{B}$-modules is not naturally a left $\mathbb{B}$-module: the two actions compete on the shared algebra, and only a diagonal action survives. The tensor-product ring structure therefore belongs to the group-theoretic side, where the representations are those of the group of units; the module classification above uses direct sums only.

## Projectivity and the Parity of Freeness

Over a field projectivity and freeness coincide, and the same holds over the quaternion division algebra. Over the matrix algebra they part, and the divergence is the whole of the departure of $\mathbb{B}$ from a field.

**Proposition.** The module $S^{\oplus k}$ is free if and only if $k$ is even, equivalently if and only if its complex dimension $2k$ is divisible by $4$:

$$
S^{\oplus k}\text{ is free}\iff 2\mid k\iff 4\mid\dim_\mathbb{C}S^{\oplus k}.
$$

*Proof.* Since $\mathbb{B}\cong S\oplus S$ as left modules, $\mathbb{B}^{\oplus m}\cong S^{\oplus 2m}$; the free modules are therefore exactly the modules $S^{\oplus k}$ with $k$ even. The dimension statement is $\dim_\mathbb{C}S^{\oplus k}=2k$.

In particular $S$ itself is projective — every module is — but not free, and it is the minimal example: a two-dimensional complex module with no basis over $\mathbb{B}$. The obstruction to freeness is a parity, and the obstruction reappears unchanged as the obstruction to a real structure (§*Real Structures*). This is the sharpest contrast with the module theory over the division ring $\mathbb{H}$, where every module is free; the quaternionic side of the comparison is treated in *Quaternion Ideals and Simplicity*.

## Endomorphisms and the Standard Bimodule

The morphisms are as simple as the objects. Because $S$ is simple, Schur's lemma gives

$$
\operatorname{End}_\mathbb{B}(S)=\mathbb{C},
$$

the scalars acting by the complex structure. A $\mathbb{B}$-linear map $S^{\oplus m}\to S^{\oplus n}$ is determined by the images of the $m$ summands, each of which is an $n$-tuple of endomorphisms of $S$, so

$$
\operatorname{Hom}_\mathbb{B}\bigl(S^{\oplus m},S^{\oplus n}\bigr)\cong M_{n\times m}(\mathbb{C}),\qquad \operatorname{End}_\mathbb{B}\bigl(S^{\oplus k}\bigr)\cong M_k(\mathbb{C}),
$$

with composition the matrix product; the automorphisms of $S^{\oplus k}$ are therefore the group $\mathrm{GL}_k(\mathbb{C})$. The double centralizer statement is the mirror of these computations: the scalars commute with $\mathbb{B}$ and nothing else does,

$$
\operatorname{End}_\mathbb{C}(S)=\mathbb{B},\qquad \{b\in\mathbb{B}: bs=sb\text{ for all }s\in S\}=\mathbb{C}.
$$

The module $S$ is consequently a bimodule over the pair $(\mathbb{B},\mathbb{C})$. The left action is the algebra action, the right action is multiplication by the central scalars, and the two commute because $\mathbb{C}$ is the centre of $\mathbb{B}$; this is the structure denoted ${}_\mathbb{B}S_\mathbb{C}$. The left and right actions are genuinely different data — the left action is the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, while the right action is scalar multiplication and has kernel only at $0$ — and it is their compatibility, not either alone, that makes $S$ the standard bimodule of the Morita theory.

**The opposite algebra.** The **opposite algebra** $A^{\mathrm{op}}$ of an algebra $A$ has the same additive group and the reversed product, $a^{\mathrm{op}}\cdot b^{\mathrm{op}}=(ba)^{\mathrm{op}}$; the construction in general is *Opposite Algebras and Anti-Isomorphisms*. For $\mathbb{B}$ the quaternion conjugation is an anti-automorphism, $(\tilde P\tilde Q)^{\natural}=\tilde Q^{\natural}\tilde P^{\natural}$, hence an isomorphism $\mathbb{B}^{\mathrm{op}}\to\mathbb{B}$: the opposite of the biquaternion algebra is the algebra itself.

The dual is not a new module. Let $S^*=\operatorname{Hom}_\mathbb{C}(S,\mathbb{C})$ carry the contragredient action, a right $\mathbb{B}$-module and hence a left $\mathbb{B}^{\mathrm{op}}$-module; under that identification $S^*$ is simple of complex dimension two and therefore isomorphic to $S$.

## Morita Equivalence with the Complex Field

The pair $(\mathbb{B},\mathbb{C})$ is a Morita pair, and the equivalence is implemented by $S$.

**Theorem.** The functor

$$
\operatorname{Hom}_\mathbb{B}(S,-):\operatorname{Mod}(\mathbb{B})\longrightarrow\operatorname{Mod}(\mathbb{C})
$$

is an equivalence of categories, with inverse $W\mapsto S\otimes_\mathbb{C}W\cong S^{\oplus\dim_\mathbb{C}W}$. On the module $S^{\oplus k}$ it returns $\mathbb{C}^k$:

$$
\operatorname{Hom}_\mathbb{B}\bigl(S,S^{\oplus k}\bigr)\cong\mathbb{C}^k.
$$

*Proof.* This is the Morita equivalence of *Morita Equivalence* with $A=\mathbb{B}$, $B=\mathbb{C}$ and the equivalence bimodule ${}_\mathbb{B}S_\mathbb{C}$ of the previous section. The module $S$ is a projective generator, $\operatorname{End}_\mathbb{B}(S)=\mathbb{C}$ and $\operatorname{End}_\mathbb{C}(S)=\mathbb{B}$, and the balanced product of the two sections recovers the algebra, $S\otimes_\mathbb{C}S^*\cong\mathbb{B}$ as a $(\mathbb{B},\mathbb{B})$-bimodule.

The consequence is stated once and used throughout: the module theory of the biquaternion algebra is the linear algebra of the complex field, and the passage to $\mathbb{B}$ doubles every dimension,

$$
\dim_{\mathbb{C}}\bigl(S\otimes_\mathbb{C}W\bigr)=2\dim_\mathbb{C}W.
$$

Every statement that can be made about $\mathbb{B}$-modules is a statement about complex vector spaces read through $S$; the algebra $\mathbb{B}$ itself is recovered as $\operatorname{End}_\mathbb{C}(S)$, so the module determines the algebra, and the two are two faces of one equivalence.

## Torsion

The naive notion of torsion does not survive the passage from a commutative domain to $\mathbb{B}$, and it is worth recording why, since the failure is a feature of the module category rather than a defect.

Recall that over a commutative domain a nonzero module element $m$ is torsion when $\operatorname{Ann}(m)\neq0$, an invariant that classifies finitely generated modules over a principal ideal domain (*Modules over a PID*). Over $\mathbb{B}$ the definition collapses. The algebra has zero divisors — this is the vanishing of the norm, treated in *Biquaternion Zero Divisors* and *Biquaternion Norm and Invertibility* — and for every nonzero $s\in S$ the annihilator

$$
\operatorname{Ann}_\mathbb{B}(s)=\{b\in\mathbb{B}:bs=0\}
$$

is a nonzero proper left ideal, since $s$ spans a submodule isomorphic to $S$ and the kernel of $b\mapsto bs$ is a maximal left ideal of $\mathbb{B}$. Under the naive definition every nonzero element of $S$ would be torsion, and in $S^{\oplus k}$ the torsion elements would be those with proportional nonzero components; the annihilator of two linearly independent vectors of $\mathbb{C}^2$ in $M_2(\mathbb{C})$ is zero, so those elements are not closed under addition and form no submodule.

The remedy is to test against non-zero-divisors. An element $a$ of a ring $A$ is **regular** if $ab=0$ implies $b=0$ and $ba=0$ implies $b=0$, and a module element $m$ is **torsion** if $\operatorname{Ann}(m)$ contains a regular element; over a commutative domain this reduces to the classical definition.

**Proposition.** Every module over a semisimple ring is torsion-free. In particular $\operatorname{Mod}(\mathbb{B})$ contains no torsion.

*Proof.* In a semisimple ring every regular element is a unit: if $a$ is regular then $Aa$ is a nonzero left ideal and has a complement $I$ with $A=Aa\oplus I$, and regularity forces $I=0$, since $0\neq b\in I$ would give $ab\in Aa\cap I=0$ with $b\neq0$; so $Aa=A$ and $a$ has a right inverse, and symmetrically a left inverse. If $a$ is regular and $am=0$ then $m=a^{-1}am=0$, so no annihilator contains a regular element.

Torsion therefore classifies nothing over $\mathbb{B}$: the structure theory is the direct-sum decomposition of §*The Category of Left Modules* and the parity of §*Projectivity and the Parity of Freeness*, not a torsion submodule. The same vanishing holds over the division algebra $\mathbb{H}$, so the invariant that governs modules over a principal ideal domain has no analogue in either system.

## Real Structures

The module category of $\mathbb{B}$ is the complex linear algebra of $S$, but $\mathbb{B}$ is a complexification, and the modules that come from the real algebra $\mathbb{H}$ form a distinguished subclass.

A **real structure** on a $\mathbb{B}$-module $W$ is an $\mathbb{H}$-module $V$ together with an isomorphism $W\cong\mathbb{C}\otimes_{\mathbb{R}}V$, that is, $W$ is obtained from a quaternionic module by extension of scalars. Since every $\mathbb{H}$-module is free, every complexification is a free $\mathbb{B}$-module, and conversely every free $\mathbb{B}$-module is a complexification; hence

$$
W\text{ admits a real structure}\iff W\text{ is a free }\mathbb{B}\text{-module},
$$

which for $W=S^{\oplus k}$ holds exactly when $k$ is even. The obstruction to descending to $\mathbb{H}$ is therefore the same parity that obstructs freeness, and $S$ is the minimal counterexample: it is defined over $\mathbb{C}$ and over $\mathbb{R}$, but not over $\mathbb{H}$. The two functors are complexification and restriction, $\mathbb{C}\otimes_{\mathbb{R}}-$ and $\operatorname{Res}^{\mathbb{B}}_{\mathbb{H}}$, carrying $\mathbb{H}^n$ to $\mathbb{B}^n\cong S^{\oplus 2n}$ and $S^{\oplus k}$ to $\mathbb{H}^k$, and they form an adjoint pair in the sense of *Change of Rings*, with composite that doubles the number of copies of $S$. The detail of the quaternionic side is in *Quaternion Ideals and Simplicity*.

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

**Proof.** The idempotents, the Peirce decomposition and the minimality of the ideals $\mathbb{B}\tilde\Pi_j$ are *Biquaternion Ideals and Peirce Decomposition*; the two minimal left ideals are isomorphic because the algebra is simple, and $S$ is their isomorphism class, the unique simple left module of §*The Defining Module*, of complex dimension two. That $\operatorname{End}_\mathbb{B}(S)=\mathbb{C}$ is Schur's lemma, recorded there; in the matrix model $S$ is the column space $\mathbb{C}^2$ of $M_2(\mathbb{C})$.

**Corollary (complete reducibility).** Every left $\mathbb{B}$-module is semisimple: it is a direct sum of copies of $S$, and by the Morita equivalence of §*Morita Equivalence with the Complex Field* it is $S\otimes_\mathbb{C}W$ for a complex vector space $W$, of complex dimension $2\dim_\mathbb{C}W$. The regular module is the particular case $W=\mathbb{C}^2$.

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

The two idempotents $\tilde\Pi_1,\tilde\Pi_2$ are orthogonal and sum to the unit; the left ideals they generate are each of complex dimension two and meet only in $0$, so that ${}_{\mathbb{B}}\mathbb{B}=\mathbb{B}\tilde\Pi_1\oplus\mathbb{B}\tilde\Pi_2$ is a direct sum of two simple modules. The right multiplications give a copy of $\mathbb{B}^{\mathrm{op}}$ in $\operatorname{End}_\mathbb{C}(\mathbb{B})$ whose commutant is the image of the left multiplications, the double centraliser statement of *Biquaternion 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$*; the only operators that are simultaneously a left and a right multiplication are the multiplications by the central scalars, and they are the bimodule endomorphisms of complex dimension one.


## Summary

The biquaternion algebra acts on its own additive group by its multiplication, giving the left regular module ${}_{\mathbb{B}}\mathbb{B}$, the right regular module $\mathbb{B}_{\mathbb{B}}$, and the regular bimodule ${}_{\mathbb{B}}\mathbb{B}_{\mathbb{B}}$ whose two actions commute. The submodules of the three objects are exactly the left, the right and the two-sided ideals, so the lattice of ideals of *Biquaternion Ideals and Peirce Decomposition* is the lattice of submodules of the regular object. The regular module is cyclic on the unit, faithful, free of rank one, a generator, and the identity of the tensor product, $M\otimes_{\mathbb{B}}{}_{\mathbb{B}}\mathbb{B}\cong M$ and ${}_{\mathbb{B}}\mathbb{B}\otimes_{\mathbb{B}}N\cong N$; every module is a quotient of a direct sum of copies of it. Its endomorphism rings are $\operatorname{End}_{\mathbb{B}}(\mathbb{B}_{\mathbb{B}})\cong\mathbb{B}$, $\operatorname{End}_{\mathbb{B}}({}_{\mathbb{B}}\mathbb{B})\cong\mathbb{B}^{\mathrm{op}}$ and $\operatorname{End}_{\mathbb{B}\text{-}\mathbb{B}}(\mathbb{B})\cong Z(\mathbb{B})=\mathbb{C}e_0\cong\mathbb{C}$.

The algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ has a single simple left module up to isomorphism, the defining module $S=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\tilde T\}$ of complex dimension two, and every left module is a direct sum $S^{\oplus k}$; the left regular module is free of rank one and decomposes as $\mathbb{B}\cong S\oplus S$. Every module is projective because $\mathbb{B}$ is semisimple, but $S^{\oplus k}$ is free if and only if $k$ is even, equivalently if and only if its complex dimension $2k$ is divisible by $4$; the module $S$ is projective and not free, and this parity is the entire distinction between the module theory of $\mathbb{B}$ and that of a field. Because $\mathbb{B}$ is simple, semisimple and Artinian, the bimodule is simple, every module is semisimple, and the algebra is von Neumann regular and self-injective; the regular module is therefore a projective generator and an injective cogenerator, the module from which the whole module theory is read.

The morphisms are the complex matrices: $\operatorname{End}_\mathbb{B}(S)=\mathbb{C}$, $\operatorname{Hom}_\mathbb{B}(S^{\oplus m},S^{\oplus n})\cong M_{n\times m}(\mathbb{C})$ and $\operatorname{End}_\mathbb{B}(S^{\oplus k})\cong M_k(\mathbb{C})$, with automorphism group $\mathrm{GL}_k(\mathbb{C})$, while the double centralizer gives $\operatorname{End}_\mathbb{C}(S)=\mathbb{B}$. The module $S$ is the standard $(\mathbb{B},\mathbb{C})$-bimodule, the two actions commuting because $\mathbb{C}$ is the centre, and it implements the Morita equivalence of $\operatorname{Mod}(\mathbb{B})$ with $\operatorname{Mod}(\mathbb{C})$: $\operatorname{Hom}_\mathbb{B}(S,-)$ has inverse $S\otimes_\mathbb{C}-$, and every complex dimension is doubled. Torsion in the naive sense degenerates over $\mathbb{B}$ because the algebra has zero divisors and the annihilator of a nonzero element of $S$ is a maximal left ideal; tested against regular elements it vanishes, since in a semisimple ring every regular element is a unit, and the module category is torsion-free. Finally, the $\mathbb{B}$-modules that come from $\mathbb{H}$ by extension of scalars are exactly the free ones, so the parity obstruction to freeness is also the obstruction to a real structure, with $S$ the minimal example.


## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{B}^{\mathrm{op}}$ | the opposite algebra, $\cong\mathbb{B}$ through the anti-automorphism ${}^{\natural}$ |
| $e_0,e_1,e_2,e_3$ | quaternion basis, $e_0=1$, $e_k^2=-e_0$ |
| $i$ | central scalar imaginary, $i^2=-1$ |
| ${}_{\mathbb{B}}\mathbb{B}$ | the left regular module, $(\mathbb{B},+)$ with $\tilde Q\cdot\tilde R=\tilde Q\tilde R$, free of rank one |
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
| $\tilde\Pi_1,\tilde\Pi_2$ | orthogonal minimal idempotents $\tfrac12(e_0\pm ie_3)$, $\tilde\Pi_1+\tilde\Pi_2=e_0$ |
| $\tilde R,\tilde T$ | the two off-diagonal elements $\tfrac12(ie_1-e_2)$, $\tfrac12(ie_1+e_2)$ |
| $S=\mathbb{B}\tilde\Pi_1=\mathbb{C}\{\tilde\Pi_1,\tilde T\}$ | defining module, the unique simple left $\mathbb{B}$-module, $\dim_\mathbb{C}=2$ |
| $S^{\oplus k}$ | general finitely generated left module, $\dim_\mathbb{C}=2k$ |
| ${}_{\mathbb{B}}\mathbb{B}\cong S\oplus S$ | left regular module, free of rank one over $\mathbb{B}$, completely reducible |
| $\operatorname{End}_\mathbb{B}(S)=\mathbb{C}$ | commutant of the simple module |
| $\operatorname{End}_\mathbb{C}(S)=\mathbb{B}$ | double centralizer |
| ${}_{\mathbb{B}}S_\mathbb{C}$ | standard Morita bimodule |
| $\operatorname{Hom}_\mathbb{B}(S,-)$, $S\otimes_\mathbb{C}-$ | the Morita equivalence $\operatorname{Mod}(\mathbb{B})\cong\operatorname{Mod}(\mathbb{C})$ |
| $\operatorname{Ann}_\mathbb{B}(s)$ | annihilator, a maximal left ideal for $s\neq0$ |
| regular element | a non-zero-divisor |
| $\operatorname{Res}^{\mathbb{B}}_{\mathbb{H}}$ | restriction of a $\mathbb{B}$-module to $\mathbb{H}$ |
| von Neumann regular, self-injective | $\tilde Q\tilde B\tilde Q=\tilde Q$; injectivity of ${}_{\mathbb{B}}\mathbb{B}$ |


## Further Reading

- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for semisimple rings, matrix algebras, Schur's lemma and Morita equivalence.
- T. Y. Lam, *Lectures on Modules and Rings* (Springer, 1999), for the regular module, its projectivity and the centre as the bimodule endomorphism ring, and for torsion, regular elements and the structure of modules over noncommutative rings.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for modules and the regular module over finite-dimensional algebras, the matrix algebra $M_2(\mathbb{C})$, its minimal left ideals, the Peirce decomposition and projective modules.
- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for the regular module, its generator property and the endomorphism ring of a module.
- Nicolas Bourbaki, *Algebra I* (Springer, 1989), for modules over rings, the regular module and the correspondence between submodules and ideals, the Morita theory of matrix algebras and change of rings.
- Paul M. Cohn, *Skew Fields: Theory of General Division Rings* (Cambridge, 1995), for rank and linear algebra over division rings, in the comparison with the quaternions.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for the tensor unit and the generator property.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the quaternion and biquaternion algebras, the matrix isomorphism $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})$ and the descent between them.
