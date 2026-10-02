
# __The Involution on the Structure Sheaf__

## Introduction

Let $(X,\mathcal{O}_X)$ be a ringed space. An **involution of the structure sheaf** is a morphism of sheaves of rings $\sigma:\mathcal{O}_X\to\mathcal{O}_X$ with $\sigma^2=\mathrm{id}$; it is an involution on the elements of the structure, the elements being the local functions of the ringed space. The involution makes $\mathcal{O}_X$ an involutive sheaf of rings: it has a **fixed structure sheaf** $\mathcal{O}_X^{\sigma}$ of self-adjoint functions, an **anti-invariant part** $\mathcal{O}_X^-$ when $2$ is invertible, and it acts on the modules and on the cohomology. The action on the cohomology is the **induced involution**: since $\sigma$ is an isomorphism of sheaves of rings, it acts on the cohomology ring $H^*(X,\mathcal{O}_X)$ by a ring automorphism of order two, the **involution on the cohomology of the structure sheaf**, and on the cohomology of any sheaf of modules that carries a compatible involution.

This article develops the involution of the structure sheaf, the fixed structure sheaf and the self-adjoint sections, the twist of a module by the involution, the induced involution on the cohomology, and the descent from the equivariant modules to the modules over the fixed structure sheaf. It is the third article of the involutive layer of the category: the general group action and the descent are *Equivariant Sheaves and Descent*, the conjugate-linear case and the real forms are *Sheaves with a Real Structure*, the general involution on cohomology is *Cohomology with an Involution*, the involution on the differential is *The Involution on the Coboundary*, and the descent of the linear structures along an involution of a ring is *Commutative Algebras with an Involution* and *Descent Theory* of Part I.

The article uses no analysis and no geometry: the structure sheaf is a sheaf of commutative rings with an involution, the modules are sheaves of modules in the sense of *Presheaves and Sheaves*, and no form, no norm and no derivative occurs. Throughout, $(X,\mathcal{O}_X)$ is a ringed space with a commutative structure sheaf, $\sigma$ is an involution of $\mathcal{O}_X$, $\mathcal{O}_X^{\sigma}$ is the fixed structure sheaf, $\mathcal{M}$ denotes a sheaf of $\mathcal{O}_X$-modules, and $2$ is invertible in the global sections $\mathcal{O}_X(X)$ whenever a decomposition into fixed and anti-invariant parts is used.

## Involutions of the Structure Sheaf

**Definition.** An **involution** of the structure sheaf is a morphism of sheaves of rings $\sigma:\mathcal{O}_X\to\mathcal{O}_X$ with $\sigma^2=\mathrm{id}$; equivalently, a ring involution $\sigma_U$ of each ring of sections $\mathcal{O}_X(U)$, natural in $U$. The **fixed structure sheaf** is

$$
\mathcal{O}_X^{\sigma}:\ U\longmapsto \mathcal{O}_X(U)^{\sigma}=\{\,a: \sigma_U(a)=a\,\},
$$

the sheaf of **self-adjoint** or **invariant** functions, and when $2$ is invertible the **anti-invariant sheaf** is $\mathcal{O}_X^-$, with $\mathcal{O}_X(U)^-=\{a:\sigma_U(a)=-a\}$.

**Proposition.** $\mathcal{O}_X^{\sigma}$ is a subsheaf of $\mathcal{O}_X$ and a sheaf of commutative rings; $\mathcal{O}_X$ is a sheaf of $\mathcal{O}_X^{\sigma}$-algebras; and when $2$ is invertible in $\mathcal{O}_X(X)$ there is a direct sum decomposition

$$
\mathcal{O}_X=\mathcal{O}_X^{\sigma}\oplus\mathcal{O}_X^-,\qquad \sigma(a^{\sigma}+a^-)=a^{\sigma}-a^-,
$$

exhibiting $\mathcal{O}_X$ as the trivial extension of $\mathcal{O}_X^{\sigma}$ by the $\mathcal{O}_X^{\sigma}$-module $\mathcal{O}_X^-$ with the product $\mathcal{O}_X^-\cdot\mathcal{O}_X^-\subseteq\mathcal{O}_X^{\sigma}$.

