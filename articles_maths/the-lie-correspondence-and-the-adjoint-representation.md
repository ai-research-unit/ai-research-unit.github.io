
# __The Lie Correspondence and the Adjoint Representation__

## Introduction

The exponential map of the companion article *The Lie Algebra and the Exponential Map* shows that a Lie group is locally determined by its Lie algebra: exponential coordinates identify a neighbourhood of the identity with a neighbourhood of zero in the algebra, and the Campbell–Baker–Hausdorff product recovers the germ of the group law. This article makes the local statement global. The functor from Lie groups to Lie algebras is an equivalence when restricted to simply connected groups, so the finite-dimensional real Lie algebras are exactly the Lie algebras of Lie groups, and the connected Lie groups with a given algebra are the quotients of its simply connected group by discrete central subgroups. The tool that carries the algebra back to the group is the adjoint representation, which associates to each group element the automorphism of the algebra it induces by conjugation.

The article states the Lie correspondence in the three forms it usually takes: the bijection between homomorphisms for a simply connected source, the classification of connected groups with a given algebra by discrete central subgroups, and the correspondence between subalgebras, ideals and the analytic subgroups of a given group. It then develops the adjoint representation $\operatorname{Ad}$ of the group and the adjoint representation $\operatorname{ad}$ of the algebra, their relation $d(\operatorname{Ad})_e = \operatorname{ad}$, the identification of the centre with the kernel of $\operatorname{Ad}$, and the description of the automorphism group of a semisimple algebra as an extension of the adjoint group by the diagram automorphisms.

The manifold and exponential conventions are those of *Lie Groups* and *The Lie Algebra and the Exponential Map*: $G$ is a smooth Lie group with Lie algebra $\mathfrak{g} = T_eG$, homomorphisms are smooth, and $d\varphi_e$ is the differential at the identity. Lie algebras are written in lowercase fraktur, so $\mathfrak{g}, \mathfrak{h}, \mathfrak{i}, \mathfrak{n}$ are Lie algebras, $\mathfrak{z}(\mathfrak{g})$ is the centre, $\operatorname{Der}(\mathfrak{g})$ and $\operatorname{Aut}(\mathfrak{g})$ are the derivations and automorphisms, and $\operatorname{ad}_x(y) = [x, y]$. The base field is $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and Lie's third theorem is stated over $\mathbb{R}$. No physics is invoked.

## The Lie Functor

### The Category of Lie Groups and Lie Algebras

The construction of *The Lie Algebra and the Exponential Map* associates to each Lie group $G$ over $\mathbb{K}$ its Lie algebra $\mathfrak{g} = \operatorname{Lie}(G)$ and to each smooth homomorphism $\varphi : G \to H$ the linear map $d\varphi_e : \mathfrak{g} \to \mathfrak{h}$, which is a homomorphism of Lie algebras. This is a functor

$$
\operatorname{Lie} : \mathbf{LieGrp}_{\mathbb{K}} \longrightarrow \mathbf{LieAlg}_{\mathbb{K}},
$$

from Lie groups and smooth homomorphisms to Lie algebras and Lie algebra homomorphisms. It is neither full nor faithful, and the failure is exactly the content of the correspondence: distinct group homomorphisms can induce the same linear map, and not every linear map descends.

**Example.** The groups $\mathbb{R}$ and $U(1) = \{z \in \mathbb{C} : |z| = 1\}$ have isomorphic Lie algebras, both $\mathbb{R}$ with zero bracket, but they are not isomorphic: $\mathbb{R}$ is simply connected and non-compact, while $U(1)$ is compact. The covering homomorphism $\mathbb{R} \to U(1)$, $t \mapsto e^{2\pi i t}$, induces an isomorphism of Lie algebras. The functor $\operatorname{Lie}$ therefore loses the information of the fundamental group.

