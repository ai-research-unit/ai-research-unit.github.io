
# __Hermitian Pairings of Sheaves__

## Introduction

A **Hermitian pairing** of sheaves is a pairing $\langle-,-\rangle:\mathcal{F}\times\mathcal{G}\to\mathcal{O}_X$ that is linear in one variable and **conjugate-linear** in the other, with a **Hermitian symmetry**, and it is the sheaf-theoretic form of the Hermitian form of linear algebra. The conjugation is an involution $\sigma$ of the structure sheaf, as in *The Involution on the Structure Sheaf*: the pairing is $\sigma$-sesquilinear, $\langle a s,t\rangle=\sigma(a)\langle s,t\rangle$ and $\langle s,a t\rangle=a\langle s,t\rangle$, and Hermitian when $\langle s,t\rangle=\sigma(\langle t,s\rangle)$. The pairing is the structure relative to which an operator has an **adjoint**: for $T:\mathcal{F}\to\mathcal{G}$ the adjoint $T^{\dagger}:\mathcal{G}\to\mathcal{F}$ is defined by $\langle Ts,t\rangle=\langle s,T^{\dagger}t\rangle$, and it is the archetype of the operators built from an involution. The dagger is the operator-layer mark of the corpus, and the Hermitian pairing is the structure that makes it exist: an operator has an adjoint exactly when it has a partner under a nondegenerate Hermitian pairing.

This article fixes the sesquilinear and Hermitian pairings, the adjoint of a morphism, the classification of the endomorphisms into the self-adjoint, skew-adjoint, unitary, normal and involutive ones with the eigensheaf decomposition of an involution, the Hermitian dual and the nondegeneracy, the compatibility of the pairing with the involution and with the descent, and the positive-definite case as a boundary leading to the metric theory. It is the second article of the `- * Operator Theory` group; the involution itself and its action on the cohomology are the previous group, the endomorphism sheaf is *The Sheaf of Operators*, the descent of the pairing and the involution on the cohomology is *Descent and the Involution on the Cohomology*, the Hermitian forms and the adjoints on an algebra are *Hermitian Adjoints on a Hilbert Algebra* and *Hermitian Forms on a Hilbert Algebra with Hermitian Adjoint* of Part I, and the metrics, the spectra and the positivity of the analysis are Part III.

The article uses no analysis and no geometry: the pairings are algebraic pairings of sheaves of modules, the conjugate-linearity is a semilinearity with respect to an involution of the structure sheaf, and positive-definiteness is defined only when a positive cone is available and is otherwise deferred. No norm and no derivative occurs. Throughout, $\sigma$ is an involution of the structure sheaf $\mathcal{O}_X$, $\mathcal{F},\mathcal{G}$ are sheaves of $\mathcal{O}_X$-modules, $\langle-,-\rangle$ is a $\sigma$-sesquilinear pairing, and the adjoint of a morphism is written with the dagger $T^{\dagger}$.

## Sesquilinear and Hermitian Pairings

**Definition.** A **$\sigma$-sesquilinear pairing** of $\mathcal{F}$ and $\mathcal{G}$ with values in $\mathcal{O}_X$ is a morphism of sheaves

$$
\langle-,-\rangle:\mathcal{F}\times\mathcal{G}\longrightarrow\mathcal{O}_X,\qquad \langle as,t\rangle=\sigma(a)\langle s,t\rangle,\qquad \langle s,at\rangle=a\langle s,t\rangle,
$$

for all sections $a$ of $\mathcal{O}_X$ and sections $s,t$ of $\mathcal{F},\mathcal{G}$ over the same open set, bilinear over the constants; it is **Hermitian** if in addition

$$
\langle s,t\rangle=\sigma\bigl(\langle t,s\rangle\bigr)\quad\text{when }\mathcal{G}=\mathcal{F},
$$

and **skew-Hermitian** if $\langle s,t\rangle=-\sigma(\langle t,s\rangle)$. A **Hermitian structure** on $\mathcal{F}$ is a Hermitian pairing $\langle-,-\rangle:\mathcal{F}\times\mathcal{F}\to\mathcal{O}_X$.

