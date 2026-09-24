
# __Morita Equivalence__

## Introduction

Two algebras have the same module theory when their categories of modules are equivalent, even if the algebras themselves are not isomorphic. This is Morita equivalence, and it is the guiding equivalence relation of the category *Linear spaces over Algebras*: it says which differences between algebras are invisible to the modules, and therefore which constructions of representation theory can depend only on the module category. The fundamental example is already visible in the preceding articles — a matrix algebra $M_n(A)$ has exactly the same modules as $A$, with the defining module of $M_n(A)$ playing the role of the regular module of $A$ — and the purpose of this article is to make that observation into a theorem, to isolate the invariant that governs it, and to identify what Morita equivalence does and does not preserve.

The conventions are those of *Modules over an Algebra*: $R$ is a commutative ring with identity, $A$ and $B$ are unital associative $R$-algebras, modules are left modules unless stated, and ${}_A P_B$ denotes an $(A,B)$-bimodule. The tensor product over an algebra is the balanced product , and the change-of-rings functors used below are those . Schur's lemma, semisimple modules and the Wedderburn–Artin theorem are used from *Simple and Semisimple Modules*.

The plan is to define equivalence of module categories, prove that matrix algebras are Morita equivalent to their ground algebra, characterize the equivalence in terms of finitely generated projective generators, and then separate the invariants from the non-invariants. The last two sections treat the two standard applications: group algebras, where Morita equivalence classifies semisimple group algebras by their basic algebra and organizes the modular theory by blocks; and central simple algebras, where Morita equivalence classes are precisely the elements of the Brauer group.

## Equivalence of Module Categories

### Equivalence of categories

Let $\mathcal{C}$ and $\mathcal{D}$ be categories. An **equivalence** between them is a functor $F: \mathcal{C} \to \mathcal{D}$ that is **fully faithful** — the map $\operatorname{Hom}_{\mathcal{C}}(X,Y)\to\operatorname{Hom}_{\mathcal{D}}(FX,FY)$ is a bijection for all $X,Y$ — and **essentially surjective**: every object of $\mathcal{D}$ is isomorphic to $FX$ for some $X$. Equivalently, there is a functor $G: \mathcal{D} \to \mathcal{C}$ and natural isomorphisms $GF \cong \mathrm{id}_{\mathcal{C}}$, $FG \cong \mathrm{id}_{\mathcal{D}}$; such a $G$ is a **quasi-inverse** of $F$. An equivalence need not be an isomorphism of categories: it is unnatural to demand that $GF$ and $FG$ be equal to the identities rather than naturally isomorphic to them, and the weaker condition is the correct one.

For module categories one restricts to functors compatible with the linear structure. A functor $F: \operatorname{Mod}(A)\to\operatorname{Mod}(B)$ is **$R$-linear**, or **additive**, if it induces $R$-module maps on hom-sets and preserves finite direct sums. Every equivalence arising below is $R$-linear.

### Morita equivalence

Two $R$-algebras $A$ and $B$ are **Morita equivalent**, written $A \sim_M B$, if there is an $R$-linear equivalence

$$
\operatorname{Mod}(A) \xrightarrow{\ \simeq\ } \operatorname{Mod}(B).
$$

Since an equivalence preserves every categorical notion, Morita equivalent algebras have the same submodule lattices, the same simple modules up to a bijection, the same injective and projective modules, the same homological algebra, and the same representation theory. They need not be isomorphic, and the smallest example is already decisive.

**Proposition.** $A$ and $M_n(A)$ are Morita equivalent for every $n \geq 1$.

This is proved below as the fundamental example. It shows, in particular, that $\mathbb{C}$ and $M_2(\mathbb{C})$ are Morita equivalent; since the biquaternion algebra is $\mathbb{B}\cong M_2(\mathbb{C})$, the module theory of the biquaternion algebra is the module theory of the complex field, a statement used repeatedly .

## The Fundamental Example: Matrix Algebras

