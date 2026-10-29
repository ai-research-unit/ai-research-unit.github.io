# __The Category of Modules__

## Introduction

Every module over the biquaternion algebra is a direct sum of copies of the simple module $\mathbb{C}^2$. This article states that classification, counts the multiplicities, reads the lattice of left ideals as a projective line, and identifies the double centraliser.

The article assumes the regular module and the minimal left ideals.

The classification is the Morita statement: $\mathbb{B}\cong M_2(\mathbb{C})$ is Morita equivalent to $\mathbb{C}$, so the category of left $\mathbb{B}$-modules is equivalent to the category of complex vector spaces, with the multiplicity as the dimension. The lattice of left ideals is the projective line over $\mathbb{C}$, read through the $M_2$ model; the proof is the one of the matrix model, and it is cited, not repeated.

## Representations and Modules

This section fixes the vocabulary of representations of the biquaternion algebra and records the dictionary between its representations and its modules. It constructs no representation and states no classification; those are the content of the classification below.

Throughout, $\mathbb{B}$ is the biquaternion algebra with the conventions of this article, its centre is $\mathbb{C}$, and a representation means a complex representation unless the real case is named.

**Definition.** A **representation** of $\mathbb{B}$ is a complex vector space $V$ together with a unital $\mathbb{C}$-algebra homomorphism

$$
\rho:\mathbb{B}\longrightarrow\operatorname{End}_\mathbb{C}(V),\qquad \rho(e_t)=\mathrm{id}_V,\qquad \rho(\tilde Q\tilde Q')=\rho(\tilde Q)\rho(\tilde Q').
$$

The **dimension** of the representation is $\dim_\mathbb{C}V$. Two representations $\rho,\rho'$ on $V,V'$ are **equivalent** when there is a $\mathbb{C}$-linear isomorphism $T:V\to V'$ with $T\rho(\tilde Q)=\rho'(\tilde Q)T$ for every $\tilde Q\in\mathbb{B}$. A **subrepresentation** is a $\mathbb{C}$-subspace $W\subseteq V$ carried into itself by every $\rho(\tilde Q)$; a representation is **irreducible**, or **simple**, when it has no proper nonzero subrepresentation, and **indecomposable** when it is not a direct sum of two proper subrepresentations. A representation is **faithful** when $\rho$ is injective.

A **real representation** of $\mathbb{B}$ is a real vector space $V$ together with a unital $\mathbb{R}$-algebra homomorphism from $\mathbb{B}$ read as a real algebra into $\operatorname{End}_\mathbb{R}(V)$; it is a separate category, related to the complex one by restriction of scalars, and the passage is *The Realification and the Effect of the Change of Scalars*.

**Theorem (representations are modules).** The representations of $\mathbb{B}$ are the left $\mathbb{B}$-modules: the action $\tilde Q\cdot v=\rho(\tilde Q)v$ makes $V$ a left $\mathbb{B}$-module, and conversely a left $\mathbb{B}$-module gives a representation by $\tilde Q\mapsto(v\mapsto\tilde Q\cdot v)$. The correspondence preserves dimension, subobjects, quotients, direct sums and equivalences, so the category of representations of $\mathbb{B}$ is the category of left $\mathbb{B}$-modules.

**Proof.** The module axioms are the homomorphism axioms read backwards: distributivity in the scalar is additivity of $\rho(\tilde Q)$, distributivity in the vector and the unit law are the two remaining homomorphism laws, and $(\tilde Q\tilde Q')\cdot v=\tilde Q\cdot(\tilde Q'\cdot v)$ is multiplicativity. A $\mathbb{B}$-module homomorphism is exactly an intertwining linear map, and direct sums are taken in the underlying complex vector spaces.

The theorem is the reason the chapter speaks of representations of $\mathbb{B}$ and of left $\mathbb{B}$-modules interchangeably, and it is the only dictionary used in what follows.

The structure of the category of left $\mathbb{B}$-modules — the simple modules, the classification of all representations up to equivalence, Schur's lemma, the intertwiners and the Morita equivalence — is the content of the sections below, and the present section supplies only the vocabulary those sections use.

## The Category of Left Modules

The classification of modules over $\mathbb{B}$ is complete and has no exceptional cases.

**Theorem.** Let $M$ be a left $\mathbb{B}$-module. Then $M$ is a direct sum of copies of $S$,

