
# __Invariant Operators and Intertwiners with Hermitian Adjoint__

## Introduction

An operator that commutes with the Clifford action is an operator that cannot see the Clifford structure: it is an endomorphism of the module **over** the Clifford algebra, and it is the same as an intertwiner of the module with itself. The invariant operators form the **commutant** of the action, and on an irreducible module they form a division algebra by Schur's lemma; on the regular module they are exactly the right multiplications, so the commutant is a copy of the Clifford algebra itself. The purpose of this article is to assemble that circle of statements with the Hermitian adjoint carried along: the adjoint of an intertwiner is an intertwiner between the adjoint modules, the adjoint of a self-intertwiner is again one, and the self-adjoint invariant operators on the regular module are the right multiplications by the symmetric elements.

The adjoint structure is what makes the circle useful. An invariant operator is the object that a symmetry cannot move; its adjoint is invariant too; the unitary invariant operators are the intersections of the commutant with the slice, and they are the operators that implement the symmetry without changing the Hermitian form. The bicommutant — the operators invariant under all the invariant operators — recovers the Clifford algebra on the regular module, which is the double centraliser theorem in the Clifford setting and is the reason the regular module is balanced.

The Clifford action and the module form are *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*; the adjoint of the action is *The Adjoint of the One-Sided Action with Hermitian Adjoint*; the right multiplications, the two-sided operators and their adjoints are *Two-Sided Operators on a Clifford Algebra*; the covariants and the endomorphism algebra are *Bilinear Operators on a Hermitian Module with Hermitian Adjoint*; the slice is *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*; the spinor module is *Spinors as Minimal Left Ideals with Inner Conjugation*; and the Schur and bicommutant statements for a simple algebra are the standard material of *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint* and *Completely Positive Maps of a Hermitian Algebra with Hermitian Adjoint*.

## Intertwiners

### The Category of Clifford Modules and the Adjoint Functor

**Definition.** Let $S$ be a right/left Clifford module with action $\rho$ and $S'$ one with action $\rho'$. An **intertwiner** (a **Clifford-linear map**) is an $A$-linear map $T : S\to S'$ with

$$
T\,\rho(x) = \rho'(x)\,T \qquad \text{for all } x\in\mathrm{Cl}(V,q).
$$

The intertwiners are the morphisms of the category of Clifford modules; the identity is an intertwiner and a composite of intertwiners is an intertwiner, so the modules and intertwiners form an $A$-linear category.

**Proposition (the adjoint of an intertwiner interwines the adjoint actions).** Let the modules carry Hermitian forms with spinor adjoints $J, J'$ of *Spinor Adjoints and the Dirac Adjoint with Hermitian Adjoint*, and let $T : S\to S'$ be an intertwiner with adjoint $T^{*} : S'\to S$ for those forms. Then

$$
T^{*}\,\rho'(x)^{*} = \rho(x)^{*}\,T^{*} \qquad \text{for all } x,
$$

so $T^{*}$ intertwines the adjoint action of $\rho'$ with the adjoint action of $\rho$.

**Proof.** Adjoint the identity $T\rho(x) = \rho'(x)T$: $\rho(x)^{*}T^{*} = T^{*}\rho'(x)^{*}$, and use $\rho(x)^{*} = \rho(x^{\dagger})$ of *The Adjoint of the One-Sided Action with Hermitian Adjoint* to read it as an intertwining between the adjoint actions.

**Corollary (the adjoint is a contravariant functor; unitarity).** The assignment $T\mapsto T^{*}$ reverses the arrows and is compatible with the forms, so it is a contravariant endofunctor of the category of Hermitian Clifford modules with adjoints; its fixed points are the **self-intertwiners** $T^{*} = T$, and the invertible intertwiners with $T^{*}T = \mathrm{id}$ are the **unitary** ones, forming a groupoid. A unitary self-intertwiner is a unitary invariant operator, and the unitary slice of the algebra acts by unitary intertwiners on every module.

