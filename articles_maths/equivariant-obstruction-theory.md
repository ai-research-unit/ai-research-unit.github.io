# __Equivariant Obstruction Theory__

## Introduction

Obstruction theory answers the extension and the lifting questions of homotopy theory degree by degree: given a map defined on the $n$-skeleton of a complex, the obstruction to extending it over the $(n+1)$-skeleton is a cohomology class with coefficients in the $n$-th homotopy group of the target, and the map extends exactly when the class vanishes. For a group acting on both the complex and the target the same scheme runs with two changes: the cells are of the form $G/H\times D^n$, one orbit type at a time, and the coefficients are the **homotopy groups of the fixed sets**, assembled into a coefficient system on the orbit category. The resulting theory, the **equivariant obstruction theory** of Bredon and tom Dieck, lives in the **Bredon cohomology** $H^*_G(X;\underline M)$ with coefficients a contravariant functor on the orbit category $\mathcal O_G$, and its classes are the **equivariant obstruction classes**. The theory is the equivariant form of the ordinary obstruction theory, and its coefficients are the coefficient systems that the equivariant homotopy theory of this category has already fixed.

The article develops the theory. It defines the orbit category and the coefficient systems on it, the Bredon cochain complex and the Bredon cohomology, states the equivariant extension problem on the $G$-CW complexes of *Equivariant Homotopy Theory*, constructs the obstruction cocycle and the obstruction class of a $G$-map and proves the vanishing criterion, treats the classification of the equivariant extensions through the difference cocycle and the equivariant Postnikov tower, and closes with the consequences and the examples. The equivariant homotopy theory, the $G$-CW complexes, the equivariant homotopy groups $\pi_n^H(X)$ and the orbit category are those of *Equivariant Homotopy Theory*; the equivariant cohomology and the fixed-point functors are those of *Equivariant Cohomology*; the fixed set and its invariants are those of *The Mod 2 Cohomology of an Involution*; the ordinary obstruction theory and its local coefficients are those of *Obstruction Theory and the Extension Problem* and *Cohomology and the Universal Coefficient Theorem*; and the spectral sequences are those of *The Leray–Serre Spectral Sequence*. Nothing analytic and nothing geometric is used.

Throughout, $G$ is a finite group, $X$ is a $G$-CW complex with cells $G/H_\alpha\times D^n$ attached equivariantly, $Y$ is a $G$-space, and $\mathcal O_G$ is the **orbit category** whose objects are the orbits $G/H$ and whose morphisms are the $G$-maps $G/H\to G/K$. A **coefficient system** is a contravariant functor $\underline M : \mathcal O_G\to \mathbf{Ab}$ to abelian groups, and its value at the orbit $G/H$ is written $M(G/H)$ or $\underline M(G/H)$. The coefficient system of the homotopy groups of a $G$-space is $\underline\pi_n(Y)(G/H) = \pi_n(Y^H)$, the $n$-th homotopy group of the fixed set of $H$. The Bredon cohomology of $X$ with coefficients $\underline M$ is written $H^*_G(X;\underline M)$. All the spaces are $G$-CW complexes or $G$-homotopy equivalent to them, and the coefficients are abelian groups.

## Coefficient Systems and Bredon Cohomology

### The Orbit Category and Its Coefficient Systems

**Definition.** The **orbit category** $\mathcal O_G$ has the orbits $G/H$ for $H \leq G$ as objects and the $G$-maps between them as morphisms; a morphism $G/H\to G/K$ exists exactly when $H$ is conjugate to a subgroup of $K$, so the morphisms are the conjugacy-class data $\{g \in G : gHg^{-1}\subseteq K\}/K$. A **coefficient system** is a contravariant functor $\underline M : \mathcal O_G\to\mathbf{Ab}$ to abelian groups; the category of coefficient systems is abelian with the pointwise structure, and it is equivalent to the category of **Mackey functors** when the extra restriction–induction structure is imposed.

**Proposition.** The assignment $G/H\mapsto\pi_n(Y^H)$ is a coefficient system $\underline\pi_n(Y)$, the **homotopy coefficient system** of the $G$-space $Y$, and it is the primary example; the assignment $G/H\mapsto H^*(Y^H;M)$ is a coefficient system for every coefficient group $M$, and the constant coefficient system $\underline M(G/H)=M$ corresponds to the trivial action. The fixed-point functors of *Equivariant Homotopy Theory* are the values of these coefficient systems, so the equivariant coefficients are exactly the fixed-point data.

