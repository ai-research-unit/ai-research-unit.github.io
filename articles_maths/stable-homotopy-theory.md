
# __Stable Homotopy Theory__

## Introduction

The homotopy groups of spheres $\pi_{n+k}(S^n)$, computed in *Homotopy Groups and Fibrations* for small values, do not depend on $n$ once $n$ is large compared with $k$: the **Freudenthal suspension theorem** makes the suspension homomorphism $\pi_{n+k}(S^n) \to \pi_{n+k+1}(S^{n+1})$ an isomorphism for $n > k+1$, so there is a single group $\pi_k^s = \operatorname{colim}_n \pi_{n+k}(S^n)$, the $k$-th **stable stem**. **Stable homotopy theory** is the study of these groups and of the objects — **spectra** — whose homotopy groups they are. A spectrum is a sequence of pointed spaces with suspension structure maps, the suspension functor on spectra is an equivalence, and the homotopy category of spectra is **triangulated** and **symmetric monoidal** under the smash product, with the sphere spectrum as unit. In that category the invariants of the preceding articles — homology and cohomology with coefficients, the cup product, the cohomology operations — arrange themselves into a single representable theory, and the computations that are impossible for unstable homotopy become tractable through the **Adams spectral sequence**.

The article presents the stable homotopy category, the suspension spectra and the Eilenberg–MacLane spectra, the representability of (co)homology theories by spectra, the multiplicative structure, and the two computational devices: the **Adams spectral sequence**, which computes $\pi_*$ of a spectrum from its mod-$p$ cohomology as a module over the Steenrod algebra, and the **Atiyah–Hirzebruch spectral sequence**, which computes the generalised homology of a space from its ordinary homology with coefficients in the coefficient ring of the theory. The **Thom spectra** and the orientation theory that follow from them are the route from stable homotopy to the characteristic classes of the written *Fibre Bundles, Connections and Curvature*; the **algebraic $K$-theory** that the Atiyah–Hirzebruch sequence computes for the operator-algebraic model is not covered here in this batch.

The stable homotopy category is the homotopy category of a stable $\infty$-category, in the sense of *Higher Algebra and Higher Categories*; the triangulated structure is a shadow of that structure, and the constructions that need coherence — the smash product, the multiplicative structure on ring spectra, the module theory used — are performed there. The classical model-theoretic treatment of spectra is the one of *Model Categories and Homotopy Theory*. **Topological $K$-theory** and **$K$-theory of operator algebras** are the subjects of articles of another agent in this Part; the present article uses $K$-theory only as an example of a generalised cohomology theory represented by a spectrum, and the distinction between the four $K$-theories of this corpus is stated explicitly.

Throughout, spectra are written $E$, their homotopy groups $\pi_k E$, and the suspension spectrum of a space $X$ is $\Sigma^\infty X$; coefficients are in a commutative ring $R$ with $1 \neq 0$.

## Spectra and the Stable Category

### Definitions

**Definition.** A **prespectrum** is a sequence of pointed topological spaces $E_n$ for $n \geq 0$ together with pointed maps $\sigma_n : \Sigma E_n \to E_{n+1}$, the **structure maps**. A **spectrum** is a prespectrum whose adjoints $\tilde\sigma_n : E_n \to \Omega E_{n+1}$ are homeomorphisms. A **CW spectrum** is a spectrum whose spaces are CW complexes and whose structure maps are cellular inclusions; the **homotopy groups** are

$$
\pi_k(E) = \operatorname{colim}_n\ \pi_{k+n}(E_n), \qquad \text{the colimit along } \pi_{k+n}(E_n) \xrightarrow{\ \cong\ } \pi_{k+n}(\Omega E_{n+1}) \to \pi_{k+n+1}(E_{n+1}).
$$

Negative degrees are permitted, and a spectrum with $\pi_k = 0$ for $k < 0$ is **connective**.

