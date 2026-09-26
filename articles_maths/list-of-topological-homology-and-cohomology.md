
# __List of Topological Homology and Cohomology__

## Introduction

This article lists the homology and cohomology theories of Parts I to III, each with the coefficient system it takes and the article that introduces it. The theories fall into four families: the singular, simplicial and cellular theories of a space, which take coefficients in a commutative ring or a module over it; the de Rham, Dolbeault and Hodge theories of a smooth or complex manifold, which take real or complex coefficients through differential forms; the sheaf and Grothendieck theories, which take coefficients in a sheaf and are defined for a space, a scheme or a site; and the algebraic theories of a group, a Galois extension, a Lie algebra or an algebra, which take coefficients in a module over the group ring, the Galois group, the enveloping algebra or the enveloping algebra of the algebra. The generalised cohomology theories and the duality theorems are listed with them.

Every entry points to the article that introduces the theory or the coefficient system. The article introduces nothing and proves nothing: it records the coefficients the introducing article allows and the degree in which the theory begins, and it neither restates a definition nor gives a proof.

The article records examples and non-examples side by side. Beside the theories that compute the same invariant it lists the pairs that do not agree — the de Rham cohomology, which takes real coefficients and is blind to torsion, so that it misses the $\mathbb{Z}/2$ in $H_1(\mathbb{RP}^2)$; the Čech cohomology, which agrees with sheaf cohomology over a good cover and disagrees with it in general; the Hochschild and cyclic theories, which are related by the Connes sequence and are not equal — each with the failure named and the article that records it.

## The Singular, Simplicial and Cellular Theories

These theories attach a graded module to a space, a pair or a simplicial complex, and their coefficients are a commutative ring $R$ with identity $1 \neq 0$, or a module $G$ over it. The default is $R = \mathbb{Z}$ and the modules are abelian groups.

| Theory | Its coefficients | Introduced in |
|---|---|---|
| simplicial homology $H_n^\Delta(K;R)$ | an $R$-module, $R$ commutative with $1 \neq 0$; the chain groups are free of rank the number of $n$-simplices | *Simplicial and Singular Homology* |
| singular homology $H_n(X;R)$ | an $R$-module; the $n$-chains are formal sums of continuous maps $\Delta_n \to X$ | *Simplicial and Singular Homology* |
| reduced homology $\tilde H_n(X;R)$ | an $R$-module; the augmentation removes the degree-zero class of a point | *Simplicial and Singular Homology* |
| relative homology $H_n(X,A;R)$ | an $R$-module; the long exact sequence of a pair has connecting map $\partial$ | *Simplicial and Singular Homology* |
| cellular homology $H_n^{\mathrm{CW}}(X;R)$ | an $R$-module; agrees with the singular theory on a CW complex | *CW Complexes and Cellular Approximation* |
| singular cohomology $H^n(X;G)$ | an $R$-module $G$; contravariant in $X$, with the universal coefficient sequence and the Bockstein | *Cohomology and the Universal Coefficient Theorem* |
| the cohomology ring $H^*(X;R)$ | a commutative ring $R$; the cup product makes the direct sum a graded-commutative ring | *Cup and Cap Products* |
| homology and cohomology with local coefficients | a local system, that is a representation of $\pi_1(X)$ | *Poincaré Duality*; *The Leray–Serre Spectral Sequence* |
| the Künneth and cross products | a commutative ring $R$, with a $\operatorname{Tor}$ correction over a general ring | *Cup and Cap Products* |
| the Bockstein homomorphism $\beta_m$ | the coefficient sequence $0 \to \mathbb{Z} \to \mathbb{Z} \to \mathbb{Z}/m \to 0$ | *Cohomology and the Universal Coefficient Theorem* |
| the Euler characteristic $\chi(X)$ | integral; the alternating sum of the ranks of $H_n(X;\mathbb{Z})$ | *Simplicial and Singular Homology* |
| Alexander duality | integral coefficients; the duality of a compact subset of $S^n$ with its complement | *Degree Theory and the Brouwer Fixed Point Theorem* |

## The de Rham, Dolbeault and Hodge Theories

The theories of a manifold take their coefficients from the differential forms, so the coefficient field is $\mathbb{R}$ or $\mathbb{C}$ and the torsion of the integral theory is invisible.

