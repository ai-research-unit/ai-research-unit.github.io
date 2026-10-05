
# __Galois Descent for Sheaves__

## Introduction

**Galois descent** is the descent of the objects over a base-changed space along a Galois extension of the base field. Let $K/k$ be a finite Galois extension with group $\Gamma=\operatorname{Gal}(K/k)$, let $X$ be a space or a scheme over $k$, and let $X_K=X\times_kK$ be the base change; a sheaf of $\mathcal{O}_{X_K}$-modules that carries a **semilinear action of $\Gamma$** — an action covering the action of $\Gamma$ on the second factor of the base change — is the same as a sheaf of $\mathcal{O}_X$-modules: the action of $\Gamma$ is the **descent datum**, the sheaf over $X$ is recovered as the **fixed part**, and under the faithful flatness of $K$ over $k$ the descent is **effective**, so that the $\Gamma$-equivariant sheaves over $X_K$ and the sheaves over $X$ form equivalent categories. The theorem is the sheaf-theoretic form of the Galois descent of vector spaces of *Descent Theory* and of the descent of the linear structures along a group of automorphisms, and it is the field-theoretic companion of the topological equivariant descent of *Equivariant Sheaves and Descent*.

This article fixes the base change and the Galois action on a sheaf, the descent datum and the fixed part, and the descent theorem for a finite Galois extension; it then describes the cohomological obstruction to the descent of a single sheaf, the classification of the twisted forms by the first nonabelian cohomology $H^1(\Gamma,\mathcal{A}ut)$, and the classical instances — the descent of the vector bundles and of the structure sheaf, and the Galois description of the central simple algebras and of the Brauer group. It is the last article of the involutive layer of the category; the group action and the general descent are *Equivariant Sheaves and Descent*, the real structure is *Sheaves with a Real Structure*, the derived theory is *Equivariant Derived Categories*, and the descent theory, the Galois theory and the group cohomology are *Descent Theory*, *Galois Theory* and *Group Cohomology* / *Galois Cohomology* of Part I.

The article uses no analysis and no geometry: the base field is arbitrary, the spaces are ringed spaces or schemes over it, and no form, no norm, no measure and no derivative occurs. Throughout, $K/k$ is a finite Galois extension with group $\Gamma$, $X$ is a ringed space over $k$ (or a scheme over $k$), $X_K=X\times_kK$ is the base change, $\mathcal{O}_{X_K}=\mathcal{O}_X\otimes_kK$, and $\mathcal{M}$ is a sheaf of $\mathcal{O}_{X_K}$-modules. The action of $\Gamma$ on $K$ is the Galois action, the fixed field is $K^{\Gamma}=k$ by the fundamental theorem of Galois theory, and the structure sheaf of $X_K$ carries the semilinear action $\gamma(a\otimes\lambda)=a\otimes\gamma(\lambda)$.

## Base Change and the Galois Action

**Definition.** For a ringed space $X$ over $k$ the **base change** is $X_K=X\times_kK$, with the structure sheaf $\mathcal{O}_{X_K}=\mathcal{O}_X\otimes_kK$; the projection $p:X_K\to X$ is an affine morphism, and every sheaf of $\mathcal{O}_{X_K}$-modules is a sheaf over $X_K$ whose sections are $K$-modules. The group $\Gamma$ acts on $X_K$ through the second factor, $\gamma\cdot(x,\lambda)=(x,\gamma\lambda)$, and on the structure sheaf by $\gamma(a\otimes\lambda)=a\otimes\gamma(\lambda)$.

**Proposition (the Galois action is an action).** The assignment $\gamma\mapsto(\gamma\cdot)$ is an action of $\Gamma$ on $X_K$ by morphisms over $k$, on $\mathcal{O}_{X_K}$ by semilinear isomorphisms, and on the category of sheaves of $\mathcal{O}_{X_K}$-modules by the pullback; the fixed subfield of the action on the coefficients is $k$.