Let $A$ be a unital ring and let $P=A^n$ be the free left $A$-module of rank $n$, whose elements we write as column vectors. The ring $M_n(A)$ acts on $P$ on the left by matrix multiplication, and $P$ is a $(M_n(A),A)$-bimodule: the left action of matrices and the right action of scalars commute by associativity. Since $A$ is not assumed commutative, it matters that the scalars act on the right of the matrices.

**Theorem.** The functor

$$
\Phi = P \otimes_A - : \operatorname{Mod}(A) \longrightarrow \operatorname{Mod}(M_n(A)),
$$

given on objects by $M \mapsto P \otimes_A M = A^n \otimes_A M$, is an equivalence of categories.

*Pro.* First, $A^n \otimes_A M \cong M^n$ naturally in $M$, by the isomorphism $(a_1,\dots,a_n)\otimes m \mapsto (a_1 m,\dots,a_n m)$; so on objects $\Phi(M)=M^n$, the direct sum of $n$ copies of $M$. The $M_n(A)$-action is the evident one, matrices acting on the columns of $M^n$.

The functor $\Phi$ has a right adjoint, namely

$$
\Psi = \operatorname{Hom}_{M_n(A)}(P,-) : \operatorname{Mod}(M_n(A)) \longrightarrow \operatorname{Mod}(A),
$$

by the tensor–hom adjunction, applied to the bimodule ${}_{M_n(A)}P_A$. We show that the unit and counit of the adjunction are isomorphisms. For $M \in \operatorname{Mod}(A)$ the unit is the natural map

$$
M \longrightarrow \operatorname{Hom}_{M_n(A)}(A^n, M^n), \qquad m \longmapsto \bigl(u \mapsto (u_1 m,\dots,u_n m)\bigr),
$$

which is an isomorphism: an $M_n(A)$-linear map $g: A^n \to M^n$ is determined by $g(e_1)$, since equivariance under the matrix units gives $g(e_j)=g(E_{j1}e_1)=E_{j1}g(e_1)$; the same equivariance with $E_{11}$ forces $g(e_1)=E_{11}g(e_1)=(m,0,\dots,0)$ for a unique $m \in M$; and then $g(e_j)$ is the vector with $m$ in the $j$-th place, so that $g(u)=(u_1m,\dots,u_nm)$ for every $u$. For $N \in \operatorname{Mod}(M_n(A))$ the counit is the natural map

$$
A^n \otimes_A \operatorname{Hom}_{M_n(A)}(A^n, N) \longrightarrow N,
$$

sending $(u,f)$ to $f(u)$; it is surjective because $A^n$ generates $\operatorname{Mod}(M_n(A))$, every module being a quotient of a direct sum of copies of the regular module $M_n(A)=A^n\oplus\cdots$ and each summand being reachable from $A^n$, and it is injective by the same description of $\operatorname{Hom}_{M_n(A)}(A^n,N)$. Hence $\Phi$ is an equivalence, with quasi-inverse $\Psi$. $\square$

The heart of the theorem is that the free module $A^n$ carries two endomorphism rings: as a left $A$-module its endomorphism ring is $M_n(A^{\mathrm{op}})$, and as a left $M_n(A)$-module its endomorphism ring is $A^{\mathrm{op}}$, the Morita theorem reading these as $M_n(A)\cong\operatorname{End}_A(A^n)^{\mathrm{op}}$ and $A\cong\operatorname{End}_{M_n(A)}(A^n)^{\mathrm{op}}$. When $A$ is commutative the two opposite rings coincide with $M_n(A)$ and $A$. The equivalence exchanges the regular module of $A$ for the module $A^n$ over $M_n(A)$: under $\Phi$, ${}_A A$ corresponds to $A^n$ as a left $M_n(A)$-module, which is the direct sum of $n$ copies of the defining module of $M_n(A)$ when $A$ is a field. This is why the defining module of $M_n(F)$ inherits the role of the regular module of $F$.