**Proposition (the pairing as a morphism to the dual).** A $\sigma$-sesquilinear pairing $\mathcal{F}\times\mathcal{G}\to\mathcal{O}_X$ is the same thing as a morphism of sheaves $\mathcal{G}\to\mathcal{F}^{\vee,\sigma}$, where $\mathcal{F}^{\vee,\sigma}=\mathcal{H}om_{\sigma}(\mathcal{F},\mathcal{O}_X)$ is the sheaf of $\sigma$-antilinear morphisms $\mathcal{F}\to\mathcal{O}_X$; the pairing is **nondegenerate** when this morphism is an isomorphism, and a nondegenerate Hermitian structure on $\mathcal{F}$ is the same thing as an isomorphism $\mathcal{F}\cong\mathcal{F}^{\vee,\sigma}$ that is its own adjoint.

*Proof.* For a fixed section $t$ of $\mathcal{G}$ the assignment $s\mapsto\langle s,t\rangle$ is $\sigma$-antilinear in $s$ by the first axiom and linear in $t$ by the second, so it defines a section of $\mathcal{F}^{\vee,\sigma}$, and the assignment is a morphism $\mathcal{G}\to\mathcal{F}^{\vee,\sigma}$; conversely a morphism gives a pairing by evaluation, and the two constructions are inverse. The nondegeneracy is the statement that the morphism is an isomorphism in each stalk, and the self-adjointness of the Hermitian case is the symmetry $\langle s,t\rangle=\sigma(\langle t,s\rangle)$ read through the identification.

**Remark (the conjugate-linear dual).** The sheaf $\mathcal{F}^{\vee,\sigma}$ is $\sigma$-antilinear in its argument and is not the usual linear dual $\mathcal{F}^{\vee}=\mathcal{H}om(\mathcal{F},\mathcal{O}_X)$ unless $\sigma=\mathrm{id}$; for the identity involution the two coincide and the Hermitian pairing becomes an ordinary symmetric bilinear pairing. The distinction is the source of every sign and every bar in the theory.

## The Adjoint of a Morphism

**Definition.** Let $\langle-,-\rangle_{\mathcal{F}}$ and $\langle-,-\rangle_{\mathcal{G}}$ be Hermitian structures on $\mathcal{F}$ and on $\mathcal{G}$, and let $T:\mathcal{F}\to\mathcal{G}$ be a morphism. The **adjoint** of $T$, when it exists, is the morphism $T^{\dagger}:\mathcal{G}\to\mathcal{F}$ with

$$
\langle Ts,t\rangle_{\mathcal{G}}=\langle s,T^{\dagger}t\rangle_{\mathcal{F}}
$$

for all sections $s$ of $\mathcal{F}$ and $t$ of $\mathcal{G}$ over the same open set.

**Theorem (existence and the dagger laws).** If the Hermitian structures are nondegenerate, every morphism $T:\mathcal{F}\to\mathcal{G}$ has a unique adjoint $T^{\dagger}:\mathcal{G}\to\mathcal{F}$, and the dagger satisfies

$$
(T^{\dagger})^{\dagger}=T,\qquad (ST)^{\dagger}=T^{\dagger}S^{\dagger},\qquad (T+S)^{\dagger}=T^{\dagger}+S^{\dagger},\qquad (aT)^{\dagger}=\sigma(a)T^{\dagger},
$$

for composable morphisms and sections $a$ of $\mathcal{O}_X$; the dagger is therefore a $\sigma$-semilinear anti-involution of the sheaf of endomorphisms.

