
# __Higher Algebraic K-Theory__

## Introduction

The **$K$-theory** of a ring is the study of its projective modules: $K_0(R)$ is the Grothendieck group of finitely generated projective $R$-modules, and $K_1(R)$ is the abelianisation of the stable general linear group, with its determinant and its relation to the Whitehead group. These two groups are the subject of the companion article *$K$-Theory of Rings* of Part I, written in parallel, and they are functors of the ring alone. **Higher algebraic $K$-theory** is the extension of the theory to the groups $K_n(R)$ for all $n \geq 0$, and it is a functor not of the ring but of a *homotopical* object: the category of projective $R$-modules, or the classifying space of the general linear group, or the stable $\infty$-category of perfect $R$-modules. Two definitions dominate: the **plus construction** of Quillen, which attaches cells to $BGL(R)$ to make the commutator subgroup of $\pi_1$ trivial without changing homology, and the **$S_\bullet$-construction**, which produces a simplicial object whose homotopy groups are the $K$-groups. Their equivalence is the main theorem, and the **$Q = +$ theorem** and the **group-completion theorem** relate $K$-theory to the classifying spaces of categories and to loop spaces.

This is one of four $K$-theories in the corpus, and the four must be distinguished at once.

- **$K$-theory of rings** (Part I, planned): the algebraic theory of $K_0$ and $K_1$ of a ring, with projective modules, the determinant, the Whitehead group and the Bass–Heller–Swan theorem. It is the *input* to the present article, not a competitor.
- **Higher algebraic $K$-theory** (this article): the functors $K_n(R)$ defined homotopically from the category of projective modules, together with their relation to the general linear group, to group completion and to the $S_\bullet$-construction.
- **Topological $K$-theory** (another agent of this Part, planned): the generalised cohomology theory $KU^*(X)$ of a space, represented by a spectrum, with Bott periodicity, which appears in the previous article *Stable Homotopy Theory* as the spectrum $KU$.
- **$K$-theory of operator algebras** (another agent of this Part, planned): the $K$-theory of $C^*$-algebras and von Neumann algebras, in which $K_0(A)$ is the Grothendieck group of projections in matrix algebras over $A$ and $K_1(A)$ is the group of unitaries modulo homotopy. On the commutative $C^*$-algebra $C(X)$ of continuous functions on a compact space it agrees with the topological $K$-theory of $X$ by Gelfand duality, and Bott periodicity holds for all $C^*$-algebras; it is not the algebraic theory of this article.

The four share a vocabulary and a group-completion mechanism; they are not the same theory, and the relation between them — the **comparison map** from algebraic to topological $K$-theory — is a theorem (the **Barratt–Priddy–Quillen** and the **Sullivan** theorems for finite groups and their group rings; the **Swan** theorem for affine varieties; the **Quillen–Lichtenbaum** conjectures in general).

The article presents the plus construction and its universal property, the $S_\bullet$-construction and the equivalence of the two definitions, the low-degree computations and $\pi_1$ via the Whitehead group, the **localisation and devissage theorems**, the relation with the Atiyah–Hirzebruch spectral sequence and with topological $K$-theory, and the definitions through stable $\infty$-categories, which is the modern form and the one that makes the multiplicative structure available. The $\infty$-categorical language is that of *Higher Algebra and Higher Categories*, the spectral sequences are those of *The Leray–Serre Spectral Sequence* and *Stable Homotopy Theory*, and the ring-theoretic input is Part I's *$K$-Theory of Rings*, written in parallel.

Throughout, $R$ is a ring; when the theory needs commutativity, unit, regularity or Noetherian hypotheses, they are stated. The symbol $\mathrm{Proj}(R)$ denotes the category of finitely generated projective left $R$-modules, and $GL(R) = \operatorname{colim}_n GL_n(R)$ the stable general linear group.

## The Plus Construction

### Statement and Universal Property

**Definition.** Let $X$ be a based CW complex and $N \leq \pi_1(X, x_0)$ a normal subgroup. A **plus construction** with respect to $N$ is a based CW complex $X^+$ and a map $q : X \to X^+$ such that:

1. $q_* : \pi_1(X,x_0) \to \pi_1(X^+,x_0)$ is surjective with kernel $N$;
2. for every local system of coefficients on $X^+$, the map $q_* : H_*(X; q^*L) \to H_*(X^+;L)$ is an isomorphism.

**Theorem (existence and uniqueness).** For every based CW complex $X$ and normal subgroup $N \leq \pi_1(X)$, a plus construction exists, and it is unique up to homotopy equivalence under $X$; the map $q$ is the universal map to a space that kills $N$ and is a homology isomorphism over the coefficients above.

*Proof sketch.* Attach $2$-cells along loops representing a generating set of $N$ and $3$-cells along the resulting relations, so that $N$ is killed without changing homology; then attach cells of dimension $\geq 3$ to make the new fundamental group exactly $\pi_1(X)/N$ and to kill the excess homology created in dimensions $\geq 3$, by an induction in which each stage corrects $\pi_1$ and $H_i$ for $i \geq 2$. The weak topology of *CW Complexes and Cellular Approximation* allows the transfinite construction. Uniqueness follows from the universal property. $\square$

**Definition.** For a ring $R$ and $n \geq 0$ the **higher algebraic $K$-groups** in Quillen's plus construction definition are

$$
K_n(R) = \pi_n\bigl(BGL(R)^+\bigr) \quad (n \geq 1),
$$

with $K_0(R)$ the Grothendieck group of finitely generated projective $R$-modules, as in Part I's *$K$-Theory of Rings*. Here $BGL(R)$ is the classifying space of the discrete group $GL(R) = \operatorname{colim}_n GL_n(R)$, the colimit being formed along the inclusions $A \mapsto \operatorname{diag}(A,1)$, and $BGL(R)^+$ the plus construction with respect to the commutator subgroup $E(R) = [GL(R),GL(R)]$, the subgroup generated by elementary matrices.

**Remark.** The subgroup killed by the plus construction is the **elementary subgroup** $E(R) = [GL(R),GL(R)]$ generated by the elementary matrices $I + r e_{ij}$ for $i \neq j$; for a commutative ring with $1 \neq 0$ the **Whitehead lemma** states that $E(R) = [GL(R),GL(R)]$, so $\pi_1(BGL(R)^+) \cong K_1(R) = GL(R)/E(R) \cong GL(R)^{\mathrm{ab}}$, the group of Part I's *$K$-Theory of Rings*. The plus construction is thus exactly the device that turns $BGL(R)$ into a space whose $\pi_1$ is $K_1$.

**Example.** For $R$ a field $F$, $GL_n(F)$ acts transitively on the nonzero vectors of $F^n$, and the plus construction gives $K_0(F) \cong \mathbb{Z}$, $K_1(F) \cong F^\times$, $K_2(F)$ the **Milnor $K_2$**, and $K_n(F)$ the higher groups computed by the **Matsumoto** and **Milnor** theory in low degrees; for a finite field $\mathbb{F}_q$, Quillen's computation gives $K_{2i}(\mathbb{F}_q) = 0$ and $K_{2i-1}(\mathbb{F}_q) \cong \mathbb{Z}/(q^i-1)$ for $i \geq 1$.

### The Universal Property and its Consequences

**Theorem (functoriality and the Whitehead group).** The assignment $R \mapsto K_n(R)$ is functorial for ring homomorphisms, and for a ring $R$ the group $K_1(R)$ fits into the exact sequence

$$
1 \to E(R) \to GL(R) \to K_1(R) \to 1,
$$

so that $K_1(R) \cong GL(R)^{\mathrm{ab}}$; the **Whitehead group** $Wh(\pi)$ of a group $\pi$ is $K_1(\mathbb{Z}[\pi])/(\pm\pi)$, and it is the obstruction group in the $s$-cobordism theorem of surgery theory.

*Proof.* Functoriality is the functoriality of $BGL(-)$ and the universal property of the plus construction; the exact sequence is the definition of the plus construction's effect on $\pi_1$. $\square$