**Definition.** The **sphere spectrum** $\mathbb{S}$ has $\mathbb{S}_n = S^n$ with the identity structure maps; the **suspension spectrum** of a pointed space $X$ is $\Sigma^\infty X$ with $(\Sigma^\infty X)_n = \Sigma^n X$; the **Eilenberg–MacLane spectrum** $H\pi$ of an abelian group $\pi$ has $\pi_0 = \pi$ and $\pi_k = 0$ for $k \neq 0$.

**Definition.** A map of spectra $f : E \to F$ is a **stable homotopy equivalence** if it induces isomorphisms on all $\pi_k$; the **stable homotopy category** $\mathcal{SH}$ is the category of CW spectra and homotopy classes of maps, equivalently the homotopy category of the stable model structure on spectra. Its morphisms satisfy

$$
[E, F]_{\mathcal{SH}} \cong \operatorname{colim}_n\ [E_n, F_n],
$$

the colimit along the structure maps, and a spectrum with all homotopy groups zero is isomorphic to the zero spectrum.

**Theorem.** $\mathcal{SH}$ is an additive category with a shift functor $\Sigma$ that is an equivalence, and it is triangulated: cofibre sequences, equivalently fibre sequences, produce the exact triangles, and every map extends to a triangle unique up to noncanonical isomorphism.

*Proof sketch.* The stable homotopy category is the homotopy category of the stable $\infty$-category of spectra, which is stable in the sense of *Higher Algebra and Higher Categories*; the theorem that the homotopy category of a stable $\infty$-category is triangulated then applies. Concretely, the cofibre of $f : E \to F$ is the spectrum $Cf$ with $Cf_n$ the mapping cone of $f_n$, and the resulting cofibre sequence is exact on homotopy groups. $\square$

**Remark.** The passage from spaces to spectra is the passage from $\pi_{n+k}(S^n)$ to $\operatorname{colim}_n\pi_{n+k}(S^n)$; this is an instance of the general principle that a stable theory is one in which the suspension is invertible, and it is what makes the stable theory computable: the suspension of a spectrum is an equivalence, so no information is lost by suspending.

### Suspension and Loops

**Definition.** For a spectrum $E$ the **suspension** $\Sigma E$ has $(\Sigma E)_n = E_{n+1}$ with the structure maps shifted, and the **loop** $\Omega E$ has $(\Omega E)_n = E_{n-1}$ for $n \geq 1$ and $(\Omega E)_0 = \ast$; there are natural isomorphisms $\pi_k(\Sigma E) \cong \pi_{k-1}(E)$ and $\pi_k(\Omega E) \cong \pi_{k+1}(E)$, and $\Sigma$ is an equivalence of categories with inverse $\Omega$.

**Theorem (the stable homotopy groups of spheres).** $\pi_k(\mathbb{S}) \cong \pi_k^s$, the $k$-th stable stem, with

$$
\pi_0^s \cong \mathbb{Z}, \quad \pi_1^s \cong \mathbb{Z}/2, \quad \pi_2^s \cong \mathbb{Z}/2, \quad \pi_3^s \cong \mathbb{Z}/24, \quad \pi_4^s = 0, \quad \pi_5^s = 0,
$$

$$
\pi_6^s \cong \mathbb{Z}/2, \quad \pi_7^s \cong \mathbb{Z}/240, \quad \pi_8^s \cong (\mathbb{Z}/2)^2, \quad \pi_9^s \cong (\mathbb{Z}/2)^3, \quad \pi_{10}^s \cong \mathbb{Z}/6.
$$

This is standard mathematics (Toda, *Composition Methods in Homotopy Groups of Spheres*), quoted here; the computation uses the Adams spectral sequence, below.

