
# __The Lie Correspondence and the Adjoint Representation__

## Introduction

The exponential map of the companion article *The Lie Algebra and the Exponential Map* shows that a Lie group is locally determined by its Lie algebra: exponential coordinates identify a neighbourhood of the identity with a neighbourhood of zero in the algebra, and the Campbell–Baker–Hausdorff product recovers the germ of the group law. This article makes the local statement global. The functor from Lie groups to Lie algebras is an equivalence when restricted to simply connected groups, so the finite-dimensional real Lie algebras are exactly the Lie algebras of Lie groups, and the connected Lie groups with a given algebra are the quotients of its simply connected group by discrete central subgroups. The tool that carries the algebra back to the group is the adjoint representation, which associates to each group element the automorphism of the algebra it induces by conjugation.

The article states the Lie correspondence in the three forms it usually takes: the bijection between homomorphisms for a simply connected source, the classification of connected groups with a given algebra by discrete central subgroups, and the correspondence between subalgebras, ideals and the analytic subgroups of a given group. It then develops the adjoint representation $\operatorname{Ad}$ of the group and the adjoint representation $\operatorname{ad}$ of the algebra, their relation $d(\operatorname{Ad})_e = \operatorname{ad}$, the identification of the centre with the kernel of $\operatorname{Ad}$, and the description of the automorphism group of a semisimple algebra as an extension of the adjoint group by the diagram automorphisms. It closes with the table of the classical groups, one row per algebra and one column each for the cover, the centre, the quotients and the fundamental group, and with the list of what the algebra does not determine: the fundamental group, compactness, the real form and the unitary dual.

The manifold and exponential conventions are those of *Lie Groups* and *The Lie Algebra and the Exponential Map*: $G$ is a smooth Lie group with Lie algebra $\mathrm{G} = T_eG$, homomorphisms are smooth, and $d\varphi_e$ is the differential at the identity. Lie algebras are written in upright capitals, so $\mathrm{G}, \mathrm{H}, \mathrm{I}, \mathrm{N}$ are Lie algebras, $\mathrm{Z}(\mathrm{G})$ is the centre, $\operatorname{Der}(\mathrm{G})$ and $\operatorname{Aut}(\mathrm{G})$ are the derivations and automorphisms, and $\operatorname{ad}_x(y) = [x, y]$. The base field is $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and Lie's third theorem is stated over $\mathbb{R}$. No physics is invoked.

## The Lie Functor

### The Category of Lie Groups and Lie Algebras

The construction of *The Lie Algebra and the Exponential Map* associates to each Lie group $G$ over $\mathbb{K}$ its Lie algebra $\mathrm{G} = \operatorname{Lie}(G)$ and to each smooth homomorphism $\varphi : G \to H$ the linear map $d\varphi_e : \mathrm{G} \to \mathrm{H}$, which is a homomorphism of Lie algebras. This is a functor

$$
\operatorname{Lie} : \mathbf{LieGrp}_{\mathbb{K}} \longrightarrow \mathbf{LieAlg}_{\mathbb{K}},
$$

from Lie groups and smooth homomorphisms to Lie algebras and Lie algebra homomorphisms. It is neither full nor faithful, and the failure is exactly the content of the correspondence: distinct group homomorphisms can induce the same linear map, and not every linear map descends.

**Example.** The groups $\mathbb{R}$ and $\mathrm{U}(1) = \{z \in \mathbb{C} : |z| = 1\}$ have isomorphic Lie algebras, both $\mathbb{R}$ with zero bracket, but they are not isomorphic: $\mathbb{R}$ is simply connected and non-compact, while $\mathrm{U}(1)$ is compact. The covering homomorphism $\mathbb{R} \to \mathrm{U}(1)$, $t \mapsto \exp(2\pi i t)$, induces an isomorphism of Lie algebras. The functor $\operatorname{Lie}$ therefore loses the information of the fundamental group.

**Example.** The covering $SU(2) \to SO(3)$ of degree $2$ induces an isomorphism $\mathrm{SU}(2) \to \mathrm{SO}(3)$ between the Lie algebras, and the two groups are not isomorphic; $SO(3)$ has fundamental group $\mathbb{Z}/2$, while $SU(2)$ is simply connected.

### Local Isomorphisms

**Definition.** A homomorphism $\varphi : G \to H$ of Lie groups is a **local isomorphism** if $d\varphi_e : \mathrm{G} \to \mathrm{H}$ is a linear isomorphism.

**Theorem.** Let $\varphi : G \to H$ be a local isomorphism of Lie groups. Then $\varphi$ is a local diffeomorphism, its kernel is a discrete subgroup of $G$, and if $G$ and $H$ are connected then $\varphi$ is a covering map onto its image. Conversely, a covering homomorphism of connected Lie groups is a local isomorphism.

**Proof.** Since $d\varphi_e$ is invertible, the inverse function theorem exhibits $\varphi$ as a local diffeomorphism near $e$; for $g$ near the identity, the left translations identify neighbourhoods of $g$ and of $\varphi(g)$, so $\varphi$ is a local diffeomorphism everywhere. A local diffeomorphism has discrete fibres, so $\ker\varphi$ is discrete. If $G$ is connected, the image of $\varphi$ is an open and closed connected subgroup, and a local diffeomorphism onto a connected group with discrete fibres is a covering. The converse is the inverse function theorem applied at the identity.

**Corollary.** A local isomorphism between connected Lie groups of the same dimension is surjective, hence a covering map, and its kernel is isomorphic to the quotient of the fundamental group of the base by the image of the fundamental group of the source; in particular $\ker\varphi \cong \pi_1(H)$ when $G$ is simply connected.

### Simply Connected Groups

**Definition.** A connected Lie group is **simply connected** if it is simply connected as a topological space, that is, if every loop in it is null-homotopic.

**Theorem.** Let $G$ be a simply connected Lie group and $H$ a Lie group with Lie algebras $\mathrm{G}, \mathrm{H}$. Then the map