**Example.** The covering $SU(2) \to SO(3)$ of degree $2$ induces an isomorphism $\mathfrak{su}(2) \to \mathfrak{so}(3)$ between the Lie algebras, and the two groups are not isomorphic; $SO(3)$ has fundamental group $\mathbb{Z}/2$, while $SU(2)$ is simply connected.

### Local Isomorphisms

**Definition.** A homomorphism $\varphi : G \to H$ of Lie groups is a **local isomorphism** if $d\varphi_e : \mathfrak{g} \to \mathfrak{h}$ is a linear isomorphism.

**Theorem.** Let $\varphi : G \to H$ be a local isomorphism of Lie groups. Then $\varphi$ is a local diffeomorphism, its kernel is a discrete subgroup of $G$, and if $G$ and $H$ are connected then $\varphi$ is a covering map onto its image. Conversely, a covering homomorphism of connected Lie groups is a local isomorphism.

**Proof.** Since $d\varphi_e$ is invertible, the inverse function theorem exhibits $\varphi$ as a local diffeomorphism near $e$; for $g$ near the identity, the left translations identify neighbourhoods of $g$ and of $\varphi(g)$, so $\varphi$ is a local diffeomorphism everywhere. A local diffeomorphism has discrete fibres, so $\ker\varphi$ is discrete. If $G$ is connected, the image of $\varphi$ is an open and closed connected subgroup, and a local diffeomorphism onto a connected group with discrete fibres is a covering. The converse is the inverse function theorem applied at the identity. $\square$

**Corollary.** A local isomorphism between connected Lie groups of the same dimension is surjective, hence a covering map, and its kernel is isomorphic to the quotient of the fundamental group of the base by the image of the fundamental group of the source; in particular $\ker\varphi \cong \pi_1(H)$ when $G$ is simply connected.

### Simply Connected Groups

**Definition.** A connected Lie group is **simply connected** if it is simply connected as a topological space, that is, if every loop in it is null-homotopic.

**Theorem.** Let $G$ be a simply connected Lie group and $H$ a Lie group with Lie algebras $\mathfrak{g}, \mathfrak{h}$. Then the map

$$
\operatorname{Hom}_{\mathbf{LieGrp}}(G, H) \longrightarrow \operatorname{Hom}_{\mathbf{LieAlg}}(\mathfrak{g}, \mathfrak{h}), \qquad \varphi \longmapsto d\varphi_e,
$$

is a bijection.

**Proof sketch.** Injectivity: if two homomorphisms induce the same map on Lie algebras, their difference is a homomorphism whose differential vanishes; the image of a connected group under a homomorphism with vanishing differential is discrete and connected, hence a point. Surjectivity: given a homomorphism $f : \mathfrak{g} \to \mathfrak{h}$, one integrates it. Along each one-parameter subgroup $\exp(tX)$ of $G$ one defines the path $\exp_H(t f(X))$; the Campbell–Baker–Hausdorff product on $G$ shows that these paths fit together into a homomorphism on a neighbourhood of the identity, and a neighbourhood of the identity generates $G$ because $G$ is connected. Simple connectivity of $G$ ensures that the construction is independent of the paths used to multiply elements, so the local homomorphism extends to all of $G$. $\square$

**Corollary.** Two simply connected Lie groups with isomorphic Lie algebras are isomorphic, and the simply connected Lie group is determined up to a unique isomorphism.

## The Lie Correspondence

### Statement

**Theorem (Lie correspondence).** Let $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$.

**(a)** Every finite-dimensional Lie algebra over $\mathbb{K}$ is the Lie algebra of a simply connected Lie group, unique up to isomorphism.

**(b)** If $G$ is a connected Lie group with Lie algebra $\mathfrak{g}$, there is a simply connected Lie group $\tilde{G}$ and a covering homomorphism $\pi : \tilde{G} \to G$ with discrete central kernel $D = \ker\pi$, and

$$
G \cong \tilde{G}/D, \qquad D \cong \pi_1(G).
$$

