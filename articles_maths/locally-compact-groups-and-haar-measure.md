
# __Locally Compact Groups and Haar Measure__

## Introduction

A **locally compact group** is a topological group whose topology is Hausdorff and locally compact: every point has a compact neighbourhood. The class contains the discrete groups, the compact groups, the additive groups $\mathbb{R}^n$, $\mathbb{Q}_p^n$ and $\mathbb{Z}_p^n$, the general linear groups over $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$, and every Lie group; and it is exactly the class on which invariant integration exists. **Haar's theorem** states that a locally compact group carries a nonzero left-invariant Radon measure, unique up to a positive scalar; the measure is the **Haar measure**. Its failure of right-invariance is measured by a continuous homomorphism $\Delta : G \to \mathbb{R}_{>0}$, the **modular function**, and the groups for which $\Delta \equiv 1$ — the abelian, compact, discrete, nilpotent and semisimple ones — are the **unimodular** groups.

This article constructs the Haar measure and states its invariance and uniqueness, develops the modular function and unimodularity, computes the measure on the standard examples, and treats the quasi-invariant measure of a homogeneous space $G/H$ with the criterion for its invariance. The article is placed in this slot of the category because the measure is an invariant of the topological group, and it is the last of the four structural articles before the representation theory; every other article of this category uses it as an object.

Two boundaries are held exactly. The **construction** of the measure and the statement of its invariance are given here, as is the identification of the standard examples; but the **integration theory** — the $\sigma$-algebra, measurability, the convergence theorems, the $L^p$ spaces, the convolution algebra $L^1(G)$ and the Plancherel theorem — is *Analysis on Groups* in Part III, where the measure and the limit are available, and it is not taken here. Where an integral is written below it is the invariant functional of the Haar integral on continuous functions of compact support, and its measure-theoretic reading is the Riesz representation theorem. The topological frame is *Topological Groups*, *Metric, Uniform and Complete Spaces* and *Topological Spaces*; the Lie-theoretic examples are ; the p-adic examples are, with their integration a Part III subject. No physics is invoked.

## Locally Compact Groups

### Definition and First Properties

**Definition.** A **locally compact group** is a topological group $G$ that is Hausdorff and locally compact: every point has a compact neighbourhood, equivalently the identity has a compact neighbourhood. The group is written multiplicatively with identity $e$, or additively when abelian.

**Proposition.** Let $G$ be a locally compact group.

**(a)** The identity component $G_0$ is a closed normal subgroup, and $G/G_0$ is totally disconnected and locally compact.

**(b)** Every open subgroup of $G$ is closed; every closed subgroup of a compact group is compact; a closed subgroup of a locally compact group is locally compact.

**(c)** If $H$ is a closed subgroup then $G/H$ is a locally compact Hausdorff space and the quotient map is open and continuous; if $H$ is normal, $G/H$ is a locally compact group.

**(d)** If $G$ is locally Euclidean, then $G$ is a Lie group, with a unique smooth structure, by the theorem of Gleason and Montgomery–Zippin recalled.

**Pro.** (a) The identity component is closed and normal because conjugation is a homeomorphism fixing $e$, hence preserving $G_0$. The quotient is locally compact by the continuity of the quotient map, and it is totally disconnected because the connected components of a homogeneous space are the cosets of the identity component. (b) An open subgroup is closed because its complement is a union of cosets; a closed subgroup of a compact group is compact; local compactness is inherited by closed subspaces. (c) is *Topological Groups*, §Subgroups and Quotients. (d) is stated. $\square$

