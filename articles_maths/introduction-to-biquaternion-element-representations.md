# __Introduction to Biquaternion Element Representations__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is isomorphic to the full matrix algebra $M_2(\mathbb{C})$, and this one fact settles its representation theory. The algebra is simple and semisimple, it has a single simple module up to isomorphism, and every representation is a direct sum of copies of it. This article introduces the representations of $\mathbb{B}$: the dictionary between representations and modules, the classification by a single dimension, Schur's lemma and the intertwiners, the defining and the half-spin representations, the tensor products and their Clebsch–Gordan rule, the real representations and the descent to the real form, and the representations of the group of units. It is the entry of the biquaternion chapter that the other representation articles presuppose.

The treatment is purely mathematical. No physics is invoked. The general theory of finite-dimensional associative algebras — Wedderburn's theorem, semisimplicity, Schur's lemma, Morita equivalence — is used as standard. The module theory of $\mathbb{B}$ is not repeated here: it is the content of *Modules over the Biquaternion Algebra*, which owns the regular module, the submodule–ideal correspondence, the endomorphism rings and the Morita equivalence, and it is cited throughout. The algebra conventions are those of *The Biquaternion Algebra and Its Vector Spaces*: the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ with $e_t=1$, $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$, the central scalar imaginary $i$ with $i^2=-1$, and a generic element written

$$
\tilde Q=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu,\qquad Q_\mu\in\mathbb{C}.
$$

The norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde{Q}^{\natural}$ and the group of units is $\mathbb{B}^{\times}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}\neq0\}$; both are the subject of *Norm Regularity and Degeneracy in the Biquaternion Algebra* and are cited here rather than restated. The matrix models are *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions* and *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions*, and the group-theoretic representation theory — the defining representation of the Lorentz group, the half-spin representations and the Clebsch–Gordan rule — is *Biquaternion Rotations and Lorentz Transformations*.

## The Algebra and Its Ground Fields

The algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is complex dimension four with basis $\{e_t,\vec e_x,\vec e_y,\vec e_z\}$, and it is a **central simple** $\mathbb{C}$-algebra:

$$
\mathbb{B}\cong M_2(\mathbb{C}),\qquad Z(\mathbb{B})=\mathbb{C}e_t\cong\mathbb{C}.
$$

The isomorphism is $\mathsf{M}_2$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*, and its existence is the reason the whole representation theory is the linear algebra of a single two-dimensional space.

Two ground structures are read on the same elements. Over its centre $\mathbb{C}$, over which it is an algebra and a four-dimensional vector space, the representations are complex. Over $\mathbb{R}$, over which it has dimension eight, the same elements form a real algebra $\mathbb{B}_{\mathbb{R}}$, and the real representations are a different category; the passage is restriction of scalars, treated below and in *The Biquaternion Algebra and Its Vector Spaces* and *The Realification and the Effect of the Change of Scalars*.

**Definition.** The **opposite algebra** $\mathbb{B}^{\mathrm{opp}}$ is the same additive group with the reversed product $\tilde Q_1\cdot\tilde Q_2=\tilde Q_2\tilde Q_1$. Quaternion conjugation $\tilde Q\mapsto\tilde{Q}^{\natural}$ is an anti-automorphism, so $\mathbb{B}^{\mathrm{opp}}\cong\mathbb{B}$, and it is the standard way the two products are identified.

## Representations and Modules

**Definition.** A **representation** of $\mathbb{B}$ is a complex vector space $V$ together with an algebra homomorphism

$$
\rho:\mathbb{B}\longrightarrow\operatorname{End}_{\mathbb{C}}(V),\qquad \rho(\tilde Q_1\tilde Q_2)=\rho(\tilde Q_1)\rho(\tilde Q_2),\qquad \rho(e_t)=\mathrm{id}_V .
$$

Its **dimension** is $\dim_{\mathbb{C}}V$. Two representations $\rho,\rho'$ on $V,V'$ are **equivalent** when there is a linear isomorphism $T:V\to V'$ with $T\rho(\tilde Q)=\rho'(\tilde Q)T$ for every $\tilde Q$.

**Theorem (representations are modules).** The representations of $\mathbb{B}$ are the left $\mathbb{B}$-modules: the action $\tilde Q\cdot v=\rho(\tilde Q)v$ makes $V$ a left module, and conversely a left module gives a representation. The correspondence preserves dimension, subobjects, quotients, direct sums and equivalences, so the category of representations is the category of left modules.