**(c)** The connected Lie groups with Lie algebra $\mathfrak{g}$ are exactly the quotients $\tilde{G}/D$ by discrete central subgroups $D \subseteq Z(\tilde{G})$, and two such quotients are isomorphic exactly when the corresponding subgroups are equal under an automorphism of $\tilde{G}$.

Part (a) is **Lie's third theorem**, and part (b) is the statement that the universal cover of a connected Lie group exists and is a Lie group with the same Lie algebra.

**Proof sketch.** For (b), the universal cover of the manifold $G$ inherits a group structure from the group structure of $G$: the multiplication lifts uniquely because the covering is a local diffeomorphism and the relevant rectangle is simply connected. The kernel of the covering is the fundamental group of $G$, and it is central: the map $\tilde{G} \to \tilde{G}$, $g \mapsto gdg^{-1}$, has discrete image and connected domain, so it is constant, equal to $d$. For (a), one builds the group by exponentiating the Lie algebra, for instance as the set of formal products of one-parameter subgroups modulo the relations imposed by the Campbell–Baker–Hausdorff product; the result is a simply connected Lie group with the given algebra. $\square$

**Corollary.** For a connected Lie group $G$ the kernel $D$ of the universal cover is central, so $\pi_1(G)$ is abelian, and the connected Lie groups with a given algebra form a partially ordered set under the quotient relation, with the simply connected group at the top. The order is not a lattice: the intersection of two discrete central subgroups of the universal cover is again discrete and central, but the subgroup they generate need not be discrete, so the two subgroups need not have a join.

### Subalgebras, Subgroups and Ideals

**Theorem (analytic subgroup theorem).** Let $G$ be a Lie group with Lie algebra $\mathfrak{g}$ and let $\mathfrak{h} \subseteq \mathfrak{g}$ be a Lie subalgebra. Then there is a unique connected immersed Lie subgroup $H \subseteq G$ with Lie algebra $\mathfrak{h}$, and its underlying set is generated by $\exp(\mathfrak{h})$. The subgroup $H$ need not be closed as a subset of $G$.

**Proof.** The distribution spanned by the left translates of $\mathfrak{h}$ is involutive because $\mathfrak{h}$ is closed under the bracket; the Frobenius theorem integrates it to a maximal connected integral submanifold through $e$, which carries a group structure because the distribution is left-invariant. Uniqueness is the uniqueness of the maximal connected integral manifold. $\square$

**Theorem (closed subgroup theorem).** Let $G$ be a Lie group and $H \subseteq G$ a subgroup that is closed as a subset. Then $H$ is an embedded Lie subgroup, and its Lie algebra is a subalgebra of $\mathfrak{g}$; the topology and manifold structure of $H$ are the induced ones.

**Corollary.** The connected Lie subgroups of $G$ correspond to the Lie subalgebras of $\mathfrak{g}$, the correspondence being inclusion-preserving. The closed connected subgroups correspond to those subalgebras whose associated subgroup happens to be closed, a topological rather than a purely algebraic condition; it holds automatically for $G$ simply connected, but not for ideals in general: a one-parameter subgroup of the torus $T^2$ of irrational slope generates a dense, non-closed normal subgroup, and its Lie algebra is an ideal of the abelian algebra $\mathbb{R}^2$.

**Theorem.** Let $H \subseteq G$ be a connected Lie subgroup with Lie algebra $\mathfrak{h}$. Then $\mathfrak{h}$ is an ideal of $\mathfrak{g}$ if and only if $H$ is a normal subgroup of $G$, and then $\operatorname{Lie}(G/H) = \mathfrak{g}/\mathfrak{h}$.

