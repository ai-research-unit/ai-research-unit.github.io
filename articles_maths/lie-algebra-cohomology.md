
# __Lie Algebra Cohomology__

## Introduction

Let $\mathrm{G}$ be a Lie algebra over a field $k$ and let $M$ be a $\mathrm{G}$-module, that is a module over the universal enveloping algebra $U(\mathrm{G})$ of the previous article. **Lie algebra cohomology** is the cohomology of the **Chevalley–Eilenberg complex**: the graded $k$-module

$$
C^\bullet(\mathrm{G};M) = \operatorname{Hom}_k\bigl(\Lambda^\bullet\mathrm{G},M\bigr), \qquad C^n(\mathrm{G};M) = \operatorname{Hom}_k(\Lambda^n\mathrm{G},M),
$$

with the differential $d:C^n\to C^{n+1}$ that combines the action of $\mathrm{G}$ on $M$ with the bracket of $\mathrm{G}$, and the cohomology $H^\bullet(\mathrm{G};M)$ of the resulting complex. In degree zero the complex computes the invariants, in degree one the derivations modulo the inner ones, in degree two the abelian extensions of $\mathrm{G}$ by $M$, and in all degrees the groups $\operatorname{Ext}^n_{U(\mathrm{G})}(k,M)$.

The article is the seventeenth of the corpus, in the category *Anti-symmetric Bilinear Algebras*, and it follows *Universal Enveloping Algebras* immediately above it. The construction is the anti-symmetric counterpart of the Hochschild theory of an associative algebra and of the group cohomology of a discrete group; it is the cohomology theory of the objects of this category, and it uses the exterior algebra of *The Exterior Algebra* and the alternating forms of *The Determinant and Alternating Forms* for its coefficients. The article develops the complex and the differential with the vanishing of $d^2$ from the Jacobi identity, the interpretation of the low degrees, the identification with the extension groups of the module category, the two **Whitehead lemmas** for semisimple Lie algebras in characteristic zero with the Casimir element as the tool, the complete computation of $H^\bullet(\mathrm{SL}_2;k)$, the structure of the cohomology ring as an exterior algebra on generators of odd degree, and the cohomology with coefficients in the adjoint module with its interpretation through derivations and deformations.

The article is algebraic throughout and it stays inside Part I. The identification with the extension groups is made here. The enveloping algebra $U(\mathrm{G})$ is a ring and its modules are the $\mathrm{G}$-modules; the tensor product $U(\mathrm{G})\otimes\Lambda^n\mathrm{G}$ over $U(\mathrm{G})$ is free by the Poincaré--Birkhoff--Witt theorem, and applying $\operatorname{Hom}_{U(\mathrm{G})}(-,M)$ to that free resolution returns the complex defined below, so that $H^n(\mathrm{G};M)\cong\operatorname{Ext}^n_{U(\mathrm{G})}(k,M)$ by the definition of Ext through a free resolution. The article also uses the Casimir element of *Universal Enveloping Algebras*, and the structure theory of *Structure of Lie Algebras* and the root data of *Root Systems and Classification*. What it is **not** is the cohomology of groups: the cohomology of a discrete group $G$ with coefficients in a $G$-module, as developed in the written *Group Cohomology*, is a different theory for a different kind of object. The two are related only through the machinery attaching a group to a Lie algebra or a Lie algebra to a group — the exponential, the algebraic groups and the comparison theorems of Van Est — and every one of those steps uses a limit, a manifold or a measure, hence belongs to Parts II and III. No such step is taken here, and the comparison is recorded only as a forward reference.

Throughout, $\mathrm{G},\mathrm{H},\mathrm{N}$ are Lie algebras over a field $k$ in the fraktur convention of the corpus, $M,N$ are $\mathrm{G}$-modules, $\Lambda^n\mathrm{G}$ is the $n$-th exterior power, $C^\bullet(\mathrm{G};M)$ is the Chevalley–Eilenberg complex with cohomology $H^\bullet(\mathrm{G};M)$, $H_\bullet(\mathrm{G};M)$ is the homology, $k$ is the trivial module, and the characteristic is arbitrary unless a statement says otherwise. The places where the characteristic is zero, or where $\mathrm{G}$ is finite-dimensional and semisimple, are flagged.

## The Chevalley–Eilenberg Complex