**Remark.** The plus construction is the precise sense in which algebraic $K$-theory is a homology theory of the general linear group: by the theorem, $H_*(BGL(R)^+) \cong H_*(BGL(R))$ with trivial coefficients, so the $K$-groups are computed by the homology of $BGL(R)$ in the range where the plus construction does not alter it, which is the route to the **Lichtenbaum–Quillen conjectures**.

## The $S_\bullet$-Construction

### Exact Categories and the $Q$-Construction

**Definition.** An **exact category** is an additive category $\mathcal{M}$ equipped with a class of diagrams $M' \rightarrowtail M \twoheadrightarrow M''$ called **exact sequences**, closed under isomorphism, containing the split exact sequences, and satisfying the closure properties that make the notions of "kernel" and "cokernel" in the class well behaved. The standard example is the category of finitely generated projective $R$-modules with the split exact sequences, or the category of coherent sheaves on a noetherian scheme with the short exact sequences.

**Definition ($Q$-construction).** For an exact category $\mathcal{M}$ let $Q\mathcal{M}$ be the category with the same objects, in which a morphism $M \to N$ is the isomorphism class of a diagram $M \leftarrowtail M' \twoheadrightarrow N$ in $\mathcal{M}$, composition being defined by pullback along the admissible epimorphisms. The identity of $M$ is represented by the split sequence $M \xleftarrow{\ \cong\ } M \twoheadrightarrow 0$, and the **Quillen $Q$-construction** is the classifying space $BQ\mathcal{M}$, with

$$
K_n(\mathcal{M}) = \pi_{n+1}\bigl(BQ\mathcal{M}\bigr) \quad (n \geq 0),
$$

with the loop space $\Omega BQ\mathcal{M}$ homotopy equivalent to $BGL(R)^+$ in the case $\mathcal{M} = \mathrm{Proj}(R)$.

*Proof sketch.* The category $Q\mathcal{M}$ carries a composition law making $BQ\mathcal{M}$ a monoid up to homotopy, and the **group-completion theorem** of Quillen identifies its group completion with $\Omega BQ\mathcal{M}$; the comparison with the plus construction is obtained by exhibiting a homotopy equivalence $\Omega BQ\mathcal{M} \simeq BGL(R)^+$ through the action of $GL(R)$ on a suitable resolution of the objects of $\mathcal{M}$. $\square$

**Remark.** The $Q$-construction is the reason algebraic $K$-theory is computable in principle: it turns the $K$-groups into the homotopy groups of a space constructed from the category, and it makes the theory functorial for exact functors, not only for ring maps. In this form it applies to categories of modules, of coherent sheaves, of vector bundles, and to the stable $\infty$-category of perfect complexes below.

### The $S_\bullet$-Construction

**Definition ($S_\bullet$).** For an exact category $\mathcal{M}$, let $S_n\mathcal{M}$ be the category of **filtered objects** $0 = M_0 \rightarrowtail M_1 \rightarrowtail \cdots \rightarrowtail M_n = M$, with the morphisms that are isomorphisms on the graded pieces; the face maps forget a term and the degeneracies repeat one, and the simplicial category $S_\bullet\mathcal{M}$ has geometric realisation $|S_\bullet\mathcal{M}|$.

**Theorem (Waldhausen).** For a ring $R$ and $\mathcal{M} = \mathrm{Proj}(R)$ there is a natural weak homotopy equivalence

$$
\Omega|S_\bullet\mathcal{M}| \simeq K(\mathcal{M}) = \Omega BQ\mathcal{M},
$$

so that $K_n(\mathcal{M}) \cong \pi_n(\Omega|S_\bullet\mathcal{M}|) \cong \pi_{n+1}(|S_\bullet\mathcal{M}|)$; equivalently $K_n \cong \pi_n$ of the loop space of the realisation.

