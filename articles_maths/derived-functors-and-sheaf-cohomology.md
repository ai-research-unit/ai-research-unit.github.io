
# __Derived Functors and Sheaf Cohomology__

## Introduction

The cohomology of a sheaf, as defined in *Sheaf Cohomology*, is the right derived functor of the global sections functor: one resolves $\mathcal{F}$ by injective sheaves and applies $\Gamma(X,-)$. That definition presupposes three things, all of them the common property of a class of categories rather than of spaces: that the category of sheaves of abelian groups on a space is abelian, that it has enough injectives, and that the derived functors may be characterised abstractly so that *any* cohomological construction — the Čech complex of *Čech Cohomology*, the de Rham complex, the singular cochain complex — can be certified to compute them. This article supplies those three things for the category of sheaves, as an instance of the general theory of Part I. The general theory itself — additive and abelian categories, the Freyd–Mitchell embedding theorem, the definition and properties of left and right derived functors, $\delta$-functors, the Grothendieck spectral sequence, the derived category — is *Abelian and Grothendieck Categories*, *Homological Algebra*, *Derived Functors* and *Derived Categories* of Part I, and it is cited here rather than repeated; the topological instance is what is developed.

The organising notion is **effaceability**. A cohomological $\delta$-functor on the category of sheaves is effaceable if every one of its groups can be killed by embedding the coefficient sheaf in a suitable sheaf — for sheaf cohomology, by embedding in a flabby or injective sheaf. Grothendieck's theorem is that an effaceable $\delta$-functor is *universal*, and that a universal $\delta$-functor agreeing with a given left exact functor in degree zero is the derived functor of that functor. The theorem has two consequences that this article is built around. The first is the **abstract de Rham theorem**: if $0\to\mathcal{F}\to\mathcal{A}^0\to\mathcal{A}^1\to\cdots$ is a resolution of $\mathcal{F}$ by sheaves that are acyclic for the functor of sections, or more generally a resolution whose sections form a cohomological functor effaceable in the required sense, then

$$
H^i(X,\mathcal{F}) \cong H^i\bigl(\Gamma(X,\mathcal{A}^\bullet)\bigr),
$$

so that any acyclic resolution computes the cohomology; the flabby resolution of Godement, the Čech complex, the singular cochain complex and the de Rham complex are all instances, and the last of them is the identification of de Rham cohomology with singular cohomology. The second is the **Grothendieck spectral sequence** of a composite of functors, whose instances on a space include the Leray spectral sequence of a continuous map and the Čech-to-derived spectral sequence. A final section records the derived-functor properties of the direct image functor $f_*$, which are the sheaf-theoretic content of the six operations, and states that the natural home of the theory is the derived category of sheaves of Part I.

The article is the last of the abstract trilogy *Sheaf Cohomology*, *Čech Cohomology*, *Derived Functors and Sheaf Cohomology*; the de Rham and geometric instances of the abstract de Rham theorem are worked out, written in this same batch, and the sheaf theory of algebraic geometry. Sheaves on a general Grothendieck site, for which the same theory is available with a site in place of a space, are Part I's *Sheaves on Sites*, and the descent-theoretic questions are Part I's *Descent Theory*.

## The Category of Sheaves

**Theorem (the category of sheaves).** Let $X$ be a topological space.

1. The category $\mathrm{Sh}(X,\mathbf{Ab})$ of sheaves of abelian groups on $X$ is an abelian category: it has kernels, cokernels and finite products and coproducts, the image of a morphism is the kernel of its cokernel, and the functor to the category of presheaves is left exact and preserves kernels.
2. Filtered colimits in $\mathrm{Sh}(X,\mathbf{Ab})$ are exact — the category is AB5 — and the sheaves $\underline{\mathbb{Z}}$ and the representable sheaves $\underline{\mathbb{Z}}_U$ form a family of generators: a nonzero morphism $\mathcal{F}\to\mathcal{G}$ is detected by a morphism from some $\underline{\mathbb{Z}}_U$.
3. The category has enough injectives, and the class of injective sheaves is contained in the class of flabby sheaves, which is contained in the class of acyclic sheaves.
4. For a ringed space $(X,\mathcal{O}_X)$, the category of sheaves of $\mathcal{O}_X$-modules is abelian with enough injectives and satisfies AB5.