| Theory | Its coefficients | Introduced in |
|---|---|---|
| de Rham cohomology $H^\bullet_{dR}(M)$ | real coefficients, through the differential forms; $H^\bullet_{dR}(M) \cong H^\bullet(M;\mathbb{R})$ for a smooth manifold | *Sheaves and the de Rham Complex* |
| the de Rham complex as a resolution | the constant sheaf $\underline{\mathbb{R}}$; the Poincaré lemma makes the complex a resolution, so sheaf cohomology computes de Rham cohomology | *Sheaf Cohomology*; *Sheaves and the de Rham Complex* |
| Stokes' theorem and the de Rham pairing | real coefficients; the integration of an $n$-form over an $n$-cycle | *Differential Forms and Stokes' Theorem* |
| Dolbeault cohomology $H^{p,q}_{\bar\partial}(M)$ | complex coefficients; the $\bar\partial$-closed $(p,q)$-forms modulo the $\bar\partial$-exact ones | *Sheaves and the de Rham Complex*; *Several Complex Variables* |
| the Hodge decomposition | complex coefficients on a compact Kähler manifold; $H^k(M;\mathbb{C}) = \bigoplus_{p+q=k}H^{p,q}$ | *Kähler Geometry*; *Sheaves and the de Rham Complex* |
| the Hodge theorem | real coefficients; each de Rham class has a unique harmonic representative | *Differential Forms and Stokes' Theorem*; *Kähler Geometry* |
| the de Rham theorem | the comparison of the smooth theory with the singular one, over $\mathbb{R}$ | *Sheaves and the de Rham Complex* |
| the Dolbeault theorem | the identification of $H^{p,q}_{\bar\partial}$ with the sheaf cohomology $H^q(M,\Omega^p)$ | *Sheaves and the de Rham Complex*; *Coherent Sheaves* |

## The Sheaf and Grothendieck Theories

A sheaf cohomology theory takes its coefficients in a sheaf of abelian groups on a space, a scheme or a site; the groups are the right derived functors of the global-section functor, and the coefficients range from the constant sheaf to the coherent, the étale and the constructible.

| Theory | Its coefficients | Introduced in |
|---|---|---|
| sheaf cohomology $H^i(X,\mathcal{F})$ | a sheaf of abelian groups $\mathcal{F}$; $H^0$ is the global sections, and flabby and soft resolutions compute | *Sheaf Cohomology* |
| the comparison with singular cohomology | the constant sheaf $\underline{A}$ on a locally contractible paracompact space; $H^i(X,\underline{A}) \cong H^i(X;A)$ | *Sheaf Cohomology* |
| cohomology with support | a family $\Phi$ of supports, in particular the compact supports $H^i_c$ | *Sheaf Cohomology* |
| higher direct images and the Leray spectral sequence | a sheaf $\mathcal{F}$ and a map $f$; $E_2^{p,q} = H^p(Y,R^qf_*\mathcal{F})$ | *Sheaf Cohomology*; *The Leray–Serre Spectral Sequence* |
| Čech cohomology $\check H^p(X,\mathcal{F})$ | a sheaf $\mathcal{F}$; agrees with sheaf cohomology over a good cover by the Leray theorem | *Čech Cohomology* |
| coherent sheaf cohomology $H^i(X,\mathcal{F})$ | a coherent $\mathcal{O}_X$-module on a scheme or a complex manifold | *Coherent Sheaves*; *Sheaves in Algebraic Geometry* |
| Serre duality | a coherent sheaf on a smooth projective variety; $H^i(X,\mathcal{F}) \cong H^{n-i}(X,\mathcal{F}^\vee\otimes\omega_X)^\vee$ | *Coherent Sheaves*; *Sheaves in Algebraic Geometry* |
| sheaf cohomology on a site, and étale cohomology | a sheaf on a Grothendieck site; the étale site of a scheme with coefficients in a sheaf of abelian groups | *Sheaves on Sites*; *Schemes* |
| the derived functors of a left exact functor | an abelian category with enough injectives; $R^iF$ with the long exact sequence | *Derived Functors*; *Derived Categories* |
| the Grothendieck spectral sequence | the composite of two derived functors; $E_2^{p,q} = R^pG(R^qF(A))$ | *Spectral Sequences* |
| the Čech-to-derived spectral sequence | a sheaf and its presheaf of cohomology; converges to the sheaf cohomology | *Čech Cohomology* |

## The Algebraic Theories: Groups, Galois, Lie and Hochschild

These theories attach a graded module to an algebraic object, and the coefficients are modules over the group ring, the Galois group, the universal enveloping algebra, the algebra or the enveloping algebra of the algebra.