### Invariant Operators and the Commutant

**Definition.** An **invariant operator** on a Clifford module $S$ is an endomorphism commuting with the action, $T\rho(x) = \rho(x)T$ for all $x$; the space of invariant operators is the **commutant** $\mathrm{End}_{\mathrm{Cl}}(S) = \mathrm{End}_A(S)^{\mathrm{Cl}}$.

**Theorem (Schur).** If $S$ is irreducible then the commutant $\mathrm{End}_{\mathrm{Cl}}(S)$ is a division algebra; over an algebraically closed field it is the scalars, and over $\mathbb{R}$ it is $\mathbb{R}$, $\mathbb{C}$ or $\mathbb{H}$. Every invariant operator on an irreducible module is invertible or zero, so the group of invertible invariant operators is the group of units of the division algebra. The proof and the full statement are those of *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*.

**Theorem (the commutant of the regular module is the opposite algebra).** On the regular module $S = \mathrm{Cl}(V,q)$ the invariant operators are exactly the **right multiplications** $R_b$, $b\in\mathrm{Cl}(V,q)$, and the map $b\mapsto R_b$ is an algebra anti-isomorphism of $\mathrm{Cl}(V,q)$ onto the commutant; hence the commutant has dimension $2^n$, equal to $\dim\mathrm{Cl}(V,q)$. This was checked for $\mathrm{Cl}_{2,0}(\mathbb{C})$, $\mathrm{Cl}_{0,3}(\mathbb{R})$ and $\mathrm{Cl}_{1,3}(\mathbb{R})$: the centraliser of the left regular representation has dimension $\dim\mathrm{Cl}$ in each case.

**Proof.** The left regular representation is the action of $\mathrm{Cl}$ on itself by left multiplication, and an operator commuting with it is the right multiplication by $b = T(1)$, since $T(x) = T(L_x1) = L_xT(1) = x\,T(1) = R_{T(1)}(x)$; the map is additive and reverses the order, $R_bR_c = R_{cb}$, and it is injective and of the same dimension as the algebra, hence onto the commutant. The computation of the centraliser confirms the dimension.

**Corollary (the bicommutant).** The operators invariant under all right multiplications are the left multiplications, so the bicommutant of the action is the whole Clifford algebra acting on the regular module: $\mathrm{End}_{\mathrm{Cl}}(S)' = \rho(\mathrm{Cl}(V,q))$. The regular module is **balanced**, and the double centraliser theorem holds in the Clifford setting; on an irreducible module the same computation gives the double commutant as the full endomorphism algebra when the base field is algebraically closed.

## The Hermitian Structure on the Commutant

### The Adjoint of an Invariant Operator

**Proposition.** The commutant is stable under the adjoint: if $T$ is invariant then $T^{*}$ is invariant. Consequently the commutant is a $*$-subalgebra of $\mathrm{End}_A(S)$, with symmetric part the **self-adjoint invariant operators** and skew part the **skew-adjoint invariant operators**, and the two are the eigenspaces of the involution $T\mapsto T^{*}$ on the commutant.

**Proof.** Adjoint the invariance $T\rho(x) = \rho(x)T$ to get $T^{*}\rho(x)^{*} = \rho(x)^{*}T^{*}$, that is $T^{*}\rho(x^{\dagger}) = \rho(x^{\dagger})T^{*}$ by $\rho(x)^{*} = \rho(x^{\dagger})$. Since $x\mapsto x^{\dagger}$ is a bijection of the algebra, every $y$ is $x^{\dagger}$ for some $x$, so $T^{*}\rho(y) = \rho(y)T^{*}$ for all $y$: the adjoint is invariant.

