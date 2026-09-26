
# __Homogeneous Dynamics__

## Introduction

Homogeneous dynamics is the study of a flow or a group action on a quotient $G/\Gamma$ of a Lie group by a discrete subgroup. The space is at once algebraic and geometric: the group $G$ acts transitively, so the quotient is homogeneous; the discrete group $\Gamma$ makes the quotient a finite-volume manifold in the lattice case; and the action of a one-parameter subgroup draws a flow whose orbits are the projections of the one-parameter subgroups of $G$. The subject sits at the meeting point of the algebra of the group, the geometry of the quotient and the measure theory of the ergodic theorems, and its results are often the only known route to a purely number-theoretic statement.

The central examples explain the subject. The geodesic flow on a hyperbolic surface is the flow of the diagonal subgroup of $SL_2(\mathbb{R})$ on $SL_2(\mathbb{R})/\Gamma$, and the horocycle flow is the flow of the upper unipotent subgroup; the modular surface, with $\Gamma = SL_2(\mathbb{Z})$, connects the dynamics to the arithmetic of quadratic forms. The rotation flow on a torus is the flow of a one-parameter subgroup of $\mathbb{R}^n$ on $\mathbb{R}^n/\mathbb{Z}^n$, and it is the abelian case of the same picture. The Heisenberg nilmanifold is the first genuinely non-abelian nilpotent example, and it exhibits the phenomenon — unipotent flows equidistribute — that organises the whole subject for nilpotent and, by Ratner's theorems, for general semisimple groups.

This article develops the frame: the homogeneous space $G/\Gamma$ and its invariant measure, the geodesic and horocycle flows on a hyperbolic surface, unipotent flows and their ergodicity, the abelian and nilpotent cases, the mixing of the Weyl chamber flow, the equidistribution of horocycle orbits, and the place of Ratner's theorems. Three boundaries are held.

- The **lattices**, the **arithmetic groups** and the **homogeneous spaces** themselves are Part II's: the existence and covolume of a lattice, the arithmetic construction of $\Gamma$, the geometry of $G/K$, and the symmetric and locally symmetric spaces are the subject of *Lattices in Lie Groups*, *Arithmetic Groups* and *Homogeneous Spaces*, and are used here as established. This article is the *dynamics* on those spaces.
- The **ergodic theory** used is that of *Ergodic Theory of Group Actions*: ergodicity, mixing, the Koopman representation, the Følner mean ergodic theorem, the Mautner phenomenon, Moore's theorem and the Howe–Moore theorem. The present article applies them to homogeneous spaces rather than developing them.
- The **Ratner classification** of orbit closures and invariant measures is not covered here, and the quantitative equidistribution of orbits . Where a statement belongs to those articles it is stated here only as a headline and the reader is directed there. No physics is invoked.

Throughout, $G$ is a connected Lie group with Lie algebra $\mathfrak{g}$, $K$ a maximal compact subgroup, $\Gamma$ a discrete subgroup of $G$, and $X = G/\Gamma$ the homogeneous space of left cosets with the quotient topology; $e$ is the identity, $dx$ a $G$-invariant measure when it exists, and the action is by left translation, $g \cdot x\Gamma = gx\Gamma$. A **lattice** is a discrete subgroup $\Gamma$ for which $G/\Gamma$ carries a finite $G$-invariant measure; $\Gamma$ is **uniform** or cocompact when $G/\Gamma$ is compact. The Lie functor is that of *The Lie Algebra and the Exponential Map*, and $\operatorname{Ad}$ is the adjoint representation of *The Lie Correspondence and the Adjoint Representation*.

## Homogeneous Spaces and Lattices

### The Quotient Space

**Definition.** Let $G$ be a locally compact group and $\Gamma$ a discrete subgroup. The **homogeneous space** $G/\Gamma$ is the set of left cosets $\{g\Gamma\}$ with the quotient topology; $G$ acts on it by left translation, $g \cdot x\Gamma = gx\Gamma$.