$$
\boxed{\;\operatorname{Hom}_{\mathbf{LieGrp}}(G, H) \longrightarrow \operatorname{Hom}_{\mathbf{LieAlg}}(\mathrm{G}, \mathrm{H}), \qquad \varphi \longmapsto d\varphi_e\;},
$$

is a bijection.

**Proof sketch.** Injectivity: if two homomorphisms induce the same map on Lie algebras, their difference is a homomorphism whose differential vanishes; the image of a connected group under a homomorphism with vanishing differential is discrete and connected, hence a point. Surjectivity: given a homomorphism $f : \mathrm{G} \to \mathrm{H}$, one integrates it. Along each one-parameter subgroup $\exp(tX)$ of $G$ one defines the path $\exp_H(t f(X))$; the Campbell–Baker–Hausdorff product on $G$ shows that these paths fit together into a homomorphism on a neighbourhood of the identity, and a neighbourhood of the identity generates $G$ because $G$ is connected. Simple connectivity of $G$ ensures that the construction is independent of the paths used to multiply elements, so the local homomorphism extends to all of $G$.

**Corollary.** Two simply connected Lie groups with isomorphic Lie algebras are isomorphic, and the simply connected Lie group is determined up to a unique isomorphism.

## The Lie Correspondence

### Statement

**Theorem (Lie correspondence).** Let $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$.

**(a)** Every finite-dimensional Lie algebra over $\mathbb{K}$ is the Lie algebra of a simply connected Lie group, unique up to isomorphism.

**(b)** If $G$ is a connected Lie group with Lie algebra $\mathrm{G}$, there is a simply connected Lie group $G_{\mathrm{cov}}$ and a covering homomorphism $\pi : G_{\mathrm{cov}} \to G$ with discrete central kernel $D = \ker\pi$, and

$$
G \cong G_{\mathrm{cov}}/D, \qquad D \cong \pi_1(G).
$$

**(c)** The connected Lie groups with Lie algebra $\mathrm{G}$ are exactly the quotients $G_{\mathrm{cov}}/D$ by discrete central subgroups $D \subseteq Z(G_{\mathrm{cov}})$, and two such quotients are isomorphic exactly when the corresponding subgroups are equal under an automorphism of $G_{\mathrm{cov}}$.

Part (a) is **Lie's third theorem**, and part (b) is the statement that the universal cover of a connected Lie group exists and is a Lie group with the same Lie algebra.

**Proof sketch.** For (b), the universal cover of the manifold $G$ inherits a group structure from the group structure of $G$: the multiplication lifts uniquely because the covering is a local diffeomorphism and the relevant rectangle is simply connected. The kernel of the covering is the fundamental group of $G$, and it is central: the map $G_{\mathrm{cov}} \to G_{\mathrm{cov}}$, $g \mapsto gdg^{-1}$, has discrete image and connected domain, so it is constant, equal to $d$. For (a), one builds the group by exponentiating the Lie algebra, for instance as the set of formal products of one-parameter subgroups modulo the relations imposed by the Campbell–Baker–Hausdorff product; the result is a simply connected Lie group with the given algebra.

**Warning (the bijection is with the simply connected groups).** The bijection is between finite-dimensional Lie algebras and **simply connected** Lie groups, up to isomorphism, and it is not a bijection between Lie algebras and connected Lie groups. The algebra $\mathbb{R}$ is the algebra of $\mathbb{R}$ and of $U(1)$; only the first of the two is simply connected, so no bijection can hold both. The general connected group enters only after the extra datum of a discrete central subgroup is supplied, which is the subject of *Coverings and the Lattice of Connected Subgroups* below.

**Corollary.** For a connected Lie group $G$ the kernel $D$ of the universal cover is central, so $\pi_1(G)$ is abelian, and the connected Lie groups with a given algebra form a partially ordered set under the quotient relation, with the simply connected group at the top. The order is not a lattice: the intersection of two discrete central subgroups of the universal cover is again discrete and central, but the subgroup they generate need not be discrete, so the two subgroups need not have a join.

### Subalgebras, Subgroups and Ideals

**Theorem (analytic subgroup theorem).** Let $G$ be a Lie group with Lie algebra $\mathrm{G}$ and let $\mathrm{H} \subseteq \mathrm{G}$ be a Lie subalgebra. Then there is a unique connected immersed Lie subgroup $H \subseteq G$ with Lie algebra $\mathrm{H}$, and its underlying set is generated by $\exp(\mathrm{H})$. The subgroup $H$ need not be closed as a subset of $G$.

**Proof.** The distribution spanned by the left translates of $\mathrm{H}$ is involutive because $\mathrm{H}$ is closed under the bracket; the Frobenius theorem integrates it to a maximal connected integral submanifold through $e$, which carries a group structure because the distribution is left-invariant. Uniqueness is the uniqueness of the maximal connected integral manifold.

**Theorem (closed subgroup theorem).** Let $G$ be a Lie group and $H \subseteq G$ a subgroup that is closed as a subset. Then $H$ is an embedded Lie subgroup, and its Lie algebra is a subalgebra of $\mathrm{G}$; the topology and manifold structure of $H$ are the induced ones.

**Corollary.** The connected Lie subgroups of $G$ correspond to the Lie subalgebras of $\mathrm{G}$, the correspondence being inclusion-preserving. The closed connected subgroups correspond to those subalgebras whose associated subgroup happens to be closed, a topological rather than a purely algebraic condition; it holds automatically for $G$ simply connected, but not for ideals in general: a one-parameter subgroup of the torus $T^2$ of irrational slope generates a dense, non-closed normal subgroup, and its Lie algebra is an ideal of the abelian algebra $\mathbb{R}^2$.

**Theorem.** Let $H \subseteq G$ be a connected Lie subgroup with Lie algebra $\mathrm{H}$. Then $\mathrm{H}$ is an ideal of $\mathrm{G}$ if and only if $H$ is a normal subgroup of $G$, and then $\operatorname{Lie}(G/H) = \mathrm{G}/\mathrm{H}$.