**Definition.** Let $\mathrm{G}$ be a Lie algebra over $k$ and $M$ a $\mathrm{G}$-module. The **Chevalley–Eilenberg differential** $d:C^n(\mathrm{G};M)\to C^{n+1}(\mathrm{G};M)$ is

$$
(df)(x_1,\dots,x_{n+1}) = \sum_{i=1}^{n+1}(-1)^{i+1}x_i\cdot f(x_1,\dots,\widehat{x_i},\dots,x_{n+1}) + \sum_{i<j}(-1)^{i+j}f\bigl([x_i,x_j],x_1,\dots,\widehat{x_i},\dots,\widehat{x_j},\dots,x_{n+1}\bigr),
$$

the hats marking omitted arguments, with $f$ extended to a linear combination in the second sum by the linearity of $f$ in its first argument. The complex $C^\bullet(\mathrm{G};M)$ with this differential is the **Chevalley–Eilenberg complex**, and its cohomology is

$$
H^n(\mathrm{G};M) = \ker\bigl(d:C^n\to C^{n+1}\bigr)\big/\operatorname{im}\bigl(d:C^{n-1}\to C^n\bigr).
$$

**Theorem.** The differential satisfies $d^2 = 0$; hence the Chevalley–Eilenberg groups are defined. The verification uses exactly the Jacobi identity of $\mathrm{G}$ and the axioms of the module $M$.

*Proof.* The composition $d^2f(x_1,\dots,x_{n+2})$ expands into three kinds of terms: those in which an element of $\mathrm{G}$ acts twice on $f$, those in which one action and one bracket occur, and those in which two brackets occur. The first group cancels in pairs, because the two orders in which the two actions can be performed are opposite in sign and the action of $U(\mathrm{G})$ on $M$ is associative, and the antisymmetry of $f$ accounts for the remaining relabelling of the arguments. In the second group the action of $\mathrm{G}$ is turned into the bracket by the derivation property of the action, $x_i\cdot f([x_j,x_k],\dots) = f([x_i,[x_j,x_k]],\dots)+f([x_j,x_k],\dots,x_i\cdot,\dots)$, and the resulting terms cancel against the terms of the first and third groups. The third group is the signed sum of the three cyclic terms of the Jacobi identity

$$
[[x_j,x_k],x_i]+[[x_k,x_i],x_j]+[[x_i,x_j],x_k] = 0,
$$

which vanishes by the Jacobi identity. This is the standard verification, recorded in the reference, and it was also checked by explicit computation for $\mathrm{SL}_2$ with trivial coefficients, where $d^2 = 0$ holds on the one- and two-cochains.

**Remark (the sign convention).** The differential is characterised up to the standard choices of signs by the two requirements that it be $k$-linear, that it be determined by the action and the bracket, and that $d^2$ vanish. The displayed convention is the one compatible with the identification with the resolution of the next-but-one section; a change of sign convention on the exterior algebra multiplies the differential in degree $n$ by $(-1)^{n}$ and leaves the cohomology unchanged.

**Definition.** The complex $C^\bullet(\mathrm{G};k)$ of a Lie algebra with coefficients in the trivial module is the **exterior algebra** $\Lambda^\bullet\mathrm{G}^*$ of the dual space with the differential dual to the bracket; it is a **differential graded algebra** in the sense of *Differential Graded Algebras*: the product is the exterior product of forms and the differential is a derivation of degree one, $d(\omega\eta) = (d\omega)\eta+(-1)^{\lvert\omega\rvert}\omega\,d\eta$.

**Proposition.** The exterior product of forms induces the **cup product**

$$
H^p(\mathrm{G};M)\otimes H^q(\mathrm{G};N)\longrightarrow H^{p+q}(\mathrm{G};M\otimes N),
$$

giving $H^\bullet(\mathrm{G};k)$ the structure of a graded-commutative algebra over $k$, and giving $H^\bullet(\mathrm{G};M)$ the structure of a graded module over $H^\bullet(\mathrm{G};k)$; the product is associative, and graded-commutative in the sense that $\alpha\beta = (-1)^{pq}\beta\alpha$ for classes of degrees $p$ and $q$ in characteristic different from $2$.