*Proof.* The module axioms are the homomorphism axioms read backwards: distributivity in the scalar is additivity of $\rho(\tilde Q)$, distributivity in the vector and the unit law are the two remaining homomorphism laws, and $(\tilde Q_1\tilde Q_2)\cdot v=\tilde Q_1\cdot(\tilde Q_2\cdot v)$ is multiplicativity. A module homomorphism is exactly an intertwining linear map, and direct sums are taken in the underlying complex vector spaces.

**Definition.** A representation is **irreducible**, or simple, when it has no proper nonzero subrepresentation, and **indecomposable** when it is not a direct sum of two proper subrepresentations. A representation is **faithful** when $\rho$ is injective.

Because $\mathbb{B}$ is semisimple, every representation is completely reducible, so irreducible and indecomposable coincide, and the classification reduces to the simple modules. That classification is the content of the next section.

## The Simple Module and Complete Reducibility

**Theorem.** Up to isomorphism the algebra $\mathbb{B}$ has exactly one simple left module $S$, and

$$
\boxed{\; S\cong\mathbb{C}^2,\qquad \operatorname{End}_{\mathbb{B}}(S)\cong\mathbb{C},\qquad {}_{\mathbb{B}}\mathbb{B}\cong S\oplus S \;}.
$$

The simple module is the defining module $S=\mathbb{B}\tilde\Pi_1$ of *Modules over the Biquaternion Algebra*, cut by the idempotent $\tilde\Pi_1=\tfrac12(e_t+i\vec e_z)$.

*Proof.* The algebra is $M_2(\mathbb{C})$, and a matrix algebra over a field has a single simple left module, its column space $\mathbb{C}^2$; the endomorphism ring is the field by Schur's lemma, and the regular module is the sum of the two column spaces. The identification with $\mathbb{B}\tilde\Pi_1$ is *Modules over the Biquaternion Algebra*.

**Corollary (classification).** Every left $\mathbb{B}$-module is a direct sum of copies of $S$,

$$
\boxed{\; M\cong S^{\oplus k},\qquad \dim_{\mathbb{C}}M=2k \quad (k\geq 0) \;},
$$

so a representation is determined up to equivalence by its dimension, and the dimension is even. A representation of dimension $2k$ is irreducible exactly when $k=1$; for $k=0$ it is the zero representation.

*Proof.* Complete reducibility is semisimplicity of $\mathbb{B}$, and the multiplicity $k$ is the dimension over the division ring $\operatorname{End}_{\mathbb{B}}(S)=\mathbb{C}$; the details are *Modules over the Biquaternion Algebra* and *Simple and Semisimple Modules*.

**Corollary (Morita equivalence).** The functor $W\mapsto S\otimes_{\mathbb{C}}W$ is an equivalence of categories from the complex vector spaces to the left $\mathbb{B}$-modules, with inverse $\operatorname{Hom}_{\mathbb{B}}(S,-)$. It doubles every complex dimension, and it is the reason a $\mathbb{B}$-module is "a complex vector space in disguise".

*Proof.* This is the Morita equivalence $\operatorname{Mod}(\mathbb{B})\cong\operatorname{Mod}(\mathbb{C})$ of *Modules over the Biquaternion Algebra*, where $S$ is the standard $(\mathbb{B},\mathbb{C})$-bimodule and $\operatorname{End}_{\mathbb{C}}(S)=\mathbb{B}$ is the double centraliser.

**Remark (the parity of freeness).** A module $S^{\oplus k}$ is free over $\mathbb{B}$ exactly when $k$ is even, that is when its complex dimension $2k$ is divisible by four: the regular module $\mathbb{B}\cong S\oplus S$ is free of rank one, while the defining module $S$ itself is projective and not free. The parity is the entire distinction between the module theory of $\mathbb{B}$ and that of a field, and it is developed in *Modules over the Biquaternion Algebra*.

## Schur's Lemma and Intertwiners

**Theorem (Schur).** For simple $\mathbb{B}$-modules $S$ and $T$, every nonzero homomorphism $S\to T$ is an isomorphism, and $\operatorname{End}_{\mathbb{B}}(S)$ is a division ring. For the single simple module of $\mathbb{B}$,

$$
\operatorname{End}_{\mathbb{B}}(S)\cong\mathbb{C}.
$$