The action is transitive, which is the sense in which the space is homogeneous, and the stabiliser of the coset $g\Gamma$ is the conjugate $g\Gamma g^{-1}$. When $G$ is a Lie group and $\Gamma$ is discrete, $G/\Gamma$ is a smooth manifold of dimension $\dim G$ with a smooth free action of $G$, and every orbit is dense in a component of the quotient by the closure of $\Gamma$.

**Theorem (invariant measure).** Let $G$ be unimodular — for instance a connected nilpotent or semisimple Lie group — with Haar measure $dg$, and let $\Gamma$ be a lattice. Then there is a unique (up to scale) $G$-invariant Radon measure $\mu$ on $G/\Gamma$, obtained by integrating over a fundamental domain: $\int_{G/\Gamma} f \, d\mu = \int_{G} \tilde f(g)\, dg$ for a $\Gamma$-invariant lift $\tilde f$ of $f$.

*Proof.* The function $g \mapsto \sum_{\gamma \in \Gamma}\tilde f(g\gamma)$ is left $\Gamma$-invariant and converges for $\tilde f$ of compact support because $\Gamma$ is discrete; the invariance of $dg$ under left translations gives the left invariance of the resulting functional, and the uniqueness of the Haar measure gives its uniqueness. The finiteness $\mu(G/\Gamma) = \operatorname{vol}(G/\Gamma) < \infty$ is the definition of a lattice. $\square$

The **covolume** $\operatorname{vol}(G/\Gamma)$ is the common value; for a cocompact lattice the quotient is compact and the volume finite, and for an arithmetic lattice the volume can be computed by the formula of Weil. The existence of lattices is a theorem of Borel for semisimple groups: every connected semisimple Lie group without compact factors contains both uniform and non-uniform lattices.

### The Standard Examples

**Example ($\mathbb{R}^n/\mathbb{Z}^n$).** For $G = \mathbb{R}^n$ and $\Gamma = \mathbb{Z}^n$ the homogeneous space is the $n$-torus $T^n$, a compact homogeneous space of volume $1$. The flow of a one-parameter subgroup is the translation flow $x \mapsto x + t\alpha$ for a fixed vector $\alpha$, and the line generated by $\alpha$ is dense exactly when $1, \alpha_1, \dots, \alpha_n$ are rationally independent; this is the abelian case of the whole theory, and it is where the equidistribution results beg.

**Example (the modular surface).** For $G = SL_2(\mathbb{R})$ and $\Gamma = SL_2(\mathbb{Z})$ the quotient $G/\Gamma$ is not compact but has finite volume: it is the unit tangent bundle of the modular surface $SL_2(\mathbb{Z})\backslash\mathbb{H}$, where $\mathbb{H}$ is the upper half-plane. The modular surface is a hyperbolic surface of finite area, with one cusp and two singular points of orders $2$ and $3$, corresponding to the elliptic elements of $\Gamma$.

**Example (higher-rank).** For $G = SL_n(\mathbb{R})$ and $\Gamma = SL_n(\mathbb{Z})$ the quotient $SL_n(\mathbb{R})/SL_n(\mathbb{Z})$ is non-compact of finite volume for $n \geq 2$, and it carries the dynamics of the Weyl chamber flow, the higher-dimensional analogue of the geodesic flow. Its diagonal subgroup has rank $n-1$, so the flow is a $\mathbb{Z}^{n-1}$- or $\mathbb{R}^{n-1}$-action rather than a single flow, and the ergodic theory of *Ergodic Theory of Group Actions* applies to this action rather than to a one-parameter group.

**Example (compact quotients of hyperbolic space).** If $\Gamma \le SL_2(\mathbb{R})$ is a cocompact torsion-free lattice, then $\Gamma\backslash\mathbb{H}$ is a compact hyperbolic surface and $G/\Gamma$ is its unit tangent bundle; the dynamics of $G$ on $G/\Gamma$ is then the geodesic flow on a compact surface, without the cusps of the modular case.

## The Geodesic and Horocycle Flows

### The Upper Half-Plane

The model space is $\mathbb{H} = \{z \in \mathbb{C} : \operatorname{Im} z > 0\}$ with the hyperbolic metric $ds^2 = (dx^2 + dy^2)/y^2$ of constant curvature $-1$. The group $PSL_2(\mathbb{R})$ acts on $\mathbb{H}$ by

