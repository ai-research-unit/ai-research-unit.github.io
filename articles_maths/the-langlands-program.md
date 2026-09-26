
# __The Langlands Program__

## Introduction

The Langlands program is a web of conjectures and theorems that relates two kinds of objects: the **Galois representations** — the finite-dimensional representations of the absolute Galois group of a number field or a local field — and the **automorphic representations** — the irreducible constituents of the space of automorphic forms of *Automorphic Forms*. The relation is a dictionary, and its content is that the two objects carry the same arithmetic information, encoded in the equality of their $L$-functions. The simplest instance is class field theory, which identifies the one-dimensional Galois representations of a global field with the automorphic representations of $GL_1$, and it is the prototype of the general statement; the deepest proved case is the modularity theorem for elliptic curves, which identifies the two-dimensional representations arising from elliptic curves with the automorphic representations of $GL_2$.

The program has three layers. The **local** layer is the local Langlands correspondence, a theorem for $GL_n$ over a local field and a conjecture in general, which parameterises the irreducible representations of $G(F)$ by homomorphisms from the local Weil group into the $L$-group ${}^L G$. The **global** layer is the reciprocity conjecture, which asserts that an automorphic representation is the automorphic shadow of a Galois representation and that the two share their $L$-functions. The **functorial** layer is the principle that every homomorphism of $L$-groups transfers automorphic representations from one group to another, and it is the source of the applications: base change, the symmetric power $L$-functions, the endoscopic classification, and the Sato–Tate and Ramanujan problems.

This article states the three layers, records the principal theorems and conjectures, and describes the trace-formula and $L$-function methods by which the theorems are proved. It is the last article of the corpus on the subject and it presupposes *Automorphic Forms*, which supplies the automorphic side; the Galois-side tools — Galois cohomology, class field theory, the arithmetic of local fields — are the arithmetic articles of the corpus, and the analytic theory of $L$-functions is. Three boundaries are held.

- The **automorphic side** — adeles, automorphic forms, the spectral decomposition, $L$-functions of automorphic representations — is *Automorphic Forms* and *Adeles and Ideles*, and is used here as established.
- The **arithmetic side** — Galois groups, Galois cohomology, the fundamental group, class field theory, local fields, global fields — is the subject of the arithmetic articles of the corpus, in particular *Class Field Theory* and *Galois Cohomology*; the geometric side of the function-field case — curves over finite fields, shtukas, moduli of bundles — is the subject of the algebraic-geometry articles and of *Elliptic Curves*. This article states the Langlands programme and does not develop those foundations.
- The **classical modular forms** areand the **$L$-functions** are; where a result is theirs, it is cited and not re-derived. No physics is invoked.

Throughout, $F$ is either a number field or a local field, $\bar F$ a separable closure, $\Gamma_F = \operatorname{Gal}(\bar F/F)$ the absolute Galois group, and $q$ the residue cardinality of a non-archimedean local field. For a reductive group $G$ over $F$, $\hat G$ is the Langlands dual group — the complex reductive group whose root datum is dual to that of $G$ — and ${}^L G = \hat G \rtimes W_F$ is the **$L$-group**, with $W_F$ the Weil group of $F$. An **$L$-parameter** is a continuous homomorphism $W_F \to {}^L G$ satisfying a boundedness condition at infinity; the notation $\pi = \otimes'_v \pi_v$, Satake parameter, and the $L$-function $L(s,\pi)$ are those of *Automorphic Forms*.

## Reciprocity and the Artin Conjecture

### Galois Representations and Artin $L$-Functions

**Definition.** A **Galois representation** is a continuous homomorphism

$$
\rho : \Gamma_F \longrightarrow GL_n(\mathbb{C}),
$$

for $F$ a global field, with the topology of $\mathbb{C}$ discrete so that the kernel is open and the image is finite. More generally one allows $\rho : \Gamma_F \to GL_n(\overline{\mathbb{Q}}_\ell)$ with $\ell$-adic coefficients and $\rho$ unramified almost everywhere, the arithmetic case of the theory.