**Example.** The first stable stem $\pi_0^s = \mathbb{Z}$ is the degree; $\pi_1^s = \mathbb{Z}/2$ is generated by the class of the Hopf map $\eta : S^3 \to S^2$ of *Homotopy Groups and Fibrations*, stabilised; $\pi_3^s \cong \mathbb{Z}/24$ is cyclic, generated by the stabilised Hopf map $\nu : S^7 \to S^4$; and the fourth Hopf map $\sigma : S^{15} \to S^8$ has its stabilised class in $\pi_7^s \cong \mathbb{Z}/240$. The three Hopf maps $\eta$, $\nu$, $\sigma$ are the only classes of Hopf invariant one, in stems $1$, $3$ and $7$, and their existence exactly there is the Hopf invariant one theorem of Adams.

**Definition (the $J$-homomorphism and the image of $J$).** For $n$ odd the **$J$-homomorphism** $J : \pi_k(SO(n)) \to \pi_{k+n}(S^n)$ maps a map $S^k \to SO(n)$ to the induced map of spheres $S^{k+n}\to S^{k+n}$ given by acting on the unit sphere of $\mathbb{R}^n$; it stabilises and produces a family of elements of $\pi_*^s$ whose orders are the Bernoulli denominators (Adams, Quillen), the **image of $J$**.

## Generalised (Co)homology and Representability

### Spectra Represent Cohomology Theories

**Definition.** A **reduced generalised homology theory** is a functor $E_*$ from pointed CW complexes to graded abelian groups with $E_*(\text{point}) = 0$, satisfying the suspension axiom $E_k(\Sigma X)\cong E_{k-1}(X)$ and carrying cofibre sequences to long exact sequences. A **reduced cohomology theory** $E^*$ is defined dually with the exactness and suspension axioms in cohomology.

**Theorem (Brown representability; the homotopy-theoretic form).** Every reduced cohomology theory on pointed CW complexes is representable: there is a spectrum $E$ with

$$
\tilde E^k(X) \cong [\Sigma^\infty X, \Sigma^k E]_{\mathcal{SH}} = \operatorname{colim}_n\bigl[\Sigma^n X, E_{k+n}\bigr]
$$

naturally in $X$; and every spectrum defines a reduced cohomology theory by this formula. The corresponding homology theory is $E_k(X) = \pi_k(E\wedge \Sigma^\infty X)$.

*Proof sketch.* The representing objects are the values of the theory on spheres, $E_n = $ a space representing $E^n(S^0)$ in the appropriate sense, and the structure maps come from the suspension isomorphisms; the argument is the classical Brown representability theorem applied to the homotopy functor on CW complexes. $\square$

**Example.** The spectrum $\mathbb{S}$ represents stable cohomotopy, $\tilde{\mathbb{S}}^k(X) \cong \operatorname{colim}_n[\Sigma^nX, S^{k+n}]$; the Eilenberg–MacLane spectrum $H\pi$ represents ordinary cohomology $\tilde H^k(X;\pi)$; the spectrum $MU$ represents complex cobordism, with $\pi_*MU$ the Lazard ring of formal group laws, and $KO$, $KU$ represent real and complex topological $K$-theory.

**Remark.** The unity of the subject is the consequence of this theorem: homology and cohomology theories *are* spectra, the natural transformations between them are stable maps, and the cohomology operations are elements of $E^*(E)$. Ordinary cohomology is the case $\pi = \mathbb{Z}$, and every generalised theory is obtained from ordinary cohomology by a sequence of extensions, which is the content of the Atiyah–Hirzebruch spectral sequence below.

### Smash Products and Ring Spectra

**Definition.** The **smash product** $E \wedge F$ of spectra is the left derived functor of the levelwise smash product, defined on a cofibrant replacement of one variable; it is symmetric monoidal with unit $\mathbb{S}$ and commutes with suspension in each variable. A **ring spectrum** is a monoid in the stable homotopy category; an $A_\infty$ or $E_\infty$ **ring spectrum** is an algebra over the corresponding $\infty$-operad of *Higher Algebra and Higher Categories*, which is the structure needed for the multiplicative constructions.