$$
\boxed{\;
M\cong S^{\oplus k}
\;},
$$

with $k$ an integer when $M$ is finitely generated. Every $\mathbb{B}$-module is projective. The left regular module is free of rank one over $\mathbb{B}$ and decomposes as

$$
\boxed{\;
{}_\mathbb{B}\mathbb{B}\cong S\oplus S
\;},
$$

the two summands being the two columns $\mathbb{B}\tilde\Pi_+$ and $\mathbb{B}\tilde\Pi_-$.

*Proof.* The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is simple and artinian, hence semisimple; over a semisimple ring every module is a direct sum of simple modules, every module is projective, and there is a single simple module up to isomorphism. The decomposition of the regular module is the Peirce decomposition read column by column, and freeness of rank one is the basis $e_t$.

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

**The opposite algebra.** The **opposite algebra** $A^{\mathrm{opp}}$ of an algebra $A$ has the same additive group and the reversed product, $a^{\mathrm{opp}}\cdot b^{\mathrm{opp}}=(ba)^{\mathrm{opp}}$; the construction in general is *Opposite Algebras and Anti-Isomorphisms*. For $\mathbb{B}$ the quaternion conjugation is an anti-automorphism, $(\tilde Q_1\tilde Q_2)^{\natural}=\tilde Q_2^{\natural}\tilde Q_1^{\natural}$, hence an isomorphism $\mathbb{B}^{\mathrm{opp}}\to\mathbb{B}$: the opposite of the biquaternion algebra is the algebra itself.

The dual is not a new module. Let $S^*=\operatorname{Hom}_\mathbb{C}(S,\mathbb{C})$ carry the contragredient action, a right $\mathbb{B}$-module and hence a left $\mathbb{B}^{\mathrm{opp}}$-module; under that identification $S^*$ is simple of complex dimension two and therefore isomorphic to $S$.

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

Recall that over a commutative domain a nonzero module element $m$ is torsion when $\operatorname{Ann}(m)\neq0$, an invariant that classifies finitely generated modules over a principal ideal domain (*Modules over a PID*). Over $\mathbb{B}$ the definition collapses. The algebra has zero divisors, treated in *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, *Zero Divisors and Units*, and for every nonzero $s\in S$ the annihilator

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

### Complete reducibility

**Corollary (complete reducibility).** Every left $\mathbb{B}$-module is semisimple: it is a direct sum of copies of $S$, and by the Morita equivalence of §*Morita Equivalence with the Complex Field* it is $S\otimes_\mathbb{C}W$ for a complex vector space $W$, of complex dimension $2\dim_\mathbb{C}W$. The regular module is the particular case $W=\mathbb{C}^2$.

**Remark (the minimal left ideals and the lines of $S$).** The minimal left ideals of $\mathbb{B}$ are the two-dimensional subspaces

$$
L_\ell=\{\tilde Q:\tilde Q S\subseteq\ell\},\qquad \ell \text{ a line in } S,
$$

one for each line $\ell$, so the family of minimal left ideals is a projective line; the two summands of the regular module correspond to the two coordinate lines, and the general element of the family is $\mathbb{B}\tilde\Pi$ for a rank-one idempotent $\tilde\Pi$ with image $\ell$. The classification is that of *The Minimal Left Ideals*; the reading here is that these are the simple submodules of the regular module.

### Von Neumann regular and self-injective

**Proposition.** The algebra $\mathbb{B}$ is von Neumann regular: for every $\tilde Q\in\mathbb{B}$ there is a $\tilde Q_5\in\mathbb{B}$ with $\tilde Q\tilde Q_5\tilde Q=\tilde Q$. It is self-injective: as a left module over itself it is injective, so every $\mathbb{B}$-linear map from a submodule of ${}_{\mathbb{B}}\mathbb{B}$ to ${}_{\mathbb{B}}\mathbb{B}$ extends to ${}_{\mathbb{B}}\mathbb{B}$.

**Proof.** Both properties are properties of the algebra $\mathbb{B}\cong M_2(\mathbb{C})$: it is von Neumann regular, and it is self-injective because it is a Frobenius algebra, the trace providing the non-degenerate associative pairing. Both are preserved by isomorphism, and the injectivity statement is the Baer criterion applied to ${}_{\mathbb{B}}\mathbb{B}$.