**Definition.** Let $\rho$ be a Galois representation of a number field $F$, unramified outside a finite set $S$ of places. The **Artin $L$-function** is the Euler product

$$
L(s, \rho) = \prod_{v \notin S} \det\!\left(1 - \rho(\operatorname{Frob}_v)\, N(v)^{-s} \mid \mathbb{C}^n\right)^{-1},
$$

where $\operatorname{Frob}_v$ is a Frobenius element at $v$, well defined up to conjugacy because $\rho$ is unramified at $v$, and $N(v)$ is the cardinality of the residue field.

The local factors at the ramified places and at infinity are defined by the decomposition theory of the local Galois group (the Weil–Deligne representations), and the completed $L$-function satisfies a functional equation. The Artin conjecture is the following.

**Conjecture (Artin).** Let $\rho$ be an irreducible nontrivial Galois representation of a number field. Then $L(s,\rho)$ extends to an entire function of $s$; more generally, the completed $L$-function satisfies the expected functional equation and has no pole except for the trivial representation.

The conjecture is known for one-dimensional $\rho$ — where the $L$-function is a Hecke $L$-function and the analytic continuation is classical — and for two-dimensional representations of odd Galois groups by the work of Langlands and Tunnell, which is the dihedral, tetrahedral, octahedral and icosahedral case of the modularity theorem. It remains open in general.

### Reciprocity

The Langlands reciprocity conjecture is the statement that Artin $L$-functions are automorphic $L$-functions, and therefore that the Artin conjecture follows from the analytic properties of the automorphic $L$-functions.

**Conjecture (Langlands reciprocity).** Let $F$ be a global field and let $\rho : \Gamma_F \to GL_n(\mathbb{C})$ be a Galois representation. Then there is a cuspidal automorphic representation $\pi$ of $GL_n(\mathbb{A}_F)$ with

$$
L(s, \pi) = L(s, \rho),
$$

the equality holding at every place including the ramified and archimedean ones. In particular $L(s,\rho)$ is entire for irreducible $\rho$ and satisfies the functional equation of $\pi$.

The case $n=1$ is **class field theory**: the one-dimensional Galois representations correspond to Hecke characters, and the Artin $L$-function of a character is the Hecke $L$-function of the corresponding idele class character; this is the theorem of *Class Field Theory*, and it is the foundation of the whole programme. The case $n=2$ over $\mathbb{Q}$ with $\rho$ arising from the mod $\ell$ representation of an elliptic curve is the modularity theorem, proved by Wiles and Taylor–Wiles for semistable curves and by Breuil, Conrad, Diamond and Taylor in general; the automorphic representation is that of a weight-two cusp form, and the equality of $L$-functions is the equality of the arithmetic and analytic descriptions of the same elliptic curve.

**Example (the Ramanujan conjecture).** For a cuspidal automorphic representation $\pi$ of $GL_2(\mathbb{A}_{\mathbb{Q}})$ of weight $k$, the Ramanujan–Petersson conjecture asserts $|a_p| \le 2p^{(k-1)/2}$. For weight $k \geq 2$ it is a theorem of Deligne, and the proof is by the reciprocity conjecture: the automorphic representation is the shadow of a Galois representation $\rho$, and the Ramanujan bound is the Weil bound for the eigenvalues of Frobenius acting on the $\ell$-adic cohomology of a variety. The passage from the automorphic statement to the geometric one is the prototype of the arithmetic use of the Langlands correspondence.

## The Weil Group and the $L$-Group

### The Weil Group

**Definition.** Let $F$ be a local or global field. The **Weil group** $W_F$ is the subgroup of $\Gamma_F$ generated by the inertia subgroup and by a Frobenius lift, topologised so that the inertia subgroup is open and the Frobenius generates a discrete cyclic quotient: for a non-archimedean local field there is a short exact sequence