**Theorem.** The stable homotopy category with the smash product is a symmetric monoidal triangulated category with unit $\mathbb{S}$; for ring spectra $E$ and $F$ the Eilenberg–MacLane spectrum $H(R)$ of a commutative ring $R$ has a commutative ring spectrum structure, and the multiplication on $H(R)$ recovers the cup product of *Cup and Cap Products* on ordinary cohomology.

**Remark.** The cup product is the shadow of the multiplication of the Eilenberg–MacLane spectrum: the cohomology ring $H^*(X;R)$ is the $\pi_*$ of the smash product $H(R)\wedge \Sigma^\infty X$, and the graded commutativity in the sense of *Cup and Cap Products* is the graded commutativity of that multiplication. This is the conceptual account of the sign $(-1)^{kl}$.

## The Adams Spectral Sequence

### Construction

**Definition.** Fix a prime $p$ and work with mod-$p$ cohomology. The **Steenrod algebra** $\mathcal{A}_p$ is the graded algebra of stable cohomology operations on mod-$p$ cohomology, $\mathcal{A}_p = H\mathbb{F}_p^*(H\mathbb{F}_p)$, generated by the **Steenrod squares** $Sq^i$ for $p = 2$ (with $Sq^0 = 1$ and $Sq^1$ the Bockstein of *Cohomology and the Universal Coefficient Theorem*) and by the **Steenrod powers** $\mathcal{P}^i$ and the Bockstein $\beta$ for $p$ odd.

**Theorem (the Adams spectral sequence).** Let $p$ be a prime and let $E$ be a spectrum whose mod-$p$ cohomology $H^*(E;\mathbb{F}_p)$ is bounded below and of finite type as a graded $\mathbb{F}_p$-vector space. Then there is a spectral sequence with

$$
E_2^{s,t} = \operatorname{Ext}^{s,t}_{\mathcal{A}_p}\bigl(\mathbb{F}_p, H^*(E;\mathbb{F}_p)\bigr) \Longrightarrow \pi_{t-s}(E)\otimes \mathbb{Z}_p,
$$

where the Ext groups are computed in the abelian category of graded $\mathcal{A}_p$-modules, the differential is $d_r : E_r^{s,t}\to E_r^{s+r,t+r-1}$, and the **Adams filtration** is by the number of stable maps in a factorisation. The spectral sequence converges conditionally in the sense of Boardman.

*Proof sketch.* Filter $\pi_*E$ by the subgroups of elements whose representing map $S^n \to E$ factors through a finite complex killed by an Adams-tower construction of length $s$; the associated graded is computed by a resolution of $H^*(E;\mathbb{F}_p)$ by free $\mathcal{A}_p$-modules, and the homology of the resulting complex is the Ext group. The construction is a special case of the derived functors of Part I's *Derived Functors*, written in parallel, applied to the module category over the Steenrod algebra, and it is the stable analogue of the Leray–Serre spectral sequence of *The Leray–Serre Spectral Sequence*. $\square$

**Remark.** The Adams spectral sequence is the central computing device of stable homotopy theory, and the systematic treatment of the Steenrod algebra and its Ext groups is a substantial theory in its own right (the **Adams–Novikov** spectral sequence replaces ordinary cohomology by complex cobordism and makes the $E_2$ page computable); only the shape of the result is required here.

### Computations

**Example ($\pi_*^s$ in low degrees, mod $2$).** For $p = 2$ and $E = \mathbb{S}$, the $E_2$ page is $\operatorname{Ext}_{\mathcal{A}_2}(\mathbb{F}_2,\mathbb{F}_2)$, which in the range $t - s \leq 10$ is generated by classes $h_i \in E_2^{1,2^i}$ for $i \geq 0$ together with products; the differentials $d_2(h_i) = h_{i-1}^2 h_{i-2}$ (the **Adams differentials**) truncate the page, and one obtains

