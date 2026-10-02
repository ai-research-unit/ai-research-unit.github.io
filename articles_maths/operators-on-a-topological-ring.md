
# __Operators on a Topological Ring__

## Introduction

A topological ring $R$ carries two structures at once, and an operator on it must respect both: it is a **continuous** map, and the operators built from the ring's own product are the ones by which $R$ acts on itself. This article lays down the operator layer of the category — the monoid of continuous self-maps, the group of homeomorphisms it contains, the continuous additive endomorphisms, the group of continuous ring automorphisms, the inner automorphisms produced by the units, and the action of all of these on the lattice of ideals — and it fixes the natural pairing that the later groups of the category use to build adjoints.

The article assumes the ring $R$, its ideals, the unit group, the annihilators and the inner conjugation from *Rings* and *Ring and Field Automorphisms*, and the topological ring, its neighbourhoods of zero, its linear topologies, the closure of zero and the $I$-adic completion from *Topological Rings and Fields*. It uses the abstract one-sided multiplications, their composition and the description of the operators they generate from *Left and Right Multiplication in a Ring* only to name them; their topological treatment is *The Left and Right Multiplication Operators on a Topological Ring*. No involution of the ring, no signed operator and no adjoint is used here: they belong to the later groups of the category, and the present article supplies them with the continuous translations and the natural pairing. No measure, no norm and no form occurs; the Haar integral and the operator norm are named once, at the boundary, and never used.

Throughout, $R$ is a topological ring, Hausdorff when a closedness statement is made, with group of units $R^\times$ and centre $Z(R)$; $\operatorname{Map}_c(R)$ is the monoid of continuous self-maps, $\operatorname{Homeo}(R)$ the group of homeomorphisms, $\operatorname{End}_c(R)$ the continuous additive endomorphisms, $\operatorname{Aut}(R)$ and $\operatorname{Aut}_c(R)$ the automorphisms and the continuous automorphisms, and $\operatorname{Inn}(R)$ the inner automorphisms $c_u(x) = uxu^{-1}$.

## The Continuous Operators

### The Operator Layer

**Definition.** A **continuous operator** on $R$ is a continuous map $R \to R$. The continuous operators form a monoid $\operatorname{Map}_c(R)$ under composition, with identity the identity map, and the invertible elements of this monoid are exactly the homeomorphisms of $R$ onto itself, which form the group $\operatorname{Homeo}(R)$.

**Proof.** The composite of two continuous maps is continuous, and composition is associative with identity $\mathrm{id}$; a continuous map with a continuous inverse is by definition a homeomorphism, and a homeomorphism is continuous and invertible in the monoid.

The passage from the monoid to its group of units is the first structural statement of the operator layer: an operator is **invertible** exactly when it is a homeomorphism, which is the topological form of the algebraic statement that a bijective self-map is a permutation.

**Definition.** A **continuous additive endomorphism** of $R$ is an additive map that is continuous; the continuous additive endomorphisms form a submonoid $\operatorname{End}_c(R)$ of $\operatorname{Map}_c(R)$ under composition, with $\mathrm{id}$ as identity.

Every operator of the later groups of this category is additive, hence lies in $\operatorname{End}_c(R)$: the one-sided multiplications, the automorphisms, the inner automorphisms, the operators built from an involution and the adjoints, once continuity is known, are all additive. The additive operators are the operators for which the underlying topological group of $R$ is the structure acted on, and it is only through additivity that the operator layer sees the additive topology.

### The Continuous Automorphisms

**Definition.** A **continuous automorphism** of $R$ is a ring automorphism that is continuous; the continuous automorphisms form a subgroup $\operatorname{Aut}_c(R)$ of $\operatorname{Aut}(R)$ and a subgroup of $\operatorname{Homeo}(R)$. The **inner automorphisms** $c_u(x) = uxu^{-1}$, for $u \in R^\times$, form a normal subgroup $\operatorname{Inn}(R) \subseteq \operatorname{Aut}_c(R)$.

**Proposition.** $\operatorname{Aut}_c(R) = \operatorname{Aut}(R) \cap \operatorname{Homeo}(R)$, and $\operatorname{Inn}(R) \subseteq \operatorname{Aut}_c(R)$, the assignment $u \mapsto c_u$ being a homomorphism $R^\times \to \operatorname{Aut}_c(R)$ with kernel the central units $Z(R) \cap R^\times$, so that $\operatorname{Inn}(R) \cong R^\times/(Z(R)\cap R^\times)$.