**Proof.** If $H$ is normal then $\operatorname{Ad}(g)\mathrm{H} = \mathrm{H}$ for all $g$ and differentiating gives $[\mathrm{G}, \mathrm{H}] \subseteq \mathrm{H}$. Conversely, if $\mathrm{H}$ is an ideal then $\exp(\mathrm{G})$ normalises $H$: the identity $\exp(\operatorname{Ad}(g)v) = g\exp(v)g^{-1}$ of *The Lie Algebra and the Exponential Map* shows that conjugation preserves $\exp(\mathrm{H}) = H$, and $\exp(\mathrm{G})$ generates $G$ when $G$ is connected. The statement about the quotient follows from the naturality of the Lie functor.

**Theorem.** Let $\varphi : G \to H$ be a homomorphism of connected Lie groups, with differential $d\varphi_e : \mathrm{G} \to \mathrm{H}$. Then

$$
\operatorname{Lie}(\ker\varphi) = \ker(d\varphi_e), \qquad \operatorname{Lie}(\overline{\operatorname{im}\varphi}) = \operatorname{im}(d\varphi_e),
$$

where the closures are taken in $H$; if the image is closed the closure is redundant.

### Simply Connected Groups and the Classification of Lie Groups

**Corollary.** Let $\mathrm{G}$ be a finite-dimensional real Lie algebra and $G_{\mathrm{cov}}$ its simply connected group. Then the connected Lie groups with Lie algebra $\mathrm{G}$ are classified by the discrete central subgroups $D \subseteq Z(G_{\mathrm{cov}})$ up to automorphisms of $G_{\mathrm{cov}}$. In particular:

- if $Z(G_{\mathrm{cov}})$ is discrete, the classification is by subgroups of a finitely generated abelian group;
- a connected Lie group has discrete centre if and only if $\operatorname{Ad}$ has discrete kernel, which holds for $\mathrm{G}$ semisimple.

## The Adjoint Representation

### $\operatorname{Ad}$ and $\operatorname{ad}$

**Definition.** For $g \in G$ let $c_g : G \to G$, $c_g(h) = ghg^{-1}$. The **adjoint representation of the group** is

$$
\operatorname{Ad} : G \to GL(\mathrm{G}), \qquad \operatorname{Ad}(g) = d(c_g)_e,
$$

and the **adjoint representation of the algebra** is $\operatorname{ad} : \mathrm{G} \to \mathrm{GL}(\mathrm{G})$, $\operatorname{ad}_x(y) = [x, y]$.

**Theorem.** $\operatorname{Ad}$ is a Lie group homomorphism and $\operatorname{ad}$ is a Lie algebra homomorphism. They are related by

$$
d(\operatorname{Ad})_e = \operatorname{ad},
$$

and by the composition rule

$$
\boxed{\;\operatorname{Ad}(\exp X) = \exp(\operatorname{ad}_X) = \sum_{k \geq 0} \frac{(\operatorname{ad}_X)^k}{k!} \in GL(\mathrm{G})\;}.
$$

**Proof.** The map $\operatorname{Ad}$ is a homomorphism because $c_{gh} = c_g \circ c_h$ and the differential is functorial. To identify $d(\operatorname{Ad})_e$, differentiate the identity $\operatorname{Ad}(g)v = \frac{d}{dt}\big|_{t=0} g\exp(tv)g^{-1}$ at $g = \exp(tx)$: the derivative of $g\exp(tv)g^{-1}$ with respect to $s$ at $s = 0$, with $g = \exp(sx)$, is $[x, v]$, so $d(\operatorname{Ad})_e(x) = \operatorname{ad}_x$. The composition rule is the naturality of the exponential applied to the homomorphism $\operatorname{Ad} : G \to GL(\mathrm{G})$, whose Lie algebra is $\mathrm{GL}(\mathrm{G})$: $\operatorname{Ad}(\exp x) = \exp(\operatorname{ad}_x)$, and the exponential in $GL(\mathrm{G})$ is the matrix exponential of the endomorphism $\operatorname{ad}_x$.

**Corollary (conjugation formula).** For all $g \in G$ and $v \in \mathrm{G}$,

$$
\exp(\operatorname{Ad}(g)v) = g \exp(v) g^{-1}.
$$

### Invariance of the Killing Form

**Proposition.** The adjoint representation preserves the Killing form of $\mathrm{G}$:

$$
\kappa(\operatorname{Ad}(g)v, \operatorname{Ad}(g)w) = \kappa(v, w), \qquad \kappa([x, v], w) + \kappa(v, [x, w]) = 0,
$$

for all $g \in G$ and $x, v, w \in \mathrm{G}$.

**Proof.** This is the invariance of $\kappa$ under the Lie algebra automorphism $\operatorname{Ad}(g)$, together with its infinitesimal form $\kappa([x,v],w) = \kappa(v,[w,x])$ established in *Structure of Lie Algebras*.

### The Centre and the Kernel

**Theorem.** Let $G$ be a connected Lie group with Lie algebra $\mathrm{G}$. Then the kernel of the adjoint representation is the centre:

$$
\boxed{\;\ker(\operatorname{Ad}) = Z(G) = \{g \in G : gh = hg \text{ for all } h \in G\}\;}.
$$

Consequently $\operatorname{Ad}$ induces an injective homomorphism $G/Z(G) \to GL(\mathrm{G})$.

**Proof.** If $g \in \ker\operatorname{Ad}$ then $\operatorname{Ad}(g) = \mathrm{id}$, so $g\exp(v)g^{-1} = \exp(v)$ for all $v$ by the conjugation formula. Since $\exp(\mathrm{G})$ generates the connected group $G$, this gives $ghg^{-1} = h$ for all $h \in G$, so $g \in Z(G)$. Conversely, if $g$ is central then $c_g = \mathrm{id}$ and $\operatorname{Ad}(g) = \mathrm{id}$.

**Corollary.** For connected $G$, the centre $Z(G)$ is a closed normal subgroup with Lie algebra

$$
\operatorname{Lie}(Z(G)) = \mathrm{Z}(\mathrm{G}) = \{x \in \mathrm{G} : [x, y] = 0 \text{ for all } y\},
$$