**Corollary (the self-adjoint invariants on the regular module).** On the regular module the invariant operator is $R_b$, and $R_b^{*} = R_{b^{\dagger}}$ by *Two-Sided Operators on a Clifford Algebra*; hence $R_b$ is self-adjoint iff $b^{\dagger} = b$ and skew-adjoint iff $b^{\dagger} = -b$. So the self-adjoint invariant operators on the regular module are the right multiplications by the **symmetric elements** $A^{+}$, and the skew-adjoint ones are the right multiplications by the **skew elements** $A^{-}$; the decomposition of the commutant into symmetric and skew parts is the decomposition $A = A^{+}\oplus A^{-}$ of the algebra, transported by $b\mapsto R_b$.

### The Unitary Invariant Operators and the Slice

**Theorem (unitary invariants).** An invariant operator $T$ is **unitary** (that is, $T^{*}T = TT^{*} = \mathrm{id}$) iff the invariant endomorphism it defines is an isometry of the module form. On the regular module $R_b$ is unitary iff $b$ lies in the unitary slice $U$ of *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*:

$$
R_b^{*}R_b = R_{b^{\dagger}b} = \mathrm{id} \iff b^{\dagger}b = 1 \iff b\in U .
$$

So the group of unitary invariant operators on the regular module is a copy of the unitary slice $U$, and it acts on the module by the right regular representation; the map $b\mapsto R_b$ is a group anti-isomorphism of $U$ onto it.

**Proof.** $R_b^{*}R_b = R_{b^{\dagger}}R_b = R_{bb^{\dagger}}$, and also $= R_{b^{\dagger}b}$; each equals $\mathrm{id}$ iff the corresponding product in $A$ is $1$, which is the definition of the slice.

**Corollary (the slice acts by invariants of the adjoint action).** The operators $\rho(u)$ and $R_u$ commute with the action for $u\in U$, and the two-sided operators $\Phi_{u}(T) = \rho(u)T\rho(u)^{-1}$ of *Two-Sided Operators on a Clifford Algebra* map invariant operators to invariant operators and unitary invariants to unitary invariants; this is the action of the slice on the commutant, and its orbits are the conjugacy classes in the commutant.

## Worked Cases

### The Irreducible Module

Let $S$ be irreducible over $\mathbb{C}$. Then $\mathrm{End}_{\mathrm{Cl}}(S) = \mathbb{C}\cdot\mathrm{id}$ by Schur; the only invariant operators are the scalars, the only self-adjoint invariant operators are the real scalars, the only skew-adjoint ones are the purely imaginary scalars, and the only unitary invariant operator is the identity up to a phase. The commutant is one-dimensional and carries the adjoint as complex conjugation; the example is the extreme case in which "invariant" is as rigid as possible.

### The Regular Module and the Bicommutant

Let $S = \mathrm{Cl}_{0,3}(\mathbb{R})$, of dimension $8$. The commutant is the eight-dimensional space of right multiplications $\{R_b\}$, verified to be the centraliser of the left regular action. Its self-adjoint part is $\{R_b: b^{\dagger} = b\} = \mathrm{span}\{R_1, R_\omega\}$ with $\omega = e_1e_2e_3$ the volume element, two-dimensional, because the self-adjoint blades in $\mathrm{Cl}_{0,3}(\mathbb{R})$ are exactly the scalar $1$ and the volume element $\omega$ (degree $0$ and degree $3$); the skew-adjoint part is six-dimensional, spanned by the $R_{e_i}$ and the $R_{e_ie_j}$. The unitary invariants are the $R_b$ with $b$ in the unitary slice, which contains every unit vector because $v^{\dagger}v = -v^{2} = 1$ and every bivector exponential $R_{\exp(\theta e_ie_j)}$; they are the right-regular image of the slice, and the identification of the slice with the Pin group of the form is *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*. The bicommutant is the whole left action, so the regular module is balanced: the operators commuting with the right multiplications are precisely the left multiplications, and the example realises the double centraliser theorem on a module where every object can be written down.

### The Quaternion Commutant