**Corollary (the regular module is projective and injective).** The left regular module is free and therefore projective, and it is injective by the proposition; the two properties together mean that ${}_{\mathbb{B}}\mathbb{B}$ is a projective generator and an injective cogenerator of the module category, the reference object from which every module is built by direct sums, quotients and submodules.

## The Lattice of Left Ideals

**The left ideals are $0$, the minimal left ideals and $\mathbb{B}$; the middle layer is a projective line, and every minimal left ideal is maximal.**

The two-sided lattice is the two-element chain $0\subset\mathbb{B}$ of *The Regular Module*, §*The Two-Sided Ideals*; the lattice with a middle layer is the left one.

Over $\mathbb{C}$, every left ideal of the simple artinian algebra $\mathbb{B}$ is a direct sum of minimal left ideals, so the left ideals are exactly $0$, the minimal ones, and $\mathbb{B}$.

| Left ideal | Form | Dimension over $\mathbb{C}$ | Minimal | Maximal |
|---|---|---|---|---|
| $0$ | $0$ | $0$ | no | no |
| minimal | $\mathbb{B}\tilde\Pi$, $\tilde\Pi$ primitive | $2$ | yes | yes |
| $\mathbb{B}$ | $\mathbb{B}$ | $4$ | no | no |

The minimal left ideals form the middle layer of the lattice,

$$
0 \;\subset\; \{\, L : L \text{ a minimal left ideal} \,\} \;\subset\; \mathbb{B},
$$

the elements of the middle layer being pairwise incomparable, each covering $0$ and covered by $\mathbb{B}$. Because the length of $\mathbb{B}$ as a left module over itself is $2$, every minimal left ideal is also a **maximal** left ideal, nothing lying strictly between it and $\mathbb{B}$. The minimal left ideals are parametrized by the projective line $\mathbb{P}^1(\mathbb{C})$. Right ideals admit the same description, with the dual parametrization.

The parameter space deserves a caution. In the Wedderburn–Artin decomposition $M_n(D)$ of a simple artinian algebra, the minimal one-sided ideals are parametrized by the projective space $\mathbb{P}^{n-1}(D)$ over the **division ring** $D$, not over an arbitrary base field. Here $D = \mathbb{C}$ and $n = 2$, so the parameter space is $\mathbb{P}^1(\mathbb{C})$. In particular, regarding $\mathbb{B}$ as an $\mathbb{R}$-algebra does not replace this by $\mathbb{P}^1(\mathbb{R})$: the one-sided ideals are still parametrized by $\mathbb{P}^1(\mathbb{C})$. The real projective line appears only as the subfamily that the real structure preserves, not as a set of fixed minimal left ideals: §*The Projective Line and the Möbius Action* below shows that no minimal left ideal is stable under coefficient conjugation.

## The Projective Line and the Möbius Action

**The middle layer of the lattice is the projective line of the defining module, the units act on it by left multiplication, and in a chart the action is the Möbius action of $PGL_2(\mathbb{C})$.**

**The parametrisation.** Let $S$ be the defining module, of complex dimension two, and let $\mathbb{P}(S)$ be its projective line. A minimal left ideal is the set of elements of $\mathbb{B}$ whose action on $S$ has image contained in a fixed line $L\in\mathbb{P}(S)$,

$$
\mathbb{B}\tilde\Pi_L=\{\tilde Q:\tilde Q S\subseteq L\},
$$

where $\tilde\Pi_L$ is any rank-one idempotent with image $L$. The assignment $L\mapsto\mathbb{B}\tilde\Pi_L$ is a bijection

$$
\mathbb{P}(S)\;\longrightarrow\;\{\text{minimal left ideals}\},
$$

because two rank-one idempotents with the same image generate the same left ideal, and every minimal left ideal is generated by a primitive idempotent, hence has a rank-one image. Choosing a basis of $S$ identifies $\mathbb{P}(S)$ with $\mathbb{P}^1(\mathbb{C})$, the parametrisation of §*The Lattice of Left Ideals*.

**The action.** For $\tilde Q\in\mathbb{B}^\times$ and a minimal left ideal $L$, put

$$
\tilde Q\cdot L=\tilde Q L .
$$

Left multiplication by a unit is an isomorphism of left modules, so it carries minimal left ideals to minimal left ideals and defines an action of $\mathbb{B}^\times$ on the projective line. In the model it is the action of the matrix $P=\mathsf M_2(\tilde Q)$ on the lines of $\mathbb{C}^2$,