*Proof.* The pairing $\langle Ts,-\rangle_{\mathcal{G}}$ is a section of $\mathcal{G}^{\vee,\sigma}$ and the nondegeneracy identifies $\mathcal{G}^{\vee,\sigma}$ with $\mathcal{G}$, so there is a unique $t'=T^{\dagger}t$ with $\langle Ts,t\rangle_{\mathcal{G}}=\langle s,t'\rangle_{\mathcal{F}}$ for every $s$; the assignment $t\mapsto t'$ is a morphism because the pairing is morphic in $t$, and the uniqueness is the nondegeneracy. The laws are the equalities of the two sides read through the same pairing: $(T^{\dagger})^{\dagger}=T$ from the symmetry of the definition, $(ST)^{\dagger}=T^{\dagger}S^{\dagger}$ from the associativity of the composition, and $(aT)^{\dagger}=\sigma(a)T^{\dagger}$ from the $\sigma$-sesquilinearity.

**Proposition (the adjoint as a morphism of the dual).** Under the identification $\mathcal{F}\cong\mathcal{F}^{\vee,\sigma}$ of a nondegenerate Hermitian structure, the adjoint of $T:\mathcal{F}\to\mathcal{G}$ is the transpose of $T$ under the duality, $T^{\dagger}=\tau(T)$; the dagger is the transport of the transpose along the Hermitian identification of the sheaves with their conjugate-linear duals.

*Proof.* The transpose $\tau(T):\mathcal{G}^{\vee,\sigma}\to\mathcal{F}^{\vee,\sigma}$ is defined by precomposition, and the identification of the sheaves with their duals turns the relation $\langle Ts,t\rangle_{\mathcal{G}}=\langle s,T^{\dagger}t\rangle_{\mathcal{F}}$ into the defining relation of the transpose; the computation is the one of *Hermitian Adjoints on a Hilbert Algebra* in the sheaf setting.

**Example (the free sheaf).** For the free sheaf $\mathcal{O}_X^n$ with the involution $\sigma$ and the standard pairing $\langle u,v\rangle=\sum_i\sigma(u_i)v_i$, the adjoint of a morphism given by a matrix $(a_{ij})$ is the matrix $(\sigma(a_{ji}))$, the conjugate transpose; for $\sigma=\mathrm{id}$ this is the transpose, and for the conjugation of a complexification it is the conjugate transpose. The example is the model of the dagger.

## The Self-Adjoint, Skew, Unitary and Normal Endomorphisms

**Definition.** An endomorphism $T$ of a sheaf $\mathcal{F}$ with a nondegenerate Hermitian structure is **self-adjoint**, or **Hermitian**, if $T^{\dagger}=T$; **skew-adjoint** if $T^{\dagger}=-T$; **normal** if $TT^{\dagger}=T^{\dagger}T$; **unitary** if $TT^{\dagger}=T^{\dagger}T=\mathrm{id}$; and an **involution** if it is unitary with $T^2=\mathrm{id}$. The endomorphisms are classified by their relation to the dagger, which is the operator-layer involution of the theory.

**Theorem (the endomorphism sheaf is an involutive sheaf of rings).** The dagger is a $\sigma$-semilinear anti-involution of the sheaf of algebras $\mathcal{E}nd(\mathcal{F})$, so that $\mathcal{E}nd(\mathcal{F})$ is an involutive sheaf of rings in the sense of *The Involution on the Structure Sheaf*: its fixed part is the subsheaf $\mathcal{H}(\mathcal{F})$ of Hermitian endomorphisms and its anti-invariant part the subsheaf $\mathcal{S}(\mathcal{F})$ of skew-adjoint endomorphisms. If $2$ is invertible in $\mathcal{O}_X(X)$,

$$
\mathcal{E}nd(\mathcal{F})=\mathcal{H}(\mathcal{F})\oplus\mathcal{S}(\mathcal{F}),\qquad T=\tfrac12(T+T^{\dagger})+\tfrac12(T-T^{\dagger}),
$$

the Hermitian part is closed under the **Jordan product** $T\bullet S=\frac12(TS+ST)$ and is a sheaf of Jordan algebras, and the skew part is closed under the **commutator** $[T,S]=TS-ST$ and is a sheaf of Lie algebras.

