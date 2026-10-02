
# __Galois Descent for the Operator Layer__

## Introduction

A **descent datum** on the operator layer is the semilinear action of the Galois group by algebra automorphisms of *Real Structures on the Operator Layer*, and a **descent datum on a module** over the layer is a module with an action of the group compatible with the operators. The **effective descent** is the theorem that the modules over the descended operator layer are exactly the modules over the layer with an effective datum, the functor being the base change and the quasi-inverse the invariants; it is the descent of Part I's *Descent Theory* read on the operator layer, and it is the tool with which the $\mathcal{D}$-modules of an operator layer over $L$ are recovered from the data over $L$. This article fixes the descent data on the algebra and on the modules, the equivalence of the effective descent, the descent of the $\mathcal{D}$-module structure, and the obstruction detected by the group cohomology, and it is the second and last article of the `- * Operator Theory` group.

The article uses the conjugation and the fixed operators of *Real Structures on the Operator Layer*, the operator layer of *The Sheaf of Differential Operators*, the descent of the sheaves of the projected *Equivariant Sheaves and Descent* and *Galois Descent for Sheaves* of the category *Sheaves and Cohomology*, the involution on the cohomology of *The Galois Action on the Cohomology*, Part I's *Descent Theory*, *Group Cohomology* and *Galois Cohomology*, and the descent of an algebra with its forms of *Real Forms and the Descent of an Algebra*. The de Rham complex and the $\mathcal{D}$-module structure are those of *The Sheaf of Differential Operators* and *Sheaves in Algebraic Geometry*.

Throughout $L/k$ is a finite Galois extension with group $G$, $X$ is a variety over $k$, $\mathcal{D} = \mathcal{D}_{X_L}$ is the operator layer with the conjugation $\mathrm{ad}_\sigma$ of *Real Structures on the Operator Layer*, and the fixed algebra is $\mathcal{D}^G = \mathcal{D}_X$.

## Descent Data for the Operator Layer

### The Descent Datum on the Algebra

**Definition.** A **descent datum** on the operator layer $\mathcal{D}$ is a semilinear action of $G$ by algebra automorphisms,
$$
\mathrm{ad}_\sigma : \mathcal{D}\to\mathcal{D}, \qquad
\mathrm{ad}_\sigma(ST) = \mathrm{ad}_\sigma(S)\mathrm{ad}_\sigma(T), \qquad
\mathrm{ad}_\sigma(fT) = \sigma(f)\,\mathrm{ad}_\sigma(T),
$$
with $\mathrm{ad}_{\sigma\tau} = \mathrm{ad}_\sigma\circ\mathrm{ad}_\tau$, as in *Real Structures on the Operator Layer*. The datum is **effective** when there is an algebra $\mathcal{D}_0$ over $k$ with an isomorphism of algebras with the action
$$
\mathcal{D}\cong\mathcal{D}_0\otimes_kL
$$
under which $\mathrm{ad}_\sigma$ is the action on the second factor, $\mathrm{ad}_\sigma(d\otimes\ell) = d\otimes\sigma(\ell)$.

**Theorem (the descent of the algebra).** The descent data on the operator layer $\mathcal{D}$ correspond to the $k$-algebras $\mathcal{D}_0$ with $\mathcal{D}_0\otimes_kL\cong\mathcal{D}$, the correspondence sending $\mathcal{D}_0$ to the action on the second factor, and the fixed algebra is the descender:
$$
\mathcal{D}^{G} = \mathcal{D}_0 .
$$
Every descent datum on the operator layer of a variety is effective, and the descended algebra is the operator layer $\mathcal{D}_X$ of the descended variety.

*Proof.* The fixed algebra of the semilinear action on $\mathcal{D}_0\otimes_kL$ is $\mathcal{D}_0$, by the fixed-point theorem of *The Galois Action as an Operator* applied to the coefficients; conversely a descent datum gives an algebra structure on the invariants whose base change is $\mathcal{D}$ by the descent of the modules of Part I's *Descent Theory*. The effectivity is the descent theorem for algebras with a semilinear action, *Real Forms and the Descent of an Algebra*, the action here being by algebra automorphisms; the descended algebra is the operator layer of the descended variety by the invariant theorem of *Real Structures on the Operator Layer*.

### The Descent Datum on a Module

**Definition.** A **descent datum** on a $\mathcal{D}$-module $M$ is an action of $G$ on $M$ by additive maps such that
$$
g(\ell m) = \sigma_g(\ell)\,g(m), \qquad g(Tm) = \mathrm{ad}_g(T)\,g(m)
$$
for $g\in G$, $\ell\in L$, $T\in\mathcal{D}$ and $m\in M$; the first identity is the semilinearity and the second is the compatibility with the operators. A $\mathcal{D}$-module with such a datum is a $(\mathcal{D},G)$-**module**, or an **equivariant** $\mathcal{D}$-module. The datum is **effective** when there is a $\mathcal{D}_X$-module $M_0$ with an isomorphism of $(\mathcal{D},G)$-modules
$$
M\cong M_0\otimes_kL .
$$