*Proof.* The action on $X_K$ and on the coefficients is the action on the second factor of the base change, which is an action by the definition of the Galois group; the fixed field is the fundamental theorem of *Galois Theory*. The functoriality on sheaves is the functoriality of the pullback.

**Definition.** A **$\Gamma$-equivariant sheaf** over $X_K$ is a sheaf $\mathcal{M}$ of $\mathcal{O}_{X_K}$-modules with, for every $\gamma\in\Gamma$, a **semilinear** isomorphism

$$
\varphi_{\gamma}:\gamma_*\mathcal{M}\longrightarrow\mathcal{M},\qquad \varphi_{\gamma}(a m)=\gamma(a)\varphi_{\gamma}(m),
$$

satisfying the cocycle $\varphi_{\gamma\delta}=\varphi_{\gamma}\circ\gamma_*(\varphi_{\delta})$ and $\varphi_e=\mathrm{id}$; a morphism of $\Gamma$-equivariant sheaves is a morphism of sheaves of $\mathcal{O}_{X_K}$-modules commuting with the $\varphi_{\gamma}$. The category is written $\mathrm{Sh}_{\Gamma}(X_K)$.

**Remark (the same structure as the equivariant sheaf).** The definition is that of *Equivariant Sheaves and Descent* with the group $\Gamma$ acting on the space $X_K$, with the one addition that the coefficient maps are required to be **semilinear** over $K$: the action of $\Gamma$ on the coefficients is the Galois action, and it must not be confused with a complex-linear or an $X$-linear action. The semilinearity is the descent datum of the Galois cover $X_K\to X$, and the descent of the next sections is the Galois descent.

## The Descent Datum and the Fixed Part

**Definition.** The **descent datum** of a $\Gamma$-equivariant sheaf $\mathcal{M}$ over $X_K$ is the family of the semilinear isomorphisms $\varphi_{\gamma}$ together with their cocycle. The **fixed part** is

$$
\mathcal{M}^{\Gamma}(V)=\mathcal{M}\bigl(p^{-1}V\bigr)^{\Gamma}=\{\,m: \varphi_{\gamma}(m)=m\ \text{for every}\ \gamma\in\Gamma\,\},
$$

for an open $V\subseteq X$, with $p^{-1}V$ the preimage in $X_K$, on which $\Gamma$ acts; it is a sheaf of $\mathcal{O}_X$-modules, the **descent** of $\mathcal{M}$.

*Proof.* The preimage $p^{-1}V$ is a $\Gamma$-invariant open set, so the equivariant structure makes $\mathcal{M}(p^{-1}V)$ a $\Gamma$-module on which the invariants are defined; the fixed part is then a sheaf, by the discussion of *Equivariant Sheaves and Descent* applied to the invariant opens, and it is a module over the fixed part of the structure sheaf, which is $\mathcal{O}_X$ because $\mathcal{O}_{X_K}^{\Gamma}=(\mathcal{O}_X\otimes_kK)^{\Gamma}=\mathcal{O}_X\otimes_kK^{\Gamma}=\mathcal{O}_X$.

**Proposition (the fixed part of the structure sheaf).** $\mathcal{O}_{X_K}^{\Gamma}=\mathcal{O}_X$, and more generally the fixed part of a sheaf of the form $\mathcal{N}\otimes_kK$ with $\Gamma$ acting through $K$ is $\mathcal{N}$; the fixed part functor is left exact and its right derived functors are the Galois cohomology $H^i(\Gamma,-)$.

*Proof.* The invariants of $\mathcal{O}_X\otimes_kK$ under the Galois action on the second factor are $\mathcal{O}_X\otimes_kK^{\Gamma}=\mathcal{O}_X$; the general statement is the same computation sieved with an $\mathcal{O}_X$-module. The left exactness is that of the invariants, and the identification of the derived functors with the group cohomology is the standard one of *Group Cohomology*.

## The Galois Descent Theorem

**Theorem (Galois descent for sheaves).** Let $K/k$ be a finite Galois extension and $X$ a ringed space or a scheme over $k$. Then the fixed-part and base-change functors