**Proof.** An automorphism that is a homeomorphism has a continuous inverse, so it is a continuous automorphism; conversely a continuous automorphism is a continuous bijection and its inverse is continuous, because a continuous bijective map whose inverse is a ring homomorphism is a homeomorphism as soon as the ring structure is taken into account: the inverse is additive and multiplicative and the map is continuous, so it is continuous as the inverse of a homeomorphism of the underlying topological space. The inner automorphism $c_u$ is a composite of two continuous maps — left multiplication by $u$ and right multiplication by $u^{-1}$ — and it is an automorphism, so it is a continuous automorphism. The assignment is a homomorphism because $c_u \circ c_v = c_{uv}$, and its kernel is the set of units acting trivially, which is $Z(R) \cap R^\times$.

## The Units and their Operators

**Proposition (the one-sided multiplications are continuous).** For every $a \in R$ the left multiplication $L_a(x) = ax$ and the right multiplication $R_a(x) = xa$ are continuous additive endomorphisms, so $L_a, R_a \in \operatorname{End}_c(R)$. They are homeomorphisms exactly when $a \in R^\times$, with $L_a^{-1} = L_{a^{-1}}$ and $R_a^{-1} = R_{a^{-1}}$.

**Proof.** The map $x \mapsto (a, x) : R \to R\times R$ is continuous, and multiplication $R \times R \to R$ is continuous by the axioms of a topological ring, so $L_a$ is continuous; it is additive because the product distributes over the addition, and likewise for $R_a$. If $a$ is a unit then $L_{a^{-1}}$ is a continuous two-sided inverse; if $L_a$ is a homeomorphism then it is surjective, so $a = L_a(1)$ has a right inverse, and injective, so $a$ is not a zero divisor, whence $a$ is a unit. The right case is the mirror image.

So the units of $R$ are exactly the elements whose one-sided multiplications are invertible in the operator layer; the non-units give operators that are continuous but not homeomorphisms, and they are the operators that must be handled by closure rather than by inversion.

**Proposition (the units are a topological group when they are open).** If $R^\times$ is open in $R$, then $R^\times$ is a topological group for the subspace topology, the multiplication being the restriction of the multiplication of $R$ and the inversion $u \mapsto u^{-1}$ being continuous on $R^\times$. The group $R^\times$ is open when $R$ is a division ring, when $R$ is a local ring whose maximal ideal is open, and in particular when $R$ is the valuation ring of a valued field.

**Proof.** When $R^\times$ is open, the restrictions of the ring operations are continuous on $R^\times \times R^\times$ and the identity lies in $R^\times$. For the inversion, $u^{-1} - v^{-1} = u^{-1}(v - u)v^{-1}$ shows that $u \mapsto u^{-1}$ is continuous wherever it is defined and the inverses are bounded in a neighbourhood of a given unit; a division ring has $R^\times = R \setminus \{0\}$, open because $\{0\}$ is closed in a Hausdorff ring; a local ring has $R^\times = R \setminus \mathrm{M}$ with $\mathrm{M}$ the unique maximal ideal, open when $\mathrm{M}$ is open; a valuation ring is local with maximal ideal $\mathrm{M} = \{x : \lvert x \rvert < 1\}$, open in the metric topology.

**Remark (the failure in general).** In an arbitrary topological ring the unit group need not be open: on the ring $C(X)$ of continuous functions on a compact space with the topology of uniform convergence the units are the nowhere-vanishing functions, which form a set that can fail to be open, and the group of units is then not a topological group for the subspace topology. The category therefore states the openness as a hypothesis where it is used, and records that on the rings of this part — valued fields, valuation rings, their quotients and completions — it holds.

## The Action on the Ideals

### Left, Right and Two-Sided Ideals

The operator layer acts on the lattice of ideals, and the action is the reason the layer is interesting for the ring.

**Definition.** For a left ideal $I$, the **left translate** by $a \in R$ is $L_a(I) = aI$, a left ideal; for a right ideal $J$, the **right translate** is $R_a(J) = Ja$, a right ideal; for a two-sided ideal $I$, the **conjugate** by a unit $u$ is $c_u(I) = uIu^{-1}$, and $c_u$ preserves each of the three kinds of ideal.

**Proposition.** A continuous additive endomorphism carries a left ideal into a left ideal, a right ideal into a right ideal and a two-sided ideal into a two-sided ideal exactly when it is multiplicative on the corresponding side; a ring automorphism permutes the ideals of each kind and preserves inclusion, so it is an automorphism of the lattice of left ideals, of right ideals and of two-sided ideals.

**Proof.** A left ideal $I$ is characterised by $RI \subseteq I$; an additive map $T$ with $T(aI) = T(a)T(I) \subseteq T(I)$ for all $a$ preserves left ideals, and this is multiplicativity. An automorphism is invertible and has an inverse of the same kind, so its action on the ideals is a permutation preserving inclusion. The two-sided case is the conjunction of the left and the right.

**Corollary (the action of the units).** The map $u \mapsto c_u$ realises $R^\times/(Z(R)\cap R^\times)$ as a group of automorphisms of the lattice of ideals; on the two-sided ideals it is the trivial action, because $c_u(I) = uIu^{-1} = I$ for a unit $u$ and a two-sided ideal $I$.