**Proof.** If $H$ is normal then $\operatorname{Ad}(g)\mathfrak{h} = \mathfrak{h}$ for all $g$ and differentiating gives $[\mathfrak{g}, \mathfrak{h}] \subseteq \mathfrak{h}$. Conversely, if $\mathfrak{h}$ is an ideal then $\exp(\mathfrak{g})$ normalises $H$: the identity $\exp(\operatorname{Ad}(g)v) = g\exp(v)g^{-1}$ of *The Lie Algebra and the Exponential Map* shows that conjugation preserves $\exp(\mathfrak{h}) = H$, and $\exp(\mathfrak{g})$ generates $G$ when $G$ is connected. The statement about the quotient follows from the naturality of the Lie functor. $\square$

**Theorem.** Let $\varphi : G \to H$ be a homomorphism of connected Lie groups, with differential $d\varphi_e : \mathfrak{g} \to \mathfrak{h}$. Then

$$
\operatorname{Lie}(\ker\varphi) = \ker(d\varphi_e), \qquad \operatorname{Lie}(\overline{\operatorname{im}\varphi}) = \operatorname{im}(d\varphi_e),
$$

where the closures are taken in $H$; if the image is closed the closure is redundant.

### Simply Connected Groups and the Classification of Lie Groups

**Corollary.** Let $\mathfrak{g}$ be a finite-dimensional real Lie algebra and $\tilde{G}$ its simply connected group. Then the connected Lie groups with Lie algebra $\mathfrak{g}$ are classified by the discrete central subgroups $D \subseteq Z(\tilde{G})$ up to automorphisms of $\tilde{G}$. In particular:

- if $Z(\tilde{G})$ is discrete, the classification is by subgroups of a finitely generated abelian group;
- a connected Lie group has discrete centre if and only if $\operatorname{Ad}$ has discrete kernel, which holds for $\mathfrak{g}$ semisimple.

## The Adjoint Representation

### $\operatorname{Ad}$ and $\operatorname{ad}$

**Definition.** For $g \in G$ let $c_g : G \to G$, $c_g(h) = ghg^{-1}$. The **adjoint representation of the group** is

$$
\operatorname{Ad} : G \to GL(\mathfrak{g}), \qquad \operatorname{Ad}(g) = d(c_g)_e,
$$

and the **adjoint representation of the algebra** is $\operatorname{ad} : \mathfrak{g} \to \mathfrak{gl}(\mathfrak{g})$, $\operatorname{ad}_x(y) = [x, y]$.

**Theorem.** $\operatorname{Ad}$ is a Lie group homomorphism and $\operatorname{ad}$ is a Lie algebra homomorphism. They are related by

$$
d(\operatorname{Ad})_e = \operatorname{ad},
$$

and by the composition rule

$$
\operatorname{Ad}(\exp X) = e^{\operatorname{ad}_X} = \sum_{k \geq 0} \frac{(\operatorname{ad}_X)^k}{k!} \in GL(\mathfrak{g}).
$$

**Proof.** The map $\operatorname{Ad}$ is a homomorphism because $c_{gh} = c_g \circ c_h$ and the differential is functorial. To identify $d(\operatorname{Ad})_e$, differentiate the identity $\operatorname{Ad}(g)v = \frac{d}{dt}\big|_{t=0} g\exp(tv)g^{-1}$ at $g = \exp(tx)$: the derivative of $g\exp(tv)g^{-1}$ with respect to $s$ at $s = 0$, with $g = \exp(sx)$, is $[x, v]$, so $d(\operatorname{Ad})_e(x) = \operatorname{ad}_x$. The composition rule is the naturality of the exponential applied to the homomorphism $\operatorname{Ad} : G \to GL(\mathfrak{g})$, whose Lie algebra is $\mathfrak{gl}(\mathfrak{g})$: $\operatorname{Ad}(\exp x) = \exp(\operatorname{ad}_x)$, and the exponential in $GL(\mathfrak{g})$ is the matrix exponential of the endomorphism $\operatorname{ad}_x$. $\square$

**Corollary (conjugation formula).** For all $g \in G$ and $v \in \mathfrak{g}$,

$$
\exp(\operatorname{Ad}(g)v) = g \exp(v) g^{-1}.
$$