*Proof.* The dagger laws of the previous section are the axioms of a $\sigma$-semilinear anti-involution, with the fixed elements the Hermitian endomorphisms and the anti-invariant elements the skew ones. The decomposition is the sectionwise decomposition of the fixed and anti-invariant parts of an involutive algebra of *Involutive Bilinear Algebras*; the Hermitian part is closed under the anticommutator and the skew part under the commutator, and the closure of the Hermitian part under the ordinary product would require $TS=T^{\dagger}S^{\dagger}=ST$, that is, the commutativity of the factors.

**Proposition (the unitary sheaf and its Lie algebra sheaf).** The unitary endomorphisms form a sheaf of groups $\mathcal{U}(\mathcal{F})$ acting on $\mathcal{F}$ by Hermitian automorphisms, and its Lie algebra sheaf is $\mathcal{S}(\mathcal{F})$: an endomorphism $T$ makes $\mathrm{id}+\epsilon T$ unitary to first order, $\epsilon^2=0$, exactly when $T$ is skew-adjoint.

*Proof.* The unitarity of $\mathrm{id}+\epsilon T$ reads $(\mathrm{id}+\epsilon T)^{\dagger}(\mathrm{id}+\epsilon T)=\mathrm{id}+\epsilon(T+T^{\dagger})$ to first order, which is $\mathrm{id}$ exactly when $T+T^{\dagger}=0$; the group axioms of the unitary sheaf are the dagger laws.

**Theorem (involutions and the eigensheaf decomposition).** Let $T$ be unitary with $T^2=\mathrm{id}$. Then $T$ is self-adjoint, $T^{\dagger}=T$, and if $2$ is invertible the sheaf decomposes as the direct sum of the eigensheaves

$$
\mathcal{F}=\mathcal{F}_+\oplus\mathcal{F}_-,\qquad \mathcal{F}_{\pm}=\ker(T\mp\mathrm{id}),\qquad \pi_{\pm}=\tfrac12(\mathrm{id}\pm T),
$$

the projections being morphisms of sheaves with $\pi_++\pi_-=\mathrm{id}$ and $\pi_+\pi_-=0$.

*Proof.* From $T^{\dagger}T=\mathrm{id}$ and $T^2=\mathrm{id}$ we get $T^{\dagger}=T^{\dagger}TT=(T^{\dagger}T)T=T$, so $T$ is self-adjoint. The projections $\pi_{\pm}$ are idempotent and orthogonal because $T^2=\mathrm{id}$, and they exhibit the sheaf as the direct sum of their images.

**Theorem (the agreement of the two layers).** Let $u$ be an equivariant structure of order two on $\mathcal{F}$, as in *The Involution on the Structure Sheaf*, compatible with the Hermitian structure: $\langle u(s),u(t)\rangle=\sigma(\langle s,t\rangle)$. Then $u$ is a self-adjoint unitary endomorphism, the fixed eigensheaf $\mathcal{F}_+$ is the fixed sheaf of the element involution and the anti-invariant eigensheaf $\mathcal{F}_-$ is the anti-invariant sheaf; the element involution and the operator adjoint agree, and the equivariant structure is a $\ast$-representation of the two-element group. Without the compatibility hypothesis the two structures differ: the element involution need not be self-adjoint, and its fixed sheaf need not be the $+1$-eigensheaf of the adjoint.

*Proof.* The compatibility condition is exactly $\langle u(s),t\rangle=\langle s,u(t)\rangle$ by the Hermitian symmetry, so $u^{\dagger}=u$; the eigensheaves are the fixed and anti-invariant sheaves of the element involution by their definition, and on the endomorphisms commuting with $u$ the adjoint acts blockwise as the element involution does. The hypothesis is a genuine restriction on the pairing, and without it the two fixed objects differ, as the matrix model of the next section shows.