$$
\tilde Q\cdot[\xi]=[P\xi].
$$

**The kernel is the centre.** An element acts trivially on every line exactly when every vector of $S$ is carried to a multiple of itself, and a matrix with that property is scalar; hence the kernel of the action is $\mathbb{C}^\times e_t$. The action therefore factors through

$$
\mathbb{B}^\times/\mathbb{C}^\times e_t\cong PGL_2(\mathbb{C})\cong\operatorname{Aut}_{\mathbb{C}}(\mathbb{B}),
$$

the last isomorphism being that of *Biquaternion Automorphisms and Derivations*. On idempotents the action reads $\tilde\Pi\mapsto\tilde Q\tilde\Pi\tilde Q^{-1}$, which is the conjugation action of the automorphism group; the two descriptions agree because $\tilde Q\mathbb{B}\tilde\Pi=\mathbb{B}(\tilde Q\tilde\Pi\tilde Q^{-1})$.

**The chart and the Möbius formula.** Write a line by the column $\xi=(z,1)^{\mathsf T}$, with $z=\xi_1/\xi_2$, and let $P=\begin{pmatrix}a&b\\c&d\end{pmatrix}$. Then

$$
P\xi=\begin{pmatrix}az+b\\ cz+d\end{pmatrix},
\qquad
z'=\frac{az+b}{cz+d},
$$

which is the Möbius transformation attached to $P$. A nonzero scalar multiple of $P$ gives the same transformation, so the formula depends only on the class $[P]\in PGL_2(\mathbb{C})$, and composition of transformations is multiplication of matrices. In this chart the idempotent $\tilde\Pi_-$ sits at $z=0$ and $\tilde\Pi_+$ at $z=\infty$; the point at infinity is the line of the first basis vector.

**Transitivity and stabilisers.** The action is transitive, since any line can be sent to any other by an invertible matrix, and it is simply transitive on ordered triples of distinct points. The stabiliser of $z=0$ is the set of matrices with $b=0$,

$$
\left\{\begin{pmatrix}a&0\\c&d\end{pmatrix}:ad\neq0\right\},
$$

a Borel subgroup of $PGL_2(\mathbb{C})$, of complex dimension two.

**The real structure.** Coefficient conjugation $\sigma$ acts on the lattice by the antiholomorphic involution, $t\mapsto-1/\bar t$ in the chart above, with no fixed point; no minimal left ideal is therefore stable under it, and the real structure preserves the subfamily $\mathbb{P}^1(\mathbb{R})$, on which it acts as the antipodal map. Since $\sigma$ is $\mathbb{C}$-antilinear, it intertwines the action of a unit with that of its image, $\sigma\circ\varphi_{\tilde Q}=\varphi_{\sigma(\tilde Q)}\circ\sigma$; the two actions are not the same action, and the real structure pairs the orbit of a line under $\mathbb{B}^\times$ with the orbit of its conjugate.

## Summary

- The algebra is Morita equivalent to $\mathbb{C}$: the category of left $\mathbb{B}$-modules is equivalent to the category of complex vector spaces.
- Every module is a direct sum of copies of the simple module $\mathbb{C}^2$; the multiplicity is its dimension as a complex vector space.
- The regular module is the sum of the two minimal left ideals, each with multiplicity one.
- The left ideals of $\mathbb{B}$ form the lattice $0\subset L\subset\mathbb{B}$, with the lines $L$ parametrised by $\mathbb{P}^1$; the Möbius action is the action of the units by change of basis.
- The double centraliser of a simple module is the algebra, and the double centraliser of an element is its centraliser.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}^2$ | the simple left module |
| $\mathbb{P}^1$ | the lattice of one-dimensional left ideals |
| $\operatorname{End}_\mathbb{B}(\mathbb{B})$ | the endomorphism ring of the regular module |

## Further Reading

- [The Regular Module](the-regular-module.html), for the ideals as submodules.
- [The Minimal Left Ideals](the-minimal-left-ideals.html), for the simple module in the algebra.
- [The Centraliser](the-centraliser.html), for the commutant of an element.
- [$M_2(\mathbb{C})$ Model : Peirce Coordinates, Matrix Units and the Spinor Planes](m2c-model-the-peirce-coordinates-matrix-units-and-the-spinor-planes.html), for the matrix model of the classification.