*Proof.* The fixed elements of a ring under an involution form a subring, and the condition is local, so the fixed functions form a subsheaf of rings. The decomposition is the sectionwise decomposition of *Commutative Algebras with an Involution*: every element is $a=\frac{a+\sigma a}{2}+\frac{a-\sigma a}{2}$, the two summands being invariant and anti-invariant, and the product of two anti-invariant elements is invariant because $\sigma(a^-b^-)=\sigma(a^-)\sigma(b^-)=a^-b^-$.

**Remark (structural and geometric involutions).** An involution of $\mathcal{O}_X$ need not come from an involution of the space $X$: it is an involution of the ring of local functions, and it may act nontrivially on the functions over a point without moving the point. When it does come from a homeomorphism $\sigma:X\to X$ of order two, with an isomorphism $\mathcal{O}_X\to\sigma_*\mathcal{O}_X$ of sheaves of rings, the fixed structure sheaf is the structure sheaf of the quotient in the cases of *Sheaves with a Real Structure*, and the descent is the one treated there; the present article treats the general structural involution, of which the geometric one is the example.

**Example (complex conjugation).** On a complexification $(X,\mathcal{O}_X)$ of a ringed space of real functions, the conjugation of the coefficients is an involution $\sigma(a)=\bar a$ in local complexified coordinates; the fixed structure sheaf is the real structure sheaf and the anti-invariant sheaf is the imaginary part. This is the geometric model.

**Example (the trivial involution).** The identity is an involution with $\mathcal{O}_X^{\sigma}=\mathcal{O}_X$ and $\mathcal{O}_X^-=0$; the descent of the next sections is then the identity equivalence, and the case is the degenerate check.

## The Twist and the Equivariant Modules

**Definition.** An involution $\sigma$ of $\mathcal{O}_X$ gives a functor $\mathcal{M}\mapsto\mathcal{M}^{\sigma}$ on sheaves of $\mathcal{O}_X$-modules, the **twist** by $\sigma$: the sheaf $\mathcal{M}^{\sigma}$ has the same underlying sheaf of abelian groups and the $\mathcal{O}_X$-module structure $\rho_{\sigma}(a,m)=\rho(\sigma(a),m)$. A **$\sigma$-equivariant module** is a sheaf of $\mathcal{O}_X$-modules $\mathcal{M}$ with an isomorphism $u:\mathcal{M}\to\mathcal{M}^{\sigma}$ of $\mathcal{O}_X$-modules, equivalently a $\sigma$-semilinear automorphism $u(a m)=\sigma(a)u(m)$, satisfying $u^2=\mathrm{id}$; the $\sigma$-equivariant modules form a category $\mathcal{M}\mathrm{od}^{\sigma}(X,\mathcal{O}_X)$.

**Proposition.** The twist is an autoequivalence of the category of $\mathcal{O}_X$-modules with inverse the twist by $\sigma$, since $\sigma^2=\mathrm{id}$; the $\sigma$-equivariant modules are the objects of the category of $\mathcal{O}_X$-modules with a $\mathbb{Z}/2$-action in which the equivariant structure on the coefficients is the involution $\sigma$.

*Proof.* The twist by $\sigma$ followed by the twist by $\sigma$ is the identity, because $(\mathcal{M}^{\sigma})^{\sigma}=\mathcal{M}$ after $\sigma^2=\mathrm{id}$; the semilinearity of the equivariant structure is the statement that the action on $\mathcal{M}$ covers the action on $\mathcal{O}_X$, which is the definition of an equivariant module.

**Proposition (the fixed module).** The **fixed part** of a $\sigma$-equivariant module is the subsheaf

$$
\mathcal{M}^{\sigma}:\ U\longmapsto \{\,m\in\mathcal{M}(U): u(m)=m\,\}\quad\text{for a $\sigma$-invariant $U$},
$$

a sheaf of $\mathcal{O}_X^{\sigma}$-modules; the same discussion of the invariant opens as in *Equivariant Sheaves and Descent* applies, and over an invariant open set the fixed part is the fixed subspace of the $\sigma$-semilinear involution.