*Proof.* A morphism $G/H\to G/K$, that is a $G$-map, restricts a $K$-fixed point to an $H$-fixed point, so it induces a map $Y^K\to Y^H$ and hence a map on homotopy groups in the reverse direction; the functoriality is the functoriality of the fixed set and of the homotopy groups, which gives the contravariance. $\square$

### The Bredon Cochain Complex

**Definition.** The **Bredon cochain complex** of the $G$-CW complex $X$ with coefficients $\underline M$ is

$$
C^n_G(X;\underline M) = \prod_{\sigma\ =\ G/H_\alpha\times D^n} M(G/H_\alpha),
$$

the product of the coefficient groups over the equivariant $n$-cells, graded by $n$, with the **Bredon differential** $\delta$ the sum over the attaching maps: on the cell $\sigma$ the value at $\sigma$ is the alternating sum of the coefficients of the restrictions of $\sigma$'s attaching map to the $(n-1)$-cells, transported by the maps of the coefficient system. The cohomology of this complex is the **Bredon cohomology**

$$
H^n_G(X;\underline M) = H^n\bigl(C^*_G(X;\underline M)\bigr).
$$

**Theorem.** The Bredon cohomology is a contravariant functor in the pair $(X,\underline M)$, natural for equivariant maps and for morphisms of coefficient systems, and it is a generalised cohomology theory on the $\mathcal O_G$-spaces. For a free $G$-CW complex with constant coefficients it reduces to ordinary cohomology with local coefficients; for $G=1$ it is the ordinary singular cohomology. The values on the cells compute it: for a $G$-CW complex the cochain complex above is the cellular Bredon complex, and a morphism of coefficient systems induces a map of the complexes.

*Proof.* The Bredon complex is the complex of the cellular $G$-chains with coefficients the coefficient system, which is a cochain complex of abelian groups; the functoriality is termwise; for $G=1$ the orbit category is the terminal category and the coefficient system is a single group, giving the ordinary cellular complex. $\square$

### The Equivariant Coefficients

**Proposition.** The coefficient system $\underline\pi_n(Y)$ is the one that carries the equivariant $n$-th homotopy groups: its value at $G/H$ is $\pi_n^H(Y) = \pi_n(Y^H)$, so the Bredon cohomology $H^{n+1}_G(X;\underline\pi_n(Y))$ is the target of the obstruction theory of the next section. For a group action through a quotient and a coefficient system factoring through it, the Bredon cohomology of the quotient group computes that of the group, so the theory is compatible with the quotient operations of *The Cohomology of an Orbit Space*.

*Proof.* The identification is the definition of the equivariant homotopy groups of *Equivariant Homotopy Theory*, and the statement about a quotient group is the functoriality of the orbit category under the quotient map $G\to G/N$. $\square$

## The Extension Problem

### The Equivariant Skeleton

**Definition.** A **$G$-CW structure** on $X$ consists of the equivariant skeleta $X^n$ obtained from $X^{n-1}$ by attaching equivariant cells $G/H_\alpha\times D^n$ along equivariant attaching maps $G/H_\alpha\times S^{n-1}\to X^{n-1}$; the **equivariant extension problem** is, given a $G$-map $f : X^n\to Y$ on the $n$-skeleton, to extend it to a $G$-map $X^{n+1}\to Y$, and, if possible, to $\bar f : X\to Y$.

**Proposition.** A $G$-map is determined on an equivariant cell $G/H\times D^n$ by its restriction to the orbit $G/H\times\{0\}$, by equivariance; the restriction of a $G$-map $f : X\to Y$ to an equivariant cell is a $G$-map $G/H\times D^n\to Y$, equivalently an ordinary map $D^n\to Y^H$, and its restriction to the boundary is an ordinary map $S^{n-1}\to Y^H$ representing a class of $\pi_{n-1}(Y^H)$. The equivariant extension problem on a single cell is the ordinary extension problem for the fixed set of $H$.

*Proof.* Equivariance determines the map on the whole cell by its values on a fundamental domain $D^n$; the adjunction $\mathrm{Map}_G(G/H\times D^n,Y)\cong\mathrm{Map}(D^n,Y^H)$ is the standard homeomorphism, and the boundary corresponds to $S^{n-1}$. $\square$

### The Obstruction Cocycle

**Definition.** Let $f : X^n\to Y$ be a $G$-map. The **obstruction cocycle** of $f$ is the Bredon cochain