**Example (the standard locally compact groups).** $\mathbb{R}^n$ and $\mathbb{C}^n$, the tori $T^n = \mathbb{R}^n/\mathbb{Z}^n$, the circle $S^1$, every discrete group, every finite group, $\mathbb{Z}_p$ and $\mathbb{Q}_p$ with the $p$-adic topology, the adeles, and the classical groups $GL_n(\mathbb{K})$, $SL_n(\mathbb{K})$, $O(n)$, $U(n)$ are locally compact. A compactly generated locally compact abelian group is $\mathbb{R}^n \times \mathbb{Z}^m \times K$ with $K$ compact, by the structure theorem of *Abelian Topological Groups*; the compact factor is finite exactly when the group contains no infinite compact subgroup, so it is infinite for $\mathbb{Z}_p$ and for $\mathbb{R}^n \times \mathbb{Z}_p$. A locally convex topological vector space is locally compact exactly when it is finite-dimensional.

**Example (groups that are not locally compact).** An infinite-dimensional Banach space is not locally compact, and neither is the group of diffeomorphisms of a compact manifold with its Fréchet topology, treated; the loop groups are likewise not locally compact. No nonzero invariant Radon measure exists on these groups, and the theory of this article does not apply to them; that is the reason the representation theory of a non-locally-compact group requires a different frame.

## Haar Measure

### Existence and Uniqueness

**Definition.** A **left Haar measure** on a locally compact group $G$ is a nonzero Radon measure $\mu$ on the Borel sets of $G$ that is left-invariant:

$$
\mu(gA) = \mu(A) \qquad \text{for every Borel set } A \subseteq G \text{ and every } g \in G .
$$

A **Radon measure** is a Borel measure that is finite on compact sets, outer regular on Borel sets and inner regular on open sets. Equivalently — and this is the form used in the construction below — a Radon measure is a positive linear functional

$$
I : C_c(G) \longrightarrow \mathbb{R}, \qquad f \longmapsto \int_G f\,d\mu ,
$$

on the continuous real-valued functions of compact support, invariant under left translation: $I(L_g f) = I(f)$ with $L_g f(x) = f(g^{-1}x)$. The passage between the two formulations is the Riesz representation theorem in Part III; the construction is carried out in the functional form, and the measure-theoretic consequences are part of the integration theory.

**Theorem (Haar).** Every locally compact group $G$ carries a left Haar measure, and it is unique up to a positive scalar: if $\mu, \nu$ are left Haar measures then $\nu = c\mu$ for a unique $c \in \mathbb{R}_{>0}$.

**Proof sketch (existence).** The construction is the Haar–Cartan argument of covering numbers. For $f, h \in C_c(G)$ with $h \geq 0$ not identically zero put

$$
(f : h) = \inf\Bigl\{\sum_i c_i : f \leq \sum_i c_i\,L_{g_i}h \text{ for some } g_i \in G,\ c_i > 0\Bigr\},
$$

a positive finite number; it is left-invariant in $f$, monotone and subadditive in $f$, and satisfies $(f:h) \leq (f:h')(h':h)$. Fix $f_0 \in C_c^+$ with $f_0 \neq 0$ and, for a compact symmetric neighbourhood $V$ of $e$ with characteristic function $\chi_V$, set

$$
\Lambda_V(f) = \frac{(f : \chi_V)}{(f_0 : \chi_V)} .
$$

Each $\Lambda_V$ is positive, left-invariant and subadditive, and $\Lambda_V(f_0) = 1$. Refining $V$ along a neighbourhood base of $e$, the net $\Lambda_V(f)$ is bounded and one extracts a limit point by a diagonal argument over a countable dense family in $C_c(G)$, extended by uniform estimates; the limit $I(f) = \lim_V \Lambda_V(f)$ is a positive left-invariant linear functional on $C_c(G)$, nonzero because $I(f_0) = 1$. Positivity on the compactly supported functions is ensured by the ambient local compactness. The functional is the left Haar integral. $\square$

**Proof sketch (uniqueness).** Let $I'$ be a nonzero left-invariant positive functional on $C_c(G)$, and let $f, h \in C_c^+(G)$ with $h \neq 0$. If $f \leq \sum_i c_i\,L_{g_i}h$ then $I'(f) \leq \sum_i c_i\,I'(h)$ by positivity and invariance, and taking the infimum over such families gives