$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix} \cdot z = \frac{az+b}{cz+d},
$$

transitively and by isometries, and the map $g \mapsto g \cdot i$ identifies $\mathbb{H}$ with $PSL_2(\mathbb{R})/PSO(2)$. The unit tangent bundle is then $PSL_2(\mathbb{R})/PSO(2)$ itself, and a lattice $\Gamma \le PSL_2(\mathbb{R})$ acts on the left, so the unit tangent bundle of $\Gamma\backslash\mathbb{H}$ is the homogeneous space $\Gamma\backslash PSL_2(\mathbb{R})$.

### The Two Flows

**Definition.** In $G = PSL_2(\mathbb{R})$ the **diagonal (geodesic) subgroup** and the **horocycle subgroup** are

$$
A = \left\{ a_s = \begin{pmatrix} e^{s/2} & 0 \\ 0 & e^{-s/2} \end{pmatrix} : s \in \mathbb{R} \right\}, \qquad
U = \left\{ u_t = \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix} : t \in \mathbb{R} \right\}.
$$

The **geodesic flow** on $G/\Gamma$ is the action of $A$, and the **horocycle flow** is the action of $U$. The two are linked by the commutation relation

$$
a_s u_t a_s^{-1} = \begin{pmatrix} 1 & e^{s}t \\ 0 & 1 \end{pmatrix} = u_{e^{s}t},
$$

which is the contraction relation of the Mautner phenomenon.

Geometrically, the $A$-orbit of a unit tangent vector is the geodesic through its base point in the direction of the vector, and the $U$-orbit is the horocycle through that point, the orbit of the parabolic one-parameter group corresponding to the limit point of the geodesic.

**Theorem (ergodicity of the geodesic flow).** Let $\Gamma \le PSL_2(\mathbb{R})$ be a lattice. The geodesic flow on $G/\Gamma$ is ergodic with respect to the invariant measure, and it is mixing.

*Proof.* The horocycle flow is ergodic: its orbits are the leaves of the stable foliation, and a $U$-invariant function is constant by the classification of the ergodic measures of the horocycle flow together with the density of the horocycle orbit in the non-compact case. By the commutation relation above, $A$ contracts $U$, so the Mautner phenomenon of *Ergodic Theory of Group Actions* shows that every $A$-invariant function is $U$-invariant, hence constant. Ergodicity follows. Mixing is the Howe–Moore theorem applied to the Koopman representation on the mean-zero part, which has no invariant vectors by ergodicity. $\square$

**Remark (the cusp).** For a non-uniform lattice the quotient is not compact, and the geodesic flow is not uniformly continuous in the sense of the flow being bounded away from the cusp; the ergodicity statement is the same, but the proof must control the visits of the orbit to the cusp. The horocycle flow, by contrast, is **minimal** — every orbit is dense — and **uniquely ergodic**, a theorem of Furstenberg; the geodesic flow is not minimal, and its orbit closures are the geodesics, which are either closed or dense.

## Unipotent Flows

### Unipotent One-Parameter Subgroups

**Definition.** An element $g$ of a Lie group $G$ is **unipotent** if $\operatorname{Ad}(g)$ is a unipotent linear transformation — that is, $\operatorname{Ad}(g) - I$ is nilpotent — and a one-parameter subgroup $\{u_t\}$ is **unipotent** if each $u_t$ is unipotent and the map $t \mapsto \operatorname{Ad}(u_t) - I$ is polynomial in $t$ of bounded degree. An element is **semisimple** if $\operatorname{Ad}(g)$ is diagonalisable over $\mathbb{C}$.

The Jordan decomposition of $\operatorname{Ad}(g)$ writes every element as the product of a commuting semisimple and unipotent part, so every element of a Lie group has a unipotent part; the flow generated by a unipotent element is the simplest kind of flow after the semisimple ones, and it is the one for which the rigidity theorems hold.

**Example.** The horocycle subgroup $U \le SL_2(\mathbb{R})$ is unipotent: $\operatorname{Ad}(u_t) - I$ is nilpotent with square zero. The subgroup generated by $u_t$ and its transpose $u_t^-$ is the whole of $SL_2(\mathbb{R})$, and the commutator $[u_t, u_s^-]$ is a diagonal element, which is the algebraic reason the two horocycle directions generate the geodesic direction.