$$
1 \longrightarrow I_F \longrightarrow W_F \longrightarrow \mathbb{Z} \longrightarrow 1,
$$

with $I_F$ the inertia group, and for an archimedean field $W_{\mathbb{R}} = \mathbb{C}^\times \cup j\mathbb{C}^\times$ and $W_{\mathbb{C}} = \mathbb{C}^\times$.

The Weil group is a substitute for the Galois group that keeps the Frobenius available while discarding the profinite topology that would make the representations hard to control; its representations are the Weil–Deligne representations, the pairs $(\rho, N)$ of a representation of $W_F$ and a nilpotent "monodromy" operator $N$ with $\rho(w)N\rho(w)^{-1} = \|w\| N$. Every Galois representation is a Weil representation, and in the arithmetic applications one works with the Weil group because the local parameters are its representations.

### The $L$-Group

**Definition.** Let $G$ be a connected reductive group over $F$ with dual group $\hat G$ and a maximal torus $T \subseteq G$ with dual torus $\hat T$. The **$L$-group** is the semidirect product

$$
{}^L G = \hat G \rtimes W_F,
$$

where $W_F$ acts on $\hat G$ through its action on the root datum of $G$; for $G$ split over $F$ the action is trivial and ${}^L G = \hat G \times W_F$.

The dual group is the algebraic home of the local data: for an unramified representation $\pi_v$ the Satake parameter is a semisimple conjugacy class in ${}^L G$, and it is exactly the image of a Frobenius element under a parameter $W_F \to {}^L G$. The purpose of the semidirect product is to accommodate the twist by the Galois action on the roots: a group $G$ that is not split over $F$ has a nontrivial action of $W_F$ on $\hat G$, and the $L$-group records it.

**Example.** For $G = GL_n$ the dual group is $\hat G = GL_n(\mathbb{C})$ and ${}^L G = GL_n(\mathbb{C}) \times W_F$; a local $L$-parameter for $GL_n$ is thus essentially an $n$-dimensional representation of $W_F$. For $G = SL_n$ the dual is $PGL_n(\mathbb{C})$; for $G$ an orthogonal group the dual is a symplectic or orthogonal group according to the type; and for $G$ a torus $T$ the dual is the dual torus $\hat T$ and the local Langlands correspondence is the local class field theory identification of the characters of $T(F)$ with the homomorphisms $W_F \to \hat T$.

## The Local Langlands Correspondence

### The Statement

**Theorem (local Langlands for $GL_n$; Harris–Taylor, Henniart).** Let $F$ be a non-archimedean local field and let $n \geq 1$. There is a canonical bijection

$$
\left\{ \text{irreducible admissible representations } \pi \text{ of } GL_n(F) \right\} \longleftrightarrow \left\{ \text{$n$-dimensional Frobenius-semisimple Weil–Deligne representations } \rho \text{ of } W_F \right\},
$$

characterised by the equality of local factors: for every irreducible representation $\pi$ and its parameter $\rho = \phi_\pi$, and for every character $\chi$ of $F^\times$,

$$
\gamma(s, \pi \times \chi, \psi) = \gamma(s, \rho \otimes \chi, \psi),
$$

where the local $\gamma$-factors on the left are those defined by the zeta integrals of *Automorphic Forms* and the local constants on the right are those of Weil–Deligne representations; equivalently, the twisted local $L$-factors and $\varepsilon$-factors agree.

The theorem is the precise form of the local reciprocity for $GL_n$, and it was proved by Harris and Taylor using the geometry of the Lubin–Tate and Drinfeld towers and by Henniart using a different method; the description by local factors characterises the bijection uniquely. For $n=1$ it is local class field theory; for $F$ archimedean it is the theorem of Langlands that classifies the irreducible admissible representations of $GL_n(\mathbb{R})$ and $GL_n(\mathbb{C})$ by parameters of the Weil group; and for a general reductive $G$ the statement is a conjecture, proved for many groups by Arthur's endoscopic classification.