$$
I'(f) \leq (f:h)\,I'(h) ; \qquad \text{exchanging } f \text{ and } h, \qquad I'(h) \leq (h:f)\,I'(f) .
$$

Hence the ratio $I'(f)/I'(h)$ is trapped between $1/(h:f)$ and $(f:h)$ for every pair. The covering numbers of the construction satisfy $(f:\chi_V)/(h:\chi_V) \to I(f)/I(h)$ and $(f:\chi_V)(\chi_V:f) \to 1$ as the compact neighbourhood $V$ shrinks to $\{e\}$; substituting $h = \chi_V$ in the two inequalities and letting $V$ shrink therefore squeezes $I'(f)/I'(h)$ onto the single value $I(f)/I(h)$, which is independent of $I'$. Fixing $h$ and putting $c = I'(h)/I(h)$ gives $I' = cI$. $\square$

**Theorem (properties).** Let $\mu$ be a left Haar measure on a locally compact group $G$.

**(a)** $\mu(U) > 0$ for every nonempty open set $U$, and $\mu(K) < \infty$ for every compact set $K$; the support of $\mu$ is all of $G$.

**(b)** $\mu$ is inner regular on open sets and outer regular on Borel sets; it is $\sigma$-finite when $G$ is $\sigma$-compact.

**(c)** If $G$ is compact then $\mu(G) < \infty$ and $\mu$ can be normalised so that $\mu(G) = 1$; then $\mu$ is also right-invariant and is the unique invariant probability measure on $G$.

**(d)** If $G$ is discrete then the counting measure is a Haar measure, and it is the only one up to scale.

**Proof.** (a) Suppose $\mu(V) = 0$ for a nonempty open $V$. By inner regularity and the nontriviality of $\mu$ there is a compact set $K$ with $0 < \mu(K) < \infty$, and the translates $gV$ of $V$ cover $G$, so finitely many cover $K$ by compactness: $K \subseteq \bigcup_{i=1}^n g_iV$. Then $0 < \mu(K) \leq \sum_i \mu(g_iV) = n\mu(V) = 0$, a contradiction; hence $\mu(V) > 0$. Compact sets have finite measure by the definition of a Radon measure, and the support statement follows from positivity on nonempty open sets. (b) is the definition of Radon. (c) A compact group has finite Haar measure because $G$ is compact and $\mu$ is finite on compact sets; normalising gives $\mu(G) = 1$. For unimodularity, the modular function maps the compact group $G$ into the compact subgroup $\Delta(G) \subseteq \mathbb{R}_{>0}$, and $\mathbb{R}_{>0}$ has no nontrivial compact subgroup, so $\Delta \equiv 1$ and $\mu$ is right-invariant as well. (d) The counting measure is invariant under both translations, and uniqueness gives the statement. $\square$

### The Modular Function and Unimodularity

A left Haar measure need not be right-invariant; the failure is measured by a homomorphism.

**Definition.** Let $\mu$ be a left Haar measure on a locally compact group $G$. For $g \in G$ the map $A \mapsto \mu(Ag)$ is again a left Haar measure, so there is $\Delta(g) > 0$ with

$$
\mu(Ag) = \Delta(g)\,\mu(A)
$$

for every Borel set $A$. The function $\Delta : G \to \mathbb{R}_{>0}$ is the **modular function** of $G$; $G$ is **unimodular** if $\Delta \equiv 1$.

**Theorem.** The modular function is a continuous homomorphism, and it is independent of the choice of left Haar measure. The right Haar measures are the measures $\Delta^{-1}\mu$: explicitly

$$
d\mu_R(g) = \Delta(g)^{-1}\, d\mu_L(g),
$$

so that $\mu_R(A) = \mu_L(A^{-1})$ up to a constant. Moreover $\Delta$ is trivial on the commutator subgroup, and $G$ is unimodular if and only if $\Delta \equiv 1$, that is, if and only if $\ker\Delta = G$.