*Proof sketch.* The simplicial object $S_\bullet\mathcal{M}$ and the $Q$-construction are related by a comparison of the two filtrations: $S_n\mathcal{M}$ has a filtration by the length of the flags, and the associated graded can be identified with $BQ\mathcal{M}$ iterated; the resulting weak equivalence $\Omega|S_\bullet| \xrightarrow{\sim}\Omega BQ\mathcal{M}$ is the **additivity theorem**'s consequence, and it is the form in which the theory generalises to Waldhausen categories. $\square$

**Remark.** The $S_\bullet$-construction is the one that generalises: for a **Waldhausen category** (a category with cofibrations and weak equivalences satisfying the gluing axioms) the same construction defines $K$-theory, and this is the form in which algebraic $K$-theory is applied to topological spaces (the $A$-theory of Waldhausen), to spectra, and to the stable homotopy theory of *Stable Homotopy Theory*.

**Definition ($K$-theory of a stable $\infty$-category).** For a stable $\infty$-category $\mathcal{C}$ with a symmetric monoidal structure, the **algebraic $K$-theory spectrum** $K(\mathcal{C})$ is defined by the $\infty$-categorical version of the $S_\bullet$-construction, or equivalently as $\Omega^\infty$ of the group completion of the underlying $E_\infty$-space of $\mathcal{C}$ with respect to the direct sum:

$$
K(\mathcal{C}) = \bigl(\text{group completion of } \coprod_n \operatorname{Map}_{\mathcal{C}}(0, \bigoplus^n X)\bigr),
$$

a spectrum with $\pi_0K(\mathcal{C}) \cong K_0(\mathcal{C})$. The distinction between this and the classical construction is that the symmetric monoidal structure provides the multiplicative (ring spectrum) structure on $K(\mathcal{C})$ when $\mathcal{C}$ is symmetric monoidal.

## Theorems and Computations

### The Fundamental Theorems

**Theorem (additivity).** Let $\mathcal{A} \to \mathcal{B} \to \mathcal{C}$ be a sequence of exact categories in which $\mathcal{A}$ is a full subcategory of $\mathcal{B}$ closed under extensions and $\mathcal{C}$ is the quotient, so that every object of $\mathcal{B}$ sits in an exact sequence with outer terms in $\mathcal{A}$ and $\mathcal{C}$. Then there is a weak homotopy equivalence

$$
K(\mathcal{B}) \xrightarrow{\ \simeq\ } K(\mathcal{A}) \times K(\mathcal{C}),
$$

and the corresponding long exact sequence of $K$-groups degenerates into split short exact sequences.

**Theorem (devissage).** Let $\mathcal{A}$ be an abelian category and $\mathcal{B}$ a full abelian subcategory closed under subobjects and quotients, such that every object of $\mathcal{A}$ has a finite filtration with quotients in $\mathcal{B}$. Then the inclusion induces a weak homotopy equivalence $K(\mathcal{B}) \to K(\mathcal{A})$.

**Theorem (localisation).** Let $\mathcal{A}$ be an abelian category and $\mathcal{B} \subseteq \mathcal{A}$ a **Serre subcategory** (closed under subobjects, quotients and extensions), with quotient $\mathcal{A}/\mathcal{B}$. Then there is a fibration of spectra

$$
K(\mathcal{B}) \to K(\mathcal{A}) \to K(\mathcal{A}/\mathcal{B}),
$$

and hence a long exact sequence

$$
\cdots \to K_n(\mathcal{B}) \to K_n(\mathcal{A}) \to K_n(\mathcal{A}/\mathcal{B}) \to K_{n-1}(\mathcal{B}) \to \cdots .
$$

*Proof sketch.* All three theorems are proved from the $S_\bullet$-construction and the additivity theorem: the localisation theorem uses the fibration sequence of Waldhausen categories associated to the quotient, and the long exact sequence is the homotopy long exact sequence of the fibration of spectra. $\square$

**Remark.** These three theorems are the working tools of the subject. Localisation gives the $K$-theory of a scheme from that of its closed subschemes and open complements; devissage gives the $K$-theory of a noetherian abelian category from that of the semisimple pieces in a filtration; additivity is the mechanism that makes $K$-theory a homology theory of categories rather than a functor with no exactness.

### Low Degrees and the Relation to Topological $K$-Theory