the centre of the Lie algebra.

**Example.** For $G = SU(2)$ the centre is $\{\pm I\}$ and $\operatorname{Ad}$ maps $SU(2)$ onto $SO(3)$, the double cover $SU(2) \to SO(3) = SU(2)/\{\pm I\}$; the kernel of $\operatorname{Ad}$ is exactly $\{\pm I\}$. For $G = \mathrm{U}(1)$ the adjoint representation is trivial, the Lie algebra being abelian, and $\ker\operatorname{Ad} = \mathrm{U}(1) = Z(G)$.

### The Semisimple Case

**Theorem.** Let $\mathrm{G}$ be a finite-dimensional semisimple Lie algebra over $\mathbb{K}$ and let $G_{\mathrm{cov}}$ be its simply connected group. Then:

**(a)** $\mathrm{Z}(\mathrm{G}) = 0$ and $\ker(\operatorname{Ad}) = Z(G)$ is discrete for every connected $G$ with Lie algebra $\mathrm{G}$;

**(b)** $\operatorname{Ad}(G_{\mathrm{cov}}) = \operatorname{Aut}(\mathrm{G})_0$, the identity component of the automorphism group of $\mathrm{G}$;

**(c)** the quotient $\operatorname{Out}(\mathrm{G}) = \operatorname{Aut}(\mathrm{G})/\operatorname{Ad}(G_{\mathrm{cov}})$ is finite, and it embeds into the group of automorphisms of the Dynkin diagram of $\mathrm{G}$; for $\mathrm{G}$ simple the embedding is an isomorphism, so $\operatorname{Out}(\mathrm{G})$ is the diagram automorphism group: trivial for $A_1$, $B_n$, $C_n$, $E_7$, $E_8$, $F_4$, $G_2$; of order $2$ for $A_n$ with $n \geq 2$, $D_n$ with $n \geq 5$, and $E_6$; and the symmetric group $S_3$ of order $6$ for $D_4$.

**Proof sketch.** Part (a) is the vanishing of the centre of a semisimple algebra, so $\operatorname{Ad}$ is injective on $G_{\mathrm{cov}}$, and a Lie group homomorphism with injective differential is a local diffeomorphism, giving discreteness of the kernel. For (b), the Lie algebra of $\operatorname{Aut}(\mathrm{G})$ is $\operatorname{Der}(\mathrm{G})$, which equals $\operatorname{ad}(\mathrm{G}) = \operatorname{Lie}(\operatorname{Ad}(G_{\mathrm{cov}}))$ because every derivation of a semisimple algebra is inner; two connected subgroups of a Lie group with equal Lie algebras coincide, so $\operatorname{Ad}(G_{\mathrm{cov}}) = \operatorname{Aut}(\mathrm{G})_0$. For (c), an automorphism of $\mathrm{G}$ permutes the simple roots and preserves the Cartan matrix, hence induces an automorphism of the Dynkin diagram; the kernel of the resulting map to the diagram automorphisms is the identity component, and the diagram automorphisms of the listed types are the classical outer automorphisms.

## The Automorphism Group

### $\operatorname{Aut}(\mathrm{G})$ and the Adjoint Group

**Definition.** The **automorphism group** $\operatorname{Aut}(\mathrm{G})$ is the group of Lie algebra automorphisms of $\mathrm{G}$; the **adjoint group** is $\operatorname{Ad}(G) = \operatorname{Int}(\mathrm{G})$, the image of a connected $G$ with Lie algebra $\mathrm{G}$.

**Theorem.** $\operatorname{Aut}(\mathrm{G})$ is a Lie group with Lie algebra $\operatorname{Der}(\mathrm{G})$, the derivations of $\mathrm{G}$ under the commutator. Its identity component is $\operatorname{Aut}(\mathrm{G})_0 = \operatorname{Ad}(G_{\mathrm{cov}})$, and

$$
\operatorname{Out}(\mathrm{G}) = \operatorname{Aut}(\mathrm{G})/\operatorname{Ad}(G_{\mathrm{cov}})
$$

is the finite group of outer automorphisms in the semisimple case.

**Proof sketch.** The automorphism group is a closed subgroup of $GL(\mathrm{G})$ and hence a Lie group by the closed subgroup theorem; differentiating the identity $\varphi([x,y]) = [\varphi x, \varphi y]$ at $\varphi = \mathrm{id}$ gives the derivation condition, so the Lie algebra is $\operatorname{Der}(\mathrm{G})$. The identity component statement follows because $\operatorname{Ad}(G_{\mathrm{cov}})$ and $\operatorname{Aut}(\mathrm{G})_0$ are connected subgroups with the same Lie algebra, by the inner-derivation theorem.

### The Adjoint Representation in Coordinates

**Example.** Let $\mathrm{G} = \mathrm{SL}(2, \mathbb{C})$ with basis $e, h, f$ and let $G = SL_2(\mathbb{C})$. The adjoint map on the group is conjugation of matrices, and $\operatorname{Ad}(g)X = gXg^{-1}$; on the algebra, $\operatorname{ad}_x(y) = [x,y]$. For $g = \operatorname{diag}(t, t^{-1})$ one has

$$
\operatorname{Ad}(g)e = t^2 e, \qquad \operatorname{Ad}(g)f = t^{-2} f, \qquad \operatorname{Ad}(g)h = h,
$$

so the weights of the adjoint representation are the roots $\alpha, 0, -\alpha$, exactly as the root space decomposition of *Root Systems and Classification* requires. The kernel of $\operatorname{Ad}$ is the centre $\{\pm I\}$, and $\operatorname{Ad}(SL_2(\mathbb{C})) = PSL_2(\mathbb{C})$ is the adjoint group of type $A_1$.

**Example.** For $\mathrm{G} = \mathrm{SO}(3)$ and $G = SO(3)$, the adjoint representation is the standard three-dimensional representation, $SO(3) \cong \operatorname{Ad}(SO(3)) = \operatorname{Aut}(\mathrm{SO}(3))_0$, and $\operatorname{Out}(\mathrm{SO}(3)) = 1$; the situation differs from $SU(2)$, where $\operatorname{Ad}$ has the nontrivial discrete kernel.