**Proof.** For Borel $A$ and $g, h \in G$, $\mu(Agh) = \Delta(gh)\mu(A)$ and also $\mu(Agh) = \Delta(h)\mu(Ag) = \Delta(h)\Delta(g)\mu(A)$, so $\Delta$ is a homomorphism. Continuity: $\Delta$ is measurable as a pointwise limit of the measurable functions $g \mapsto \mu(Ag)/\mu(A)$ and a measurable homomorphism of a locally compact group into $\mathbb{R}_{>0}$ is continuous (the standard automatic-continuity argument, using that a measurable homomorphism is continuous on a neighbourhood of the identity and hence everywhere). Independence of the choice: replacing $\mu$ by $c\mu$ does not change the ratio. Triviality on the commutator: $\Delta$ takes values in the abelian group $\mathbb{R}_{>0}$, so it factors through the abelianisation $G/[G,G]$. Finally $\mu_R(A) := \mu_L(A^{-1})$ is right-invariant, because $\mu_R(Ah) = \mu_L(h^{-1}A^{-1}) = \mu_L(A^{-1}) = \mu_R(A)$; the relation $d\mu_R = \Delta^{-1}d\mu_L$ is the standard computation $\mu_L(A^{-1}) = \int_A \Delta(g)^{-1}\,d\mu_L(g)$. $\square$

**Example (the affine group is not unimodular).** Let

$$
G = \Bigl\{(a, b) : a \in \mathbb{R}_{>0},\ b \in \mathbb{R}\Bigr\}, \qquad (a, b)(a', b') = (aa',\ ab' + b),
$$

the group of affine transformations $x \mapsto ax + b$ of the line, written as pairs. Its multiplication is smooth, so $G$ is a Lie group of dimension $2$. The left Haar measure is $\mu_L = a^{-2}\,da\,db$ and the modular function is

$$
\Delta(a, b) = a^{-1},
$$

so $G$ is not unimodular. The verification is a Jacobian computation. Right translation by $(a,b)$ is the map $\varphi(x,y) = (xa, xb + y)$ with Jacobian matrix $\begin{pmatrix} a & 0 \\ b & 1 \end{pmatrix}$ of determinant $a$, so for a measure with density $\rho$ the pushforward has density $a^{-1}\rho(\varphi^{-1}(u,v))$; taking $\rho(x,y) = x^{-2}$ gives $\rho(\varphi^{-1}(u,v)) = (u/a)^{-2} = a^2 u^{-2}$ and the pushforward density $a\,u^{-2}$, that is $(R_{(a,b)})_*\mu_L = a\,\mu_L$. Hence $\mu_L(A(a,b)^{-1}) = a\,\mu_L(A)$, equivalently $\mu_L(A(a,b)) = a^{-1}\mu_L(A)$, so $\Delta(a,b) = a^{-1}$. The right Haar measure is accordingly $a^{-1}\,da\,db$, and it differs from the left one.

**Theorem (classes of unimodular groups).** The following locally compact groups are unimodular: abelian groups; compact groups; discrete groups; nilpotent groups; groups equal to their commutator subgroup, and groups whose commutator subgroup is dense; and semisimple Lie groups. A locally compact group containing a closed non-unimodular subgroup is non-unimodular, since the modular function of the closed subgroup is the restriction of the modular function of the group.