**Example ($K_0$, $K_1$, $K_2$).** $K_0(R)$ is the Grothendieck group of finitely generated projective modules, as in *$K$-Theory of Rings*; $K_1(R) \cong GL(R)^{\mathrm{ab}}$; and $K_2(R)$ is the centre of the universal central extension of $E(R)$, the **Steinberg group** quotient, with $K_2(R) \cong H_2(E(R);\mathbb{Z})$ by the Hopf formula. For a field these recover the Milnor groups, and for a local ring $K_2$ is generated by the symbols $\{a,b\}$ with the Steinberg relations.

**Example (finite fields).** For $R = \mathbb{F}_q$, Quillen's computation by the **Quillen spectral sequence** (the Atiyah–Hirzebruch sequence applied to the classifying space of the general linear group of a finite field, using the action on the building) gives

$$
K_0(\mathbb{F}_q) \cong \mathbb{Z}, \qquad K_{2i-1}(\mathbb{F}_q) \cong \mathbb{Z}/(q^i - 1), \qquad K_{2i}(\mathbb{F}_q) = 0 \quad (i \geq 1).
$$

The first few values, $K_0 = \mathbb{Z}$, $K_1 \cong \mathbb{Z}/(q-1)$, $K_2 = 0$, $K_3 \cong \mathbb{Z}/(q^2-1)$, show that the groups are finite of computable orders.

**Example ($R = \mathbb{Z}$).** $K_0(\mathbb{Z}) \cong \mathbb{Z}$, $K_1(\mathbb{Z}) \cong \mathbb{Z}/2$, $K_2(\mathbb{Z}) \cong \mathbb{Z}/2$, and $K_3(\mathbb{Z}) \cong \mathbb{Z}/48$. The higher groups are the subject of the **Quillen–Lichtenbaum conjectures**, which relate $K_n(\mathbb{Z})$ to the étale cohomology of $\mathbb{Z}$ up to finite groups of small order in the range $n \geq 2$. The ranks are known by Borel's computation of the cohomology of arithmetic groups:

$$
\operatorname{rk} K_n(\mathbb{Z}) = \begin{cases} 1, & n > 1,\ n \equiv 1 \bmod 4, \\ 0, & \text{otherwise}, \end{cases}
$$

so that $K_1$, $K_2$, $K_3$, $K_4$ are finite — $K_1 \cong \mathbb{Z}/2$, $K_2 \cong \mathbb{Z}/2$, $K_3 \cong \mathbb{Z}/48$, $K_4 = 0$ — and the first groups of positive rank are $K_5, K_9, K_{13}, \ldots$, each free of rank one. The torsion is where the Borel regulator and the image of the $J$-homomorphism of *Stable Homotopy Theory* interfere.

**Theorem (the comparison map and the Atiyah–Hirzebruch sequence).** For a ring $R$ that is regular and noetherian there is a natural map, the **Chern character**,

$$
\operatorname{ch} : K_n(R)\otimes\mathbb{Q} \longrightarrow \bigoplus_{i\geq 0} H^{n-2i}\bigl(\mathrm{Spec}\,R;\mathbb{Q}\bigr),
$$

obtained from the $\lambda$-operations on the $K$-theory and the Chern classes of a projective module, and it is an isomorphism after tensoring with $\mathbb{Q}$ for $R$ regular. The **Atiyah–Hirzebruch spectral sequence** of *Stable Homotopy Theory*,

$$
E^2_{p,q} = H_p(X;K_q(R)) \Longrightarrow K_{p+q}(R),
$$

organises the computation. In particular for $R = \mathbb{C}$ the comparison with topological $K$-theory is detected by the Chern character: $K_0(\mathbb{C}) \cong \mathbb{Z}$ and $K_1(\mathbb{C}) \cong \mathbb{C}^\times$, and rationally $K_n(\mathbb{C})\otimes\mathbb{Q}$ is $\mathbb{Q}$ for even $n$ and $0$ for odd $n$, matching the topological $K$-theory of a point of *Stable Homotopy Theory*; the higher algebraic $K$-groups of $\mathbb{C}$ are divisible by the theorem of Suslin, so the comparison is rational and not integral, and this is the precise sense in which algebraic $K$-theory of $\mathbb{C}$ agrees with topological $K$-theory after inverting the primes.