*Proof.* Schur's lemma is standard. The endomorphism ring is a division ring, and since $\mathbb{B}$ is central simple and $\mathbb{C}$ is algebraically closed, the division ring is $\mathbb{C}$; concretely, an endomorphism of the column space commuting with all of $M_2(\mathbb{C})$ is a scalar matrix.

**Corollary (intertwiners).** Between the modules $S^{\oplus m}$ and $S^{\oplus n}$ the homomorphisms are the complex matrices,

$$
\operatorname{Hom}_{\mathbb{B}}\bigl(S^{\oplus m},S^{\oplus n}\bigr)\cong M_{n\times m}(\mathbb{C}),\qquad \operatorname{End}_{\mathbb{B}}\bigl(S^{\oplus k}\bigr)\cong M_k(\mathbb{C}),
$$

with automorphism group $\mathrm{GL}_k(\mathbb{C})$. In particular the commutant of the representation on $S^{\oplus k}$ is $M_k(\mathbb{C})$, and the double centraliser of the defining representation is $\operatorname{End}_{\mathbb{C}}(S)=\mathbb{B}$.

*Proof.* A homomorphism is determined by the images of the $m$ copies of $S$, each of which is a homomorphism $S\to S^{\oplus n}$, that is an $n$-tuple of elements of $\operatorname{End}_{\mathbb{B}}(S)=\mathbb{C}$; assembling the tuples gives the matrix. The endomorphisms of $S^{\oplus k}$ are the square case, and the double centraliser is *Modules over the Biquaternion Algebra*.

## The Defining Representation

**Definition.** The **defining representation** of $\mathbb{B}$ is the simple module $S\cong\mathbb{C}^2$, with the action of $\mathbb{B}$ through the isomorphism $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb{C})$ of Biquaternions*:

$$
\tilde Q\cdot v=\mathsf{M}_2(\tilde Q)v,\qquad v\in\mathbb{C}^2 .
$$

**Theorem.** The defining representation is irreducible, of complex dimension two, and faithful. It is the unique irreducible representation up to equivalence, and every faithful representation contains it and has dimension at least two; the smallest faithful representation is $S$ itself, and the regular representation $\mathbb{B}\cong S\oplus S$ is faithful of dimension four.

*Proof.* Irreducibility and uniqueness are the classification above; faithfulness is injectivity of $\mathsf{M}_2$, which is an isomorphism. A faithful module is nonzero and therefore contains a copy of $S$; the defining module is faithful itself, and the regular module is the smallest regular one.

**Remark (the same representation in other writings).** The defining representation is written in several arrays of the corpus, none of which changes it. The four-vector realization of *The Four-Vector Element Representation of Biquaternions* writes an element by its coefficient column and the action by the component product; the $2\times2$ matrix realization writes it by $\mathsf{M}_2$; the left regular realization $\mathsf{M}_4$ of *Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions* is the action on $S\oplus S$, and in a basis adapted to the two minimal left ideals it is block diagonal with $\mathsf{M}_2(\tilde Q)$ in both blocks. The regular matrix therefore contains the defining matrix twice, which is the array form of ${}_{\mathbb{B}}\mathbb{B}\cong S\oplus S$.

**Theorem (the half-spin pair).** The dual module $S^{*}=\operatorname{Hom}_{\mathbb{C}}(S,\mathbb{C})$ is a right $\mathbb{B}$-module, and its conjugate-dual, read as a left module through the identification $\mathbb{B}^{\mathrm{opp}}\cong\mathbb{B}$ by conjugation, is isomorphic to $S$. The two chiral halves of the spinor module are therefore $S$ and $S^{*}$, and as left modules they coincide; their separation is a reality and chirality statement, not an isomorphism class, and it belongs to *Biquaternion Spin Geometry* and *The Twisted Spinor Operator Representation of Biquaternions*.

*Proof.* The dual $S^{*}$ is a right module with $(\varphi\cdot\tilde Q)(v)=\varphi(\tilde Q v)$; carrying it to a left module by $\tilde Q\star\varphi=\varphi\cdot\tilde{Q}^{\natural}$ uses the anti-automorphism ${}^{\natural}$ and gives a left module isomorphic to $S$ because there is only one simple left module. The invariant pairing is the antisymmetric form $\epsilon=i\sigma_2$ of the biquaternion spinor structure.

## Tensor Products and the Clebsch–Gordan Rule