*Proof.* If $m$ is fixed and $a$ is self-adjoint then $am$ is fixed, since $u(am)=\sigma(a)u(m)=am$; the module axioms are inherited from $\mathcal{M}$. The locality is that of the fixed elements of a sheaf with an involution.

**Example (the structure sheaf as an equivariant module).** The structure sheaf $\mathcal{O}_X$ with the equivariant structure $u=\sigma$ is a $\sigma$-equivariant module whose fixed part is $\mathcal{O}_X^{\sigma}$; the example shows that the fixed structure sheaf is the fixed part of the structure sheaf, and that the descent of the next section generalises the identity $\mathcal{O}_X\mapsto\mathcal{O}_X^{\sigma}$.

## The Induced Involution on Cohomology

**Theorem (the induced involution).** Let $\sigma$ be an involution of $\mathcal{O}_X$. Then:

1. $\sigma$ induces a map $\sigma^*:H^i(X,\mathcal{O}_X)\to H^i(X,\mathcal{O}_X)$ for every $i$, and $\sigma^*$ is a ring automorphism of the graded ring $H^*(X,\mathcal{O}_X)$ of order two: $(\sigma^*)^2=\mathrm{id}$ and $\sigma^*(\alpha\smile\beta)=\sigma^*\alpha\smile\sigma^*\beta$.
2. For a $\sigma$-equivariant module $\mathcal{M}$ the involution induces a map on the cohomology, $\sigma^*_{\mathcal{M}}:H^i(X,\mathcal{M})\to H^i(X,\mathcal{M})$, with $(\sigma^*_{\mathcal{M}})^2=\mathrm{id}$ and compatible with the $\mathcal{O}_X(X)$-module structure twisted by $\sigma$.
3. The induced map is natural: for a $\sigma$-equivariant morphism of modules, the induced maps commute with the morphisms on cohomology.

*Proof.* The involution is an isomorphism of sheaves of rings, so it is functorial on the category of $\mathcal{O}_X$-modules and carries injective sheaves to injective sheaves, for instance because it is an equivalence of categories; applying the derived functor of global sections gives the maps $\sigma^*$ and $\sigma^*_{\mathcal{M}}$. The order and the multiplicativity: the first holds because $\sigma^2=\mathrm{id}$ on the coefficients, and the second is the naturality of the cup product of *The Cup Product on Sheaf Cohomology*, $\sigma^*(\alpha\smile\beta)=\sigma^*\alpha\smile\sigma^*\beta$ for a morphism of sheaves of rings, since the product on the cohomology is induced by the multiplication of $\mathcal{O}_X$ and $\sigma$ is multiplicative. The naturality is the functoriality of the derived functor.

**Definition.** The **fixed cohomology** of the structure sheaf is the fixed subring

$$
H^*(X,\mathcal{O}_X)^{\sigma}=\{\,\alpha:\sigma^*\alpha=\alpha\,\},
$$

and the **anti-invariant cohomology** is the set of classes with $\sigma^*\alpha=-\alpha$ when $2$ is invertible; the cohomology decomposes as the direct sum of the two eigenspaces in that case.

**Corollary (the fixed subring is a subring).** The fixed cohomology is a graded subring of $H^*(X,\mathcal{O}_X)$ containing the unit, and the anti-invariant part is a module over it whose products lie in the fixed part; when $2$ is invertible in $\mathcal{O}_X(X)$, $H^*(X,\mathcal{O}_X)=H^*(X,\mathcal{O}_X)^{\sigma}\oplus H^*(X,\mathcal{O}_X)^-$.

*Proof.* The fixed elements of a ring under an automorphism of order two form a subring containing the unit; the multiplicativity of $\sigma^*$ gives the module and product statements; the decomposition is the sectionwise decomposition of a module under an involution of order two with $2^{-1}$ available.

**Proposition (the action on the sections).** The induced involution on $H^0(X,\mathcal{O}_X)=\mathcal{O}_X(X)$ is the involution $\sigma$ itself, and its fixed part is $\mathcal{O}_X^{\sigma}(X)$; in positive degree the induced involution is the one of *Cohomology with an Involution*, and its fixed classes are the self-adjoint classes.