### Invariance of the Killing Form

**Proposition.** The adjoint representation preserves the Killing form of $\mathfrak{g}$:

$$
\kappa(\operatorname{Ad}(g)v, \operatorname{Ad}(g)w) = \kappa(v, w), \qquad \kappa([x, v], w) + \kappa(v, [x, w]) = 0,
$$

for all $g \in G$ and $x, v, w \in \mathfrak{g}$.

**Proof.** This is the invariance of $\kappa$ under the Lie algebra automorphism $\operatorname{Ad}(g)$, together with its infinitesimal form $\kappa([x,v],w) = \kappa(v,[w,x])$ established in *Structure of Lie Algebras*. $\square$

### The Centre and the Kernel

**Theorem.** Let $G$ be a connected Lie group with Lie algebra $\mathfrak{g}$. Then the kernel of the adjoint representation is the centre:

$$
\ker(\operatorname{Ad}) = Z(G) = \{g \in G : gh = hg \text{ for all } h \in G\}.
$$

Consequently $\operatorname{Ad}$ induces an injective homomorphism $G/Z(G) \to GL(\mathfrak{g})$.

**Proof.** If $g \in \ker\operatorname{Ad}$ then $\operatorname{Ad}(g) = \mathrm{id}$, so $g\exp(v)g^{-1} = \exp(v)$ for all $v$ by the conjugation formula. Since $\exp(\mathfrak{g})$ generates the connected group $G$, this gives $ghg^{-1} = h$ for all $h \in G$, so $g \in Z(G)$. Conversely, if $g$ is central then $c_g = \mathrm{id}$ and $\operatorname{Ad}(g) = \mathrm{id}$. $\square$

**Corollary.** For connected $G$, the centre $Z(G)$ is a closed normal subgroup with Lie algebra

$$
\operatorname{Lie}(Z(G)) = \mathfrak{z}(\mathfrak{g}) = \{x \in \mathfrak{g} : [x, y] = 0 \text{ for all } y\},
$$

the centre of the Lie algebra.

**Example.** For $G = SU(2)$ the centre is $\{\pm I\}$ and $\operatorname{Ad}$ maps $SU(2)$ onto $SO(3)$, the double cover $SU(2) \to SO(3) = SU(2)/\{\pm I\}$; the kernel of $\operatorname{Ad}$ is exactly $\{\pm I\}$. For $G = U(1)$ the adjoint representation is trivial, the Lie algebra being abelian, and $\ker\operatorname{Ad} = U(1) = Z(G)$.

### The Semisimple Case

**Theorem.** Let $\mathfrak{g}$ be a finite-dimensional semisimple Lie algebra over $\mathbb{K}$ and let $\tilde{G}$ be its simply connected group. Then:

**(a)** $\mathfrak{z}(\mathfrak{g}) = 0$ and $\ker(\operatorname{Ad}) = Z(G)$ is discrete for every connected $G$ with Lie algebra $\mathfrak{g}$;

**(b)** $\operatorname{Ad}(\tilde{G}) = \operatorname{Aut}(\mathfrak{g})_0$, the identity component of the automorphism group of $\mathfrak{g}$;

**(c)** the quotient $\operatorname{Out}(\mathfrak{g}) = \operatorname{Aut}(\mathfrak{g})/\operatorname{Ad}(\tilde{G})$ is finite, and it embeds into the group of automorphisms of the Dynkin diagram of $\mathfrak{g}$; for $\mathfrak{g}$ simple the embedding is an isomorphism, so $\operatorname{Out}(\mathfrak{g})$ is the diagram automorphism group: trivial for $A_1$, $B_n$, $C_n$, $E_7$, $E_8$, $F_4$, $G_2$; of order $2$ for $A_n$ with $n \geq 2$, $D_n$ with $n \geq 5$, and $E_6$; and the symmetric group $S_3$ of order $6$ for $D_4$.

