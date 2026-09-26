
# __Separable Algebras__

## Introduction

A **separable algebra** is an algebra whose multiplication remains as well behaved as possible under every extension of scalars. Over a field it is the same condition as semisimplicity when the field is perfect, and in general it adds to semisimplicity the requirement that the centre be a product of separable field extensions; over a commutative ring it is the condition that the multiplication map split as a map of bimodules, and it becomes the algebraic theory of the **Azumaya algebra** and the **étale algebra**, the two notions that generalise central simple algebras and finite separable field extensions from a field to a ring.

The article is the third of the structure-theoretic articles of the category. It follows *Central Simple Algebras and the Brauer Group* and *Crossed Products*, whose objects it re-reads as the central separable algebras over a field and over a ring, and it precedes the representation-theoretic layer that begins. The separable field extension is treated first, by the elementary test on minimal polynomials, because it is the case in which the definition can be checked directly; the algebra definition is then given, first over a field and then over a commutative ring, and the two are shown to agree.

The article is algebraic throughout. The trace form of a field extension, the discriminant of a form, and the non-degeneracy of a bilinear pairing are tools of Part II, where bilinear and quadratic forms are introduced; where the classical theory would use them, this article substitutes the resultant of two polynomials and explicit polynomial identities, which are available here. The étale algebras are the commutative separable algebras of this article; their sheaf-theoretic description over a site belongs to the later Part, and the affine morphisms that they model belong to algebraic geometry.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$ and $A$ is a unital associative $R$-algebra that is finitely generated and projective as an $R$-module where stated. We write

$$
A^{\mathrm{e}} = A \otimes_R A^{\mathrm{op}}
$$

for the **enveloping algebra** of $A$, and $\mu : A^{\mathrm{e}} \to A$ for the multiplication, $\mu(a \otimes b) = ab$. The algebra $A^{\mathrm{e}}$ is an $R$-algebra and every $A$-bimodule is a left $A^{\mathrm{e}}$-module, with $(a\otimes b)\cdot m = amb$.

## Separable Field Extensions

### Definition and the polynomial test

**Definition.** Let $L/F$ be an algebraic field extension. An element $\alpha \in L$ is **separable** over $F$ if its minimal polynomial $f_\alpha \in F[x]$ has distinct roots in a splitting field, equivalently if $f_\alpha$ and its formal derivative $f_\alpha'$ have no common root, equivalently if $\gcd(f_\alpha, f_\alpha') = 1$ in $F[x]$. The extension $L/F$ is **separable** if every element of $L$ is separable over $F$.