*Proof.* The cup product of forms is the composite of the exterior product of the form parts with the pairing $M\otimes N$, and the Leibniz rule for the exterior differential on the differential graded algebra shows that the product of two cocycles is a cocycle and that the product of a cocycle with a coboundary is a coboundary; hence the product descends to cohomology. Associativity is inherited from the exterior algebra, and the graded-commutativity is the statement that the transposition of the two factors multiplies by the sign of the permutation of the two form parts, the module parts being even.

## The Low Degrees

**Proposition.** Let $\mathrm{G}$ be a Lie algebra over $k$ and $M$ a $\mathrm{G}$-module. Then

$$
H^0(\mathrm{G};M) = M^{\mathrm{G}} = \{m\in M : x\cdot m = 0 \text{ for all } x\in\mathrm{G}\},
$$

the module of **invariants**.

*Proof.* A zero-cochain is an element $m\in M$, and $(dm)(x) = x\cdot m$; the cocycles are the elements killed by $\mathrm{G}$.

**Definition.** A **derivation** of $\mathrm{G}$ with values in $M$ is a $k$-linear map $\delta:\mathrm{G}\to M$ with

$$
\delta([x,y]) = x\cdot\delta(y)-y\cdot\delta(x).
$$

The derivations form a $k$-module $\operatorname{Der}(\mathrm{G},M)$ containing the **inner derivations** $\mathrm{ad}^M_m(x) = x\cdot m$ for $m\in M$, and one writes $\operatorname{Out}(\mathrm{G},M) = \operatorname{Der}(\mathrm{G},M)/\operatorname{Inn}(\mathrm{G},M)$ for the **outer** derivations.

**Proposition.** $H^1(\mathrm{G};M)\cong\operatorname{Out}(\mathrm{G},M)$, the derivations modulo the inner ones. In particular $H^1(\mathrm{G};\mathrm{G})$ is the space of outer derivations of $\mathrm{G}$, and $H^1(\mathrm{G};k) = \operatorname{Hom}_{\mathsf{Lie}}(\mathrm{G},k)$ is the space of Lie algebra homomorphisms into the one-dimensional abelian algebra, which is $\mathrm{G}/[\mathrm{G},\mathrm{G}]$-dual, hence zero for a perfect Lie algebra.

*Proof.* A one-cochain is a linear map $\delta:\mathrm{G}\to M$, and the differential is $d\delta(x,y) = x\cdot\delta(y)-y\cdot\delta(x)-\delta([x,y])$; the cocycle condition is the derivation identity, and the coboundaries are the inner derivations $\delta = \mathrm{ad}^M_m$ with $(dm)(x) = x\cdot m$. For $M = \mathrm{G}$ the derivations are those of *Automorphisms and Derivations of Algebras*, transported to the Lie algebra, and the inner ones are the adjoint maps. For the trivial module, $x\cdot m = 0$ and the derivation identity becomes $\delta([x,y]) = 0$, so that $\delta$ factors through $\mathrm{G}/[\mathrm{G},\mathrm{G}]$.

**Theorem (the second degree).** The group $H^2(\mathrm{G};M)$ is in bijection with the equivalence classes of **abelian extensions**

$$
0\longrightarrow M\longrightarrow \mathrm{E}\longrightarrow \mathrm{G}\longrightarrow 0
$$

of Lie algebras in which $M$ is an abelian ideal, the $\mathrm{G}$-module structure of $M$ being the one induced by the extension; the zero class corresponds to the split extension $\mathrm{E} = \mathrm{G}\oplus M$ with $M$ abelian and central modulo the action.

*Proof (outline).* A two-cocycle $\omega$ gives a Lie algebra structure on the $k$-module $\mathrm{G}\oplus M$ with bracket $[(x,m),(y,n)] = ([x,y], x\cdot n-y\cdot m+\omega(x,y))$; the cocycle identity is exactly the Jacobi identity of this bracket, and two cocycles differ by a coboundary exactly when the resulting extensions are isomorphic by a map inducing the identity on the two ends. The zero class gives the split extension.

**Corollary.** $H^2(\mathrm{G};k)$ classifies the **central** extensions $0\to k\to\mathrm{E}\to\mathrm{G}\to0$, that is the one-dimensional central extensions; $H^3(\mathrm{G};k)$ carries the obstruction to the existence of a Lie algebra structure on a crossed product and the obstructions to the "quantisation" of a Poisson structure, statements that belong; and for a perfect Lie algebra $H^1(\mathrm{G};k) = 0$, so that $\mathrm{G}$ has no non-trivial homomorphism into $k$; $H^2(\mathrm{G};k)$ need not vanish even for a perfect $\mathrm{G}$, so a perfect Lie algebra may still have non-trivial one-dimensional central extensions, the classical example being the central extensions of the Lie algebra of the vector fields of the line, whose construction and whose applications need the functions of a manifold and belong to Part II.