$$
\mathfrak o(f) \in C^{n+1}_G(X;\underline\pi_n(Y)), \qquad \mathfrak o(f)(\sigma) = [\,f|_{\partial\sigma}\,] \in \pi_n(Y^{H_\alpha}),
$$

where $\sigma = G/H_\alpha\times D^{n+1}$ runs over the equivariant $(n+1)$-cells, the boundary $\partial\sigma = G/H_\alpha\times S^{n}$ maps under $f$ into $Y$, and the class of the restriction is taken in $\pi_n(Y^{H_\alpha})$ under the adjunction of the previous proposition.

**Theorem.** The obstruction cocycle is a cocycle, $\delta\,\mathfrak o(f) = 0$, so it defines a cohomology class

$$
[\mathfrak o(f)] \in H^{n+1}_G(X;\underline\pi_n(Y)),
$$

the **obstruction class** of $f$; the map $f$ extends to a $G$-map $X^{n+1}\to Y$ if and only if $[\mathfrak o(f)] = 0$, and then the obstruction cocycle itself vanishes for a suitable choice of the extension.

*Proof.* The coboundary $\delta\mathfrak o(f)$ evaluated on an $(n+2)$-cell is the alternating sum of the classes on the boundary $(n+1)$-cells, and the sum telescopes because the boundary of the boundary vanishes in the equivariant cellular chain complex, each summand being the image of the corresponding cell class under the maps of the coefficient system; hence $\delta\mathfrak o(f)=0$. The extension exists exactly when each class $\mathfrak o(f)(\sigma)$ is zero, because on each cell the extension over $D^{n+1}$ is the null-homotopy of the boundary map, and the vanishing of the cohomology class is the existence of a cochain whose coboundary is the cocycle, which is the corrected choice of the values on the cells. $\square$

### The Refined Criterion

**Theorem.** If the obstruction class vanishes, the extensions over $X^{n+1}$ are classified up to homotopy relative to $X^n$ by the Bredon group $H^n_G(X;\underline\pi_{n+1}(Y))$: the difference of two extensions is the cocycle

$$
\mathfrak d(f,f') \in C^n_G(X;\underline\pi_{n+1}(Y)), \qquad \mathfrak d(f,f')(\tau) = [\,\text{the class of the homotopy on the }n\text{-cell }\tau\,],
$$

and it vanishes exactly when the two extensions are homotopic as $G$-maps relative to the $n$-skeleton. The obstructions to the successive extensions are the classes $[\mathfrak o]\in H^{n+1}_G(X;\underline\pi_n(Y))$ for $n$ increasing, and a $G$-map $X\to Y$ exists with prescribed restriction to $X^n$ exactly when all of them vanish.

*Proof.* Two extensions differ by a map of the $G$-spheres to $Y$ on each cell, which is a class in the next coefficient group; the cocycle condition is the same computation as before, and the vanishing is the existence of a homotopy of $G$-maps on each cell, assembled by the equivariance. $\square$

## The Classification of Equivariant Maps

### The Postnikov Tower

**Definition.** The **equivariant Postnikov tower** of the $G$-space $Y$ is the tower of $G$-spaces $Y\to\cdots\to Y_{n}\to Y_{n-1}\to\cdots$, in which $Y_n$ has the same equivariant homotopy groups as $Y$ in degrees at most $n$ and vanishing above, each fibration $Y_n\to Y_{n-1}$ being a twisted product of Eilenberg–Mac Lane $G$-spaces with coefficients the coefficient system $\underline\pi_n(Y)$, classified by a **$k$-invariant**

$$
k_n \in H^{n+1}_G\bigl(Y_{n-1};\underline\pi_n(Y)\bigr).
$$

**Theorem.** A $G$-map $X\to Y$ is, up to equivariant homotopy, the same as a compatible family of $G$-maps $X\to Y_n$ for all $n$, and the lifting over $Y_{n-1}$ to $Y_n$ of a given $G$-map $X\to Y_{n-1}$ has obstruction class in $H^{n+1}_G(X;\underline\pi_n(Y))$; the set of equivariant homotopy classes $[X,Y]_G$ is therefore computed by the successive obstruction classes, and it is a tower of torsors over the Bredon groups $H^n_G(X;\underline\pi_n(Y))$.

*Proof.* The Postnikov tower is the obstruction-theoretic decomposition of the target; a lift over $Y_{n-1}$ exists exactly when the obstruction class vanishes, by the extension theorem applied to the fibration, and the successive lifts produce the map to the limit; the torsor structure is the classification theorem of the previous section. $\square$

### The Classification Theorem