## Coverings and the Lattice of Connected Subgroups

**Theorem.** Let $G$ be a connected Lie group with Lie algebra $\mathrm{G}$ and universal cover $\pi : G_{\mathrm{cov}} \to G$. Then:

**(a)** $D = \ker\pi$ is a discrete central subgroup of $G_{\mathrm{cov}}$ isomorphic to $\pi_1(G)$;

**(b)** every connected Lie group with Lie algebra $\mathrm{G}$ is a quotient of $G_{\mathrm{cov}}$ by a discrete central subgroup, and the covering homomorphisms between them correspond to inclusions of the subgroups;

**(c)** if $G$ is simply connected and $H$ is any Lie group with Lie algebra $\mathrm{H}$, then $\operatorname{Hom}(G, H)$ is in bijection with $\operatorname{Hom}(\mathrm{G}, \mathrm{H})$; in particular, when $\mathrm{H} = \mathrm{G}$, the isomorphisms $G \to H$ correspond to the automorphisms of $\mathrm{G}$, and the image of a homomorphism with invertible differential is a connected subgroup with the same algebra.

**Proof.** Parts (a) and (b) are the Lie correspondence above; (c) is the bijection on homomorphisms applied to $\operatorname{Hom}(\mathrm{G}, \mathrm{H})$ and the fact that a homomorphism of connected groups is determined by its differential.

**Example.** For $\mathrm{G} = \mathbb{R}$ the simply connected group is $\mathbb{R}$, and the discrete central subgroups are the lattices $\lambda\mathbb{Z}$; the quotients are $S^1$ for each $\lambda \neq 0$, all isomorphic, together with $\mathbb{R}$ itself. This is the simplest illustration of the partially ordered set of connected groups with a given algebra and of the failure of the Lie functor to be injective on objects: the classification requires the subgroup, not only the algebra.

## The Classical Groups with a Given Algebra

**The recipe.** Four steps produce every row of the table below. Write the algebra $\mathrm{G}$. Name its simply connected group $G_{\mathrm{cov}}$, which exists and is unique by the correspondence. Compute the centre $Z(G_{\mathrm{cov}})$, which for a connected matrix group is $\ker\operatorname{Ad}$ by *The Adjoint Representation* above. List the discrete central subgroups $\Gamma \subseteq Z(G_{\mathrm{cov}})$ and read the quotients $G_{\mathrm{cov}}/\Gamma$, whose fundamental group is $\Gamma$.

**Theorem.** For a compact semisimple algebra the fourth column is the complete list of connected groups with that algebra, and the fifth gives their fundamental groups. For $\mathbb{R}$ the list is complete as well, the quotients being $S^1$ for every non-zero lattice together with $\mathbb{R}$ itself. For $\mathrm{U}(n)$ the row records $U(n)$ and its central quotients; the full list is longer, because the centre has a vector factor and the quotients then form a continuous family as in the abelian case.

The fundamental groups themselves are computed in *The Fundamental Group of a Lie Group*; the table records them only to show which group a given $\Gamma$ produces.

| Lie algebra | simply connected group | centre of the cover | connected groups | fundamental groups |
|---|---|---|---|---|
| $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R}$; $\mathbb{R}/a\mathbb{Z} \cong S^1$, $a>0$ | $0$; $\mathbb{Z}$ |
| $\mathrm{SU}(2)$ | $SU(2)$ | $\mathbb{Z}/2$ | $SU(2)$; $SO(3)$ | $0$; $\mathbb{Z}/2$ |
| $\mathrm{SL}(2,\mathbb{R})$ | $\widetilde{SL_2(\mathbb{R})}$ | $\mathbb{Z}$ | $\widetilde{SL_2(\mathbb{R})}$; $SL_2(\mathbb{R})$; $PSL_2(\mathbb{R})$ | $0$; $\mathbb{Z}$; $\mathbb{Z}$ |
| $\mathrm{SO}(3,1)$ | $SL_2(\mathbb{C})$ | $\mathbb{Z}/2$ | $SL_2(\mathbb{C})$; $SO^+(3,1)$ | $0$; $\mathbb{Z}/2$ |
| $\mathrm{SO}(4)$ | $SU(2)\times SU(2)$ | $\mathbb{Z}/2\times\mathbb{Z}/2$ | $S^3\times S^3$; $SO(4)$; $SO(3)\times SU(2)$; $SU(2)\times SO(3)$; $SO(3)\times SO(3)$ | $0$; $\mathbb{Z}/2$ |
| $\mathrm{SO}(n)$, $n\geq3$ | $Spin(n)$ | the second table | $Spin(n)$ and its quotients | $0$; $\mathbb{Z}/2$; further entries |
| $\mathrm{U}(n)$, $n\geq1$ | $SU(n)\times\mathbb{R}$ | $\mathbb{Z}/n\times\mathbb{R}$ | $U(n)$; its central quotients $U(n)/\mu_d$ | $\mathbb{Z}$ |

The centre of the spin group depends on the residue of $n$ modulo four.

| $n$ | $Z(Spin(n))$ | number of connected groups with algebra $\mathrm{SO}(n)$ |
|---|---|---|
| odd, $n\geq3$ | $\mathbb{Z}/2$ | $2$ |
| $n\equiv2\pmod4$ | $\mathbb{Z}/4$ | $3$ |
| $n\equiv0\pmod4$ | $\mathbb{Z}/2\times\mathbb{Z}/2$ | $5$ |

**Remark (the count is the number of subgroups).** A quotient of the cover is determined by the subgroup, and only the subgroups of the centre give quotients of the same dimension. The group $\mathbb{Z}/2$ has two subgroups, $\mathbb{Z}/4$ has three, and $\mathbb{Z}/2\times\mathbb{Z}/2$ has five. For odd $n$ the two groups are $Spin(n)$ and $SO(n)$; for $n\equiv2\pmod4$ the third is $Spin(n)$ modulo its whole centre, with $\pi_1 = \mathbb{Z}/4$; for $n\equiv0\pmod4$ the three beyond $SO(n)$ are the two semi-spin quotients and the quotient by the whole centre. For $n=2$ the pattern fails at the notation: $SO(2) = S^1$ has algebra $\mathbb{R}$ and cover $\mathbb{R}$, and $Spin(2) = S^1$ is not simply connected.