## Progenerators and the Morita Theorems

### Generators

A left $A$-module $P$ is a **generator** if every left $A$-module is a quotient of a direct sum of copies of $P$. Equivalently, the **trace ideal**

$$
\operatorname{Tr}_A(P)=\Bigl\{\sum_i f_i(p_i) : f_i \in \operatorname{Hom}_A(P,A),\ p_i \in P\Bigr\} \subseteq A
$$

is all of $A$. Equivalently, $\operatorname{Hom}_A(P,-): \operatorname{Mod}(A)\to\operatorname{Mod}(\operatorname{End}_A(P)^{\mathrm{op}})$ is faithful. The regular module ${}_A A$ is a generator, and any module admitting $A$ as a direct summand of a finite direct sum of copies of itself is a generator. A **progenerator** is a finitely generated projective generator.

### The Morita theorems

**Theorem (Morita I).** Let $P$ be a progenerator of left $A$-modules and put

$$
B=\operatorname{End}_A(P)^{\mathrm{op}}.
$$

Then $P$ is an $(A,B)$-bimodule, and

$$
\operatorname{Hom}_A(P,-) : \operatorname{Mod}(A) \longrightarrow \operatorname{Mod}(B)
$$

is an equivalence of categories, with quasi-inverse $P \otimes_B -$. Conversely, every equivalence $\operatorname{Mod}(A)\to\operatorname{Mod}(B)$ arises in this way from a progenerator.

*Proof.* The right $B$-module structure on $P$ is $p \cdot b = b(p)$, which is a right action because $B$ is the opposite of the endomorphism ring; this makes $P$ an $(A,B)$-bimodule since endomorphisms are $A$-linear. The adjunction $\operatorname{Hom}_A(P \otimes_B -, -)\cong\operatorname{Hom}_B(-,\operatorname{Hom}_A(P,-))$ has unit and counit which are isomorphisms precisely because $P$ is a generator (counit) and finitely generated projective (unit), by the standard argument dual to the matrix case above. $\square$

**Theorem (Morita II).** The following are equivalent for unital rings $A$ and $B$.

1. $A$ and $B$ are Morita equivalent.
2. $B \cong \operatorname{End}_A(P)^{\mathrm{op}}$ for some progenerator $P$ of left $A$-modules.
3. $B \cong eM_n(A)e$ for some $n \geq 1$ and some idempotent $e \in M_n(A)$ with $M_n(A)eM_n(A)=M_n(A)$.

*Proof.* The equivalence of (1) and (2) is Morita I. For (2)$\Leftrightarrow$(3), a finitely generated projective left $A$-module is a direct summand of $A^n$ for some $n$, hence of the form $P\cong A^ne$ for an idempotent $e \in M_n(A)$ acting on the right of the row module $A^n$; then $\operatorname{End}_A(P)^{\mathrm{op}}\cong eM_n(A)e$, and the generator condition is exactly $M_n(A)eM_n(A)=M_n(A)$. $\square$

An idempotent $e$ with $M_n(A)eM_n(A)=M_n(A)$ is called **full**. The characterization (3) shows that the Morita equivalence class of $A$ consists exactly of the full corner rings of matrix algebras over $A$, and the algebra $eM_n(A)e$ is the general form of an algebra with the same module category.

### The basic algebra

Let $A$ be a finite-dimensional algebra over a field and let $S_1,\dots,S_r$ be its simple modules up to isomorphism, with projective covers $P_1,\dots,P_r$. The module

$$
P=P_1 \oplus \cdots \oplus P_r
$$

is a finitely generated projective generator — each simple module is a quotient of $P$, and each $P_i$ is a direct summand of the regular module — and

$$
A^{\mathrm{b}}=\operatorname{End}_A(P)^{\mathrm{op}}
$$