**Example (the Heisenberg group).** Let $N$ be the group of upper unitriangular $3\times3$ real matrices, with the coordinates

$$
(x, y, z) = \begin{pmatrix} 1 & x & z \\ 0 & 1 & y \\ 0 & 0 & 1 \end{pmatrix}, \qquad (x,y,z)(x',y',z') = (x+x', y+y', z+z'+xy').
$$

Its Lie algebra is generated by $X, Y, Z$ with $[X,Y] = Z$ and $Z$ central. Every one-parameter subgroup other than the centre direction is unipotent, and the centre direction is semisimple but acts trivially on the quotient by the lattice.

### Ergodicity of Unipotent Flows

**Theorem (Dani).** Let $G$ be a connected semisimple Lie group and $\Gamma$ a lattice. Let $\{u_t\}$ be a unipotent one-parameter subgroup of $G$ generated by an element of a simple factor. Then the flow $u_t$ on $G/\Gamma$ is ergodic with respect to the invariant measure if and only if no element of $g\Gamma g^{-1}$ lies in a proper parabolic subgroup of $G$ containing $u_t$; in particular, the flow is ergodic for a.e. $g$ and, for $G$ simple of rank one, it is ergodic for every $g$.

Dani's theorem is the unipotent counterpart of Moore's theorem; it says that the unipotent flow cannot be trapped by an algebraic subgroup unless the orbit is confined to a smaller homogeneous subspace, and it is the local form of Ratner's classification. For $G = SL_2(\mathbb{R})$ it reduces to the ergodicity of the horocycle flow, which is Furstenberg's theorem, and for nilpotent groups the corresponding statement is unconditional.

**Theorem (ergodicity on nilmanifolds).** Let $N$ be a connected simply connected nilpotent Lie group with a lattice $\Gamma$, and let $\{u_t\}$ be a one-parameter subgroup. Then the flow on $N/\Gamma$ is ergodic if and only if the image of the generator in the abelianisation $\mathfrak{n}/[\mathfrak{n},\mathfrak{n}]$ lies outside the union of the rational hyperplanes of the lattice $\Gamma$, and the flow is then uniquely ergodic with respect to the Haar measure.

The nilpotent case is the model: the flow is a translation on a nilmanifold, and the criterion is exactly the rational-independence criterion of the torus, transported to the abelianisation. The higher commutators supply the corrections that make the flow non-abelian but do not change the ergodicity criterion.

## Nilmanifolds and the Abelian Case

### The Torus

The simplest homogeneous flow is the translation flow on $T^n = \mathbb{R}^n/\mathbb{Z}^n$ generated by $\alpha \in \mathbb{R}^n$. Its orbits are the images of the lines $t \mapsto t\alpha$; the orbit is dense precisely when the coordinates $1, \alpha_1, \dots, \alpha_n$ are rationally independent, and then the flow is uniquely ergodic with respect to Lebesgue measure. Every higher-dimensional nilmanifold is a successive $\mathbb{R}$-bundle over a torus, and this abelian base accounts for the rational-independence part of the ergodicity criterion.

### The Heisenberg Nilmanifold

**Example.** Let $N$ be the Heisenberg group and $\Gamma = N(\mathbb{Z})$ the integer points. The quotient $N/\Gamma$ is a compact three-manifold, a circle bundle over $T^2$; the projection to the abelianisation is $(x,y,z)\Gamma \mapsto (x,y) + \mathbb{Z}^2$. The centre direction $z$ is a circle, and the flow generated by $Z$ is periodic: its orbits are the fibres. The flow generated by $X$ alone, $\{u_t\}$ with $u_t(x,y,z) = (x+t, y, z + ty)$, is unipotent; its orbits are the lifts of lines of slope $0$ in the base, and they are dense in the nilmanifold, the flow being uniquely ergodic. The flow generated by $X + \lambda Y$ has orbits that are the lifts of lines of slope $\lambda$ and is ergodic for every $\lambda$, exactly as the abelian criterion along the base predicts.

The nilmanifold case is the natural testing ground for the general statements. The following is the clean form of the classification for unipotent flows on nilmanifolds, and it is a theorem of Leon Green, Parry and Auslander.

**Theorem (Green, Parry, Auslander).** Let $N$ be a connected simply connected nilpotent Lie group, $\Gamma$ a lattice, and $H$ a connected closed subgroup of $N$ acting on $N/\Gamma$ by left translation. Then the orbit closure $\overline{Hx}$ is a finite union of $H$-orbits, each of which is the orbit of $x$ under a closed subgroup $L$ with $L \supseteq H$ and $L \cap x\Gamma x^{-1}$ cocompact in $L$; consequently the action of $H$ on $N/\Gamma$ is uniquely ergodic if and only if it is minimal.

The theorem is the nilpotent case of Ratner's topological classification, and its proof by the "one-dimensional" reduction via the lower central series is the model for the general proof.

## Ergodicity and Mixing of Higher-Rank Actions

### Weyl Chamber Flows

For a semisimple group $G$ of real rank at least two the diagonal subgroup $A$ is no longer one-dimensional; it is a product $A \cong \mathbb{R}^r$, and the action of $A$ on $G/\Gamma$ is the **Weyl chamber flow**, with $r$ independent directions. The ergodic theory of the flow is the ergodic theory of a $\mathbb{Z}^r$- or $\mathbb{R}^r$-action, and it is genuinely different from the rank-one case: the action can be ergodic without any single direction being ergodic, and the mixing properties are governed by the geometry of the chamber.

**Theorem (ergodicity of the Weyl chamber flow).** Let $G$ be a connected semisimple Lie group with finite centre and no compact factors, and let $\Gamma$ be an irreducible lattice. Then the action of $A$ on $G/\Gamma$ is ergodic, and it is mixing.

*Proof.* Ergodicity is Moore's theorem applied to the factors: an $A$-invariant function that is not constant would define a nonzero invariant vector in a representation of a simple factor, contradicting the irreducibility of the lattice. Mixing is the Howe–Moore theorem, whose decay statement holds for the whole group $G$ and hence for $A$; the mean-zero part of $L^2$ has no invariant vectors by ergodicity. $\square$

**Example (the modular surface revisited by a higher-rank action).** For $G = SL_n(\mathbb{R})$, $n \geq 3$, and $\Gamma = SL_n(\mathbb{Z})$ the diagonal subgroup has rank $n-1$, and the Weyl chamber flow mixes. A single diagonal one-parameter subgroup is the horospherical flow of a rank-one subgroup, and its ergodicity follows from the Mautner phenomenon applied to the unipotent subgroup contracted by it; the passage from rank one to higher rank is exactly the passage from a single geodesic to the whole chamber, and it is what makes the higher-rank dynamics rigid.

### Rigidity

**Theorem (Mostow rigidity, dynamical form).** Let $G$ and $G'$ be connected semisimple Lie groups with no compact factors, trivial centre and real rank at least $2$, and let $\Gamma \le G$, $\Gamma' \le G'$ be irreducible lattices. Then any isomorphism of the measure spaces $G/\Gamma$ and $G'/\Gamma'$ that conjugates the $G$-action to the $G'$-action is, up to a normalising factor, the restriction of an isomorphism of Lie groups; there is no measurable deformation of an irreducible lattice in higher rank.

The dynamical reading is that in higher rank the action of $G$ on $G/\Gamma$ determines $G$ and $\Gamma$ up to finitely many possibilities, so the flow is rigid, in contrast with the rank-one case where the Teichmüller space of a surface supplies a continuum of non-isomorphic lattices. The rigidity is proved by the theory of the Weyl chamber flow, and it is the reason the higher-rank theory has a different flavour: there are no continuous deformations to average over.

## Equidistribution of Orbits

### Horocycle Orbits

**Theorem (Furstenberg).** Let $\Gamma \le SL_2(\mathbb{R})$ be a lattice and let $x \in G/\Gamma$. Then the horocycle orbit $\{u_t x : t \in \mathbb{R}\}$ is equidistributed in $G/\Gamma$ with respect to the invariant measure:

$$
\frac{1}{T}\int_0^T f(u_t x)\, dt \longrightarrow \int_{G/\Gamma} f \, d\mu \qquad \text{as } T \to \infty,
$$

for every $f \in C_c(G/\Gamma)$. In particular the horocycle flow is uniquely ergodic.

The theorem is the prototype of all equidistribution results of the subject, and it is the statement that the time average along every horocycle equals the space average; it holds for every point $x$, not merely almost every one, which is the sense of unique ergodicity. The proof uses the commutation relation $a_s u_t a_s^{-1} = u_{e^s t}$ to rescale the horocycle, together with the ergodicity of the geodesic flow; the two flows are two sides of the same ergodic theorem.

**Corollary (equidistribution of horocycles over closed geodesics).** If $x$ is a point whose geodesic returns to a neighbourhood of itself — a periodic point of the geodesic flow — then the horocycle through $x$ equidistributes, and the equidistribution is uniform over the set of points with the same period.

This last statement is the geometric form of Duke's theorem on the equidistribution of Heegner points and of the equidistribution of closed horocycles; the arithmetic content is that the quadratic irrationals are equidistributed in the modular surface ordered by discriminant, and the dynamical content is the unique ergodicity of the horocycle flow. The general quantitative statement lies outside this article.

### From Nilmanifolds to Semisimple Groups

**Example (equidistribution of polynomial sequences).** On the torus $T^n$ the equidistribution of the sequence $\{n\alpha\}$ is Weyl's theorem, and its generalisation to polynomial sequences, $n \mapsto p(n)\alpha$ with $p$ a polynomial, is the theorem of Weyl and of Green: the sequence is equidistributed unless the polynomial takes values in a coset of a proper closed subgroup. This is the abelian model of the general equidistribution theorem for unipotent flows.

**Example (equidistribution of translates).** Let $H \le G$ be a connected subgroup generated by unipotent elements, and let $x \in G/\Gamma$. Then the closure of the orbit $Hx$ is a homogeneous subspace $Lx$ with $L \supseteq H$, and the orbit is equidistributed in $Lx$ with respect to the invariant measure of $Lx$ after normalisation. This single statement contains most of the classical equidistribution theorems as special cases, and it is Ratner's equidistribution theorem; it is not covered here, together with the measure classification that proves it.

## Summary

A homogeneous space $G/\Gamma$ is the quotient of a Lie group by a discrete subgroup, acted on by left translations; when $\Gamma$ is a lattice, $G/\Gamma$ carries a finite invariant measure, unique up to scale, and a fundamental domain computes it. The standard examples are the torus $\mathbb{R}^n/\mathbb{Z}^n$, the unit tangent bundle of a hyperbolic surface, the modular surface $SL_2(\mathbb{Z})\backslash\mathbb{H}$, the higher-rank quotients $SL_n(\mathbb{Z})\backslash SL_n(\mathbb{R})$, and the nilmanifolds $N/\Gamma$ of nilpotent groups.

On $G/\Gamma$ for $G = SL_2(\mathbb{R})$ the geodesic flow is the action of the diagonal subgroup $A$ and the horocycle flow the action of the upper unipotent subgroup $U$, and the commutation relation $a_su_ta_s^{-1}=u_{e^st}$ exposes the contraction that the Mautner phenomenon needs: the geodesic flow is ergodic because the horocycle flow is, and it is mixing by Howe–Moore. Unipotent flows on semisimple quotients are ergodic by Dani's theorem, and on nilmanifolds by the rational-independence criterion in the abelianisation; the orbit closures on a nilmanifold are finite unions of orbits of larger subgroups, the theorem of Green, Parry and Auslander.

In higher rank the diagonal subgroup is a chamber $\mathbb{R}^r$, the Weyl chamber flow is ergodic and mixing by Moore and Howe–Moore, and the dynamics is rigid: Mostow rigidity says that an isomorphism of the flows is algebraic, so there is no measurable deformation of an irreducible lattice in rank at least two. The equidistribution of horocycles is Furstenberg's theorem, holding for every orbit, and it is the prototype of the general equidistribution of unipotent orbits that is the subject of Ratner's theorems . The nilpotent case is the model throughout: the abelian base supplies the rational-independence criterion, the commutators supply the corrections, and the flow is uniquely ergodic exactly when it is minimal.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $\mathfrak{g}$, $\Gamma$ | Connected Lie group, its Lie algebra, a discrete subgroup |
| $X = G/\Gamma$ | Homogeneous space of left cosets, with the quotient topology |
| lattice, uniform | discrete $\Gamma$ with $G/\Gamma$ of finite invariant volume; cocompact case |
| $\mu$, $\operatorname{vol}(G/\Gamma)$ | $G$-invariant measure and covolume |
| $K$ | Maximal compact subgroup; $G/K$ the symmetric space |
| $\mathbb{H}$, $PSL_2(\mathbb{R})$ | Upper half-plane and its isometry group |
| $A$, $a_s$ | Diagonal (geodesic) subgroup, $\operatorname{diag}(e^{s/2},e^{-s/2})$ |
| $U$, $u_t$ | Upper unipotent (horocycle) subgroup, $\begin{pmatrix}1&t\\0&1\end{pmatrix}$ |
| $a_su_ta_s^{-1}=u_{e^st}$ | Commutation relation; the contraction of the Mautner phenomenon |
| unipotent | $\operatorname{Ad}(g)-I$ nilpotent; one-parameter flow with polynomial $\operatorname{Ad}(u_t)-I$ |
| semisimple | $\operatorname{Ad}(g)$ diagonalisable over $\mathbb{C}$ |
| $N$, $\mathfrak{n}$, $[\mathfrak{n},\mathfrak{n}]$ | Nilpotent group, its Lie algebra, the abelianisation |
| Heisenberg group | Upper unitriangular $3\times3$ matrices, $[X,Y]=Z$ central |
| Weyl chamber flow | Action of the diagonal subgroup $A\cong\mathbb{R}^r$ in real rank $r$ |
| Furstenberg | horocycle orbits are equidistributed for every point; the flow is uniquely ergodic |
| Dani | ergodicity criterion for unipotent flows on semisimple quotients |
| Green–Parry–Auslander | orbit closures on a nilmanifold are finite unions of orbits of larger subgroups |







## Further Reading

- Morris W. Hirsch, *Differential Topology* (Springer, 1976), and Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the geometry of homogeneous spaces and symmetric spaces.
- Gustav A. Hedlund, "The dynamics of geodesic flows", *Bulletin of the American Mathematical Society* 45 (1939), 241–260, for the geodesic and horocycle flows on surfaces.
- Harry Furstenberg, "The unique ergodicity of the horocycle flow", in *Recent Advances in Topological Dynamics* (Springer Lecture Notes 318, 1973), for the equidistribution of horocycles.
- Armand Borel, *Introduction aux groupes arithmétiques* (Hermann, 1969), for lattices, arithmetic groups and the finiteness of covolume.
- Gopal Prasad and M. S. Raghunathan, "Cartan subgroups and lattices in semi-simple groups", *Annals of Mathematics* 96 (1972), 296–317, for the structure of lattices and their relation to unipotent flows.
- S. G. Dani, "Invariant measures and minimal sets of horospherical flows", *Inventiones Mathematicae* 64 (1981), 357–385, for the ergodicity criterion for unipotent flows.
- Leon Green, "Spectra of nilflows", *Bulletin of the American Mathematical Society* 67 (1961), 414–415, and William Parry, "Ergodic properties of affine transformations and flows on nilmanifolds", *American Journal of Mathematics* 91 (1969), 757–771, for the nilmanifold classification.
- G. D. Mostow, *Strong Rigidity of Locally Symmetric Spaces* (Princeton University Press, 1973), and Marina Ratner, "Rigidity of horocycle flows", *Annals of Mathematics* 115 (1982), 597–614, for the rigidity of higher-rank dynamics.
- Manfred Einsiedler and Thomas Ward, *Ergodic Theory with a View towards Number Theory* (Springer, 2011), for the modern unified treatment of homogeneous dynamics and its arithmetic applications.