**Remark ($Spin(4)$ and the quaternions).** $Spin(4) \cong SU(2)\times SU(2) \cong S^3\times S^3$ acts on $\mathbb{H}\cong\mathbb{R}^4$ by $(u_1,u_2)(x) = u_1xu_2^{-1}$. The kernel is $\{(\pm1,\pm1)\}$ with the same sign, the map is two-to-one, and its image is $SO(4)$. Quotienting by the three subgroups of order two gives $SO(4)$, $SO(3)\times SU(2)$ and $SU(2)\times SO(3)$, and quotienting by the whole centre gives $SO(3)\times SO(3)$. Five groups, one algebra, all realised on the quaternions.

**Remark (which subgroup gives which quotient).** The order is reversed: a larger $\Gamma$ gives a smaller group. For $\mathrm{SL}(2,\mathbb{R})$ the centre of the cover is infinite cyclic, generated by an element $z$ whose image is $-I$. The subgroup $2\mathbb{Z}$ gives $SL_2(\mathbb{R}) = \widetilde{SL_2(\mathbb{R})}/2\mathbb{Z}$ and the whole $\mathbb{Z}$ gives $PSL_2(\mathbb{R}) = SL_2(\mathbb{R})/\{\pm I\}$; both have fundamental group $\mathbb{Z}$, and the cover has none.

**Remark (the cover need not be a matrix group).** $SL_2(\mathbb{R})$ is a group of matrices and $\widetilde{SL_2(\mathbb{R})}$ is not. Every finite-dimensional representation of the algebra $\mathrm{SL}(2,\mathbb{R})$ exponentiates to the group $SL_2(\mathbb{R})$, since the irreducible ones are the symmetric powers of the defining representation, so every finite-dimensional representation of the cover is trivial on the kernel $\mathbb{Z}$ and none is faithful. The correspondence is therefore not a statement about matrix groups: the cover exists as a Lie group whether or not it can be written with matrices.

**Remark ($\mathrm{U}(n)$).** The centre of $SU(n)$ is $\mu_n = \{\zeta I : \zeta^n = 1\}$, and the cover is $SU(n)\times\mathbb{R}$ with the map $(A,t)\mapsto e^{it}A$. The kernel is generated by $(\zeta^{-1}I,\,2\pi/n)$, cyclic of infinite order, so $U(n) = (SU(n)\times\mathbb{R})/\mathbb{Z}$ and $\pi_1(U(n)) = \mathbb{Z}$, a generator being the loop $t\mapsto\operatorname{diag}(e^{it},1,\dots,1)$.

**Remark (a continuous family).** For $\mathrm{G} = \mathbb{R}^k$ the discrete central subgroups are the lattices, and two lattices give isomorphic tori exactly when one is the image of the other under an automorphism of $\mathbb{R}^k$. The connected groups with an abelian algebra therefore form a continuous family and not a finite list. For a semisimple algebra the list is finite, because the centre of the cover is then finite and has finitely many subgroups.

**Warning (the subgroup is not a function of the algebra).** The algebra fixes the first, second and third columns of the table and stops there. The fourth column is the list of possibilities, and nothing in the bracket selects one of them. Different choices of $\Gamma$ give different groups with the same algebra, and the difference is invisible to every construction made from the bracket. The fundamental group, which is $\Gamma$, is extra data.

## What the Lie Algebra Does Not Determine

The correspondence is exact, and it is exact about one thing: the algebra fixes the simply connected group. For any other connected group with that algebra the pair $(\mathrm{G},\Gamma)$ fixes the group, and the second entry leaves no trace in the first. The items below are the ones a reader is most likely to attribute to the algebra and should not.

### The Fundamental Group

$SU(2)$ and $SO(3)$ have the same Lie algebra $\mathrm{SU}(2)$ and fundamental groups $0$ and $\mathbb{Z}/2$. $\mathbb{R}$ and $S^1$ have the same Lie algebra $\mathbb{R}$ and fundamental groups $0$ and $\mathbb{Z}$. In both pairs the groups are connected, the bracket is the same, and only the exponential map tells them apart, being injective on $\mathbb{R}$ and $2\pi$-periodic on $S^1$. No computation inside the bracket can separate them, because the bracket is the derivative of the group law at a single point.

### Compactness

The algebra does not fix compactness, but it fixes it modulo the centre, and that is the precise statement.

**Theorem.** Let $\mathrm{G}$ be a compact Lie algebra, that is, a Lie algebra with negative semidefinite Killing form, and let $G$ be a connected group with Lie algebra $\mathrm{G}$. Then $\operatorname{Ad}(G)$ is compact, equivalently $G/Z(G)$ is compact. If $\mathrm{G}$ is semisimple as well, then $G$ is compact.

**Proof.** A compact algebra decomposes as $\mathrm{G} = \mathrm{Z}(\mathrm{G})\oplus[\mathrm{G},\mathrm{G}]$, with $[\mathrm{G},\mathrm{G}]$ compact semisimple, by *Structure of Lie Algebras*. The adjoint representation kills $\mathrm{Z}(\mathrm{G})$, so $\operatorname{Ad}(G)$ is the adjoint image of the simply connected group $\widetilde S$ of $[\mathrm{G},\mathrm{G}]$, which is compact because its Killing form is negative definite. Hence $\operatorname{Ad}(G) = \widetilde S/Z(\widetilde S)$ is compact. When $\mathrm{G}$ is semisimple the centre of the cover is finite, so $G$ is a finite quotient of a compact group.