is the **basic algebra** of $A$. It is Morita equivalent to $A$ by Morita II, it is basic in the sense that $A^{\mathrm{b}}/J(A^{\mathrm{b}})\cong\prod_i D_i$ is a product of division rings with no matrix factor of size greater than one, and it is determined by $A$ up to isomorphism. For a semisimple $A$ the projective covers are the simple modules themselves, so that $P=S_1\oplus\cdots\oplus S_r$; by Wedderburn–Artin a semisimple algebra $A\cong\prod_i M_{n_i}(D_i)$ therefore has basic algebra $\prod_i D_i$, and Morita equivalence of semisimple algebras is exactly isomorphism of their basic algebras, that is, equality of the multiset of division rings $\{D_i\}$.

## Invariants and Non-Invariants

An $R$-linear equivalence preserves everything expressed categorically in terms of modules and homomorphisms. The following are therefore Morita invariants of $A$.

- **The center.** $Z(A)\cong Z(B)$. More precisely, $Z(A)$ is the ring of natural endomorphisms of the identity functor of $\operatorname{Mod}(A)$, and this description is manifestly intrinsic to the category.
- **The simple modules.** The equivalence induces a bijection between the isomorphism classes of simple left $A$-modules and those of simple left $B$-modules, and carries the endomorphism division ring $\operatorname{End}_A(S)$ isomorphically onto $\operatorname{End}_B(F(S))$, by the theorem of *Automorphisms of Modules over an Algebra* on transport of endomorphism rings.
- **The finitely generated projectives.** The equivalence restricts to an equivalence between the categories of finitely generated projective modules, and so induces an isomorphism of the Grothendieck groups $K_0(A)\cong K_0(B)$ and preserves the isomorphism classes of indecomposable projectives.
- **The lattice of two-sided ideals.** The equivalence induces an order isomorphism between the lattices of two-sided ideals of $A$ and of $B$. Hence simplicity, semisimplicity, primeness and the artinian and noetherian conditions are Morita invariant.
- **The isotypic structure.** Multiplicities of simple modules and lengths of modules are preserved.

The following are not Morita invariants.

- **The algebra itself.** $\mathbb{C}$ and $M_2(\mathbb{C})$ are Morita equivalent but not isomorphic, being of different dimensions over $\mathbb{C}$.
- **The group of units.** $\mathbb{C}^{\times}$ is abelian and $GL_2(\mathbb{C})$ is not, yet $\mathbb{C}$ and $M_2(\mathbb{C})$ are Morita equivalent. What is preserved is $\operatorname{Aut}_A(M)$ for corresponding modules $M$ and $F(M)$, not the group of units of the algebra as such.
- **Dimensions and cardinalities.** Morita equivalence can change the dimension of the algebra over its base ring arbitrarily, as the passage from $A$ to $M_n(A)$ shows.
- **The trace form, the norm form and other algebra-level structures.** These are not determined by the module category.

The dividing line is exact: Morita equivalence has access only to the category of modules, so anything that can be stated using modules and maps is invariant, and anything requiring the elements of the algebra as such need not be.

## Simple Modules under Morita Equivalence

The behaviour of the simple modules deserves to be stated separately, because it is the form in which Morita equivalence is used in representation theory.

**Theorem.** Let $F: \operatorname{Mod}(A)\to\operatorname{Mod}(B)$ be an equivalence. Then $F$ restricts to a bijection between the isomorphism classes of simple left $A$-modules and those of simple left $B$-modules, and for corresponding simple modules $S$ and $S'=F(S)$ there is a ring isomorphism $\operatorname{End}_A(S)\cong\operatorname{End}_B(S')$. Consequently the number of simple modules up to isomorphism is a Morita invariant, and so is the multiset of their endomorphism division rings.

*Proof.* An equivalence preserves submodule lattices and, being additive and exact, preserves the property of having no proper nonzero submodule; fully faithful functors induce isomorphisms on endomorphism rings. $\square$