**Definition.** An **$L$-parameter** for $G$ over $F$ is a homomorphism

$$
\phi : W_F \times SL_2(\mathbb{C}) \longrightarrow {}^L G
$$

whose restriction to $W_F$ is continuous, whose images of the two factors commute, and whose composition with ${}^L G \to W_F$ is the identity map on $W_F$; the factor $SL_2(\mathbb{C})$ encodes the monodromy and is the algebraic form of the unipotent part of the Weil–Deligne representation. The local conjecture is that the irreducible admissible representations of $G(F)$ are parameterised by the $L$-parameters up to conjugacy by $\hat G$, and that the fibres are the **$L$-packets**.

### The Local Factors

The local Langlands correspondence is characterised by the equality of local factors, and this is what makes it a working theorem rather than a classification alone.

**Definition.** For an $L$-parameter $\phi$ of $GL_n(F)$ the **local $L$-factor** and **$ \varepsilon$-factor** are

$$
L(s, \phi) = \det\!\left(1 - \phi(\operatorname{Frob})\, q^{-s}\right)^{-1}, \qquad \varepsilon(s, \phi, \psi) = \varepsilon(\phi)\, q^{-c(s-1/2)},
$$

for unramified $\phi$, with the general case defined by the local analysis of the Weil–Deligne representation; $c$ is the conductor and $\psi$ a nontrivial additive character.

The local factors are multiplicative in exact sequences — the inductivity of $\gamma$-factors — and this multiplicativity is the technical reason functoriality can be formulated: a homomorphism of $L$-groups transfers parameters, and the equality of local factors transfers the corresponding automorphic data.

## The Global Langlands Correspondence

### The Conjecture

**Conjecture (global Langlands reciprocity).** Let $F$ be a number field and $G$ a connected reductive group over $F$. Then there is a partition of the set of automorphic representations of $G(\mathbb{A}_F)$ into $L$-packets in such a way that the packets are in bijection with the global $L$-parameters $W_F \to {}^L G$ whose local components are the parameters of the local packets, and the $L$-functions correspond: for a parameter $\phi = \otimes_v\phi_v$ and the packet $\Pi_\phi = \otimes'_v \Pi_{\phi_v}$,

$$
L(s, \Pi_\phi) = L(s, \phi) = \prod_v L(s, \phi_v).
$$

The conjecture has two directions. The **arithmetic-to-automorphic** direction attaches to each Galois representation an automorphic representation with the same $L$-function; the **automorphic-to-arithmetic** direction asserts that every automorphic representation of the relevant type arises this way, and it is the form taken by the Fontaine–Mazur conjecture: a geometric $\ell$-adic Galois representation of a number field should be automorphic. The two directions are the content of the reciprocity between the Galois world and the automorphic world.

### The Known Cases

**Theorem (Drinfeld; Lafforgue).** Let $F$ be a global function field of characteristic $p$ and let $n \geq 1$. The global Langlands correspondence for $GL_n$ over $F$ holds: the cuspidal automorphic representations of $GL_n(\mathbb{A}_F)$ correspond to the $n$-dimensional irreducible $\ell$-adic Galois representations of $F$ with the equality of $L$-functions, and the correspondence is compatible with the local Langlands correspondence at every place.

Drinfeld proved the case $n=2$ and introduced the moduli of **shtukas** — the function-field analogue of the moduli of elliptic curves, carrying two modifications of a vector bundle — and Lafforgue proved the general case by developing the trace formula for the moduli of shtukas. The function-field theorem is the strongest known global result, and it is the model for the number-field conjecture, which remains open for $GL_n$ with $n \geq 3$ except for the cases supplied by functoriality from smaller groups.

**Theorem (modularity; Wiles, Taylor–Wiles, Breuil–Conrad–Diamond–Taylor).** Let $E$ be an elliptic curve over $\mathbb{Q}$. Then there is a cuspidal automorphic representation $\pi$ of $GL_2(\mathbb{A}_{\mathbb{Q}})$ of weight two and level $N_E$ with