**Proof.** Abelian groups are unimodular because left and right translation coincide; this is the proposition of *Abelian Topological Groups*, §The Additive Setting, and the same argument covers the discrete case with the counting measure. A compact group is unimodular by the normalisation in the theorem above. A group equal to its commutator subgroup has $\Delta \equiv 1$ because $\Delta$ is a homomorphism to the abelian group $\mathbb{R}_{>0}$ and therefore kills the commutator subgroup; density of the commutator subgroup gives the same by continuity. A semisimple Lie group is unimodular because its abelianisation is finite, so a continuous homomorphism to the abelian group $\mathbb{R}_{>0}$ is trivial. For a nilpotent group: on the identity component, which is a pro-Lie group with nilpotent Lie algebra $\mathfrak{g}$, the adjoint action is unipotent, $\operatorname{Ad}(\exp X) = \exp(\operatorname{ad}_X)$ has determinant $1$, and the modular function of a connected Lie group is $|\det \operatorname{Ad}|$, hence trivial; a compact open subgroup of the totally disconnected part has compact image in $\mathbb{R}_{>0}$ under $\Delta$, hence image $\{1\}$, and these subgroups cover $G$ locally, so $\Delta \equiv 1$ on all of $G$. The final statement: if $G$ contains a closed non-unimodular subgroup $H$, then $\Delta_G$ restricts to $\Delta_H$ and is therefore nontrivial. $\square$

**Remark.** The classes overlap, and none contains the others: the Heisenberg group is nilpotent hence unimodular but its left and right uniformities differ, as recorded in *Topological Groups*; the affine group is solvable and non-unimodular; a finite group is both compact and discrete and unimodular.

## Haar Measure on the Standard Examples

**Example ($\mathbb{R}^n$).** Lebesgue measure $d\mu = dx_1 \cdots dx_n$ is the Haar measure of $(\mathbb{R}^n, +)$; it is the unique translation-invariant Radon measure up to scale, and $\Delta \equiv 1$. On $\mathbb{R}^\times$ with multiplication, the invariant measure is $dx/|x|$: the substitution $x \mapsto ax$ scales $dx$ by $|a|$ and $|x|$ by $|a|$, so $dx/|x|$ is invariant, and $\mathbb{R}^\times$ is abelian hence unimodular.

**Example (the circle and the torus).** On $S^1 = \mathbb{R}/\mathbb{Z}$ the normalised Haar measure is $d\theta$ with total mass $1$, obtained from Lebesgue measure on $[0,1)$; on $T^n$ it is the product measure of total mass $1$. These are the invariant probability measures of the compact groups, and $\Delta \equiv 1$.

**Example (discrete groups and $\mathbb{Z}$).** The counting measure is Haar on a discrete group; on $\mathbb{Z}$ it is the measure of mass $1$ at each integer, and the invariant sum $\sum_{n \in \mathbb{Z}} f(n)$ is its functional form.

**Example (the $p$-adic line).** On $\mathbb{Q}_p$ the Haar measure is normalised by $\mu(\mathbb{Z}_p) = 1$; then $\mu(p^k\mathbb{Z}_p) = p^{-k}$ for $k \in \mathbb{Z}$, and the measure is the unique Haar measure of the additive group with that normalisation. The compact group $\mathbb{Z}_p$ has Haar measure of total mass $1$, and the profinite group $\prod_p \mathbb{Z}_p = \hat{\mathbb{Z}}$ carries the product of the normalised Haar measures, under which it is a probability space; its integration is the limit of the finite sums over the quotients $\mathbb{Z}/n\mathbb{Z}$.

**Example ($GL_n(\mathbb{R})$ and $GL_n(\mathbb{C})$).** The group $GL_n(\mathbb{R})$, as an open subset of $M_n(\mathbb{R}) \cong \mathbb{R}^{n^2}$, carries the measure

$$
d\mu(A) = |\det A|^{-n}\, dA,
$$

with $dA$ Lebesgue measure, and this is a bi-invariant Haar measure: $GL_n(\mathbb{R})$ is unimodular. Indeed, left translation $A \mapsto BA$ has Jacobian $|\det B|^n$ on the vector space $M_n(\mathbb{R})$, and $|\det(BA)|^{-n} = |\det B|^{-n}|\det A|^{-n}$, so the density is transported to itself. The same computation over $\mathbb{C}$, with $dA$ Lebesgue measure on $\mathbb{C}^{n^2}$ and the modulus of the complex determinant, gives $|\det A|^{-2n}\,dA$ for $GL_n(\mathbb{C})$.