For a non-commutative algebra the tensor product of two left modules is not naturally a left module: the only candidate action would use one factor of $\mathbb{B}$ on each slot, and the resulting map $\tilde Q\mapsto\rho(\tilde Q)\otimes\sigma(\tilde Q)$ is not linear in $\tilde Q$. The tensor product of two left $\mathbb{B}$-modules is a left module not over $\mathbb{B}$ but over the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}$; since $\mathbb{B}\cong M_2(\mathbb{C})$, that enveloping algebra is

$$
\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\cong M_2(\mathbb{C})\otimes_{\mathbb{C}}M_2(\mathbb{C})\cong M_4(\mathbb{C}).
$$

On the single simple module the tensor square still decomposes with the classical multiplicities, but as a module over the enveloping algebra and, when the action is restricted to the group of units, as a group representation. On $S\cong\mathbb{C}^2$ the tensor square splits into the symmetric and the alternating parts,

$$
S\otimes_{\mathbb{C}}S\cong \operatorname{Sym}^{2}S\oplus\Lambda^{2}S,\qquad \dim_{\mathbb{C}}\operatorname{Sym}^{2}S=3,\quad \dim_{\mathbb{C}}\Lambda^{2}S=1,
$$

and the alternating square is the trivial module because the antisymmetric form $\epsilon=i\sigma_2$ is invariant. More generally the symmetric powers form the Clebsch–Gordan chain

$$
\operatorname{Sym}^{m}S\otimes_{\mathbb{C}}\operatorname{Sym}^{n}S\cong\bigoplus_{j=0}^{\min(m,n)}\operatorname{Sym}^{m+n-2j}S,
$$

each summand once. This is the tensor product of the irreducible representations of the unit group, and its derivation, together with the half-spin representations, is *Biquaternion Rotations and Lorentz Transformations*.

**Remark (the algebra-level tensor).** At the level of the algebra the same computation reads $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\cong M_4(\mathbb{C})$, which is the algebra form of the array isomorphism $M_n(\mathbb{B})\cong M_{2n}(\mathbb{C})$ recorded in *Biquaternion Other Algebraic Element Representations*; the two are the same dimension count, one for the tensor square of the algebra and one for the array of several elements.

## Real Representations and the Real Forms

**Definition.** A **real representation** of $\mathbb{B}$ is a real vector space $V$ together with an $\mathbb{R}$-algebra homomorphism $\mathbb{B}_{\mathbb{R}}\to\operatorname{End}_{\mathbb{R}}(V)$, where $\mathbb{B}_{\mathbb{R}}$ is $\mathbb{B}$ read as a real algebra of dimension eight.

Restriction of scalars relates the two categories. A complex representation $V$ of complex dimension $n$ is a real representation of real dimension $2n$ when the complex scalars are forgotten, and the passage is not invertible: a real representation carries no complex structure in general, and the ones that do are exactly the complex representations, distinguished by a real-linear operator $J$ with $J^{2}=-\mathrm{id}$ commuting with the algebra. The criterion and the two block shapes it gives are *The Biquaternion Algebra and Its Vector Spaces* and *The Realification and the Effect of the Change of Scalars*.

**Theorem.** Every real representation of $\mathbb{B}$ is a direct sum of copies of the realification $S_{\mathbb{R}}$ of the defining module, of real dimension four:

$$
\boxed{\; M\cong S_{\mathbb{R}}^{\oplus k},\qquad \dim_{\mathbb{R}}M=4k \quad (k\geq0) \;}.
$$

*Proof.* The real algebra $\mathbb{B}_{\mathbb{R}}$ is the realification of $M_2(\mathbb{C})$, which is a simple Artinian real algebra with a single simple module, the realification of $\mathbb{C}^2$; complete reducibility and the multiplicity count are as over $\mathbb{C}$. The statement is the real reading of the classification, and it matches the complex classification through $\dim_{\mathbb{R}}M=2\dim_{\mathbb{C}}M$.

**Remark (the real forms).** The algebra $\mathbb{B}$ contains the quaternion division algebra $\mathbb{H}$ and the real matrix algebra $M_2(\mathbb{R})$ as subalgebras of real dimension four, and its Clifford reading is $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}(\mathbb{R})$, the even Clifford algebra of the Minkowski form, which is *Biquaternion Other Algebraic Element Representations*. The four real forms — $\mathbb{B}$, $\mathbb{H}$, $M_2(\mathbb{R})$ and the split quaternions — are the real algebras of the same complexification, and the place of $\mathbb{B}$ among them is *The Realification and the Effect of the Change of Scalars*, with the split comparison in *Split-Biquaternion Element Representation Theory*. Only $\mathbb{H}$ is a division algebra, which is why only its module category is the category of quaternionic vector spaces.