For $A=M_n(F)$ the statement is the one already met: the simple module of $M_n(F)$ is $F^n$, and the simple module of $F$ is $F$, with the same endomorphism ring $F$; the equivalence of §The Fundamental Example carries the one to the other. For the biquaternion algebra, the equivalence $\operatorname{Mod}(\mathbb{B})\simeq\operatorname{Mod}(\mathbb{C})$ matches the simple module $\mathbb{C}^2$ of $\mathbb{B}$ with the simple module $\mathbb{C}$ of $\mathbb{C}$, and the division rings match: $\operatorname{End}_{\mathbb{B}}(\mathbb{C}^2)=\mathbb{C}$ and $\operatorname{End}_{\mathbb{C}}(\mathbb{C})=\mathbb{C}$.

The multiplicities are visible in the regular module. For $A=F$ and $B=M_n(F)$, with $P=F^n$ regarded as an $(M_n(F),F)$-bimodule, the equivalence $P\otimes_F-$ carries the regular module ${}_F F$ to $P=F^n$, which is the isotypic module with multiplicity $n$ over the unique simple module; this is the categorical origin of the multiplicity $n$ in the Wedderburn–Artin factor $M_n(F)$. In general, with $P$ a progenerator of left $A$-modules and $B=\operatorname{End}_A(P)^{\mathrm{op}}$, the equivalence $\operatorname{Hom}_A(P,-)$ carries ${}_A A$ to the dual progenerator $\operatorname{Hom}_A(P,A)$, while the quasi-inverse $P\otimes_B-$ carries the regular module ${}_B B$ to $P$; the two regular modules, and the multiplicity data they carry, are therefore both read off from the progenerator and its dual.

## Morita Equivalence as a Tensor Equivalence

The equivalence of Morita I is implemented by the balanced product. For a progenerator ${}_A P_B$ with $B=\operatorname{End}_A(P)^{\mathrm{op}}$, the two functors

$$
P \otimes_B - : \operatorname{Mod}(B) \to \operatorname{Mod}(A), \qquad \operatorname{Hom}_A(P,-) : \operatorname{Mod}(A) \to \operatorname{Mod}(B)
$$

are quasi-inverse, and the bimodule $P$ is an **invertible bimodule**: there is a $(B,A)$-bimodule $Q$ with $P\otimes_B Q\cong A$ as $(A,A)$-bimodules and $Q\otimes_A P\cong B$ as $(B,B)$-bimodules, namely $Q=\operatorname{Hom}_A(P,A)$. The tensor product of bimodules, developed, is the composition of the corresponding functors, so the statement that $P$ is invertible is the statement that the two functors are quasi-inverse. The Picard group $\operatorname{Pic}(A)$ consists of the isomorphism classes of invertible $(A,A)$-bimodules, with product $[M][N]=[M\otimes_A N]$ and identity $[A]$; by the Eilenberg–Watts theorem these are the auto-equivalences of $\operatorname{Mod}(A)$ implemented by bimodules. The full group of auto-equivalences of $\operatorname{Mod}(A)$ up to natural isomorphism is the semidirect product $\operatorname{Pic}(A)\rtimes\operatorname{Out}(A)$, in which an automorphism of $A$ twists the left action on an invertible bimodule and $\operatorname{Out}(A)=\operatorname{Aut}(A)/\operatorname{Inn}(A)$; equivalently, the inner automorphisms of $A$ act trivially on the module category, and only the outer ones are visible there.

The tensor equivalence also explains why Morita equivalence preserves flatness, projectivity and exactness: these are properties of the functors $M\otimes_A-$ or $\operatorname{Hom}_A(M,-)$, and conjugation by an equivalence preserves them.

## Group Algebras

Let $G$ be a finite group and $F$ a field. The group algebra $F[G]$ is a unital associative $F$-algebra, and $F[G]$-modules are the representations of $G$ over $F$, . Morita equivalence therefore compares the representation theories of groups, and the general theory applies directly.

### The semisimple case