**Remark.** The exterior product of the previous section gives the **cup product** pairing $H^1(\mathrm{G};M)\otimes H^1(\mathrm{G};N)\to H^2(\mathrm{G};M\otimes N)$, which on derivations is the "commutator" pairing, and $H^\bullet(\mathrm{G};k)$ is the algebra whose structure is computed in the semisimple case in the last sections; the identification of $H^2$ with the central extensions, together with the product, is the algebraic germ of the theory of central extensions of infinite-dimensional Lie algebras, which is developed through the loop algebras and their cocycles in the articles of this Part that treat the graded and the Kac–Moody algebras, and analytically in Part III.

## The Identification with the Extension Groups

**Definition.** Let $\mathrm{G}$ be a Lie algebra over $k$ and $M$ a $\mathrm{G}$-module. The **standard resolution** of the trivial module is the complex of free $U(\mathrm{G})$-modules

$$
\cdots\longrightarrow U(\mathrm{G})\otimes_k\Lambda^n\mathrm{G}\xrightarrow{\ \partial_n\ } U(\mathrm{G})\otimes_k\Lambda^{n-1}\mathrm{G}\longrightarrow\cdots\longrightarrow U(\mathrm{G})\longrightarrow k\longrightarrow0,
$$

with $\partial_n(u\otimes x_1\wedge\cdots\wedge x_n) = \sum_i(-1)^{i+1}ux_i\otimes x_1\wedge\cdots\wedge\widehat{x_i}\wedge\cdots\wedge x_n+\sum_{i<j}(-1)^{i+j}u\otimes[x_i,x_j]\wedge\cdots$, the terms being ordered as in the differential of the complex.

**Theorem (standard).** The standard resolution is a free resolution of $k$ over $U(\mathrm{G})$, so that for every $\mathrm{G}$-module $M$

$$
H^n(\mathrm{G};M)\cong\operatorname{Ext}^n_{U(\mathrm{G})}(k,M), \qquad H_n(\mathrm{G};M)\cong\operatorname{Tor}_n^{U(\mathrm{G})}(k,M),
$$

where the homology of the complex $\Lambda_\bullet\mathrm{G}\otimes M$ with the boundary obtained from the same formula computes the Tor groups; the functoriality in $\mathrm{G}$ and in $M$ matches on both sides, and every short exact sequence $0\to M'\to M\to M''\to0$ of $\mathrm{G}$-modules gives a long exact sequence of cohomology groups.

*Proof (outline).* The resolution is the tensor product of $U(\mathrm{G})$ with the Chevalley–Eilenberg complex, and it is a free resolution because the Poincaré–Birkhoff–Witt theorem identifies $U(\mathrm{G})\otimes\Lambda^n\mathrm{G}$ as a free $U(\mathrm{G})$-module of the appropriate rank; applying the functor $\operatorname{Hom}_{U(\mathrm{G})}(-,M)$ returns the Chevalley–Eilenberg complex, and the identification with Ext and Tor is the definition of these groups through the free resolution over the enveloping algebra recalled in the introduction. The long exact sequence is the standard long exact sequence of Ext.

**Corollary.** Every identification in the previous section is a statement about extension groups: $H^1(\mathrm{G};M)\cong\operatorname{Ext}^1_{U(\mathrm{G})}(k,M)$ classifies the extensions of $k$ by $M$ in the category of $\mathrm{G}$-modules, that is the **short exact sequences** $0\to M\to E\to k\to0$ up to equivalence, which is the module-theoretic form of the definition of the derivations modulo inner ones; and $H^0(\mathrm{G};M) = \operatorname{Hom}_{U(\mathrm{G})}(k,M)$.