**Proof.** For a two-sided ideal $I$ and a unit $u$, $uI \subseteq I$ and $Iu^{-1} \subseteq I$, hence $uIu^{-1} \subseteq I$; applying the same to $u^{-1}$ gives $u^{-1}Iu \subseteq I$, that is $I \subseteq uIu^{-1}$, so $c_u(I) = I$. The inner automorphism therefore acts trivially on the two-sided ideals and moves only the one-sided ones.

**Proposition (the action on the maximal ideals).** A continuous automorphism carries a maximal ideal onto a maximal ideal, a prime ideal onto a prime ideal and a closed ideal onto a closed ideal; the action on the set of maximal ideals is a permutation, and the stabiliser of every maximal ideal contains the inner automorphisms.

**Proof.** An automorphism of the ring carries an ideal maximal among proper ideals onto an ideal maximal among proper ideals, and a prime ideal onto a prime ideal; a homeomorphism carries a closed set onto a closed set, so the closed ideals are permuted. The stabiliser statement is the corollary above.

### The Closed Ideals and the Operator Layer

**Proposition (kernels and images).** Let $T \in \operatorname{End}_c(R)$ be additive and continuous. Then $\ker T$ is a closed additive subgroup of $R$, and if $T = L_a$ then $\ker L_a = \ell(a)$, the left annihilator of $a$, and $\operatorname{im} L_a = Ra$; the image of a continuous additive map need not be closed, and the closure of $Ra$ is the smallest closed left ideal containing $\operatorname{im} L_a$.

**Proof.** The kernel of a continuous map into a Hausdorff space is closed, being the preimage of $\{0\}$. The kernel and image of $L_a$ are the annihilator and the principal left ideal of *Left and Right Multiplication in a Ring*. The image of a continuous map need not be closed; the intersection of the closed left ideals containing $\operatorname{im} L_a$ is closed and contains it, so it contains the closure, and the closure is itself a closed left ideal because the closure of an ideal is an ideal — continuity of the multiplication gives $R\overline{Ra} \subseteq \overline{Ra}$.

**Corollary.** For $a \in R$ the operator $L_a$ has closed image exactly when $Ra$ is closed, and it is injective exactly when $a$ is a left non-zero-divisor; it is a homeomorphism onto its image when $a$ is a unit and the inverse is the continuous $L_{a^{-1}}$.

**Proof.** The image is $Ra$, closed by hypothesis; injectivity is the vanishing of the left annihilator; the last statement is the previous section.

**Remark (the completion of the layer).** The operator layer is not complete: the uniform limit of a sequence of continuous operators is continuous on a uniform space, and $R$ with its additive uniformity is uniform, so the continuous operators are closed in the uniform topology of pointwise convergence under the hypotheses in which that topology is defined; the operator norm that measures the size of an operator on a normed ring is *The Involution on Bounded Operators of a Ring*, later in this group, and no norm is used here.

## The Natural Pairing

The later groups of the category build adjoints, and an adjoint is taken with respect to a pairing. This article fixes the pairing once.

**Definition.** Let $k$ be a field and $k\{R\}$ the free $k$-module on the set $R$, that is the $k$-vector space of finitely supported functions $R \to k$; write $C(R)$ for the $k$-algebra of continuous functions $R \to k$, carrying the topology of uniform convergence on compacta when $R$ is locally compact. The **natural pairing** of the category is

$$
\langle\cdot,\cdot\rangle : C(R)\times k\{R\} \longrightarrow k, \qquad \langle f, u\rangle = \sum_{x \in R} f(x)\,u_x ,
$$

the sum being finite because $u$ has finite support.

**Proposition.** The natural pairing is bilinear, it separates points of each side, and it is separately continuous for the topology of $C(R)$ and the discrete topology of $k\{R\}$.

**Proof.** Bilinearity is the bilinearity of the sum. For separation: if $\langle f, u\rangle = 0$ for all $f \in C(R)$ then evaluating at the functions of finite support gives $u = 0$; if $\langle f, u\rangle = 0$ for all $u$ then taking $u = \delta_a$, the basis element at $a$, gives $f(a) = 0$ for every $a$. Separate continuity: for fixed $f$ the functional $u \mapsto \langle f, u\rangle$ depends on finitely many coordinates, hence is continuous for the discrete topology; for fixed $u$ the functional $f \mapsto \langle f, u\rangle$ is a finite linear combination of evaluations, each continuous in the topology of uniform convergence on compacta.

**Proposition (the one-sided multiplications are adjoint to their inverses).** Let $L_a$ act on $C(R)$ by $(L_a f)(x) = f(a^{-1}x)$ when $a$ is a unit, and on $k\{R\}$ by the linear extension of $x \mapsto ax$; let $R_a$ act by $(R_a f)(x) = f(xa)$ and on $k\{R\}$ by the linear extension of $x \mapsto xa$. Then