**Proof sketch.** Part (a) is the vanishing of the centre of a semisimple algebra, so $\operatorname{Ad}$ is injective on $\tilde{G}$, and a Lie group homomorphism with injective differential is a local diffeomorphism, giving discreteness of the kernel. For (b), the Lie algebra of $\operatorname{Aut}(\mathfrak{g})$ is $\operatorname{Der}(\mathfrak{g})$, which equals $\operatorname{ad}(\mathfrak{g}) = \operatorname{Lie}(\operatorname{Ad}(\tilde{G}))$ because every derivation of a semisimple algebra is inner; two connected subgroups of a Lie group with equal Lie algebras coincide, so $\operatorname{Ad}(\tilde{G}) = \operatorname{Aut}(\mathfrak{g})_0$. For (c), an automorphism of $\mathfrak{g}$ permutes the simple roots and preserves the Cartan matrix, hence induces an automorphism of the Dynkin diagram; the kernel of the resulting map to the diagram automorphisms is the identity component, and the diagram automorphisms of the listed types are the classical outer automorphisms. $\square$

## The Automorphism Group

### $\operatorname{Aut}(\mathfrak{g})$ and the Adjoint Group

**Definition.** The **automorphism group** $\operatorname{Aut}(\mathfrak{g})$ is the group of Lie algebra automorphisms of $\mathfrak{g}$; the **adjoint group** is $\operatorname{Ad}(G) = \operatorname{Int}(\mathfrak{g})$, the image of a connected $G$ with Lie algebra $\mathfrak{g}$.

**Theorem.** $\operatorname{Aut}(\mathfrak{g})$ is a Lie group with Lie algebra $\operatorname{Der}(\mathfrak{g})$, the derivations of $\mathfrak{g}$ under the commutator. Its identity component is $\operatorname{Aut}(\mathfrak{g})_0 = \operatorname{Ad}(\tilde{G})$, and

$$
\operatorname{Out}(\mathfrak{g}) = \operatorname{Aut}(\mathfrak{g})/\operatorname{Ad}(\tilde{G})
$$

is the finite group of outer automorphisms in the semisimple case.

**Proof sketch.** The automorphism group is a closed subgroup of $GL(\mathfrak{g})$ and hence a Lie group by the closed subgroup theorem; differentiating the identity $\varphi([x,y]) = [\varphi x, \varphi y]$ at $\varphi = \mathrm{id}$ gives the derivation condition, so the Lie algebra is $\operatorname{Der}(\mathfrak{g})$. The identity component statement follows because $\operatorname{Ad}(\tilde{G})$ and $\operatorname{Aut}(\mathfrak{g})_0$ are connected subgroups with the same Lie algebra, by the inner-derivation theorem. $\square$

### The Adjoint Representation in Coordinates

**Example.** Let $\mathfrak{g} = \mathfrak{sl}(2, \mathbb{C})$ with basis $e, h, f$ and let $G = SL_2(\mathbb{C})$. The adjoint map on the group is conjugation of matrices, and $\operatorname{Ad}(g)X = gXg^{-1}$; on the algebra, $\operatorname{ad}_x(y) = [x,y]$. For $g = \operatorname{diag}(t, t^{-1})$ one has

$$
\operatorname{Ad}(g)e = t^2 e, \qquad \operatorname{Ad}(g)f = t^{-2} f, \qquad \operatorname{Ad}(g)h = h,
$$

so the weights of the adjoint representation are the roots $\alpha, 0, -\alpha$, exactly as the root space decomposition of *Root Systems and Classification* requires. The kernel of $\operatorname{Ad}$ is the centre $\{\pm I\}$, and $\operatorname{Ad}(SL_2(\mathbb{C})) = PSL_2(\mathbb{C})$ is the adjoint group of type $A_1$.