$$
L(s, E) = L(s, \pi),
$$

where $L(s,E)$ is the Hasse–Weil $L$-function of $E$. Equivalently, every elliptic curve over $\mathbb{Q}$ is modular.

The theorem is the number-field case $GL_2$ of reciprocity for representations of geometric origin, and it was the key to Wiles's proof of Fermat's last theorem: the Frey curve attached to a hypothetical solution has a mod $p$ Galois representation that cannot be modular, so no solution exists. The proof uses the Taylor–Wiles patching method, which constructs an automorphic representation from a deformation ring by comparing it with a Hecke algebra, and the automorphy lifting theorems that grew from it are the main technical engine of the modern arithmetic Langlands programme.

## Functoriality

### The Principle

**Conjecture (functoriality; Langlands).** Let $H$ and $G$ be connected reductive groups over a global field $F$ and let

$$
{}^L H \longrightarrow {}^L G
$$

be an $L$-homomorphism — a homomorphism of the $L$-groups respecting the projections to $W_F$ and algebraic on the dual groups. Then there is a **transfer** of automorphic representations: to each automorphic representation $\pi$ of $H(\mathbb{A}_F)$ there corresponds an automorphic representation $\Pi$ of $G(\mathbb{A}_F)$ such that, for every finite-dimensional representation $r$ of ${}^L G$,

$$
L(s, \Pi, r) = L(s, \pi, r \circ {}^L\phi),
$$

so that the $L$-functions of $\pi$ and $\Pi$ agree for all the representations of the dual groups related by the $L$-homomorphism.

Functoriality is the generalisation of the reciprocity conjecture from the case $H$ trivial: the reciprocity conjecture attaches to the homomorphism $W_F \to {}^L G$ the transfer of the trivial automorphic representation of the trivial group, and the general statement transfers automorphic representations between groups. It is the organising conjecture of the subject, and it is known in a substantial number of cases.

### Base Change and Induction

**Theorem (cyclic base change; Langlands, Saito, Shintani).** Let $E/F$ be a cyclic extension of number fields of prime degree and let $G = GL_n$. For each automorphic representation $\pi$ of $G(\mathbb{A}_F)$ there is a **base change** $\Pi = BC_{E/F}(\pi)$, an automorphic representation of $G(\mathbb{A}_E)$ whose $L$-function is the $L$-function of $\pi$ with respect to the restriction of the Galois representation, and the map is compatible with the local Langlands correspondence: the local parameter of $\Pi_v$ is the restriction of the local parameter of $\pi_v$ to $W_{E_w}$.

**Theorem (automorphic induction).** Let $E/F$ be as above and let $\pi$ be an automorphic representation of $GL_n(\mathbb{A}_E)$. Then there is an automorphic representation $\Pi = AI_{E/F}(\pi)$ of $GL_n(\mathbb{A}_F)$ with the $L$-function of the induced $n$-dimensional parameter; it corresponds to the $L$-homomorphism ${}^L H \to {}^L G$ induced by the inclusion of the dual groups when it exists, and to the induction of Galois representations.

Base change and automorphic induction are the functorial transfers obtained from cyclic covers, and they are proved by the trace formula: one compares the twisted trace formula for $GL_n$ over $E$ with the stable trace formula over $F$ and identifies the spectral terms. They are the classical source of the applications — the proof of the Artin conjecture for the two-dimensional cases, the existence of automorphic forms of level one, and the Sato–Tate conjecture.

### Endoscopy and the Trace Formula