The criterion is intrinsic and uses no form theory: $f$ has a repeated root exactly when $\gcd(f,f') \neq 1$, and the gcd is computed in $F[x]$ by the Euclidean algorithm.

**Proposition.** Every algebraic extension of a field of characteristic $0$ is separable. Every algebraic extension of a finite field is separable. A field $F$ every algebraic extension of which is separable is called **perfect**, so fields of characteristic $0$ and finite fields are perfect.

*Proof.* If $f \in F[x]$ is irreducible of degree $n$ and $f' \neq 0$ has degree $n-1$, then $f \nmid f'$, so $\gcd(f,f') = 1$ and $f$ has distinct roots. Over a field of characteristic $0$ every irreducible $f$ has $f' \neq 0$. Over a finite field $F = \mathbb{F}_q$, an irreducible $f$ of degree $n$ divides $x^{q^n} - x$, whose derivative is $-1$, so $f$ is coprime to its derivative; hence $f$ is separable. $\square$

**Example (a non-separable extension).** Let $F = \mathbb{F}_p(t)$ be the field of rational functions in one variable over $\mathbb{F}_p$ and let $L = F(t^{1/p})$. Then $t^{1/p} \notin F$ and its minimal polynomial is $x^p - t$, whose derivative $px^{p-1}$ is zero; so $x^p - t = (x - t^{1/p})^p$ has a single root of multiplicity $p$, and $L/F$ is not separable. This is the standard example: non-separability is a phenomenon of imperfect fields in positive characteristic.

### Separability and the number of embeddings

**Theorem.** Let $L/F$ be a finite extension of degree $n$ and let $\bar F$ be an algebraic closure. Then the number of distinct $F$-embeddings $L \to \bar F$ is at most $n$, and it equals $n$ if and only if $L/F$ is separable.

*Proof.* Write $L = F(\alpha_1,\dots,\alpha_r)$ and build the tower $F = L_0 \subseteq L_1 \subseteq \cdots \subseteq L_r = L$ with $L_i = L_{i-1}(\alpha_i)$. An embedding of $L_i$ extending a fixed embedding of $L_{i-1}$ is determined by the image of $\alpha_i$, which must be a root in $\bar F$ of the minimal polynomial of $\alpha_i$ over $L_{i-1}$; the number of such roots is at most $[L_i : L_{i-1}]$, with equality exactly when that minimal polynomial is separable. Multiplying over the tower gives the bound and the criterion. $\square$

**Corollary.** If $L/F$ is finite separable then $L = F(\alpha)$ for some $\alpha$, and the minimal polynomial of $\alpha$ has degree $[L:F]$ and distinct roots.

*Proof.* The theorem of the primitive element for finite separable extensions follows by choosing $\alpha$ whose minimal polynomial has degree $[L:F]$, which the embedding count guarantees; the proof is the standard induction on the number of generators. $\square$

## Separable Algebras over a Field

### Definition and the centre criterion

**Definition.** Let $F$ be a field and let $A$ be a finite-dimensional unital $F$-algebra. Then $A$ is **separable** over $F$ if $A \otimes_F L$ is semisimple for every field extension $L/F$.

It suffices to test one extension: $A$ is separable if and only if $A \otimes_F \bar F$ is semisimple for an algebraic closure $\bar F$, because a finite-dimensional algebra is semisimple over a field exactly when its base change to an algebraic closure is. This is the definition used in practice.

**Theorem (the structure of separable algebras).** Let $A$ be a finite-dimensional unital $F$-algebra. Then $A$ is separable over $F$ if and only if

$$
A \;\cong\; \prod_{i=1}^r M_{n_i}(D_i)
$$

where each $D_i$ is a finite-dimensional division algebra over $F$ whose centre $Z(D_i)$ is a finite separable field extension of $F$.

*Proof (outline).* If $A$ is separable, then $A$ is semisimple, so Wedderburn–Artin gives $A \cong \prod_i M_{n_i}(D_i)$, and the centre is $Z(A) \cong \prod_i Z(D_i)$, a product of fields finite over $F$. Each $Z(D_i)$ is separable over $F$, because if $Z(D_i)$ contained a non-separable element then $D_i \otimes_F \bar F$ would acquire nilpotents and fail to be semisimple. Conversely, if each $D_i$ has separable centre, then $D_i \otimes_F \bar F$ is a product of matrix algebras over $\bar F$ — the centre splits into a product of copies of $\bar F$ and the division algebra becomes a matrix algebra over each copy — so $A \otimes_F \bar F$ is a product of matrix algebras and is semisimple. $\square$

**Corollary.** If $F$ is perfect — in particular if $F$ has characteristic $0$ or is finite — then a finite-dimensional $F$-algebra is separable if and only if it is semisimple. Over an arbitrary field, separable implies semisimple, but the field extension $L/F$ of the example above is a division algebra over $F$ that is not separable.

**Corollary.** Every finite-dimensional central simple $F$-algebra is separable, because its centre is $F$, and $F$ is trivially separable over itself. Hence the central simple algebras of *Central Simple Algebras and the Brauer Group* form a subclass of the separable algebras, the subclass on which the centre is as small as possible.

### The separability idempotent

**Theorem (bimodule characterisation over a field).** For a finite-dimensional unital $F$-algebra $A$, the following are equivalent:

1. $A$ is separable over $F$;
2. the multiplication map $\mu : A^{\mathrm{e}} \to A$ splits as a homomorphism of $A^{\mathrm{e}}$-modules, that is, there is an $A$-bimodule map $s : A \to A^{\mathrm{e}}$ with $\mu \circ s = \mathrm{id}_A$;
3. there is an idempotent $e \in A^{\mathrm{e}}$ with $\mu(e) = 1$, where $e = \sum_i x_i \otimes y_i$ satisfies
$$
\sum_i x_i y_i = 1, \qquad \sum_i a x_i \otimes y_i = \sum_i x_i \otimes y_i a \quad \text{for all } a \in A .
$$

The element $e$ is the **separability idempotent**; condition 3 is the explicit form of condition 2, since an $A^{\mathrm{e}}$-linear splitting is determined by the image $s(1) = e$, and $\mu\circ s = \mathrm{id}$ says $\mu(e) = 1$ while $s$ being $A^{\mathrm{e}}$-linear says $ae = ea$ for all $a$ under the identification of $A$ with the diagonal copy of $A^{\mathrm{e}}$.

*Proof (equivalences).* The equivalence of 2 and 3 is the observation just made. For $2 \Rightarrow 1$, suppose $\mu$ splits and let $M$ be any $A$-bimodule. Applying $\operatorname{Hom}_{A^{\mathrm{e}}}(-, M)$ to a split exact sequence preserves exactness, so every $A^{\mathrm{e}}$-linear map out of $A$ extends; taking $M = A$ shows that $A$ is projective as an $A^{\mathrm{e}}$-module. Projectivity of $A$ over $A^{\mathrm{e}}$ is equivalent to semisimplicity of $A$ when $A$ is finite-dimensional over $F$, by the Wedderburn–Artin description of $A^{\mathrm{e}}$-modules; and the argument applies after every base change, giving separability. For $1 \Rightarrow 2$, if $A$ is semisimple, then $A^{\mathrm{e}}$ is semisimple, $A$ is a projective $A^{\mathrm{e}}$-module, and $\mu$ splits. $\square$

**Example.** For $A = M_n(F)$ the separability idempotent is built from the matrix units: with $A^{\mathrm{e}} = M_n(F)\otimes_F M_n(F)^{\mathrm{op}}$,

$$
e = \sum_{i,j=1}^n E_{ij} \otimes E_{ji}, \qquad \mu(e) = \sum_{i,j} E_{ij}E_{ji} = \sum_j E_{jj} = I_n ,
$$

and the bimodule condition holds because $\sum_{i,j} a E_{ij} \otimes E_{ji} = \sum_{i,j} E_{ij}\otimes E_{ji} a$ for every $a$. This element is the algebraic model of the identity matrix, and it is exactly the element that makes $M_n(F)$ separable.

## Separable Algebras over a Commutative Ring

### Definition

**Definition.** Let $R$ be a commutative ring. A unital associative $R$-algebra $A$, finitely generated and projective as an $R$-module, is **separable** over $R$ if the multiplication $\mu : A^{\mathrm{e}} \to A$ splits as a homomorphism of $A^{\mathrm{e}}$-modules. Equivalently, the separability idempotent condition

$$
\exists\, e = \sum_i x_i \otimes y_i \in A^{\mathrm{e}}, \qquad \mu(e) = 1, \quad ae = ea \ \text{for all } a \in A
$$

holds; equivalently $A$ is a projective left $A^{\mathrm{e}}$-module.

**Theorem (Hattori–Villamayor, standard).** Let $A$ be a finitely generated projective $R$-algebra. The following are equivalent:

1. $A$ is separable over $R$;
2. $A$ is a projective $A^{\mathrm{e}}$-module;
3. for every $A$-bimodule $M$ and every $A$-bimodule map $f : A \to M$, every $R$-linear derivation $D : A \to M$ is inner, that is, $D(a) = am - ma$ for some $m \in M$;
4. the functor $\operatorname{Hom}_{A^{\mathrm{e}}}(A,-)$ is exact.

*Proof (sketch).* The equivalence of 1 and 2 is the definition restated, since $\mu$ is a surjection of $A^{\mathrm{e}}$-modules and a surjection splits exactly when the source is projective over the target's complement. Statement 3 is the universal property of the module of Kähler differentials recast: derivations $A \to M$ correspond to $A^{\mathrm{e}}$-linear maps $\Omega_{A/R} \to M$, and every such map is inner exactly when the universal derivation is inner, which is equivalent to $A$ being projective over $A^{\mathrm{e}}$. Statement 4 is the exactness of the functor represented by a projective object. $\square$

### Base change and examples

**Proposition.** Separability is preserved by base change: if $A$ is separable over $R$ and $R \to S$ is a homomorphism of commutative rings, then $A \otimes_R S$ is separable over $S$.

*Proof.* The separability idempotent $e \in A^{\mathrm{e}}$ base-changes to an element $e \otimes 1 \in (A\otimes_R S)^{\mathrm{e}} \cong A^{\mathrm{e}}\otimes_R S$ with $\mu(e\otimes1) = 1$ and $(a\otimes1)(e\otimes1) = (e\otimes1)(a\otimes1)$. $\square$

**Example (matrix algebras).** For every $n \geq 1$ and every commutative ring $R$, the algebra $M_n(R)$ is separable over $R$, with the idempotent $e = \sum_{i,j} E_{ij}\otimes E_{ji}$ of the field case, which is an element of $M_n(R)\otimes_R M_n(R)^{\mathrm{op}}$ with no denominators.

**Example (products).** If $A$ and $B$ are separable over $R$, then $A \times B$ is separable over $R$, with separability idempotent $e_A + e_B$ under the identification $(A\times B)^{\mathrm{e}} \cong A^{\mathrm{e}} \times B^{\mathrm{e}} \times (A\otimes_R B^{\mathrm{op}}) \times (B\otimes_R A^{\mathrm{op}})$ restricted to the two diagonal blocks; in particular $R \times R$ is separable over $R$.

**Example (polynomial quotients and the resultant criterion).** Let $f \in R[x]$ be monic of degree $n$ and let $A = R[x]/(f)$. Then $A$ is a free $R$-module of rank $n$ and

$$
A \ \text{is separable over } R \iff (f, f') = R[x] \iff \operatorname{Res}(f, f') \in R^\times ,
$$

where $\operatorname{Res}$ is the resultant, the determinant of the Sylvester matrix of $f$ and $f'$. The first equivalence is the classical Jacobian criterion for a polynomial quotient and the second holds because the resultant generates the ideal of $R$ cut out by $(f,f')$. For $R = \mathbb{Z}$ and $f = x^2+1$ the resultant is $\operatorname{Res}(x^2+1,2x) = 4$, so $\mathbb{Z}[x]/(x^2+1) = \mathbb{Z}[i]$ is separable over $\mathbb{Z}[\tfrac12]$ but not over $\mathbb{Z}$; over $\mathbb{F}_2$ the polynomial becomes $(x+1)^2$ and the algebra acquires nilpotents, which is the failure of separability made visible.

**Example (group algebras and Maschke).** For a finite group $G$ and a field $F$, the group algebra $F[G]$ is separable over $F$ if and only if $\operatorname{char} F$ does not divide $\lvert G\rvert$. The separability idempotent is

$$
e = \frac{1}{\lvert G\rvert}\sum_{g\in G} g \otimes g^{-1} ,
$$

which lies in $F[G]\otimes_F F[G]^{\mathrm{op}}$ exactly when $\lvert G\rvert$ is invertible, and it satisfies $\mu(e) = 1$ and the bimodule condition. This is the algebra-level form of Maschke's theorem, and it is developed .

## Central Separable Algebras and Azumaya Algebras

### Definition and characterisations

**Definition.** Let $R$ be a commutative ring. An $R$-algebra $A$ is an **Azumaya algebra** if $A$ is a finitely generated projective faithful $R$-module, the centre of $A$ is $R \cdot 1_A$, and $A$ is separable over $R$.

The central element of the definition is the isomorphism

$$
A \otimes_R A^{\mathrm{op}} \longrightarrow \operatorname{End}_R(A), \qquad a \otimes b \longmapsto (x \mapsto axb),
$$

which is always an $R$-algebra homomorphism and is an isomorphism exactly for the Azumaya algebras among the finitely generated projective faithful ones; this is the **Azumaya property**, and it is the algebraic form of the statement that $A$ is an invertible $A^{\mathrm{e}}$-module. Over a field an Azumaya algebra is precisely a central simple algebra: centrality is the centre condition and separability is simplicity together with the corresponding centre condition, so *Central Simple Algebras and the Brauer Group* treats exactly the field case of the present theory.

**Theorem.** For a field $F$, the finite-dimensional $F$-algebras that are Azumaya over $F$ are the central simple $F$-algebras.

*Proof.* A central simple algebra has centre $F$ and is separable, and it is finite-dimensional, hence finitely generated projective and faithful over $F$. Conversely an Azumaya algebra over $F$ has centre $F$ and is separable, so it is semisimple with all division algebra factors central over $F$; but a semisimple algebra with centre $F$ is simple, since a product of two factors would have a larger centre. Hence it is central simple. $\square$

### The Brauer group of a commutative ring

**Definition.** Let $R$ be a connected commutative ring. Two Azumaya $R$-algebras $A$ and $B$ are **similar**, $A \sim B$, if

$$
A \otimes_R M_m(R) \;\cong\; B \otimes_R M_n(R) \qquad \text{for some } m,n \geq 1 ,
$$

and the set of similarity classes, with the product induced by $\otimes_R$, is the **Brauer group** $\operatorname{Br}(R)$.

That the product is well defined and gives a group rests on the same facts as over a field: the tensor product of two Azumaya algebras is Azumaya, the class of $M_n(R)$ is the identity, and the opposite algebra is inverse, with $A\otimes_R A^{\mathrm{op}} \cong \operatorname{End}_R(A) \cong M_n(R)$ when $A$ has rank $n$ as a projective $R$-module. The verification is word for word that of the field case once the module-theoretic statements are made, and the group is the natural home of the Azumaya algebras. For $R = F$ a field it reduces to the Brauer group of *Central Simple Algebras and the Brauer Group*.

**Theorem (standard).** For a commutative ring $R$ the Azumaya Brauer group sits in a natural exact sequence

$$
1 \longrightarrow \operatorname{Pic}(R) \longrightarrow \operatorname{Br}(R) \longrightarrow \operatorname{Br}'(R),
$$

in which the first map sends an invertible module $L$ to the Azumaya algebra $\operatorname{End}_R(L)$ and the second is the comparison map to the cohomological Brauer group $\operatorname{Br}'(R)$, defined by the étale cohomology of the sheaf of units. The sequence expresses that the Azumaya algebras are the algebraic part of the cohomological Brauer group, and that the kernel of the comparison is the Picard group of invertible modules.

This is the point at which the separability theory meets algebraic geometry, and the cohomological Brauer group, the étale topology and the sheaf-theoretic comparison belong to the later Part.

## Galois Extensions of Rings and the Étale Algebras

**Definition.** A **Galois extension of rings** is a homomorphism $R \to S$ of commutative rings together with a finite group $G$ acting on $S$ by $R$-algebra automorphisms such that $S$ is a finitely generated projective $R$-module and the map

$$
S \otimes_R S \longrightarrow \prod_{\sigma \in G} S, \qquad s \otimes t \longmapsto \bigl(s\,\sigma(t)\bigr)_{\sigma }
$$

is an isomorphism of $S$-algebras. Equivalently, $S$ is a $G$-Galois algebra over $R$ in the sense of the **Galois descent** of *Group Cohomology*.

**Theorem.** A Galois extension of rings is separable over $R$; conversely, the separable commutative $R$-algebras are the algebras that are locally Galois, that is, become Galois after a faithfully flat base change. A commutative separable $R$-algebra is called **étale** over $R$.

*Proof (sketch).* For a Galois extension the separability element is built from the inverse of the Galois isomorphism: applying the inverse of $S\otimes_R S \to \prod_{\sigma\in G}S$ to the family with a single nonzero entry $1$ at the identity produces an element $e \in S\otimes_R S$ whose image under the isomorphism is supported at the identity, and the $G$-invariance of the construction gives $\sum s_i t_i = 1$ and $se = es$ for all $s \in S$. Conversely, a commutative separable algebra is a finitely generated projective $R$-module, and its separability element provides, after a faithfully flat base change that splits the algebra into a product of copies of the base, the finite group action and the isomorphism required by the definition. $\square$

**Example.** The étale algebras over a field $F$ are exactly the products of finite separable field extensions of $F$. For the number ring $R = \mathbb{Z}[\tfrac1n]$, the étale $R$-algebras are the products of rings of integers of number fields unramified outside the primes dividing $n$; since no number field other than $\mathbb{Q}$ has discriminant $\pm1$, the étale $\mathbb{Z}$-algebras are exactly the products $\mathbb{Z}^n$. Thus $\mathbb{Z}[i]$ is not étale over $\mathbb{Z}$ but becomes étale over $\mathbb{Z}[\tfrac12]$, and $\mathbb{Z}[x]/(x^2-x) \cong \mathbb{Z}\times\mathbb{Z}$ is étale over $\mathbb{Z}$.

## Summary

A finite algebraic field extension $L/F$ is **separable** when every element has a minimal polynomial with distinct roots, equivalently when $L$ has $[L:F]$ distinct embeddings into an algebraic closure; fields of characteristic $0$ and finite fields are perfect, and $\mathbb{F}_p(t^{1/p})/\mathbb{F}_p(t)$ is the standard non-separable extension. A finite-dimensional $F$-algebra $A$ is **separable** when $A \otimes_F L$ is semisimple for every field extension $L$; equivalently $A \cong \prod_i M_{n_i}(D_i)$ with each division algebra $D_i$ having separable centre, so over a perfect field separability is exactly semisimplicity, and every central simple algebra is separable. The characterisation that works over a ring is the splitting of the multiplication map: $A$ is separable over $R$ when $\mu : A^{\mathrm{e}} = A \otimes_R A^{\mathrm{op}} \to A$ splits as an $A^{\mathrm{e}}$-module map, equivalently when $A$ is projective over $A^{\mathrm{e}}$, equivalently when the **separability idempotent** $e = \sum_i x_i\otimes y_i$ with $\mu(e)=1$ and $ae=ea$ exists. Separability is preserved by base change; $M_n(R)$ and $R\times R$ are separable; $R[x]/(f)$ is separable for monic $f$ exactly when $(f,f') = R[x]$, that is, when the resultant $\operatorname{Res}(f,f')$ is a unit; and $F[G]$ is separable exactly when $\lvert G\rvert$ is invertible in $F$, the algebra form of Maschke's theorem.

An **Azumaya algebra** is a central separable algebra over a commutative ring; over a field these are exactly the central simple algebras, and the Azumaya algebras up to similarity form the Brauer group $\operatorname{Br}(R)$ of the ring, which reduces to the Brauer group of the field when $R$ is a field. The commutative separable algebras are the **étale algebras**, the algebras that are locally Galois; they include $\mathbb{Z}\times\mathbb{Z}$ and $\mathbb{Z}[\tfrac12][x]/(x^2+1)$, while $\mathbb{Z}[i]$ is not étale over $\mathbb{Z}$. The sheaf-theoretic comparison of the Azumaya and the cohomological Brauer groups, and the étale topology that names them, belong to a later Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity $1 \neq 0$ |
| $F$, $L$ | fields; $L/F$ a field extension |
| $A$ | unital associative $R$-algebra, finitely generated projective where stated |
| $A^{\mathrm{e}} = A \otimes_R A^{\mathrm{op}}$ | enveloping algebra; $A$-bimodules are $A^{\mathrm{e}}$-modules |
| $\mu : A^{\mathrm{e}} \to A$ | multiplication map, $\mu(a\otimes b) = ab$ |
| $e = \sum_i x_i \otimes y_i$ | separability idempotent, $\mu(e)=1$, $ae=ea$ |
| $f_\alpha$, $f'$ | minimal polynomial and formal derivative |
| $\operatorname{Res}(f,f')$ | resultant, $\det$ of the Sylvester matrix |
| $M_n(R)$, $E_{ij}$ | matrix algebra and matrix units |
| $A \sim B$ | similarity of Azumaya algebras |
| $\operatorname{Br}(R)$ | Brauer group of a commutative ring (Azumaya classes) |
| $\operatorname{Pic}(R)$ | Picard group of invertible rank-one modules |
| Azumaya algebra | central separable $R$-algebra, $A\otimes_R A^{\mathrm{op}} \cong \operatorname{End}_R(A)$ |
| étale algebra | commutative separable $R$-algebra |
| $F[G]$ | group algebra; separable iff $\lvert G\rvert \in F^\times$ |
| perfect field | every algebraic extension is separable |
| $\mathbb{Z}[i] = \mathbb{Z}[x]/(x^2+1)$ | étale over $\mathbb{Z}[\tfrac12]$, not over $\mathbb{Z}$ |



## Further Reading

- Frank DeMeyer and Edward Ingraham, *Separable Algebras over Commutative Rings* (Springer, 1971), for the Hattori–Villamayor theorem and separable algebras over a ring.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, 1991), for Azumaya algebras and the Brauer group of a ring, with the form-theoretic material that belongs to the later Part.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the separability idempotent and the structure of separable algebras.
- Morris Orzech and Charles Small, *The Brauer Group of Commutative Rings* (Marcel Dekker, 1975), for the Azumaya Brauer group and the comparison with the cohomological group.
- I. Martin Isaacs, *Character Theory of Finite Groups* (Academic Press, 1976), for the Maschke condition and the separability of group algebras.
- Benson Farb and R. Keith Dennis, *Noncommutative Algebra* (Springer, 1993), for separable algebras, Azumaya algebras and Galois extensions of rings as an introduction to noncommutative algebra.