**Example (the matrix model).** For the free sheaf $\mathcal{O}_X^n$, the Hermitian endomorphisms are the matrices with $A^{\dagger}=A$ for the conjugate transpose, the skew ones those with $A^{\dagger}=-A$, the unitary ones those with $A^{\dagger}A=AA^{\dagger}=\mathrm{id}$, and an involution is a unitary matrix with $A^2=\mathrm{id}$; the eigensheaf decomposition is the decomposition into the $+1$ and $-1$ eigenspaces. The example is the matrix model of the classification.

## Positivity and the Metric Case

**Definition.** Suppose the structure sheaf carries a **positive cone** $\mathcal{O}_X^+\subseteq\mathcal{O}_X^{\sigma}$ closed under sums and products, containing the squares, and total: every self-adjoint section is in $\mathcal{O}_X^+\cup(-\mathcal{O}_X^+)$. A Hermitian structure is **positive definite** if $\langle s,s\rangle\in\mathcal{O}_X^+$ for every section $s$ and $\langle s,s\rangle=0$ only for $s=0$; it is then a **Hermitian metric**.

**Proposition (the associated norm).** A Hermitian metric on $\mathcal{F}$ gives a norm on the sections over an open set of positive cone $\mathcal{O}_X^+(U)$, $s\mapsto\|s\|$ with $\|s\|^2=\langle s,s\rangle$, and the metric makes the endomorphism sheaf an involutive algebra with the dagger; the completeness of the norm is not part of the algebraic theory.

*Proof.* The axioms of a norm are those of the Hermitian form of *Hermitian Adjoints on a Hilbert Algebra* transported sectionwise, with the triangle inequality from the Cauchy–Schwarz inequality of the positive definite pairing; the completeness is a statement of analysis and is not used.

**Remark (the boundary).** The positive definite case is the entry to the metric and analytic theory of sheaves, in which the sections are completed to Hilbert spaces, the pairings are the fibres of a Hermitian vector bundle, and the operators are bounded; the subject is that of *Hilbert Algebras*, *Hermitian Adjoints on a Hilbert Algebra* and the Hilbert $C^*$-module articles of Part III. The present article keeps the pairing algebraic and states the positivity as a boundary; the algebraic content of the adjoint is already complete without it.

## The Pairing, the Involution and the Descent

**Proposition (the pairing and the involution).** Let $\mathcal{F}$ and $\mathcal{G}$ carry $\sigma$-equivariant structures as in *The Involution on the Structure Sheaf*, and let the pairing be compatible with them: $\langle u_{\mathcal{F}}(s),u_{\mathcal{G}}(t)\rangle=\sigma(\langle s,t\rangle)$ under the equivariant structures $u$. Then the adjoint of an equivariant morphism is equivariant, the dagger commutes with the involution, and the pairing restricts to the fixed parts as an $\mathcal{O}_X^{\sigma}$-valued Hermitian pairing.

*Proof.* The compatibility condition is the equivariance of the pairing, and the adjoint is determined by the pairing, so it is equivariant; on the fixed parts the involution acts trivially and the pairing takes values in the fixed structure sheaf.

**Proposition (the descent of a Hermitian pairing).** Under the descent of *Sheaves with a Real Structure* or of *Galois Descent for Sheaves*, a Hermitian pairing on a complex or extended sheaf compatible with the real or the Galois structure descends to a Hermitian pairing on the descended sheaf over the fixed structure sheaf; the adjoint descends with it.

*Proof.* The pairing is a morphism $\mathcal{G}\to\mathcal{F}^{\vee,\sigma}$ that is equivariant for the involution, so it descends by the descent of the equivariant sheaves; the descended pairing is $\mathcal{O}_X^{\sigma}$-valued and Hermitian for the descended structure, and the adjoint, being determined by the pairing, descends with it.

**Remark (the pairing on the cohomology).** A Hermitian pairing of sheaves induces pairings on the cohomology through the cup product of *The Cup Product on Sheaf Cohomology* and a trace or an evaluation: for a proper map and a dualising sheaf, the pairing $\mathcal{F}\times\mathcal{G}\to\omega$ gives $H^p(X,\mathcal{F})\times H^q(X,\mathcal{G})\to H^{p+q}(X,\omega)$, and when $X$ is compact and $\omega$ is the constants modulo the top cohomology this is the intersection pairing of Poincaré duality, *Poincaré Duality*; the adjoints of the operators on the cohomology are then taken with respect to this pairing. The construction is stated for orientation and is not developed here.