**Proposition (the datum on the structure sheaf).** The structure sheaf $\mathcal{O}_{X_L}$, with the $\mathcal{D}$-module structure of *The Sheaf of Differential Operators*, carries the descent datum of the semilinear action on the functions, and it is effective, with descended module $\mathcal{O}_X$:
$$
\mathcal{O}_{X_L}\cong\mathcal{O}_X\otimes_kL .
$$

*Proof.* The functions form the natural $\mathcal{D}$-module, the action on them is the semilinear action of *The Galois Action as an Operator* and is compatible with the operators by the definition of $\mathrm{ad}_g$ as the conjugation; the descended module is the invariant functions $\mathcal{O}_X$, by the fixed-point theorem.

**Example (the Weyl algebra and its modules).** For the affine line and the Weyl algebra $A_1$ of *Real Structures on the Operator Layer*, a module over $A_1(L)$ with a semilinear $G$-action compatible with the operators is the base change of a module over $A_1(k)$ exactly when the action is effective; the module $A_1(L)$ itself and the structure sheaf $L[x]$ are effective, while a module with the twist $i\partial$ acting with a sign is the base change of a module over $A_1(k)$ only after the coefficient field is enlarged. The descent computes the $A_1(k)$-modules from the $A_1(L)$-modules and their data.

## The Effective Descent

### The Equivalence of Categories

**Theorem (the effective descent of the operator modules).** Let $L/k$ be a finite Galois extension with group $G$ and let $\mathcal{D}=\mathcal{D}_{X_L}$ be the operator layer with the conjugation. Then the base-change functor
$$
M_0\longmapsto M_0\otimes_kL, \qquad T(m\otimes\ell) = (Tm)\otimes\ell,
$$
is an equivalence of categories from the quasi-coherent $\mathcal{D}_X$-modules to the quasi-coherent $\mathcal{D}$-modules with an effective descent datum, with quasi-inverse the invariants
$$
M\longmapsto M^{G} = \{m\in M : g(m) = m \text{ for all } g\in G\} .
$$

*Proof.* On an affine chart the statement is the descent of the modules of Part I's *Descent Theory* with the additional compatibility with the operators, which is preserved by the invariants because the action on the operators is by algebra automorphisms; the two functors are inverse on the objects with a datum by the unit and the counit of the adjunction, and the compatibility of the operators is checked on the generators. The global statement follows by glueing over a $G$-stable affine cover, which exists because $G$ is finite.

**Corollary (the category of the $\mathcal{D}$-modules as the invariants).** The category of the $\mathcal{D}_X$-modules is equivalent to the category of the $\mathcal{D}$-modules with an effective descent datum, and it is the category of the $G$-invariants of the operator modules,
$$
\mathcal{D}_X\text{-mod}\ \simeq\ \bigl(\mathcal{D}\text{-mod}\bigr)^{G} ,
$$
the equivalence sending $M_0$ to the module with the action on the second factor and its quasi-inverse sending $M$ to the invariants $M^G$.

*Proof.* The equivalence is the theorem, and the second description is the reading of the same equivalence as the fixed category under the action: a module with an effective datum is a module with a $G$-action, and the invariants are the descended module.

### The Descent of the $\mathcal{D}$-Module Structure

**Theorem (the descended structure).** Let $M$ be a $\mathcal{D}$-module with an effective descent datum and let $M_0 = M^G$ be the descended module. Then $M_0$ is a $\mathcal{D}_X$-module for the fixed algebra $\mathcal{D}_X = \mathcal{D}^G$, the action
$$
\mathcal{D}_X\times M_0\longrightarrow M_0, \qquad T\cdot m = Tm ,
$$
is well defined, and the base change recovers the action of $\mathcal{D}$; the de Rham complex of $M_0$ is the invariants of the de Rham complex of $M$,
$$
\Omega^\bullet_{X}(M_0) = \bigl(\Omega^\bullet_{X_L}(M)\bigr)^{G} .
$$

*Proof.* For $T\in\mathcal{D}^G$ and $m\in M^G$ the product $Tm$ is fixed because $g(Tm) = \mathrm{ad}_g(T)g(m) = Tm$, so the action of the fixed algebra preserves the invariants; the base change recovers the action of $\mathcal{D}$ by the effective descent. The de Rham complex is built from the module and the derivations, and both are descended, so its invariants are the de Rham complex of the descended module, by the compatibility of the invariants with the tensor product and the differential.