Suppose that $\operatorname{char} F$ does not divide $|G|$, so that $F[G]$ is semisimple by Maschke's theorem. Then, by Wedderburn–Artin,

$$
F[G] \cong \prod_{i=1}^{r} M_{n_i}(D_i),
$$

where $r$ is the number of isomorphism classes of simple $F[G]$-modules, $S_i$ is the defining module of the $i$-th factor, $\operatorname{End}_{F[G]}(S_i)\cong D_i^{\mathrm{op}}$, and $D_i$ is a finite-dimensional division algebra over $F$. The basic algebra of $F[G]$ is

$$
F[G]^{\mathrm{b}} \cong \prod_{i=1}^{r} D_i,
$$

and therefore

$$
F[G] \sim_M F[H] \iff \prod_{i} D_i(G) \cong \prod_{i} D_i(H),
$$

that is, if and only if the two groups have the same number of simple modules with the same endomorphism division algebras, up to permutation. Over an algebraically closed field every $D_i$ is $F$, so the criterion reduces to equality of the number of simple modules. Over $F=\mathbb{C}$ the number of simple modules is the number of conjugacy classes of $G$, and the criterion becomes

$$
\mathbb{C}[G] \sim_M \mathbb{C}[H] \iff |\{\text{conjugacy classes of } G\}|=|\{\text{conjugacy classes of } H\}|.
$$

**Example.** $\mathbb{C}[S_3]\cong\mathbb{C}\times\mathbb{C}\times M_2(\mathbb{C})$ and $\mathbb{C}[C_3]\cong\mathbb{C}^3$, since $S_3$ has three conjugacy classes and $C_3$ has three. Both have basic algebra $\mathbb{C}^3$, so

$$
\mathbb{C}[S_3] \sim_M \mathbb{C}[C_3],
$$

although $S_3$ and $C_3$ are not isomorphic and their group algebras are not isomorphic. Morita equivalence matches the three simple modules of the one with the three simple modules of the other — the two-dimensional simple module of $\mathbb{C}[S_3]$ corresponding to the simple $\mathbb{C}[C_3]$-module on which a generator acts by a primitive cube root of unity — and it does not preserve the dimensions of simple modules. It does not carry the regular module to the regular module either: an equivalence preserves endomorphism rings, and

$$
\operatorname{End}_{\mathbb{C}[S_3]}(\mathbb{C}[S_3])\cong\mathbb{C}\times\mathbb{C}\times M_2(\mathbb{C}) \neq \mathbb{C}^3\cong\operatorname{End}_{\mathbb{C}[C_3]}(\mathbb{C}[C_3]),
$$

so the image of the regular module of $\mathbb{C}[S_3]$ has endomorphism algebra $\mathbb{C}\times\mathbb{C}\times M_2(\mathbb{C})$ and is the four-dimensional module with multiplicities $1,1,2$ over the three simples, not the regular module of $\mathbb{C}[C_3]$.

**Example.** Over $\mathbb{R}$ noncommutative division algebras occur. For the quaternion group $Q_8$,

$$
\mathbb{R}[Q_8] \cong \mathbb{R} \oplus \mathbb{R} \oplus \mathbb{R} \oplus \mathbb{R} \oplus \mathbb{H},
$$

with $r=5$ simple modules: four of dimension one and one of dimension two with endomorphism division ring $\mathbb{H}$. The basic algebra is $\mathbb{R}^4\oplus\mathbb{H}$, and $\mathbb{R}[Q_8]$ is not Morita equivalent to $\mathbb{R}[C_2\times C_2\times C_2]$, whose basic algebra is $\mathbb{R}^8$, nor is it Morita equivalent over $\mathbb{R}$ to any algebra with only real endomorphism rings.

### The modular case

When $\operatorname{char} F=p$ divides $|G|$, the group algebra is not semisimple and its indecomposable two-sided direct summands are the **blocks**:

$$
F[G]=\bigoplus_{b} B_b.
$$