**Example (compact Lie groups).** On a compact Lie group $G$ of dimension $n$ with a left-invariant volume form $\omega$, the Haar measure is $|\omega|$, normalised so that the total volume is $1$. For $SU(2) \cong S^3$ the normalised Haar measure is the normalised surface measure on the unit sphere, and for $SO(3) \cong \mathbb{RP}^3$ it is the pushforward of that measure under the two-to-one cover, which is why the class function theory uses the sphere parametrisation.

## Quotients and Homogeneous Spaces

### Quasi-Invariant Measures

Let $H$ be a closed subgroup of a locally compact group $G$ and let $G/H$ be the homogeneous space of left cosets, a locally compact Hausdorff space.

**Definition.** A Radon measure $\nu$ on $G/H$ is **quasi-invariant** under the left action of $G$ if for every $g \in G$ the measures $\nu$ and $g_*\nu$ have the same null sets, equivalently $\nu(gA) = 0$ if and only if $\nu(A) = 0$. It is **invariant** if $\nu(gA) = \nu(A)$ for all $g$ and all Borel $A$.

**Theorem.** Let $H$ be a closed subgroup of a locally compact group $G$. Then $G/H$ carries a nonzero quasi-invariant Radon measure, unique up to equivalence and up to a positive scalar; it carries a nonzero invariant Radon measure if and only if

$$
\Delta_G\big|_H = \Delta_H ,
$$

that is, the modular function of $G$ restricts to the modular function of $H$. In that case the invariant measure is unique up to a positive scalar.

**Proof sketch.** Choose left Haar measures $\mu_G$ on $G$ and $\mu_H$ on $H$. For $f \in C_c(G)$ the function $h \mapsto f(gh)$ has compact support in $H$ for each $g$, so the inner integral $F(g) = \int_H f(gh)\,d\mu_H(h)$ is defined and continuous in $g$, and it satisfies $F(gh_0) = \Delta_H(h_0)^{-1}F(g)$ for $h_0 \in H$: a right translate of the variable of integration changes the Haar measure of $H$ by the factor $\Delta_H(h_0)$. There is therefore a positive continuous transfer function $\rho$ on $G$ with $\rho(gh) = \rho(g)\,\Delta_G(h)\,\Delta_H(h)^{-1}$ for $h \in H$ (extend the character $\Delta_G\Delta_H^{-1}$ of $H$ to a positive continuous function and average against a partition of unity), and the standard formula of Weil

$$
\int_G f(g)\,\rho(g)\,d\mu_G(g) = \int_{G/H}\Bigl(\int_H f(gh)\,d\mu_H(h)\Bigr)d\nu(gH)
$$

defines a nonzero Radon measure $\nu$ on $G/H$; the factor $\rho$ is exactly what corrects the equivariance of $F$, so $\nu$ is well defined. The measure $\nu$ is quasi-invariant in general, and it is invariant exactly when $\rho$ can be chosen to be right-$H$-invariant, that is, exactly when $\Delta_G(h) = \Delta_H(h)$ for all $h \in H$. Changing $\rho$ multiplies $\nu$ by a positive continuous density and rescaling $\nu$ changes it by a positive scalar, which gives the uniqueness statements; the local construction of an arbitrary quasi-invariant measure from the formula is the standard reduction, and the two measures differ by a Radon–Nikodym cocycle. $\square$