**Theorem.** Let $X$ be a $G$-CW complex with $\dim X \leq N$ and let $Y$ be a $G$-space. Then the set $[X,Y]_G$ of equivariant homotopy classes of $G$-maps is non-empty if and only if the successive obstruction classes vanish, and it is a tower of torsors over the groups $H^n_G(X;\underline\pi_n(Y))$, $0 \leq n \leq N$; the whole set is computed by the Bredon cohomology of $X$ with the homotopy coefficient systems of $Y$. For a free action and a constant coefficient system this is the ordinary classification with local coefficients, and for $G=1$ it is the ordinary classification of homotopy classes by obstruction theory.

*Proof.* The tower statement is the classification theorem of the previous section read degree by degree, and the identification with ordinary obstruction theory in the two extreme cases is the reduction of the coefficient systems described above. $\square$

## The Lifting Problem and the Representations

### The Equivariant Lifting

**Definition.** For a $G$-fibration $p : E\to B$ with fibre the $G$-space $F$ and a $G$-map $f : X\to B$, the **equivariant lifting problem** is the search for a $G$-map $\tilde f : X\to E$ with $p\tilde f=f$; it is solved degreewise on the equivariant skeleta, and its obstructions are the equivariant obstruction classes with coefficients the homotopy groups of the fibre fixed sets.

**Theorem.** A $G$-lift of $f$ over the $n$-skeleton extends over the $(n+1)$-skeleton exactly when the equivariant obstruction class in $H^{n+1}_G(X;\underline\pi_n(F))$ vanishes, computed with the same obstruction cocycle as in the extension problem, the value on an equivariant cell being the class of the lifting problem on its boundary in $\pi_n(F^{H})$; the successive obstructions for $n$ increasing are the only obstructions. The lifting problem is thus the extension problem with the coefficient system of the fibre, and the two are the same computation.

*Proof.* The $G$-fibration is the equivariant analogue of a fibration, and the lifting over a cell reduces to the ordinary lifting over the fixed set of the isotropy, by the adjunction of *Equivariant Homotopy Theory*; the obstruction cocycle is the same as in the extension problem with the target replaced by the fibre, and the vanishing criterion is the previous theorem. $\square$

### The Comparison with the Ordinary Theory

**Theorem.** The equivariant obstruction theory specialises to the ordinary one: for $G=1$ the orbit category is the terminal category, the coefficient systems are the coefficient groups and the Bredon cohomology is the ordinary cohomology, so the obstruction classes are the classical ones; for a free action with a constant coefficient system the Bredon cohomology is the ordinary cohomology of the quotient with local coefficients, and the obstruction theory is the ordinary one on $X/G$. More generally the equivariant theory over the orbit category is the ordinary theory fibrewise over $\mathcal O_G$.

*Proof.* The orbit category of the trivial group has one object and the identity morphism, so the coefficient systems are the coefficient groups and the Bredon complex is the ordinary cellular complex; the free case is the identification of the equivariant cells with the cells of the quotient and of the coefficient system with the local system $\underline M(G/H)=M$ along the covering. $\square$

### The Representing Spaces

**Theorem (representability).** For every coefficient system $\underline M$ and every $n \geq 0$ there is a $G$-space $K(\underline M,n)$, the **equivariant Eilenberg–Mac Lane space**, with the property that

$$
\pi_i^H\bigl(K(\underline M,n)\bigr) = \begin{cases} \underline M(G/H) , & i=n, \\ 0, & i \neq n, \end{cases}
$$

and the Bredon cohomology is represented by the equivariant homotopy classes:

$$
H^n_G(X;\underline M) \cong [X, K(\underline M,n)]_G .
$$

The obstruction classes are therefore the classes of the maps into these $G$-spaces, and the extension problem is the problem of the homotopy classes of the equivariant maps.

*Proof.* The equivariant Eilenberg–Mac Lane $G$-spaces are constructed cell by cell on the orbit category, with the $n$-cells indexed by the generators of the coefficient groups and the attaching maps determined by the functoriality; the representability is the analogue of the Brown representability theorem for the $\mathcal O_G$-spectra, and the identification of the cohomology classes with the homotopy classes of maps is the natural transformation that is an isomorphism on the cells. $\square$

## The Obstruction Groups in the Low Degrees

### The First Obstruction

**Theorem.** For a $G$-map defined on the zero skeleton the first obstruction lies in $H^1_G(X;\underline\pi_0(Y))$ and it vanishes if and only if the map is equivariantly homotopic to one extending over the 1-skeleton; if all the fixed sets $Y^H$ are connected, the coefficient system $\underline\pi_0(Y)$ is the zero system, the group vanishes, and every equivariant map of the zero skeleton extends over the 1-skeleton.