$$
\pi_0^s \cong \mathbb{Z},\ \pi_1^s \cong \mathbb{Z}/2,\ \pi_2^s \cong \mathbb{Z}/2,\ \pi_3^s \cong \mathbb{Z}/24,\ \pi_6^s \cong \mathbb{Z}/2,\ \pi_7^s \cong \mathbb{Z}/240,
$$

in agreement with the table above; the classes $h_0h_1$, $h_1^2$, $h_1h_2$, $h_2^2$ detect the elements of the Adams filtration two, and the **Adams periodicity** relates the families $\{\pi_{8k}^s\}$ through the Bott element.

**Example (stable stems and the $J$-homomorphism).** The image of the $J$-homomorphism in $\pi_{4k-1}^s$ is cyclic of order equal to the denominator of $B_{2k}/4k$, where $B_{2k}$ is the $2k$-th Bernoulli number; for $k=1,2,3$ it is the whole stem, so that $\pi_3^s \cong \mathbb{Z}/24$, $\pi_7^s \cong \mathbb{Z}/240$ and $\pi_{11}^s \cong \mathbb{Z}/504$. The identities $24 = \operatorname{den}(B_2/4)$, $240 = \operatorname{den}(B_4/8)$ and $504 = \operatorname{den}(B_6/12)$ are verified directly from the Bernoulli numbers $B_2 = 1/6$, $B_4 = -1/30$, $B_6 = 1/42$: $B_2/4 = 1/24$, $B_4/8 = -1/240$ and $B_6/12 = 1/504$.