$$
\langle L_a f, u\rangle = \langle f, L_{a^{-1}}u\rangle , \qquad \langle R_a f, u\rangle = \langle f, R_{a^{-1}}u\rangle .
$$

**Proof.** $\langle L_a f, u\rangle = \sum_x f(a^{-1}x)u_x = \sum_y f(y)u_{ay}$ on reindexing $y = a^{-1}x$, and $(L_{a^{-1}}u)_y = u_{ay}$, so the first identity is the definition of the pairing. Similarly $\langle R_a f, u\rangle = \sum_x f(xa)u_x = \sum_y f(y)u_{ya^{-1}}$, and $(R_{a^{-1}}u)_y = u_{ya}$, which gives the second.

The two identities are the algebraic content of the statement that the inversion of a unit carries the left regular operators to their adjoints, and they are the ring form of the corresponding statement for a topological group. The **form of the category**, the bilinear form on $R$ with respect to which the operator adjoints of the involutive part are taken, is a different structure: it is introduced in *The Adjoint of the Left Multiplication on a Topological Ring*, later in this category, and its concrete instances are *Adjoints under the Residue Pairing* and *The Adjoint under a Hermitian Valuation*.

## Summary

A continuous operator on a topological ring is a continuous self-map, the invertible ones are exactly the homeomorphisms, and the additive ones form the monoid $\operatorname{End}_c(R)$; the continuous automorphisms are the automorphisms that are homeomorphisms, the inner automorphisms $c_u$ for $u \in R^\times$ form the normal subgroup $\operatorname{Inn}(R) \cong R^\times/(Z(R)\cap R^\times)$, and $u \mapsto c_u$ is a homomorphism whose kernel is the central units. The one-sided multiplications $L_a$ and $R_a$ are continuous for free, they are homeomorphisms exactly when $a$ is a unit and then $L_a^{-1} = L_{a^{-1}}$, and the units form a topological group for the subspace topology whenever they are open, which they are for a division ring, for a local ring with open maximal ideal and hence for a valuation ring.

An automorphism permutes the ideals of each kind and preserves inclusion, so it acts on the lattice of left, right and two-sided ideals; the units act through the inner automorphisms, trivially on the two-sided ideals and nontrivially on the one-sided ones; the continuous automorphisms act on the sets of maximal, prime and closed ideals. The kernel of a continuous additive operator is closed, the image of $L_a$ is the left ideal $Ra$ and need not be closed, and its closure is the smallest closed left ideal containing it. Finally the category carries a natural pairing between the continuous functions and the finitely supported elements, and with respect to it the one-sided multiplications are adjoint to their inverses, which is the form the unit group takes on the operator layer.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $R^\times$, $Z(R)$ | Topological ring, its units, its centre |
| $\operatorname{Map}_c(R)$ | The monoid of continuous self-maps of $R$ |
| $\operatorname{Homeo}(R)$ | The group of homeomorphisms of $R$, the units of $\operatorname{Map}_c(R)$ |
| $\operatorname{End}_c(R)$ | The continuous additive endomorphisms, a submonoid |
| $\operatorname{Aut}(R)$, $\operatorname{Aut}_c(R)$ | All automorphisms, and the continuous ones |
| $\operatorname{Inn}(R)$, $c_u$ | The inner automorphisms, $c_u(x) = uxu^{-1}$ |
| $L_a$, $R_a$ | One-sided multiplications, continuous; homeomorphisms iff $a \in R^\times$ |
| $Ra$, $\ell(a)$ | Image and kernel of $L_a$: a left ideal, and the left annihilator |
| $C(R)$, $k\{R\}$ | Continuous functions to $k$, and finitely supported functions on $R$ |
| $\langle f, u\rangle = \sum_x f(x)u_x$ | The natural pairing of the category |
| $\langle L_a f, u\rangle = \langle f, L_{a^{-1}}u\rangle$ | The one-sided multiplications are adjoint to their inverses |
| $\overline{Ra}$ | The closure of the image, the smallest closed left ideal containing it |

## Further Reading

- Nicolas Bourbaki, *General Topology, Chapters 1–4* (Springer, 1995), for the monoid of continuous maps, the group of homeomorphisms and the function-space topology used on $C(R)$.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the automorphism group of a ring, the inner automorphisms and the centre.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for the operator layer of a topological ring, the openness of the unit group and the topology of a valuation ring.
- Tsi-Yuen Lam, *A First Course in Noncommutative Rings*, Graduate Texts in Mathematics 131 (Springer, 2nd ed. 2001), for the lattice of ideals, the maximal and prime ideals and the action of the automorphisms on them.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the endomorphism ring of a module, the regular representations and the operators they generate.