**Remark (the four $K$-theories, again).** The comparison with topological $K$-theory is a theorem, not an identification: algebraic $K$-theory of a ring is built from algebraic modules and is not a generalised cohomology theory of a space with a suspension axiom; topological $K$-theory is a spectrum-valued theory of spaces; the $K$-theory of operator algebras extends the topological one from spaces to $C^*$-algebras, agreeing with it on the commutative $C^*$-algebra $C(X)$ by Gelfand duality, where $K_0$ counts projections and $K_1$ counts unitaries, with the same Bott periodicity but with the algebra structure carried along; and the $K$-theory of rings of Part I is the degree-zero and degree-one part of the present theory with the module-theoretic proofs.

## The $K$-Theory Spectrum and Waldhausen's Generalisation

### The $K$-Theory Spectrum

**Definition.** The $S_\bullet$-construction is a simplicial object in exact categories, and its realisation is the based space $|S_\bullet\mathcal{C}|$, whose loop space is the zeroth space of the $K$-theory **spectrum** $K(\mathcal{C})$: the spectrum has $n$-th space $\Omega^{n-1}|S_\bullet\mathcal{C}|$ for $n\geq1$, its homotopy groups are the groups $K_n(\mathcal{C})$, and it is connected, so $K_0$ appears as $\pi_0$ of the first space and the $S_\bullet$-construction recovers the plus construction for the exact category of finitely generated projective modules over a ring.

**Theorem.** Let $R$ be a ring.

1. $K(R)$ is a commutative ring spectrum: the tensor product of projective modules, together with the $\lambda$-operations, defines a multiplication $K(R)\wedge K(R)\to K(R)$ which is associative, commutative and unital up to coherent homotopy, so that $K_*(R) = \pi_*K(R)$ is a graded commutative ring and $K_0(R)$ carries the ring structure of the Grothendieck ring of Part I's *$K$-Theory of Rings*.
2. For rings $R$ and $S$ there is a product $K(R)\wedge K(S)\to K(R\otimes_{\mathbb{Z}}S)$, the **external product**, and the resulting multiplicative structure on the $K$-groups is the one used in the comparison theorems.
3. The $K$-theory of a regular noetherian ring is **homotopy invariant**: $K_n(R[t]) \cong K_n(R)$ for all $n$, and more generally $K_n(R[t_1,\ldots,t_m]) \cong K_n(R)$; for a general ring the fundamental theorem gives $K_n(R[t,t^{-1}])\cong K_n(R)\oplus K_{n-1}(R)$ for $n\geq1$, with the two summands coming from the localisation sequence of the affine line at the origin and infinity.

*Proof.* (1) the tensor product and the $\lambda$-operations are defined on the exact category of projective modules, they are compatible with the $S_\bullet$-construction, and the coherence is the standard one for the multiplicative structure of $K$-theory; the identification of $\pi_0$ is the Grothendieck construction of Part I's *$K$-Theory of Rings*. (2) is the tensor product of modules over the two rings. (3) is Quillen's resolution theorem applied to the comparison of the categories of projective modules over $R$ and over $R[t]$, the polynomial ring being flat and the theorem giving the equivalence of the $K$-theory spectra; the fundamental theorem is the localisation sequence for the pair $(\mathbb{A}^1,\mathbb{G}_m)$ over $R$. $\square$

### Waldhausen's Generalisation

**Definition.** A **Waldhausen category** is a category with a class of **cofibrations**, a class of **weak equivalences** containing the isomorphisms and compatible with the cofibrations, and a zero object, satisfying the axioms that make the quotient of a cofibration by a cofibration a cofibration and the pushout of a weak equivalence along a cofibration a weak equivalence. The $S_\bullet$-construction applies verbatim to a Waldhausen category with the cofibrations in place of the admissible monomorphisms, and its homotopy groups are the **Waldhausen $K$-groups**.