**Example (the first Hopf invariant one problem).** The Hopf maps $\eta : S^3\to S^2$, $\nu : S^7\to S^4$, $\sigma : S^{15}\to S^8$ exist exactly in dimensions $n = 1,2,4,8$ (Adams' theorem that $H^*(S^n;\mathbb{F}_2)$ admits a square of a degree-$k$ class only for $k = 1,2,4,8$); the stable classes they define in $\pi_1^s$, $\pi_3^s$, $\pi_7^s$ are the lowest elements of the corresponding families, and the non-existence of a fifth is the statement that $Sq^{2^k}$ decomposes for $k \geq 4$.

## The Atiyah–Hirzebruch and Adams–Novikov Spectral Sequences

### Oriented Cohomology Theories and the Atiyah–Hirzebruch Spectral Sequence

**Theorem (Atiyah–Hirzebruch).** Let $E$ be a spectrum representing a reduced cohomology theory, let $X$ be a CW complex, and write $E_* = \pi_*E$ for the coefficient ring. There is a first quadrant spectral sequence

$$
E^2_{p,q} = H_p\bigl(X; E_q\bigr) \Longrightarrow E_{p+q}(X),
$$

the **Atiyah–Hirzebruch spectral sequence**, with differentials $d^r : E^r_{p,q} \to E^r_{p-r,q+r-1}$; dually in cohomology, $E_2^{p,q} = H^p(X;E^{-q}) \Rightarrow E^{p+q}(X)$. It is natural in $X$ and in the spectrum $E$, and it is multiplicative when $E$ is a ring spectrum.

*Proof sketch.* Filter the CW spectrum $E\wedge \Sigma^\infty X$ by the skeleta of $X$; the associated graded pieces are the smash products of $E$ with the quotients $X^{(p)}/X^{(p-1)}$, which are wedges of spheres, so the $E^1$ page is the cellular chains of $X$ with coefficients in $E_*$; hence $E^2_{p,q} = H_p(X;E_q)$ and convergence is to the homotopy of the total spectrum. $\square$

**Example.** For $E = H\mathbb{Z}$ and $R$ coefficients the spectral sequence has $E^2_{p,q} = H_p(X;\mathbb{Z})$ concentrated in $q = 0$ and collapses, recovering ordinary homology. For $E = KU$ the coefficient ring is $\mathbb{Z}[u^{\pm1}]$ with $|u| = 2$, so the $E^2$ page is ordinary homology with a degree-two coefficient; the differentials $d^3$ are the integral Steenrod operations, and the **Bott periodicity** makes the $E^\infty$ page the associated graded of $K^*$-theory.

**Example (the Chern character and $K$-theory of spheres).** For complex topological $K$-theory, the Atiyah–Hirzebruch spectral sequence for $X = S^{2n}$ has two nonzero rows and two nonzero columns and collapses; it gives $KU^0(S^{2n}) \cong \mathbb{Z}$ and $KU^1(S^{2n}) = 0$, with $KU^0(S^{2n})$ generated by the $n$-th power of the Bott class. This is the computation underlying **Bott periodicity**, and it is the model for the $K$-theory computations of the operator-algebraic kind treated by another article of this Part.

### Transgression and the Edge Homomorphism

**Theorem.** In the Atiyah–Hirzebruch spectral sequence the edge homomorphism

$$
H_n(X;E_0) = E^2_{n,0} \longrightarrow E^\infty_{n,0} \subseteq E_n(X)
$$

is the **Hurewicz map** of the theory $E$, the natural transformation sending a homology class to its image under the unit $\mathbb{S}\to E$; and the transgression $d^2 : E^2_{0,1}\to E^2_{2,0}$ is the map that carries $E_1 = \pi_1E$ to $H_2(X;E_0)$ through the cohomology operation classifying the first $k$-invariant of $E$.

*Proof.* Both statements are the identification of the low-degree terms of the spectral sequence; the first is the naturality of the unit, the second is the identification of $d^2$ with the $k$-invariant of the spectrum, in the sense of the Postnikov tower of *The Leray–Serre Spectral Sequence*. $\square$

**Example (the mod-$p$ Moore spectrum and the first differential).** The **Moore spectrum** $S/p$ is the cofibre of the multiplication-by-$p$ map $p : \mathbb{S} \to \mathbb{S}$, so that there is a cofibre sequence $\mathbb{S} \xrightarrow{p}\mathbb{S} \to S/p \to \Sigma\mathbb{S}$; its mod-$p$ homology is that of the mod-$p$ Eilenberg–MacLane spectrum. The Atiyah–Hirzebruch spectral sequence for $S/p$ computes $\pi_*(S/p)$ from $H_*(S/p;\mathbb{Z})$, whose only nonzero groups are $\mathbb{Z}$ in degree $0$ and $\mathbb{Z}/p$ in degree $1$, and the first nontrivial differential is the Bockstein $\beta$ of *Cohomology and the Universal Coefficient Theorem*; the mod-$p$ stable homotopy of spheres is thereby organised into the **$\mathcal{A}_p$-module** structure of $H_*(S/p)$.

## The Chromatic Picture

### Morava $K$-Theory and the Chromatic Filtration

**Definition.** Let $p$ be a prime. For each $n\geq0$ there is a spectrum $K(n)$, **Morava $K$-theory** at height $n$, with $K(0) = H\mathbb{Q}$ and $K(1)$ a summand of mod-$p$ complex $K$-theory, whose coefficient ring is $K(n)_* = \mathbb{F}_p[v_n^{\pm1}]$ with $v_n$ of degree $2(p^n-1)$. A spectrum $X$ is said to have **type $n$** if $K(n)_*(X)\neq0$ and $K(m)_*(X) = 0$ for $m>n$; the **chromatic filtration** of $X$ is the tower of Bousfield localisations with respect to the theories $K(0), K(1), K(2),\dots$ of *Model Categories and Homotopy Theory*.

**Theorem (the nilpotence and periodicity theorems).** Let $X$ be a finite spectrum.

1. **(Nilpotence, Devinatz–Hopkins–Smith.)** Every element of $\pi_*X$ that is annihilated by all Morava $K$-theories is nilpotent in the ring $\pi_*X$.
2. **(Periodicity, Hopkins–Smith.)** If $X$ is of type $n$, then there is a self-map $v : \Sigma^{d}X\to X$ inducing an isomorphism in $K(n)_*$ and nilpotent in $K(m)_*$ for $m>n$; the iteration of $v$ gives the **periodic families** of elements in the stable homotopy groups of spheres.
3. **(Thick subcategory theorem.)** The thick subcategories of the homotopy category of finite spectra are exactly the categories of spectra of type $\geq n$, one for each $n$.

*Proof.* These are the three central theorems of chromatic homotopy theory; the common input is the theory of formal groups and the complex cobordism spectrum $MU$ of *Cobordism and Surgery Theory*, whose coefficient ring carries the universal formal group law and whose Morava $K$-theories are the $p$-typical reductions. The proofs use the **Bousfield localisation** at $K(n)$ and the **telescopic** localisations built from the self-maps of (2), and they are quoted as standard. $\square$

**Remark (what the picture explains).** The Adams–Novikov spectral sequence is the computational shadow of the chromatic picture: its $E_2$ page is built from the complex cobordism of the point, the $v_n$-periodic families appear as the columns of the $E_2$ page, and the nilpotence theorem says that outside the periodic families the elements are nilpotent, so that the stable homotopy groups of spheres are, in a precise sense, generated by the periodic families and their nilpotent multiples. The chromatic filtration is not finite for a general spectrum: the localisations $L_{K(n)}$ assemble into a tower whose inverse limit is the $p$-local sphere, and each layer is governed by the formal group of height $n$ and its Morava stabiliser group. The detailed computation of the layers belongs to the arithmetic of formal groups and stable homotopy theory beyond the scope of this article, and the rational and $v_1$-periodic parts are the ones used in the comparison with algebraic $K$-theory.

## Summary

A spectrum is a sequence of pointed spaces with suspension structure maps; its homotopy groups are the colimit along the structure maps, and the stable stems of the sphere are the homotopy groups of the sphere spectrum. The stable homotopy category is additive, triangulated and symmetric monoidal under the smash product with unit $\mathbb{S}$, the suspension is an equivalence, and it is the homotopy category of a stable $\infty$-category, so that the constructions needing higher coherence — the smash product, ring spectra, module theory — are available in the higher setting.

Brown representability identifies reduced cohomology theories with spectra, so ordinary cohomology, complex cobordism and topological $K$-theory are spectra and the natural transformations and operations between theories are stable maps; the cup product of ordinary cohomology is the multiplication of the Eilenberg–MacLane spectrum. The Adams spectral sequence computes the homotopy of a spectrum from its mod-$p$ cohomology as a module over the Steenrod algebra, with $E_2 = \operatorname{Ext}_{\mathcal{A}_p}(\mathbb{F}_p, H^*(E))$, and with it the low stable stems, the image of the $J$-homomorphism and the Hopf invariant one problem are accessible. The Atiyah–Hirzebruch spectral sequence computes the generalised homology of a space from its ordinary homology with coefficients in the coefficient ring of the theory, with the edge homomorphism the Hurewicz map of the theory; it computes topological $K$-theory and gives Bott periodicity, and it is the device used to compute algebraic $K$-theory in the cases where the two agree. The chromatic picture organises the stable category by the Morava $K$-theories $K(n)$: every finite spectrum has a type, the nilpotence and periodicity theorems of Devinatz–Hopkins–Smith and Hopkins–Smith produce the $v_n$-periodic families of elements, and the thick subcategories of the homotopy category of finite spectra are exactly the classes of spectra of a given type.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Sigma E_n \to E_{n+1}$ | Structure maps of a (pre)spectrum |
| $\pi_k(E) = \operatorname{colim}_n \pi_{k+n}(E_n)$ | Homotopy groups of a spectrum |
| $\mathbb{S}$, $\pi_k^s$ | Sphere spectrum; stable stems, $\pi_k^s = \pi_k(\mathbb{S})$ |
| $\Sigma^\infty X$, $\Omega^\infty E$ | Suspension spectrum of $X$; zero space of $E$ |
| $H\pi$ | Eilenberg–MacLane spectrum; $\pi_0 \cong \pi$, $\pi_k = 0$ for $k \neq 0$ |
| $\Sigma$, $\Omega$ | Suspension and loops on spectra; inverse equivalences |
| $\mathcal{SH}$ | Stable homotopy category; $[E,F]_{\mathcal{SH}} = \operatorname{colim}[E_n,F_n]$ |
| $E \wedge F$ | Smash product; unit $\mathbb{S}$ |
| $E_*$, $E^*$ | Generalised homology and cohomology represented by $E$ |
| $J$ | $J$-homomorphism $\pi_k(SO(n)) \to \pi_{k+n}(S^n)$, stabilising |
| $\mathcal{A}_p$, $Sq^i$, $\mathcal{P}^i$, $\beta$ | Steenrod algebra, squares, powers, Bockstein |
| Adams SS | $E_2^{s,t} = \operatorname{Ext}^{s,t}_{\mathcal{A}_p}(\mathbb{F}_p,H^*(E;\mathbb{F}_p)) \Rightarrow \pi_{t-s}(E)\otimes\mathbb{Z}_p$ |
| $h_i \in \operatorname{Ext}^{1,2^i}_{\mathcal{A}_2}$ | Adams $E_2$ generators; $d_2(h_i) = h_{i-1}^2h_{i-2}$ |
| Atiyah–Hirzebruch SS | $E^2_{p,q} = H_p(X;E_q) \Rightarrow E_{p+q}(X)$ |
| $MU$, $KU$, $KO$ | Complex cobordism; complex and real topological $K$-theory |
| $K(n)$ | Morava $K$-theory of height $n$; $K(n)_* = \mathbb{F}_p[v_n^{\pm1}]$ |
| Type $n$ | $K(n)_*(X)\neq0$ and $K(m)_*(X) = 0$ for $m>n$, $X$ finite |
| Chromatic filtration | Tower of Bousfield localisations at $K(0), K(1), K(2),\dots$ |
| $\eta$, $\nu$, $\sigma$ | Hopf maps $S^3\to S^2$, $S^7\to S^4$, $S^{15}\to S^8$ |
| $S/p$ | Moore spectrum, cofibre of $p : \mathbb{S}\to\mathbb{S}$ |





## Further Reading

- Douglas C. Ravenel, *Complex Cobordism and Stable Homotopy Groups of Spheres* (Academic Press, 2nd ed. 2003), for the Adams–Novikov spectral sequence and the chromatic picture.
- J. Frank Adams, *Stable Homotopy and Generalised Homology* (University of Chicago Press, 1974), for the Adams spectral sequence, the $J$-homomorphism and the Hopf invariant.
- J. Frank Adams, *On the Non-Existence of Elements of Hopf Invariant One* (Annals of Mathematics 72, 1960), for the Hopf invariant one theorem.
- Hirosi Toda, *Composition Methods in Homotopy Groups of Spheres* (Princeton University Press, 1962), for the unstable and stable stems in low dimensions.
- Michael F. Atiyah and Friedrich Hirzebruch, *Vector Bundles and Homogeneous Spaces* (Proceedings of Symposia in Pure Mathematics 3, 1961), for the Atiyah–Hirzebruch spectral sequence and its applications.
- Stanley O. Kochman, *Stable Homotopy Groups of Spheres: A Computer-Assisted Approach* (Springer Lecture Notes in Mathematics 1423, 1990), for the systematic computation of the mod-2 stems.
- Anthony D. Elmendorf, Igor Kriz, Michael A. Mandell and J. Peter May, *Rings, Modules and Algebras in Stable Homotopy Theory* (American Mathematical Society, 1997), for $S$-modules and the multiplicative structure.
- Neil P. Strickland, *An Introduction to the Adams Spectral Sequence* (lecture notes), for a concise treatment aimed at computation.