*Proof.* (1) and (2) are *Abelian and Grothendieck Categories* of Part I, applied to the category of functors from the poset of open sets to abelian groups with the sheaf condition; the generation statement uses that the sections of a sheaf over an open set are the homomorphisms from the sheaf $\underline{\mathbb{Z}}_U$ represented by $U$, so a nonzero morphism is nonzero on some sections. (3) is the construction of the previous article: a sheaf embeds in a product of skyscraper sheaves over injective stalks, which is flabby and injective; injective objects are flabby, and flabby sheaves are acyclic. (4) is the same argument over a sheaf of rings. $\square$

**Corollary (derived functors exist).** Every left exact functor $F : \mathrm{Sh}(X,\mathbf{Ab}) \to \mathbf{Ab}$, and every left exact functor to another abelian category, has right derived functors $R^iF$, defined by injective resolutions and forming a cohomological $\delta$-functor with $R^0F = F$; the categories of sheaves of modules likewise have enough injectives, so the functors $\mathcal{H}om_{\mathcal{O}_X}(\mathcal{F},-)$, $f_*$ and $\Gamma(X,-)$ all have right derived functors. This is *Derived Functors* of Part I, applied to the categories of the theorem; the topological content of the article is the identification of these derived functors with the cohomological constructions available on a space.

## $\delta$-Functors, Effaceability and Universality

The abstract machinery of this and the following section is *Homological Algebra* and *Derived Functors* of Part I; it is restated in the form in which it is used on a space, and the proofs are those of the general theory.

**Definition.** A **cohomological $\delta$-functor** from an abelian category $\mathcal{A}$ to an abelian category $\mathcal{B}$ is a sequence of additive functors $T^i : \mathcal{A}\to\mathcal{B}$, $i \geq 0$, together with, for every short exact sequence $0\to A'\to A\to A''\to 0$ in $\mathcal{A}$, morphisms $\delta^i : T^i(A'') \to T^{i+1}(A')$ natural in the sequence and such that the long sequence

$$
\cdots \to T^i(A') \to T^i(A) \to T^i(A'') \xrightarrow{\ \delta^i\ } T^{i+1}(A') \to \cdots
$$

is exact. A **morphism of $\delta$-functors** $T^\bullet\to S^\bullet$ is a sequence of natural transformations $T^i\to S^i$ commuting with the $\delta$'s. A $\delta$-functor is **effaceable** if for every object $A \in \mathcal{A}$ and every $i > 0$ there is a monomorphism $u : A \hookrightarrow B$ such that $T^i(u) = 0$; it is **universal** if every morphism of $\delta$-functors from $T^\bullet$ to any $\delta$-functor $S^\bullet$ is determined by its degree-zero component.