**Theorem (the algebraic $K$-theory of spaces).** Let $X$ be a based finite CW complex and let $\mathcal{R}(X)$ be the Waldhausen category of retractive spaces over $X$, with the cofibrations the maps with the homotopy extension property and the weak equivalences the homotopy equivalences. Then the Waldhausen $K$-theory of $\mathcal{R}(X)$ is the **$A$-theory** $A(X)$, and:

1. $A(\ast)$ is equivalent to the sphere spectrum, so $\pi_nA(\ast)\cong\pi_n^s(\mathbb{S})$, the stable homotopy groups of spheres of *Stable Homotopy Theory*;
2. for a ring $R$ there is a natural map $K(R)\to A(BGL(R)^+)$, Waldhausen's **linear approximation**, which is an equivalence in a range of degrees, so that the algebraic $K$-theory of a ring is the linear part of the $K$-theory of its classifying space;
3. the **Whitehead theorem** of Waldhausen identifies the diffeomorphism groups of high-dimensional manifolds with the $K$-theory of spaces up to a codimension-three range, which is the bridge from the present article to the surgery theory of *Cobordism and Surgery Theory*.

*Proof.* (1) is the theorem of Barratt, Priddy and Quillen in its algebraic form, the group completion of the monoid of spheres; (2) is the comparison of the linear category of free modules with the category of retractive spaces over $BGL(R)^+$, which is a theorem of Waldhausen quoted as standard; (3) is Waldhausen's theorem on the relation of $A(X)$ to the pseudoisotopy space and hence to the diffeomorphism groups by the $h$- and $s$-cobordism theorems, stated in *Cobordism and Surgery Theory*. $\square$

**Remark (the additive structure of the arithmetic computations).** The computations quoted above acquire their shape from the general theory. For a finite field the Quillen spectral sequence degenerates in the fashion described, and $K_{2i-1}(\mathbb{F}_q)$ is cyclic of order $q^i-1$; for a number field the Borel computation determines the ranks through the values of the Riemann zeta function at negative integers, the regulator being the volume of the lattice of $K$-classes in the cohomology of the arithmetic group; and the torsion of $K_*(\mathbb{Z})$, such as $K_3(\mathbb{Z})\cong\mathbb{Z}/48$, is the arithmetic content of the torsion conjectures and of the $J$-homomorphism of *Stable Homotopy Theory*. The general theorems above — multiplicativity, homotopy invariance, the fundamental theorem — supply the structural frame, and the arithmetic supplies the deviations from it.

## Summary

The plus construction attaches cells to a based CW complex to kill a normal subgroup of its fundamental group while preserving homology, and it is universal and essentially unique. Applying it to $BGL(R)$ with respect to the elementary subgroup $E(R)$ defines the higher algebraic $K$-groups $K_n(R) = \pi_n(BGL(R)^+)$ for $n \geq 1$, with $\pi_1(BGL(R)^+) \cong K_1(R)$ by the Whitehead lemma. The $Q$-construction and the equivalent $S_\bullet$-construction realise the same groups as the homotopy of a space built from an exact category; the $S_\bullet$ form generalises to Waldhausen categories and to the algebraic $K$-theory spectrum of a symmetric monoidal stable $\infty$-category, where the multiplicative structure is available.