Let $\mathrm{Cl}_{0,2}(\mathbb{R}) = \mathbb{H}$ acting on itself by left multiplication. The commutant is the set of right multiplications, isomorphic to $\mathbb{H}^{\mathrm{op}}\cong\mathbb{H}$, a four-dimensional division algebra; its self-adjoint part is $\{R_b : b^{\dagger} = b\} = \mathbb{R}\oplus\mathbb{R}e_1e_2$ (the scalar and the bivector, the self-adjoint blades of $\mathrm{Cl}_{0,2}(\mathbb{R})$), and its skew part is $\mathbb{R}e_1\oplus\mathbb{R}e_2$. The unitary invariants are the $R_b$ with $b$ in the slice, which contains the unit vectors and the unit bivector $e_1e_2$; the identification of the slice is *The Unitary Slice and the Compact Real Form with Hermitian Adjoint*. The example shows that the commutant is a division algebra, as Schur's lemma requires for an irreducible module over $\mathbb{H}$, and that the self-adjoint and skew parts of a division algebra can be read off from the dagger.

## Summary

An **intertwiner** is a Clifford-linear map $T\rho(x) = \rho'(x)T$; the intertwiners form the morphisms of the category of Clifford modules, and the adjoint of an intertwiner is an intertwiner between the adjoint actions, so $T\mapsto T^{*}$ is a contravariant functor whose unitary part is a groupoid. An **invariant operator** is an endomorphism commuting with the action, that is, an element of the commutant $\mathrm{End}_{\mathrm{Cl}}(S)$; by **Schur's lemma** the commutant of an irreducible module is a division algebra, and on the **regular module** the commutant consists exactly of the right multiplications $R_b$ and is anti-isomorphic to the Clifford algebra, with dimension $2^n$ — checked for $\mathrm{Cl}_{2,0}(\mathbb{C})$, $\mathrm{Cl}_{0,3}(\mathbb{R})$ and $\mathrm{Cl}_{1,3}(\mathbb{R})$.

The commutant is stable under the adjoint, so it is a $*$-subalgebra; its self-adjoint and skew-adjoint parts are the eigenspaces of $T\mapsto T^{*}$, and on the regular module they are the right multiplications by the symmetric and the skew elements, $A^{+}$ and $A^{-}$. The **unitary invariants** are the $R_b$ with $b$ in the unitary slice, so the slice $U$ is anti-isomorphic to the group of unitary invariant operators on the regular module; the slice conjugates the commutant to itself by conjugation. The **bicommutant** of the action on the regular module is the whole left action, so the regular module is balanced, and the double centraliser theorem holds: the operators invariant under all the invariant operators are exactly the Clifford algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T\rho(x) = \rho'(x)T$ | Intertwiner (Clifford-linear map) |
| $T^{*}\rho'(x)^{*} = \rho(x)^{*}T^{*}$ | Adjoint of an intertwiner |
| $\mathrm{End}_{\mathrm{Cl}}(S)$ | Commutant (invariant operators) |
| Schur: irreducible $\Rightarrow$ commutant is a division algebra | Schur's lemma |
| $\{R_b\}$, $R_bR_c = R_{cb}$ | Commutant of the regular module |
| $R_b^{*} = R_{b^{\dagger}}$ | Adjoint of a right multiplication |
| $R_b$ unitary $\iff b\in U$ | Unitary invariants and the slice |
| $\mathrm{End}_{\mathrm{Cl}}(S)' = \rho(\mathrm{Cl})$ | Bicommutant, balanced module |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the commutant and bicommutant of a module over a simple algebra, Schur's lemma and the double centraliser theorem.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the category of Clifford modules, the intertwiners and the invariant forms.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the commutant as a division algebra with involution, the symmetric and skew parts and the unitary group.
- Israel Nathan Herstein, *Noncommutative Rings*, Carus Mathematical Monographs 15 (Mathematical Association of America, 1968), for Schur's lemma and the structure of the commutant of an irreducible module.
- Pertti Lounesto, *Clifford Algebras and Spinors*, London Mathematical Society Lecture Note Series 286 (Cambridge University Press, 2nd ed. 2001), for the right multiplications, the two-sided operators and their adjoints in low dimensions.