**Theorem (Grothendieck's universality theorem).** Let $T^\bullet$ be a cohomological $\delta$-functor.

1. If $T^\bullet$ is effaceable then it is universal.
2. If $T^0$ is left exact and $T^\bullet$ is effaceable, then $T^\bullet$ is canonically isomorphic to the right derived functor $\delta$-functor $R^\bullet T^0$.
3. The right derived functors $R^\bullet F$ of a left exact functor on a category with enough injectives are effaceable, hence universal; in particular the derived functor $\delta$-functor is determined up to canonical isomorphism by $F$ and by the existence of enough injectives.

*Proof.* (1) Given a morphism $\varphi : T^\bullet\to S^\bullet$ and an object $A$, choose an embedding $u : A\hookrightarrow B$ with $T^i(u) = 0$ for $i>0$ and consider the commutative diagram with exact rows coming from $0\to A\xrightarrow{u}B\to C\to 0$; induction on $i$ shows that $\varphi^i_A$ is determined by $\varphi^0$, from the exactness of the rows and the vanishing of $T^i(u)$. (2) Embedding $A$ in an injective object $I$ and comparing the resulting long exact sequences, one shows $T^i(I) = 0$ for $i>0$ and builds the degree-zero-compatible morphism $T^\bullet\to R^\bullet T^0$ by induction, which is an isomorphism by (1) applied to both functors. (3) The definition of $R^iF$ from injective resolutions makes $R^iF(u) = 0$ for $u$ a monomorphism into an injective object and $i>0$; universality is then (1). $\square$

**Corollary (uniqueness of cohomology theories on a space).** Let $T^\bullet$ be a cohomological $\delta$-functor from sheaves of abelian groups on $X$ to abelian groups with $T^0 = \Gamma(X,-)$ and $T^i$ effaceable for $i > 0$. Then $T^\bullet$ is canonically isomorphic to the sheaf cohomology $H^\bullet(X,-) = R^\bullet\Gamma(X,-)$. In particular, any two such theories — sheaf cohomology, Čech cohomology in the limit, hypercohomology of a resolution — are canonically isomorphic.

*Proof.* By the theorem, both $T^\bullet$ and $H^\bullet(X,-)$ are universal $\delta$-functors with the same degree-zero functor $\Gamma(X,-)$; the identity of degree zero extends to an isomorphism of universal $\delta$-functors, and by universality the extension is unique. $\square$

## Effaceability on a Space

**Theorem ($\Gamma$ is effaceable).** For every sheaf $\mathcal{F}$ on $X$ and every $i>0$ there is a monomorphism $\mathcal{F}\hookrightarrow\mathcal{G}$ into a sheaf $\mathcal{G}$ with $H^i(X,\mathcal{G}) = 0$; in particular $H^\bullet(X,-)$ is an effaceable $\delta$-functor and the corollary of the previous section applies to it.

*Proof.* Take $\mathcal{G} = \prod_{x\in X}(i_x)_*I_x$ with $\mathcal{F}_x\hookrightarrow I_x$ an embedding of $\mathcal{F}_x$ into an injective abelian group, as in the construction of enough injectives: $\mathcal{G}$ is flabby and injective, and injective objects have vanishing higher cohomology. $\square$

**Theorem (the abstract de Rham theorem).** Let

$$
0 \to \mathcal{F} \to \mathcal{A}^0 \xrightarrow{\ d^0\ } \mathcal{A}^1 \xrightarrow{\ d^1\ } \mathcal{A}^2 \to \cdots
$$

be a resolution of $\mathcal{F}$ — a complex of sheaves, exact at every stage including $\mathcal{A}^0$, with only $\mathcal{F}$ in degree $-1$ — such that the cohomological $\delta$-functor $T^i = H^i\bigl(\Gamma(X,\mathcal{A}^\bullet)\bigr)$ is effaceable; for instance, such that each $\mathcal{A}^i$ is acyclic, $H^j(X,\mathcal{A}^i) = 0$ for $j>0$. Then the natural map

$$
H^i\bigl(\Gamma(X,\mathcal{A}^\bullet)\bigr) \to H^i(X,\mathcal{F})
$$

induced by lifting $\mathcal{F}\to\mathcal{A}^\bullet$ to injective resolutions is an isomorphism for every $i$.

*Proof.* The functor $T^i = H^i(\Gamma(X,\mathcal{A}^\bullet))$ is a cohomological $\delta$-functor in $\mathcal{F}$ with $T^0 = \ker(d^0) = \Gamma(X,\mathcal{F})$ by the exactness of the resolution at $\mathcal{A}^0$, and the six-term exact sequence of a short exact sequence of complexes gives the connecting morphisms. If each $\mathcal{A}^i$ is acyclic, $T^i$ is effaceable, since embedding $\mathcal{F}$ in an acyclic $\mathcal{G}$ makes the comparison map $T^i(\mathcal{F})\to T^i(\mathcal{G})$ factor through $H^i(X,\mathcal{G}) = 0$; the complex case is the same argument with the defining property of effaceability. The corollary above then identifies $T^\bullet$ with $H^\bullet(X,-)$. $\square$

**Corollary (the cohomology theories of a space agree).** On a space $X$ the following constructions all compute $H^i(X,\mathcal{F})$:

1. the flabby resolution of Godement of *Sheaf Cohomology*;
2. the Čech complex of a cover in the limit, when $X$ is paracompact, by *Čech Cohomology*;
3. the de Rham complex of a smooth manifold, when $\mathcal{F}$ is the constant sheaf and the de Rham complex is a resolution by fine sheaves: $H^i_{dR}(M)\cong H^i(M;\underline{\mathbb{R}})$, the de Rham theorem, developed;
4. the singular cochain complex, on a locally contractible paracompact space, when $\mathcal{F} = \underline{A}$ is constant: $H^i(X;\underline{A})\cong H^i(X;A)$, the comparison theorem of *Sheaf Cohomology*;
5. the hypercohomology of a bounded below complex of sheaves, whose two spectral sequences are the subject of the next section.

*Proof.* Each item exhibits a resolution or a complex whose sections give a cohomological $\delta$-functor in the coefficient sheaf, with degree zero the global sections, and which is effaceable either because the terms are acyclic or by the comparison argument; the abstract de Rham theorem applies. For (4) one uses the resolution of $\underline{A}$ by the sheaves of singular cochains, whose acyclicity is the local contractibility of $X$. $\square$

**Remark (the role of effaceability).** Effaceability is the abstract form of the statement that a cohomology theory on a space is determined by its behaviour on the small open sets: the ability to kill a class by embedding the coefficient sheaf in a larger sheaf is exactly the ability to push a class off any open set on which it is supported, and it is this that makes the theory computable from local data and that forces different local constructions to agree.

## Hypercohomology and the Grothendieck Spectral Sequence

**Definition.** Let $\mathcal{A}^\bullet$ be a bounded below complex of sheaves on $X$, with the convention that the differentials increase the degree. The **hypercohomology** of $\mathcal{A}^\bullet$ is the sequence of groups

$$
\mathbb{H}^i(X,\mathcal{A}^\bullet) = R^i\Gamma(X,\mathcal{A}^\bullet),
$$

the right derived functors of the global sections functor applied to the complex, computed by replacing $\mathcal{A}^\bullet$ by a bounded below complex of injective sheaves quasi-isomorphic to it and taking the cohomology of the total complex of the resulting double complex. The two spectral sequences of the filtration of the total complex by the first and second degree have

$$
{}'E_2^{p,q} = H^p(X,\mathcal{H}^q(\mathcal{A}^\bullet)) \Longrightarrow \mathbb{H}^{p+q}(X,\mathcal{A}^\bullet), \qquad {}''E_1^{p,q} = H^q(X,\mathcal{A}^p) \Longrightarrow \mathbb{H}^{p+q}(X,\mathcal{A}^\bullet),
$$

and when $\mathcal{A}^\bullet$ is a resolution of a single sheaf $\mathcal{F}$, the hypercohomology is $H^i(X,\mathcal{F})$, so that the two spectral sequences compute the cohomology of $\mathcal{F}$ from a resolution whose terms need not be acyclic.

**Theorem (the Grothendieck spectral sequence).** Let $F : \mathcal{A}\to\mathcal{B}$ and $G : \mathcal{B}\to\mathcal{C}$ be left exact functors between abelian categories, and suppose that $F$ sends injective objects of $\mathcal{A}$ to $G$-acyclic objects of $\mathcal{B}$ (that is, $R^jG(F(I)) = 0$ for $j>0$ and $I$ injective). Then for every object $A$ of $\mathcal{A}$ there is a spectral sequence of cohomological type

$$
E_2^{p,q} = \bigl(R^pG\bigr)\bigl(R^qF(A)\bigr) \Longrightarrow R^{p+q}(G\circ F)(A),
$$

natural in $A$. When $\mathcal{A}$ is a category of sheaves, $\mathcal{B} = \mathcal{C} = \mathbf{Ab}$, $F = f_*$ for a continuous map $f : X\to Y$ and $G = \Gamma(Y,-)$, the hypothesis holds and the sequence becomes the **Leray spectral sequence**

$$
E_2^{p,q} = H^p\bigl(Y, R^qf_*\mathcal{F}\bigr) \Longrightarrow H^{p+q}(X,\mathcal{F})
$$

of *Sheaf Cohomology*; when $F$ is the functor of sections of a complex of sheaves and $G$ the global sections, one obtains the Čech-to-derived and the hypercohomology sequences. The statement and proof of the general theorem, and the construction of the spectral sequence of a filtered complex, are *Spectral Sequences* of Part I; the fibration case $E_2^{p,q} = H^p(B;\underline{H}^q(F;A))\Rightarrow H^{p+q}(E;A)$ is the Leray–Serre sequence of *The Leray–Serre Spectral Sequence*.

*Proof sketch.* Take an injective resolution $A\to I^\bullet$; the hypothesis makes $F(I^\bullet)$ a complex of $G$-acyclic objects, and the double complex obtained by resolving each $F(I^q)$ by injectives has two filtrations whose spectral sequences are the ones displayed; the $E_2$ of the first filtration computes the cohomology of $F(I^\bullet)$ in the $q$-direction and then applies $R^pG$, and the abutment is the cohomology of the total complex, which computes $R^{p+q}(G\circ F)(A)$ by the standard comparison argument. $\square$

**Corollary (the five-term exact sequence).** In the situation of the theorem there is an exact sequence

$$
0 \to E_2^{1,0}\to R^1(G\circ F)(A) \to E_2^{0,1}\xrightarrow{\ d_2\ } E_2^{2,0}\to R^2(G\circ F)(A),
$$

the **five-term exact sequence** of the spectral sequence, obtained from the edge homomorphisms and the differential $d_2 : E_2^{0,1}\to E_2^{2,0}$. For the Leray spectral sequence it reads

$$
0 \to H^1(Y,f_*\mathcal{F})\to H^1(X,\mathcal{F})\to H^0(Y,R^1f_*\mathcal{F})\xrightarrow{\ d_2\ } H^2(Y,f_*\mathcal{F})\to H^2(X,\mathcal{F}),
$$

which is the exact sequence used to compute the cohomology of a fibration and of a covering map.

## Derived Functors of the Direct Image

**Definition.** For a continuous map $f : X\to Y$ the functors $f^{-1} : \mathrm{Sh}(Y)\to\mathrm{Sh}(X)$ and $f_* : \mathrm{Sh}(X)\to\mathrm{Sh}(Y)$ form an adjoint pair $f^{-1}\dashv f_*$: $\operatorname{Hom}(f^{-1}\mathcal{G},\mathcal{F})\cong\operatorname{Hom}(\mathcal{G},f_*\mathcal{F})$. Since $f^{-1}$ is left adjoint to a left exact functor it is right exact, and it is in fact exact; since $f_*$ is left adjoint to an exact functor, or directly from the definition, it preserves limits and is left exact. The higher direct images $R^qf_*$ are the right derived functors of $f_*$, the sheaves on $Y$ whose stalk at $y$ is the cohomology of the fibre: $(R^qf_*\mathcal{F})_y = \varinjlim_{V\ni y}H^q(f^{-1}(V),\mathcal{F})$.

**Theorem (properties).** Let $f : X\to Y$ and $g : Y\to Z$ be continuous.

1. $R^qf_* = 0$ for $q<0$ and $R^0f_* = f_*$; for a closed immersion $f$, $R^qf_* = 0$ for $q>0$.
2. There is a natural spectral sequence $E_2^{p,q} = R^pg_*(R^qf_*\mathcal{F})\Rightarrow R^{p+q}(g\circ f)_*\mathcal{F}$, the Grothendieck spectral sequence of the composite of the two left exact functors.
3. The **base change map** $g^{-1}R^qf_*\mathcal{F}\to R^qf'_*(g'^{-1}\mathcal{F})$ for a cartesian square with maps $f, g, f', g'$ is an isomorphism when $f$ is proper and of finite cohomological dimension, or when $g$ is flat; more generally there is a base change spectral sequence.
4. The **projection formula** $R^qf_*\mathcal{F}\otimes_{\mathcal{O}_Y}\mathcal{G}\cong R^qf_*(\mathcal{F}\otimes_{\mathcal{O}_X}f^*\mathcal{G})$ holds when the tensor and direct image are taken over compatible structure sheaves.