**Example.** The algebra $\mathbb{R}$ is compact, its Killing form being zero, and it carries the non-compact $\mathbb{R}$ and the compact $S^1$. The theorem is not contradicted: $Z(\mathbb{R}) = \mathbb{R}$ and $Z(S^1) = S^1$, and in both groups the quotient by the centre is a point. The ambiguity therefore lives in the centre, and it disappears for a semisimple algebra, where the centre of the cover is finite: every connected group with a compact semisimple algebra is compact, and none with a non-compact semisimple algebra is.

### The Real Form

A complex algebra has several real forms and the correspondence is run after one of them is chosen. The complex algebra $\mathrm{SL}(2,\mathbb{C})$ has exactly two, $\mathrm{SU}(2)$ and $\mathrm{SL}(2,\mathbb{R})$, as *Real Forms of a Complex Lie Algebra* states; their simply connected groups are $SU(2)$ and $\widetilde{SL_2(\mathbb{R})}$, and nothing global is shared. The first is compact and simply connected; the second is neither. Reading a complex group as a real one doubles the dimension and gives the realification: $\mathrm{SL}(2,\mathbb{C})$ read over $\mathbb{R}$ is $\mathrm{SO}(3,1)$, the algebra of the Lorentz group. The real form is therefore a choice that precedes the choice of $\Gamma$, and no statement about it follows from the complex algebra alone.

### The Unitary Representations

Two different failures are collected here, and they belong to different entries of the pair.

The first is the choice of $\Gamma$. The spin-$\tfrac12$ representation of $\mathrm{SU}(2)$ has dimension two, and $-I$ acts on it as $-1$; it is a representation of $SU(2)$ and not of $SO(3)$, although the two groups have the same algebra. The algebra fixes the representations of the cover, and $\Gamma$ fixes which of them descend to the group.

The second is the choice of real form. $SU(2)$ has only finite-dimensional unitary irreducible representations, the spins $j\in\tfrac12\mathbb{Z}_{\geq0}$. The group $\widetilde{SL_2(\mathbb{R})}$ has no nontrivial finite-dimensional unitary representation at all, because the image of such a representation would be a compact subgroup of a unitary group while $\mathrm{SL}(2,\mathbb{R})$ is simple and non-compact, and it has infinite-dimensional unitary irreducible representations instead. The two groups have different real algebras, so this is a case of the previous subsection; the unitary dual is a function of the real algebra and not of its complexification.

### The Exponential Map

The exponential map is a local diffeomorphism and nothing more, and it cannot be used to pass from the algebra to the group. It is surjective for a compact connected group, and for a simply connected nilpotent group, and it fails for $SL_2(\mathbb{R})$. For $X$ of trace zero the eigenvalues of $\exp X$ are $e^{\lambda}$ and $e^{-\lambda}$ for one complex number $\lambda$, so they are both positive when $\lambda$ is real and a complex conjugate pair when $\lambda$ is imaginary. Two distinct negative real eigenvalues do not occur. The matrix $\operatorname{diag}(-2,-\tfrac12)$ lies in $SL_2(\mathbb{R})$ and has exactly those eigenvalues, so it is not an exponential, and the missed set is precisely the elements conjugate to $\operatorname{diag}(-a,-1/a)$ with $a>0$ and $a\neq1$. A scan of $100$ random traceless matrices produces no exponential with two distinct negative real eigenvalues.

The failure is not repaired by passing to the cover. If $g\in G_{\mathrm{cov}}$ satisfied $g = \exp(X)$ then its image would satisfy $\pi(g) = \exp(d\pi X)$, so an element of $G$ that is missed by the exponential of $G$ has all its lifts missed by the exponential of $G_{\mathrm{cov}}$. The exponential of $\widetilde{SL_2(\mathbb{R})}$ is therefore not surjective either, and the same argument applies to every group in the same row.

**Warning (what the algebra leaves to $\Gamma$).** The algebra fixes $G_{\mathrm{cov}}$ and the local structure. It fixes nothing else about $G$: the fundamental group, the compactness and the unitary dual are functions of $\Gamma$ once $\mathrm{G}$ is fixed, and none of them is a function of $\mathrm{G}$. When the algebra is complex, the real form is a further choice that precedes $\Gamma$. A statement derived from the Lie algebra alone is therefore a statement about the cover, and it must be checked against $\Gamma$ before it is asserted of the group.

## Summary

The functor $\operatorname{Lie}$ from Lie groups to Lie algebras is neither full nor faithful; it preserves exactly the local structure, and a homomorphism is a local isomorphism precisely when it induces an isomorphism of Lie algebras. For a simply connected source $G$ the map $\varphi \mapsto d\varphi_e$ is a bijection from $\operatorname{Hom}(G,H)$ to $\operatorname{Hom}(\mathrm{G},\mathrm{H})$, so the simply connected Lie groups and the finite-dimensional Lie algebras form equivalent categories, and Lie's third theorem says that every finite-dimensional real Lie algebra occurs.

Every connected Lie group $G$ with algebra $\mathrm{G}$ is a quotient $G_{\mathrm{cov}}/D$ of its simply connected cover by a discrete central subgroup $D \cong \pi_1(G)$, so the connected groups with a given algebra are classified by those subgroups, and the fundamental group of $G$ is abelian. Lie subalgebras correspond to connected immersed subgroups, ideals to normal connected subgroups, and quotients of algebras to quotients of groups; closed subgroups of a Lie group are embedded Lie subgroups by the closed subgroup theorem.

The adjoint representation $\operatorname{Ad} : G \to GL(\mathrm{G})$ is a group homomorphism with $d(\operatorname{Ad})_e = \operatorname{ad}$ and $\operatorname{Ad}(\exp X) = \exp(\operatorname{ad}_X) = \sum_k (\operatorname{ad}_X)^k/k!$; it preserves the Killing form, its kernel is the centre $Z(G)$ for connected $G$, and its image is the adjoint group. For a semisimple algebra the kernel is discrete, the identity component of the automorphism group is the adjoint group because every derivation is inner, and the outer automorphism group is finite, acting through the automorphisms of the Dynkin diagram.