The theory is governed by additivity, devissage and localisation, the last giving a fibration of $K$-theory spectra and hence a long exact sequence for a Serre subcategory and its quotient. The low groups recover $K_0$ and $K_1$ of the ring-theoretic theory, $K_2$ is the second homology of the elementary group, and the computations for finite fields and for $\mathbb{Z}$ give finite values in low degrees with arithmetic meaning. The comparison with topological $K$-theory is by the Chern character and by the Atiyah–Hirzebruch spectral sequence, and it is an isomorphism only after inverting the primes and only in a range; the four $K$-theories of the corpus — of rings, higher algebraic, topological, and of operator algebras — are related by comparison maps and are not the same theory. The $K$-groups are the homotopy groups of a commutative ring spectrum, whose multiplication comes from the tensor product and whose external form is used in the comparison theorems, and Waldhausen's generalisation applies the construction to categories with cofibrations and weak equivalences, producing the $K$-theory of spaces, whose value at a point is the sphere spectrum and which is the input to the surgery theory of high-dimensional manifolds.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X^+$, $q : X \to X^+$ | Plus construction killing $N \leq \pi_1(X)$ |
| $GL(R) = \operatorname{colim}_n GL_n(R)$ | Stable general linear group |
| $E(R) = [GL(R),GL(R)]$ | Elementary subgroup; killed by the plus construction |
| $K_n(R) = \pi_n(BGL(R)^+)$ | Higher algebraic $K$-groups, $n \geq 1$ |
| $K_0(R)$ | Grothendieck group of finitely generated projective $R$-modules |
| $Wh(\pi)$ | Whitehead group $K_1(\mathbb{Z}[\pi])/(\pm\pi)$ |
| $\mathcal{M}$, $\mathrm{Proj}(R)$ | Exact category; finitely generated projective $R$-modules |
| $Q\mathcal{M}$, $BQ\mathcal{M}$ | $Q$-construction and its classifying space |
| $S_\bullet\mathcal{M}$, $|S_\bullet\mathcal{M}|$ | $S_\bullet$-construction and its realisation |
| $K(\mathcal{C})$ | Algebraic $K$-theory spectrum; $\pi_nK(\mathcal{C}) = K_n(\mathcal{C})$ |
| Waldhausen category | Category with cofibrations and weak equivalences, for which $S_\bullet$ applies |
| $A(X)$ | Waldhausen's algebraic $K$-theory of a space $X$; $A(\ast)$ is the sphere spectrum |
| $R[t]$, $R[t,t^{-1}]$ | Polynomial and Laurent extensions; homotopy invariance and the fundamental theorem |
| Additivity, devissage, localisation | The three structural theorems of the theory |
| $K(\mathcal{A}/\mathcal{B})$ | Quotient of an abelian category by a Serre subcategory |
| Chern character | Comparison $K_n(R)\otimes\mathbb{Q} \to$ (co)homology of $\mathrm{Spec}\,R$ |
| $KU$, $KO$ | Topological $K$-theory spectra (other agent's article) |
| $K_*(A)$, $A$ a $C^*$-algebra | Operator-algebraic $K$-theory (other agent's article) |
| Atiyah–Hirzebruch SS | $E^2_{p,q} = H_p(X;K_q(R)) \Rightarrow K_{p+q}(R)$ |

## Further Reading

- Daniel G. Quillen, *Higher Algebraic K-Theory I* (Springer Lecture Notes in Mathematics 341, 1973), for the plus construction, the $Q$-construction and the fundamental theorems.
- Friedhelm Waldhausen, *Algebraic K-Theory of Generalized Free Products* (Annals of Mathematics 108, 1978), for the $S_\bullet$-construction and Waldhausen categories.
- Jonathan Rosenberg, *Algebraic K-Theory and Its Applications* (Springer, 1994), for a systematic account with the computations for finite fields and for $\mathbb{Z}$.
- Charles A. Weibel, *The K-Book: An Introduction to Algebraic K-Theory* (American Mathematical Society, 2013), for the exact-category approach, localisation and devissage.
- Daniel R. Grayson, *Higher Algebraic K-Theory II* (Springer Lecture Notes in Mathematics 551, 1976), for the computations and the localisation theorem.
- Eric M. Friedlander and Daniel R. Grayson, *Handbook of K-Theory* (Springer, 2005), for the comparison with topological $K$-theory and the Quillen–Lichtenbaum conjectures.
- Clark Barwick, *On the Algebraic K-Theory of Higher Categories* (Journal of Topology 9, 2016), for the $\infty$-categorical construction and its multiplicative structure.
- Armand Borel, *Stable Real Cohomology of Arithmetic Groups* (Annales Scientifiques de l'École Normale Supérieure 7, 1974), for the ranks of the $K$-groups of rings of integers.