$$
\mathcal{M}\longmapsto\mathcal{M}^{\Gamma},\qquad \mathcal{N}\longmapsto\mathcal{N}\otimes_kK\ \text{with the Galois action},
$$

are inverse equivalences between the category $\mathrm{Sh}_{\Gamma}(X_K)$ of $\Gamma$-equivariant sheaves of $\mathcal{O}_{X_K}$-modules over $X_K$ and the category $\mathrm{Sh}(X)$ of sheaves of $\mathcal{O}_X$-modules over $X$,

$$
\mathrm{Sh}_{\Gamma}(X_K)\simeq\mathrm{Sh}(X).
$$

*Proof.* The pair is adjoint, as in *Equivariant Sheaves and Descent*; the unit and the counit are checked on the sections. A section of the counit over a $\Gamma$-invariant open set $U\subseteq X_K$ is a $\Gamma$-equivariant map $\mathcal{M}(U)^{\Gamma}\otimes_kK\to\mathcal{M}(U)$, which is the multiplication by the coefficients; it is an isomorphism by the descent lemma: an element of a $\Gamma$-module that is fixed splits as $m=\sum_{\gamma}\gamma(\lambda)m_{\gamma}$ with a normal basis $\{\lambda\}$ of $K/k$. The unit is the analogous computation, and the effectiveness is the faithful flatness of $K$ over $k$, which is the descent theorem of *Descent Theory*.

**Corollary (the structure sheaf and the vector bundles).** The structure sheaf descends, $\mathcal{O}_X=\mathcal{O}_{X_K}^{\Gamma}$; the base change identifies the locally free sheaves of finite rank on $X$ with the $\Gamma$-equivariant locally free sheaves on $X_K$, and the descent is effective for all quasicoherent sheaves when $X$ is a scheme over $k$.

*Proof.* The structure-sheaf statement is the proposition on the fixed part; the vector-bundle statement is the theorem applied to the locally free sheaves, whose rank is preserved by the base change and the descent; the effectiveness for quasicoherent sheaves is the faithfully flat descent of *Descent Theory*.

## The Cohomological Obstruction

**Theorem (the twisted forms).** Fix a $\Gamma$-equivariant sheaf $\mathcal{M}$ over $X_K$ with automorphism group $\mathcal{A}ut_{\Gamma}(\mathcal{M})$ — the sheaf of $\Gamma$-equivariant automorphisms. The $\Gamma$-equivariant sheaves over $X_K$ that become isomorphic to $\mathcal{M}$ after a base change to a Galois extension are classified by the first nonabelian cohomology

$$
H^1\bigl(\Gamma,\mathcal{A}ut_{\Gamma}(\mathcal{M})\bigr),
$$

the pointed set of classes of $1$-cocycles of $\Gamma$ with values in the automorphisms, two cocycles giving the same form when they differ by a coboundary; the trivial class corresponds to the descended sheaf $\mathcal{M}^{\Gamma}$.

*Proof.* A twisted form is described on the Galois cover $X_K\to X$ by a cocycle with values in the automorphisms of $\mathcal{M}$, the cocycle condition being the descent condition of the equivariant structure; two descriptions give isomorphic forms exactly when the cocycles differ by a coboundary, and the computation is the Čech computation of *Čech Cohomology* for the cover. This is the nonabelian $H^1$ of *Group Cohomology* and *Galois Cohomology*.

**Corollary (the classical instances).** The twisted forms of the trivial rank-$n$ vector space are classified by $H^1(\Gamma,GL_n(K))$, which is trivial by **Hilbert's Theorem 90** for a finite Galois extension, so that every $\Gamma$-equivariant vector bundle is descended; the twisted forms of the matrix algebra $M_n(K)$ are classified by $H^1(\Gamma,PGL_n(K))=H^2(\Gamma,K^{\times})=\mathrm{Br}(K/k)$, the **Brauer group** of the extension, so that the central simple $k$-algebras split by $K$ are the twisted forms of the matrix algebra; the twisted forms of a quadratic space are classified by $H^1(\Gamma,O_n(K))$.

