
# __Affine Spaces and Translations__

## Introduction

A vector space has a distinguished point, its origin, and every linear statement is made with respect to it. An affine space is what remains when the origin is forgotten: a set of points on which the additive group of a vector space acts freely and transitively, so that any two points determine a difference vector but no point is singled out. This is a torsor structure, and it is the correct language for geometry, since points, lines, planes, barycentres and distances are all affine notions and none of them survives the loss of translational symmetry that a fixed origin would impose.

Throughout, $F$ is a field, $V$ is an $F$-vector space of dimension $n$, and an affine space with direction $V$ is a set $\mathbb{A}$ equipped with a free and transitive action of $(V,+)$. Translating between the affine and linear pictures is done by choosing an origin, and every construction in the article is checked to be independent of that choice. The affine group $\operatorname{Aff}(V)=V \rtimes \operatorname{GL}(V)$ is the symmetry group of the affine structure, exactly as $\operatorname{GL}(V)$ is the symmetry group of the linear structure; the final sections specialise to the Euclidean case, where the relevant subgroup is $V \rtimes O(V,Q)$, and to a form of arbitrary signature.

## Affine Spaces

### Definition as a Torsor

**Definition.** Let $V$ be a vector space. An **affine space** with direction $V$ is a set $\mathbb{A}$ together with a map

$$
\mathbb{A} \times V \longrightarrow \mathbb{A}, \qquad (a,v) \longmapsto a+v,
$$

such that (i) $a+0=a$ and $(a+v)+w=a+(v+w)$ for all $a \in \mathbb{A}$, $v,w \in V$; (ii) for every $a,b \in \mathbb{A}$ there is exactly one $v \in V$ with $a+v=b$. The unique such $v$ is written $b-a$, and $\mathbb{A}$ is called a **torsor** under $V$. Its elements are **points**, and $V$ is the **direction space**.

Condition (i) says that $V$ acts on $\mathbb{A}$; condition (ii) says the action is free (if $a+v=a$ then $v=0$) and transitive. Free and transitive actions are called **simply transitive**.

**Proposition.** With the notation above, for all points $a,b,c$:

(i) $a-a=0$ and $b-a=-(a-b)$;

(ii) $(c-b)+(b-a)=c-a$;

(iii) $a+(b-a)=b$.

*Proof.* All three are immediate from the uniqueness in the definition: the element $c-a$ is the unique $v$ with $a+v=c$, and evaluating the left-hand sides at $a$ gives $c$. $\square$

### Choosing an Origin

**Definition.** An **origin** in $\mathbb{A}$ is a point $o \in \mathbb{A}$. Given $o$, the **position map** is

$$
\varphi_o:\mathbb{A} \longrightarrow V, \qquad a \longmapsto a-o .
$$

**Proposition.** For every origin $o$, the position map $\varphi_o$ is a bijection. For two origins $o,o'$,

$$
\varphi_{o'}(a)=\varphi_o(a)-(o'-o),
$$