*Proof.* The obstruction cocycle on a 1-cell records whether the two components assigned to its endpoints agree, so the vanishing is the existence of the extension over the 1-skeleton; the coefficient system is the assignment $G/H\mapsto\pi_0(Y^H)$, which is zero exactly when the fixed sets are connected. $\square$

### The Second Obstruction and the Fundamental Group

**Theorem.** The next obstruction lies in $H^2_G(X;\underline\pi_1(Y))$ and it obstructs the extension over the 2-skeleton; for a $G$-space $Y$ whose fixed sets are connected and simply connected this group vanishes and every equivariant map of the 1-skeleton extends over the 2-skeleton. The tower therefore begins with the components, continues with the fundamental groups of the fixed sets, and proceeds with the higher homotopy groups, each in the Bredon group with the corresponding coefficient system.

*Proof.* The obstruction cocycle on a 2-cell is the class of the attaching map in the fundamental group of the fixed set of the isotropy, which is the stated group; the successive groups are read from the coefficient systems $\underline\pi_n(Y)$ of the tower. $\square$

## The Computation of the Obstruction Groups

### The Free Case

**Theorem.** For a free $G$-CW complex with a constant coefficient system the Bredon cohomology is the cohomology of the quotient,

$$
H^n_G(X;\underline M) \cong H^n(X/G;M) ,
$$

so the obstruction groups are the ordinary ones of the quotient and the obstruction theory reduces to the classical theory on $X/G$; this is the case of the equivariant obstruction theory in which the group acts without fixed points and the coefficients do not see the isotropy.

*Proof.* The free $G$-CW complex has all the isotropy groups trivial, so the orbit category restricts to the terminal category and the Bredon complex is the cellular complex of the quotient with the constant coefficients; the identification is that of *The Cohomology of an Orbit Space*. $\square$

### The Coefficients of the Tower

**Theorem.** The coefficient system $\underline\pi_n(Y)$ of the obstruction tower is determined by the fixed-point homotopy groups, and the tower inherits the naturality of the target: a $G$-map $Y\to Y'$ induces a morphism of the coefficient systems and hence a map of the obstruction groups, so the obstructions are natural in the target and in the source. The tower is therefore a natural invariant of the equivariant homotopy type, and the classification of the equivariant maps is the same tower computed for each target.

*Proof.* The naturality of the fixed-point functors and of the homotopy groups gives the morphism of the coefficient systems, and the functoriality of the Bredon cohomology gives the map of the groups; the classification theorem then applies to each target. $\square$

## Examples and Consequences

**Example (the obstruction to extending an equivariant map).** Let $G=\mathbb{Z}/2$ act on $X=S^n$ by the antipodal map and let $Y$ be a $G$-space; a $G$-map defined on the $k$-skeleton of $X$ extends over the $(k+1)$-skeleton exactly when its obstruction class in $H^{k+1}_G(X;\underline\pi_k(Y))$ vanishes, so the existence of a $G$-map on the whole of $X$ is decided by the single group $H^{n}_G(X;\underline\pi_{n-1}(Y))$ when the lower obstruction groups vanish. The coefficients are the fixed-point homotopy groups $\pi_k(Y^H)$, and the vanishing of the class is the only obstruction, so the equivariant extension problem is a sequence of computations in Bredon cohomology.

**Example (the obstruction to an equivariant section).** For a $G$-fibre bundle with fibre the $G$-space $Y$ and base $X$, the obstruction to an equivariant section is the same tower of classes with coefficients the homotopy groups of the fibre fixed sets; for the sphere bundles over a $G$-CW base the classes live in the Bredon cohomology and their vanishing is the existence of an equivariant section, recovering the Euler-class obstruction of *The Gysin Sequence of a Two-Fold Covering* for the double cover when the fibre is $S^0$.

**Example (the classifying spaces).** The existence of $G$-maps into the classifying spaces of *Equivariant Cohomology* is an obstruction-theoretic statement: a $G$-map $X\to EG$ exists always because $EG$ is weakly contractible in the equivariant homotopy theory, and the obstruction to an equivariant map into a general $G$-space is the content of the tower; the homotopy quotient $X_G$ is the total space over which the free action is read. The Bredon cohomology of $X$ with coefficients the homotopy coefficient system is the natural receiver of all the obstruction classes.