Each block is an indecomposable $F$-algebra, and the module theory of $F[G]$ is the product of the module theories of its blocks, so the classification problem splits across blocks. Blocks are compared up to Morita equivalence; a block $B$ is Morita equivalent to $B'$ when they have the same module category, and this is the standard sense in which distinct groups can have "the same" modular representation theory. The theory of blocks and their Morita equivalences — Clifford theory for normal subgroups, Green correspondence, and the Picard group of a block — is a substantial subject, developed in the literature cited below. Two immediate facts follow from the general theory: Morita equivalent blocks have isomorphic centers, and a block is Morita equivalent to its basic algebra.

## Central Simple Algebras and the Brauer Group

Let $F$ be a field. A finite-dimensional $F$-algebra $A$ is **central simple** if $Z(A)=F$ and the only two-sided ideals are $0$ and $A$. By Wedderburn, every central simple $F$-algebra is of the form $M_n(D)$ for a division algebra $D$ with center $F$, and the integer $n$ and the division algebra $D$ are determined up to isomorphism.

**Theorem.** Two central simple $F$-algebras $A$ and $B$ are Morita equivalent if and only if they have the same underlying division algebra, i.e. $A\cong M_m(D)$ and $B\cong M_n(D)$ for the same division algebra $D$ with center $F$.

*Proof.* By the fundamental example, $M_m(D)$ and $M_n(D)$ are both Morita equivalent to $D$. Conversely, if $A\sim_M B$, then their simple modules have isomorphic endomorphism division rings by §Simple Modules under Morita Equivalence; the simple module of $M_n(D)$ is $D^n$ with endomorphism ring $D^{\mathrm{op}}$, so the underlying division algebras of $A$ and $B$ are isomorphic. $\square$

The set of Morita equivalence classes of central simple $F$-algebras therefore coincides with the set of isomorphism classes of finite-dimensional central division algebras over $F$, and it is a group under

$$
[A]\cdot[B]=[A\otimes_F B].
$$

This is the **Brauer group** $\operatorname{Br}(F)$. Morita equivalence is thus the equivalence relation that the Brauer group quotients out, and this is the reason Brauer-group computations are phrased in terms of matrix algebras.

**Example.** Over $\mathbb{R}$ the Frobenius theorem gives $\operatorname{Br}(\mathbb{R})=\mathbb{Z}/2$, with classes represented by $\mathbb{R}$ and $\mathbb{H}$. The quaternion algebra $\mathbb{H}$ is a division algebra with center $\mathbb{R}$, so it is not Morita equivalent to $\mathbb{R}$ over $\mathbb{R}$; but

$$
\mathbb{H} \otimes_{\mathbb{R}} \mathbb{C} \cong M_2(\mathbb{C}) \sim_M \mathbb{C},
$$

so the Brauer class of $\mathbb{H}$ becomes trivial after base change to $\mathbb{C}$. This is the algebraic content of the statement that $\mathbb{H}$ splits over $\mathbb{C}$, and it is the reason the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}\cong M_2(\mathbb{C})$ is Morita equivalent to $\mathbb{C}$.

## Summary