## The Group of Units and Its Representations

**Theorem.** The group of units of $\mathbb{B}$ is the complement of the zero divisors,

$$
\mathbb{B}^{\times}=\{\tilde Q:\langle\tilde Q\rangle_{\natural}\neq0\}\cong GL_2(\mathbb{C}),
$$

a complex Lie group of dimension four over $\mathbb{C}$, equivalently eight over $\mathbb{R}$, non-compact. Under the norm and the dagger it splits as

$$
\mathbb{B}^{\times}\cong\frac{SL_2(\mathbb{C})\times\mathbb{C}^{\times}}{\{\pm1\}},\qquad SL_2(\mathbb{C})=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=1\},
$$

with maximal compact subgroup $\mathrm{U}(2)$.

*Proof.* An element is a unit in $M_2(\mathbb{C})$ exactly when its determinant is nonzero, and the determinant is the norm; the splitting is that of $GL_2(\mathbb{C})$ into its unimodular part and the scalar matrices, whose intersection is $\{\pm I\}$. The norm-one group is $SL_2(\mathbb{C})$ and the compact part is $\mathrm{U}(2)$; the matrix groups are *The Unitary Group of the Biquaternion Algebra* and *The Biquaternion Unit Group as a Topological Group*.

**Theorem.** The finite-dimensional continuous representations of the norm-one group are the symmetric powers,

$$
SL_2(\mathbb{C})\longrightarrow GL\bigl(\operatorname{Sym}^{n}S\bigr),\qquad \dim_{\mathbb{C}}\operatorname{Sym}^{n}S=n+1 \quad (n\geq0),
$$

and they are irreducible and pairwise inequivalent; the symmetric square $\operatorname{Sym}^{2}S$ is the adjoint representation, and the defining representation $S=\operatorname{Sym}^{1}S$ is the source of the double cover $SL_2(\mathbb{C})\to SO^{+}(1,3)$. The finite-dimensional continuous representations of the compact part are $\det^{k}\otimes\operatorname{Sym}^{n}S$ with $k\in\mathbb{Z}$, $n\geq0$.

*Proof.* The complex Lie group $SL_2(\mathbb{C})$ is simply connected with complexified Lie algebra $\mathfrak{sl}_2(\mathbb{C})$, whose finite-dimensional representations are the symmetric powers; the statement is the usual highest-weight classification, and the double cover and the adjoint reading are *Biquaternion Rotations and Lorentz Transformations*. The compact case is the representation theory of $\mathrm{U}(2)$, whose irreducible representations are indexed by an integer $\det$-power and a non-negative integer $n$, developed in *The Unitary Group of the Biquaternion Algebra*.

**Remark (faithfulness of the group representation).** The defining representation of the unit group is faithful; unlike the split biquaternion algebra, the biquaternion algebra therefore has a faithful irreducible representation. The reason is that $\mathbb{B}$ is simple, and a simple algebra with a single simple module is represented faithfully by it.

## The Relation to the Representation Theory of the Split Biquaternions

The biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is simple, with one simple module $S\cong\mathbb{C}^2$, division ring $\mathbb{C}$ and regular module of complex dimension four. The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}\cong\mathbb{H}\oplus\mathbb{H}$ is semisimple but not simple, with two simple modules, division ring $\mathbb{H}$ and regular module of real dimension eight. The correspondence is

$$
\mathbb{B}\longleftrightarrow\mathbb{H}\oplus\mathbb{H},\qquad \mathbb{C}\longleftrightarrow\mathbb{H},
$$

the replacement of the simple algebra $M_2(\mathbb{C})$ by a product of two division algebras; the module categories are the linear algebra of $\mathbb{C}$ on one side and the product of two copies of the category of quaternionic vector spaces on the other. The comparison is developed in *Split-Biquaternion Element Representation Theory*, where the two simple modules, the Peirce decomposition and the exterior tensor products of the unit group are recorded.

## Summary

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ is central simple, so its representations are the left $\mathbb{B}$-modules and every one of them is a direct sum of copies of a single simple module $S\cong\mathbb{C}^2$. A representation is equivalent to a complex vector space through the Morita equivalence $W\mapsto S\otimes_{\mathbb{C}}W$, it is classified up to equivalence by its dimension, and the dimension is even; the multiplicities are the complex dimensions. Schur's lemma gives $\operatorname{End}_{\mathbb{B}}(S)=\mathbb{C}$, the intertwiners are the complex matrices $\operatorname{Hom}_{\mathbb{B}}(S^{\oplus m},S^{\oplus n})\cong M_{n\times m}(\mathbb{C})$, and the double centraliser is $\operatorname{End}_{\mathbb{C}}(S)=\mathbb{B}$.