**Example (the ordinary case).** For a group acting trivially, the orbit category is the category of the group and the coefficient systems are the representations of the group by abelian groups; the Bredon cohomology becomes the group cohomology $H^*(G;M)$ with the fixed coefficients, and the obstruction theory reduces to the ordinary one for the quotient $X/G$ when the action is free. The example shows that the equivariant theory is the ordinary theory made fibrewise over the orbit category.

## Summary

The equivariant obstruction theory is the obstruction theory of the $G$-CW complexes with coefficients in a coefficient system $\underline M$ on the orbit category, that is a contravariant functor $\mathcal O_G\to\mathbf{Ab}$; its cohomology is the Bredon cohomology $H^*_G(X;\underline M)$, computed by the Bredon cochain complex whose degree-$n$ part is the product of the coefficient groups over the equivariant $n$-cells. For a $G$-map $f$ defined on the $n$-skeleton the obstruction to extending it over the $(n+1)$-skeleton is the obstruction cocycle $\mathfrak o(f)\in C^{n+1}_G(X;\underline\pi_n(Y))$, defined on each cell $G/H\times D^{n+1}$ by the class of the boundary map in $\pi_n(Y^H)$, and the extension exists exactly when the obstruction class $[\mathfrak o(f)]\in H^{n+1}_G(X;\underline\pi_n(Y))$ vanishes; the extensions are then classified by $H^n_G(X;\underline\pi_{n+1}(Y))$ through the difference cocycle. The classification of equivariant maps $[X,Y]_G$ is the tower of these obstructions, equivalently the equivariant Postnikov tower of $Y$ with its Bredon $k$-invariants; for $G=1$ the theory is the ordinary obstruction theory, and for a free action with constant coefficients it is the ordinary theory with local coefficients. The equivariant homotopy theory, the $G$-CW complexes and the orbit category are those of *Equivariant Homotopy Theory*, the equivariant cohomology is that of *Equivariant Cohomology*, and the ordinary obstruction theory is that of *Obstruction Theory and the Extension Problem*. Nothing analytic and nothing geometric was used.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $G/H$ | Finite group and its orbits |
| $\mathcal O_G$ | Orbit category of $G$; objects the orbits, morphisms the $G$-maps |
| $\underline M : \mathcal O_G\to\mathbf{Ab}$ | Coefficient system (contravariant functor) |
| $\underline\pi_n(Y)(G/H)=\pi_n(Y^H)$ | Homotopy coefficient system of the $G$-space $Y$ |
| $C^n_G(X;\underline M)=\prod_{G/H\times D^n}M(G/H)$ | Bredon cochain complex |
| $H^n_G(X;\underline M)$ | Bredon cohomology |
| $G/H\times D^n$, $X^n$ | Equivariant cell and equivariant $n$-skeleton |
| $\mathfrak o(f)\in C^{n+1}_G(X;\underline\pi_n(Y))$ | Obstruction cocycle of the $G$-map $f$ on $X^n$ |
| $[\mathfrak o(f)]\in H^{n+1}_G(X;\underline\pi_n(Y))$ | Obstruction class; vanishing is the extension criterion |
| $\mathfrak d(f,f')\in C^n_G(X;\underline\pi_{n+1}(Y))$ | Difference cocycle of two extensions |
| $k_n\in H^{n+1}_G(Y_{n-1};\underline\pi_n(Y))$ | Bredon $k$-invariant of the equivariant Postnikov tower |
| $[X,Y]_G$ | Equivariant homotopy classes of $G$-maps |

## Further Reading

- Glen E. Bredon, *Equivariant Cohomology Theories* (Lecture Notes in Mathematics 34, Springer, 1967), for the Bredon cohomology and the coefficient systems on the orbit category.
- Glen E. Bredon, *Introduction to Compact Transformation Groups* (Academic Press, 1972), for the equivariant obstruction theory and the extension problem.
- Tammo tom Dieck, *Transformation Groups* (de Gruyter, 1987), for the equivariant obstruction theory, the orbit category and the Postnikov tower.
- Peter May, *Equivariant Homotopy and Cohomology Theory* (CBMS Regional Conference Series 91, 1996), for the modern formulation with Mackey functors and the classification of equivariant maps.
- Stefan Waner, "Equivariant homotopy theory and Milnor's theorem", *Transactions of the American Mathematical Society* 258 (1980), 351–368, for the equivariant Postnikov tower and the $k$-invariants.
- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the ordinary obstruction theory that the equivariant theory extends.