*Proof.* (1) is immediate from the definition; for a closed immersion the direct image is exact because the induced map on stalks is an isomorphism or zero. (2) is the Grothendieck spectral sequence applied to $F = f_*$, $G = g_*$; the hypothesis is verified by resolving on $X$, since an injective sheaf on $X$ is flabby and $R^pf_*$ of a flabby sheaf vanishes for $p>0$. (3) and (4) are the standard constructions of the subject, proved by reducing to the affine or the locally free case and using the exactness of $g^{-1}$ and the projection formula for modules. $\square$

**Remark (the derived category and the six operations).** The statements above look asymmetric because the derived functors are taken in one direction only. The symmetric formulation is the derived category $D^+(\mathrm{Sh}(X))$ of *Derived Categories* of Part I: a morphism of spaces $f$ induces $f^* = f^{-1}$ (exact, so no derived functor is needed), the right derived functor $Rf_*$, the proper direct image $Rf_!$ for maps of finite cohomological dimension between locally compact spaces, its right adjoint $f^!$, and the derived tensor product and sheaf hom; the six operations $f^*, f_*, f_!, f^!, \otimes, \mathcal{H}om$ satisfy the base change, projection and duality formulae. **Verdier duality** is the adjunction $\mathbb{R}f_! \dashv f^!$, the assertion that the proper direct image has a right adjoint $f^!$ on the derived categories whenever $f$ is of finite cohomological dimension between locally compact spaces; it has a purely topological content, and it specialises for $f$ the map to a point to the Poincaré duality of *Poincaré Duality*: for a closed oriented $n$-manifold with constant coefficients it reads $H^k(M)\cong H_{n-k}(M)^{\vee}$, and its sheaf-theoretic form is the twisted duality of *Sheaf Cohomology*. The derived category is Part I's and is not developed here; the constructions of this section are its degreewise shadow, and the applications to algebraic geometry are.