**Corollary (the descent of the solutions and of the cohomology).** The solutions of a descended system, that is $\operatorname{Hom}_{\mathcal{D}_X}(\mathcal{M},\mathcal{O}_X)$, are the invariants of the solutions over $L$,
$$
\operatorname{Hom}_{\mathcal{D}_X}(\mathcal{M}_0,\mathcal{O}_X) = \operatorname{Hom}_{\mathcal{D}}(\mathcal{M},\mathcal{O}_{X_L})^{G},
$$
and the de Rham cohomology of the descended module is the invariant cohomology, by *The Galois Action on the Cohomology*.

*Proof.* The Hom functor is computed on the invariants because both the module and the structure sheaf are descended; the invariant identification is the invariant-cohomology theorem of *The Galois Action on the Cohomology* applied to the de Rham complex.

## The Invariants and the Cohomology

### The Invariant Modules and the Obstruction

**Theorem (the obstruction to the descent).** Let $M$ be a $\mathcal{D}$-module with a descent datum. The datum is effective if and only if the natural map
$$
M^{G}\otimes_kL\longrightarrow M
$$
is an isomorphism, and the obstruction to the effectivity is a class in the first group cohomology
$$
\operatorname{ob}(M)\in H^1\bigl(G,\ \underline{\operatorname{Aut}}_{\mathcal{D}}(M)\bigr),
$$
which vanishes for $M$ with the automorphism sheaf a linear group, by Hilbert's theorem 90 for $GL_n$.