*Proof.* The forms of the trivial vector space are the $K$-vector spaces with a semilinear $\Gamma$-action, that is the vector spaces with a descent datum; Hilbert's theorem $H^1(\Gamma,GL_n(K))=1$ shows that each has a basis of invariant vectors, hence descends. The forms of the matrix algebra are the central simple algebras with a $\Gamma$-action, classified by the projective group, and the boundary $GL_n\to PGL_n$ gives the identification of $H^1(\Gamma,PGL_n)$ with $H^2(\Gamma,K^{\times})$, computed from the exact sequence $1\to K^{\times}\to GL_n(K)\to PGL_n(K)\to1$ and Hilbert's theorem $90$; the quadratic case is the same computation for the orthogonal group. The computation is that of *Galois Cohomology* and of *Sheaves in Algebraic Geometry* for the Brauer group.

**Remark (descent of the structure sheaf and of the modules of a ring).** The descent of the structure sheaf and of the sheaves of modules over it is the sheaf-theoretic form of the descent of an algebra and of its modules along an involution or a group of automorphisms, that is, of *Commutative Algebras with an Involution* and of *Involutive Bilinear Algebras*; the Galois case is the case in which the group is the Galois group of the extension and the involution is an automorphism of the coefficients.

## Relation to the Equivariant Descent

**Remark (the two descents).** The Galois descent of this article is the case of the equivariant descent of *Equivariant Sheaves and Descent* in which the group is the Galois group of a finite extension and the space is the base change $X_K$; the topological descent is the case in which the group acts freely and properly discontinuously on a space and the quotient is a covering. The two share the descent datum and the fixed part; they differ in the source of the action — a group of homeomorphisms of the space in one case, the Galois group of the coefficients in the other — and in the effectiveness, which comes from the covering in one case and from the faithful flatness of the extension in the other. The comparison is the principle that descent along a cover and descent along a Galois action are the same computation, and it is stated in *Descent Theory*.

## Worked Cases

### The Descent of a Vector Bundle

For a finite Galois extension $K/k$ and a $\Gamma$-equivariant vector bundle $\mathcal{E}$ over $X_K$, the fixed part $\mathcal{E}^{\Gamma}$ is a vector bundle over $X$ of the same rank with $\mathcal{E}^{\Gamma}\otimes_kK\cong\mathcal{E}$; the descent is effective, and the fixed part is computed on the sections as the invariants under the semilinear action. For the trivial bundle with the action through a representation of $\Gamma$ on the fibres, the fixed part is the bundle of invariant vectors, and its rank is the dimension of the invariants of the representation.

### The Structure Sheaf and the Fixed Functions

For $X_K=X\times_kK$ the structure sheaf descends to $\mathcal{O}_X$, and the fixed part of the structure sheaf under the Galois action is the sheaf of functions over $X$: the Galois descent of the structure sheaf is the statement $\mathcal{O}_{X_K}^{\Gamma}=\mathcal{O}_X$, the sheaf-theoretic form of the fundamental theorem $K^{\Gamma}=k$. The case is the model of the descent of an algebra of functions along its group of automorphisms.

### The Central Simple Algebras and the Brauer Group

The twisted forms of the matrix algebra over $K$ are the central simple $k$-algebras split by $K$, classified by $H^1(\Gamma,PGL_n)=H^2(\Gamma,K^{\times})$; the union over the finite Galois extensions is the **Brauer group** of $k$, and the descent gives the sheaf-theoretic form of the classification: a central simple algebra is a matrix algebra with a Galois descent datum to a smaller field. The example is the classical instance of the cohomological obstruction and the entry to *Sheaves in Algebraic Geometry* and *Group Cohomology*.

## Summary