| Theory | Its coefficients | Introduced in |
|---|---|---|
| group cohomology $H^n(G,M)$ | a $G$-module $M$, equivalently a module over the group ring $\mathbb{Z}[G]$ | *Group Cohomology* |
| group homology $H_n(G,M)$ | a $G$-module; $H_1(G,\mathbb{Z}) = G^{\mathrm{ab}}$ and $M(G) = H_2(G,\mathbb{Z})$ is the Schur multiplier | *Group Cohomology* |
| Tate cohomology $\hat H^n(G,M)$ | a $G$-module for a finite group $G$; defined in all degrees $n \in \mathbb{Z}$ | *Group Cohomology* |
| the classification of group extensions | an abelian group $M$; $H^2(G,M)$ is the extension classes | *Group Cohomology* |
| group cohomology through a classifying space | a $G$-module, through $H^*(G;M) \cong H^*(BG;M)$ | *Classifying Spaces and Cohomology Operations* |
| Galois cohomology $H^n(K,A)$ | a Galois module $A$: $\mu_n$, $\overline K^\times$, $\mathbb{Z}/n$, with the action of $G_K$ | *Galois Cohomology* |
| the Brauer group as a second cohomology | $H^2(K,\overline K^\times)$; the $n$-torsion ${}_n\operatorname{Br}(K)$ | *Galois Cohomology*; *Central Simple Algebras and the Brauer Group* |
| Lie algebra cohomology $H^\bullet(\mathfrak{g};M)$ | a $\mathfrak{g}$-module $M$, equivalently a module over $U(\mathfrak{g})$; the Chevalley–Eilenberg complex | *Lie Algebra Cohomology* |
| Hochschild homology and cohomology $HH_\bullet(A,M)$ | an $A$-bimodule $M$, equivalently a module over $A^{\mathrm{e}} = A\otimes_kA^{\mathrm{op}}$ | *Hochschild Homology* |
| Hochschild–Kostant–Rosenberg | the identification of $HH_\bullet(A)$ with the Kähler differential forms for a smooth commutative algebra | *Hochschild Homology* |
| cyclic homology $HC_\bullet(A)$ | an algebra $A$ over a commutative ring, with a cyclic structure on the Hochschild complex | *Cyclic Homology* |
| cyclic cohomology $HC^\bullet(A)$ | an algebra over a field of characteristic zero; the dual complex, pairing with the $K$-theory | *Cyclic Cohomology* |
| the Dennis trace and the Chern character | the maps $K_n(R) \to HH_n(R)$ and to cyclic homology | *Cyclic Homology* |
| the $\operatorname{Ext}$ and $\operatorname{Tor}$ families | $R$-modules; the universal coefficient and Künneth corrections | *Ext and Tor* |
| algebraic $K$-theory | the $K$-theory of a ring; coefficients in the category of projective modules | *K-Theory of Rings* |

## The Generalised Cohomology Theories and the Dualities

A generalised cohomology theory is a graded functor on spaces that satisfies the Eilenberg–Steenrod axioms except the dimension axiom; the corpus's examples take their coefficients in vector bundles, in spectra or in analytic data, and the duality theorems are the pairings that organise the coefficients.

| Theory | Its coefficients | Introduced in |
|---|---|---|
| topological $K$-theory $K^*(X)$ | real or complex vector bundles, equivalently finitely generated projective modules over $C(X)$ | *Topological K-Theory* |
| the Atiyah–Singer index theorem | the $K$-theory of the symbol and the index pairing; the topological index equals the analytic one | *The Atiyah–Singer Index Theorem and K-Theory* |
| $K$-theory of operator algebras | the projection classes of a $\mathrm{C}^*$-algebra in $K_0$ and the unitaries in $K_1$ | *K-Theory of Operator Algebras* |
| $KK$-theory | the Kasparov bimodules; the bivariant theory whose $KK(A,B)$ classifies the extensions | *KK-Theory* |
| higher algebraic $K$-theory | the Quillen $K$-groups of an exact category; coefficients in the category of modules | *Higher Algebraic K-Theory* |
| cohomology operations and the Steenrod algebra | $\mathbb{Z}/2$ and $\mathbb{Z}/p$ coefficients; the algebra of stable operations | *Classifying Spaces and Cohomology Operations* |
| cobordism | the bordism classes of manifolds, with the Thom spectrum coefficients | *Cobordism and Surgery Theory* |
| Floer homology | analytic coefficients, through the moduli spaces of trajectories; the homology of an infinite-dimensional Morse theory | *Floer Homology* |
| Poincaré duality | a fundamental class over $\mathbb{Z}$ for a closed orientable manifold, and over $\mathbb{Z}/2$ in general | *Poincaré Duality* |
| Lefschetz and Poincaré–Lefschetz duality | a compact manifold with boundary and the cohomology with compact supports | *Poincaré Duality* |
| the homology of a Lie group and its homogeneous spaces | the classifying-space coefficients, through the Leray–Serre spectral sequence | *Homology of Classical Groups and Homogeneous Spaces* |