*Proof.* The unit of the adjunction $M^G\otimes_kL\to M$ is an isomorphism exactly when the datum is effective; the failure is detected by the $1$-cocycles of the action, a cocycle presentation giving a class in the first cohomology of $G$ with coefficients in the automorphisms of $M$, in the sense of Part I's *Group Cohomology* and *Galois Cohomology*. For a linear group the first cohomology vanishes by Hilbert's theorem 90 in its functorial form (Speiser's lemma), so the datum is effective, which is the statement of the effective descent.

**Theorem (the Hochschild–Serre sequence of the descent).** For a $\mathcal{D}$-module with a descent datum there is a spectral sequence
$$
E_2^{pq} = H^p\bigl(G,\ H^q(\mathcal{M})\bigr)\ \Longrightarrow\ H^{p+q}(\mathcal{M}^{G}),
$$
the group cohomology of the cohomology of the module converging to the cohomology of the descended module, and its five-term sequence detects the failure of the invariants to compute the cohomology.

*Proof.* The same Grothendieck spectral sequence of the invariants and the global sections as in *The Galois Action on the Cohomology*, applied to the complex that computes the cohomology of the $\mathcal{D}$-module; the edge maps give the five-term sequence. The convergence is the convergence of Part I's *Spectral Sequences* for the composite of the two functors.

### Examples

**Example (the descent of the structure sheaf and of the de Rham complex).** For the structure sheaf the descent is effective and the descended module is $\mathcal{O}_X$; the de Rham complex of *Sheaves in Algebraic Geometry* on $\mathcal{O}_{X_L}$ has the invariants the de Rham complex of $\mathcal{O}_X$, so the algebraic de Rham cohomology of the descended variety is the invariant part of the de Rham cohomology over $L$, in agreement with *The Galois Action on the Cohomology*.

**Example (a twisted module over the affine line).** Let $M = L[x]$ with the action of the conjugation on the coefficients twisted by the sign, $g(f) = \sigma(f)$ and $g(T) = \mathrm{ad}_g(T)$ with the automorphism $T\mapsto (i\partial)T(i\partial)^{-1}$ of the Weyl algebra; the module is a $\mathcal{D}$-module with a descent datum whose invariant part is $k[x]$ only when the twist is trivial, and the twisted module is an isotropic instance of the obstruction of the first cohomology. The effective descent recovers the $k[x]$-modules from the $L[x]$-modules and their data.

**Example (the descent of a locally free $\mathcal{D}$-module).** A locally free $\mathcal{D}$-module over $X_L$ corresponds to a connection on a vector bundle in the language of the written *Fibre Bundles, Connections and Curvature* of Part III, named but not constructed here; a descent datum on it is a $\mathcal{D}$-module structure preserved by the conjugation, and the effective descent gives the descended locally free $\mathcal{D}$-module over $X$. The descent of the extra structure that the connection names is the descent of the $\mathcal{D}$-module structure, so the effectivity for the locally free modules is the same as for the structure sheaf.

## Summary

A **descent datum** on the operator layer $\mathcal{D}=\mathcal{D}_{X_L}$ is the semilinear action of the Galois group by algebra automorphisms; it is **effective** when $\mathcal{D}\cong\mathcal{D}_0\otimes_kL$ with the action on the second factor, and the descender is the fixed algebra $\mathcal{D}^{G}=\mathcal{D}_0=\mathcal{D}_X$. A **descent datum on a module** is an action of the group that is semilinear on the scalar and compatible with the operators, $g(Tm)=\mathrm{ad}_g(T)g(m)$, so that the module is a $(\mathcal{D},G)$-module; it is effective when $M\cong M_0\otimes_kL$ for a $\mathcal{D}_X$-module $M_0$. The **effective descent** is the equivalence
$$
\mathcal{D}_X\text{-mod}\ \simeq\ \bigl(\mathcal{D}\text{-mod}\bigr)^{G},
$$
with the base change as one functor and the invariants $M\mapsto M^{G}$ as the quasi-inverse; equivalently, the $\mathcal{D}_X$-modules are the $\mathcal{D}$-modules with an effective datum. The descended $\mathcal{D}_X$-module structure is $T\cdot m = Tm$ for $T\in\mathcal{D}_X$ and $m\in M_0$, the de Rham complex and the solution sheaf descend to the invariants, and the obstruction to the effectivity of a datum is a class in $H^1(G,\underline{\operatorname{Aut}}_{\mathcal{D}}(M))$, which vanishes for the linear groups by Hilbert's theorem 90. The descent of the cohomology is the Hochschild–Serre spectral sequence of *The Galois Action on the Cohomology*, so the operator layer descends exactly as the varieties, the sheaves and the cohomology do.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{ad}_\sigma$, $\mathrm{ad}_\sigma(ST)=\mathrm{ad}_\sigma(S)\mathrm{ad}_\sigma(T)$ | the descent datum on the operator layer |
| $\mathrm{ad}_\sigma(fT)=\sigma(f)\mathrm{ad}_\sigma(T)$ | semilinearity over the structure sheaf |
| $\mathcal{D}\cong\mathcal{D}_0\otimes_kL$ | the effectivity of the datum; the descended algebra |
| $\mathcal{D}^{G}=\mathcal{D}_0=\mathcal{D}_X$ | the fixed algebra is the operator layer of $X$ |
| $g(\ell m)=\sigma_g(\ell)g(m)$, $g(Tm)=\mathrm{ad}_g(T)g(m)$ | the datum on a module; a $(\mathcal{D},G)$-module |
| $M\cong M_0\otimes_kL$ | the effective datum on a module |
| $\mathcal{D}_X\text{-mod}\simeq(\mathcal{D}\text{-mod})^{G}$ | the effective descent; the invariants |
| $M^{G}=\{m:g(m)=m\}$ | the descended module |
| $T\cdot m=Tm$, $T\in\mathcal{D}_X$, $m\in M^{G}$ | the descended $\mathcal{D}_X$-module structure |
| $\Omega^\bullet_X(M_0)=(\Omega^\bullet_{X_L}(M))^{G}$ | the de Rham complex descends |
| $\operatorname{Hom}_{\mathcal{D}_X}(\mathcal{M}_0,\mathcal{O}_X)=\operatorname{Hom}_{\mathcal{D}}(\mathcal{M},\mathcal{O}_{X_L})^{G}$ | the solutions descend |
| $\operatorname{ob}(M)\in H^1(G,\underline{\operatorname{Aut}}_{\mathcal{D}}(M))$ | the obstruction to the effectivity |
| $H^p(G,H^q(\mathcal{M}))\Rightarrow H^{p+q}(\mathcal{M}^{G})$ | the Hochschild–Serre sequence of the descent |

## Further Reading

- Alexander Grothendieck, *Technique de descente et théorèmes d'existence en géométrie algébrique* (Séminaire Bourbaki, 1959–1962), for the effective descent of the algebras and the modules and the descent of the morphisms.
- Jean-Pierre Serre, *Galois Cohomology* (Springer, 1997), for the descent of the algebras with a semilinear action and Hilbert's theorem 90 in its functorial form.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the descent of an algebra with an involution and the forms it classifies.
- Armand Borel, Pierre-Paul Grivel, Bernhard Kaup and others, *Algebraic D-Modules* (Perspectives in Mathematics 2, Academic Press, 1987), for the $\mathcal{D}$-modules, their base change and their descent.
- Alexander Grothendieck, *Sur quelques points d'algèbre homologique* (Tohoku Mathematical Journal 9, 1957), for the spectral sequence of the composite of the invariants and the global sections.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, Ergebnisse der Mathematik 5, third edition, 1971), for the descent of the operators and the two operations of the operator layer.