*Proof.* In degree zero the global sections functor is the identity on the sections and the induced map is $\sigma_{X}$ on $\mathcal{O}_X(X)$; the higher degrees are the general theory of the action on cohomology, developed in *Cohomology with an Involution*.

## Descent to the Fixed Structure Sheaf

**Theorem (descent for an involution of a sheaf of rings).** Let $\sigma$ be an involution of the structure sheaf and suppose that $\mathcal{O}_X$ is a faithfully flat $\mathcal{O}_X^{\sigma}$-algebra with the descent cocycle $\sigma$ — the **Galois condition** for the group $\mathbb{Z}/2$. Then the fixed-part functor

$$
\mathcal{M}\longmapsto\mathcal{M}^{\sigma},\qquad \mathcal{N}\longmapsto\mathcal{N}\otimes_{\mathcal{O}_X^{\sigma}}\mathcal{O}_X,
$$

are inverse equivalences between the category of $\sigma$-equivariant $\mathcal{O}_X$-modules on $X$ and the category of sheaves of $\mathcal{O}_X^{\sigma}$-modules,

$$
\mathcal{M}\mathrm{od}^{\sigma}(X,\mathcal{O}_X)\simeq\mathcal{M}\mathrm{od}(X,\mathcal{O}_X^{\sigma}),
$$

and the structure sheaf itself descends, $\mathcal{O}_X^{\sigma}$ being recovered as the fixed part of $\mathcal{O}_X$.

*Proof.* This is the descent of *Commutative Algebras with an Involution* and of *Descent Theory*, applied sectionwise over the ringed space: a $\sigma$-equivariant module is a module with a semilinear involution, and the descent data for the cover $\mathcal{O}_X^{\sigma}\to\mathcal{O}_X$ are exactly the equivariant structures; the fixed-part functor is the equalizer of the identity and the involution, and the extension of scalars is its inverse under the Galois and flatness hypotheses, exactly as in the faithfully flat descent theorem.

**Proposition (descent on cohomology).** Under the descent, the cohomology of a descended module is the fixed part of the cohomology of its extension, $H^i(X,\mathcal{M}^{\sigma})\cong H^i(X,\mathcal{M})^{\sigma}$ under the identification of the descended module with its restriction to the fixed structure sheaf; the comparison is the induced involution of the previous section.

*Proof.* An acyclic resolution of $\mathcal{M}^{\sigma}$ by $\mathcal{O}_X^{\sigma}$-modules extends to an acyclic resolution of $\mathcal{M}$ by $\mathcal{O}_X$-modules on which $\sigma$ acts, and the fixed part of the extended complex computes the cohomology by the descent of the coefficients; the identification is that of the derived functors under the equivalence of categories.

## Worked Cases

### The Complexification

For the complexification $(X,\mathcal{O}_X)$ of a real ringed space with the conjugation involution $\sigma(a)=\bar a$, the fixed structure sheaf is the real structure sheaf, the anti-invariant sheaf is the imaginary part, and the descent identifies the conjugation-equivariant modules with the modules over the real structure sheaf. On the cohomology the involution acts by conjugation, the fixed classes are the real classes, and the comparison $H^i(X,\mathcal{O}_X)=H^i(X,\mathcal{O}_X^{\sigma})\otimes_{\mathbb{R}}\mathbb{C}$ holds when the descent applies. This is the model of a real structure on the cohomology.

### The Trivial Involution

For the identity involution the fixed structure sheaf is the structure sheaf, the anti-invariant sheaf vanishes, and the descent is the identity equivalence; the induced involution on cohomology is the identity and every class is self-adjoint. The case shows that all the statements reduce to the tautologies of the identity, and it is the check that the definitions do not exclude the degenerate case.

### The Involution of the Cohomology of a Constant Sheaf

On a space $X$ with an involution $\sigma:X\to X$ and the constant sheaf $\mathcal{O}_X=\underline{\mathbb{C}}$ with the conjugation, the induced involution on $H^*(X,\underline{\mathbb{C}})$ is the one of *Sheaves with a Real Structure*, and the fixed classes are the real classes of the cohomology; the structure sheaf is constant, the fixed structure sheaf is $\underline{\mathbb{R}}$, and the fixed cohomology is the cohomology of the quotient with real coefficients when the descent applies.