## Worked Cases

### The Standard Pairing on a Free Sheaf

For the free sheaf $\mathcal{O}_X^n$ with the involution $\sigma$ of the structure sheaf and the pairing $\langle u,v\rangle=\sum_i\sigma(u_i)v_i$, the adjoint of the matrix $(a_{ij})$ is $(\sigma(a_{ji}))$, the self-adjoint morphisms are the matrices with $a_{ij}=\sigma(a_{ji})$, and the unitary morphisms are the matrices with $A^{\dagger}A=AA^{\dagger}=\mathrm{id}$. For the identity involution the theory reduces to the symmetric bilinear pairings and the transpose; for the conjugation of a complexification it is the Hermitian linear algebra of Part I.

### The Pairing over a Point

Over a point the sheaves are vector spaces, the pairing is a Hermitian form, and the adjoint is the conjugate transpose of a matrix with respect to the form; the self-adjoint operators are the Hermitian matrices, the unitary operators the unitary matrices, and the theory is that of *Hermitian Adjoints on a Hilbert Algebra* and *Hermitian Forms on a Hilbert Algebra with Hermitian Adjoint*, without the sheaf-theoretic complications of the morphisms between different sheaves.

### The Invariant Pairing of a Group Action

For a group acting on $X$ and a Hermitian pairing invariant under the action, the pairing descends to the quotient by *Equivariant Sheaves and Descent*; the descended pairing is Hermitian for the descended structure sheaf, and the adjoint of a descended operator is the descent of the adjoint. The example connects the Hermitian structure to the descent and is the model of the invariant forms of the invariant theory.

## Summary

A Hermitian pairing of sheaves is a $\sigma$-sesquilinear pairing $\langle-,-\rangle:\mathcal{F}\times\mathcal{G}\to\mathcal{O}_X$, linear in the second variable and $\sigma$-linear in the first, Hermitian when $\langle s,t\rangle=\sigma(\langle t,s\rangle)$; it is the same thing as a morphism $\mathcal{G}\to\mathcal{F}^{\vee,\sigma}$ to the conjugate-linear dual, and it is nondegenerate when that morphism is an isomorphism. A nondegenerate Hermitian structure is the structure relative to which every morphism $T:\mathcal{F}\to\mathcal{G}$ has a unique adjoint $T^{\dagger}:\mathcal{G}\to\mathcal{F}$, with the dagger laws $(T^{\dagger})^{\dagger}=T$, $(ST)^{\dagger}=T^{\dagger}S^{\dagger}$, $(T+S)^{\dagger}=T^{\dagger}+S^{\dagger}$ and $(aT)^{\dagger}=\sigma(a)T^{\dagger}$: the dagger is a $\sigma$-semilinear anti-involution of the endomorphism sheaf, and it is the transport of the transpose under the identification of the sheaves with their conjugate-linear duals.

The endomorphisms are classified by the dagger: the self-adjoint, the skew-adjoint, the unitary, the normal and the involutions. The endomorphism sheaf is an involutive sheaf of rings whose fixed part is the sheaf of Hermitian endomorphisms and whose anti-invariant part is the sheaf of skew endomorphisms; when $2$ is invertible it decomposes as $\mathcal{E}nd(\mathcal{F})=\mathcal{H}(\mathcal{F})\oplus\mathcal{S}(\mathcal{F})$, the Hermitian part being a sheaf of Jordan algebras under the anticommutator and the skew part a sheaf of Lie algebras under the commutator, and the unitary endomorphisms form a sheaf of groups whose Lie algebra sheaf is the skew part. A unitary endomorphism of order two is self-adjoint and decomposes the sheaf into the eigensheaves of $+1$ and $-1$ with the projections $\frac12(\mathrm{id}\pm T)$; the element involution and the operator adjoint agree exactly when the Hermitian structure is compatible with the equivariant structure, in which case the equivariant structure is a self-adjoint unitary endomorphism and the representation is a $\ast$-representation.