Morita equivalence is the equivalence relation on algebras generated by having equivalent module categories, equivalently by the existence of an $R$-linear equivalence $\operatorname{Mod}(A)\simeq\operatorname{Mod}(B)$. It is realized by a progenerator $P$ of left $A$-modules with $B\cong\operatorname{End}_A(P)^{\mathrm{op}}$, the equivalence being $\operatorname{Hom}_A(P,-)$ with quasi-inverse $P\otimes_B-$; equivalently, $B$ is a full corner $eM_n(A)e$ of a matrix algebra over $A$. The fundamental example is that $A$ and $M_n(A)$ are always Morita equivalent, via $P=A^n$, whose two endomorphism rings are $A^{\mathrm{op}}$ and $M_n(A^{\mathrm{op}})$. Morita equivalence preserves the center, the simple modules together with their endomorphism division rings, the finitely generated projectives and $K_0$, the lattice of two-sided ideals, and the isotypic structure of modules; it does not preserve the algebra, its dimension, its group of units, or algebra-level forms such as the trace and norm. Every finite-dimensional algebra is Morita equivalent to a unique basic algebra, and a semisimple algebra $\prod_i M_{n_i}(D_i)$ has basic algebra $\prod_i D_i$, so semisimple algebras over an algebraically closed field are classified up to Morita equivalence by the number of simple modules. For group algebras this gives $\mathbb{C}[G]\sim_M\mathbb{C}[H]$ exactly when $G$ and $H$ have the same number of conjugacy classes; in the modular case the group algebra splits into blocks and the comparison of blocks up to Morita equivalence is the organising principle. For central simple algebras the Morita equivalence classes are exactly the classes in the Brauer group, so $\operatorname{Br}(F)$ measures the failure of matrix algebras over $F$ to exhaust the central simple ones.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity, the base ring |
| $A$, $B$ | unital associative $R$-algebras |
| $F$ | a field |
| $\operatorname{Mod}(A)$ | category of left $A$-modules |
| $A \sim_M B$ | $A$ and $B$ are Morita equivalent |
| ${}_A P_B$ | $(A,B)$-bimodule |
| $P=A^n$ | free left $A$-module of rank $n$, a progenerator |
| $M_n(A)$ | matrix algebra over $A$ |
| $\operatorname{End}_A(P)$ | endomorphism ring of $P$, the endomorphism algebra |
| $B=\operatorname{End}_A(P)^{\mathrm{op}}$ | the algebra Morita equivalent to $A$ via $P$ |
| $\operatorname{Tr}_A(P)$ | trace ideal of $P$ |
| $eM_n(A)e$ | full corner ring of a matrix algebra |
| $A^{\mathrm{b}}=\operatorname{End}_A(\bigoplus_i P_i)^{\mathrm{op}}$ | basic algebra of $A$, with $P_i$ the projective covers |
| $J(A)$ | Jacobson radical |
| $S_i$ | simple modules up to isomorphism |
| $P_i$ | projective cover of $S_i$ |
| $D_i\cong\operatorname{End}_A(S_i)^{\mathrm{op}}$ | division ring of the $i$-th Wedderburn factor |
| $K_0(A)$ | Grothendieck group of finitely generated projective $A$-modules |
| $F[G]$ | group algebra of a finite group $G$ |
| $B_b$ | a block of $F[G]$ |
| $\operatorname{Br}(F)$ | Brauer group of $F$ |
| $\mathbb{H}$, $\mathbb{B}$ | quaternions, biquaternions |
| $\operatorname{Pic}(A)$ | Picard group of invertible bimodules |



## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for the Morita theorems, progenerators and equivalence of module categories.
- Hyman Bass, *Algebraic K-Theory* (Benjamin, 1968), for the Morita-invariance of $K_0$ and the Picard group.
- Nicolas Bourbaki, *Algebra VIII* (Springer, 2012), for the structure of semisimple algebras and the Brauer group.
- Charles W. Curtis and Irving Reiner, *Methods of Representation Theory, Vol. I* (Wiley, 1981), for blocks of group algebras and Morita equivalence of blocks.
- Yu. A. Drozd and V. V. Kirichenko, *Finite Dimensional Algebras* (Springer, 1994), for basic algebras, progenerators and the module category.
- Walter Feit, *The Representation Theory of Finite Groups* (North-Holland, 1982), for the modular representation theory in which block Morita equivalence is used.
- I. Martin Isaacs, *Character Theory of Finite Groups* (Academic Press, 1976), for Clifford theory and the reduction of group algebras by normal subgroups.
- Nathan Jacobson, *Basic Algebra II* (Dover, 2nd ed. 2009), for the Wedderburn theory behind the central simple case.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for Morita equivalence, the density theorem and simple algebras.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the basic algebra and the structure of finite-dimensional algebras.