## Summary

The category of sheaves of abelian groups on a space is an abelian AB5 category with a family of generators and enough injectives, so that every left exact functor on it has right derived functors; the general theory of abelian categories, of derived functors and of spectral sequences is Part I's, and the article applies it to the two functors that occur on a space, the global sections $\Gamma(X,-)$ and the direct image $f_*$. The abstract notion that makes the application work is effaceability: a cohomological $\delta$-functor is effaceable if every class in positive degree can be killed by embedding the coefficient in a suitable object, and Grothendieck's theorem states that an effaceable $\delta$-functor is universal and that an effaceable $\delta$-functor with a left exact degree-zero part is that part's derived functor. Consequently the sheaf cohomology $H^\bullet(X,-)$ is the only cohomological theory with $H^0 = \Gamma$ whose positive-degree functors are effaceable, and the **abstract de Rham theorem** follows: any resolution of a sheaf by acyclic sheaves, or any resolution whose sections give an effaceable functor, computes the cohomology. The flabby resolution of Godement, the Čech complex in the limit, the de Rham complex of a manifold and the singular cochain complex of a locally contractible space are all instances, which is why the different cohomology theories of a space agree.

The **Grothendieck spectral sequence** $E_2^{p,q} = R^pG(R^qF(A)) \Rightarrow R^{p+q}(G\circ F)(A)$ for a composite of left exact functors, its five-term exact sequence and its instances — the Leray spectral sequence of a continuous map, the hypercohomology of a complex of sheaves and the spectral sequence of a double complex — organise the computation of sheaf cohomology from a filtration, and the derived functors $R^qf_*$ of the direct image, with their base change and projection formulae and the duality of Verdier, are the degreewise shadow of the six operations of the derived category of Part I.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Sh}(X,\mathbf{Ab})$, $\mathrm{Sh}(X,\mathcal{O}_X)$ | abelian category of sheaves of groups or of $\mathcal{O}_X$-modules |
| AB5 | filtered colimits are exact |
| $R^iF$, $R^i\Gamma(X,-)$ | right derived functors; sheaf cohomology $H^i(X,\mathcal{F})$ |
| $\delta^i$ | connecting morphism of a cohomological $\delta$-functor |
| effaceable | $T^i(A)$ killed by some monomorphism $A\hookrightarrow B$ for $i>0$ |
| universal | morphisms out of the $\delta$-functor determined by degree zero |
| $\mathcal{A}^\bullet$, $\mathbb{H}^i(X,\mathcal{A}^\bullet)$ | complex of sheaves; hypercohomology $R^i\Gamma(X,\mathcal{A}^\bullet)$ |
| $E_2^{p,q} = R^pG(R^qF(A))$ | Grothendieck spectral sequence of a composite of functors |
| $E_2^{p,q} = H^p(Y,R^qf_*\mathcal{F})$ | Leray spectral sequence of a continuous map |
| $f^{-1}\dashv f_*$, $R^qf_*$ | inverse and direct image adjunction; higher direct images |
| $f^*, f_*, f_!, f^!, \otimes, \mathcal{H}om$ | the six operations of the derived category |
| Verdier duality | the adjunction $\mathbb{R}f_!\dashv f^!$; for $f$ to a point, $H^k(M)\cong H_{n-k}(M)^{\vee}$ |



## Further Reading

- Alexander Grothendieck, *Sur quelques points d'algèbre homologique* (Tohoku Mathematical Journal 9, 1957), for effaceable $\delta$-functors, universality and the spectral sequence of a composite of functors.
- Roger Godement, *Topologie algébrique et théorie des faisceaux* (Hermann, 1958), for the flabby resolution and the effacement of sheaf cohomology.
- Jean-Louis Verdier, *Des catégories dérivées des catégories abéliennes* (Astérisque 239, 1996), for the derived category, the six operations and duality.
- Glen E. Bredon, *Sheaf Theory* (Springer, second edition, 1997), for the derived-functor theory on a space and the properties of $f_*$ and $f^{-1}$.
- Birger Iversen, *Cohomology of Sheaves* (Springer, 1986), for the six operations and Verdier duality in the topological setting.
- Masaki Kashiwara and Pierre Schapira, *Sheaves on Manifolds* (Springer, 1990), for the cohomological theory of sheaves on a space and its applications.