**Example.** For $\mathfrak{g} = \mathfrak{so}(3)$ and $G = SO(3)$, the adjoint representation is the standard three-dimensional representation, $SO(3) \cong \operatorname{Ad}(SO(3)) = \operatorname{Aut}(\mathfrak{so}(3))_0$, and $\operatorname{Out}(\mathfrak{so}(3)) = 1$; the situation differs from $SU(2)$, where $\operatorname{Ad}$ has the nontrivial discrete kernel.

## Coverings and the Lattice of Connected Subgroups

**Theorem.** Let $G$ be a connected Lie group with Lie algebra $\mathfrak{g}$ and universal cover $\pi : \tilde{G} \to G$. Then:

**(a)** $D = \ker\pi$ is a discrete central subgroup of $\tilde{G}$ isomorphic to $\pi_1(G)$;

**(b)** every connected Lie group with Lie algebra $\mathfrak{g}$ is a quotient of $\tilde{G}$ by a discrete central subgroup, and the covering homomorphisms between them correspond to inclusions of the subgroups;

**(c)** if $G$ is simply connected and $H$ is any Lie group with Lie algebra $\mathfrak{h}$, then $\operatorname{Hom}(G, H)$ is in bijection with $\operatorname{Hom}(\mathfrak{g}, \mathfrak{h})$; in particular, when $\mathfrak{h} = \mathfrak{g}$, the isomorphisms $G \to H$ correspond to the automorphisms of $\mathfrak{g}$, and the image of a homomorphism with invertible differential is a connected subgroup with the same algebra.

**Proof.** Parts (a) and (b) are the Lie correspondence above; (c) is the bijection on homomorphisms applied to $\operatorname{Hom}(\mathfrak{g}, \mathfrak{h})$ and the fact that a homomorphism of connected groups is determined by its differential. $\square$

**Example.** For $\mathfrak{g} = \mathbb{R}$ the simply connected group is $\mathbb{R}$, and the discrete central subgroups are the lattices $\lambda\mathbb{Z}$; the quotients are $S^1$ for each $\lambda \neq 0$, all isomorphic, together with $\mathbb{R}$ itself. This is the simplest illustration of the partially ordered set of connected groups with a given algebra and of the failure of the Lie functor to be injective on objects: the classification requires the subgroup, not only the algebra.

## Summary

The functor $\operatorname{Lie}$ from Lie groups to Lie algebras is neither full nor faithful; it preserves exactly the local structure, and a homomorphism is a local isomorphism precisely when it induces an isomorphism of Lie algebras. For a simply connected source $G$ the map $\varphi \mapsto d\varphi_e$ is a bijection from $\operatorname{Hom}(G,H)$ to $\operatorname{Hom}(\mathfrak{g},\mathfrak{h})$, so the simply connected Lie groups and the finite-dimensional Lie algebras form equivalent categories, and Lie's third theorem says that every finite-dimensional real Lie algebra occurs.

Every connected Lie group $G$ with algebra $\mathfrak{g}$ is a quotient $\tilde{G}/D$ of its simply connected cover by a discrete central subgroup $D \cong \pi_1(G)$, so the connected groups with a given algebra are classified by those subgroups, and the fundamental group of $G$ is abelian. Lie subalgebras correspond to connected immersed subgroups, ideals to normal connected subgroups, and quotients of algebras to quotients of groups; closed subgroups of a Lie group are embedded Lie subgroups by the closed subgroup theorem.