**Theorem (Weil's integral formula).** Let $H$ be a closed subgroup of a locally compact group $G$, let $\mu_G$ be a left Haar measure, $\mu_H$ a left Haar measure, and $\nu$ a quasi-invariant measure on $G/H$ with cocycle $\rho$. Then for $f \in C_c(G)$,

$$
\int_G f(g)\,d\mu_G(g) = \int_{G/H}\int_H f(gh)\,\rho(g,h)\,d\mu_H(h)\,d\nu(gH) ,
$$

where the cocycle reduces to a constant when the invariance criterion holds. In particular the double integral of a compactly supported continuous function is well defined in either order.

**Proof sketch.** The functional $f \mapsto \int_G f\,d\mu_G$ is positive and left-invariant; the iterated functional is positive and left-invariant, and uniqueness of Haar measure on the product forces them to be proportional. The proportionality constant is fixed by a test function supported in a small neighbourhood of $e$ over which the projection $G \to G/H$ admits a local section; the cocycle appears because the local sections change by the action of $H$, and its form is forced by the descent condition. $\square$

**Example (lattices and finite volume).** If $\Gamma \subseteq G$ is a discrete subgroup of a locally compact group $G$ and the invariant measure on $G/\Gamma$ is finite of positive total mass, then $\Gamma$ is a **lattice** and that total mass is the **covolume**; the criterion $\Delta_G|_\Gamma = \Delta_\Gamma$ reduces to $\Delta_G|_\Gamma = 1$, because a discrete group has $\Delta_\Gamma \equiv 1$, and it holds automatically since a group that admits a lattice is unimodular. Lattices in Lie groups are the subject, and the finite covolume there is the Haar volume of this article. For $G = SL_n(\mathbb{R})$ and $\Gamma = SL_n(\mathbb{Z})$ the quotient has finite volume because $\Gamma$ is a lattice, and the construction of the finite measure on $G/\Gamma$ is the reduction theory of Mahler and Siegel.

**Example (the modular function of a quotient group).** If $N \trianglelefteq G$ is a closed normal subgroup then $G/N$ is locally compact, but $\Delta_{G/N}$ is **not** in general the composite of $\Delta_G$ with the quotient map: for the affine group $G$ above and its normal subgroup $N = \{(1,b)\}$ of translations, the quotient $G/N \cong \mathbb{R}_{>0}$ is abelian, hence unimodular, while $\Delta_G(a,b) = a^{-1}$ is nontrivial on the elements projecting to an $a \neq 1$. The relation $\Delta_{G/N} = \Delta_G \circ \pi$ does hold for a direct product of unimodular factors, $\Delta_{N \times H} = \Delta_N \cdot \Delta_H$. In general the kernel of $\Delta_G$ is a closed normal unimodular subgroup of $G$ with abelian quotient embedded in $\mathbb{R}_{>0}$, and $G$ is unimodular exactly when that kernel is all of $G$.

## The Boundary with Analysis

The Haar measure is an object of the topological theory; the analysis built on it is not.

- The **spaces $L^p(G)$** ($1 \leq p \leq \infty$), the completeness and duality of $L^2(G)$, and the **convolution algebra** $L^1(G)$ with the involution $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ are *Analysis on Groups* in Part III, beginning and continuing.
- The **regular representation** of $G$ on $L^2(G)$, the **Peter–Weyl theorem** for a compact group and the **Plancherel theorem** for a unimodular group are likewise Part III; the algebraic skeleton — unitary representations, irreducibility and intertwiners — is the subject, which uses the Haar measure only through the invariance defining integration over $G$.
- The **modular function** appears in the analysis in the formula for the adjoint of a convolution and in the definition of the group von Neumann algebra; both are Part III or the operator-algebra articles of *Topology on Linear Algebras*.

## Summary

A locally compact group is a Hausdorff topological group in which every point has a compact neighbourhood; the class contains the discrete, compact, Lie, Euclidean and $p$-adic examples and is exactly the class for which invariant integration is available. Haar's theorem gives a nonzero left-invariant Radon measure, unique up to positive scale; it is positive on nonempty open sets, finite on compact sets, of full support, and is a probability measure on a compact group and the counting measure on a discrete group.

The failure of right-invariance is measured by the modular function $\Delta : G \to \mathbb{R}_{>0}$, a continuous homomorphism with $\mu(Ag) = \Delta(g)\mu(A)$ and $d\mu_R = \Delta^{-1}d\mu_L$. The group is unimodular exactly when $\Delta \equiv 1$, which holds for abelian, compact, discrete, nilpotent, perfect and semisimple groups; the affine group of the line is the standard non-unimodular example, with $\mu_L = a^{-2}da\,db$, $\mu_R = a^{-1}da\,db$ and $\Delta(a,b) = a^{-1}$. Haar measure is computed explicitly on $\mathbb{R}^n$, $S^1$, $T^n$, $\mathbb{Z}$, $\mathbb{Z}_p$, $\mathbb{Q}_p$, $GL_n(\mathbb{R})$, $GL_n(\mathbb{C})$ and the compact Lie groups.

For a closed subgroup $H$ the homogeneous space $G/H$ carries a quasi-invariant Radon measure, and an invariant one exactly when $\Delta_G|_H = \Delta_H$; Weil's formula expresses integration over $G$ as an iterated integral over $H$ and $G/H$. All of the integration theory — the $L^p$ spaces, the convolution algebra $L^1(G)$, the regular representation, the Peter–Weyl and Plancherel theorems — belongs to *Analysis on Groups* in Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $e$ | A locally compact group and its identity |
| $G_0$ | Identity component, closed and normal |
| $G/H$ | Homogeneous space of left cosets, locally compact Hausdorff |
| $\mu$, $\mu_L$ | A left Haar measure (Radon, left-invariant, nonzero) |
| $\mu_R$ | Right Haar measure, $d\mu_R = \Delta^{-1}d\mu_L$ |
| $\Delta = \Delta_G$ | Modular function $G \to \mathbb{R}_{>0}$, $\mu(Ag) = \Delta(g)\mu(A)$ |
| unimodular | $\Delta \equiv 1$; left Haar measure is right-invariant |
| $C_c(G)$ | Continuous real- or complex-valued functions of compact support |
| $L_g f(x) = f(g^{-1}x)$ | Left translate of a function |
| $dx$, $d\theta$ | Lebesgue measure; normalised measure on the circle |
| $dx/|x|$ | Haar measure of $\mathbb{R}^\times$ |
| $a^{-2}da\,db$, $a^{-1}da\,db$ | Left and right Haar measure of the affine group |
| $|\det A|^{-n} dA$ | Bi-invariant Haar measure of $GL_n(\mathbb{R})$ |
| $\mu(\mathbb{Z}_p) = 1$ | Normalisation of the Haar measure on $\mathbb{Q}_p$ |
| $\nu$, cocycle $\rho$ | Quasi-invariant measure on $G/H$ and its Radon–Nikodym cocycle |
| lattice, covolume | Discrete $\Gamma$ with $G/\Gamma$ of finite invariant volume, and that volume |
| $L^p(G)$, $L^1(G)$ | Part III objects: the $L^p$ spaces and the convolution algebra |
| $\Delta_G|_H = \Delta_H$ | Criterion for an invariant measure on $G/H$ |



## Further Reading

- Leopoldo Nachbin, *The Haar Integral* (Van Nostrand, 1965; reprinted Krieger, 1976), for a direct construction of the Haar integral.
- Edwin Hewitt and Kenneth A. Ross, *Abstract Harmonic Analysis I* (Springer, 2nd ed. 1979), for Haar measure, the modular function and the standard examples.
- Lynn H. Loomis, *An Introduction to Abstract Harmonic Analysis* (Van Nostrand, 1953; reprinted Dover, 2011), for a concise account of invariant integration.
- Nicolas Bourbaki, *Integration II* (Springer, 2004), for Radon measures, the modular function and integration on homogeneous spaces.
- André Weil, *L'intégration dans les groupes topologiques et ses applications* (Hermann, 1940), for the integral formula on a homogeneous space.
- Gerald B. Folland, *Real Analysis* (Wiley, 2nd ed. 1999), for Radon measures, regularity and the Riesz representation theorem underlying the functional form.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for invariant measures and integration on symmetric spaces.
- Gerald B. Folland, *A Course in Abstract Harmonic Analysis* (CRC Press, 2nd ed. 2015), for Haar measure as the frame of the representation theory.