so the two identifications of $\mathbb{A}$ with $V$ differ by the translation $v \mapsto v-(o'-o)$. Consequently any statement about $\mathbb{A}$ that is to be intrinsic must be invariant under the translations of $V$.

*Proof.* The map is a bijection because for each $v$ there is a unique $a=o+v$ with $a-o=v$. The relation $\varphi_{o'}(a)=a-o'=(a-o)-(o'-o)$ gives the second statement. $\square$

The content of the definition is thus that an affine space is a vector space **together with a forgotten origin**, and the choice of an origin converts it into a vector space in a way that is canonical only up to translation. This is why statements in affine geometry come in two forms: an intrinsic form using differences of points, and a coordinate form after an origin is chosen.

**Example.** The set of solutions of a consistent system $Ax=b$ is an affine space with direction $\ker A$, by the rank criterion of the linear-maps article: if $x_0$ is one solution, every solution is $x_0+u$ with $Au=0$.

## Translations

### The Translation Group

**Definition.** For $v \in V$, the **translation** by $v$ is the map

$$
t_v:\mathbb{A} \longrightarrow \mathbb{A}, \qquad t_v(a)=a+v .
$$

**Proposition.** (i) $t_0=\operatorname{id}_{\mathbb{A}}$ and $t_v \circ t_w=t_{v+w}$, so $v \mapsto t_v$ is an injective homomorphism $(V,+) \to \operatorname{Sym}(\mathbb{A})$; the image $T(\mathbb{A})=\{t_v\}$ is the **translation group**, isomorphic to $(V,+)$ and normal in the group of all affine automorphisms.

(ii) For $v \neq 0$, the translation $t_v$ has no fixed point.

(iii) No translation $t_v$ with $v \neq 0$ is linear, for any choice of origin making $\mathbb{A}=V$: in that identification $t_v(x)=x+v$ and $t_v(0)=v \neq 0$.

*Proof.* (i) is the action axiom. (ii) $t_v(a)=a$ means $a+v=a$, hence $v=0$ by freeness. (iii) A linear map sends $0$ to $0$, and $t_v(0)=v \neq 0$. $\square$

Part (iii) is the precise sense in which translations are not linear maps but **affine** maps: they preserve the affine structure and not the linear structure. The failure is exactly the displacement of the origin, and it is not repaired by a change of origin, since changing the origin leaves a translation unchanged; conjugation by a general affine map $(T,b)$ carries $t_v$ to $t_{Tv}$, so the translations form a normal subgroup isomorphic to $V$.

### Simply Transitive Action

**Proposition.** The translation group acts simply transitively on $\mathbb{A}$. Consequently, after the choice of any point $o$, the map $t_v \mapsto o+v$ is a bijection $T(\mathbb{A}) \to \mathbb{A}$.

*Proof.* Transitivity is axiom (ii): for any $a,b$ there is $v$ with $b=a+v=t_v(a)$. Freeness is (ii) as well: if $t_v(a)=a$ then $v=0$. $\square$

## The Affine Group

### Definition and Composition

**Definition.** An **affine automorphism** of $\mathbb{A}$ is a bijection $f:\mathbb{A} \to \mathbb{A}$ such that $f(a+v)=f(a)+L(v)$ for a linear map $L \in \operatorname{GL}(V)$ and all $a,v$. The group of affine automorphisms is the **affine group** $\operatorname{Aff}(\mathbb{A})=\operatorname{Aff}(V)$.

**Proposition.** Affine automorphisms are exactly the maps of the form

$$
f(a)=o'+T(a-o)
$$

for some origin $o \in \mathbb{A}$, some $T \in \operatorname{GL}(V)$ and some $o' \in \mathbb{A}$. The linear part $T$ is independent of $o$, and $\operatorname{Aff}(V) \cong V \rtimes \operatorname{GL}(V)$, where the semidirect product is taken with respect to the natural action of $\operatorname{GL}(V)$ on $V$.

*Proof.* Choose an origin $o$ and identify $\mathbb{A}$ with $V$ by $a \mapsto a-o$. Then an affine automorphism becomes a map $x \mapsto Tx+b$ with $T \in \operatorname{GL}(V)$ and $b \in V$, and every such map is an affine automorphism. Composition is

$$
(x \mapsto T_1x+b_1)\circ(x \mapsto T_2x+b_2)=(x \mapsto T_1T_2x+T_1b_2+b_1),
$$

which is the multiplication law $(T_1,b_1)(T_2,b_2)=(T_1T_2,\,T_1b_2+b_1)$ of the semidirect product $V \rtimes \operatorname{GL}(V)$ with $\operatorname{GL}(V)$ acting on $V$ in the standard way. Changing the origin conjugates the pair by a translation from the translation subgroup $V$, so the decomposition is intrinsic. $\square$

In the notation $(T,b)$ for the map $x \mapsto Tx+b$, the exact sequence

$$
1 \longrightarrow V \longrightarrow \operatorname{Aff}(V) \longrightarrow \operatorname{GL}(V) \longrightarrow 1
$$

is split by $T \mapsto (T,0)$, and the action of $\operatorname{GL}(V)$ on the normal translation subgroup $V$ is the defining representation. For $n \ge 1$ the affine group is generated by the translations and the linear maps: every element is the product $(T,b)=(I,b)(T,0)$ of a translation and a linear map, while the opposite product is $(T,0)(I,b)=(T,Tb)$, so the order of the factors is not interchangeable.

### Invariants

**Proposition.** $\operatorname{Aff}(V)$ acts transitively on $\mathbb{A}$, and the stabiliser of a point $o$ is the subgroup $\{(T,0)\} \cong \operatorname{GL}(V)$ of linear maps fixing $o$. The action is $2$-transitive for $n \ge 1$: it is transitive on ordered pairs of distinct points.

*Proof.* Transitivity: $(0,b)$ sends $o$ to $o+b$, so the translations already act transitively. The stabiliser of $o$ consists of the maps $x \mapsto Tx$ with $b=0$, a copy of $\operatorname{GL}(V)$. For $2$-transitivity, given distinct $a,b$ and distinct $a',b'$, choose $T \in \operatorname{GL}(V)$ with $T(b-a)=b'-a'$, and then a translation correcting the images of $a$. $\square$

## Affine Combinations and Independence

### Barycentres

**Definition.** Let $a_1,\dots,a_k \in \mathbb{A}$ and $\lambda_1,\dots,\lambda_k \in F$ with $\sum_i\lambda_i=1$. The **affine combination** $\sum_i\lambda_ia_i$ is the point

$$
o+\sum_{i=1}^{k}\lambda_i(a_i-o),
$$

which is independent of the origin $o$. When all $\lambda_i=1/k$ and $k$ is invertible in $F$, this point is the **barycentre** of $a_1,\dots,a_k$.

**Proposition.** The affine combination is well defined, and it is the unique point $b$ such that $\sum_i\lambda_i(b-a_i)=0$ in the sense of the difference map.

*Proof.* Independence of the origin: for $o'$ another origin,

$$
o'+\sum_i\lambda_i(a_i-o')=o+\sum_i\lambda_i(a_i-o)+(o'-o)\Bigl(1-\sum_i\lambda_i\Bigr)=o+\sum_i\lambda_i(a_i-o),
$$

using $\sum_i\lambda_i=1$. The characterisation is immediate from the definition. $\square$

The requirement $\sum\lambda_i=1$ is what replaces the condition for a linear combination to be well defined without a chosen zero; a linear combination of points has no intrinsic meaning. Over a field of characteristic $p$ and a set of $p$ points, the barycentre with weights $1/p$ does not exist, and one uses instead any weights summing to $1$ that avoid the characteristic.

### Affine Independence and Bases

**Definition.** Points $a_0,\dots,a_k \in \mathbb{A}$ are **affinely independent** if the vectors $a_1-a_0,\dots,a_k-a_0$ are linearly independent in $V$. An **affine basis** of $\mathbb{A}$ is a set of $n+1$ affinely independent points.

**Proposition.** $a_0,\dots,a_k$ are affinely independent if and only if the only relation $\sum_i\lambda_ia_i=0$ in the sense of affine combinations with $\sum_i\lambda_i=0$ is the trivial one $\lambda_0=\cdots=\lambda_k=0$. Every affine basis $a_0,\dots,a_n$ gives every point $b \in \mathbb{A}$ a unique expression

$$
b=\sum_{i=0}^{n}\alpha_ia_i, \qquad \sum_{i=0}^{n}\alpha_i=1,
$$

the **barycentric coordinates** $(\alpha_0,\dots,\alpha_n)$ of $b$ with respect to the basis.

*Proof.* Translating by $a_0$ turns the vectors $a_i-a_0$ into a basis of $V$, and $b-a_0$ has a unique expression in that basis; the coefficients together with $\alpha_0=1-\sum_{i\ge1}\alpha_i$ give the statement. $\square$

## Affine Subspaces

### Definition and Incidence

**Definition.** An **affine subspace** of $\mathbb{A}$ is a subset of the form

$$
B=a+W=\{a+w : w \in W\}
$$

for a point $a$ and a linear subspace $W \subseteq V$, called the **direction** of $B$. The dimension of $B$ is $\dim_F W$.

**Proposition.** (i) The direction of a nonempty affine subspace is determined by the set: $W=\{b-c : b,c \in B\}$. (ii) If $B=a+W$ and $C=b+U$ then $B \subseteq C$ if and only if $W \subseteq U$ and $a-b \in U$. (iii) Two affine subspaces with the same direction are either equal or disjoint. (iv) The intersection of two affine subspaces is either empty or an affine subspace with direction $W \cap U$. Two affine subspaces are **parallel** when $W \subseteq U$ or $U \subseteq W$; disjointness alone does not force parallelism, since the skew lines of a three-dimensional space are disjoint and neither direction contains the other.

*Proof.* (i) The differences of elements of $a+W$ are exactly the elements of $W$. (ii) If $B\subseteq C$ then $a \in C$, so $a-b \in U$, and for $w \in W$ one has $a+w \in C$, whence $w=(a+w)-a \in U$ and $W \subseteq U$; conversely $W \subseteq U$ and $a-b \in U$ give $a+W \subseteq b+U$. (iii) If $a+W$ and $b+W$ meet, then $a-b \in W$ by (ii) applied both ways, and the two are equal. (iv) If $c \in B \cap C$ then $B=c+W$, $C=c+U$, and $B \cap C=c+(W \cap U)$. $\square$

For $n=1$ an affine subspace of dimension $1$ is the whole of $\mathbb{A}$, and of dimension $0$ a single point: over a one-dimensional direction space there is nothing else. For $n=2$ the subspaces of dimension $1$ are the **lines**, for $n=3$ the subspaces of dimension $1$ and $2$ are the **lines** and **planes**, and in general a **hyperplane** is an affine subspace of dimension $n-1$, of the form $\{a: \varphi(a-o)=\lambda\}$ for a nonzero linear functional $\varphi$. Two distinct lines in a plane meet in a point or are disjoint and parallel, and this is the intersection statement (iv) with $\dim W=\dim U=1$: either $W=U$ (parallel or equal) or $W \cap U=0$ and the intersection is a single point.

### Affine Maps

**Definition.** An **affine map** $f:\mathbb{A} \to \mathbb{A}'$ between affine spaces with direction spaces $V,V'$ is a map such that $f(a+v)=f(a)+L(v)$ for a linear map $L:V \to V'$ and all $a,v$. The linear map $L$ is the **linear part** of $f$.

**Proposition.** Affine maps are exactly the maps $f(a)=o'+L(a-o)$ for some origins $o,o'$; they form a set $\operatorname{Aff}(\mathbb{A},\mathbb{A}')=\operatorname{Hom}_F(V,V') \times V'$ under the correspondence $(L,b) \leftrightarrow (x \mapsto Lx+b)$ after origins are chosen, and composition is composition of maps. Affine automorphisms are the case $L$ invertible.

*Proof.* The computation is the one already done in coordinates for $\operatorname{Aff}(V)$: composing $x \mapsto L_1x+b_1$ with $x \mapsto L_2x+b_2$ gives $x \mapsto L_1L_2x+L_1b_2+b_1$. $\square$

An affine map with linear part zero is constant; an affine map with $L=\operatorname{id}$ is a translation; an affine map fixing a point $o$ and with $L$ invertible is linear in the coordinates centred at $o$.

## The Euclidean Group

### Isometries are Affine

Let $\mathbb{A}$ be a Euclidean affine space, so that $V$ carries a positive definite inner product $Q$ and the distance between points is $d(a,b)=\sqrt{Q(a-b)}$; define the distance algebraically, without the square root, by $d(a,b)^2=Q(a-b)$.

**Theorem (Mazur–Ulam).** Every bijection $f:\mathbb{A} \to \mathbb{A}$ preserving distances is affine, with linear part in the orthogonal group $O(V,Q)$. Conversely every affine map whose linear part lies in $O(V,Q)$ preserves distances.

*Proof.* The converse is immediate from $Q(Lu,Lv)=Q(u,v)$ for $L \in O(V,Q)$. For the direct statement, $f$ preserves the midpoint operation, hence affine combinations with dyadic coefficients, and continuity or an algebraic substitute extends this to all coefficients; this is the content of the Mazur–Ulam theorem, quoted as standard. $\square$

**Definition.** The **Euclidean group** (or **isometry group**) of $\mathbb{A}$ is

$$
E(\mathbb{A})=V \rtimes O(V,Q),
$$

the subgroup of $\operatorname{Aff}(V)$ with linear part orthogonal.

### Classification of Isometries

**Proposition.** Every isometry of a Euclidean affine space can be written uniquely as the composite of a translation and an isometry fixing a chosen point: $f=t_b \circ L$ with $L \in O(V,Q)$. Its fixed points, if any, form an affine subspace $a+W$ where $W=\ker(L-\operatorname{id})$.

*Proof.* The decomposition is the semidirect product description. Writing $f(x)=Lx+b$, a point $x$ is fixed exactly when $(L-\operatorname{id})x=-b$, so the fixed set is empty when $-b \notin \operatorname{im}(L-\operatorname{id})$, and otherwise it is the coset of $\ker(L-\operatorname{id})$ through any one fixed point, that is, an affine subspace with direction $\ker(L-\operatorname{id})$. $\square$

For a Euclidean plane the possibilities for a non-identity isometry are: a translation (no fixed point, $L=\operatorname{id}$); a rotation (one fixed point, $L$ a rotation by an angle not $0$, the half-turn included); a reflection (fixed line, $L$ a reflection); or a glide reflection (no fixed point, $L$ a reflection, the translation along the reflecting line nonzero). The classification is by the type of the orthogonal part and the position of the translation vector relative to the fixed space of the linear part.

### Forms of Arbitrary Signature

Let $Q$ be a nondegenerate quadratic form of signature $(p,q)$ on a real vector space $V$, and let $\mathbb{A}$ be an affine space with direction $V$. The group relevant to the geometry determined by $Q$ is

$$
G(Q)=V \rtimes O(V,Q),
$$

acting on $\mathbb{A}$ and preserving the polar form of $Q$ on differences of points, $g(u,v)=Q(u+v)-Q(u)-Q(v)$. For the positive definite form this is the Euclidean group; for the split form of signature $(n/2,n/2)$ the polar form is a nondegenerate symmetric form of that signature, whose maximal isotropic subspaces are Lagrangian, and $O(V,Q)$ is the corresponding indefinite orthogonal group. The algebraic structure $V \rtimes O(V,Q)$ is the same in every signature; what changes is the geometry the form defines, and no metric of positive definite type is needed to write down the group.

## Summary

An affine space with direction a vector space $V$ is a set $\mathbb{A}$ on which $V$ acts freely and transitively; equivalently, every ordered pair of points has a unique difference in $V$, and the difference map satisfies $(c-b)+(b-a)=c-a$. Choosing an origin identifies $\mathbb{A}$ with $V$, and two origins differ by a translation, so an affine space is a vector space with its origin forgotten.

The translations $t_v(a)=a+v$ form a normal subgroup isomorphic to $(V,+)$ and act simply transitively; a nonzero translation has no fixed point and is not linear. The affine group $\operatorname{Aff}(\mathbb{A})=\operatorname{Aff}(V)\cong V \rtimes \operatorname{GL}(V)$ consists of the maps $x \mapsto Tx+b$ with $T$ invertible, and sits in the split exact sequence $1 \to V \to \operatorname{Aff}(V) \to \operatorname{GL}(V) \to 1$; it acts transitively, and the stabiliser of a point is a copy of $\operatorname{GL}(V)$.

Affine combinations $\sum\lambda_ia_i$ with $\sum\lambda_i=1$ are well defined independently of the origin and give barycentres when the weights are equal and the number of points is invertible; affinely independent points give barycentric coordinates, and an affine basis of $n+1$ points gives every point a unique coordinate vector summing to $1$. Affine subspaces $a+W$ have a well-defined direction, two subspaces with the same direction are equal or disjoint, and a nonempty intersection has direction $W \cap U$; in dimensions two and three this is the incidence theory of points, lines and planes. Affine maps are the maps with a linear part, and affine automorphisms form the affine group.

Finally, in a Euclidean affine space the distance-preserving bijections are exactly the affine maps with orthogonal linear part, by the Mazur–Ulam theorem, and they form the Euclidean group $E(\mathbb{A})=V \rtimes O(V,Q)$; every isometry is a translation composed with an isometry fixing a point, and in the plane the non-identity isometries are translations, rotations, reflections and glide reflections. For a form of arbitrary signature the analogous group is $V \rtimes O(V,Q)$, the algebraic structure being independent of the signature.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | a field |
| $V$ | direction vector space, $\dim_F V=n$ |
| $\mathbb{A}$ | affine space with direction $V$ |
| $a+v$, $b-a$ | action of $V$ on $\mathbb{A}$ and difference of points |
| $o$ | an origin; $\varphi_o(a)=a-o$ |
| $t_v$ | translation by $v$, $t_v(a)=a+v$ |
| $T(\mathbb{A}) \cong (V,+)$ | translation group |
| $\operatorname{Aff}(\mathbb{A})=\operatorname{Aff}(V)$ | affine group |
| $V \rtimes \operatorname{GL}(V)$ | semidirect product structure, $(T,b)(T',b')=(TT',Tb'+b)$ |
| $(T,b)$ | affine map $x \mapsto Tx+b$ |
| $\sum_i\lambda_ia_i$, $\sum_i\lambda_i=1$ | affine combination |
| $(\alpha_0,\dots,\alpha_n)$ | barycentric coordinates |
| $B=a+W$ | affine subspace with direction $W$ |
| $Q$, $g$ | quadratic form and its polar form |
| $O(V,Q)$ | orthogonal group of the form |
| $E(\mathbb{A})=V \rtimes O(V,Q)$ | Euclidean group / isometry group |
| $d(a,b)^2=Q(a-b)$ | squared distance |

## Further Reading

- Emil Artin, *Geometric Algebra* (Interscience, 1957), for affine geometry and the structure of the affine group.
- Marcel Berger, *Geometry I* (Springer, 1987), for affine spaces, barycentres and the classification of isometries.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for torsors and semidirect products.
- Harold S. M. Coxeter, *Introduction to Geometry* (Wiley, 2nd ed. 1969), for the classical affine and Euclidean geometry.
- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 3rd ed. 1971), for the groups $V \rtimes O(V,Q)$ and their classical geometry.
- Igor R. Shafarevich, *Basic Algebraic Geometry 1* (Springer, 3rd ed. 2013), for affine spaces over arbitrary fields and their coordinate rings.
- John Stillwell, *The Four Pillars of Geometry* (Springer, 2005), for the interplay between affine, projective and Euclidean structures.