The adjoint representation $\operatorname{Ad} : G \to GL(\mathfrak{g})$ is a group homomorphism with $d(\operatorname{Ad})_e = \operatorname{ad}$ and $\operatorname{Ad}(\exp X) = e^{\operatorname{ad}_X} = \sum_k (\operatorname{ad}_X)^k/k!$; it preserves the Killing form, its kernel is the centre $Z(G)$ for connected $G$, and its image is the adjoint group. For a semisimple algebra the kernel is discrete, the identity component of the automorphism group is the adjoint group because every derivation is inner, and the outer automorphism group is finite, acting through the automorphisms of the Dynkin diagram.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{K}$ | $\mathbb{R}$ or $\mathbb{C}$; the base of the Lie groups |
| $G, H$ | Connected Lie groups over $\mathbb{K}$ |
| $\mathfrak{g} = \operatorname{Lie}(G)$ | Lie algebra of $G$; $T_eG$ with the bracket |
| $d\varphi_e$ | Differential at the identity; a Lie algebra homomorphism |
| $\operatorname{Hom}(G,H)$, $\operatorname{Hom}(\mathfrak{g},\mathfrak{h})$ | Lie group and Lie algebra homomorphisms; $\varphi \mapsto d\varphi_e$ is a bijection between them |
| $\operatorname{Lie} : \mathbf{LieGrp} \to \mathbf{LieAlg}$ | The Lie functor; neither full nor faithful |
| $\varphi : G \to H$ local isomorphism | $d\varphi_e$ invertible; then $\varphi$ is a covering for connected $G, H$ |
| $\tilde{G}, \pi : \tilde{G} \to G$ | Simply connected cover; $\ker\pi \cong \pi_1(G)$, discrete and central |
| $G \cong \tilde{G}/D$ | Classification of connected groups with a given algebra by discrete central $D$ |
| $\mathfrak{h} \subseteq \mathfrak{g} \longleftrightarrow H \subseteq G$ | Lie subalgebras correspond to connected immersed subgroups |
| $\mathfrak{h}$ an ideal $\iff H$ normal | Then $\operatorname{Lie}(G/H) = \mathfrak{g}/\mathfrak{h}$ |
| $c_g(h) = ghg^{-1}$ | Conjugation by $g$ |
| $\operatorname{Ad}(g) = d(c_g)_e$ | Adjoint representation of $G$ on $\mathfrak{g}$ |
| $\operatorname{ad}_x(y) = [x,y]$ | Adjoint representation of $\mathfrak{g}$; $d(\operatorname{Ad})_e = \operatorname{ad}$ |
| $\mathfrak{gl}(\mathfrak{g})$ | Endomorphisms of $\mathfrak{g}$; the target of $\operatorname{ad}$ |
| $\operatorname{Ad}(\exp X) = e^{\operatorname{ad}_X}$ | The exponential intertwines $\operatorname{Ad}$ and $\operatorname{ad}$ |
| $\ker(\operatorname{Ad}) = Z(G)$ | Centre of a connected group |
| $\operatorname{Lie}(Z(G)) = \mathfrak{z}(\mathfrak{g})$ | Centre of the Lie algebra |
| $\operatorname{Aut}(\mathfrak{g})$, $\operatorname{Der}(\mathfrak{g})$ | Automorphisms; derivations; $\operatorname{Lie}(\operatorname{Aut}(\mathfrak{g})) = \operatorname{Der}(\mathfrak{g})$ |
| $\operatorname{Ad}(G) = \operatorname{Int}(\mathfrak{g})$ | Adjoint group; $\operatorname{Aut}(\mathfrak{g})_0$ in the semisimple case |
| $\operatorname{Out}(\mathfrak{g}) = \operatorname{Aut}(\mathfrak{g})/\operatorname{Ad}(\tilde{G})$ | Finite outer automorphism group; diagram automorphisms |

## Further Reading

- John M. Lee, *Introduction to Smooth Manifolds* (Springer, 2nd ed. 2013), for local diffeomorphisms, coverings, and the closed subgroup theorem.
- John F. Adams, *Lectures on Lie Groups* (University of Chicago Press, 1969), for the Lie correspondence and the adjoint representation.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the analytic subgroup theorem and the classification of connected groups.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the correspondence between subalgebras, subgroups and ideals.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2nd ed. 2015), for the Lie correspondence with matrix groups and the adjoint representation.
- Jean-Pierre Serre, *Lie Algebras and Lie Groups* (Springer, 1992), for Lie's third theorem and the equivalence of categories.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the automorphism group, inner derivations, and the outer automorphism group.