## Summary

An involution of the structure sheaf is a ring involution of the sheaf of local functions; the self-adjoint functions form the fixed structure sheaf, a sheaf of commutative rings over which the structure sheaf is an algebra, and when $2$ is invertible the structure sheaf decomposes as the fixed part plus the anti-invariant part with the anti-invariant product landing in the fixed part. The involution twists the modules and defines the equivariant modules with a semilinear involution; the fixed part of an equivariant module is a module over the fixed structure sheaf.

Because the involution is an isomorphism of sheaves of rings, it acts on the cohomology: the induced involution $\sigma^*$ is a ring automorphism of order two of the cohomology ring $H^*(X,\mathcal{O}_X)$, commuting with the cup product; its fixed subring is the fixed cohomology, its anti-invariant part is a module over it, and the two span the cohomology when $2$ is invertible. In degree zero the induced involution is the involution on the global sections. Under the Galois and flatness hypotheses the descent identifies the equivariant modules with the modules over the fixed structure sheaf, and the cohomology of a descended module is the fixed part of the cohomology of its extension; the complexification with the conjugation is the model.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma:\mathcal{O}_X\to\mathcal{O}_X$ | involution of the structure sheaf; $\sigma^2=\mathrm{id}$ |
| $\mathcal{O}_X^{\sigma}$ | fixed structure sheaf of self-adjoint functions; a sheaf of rings |
| $\mathcal{O}_X^-$ | anti-invariant sheaf; $\mathcal{O}_X=\mathcal{O}_X^{\sigma}\oplus\mathcal{O}_X^-$ when $2$ is invertible |
| $\mathcal{M}^{\sigma}$ | twist of a module by $\sigma$; the same sheaf with the structure $\rho(\sigma(a),m)$ |
| $\mathcal{M}\mathrm{od}^{\sigma}(X,\mathcal{O}_X)$ | category of $\sigma$-equivariant modules with a semilinear involution |
| $\mathcal{M}^{\sigma}$ | fixed part of an equivariant module; a sheaf of $\mathcal{O}_X^{\sigma}$-modules |
| $\sigma^*:H^i(X,\mathcal{O}_X)\to H^i(X,\mathcal{O}_X)$ | induced involution; a ring automorphism of order two |
| $H^*(X,\mathcal{O}_X)^{\sigma}$ | fixed cohomology, a graded subring |
| $H^*(X,\mathcal{O}_X)=H^*(X,\mathcal{O}_X)^{\sigma}\oplus H^*(X,\mathcal{O}_X)^-$ | eigenspace decomposition when $2$ is invertible |
| Galois condition | $\mathcal{O}_X$ faithfully flat over $\mathcal{O}_X^{\sigma}$ with the cocycle $\sigma$ |
| $\mathcal{M}\mathrm{od}^{\sigma}(X,\mathcal{O}_X)\simeq\mathcal{M}\mathrm{od}(X,\mathcal{O}_X^{\sigma})$ | descent to the fixed structure sheaf |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for involutions of rings, their fixed parts and the descent of the modules.
- Alexander Grothendieck, *Technique de descente et théorèmes d'existence en géométrie algébrique (FGA)* (Séminaire Bourbaki, 1959–1962), for the descent along an involution of a sheaf of rings.
- Alexander Grothendieck and Jean Dieudonné, *Éléments de géométrie algébrique I* (Publications Mathématiques de l'IHÉS 4, 1960), for the sheaves of rings with involution and their modules.
- Glen E. Bredon, *Sheaf Theory* (Springer, second edition, 1997), for the action of a ring involution on the cohomology and the fixed part of a sheaf of modules.
- Peter T. Johnstone, *Sketches of an Elephant: A Topos Theory Compendium* (Oxford University Press, 2002), for the internal involution of a sheaf of rings and the descent.
- Jean-Pierre Serre, *Galois Cohomology* (Springer, 1997), for the descent of the linear structures along an involution of a ring and the Galois condition.