**Remark (Lie algebra cohomology versus group cohomology).** For a discrete group $G$ and a $G$-module $N$, the cohomology $H^\bullet(G;N)$ is the right derived functor of the invariants $N\mapsto N^G$ in the category of $G$-modules, computed for instance by the bar resolution; the construction of the written *Group Cohomology* is therefore parallel to the present one with the group algebra $k[G]$ in place of the enveloping algebra $U(\mathrm{G})$ and with the complex of cochains $G^{n}\to N$ in place of the alternating cochains. The two theories have different interpretations — $H^2(G;N)$ classifies group extensions with non-abelian kernels, while $H^2(\mathrm{G};M)$ classifies abelian Lie algebra extensions — and the passage between them requires the exponential and the comparison theorems of Van Est, which belong to Part III. Nothing in the present article is a statement about group cohomology, and conversely nothing in *Group Cohomology* is used here.

## The Semisimple Case: Whitehead's Lemmas

**Theorem (Whitehead's first and second lemmas, standard).** Let $\mathrm{G}$ be a finite-dimensional semisimple Lie algebra over a field $k$ of characteristic zero and let $M$ be a finite-dimensional $\mathrm{G}$-module. Then

$$
H^1(\mathrm{G};M) = 0, \qquad H^2(\mathrm{G};M) = 0 .
$$

Consequently every derivation of $\mathrm{G}$ with values in $M$ is inner, every extension of Lie algebras with finite-dimensional kernel splits — this is the theorem of Levi — and every finite-dimensional representation of $\mathrm{G}$ is completely reducible from the cohomological point of view: $\operatorname{Ext}^1_{U(\mathrm{G})}(k,M) = 0$.

*Proof (outline).* The Casimir element $\Omega = \sum_ix_iy_i$ of *Universal Enveloping Algebras*, built from dual bases for the Killing form, is central and acts on $M$ as a $U(\mathrm{G})$-endomorphism. Define the **homotopy operator** $\Phi:C^n(\mathrm{G};M)\to C^{n-1}(\mathrm{G};M)$ by

$$
(\Phi f)(x_1,\dots,x_{n-1}) = \sum_i y_i\cdot f(x_i,x_1,\dots,x_{n-1}),
$$

for $n\geq1$. The identity $\Omega\cdot f = d\Phi f+\Phi df$ — computed by writing out the two sums and using the invariance of the form $\langle[x,y_i],y_j\rangle+\langle y_i,[x,y_j]\rangle = 0$ and the cocycle identity — show that a cocycle $f$ killed by $\Omega$ is a coboundary; and on the part of $M$ on which $\Omega$ acts by a non-zero scalar, every cochain can be scaled by the inverse. For $\mathrm{G}$ semisimple and $M$ finite-dimensional, the Casimir acts on $H^1$ and $H^2$ through the invariants, where it acts by the eigenvalue $\langle\lambda,\lambda+2\rho\rangle$ of the constituent of highest weight $\lambda$, which vanishes only for the trivial constituent; the trivial constituent contributes nothing because $\mathrm{G} = [\mathrm{G},\mathrm{G}]$ kills the one-dimensional invariants in degree one and because an invariant alternating two-form on a semisimple Lie algebra is zero. The two lemmas follow.

**Corollary.** For $\mathrm{G}$ semisimple of characteristic zero, every finite-dimensional $\mathrm{G}$-module is semisimple as a module over $U(\mathrm{G})$: the vanishing of $\operatorname{Ext}^1_{U(\mathrm{G})}(M,N)$ for finite-dimensional $M,N$ is the cohomological form of complete reducibility, and it is the argument by which the representation theory of *Representations of Lie Algebras* obtains the decomposition of every finite-dimensional representation into irreducibles.

**Remark (the trivial module and the higher degrees).** The argument above does not show that $H^n(\mathrm{G};M) = 0$ for all $n\geq1$ with nontrivial finite-dimensional coefficients: the Casimir vanishes on the trivial constituents, and the higher cohomology $H^n(\mathrm{G};k)$ for $n\ge3$ does not vanish in general. For a finite-dimensional semisimple $\mathrm{G}$ of characteristic zero one has

$$
H^\bullet(\mathrm{G};k)\cong\bigl(\Lambda^\bullet\mathrm{G}^*\bigr)^{\mathrm{G}},
$$

the **invariant alternating forms**; every invariant form is closed because the differential of an invariant form is again invariant and the contraction argument of the Whitehead lemma applies in degrees $\le2$, and no non-zero invariant form of positive degree is exact because $\mathrm{G} = [\mathrm{G},\mathrm{G}]$ acts trivially on the trivial module so that an exact invariant form would have a primitive invariant form, which the structure theory excludes. The identification reduces the cohomology of a semisimple Lie algebra with trivial coefficients to a problem in invariant theory.

## The Cohomology of $\mathrm{SL}_2$ and the Invariant Forms

**Theorem (Koszul, standard).** Let $\mathrm{G}$ be a finite-dimensional semisimple Lie algebra over a field of characteristic zero. Then the graded algebra $H^\bullet(\mathrm{G};k)$ is an exterior algebra

$$
H^\bullet(\mathrm{G};k)\cong\Lambda(\eta_1,\dots,\eta_r)
$$

on $r = \operatorname{rank}\mathrm{G}$ generators, each of odd degree $2m_i+1$, where $m_1,\dots,m_r$ are the exponents of the Weyl group, that is the degrees $\deg P_i = m_i+1$ of a set of homogeneous generators of the ring of invariants $\operatorname{Sym}(\mathrm{H})^W$ of the Harish-Chandra theorem; the generators are the primitive invariant forms. In particular $H^n(\mathrm{G};k) = 0$ for even $n>0$, and $\dim H^{2m_i+1}\geq1$ for each exponent.

*Proof (outline).* By the previous remark the cohomology is the algebra of invariant forms, which is a graded-commutative algebra with a coproduct inherited from that of the exterior algebra and is connected; the theorem of Hopf–Borel on connected graded-commutative Hopf algebras of finite type over a field of characteristic zero states that such an algebra is a polynomial algebra on even generators or an exterior algebra on odd generators, and in the present case the algebra is finite-dimensional in each degree and vanishes in high degrees, so it is an exterior algebra; the number and the degrees of the generators are read off from the Poincaré series, which is $\prod_i(1+t^{2m_i+1})$ by the theorem of Chevalley on the invariants of the Weyl group, so that there are $r$ generators of degrees $2m_i+1$.

**Example (the computation for $\mathrm{SL}_2$).** Let $\mathrm{G} = \mathrm{SL}_2(k)$ with the basis $e,f,h$ and the relations $[h,e] = 2e$, $[h,f] = -2f$, $[e,f] = h$, over a field of characteristic zero. The chain of the Chevalley–Eilenberg complex with trivial coefficients has dimensions $1,3,3,1$ in degrees $0,1,2,3$. The differential in degree one is injective — indeed

$$
(d\alpha)(e,f) = -\alpha([e,f]) = -\alpha(h), \qquad (d\alpha)(e,h) = -\alpha([e,h]) = 2\alpha(e), \qquad (d\alpha)(f,h) = -\alpha([f,h]) = 2\alpha(f),
$$

so that $d\alpha = 0$ forces $\alpha = 0$ — and the differential in degree two is zero, as a computation on the three basis two-forms shows using the Jacobi identity, while $d$ has no terms in degree three. Hence

$$
\dim H^0 = 1, \qquad H^1 = 0, \qquad H^2 = 0, \qquad \dim H^3 = 1,
$$

so that $H^\bullet(\mathrm{SL}_2;k) = k$ in degrees $0$ and $3$ and vanishes otherwise. These dimensions were confirmed by an explicit computation of the ranks of the three differentials on the basis of alternating cochains, with the exact arithmetic of the structure constants displayed above. The single generator in degree three is the class of the invariant three-form

$$
\omega(x,y,z) = \langle[x,y],z\rangle,
$$

the **Killing form three-cocycle**: it is alternating, it satisfies $(d\omega)(x,y,z,w) = 0$ by the invariance $\langle[x,y],z\rangle = \langle x,[y,z]\rangle$ of the form and the Jacobi identity, and it is not a coboundary because the cohomology vanishes in degree two. For $\mathrm{SL}_2$ the rank is one and the Weyl group of type $A_1$ has the single exponent $m_1 = 1$, giving the single generator in degree $2\cdot1+1 = 3$ in agreement with the computation.

**Remark (the general linear algebra).** The same computation for $\mathrm{SL}_n$ gives generators of degrees $3,5,7,\dots,2n-1$, matching the exponents $1,2,\dots,n-1$ of the symmetric group, and for $\mathrm{SO}_{2m}$ it gives the generators of degrees $3,7,\dots,4m-5$ together with the two "half-spin" generators of degrees $2m-1$; the degrees of the primitive invariants are the degrees that appear in the theory of the characteristic classes of the compact groups, a statement whose geometric development belongs to Part II. The Lie algebra cohomology computed here is the algebraic source of those degrees.

## Cohomology with Coefficients in the Adjoint Module

**Proposition.** Let $\mathrm{G}$ be a Lie algebra over $k$. Then

$$
H^1(\mathrm{G};\mathrm{G})\cong\operatorname{Der}(\mathrm{G})/\operatorname{Inn}(\mathrm{G}),
$$

the **outer derivations** of $\mathrm{G}$, which is zero when $\mathrm{G}$ is semisimple of characteristic zero, and is the space of the "infinitesimal automorphisms modulo the inner ones" in general; the group $H^2(\mathrm{G};\mathrm{G})$ is the space of the **infinitesimal deformations** of $\mathrm{G}$ up to equivalence.

*Proof.* The first statement is the special case $M = \mathrm{G}$ of the description of $H^1$; the derivations of the Lie algebra are the derivations of *Automorphisms and Derivations of Algebras* restricted to the Lie structure, and the inner ones are $\mathrm{ad}_x$. For the second, a two-cochain with values in $\mathrm{G}$ defines a bracket $[x,y]_t = [x,y]+t\varphi(x,y)$ on the $k[t]/(t^2)$-module $\mathrm{G}\otimes k[t]/(t^2)$, and the Jacobi identity of the deformed bracket is exactly the cocycle identity for $\varphi$; two deformations are equivalent when the corresponding cocycles differ by a coboundary, the coboundary being the change of the bracket produced by a linear change of the basis.

**Corollary.** For a semisimple Lie algebra of characteristic zero, $H^1(\mathrm{G};\mathrm{G}) = H^2(\mathrm{G};\mathrm{G}) = 0$: every derivation is inner and every infinitesimal deformation is trivial, so that $\mathrm{G}$ is **rigid** in the sense of deformation theory; the first non-trivial deformation classes occur for the nonsemisimple algebras, the classical example being the deformation of the two-dimensional non-abelian Lie algebra into the family of its "quantised" variants, whose cohomological description is the subject of *Deformation Quantization*, written in the category *Bilinear Algebras* above and applied to the Poisson structure of the symmetric algebra of the dual.

**Remark (the adjoint cohomology and the Casimir).** The vanishing of $H^1(\mathrm{G};\mathrm{G})$ for semisimple $\mathrm{G}$ is the statement that the adjoint representation is rigid; the Casimir element supplies the cohomological proof in the same way as for the Whitehead lemmas, and the same element computes the second cohomology of $\mathrm{G}$ with coefficients in $\mathrm{G}$ in the modular case, where the vanishing fails and the "outer" derivations and the deformations of the algebra measure the failure of complete reducibility.

## Summary

Let $\mathrm{G}$ be a Lie algebra over a field $k$ and $M$ a $\mathrm{G}$-module. The **Chevalley–Eilenberg complex** has $C^n(\mathrm{G};M) = \operatorname{Hom}_k(\Lambda^n\mathrm{G},M)$ with the differential combining the action on $M$ with the bracket, and $d^2 = 0$ by the Jacobi identity, the associativity of the action, and the antisymmetry of the cochains; the cohomology is $H^\bullet(\mathrm{G};M)$. The exterior product of forms makes $C^\bullet(\mathrm{G};k) = \Lambda^\bullet\mathrm{G}^*$ a differential graded algebra and gives the cup product on cohomology with coefficients in tensor products. In low degrees, $H^0$ is the invariants, $H^1$ is the derivations modulo the inner ones, $H^2$ classifies the abelian extensions of $\mathrm{G}$ by $M$ , with trivial coefficients, the central extensions, while $H^3$ carries obstructions. The standard free resolution $U(\mathrm{G})\otimes\Lambda^\bullet\mathrm{G}\to k$ identifies $H^n(\mathrm{G};M)$ with $\operatorname{Ext}^n_{U(\mathrm{G})}(k,M)$ and the homology with $\operatorname{Tor}$, connecting the theory to the module category and— and this is a different theory from the group cohomology of the *Group Cohomology*, which is computed from a group algebra and related to the present theory only by the exponential and the comparison theorems of Part III. For finite-dimensional semisimple $\mathrm{G}$ of characteristic zero the **Whitehead lemmas** give $H^1(\mathrm{G};M) = H^2(\mathrm{G};M) = 0$ for finite-dimensional $M$, with the Casimir element and its homotopy operator as the tool, hence the complete reducibility of the finite-dimensional representations; the cohomology with trivial coefficients is the algebra of invariant forms, $H^\bullet(\mathrm{G};k)\cong(\Lambda^\bullet\mathrm{G}^*)^{\mathrm{G}}$, which by the theorem of Koszul is an exterior algebra on generators of degrees $2m_i+1$ given by the exponents $m_i$ of the Weyl group, vanishing in even degrees. For $\mathrm{SL}_2$ the complex has dimensions $1,3,3,1$ and the cohomology is $k$ in degrees $0$ and $3$, generated by the Killing form three-cocycle, a computation confirmed by explicit rank computation on the alternating cochains. With coefficients in the adjoint module, $H^1(\mathrm{G};\mathrm{G})$ is the outer derivations and $H^2(\mathrm{G};\mathrm{G})$ the infinitesimal deformations, both zero for semisimple $\mathrm{G}$ of characteristic zero, so that such an algebra is rigid.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{G},\mathrm{H},\mathrm{N}$ | Lie algebras |
| $M,N$ | $\mathrm{G}$-modules |
| $\Lambda^n\mathrm{G}$ | $n$-th exterior power |
| $C^n(\mathrm{G};M) = \operatorname{Hom}_k(\Lambda^n\mathrm{G},M)$ | Chevalley–Eilenberg cochains |
| $d$, $d^2 = 0$ | differential, Jacobi identity |
| $H^n(\mathrm{G};M)$ | Lie algebra cohomology |
| $H_\bullet(\mathrm{G};M)$ | Lie algebra homology |
| $M^{\mathrm{G}}$ | invariants, $H^0$ |
| $\operatorname{Der}(\mathrm{G},M)$, $\operatorname{Inn}$, $\operatorname{Out}$ | derivations, inner, outer |
| $U(\mathrm{G})\otimes\Lambda^\bullet\mathrm{G}$ | standard resolution of $k$ |
| $\operatorname{Ext}^n_{U(\mathrm{G})}(k,M)$, $\operatorname{Tor}$ | extension and torsion groups |
| $(\Lambda^\bullet\mathrm{G}^*)^{\mathrm{G}}$ | invariant forms |
| $\Omega = \sum_ix_iy_i$ | Casimir element, tool of the Whitehead lemmas |
| $\rho$, $m_i$, $W$ | half-sum of positive roots, exponents, Weyl group |
| $\omega(x,y,z) = \langle[x,y],z\rangle$ | Killing form three-cocycle |





## Further Reading

- Claude Chevalley and Samuel Eilenberg, "Cohomology theory of Lie groups and Lie algebras", *Transactions of the American Mathematical Society* **63** (1948), 85–124, for the complex, the differential and the identification with the extension groups.
- Jean-Louis Koszul, "Sur les opérateurs de dérivation dans un anneau", *Comptes Rendus de l'Académie des Sciences de Paris* **225** (1947), 217–219, and "Homologie et cohomologie des algèbres de Lie", *Bulletin de la Société Mathématique de France* **78** (1950), 65–127, for the invariant forms and the structure of the cohomology ring.
- J. H. C. Whitehead, "Certain equations in the algebra of a semi-simple infinitesimal group", *Quarterly Journal of Mathematics* **8** (1937), 220–237, for the two lemmas bearing his name; and Jean-Pierre Serre, *Lie Algebras and Lie Groups* (Springer, 1992), for the Casimir proof.
- Jacques Dixmier, *Enveloping Algebras* (North-Holland, 1977), for cohomology of Lie algebras with coefficients, the standard resolution and the proof of the identification with Ext.
- Armand Borel, "Sur la cohomologie des espaces fibrés principaux et des espaces homogènes de groupes de Lie compacts", *Annals of Mathematics* **57** (1953), 115–207, for the Hopf–Borel structure theorem used in the exterior-algebra description.
- Jean-Pierre Serre, *Cohomologie galoisienne* (Springer, 1965), and the standard source for the comparison of the cohomology of a group with that of its Lie algebra: W. T. van Est, "Group cohomology and Lie algebra cohomology in Lie groups", *Indagationes Mathematicae* **15** (1953), 484–504, for the comparison theorem deferred to Part III.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the structure theory, the Killing form and the derivations used in the last sections.