The defining representation is the simple module $S$, irreducible, of complex dimension two and faithful; it is the unique irreducible representation, the smallest faithful one, and the regular representation is $S\oplus S$. The dual and conjugate-dual modules give the half-spin pair, which as left modules coincides. The tensor product of two left modules is a module over the enveloping algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\cong M_4(\mathbb{C})$, and on the defining module it follows the Clebsch–Gordan rule, with $S\otimes S\cong\operatorname{Sym}^{2}S\oplus\Lambda^{2}S$ of dimensions three and one.

Over $\mathbb{R}$ every representation is a direct sum of copies of the realification $S_{\mathbb{R}}$ of dimension four, and the algebra has the real forms $\mathbb{B}$, $\mathbb{H}$, $M_2(\mathbb{R})$ and the split quaternions, of which only $\mathbb{H}$ is a division algebra. The group of units is $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})\cong(SL_2(\mathbb{C})\times\mathbb{C}^{\times})/\{\pm1\}$ with maximal compact subgroup $\mathrm{U}(2)$; the finite-dimensional continuous representations of the norm-one group are the symmetric powers $\operatorname{Sym}^{n}S$, the adjoint representation is $\operatorname{Sym}^{2}S$, and the defining representation is the source of the double cover $SL_2(\mathbb{C})\to SO^{+}(1,3)$. The whole theory is the module theory of a single simple algebra, in contrast with the split biquaternion algebra, whose two simple modules and product structure are the subject of *Split-Biquaternion Element Representation Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ | Biquaternion algebra, central simple |
| $Z(\mathbb{B})=\mathbb{C}e_t$ | Centre, the scalar matrices |
| $S\cong\mathbb{C}^2$ | The unique simple left module, the defining representation |
| $S^{*}$ | Dual module; the half-spin pair with $S$ |
| $\rho:\mathbb{B}\to\operatorname{End}_{\mathbb{C}}(V)$ | A representation, equivalently a left module |
| $\operatorname{End}_{\mathbb{B}}(S)\cong\mathbb{C}$ | Schur endomorphism ring |
| $\operatorname{Hom}_{\mathbb{B}}(S^{\oplus m},S^{\oplus n})\cong M_{n\times m}(\mathbb{C})$ | Intertwiners |
| ${}_{\mathbb{B}}\mathbb{B}\cong S\oplus S$ | Regular module |
| $S^{\oplus k}$, $\dim_{\mathbb{C}}=2k$ | Classification of modules by multiplicity |
| $S\otimes_{\mathbb{C}}-$ | Morita equivalence with the complex vector spaces |
| $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}\cong M_4(\mathbb{C})$ | Enveloping algebra |
| $\operatorname{Sym}^{n}S$, $\Lambda^{2}S\cong\mathbb{C}$ | Symmetric powers; invariant alternating square |
| $\mathbb{B}_{\mathbb{R}}$, $S_{\mathbb{R}}$ | Real algebra of dimension eight; realification of the defining module |
| $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$ | Group of units, $\langle\tilde Q\rangle_{\natural}\neq0$ |
| $SL_2(\mathbb{C})$ | Norm-one group, double cover of $SO^{+}(1,3)$ |
| $\mathrm{U}(2)$ | Maximal compact subgroup of the unit group |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for central simple algebras, matrix algebras, Wedderburn's theorem and the classification of modules.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for semisimple rings, Schur's lemma, Morita equivalence and the representation theory of matrix algebras.
- Irving Kaplansky, *Fields and Rings* (Chicago, 1972), for the structure of simple algebras and their module categories.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Wiley, 1962), for intertwiners, tensor products and the Clebsch–Gordan rule.
- Theodore Bröcker and Tammo tom Dieck, *Representations of Compact Lie Groups* (Springer, 1985), for the representation theory of $\mathrm{U}(2)$ and the symmetric powers of $SU(2)$.
- Jacques Dixmier, *Enveloping Algebras* (North-Holland, 1977), for the finite-dimensional representation theory of $\mathfrak{sl}_2(\mathbb{C})$ and the symmetric powers.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the complexified quaternion algebra, the isomorphism $\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})$ and the descent to the real forms.