## The Coefficients

The coefficient system is the part of the theory that the article introducing the theory fixes, and the same letters appear in different theories with different meanings. The table collects the principal coefficients and the theory each serves.

| Coefficient system | The theory it serves | Introduced in |
|---|---|---|
| a commutative ring $R$ with $1 \neq 0$ | simplicial, singular, cellular homology and cohomology; the default is $\mathbb{Z}$ | *Simplicial and Singular Homology* |
| an $R$-module $G$ | singular cohomology, through $\operatorname{Hom}_R$; the universal coefficient theorem | *Cohomology and the Universal Coefficient Theorem* |
| $\mathbb{Z}$, $\mathbb{Z}/m$ | the integral theories and the Bockstein; the torsion of the coefficient group | *Cohomology and the Universal Coefficient Theorem* |
| $\mathbb{Z}/2$ | characteristic classes, Steenrod operations and the unoriented cobordism | *Classifying Spaces and Cohomology Operations* |
| $\mathbb{R}$ | de Rham cohomology and the de Rham theorem; torsion is invisible | *Sheaves and the de Rham Complex* |
| $\mathbb{C}$ | Dolbeault cohomology and the Hodge decomposition of a Kähler manifold | *Several Complex Variables* |
| a local system | homology and cohomology with local coefficients, through $\pi_1$ | *Poincaré Duality* |
| a sheaf of abelian groups | sheaf cohomology, with the comma convention $H^i(X,\mathcal{F})$ | *Sheaf Cohomology* |
| a coherent $\mathcal{O}_X$-module | coherent sheaf cohomology and Serre duality | *Coherent Sheaves* |
| a $G$-module, or a $\mathbb{Z}[G]$-module | group cohomology and homology | *Group Cohomology* |
| a Galois module, such as $\mu_n$ or $\overline K^\times$ | Galois cohomology and the Brauer group | *Galois Cohomology* |
| a $\mathfrak{g}$-module | Lie algebra cohomology, through the universal enveloping algebra | *Lie Algebra Cohomology* |
| an $A$-bimodule | Hochschild homology and cohomology | *Hochschild Homology* |
| a vector bundle | topological $K$-theory | *Topological K-Theory* |

## Non-examples and Warnings

The failures of agreement are recorded beside the theories, since the reader who expects one theorem of comparison must find where it fails.

| Object | Why the expected statement fails | Introduced in |
|---|---|---|
| $H_1(\mathbb{RP}^2;\mathbb{Z}) = \mathbb{Z}/2$ | the torsion is invisible to de Rham cohomology, which takes real coefficients; the de Rham theorem sees only $H^\bullet(M;\mathbb{R})$ | *Sheaves and the de Rham Complex* |
| the non-abelian fundamental group $\pi_1(X,x)$ | there is no homology or cohomology with coefficients in a non-abelian group; $H_1$ is the abelianisation, and the description of $\pi_1$ is of *The Fundamental Group and Covering Spaces* | *Simplicial and Singular Homology* |
| Čech cohomology in general | it agrees with sheaf cohomology over a good cover and over a paracompact space, and it is only an approximation in general; the Leray theorem names the hypothesis | *Čech Cohomology* |
| singular cohomology of the constant sheaf | the comparison $H^i(X,\underline{A}) \cong H^i(X;A)$ needs the space locally contractible and paracompact; the proof is by a flabby resolution | *Sheaf Cohomology* |
| group cohomology versus Lie algebra cohomology | the two are different theories; Van Est's comparison requires the exponential, a manifold and a limit, and belongs to Parts II and III | *Lie Algebra Cohomology* |
| Hochschild homology versus cyclic homology | the two are related by the Connes $SBI$ sequence and are not equal; the cyclic theory remembers the cyclic symmetry of the Hochschild complex | *Cyclic Homology* |
| Tate cohomology for an infinite group | it is defined only for a finite group; for an infinite group the norm map has no meaning | *Group Cohomology* |
| Floer homology | an infinite-dimensional homology whose definition uses the analytic moduli spaces of Part III; it is named here with its coefficients and not computed | *Floer Homology* |

Objects that a reader may expect to find in a list of homology and cohomology theories, and does not.