The classical groups show what the choice of $\Gamma$ carries. The algebra $\mathrm{SU}(2)$ gives $SU(2)$ and $SO(3)$; $\mathrm{SL}(2,\mathbb{R})$ gives $\widetilde{SL_2(\mathbb{R})}$, $SL_2(\mathbb{R})$ and $PSL_2(\mathbb{R})$; $\mathrm{SO}(4)$ gives five groups, all realised on the quaternions; $\mathrm{U}(n)$ comes from the cover $SU(n)\times\mathbb{R}$. Along each row the fundamental group, the compactness and the unitary dual vary, and none of them is a function of the algebra: the algebra fixes the cover, and $\Gamma$ fixes the rest. The compactness is fixed only modulo the centre, and it is fixed outright for a semisimple algebra, where the centre of the cover is finite. The real form, when the algebra is complex, is a choice that precedes $\Gamma$. The exponential map is a local object, surjective for a compact connected group and not for $SL_2(\mathbb{R})$ or its cover.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{K}$ | $\mathbb{R}$ or $\mathbb{C}$; the base of the Lie groups |
| $G, H$ | Connected Lie groups over $\mathbb{K}$ |
| $\mathrm{G} = \operatorname{Lie}(G)$ | Lie algebra of $G$; $T_eG$ with the bracket |
| $d\varphi_e$ | Differential at the identity; a Lie algebra homomorphism |
| $\operatorname{Hom}(G,H)$, $\operatorname{Hom}(\mathrm{G},\mathrm{H})$ | Lie group and Lie algebra homomorphisms; $\varphi \mapsto d\varphi_e$ is a bijection between them |
| $\operatorname{Lie} : \mathbf{LieGrp} \to \mathbf{LieAlg}$ | The Lie functor; neither full nor faithful |
| $\varphi : G \to H$ local isomorphism | $d\varphi_e$ invertible; then $\varphi$ is a covering for connected $G, H$ |
| $G_{\mathrm{cov}}, \pi : G_{\mathrm{cov}} \to G$ | Simply connected cover; $\ker\pi \cong \pi_1(G)$, discrete and central |
| $G \cong G_{\mathrm{cov}}/D$ | Classification of connected groups with a given algebra by discrete central $D$ |
| $\Gamma \subseteq Z(G_{\mathrm{cov}})$ | Discrete central subgroup; $G = G_{\mathrm{cov}}/\Gamma$ and $\Gamma \cong \pi_1(G)$ |
| $Z(G_{\mathrm{cov}})$ | Centre of the cover: finite, a torus, a vector space, or a product |
| compact Lie algebra | Negative semidefinite Killing form; then $\operatorname{Ad}(G)$ is compact for every connected $G$ |
| $\mu_n$ | The centre $\{\zeta I : \zeta^n = 1\}$ of $SU(n)$ |
| $Spin(n)$ | The simply connected cover of $SO(n)$ for $n \geq 3$; $Spin(2) = S^1$ is not simply connected |
| $\mathrm{H} \subseteq \mathrm{G} \longleftrightarrow H \subseteq G$ | Lie subalgebras correspond to connected immersed subgroups |
| $\mathrm{H}$ an ideal $\iff H$ normal | Then $\operatorname{Lie}(G/H) = \mathrm{G}/\mathrm{H}$ |
| $c_g(h) = ghg^{-1}$ | Conjugation by $g$ |
| $\operatorname{Ad}(g) = d(c_g)_e$ | Adjoint representation of $G$ on $\mathrm{G}$ |
| $\operatorname{ad}_x(y) = [x,y]$ | Adjoint representation of $\mathrm{G}$; $d(\operatorname{Ad})_e = \operatorname{ad}$ |
| $\mathrm{GL}(\mathrm{G})$ | Endomorphisms of $\mathrm{G}$; the target of $\operatorname{ad}$ |
| $\operatorname{Ad}(\exp X) = \exp(\operatorname{ad}_X)$ | The exponential intertwines $\operatorname{Ad}$ and $\operatorname{ad}$ |
| $\ker(\operatorname{Ad}) = Z(G)$ | Centre of a connected group |
| $\operatorname{Lie}(Z(G)) = \mathrm{Z}(\mathrm{G})$ | Centre of the Lie algebra |
| $\operatorname{Aut}(\mathrm{G})$, $\operatorname{Der}(\mathrm{G})$ | Automorphisms; derivations; $\operatorname{Lie}(\operatorname{Aut}(\mathrm{G})) = \operatorname{Der}(\mathrm{G})$ |
| $\operatorname{Ad}(G) = \operatorname{Int}(\mathrm{G})$ | Adjoint group; $\operatorname{Aut}(\mathrm{G})_0$ in the semisimple case |
| $\operatorname{Out}(\mathrm{G}) = \operatorname{Aut}(\mathrm{G})/\operatorname{Ad}(G_{\mathrm{cov}})$ | Finite outer automorphism group; diagram automorphisms |

## Further Reading

- John M. Lee, *Introduction to Smooth Manifolds* (Springer, 2nd ed. 2013), for local diffeomorphisms, coverings, and the closed subgroup theorem.
- John F. Adams, *Lectures on Lie Groups* (University of Chicago Press, 1969), for the Lie correspondence and the adjoint representation.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (American Mathematical Society, 2001), for the analytic subgroup theorem and the classification of connected groups.
- V. S. Varadarajan, *Lie Groups, Lie Algebras, and Their Representations* (Springer, 1984), for the correspondence between subalgebras, subgroups and ideals.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2nd ed. 2015), for the Lie correspondence with matrix groups and the adjoint representation.
- Jean-Pierre Serre, *Lie Algebras and Lie Groups* (Springer, 1992), for Lie's third theorem and the equivalence of categories.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the automorphism group, inner derivations, and the outer automorphism group.
- A. L. Onishchik and E. B. Vinberg, *Lie Groups and Lie Algebras I: Foundations of Lie Theory* (Springer, 1994), for the classification of the connected groups with a given Lie algebra and the centres of the classical covers.
- J. J. Duistermaat and J. A. C. Kolk, *Lie Groups* (Springer, 2000), for the exponential map, its surjectivity on compact groups, and the counterexamples.