The positive definite case, when a positive cone is available in the structure sheaf, is the Hermitian metric and the entry to the metric theory of Part III; it is stated as a boundary and not developed. The pairing is compatible with the involution of the structure sheaf and descends along the real structure and the Galois descent, the adjoint descending with it; on the cohomology the pairing induces the intersection pairings through the cup product, stated for orientation. The free sheaf with the conjugate transpose is the model of the whole theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle-,-\rangle:\mathcal{F}\times\mathcal{G}\to\mathcal{O}_X$ | $\sigma$-sesquilinear pairing; $\sigma$-linear in the first variable, linear in the second |
| $\langle s,t\rangle=\sigma(\langle t,s\rangle)$ | Hermitian symmetry; the skew case with a minus sign |
| $\mathcal{F}^{\vee,\sigma}=\mathcal{H}om_{\sigma}(\mathcal{F},\mathcal{O}_X)$ | conjugate-linear dual; a pairing $=$ a morphism $\mathcal{G}\to\mathcal{F}^{\vee,\sigma}$ |
| nondegenerate pairing | the morphism $\mathcal{G}\to\mathcal{F}^{\vee,\sigma}$ is an isomorphism |
| $T^{\dagger}$ | adjoint; $\langle Ts,t\rangle_{\mathcal{G}}=\langle s,T^{\dagger}t\rangle_{\mathcal{F}}$ |
| $(T^{\dagger})^{\dagger}=T$, $(ST)^{\dagger}=T^{\dagger}S^{\dagger}$, $(aT)^{\dagger}=\sigma(a)T^{\dagger}$ | the dagger laws; a $\sigma$-semilinear anti-involution |
| $\mathcal{H}(\mathcal{F})$, $\mathcal{S}(\mathcal{F})$ | sheaves of Hermitian and skew-adjoint endomorphisms; the fixed and anti-invariant parts of the dagger |
| $\mathcal{E}nd(\mathcal{F})=\mathcal{H}\oplus\mathcal{S}$ | decomposition when $2$ is invertible; Jordan structure on $\mathcal{H}$, Lie structure on $\mathcal{S}$ |
| $\mathcal{F}=\mathcal{F}_+\oplus\mathcal{F}_-$, $\pi_{\pm}=\frac12(\mathrm{id}\pm T)$ | eigensheaf decomposition of an involution $T$; $T^2=\mathrm{id}$ |
| $\mathcal{O}_X^+$ | positive cone of the structure sheaf; used only for the positive definite case |
| Hermitian metric | positive definite Hermitian structure; the boundary to Part III |
| $H^p(X,\mathcal{F})\times H^q(X,\mathcal{G})\to H^{p+q}(X,\omega)$ | induced pairing on cohomology; orientation only |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the Hermitian forms, the adjoints and the involutions of the algebras.
- Serge Lang, *Algebra* (Springer, revised third edition, 2002), for the Hermitian forms and the adjoints of the linear algebra, cited for the models.
- Alexander Grothendieck, *Éléments de géométrie algébrique* and the duality theory, for the conjugate-linear duals and the pairings on the cohomology; see also Robin Hartshorne, *Residues and Duality* (Springer Lecture Notes in Mathematics 20, 1966).
- Glen E. Bredon, *Sheaf Theory* (Springer, second edition, 1997), for the pairings of sheaves and their induced pairings on the cohomology.
- Masaki Kashiwara and Pierre Schapira, *Sheaves on Manifolds* (Springer, 1990), for the Verdier duality and the pairings of the derived category.
- Michael Atiyah, "K-theory and reality", *Quarterly Journal of Mathematics* (2) 17 (1966), 367–386, for the Hermitian structures compatible with a real structure, cited for the descent.