| Object | Why it is not listed | Introduced in |
|---|---|---|
| Borel–Moore homology | the corpus does not introduce it; the cohomology with compact supports $H^i_c$ is the form in which it meets the compactly supported theory | *Sheaf Cohomology* |
| Deligne cohomology | not introduced; the Hodge-theoretic combination of the de Rham and integral theories is not one of the corpus's theories | *Sheaves and the de Rham Complex* |
| intersection cohomology | not introduced as such; it appears only as a name in the Hecke-theoretic literature | *Hecke Algebras* |
| crystalline cohomology | recorded with the divided-power constructions of the algebraic geometry and not as a theory of this list | *Divided Powers* |
| étale cohomology as a topological theory | it is a sheaf cohomology on the étale site of a scheme and is listed with the sheaf theories | *Schemes*; *Sheaves on Sites* |
| Morse homology | the corpus reaches it through Floer homology and does not introduce the finite-dimensional Morse theory | *Floer Homology* |
| orbifold and equivariant cohomology | the corpus treats the equivariant theories through the classifying spaces and the group cohomology | *Classifying Spaces and Cohomology Operations* |

## Summary

This article has listed the homology and cohomology theories of the corpus with their coefficients: the simplicial, singular and cellular theories with coefficients in a ring or a module; the de Rham, Dolbeault and Hodge theories with real or complex coefficients; the sheaf, Čech, coherent, étale and derived-functor theories with coefficients in a sheaf on a space, a scheme or a site; the group, Galois, Lie algebra, Hochschild and cyclic theories with coefficients in a module over the appropriate algebra; and the generalised theories of $K$-theory, cobordism and Floer homology, together with the duality theorems of Poincaré, Lefschetz, Serre and Alexander. Beside the theories that agree stand the pairs that do not: de Rham cohomology blind to torsion, Čech cohomology agreeing with the derived theory only under the Leray hypothesis, and the Hochschild and cyclic theories separated by the Connes sequence. The list introduces and proves nothing; it is the index of the (co)homology theories of the corpus.

## Summary of Notation

A catalogue denotes its objects by name rather than by symbol. The symbols that appear in the tables are the following.

| Symbol | Meaning |
|---|---|
| $H_n(X;R)$, $H^n(X;G)$ | singular homology and cohomology; the semicolon separates the space from the coefficient |
| $H^i(X,\mathcal{F})$ | sheaf cohomology; the comma is the convention of *Sheaf Cohomology*, deliberately distinct from the semicolon |
| $\check H^p$ | Čech cohomology, with the check |
| $\tilde H_n$, $\tilde H^n$ | reduced homology and cohomology |
| $\partial$, $\delta$ | the boundary and the coboundary |
| $\smile$, $\frown$ | the cup and cap products |
| $\chi(X)$ | the Euler characteristic |
| $[M] \in H_n(M;\mathbb{Z})$ | the fundamental class of a closed orientable manifold |
| $H^i_c$ | cohomology with compact supports |
| $R$, $G$, $M$, $A$ | a commutative coefficient ring with $1 \neq 0$; an $R$-module; a module of coefficients; a coefficient group or algebra |
| $\mathbb{Z}[G]$ | the group ring of $G$ |
| $A^{\mathrm{e}} = A\otimes_kA^{\mathrm{op}}$ | the enveloping algebra of an algebra $A$ |
| $U(\mathfrak{g})$ | the universal enveloping algebra of a Lie algebra |
| $H^n(G,M)$, $H^n(K,A)$, $H^\bullet(\mathfrak{g};M)$, $HH_\bullet(A,M)$ | group, Galois, Lie algebra and Hochschild theories |
| $HC_\bullet(A)$, $HC^\bullet(A)$ | cyclic homology and cyclic cohomology |
| $K^*(X)$, $K_*(A)$ | topological $K$-theory; the $K$-theory of an operator algebra or a ring |
| $\beta_m$ | the Bockstein homomorphism of the coefficient sequence $0 \to \mathbb{Z} \to \mathbb{Z} \to \mathbb{Z}/m \to 0$ |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the singular, simplicial and cellular theories, the universal coefficient theorem and Poincaré duality.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the de Rham theory, the Čech–de Rham complex and the spectral sequences of a fibration.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for the derived functors, Ext and Tor, the spectral sequences and the algebraic theories of groups and Lie algebras.
- Joseph Bernstein and Valery Lunts, *Equivariant Sheaves and Functors* (Springer, 1994), for the sheaf-theoretic cohomology, the higher direct images and the derived categories used with them.