**Theorem (Arthur's endoscopic classification).** Let $G$ be a quasi-split symplectic or orthogonal group over a number field. Then the discrete automorphic spectrum of $G$ is described by the endoscopic data of $G$: the automorphic representations are parameterised by the elliptic $L$-parameters, and the multiplicities in the discrete spectrum are given by the stable trace formula.

The endoscopic classification is the strongest general theorem in the direction of functoriality; it was established by Arthur, following the strategy of Langlands, and it supplies functoriality for the classical groups in a form strong enough for the applications (the Ramanujan conjecture for classical groups, the automorphic descriptions of the symmetric powers, and the classification of the residual spectrum). The method is the **stable trace formula**: one writes the trace formula in a form that is stable under inner forms, computes the geometric side by the fundamental lemma of Ngô, and compares the stable trace formula of $G$ with the sum of the stable trace formulas of its endoscopic groups. The comparison produces the classification, and the fundamental lemma — proved by Ngô Bao Châu — is the local input that makes the comparison possible.

## The Geometric Langlands Program

The function-field case of the global correspondence has a geometric refinement that replaces Galois representations by local systems on a curve and automorphic representations by Hecke eigensheaves on the moduli of bundles.

**Conjecture (geometric Langlands).** Let $X$ be a smooth projective curve over an algebraically closed field, let $G$ be a connected reductive group over the base, and let $\hat G$ be its dual. Then there is an equivalence of categories between the coherent sheaves on the moduli of $\hat G$-local systems on $X$ — or the derived category of D-modules on it, depending on the formulation — and the sheaves on the moduli stack of $G$-bundles on $X$ that are eigen for the Hecke operators, with the eigen-labels the local systems.

The geometric conjecture implies the function-field Langlands correspondence when the curve is defined over a finite field and one takes traces of Frobenius, and it organises the arithmetic statement into a geometric and representation-theoretic one. It is known in the abelian case (the geometric class field theory of the moduli of line bundles), for $GL_2$ by Drinfeld, and in the rank-one case by Gaitsgory and collaborators; the de Rham, Betti and étale versions differ in the sheaf theory they use, and the relation to the arithmetic case is the subject of the **arithmetic geometric Langlands** programme.

## Summary

The Langlands program relates the Galois representations of a number field or local field to the automorphic representations of *Automorphic Forms*, and the content of the relation is the equality of the $L$-functions. The local layer is the local Langlands correspondence, a theorem for $GL_n$ over a local field which parameterises the irreducible admissible representations by Frobenius-semisimple Weil–Deligne representations of the local Weil group and is characterised by the equality of local and $\varepsilon$-factors; the general-group statement is a conjecture, with the factor $SL_2(\mathbb{C})$ in the $L$-parameter encoding the monodromy and the fibres being the $L$-packets. The global layer is the reciprocity conjecture, which asserts that automorphic representations and global $L$-parameters correspond with equal $L$-functions; its known cases are class field theory for $GL_1$, the modularity theorem for elliptic curves over $\mathbb{Q}$ for $GL_2$, and the theorems of Drinfeld and Lafforgue for $GL_n$ over a function field.

The functorial layer is the principle that an $L$-homomorphism ${}^L H \to {}^L G$ transfers automorphic representations, with base change and automorphic induction for cyclic covers as the classical cases and Arthur's endoscopic classification for symplectic and orthogonal groups as the strongest general theorem; the tool throughout is the trace formula, in the stable form whose local input is the fundamental lemma of Ngô. The Artin conjecture is the statement that the Galois $L$-functions are entire, and it is a corollary of reciprocity; the Ramanujan–Petersson conjecture follows from the Galois side in the cases where the correspondence is known, as in Deligne's proof for weight at least two. The function-field case admits the geometric refinement that replaces the arithmetic correspondence by an equivalence of categories of sheaves on the moduli of bundles, which is proved in the abelian and rank-one cases and is the subject of an active programme.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $\bar F$, $\Gamma_F$ | Global or local field, separable closure, absolute Galois group |
| $W_F$, $I_F$ | Weil group and inertia subgroup |
| $\rho$ | Galois or Weil–Deligne representation |
| $L(s,\rho)$ | Artin $L$-function of a Galois representation |
| $\hat G$, ${}^L G = \hat G \rtimes W_F$ | Langlands dual group and $L$-group |
| $L$-parameter, $L$-packet | homomorphism $W_F\times SL_2(\mathbb{C})\to{}^L G$, and its fibre of representations |
| $\gamma(s,\pi\times\chi,\psi)$, $\varepsilon(s,\phi,\psi)$ | Local gamma and epsilon factors |
| $L(s,\pi)$, $\Lambda(s,\pi)$ | Automorphic $L$-function and its completion |
| $BC_{E/F}$ | Cyclic base change |
| $AI_{E/F}$ | Automorphic induction |
| functoriality | transfer of automorphic representations along ${}^L H\to{}^L G$ |
| endoscopic classification | description of the discrete spectrum of a classical group by its endoscopic data |
| shtuka, Drinfeld, Lafforgue | function-field reciprocity and its proof |
| modularity | $L(s,E)=L(s,\pi)$ for an elliptic curve $E/\mathbb{Q}$ |
| geometric Langlands | equivalence of sheaf categories on the moduli of bundles |



## Further Reading

- Robert P. Langlands, "Problems in the theory of automorphic forms", in *Lectures in Modern Analysis and Applications III* (Springer Lecture Notes 170, 1970), for the foundational conjectures including functoriality and reciprocity.
- Robert P. Langlands, *Base Change for $GL(2)$* (Princeton University Press, 1980), for cyclic base change for $GL_2$.
- Michael Harris and Richard Taylor, *The Geometry and Cohomology of Some Simple Shimura Varieties* (Princeton University Press, 2001), and Guy Henniart, "Une preuve simple des conjectures de Langlands pour $GL(n)$ sur un corps $p$-adique", *Inventiones Mathematicae* 139 (2000), 439–455, for the local Langlands correspondence for $GL_n$.
- Vladimir Drinfeld, "Langlands' conjecture for $GL(2)$ over functional fields", *Proceedings of the International Congress of Mathematicians* (1978), and Laurent Lafforgue, "Chtoucas de Drinfeld et correspondance de Langlands", *Inventiones Mathematicae* 147 (2002), 1–241, for the function-field case.
- Andrew Wiles, "Modular elliptic curves and Fermat's last theorem", *Annals of Mathematics* 141 (1995), 443–551, and Christophe Breuil, Brian Conrad, Fred Diamond and Richard Taylor, "On the modularity of elliptic curves over $\mathbb{Q}$", *Journal of the American Mathematical Society* 14 (2001), 843–939, for modularity.
- James Arthur and Laurent Clozel, *Simple Algebras, Base Change, and the Advanced Theory of the Trace Formula* (Princeton University Press, 1989), and James Arthur, *The Endoscopic Classification of Representations* (AMS, 2013), for the trace-formula method and endoscopy.
- Ngô Bao Châu, "Le lemme fondamental pour les algèbres de Lie", *Publications Mathématiques de l'IHÉS* 111 (2010), 1–169, for the fundamental lemma.
- Thomas Hales, "A proof of the Sato–Tate conjecture", *Journal of the American Mathematical Society* 9 (1996), 309–332 (under the Ramanujan conjecture), and Laurent Clozel, Michael Harris, Nicholas Shepherd-Barron and Richard Taylor, "Automorphy for some $\ell$-adic lifts of automorphic mod $\ell$ Galois representations", *Publications Mathématiques de l'IHÉS* 108 (2008), 1–181, for the unconditional Sato–Tate theorem.
- Alexander Beilinson and Vladimir Drinfeld, "Quantization of Hitchin's integrable system and Hecke eigensheaves" (preprint, 1991), and Dennis Gaitsgory et al., "Proof of the geometric Langlands conjecture" (2024), for the geometric programme.
- Jean-Pierre Serre, *Local Fields* (Springer, 1979), and J. S. Milne, *Class Field Theory* (available from the author), for the arithmetic foundations used throughout.