Let $K/k$ be a finite Galois extension with group $\Gamma$, and let $X_K=X\times_kK$ be the base change of a space or a scheme over $k$. A $\Gamma$-equivariant sheaf over $X_K$ is a sheaf of $\mathcal{O}_{X_K}$-modules with a semilinear action of $\Gamma$ covering the action on the coefficients; the descent datum is the action, the fixed part is the sheaf of invariants over the quotient $X$, and the fixed part of the structure sheaf is $\mathcal{O}_X$ because $K^{\Gamma}=k$. The Galois descent theorem states that the fixed part and the base change are inverse equivalences between the $\Gamma$-equivariant sheaves over $X_K$ and the sheaves over $X$; the proof is the unit-counit computation on the normal basis of $K/k$, and the effectiveness is the faithful flatness of the extension.

A single sheaf need not descend: the obstruction is a class in the first nonabelian cohomology $H^1(\Gamma,\mathcal{A}ut_{\Gamma}(\mathcal{M}))$, and the classical computations are the triviality of $H^1(\Gamma,GL_n)$ by Hilbert's Theorem 90, so that every equivariant vector bundle descends, and the identification of the forms of the matrix algebra with $H^2(\Gamma,K^{\times})$, the Brauer group. The Galois descent is the coefficient-action case of the equivariant descent, the companion of the topological and the real-structure descents, and the sheaf-theoretic form of the descent of a linear structure along a group of automorphisms of the coefficients.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K/k$, $\Gamma=\operatorname{Gal}(K/k)$ | finite Galois extension and its group; $K^{\Gamma}=k$ |
| $X_K=X\times_kK$ | base change; $\mathcal{O}_{X_K}=\mathcal{O}_X\otimes_kK$ |
| $p:X_K\to X$ | projection; a Galois cover of the base |
| $\varphi_{\gamma}:\gamma_*\mathcal{M}\to\mathcal{M}$ | semilinear descent datum; $\varphi_{\gamma}(am)=\gamma(a)\varphi_{\gamma}(m)$ |
| $\mathrm{Sh}_{\Gamma}(X_K)$ | category of $\Gamma$-equivariant sheaves over $X_K$ |
| $\mathcal{M}^{\Gamma}$ | fixed part, the descended sheaf; a sheaf of $\mathcal{O}_X$-modules |
| $\mathrm{Sh}_{\Gamma}(X_K)\simeq\mathrm{Sh}(X)$ | Galois descent equivalence |
| $H^1(\Gamma,\mathcal{A}ut_{\Gamma}(\mathcal{M}))$ | classes of twisted forms of $\mathcal{M}$ |
| $H^1(\Gamma,GL_n(K))=1$ | Hilbert's Theorem 90; every equivariant vector bundle descends |
| $H^1(\Gamma,PGL_n(K))\cong H^2(\Gamma,K^{\times})$ | forms of the matrix algebra; the Brauer group |

## Further Reading

- Alexander Grothendieck, *Technique de descente et théorèmes d'existence en géométrie algébrique (FGA)* (Séminaire Bourbaki, 1959–1962), for the faithfully flat descent and the descent of the sheaves.
- Alexander Grothendieck, *Le groupe de Brauer* (Séminaire Bourbaki 290, 1965; and Dix exposés sur la cohomologie des schémas, 1968), for the Brauer group and the descent of the central simple algebras.
- Jean-Pierre Serre, *Galois Cohomology* (Springer, 1997), for the nonabelian $H^1$, Hilbert's Theorem 90 and the classification of the forms.
- Jean-Pierre Serre, *Local Fields* (Springer, 1979), for the Galois descent of the vector spaces and the comparison with the local theory.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the descent of the linear structures and the forms of the classical groups.
- Alexander Grothendieck and Jean Dieudonné, *Éléments de géométrie algébrique* (Publications Mathématiques de l'IHÉS, 1960–1967), for the descent of the quasicoherent sheaves along a faithfully flat morphism.
- Glen E. Bredon, *Sheaf Theory* (Springer, second edition, 1997), for the fixed part and the invariant sections under a group of automorphisms of the coefficients.
